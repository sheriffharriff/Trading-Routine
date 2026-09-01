# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-01 01:15 ET 1-premarket-research (second run of the day)
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

- **⚠ THE SCHEDULE IS WRONG, AND IT IS THE MOST ACTIONABLE ITEM HERE.** Routine 1 is specified
  to run at **08:00 ET on weekdays**. It has now fired **twice on 2026-09-01, at 00:48 ET and
  at 01:15 ET** — both roughly seven hours early, 27 minutes apart. (Times are Alpaca server
  timestamps, not container clock, so this is not a timezone artifact locally: `alpaca.py clock`
  returned `2026-09-01T01:15:35-04:00`.) Two independent faults, and they need separating:
  **(a)** the trigger time is off by ~7 hours — consistent with a cron expression written in UTC
  and interpreted as ET, or the reverse; **(b)** it fired *twice*, which a single misconfigured
  time does not explain on its own.
  **Why this is not cosmetic.** Research done at 01:00 ET is done against a stale tape: no
  pre-market prints, no overnight-to-open gap, and a `move --sessions 5` window that still ends
  at the *prior* session's close. Every priced-in check in `research_log.md` for 2026-09-01 was
  computed on that basis. They are not wrong, but they are older than the 08:00 slot intends,
  and the 09:35 run's `revalidate` step is doing more work than it was designed to.
  A human has to fix the schedule — no run can fix it from inside. **Do not clear this line
  until a Routine 1 run actually fires at 08:00 ET.**

- **Today's research is spread over two runs and five thesis IDs.** T-2026-09-01-01 (NOC),
  -02 (LHX), -03 (RTX) came from the 00:48 run; -04 (MU), -05 (WDC) from the 01:15 run. All
  five REJECTED. A reader scanning `research_log.md` should not mistake this for two days of
  work — it is one news window examined twice.

- **Core sleeve still does not exist.** `core_established: false`, core 0.0% against a 70%
  target — outside the §2 65–75% band. A REBALANCE intent to buy $70,000 of VOO is written
  into `plan_today.md` for the 09:35 run. Do not clear this until a VOO fill is verified in
  `trade_log.md`.

- **`TRADING_ENABLED: false` — the bootstrap will not actually execute.** The open run will
  dry-run the VOO buy and the account will stay 100% cash. This intent will therefore
  regenerate every day until a human sets `TRADING_ENABLED: true` in `control.md`. The next
  run should expect to see this same carry-forward line and should **not** treat its
  reappearance as evidence that something failed — but it also should not let it go quiet.
  This is a human decision, and it is the single most consequential open item in the system.

- **Week rollover: checked, none needed this run.** ISO Monday of 2026-09-01 (Tuesday) is
  2026-08-31, which already matches `week_of`. The 00:48 run advanced it from 2026-08-03.
  `new_positions_this_week` stays 0 — the §6 weekly cap is fully available (0 of 3 used).

- **PAC-3 MSE / THAAD ramp is a live event, deliberately not traded.** The Pentagon's 7-year
  multi-year procurement (announced 2026-08-31, 3–4x interceptor output) produced three
  rejected theses today: NOC, LHX, RTX. If a later run rediscovers this event, read
  `research_log.md` T-2026-09-01-01 through -03 first rather than re-deriving it — the
  rejections were on §4.3 timing (revenue is 2027+) and on magnitude, and neither of those
  facts will have changed by tomorrow. **NOC and LHX share one driver**; §4's correlation
  rule permits at most one of them, ever, at the same time.

- **LHX watch item, not a thesis.** L3Harris is at a 52-week low (~$261.62 on 2026-08-24)
  on a postponed Missile Solutions IPO, possibly delayed to mid-2027 — not on deteriorating
  fundamentals (Q2 2026 beat on both revenue and EPS). Recorded because a future run will
  see a cheap defense name with a real missile-demand story and may mistake the two for the
  same thing. They are not. The IPO timeline is what moves this stock right now.

- **Process correction from the 00:48 run — applied, and it worked.** That run flagged that it
  had screened RTX through the priced-in check before establishing RTX had any documented
  PAC-3/THAAD content: a filter is not a substitute for a sourced candidate. The 01:15 run
  screened on the mechanism first (NVDA names memory costs → who sells memory?) and only then
  filtered. Keep doing it in that order.

- **Second process correction, from T-2026-09-01-05 (WDC) — verify the business before the
  screen.** WDC was the only memory-complex name to clear the priced-in filter, and it cleared
  it because it **is not in the memory complex**: the Sandisk separation completed 2026-02-21
  and WDC is now HDD-only (Cloud 89% / Client 8% / Consumer 3%). A candidate that "passes while
  its peers are late" is an inviting shape and was, here, entirely an artifact of the company
  no longer selling the product. Generalised: **a passing priced-in check is not evidence of an
  opportunity.** "Has not moved" and "should have moved but didn't" are the same number, and
  the filter cannot tell them apart. Confirm current segment exposure — post-spin,
  post-divestiture — before a name enters the funnel.

- **The memory-cost cycle is a live event, examined and deliberately not traded.** NVDA guided
  gross margin 75% → 71–72% by fiscal Q4 2027 on rising memory-chip costs. MU is the clean
  second-order name and its thesis is the strongest written so far (one-clause mechanism, DRAM
  76% of a $37.4B revenue base, in-horizon) — **rejected solely on §4 priced-in: +5.27% over 5
  sessions, +15.6% over 20.** STX (+4.20%) and SNDK (+5.11%) also fail; WDC is not exposed.
  **MU, STX and SNDK share one driver** — §4's correlation rule permits at most one of them.
  If a later run rediscovers this event, read T-2026-09-01-04 before re-deriving it, and note
  that MU is **rejected, not queued**: re-run the priced-in check fresh and re-test the timing
  window from that day's date rather than inheriting either.
