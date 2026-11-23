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
last_run: 2026-11-23 08:36 ET 2-market-open-execution — selftest 5/5 exit 0. Market CLOSED, 54 min pre-bell. Plan was FRESH (plan_date = today) and carried zero intents, so no execution was owed and nothing was lost. No orders placed. Ledger agrees. Core 67.71% on Friday's official close, in band, no rebalance.
prior_run: 2026-11-23 07:01 ET 1-premarket-research — six theses written, six rejected; plan dated 2026-11-23 with zero BUY, zero SELL, zero REBALANCE intents.
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

## Where things stand (2026-11-23 08:36 ET, **PRE-BELL — the sleeve block above is stamped on Friday's OFFICIAL CLOSE**)

- **Sleeve figures in the block are the close basis, not this morning's print**, per carry-forward
  item 6. Friday 2026-11-20 official `bars` close **VOO 635.01** (`n` 5,353, `v` 250,937,
  `--adjustment all`) → core value **$62,895.40**, equity **$92,895.40**, core **67.706%**,
  cash **32.29%**. Core unrealized on that basis **−$7,104.59 / −10.149%** against the
  $69,999.99 cost basis.
- **The live 08:36 read, for contrast and NOT durable:** `sleeves` equity **$94,367.23**, core
  **$64,372.18**, core **68.21%**, cash 31.79%, `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: 1684.88`. Read off `current_price` **649.92**, a **PRE-MARKET PRINT**
  (+2.35% on Friday's close). `account` a moment later read equity **$94,391.99**. These moved
  between two calls one minute apart and will move again before the bell.
- **§2 BAND VERDICT IS ROBUST TO THE BASIS — solved, not assumed.** Core reads **67.71%** on the
  official close and **68.21%** pre-market; both sit well inside 65–75%, so no rebalance is
  authorized on either reading. With cash pinned at exactly $30,000 and 99.046311231 shares, the
  **65% floor breaks at VOO 562.51** (−11.4% from Friday's close) and the **75% ceiling at 908.67**
  (+43.1%). Both re-derived at this seat from `0.65·30000/0.35 ÷ q` and `0.75·30000/0.25 ÷ q`.
- **Satellite sleeve is empty and always has been.** Zero positions, zero satellite orders ever.
  The account's entire order history is the 2026-09-03 VOO core bootstrap. Nothing is in limbo,
  and no order from any seat is awaiting verification.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists anywhere. ⚠⚠ **Core VOO is EXEMPT from §5; its −10.149% close-basis
  loss is NOT a §5.3 reading and its drawdown is NOT a §5.4 reading.** That is a rule, not a
  judgment call, and it is restated because the magnitude now clears **both** thresholds by a wide
  margin and a fresh-clone seat reading only the P&L line could mistake it for a trigger.
  **The §5 machinery remains unproven code, 81 days old and never once run against a position.**
- **299 theses written, 0 ever accepted in 81 days.** Inherited from the 07:01 seat, which
  re-derived it; this seat wrote no new thesis and rejected none, so the count is unchanged.
- Breaker **INACTIVE 0/3** · weekly cap **0/3** used · `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `alerts.md` has no open and no systemic incidents.
- **Week rollover: no reset due, re-derived at this seat.** `week_anchor(2026-11-23)` →
  **2026-11-23** (imported from `common.py`, not assumed) = inherited `week_of`. Anchor and value
  agree, so `new_positions_this_week` stays **0**.
- ⚠ **Endpoint disagreement, same instance the 07:01 seat recorded, NOT a 15th:**
  `positions.lastday_price` **635.54** vs official `bars` **635.01** for 2026-11-20 =
  **0.53 / 0.0835%**. Confirmed independently here off a second `bars` call; recorded range
  remains 0.04–1.41. The count stays at **14 distinct instances**.

## What this run did, and the one thing worth noticing

**Nothing, lawfully.** The staleness gate **PASSED** — `plan_date` read **2026-11-23**, today —
and the plan behind it carried **zero BUY, zero SELL and zero REBALANCE intents**. Step 3 was
skipped (`core_established: true`), Step 4 had no operand, Steps 5–6 had no intent to re-validate
so **no `move` call was spent**, and Step 7's band test says hold. No order was placed and none
was owed.

⚠⚠ **TODAY SEPARATES THE TWO STANDING DEFECTS FOR THE FIRST TIME IN THIS CLONE'S RECORD, AND THE
HUMAN SHOULD READ THAT.** The plan handoff worked exactly as designed — fresh date, correct
contents, nothing stale. The *only* reason the 54-minute pre-bell firing cost nothing again is
that **the funnel was empty**. On every prior occasion the two defects were tangled together and
either could be blamed; today the handoff is exonerated and the shut door stands alone. **Fix the
funnel (carry-forward item 1) and the schedule defect becomes binding on the very next day a
thesis survives.** That ordering matters for which fix the human does first.

## Carry forward

1. ⚠⚠⚠ **STILL THE MOST IMPORTANT THING IN THIS FILE — FOR THE HUMAN. THE FUNNEL MAY BE
   UNSATISFIABLE BY CONSTRUCTION, AND THAT IS A BETTER EXPLANATION OF 299→0 THAN "OPPORTUNITIES
   ARE RARE."** The sweep that has done most of the recent killing asks whether a **news source has
   already named** the second-order company and its segment. **§4 demands no such thing** — it asks
   the *agent* to write a mechanism, dollar path, timing and invalidation that are honest and
   sourceable. Requiring the *source* to have done the second-order reasoning restricts the funnel
   to links the market has already been told about, **which is precisely the set §4's own priced-in
   filter then kills.** The two gates in combination are close to unsatisfiable.
   ⚠⚠ **RAISED, NOT ACTED ON, AND NO SEAT MAY GRANT ITSELF THE FIX.** Loosening the sourcing
   standard is exactly what §4's honest-broker rule exists to prevent, and a run that diagnosed its
   own filter as too strict and then relaxed it would be the failure mode rather than the remedy.
   **Both readings fit the evidence and a seat inside the loop cannot distinguish them. The
   calibration is the human's to set.** ⚠ **This seat now ranks this ABOVE item 2**, because today
   showed the empty funnel is the binding constraint and the schedule is the one that bites second.
2. ⚠⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** With today,
   **ten of eleven** recorded routine-2 seats fired pre-bell (~08:35–08:41, ~50–55 min early);
   2026-11-13 at 10:47 was the lone exception and 2026-11-16 did not fire at all. **No alert was
   posted this run and none should be** — re-send **only** if routine 2 begins firing *after* the
   bell in a way that changes what the human must fix. **Recorded, not diagnosed**, per
   `control.md`'s standing note that manual and scheduled runs are indistinguishable in run logs.
   ⚠⚠ **THE STANDING COST IS STILL ZERO, BUT THE REASON NARROWED TODAY** — see the section above.
   The only seat licensed to open a position has been unable to act for essentially this clone's
   history; until today the empty funnel and the shut door masked each other. **Today the plan was
   fresh and well-formed, so the funnel alone is what made the shut door harmless.**
   ⚠⚠⚠ **THE UNRESOLVED RULE QUESTION, RAISED NOT RESOLVED, AND IT DID NOT BIND TODAY.** Routine
   2's prompt says that if the market is closed, log the skip and exit. Read literally, **a pre-bell
   seat holding a live BUY or a mandatory §5 exit must discard it.** There was no such intent today,
   so the question stayed hypothetical for the eleventh time. The two fixes — hold ~50 min for the
   open, or fix the schedule — are **the human's to choose; a run must not grant itself the first**,
   and this run did not.
   ⚠ Routines 3, 4 and 5 are **different, milder cases and must not be folded in.**
3. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md`** — that scoping error is what cost
   2026-11-13, whose journal entry and ClickUp summary do not exist and never will. **Applies to
   routine 4, not to this one.**
4. ✅ **HOLD FOR THE BELL HAS PAID EVERY TIME IT WAS USED — BUT IT IS A CLOSE-ROUTINE TOOL, AND
   THIS SEAT DID NOT USE IT.** The 11-20 review polled `clock` to the post-bell signature
   (`is_open: false` with **both** `next_open` and `next_close` on the *next* session — the only
   reading that separates post-bell from pre-market), waited 5 minutes, and got the official close;
   its 15:46 partial read 637.30 was high by **2.29 / +0.361%**. ⚠ **Waiting for the OPEN is a
   different act and is NOT cleared** — see item 2.
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.**
   14 distinct instances, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.** ✅ **This seat followed it** — the sleeve block above is stamped on
   the 635.01 official close, not on the 649.92 pre-market print it also read.
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** Both re-derived 2026-11-20.
   (i) **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** — byte-identical to the
   unadjusted series on 259 of 260 sessions across all four ex-dates. Reconstruct by reinvesting at
   the ex-date close: 2025-12-22 $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28
   $1.8226 (TTM $7.43; **none since 09-28**). Following Step 1 literally understates the 12-month
   benchmark by **1.25pp**.
   (ii) **THE PAPER BROKER NEVER CREDITS DISTRIBUTIONS** — `cash` is exactly `30000`, not
   $30,180.52; confirmed again at this seat (`account.cash` = `30000`, `accrued_fees` 0). The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark, widening every
   quarter. ⚠⚠ **The two defects roughly cancel, which is why ten reviews caught neither.**
8. ⚠ **THIS CLONE IS SHALLOW.** Any run citing git history beyond ~2 weeks is citing something it
   cannot see. Do not repeat inherited history claims as measured.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING.** `positions.md` was **369,010 B** when
   this seat read it (`wc -c`, not inherited) — up 1,482 B since Friday, **still describing a ledger
   that has been empty for all 81 days of this account's history.** It is excluded from Step 6
   rollover on the premise that it "only holds open positions," which has been false the whole time,
   **so no run has standing to truncate it. The human must set a retention rule.** This seat
   appended **no new digest block** — it added its seat and ordinal to the existing 2026-11-23
   header, which is the smallest lawful write available to it.
