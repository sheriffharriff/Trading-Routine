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
plan_date: 2026-11-09
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-09 at 09:30 ET** (`clock` 07:02:15 ET: `is_open: false`, `next_open`
`2026-11-09T09:30:00-05:00`, `next_close` `2026-11-09T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**

The plan this seat replaced was dated **2026-11-06** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

**✅ WEEK ROLLOVER DONE AT THIS SEAT.** ISO **2026-W46**, weekday **1**; Monday anchor
**2026-11-09** ≠ the inherited `week_of` **2026-11-02**. `week_of` advanced and
`new_positions_this_week` reset to **0**. ⚠ **Recorded as PERFORMED, not as unnecessary: it
was already 0, but §6's cap must not depend on the Friday seat having run.**

---

## ⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`. That was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Dispatches since: `08:47` (11-02) ·
`08:36` (11-03) · `08:35` (11-04) · `08:37` (11-05) · `08:37` (11-06) — **five for five, each
read `is_open: false` and placed nothing.** This seat dispatched at `07:02` against a nominal
`08:00`: the same −1h.

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED, CONFIRMED
CONDITION — NOT A NEW FAULT AND NOT A HOLIDAY.** §7 forbids trading a closed market, so
**placing nothing is CORRECT.** Record the firing time and `is_open` as your first line, log
the skip, commit. `control.md` forbids diagnosing a schedule fault **from a firing time**; the
stored-schedule reading plus the DST calendar is different evidence.

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS WHAT
MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed seat over an empty
plan are byte-identical in output. The day this plan carries a BUY, the trade simply will not
happen, and nothing in the order count will say why.** **Sixth consecutive EST session in that
condition.**

⚠ **ONE THING THE 11-06 CLOSE SEAT PROVED AND THIS SEAT INHERITED CLEAN: the pre-CLOSE half of
this fault IS self-mitigable — that seat held past the bell and committed the official close, so
this Monday needed NO backfill, the first time in the fault's history.** **It does not help
routine 2: waiting 53 minutes for the open is available, but §7's bar on a closed market is
what blocks execution, and holding does not change `is_open`.** The ask is unchanged and is the
human's alone: **re-anchor all five triggers to `America/New_York`.**

---

## Intents

### BUY

**NONE.** Four broad Perplexity sweeps and one drill query spent; **five theses logged; zero
survived.**

New positions were **permitted** and the absence of intents is a research outcome, not a block:
breaker **INACTIVE 0/3** · `new_positions_this_week` **0 of 3** (freshly rolled) · satellite
sleeve **0.0% deployed** with **$30,000 cash** · `control.md` **Notes: (none)**. Nothing stopped
a buy except the candidates.

⚠⚠ **THREE OF THE FOUR SWEEPS RETURNED AN EXPLICIT NIL.** No qualifying named supply agreement,
offtake, capacity expansion or purchase commitment by any US-listed company 11-06→11-09; an
explicit nil on FDA, FTC/DOJ/FCC/EPA, plant closures, strikes and recalls; and the structural
sweep — which required **one source sentence carrying both the dollar figure and the name of the
company receiving it** — answered *"No qualifying disclosure was identified."*

**The day's best candidate was `T-2026-11-09-01`, COHR, and it died four ways.** Coherent's
~$20B five-year PhotonLink agreement (disclosed 11-04) is large, dated, genuinely new and
carries an exact figure — but **the customer is unnamed** (rule (v)), **Coherent expanded its own
internal indium-phosphide capacity and names no external supplier** (rule (vii)), **revenue
"begins ramping in early calendar 2028"** — ~5 quarters before the ramp *starts*, against §4's
two-quarter ceiling — and the only real dollar path is **COHR's own revenue line**, i.e. the
first-order leg §4 exists to avoid. See `research_log.md` `T-2026-11-09-01` … `-05`.

### SELL

**NONE — no operand.** `positions.md` satellite block count **0**; `alpaca.py positions` returns
**one row, core VOO only**. §5.1 and §5.2 were evaluated and have nothing to evaluate against:
all four sell rules are **ABSENT, NOT PASSING.** Core VOO is §5-exempt and was struck from the
working list rather than stamped as passing. **Zero §5.1 Perplexity calls were spent, because
there is no position to check news on.**

### REBALANCE

**NONE.** `sleeves` 07:02 ET: equity **$97,368.33** · core **VOO $67,368.33 = 69.19%** ·
satellite **$0 / 0.0% / count 0** · cash **$30,000 = 30.81%** · `core_in_band: true` ·
`rebalance_needed: false` · `rebalance_delta: 789.50`. **69.19% sits 4.19pp inside the 65%
edge.** ⚠ **Band distance in VOO terms, COMPUTED IN A SCRIPT: the 65% floor needs VOO 562.51
(−17.30% from 680.17) and the 75% ceiling 908.67 (+33.59%).** ⚠⚠ **THIS SEAT'S FIRST DRAFT OF
THIS LINE SAID "≈563.42 / ≈910.14", WRITTEN FROM INTENT BEFORE THE SCRIPT RAN, AND BOTH FIGURES
WERE WRONG — REPLACED HERE, NOT LEFT BESIDE THEIR CORRECTION. The threshold is a function of the
INERT CASH LEG ALONE (`cv = t·cash/(1−t)`, then `÷ qty`), so it does NOT move with the mark and
is identical to the 11-06 figures. A seat that re-derives it per-session is inviting the error
this line just made.**
**NO REBALANCE DUE.**

---

## Revalidate

Nothing to revalidate — **no BUY intents.** The `revalidate` line names the specific number an
overnight gap could invalidate, and with no intent there is no number.

⚠ **One standing instruction that is NOT an intent:** if you execute nothing today, that is
correct and expected on this plan. Do **not** read an empty intent list as licence to construct
a trade at the point of execution — §4 requires the written thesis to pre-date the order, and
**no thesis dated today survived.**

⚠ **Two scheduled macro prints land after this seat and are NOT reasons to pre-position:**
October **CPI on 11-10** and **PPI on 11-13**. A reported ~**75%** implied probability of a
December Fed hike is quoted **with its provenance and is not treated as established** — the
11-06 seat logged two contradictory answers from this same model on this same question.

---

## Carry to the open seat

- **✅ NO BACKFILL IS DUE AND THIS IS THE FIRST MONDAY THAT HAS BEEN TRUE.** The 11-06 close seat
  held past the bell and committed the official **VOO close 676.02**. Broker `lastday_price` reads
  **675.99**, 3¢ below it — inside the known moving broker/bar midpoint, requiring nothing. ⚠ **Do
  not "correct" the committed 676.02 toward the broker figure; the bar close is the official print.**
- **Ledger reconciliation CLEAN, re-derived at this seat, not inherited:** three independent sides
  agree on zero satellites (`positions.md` count 0 · `sleeves satellite.count 0` · `positions`
  core-only). Core VOO 99.046311231 sh @ 706.74, cost basis $69,999.99, unchanged since the
  2026-09-03 fill; only the mark moves. Unrealised **−$2,631.66 / −3.76%** at 680.17.
- **⚠⚠ THE DIRECTION-BLIND `move` DEFECT REACHED A NON-SEMICONDUCTOR NAME TODAY — THIRTEENTH
  INSTANCE.** `move --symbol COHR --sessions 5` returns **−8.32%** (210.28 → 192.79) and verdicts
  `priced_in: true` / *"LATE — skip"*. **COHR FELL**; one source headline reads *"Coherent sinks
  16% despite $20B"*. The script thresholds **absolute** magnitude, so a decline reads as late.
  ⚠ **THIS SEAT DID NOT LEAN ON THAT VERDICT — the thesis was already dead at part 3 and rule (v),
  and the filter is recorded as having answered the wrong question rather than as having saved the
  run.** ⚠ **OBEY IT ANYWAY: it fails safe, over-blocking and never wrongly permitting. And NEVER
  quote such a reading as "the market has captured this upside" — it has now meant the reverse
  thirteen times.** Fix is a **signed** threshold in `scripts/alpaca.py` — script-level, **not a
  seat's to install.** Human notified 11-03, 11-05, 11-06 and today.
- **⚠ `T-2026-11-09-03` added an instance, NOT a new rule, and the distinction is deliberate.** The
  Children's Place Chapter 11 names its three liquidation consultants (GA Group, Tiger Group, SB360
  Capital) — **all private.** That is rule (viii)'s existing private-recipient shape (GEHC/Sofie),
  arriving with three named recipients at once. ⚠ **An ANSWERED blank with no listed occupant is a
  cleaner kill than an unnamed tier. A seat must not promote it to a new standing rule.**
- **⚠ NVDA is at THREE appearances in four sessions** (11-05 unwind · 11-06 IREN · 11-09 the
  SK Telecom / Rebellions sovereign-AI collaboration), dead at part 1 then part 2 twice. **Rule
  (iv): expect it again. NVIDIA announces COLLABORATIONS — frameworks without figures — and the
  answer is already written.** Do not spend a drill query asking who supplies an unnamed tier.
