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

*(none — no **satellite** positions have been opened yet. Core VOO exists and is deliberately not tracked here, per the top-of-file rules and the fill note further down.)*

**Reconciliation 2026-09-08 09:35 ET (2-market-open-execution) — RECONCILED, NO ORDERS, NO §5
EVALUATION DUE, NOTHING TO BACKFILL:** selftest passed all five checks (`trading_enabled: true`,
LIVE paper account, equity $99,975.23). **`clock` at 09:35:47 ET returns `is_open: true`** —
the session is live and this was a real execution window, not a closed-market skip.
`alpaca.py positions` returns **one row, VOO core** (99.046311231 shares, avg_entry 706.74,
market_value $69,979.19, broker mark **706.53**, `lastday_price` 708.01, `change_today`
**−0.209%**, unrealized_pl **−$20.80, −0.03%**). `alpaca.py sleeves`: equity **$99,975.72**,
cash $30,000.00, core **70.00%**, satellite **0.0% (count 0)**, cash 30.01%,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +3.81`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** No
discrepancy, and no order was placed on top of a doubtful ledger. Compare **satellite to
satellite**, never raw ledger to raw broker.

**The staleness gate passed and there was still nothing to execute — two different things.**
`plan_date: 2026-09-08` equals today ET, so today's intents were fully executable; the plan
simply contained **none** (four theses researched pre-market, all four rejected). That is a
no-trade day under §4, **not** a stale-plan refusal: **no `stale-plan` alert was due and none
was posted.** Step 3 was skipped on `core_established: true` — the bootstrap path is closed
permanently. **Zero orders submitted this run, so nothing can be in a non-terminal state.**

**No REBALANCE.** Core sits at **70.00%** against a 65–75% band; `rebalance_delta` is **+$3.81**,
0.004% of equity and the closest to target the core has ever been. §2 rebalances at the **band
edge**, not to the exact target.

**No §5 rule was evaluated and none was due.** Zero satellite blocks means §5.1 has no
invalidation condition to test, §5.2 no deadline, §5.3/§5.4 no entry price or high-water mark.
**No `sell_rule_status` field was updated because none exists.**

**No high-water backfill was run and none was due.** There is still **no `highest_close` field
and no `(as of ...)` date anywhere** in this section, so the staleness trigger has nothing to key
on. **Absent is not stale — do not backfill from `bars`.** Core VOO was again deliberately not
given a mark: stamping one would fabricate a §5.4 trailing stop on a position §5 exempts.
**§5.4 remains NOT ARMED, not disabled** — it arms the day the first *satellite* position opens.

**⚠ The two-price trap, carried forward because the day it matters there will be a position.**
Use `bars --adjustment all` for any official close and a fresh `quote` for execution — never a
`positions` field for either. Seen in three shapes: intraday fades; the 09-04 close where the
official **707.86** sat *above* the broker mark **707.59** (a $26.75 gap on 99.046311231 shares,
the reverse of what an intraday fade suggests); and on the holiday a third number entirely
(`current_price` = `lastday_price` = 708.01 against Friday's official 707.86). Today's mark
**706.53** is likewise not a close and was written nowhere as one.

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-08 08:24) HAVE BEEN COLLAPSED,
DELIBERATELY.** Sixteen blocks spanning 09-01 to the 09-08 pre-market run each recorded the same
null result — zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no
§5 rule evaluated; no high-water mark to stamp; no backfill due. `state.md` flags this
accumulation as
actively harmful rather than untidy: this repo's only continuity mechanism is the next run
*reading* these files, and padding them with restatements of one null fact raises the odds that
a genuinely live item gets skimmed. Carry-forward is defined as **cleared once acted on**, and
each of those blocks was acted on by the run that read it. **The correct response to the pull to
append is to collapse, not to add another.** Nothing live was discarded — the load-bearing facts
those blocks carried are preserved here:

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional
  $70,000.00**, order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**,
  verified terminal before it was written. Audit record in `trade_log.md`.
- **Measure the core from the 706.74 fill, not from a prior VOO close.** The fill landed
  **+0.483% above the previous close**, and that one-time entry gap — not tracking error and
  never skill — is the whole of the core's reported divergence from VOO.
- **The core is not tracked in this ledger by design.** §5 exempts it from all four sell rules,
  so it has no thesis state, no timing window and no `highest_close`. **Every reconciliation
  compares satellite blocks to satellite Alpaca positions**; a run that compares the raw ledger
  to the raw broker will read a correct ledger as broken.
- **§5.4 has never been armed.** It arms on the first *satellite* fill. The 09-03 core fill was
  not that day, and no day since has been either.
- **All four §5 sell rules remain untested code paths.** Nothing has ever closed, so the string
  of "no exits" entries recorded the absence of a subject, not clean bills of health.
