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
plan_date: 2026-11-16
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-16 at 09:30 ET** (`clock` 07:01:57 ET: `is_open: false`, `next_open`
`2026-11-16T09:30:00-05:00`, `next_close` `2026-11-16T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Monday, an ordinary full session.

The plan this seat replaced was dated **2026-11-13** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W47**, weekday **1**; Monday anchor **2026-11-16** = the inherited `week_of`
**2026-11-16**. `new_positions_this_week` stays **0 of 3**. ⚠ **The 11-13 review set `week_of`
forward to next Monday and warned a weekend run would reset it backward to 2026-11-09. No seat
ran in between, so the forward-set value is simply correct today and the warning never bound.**

---

## ⚠⚠ READ THIS FIRST — WHAT THE OPEN SEAT SHOULD EXPECT

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`, which was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Nine consecutive sessions (11-02 →
11-12) dispatched between `08:35` and `08:47`, each reading `is_open: false` and placing
nothing.

⚠⚠ **BUT ON 2026-11-13 ROUTINE 2 FIRED AT 10:43 ET WITH `is_open: true`, MID-SESSION, FOR THE
FIRST TIME IN TEN SESSIONS.** The harness reported that run's *scheduled* time as `09:17 ET` and
the dispatch landed 86 minutes later. **This seat did not re-read the stored schedule and does
not diagnose anything from it** — `control.md` forbids diagnosing a schedule fault from a firing
time, and one session is not a trend in either direction.

⚠ **PRACTICAL CONSEQUENCE FOR THE OPEN SEAT: `is_open` could read either way today, and BOTH are
expected. Record the firing time and `is_open` as your first line, and do not treat `false` as a
holiday or as a new fault.** This seat itself dispatched at **07:01** against a nominal `08:00`,
the same −1h shape, for the **thirteenth consecutive EST session**.

⚠⚠ **STATUS OF THE ASK: DELIVERED, AWAITING THE HUMAN. DO NOT RE-SEND.** The 11-12 close seat
sent this fault out of band by push notification. **The 11-13 10:43 dispatch is a change of
shape and is recorded here**, but it is a change toward the fault *not binding*, which is not an
escalation and does not warrant re-interrupting the human. **Re-send only if routine 2 begins
firing consistently after the bell in a way that changes what the human must fix, or if a seat
is skipped entirely.**

**PROCEDURE IF YOU ARE THE OPEN SEAT AND THIS PLAN CARRIES ANY INTENT:** finish every
closed-market-safe step, **COMMIT AS INSURANCE** (say in the message that a hold is in progress
and what to backfill if the second commit never lands), poll `clock` until `is_open: true`, then
execute and commit again. **DO NOT log a skip over a non-empty plan.** ⚠ **This plan carries no
intents, so the procedure is not due today — it is written here because the day it IS due, the
seat will be reading this file and nothing else.**

⚠⚠⚠ **AND THE HOLD IS NOT HYPOTHETICAL: THE 11-13 CLOSE SEAT'S SECOND COMMIT NEVER LANDED.** Its
insurance commit went in at 15:15 and the post-bell commit did not. **That is what the backfill
below exists to repair, and it is the strongest argument for the insurance-commit discipline
rather than against it** — the insurance commit is the only reason 11-13 is in the record at all.

---

## ✅ BACKFILL OWED TO THIS SEAT — PRICE LEG DISCHARGED

`state.md` recorded four things lost when the 11-13 close seat's second commit failed. **This
seat retrieved the two that are recoverable from the broker and leaves the two that are not.**

**RECOVERED — `bars --symbol VOO --days 6 --adjustment all`, pulled 07:02 this seat:**

```
OFFICIAL 2026-11-13 VOO CLOSE:  693.05   (n 2,492 · v 42,853 · adjustment=all)
close-basis equity:             98,644.05   (99.046311231 sh x 693.05 + 30,000.00 cash)
close-basis core / sat / cash:  69.59% / 0.00% / 30.41%
close-basis unrealised on VOO:  -1,355.94  (-1.937% vs 706.74 cost)
day P&L 11-13 (close basis):    -296.15    (-0.430% vs 11-12 close 696.04)
```

⚠ **AND IT SETTLES THE PARTIAL-BAR MEASUREMENT THE 11-13 CLOSE SEAT LEFT OPEN.** That seat
recorded the in-progress 15:17 bar at **692.64** and said "whatever the official close turns out
to be, the gap is the measurement." **The gap is +0.41, or +0.0592%.** A sixth point for that
series, and a small one.

**NOT RECOVERED, AND NOT RECOVERABLE BY THIS SEAT:** the `journal.md` entry for **2026-11-13**
and that day's **ClickUp daily summary**. ⚠ **This seat did NOT write a backdated journal entry.
`journal.md` is the close routine's file; a pre-market seat inventing a close-day narrative three
days later would put something in the record that no seat observed.** The figures above are where
the next reader should look instead.

---

## Account state at plan time

```
equity:                   98345.92
cash:                     30000.00
core (VOO):               68345.92  = 69.50%
satellite:                       0  =  0.00%  (0 positions)
cash_pct:                              30.50%
core_in_band:             true   (§2 band 65-75%)
rebalance_needed:         false
rebalance_delta:          +496.23
circuit_breaker:          INACTIVE  (consecutive_closed_losses 0)
new_positions_this_week:  0 of 3
```

**LEDGER RECONCILED, THREE SIDES, RE-DERIVED NOT INHERITED.** `positions.md` carries **zero**
satellite positions (the one `### <TICKER>` heading in the file is the template at line 42);
`sleeves` reports satellite **count 0, value 0, pct 0.0**; `positions` returns **one row, core
VOO only** — 99.046311231 sh, `avg_entry_price` 706.74, `cost_basis` 69,999.99, `market_value`
68,345.92, `unrealized_plpc` **−2.363%**, unchanged since the 2026-09-03 fill. ⚠ **No
disagreement between Alpaca and the ledger. Nothing to reconcile and nothing flagged.**

---

## BUY intents

**NONE.**

⚠ **New positions were PERMITTED THROUGHOUT this run** — breaker inactive, 0 of 3 on the §6
weekly cap, satellite sleeve 0.0% deployed with $30,000 of uninvested cash, `control.md` Notes
`(none)`. **Nothing structural blocked a buy. Four candidates were considered and all four were
rejected on their merits** — full disposal in `research_log.md` at `T-2026-11-16-01` through
`-04`, the last of which disposes thirteen sweep items as one.

⚠⚠ **TODAY'S SHAPE IS DIFFERENT FROM FRIDAY'S AND THE DIFFERENCE IS WORTH THE OPEN SEAT KNOWING:
NOT ONE CANDIDATE REACHED THE HARD FILTERS. ZERO `move` CALLS WERE MADE.** Friday's two finalists
died on arithmetic (LEU +17.11%, AMAT +19.34%); today's died at part 1 or part 2, before a
priced-in check was worth paying for. **The 11-13 hypothesis — that well-formed and already-priced
may be the same property — gained ZERO new data points. Recorded as a null, not as support.**

⚠ **Two of the three non-sweep candidates died on the same shape: an event that PRESERVES the
status quo.** An FDA Complete Response Letter (`-01`) and a court ruling leaving tariffs in place
(`-03`) both change a *forecast* rather than a revenue line. **The headline is large and the
economics do not move.** It is an easy shape to mistake for news.

⚠ **§2 is explicit that uninvested satellite cash is fine and that trades must not be forced to
stay fully invested. A 0.0%-deployed satellite sleeve is not a reason to lower the bar, and the
30.5% cash balance is NOT an instruction to this plan.**

---

## SELL intents

**NONE — NO OPERAND.** Zero satellite positions are held, so §5 has nothing to evaluate.

⚠⚠ **RECORDED PRECISELY, BECAUSE THE DISTINCTION IS LOAD-BEARING: SELL RULES 5.1, 5.2, 5.3 AND
5.4 ARE *ABSENT*, NOT *PASSING*.** A run holding nothing cannot exercise a sell rule, and writing
"all rules pass" would file a false clean bill of health. **No distance-to-stop is writable** —
5.3 needs an entry price and 5.4 needs a `highest_close`, and neither exists.

**Core VOO is STRUCK from the §5 working list, not stamped as passing it.** §5 exempts core from
all four rules. Its **−2.363%** unrealised loss is **NOT** a §5.3 reading and must never be
logged as one.

⚠ **The §5.4 trailing-stop staleness detector remains UNEXERCISED for the 84th consecutive
absent-seat ordinal — still unproven code.** (Derivation, not assertion: the 11-13 close seat was
the 83rd; this is the next.) **A standing risk to flag, not a defect to fix mid-run:** the first
real satellite position will be the first live test of that path.

**Step 4 (position review) had no operand.** Zero Perplexity invalidation checks were run on
holdings, because there are no holdings. ⚠ **No-operand is not no-work, and it is also not a
pass.**

---

## REBALANCE intent

**NONE.** Core **69.50%**, inside the §2 65–75% band (`core_in_band: true`,
`rebalance_needed: false`). `rebalance_delta` **+$496.23**, i.e. **4.50pp of room to the 65%
floor** and 5.50pp to the ceiling — residual fractional-share drift against a falling mark,
nowhere near a trigger.

⚠ **The delta has widened at every seat since Friday morning (+257.62 → +519.40 → +527.72 →
+423.76 → +496.23) as VOO has fallen. That is the arithmetic of a fixed share count against a
moving mark, not drift in the position.** Core has not been touched since 2026-09-03.

⚠ **The open seat should re-read `sleeves` rather than trusting this line:** it was computed at
07:01 against a pre-market mark, and §2's band is checked at the open run, not inherited from the
pre-market run. **If core has left 65–75%, a REBALANCE is due under §2 even though this plan
carries none — the band is a standing rule, not an intent.**

---

## Revalidation instructions for the open seat

There are no intents to revalidate. **If this plan is consumed as written, the correct action on
the satellite sleeve is to place nothing.**

The only live numbers worth re-checking:

1. **`sleeves` → `core_in_band` / `rebalance_delta`.** Re-derive; do not inherit the 69.50%
   above.
2. **`plan_date` above = `2026-11-16`.** If today's ET date is not 2026-11-16, this plan is
   stale: log it, alert, and go to the core/rebalance section only.
3. **Nothing else.** ⚠ **Specifically: do NOT revisit LEU, AMAT, or the Oklo/Centrus HALEU
   complex on a favourable gap.** A gap down does not repair a part-3 failure of ~12 quarters and
   does not make a first-order leg second-order. **Re-screening them would be looking for
   permission for a trade two seats have now declined.**

---

## Note to the next seat

**A run that places nothing is the normal case, and §4 says so in terms:** *"The correct output
of most research runs is no trade. A run that finds nothing worth buying is a successful run."*

⚠ **The thing this seat produced that is worth reading is in `research_log.md`, not here:** the
single drill query of the day (`T-2026-11-16-01`) killed its own thesis on **evidence** — the
sources say ivonescimab had *no approved equivalent* in that indication, so the CRL protected
nobody's share — rather than on analogy to the near-identical `T-2026-11-10-03`. **A precedent and
a verified fact are not the same object and the log should be able to tell them apart.** That is
what the $0.005 bought.

⚠ **Standing, unchanged, for the human only:** `positions.md` is **302KB describing an empty
ledger** and is unreachable by the monthly rollover. **No run has standing to truncate it.** See
`weekly_review.md`, week ending 2026-11-13, Recurring Error 1.
