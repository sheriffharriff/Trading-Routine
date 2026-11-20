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
plan_date: 2026-11-20
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-20 at 09:30 ET** (`clock` 07:02:16 ET: `is_open: false`, `next_open`
`2026-11-20T09:30:00-05:00`, `next_close` `2026-11-20T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Friday, an ordinary full session. `clock` was re-read at **07:04:48** before the two `move`
calls and gave the same signature.

The plan this seat replaced was dated **2026-11-19** — the previous trading day, the ordinary
shape. It carried **zero intents**. **Nothing was lost: a plan with no intents has no
execution to perform.**

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W47 weekday 5**; Monday anchor **2026-11-16**; inherited `week_of` **2026-11-16**.
They match, so `new_positions_this_week` stays at **0**. ⚠ The reset is done here rather than
trusted to the Friday review, **which has not yet run today** — so a failed Friday run cannot
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
| §4 four-part thesis | **Five written, FIVE REJECTED, ZERO accepted** | **YES — this is the only thing stopping a trade today** |

⚠ **Stated plainly so the next seat does not misread this plan's emptiness:** this is **not** a
halted day and **not** a blocked day. **Nothing structural prevented a buy. The candidates did.**
Those two cases produce an identical-looking plan and must never be conflated — one is a system
state, the other is a research outcome.

---

## BUY intents

**NONE.**

Five theses were written and all five were rejected (`T-2026-11-20-01` … `-05`, full entries in
`research_log.md`). **No candidate survived to the sizing stage, so there is no notional, no
ticker and no `revalidate` line to write.**

Where they died, in §4's own ordering:

| ID | Candidate | Died on |
|---|---|---|
| `-01` | **BKR** (Baker Hughes) ← FERC approval of Cheniere's Sabine Pass Stage V, ~20 mtpa (11-19) | **part 2** — drill query: **no disclosed scope value, no identified segment, no derivable revenue share**; **part 3** independently (multi-year LNG train programme vs the two-quarter horizon); **priced-in `true`, −4.46%** independently |
| `-02` | **AMKR** / the NVIDIA memory & packaging supply base ← supply commitments $279B → **$390B**, +$111B, as of 10-25 | **part 1** — drill query: **NVIDIA names no memory supplier and Micron has not confirmed NVIDIA as a customer**; **§3** — AMKR market cap **~$8.9B**, below the floor (Trefis, 11-19); **part 2** (nothing attributable); **priced-in `true`, −8.04%** |
| `-03` | Own-results cluster: **KEYS** FQ4 beat + ~20% FY27 target · **INTU** FQ2 guide-down · **ROST** Q3 beat, comps +8% | **part 1** — an own-results print is a **condition, not a transaction**; **no second-order recipient named in any of the three** |
| `-04` | Macro / policy complex (final UMich sentiment & inflation expectations, Waller & Cook, rig count, 6th straight decline, dollar near a 19-month high) | **part 1** — **no Company A**; the standing government-action object, unchanged |
| `-05` | Sweep: **thirteen** remaining disclosed events | **§3 / part 2 / no named Company B**, one named test each; **two are re-serves** of already-disposed events |

---

## ⚠⚠ THINGS THE OPEN SEAT MUST READ BEFORE IT CONSIDERS ANYTHING OF ITS OWN

**1. The priced-in gate was actually reached today, and BOTH readings were `true` BY FALLING.**
`clock`-gated at 07:04:48 (`is_open: false`, both dates 2026-11-20, window ending on the finished
2026-11-19 bar):

| Symbol | `from_close` → `to_close` | `move_pct` | `priced_in` |
|---|---|---:|---|
| **BKR** | 48.85 → 46.67 | **−4.46%** | **true — LATE** |
| **AMKR** | 37.12 → 34.135 | **−8.04%** | **true — LATE** |

⚠⚠ **This is carry-forward item 12's direction-blind filter (`abs(move) > 4`) appearing TWICE in
one run**, one session after NVDA read `true` by falling 13.22%. **"The filter is direction-blind,
therefore buy the faller" is averaging into weakness in a costume, and §7 forbids averaging down.
No override was taken at this seat and none may be taken at yours.** It is for the human to fix in
code. ✅ **And neither reading was load-bearing: both names die on part 2 / part 3, which precede
the filter in §4's ordering.**

**2. The pre-event-window rule is MOOT for these two, NOT discharged — keep it verbatim.**
*When the plan's catalyst broke after the prior close, the open seat is the first that can actually
perform the priced-in test; re-run `move --sessions 5` after the open and treat the pre-market
reading as UNPERFORMED, not passed.* Today's catalysts broke **during or after the 2026-11-19
session**, so the five-session window **does** contain a post-catalyst finished bar — and a `true`
reading is the conservative direction anyway, so no re-test could make either name eligible. ⚠ **The
rule stays live for the first seat that holds an intent on a post-close catalyst.** Measured
precedent: `research_log.md` ADDENDUM 2026-11-18 — re-running thirteen names after a completed
post-catalyst session **flipped 7 of 13 verdicts**; the eligible set went from **eight names to
five**; **five names reading `false` that morning were already 4.5–14% LATE.**

**3. If you write an intent of your own, item 13's `clock` gate is a CONVENTION, NOT CODE.**
`move` reads the in-progress bar. Run mid-session, the five-session window silently rolls onto
today's unfinished bar (demonstrated 2026-11-18: NVDA `to_close` 150.87 at ~15:25 vs 155.49 at
07:03). **Re-read `clock` immediately before any `move` call and say what it returned.**

**4. `sleeves` and `positions.current_price` are MIDPOINTS, not closes.** At 07:02 this seat read
equity **94,781.24** and core **68.35%** off a `current_price` of **654.05** — a pre-market
midpoint. The last authoritative figures are **close-basis** (below). Use `bars` for a close, a
fresh `quote` for execution, **never** a `positions` field or `sleeves` for a close-basis figure.

---

## SELL intents

**NONE — and this is the ABSENCE OF A SUBJECT, not four clean bills of health.**

`positions.md` lists **zero satellite positions** (`grep -ci 'status: *open'` → 0). `alpaca.py
positions` returns **one row — VOO 99.046311231 sh @ 706.74**, the designated §2 core, which is
**§5-exempt** and was **struck from the §5 working list, not cleared**. **Ledger reconciled, it
agrees.**

| Rule | Status | Why ABSENT rather than passing |
|---|---|---|
| §5.1 thesis invalidation | **ABSENT** | No invalidation string exists — 293 thesis IDs, 0 ever accepted. **No per-name Perplexity news check was run or owed: there is no name to check.** |
| §5.2 time stop | **ABSENT** | No timing window, no deadline. |
| §5.3 hard stop (−7% from entry) | **ABSENT** | No satellite entry price. |
| §5.4 trailing stop (−10% from `highest_close`) | **ABSENT** | No `highest_close` exists. |

**99th absent seat, 82nd absent date.** ⚠ **All four §5 sell rules remain UNTESTED CODE PATHS**, as
do the §5.4 staleness detector and the `highest_close` backfill branch. The first satellite position
is their first live test.

---

## REBALANCE intent

**NONE — core is IN BAND on both bases available this morning.**

| Basis | Equity | Core value | Core % | §2 verdict |
|---|---|---|---|---|
| **Official close 2026-11-19** (`bars` VOO **658.05**, `n` 2,902, `v` 132,178) | **95,177.43** | 65,177.43 | **68.4799%** | **IN BAND** — 3.4799pp above the 65% floor |
| **07:02 pre-market `sleeves`** (midpoint 654.05 — ⚠ not a close) | 94,781.24 | 64,781.24 | **68.35%** | **IN BAND** — 3.35pp above the floor |

`core_in_band: true`, `rebalance_needed: false`, satellite **0.00%**, cash **$30,000.00** (**31.65%**
on the midpoint basis, 31.5201% on the close basis). ⚠ `rebalance_delta` **1,565.63** is a distance
readout to the 70% target, **NOT an order** — §2 rebalances at the 65/75 band, not at the target.

⚠ **FLOOR HEADROOM HAS NARROWED SIX READS RUNNING:** 3.9074pp (11-18 close) → 3.9300pp (11-19
midday) → 3.4983pp (11-19 15:15) → 3.4799pp (11-19 close) → **3.35pp (11-20 07:02 midpoint)**. The
band is wide; **it is not getting wider.** A sixth consecutive down session on the index is what is
driving it, and §2 holds core permanently regardless. **The §5.4/§2 variance hazard becomes
load-bearing the first day core sits within a point of 65%.**

---

## Core sleeve

**No action.** Core is established (`core_established: true`, `core_ticker: VOO`, 99.046311231 sh
from the 2026-09-03 fill at 706.74 — the only fill in this account's history). §2 says buy once and
hold; §5 exempts it; §7 forbids selling it to fund a satellite trade. **It is not sold on news and
today's six-session index drawdown is news.**

---

## Not a holiday, and the dates say so

`clock` at **07:02:16** returned `is_open: false` — but `next_open` **2026-11-20T09:30** and
`next_close` **2026-11-20T16:00** both carry **today's** date. That is the pre-market signature of a
**normal full session**. A holiday shows `next_open` on a **later** date. Re-read at 07:04:48,
unchanged. **Market opens today at 09:30 ET and closes at 16:00 ET.**
