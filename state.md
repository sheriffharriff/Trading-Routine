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
last_run: 2026-11-24 07:02 ET 1-premarket-research — selftest 5/5 exit 0. Not a holiday. Ledger reconciled, AGREES (0 satellite blocks vs 1 Alpaca row, VOO core). Step 4 no operand. 5 theses, 0 accepted; plan_today.md dated 2026-11-24 with ZERO intents. Core 68.51% in band, no rebalance. Breaker INACTIVE 0/3, cap 0/3. Did NOT run the disputed source-must-name-it sweep; the one strong object (DRC cobalt ban) died on §4 part 2 materiality instead.
prior_run: 2026-11-23 16:06 ET 4-market-close-journal — equity 95767.74 close basis, day +3.092%, core 68.67%, 6 theses 0 accepted, journal + ClickUp done.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.51
satellite_pct: 0.0
cash_pct: 31.49
open_thesis_ids: none
```

---
## Where things stand (2026-11-24, **PRE-MARKET MARK — `current_price` VOO 658.84 at 07:02, −0.78% on the 664.01 official close**)

- **Satellite sleeve is empty, 85th consecutive session.** `positions.md`
  `grep -ci 'status: *open'` → **0**; `alpaca.py positions` returns **one** row, VOO 99.046311231 sh
  @ 706.74 — the §2 core, **§5-exempt, struck from the working list, not cleared.** **The ledger and
  the broker agree; there was no disagreement to reconcile.**
- **§5.1–§5.4 are ABSENT, NOT PASSING.** No entry price, no `highest_close`, no deadline, no
  invalidation string exists anywhere. **Step 4 had NO OPERAND and Step 6's `sell_rule_status`
  update had nothing to update.** ⚠ Today's midday seat must not read this as a clean §5 pass. The
  §5.4 staleness detector and backfill branch remain **unexecuted code at 85 absent dates.**
- **§2 band: NO REBALANCE DUE.** Core **68.51%** pre-market / **68.67%** on yesterday's official
  close, satellite 0.0%, cash 31.49%, `core_in_band: true`, `rebalance_needed: false`. Thresholds
  solved, not assumed: with cash at $30,000 and 99.046311231 shares the **65% floor breaks at VOO
  562.51** (−14.6% from here), the **75% ceiling at 908.67**. `rebalance_delta: 1423.30` is the
  distance to the 70% *target*, **not a breach of the band** — §2 rebalances on the band.
- **Equity $95,255.67 · core market value $65,255.67 · unrealized −$4,744.32 / −6.778% · cash
  $30,000.00.** ⚠⚠ **CORE −6.778% IS NOT A §5 EVENT IN EITHER DIRECTION.** §5 exempts core and §2
  says core is not sold on news. Restated because the magnitude has recently sat past both the §5.3
  and §5.4 thresholds and a fresh-clone seat reading only the P&L line could mistake it for a
  trigger.
- ⚠ **ENDPOINT DISAGREEMENT, 16th INSTANCE AND THE NARROWEST YET:** `positions.lastday_price`
  **663.91** vs official `bars` close **664.01** for 11-23 = **0.10 / 0.0151%**, against a recorded
  spread of 0.04–1.41. **A new session is a new instance.** Figures built from official `bars` only.
- **Week rollover: none due, re-derived.** `week_anchor(2026-11-24)` → **2026-11-23** (imported from
  `common.py`) = inherited `week_of`. `new_positions_this_week` stays **0 of 3**.
- **Breaker correctly INACTIVE 0/3** — nothing has ever closed, so there is no streak to confirm and
  no §6 alert was owed. `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md` Notes
  **(none)** · `alerts.md` **no open and no SYSTEMIC incidents**.
- **Today: 5 theses written, 0 accepted** (`T-2026-11-24-01`…`-05`). Spend: **five sweeps, two drill
  queries, one `bars` call.** ⚠ **No `move` call was made and that is not a skipped check** — §4
  orders the four parts ahead of the hard filters, and every candidate died on part 1 or part 2.
- ⚠⚠ **THURSDAY 2026-11-26 IS THANKSGIVING; FRIDAY 2026-11-27 IS AN EARLY CLOSE.** Today and
  tomorrow are ordinary full sessions. Do not plan a Thursday execution, and do not read Thursday's
  `is_open: false` as the pre-market signature — **check the `next_open` date.**

## What this run did

Researched five objects and rejected five, then wrote a correctly-dated plan with **zero intents**.
The one judgment that mattered was **what not to run**: carry-forward item 1 holds that the sweep
doing most of the recent killing demands a *news source* have already done the second-order
reasoning, which **§4 does not ask for**. This seat **did not run that sweep.** It took the
second-order step itself — DRC bans cobalt exports → cobalt price → *which §3-eligible company books
cobalt revenue?* — and spent the drill query only to source facts.

**The answer was still no, and it came from §4's own part-2 materiality test:** no US-listed company
above the $10B floor has cobalt anywhere near 10% of revenue (the one cobalt pure-play, ELBM, is
~$35M — 280× below the floor). ⚠ **One session is weak evidence, not a finding**, but it is the
first clean observation on item 1, and it points slightly *against* the disputed gate being the
whole explanation for the 0-of-N record.

⚠ **Byte accounting, measured with `wc -c` after the last write, not claimed from intent:**
`state.md` came in at 11,052 B and goes out at **~11.1 KB — essentially flat, NOT the cut this seat
intended.** Recorded as a miss, because carry-forward item 9 has logged five consecutive seats
claiming they "added the least they could" while the corpus grew anyway. `positions.md` **375,302 → 376,615 B
(+1,313)** — one reconciliation line and **no digest block**, against ~5 KB added by the three 11-23
seats to record the same absence three times. `research_log.md` grew ~20.9 KB, which is the one
growth this seat defends: five theses with their reasoning is the product.

## Carry forward

1. ⚠⚠⚠ **THE FUNNEL MAY BE UNSATISFIABLE BY CONSTRUCTION — STILL THE HUMAN'S CALL, AND NOW WITH ONE
   DATA POINT AGAINST IT.** The disputed sweep asks whether a **news source has already named** the
   second-order company and segment; **§4 demands no such thing**, and requiring it restricts the
   funnel to links the market has already been told about — **exactly the set §4's priced-in filter
   then kills.** ⚠ **TODAY'S RUN OMITTED THAT SWEEP AND STILL FOUND NOTHING**, dying on part 2
   materiality instead. **That is one session and must not be over-read.** The useful next step is to
   keep omitting it and see whether the kill reasons migrate from part 1 to parts 2/3 — a *diagnostic*
   change, not a calibration change. **RAISED, NOT ACTED ON beyond the omission: no seat may relax a
   §4 test, and none was relaxed.**
2. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING — AND TODAY SHOWS BOTH HALVES OF IT.**
   `T-2026-11-24-02` (Capricor CRL) is the **third** "FDA rejection → incumbent benefits" object in
   three weeks; **zero drill queries were spent on it** because the prior entries were read and
   applied. `T-2026-11-24-03` (Applied Digital) is the **sixth-plus** unnamed-hyperscaler object.
   ⚠ **Re-use worked here only because those kills are structural** ("a rejection preserves the
   status quo" is true independent of drug, company and date). **An object whose kill depends on a
   figure that can change still needs re-checking.** A disposed-objects list the pre-market seat
   checks first would help, **but defining "disposed" is a calibration change and so is the
   human's.**
3. ⚠⚠ **ROUTINE 4 FIRES ~60 MIN EARLY (15:15 for a 16:15 slot), ~13 consecutive times.** ⚠
   **RECORDED, NOT DIAGNOSED** — `control.md` states manual "Run now" invocations are
   indistinguishable from scheduled ones in run logs, so no run may call this a schedule fault.
   **The consequence is specific: routine 4's job is recording *closing* prices.** Mitigation that
   has worked every time used: **poll `clock` to the post-bell signature** (`is_open: false` with
   **both** `next_open` and `next_close` on the *next* session), wait ~5 min, then read `bars`.
   ⚠ Routine 2 fires early too (08:36 for 09:35 on 11-23) — a **separate** defect; do not fold them
   together. **Waiting for the OPEN is a different act and is NOT cleared.**
4. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`.** That scoping error cost 2026-11-13, whose
   journal entry and ClickUp summary do not exist and never will.
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 16
   distinct instances, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
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
   HUMAN.** Measured with `wc -c` after this seat's last write: `weekly_review.md` **415,188 B** ·
   `positions.md` **376,615 B** · `research_log.md` **~345 KB** · `journal.md` **158,415 B** —
   **~1.3 MB of markdown documenting ZERO satellite trades.** `positions.md` is excluded from
   monthly rollover on the premise that it "only holds open positions," which has been false for all
   85 days, **so no run has standing to truncate it.** ⚠ The one lever a run *does* have is to stop
   feeding it: this seat wrote **one line instead of a digest block**. ⚠ The `state.md` figure is the
   one number that cannot be exact, because writing it changes it.
