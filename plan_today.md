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
plan_date: 2026-11-10
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-10 at 09:30 ET** (`clock` 07:01:59 ET: `is_open: false`, `next_open`
`2026-11-10T09:30:00-05:00`, `next_close` `2026-11-10T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**

The plan this seat replaced was dated **2026-11-09** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

**WEEK ROLLOVER — NO ACTION DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W46**, weekday **2**; Monday anchor **2026-11-09** = the inherited `week_of`
**2026-11-09**. `new_positions_this_week` stays **0 of 3**. ⚠ **Recorded as re-derived rather
than skipped: §6's cap must not depend on any earlier seat having run.**

---

## ⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`. That was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Dispatches since: `08:47` (11-02) ·
`08:36` (11-03) · `08:35` (11-04) · `08:37` (11-05) · `08:37` (11-06) · `08:36` (11-09) —
**six for six, each read `is_open: false` and placed nothing.** This seat dispatched at `07:02`
against a nominal `08:00`: the same −1h, **seventh consecutive EST session.**

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED, CONFIRMED
CONDITION — NOT A NEW FAULT AND NOT A HOLIDAY.** Record the firing time and `is_open` as your
first line. `control.md` forbids diagnosing a schedule fault **from a firing time**; the
stored-schedule reading plus the DST calendar is different evidence.

⚠⚠⚠ **CORRECTED 2026-11-09 AND THIS COPY NOW CARRIES THE CORRECTION RATHER THAN THE ERROR:
the previous version of this file said *"holding does not change `is_open`."* **THAT IS FALSE.**
Holding past 09:30 is exactly what changes it, and routine 4 has now proved the hold **twice**
(11-06 and 11-09), recording the official close both times.
⚠⚠ **PROCEDURE IF YOU ARE THE OPEN SEAT AND THIS PLAN CARRIES ANY INTENT: finish every
closed-market-safe step, **COMMIT AS INSURANCE** (say in the message that a hold is in progress
and what to backfill if the second commit never lands), poll `clock` until `is_open: true`,
then execute and commit again. DO NOT log a skip over a non-empty plan.** ⚠ **This plan carries
no intents, so the procedure is not due today — it is written here because the day it IS due,
the seat will be reading this file and nothing else.**

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS WHAT
MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed seat over an empty
plan are byte-identical in output.** The ask is unchanged and is the human's alone:
**re-anchor all five triggers to `America/New_York`.** A flat +1h UTC shift is correct for EST
and **wrong again from 2027-03-14**, so it is a stopgap, not the fix.

---

## Intents

### BUY

**NONE.** Four broad Perplexity sweeps and one drill query spent; **six theses logged; zero
survived.**

New positions were **permitted throughout, and the absence of intents is a research outcome,
not a block**: breaker **INACTIVE 0/3** · `new_positions_this_week` **0 of 3** · satellite
sleeve **0.0% deployed** with **$30,000 cash** · `control.md` **Notes: (none)**. ⚠ **Nothing
stopped a buy except the candidates.**

⚠⚠ **THREE OF THE FOUR SWEEPS RETURNED AN EXPLICIT NIL.** The transaction sweep — both parties
named **and** a figure — returned *"no qualifying announcement was identified."* The structural
sweep, which required **one source sentence carrying both the dollar figure and the name of the
company RECEIVING it**, returned *"No qualifying disclosure was identified."* The
overnight-events sweep said the reporting *"does not support a reliable, comprehensive list of
major US corporate events for November 9–10, 2026."*

**The day's best candidate was `T-2026-11-10-01` — NASA's $10B CLPS 2 lunar award — and it had
more disclosed material than almost anything in this log: eight named companies, two §3-eligible
mega-caps (LMT, NOC), a ten-billion-dollar figure and a dated government award.** It died
because **no dollar was allocated to anyone**: NASA's own language is *"a 10-year, multiple-award
IDIQ master contract with a **combined maximum value** of $10 billion"*, and ispace-U.S. stated
the selection *"does not itself constitute a funded mission."* Even $10B ÷ 8 ÷ 10yr ≈ $125M/yr
is **~0.17% of LMT's revenue, ~60× below §4's materiality floor** — and that division is
invented, because the ceiling is not divisible. Rule (iii) rides on top: **announced 2026-11-07,
NASA release merely UPDATED 11-10**, so a sweep run today surfaces a three-day-old award as
fresh.

**The entry most worth reading is `T-2026-11-10-02`, AAON** — it raised its **own** FY
sales-growth guidance to **72–75% from its own prior 55–60%**, the cleanest rule (iii) pass in
weeks. It still died at **part 1**: a company disclosing that its own order book is bigger than
it said is **evidence of a condition that pre-dates the remark**, not an event, and the source
states **no named customer, no named supplier and no capex figure** appears in the release.
See `research_log.md` `T-2026-11-10-01` … `-06`.

### SELL

**NONE — NO OPERAND.** `positions.md` satellite block count **0**; `alpaca.py positions` returns
**one row, core VOO only**. §5.1 and §5.2 were evaluated and have nothing to evaluate against:
all four sell rules are **ABSENT, NOT PASSING.** Core VOO is §5-exempt and was struck from the
working list rather than stamped as passing. **Zero §5.1 Perplexity calls were spent, because
there is no position to check news on.** **70th consecutive seat with an empty ledger.**

### REBALANCE

**NONE.** `sleeves` 07:02 ET: equity **$98,589.57** · core **VOO $68,589.57 = 69.57%** ·
satellite **$0 / 0.0% / count 0** · cash **$30,000.00 = 30.43%** · `core_in_band: true` ·
`rebalance_needed: false` · `rebalance_delta: 423.13`. **69.57% sits 4.57pp inside the 65%
edge.**
⚠ **Band distance in VOO terms, COMPUTED IN A SCRIPT AND NOT RE-DERIVED FROM THE MARK: the 65%
floor needs VOO **562.51** and the 75% ceiling **908.67**.** ⚠⚠ **These are IDENTICAL to the
11-06 and 11-09 figures by construction, not by coincidence — the threshold is a function of the
INERT CASH LEG ALONE (`cv = t·cash/(1−t)`, then `÷ qty`), so it does NOT move with the mark.
There is nothing here to re-derive, and the 11-09 seat's wrong first draft (563.42 / 910.14) came
from re-deriving it.** **NO REBALANCE DUE.**

---

## Revalidate

Nothing to revalidate — **no BUY intents.** The `revalidate` line names the specific number an
overnight gap could invalidate, and with no intent there is no number.

⚠ **One standing instruction that is NOT an intent:** if you execute nothing today, that is
correct and expected on this plan. Do **not** read an empty intent list as licence to construct
a trade at the point of execution — §4 requires the written thesis to pre-date the order, and
**no thesis dated today survived.**

⚠⚠ **ONE SCHEDULED PRINT LANDS BETWEEN THIS SEAT AND THE OPEN, AND IT IS NOT A REASON TO
PRE-POSITION OR TO SKIP ANYTHING: October CPI is released TODAY.** Consensus was headline
**+0.3% m/m** (from 0.6%) and core **+0.2%** (from 0.3%) — ⚠ **those are ESTIMATES, the source
said so explicitly, and this seat has NOT seen the print. Do not quote them as outcomes.** PPI
follows **11-13**. A reported ~75% implied probability of a December Fed hike is carried **with
its provenance and is NOT treated as established** — the 11-06 seat logged two contradictory
answers from this same model on this same question minutes apart.

---

## Carry to the open seat

- **✅ NO BACKFILL IS DUE — SECOND SESSION RUNNING, THE FIRST BACK-TO-BACK PAIR IN THIS FAULT'S
  HISTORY.** The 11-09 close seat held past the bell and committed the official **VOO close
  691.93** (2,880 prints, `adjustment=all`). Broker `lastday_price` reads **691.87**, **6¢ below
  it** — inside the known moving broker/bar midpoint, requiring nothing. ⚠ **Do not "correct" the
  committed 691.93 toward the broker figure; the bar close is the official print.** Broker/bar gap
  series now **$0.02 · $0.03 · $0.45 · $0.21 · −$0.06** (11-04/05/06/09/10) — ⚠ **the fifth
  reading is the FIRST NEGATIVE ONE, which settles it: a moving midpoint, not an offset, and not
  correctable in either direction.**
- **Ledger reconciliation CLEAN, re-derived at this seat three independent ways, not inherited:**
  `positions.md` satellite count **0** · `sleeves satellite.count 0` · `positions` core-only.
  Core VOO **99.046311231 sh @ 706.74**, cost basis **$69,999.99**, unchanged since the
  2026-09-03 fill; only the mark moves. Mark **692.50**; unrealised **−$1,410.42 / −2.0149%**.
  ⚠ **That dollar figure equals the whole-account drawdown to the cent (−$1,410.43) for the fifth
  session running, because the cash leg has never moved.**
- **⚠⚠ THE §1 SHORTFALL IS A STANDING, MEASURED STRUCTURAL FINDING AND IT IS THE HUMAN'S CALL,
  NOT A SEAT'S.** With satellite at **0.0%** and $30,000 inert, the account captures only
  **69.57%** of any index move and **cannot beat the benchmark on any up session.** The 11-09
  close measured the cost at **0.728pp in one session** (VOO +2.3535% vs account +1.6253%).
  ⚠ **Recorded as the measured price of 70 honest no-trade seats, EXPLICITLY NOT as an argument
  for lowering §4's bar — manufacturing a thesis to close this gap is the one response that makes
  it worse.**
- **⚠⚠ THE DIRECTION-BLIND `move` DEFECT — NO NEW INSTANCE TODAY, AND THE REASON IS WORTH
  STATING: ZERO `move` CALLS WERE SPENT THIS RUN, because every candidate died at part 1, 2 or 3
  before a hard filter was due.** The defect stands at **thirteen** instances. ⚠ **If you reach
  the priced-in check on anything: the script thresholds ABSOLUTE 5-session magnitude, so a
  DECLINE reads as `priced_in: true` / "LATE — skip". OBEY IT ANYWAY — it fails safe, over-blocking
  and never wrongly permitting — but NEVER quote such a reading as "the market has captured this
  upside"; it has meant the reverse thirteen times.** Fix is a **signed** threshold in
  `scripts/alpaca.py`: script-level, **not a seat's to install.** Human notified 11-03, 11-05,
  11-06, 11-09.
- **⚠ RULE (iv) ROLL-CALL FOR THE NEXT SEAT, so no drill query is wasted re-deriving a written
  answer:** **NVDA** is at **four appearances in five sessions** (11-05 unwind · 11-06 IREN ·
  11-09 SK Telecom/Rebellions · 11-10 the Huang governance story) — dead at part 1 or part 2 every
  time. **RDW** returned today inside rule (v)'s CEILING sub-shape, **the very shape its own
  "$980M" ceiling was first used to illustrate.** **Venture Global** reported earnings today and
  is at **three prior appearances**, dead on part 3 / rule (vi) all three times. ⚠ **A ticker that
  keeps arriving and keeps dying the same death is telling you about its industry's disclosure
  practice, not about a candidate maturing.**
- **⚠ NEW TODAY, FOR THE FUNNEL'S FDA RANGE — the first REJECTION and the first COMPETITIVE
  ENTRANT.** `T-2026-11-10-03`: Novocure's Optune Mya was **declined**, and a rejection creates
  **nothing** — it preserves the status quo, so no incumbent's economics changed on any date.
  `T-2026-11-10-04`: Bayer's asundexian was **approved**, and its only second-order read
  (incumbent DOAC franchises) has the **WRONG SIGN for a long-only book.** ⚠ **The range now has
  three points: a first approval creates a chain, an expanded indication creates nothing, and a
  competitive entrant destroys incumbent economics. Only the first can produce a §4 candidate.**
