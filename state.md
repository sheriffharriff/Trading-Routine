# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** Compacted from 324 KB on 11-13, regrew ×7.8, compacted again
11-20 (to 9,112 B) and **regrew ×2.38 to 21,708 B in four sessions.** **A value that needs a
paragraph belongs in `journal.md` or `weekly_review.md`.** See `weekly_review.md` 2026-11-27,
recurring error 8.

```
last_run: 2026-11-27 15:45 ET 5-friday-weekly-review — TWELFTH REVIEW, no trading in this routine. Selftest 5/5 exit 0. Fired 60 min early but 2h45m AFTER the 13:00 early-close bell, so the bar was final (n=1,486) and no hold was needed — DO NOT GENERALISE, Monday 11-30 is a full session. THE FINDING: `--adjustment all` DOES deliver total return; the two prior reviews' "defect" was a comparison against argparse's own `default="all"` (alpaca.py:427), so adjusted-vs-adjusted. Verified against `--adjustment raw`: 216/260 sessions differ, adj/raw ratio piecewise constant stepping exactly 4× at the 4 declared ex-dates, last step matching 1−1.8226/710.705. The hand "reconstruction" double-counted dividends and overstated the 12-month §1 benchmark by 1.247pp. Carry-forward 7(i) RETRACTED; 7(ii) stands and is now UNCANCELLED. Core −5.1985% vs VOO TR −5.4847% = +0.2862pp, fully decomposed to entry-vs-close +0.5603 less the uncredited $180.52 dividend −0.2579. Satellite 0.0000%, 100% idle cash, $30,000 — week excess −5.510pp/−$1,653.04 (the index ROSE 5.510%), 1M/3M/inception still +5.295/+5.229/+4.942pp. 314 theses 0 accepted 113 days. 0 closed trades ever; §5.1–5.4 all 0 fires, §5.4 unexecuted code. Reject board 29 names/18 decisions: mean +0.93pp per decision, but MONOTONIC in holding window — 1–4 sessions +3.15pp (12/14 beat), 5–8 −2.09pp, 9–16 −5.70pp. Equity $96,361.03 at the official 670.00 close (broker 96,543.59, 20th endpoint disagreement +1.8432/sh with a post-close-tape caveat). Core 68.8671% IN BAND, no rebalance due. Breaker INACTIVE, streak 0/3. Week reset: week_of 2026-11-23 → 2026-11-30, cap 0/3 expired unused for the 12th straight week. Monthly rollover NOT DUE (3rd Nov review; next 2026-12-04). alerts.md open: none, nothing SYSTEMIC. ClickUp weekly task 86bd7c8bj posted.
prior_run: 2026-11-27 15:16 ET 4-market-close-journal — SESSION DAY (09:30–13:00 early close) read off `bars` not the `clock` boolean, which showed the holiday shape (both dates on Mon 11-30) on a day that was a session; the prompt's holiday branch would have discarded a +1.19% day. Step 2 had NO OPERAND (zero satellite positions, no `highest_close` field anywhere — ABSENT, not stale, so no backfill owed). Equity 96,389.75, day +1.1874% off the 11-25 close, 0 trades, nothing non-terminal.
week_of: 2026-11-30
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.87
satellite_pct: 0.0
cash_pct: 31.13
open_thesis_ids: none
```

---

## Where things stand (2026-11-27, post-close, weekly review complete)

- ✅ **Selftest 5/5, exit 0.** `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md`
  Notes **(none)** · `alerts.md` Open incidents **(none)**, Resolved **(none)**.
- **Account at the official close:** equity **$96,361.03** = core mv **$66,361.03**
  (99.046311231 sh × 670.00) + cash **$30,000.00**. Inception **−3.6390%** from $100,000.
  Broker equity 96,543.59 off its 671.8432 mark; **same verdict either way.**
- **§2 band IN BAND.** Core **68.8671%** · satellite **0.0000%** · cash **31.1329%**.
  `rebalance_needed: false`; the $1,036.92 delta is distance to the 70% *target*, not a breach.
  **No rebalance due Monday.** The 65% floor breaks at VOO **562.51**, the 75% ceiling at
  **908.67** — invariant while cash is exactly $30,000 and the share count is unchanged.
- ✅ **Ledger reconciled, checked not inherited.** `grep -ci 'status: *open'` → **0** against one
  live `positions` row, VOO 99.046311231 sh @ 706.74 — the §2 core, **§5-exempt.** Core at
  −5.1985% is past §5.3's figure and **DO NOT SELL CORE** (§5 exempts it; §2 says core is not
  sold on news).
- ✅ **Nothing in limbo (§7).** `orders --status all` → one order in the account's entire history.
- **Week reset done per Step 6:** `week_anchor(2026-11-27)` → 2026-11-23 (imported from
  `common.py`) matched the inherited `week_of`, so nothing was owed mid-week; `week_of` is now
  **2026-11-30** and `new_positions_this_week` **0**.

## What this run did

Read every memory file, pulled account/positions/sleeves/bars, **measured the three §1 numbers
separately**, built a 29-name / 18-decision reject board with `move`, named ten recurring errors,
reset the weekly counter, confirmed the monthly rollover is not due, appended the review to
`weekly_review.md` (+26,349 B), posted it to ClickUp and committed. **No orders — routine 5 does
not trade.** No `trade_log.md`, `research_log.md` or `positions.md` write: nothing was submitted,
this routine generates no theses, and there is no open position to digest.

## Carry forward

1. ⚠⚠ **CARRY-FORWARD 7(i) IS RETRACTED. `--adjustment all` IS a total-return series.** The
   "defect" was a comparison against `argparse`'s own `default="all"` (`scripts/alpaca.py:427`),
   i.e. adjusted vs adjusted. **Verified four ways against `--adjustment raw`** (216/260 sessions
   differ; adj/raw piecewise constant with exactly 4 steps, at the 4 declared ex-dates; last step
   = 1−1.8226/710.705 to five decimals; start-of-series drag 1.1385% ≈ the TTM yield). **Use
   `--adjustment all` and stop reconstructing.** The 11-13 and 11-20 reviews' VOO total-return
   rows are overstated on any window containing an ex-date — 12-month by **1.247pp**, 3-month and
   inception by ~0.23pp; week and 1-month unaffected.
2. ⚠⚠ **7(ii) STANDS AND IS NOW UNCANCELLED: the paper broker never credits distributions.**
   `cash` is exactly `30000`, `accrued_fees` `0`, and the **$180.52** owed on the 2026-09-28
   ex-date was never paid. Against a total-return benchmark the core sleeve is structurally short
   **~1.07%/yr**, widening each quarter. **This is visible in the core number, not hidden behind
   an offsetting error, and it is the human's to fix or accept.**
3. ⚠⚠ **RE-RUNNING A COMPARISON IS NOT VERIFYING IT.** Item 1's error survived a run that
   explicitly re-derived it "from two fresh calls" and watched it reproduce. **A re-derivation that
   cannot fail differently from the original is a ritual.** Change the basis, not the timestamp.
4. ⚠⚠ **THE FUNNEL: 314 theses, 0 accepted, 113 days, 80 sessions.** The binding constraint is
   part 1 / no named counterparty, for the sixth consecutive review. ⚠ Whether the *search* should
   change — screening disclosed supplier relationships before news — is a `strategy.md` question.
   **No seat may lower a bar. Flagged for the human, six reviews running.**
5. ⚠⚠ **THE §4 PRICED-IN FILTER TESTS ABSOLUTE MAGNITUDE AND THE FIRST REAL EVIDENCE IS
   TWO-SIDED.** `T-2026-11-25-01` (MU) passed **all four parts with sourced figures** — the only
   one in 113 days — and died on a **−11.63%** DOWN move; one session later MU is +7.36%/+5.65pp,
   SNDK +15.55%/+13.84pp, STX +7.96%/+6.25pp (three tickers, ONE driver, so ONE forgone trade).
   ⚠ But the **up**-move kills are the filter's cleanest wins: LEU (+17.11% at rejection) is
   −17.50%/−14.17pp and AMAT (+19.34%) is −12.92%/−9.59pp nine sessions on; and the same memory
   shape rejected on 11-02/11-03/11-18 would have run **−22.66% / −39.63% / −8.55%**, the last
   past §5.3's stop. **One session of bounce does not test a weeks-to-months thesis. Recorded as a
   measurement, NOT a conclusion. A directional variant is a calibration change — the human's.**
6. ⚠ **THE REJECT BOARD'S SIGN TRACKS THE HOLDING WINDOW, NOT THE JUDGMENT.** 1–4 sessions
   **+3.15pp** (12/14 beat VOO) · 5–8 **−2.09pp** · 9–16 **−5.70pp** (1/4). Every reject old enough
   to judge on §1's horizon fell. **Report per decision as well as per name** — one tier thesis
   supplies 7 of 29 names.
7. ⚠⚠ **ALL ROUTINES FIRE ~45–60 MIN EARLY — RECORDED, NOT DIAGNOSED.** `control.md` says manual
   "Run now" invocations are indistinguishable from scheduled ones, so **no run may call this a
   schedule fault.** ⚠ Counts (routine 4 ≈17, routine 2 ≈5, routine 3 ≈3, routine 1 ≈4) are
   **inherited and unverifiable — this is a shallow clone and anything before ~11-09 is invisible
   to a git check.** ⚠⚠ **Consequences differ and must not be folded together:** routine 2's
   pre-market fire can skip a whole session on a literal reading of its own prompt (wrong on four
   session days, exactly right on the 11-26 holiday; mitigate by polling to `is_open: true` **only
   when both `clock` dates read today**, with a deadline); routine 4's hurts on a full session and
   helped on today's early close. **`bars` is the discriminator for "did today open?" — a session
   day returns a bar dated today with real volume, a holiday returns none. Reconciling the prompts
   is the human's call.**
8. ⚠⚠ **§5.4 IS UNEXECUTED CODE.** No `highest_close` and no `(as of …)` date exists in
   `positions.md` — 196 strings match `highest_close` and the only one with a number is the
   template's `0.00`. **ABSENT is a third state, distinct from current-and-unchanged and stale**,
   so the midday backfill branch finds no date rather than an old one and owes no `bars` call.
   ⚠ **When a mark is first stamped it must come from official `bars` closes only, one basis, one
   call — never from `positions.current_price`:** the two endpoints have now disagreed on **20**
   distinct sessions, range 0.04–1.84/share, today's +1.8432 being the widest (with a post-close
   tape caveat). The convenient endpoint and the correct one are not the same endpoint.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND NEEDS A RETENTION RULE FROM THE HUMAN.**
   Measured from `git show 7475620:` — **1,266,946 B → 1,433,421 B in four sessions (+166,475 B,
   ~41.6 KB/session)** documenting **one trade**, with `weekly_review.md` adding 26,349 B on top.
   `state.md` 9,112 → 21,708 B (×2.38) before this rewrite. **`positions.md` is ~391 KB and holds
   ZERO open positions**, excluded from rollover on a premise false for all 113 days. Three asks,
   none actioned: a retention rule for `positions.md`; a hard one-line cap on `last_run`; and an
   archive policy for `weekly_review.md` (now 441 KB, never archived).
10. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT, OR A NUMBER FROM INTENT BEFORE COMPUTING
    IT.** 11-16 published a false "worst session ever" (off by 2×); 11-25 drafted "narrowed" for a
    loss that had **widened** 0.27pp, in the flattering direction, left in `journal.md` with its
    correction. ⚠ **Applied at this seat:** the core's +0.2862pp excess was **decomposed to the
    cent** before being described, rather than read as skill; the week's **−5.510pp** was reported
    as the lead even though three other windows were positive; this review's own byte cost was
    **counted after drafting** (+26,349 B); and the endpoint counter moved 19 → 20 only because
    today is a new close.
11. ⚠ **ONE REVIEW IS MISSING FROM THE SERIES: 2026-11-06.** Thirteen Fridays, twelve reviews. The
    October archive rollover it owed was carried late by the 11-13 run. **Not recoverable.**
