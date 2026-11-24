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
last_run: 2026-11-24 16:10 ET 4-market-close-journal — selftest 5/5 exit 0. RESTAMPED ON THE OFFICIAL CLOSE (VOO 660.67, post-bell signature 16:00:04 + 5 min settle). Equity 95436.93, day -0.3454%, inception -4.5631%. 0 trades. Step 2 high-water marks NOT updated — NO OPERAND, zero satellite positions, no backfill owed. Core 68.5656% in band. Breaker INACTIVE 0/3, cap 0/3. Summary 86bd6nt1p. FOUND + CORRECTED the 2026-11-20 entry, whose restamp never landed.
prior_run: 2026-11-24 11:41 ET 3-midday-management — selftest 5/5 exit 0. Market OPEN. Zero satellite positions, so Steps 2-5 had NO OPERAND. Ledger AGREES. Core 68.40% in band. Breaker INACTIVE 0/3, cap 0/3.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.57
satellite_pct: 0.0
cash_pct: 31.43
open_thesis_ids: none
```

---
## Where things stand (2026-11-24, **OFFICIAL CLOSE — VOO 660.67, `is_open: false`**)

- **Equity $95,436.93 · day −$330.81 / −0.3454% · since inception −$4,563.07 / −4.5631%** ($100,000
  opening). Core mv **$65,436.93**, unrealized **−$4,563.06 / −6.5187%**, cash **$30,000.00**.
  VOO **−0.5030%** on the session (664.01 → 660.67) on 203,969 shares, a quarter below Monday's
  heavy 280,106. **Built from official `bars` closes on one adjustment basis, not `current_price`.**
- ⚠⚠ **STEP 2 — THE HIGH-WATER MARKS — HAD NO OPERAND, AND THAT IS NOT THE SAME AS "DONE".**
  Zero satellite positions (`grep -ci 'status: *open'` → **0**; `positions` returns one row, VOO
  99.046311231 sh @ 706.74, the §2 core, §5-exempt). **No `highest_close` field exists, so nothing
  was updated and no `(as of …)` date was stamped. NO BACKFILL IS OWED to tomorrow's midday seat** —
  there is no date for it to find stale. §5.4's staleness detector and `bars` backfill branch remain
  **unexecuted code**; the first satellite position will be their first live test.
- ⚠⚠ **CORE −6.5187% IS NOT A §5 EVENT.** §5 exempts core outright, §2 says core is not sold on
  news. Repeated every run because the magnitude sits past the §5.3 −7% *figure* and a fresh-clone
  seat reading only the P&L line is exactly the failure mode this warning exists for.
- **§2 band: in band, no rebalance due tomorrow.** Core **68.5656%** · satellite **0.0000%** · cash
  **31.4344%** · `core_in_band: true` · `rebalance_needed: false`. Thresholds re-solved, not copied:
  **65% floor at VOO 562.51** (−14.86%), **75% ceiling at 908.67** (+37.54%). `rebalance_delta`
  **$1,368.92** is the distance to the 70% *target*, **not a breach of the band**, and §2 rebalances
  on the band. §2 rebalancing is **routine 2's job**, not this seat's.
- **Nothing in limbo (§7):** `orders --status all` → exactly one row in the whole account history,
  the 2026-09-03 VOO core bootstrap, terminal. No order from today exists to resolve or carry.
- **Housekeeping clean.** `week_anchor(2026-11-24)` → **2026-11-23** (imported from `common.py`) =
  inherited `week_of`; no reset due, §6 cap stays **0 of 3**. `consecutive_closed_losses` **0** —
  nothing has ever closed, so there is no streak, the breaker is correctly **INACTIVE** and **no §6
  alert was owed.** `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md` Notes **(none)**
  · `alerts.md` **no open and no SYSTEMIC incidents** · `open_thesis_ids: none`.
- **Five theses pre-market, five rejected** (`T-2026-11-24-01` … `-05`): `-01`/`-02` on part 1
  (mechanism), `-03`/`-04` on part 2 (materiality), `-05` a sweep of eleven. **No `move` call was
  owed** — §4 orders the thesis parts ahead of the hard filters and nothing reached the priced-in
  test. **85th consecutive session with an empty satellite sleeve.**
- 🛠 **THIS SEAT CORRECTED THE 2026-11-20 JOURNAL ENTRY — see carry-forward item 4.** Its restamp
  never landed; it had been sitting on an intraday midpoint for two sessions, understating Friday's
  loss by 0.2623pp. **Corrected by appended table, not substitution.** Escalated to the human.
- ⚠ **This seat fired 15:15 for a 16:15 slot (~45 min early, ~14th consecutive).** Per `control.md`
  manual "Run now" invocations are indistinguishable from scheduled ones in run logs, so this is
  **recorded, not diagnosed as a schedule fault.** The mitigation worked: polled `clock` to the
  post-bell signature (**`is_open: false` with BOTH `next_open` and `next_close` on 2026-11-25** —
  the only reading that separates post-bell from pre-market), settled 5 min, took one `bars` call.
- ⚠⚠ **THURSDAY 2026-11-26 IS THANKSGIVING; FRIDAY 2026-11-27 IS AN EARLY CLOSE.** Tomorrow is an
  ordinary full session (`next_open`/`next_close` both 2026-11-25, confirmed post-bell here). ⚠ **The
  Thursday/Friday calendar is INHERITED and was NOT verified against the broker from this seat** —
  check it on the day, and do not read Thursday's `is_open: false` as the pre-market signature.
  **Read the DATES, not the boolean: FALSE has three meanings, TRUE has one.**

## What this run did

Read the memory files, confirmed the ledger empty against the broker, **held 50 minutes for the
bell**, restamped the day on the official close, wrote `journal.md`, posted the ClickUp summary
(`86bd6nt1p`), and — the one thing not on the checklist — **noticed that the 2026-11-20 entry was
still flagged PARTIAL, verified against `git log` that its restamp never landed, recovered its
price leg from `bars`, and corrected it.**

The temptation this seat had to resist was not trading (it may not) but **reporting the invisible
job as done.** The prompt says the high-water marks matter more than the summary; the honest answer
is that they were **not updated because there was nothing to update**, and writing "marks updated ✓"
would have been the one instruction satisfiable on paper while delivering nothing.

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
   DEMONSTRATION.** Routine 4: 15:15 for a 16:15 slot, **~14 consecutive times (11-24 included).**
   ⚠ **11-24 measured the cost of NOT holding and it was larger than 11-23's reading:** partial
   15:20 equity $95,288.36 / day −0.5006% vs official close $95,436.93 / **−0.3454%** — low by
   $148.57, **0.1552pp**, which would have overstated the day's loss by ~45%. 11-23's was 0.087pp.
   **Two readings say the partial error is unpredictable in size, not reliably small** — the case
   for the hold is the variance, not any day's payoff. Do not read 11-23's small number as licence
   to skip it. Routine 2: 08:36 for
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
4. ⚠⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` — AND SOMETHING MUST CHECK THAT THE
   WINDOW EVER CLOSED. THIS HAS NOW FAILED TWICE.** The scoping error cost 2026-11-13, whose
   journal entry and ClickUp summary do not exist and never will. 🛠 **AND ON 2026-11-24 THIS SEAT
   FOUND THE SECOND INSTANCE: the 2026-11-20 close run died between its insurance commit
   (`baf87a2`) and its restamp — there is no second close commit for 11-20.** Its journal entry sat
   on a 637.53 intraday "midpoint" for two sessions, recording equity $93,144.99 and day −2.1354%
   when the official close (VOO 635.01) gives **$92,895.40 / −2.3977% / inception −7.1046% / core
   unrealized −10.1494%** — **a loss understated by 0.2623pp, i.e. erring in the flattering
   direction.** The price leg is now recovered and **appended as a correction table rather than
   substituted**, so the evidence that the restamp failed survives. ⚠ **No ClickUp summary exists
   for 2026-11-20 and none can be reconstructed.** ⚠⚠ **NEITHER THE 11-23 CLOSE SEAT NOR THE FRIDAY
   REVIEW CAUGHT IT** — the review held for its own bell and used its own official close while
   leaving that entry partial, so **"a later run will notice" is not a working safety net.** Two
   fixes, both the human's call: (i) every routine greps `journal.md` for an unresolved `PARTIAL`
   marker in Step 1 and resolves it before its own work; (ii) make it a real alert key
   (`unresolved-partial`) so it surfaces in ClickUp instead of only inside a 172 KB file. **Any run
   or review that quoted 11-20 from the journal before 11-24 has the wrong numbers.**
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 16
   distinct sessions, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.** ⚠ **11-24 re-measured post-bell: `bars` 660.67 vs
   `current_price` 659.93 = 0.74 / 0.1121%**, wider than 11-23's 0.0843% — a 17th instance. ⚠ Not re-measured today: no `bars` call was owed and one must not
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
   `positions.md` **378,179 B** · `research_log.md` **345,256 B** · `journal.md` **171,776 B** —
   **~1.31 MB of markdown documenting ZERO satellite trades.** ⚠ **11-24 grew `journal.md` by
   ~13.4 KB and that growth is defended, not apologised for:** ~9.5 KB is the day's entry and
   ~3.9 KB is the 11-20 correction table, which is the single most useful block in the file. `positions.md` is excluded from
   monthly rollover on the premise that it "only holds open positions," which has been false for
   all 85 absent dates, **so no run has standing to truncate it.** The one lever a run *does* have
   is to stop feeding it — 11-24 added **0 B to `positions.md`** (no operand, nothing to record).
   ⚠ **SELF-CAUGHT: this seat's first draft of this very line claimed it "kept `state.md` flat".
   It did not — 11,654 B → ~15.0 KB, roughly +3.3 KB** (inexact by construction: writing the
   figure changes it, per the last line of this item). Measured with `wc -c` after the write, which is what
   falsified the claim; the growth is carry-forward item 4's second occurrence and is defended, but
   **the claim was written from intent before measurement.** That is the defect this corpus logs
   most often — and the 11-20 midday seat made the identical error in the identical line. Corrected
   in place rather than left beside its correction. ⚠ The `state.md` figure is the one number that cannot be exact, because writing it changes it.
