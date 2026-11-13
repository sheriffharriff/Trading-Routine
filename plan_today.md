# Today's Plan

**AGENT-OWNED. Written by the pre-market routine, consumed by the market-open routine,
overwritten daily.**

This file is the handoff between the two runs. The pre-market run does the thinking and
writes intents here; the market-open run executes them. Nothing gets bought that was not
written here first, which is what forces every buy to sleep on a written thesis instead of
being reasoned into existence at the moment of execution.

The market-open run **re-validates every intent against fresh quotes before acting**. An
intent written at 08:00 can be dead by 09:35 — an overnight gap can push a candidate past
the §4 4%-in-five-sessions priced-in threshold, in which case the trade is skipped and the
skip is logged. A stale intent is a proposal, not an instruction.

---

## Status

`plan_date` is load-bearing, not a comment. The market-open routine compares it to today's
ET date and **refuses to execute any intent from a plan not dated today** — it logs the
stale plan, posts an alert, and proceeds to the core/rebalance section only.

```
plan_date: 2026-11-13
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-13 at 09:30 ET** (`clock` 07:01:40 ET: `is_open: false`, `next_open`
`2026-11-13T09:30:00-05:00`, `next_close` `2026-11-13T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Friday, an ordinary full session.

The plan this seat replaced was dated **2026-11-12** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

**WEEK ROLLOVER — NO ACTION DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W46**, weekday **5**; Monday anchor **2026-11-09** = the inherited `week_of`
**2026-11-09**. `new_positions_this_week` stays **0 of 3**. ⚠ **Recorded as re-derived rather
than skipped: §6's cap must not depend on any earlier seat having run.**

---

## ⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`. That was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Dispatches since: `08:47` (11-02) ·
`08:36` (11-03) · `08:35` (11-04) · `08:37` (11-05) · `08:37` (11-06) · `08:36` (11-09) ·
`08:36` (11-10) · `08:35` (11-11) · `08:37` (11-12) — **nine for nine, each read
`is_open: false` and placed nothing.** This seat dispatched at `07:01` against a nominal
`08:00`: the same −1h, **tenth consecutive EST session.**

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED, CONFIRMED
CONDITION — NOT A NEW FAULT AND NOT A HOLIDAY.** Record the firing time and `is_open` as your
first line. `control.md` forbids diagnosing a schedule fault **from a firing time**; the
stored-schedule reading plus the DST calendar is different evidence.

⚠⚠ **STATUS OF THE ASK: DELIVERED, AWAITING THE HUMAN.** The 11-12 close seat sent this fault
to the human **out of band by push notification** — the first time in nine sessions it left the
repo. ⚠ **It has NOT been re-sent today and must not be re-sent daily:** the evidence is
complete, the fix is the human's alone, and a fault already delivered does not become more
deliverable by repetition. **Re-send only if it changes shape** — e.g. routine 2 begins firing
*after* the bell, or a seat is skipped entirely.

**PROCEDURE IF YOU ARE THE OPEN SEAT AND THIS PLAN CARRIES ANY INTENT:** finish every
closed-market-safe step, **COMMIT AS INSURANCE** (say in the message that a hold is in progress
and what to backfill if the second commit never lands), poll `clock` until `is_open: true`,
then execute and commit again. **DO NOT log a skip over a non-empty plan.** Holding past the
bell is exactly what changes `is_open`, and routine 4 has now proved the hold **five times**
(11-06, 11-09, 11-10, 11-11, 11-12), recording the official close each time. ⚠ **This plan
carries no intents, so the procedure is not due today — it is written here because the day it
IS due, the seat will be reading this file and nothing else.**

---

## Account state at plan time

```
equity:                   99141.26
cash:                     30000.00
core (VOO):               69141.26  = 69.74%
satellite:                       0  =  0.00%  (0 positions)
cash_pct:                              30.26%
core_in_band:             true   (§2 band 65-75%)
rebalance_needed:         false
rebalance_delta:          +257.62
circuit_breaker:          INACTIVE  (consecutive_closed_losses 0)
new_positions_this_week:  0 of 3
```

**LEDGER RECONCILED, THREE SIDES, RE-DERIVED NOT INHERITED.** `positions.md` carries **zero**
satellite positions; `sleeves` reports satellite **count 0, value 0, pct 0.0**; `positions`
returns **one row, core VOO only** — 99.046311231 sh, `avg_entry_price` 706.74, `cost_basis`
69,999.99, unchanged since the 2026-09-03 fill. ⚠ **No disagreement between Alpaca and the
ledger. Nothing to reconcile and nothing flagged.**

---

## BUY intents

**NONE.**

⚠ **New positions were PERMITTED THROUGHOUT this run** — breaker inactive, 0 of 3 on the §6
weekly cap, satellite sleeve 0.0% deployed with $30,000 of uninvested cash, `control.md` Notes
`(none)`. **Nothing structural blocked a buy. Six candidates were considered and all six were
rejected on their merits** — the full disposal is in `research_log.md` under `T-2026-11-13-01`
through `-06`.

⚠⚠ **THE TWO THAT GOT FURTHEST DIED ON THE MECHANICAL PRICED-IN FILTER, BY 4× AND 5×:**
**LEU +17.11%** over five sessions (88.90 → 104.115) and **AMAT +19.34%** (319.335 → 381.095),
both returning `priced_in: true` and *"LATE - skip"*. Both were independently dead on part 3 as
well (LEU deliveries begin **2029**, ~12 quarters out; AMAT's figure is a **full-year 2027**
industry projection), and both are **first-order legs** — the companies named in their own
releases, which is what §4 opens by forbidding.

⚠ **§2 is explicit that uninvested satellite cash is fine and that trades must not be forced to
stay fully invested. A 0.0%-deployed satellite sleeve is not a reason to lower the bar, and the
30% cash balance is NOT an instruction to this plan.**

---

## SELL intents

**NONE — NO OPERAND.** Zero satellite positions are held, so §5 has nothing to evaluate.

⚠⚠ **RECORDED PRECISELY, BECAUSE THE DISTINCTION IS LOAD-BEARING: SELL RULES 5.1, 5.2, 5.3 AND
5.4 ARE *ABSENT*, NOT *PASSING*.** A run with no positions cannot exercise a sell rule, and
writing "all rules pass" would put a false clean bill of health into the ledger. **Core VOO is
struck from the §5 working list entirely** — §5 exempts core from all four rules; it is not
stamped as passing them either.

⚠ **The §5.4 trailing-stop staleness detector remains UNEXERCISED for the 80th consecutive
absent-seat ordinal — still unproven code.** It has never run against a real `highest_close`.
**That is a standing risk to flag, not a defect to fix mid-run:** the first real satellite
position will be the first live test of that path.

**Step 4 (position review) therefore had no operand.** No Perplexity invalidation checks were
run on holdings, because there are no holdings. ⚠ **No-operand is not the same as no-work, and
it is also not a pass.**

---

## REBALANCE intent

**NONE.** Core **69.74%**, inside the §2 65–75% band (`core_in_band: true`,
`rebalance_needed: false`). `rebalance_delta` **+$257.62**, i.e. **4.74pp of room to the 65%
floor** and 5.26pp to the ceiling — residual fractional-share drift against a moving mark,
nowhere near a trigger.

⚠ **The open seat should re-read `sleeves` rather than trusting this line:** it was computed at
07:01 against a pre-market mark, and §2's band is checked at the open run, not inherited from
the pre-market run.

---

## Revalidation instructions for the open seat

There are no intents to revalidate. **If this plan is consumed as written, the correct action
on the satellite sleeve is to place nothing.**

The only live numbers worth re-checking:

1. **`sleeves` → `core_in_band` / `rebalance_delta`.** Re-derive; do not inherit the 69.74%
   above. If core has left 65–75%, a REBALANCE is due under §2 **even though this plan carries
   none** — the band is a standing rule, not an intent.
2. **`plan_date` above = `2026-11-13`.** If today's ET date is not 2026-11-13, this plan is
   stale: log it, alert, and go to the core/rebalance section only.
3. **Nothing else.** ⚠ **Specifically: do NOT revisit LEU or AMAT on a favourable gap.** A gap
   down does not repair a part-3 failure of ~12 quarters or a full-year-2027 horizon, and it does
   not make a first-order leg second-order. The priced-in filter was the *cheapest* of the three
   kills, not the only one. **Re-screening them would be looking for permission for a trade this
   seat already declined twice over.**

---

## Note to the next seat

**A run that places nothing is the normal case, and §4 says so in terms:** *"The correct output
of most research runs is no trade. A run that finds nothing worth buying is a successful run."*

⚠ **The one thing this seat produced that is worth reading is in `research_log.md`, not here:**
both candidates that survived to the hard filters were killed by **arithmetic rather than
judgement**, which is the first time that has happened on every candidate in a session. The
hypothesis it raises — that being well-formed enough to pass parts 1–4 and being already-priced
may be **the same property** — is written up there as a hypothesis, with the test that would
settle it. ⚠ **Two instances is not evidence, and a seat may not promote it to a standing rule.
Only the human may.**
