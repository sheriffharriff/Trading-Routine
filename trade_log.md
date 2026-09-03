# Trade Log

**AGENT-OWNED. Newest first.**

Every order gets an entry, with the thesis ID it came from (§8). Only write an entry after
the order has been **polled to a terminal state** — §7 forbids orders you cannot verify
filled, and an entry written at submission time records an intention, not a trade.

Rejected and canceled orders get entries too. An order the broker refused is something the
next run needs to know about.

**Monthly rollover:** the Friday review archives prior months into
`archive/trade_log/YYYY-MM.md`.

---

## Template

```
### YYYY-MM-DD HH:MM ET — BUY | SELL — <TICKER> — <filled | rejected | canceled>
- thesis_id:      T-YYYY-MM-DD-NN   (or "core" for the core sleeve)
- order_id:       <alpaca order id>
- qty:            0.000
- fill_price:     0.00
- notional:       0.00
- pct_of_account: 0.0%
- routine:        <which of the five runs placed it>

For buys (satellite):
- asset_type:     stock | etf
- market_cap:     $00.0B
- market_cap_src: <source — this is what makes the §3 floor auditable after the fact>

For sells:
- rule:           §5.1 invalidation | §5.2 time stop | §5.3 hard stop | §5.4 trailing stop | §2 rebalance
- evidence:       <the observable fact that triggered it>
- realized_pnl:   +/-0.00 (+/-0.0%)
- streak_effect:  consecutive_closed_losses N → M

- notes:          <anything odd: slippage, partial fill, retry>
```

The `market_cap_src` field matters more than it looks. The $10B floor is checked against a
figure the agent supplies from research, so the script can catch a missing or below-floor
number but cannot catch a wrong one. Recording where the number came from is what lets you
audit it later.

---

## Entries

### 2026-09-03 09:36 ET — BUY — VOO — filled
- thesis_id:      core
- order_id:       d177d8f0-cd0c-41bf-95c1-4772318265fd
- qty:            99.046311231
- fill_price:     706.74
- notional:       70000.00
- pct_of_account: 70.0% (at entry, against $100,000.00 pre-trade equity)
- routine:        2-market-open-execution
- asset_type:     etf
- market_cap:     n/a — VOO is the designated core sleeve ticker; §3 stock market-cap floor
                  does not apply and `alpaca.py buy --core` does not require it. ADV is well
                  above the §3 500k-shares ETF threshold (VOO trades in the millions daily).
- market_cap_src: n/a (core sleeve, ETF — §3 checks ADV, not market cap)
- notes:          **First real fill in this repo's history.** Bootstrapped the §2 core sleeve
                  from 0% to 70% in a single order — Step 3's bootstrap and Step 7's rebalance
                  are the same order on this account, so this fill satisfies both. Verified
                  terminal (`"status": "filled", "terminal": true`) before writing this entry.
                  Post-fill sleeves check: core 69.99%, cash 30.01%, `core_in_band: true`,
                  `rebalance_needed: false`, `rebalance_delta: 5.06` (residual from fractional
                  share rounding against a moving mark, well inside §2's 65–75% band). Live
                  equity was $100,000.00 at the open, so the plan's $70,000 notional was also
                  70% of live equity — no size-to-equity adjustment needed. Fill price 706.74
                  is +0.483% from VOO's 703.41 prior close, i.e. a normal open bar.

---

## Dry-run intents (NOT trades)

Recorded separately and deliberately kept out of `## Entries` above, which is reserved for
orders that actually reached a terminal state. A future reader looking for the missing VOO core
position should find the reason here rather than infer a broken run.

### 2026-09-02 — VOO core bootstrap — INTENT ONLY, NOT FILLED
- routine:        2-market-open-execution (09:36 ET)
- thesis_id:      core
- intended:       BUY VOO, notional $70,000.00 (70% of $100,000.00 live equity, §2 target)
- command:        `python scripts/alpaca.py buy --symbol VOO --notional 70000 --core`
- result:         `{"ok": true, "dry_run": true, "reason": "TRADING_ENABLED is not true in
                  control.md"}` — exit 0, **no order submitted, no fill, no position**
- reference:      VOO last trade 700.555 at 09:36:15 ET; bid/ask 700.15 / 700.71 (a live,
                  40x40, 56-cent regular-hours book — not the stale 679.52 / 721.61
                  after-hours spread the 08:30 pre-market run correctly refused to use);
                  prior close 700.14 (2026-09-01), i.e. about +0.06% on the session
- asset check:    `tradable: true`, `fractionable: true`, ARCA, us_equity, status active —
                  eligible, §3 clear
- sizing:         re-derived from live equity at the open per the plan's `revalidate` line,
                  not copied from the $70,000 written pre-market. Live equity was still
                  $100,000.00, so the two numbers coincide — the figure was re-derived, not
                  merely reused.
- effect:         none. `core_established` stays `false`; account remains 100% cash; the same
                  intent regenerates tomorrow until a human sets `TRADING_ENABLED: true`.
- **submitted once, not twice.** Step 3's bootstrap and Step 7's rebalance are the same
                  $70,000 VOO buy on this account (`core_established: false` **and** core 0.0%
                  against a 70% target are one condition with one remedy). Step 7 was
                  evaluated and deliberately not submitted as a second order.

### 2026-09-01 — VOO core bootstrap — INTENT ONLY, NOT FILLED
- routine:        2-market-open-execution (09:36 ET)
- thesis_id:      core
- intended:       BUY VOO, notional $70,000.00 (70% of $100,000.00 equity, §2 target)
- command:        `python scripts/alpaca.py buy --symbol VOO --notional 70000 --core`
- result:         `{"ok": true, "dry_run": true, "reason": "TRADING_ENABLED is not true in
                  control.md"}` — exit 0, **no order submitted, no fill, no position**
- reference:      VOO last trade 700.625 at 09:35:37 ET; bid/ask 700.04 / 700.67; prior close
                  704.875 (2026-08-31), i.e. about −0.6% on the session open
- asset check:    `tradable: true`, `fractionable: true`, ARCA, us_equity — eligible, §3 clear
- effect:         none. `core_established` stays `false`; account remains 100% cash; the same
                  intent regenerates tomorrow until a human sets `TRADING_ENABLED: true`.
