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

**Reconciliation 2026-09-16 16:16 ET (4-market-close-journal) — LEDGER AGREES WITH THE BROKER;
NO SATELLITE SUBJECT EXISTS, EIGHTEENTH CONSECUTIVE SESSION. NO HIGH-WATER MARK WAS WRITTEN AND
NONE WAS DUE.**
*(This block **replaces** the 09-16 12:35 midday reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — twenty-seventh consecutive
run.** Today had four runs to tempt four blocks; it has one.)*
Selftest passed all five checks at **16:16 ET** (`trading_enabled: true`, LIVE paper account, equity
$98,658.80).

**⚠ THIS RUN TRADES NOTHING AT ALL, AND THE 30.41% IDLE CASH IT SEES IS NOT AN OPPORTUNITY.**
Routine 4 places no orders of any kind — it records closes and journals. **Nothing here was blocked
by a guardrail; the run is scoped so the question never arises.**

**`clock` READ `is_open: false` AT 16:16:10 WITH `next_open` 2026-09-17T09:30 — TOMORROW. That is
the POST-BELL shape, not a holiday.** Today supplied all four: pre-market (08:17, `false`/next_open
**today**), opening bell (09:35, `true`), mid-session (12:35, `true`) and this post-bell read
(`false`/next_open **tomorrow**). **Two of the four share one boolean and differ only in the
`next_open` DATE.** **Read the date, not the boolean** — the holiday branch of this routine triggers
on exactly the flag this run always sees, and the first real holiday will arrive without warning.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares, avg_entry 706.74, market_value $68,658.80, cost_basis $69,999.99,
broker `current_price` **693.199**, `lastday_price` 696.20, unrealized_pl **−$1,341.19 / −1.916%**,
`change_today` −0.431%). **`current_price` 693.199 is a LIVE QUOTE MIDPOINT, not a close** — today's
official close from `bars --adjustment all` is **693.215**, and the same field read 698.88
pre-market, 698.08 at the bell and 698.41 at midday. **Four reads of one field on one day, four
numbers. Never mix the two sources in one comparison.** `alpaca.py sleeves`: equity **$98,658.80**,
cash **$30,000.00**, core **69.59%**, satellite **0.0% (count 0)**, cash **30.41%**, `core_in_band:
true`, `rebalance_needed: false`, `rebalance_delta: +402.36` = **0.41% of equity**. **NO REBALANCE IS
DUE TOMORROW, and this routine could not execute one in any case** — §2 rebalances at the **band edge
(65/75)** and at the **market-open** run. **Twentieth consecutive run inside a 0.39-point range
(69.59–69.98)**, today's being the lowest of the twenty: a drifting core mark on an unchanged share
count, not a position being reduced.

**STEP 2 — THE CLOSES WERE NOT RECORDED BECAUSE THERE IS NOTHING TO RECORD THEM AGAINST, AND THAT IS
A READING, NOT AN ASSUMPTION.** Step 2 writes every open **satellite** position's official close into
`highest_close` and refreshes the `(as of ...)` date **whether or not the value moves**, so that
tomorrow's midday run can tell a *current* mark from a *stale* one. **There is no `highest_close`
field in this file at all**, because there is no satellite block to carry one.
**ABSENT is a third state, distinct from "current and unchanged" and from "stale" — and it is the
only one carrying no date.** The missing date is exactly what discharges both this step and
tomorrow's backfill check: a stale mark silently disables §5.4, an absent mark means §5.4 **has never
been armed**. **Zero `alpaca.py bars` calls were issued for a high-water purpose** — the VOO bars
this run pulled priced the book and stamped nothing. **Core VOO is deliberately NOT stamped, and
today it had an accomplice**: its 693.215 close was already sitting in this run's terminal output
with nothing to do. Writing it into this file would fabricate a §5.4 trailing stop on the one
position §5 exempts from all four sell rules, and **it would not feel like a violation — it would
feel like tidiness.** Refused again.

**§5.1–§5.4 HAD NO SUBJECT — eighteenth consecutive session, and it is not a clean bill of
health.** No thesis to test for invalidation (§5.1) and **zero Perplexity invalidation queries were
issued — an absent check, not a skipped one**; no `timing_window` to expire (§5.2); no `entry_price`
to measure −7% against (§5.3); no `highest_close` to measure −10% against (§5.4). **Nothing was near
triggering because nothing exists to trigger.** `sell_rule_status` is **absent rather than blank**,
and there is no "closest to a stop" line to write because there is no distribution to take a minimum
over. **All four remain untested code paths.** **This routine executed no orders of any kind — none
is permitted here.** **The most important line this run can produce — a stop that should have fired
and did not — DOES NOT EXIST TODAY, and that is because there is no position, not because every stop
was checked and passed.**

**UNRESOLVED ORDERS — CHECKED, NONE.** `alpaca.py orders --status all` returns **one row for the
account's entire history**: the 09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`,
`status: filled`, `filled_at` 2026-09-03T13:36:21Z, terminal. **No order from today exists to sit in
limbo overnight**, and no `"terminal": false` case has ever arisen (§7).

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-16
(Wednesday) is **2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday
2026-09-21. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`; `consecutive_closed_losses`
stays at **0** because nothing has ever closed in this account, so the §6 streak cannot move, no
`HALT_CLEARED_AT` comparison was required and **no circuit-breaker alert was due.** **Sleeve drift:**
core **69.59%**, inside the 65–75% band. `open_thesis_ids` stays **none** — nothing to remove.

**⚠ THE FOMC RESOLVED AT 14:00 ET TODAY: +25bp TO 3.75%–4.00%, UNANIMOUS 12–0, THE FIRST US HIKE
SINCE 2023, WITH ANOTHER SIGNALLED FOR THIS YEAR.** Verified this run rather than inherited from the
plan's ">90% odds" — a probability is not a fact. **VOO closed −0.442% (693.215 from 696.29) on an
intraday range of 689.095–699.99, about 1.58% of the low against 0.53% yesterday and 0.68% Monday.**
**It is a price move, not a thesis**, there was no satellite thesis for it to invalidate, and **core
is exempt from all four §5 sell rules**, so the mark carries no exit at any number. **The FOMC is now
an input to the environment, not a Company A** — a rate-sensitive candidate arriving tomorrow enters
through §4 like anything else: mechanism, segment share, timing window, invalidation.

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
