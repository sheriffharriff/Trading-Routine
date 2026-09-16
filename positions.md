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

**Reconciliation 2026-09-16 12:35 ET (3-midday-management) — LEDGER AGREES WITH THE BROKER;
NO SATELLITE SUBJECT EXISTS, EIGHTEENTH CONSECUTIVE SESSION. ZERO EXITS AND NONE WAS DUE.**
*(This block **replaces** the 09-16 09:35 market-open reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — twenty-sixth consecutive
run.**)*
Selftest passed all five checks at **12:35 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,169.04).

**⚠ THIS RUN MAY NOT OPEN A POSITION, AND THE 30.25% IDLE CASH IT SEES IS NOT AN OPPORTUNITY.**
Routine 3 is **exits only**. A midday entry would route around the pre-market research funnel and
the 09:35 execution run, which is the path that forces every buy to sleep on a written thesis.
**Nothing here was blocked by a guardrail — the run is scoped so the question never arises.**

**`clock` READ `is_open: TRUE` AT 12:35:11 — the in-session shape, mid-session this time.**
`next_close` **2026-09-16T16:00 — today**; `next_open` **2026-09-17T09:30 — tomorrow**. Today has
now supplied the pre-market read (08:17, `false`/next_open today), the opening-bell read (09:35,
`true`), this mid-session read (12:35, `true`) and will supply the post-bell read (16:16, `false`/
next_open tomorrow). **Two of those four share one boolean and differ only in the `next_open`
DATE.** Read the date, not the boolean.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares, avg_entry 706.74, market_value $69,174.93, cost_basis $69,999.99,
broker `current_price` **698.41**, `lastday_price` 696.20, unrealized_pl **−$825.06 / −1.179%**,
`change_today` +0.317%). **`current_price` 698.41 is a LIVE INTRADAY QUOTE MIDPOINT, not a close** —
yesterday's official close was **696.29**, and the same field read 698.88 pre-market and 698.08 at
the bell. **Three reads of one field on one day, three numbers. Never mix the two sources in one
comparison.** `alpaca.py sleeves`: equity **$99,169.04**, cash **$30,000.00**, core **69.75%**,
satellite **0.0% (count 0)**, cash **30.25%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: +247.52` = **0.25% of equity**. **NO REBALANCE IS DUE, and this routine could not
execute one in any case** — §2 rebalances at the **band edge (65/75)** and at the **market-open**
run. **Nineteenth consecutive run inside a 0.29-point range (69.69–69.98).**

**STEP 2 HIGH-WATER REPAIR — NO BACKFILL WAS DUE, AND THAT IS A READING, NOT AN ASSUMPTION.**
The backfill trigger is a `highest_close` whose `(as of ...)` date lags the last trading day. **There
is no `highest_close` field in this file at all**, because there is no satellite block to carry one.
**ABSENT is a third state, distinct from "current and unchanged" and from "stale" — and it is the
only one carrying no date.** The missing date is exactly what discharges Step 2: a stale mark
silently disables §5.4, an absent mark means §5.4 **has never been armed**. **Zero `alpaca.py bars`
calls were issued and none was due.** **Core VOO is deliberately NOT stamped**; writing a close into
this file for core would fabricate a §5.4 trailing stop on the one position §5 exempts from all four
sell rules, and it would look like tidiness while doing it.

**STEP 3 §5.1–§5.4 HAD NO SUBJECT — eighteenth consecutive session, and it is not a clean bill of
health.** No thesis to test for invalidation (§5.1) and **zero Perplexity invalidation queries were
issued — an absent check, not a skipped one**; no `timing_window` to expire (§5.2); no `entry_price`
to measure −7% against (§5.3); no `highest_close` to measure −10% against (§5.4). **Nothing was near
triggering because nothing exists to trigger.** `sell_rule_status` is **absent rather than blank**,
and there is no "closest to a stop" line to write because there is no distribution to take a minimum
over. **All four remain untested code paths.** **STEP 4 executed zero sells; no order id, no
`terminal: false` to re-check, no dry-run intent to flag.** **The most important line this run can
produce — a stop that should have fired and did not — DOES NOT EXIST TODAY, and that is because
there is no position, not because every stop was checked and passed.**

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-16
(Wednesday) is **2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday
2026-09-21. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`; `consecutive_closed_losses`
stays at **0** because nothing has ever closed in this account, so the §6 streak cannot move, no
`HALT_CLEARED_AT` comparison was required and **no circuit-breaker alert was due.** **Sleeve drift:**
core **69.75%**, inside the 65–75% band. `open_thesis_ids` stays **none** — nothing to remove.

**⚠ THE FOMC DECIDES AT 14:00 ET TODAY, ~85 MINUTES AFTER THIS RUN, AT >90% ODDS OF A 25bp HIKE.**
**It changes nothing here and there is no action at any number.** There is no satellite thesis for it
to invalidate, and **core is exempt from all four §5 sell rules**, so a hard move in the core mark
carries no exit. **The 16:15 close run is the first routine that sees the aftermath, and its job
there is to journal a price move, not to find a thesis in it.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-15 12:35) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-one blocks spanning 09-01 to today's midday run each recorded the same
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
- **The two-price defect is SOLVED and it is a live quote midpoint, not an offset** — which is why
  the broker/official gap (6.5c, 59.85c, 4c on successive days) never had a stable size and never
  will. A `current_price` of 700.57 against a `lastday_price` of 702.56 is an **intraday midpoint,
  not a close.** Always `bars --adjustment all` for a close, a fresh `quote` for execution, **never
  a `positions` field for either.** Cosmetic on core; **load-bearing the moment a satellite
  position exists**, because a `highest_close` read from a `positions` field records an after-hours
  midpoint and silently moves the §5.4 stop.
- **The 09-11 Alpaca data-plane outage is resolved** (every endpoint 200 at the 09-11 close, probed
  by hand), **but `selftest.py` still does not probe `clock` or market data** — a green pre-flight
  certifies nothing about the data plane. Probe by hand before relying on a price.
