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
plan_date: 2026-11-25
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-25 at 09:30 ET** (`clock` 07:01:52 ET: `is_open: false`, `next_open`
`2026-11-25T09:30:00-05:00`, `next_close` `2026-11-25T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Wednesday of Thanksgiving week — today is an ordinary full session.

⚠⚠ **THURSDAY 2026-11-26 IS THANKSGIVING AND FRIDAY 2026-11-27 IS AN EARLY CLOSE — AND THAT
CALENDAR IS STILL INHERITED, NOT VERIFIED.** No seat has confirmed it against the broker.
**Check `clock` on the day**, and do not read Thursday's `is_open: false` as the pre-market
signature.

The plan this seat replaced was dated **2026-11-24** — the previous trading day, the ordinary
shape. It carried **zero intents**. **Nothing was lost: a plan with no intents has no
execution to perform.**

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT, NOT INHERITED.**
`week_anchor(2026-11-25)` → **2026-11-23** (imported from `common.py`, not hand-computed);
inherited `week_of` **2026-11-23**. They match, so `new_positions_this_week` stays at **0 of 3**.
⚠ The reset is done here rather than trusted to the Friday review, so a failed Friday run cannot
leave the §6 weekly cap stuck at its limit. ⚠ **Thursday is a holiday and Friday a half day, so
this week's cap will almost certainly expire unused — that is not a reason to spend it.**

**Selftest 5/5, exit 0.** `trading_enabled: true`, LIVE against the paper account.

⚠ **This seat fired ~07:02 for an 08:00 slot (~58 min early).** Per `control.md`, manual
"Run now" invocations are indistinguishable from scheduled ones in run logs, so this is
**recorded, not diagnosed as a schedule fault.** **It is benign for this routine** — routine 1
places no orders and the only cost is that the "last 24 hours" research window starts an hour
earlier. ⚠ **It is NOT benign for routine 2**, which has fired ~08:36 for 09:35 twice; see
`state.md` carry-forward.

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
prevented a position today. **Five theses were written and five were rejected on §3 and §4's own
tests.** A plan that is empty because the breaker is active and a plan that is empty because
nothing qualified are different facts about the system, and only one of them is a successful run.
**This is the second kind.**

---

## Account snapshot (pre-market mark — said once, not repeated per section)

- Equity **$94,185.06** · core **VOO** 99.046311231 sh @ 706.74 · market value **$64,185.06** ·
  unrealized **−$5,814.93 / −8.307%** · cash **$30,000.00**.
- Sleeves: **core 68.15% · satellite 0.00% · cash 31.85%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: 1744.48`.
- ⚠ **These are read off `current_price` 648.0308 at 07:02 — a PRE-MARKET PRINT, not a close**
  (**−1.913%** on yesterday's official `bars` close of **660.67**). They will move before the
  bell. **The §2 band verdict is robust to that:** core reads **68.148%** on the pre-market mark
  and **68.566%** on yesterday's official close — both well inside 65–75%. The 65% floor breaks
  at VOO **562.51** and the 75% ceiling at **908.67** — both **re-solved at this seat, not
  copied** (19500 = 0.35 × 99.046311231 × P; 22500 = 0.25 × 99.046311231 × P). The floor is a
  further **−13.20%** from the pre-market mark.
- ⚠⚠ **CORE −8.307% IS NOT A §5 EVENT.** §5 exempts core outright and §2 says core is not sold on
  news. **Restated prominently because the magnitude now sits past BOTH the §5.3 −7% figure and
  within reach of §5.4's −10%**, and a fresh-clone seat reading only the P&L line could mistake
  it for a trigger. **It is not one. Do not sell core.**
- ⚠ **ENDPOINT DISAGREEMENT, SAID ONCE:** `positions.lastday_price` **660.71** vs the official
  `bars` close **660.67** for 2026-11-24 = **0.04 / 0.0061%**, which **ties the narrowest value
  in the recorded 0.04–1.41 spread.** ⚠ **No `bars` call was spent today** — none was owed, and
  one must not be spent merely to extend a tally. Figures above are built from the inherited
  official close, not re-pulled.

---

## §2 REBALANCE — none due

`rebalance_needed: false`. Core **68.15%** sits inside the 65–75% band; `rebalance_delta` of
**$1,744.48** is the distance to the 70% *target*, not a breach of the band, and §2 rebalances on
the band, not the target. **No REBALANCE intent.** ⚠ The core is below target because it is down
8.3% from entry, not from drift worth chasing — buying to target here would be adding to the core
on weakness, which §2 does not ask for. ⚠ **Re-read the band off live prices at the open anyway:**
the verdict here survives a −13.2% move in VOO, but the band is a live test and the open seat
owns it.

---

## SELL intents — none, and the reason is that there is nothing to sell

**Zero open satellite positions — 86th consecutive session.** `positions.md`
`grep -ci 'status: *open'` → **0**; `alpaca.py positions` returns **one** row, VOO
99.046311231 sh @ 706.74, the designated §2 core, **§5-exempt and deliberately untracked**
in `positions.md`. **The ledger and the broker agree; there was no disagreement to reconcile.**

⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING.** No entry price, no `highest_close`, no deadline and
no invalidation string exists anywhere in `positions.md`. **Step 4 therefore had NO OPERAND** —
no sell rule was evaluated because there is nothing to evaluate it against, which is **not** the
same as every rule having been checked and cleared. The midday seat must not read this as a
clean §5 pass. **No `perplexity` call was spent on §5.1** — it needs an invalidation condition to
test and none exists.

**Nothing in limbo:** no open orders to inherit. No §7 exposure carried into today.

---

## BUY intents — NONE

**Five theses written, zero accepted** (`T-2026-11-25-01` … `-05`). Full reasoning in
`research_log.md`; the one-line dispositions:

| ID | Object | Died on |
|---|---|---|
| `-01` | HP/Dell quantifying memory+storage cost inflation (15–18% → ~40% of PC BOM) → **MU** | ⚠⚠ **The §4 PRICED-IN HARD FILTER, at −11.63% over 5 sessions — NOT the thesis.** All four parts passed with sourced figures (DRAM = **73% of $54.2B** FQ4 revenue; reports FQ1 in **December**). **First time in 86 days a candidate has cleared all four parts.** |
| `-02` | Same event → **SNDK**, **STX** | **Priced-in** (SNDK −21.86%, STX −4.37%) **and, independently, §4's correlation test** — same driver as `-01`; at most one of the three could ever be opened. |
| `-03` | Same event → **WDC** | **Part 1 — the drill query denied the causal path:** the source states HDDs are **not** a driver of HP's or Dell's cost pressure. ⚠ **The only name of seven to PASS the priced-in filter was the wrong name.** |
| `-04` | CF Industries buying Mosaic's Faustina ammonia plant, $600M + 20-yr/$240M/200kt offtake | **Part 1 — no second-order leg exists.** Both parties are named first-order principals. The gas, ammonia-peer and contractor legs are immaterial, §3-ineligible or unnamed. **Best-shaped object of the day; still not a §4 structure.** |
| `-05` | Sweep: eleven items disposed as one | §3 floors (foreign/OTCQB/sub-$10B), unquantifiable magnitudes, unnamed counterparties, own-results prints, and the standing no-Company-A macro object. |

⚠ **THERE IS NO `revalidate` LINE BELOW BECAUSE THERE IS NO INTENT TO REVALIDATE.** ⚠ **And note
the asymmetry if the open seat is tempted:** `-01`'s filter reading was **−11.63%**, i.e. **7.6pp
past the threshold.** An overnight gap cannot rescue it, and §4's re-validation only ever
*removes* intents. **It does not authorise adding one.**

---

## ⚠⚠⚠ ONE THING THE HUMAN SHOULD SEE — IT IS IN `research_log.md`, NOT ACTIONABLE BY ANY RUN

`T-2026-11-25-01` passed **all four §4 thesis parts with sourced figures** and was killed by the
priced-in filter on a **−11.63%** move. §4's wording is *"moved more than 4% … **on this news**,
you are late."* **The move was DOWN and the thesis is LONG** — that is a drawdown against the
thesis, not the news being priced in. `alpaca.py move` mechanises the test on **absolute**
magnitude, which makes it a **volatility filter** in practice. Today it killed **five of the
seven names checked, all five on down moves**, in a week the whole AI complex sold off.

⚠⚠ **NO RUN MAY ACT ON THIS AND THIS SEAT DID NOT.** The guardrail is in code, §4 and the routine
prompt both say `priced_in: true` → skip, and a run that diagnosed a filter as miscalibrated and
then reasoned past it would be the precise failure mode §4's honest-broker rule exists to prevent.
⚠ **The counter-argument, against this seat's own finding:** a name down 11.6% in five sessions is
one the market is repricing *against* the thesis, and a long entry there is what the §5.3 −7% hard
stop punishes fastest. **The filter may be doing useful work by accident.** Both readings fit.
**The calibration is the human's to set.**

---

## What the market-open run should do

1. **Nothing to execute.** No BUY, no SELL, no REBALANCE intent. This plan is correctly dated
   `2026-11-25`, so the staleness guard will pass and find an empty instruction set — **that is
   the intended state, not a failure to parse.**
2. **Do not treat an empty plan as licence to improvise.** §4's thesis requirement runs through
   `plan_today.md`; a buy reasoned into existence at 09:35 is exactly what this handoff exists to
   prevent. If the open seat finds a candidate it likes, the place for it is tomorrow's plan.
   ⚠ **Specifically: `-01` through `-04` are rejected, not deferred. Do not revive one.**
3. ⚠⚠ **IF THIS SEAT FIRES EARLY AGAIN (~08:36 for 09:35), POLL `clock` TO `is_open: true`
   BEFORE DOING ANYTHING.** This has happened twice (11-23, 11-24); the mitigation worked both
   times and took 28 min on 11-24. An early fire that exits on `is_open: false` **skips a whole
   day's execution.** **Read the DATES, not the boolean.**
4. **Re-read the §2 band off live prices** and **confirm the ledger still agrees** (`positions` →
   one VOO row) before concluding §5 has no operand.
