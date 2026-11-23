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
last_run: 2026-11-23 07:01 ET 1-premarket-research — selftest 5/5 exit 0. Six theses written, six rejected; plan dated 2026-11-23 carries zero intents. Ledger agrees. No rebalance due.
prior_run: 2026-11-20 16:05 ET 5-friday-weekly-review — held for the bell, official 635.01 close basis, weekly counters advanced.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.29
satellite_pct: 0.0
cash_pct: 31.71
open_thesis_ids: none
```

---

## Where things stand (2026-11-23 07:01 ET, **PRE-MARKET MARK — not a close**)

- **Equity $94,598.00** · core VOO 99.046311231 sh @ 706.74, market value **$64,598.00**,
  unrealized **−$5,401.99 / −7.717%** · cash exactly **$30,000.00**.
  ⚠⚠ **Read off `current_price` 652.20, a PRE-MARKET PRINT (+2.70% on Friday's official `bars`
  close of 635.01).** These figures will move before the bell. The next seat with a finished bar
  should restate them; **do not treat them as a close.**
- **Sleeves: core 68.29% / satellite 0.00% / cash 31.71%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 1620.60`. **The band verdict is robust to the
  pre-market basis** — core reads 68.29% pre-market and 67.71% on Friday's close, both well inside
  65–75%. The 65% floor breaks at VOO **562.51**, a further **−13.7%** — solved, not assumed
  (19500 = 0.35 × 99.046311231 × P).
- **Satellite sleeve is empty and always has been.** Zero positions, zero satellite orders ever.
  The account's entire order history is the 2026-09-03 VOO core bootstrap. Nothing is in limbo.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists anywhere. ⚠⚠ **Core VOO is EXEMPT from §5; its −7.717% is NOT a §5.3
  reading and its drawdown is NOT a §5.4 reading.** That is a rule, not a judgment call.
  **The §5 machinery remains unproven code, 81 days old and never once run against a position.**
- **299 theses written, 0 ever accepted in 81 days** — **re-derived at this seat, not inherited**:
  `^### T-` header lines give 84 live in `research_log.md` less its own template = **83**, plus **87**
  archived 2026-09 and **129** archived 2026-10. 293 inherited + six today reconciles to the same 299.
- Breaker INACTIVE 0/3 · weekly cap 0/3 used · `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none`
  · `alerts.md` has no open and no systemic incidents.
- **Week rollover: no reset due.** `week_anchor(2026-11-23)` → **2026-11-23** = inherited
  `week_of`. The 11-20 review's weekend-anchor hazard **did not materialise** — no run fired over
  the weekend. From today the anchor and this value agree.
- ⚠ **Endpoint disagreement, 14th distinct instance:** `positions.lastday_price` **635.54** vs
  official `bars` **635.01** for 2026-11-20 = **0.53 / 0.0835%** (recorded range 0.04–1.41).

## Carry forward

1. ⚠⚠⚠ **NEW, AND THIS SEAT THINKS IT IS THE MOST IMPORTANT THING IN THIS FILE — FOR THE HUMAN.
   THE FUNNEL MAY BE UNSATISFIABLE BY CONSTRUCTION, AND THAT IS A BETTER EXPLANATION OF 299→0 THAN
   "OPPORTUNITIES ARE RARE."** The sweep that has done most of the recent killing asks whether a
   **news source has already named** the second-order company and its segment. **§4 demands no such
   thing** — it asks the *agent* to write a mechanism, dollar path, timing and invalidation that are
   honest and sourceable. Requiring the *source* to have done the second-order reasoning restricts
   the funnel to links the market has already been told about, **which is precisely the set §4's own
   priced-in filter then kills.** The two gates in combination are close to unsatisfiable.
   ⚠⚠ **RAISED, NOT ACTED ON, AND NO SEAT MAY GRANT ITSELF THE FIX.** Loosening the sourcing
   standard is exactly what §4's honest-broker rule exists to prevent, and a run that diagnosed its
   own filter as too strict and then relaxed it would be the failure mode rather than the remedy.
   **Both readings fit the evidence and a seat inside the loop cannot distinguish them. The
   calibration is the human's to set.** Distinct from, and sharper than, the standing taxonomy ask.
2. ⚠⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** Nine of ten recorded
   routine-2 seats fired pre-bell (~08:35–08:41, ~50 min early); 2026-11-13 at 10:47 was the lone
   exception and 2026-11-16 did not fire at all. Re-send **only** if routine 2 begins firing *after*
   the bell in a way that changes what the human must fix. **Recorded, not diagnosed**, per
   `control.md`.
   ⚠⚠ **THE STANDING COST, AND IT IS STILL ZERO:** the only seat licensed to open a position has
   been unable to act for essentially this clone's history, **and every `plan_today.md` in the
   window carried zero intents.** The two defects mask each other — an empty funnel feeding a shut
   door. **Fix either and the other becomes binding immediately**, which is why item 1 matters now.
   ⚠⚠⚠ **THE UNRESOLVED RULE QUESTION, RAISED NOT RESOLVED.** Routine 2's prompt says that if the
   market is closed, log the skip and exit. Read literally, **a pre-bell seat holding a live BUY or
   a mandatory §5 exit must discard it.** The two fixes — hold ~50 min for the open, or fix the
   schedule — are **the human's to choose; a run must not grant itself the first.**
   ⚠ Routines 3, 4 and 5 are **different, milder cases and must not be folded in.**
3. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`** — that scoping error is what cost
   2026-11-13, whose journal entry and ClickUp summary do not exist and never will. **Applies to
   routine 4, not to this one.**
4. ✅ **HOLD FOR THE BELL. IT HAS PAID EVERY TIME IT WAS USED.** The 11-20 review polled `clock` to
   the post-bell signature (`is_open: false` with **both** `next_open` and `next_close` on the
   *next* session — the only reading that separates post-bell from pre-market), waited 5 minutes,
   and got the official close: its 15:46 partial read 637.30 against an official 635.01, **high by
   2.29 / +0.361%.** Ten prior reviews published a basis caveat instead of waiting.
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.**
   14 distinct instances, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.**
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** Both re-derived 2026-11-20.
   (i) **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** — byte-identical to the
   unadjusted series on 259 of 260 sessions across all four ex-dates. Reconstruct by reinvesting at
   the ex-date close: 2025-12-22 $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28
   $1.8226 (TTM $7.43; **none since 09-28**). Following Step 1 literally understates the 12-month
   benchmark by **1.25pp**.
   (ii) **THE PAPER BROKER NEVER CREDITS DISTRIBUTIONS** — `cash` is exactly `30000`, not
   $30,180.52. The core sleeve is structurally short ~1.07%/yr against any honest total-return
   benchmark, widening every quarter. ⚠⚠ **The two defects roughly cancel, which is why ten reviews
   caught neither.**
8. ⚠ **THIS CLONE IS SHALLOW.** Any run citing git history beyond ~2 weeks is citing something it
   cannot see. Do not repeat inherited history claims as measured.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING.** `positions.md` was **367,528 B** when
   this seat read it (`wc -c`, not inherited) — **describing a ledger that has been empty for all 81
   days of this account's history.** It is excluded from Step 6 rollover on the premise that it "only holds open positions,"
   which has been false the whole time, **so no run has standing to truncate it. The human must set
   a retention rule.** This seat added a header and a reconciliation note and nothing else.
