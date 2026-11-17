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
plan_date: 2026-11-17
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-17 at 09:30 ET** (`clock` 07:02:09 ET: `is_open: false`, `next_open`
`2026-11-17T09:30:00-05:00`, `next_close` `2026-11-17T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Tuesday, an ordinary full session.

The plan this seat replaced was dated **2026-11-16** — the previous trading day, the ordinary
shape. It carried **zero intents**, and `git log` confirms no `2-market-open` commit consumed
it. **Nothing was lost: a plan with no intents has no execution to perform.**

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W47**, weekday **2**; Monday anchor **2026-11-16** = the inherited `week_of`
**2026-11-16**. `new_positions_this_week` stays **0 of 3**.

---

## ⚠⚠ READ THIS FIRST — WHAT THE OPEN SEAT SHOULD EXPECT

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`, which was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Nine consecutive sessions (11-02 →
11-12) dispatched between `08:35` and `08:47`, each reading `is_open: false` and placing
nothing. **11-13 fired at 10:43 with `is_open: true`. 11-16 did not fire at all** — `git log`
confirms three commits for that date (07:08 pre-market, 11:44 midday, 15:22/16:05 close) and
**no `2-market-open` commit at any hour**, the first whole-session absence. That was settled by
the 11-16 close seat, not merely suspected.

⚠ **PRACTICAL CONSEQUENCE FOR THE OPEN SEAT: `is_open` could read either way today, and so
could a total absence. ALL THREE ARE EXPECTED. Record your firing time and `is_open` as your
first line, and do not treat `false` as a holiday or as a new fault.** This seat itself
dispatched at **07:02** against a nominal `08:00` — the same −1h shape, **fourteenth
consecutive EST session**. ⚠ Per `control.md` this is **recorded, not diagnosed**: a firing time
is not a schedule diagnosis, and manual "Run now" invocations are indistinguishable from
scheduled ones.

⚠⚠ **STATUS OF THE ASK: DELIVERED AND RE-SENT. DO NOT RE-SEND AGAIN.** The 11-12 close seat
sent the fault out of band by push notification; the 11-16 close seat re-sent it on the
condition the 11-12 carry-forward named explicitly (*"or if a seat is skipped entirely"*).
**It is now with the human and nothing has changed since.** Re-send only if routine 2 begins
firing consistently *after the bell* in a way that changes what the human must fix. **A second
whole-session absence is NOT new information and does not warrant re-interrupting anyone.**

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

Four theses were written and all four rejected — `T-2026-11-17-01` through `-04`, the last a
fifteen-item sweep. Full reasoning in `research_log.md`. The two that cost a drill query each:

- **`T-2026-11-17-01`** — the BIS interim final rule (first disclosed **11-16**) licensing
  advanced AI-chip shipments to data centres in Singapore/Thailand/Malaysia/Indonesia/Brazil,
  plus a 90-day clock on overseas facilities serving China/Macau-headquartered customers.
  **A real government action with a named authority — and it died on DIRECTION:** every
  §3-eligible beneficiary (the global colocation names) carries the very Asia-Pacific book the
  rule encumbers, so the net sign is undetermined and no source quantifies either leg.
- **`T-2026-11-17-02`** — ExxonMobil's **Longtail** FID (**11-17**, $12.5B project): SBM
  Offshore awarded the FPSO, Saipem the SURF scope at up to $1.5B. **The best-formed event of
  the window — fresh, dated, operator-named, quantified — and §3 killed it in one line:** SBM is
  **Amsterdam-listed**, Saipem is **Milan-listed**, the source states **zero equipment suppliers
  are named**, and the only US-listed party is **ExxonMobil, which is paying the capex out**.
  Part 3 is ~16 quarters out besides.

**NOTHING FOR THE OPEN SEAT TO REVALIDATE.** `revalidate` lines exist to catch an overnight gap
pushing a candidate past the §4 priced-in threshold between 08:00 and 09:35. **With zero BUY
intents there is no number to re-check, and no `move` call is owed.** ⚠ **Do not read the
absence of a `revalidate` line as an oversight — the priced-in check was not run once this
session because no candidate reached the hard filters** (second consecutive session).

## SELL intents

**NONE. Zero SELL intents — NO OPERAND, not a pass.**

The satellite sleeve holds **zero positions** and always has. `alpaca.py positions` returns
exactly one row, the **VOO core** holding, which is **exempt from §5 entirely** — core is not
sold on news. §5.1 through §5.4 were therefore **not evaluated and could not be**: there is no
entry price, no `highest_close`, no deadline and no invalidation string in existence.

⚠ **`sell_rule_status` in `positions.md` reads ABSENT, not PASSING.** A rule that cannot fire
for want of a position is not a rule that was checked and cleared, and the two must not be
allowed to look alike to the next reader.

## REBALANCE intents

**NONE. Core is in band.**

`alpaca.py sleeves` at 07:02: equity **$97,440.08** · core **VOO $67,440.08 = 69.21%** ·
satellite **0.00%** · cash **$30,000.00 = 30.79%**. `core_in_band: true`,
`rebalance_needed: false`.

⚠ **`rebalance_delta: 767.98` IS A DISTANCE READOUT, NOT AN ORDER.** It is how far core sits
from its exact 70% target value, which §2 does not require it to hit. The band is **65–75%** and
core has **4.21pp of room to the floor**. **Do not buy $767.98 of VOO because this field is
non-zero.**

---

## Notes for the open seat

1. **Yesterday's official close is confirmed at VOO 680.36** (`bars`, 2026-11-16). ⚠ **The
   endpoint disagreement is live again, third distinct instance:** `positions.lastday_price`
   reads **680.26** against the official bar close **680.36** — gap **0.10 / 0.0147%**, narrower
   than the 11-13 reading (+0.33) and the 11-16 post-bell reading (0.27), but present. **Build
   P&L from official `bars` closes only.** A `highest_close` stamped from `lastday_price` and
   compared against a `bars` close manufactures a phantom move at the 0.01–0.05% scale.
2. **`bars` returned NO 2026-11-17 row**, consistent with a pre-market pull. The in-progress-bar
   defect is therefore not in play at this hour — but **gate any high-water write on `clock`,
   never on the shape of the bar**, because a mid-session pull does return the unfinished
   session as a bar.
3. **No open incidents.** `alerts.md` carries nothing OPEN and nothing SYSTEMIC.
4. **The corpus-size finding is unchanged and still needs the human, not a run.**
   `positions.md` is ~317KB describing an empty ledger and is unreachable by the monthly
   rollover. **No run has standing to truncate it.** This seat added the shortest digest it
   could rather than rewriting other seats' prose, and **claims no collapse ratio.**
