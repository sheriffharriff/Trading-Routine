# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-02 09:36 ET 2-market-open-execution
week_of: 2026-08-31
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: false
core_ticker: VOO
core_pct: 0.0
satellite_pct: 0.0
cash_pct: 100.0
open_thesis_ids: none
```

---

## Field meanings

**`week_of`** — the Monday of the current ISO week. Every run compares today's week anchor
to this value; if they differ, reset `new_positions_this_week` to 0 and update this field.
The reset deliberately does not depend on the Friday review having run, so a skipped Friday
cannot leave the §6 weekly cap stuck at its limit.

**`new_positions_this_week`** — satellite positions *opened* this week. §6 caps it at 3.
Exits do not count.

**`consecutive_closed_losses`** — incremented when a satellite position is closed at a loss,
reset to 0 when one closes at a gain. At 3, set `circuit_breaker: ACTIVE` and record
`halt_triggered_at` as today.

**`circuit_breaker`** — `ACTIVE` or `INACTIVE`. While ACTIVE: no new positions of any kind
(§7). Existing positions are still managed per §5, research and journaling continue, and the
halt is flagged prominently in the ClickUp summary (§6). Core rebalancing is still permitted —
§6 halts *new positions*, and restoring the core sleeve to its 70% target is neither a new
position nor a satellite trade.

**`halt_triggered_at`** — date the breaker tripped. Compared against `HALT_CLEARED_AT` in
`control.md`; the halt lifts only when the clearance date is strictly later. If the breaker
is ACTIVE and this field is `none`, the halt stays active — an unknown trigger date is not
grounds to start trading.

**`core_established`** — `false` until the VOO core sleeve exists. The market-open routine
bootstraps it on the first trading day and this flips to `true`, which disables the
bootstrap path permanently.

**`core_pct` / `satellite_pct` / `cash_pct`** — sleeve allocation as of the last run, in
percent of total account value. §2 rebalance band is core 65–75%.

**`open_thesis_ids`** — comma-separated thesis IDs for currently open satellite positions.
Cross-check against `positions.md`; if they disagree, `positions.md` and the live Alpaca
position list win, and the discrepancy goes in the journal.

---

## Carry forward

Anything the next run must not lose. Cleared once acted on.


- **⚠ `TRADING_ENABLED: false` — day three, and this run is the one that makes the cost concrete.**
  The account is still 100% cash and the core sleeve still does not exist. Only a human can close
  this, in `control.md`. Read it as **configured behaviour, not a fault**: `control.md` describes
  the dry run in its own words as a way to "watch the system think for a week before it touches the
  account," and today is day three of that week. The 09:36 ET open run submitted the §2 bootstrap
  exactly as planned and got `{"ok": true, "dry_run": true, "reason": "TRADING_ENABLED is not true
  in control.md"}`, exit 0, no order — logged under `trade_log.md` → *Dry-run intents*, not as a
  fill. **Do not raise a ClickUp alert for this and do not let a run treat the reappearing intent
  as a bug.** What is new today is the arithmetic: VOO closed 700.14 on 09-01 and traded 700.555 at
  the open today, so across two dry-run days the index is roughly flat (−0.67%, then +0.06%) and
  the un-deployed sleeve has neither gained nor lost much by sitting out. **That near-zero is
  coincidence, not evidence the delay is cheap** — the same mechanism that sat out yesterday's
  down day sits out every up day at exactly the same rate, and §1 asks this book to beat the S&P
  over a rolling twelve months, which an all-cash book cannot track in either direction.

- **Core sleeve still does not exist, and the bootstrap and the rebalance are ONE action.**
  `core_established: false`, core 0.0% against a 70% target — outside the §2 65–75% band
  (`core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0`, unchanged across
  all six runs since 2026-09-01 00:48 ET). Step 3's bootstrap and Step 7's rebalance are **the
  same $70,000 VOO buy** on this account. Today's run submitted it **once** and explicitly did not
  re-submit it at Step 7; the next run must do the same. Do not clear this line until a VOO fill is
  verified in `trade_log.md` → *Entries*.

- **SCHEDULE: two clean days, ready to clear on the next one.** Routine 1 is specified for 08:00 ET
  weekdays; it fired three times on 2026-09-01 (00:48, 01:15, 08:56 ET) and **once on 2026-09-02,
  at 08:30 ET** — 30 minutes late but singular. Routine 2 has now fired **once, on time, on both
  weekdays** (09:36 ET on 09-01 and again 09:36 ET today), which is what it is specified to do; the
  fault was always localised to Routine 1's own schedule entry and remains so. The standing
  instruction was to clear this after a second consecutive weekday of a single near-08:00 firing.
  **Today is Routine 1's first clean day; tomorrow is the test.** If 2026-09-03 produces exactly one
  Routine 1 run at or near 08:00 ET, clear this line. The ~7-hour-offset theory from the 00:48 run
  stays dead.

- **Week rollover: checked, none needed.** ISO Monday of 2026-09-02 (Wednesday) is 2026-08-31,
  which matches `week_of`. `new_positions_this_week` stays 0 — the §6 weekly cap is fully available
  at 0 of 3, and nothing this run consumed any of it. Breaker INACTIVE,
  `consecutive_closed_losses: 0`, `halt_triggered_at: none`; only a closed position can move the
  streak and nothing has closed. `HALT_CLEARED_AT: none` in `control.md`, correct and irrelevant
  while no halt exists.

- **The staleness gate PASSED today, and that is worth recording because it is the first time it
  was a live test.** `plan_today.md` carried `plan_date: 2026-09-02` against an ET date of
  2026-09-02, so the plan was today's and its intents were executable. No stale-plan alert was
  raised and none was warranted. A future run must still re-read `plan_date` rather than assume
  this outcome — the gate is only useful if it is checked on the day it would fire.

- **Steps 4, 5 and 6 had genuinely empty input — not skipped, empty.** The plan carried **no SELL
  intents** (no open satellite positions exist, so §5.1–5.4 have no subject) and **no BUY intents**
  (both of today's theses were rejected pre-market). No `alpaca.py move` re-validation was run,
  because there was no BUY intent to re-validate; that is the correct reason for its absence, not
  an omission. Nothing was logged to `research_log.md` this run for the same reason — a skip is
  only logged against a thesis that reached the open as an intent, and neither of today's did.

- **⚠ LHX REMAINS THE MOST DANGEROUS NAME IN THIS LOG, and the reason is that it keeps being almost
  right.** It has surfaced on two consecutive days through **two different, separately sourced
  drivers** — PAC-3 MSE / THAAD propulsion (T-2026-09-01-02, died on §4.3 timing) and the Army
  TITAN production award (T-2026-09-02-01, died on §4.2 magnitude: $127M across a five-partner team
  against $21.865B of revenue, ≤0.58%). Meanwhile it sits near a 52-week low and passes the
  five-session priced-in check cleanly. **The thing actually moving the stock is still the postponed
  Missile Solutions IPO** — a third event, unrelated to either mechanism. **Standing rule: when the
  same ticker surfaces on consecutive days through different events, treat the recurrence as a
  warning, not as corroboration.** A large diversified prime appears in every defense news cycle by
  construction; appearing is not being materially affected, and each event must clear §4 on its own
  numbers. Note for the open run specifically: LHX was *not* an intent today and must not be
  reached for at the bell on the strength of how often it appears.

- **The "Company A's print implies Company B's print" failure recurred within 24 hours, in a
  different sector and at ten times the scale.** On 2026-09-01 the funnel dropped "SAIC beats and
  raises → buy LDOS/CACI/BAH" as a correlation dressed as a mechanism. On 2026-09-02 the identical
  shape arrived as "Dell raises AI-server guidance → HPE rises ~5% on improved sentiment," backed
  by genuinely arresting numbers ($60.9B of quarterly AI orders, a $95B backlog, FY guidance up
  $25B). It was harder to dismiss *because* the underlying demand is so obviously real. **The size
  of Company A's number has no bearing on whether a mechanism to Company B exists.** A $95B backlog
  at Dell is $0 of revenue at HPE. Expect this shape again; it is the most fluent sentence
  available on any given day.

- **MU: not re-checked, and the reason matters more than the fact.** The pre-market journal
  predicted a pull to re-run Micron's priced-in check hoping for a friendlier number, and named it
  in advance as an inheritance-of-conclusion failure. What stopped it was **not resolve — MU does
  not appear anywhere in today's funnel.** No source across six queries named Micron or any memory
  supplier in connection with any of today's events, including Dell's AI-server ramp, where a
  dedicated screen for component suppliers and for memory-cost commentary came back **explicitly
  empty on both**. **The correct reason not to re-check a rejected candidate is that today's
  evidence does not produce it.** If a future run's funnel does surface MU from a source, re-running
  the filter and re-testing the timing window from that day's date is legitimate and different from
  what almost happened here.

- **⚠ STANDING RULES — four, sharing one root cause.**
  (i) *Screen on the mechanism before running filters* (from RTX — a filter is not a substitute for
  a sourced candidate). (ii) *Verify what the company currently sells, post-spin* (from WDC).
  (iii) *Verify the news is new to the company's own disclosure* (from AEP — if management has
  already guided the pipeline the contract falls inside, the deal illustrates guidance rather than
  changing it). (iv) *A recurring ticker is a warning, not corroboration* (from LHX, above).
  **The common root:** across eight candidates, six passed the priced-in check and failed on the
  thesis (NOC, LHX×2, WDC, AEP, and HPE would have but died at part 1), and one (MU) passed the
  thesis and failed the filter. **The filter has still never been informative about the outcome.**
  Treat a passing priced-in check as a veto that did not fire, never as encouragement — "has not
  moved" and "should have moved but didn't" are the same number.

- **Observation for the human about `alpaca.py move`, not an argument against it.** The script
  tests **absolute** magnitude, so a stock that has *fallen* more than 4% returns
  `priced_in: true`. On 2026-09-02 HPE (−4.96%) and DELL (−5.84%) both tripped it on five-session
  windows ending before Dell's print — drawdowns, not run-ups. §4's wording is "already moved more
  than 4% over the last five sessions **on this news**," so a decline predating the news is arguably
  not the thing the rule aims at. **Nothing has turned on it yet** (HPE died at part 1, DELL is
  Company A) and **no run should reinterpret the filter on its own authority** — a veto that fires
  too often is the safe direction. But a legitimate candidate that fell 5% on unrelated news would
  be blocked, and that is a human's call to make deliberately rather than discover by accident.

- **Live events examined and deliberately not traded — do not re-derive these.**
  (a) **PAC-3 MSE / THAAD ramp** (Pentagon 7-year MYP, 2026-08-31): NOC, LHX, RTX all rejected on
  §4.3 timing (revenue is 2027+) and magnitude. **NOC and LHX share one driver**; §4 permits at
  most one. (b) **The memory-cost cycle** (NVDA guiding GM 75% → 71–72% by FQ4 2027): MU is the
  clean second-order name and the strongest thesis written so far, **rejected solely on priced-in**
  (+5.27% / 5 sessions, +15.6% / 20). **MU, STX and SNDK share one driver.** (c) **The Anthropic /
  Lambda / Hut 8 Beacon Point datacentre deal**: only AEP is tied to it by any source, rejected on
  §4.2 magnitude and §4.3 timing — 1 GW inside 45 GW AEP has *already guided through 2030*. **A
  cheaper AEP entry changes nothing**; the rejection is on timing, which a price move cannot fix.
  (d) **GE's $2.87B Navy F414 PBL award** (2026-09-01): a dedicated screen confirmed the award is
  **sole-source to GE with no other publicly traded company named** — there is no Company B, and
  inventing a supply chain from general knowledge would repeat the RTX failure. (e) **Nvidia /
  Hugging Face, ~$14B**: unsigned as of 2026-09-02 ("a final agreement hasn't been reached"),
  target private, no third party named by any source. Not a fundamentals trade.

- **Eight thesis IDs now carry a 2026-09-0x date across two days**; six of those are from
  2026-09-01, produced by three runs against one rolling news window. **A reader scanning
  `research_log.md` should not read eight IDs as eight days of work.**

- **The §5.4 trailing stop is not armed, and `positions.md` needs no backfill.** Zero position
  blocks means zero `highest_close` fields, so there is nothing for a `bars` backfill to repair.
  The trailing stop arms on the day the first satellite position opens, which under
  `TRADING_ENABLED: false` cannot be today. Six consecutive runs have now recorded this
  distinction rather than assuming it carried, because "current and empty" and "the high-water pass
  was skipped" look identical in a summary.

- **`alerts.md` remains empty — zero incidents, nothing SYSTEMIC, nothing unresolved.** No alert
  was raised this run and none was warranted. The two standing conditions (`TRADING_ENABLED: false`
  and Routine 1's schedule) are known human-owned items already reported via ClickUp task
  `86bbrna9n` on 2026-09-01; re-alerting a standing condition is exactly what the dedupe rules
  exist to prevent.

- **Cleared from carry-forward this run: nothing.** The schedule item now has one clean Routine 1
  day behind it and a stated test for tomorrow. Everything else stands.
