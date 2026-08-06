#!/usr/bin/env python3
"""Alpaca REST client for the trading routines. Paper endpoint only.

Usage:
  python scripts/alpaca.py clock
  python scripts/alpaca.py account
  python scripts/alpaca.py positions
  python scripts/alpaca.py sleeves
  python scripts/alpaca.py quote --symbols NVDA,VRT
  python scripts/alpaca.py bars --symbol VOO --days 30 [--adjustment all]
  python scripts/alpaca.py move --symbol VRT --sessions 5
  python scripts/alpaca.py asset --symbol VRT

  python scripts/alpaca.py buy --symbol VRT --notional 4000 \
      --thesis-id T-2026-08-05-01 --asset-type stock \
      --market-cap 47.2B --market-cap-source "Perplexity / company 10-Q"

  python scripts/alpaca.py buy --symbol VOO --notional 70000 --core
  python scripts/alpaca.py sell --symbol VRT --reason "5.3 hard stop -7.4% from entry"
  python scripts/alpaca.py orders [--status open]
  python scripts/alpaca.py order --id <order_id>

Every eligibility rule in strategy.md section 3, the position cap and circuit
breaker in section 6, and the verification requirement in section 7 are enforced
here. The routine prompts describe these rules; this file is what makes them true.
"""

import argparse
import re
import statistics
import sys
import time
from datetime import timedelta

import common as c

# Leveraged and inverse products. strategy.md section 3 bans them outright, and
# their names are not machine-readable in the Alpaca asset record, so this is a
# denylist plus a name-pattern net.
LEVERAGED_TICKERS = {
    "TQQQ", "SQQQ", "SOXL", "SOXS", "UPRO", "SPXU", "SPXL", "SPXS", "UDOW", "SDOW",
    "TNA", "TZA", "FAS", "FAZ", "LABU", "LABD", "NUGT", "DUST", "JNUG", "JDST",
    "YINN", "YANG", "ERX", "ERY", "QLD", "SSO", "SDS", "QID", "PSQ", "SH", "DOG",
    "TWM", "UWM", "MVV", "MZZ", "DXD", "DDM", "UVXY", "SVXY", "VIXY", "VXX", "UVIX",
    "SVIX", "TMF", "TMV", "TYD", "TYO", "BOIL", "KOLD", "UCO", "SCO", "AGQ", "ZSL",
    "UGL", "GLL", "NVDL", "NVDU", "NVD", "TSLL", "TSLQ", "TSLS", "AAPU", "AAPD",
    "MSFU", "MSFD", "GGLL", "GGLS", "AMZU", "AMZD", "METU", "METD", "CONL", "MSTU",
    "MSTX", "MSTZ", "AMDL", "AMUU", "PLTU", "SMCL", "FNGU", "FNGD", "BULZ", "WEBL",
    "WEBS", "HIBL", "HIBS", "DFEN", "DRN", "DRV", "CURE", "RETL", "PILL", "TECL",
    "TECS", "UTSL", "NAIL", "MIDU", "EDC", "EDZ", "KORU", "MEXX", "BRZU", "INDL",
}

# Crypto-tracking products. Also banned by section 3, and unlike actual crypto
# these carry class "us_equity" in the asset record -- the class check alone
# would let them straight through.
CRYPTO_TRACKING = {
    "BITO", "BITX", "BITI", "BTF", "GBTC", "BTC", "IBIT", "FBTC", "ARKB", "BITB",
    "HODL", "BRRR", "EZBC", "BTCO", "BTCW", "DEFI", "ETHE", "ETHA", "ETHW", "ETHV",
    "FETH", "EZET", "CETH", "QETH", "ETHU", "ETHD", "MAXI", "BLOK", "BKCH", "DAPP",
    "WGMI", "SATO", "BITQ", "LEGR", "CRPT",
}

# Deliberately wide. A false positive refuses a legitimate trade; a false
# negative buys a 3x fund. Those costs are not symmetric.
LEVERAGE_NAME_PATTERN = re.compile(
    r"(\b[-+]?[1-9](?:\.5)?x\b|\bultra\b|\bultrashort\b|\bultrapro\b|\bbull\b|\bbear\b"
    r"|\binverse\b|\bleveraged\b|\bgeared\b|\bdaily\s+\w*\s*[1-9]x\b|\bshort\b|\b2x\b|\b3x\b)",
    re.IGNORECASE,
)

CRYPTO_NAME_PATTERN = re.compile(
    r"(\bbitcoin\b|\bethereum\b|\bcrypto\b|\bblockchain\b|\bdigital\s+asset\b|\bsolana\b|\bxrp\b)",
    re.IGNORECASE,
)


# --------------------------------------------------------------------------
# Reads
# --------------------------------------------------------------------------

def get_clock():
    status, payload = c.alpaca("GET", "/v2/clock")
    if not c.ok(status):
        c.fail("could not read market clock", status=status, response=payload)
    return payload


def get_account():
    status, payload = c.alpaca("GET", "/v2/account")
    if not c.ok(status):
        c.fail("could not read account", status=status, response=payload)
    return payload


def get_positions():
    status, payload = c.alpaca("GET", "/v2/positions")
    if not c.ok(status):
        c.fail("could not read positions", status=status, response=payload)
    return payload


def get_asset(symbol):
    status, payload = c.alpaca("GET", f"/v2/assets/{symbol}")
    if not c.ok(status):
        c.fail(f"could not read asset record for {symbol}", status=status, response=payload)
    return payload


def get_bars(symbol, days, adjustment="all", feed="iex"):
    """Daily bars. adjustment=all keeps dividends and splits in, which is what
    makes a VOO series a total-return series rather than a price series."""
    start = (c.et_today() - timedelta(days=int(days) * 2 + 10)).isoformat()
    status, payload = c.alpaca_data(
        "GET", f"/v2/stocks/{symbol}/bars",
        params={"timeframe": "1Day", "start": start, "limit": 10000,
                "adjustment": adjustment, "feed": feed},
    )
    if not c.ok(status):
        c.fail(f"could not read bars for {symbol}", status=status, response=payload)
    bars = (payload or {}).get("bars") or []
    return bars[-int(days):] if days else bars


def get_snapshots(symbols, feed="iex"):
    status, payload = c.alpaca_data(
        "GET", "/v2/stocks/snapshots",
        params={"symbols": ",".join(symbols), "feed": feed},
    )
    if not c.ok(status):
        c.fail("could not read snapshots", status=status, response=payload)
    return payload


def sleeves():
    """Core / satellite / cash split. strategy.md section 2 -- every run reports drift."""
    account = get_account()
    positions = get_positions()
    equity = c.money(account.get("equity") or account.get("portfolio_value"))
    core_value = sum(c.money(p.get("market_value")) for p in positions
                     if p.get("symbol") == c.CORE_TICKER)
    satellite_value = sum(c.money(p.get("market_value")) for p in positions
                          if p.get("symbol") != c.CORE_TICKER)
    cash = c.money(account.get("cash"))
    core_pct = c.pct(core_value, equity)
    low, high = c.CORE_BAND
    return {
        "equity": equity,
        "cash": cash,
        "core": {"ticker": c.CORE_TICKER, "value": core_value, "pct": core_pct},
        "satellite": {"value": satellite_value, "pct": c.pct(satellite_value, equity),
                      "count": len([p for p in positions if p.get("symbol") != c.CORE_TICKER])},
        "cash_pct": c.pct(cash, equity),
        "core_in_band": low * 100 <= core_pct <= high * 100,
        "rebalance_needed": not (low * 100 <= core_pct <= high * 100),
        "core_target_value": round(equity * c.CORE_TARGET, 2),
        "rebalance_delta": round(equity * c.CORE_TARGET - core_value, 2),
    }


def session_move(symbol, sessions=None):
    """Percent move over the last N sessions -- the section 4 priced-in filter.

    Mechanical rather than eyeballed: >4% over five sessions on the news means
    you are late, and that judgment should not depend on how a chart looks.
    """
    sessions = int(sessions or c.PRICED_IN_LOOKBACK)
    bars = get_bars(symbol, sessions + 1, adjustment="all")
    if len(bars) < 2:
        c.fail(f"not enough bar history for {symbol} to run the priced-in check",
               bars_returned=len(bars))
    first, last = c.money(bars[0].get("c")), c.money(bars[-1].get("c"))
    move = c.pct(last - first, first)
    return {
        "symbol": symbol, "sessions": len(bars) - 1,
        "from_close": first, "to_close": last, "move_pct": move,
        "threshold_pct": c.PRICED_IN_MOVE_PCT,
        "priced_in": abs(move) > c.PRICED_IN_MOVE_PCT,
        "verdict": ("LATE - skip per strategy.md section 4"
                    if abs(move) > c.PRICED_IN_MOVE_PCT else "passes the priced-in check"),
    }


def average_volume(symbol, sessions=20):
    bars = get_bars(symbol, sessions, adjustment="all")
    volumes = [c.money(b.get("v")) for b in bars if b.get("v")]
    return statistics.mean(volumes) if volumes else 0.0


# --------------------------------------------------------------------------
# Eligibility -- strategy.md section 3
# --------------------------------------------------------------------------

def check_universe(symbol, asset_type=None, market_cap=None):
    """Raise via c.fail unless the symbol is eligible. Returns the asset record."""
    symbol = symbol.upper()
    asset = get_asset(symbol)
    name = str(asset.get("name") or "")

    if symbol in LEVERAGED_TICKERS or LEVERAGE_NAME_PATTERN.search(name):
        c.fail(f"{symbol} looks like a leveraged or inverse product -- banned by "
               f"strategy.md section 3",
               asset_name=name,
               note="this check errs toward false positives on purpose; if this is a "
                    "genuine rejection of an eligible name, the universe rule still says no "
                    "to anything with leverage in its mandate")

    if symbol in CRYPTO_TRACKING or CRYPTO_NAME_PATTERN.search(name):
        c.fail(f"{symbol} is a crypto or crypto-tracking product -- banned by "
               f"strategy.md section 3", asset_name=name)

    if str(asset.get("class") or asset.get("asset_class")) != "us_equity":
        c.fail(f"{symbol} is not US equity (class={asset.get('class')}) -- section 3 allows "
               f"only US-listed common stock and ETFs", asset=asset)

    if str(asset.get("status")) != "active" or not asset.get("tradable"):
        c.fail(f"{symbol} is not active and tradable at Alpaca",
               status_field=asset.get("status"), tradable=asset.get("tradable"))

    if asset_type == "stock":
        cap = c.parse_amount(market_cap)
        if cap is None:
            c.fail("--market-cap is required for a stock and could not be parsed",
                   received=market_cap,
                   hint="accepts forms like 47.2B, $47.2B, 47200000000")
        if cap < c.MARKET_CAP_FLOOR:
            c.fail(f"{symbol} market cap {cap:,.0f} is below the "
                   f"{c.MARKET_CAP_FLOOR:,.0f} floor in strategy.md section 3",
                   market_cap=cap, floor=c.MARKET_CAP_FLOOR)

    if asset_type == "etf":
        adv = average_volume(symbol)
        if adv < c.ETF_MIN_ADV:
            c.fail(f"{symbol} average daily volume {adv:,.0f} is below the "
                   f"{c.ETF_MIN_ADV:,.0f} floor for ETFs in strategy.md section 3",
                   adv=adv, floor=c.ETF_MIN_ADV)

    return asset


# --------------------------------------------------------------------------
# Orders
# --------------------------------------------------------------------------

def poll_order(order_id, timeout=150, interval=3):
    """Poll until the order reaches a terminal state.

    strategy.md section 7 forbids placing orders you cannot verify filled, so
    nothing downstream is allowed to treat a submission as a trade. If this
    times out the caller gets ok=false and the order is reported as unresolved
    rather than assumed good.
    """
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        status, payload = c.alpaca("GET", f"/v2/orders/{order_id}")
        if not c.ok(status):
            c.fail("could not poll order status", order_id=order_id, response=payload)
        last = payload
        if str(payload.get("status", "")).lower() in c.ORDER_TERMINAL_STATES:
            return payload, True
        time.sleep(interval)
    return last, False


def submit(symbol, side, notional=None, qty=None):
    body = {"symbol": symbol, "side": side, "type": "market", "time_in_force": "day"}
    if notional is not None:
        body["notional"] = str(round(float(notional), 2))
    if qty is not None:
        body["qty"] = str(qty)
    status, payload = c.alpaca("POST", "/v2/orders", body=body)
    if not c.ok(status):
        c.fail(f"{side} order for {symbol} was rejected at submission",
               status=status, response=payload, request=body)
    return payload


def finish(order, symbol, side, extra):
    order, terminal = poll_order(order.get("id"))
    state = str(order.get("status", "unknown")).lower()
    result = {
        "ok": terminal and state == "filled",
        "symbol": symbol,
        "side": side,
        "order_id": order.get("id"),
        "status": state,
        "terminal": terminal,
        "filled_qty": order.get("filled_qty"),
        "filled_avg_price": order.get("filled_avg_price"),
        "submitted_at": order.get("submitted_at"),
        "filled_at": order.get("filled_at"),
        "et_time": c.et_stamp(),
    }
    result.update(extra)
    if not terminal:
        result["warning"] = ("order did not reach a terminal state within the poll window; "
                             "do NOT log this as a trade -- re-check with "
                             f"`alpaca.py order --id {order.get('id')}` before writing "
                             "anything to trade_log.md")
    return result


def cmd_buy(args):
    symbol = args.symbol.upper()
    control = c.read_control()
    state = c.read_state()

    if args.core:
        # The core path exists so the section 2 bootstrap and rebalance can run at
        # all: they have no thesis and are deliberately larger than the 5% cap.
        # Restricting it to the designated core ticker is what stops the bypass
        # from being borrowed for a satellite trade.
        if symbol != c.CORE_TICKER:
            c.fail(f"--core is only valid for the designated core ticker "
                   f"({c.CORE_TICKER}); refusing to apply the core exemptions to {symbol}",
                   hint="satellite buys require --thesis-id and --asset-type and are "
                        "capped at 5% of account value")
        check_universe(symbol)
        thesis_id = "core"
        extra = {"sleeve": "core", "thesis_id": "core"}
    else:
        if not args.thesis_id:
            c.fail("--thesis-id is required for a satellite buy",
                   hint="strategy.md section 7: no position without a four-part thesis "
                        "written to research_log.md")
        if not c.thesis_exists(args.thesis_id):
            c.fail(f"thesis {args.thesis_id} does not appear in research_log.md",
                   hint="write the four-part thesis first; the log is the record that "
                        "makes the trade legitimate, not paperwork after the fact")
        if args.asset_type not in ("stock", "etf"):
            c.fail("--asset-type must be 'stock' or 'etf'",
                   hint="strategy.md section 3 sets a market-cap floor for stocks and a "
                        "volume floor for ETFs; the applicable test cannot be inferred")
        if args.asset_type == "stock" and not args.market_cap_source:
            c.fail("--market-cap-source is required for a stock",
                   hint="the cap figure comes from your own research, so recording where "
                        "it came from is the only thing that makes it auditable later")

        halted, why = c.halt_active(state, control)
        if halted:
            c.fail("circuit breaker is active -- no new positions", detail=why,
                   hint="strategy.md section 6: manage existing positions, keep researching "
                        "and journaling, flag the halt in the ClickUp summary")

        check_universe(symbol, args.asset_type, args.market_cap)

        equity = c.money(get_account().get("equity"))
        cap = equity * c.MAX_SATELLITE_PCT
        if float(args.notional) > cap + 0.01:
            c.fail(f"notional {float(args.notional):,.2f} exceeds the "
                   f"{c.MAX_SATELLITE_PCT:.0%} single-position cap ({cap:,.2f}) in "
                   f"strategy.md section 6", equity=equity, max_notional=round(cap, 2))

        weekly = int(c.parse_amount(state.get("new_positions_this_week", "0")) or 0)
        if weekly >= c.MAX_NEW_POSITIONS_PER_WEEK:
            c.fail(f"already opened {weekly} positions this week; section 6 caps it at "
                   f"{c.MAX_NEW_POSITIONS_PER_WEEK}", hint="slow down")

        thesis_id = args.thesis_id
        extra = {
            "sleeve": "satellite",
            "thesis_id": thesis_id,
            "asset_type": args.asset_type,
            "market_cap": args.market_cap,
            "market_cap_source": args.market_cap_source,
        }

    if not control["trading_enabled"]:
        c.emit({"ok": True, "dry_run": True, "action": "buy", "symbol": symbol,
                "notional": float(args.notional), "reason": control["reason"],
                "note": "TRADING_ENABLED is not true in control.md; no order was submitted",
                **extra})

    order = submit(symbol, "buy", notional=float(args.notional))
    c.emit(finish(order, symbol, "buy", {"notional": float(args.notional), **extra}))


def cmd_sell(args):
    symbol = args.symbol.upper()
    control = c.read_control()

    if not args.reason:
        c.fail("--reason is required on every exit",
               hint="name the rule: section 5.1 invalidation, 5.2 time stop, 5.3 hard stop, "
                    "5.4 trailing stop, or section 2 rebalance")

    if symbol == c.CORE_TICKER and not args.core:
        c.fail(f"{symbol} is the core holding; pass --core to sell any of it",
               hint="strategy.md section 5 exempts core from all sell rules and section 7 "
                    "forbids selling core to fund a satellite trade. The only legitimate "
                    "core sale is a section 2 rebalance from above the band.")

    if not control["trading_enabled"]:
        c.emit({"ok": True, "dry_run": True, "action": "sell", "symbol": symbol,
                "qty": args.qty or "all", "rule": args.reason, "reason": control["reason"],
                "note": "TRADING_ENABLED is not true in control.md; no order was submitted"})

    params = {}
    if args.qty:
        params["qty"] = str(args.qty)
    status, payload = c.alpaca("DELETE", f"/v2/positions/{symbol}", params=params or None)
    if not c.ok(status):
        c.fail(f"could not close position in {symbol}", status=status, response=payload)

    c.emit(finish(payload, symbol, "sell",
                  {"rule": args.reason, "qty_requested": args.qty or "all"}))


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("clock")
    sub.add_parser("account")
    sub.add_parser("positions")
    sub.add_parser("sleeves")

    p = sub.add_parser("quote"); p.add_argument("--symbols", required=True)
    p = sub.add_parser("bars")
    p.add_argument("--symbol", required=True)
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--adjustment", default="all")
    p = sub.add_parser("move")
    p.add_argument("--symbol", required=True)
    p.add_argument("--sessions", type=int, default=c.PRICED_IN_LOOKBACK)
    p = sub.add_parser("asset"); p.add_argument("--symbol", required=True)

    p = sub.add_parser("buy")
    p.add_argument("--symbol", required=True)
    p.add_argument("--notional", required=True)
    p.add_argument("--thesis-id")
    p.add_argument("--asset-type", choices=["stock", "etf"])
    p.add_argument("--market-cap")
    p.add_argument("--market-cap-source")
    p.add_argument("--core", action="store_true",
                   help=f"core sleeve buy; only valid for {c.CORE_TICKER}")

    p = sub.add_parser("sell")
    p.add_argument("--symbol", required=True)
    p.add_argument("--reason", required=True)
    p.add_argument("--qty")
    p.add_argument("--core", action="store_true", help="required to sell any of the core")

    p = sub.add_parser("orders"); p.add_argument("--status", default="all")
    p = sub.add_parser("order"); p.add_argument("--id", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == "clock":
            c.emit(get_clock())
        elif args.cmd == "account":
            c.emit(get_account())
        elif args.cmd == "positions":
            c.emit(get_positions())
        elif args.cmd == "sleeves":
            c.emit(sleeves())
        elif args.cmd == "quote":
            c.emit(get_snapshots([s.strip().upper() for s in args.symbols.split(",") if s.strip()]))
        elif args.cmd == "bars":
            c.emit({"symbol": args.symbol.upper(),
                    "bars": get_bars(args.symbol.upper(), args.days, args.adjustment)})
        elif args.cmd == "move":
            c.emit(session_move(args.symbol.upper(), args.sessions))
        elif args.cmd == "asset":
            c.emit(get_asset(args.symbol.upper()))
        elif args.cmd == "buy":
            cmd_buy(args)
        elif args.cmd == "sell":
            cmd_sell(args)
        elif args.cmd == "orders":
            status, payload = c.alpaca("GET", "/v2/orders",
                                       params={"status": args.status, "limit": 100})
            c.emit(payload if c.ok(status) else c.fail("could not list orders",
                                                       response=payload))
        elif args.cmd == "order":
            status, payload = c.alpaca("GET", f"/v2/orders/{args.id}")
            c.emit(payload if c.ok(status) else c.fail("could not read order",
                                                       response=payload))
    except c.ApiError as exc:
        c.fail(str(exc))


if __name__ == "__main__":
    main()
