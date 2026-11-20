# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** The 2026-11-13 review compacted this file from 324KB /
2,988 lines after its `last_run` value had grown into a multi-thousand-byte paragraph. **Five
sessions later it had regrown to 39KB** (measured from git: 5,052 B → 39,424 B, ×7.8), so this
review has compacted it again. **A value that needs a paragraph belongs in `journal.md`.** See
`weekly_review.md` 2026-11-20, Recurring Error 8.

```
last_run: 2026-11-20 16:05 ET 5-friday-weekly-review — selftest 5/5 exit 0. HELD FOR THE BELL: official close 635.01 basis (first review in the series not written on a partial bar). Weekly counters advanced.
prior_run: 2026-11-20 15:15 ET 4-market-close-journal — insurance pass, partial basis; its post-bell commit landed and the 2026-11-20 journal entry exists.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 67.71
satellite_pct: 0.0
cash_pct: 32.29
open_thesis_ids: none
```

---

## Where things stand (2026-11-20, **official close basis**)

- **Equity $92,895.40** on the official close · core VOO 99.046311231 sh @ 706.74, close
  **635.01**, market value **$62,895.40**, unrealized **−$7,104.59 / −10.149%** · **cash exactly
  $30,000.00**.
  ⚠ The broker reported `equity` **93,035.05** at 16:05 off `current_price` **636.42**, which
  disagrees with the official `bars` close by **1.41/share**. **Figures here are built from
  official `bars` closes only** — the standing rule, and what makes the choice reproducible.
- **Sleeves: core 67.71% / satellite 0.00% / cash 32.29%.** `core_in_band: true`,
  `rebalance_needed: false`. Floor headroom **2.71pp**; the 65% floor breaks at VOO **562.51**
  (a further −11.4%) — **computed, not assumed.** A rebalance is routine 2's order in any case.
- **Satellite sleeve is empty and always has been.** Zero positions, zero orders ever.
  `orders --status all` returns exactly one order in the account's whole history: the
  2026-09-03 VOO core bootstrap. Nothing is in limbo.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists anywhere. ⚠⚠ **Core VOO is EXEMPT from §5; its −10.149% is NOT a
  §5.3 reading and NOT a §5.4 reading**, though it is now past both thresholds in magnitude.
  That is a rule, not a judgment call. **The §5 machinery remains unproven code.**
- **293 theses written, 0 ever accepted** (87 + 129 archived, 77 live in `research_log.md`;
  re-derived this run from `^### T-` header *lines*, 294 lines less the file's own template).
- Breaker INACTIVE 0/3 · weekly cap 0/3 used · `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none`
  · `alerts.md` has no open and no systemic incidents.
- VOO closed **7 of 8 sessions down**; the index is **11.35% below its 2026-10-06 peak of 716.29**.

## Note on `week_of`

Set to **2026-11-23** (next Monday) per routine 5 Step 6. ⚠ `week_anchor()` returns
**2026-11-16** for Fri 11-20 and for Sat/Sun 11-21–22, so **a run firing over the weekend will
see a mismatch and reset `week_of` back to 2026-11-16.** **That is harmless** —
`new_positions_this_week` is 0 under either anchor and the §6 cap cannot be stuck — but do not
read it as a corrupted counter. From Mon 11-23 the anchor and this value agree.

## Carry forward

1. ⚠⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** **9 of 10 routine-2
   seats visible in this clone fired pre-bell** (08:38–08:41 ET, ~50 min before the open); the
   lone exception was 2026-11-13 at 10:47, and **2026-11-16 did not fire at all.** This week:
   five sessions, **zero on which an order could lawfully have been placed.** Re-send **only** if
   routine 2 begins firing *after* the bell in a way that changes what the human must fix.
   **Recorded, not diagnosed** per `control.md`.
   ⚠⚠ **THE STANDING COST: the only seat licensed to open a position has been unable to act for
   essentially this clone's whole history, AND THE DAMAGE TO DATE IS STILL ZERO** — every
   `plan_today.md` in the window carried zero intents, because research accepted nothing. **The two
   defects have been masking each other: an empty funnel feeding a shut door. Fix either one and
   the other becomes binding immediately.**
   ⚠⚠⚠ **THE UNRESOLVED RULE QUESTION, RAISED NOT RESOLVED.** Routine 2's prompt says that if the
   market is closed, log the skip and exit. Read literally, **a pre-bell seat holding a live BUY or
   a mandatory §5 exit must discard it.** The two fixes — hold ~50 min for the open, or fix the
   schedule — are **the human's to choose; a run must not grant itself the first.**
   ⚠ **Routines 3, 4 and 5 are DIFFERENT, MILDER cases and must not be folded in:** an early
   midday seat still lands inside the session; a close seat can hold for the bell; and **this
   review proved a review seat can too** (see item 3).
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`** — that scoping error is what cost
   2026-11-13, whose journal entry and ClickUp summary do not exist and never will. 11-16 → 11-20
   all did it correctly. **Applies to routine 4, not to this one.**
3. ✅⚠ **HOLD FOR THE BELL. IT IS NINETEEN MINUTES AND IT PAID BY THE WIDEST MARGIN YET RECORDED.**
   This review fired 15:46 against a stated 16:45, polled `clock` to the post-bell signature
   (`is_open: false` with **both** `next_open` and `next_close` on the *next* session — the only
   reading that separates post-bell from pre-market), then let the bar settle 5 minutes.
   **The 15:46 partial read 637.30; the official close was 635.01 — the partial was HIGH by 2.29 /
   +0.361%**, which would have put every VOO figure ~0.36pp out and equity ~$227 out. **Ten prior
   reviews published a basis caveat instead of waiting. This one has no caveat.**
4. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
   A fresh-clone seat has seen one day and will mistake it for the record.
5. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** Today:
   `positions.current_price` **636.42** vs official `bars` **635.01** = **1.41/share**, the widest
   recorded (priors 0.04–0.42). **Read at 16:05:32 post-bell, so it may carry an extended-hours
   print — recorded with that caveat.** **Build P&L and stamp `highest_close` from official `bars`
   closes only, one adjustment basis, one call.**
6. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** Both re-derived 2026-11-20,
   not inherited; both reproduced.
   (i) **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** — it is byte-identical to
   the unadjusted series on **259 of 260** sessions across all four ex-dates. Reconstruct by
   reinvesting at the ex-date close: 2025-12-22 $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 ·
   2026-09-28 $1.8226 (TTM $7.43, verified against ten sources; **none since 09-28**). Following
   Step 1 literally understates the 12-month benchmark by **1.25pp**.
   (ii) **THE PAPER BROKER NEVER CREDITS DISTRIBUTIONS** — `cash` is exactly `30000`, not
   $30,180.52. The 2026-09-28 distribution ($1.8226 × 99.0463 = **$180.52**) was never paid, so the
   core sleeve is structurally short ~1.07%/yr against any honest total-return benchmark, widening
   every quarter. ⚠⚠ **The two defects roughly cancel, which is why ten reviews caught neither.**
7. ⚠ **THIS CLONE IS SHALLOW — 100 commits, earliest 2026-11-09.** Any run citing git history
   beyond ~11 days is citing something it cannot see. `state.md` carried "15 pre-bell firings since
   11-02"; that is consistent with but **not verifiable** here, and was not repeated as measured.
8. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING.** Measured from git at the 11-13 review
   (`9dfa6fc`) to today: `state.md` 5,052 → 39,424 B · `positions.md` 302,248 → 367,528 B (**+65KB
   describing an EMPTY ledger**) · `research_log.md` 189,849 → 308,066 B · `journal.md` 93,942 →
   148,739 B. **+272,666 B in five sessions, ~54 KB/session.** The corpus total only *fell* this
   week because last week's one-time `state.md` compaction saved ~319 KB. **`positions.md` is
   excluded from Step 6 rollover on the premise that it "only holds open positions" — false for 78
   days — so no run has standing to truncate it. The human must set a retention rule.**
