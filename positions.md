# Open Positions Ledger

**AGENT-OWNED.** One block per open **satellite** position. The core holding is not
tracked here — it is never sold on news (§5) and needs no thesis state.

Alpaca is authoritative for what is held and at what cost. This file exists for the
things Alpaca does not store and that §5 cannot be enforced without:

- the **highest close since entry**, without which the §5.4 trailing stop does not exist
- the **timing window deadline**, without which the §5.2 time stop never fires
- the **invalidation condition**, verbatim, because §7 forbids softening it later —
  keeping it written down is what makes softening visible

**High-water maintenance:** the market-close routine writes every open position's official
close into `highest_close` each day (only if it is higher). If a close run was skipped, the
next run must backfill from `python scripts/alpaca.py bars --symbol X --days N` before
evaluating §5.4. A gap in this field silently disables the trailing stop, which is the kind
of failure that looks like nothing is wrong.

---

## Template

```
### <TICKER> — <thesis-id>

- entry_date:            YYYY-MM-DD
- entry_price:           0.00
- qty:                   0.000
- notional_at_entry:     0.00
- pct_of_account_entry:  0.0%
- voo_close_at_entry:    0.00  (adjustment=all — the same-period baseline for this position)
- asset_type:            stock | etf
- market_cap_at_entry:   $00.0B
- market_cap_source:     <where the figure came from>
- highest_close:         0.00  (as of YYYY-MM-DD)
- timing_window:         <next earnings | Q_ YYYY>  → deadline YYYY-MM-DD
- invalidation:          <verbatim from the thesis, part 4 — never reworded>
- sell_rule_status:      <which of §5.1–5.4 are near triggering, and the distance to each>
- driver:                <the underlying catalyst, for the §4 correlation check>
```

The `driver` line is what makes the correlation check possible. Before opening anything new,
the pre-market routine reads every `driver` here and rejects a candidate exposed to the same
one — otherwise you are making a single bet spread across several tickers and mistaking it
for diversification.

`voo_close_at_entry` is recorded once, at entry, and never updated. The Friday review needs
each position measured against what the same capital would have done in VOO over that
position's own holding window; capturing the baseline at entry means the review never has to
re-derive it from price history, and it stays correct for positions closed months later.

---

## Open positions

*(none — no positions have been opened yet)*

**Reconciliation 2026-09-01 09:36 ET (2-market-open-execution — the first open run in this repo's
history):** checked against live Alpaca from inside regular trading hours (`clock`: `is_open:
true`, timestamp 09:35:59 ET). `alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports
equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_delta: 70000.0`. This ledger is empty and **agrees with the
broker.** No discrepancy, so no reconciliation was required before placing orders.

**Nothing was opened or closed.** The plan carried no BUY and no SELL intents — all six of
today's theses were rejected pre-market — so §5.1–5.4 had nothing to evaluate and no new block
was written. The §2 core bootstrap was attempted and returned `"dry_run": true`
(`TRADING_ENABLED: false`); it would not have produced a block here in any case, since the core
holding is deliberately not tracked in this file.

The high-water backfill warning at the top of this file is **not** in play — there is no
`highest_close` gap to backfill, because there is no position. It goes live the day the first
satellite position is opened, which under `TRADING_ENABLED: false` cannot be today.

---

**Reconciliation 2026-09-01 08:56 ET (1-premarket-research, third run of the day):** re-checked
against live Alpaca from inside the pre-market session. `alpaca.py positions` returned `[]`;
`alpaca.py sleeves` reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0%
(count 0), cash 100.0% — unchanged from both earlier runs today. This ledger is empty and
**agrees with the broker.** No discrepancy.

No §5 evaluation was possible or required: with no open positions there is no invalidation to
test (5.1), no timing window to expire (5.2), and no entry or high-water mark to measure a stop
against (5.3, 5.4). No `sell_rule_status` fields exist to update.

The high-water backfill warning at the top of this file is **not** in play — there is no
`highest_close` gap to backfill, because there is no position. It becomes live the day the first
satellite position is opened, which under `TRADING_ENABLED: false` is not today.

---

**Reconciliation 2026-09-01 01:15 ET (1-premarket-research, second run of the day):** re-checked
against live Alpaca. `alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports equity
$100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0% — identical to
the 00:48 ET run. This ledger is empty and **agrees with the broker.** No discrepancy.

No §5 evaluation was possible or required: with no open positions there is no invalidation to
test (5.1), no timing window to expire (5.2), and no entry or high-water mark to measure a stop
against (5.3, 5.4). No `sell_rule_status` fields exist to update.

The high-water backfill warning at the top of this file is **not** in play — there is no
`highest_close` gap to backfill, because there is no position. It becomes live the day the
first satellite position is opened.

---

**Reconciliation 2026-09-01 00:48 ET (1-premarket-research, first run of the day):** checked against live Alpaca.
`alpaca.py positions` returned `[]`; `alpaca.py sleeves` reports equity $100,000.00, cash
$100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%. This ledger is also empty.
**They agree — no discrepancy.** No §5 evaluation was possible or required: with no open
positions there is no invalidation to test (5.1), no timing window to expire (5.2), and no
entry or high-water mark to measure a stop against (5.3, 5.4). No `sell_rule_status` fields
to update.

The core sleeve is not tracked in this file by design (§5 exempts it), so the fact that core
is 0% is a `plan_today.md` / `state.md` matter, not a gap here.
