# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** The 2026-11-13 review compacted this file from 324KB /
2,988 lines after its `last_run` value had grown into a multi-thousand-byte paragraph; five
sessions later it had regrown ×7.8 and the 2026-11-20 review compacted it again. **A value that
needs a paragraph belongs in `journal.md`.** See `weekly_review.md` 2026-11-20, Recurring Error 8.

```
last_run: 2026-11-23 15:18 ET 4-market-close-journal — INSURANCE WRITE, pre-bell (is_open true, 42 min early). Selftest 5/5 exit 0. Zero satellite positions: Step 2 high-water update had NO OPERAND, no mark updated because none exists. Holding for the bell to restamp on the official close. Core 68.72% in band, no rebalance. Breaker INACTIVE 0/3. 6 theses, 0 accepted.
prior_run: 2026-11-23 11:41 ET 3-midday-management — market OPEN, zero satellite positions, §5.1-5.4 no operand, no exit owed, nothing placed.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.72
satellite_pct: 0.0
cash_pct: 31.28
open_thesis_ids: none
```

---
## Where things stand (2026-11-23, **PRE-BELL INSURANCE MARK — restamped on the official close below if the hold completed**)

- **Satellite sleeve is empty, 84th consecutive session.** `positions.md` `grep -ci 'status: *open'`
  → **0**; `alpaca.py positions` returns **one** row, VOO 99.046311231 sh @ 706.74 — the §2 core,
  **§5-exempt, struck from the working list, not cleared.**
- **§5.1–§5.4 are ABSENT, NOT PASSING.** No entry price, no `highest_close`, no deadline, no
  invalidation string exists anywhere. **Step 2 therefore had NO OPERAND: no mark was updated
  because none exists, and no `(as of …)` date exists to be found stale.** ⚠ Tomorrow's midday seat
  must not read this as a current high-water stamp. **The §5.4 staleness detector and backfill
  branch remain unexecuted code at 84 absent dates.**
- **Nothing in limbo.** `orders --status all` → one row, the 2026-09-03 core bootstrap, terminal.
  `orders --status open` → `[]`. No §7 exposure overnight.
- **§2 band: no rebalance due.** Core **68.72%** on the 15:16 mark (VOO 665.37), satellite 0.0%,
  cash 31.28%, `core_in_band: true`. Thresholds solved, not assumed: with cash at $30,000 and
  99.046311231 shares the **65% floor breaks at VOO 562.51**, the **75% ceiling at 908.67**.
- ⚠⚠ **CORE VOO +4.69% INTRADAY IS NOT A §5 EVENT IN EITHER DIRECTION.** 665.37 vs Friday's
  `lastday_price` 635.54; unrealized **−$4,097.55 / −5.854%** on the $69,999.99 basis, improved from
  Friday's −10.1% close basis. §5 exempts core. Restated because the magnitude has recently sat past
  both thresholds and a fresh-clone seat reading only the P&L line could mistake it for a trigger.
- **Week rollover: none due, re-derived.** `week_anchor(2026-11-23)` → 2026-11-23 (imported from
  `common.py`) = inherited `week_of`. `new_positions_this_week` stays **0**.
- **Breaker correctly INACTIVE 0/3** — nothing has ever closed, so there is no streak to confirm and
  no §6 alert was owed. Weekly cap 0/3 · `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` ·
  `alerts.md` has no open and no systemic incidents.
- **299 unique thesis IDs, 0 ever accepted in 84 days.** Today: 6 written, 6 rejected
  (`T-2026-11-23-01`…`-06`), every one dying on part 1 or part 3, both of which precede the hard
  filters — **so no `move` call was owed or spent.**

## What this run did

Journaled a day with no trade, no position and no rule event, and **recorded the high-water
non-update as an absence rather than ticking it as done.** The one judgment that mattered was
procedural: the seat fired at **15:15 with the market open**, so it wrote this insurance commit and
**held for the bell** rather than publishing an intraday print as the close.

⚠ **This seat shortened `state.md` instead of growing it** (14,123 B → this). Carry-forward item 9
has recorded every seat since 11-13 writing "added the least it could" while the file grew anyway;
the only way to stop reporting that is to not do it.

## Carry forward

1. ⚠⚠⚠ **THE FUNNEL MAY BE UNSATISFIABLE BY CONSTRUCTION — THE HUMAN'S CALL, AND STILL THE MOST
   IMPORTANT THING IN THIS FILE.** The sweep doing most of the killing asks whether a **news source
   has already named** the second-order company and segment. **§4 demands no such thing** — it asks
   the *agent* to write an honest, sourceable mechanism. Requiring the *source* to have done the
   second-order reasoning restricts the funnel to links the market has already been told about,
   **which is exactly the set §4's priced-in filter then kills.** The two gates together are close
   to unsatisfiable. **RAISED, NOT ACTED ON: no seat may grant itself this fix** — a run that
   diagnosed its own filter as too strict and relaxed it is the failure mode, not the remedy.
2. ⚠⚠ **NEW, AND IT NEIGHBOURS ITEM 1: THE FUNNEL IS PARTLY RECIRCULATING.** `T-2026-11-23-04`
   (Venture Global / China Gas) was rejected today on its **fifth** appearance, on the same
   unchanged part-3 test; `-02` (BIS chip rule) on its **third in five sessions**, each time because
   the only measurable direction is negative in a long-only strategy. Re-researching objects four
   prior seats killed on structural tests consumes the drill budget the 299→0 problem needs spent
   elsewhere. **A disposed-objects list the pre-market seat checks before spending a query would end
   it — but defining "disposed" is a calibration change, so it is the human's, not a run's.**
3. ⚠⚠ **ROUTINE 4 FIRED ~60 MIN EARLY (15:15 for a 16:15 slot) AND THIS IS THE ~13th CONSECUTIVE
   TIME.** The digests in `positions.md` record 15:15/15:16 firings running back many sessions, with
   one 16:17 outlier. ⚠ **RECORDED, NOT DIAGNOSED** — `control.md` states that manual "Run now"
   invocations are indistinguishable from scheduled ones in run logs, so a run may not call this a
   schedule fault. **The consequence is what matters and it is specific to this routine:** routine
   4's primary job is recording *closing* prices, so firing before the bell attacks the one thing it
   exists to do. **Mitigation that has now worked every time it was used: poll `clock` to the
   post-bell signature** (`is_open: false` with **both** `next_open` and `next_close` on the *next*
   session — the only reading separating post-bell from pre-market), wait ~5 min, then read `bars`.
   ⚠ Do not fold this into routine 2's separate pre-bell problem; and **waiting for the OPEN is a
   different act that is NOT cleared.**
4. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`.** That scoping error is what cost
   2026-11-13, whose journal entry and ClickUp summary do not exist and never will. **This seat
   included it.**
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 14+
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
   HUMAN.** `positions.md` **373,588 B** · `weekly_review.md` **415,188 B** · `research_log.md`
   **324,382 B** · `journal.md` ~**154 KB** — **~1.27 MB of markdown documenting zero satellite
   trades.** `positions.md` is excluded from rollover on the premise that it "only holds open
   positions," which has been false for all 84 days, **so no run has standing to truncate it.**
