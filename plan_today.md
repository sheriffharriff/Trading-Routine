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
plan_date: 2026-11-11
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-11 at 09:30 ET** (`clock` 07:02:17 ET: `is_open: false`, `next_open`
`2026-11-11T09:30:00-05:00`, `next_close` `2026-11-11T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**

⚠⚠ **AND TODAY IS THE DATE THAT RULE WAS WRITTEN FOR: 2026-11-11 IS VETERANS DAY. THE BOND
MARKET IS CLOSED AND THE EQUITY MARKET IS OPEN.** A seat reasoning from "federal holiday"
instead of from `next_open` would log a holiday skip over a full trading session — the one
failure in this routine that looks exactly like success. **`market_open_today: yes`.**

The plan this seat replaced was dated **2026-11-10** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

**WEEK ROLLOVER — NO ACTION DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W46**, weekday **3**; Monday anchor **2026-11-09** = the inherited `week_of`
**2026-11-09**. `new_positions_this_week` stays **0 of 3**. ⚠ **Recorded as re-derived rather
than skipped: §6's cap must not depend on any earlier seat having run.**

---

## ⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`. That was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Dispatches since: `08:47` (11-02) ·
`08:36` (11-03) · `08:35` (11-04) · `08:37` (11-05) · `08:37` (11-06) · `08:36` (11-09) ·
`08:36` (11-10) — **seven for seven, each read `is_open: false` and placed nothing.** This seat
dispatched at `07:02` against a nominal `08:00`: the same −1h, **eighth consecutive EST session.**

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED, CONFIRMED
CONDITION — NOT A NEW FAULT AND NOT A HOLIDAY.** Record the firing time and `is_open` as your
first line. `control.md` forbids diagnosing a schedule fault **from a firing time**; the
stored-schedule reading plus the DST calendar is different evidence.

**PROCEDURE IF YOU ARE THE OPEN SEAT AND THIS PLAN CARRIES ANY INTENT:** finish every
closed-market-safe step, **COMMIT AS INSURANCE** (say in the message that a hold is in progress
and what to backfill if the second commit never lands), poll `clock` until `is_open: true`,
then execute and commit again. **DO NOT log a skip over a non-empty plan.** Holding past the
bell is exactly what changes `is_open`, and routine 4 has now proved the hold **three times**
(11-06, 11-09, 11-10), recording the official close each time. ⚠ **This plan carries no
intents, so the procedure is not due today — it is written here because the day it IS due, the
seat will be reading this file and nothing else.**

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS WHAT
MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed seat over an empty
plan are byte-identical in output.** The ask is unchanged and is the human's alone:
**re-anchor all five triggers to `America/New_York`.** A flat +1h UTC shift is correct for EST
and **wrong again from 2027-03-14**, so it is a stopgap, not the fix.

---

## Intents

### BUY

**NONE.** Four broad Perplexity sweeps and one drill query spent; **five theses logged; zero
survived.**

New positions were **permitted throughout, and the absence of intents is a research outcome,
not a block**: breaker **INACTIVE 0/3** · `new_positions_this_week` **0 of 3** · satellite
sleeve **0.0% deployed** with **$30,000 cash** · `control.md` **Notes: (none)**. ⚠ **Nothing
stopped a buy except the candidates.**

**The day's best candidate was `T-2026-11-11-01` — Curtiss-Wright's >$140M of contracts from
General Dynamics Electric Boat — and it is the best-FORMED transaction this funnel has
surfaced in weeks: both parties NAMED, a dollar figure, a dated 8-K-grade press release, a
§3-eligible buyer and a §3-eligible seller.** ⚠⚠ **IT DIED BECAUSE THE THING THAT MADE IT
FINDABLE IS THE THING THAT DISQUALIFIES IT: a company announcing its own award is, by
construction, Company A.** The drill query then produced a **harder** kill than predicted —
performance runs **through 2030** (~16 quarters against §4's two), and ~$140M over that period
is **~$35M/yr against ~$3.8B of annualised revenue, ~0.9%**, more than ten times below §4's
materiality floor — and the figure is **not even allocable**, being split between Naval & Power
and Defense Electronics with no breakout. **No supplier TO Curtiss-Wright is named**, so the
second-order door is a blank.

**The entry most worth reading is `T-2026-11-11-02`, CoreWeave** — it raised its **own** FY2026
revenue guidance to **$13.0–13.3B from its own prior $12.4–13.2B**, a clean rule (iii) pass.
⚠⚠ **It died at part 1 on the 10-15 TSMC defect arriving in a new sector: THE FIGURE THAT MOVED
IS REVENUE, AND REVENUE HAS NO SUPPLIER CHAIN HANGING OFF IT. The figure a supplier thesis runs
on is capex, and no change to it was disclosed — so the mechanism needs "and also CoreWeave will
have to spend more", the second clause §4 forbids.** Apply rule (iii) to the figure the
mechanism runs on, not to the release.

See `research_log.md` `T-2026-11-11-01` … `-05`.

### SELL

**NONE — NO OPERAND.** `positions.md` satellite block count **0**; `alpaca.py positions` returns
**one row, core VOO only**. §5.1 and §5.2 were evaluated and have nothing to evaluate against:
all four sell rules are **ABSENT, NOT PASSING.** Core VOO is §5-exempt and was struck from the
working list rather than stamped as passing. **Zero §5.1 Perplexity calls were spent, because
there is no position to check news on.** **74th consecutive seat with an empty ledger.**

### REBALANCE

**NONE.** `sleeves` 07:02 ET: equity **$98,901.57** · core **VOO $68,901.57 = 69.67%** ·
satellite **$0 / 0.0% / count 0** · cash **$30,000.00 = 30.33%** · `core_in_band: true` ·
`rebalance_needed: false` · `rebalance_delta: 329.53`. **69.67% sits 4.67pp inside the 65%
edge.**
⚠ **Band distance in VOO terms, CARRIED NOT RE-DERIVED: the 65% floor needs VOO **562.51** and
the 75% ceiling **908.67** — identical to 11-06, 11-09 and 11-10 **by construction**, because
the threshold is a function of the INERT CASH LEG ALONE (`cv = t·cash/(1−t)`, then `÷ qty`) and
does not move with the mark. The 11-09 seat's wrong first draft (563.42 / 910.14) came from
re-deriving it.** **NO REBALANCE DUE.**

---

## Revalidate

Nothing to revalidate — **no BUY intents.** The `revalidate` line names the specific number an
overnight gap could invalidate, and with no intent there is no number.

⚠ **One standing instruction that is NOT an intent:** if you execute nothing today, that is
correct and expected on this plan. Do **not** read an empty intent list as licence to construct
a trade at the point of execution — §4 requires the written thesis to pre-date the order, and
**no thesis dated today survived.**

⚠ **NO SCHEDULED PRINT LANDS BETWEEN THIS SEAT AND THE OPEN.** October CPI **printed overnight**
and is now an outcome rather than an estimate: headline **+0.4% m/m**, core **+0.3%**, both
**above** the +0.3% / +0.2% consensus the 11-10 plan carried as estimates. Futures moved to a
**near-certain December 25bp hike with ~15% on 50bp**; the **2-year rose 17bp to 4.73%** and the
**10-year 10bp to 4.98%**. PPI follows **11-13**. ⚠ **All of it is logged at
`T-2026-11-11-04` as the standing government-action object — NO Company A, no named recipient,
and NOT a reason to pre-position or to skip anything.**

---

## Carry to the open seat

- **✅ NO BACKFILL IS DUE — THIRD SESSION RUNNING.** The 11-10 close seat held past the bell and
  committed the official **VOO close 689.415** (1,671 prints, `adjustment=all`).
  ⚠⚠ **THE BROKER/BAR SERIES IS NOW LABELLED, WHICH WAS THE 11-10 CLOSE SEAT'S OWN DIRECTION
  AFTER IT RETIRED THE OLD ONE AS MIXED. SERIES A — `lastday_price` vs the PRIOR session's
  committed bar — opens today at broker **689.50** vs committed **689.415** = **+$0.085**. ONE
  POINT IS NOT A SERIES AND NO TREND IS CLAIMED. SERIES B — `current_price` vs the SAME
  session's bar — cannot be read pre-market and is empty.** ⚠ **Do not "correct" the committed
  689.415 toward the broker figure; the bar close is the official print.**
- **Ledger reconciliation CLEAN, re-derived at this seat three independent ways, not inherited:**
  `positions.md` satellite count **0** · `sleeves satellite.count 0` · `positions` core-only.
  Core VOO **99.046311231 sh @ 706.74**, cost basis **$69,999.99**, unchanged since the
  2026-09-03 fill; only the mark moves. Mark **695.65** (pre-market, not a close); unrealised
  **−$1,098.42 / −1.5690%**. ⚠ **That figure equals the whole-account drawdown from $100,000 to
  the cent (−$1,098.43) for the sixth session running, because the cash leg has never moved.**
- **⚠⚠ THE §1 SHORTFALL IS A STANDING, MEASURED STRUCTURAL FINDING AND IT IS THE HUMAN'S CALL,
  NOT A SEAT'S.** With satellite at **0.0%** and $30,000 inert, the account captures only
  **69.67%** of any index move and **cannot beat the benchmark on any up session.** ⚠⚠ **THE
  11-10 CLOSE SEAT MEASURED BOTH SIGNS OF THE SAME STRUCTURE WITHIN 24 HOURS AND THE PAIR IS THE
  WHOLE ARGUMENT: on 11-09 the structure COST 0.728pp on an up day (VOO +2.3535% vs account
  +1.6253%); on 11-10 it APPEARED to EARN +0.1107pp on a down day (VOO −0.3635% vs account
  −0.2528%) — and weight × VOO move predicted the account's move TO FOUR DECIMAL PLACES, so the
  "outperformance" was cash drag with the sign flipped and nothing else. LOWER BETA IS NOT
  ALPHA.** ⚠ **Recorded as the measured price of 74 honest no-trade seats, EXPLICITLY NOT as an
  argument for lowering §4's bar — manufacturing a thesis to close this gap is the one response
  that makes it worse.**
- **⚠⚠ THE DIRECTION-BLIND `move` DEFECT — THREE NEW INSTANCES TODAY, TAKING IT TO SIXTEEN, AND
  TODAY IS THE FIRST TIME ALL THREE READINGS WERE DECLINES.** `CW` **−3.93%** → `priced_in:
  false` "passes" · `CRWV` **−9.29%** → `priced_in: true` "LATE — skip" · `VG` **−7.77%** →
  "LATE — skip". ⚠ **The script thresholds ABSOLUTE 5-session magnitude, so a FALLING stock reads
  as "the market has already moved on this news". OBEY IT ANYWAY — it fails safe, over-blocking
  and never wrongly permitting — but NEVER quote such a reading as "the upside is captured";
  it has meant the reverse sixteen times.** ⚠ **IMMATERIAL TODAY, AND SAY SO RATHER THAN IMPLY
  IT: all three names died at part 1, 2 or 3 before the filter could decide anything.** Fix is a
  **signed** threshold in `scripts/alpaca.py`: script-level, **not a seat's to install.** Human
  notified 11-03, 11-05, 11-06, 11-09, 11-11.
- **⚠ RULE (iv) ROLL-CALL FOR THE NEXT SEAT, so no drill query is wasted re-deriving a written
  answer:** **Venture Global** returned for its **FOURTH** appearance today (`T-2026-11-11-03`)
  and **the standing roll-call predicted it by name — "expect this issuer again; the answer is
  already written." It was, and zero queries were spent on it, which is what the roll-call is
  FOR.** ⚠ **One thing DID change and it is worth carrying: the three prior VG deaths were all
  part 3 / rule (vi) on long-dated contracting, and this one — a plant entering commercial
  operation — is NOT long-dated. The kill moved UP a rung to part 1. A kill moving is real news
  about the issuer; it still produced no candidate.** **The AI-infrastructure complex is at
  FIVE consecutive sessions** (11-05 the unwind · 11-06 IREN/QCOM · 11-09 sovereign-AI · 11-10
  AAON/AAOI · 11-11 CRWV), dead at part 1 or 2 every time, **through four different disclosure
  types.** ⚠ **A ticker or complex that keeps arriving and keeps dying the same death is telling
  you about its industry's DISCLOSURE PRACTICE, not about a candidate maturing.**
- **⚠ NEW TODAY, AND IT IS A ONE-CLAUSE CHANGE TO THE SWEEP THAT PAID FOR ITSELF TWICE:** two of
  the three cheapest kills were **VOLUNTEERED BY THE SOURCES** once the query asked for the
  **disclosure** date rather than accepting the publication date — **Freeport's $4.5B Bagdad
  expansion was announced 11-04** and **Lydian's Faraday battery plant has been operating since
  09-18**, both surfaced as fresh by a `--recency day` sweep. ⚠ **A SWEEP WINDOW IS NOT A
  DISCLOSURE DATE. Ask for the disclosure history in the sweep itself; it costs one clause and
  it killed two items before a mechanism was attempted.**
