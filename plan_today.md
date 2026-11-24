# Today's Plan

**AGENT-OWNED. Written by the pre-market routine, consumed by the market-open routine,
overwritten daily.**

This file is the handoff between the two runs. The pre-market run does the thinking and
writes intents here; the market-open run executes them. Nothing gets bought that was not
written here first, which is what forces every buy to sleep on a written thesis instead of
being reasoned into existence at the moment of execution.

The market-open run **re-validates every intent against fresh quotes before acting**. An
intent written at 07:00 can be dead by 09:35 — an overnight gap can push a candidate past
the §4 4%-in-five-sessions priced-in threshold, in which case the trade is skipped and the
skip is logged. A stale intent is a proposal, not an instruction.

---

## Status

`plan_date` is load-bearing, not a comment. The market-open routine compares it to today's
ET date and **refuses to execute any intent from a plan not dated today**.

```
plan_date: 2026-11-24
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-24 at 09:30 ET** (`clock` 07:02:02 ET: `is_open: false`, `next_open`
`2026-11-24T09:30:00-05:00`, `next_close` `2026-11-24T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Tuesday of Thanksgiving week — today is an ordinary full session. ⚠ **Thursday 2026-11-26 is
Thanksgiving and Friday 2026-11-27 is an early close.** Do not plan a Thursday execution.

The plan this seat replaced was dated **2026-11-23** — the previous trading day, the ordinary
shape. It carried **zero intents**. **Nothing was lost: a plan with no intents has no
execution to perform.**

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT, NOT INHERITED.**
`week_anchor(2026-11-24)` → **2026-11-23** (imported from `common.py`, not hand-computed);
inherited `week_of` **2026-11-23**. They match, so `new_positions_this_week` stays at **0 of 3**.
⚠ The reset is done here rather than trusted to the Friday review, so a failed Friday run cannot
leave the §6 weekly cap stuck at its limit.

**Selftest 5/5, exit 0.** `trading_enabled: true`, LIVE against the paper account.

---

## Gate state — every §6 / §7 gate open, and no intent written anyway

| Gate | Reading | Blocks a buy? |
|---|---|---|
| §6 circuit breaker | **INACTIVE**, `consecutive_closed_losses` **0 of 3**, `halt_triggered_at: none` | No |
| §6 weekly cap | **0 of 3** new positions this week | No |
| §2 satellite sleeve | **0.00% deployed**, **$30,000.00** cash available | No |
| `control.md` `TRADING_ENABLED` | **true** | No |
| `control.md` Notes | **(none)** | No |
| `alerts.md` open incidents | **(none)** — nothing SYSTEMIC to flag | No |

⚠⚠ **THIS IS THE UNHALTED ZERO, AND THE DISTINCTION IS THE WHOLE POINT.** Nothing structural
prevented a position today. **Five candidates were researched and five were rejected on §3 and
§4's own tests.** A plan that is empty because the breaker is active and a plan that is empty
because nothing qualified are different facts about the system, and only one of them is a
successful run. **This is the second kind.**

---

## Account snapshot (pre-market mark — said once, not repeated per section)

- Equity **$95,255.67** · core **VOO** 99.046311231 sh @ 706.74 · market value **$65,255.67** ·
  unrealized **−$4,744.32 / −6.778%** · cash **$30,000.00**.
- Sleeves: **core 68.51% · satellite 0.00% · cash 31.49%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: 1423.30`.
- ⚠ **These are read off `current_price` 658.84 at 07:02 — a PRE-MARKET PRINT, not a close**
  (−0.78% on yesterday's official `bars` close of **664.01**). They will move before the bell.
  **The §2 band verdict is robust to that:** core reads **68.51%** pre-market and **68.67%** on
  yesterday's official close — both well inside 65–75%. The 65% floor breaks at VOO **562.51**
  and the 75% ceiling at **908.67** — both solved, not assumed (19500 = 0.35 × 99.046311231 × P;
  22500 = 0.25 × 99.046311231 × P). The floor is a further **−14.6%** from the pre-market mark.
- ⚠ **CORE −6.778% IS NOT A §5 EVENT.** §5 exempts core and §2 says core is not sold on news.
  Restated because the magnitude has recently sat past both the §5.3 and §5.4 thresholds and a
  fresh-clone seat reading only the P&L line could mistake it for a trigger.

---

## §2 REBALANCE — none due

`rebalance_needed: false`. Core **68.51%** sits inside the 65–75% band; `rebalance_delta` of
**$1,423.30** is the distance to the 70% *target*, not a breach of the band, and §2 rebalances on
the band, not the target. **No REBALANCE intent.** ⚠ The core is below target because it is down
6.8% from entry, not from drift worth chasing — buying to target here would be adding to the core
on weakness, which §2 does not ask for.

---

## SELL intents — none, and the reason is that there is nothing to sell

**Zero open satellite positions — 85th consecutive session.** `positions.md`
`grep -ci 'status: *open'` → **0**; `alpaca.py positions` returns **one** row, VOO
99.046311231 sh @ 706.74, the designated §2 core, **§5-exempt and deliberately untracked**
in `positions.md`. **The ledger and the broker agree; there was no disagreement to reconcile.**

⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING.** No entry price, no `highest_close`, no deadline and
no invalidation string exists anywhere in `positions.md`. **Step 4 therefore had NO OPERAND** —
no sell rule was evaluated because there is nothing to evaluate it against, which is **not** the
same as every rule having been checked and cleared. The midday seat must not read this as a
clean §5 pass.

**Nothing in limbo:** no open orders to inherit. No §7 exposure carried into today.

---

## BUY intents — NONE

**Five theses written, zero accepted** (`T-2026-11-24-01` … `-05`). Full reasoning in
`research_log.md`; the one-line dispositions:

| ID | Object | Died on |
|---|---|---|
| `-01` | Oracle's "OpenAI deal fully funded" statement → the AI-datacenter supply tier | **Part 1** — a confirmation that *previously outlined* financing is in place is not an event that moves a revenue line. The one new fact (vendor financing, customer prepayments) has the **wrong sign** for a supplier long. |
| `-02` | FDA's second CRL to Capricor for deramiocel → the DMD incumbent tier | **Part 1** — a rejection preserves the status quo and changes nobody's economics. **Third instance of this exact shape in three weeks.** |
| `-03` | Applied Digital's 150 MW / 18-year lease → the build-and-equip tier | **Part 2** — counterparty is "a tier-one investment-grade hyperscaler", unnamed; APLD is the first-order leg §4 excludes; no second-order supplier is named with a disclosed contract. |
| `-04` | DRC suspending cobalt exports (ARECOMS, 2026-11-23, effective 11-30) → US-listed cobalt producers | **Part 2** — **the best-shaped object of the day.** Died on materiality: no §3-eligible US-listed company has cobalt above 10% of revenue. One drill query spent; the source applied the kill. |
| `-05` | Sweep: eleven items disposed as one | §3 floors, immaterial values, unnamed counterparties, stale disclosure dates, and the standing no-Company-A macro object. |

⚠ **NO `move` CALL WAS MADE, AND THAT IS NOT A SKIPPED CHECK.** §4 orders the four thesis parts
*ahead of* the hard filters. Every candidate above died on part 1 or part 2, so no candidate ever
reached the priced-in filter. Spending `move` calls on names already dead would be theatre.
**There is consequently no `revalidate` line below, because there is no intent to revalidate.**

---

## What the market-open run should do

1. **Nothing to execute.** No BUY, no SELL, no REBALANCE intent. This plan is correctly dated
   `2026-11-24`, so the staleness guard will pass and find an empty instruction set — **that is
   the intended state, not a failure to parse.**
2. **Do not treat an empty plan as licence to improvise.** §4's thesis requirement runs through
   `plan_today.md`; a buy reasoned into existence at 09:35 is exactly what this handoff exists to
   prevent. If the open seat finds a candidate it likes, the place for it is tomorrow's plan.
3. **Re-read the §2 band off live prices anyway.** The verdict here is robust across a −14.6%
   move in VOO, but the band is a live test and the open seat owns it at the open.
4. **Confirm the ledger still agrees** (`positions` → one VOO row) before concluding §5 has no
   operand.
