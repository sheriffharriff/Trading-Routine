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

**High-water mark update 2026-09-01 16:16 ET (4-market-close-journal — the first close run in
this repo's history):** selftest passed all five checks. Market **was open today and has since
closed** (`clock`: `is_open: false` at 16:16:22 ET, `next_open: 2026-09-02 09:30 ET`) — this is
a normal post-close run, **not a holiday skip**. `alpaca.py positions` returned `[]`;
`alpaca.py sleeves` reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0%
(count 0), cash 100.0%, `core_in_band: false`, `rebalance_delta: 70000.0` — identical to the
09:36 and 12:35 reads. This ledger is empty and **agrees with the broker.** No discrepancy.

**Step 2 recorded no closes, and there were none to record.** The close routine's core job is to
write today's official close into every open satellite position's `highest_close` and to refresh
the `(as of ...)` date whether or not the value moved. There is no position block in this file,
so there is no `highest_close` to compare against and no date to stamp. **A future run must read
this as "current and empty", not as "the close run skipped its high-water pass"** — those two
states are exactly what the `(as of ...)` date exists to distinguish, and with zero positions the
distinction has no subject. **Do not backfill from `bars` tomorrow. There is nothing to backfill.**
The §5.4 trailing stop is not silently disabled; it is not yet armed, and it arms on the day the
first satellite position opens.

For reference only, and deliberately **not** recorded as a high-water mark anywhere: VOO closed
**700.14** on 2026-09-01 (`bars --days 2 --adjustment all`) against 704.875 on 2026-08-31,
−0.67%. The core sleeve is not tracked in this file by design (§5 exempts it), so this figure is
context for the journal, not ledger state.

---

**Reconciliation 2026-09-01 12:35 ET (3-midday-management — the first midday run in this repo's
history):** selftest passed all five checks. Market confirmed open (`is_open: true`, timestamp
12:35:21 ET, next close 16:00 ET). `alpaca.py positions` returned `[]`; `alpaca.py sleeves`
reports equity $100,000.00, cash $100,000.00, core 0.0%, satellite 0.0% (count 0), cash 100.0%,
`core_in_band: false`, `rebalance_delta: 70000.0` — unchanged from the 09:36 ET open run. This
ledger is empty and **agrees with the broker.** No discrepancy.

**Nothing to manage, and nothing was done.** Routine 3 is exits-only and may not open a position;
with zero open satellite positions there was nothing to evaluate. §5.1 (no invalidation condition
exists to test), §5.2 (no timing window to expire), §5.3 and §5.4 (no entry price and no
high-water mark to measure against) all had empty input. No Perplexity invalidation queries were
run, because there is no `invalidation` line in this file to check — running news queries with no
position to defend would be manufacturing activity, which §4's honest-broker rule forbids.

**Step 2 high-water repair: nothing to repair.** The `highest_close` staleness check has no
subject — no position block exists, so no `(as of ...)` date can be stale and no `bars` backfill
was needed. This is materially different from a backfill that was skipped: the trailing stop is
not silently disabled, it is simply not yet armed. It becomes live the day the first satellite
position is opened, which under `TRADING_ENABLED: false` cannot be today.

**Read this next to the 09:36 note, not as new information.** The two runs saw an identical
account three hours apart. The absence of a VOO core position is the dry-run intent recorded in
`trade_log.md`, not a failed fill.

---

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
