# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-01 12:35 ET 3-midday-management
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

- **⚠ `TRADING_ENABLED: false` — the core bootstrap was dry-run and the account is still 100%
  cash. This is now the single most consequential open item, and it has moved from a prediction
  to an observed fact.** The 09:35 open run executed the §2 bootstrap exactly as planned —
  `buy VOO --notional 70000 --core` — and got back `"dry_run": true`, `"reason": "TRADING_ENABLED
  is not true in control.md"`, exit 0, **no order submitted**. `core_established` therefore stays
  `false` and the identical intent will regenerate tomorrow, and every day after, until a human
  sets `TRADING_ENABLED: true` in `control.md`. Nothing inside the system can change this and no
  run should try. **Do not read the reappearance of this line as a fault** — it is the configured
  behaviour working correctly — but do not let it go quiet either: §1 asks the book to beat the
  S&P over a rolling 12 months, and an all-cash book cannot track the index in either direction.
  Every day this stays false is a day of tracking error accruing in whichever direction the index
  happens to move. A ClickUp/push summary was sent on this run.

- **The full open-run path has now been exercised end to end, and it works.** This was the first
  `2-market-open-execution` run in the repo's history (`trade_log.md` and `journal.md` were both
  empty before it). Selftest passed all five checks; market confirmed open (`is_open: true`,
  09:35:59 ET); the staleness gate passed (`plan_date: 2026-09-01` == today); ledger reconciled
  against a live broker read; the bootstrap command ran and returned cleanly. **The only thing
  that did not happen is the fill.** That distinction matters for a future reader: the absence of
  a VOO position is not evidence of a broken run.

- **⚠ THE SCHEDULE IS STILL WRONG — carried forward unchanged, and still needs a human.**
  Routine 1 is specified for **08:00 ET weekdays** and fired **three times on 2026-09-01: 00:48,
  01:15 and 08:56 ET** (Alpaca server timestamps). The two faults, still separate:
  **(a) the ~7-hour offset did NOT repeat** — the 08:56 run landed inside the pre-market session,
  so the "cron written in UTC, read as ET" hypothesis does not fit and should be revised, not
  inherited; **(b) the duplicate firing DID repeat and got worse** — two became three in one day.
  Each firing writes a fresh set of thesis IDs against the same rolling news window, so
  `research_log.md` accumulates at ~3x the intended rate and `plan_today.md` is overwritten
  repeatedly before the open run consumes it. **Today that caused no harm** — all three
  pre-market runs agreed on every intent and the open run consumed the last one — but it is
  luck, not design. **This routine (2) fired once, at 09:35 ET, exactly as specified**, which
  narrows the fault to Routine 1's schedule entry specifically rather than the scheduler as a
  whole. That is new information and worth acting on. **Do not clear this line until Routine 1
  fires exactly once on a weekday, at or near 08:00 ET.**
  **Update 12:35 ET — Routine 3 also fired once, on time** (specified 12:30 ET, selftest clock
  12:35 ET). Two routines have now fired exactly once at their specified times on the same day.
  The scheduler is behaving; **the fault is in Routine 1's schedule entry alone.** A human
  fixing this should look at that one cron entry and nothing else.

- **Core sleeve still does not exist.** `core_established: false`, core 0.0% against a 70%
  target — outside the §2 65–75% band (`rebalance_needed: true`, `rebalance_delta: 70000.0`).
  Step 7's rebalance and Step 3's bootstrap are **the same $70,000 VOO buy** on this account, not
  two actions; a future run must not submit both. Do not clear this line until a VOO fill is
  verified in `trade_log.md`.

- **Week rollover: checked, none needed.** ISO Monday of 2026-09-01 (Tuesday) is 2026-08-31,
  which matches `week_of`. `new_positions_this_week` stays 0 — the §6 weekly cap is fully
  available (0 of 3 used). Breaker INACTIVE, `consecutive_closed_losses: 0`, no positions to
  evaluate against §5.

- **Today's research was spread over three runs and six thesis IDs, all REJECTED.**
  T-2026-09-01-01 (NOC), -02 (LHX), -03 (RTX) from the 00:48 run; -04 (MU), -05 (WDC) from
  01:15; -06 (AEP) from 08:56. A reader scanning `research_log.md` should not mistake this for
  three days of work — it is one rolling news window examined three times. **No BUY intents
  reached this run, so no priced-in re-checks were run and no skips were logged.**

- **PAC-3 MSE / THAAD ramp is a live event, deliberately not traded.** The Pentagon's 7-year
  multi-year procurement (announced 2026-08-31, 3–4x interceptor output) produced three
  rejected theses: NOC, LHX, RTX. If a later run rediscovers this event, read `research_log.md`
  T-2026-09-01-01 through -03 first rather than re-deriving it — the rejections were on §4.3
  timing (revenue is 2027+) and on magnitude, and neither fact will have changed by tomorrow.
  **NOC and LHX share one driver**; §4's correlation rule permits at most one of them at a time.

- **LHX watch item, not a thesis.** L3Harris is at a 52-week low (~$261.62 on 2026-08-24) on a
  postponed Missile Solutions IPO, possibly delayed to mid-2027 — not on deteriorating
  fundamentals (Q2 2026 beat on both revenue and EPS). Recorded because a future run will see a
  cheap defense name with a real missile-demand story and may mistake the two for the same
  thing. They are not. The IPO timeline is what moves this stock right now.

- **The memory-cost cycle is a live event, examined and deliberately not traded.** NVDA guided
  gross margin 75% → 71–72% by fiscal Q4 2027 on rising memory-chip costs. MU is the clean
  second-order name and its thesis is the strongest written so far — **rejected solely on §4
  priced-in: +5.27% over 5 sessions, +15.6% over 20.** STX (+4.20%) and SNDK (+5.11%) also fail;
  WDC is not exposed. **MU, STX and SNDK share one driver.** MU is **rejected, not queued** —
  re-run the priced-in check fresh and re-test the timing window from that day's date rather
  than inheriting either.

- **The Anthropic / Lambda / Hut 8 datacentre deal is a live event, examined and deliberately not
  traded.** ~350 MW at Hut 8's 1 GW Beacon Point campus, Nueces County TX, Nvidia holding the
  lease (WSJ/Reuters, 2026-08-31). Worked as T-2026-09-01-06. **Only AEP is tied to it by any
  source**, via AEP Texas's interconnection agreement — no equipment, cooling, EPC or land
  counterparty is named anywhere, and inventing one would repeat the RTX failure. Rejected on
  §4.2 magnitude and §4.3 timing: the 1 GW sits inside 45 GW of SB6-compliant load AEP Texas has
  *already contracted and guided through 2030*. **A cheaper AEP entry changes nothing** — the
  rejection is on timing, which a price move cannot fix.

- **⚠ STANDING RULES — three, sharing one root cause. Carried forward intact.**
  (i) *Screen on the mechanism before running filters* (from RTX — a filter is not a substitute
  for a sourced candidate). (ii) *Verify what the company currently sells, post-spin* (from WDC —
  it cleared the priced-in filter because it had sold the flash business). (iii) *Verify the news
  is new to the company's own disclosure* (from AEP — if management has already guided the
  pipeline the contract falls inside, the deal illustrates guidance rather than changing it).
  **The common root:** four of the six candidates (NOC, LHX, WDC, AEP) passed the §4 priced-in
  check and failed on the thesis; one (MU) passed the thesis and failed the filter. **The filter
  has not once been informative about the outcome.** Treat a passing priced-in check as a veto
  that did not fire, never as encouragement — "has not moved" and "should have moved but didn't"
  are the same number and the filter cannot tell them apart.

- **Cleared from carry-forward this run: nothing.** Every item above is still open. The
  `TRADING_ENABLED` item has changed in character — from an anticipated consequence to an
  observed one — and the schedule item has gained the observation that Routine 2 fired correctly,
  which localises the fault to Routine 1.

- **12:35 ET midday run (3-midday-management, first ever): nothing to manage, nothing done.**
  Market open, `positions` returned `[]`, sleeves identical to the 09:36 open run (equity
  $100,000.00, 100% cash). With zero open satellite positions, §5.1–5.4 had no input: no
  invalidation to test, no timing window to expire, no entry or high-water mark to measure a stop
  against. **No exits were taken and none should have been** — this is the important distinction
  for the next reader, because "no exits" and "an exit that failed to fire" look identical in a
  summary. No Perplexity queries were run; with no `invalidation` line in `positions.md` to check,
  a news query would have been activity for its own sake. **Step 2 high-water repair had no
  subject:** the trailing stop is not silently disabled, it is not yet armed, and it arms on the
  day the first satellite position opens. Week rollover re-checked: ISO Monday of 2026-09-01 is
  2026-08-31, matches `week_of`; `new_positions_this_week` stays 0 (0 of 3 used). Breaker
  INACTIVE, `consecutive_closed_losses: 0` — unchanged, and unchangeable by this run, since only
  a closed position moves the streak. **No ClickUp alert was raised and none was warranted:**
  `TRADING_ENABLED: false` is a configured state already reported by the 09:36 run, not a new
  incident, and re-alerting a standing condition is what the dedupe rules exist to prevent.
