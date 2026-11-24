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
last_run: 2026-11-24 09:32 ET 2-market-open-execution — selftest 5/5 exit 0. Fired 08:36 for a 09:35 slot; polled clock 28 min to is_open=true and executed AFTER the bell. Plan dated today, staleness gate PASSED, zero intents — 0 buys, 0 sells. Ledger AGREES (0 satellite blocks vs 1 Alpaca row, VOO core). Steps 3/4/5/6 had no operand. Core 68.39% live, in band, no rebalance. Breaker INACTIVE 0/3, cap 0/3.
prior_run: 2026-11-24 07:02 ET 1-premarket-research — 5 theses, 0 accepted; plan_today.md dated 2026-11-24 with ZERO intents; core 68.51% in band.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.39
satellite_pct: 0.0
cash_pct: 31.61
open_thesis_ids: none
```

---
## Where things stand (2026-11-24, **LIVE POST-OPEN MARK — VOO 655.305 at 09:31, `is_open: true`**)

- **Nothing was executed and nothing should have been.** `plan_today.md` carried `plan_date:
  2026-11-24` — **today** — so the Step 2 staleness gate **passed**, and the instruction set it
  guards was **empty**. ⚠ **An empty plan that passed the gate is not a stale plan that was
  blocked**, and it is not licence to improvise: §4 routes every buy through the pre-market seat,
  so a candidate found at the open belongs in tomorrow's plan.
- **Satellite sleeve empty, 85th consecutive session** (same session as this morning's count — not
  incremented). `positions.md` `grep -ci 'status: *open'` → **0**; `positions` returns **one** row,
  VOO 99.046311231 sh @ 706.74, the §2 core, **§5-exempt, struck from the working list, not
  cleared.** **Ledger and broker agree; there was no disagreement to reconcile.**
- **§5.1–§5.4 are ABSENT, NOT PASSING.** No entry price, no `highest_close`, no deadline and no
  invalidation string exists anywhere. **Step 4 had NO OPERAND.** The §5.4 staleness detector and
  backfill branch remain **unexecuted code at 85 absent dates.**
- **§2 band: NO REBALANCE DUE, read LIVE and not inherited.** Core **68.39%** (07:02 pre-market
  read was 68.51%), satellite **0.00%**, cash **31.61%**, `core_in_band: true`,
  `rebalance_needed: false`. Thresholds **re-solved here, not copied**: with cash $30,000 and
  99.046311231 shares the **65% floor breaks at VOO 562.51** (19500 = 0.35 × 99.046311231 × P) and
  the **75% ceiling at 908.67** — **−14.1% / +38.7%** from here. `rebalance_delta: 1528.49` is the
  distance to the 70% *target*, **not a breach of the band**; §2 rebalances on the band.
- **Equity $94,905.05 · core mv $64,905.05 · unrealized −$5,094.45 / −7.278% · cash $30,000.00.**
  ⚠⚠ **CORE −7.278% IS NOT A §5 EVENT, AND IT HAS NOW CROSSED THE §5.3 MAGNITUDE.** §5 exempts
  core outright and §2 says core is not sold on news. Emphasised because the number is now past
  the 7% hard-stop *figure*, and a fresh-clone seat reading only the P&L line is exactly the
  failure mode this warning exists for.
- ⚠ **ENDPOINT DISAGREEMENT — RE-CONFIRMED, NOT A NEW INSTANCE.** `lastday_price` **663.91** vs
  official `bars` close **664.01** for 11-23 = **0.10 / 0.0151%**, narrowest of the recorded
  0.04–1.41 spread. **Still the 16th instance:** same session the 07:02 seat logged it in, and the
  convention counts sessions, not reads. Figures built from official `bars` only.
- **Week rollover: none due, re-derived.** `week_anchor(2026-11-24)` → **2026-11-23** (imported
  from `common.py`) = inherited `week_of`. `new_positions_this_week` stays **0 of 3**.
- **Breaker correctly INACTIVE 0/3** — nothing has ever closed, so there is no streak and no §6
  alert was owed. `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md` Notes
  **(none)** · `alerts.md` **no open and no SYSTEMIC incidents**. All five of today's thesis IDs
  (`T-2026-11-24-01`…`-05`) are present in `research_log.md`, checked though no buy needed one.
- ⚠⚠ **THURSDAY 2026-11-26 IS THANKSGIVING; FRIDAY 2026-11-27 IS AN EARLY CLOSE.** Tomorrow is an
  ordinary full session. Do not plan a Thursday execution, and do not read Thursday's
  `is_open: false` as the pre-market signature — **check the `next_open` date.**

## What this run did

Executed an empty plan correctly, and **waited for the bell to do it.** The run fired at **08:36
for a 09:35 slot**, so the first decision was what `is_open: false` meant: **both** `next_open`
and `next_close` carried **today's** date — the pre-market signature, **not** the closed-market
one — so Step 1's "market closed → log the skip and exit" branch **did not apply.** This seat
polled `clock` every 2 min for **28 minutes** to `is_open: true` (`next_open` rolled to
**2026-11-25**) and read the §2 band **after** the open.

⚠ **That matters more than today's zero.** With no intents, waiting changed no action — the band
verdict is robust across −14.1% in VOO. **On a day carrying intents it changes everything:**
exiting on "market closed" at 08:36 would silently skip the day's whole execution while the gate
reported a pass. Carry-forward item 3 held that waiting for the OPEN was **not cleared** at
routine 2. **It is now demonstrated once** — one instance, logged as evidence, not a solved defect.

⚠ **Byte accounting, measured with `wc -c` after the write, not claimed from intent:**
`state.md` **11,332 → 12,069 B (+737)** · `positions.md` **376,615 → 377,211 B (+596)**, a
six-line reconciliation block, no digest. `research_log.md` and `trade_log.md` **untouched —
correctly:** no intent was skipped, so no §4 skip was owed, and no order reached a terminal state,
so no trade entry was owed. **An append to either would have been a fabrication.**
⚠⚠ **TWO FALSE CLAIMS BY THIS SEAT, CAUGHT BY MEASURING AND CORRECTED BEFORE THE COMMIT, LOGGED
BECAUSE THE CORRECTION IS THE DATA:** an earlier draft of this file claimed a **3.7 KB cut** and
measured **12,165 B — it had GROWN**; and the first version of this paragraph said `positions.md`
**“+1 line”** when the append was **six lines / +596 B**. Carry-forward item 9 has logged five
consecutive seats claiming a cut while the corpus grew. **This seat did not beat that pattern — it
only measured itself and published the real numbers.**

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
   the boolean: FALSE has three meanings, TRUE has one.**
4. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`.** That scoping error cost 2026-11-13,
   whose journal entry and ClickUp summary do not exist and never will.
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 16
   distinct sessions, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.**
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
   `positions.md` **376,615 B** · `research_log.md` **345,256 B** · `journal.md` **158,415 B** —
   **~1.3 MB of markdown documenting ZERO satellite trades.** `positions.md` is excluded from
   monthly rollover on the premise that it "only holds open positions," which has been false for
   all 85 days, **so no run has standing to truncate it.** The one lever a run *does* have is to
   stop feeding it. ⚠ The `state.md` figure is the one number that cannot be exact, because
   writing it changes it.
