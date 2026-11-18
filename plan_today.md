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
plan_date: 2026-11-18
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-18 at 09:30 ET** (`clock` 07:03:10 ET: `is_open: false`, `next_open`
`2026-11-18T09:30:00-05:00`, `next_close` `2026-11-18T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Wednesday, an ordinary full session.

The plan this seat replaced was dated **2026-11-17** — the previous trading day, the ordinary
shape. It carried **zero intents**. **Nothing was lost: a plan with no intents has no
execution to perform**, so whether a `2-market-open` seat consumed it is immaterial.

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W47**, weekday **3**; Monday anchor **2026-11-16** = the inherited `week_of`
**2026-11-16**. `new_positions_this_week` stays **0 of 3**.

---

## ⚠⚠ READ THIS FIRST — WHAT THE OPEN SEAT SHOULD EXPECT

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`, which was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Nine consecutive sessions (11-02 →
11-12) dispatched between `08:35` and `08:47`, each reading `is_open: false` and placing
nothing. **11-13 fired at 10:43 with `is_open: true`. 11-16 did not fire at all** (the first
whole-session absence). **11-17 fired at 08:36, the ordinary pre-bell shape.**

⚠ **PRACTICAL CONSEQUENCE FOR THE OPEN SEAT: `is_open` could read either way today, and so
could a total absence. ALL THREE ARE EXPECTED. Record your firing time and `is_open` as your
first line, and do not treat `false` as a holiday or as a new fault.** This seat itself
dispatched at **07:03** against a nominal `08:00` — the same −1h shape, **fifteenth
consecutive EST session**. ⚠ Per `control.md` this is **recorded, not diagnosed**: a firing time
is not a schedule diagnosis, and manual "Run now" invocations are indistinguishable from
scheduled ones.

⚠⚠ **STATUS OF THE ASK: DELIVERED AND RE-SENT. DO NOT RE-SEND AGAIN.** The 11-12 close seat
sent the fault out of band by push notification; the 11-16 close seat re-sent it on the
condition the 11-12 carry-forward named explicitly. **It is now with the human and nothing has
changed since.** Re-send only if routine 2 begins firing consistently *after the bell* in a way
that changes what the human must fix. **A repeat pre-bell firing is not new information and
does not warrant re-interrupting anyone.**

**PROCEDURE IF YOU ARE THE OPEN SEAT AND THIS PLAN CARRIES ANY INTENT:** finish every
closed-market-safe step, **COMMIT AS INSURANCE** (say in the message that a hold is in progress
and what to backfill if the second commit never lands), poll `clock` until `is_open: true`, then
execute and commit again. **DO NOT log a skip over a non-empty plan.** ⚠ **This plan carries no
intents, so the procedure is not due today — it is written here because the day it IS due, the
seat will be reading this file and nothing else.**

---

## BUY intents

**NONE. Zero BUY intents.**

⚠ **This is a decision, not an omission, and nothing structural caused it.** New positions were
**permitted throughout this run**: breaker **INACTIVE (0/3)**, weekly cap **0 of 3 used**,
satellite sleeve **0.0% deployed with $30,000 of cash**, `TRADING_ENABLED: true`, `control.md`
Notes **(none)**. **The candidates failed, not the gates.**

Five theses were written and all five rejected — `T-2026-11-18-01` through `-05`, the last a
six-item sweep. Full reasoning in `research_log.md`. The overnight window was **dominated by a
single event**, and it is worth the open seat knowing how it died:

- **Nvidia reported after the 11-17 close** — FQ4 revenue guided to **~$130B ±3%** (consensus
  ~$124.89B), next-FY growth raised to **~75% from ~70%**, +4% extended trading, NDX futures
  +1.3%. **The best-formed catalyst this corpus has seen for the AI complex: dated, quantified,
  first-disclosure, straight from the demand source.** It still produced no trade.
  - **`T-2026-11-18-01` (MU)** — part 1 **passed** cleanly; killed on **part 4**: Micron's
    calendar-2026 HBM book is **sold out on price and volume** (management, 2025-12-17), so no
    observable in the next two quarters can distinguish "Nvidia's raise flowed through" from
    "the memory cycle did what it was already doing." **An invalidation condition that cannot
    fail is not one.** Part 2 also unsourceable — the drill returned **$41.5B and $54.2B for the
    same quarter**, a 30% disagreement on the denominator, neither from a filing.
  - **`T-2026-11-18-02` (the infra tier)** — killed on **part 3**: an **FY28** demand revision
    reaches power/cooling/networking **revenue** through orders → backlog → recognition, which is
    two-to-four quarters out. Only the narrative lands inside §4's window, and **backlog is not
    a reported result.**

**NOTHING FOR THE OPEN SEAT TO REVALIDATE.** `revalidate` lines exist to catch an overnight gap
pushing a candidate past the §4 priced-in threshold between 08:00 and 09:35. **With zero BUY
intents there is no number to re-check, and no `move` call is owed.**

## ⚠⚠⚠ BUT READ THIS BEFORE YOU EVER TRUST A PRE-MARKET `priced_in: false` AGAIN

**This is the finding of the run and it is mechanically verified.** It changes nothing today
and will matter enormously on the first session where a post-close catalyst produces a BUY
intent.

**The §4 priced-in filter reads the trailing five COMPLETED sessions.** `bars` returns **no
2026-11-18 row** at this hour, and `move --sessions 5` reported `to_close` **155.49 for NVDA**
and **712.975 for MU** — both confirmed by `bars` to be the **2026-11-17** closes.
**Nvidia reported AFTER that close.**

⚠ **So every `priced_in` verdict computed this morning rests on a window containing ZERO
post-catalyst sessions.** A `false` does not mean "the market has not repriced this news" — it
means **"no session has traded since this news,"** which carries no information about lateness
whatsoever. **Nine of thirteen names "passed" a test that could not have failed**, because the
complex **sold off into the print** (NVDA itself **−7.88%** over the window; MU −1.64%, VRT
−2.06%, MRVL −3.60%).

⚠⚠ **SEPARATELY, AND DO NOT CONFLATE THE TWO: the filter is magnitude-based and
direction-blind.** §4's text is *"moved more than 4%... you are late"*; the script implements
`abs(move) > 4`. **SMCI read `priced_in: true` after FALLING 13.10%**, as did APH (−4.50%) and
ETN (−4.86%). **This seat honored all four `true` verdicts as skips and attempted no override** —
the argument "the filter is direction-blind, so let me buy the one that fell 13%" is averaging
into weakness in a costume, and §7 forbids averaging down. **It is reported for the human to fix
in code if they choose; it is not a permission a run may grant itself.**

**OPERATIONAL RULE FOR A FUTURE OPEN SEAT:** when the plan's catalyst broke after the prior
close, **you are the first seat that can actually perform the priced-in test.** Re-run
`move --sessions 5` after the open, and treat the pre-market reading as unperformed rather than
passed.

## SELL intents

**NONE. Zero SELL intents — NO OPERAND, not a pass.**

The satellite sleeve holds **zero positions** and always has. `alpaca.py positions` returns
exactly one row, the **VOO core** holding, which is **exempt from §5 entirely** — core is not
sold on news. §5.1 through §5.4 were therefore **not evaluated and could not be**: there is no
entry price, no `highest_close`, no deadline and no invalidation string in existence.

⚠ **`sell_rule_status` in `positions.md` reads ABSENT, not PASSING.** A rule that cannot fire
for want of a position is not a rule that was checked and cleared, and the two must not be
allowed to look alike to the next reader.

⚠ **The §5.1 news check was therefore NOT run on any holding, and no Perplexity query was spent
on one.** With no position there is no company to check for invalidating news. **This is the
91st consecutive seat with no operand for §5.**

## REBALANCE intents

**NONE. Core is in band.**

`alpaca.py sleeves` at 07:03: equity **$96,856.26** · core **VOO $66,856.26 = 69.03%** ·
satellite **0.00%** · cash **$30,000.00 = 30.97%**. `core_in_band: true`,
`rebalance_needed: false`.

⚠ **`rebalance_delta: 943.12` IS A DISTANCE READOUT, NOT AN ORDER.** It is how far core sits
from its exact 70% target value (`core_target_value: 67,799.38`), which §2 does not require it
to hit. The band is **65–75%** and core has **4.03pp of room to the floor**. **Do not buy
$943.12 of VOO because this field is non-zero.** ⚠ The share count has not changed since the
2026-09-03 fill; this field tracks **the mark, not the position**, which 11-17's intraday series
demonstrated by rising 767.98 → 1088.12 and then falling back to 1008.49 on the close.

---

## Notes for the open seat

1. **Yesterday's official close is confirmed at VOO 672.80** (`bars`, 2026-11-17). ⚠ **The
   endpoint disagreement is live again — EIGHTH distinct instance, and the widest intraday
   reading of the series:** `positions.lastday_price` reads **673.19** against the official bar
   close **672.80** — gap **0.39 / 0.0580%**. **Build P&L and stamp `highest_close` from official
   `bars` closes only, on one adjustment basis, one call.** A `highest_close` stamped from
   `lastday_price` and compared against a `bars` close manufactures a phantom move.
2. ⚠ **`positions.current_price` reads 675.00 — that is a PRE-MARKET INDICATION, NOT A TRADED
   CLOSE**, and it is what makes live equity (**$96,856.26**) sit **$217.90 above** 11-17's
   close-basis equity of $96,638.36. **Do not record 675.00 as a close or build a day-change off
   it.** `bars` returned **no 2026-11-18 row**, which is the correct pre-market shape.
3. **The in-progress-bar defect is not in play at this hour** (no today-row exists) — but
   **gate any high-water write on `clock`, never on the shape, presence or apparent stability of
   the bar.** 11-17 caught the same dated bar at **669.96 and then 670.45 two minutes apart**
   with the market open; a finished close does not change between pulls. ⚠ **All three of
   11-17's partial prints read LOW against the official 672.80, and so did 11-16's — TWO
   SESSIONS IS NOT A RULE. Do not treat "partials read low" as a correction factor.**
4. **Ledger reconciled on three sides and it AGREES.** `positions` returns exactly one row
   (VOO, qty 99.046311231, avg entry 706.74); `sleeves` reports satellite `count: 0`;
   `positions.md` carries zero satellite blocks under **Open positions**. **No discrepancy, so
   no repair was owed and none was performed.**
5. **No open incidents.** `alerts.md` carries nothing OPEN and nothing SYSTEMIC. Selftest
   **5/5, exit 0**.
6. **The corpus-size finding is unchanged and still needs the human, not a run.**
   `positions.md` is ~334KB describing an empty ledger and is unreachable by the monthly
   rollover. **No run has standing to truncate it.** This seat added the shortest digest it
   could and **claims no collapse ratio** — the line count is the wrong instrument.
7. ⚠ **This seat deliberately avoided the agent-authored "rule (iii)…(viii)" shorthand** and
   wrote its five rejections in §3/§4's own language instead, naming prior findings by date and
   content. That is a direct response to the **second standing item in `weekly_review.md`** —
   that the taxonomy carries most of the rejection load while existing nowhere in `strategy.md`.
   **It is a response to the ask, not a new rule, and it binds no later seat.**
