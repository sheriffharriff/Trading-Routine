# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** The 2026-11-13 review compacted this file from 324KB /
2,988 lines after its `last_run` value had grown into a multi-thousand-byte paragraph; it
regrew ×7.8 and was compacted again on 11-20. **A value that needs a paragraph belongs in
`journal.md`.** See `weekly_review.md` 2026-11-20, Recurring Error 8.

```
last_run: 2026-11-24 11:41 ET 3-midday-management — selftest 5/5 exit 0. Market OPEN. Zero satellite positions, so Steps 2-5 had NO OPERAND: no high-water backfill owed, no §5 rule evaluable, no perplexity call spent, no exit possible. Ledger AGREES (0 blocks vs 1 Alpaca row, VOO core, §5-exempt). Core 68.40% in band. Breaker INACTIVE 0/3, cap 0/3.
prior_run: 2026-11-24 09:32 ET 2-market-open-execution — plan dated today, staleness gate PASSED, zero intents; 0 buys, 0 sells; waited 28 min for the bell before acting.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.40
satellite_pct: 0.0
cash_pct: 31.60
open_thesis_ids: none
```

---
## Where things stand (2026-11-24, **LIVE MIDDAY MARK — VOO 655.745, `is_open: true`**)

- **Nothing was managed because there was nothing to manage, and that is the whole run.**
  **Satellite sleeve empty, 84th absent date** (`grep -ci 'status: *open'` → **0**); `positions`
  returns **one** row, VOO 99.046311231 sh @ 706.74 — the §2 core, **§5-exempt, struck from the
  working list, not cleared.** **Ledger and broker agree; no disagreement to reconcile.**
- **§5.1–§5.4 are ABSENT, NOT PASSING.** No `entry_price`, no `highest_close`, no `(as of …)`
  date, no deadline and no invalidation string exists anywhere. **Step 2's staleness detector and
  `bars` backfill branch remain unexecuted code at 84 absent dates**, as do all four sell rules.
  ⚠ **No `perplexity` call was spent:** §5.1 tests a written invalidation condition against the
  news, and with no condition there is no query to ask. Spending one would have manufactured work.
- **This routine opened nothing and could not have.** Exits only, by design — §4 routes every buy
  through the pre-market seat and the 09:35 execution run. **No candidate was looked for.**
- **§2 band: in band, read LIVE, not inherited** — and §2 rebalancing is **routine 2's job, not
  this seat's.** Core **68.40%**, satellite **0.00%**, cash **31.60%**, `core_in_band: true`,
  `rebalance_needed: false`. Thresholds **re-solved here, not copied**: with cash $30,000 and
  99.046311231 shares the **65% floor breaks at VOO 562.51** and the **75% ceiling at 908.67** —
  **−14.2% / +38.6%** from the 655.745 mark. `rebalance_delta: 1516.60` is the distance to the
  70% *target*, **not a breach of the band**; §2 rebalances on the band.
- **Equity $94,944.68 · core mv $64,944.68 · unrealized −$5,050.87 / −7.216% · cash $30,000.00.**
  ⚠⚠ **CORE −7.216% IS NOT A §5 EVENT, AND IT SITS PAST THE §5.3 MAGNITUDE.** §5 exempts core
  outright and §2 says core is not sold on news. Emphasised because the number is past the 7%
  hard-stop *figure*, and a fresh-clone seat reading only the P&L line is exactly the failure mode
  this warning exists for. **VOO −1.23% on the session; this is a market drawdown, not a signal.**
- **Week rollover: none due, re-derived.** `week_anchor(2026-11-24)` → **2026-11-23** (imported
  from `common.py`) = inherited `week_of`. `new_positions_this_week` stays **0 of 3**.
- **Breaker correctly INACTIVE 0/3** — nothing has ever closed, so there is no streak and no §6
  alert was owed. `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md` Notes
  **(none)** · `alerts.md` **no open and no SYSTEMIC incidents** · `open_thesis_ids: none`.
- ⚠ **This seat fired 11:41 for a 12:30 slot (~49 min early) and it cost nothing: the market was
  OPEN, so an exit was placeable had one been due.** Per `control.md` Notes, manual "Run now"
  invocations are indistinguishable from scheduled ones in run logs, so **this is recorded, not
  diagnosed as a schedule fault.** Contrast carry-forward item 3, where early firing lands
  *before* the bell and does bite.
- ⚠⚠ **THURSDAY 2026-11-26 IS THANKSGIVING; FRIDAY 2026-11-27 IS AN EARLY CLOSE.** Tomorrow is an
  ordinary full session (`next_open` 2026-11-25 09:30). Do not plan a Thursday execution, and do
  not read Thursday's `is_open: false` as the pre-market signature — **check the `next_open` date.**

## What this run did

Read the five memory files, confirmed the market open, confirmed the ledger empty against the
broker, and **stopped.** The routine's own instruction for an empty ledger is "note it, commit,
exit — do not go looking for something to do," and the temptation this seat had to resist was not
trading (it may not) but **generating analysis to fill the run**: re-deriving the band it does not
own, pulling `bars` for a position that does not exist, or querying news against an invalidation
condition that was never written. **None of that was done.**

⚠ **Byte accounting, measured with `wc -c` after the write, not claimed from intent:**
`positions.md` **377,211 → 378,179 B (+968)**, one reconciliation note, no digest block.
`state.md` rewritten from **12,069 B** — the compression came from the two per-run narration
sections, not from carry-forward, which is left intact because it is the only continuity.
`research_log.md`, `trade_log.md` and `journal.md` **untouched — correctly:** no order reached a
terminal state, so no trade entry was owed, and **an append to any of them would have been a
fabrication.** ⚠ **Three seats today have now each recorded the same absence** (07:02 ~1 KB,
09:32 ~0.6 KB, 11:41 ~1 KB). That is the standing finding in item 9 arriving again, and **no seat
has standing to truncate another's prose.**

## Carry forward

1. ⚠⚠⚠ **THE FUNNEL MAY BE UNSATISFIABLE BY CONSTRUCTION — STILL THE HUMAN'S CALL.** The disputed
   sweep asks whether a **news source has already named** the second-order company and segment;
   **§4 demands no such thing**, and requiring it restricts the funnel to links the market has
   already been told about — **exactly the set §4's priced-in filter then kills.** 11-24's
   pre-market seat **omitted that sweep and still found nothing**, dying on part-2 materiality
   instead: one data point *against* the gate being the whole explanation, and **one session must
   not be over-read.** Useful next step: keep omitting it and watch whether kill reasons migrate
   from part 1 to parts 2/3 — a *diagnostic* change, not a calibration change. **No seat may relax
   a §4 test, and none has.**
2. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING.** `T-2026-11-24-02` (Capricor CRL) was the **third**
   "FDA rejection → incumbent benefits" object in three weeks, disposed with **zero** drill
   queries because the prior entries were read and applied; `-03` was the **sixth-plus**
   unnamed-hyperscaler object. ⚠ **Re-use worked only because those kills are structural** ("a
   rejection preserves the status quo" holds independent of drug, company and date). **An object
   whose kill depends on a figure that can change still needs re-checking.** A disposed-objects
   list the pre-market seat checks first would help, **but defining "disposed" is a calibration
   change and so is the human's.**
3. ⚠⚠ **BOTH EXECUTION ROUTINES FIRE ~60 MIN EARLY — AND THE ROUTINE-2 MITIGATION NOW HAS ONE
   DEMONSTRATION.** Routine 4: 15:15 for a 16:15 slot, ~13 consecutive times. Routine 2: 08:36 for
   09:35, **now twice (11-23, 11-24)**. ⚠ **RECORDED, NOT DIAGNOSED** — `control.md` states manual
   "Run now" invocations are indistinguishable from scheduled ones in run logs, so **no run may
   call this a schedule fault.** Consequences differ and must not be folded together: routine 4's
   job is recording *closing* prices; **routine 2's job is placing orders, and an early fire that
   exits on `is_open: false` skips a whole day's execution.** Mitigation is the same shape and has
   worked every time used: **poll `clock` to the right signature** — routine 4 waits for
   `is_open: false` with **both** `next_open` and `next_close` on the *next* session, then ~5 min,
   then `bars`; routine 2 waits for **`is_open: true`** (28 min on 11-24). ⚠ **Read the DATES, not
   the boolean: FALSE has three meanings, TRUE has one.** ⚠ Routine 3 also fires early (11:41 for
   12:30) but lands **inside** the session, so it is benign — do not fold it into this item.
4. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`.** That scoping error cost 2026-11-13,
   whose journal entry and ClickUp summary do not exist and never will.
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 16
   distinct sessions, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.** ⚠ Not re-measured today: no `bars` call was owed and one must not
   be spent merely to extend a tally.
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** (i) **`--adjustment all` is not
   a total-return series on this feed** — byte-identical to the unadjusted series on 259 of 260
   sessions across all four ex-dates. Reconstruct by reinvesting at the ex-date close: 2025-12-22
   $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28 $1.8226 (TTM $7.43; **none since
   09-28**). Taken literally, Step 1 understates the 12-month benchmark by **1.25pp**.
   (ii) **The paper broker never credits distributions** — `cash` is exactly `30000`, not
   $30,180.52; `accrued_fees` 0. The core sleeve is structurally short ~1.07%/yr against any honest
   total-return benchmark, widening every quarter. ⚠⚠ **The two defects roughly cancel, which is why
   ten reviews caught neither.**
8. ⚠ **THIS CLONE IS SHALLOW.** Any run citing git history beyond ~2 weeks is citing something it
   cannot see. Do not repeat inherited history claims as measured.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` before this seat's writes: `weekly_review.md` **415,188 B** ·
   `positions.md` **377,211 B** · `research_log.md` **345,256 B** · `journal.md` **158,415 B** —
   **~1.3 MB of markdown documenting ZERO satellite trades.** `positions.md` is excluded from
   monthly rollover on the premise that it "only holds open positions," which has been false for
   all 84 absent dates, **so no run has standing to truncate it.** The one lever a run *does* have
   is to stop feeding it — this seat added **968 B** and compressed `state.md` rather than growing
   it. ⚠ The `state.md` figure is the one number that cannot be exact, because writing it changes it.
