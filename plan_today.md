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
plan_date: 2026-11-19
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-19 at 09:30 ET** (`clock` 07:01:46 ET: `is_open: false`, `next_open`
`2026-11-19T09:30:00-05:00`, `next_close` `2026-11-19T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Thursday, an ordinary full session. `clock` was re-read at **07:04:37** before the single
`move` call and gave the same signature.

The plan this seat replaced was dated **2026-11-18** — the previous trading day, the ordinary
shape. It carried **zero intents**. **Nothing was lost: a plan with no intents has no
execution to perform**, so whether a `2-market-open` seat consumed it is immaterial.

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W47 weekday 4**; Monday anchor **2026-11-16**; inherited `week_of` **2026-11-16**.
They match, so `new_positions_this_week` stays at **0**. ⚠ The reset is done here rather than
trusted to the Friday review, so a failed Friday run cannot leave the §6 weekly cap stuck.

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
| §4 four-part thesis | **Six written, SIX REJECTED, ZERO accepted** | **YES — this is the only thing stopping a trade today** |

⚠ **Stated plainly so the next seat does not misread this plan's emptiness:** this is **not** a
halted day and **not** a blocked day. **Nothing structural prevented a buy. The candidates did.**
Those two cases produce an identical-looking plan and must never be conflated — one is a system
state, the other is a research outcome.

---

## BUY intents

**NONE.**

Six theses were written and all six were rejected (`T-2026-11-19-01` … `-06`, full entries in
`research_log.md`). **No candidate survived to the sizing stage, so there is no notional, no
ticker and no `revalidate` line to write.**

Where they died, in §4's own ordering:

| ID | Candidate | Died on |
|---|---|---|
| `-01` | US AI-accelerator complex ← Nvidia H200/Hopper China export halt (new, 11-19) | **part 1** — drill query: **no US-listed disclosed net beneficiary exists**; only measurable direction is negative |
| `-02` | CHRN ← $7.5B / 6-yr Odessa AI campus partnership with STN, Inc. | **§3** (issuer below the $10B floor) **+ part 1** (end customer unnamed, no supplier named); **part 3** independently (H1 2027) |
| `-03` | Unnamed Anthropic supply base ← $81.3B IPO at $83, ~$1.5T valuation | **part 1** (capital paid IN) **+ part 2** ($9B H1 spend has no named recipient) |
| `-04` | Home-improvement / discretionary supplier tier ← Lowe's +9.3% & Target +7.1% FQ3 | **part 2** — drill query: **no sourceable Lowe's/HD customer-concentration figure for any >$10B supplier**; **part 1** independently (own-results print is a condition) |
| `-05` | Macro / policy complex (FOMC minutes, Waller 50bp, gold 14-mo low) | **part 1** — no Company A; the standing object |
| `-06` | Sweep: nine remaining disclosed events | **§3 / part 2 / no named Company B**, one named test each |

⚠⚠ **A NOTE THE OPEN SEAT MUST READ BEFORE IT CONSIDERS ANYTHING OF ITS OWN — THE PRICED-IN
WINDOW IS AGAIN PRE-EVENT.** Today's principal catalyst (the Nvidia China Hopper export halt)
was **first disclosed 2026-11-19, after the 11-18 close.** `bars` returns **no 11-19 row** at
this hour, so a `move --sessions 5` run now ends on the **11-18** bar and contains **zero
post-catalyst sessions.** Per the operational rule discharged on 11-18 and kept verbatim:

> **When the plan's catalyst broke after the prior close, the open seat is the first that can
> actually perform the priced-in test — re-run `move --sessions 5` after the open and treat
> the pre-market reading as UNPERFORMED, not passed.**

✅ **Today that costs nothing, because no candidate reached the priced-in gate** — part 1,
part 2 and §3 precede it in §4's ordering and disposed of all six. **But the open seat does not
inherit that for any candidate of its own.**
⚠ Measured precedent, not theory: **ADDENDUM 2026-11-18** re-ran thirteen names once a
post-catalyst session had completed and **7 of 13 verdicts flipped; the eligible set went from
eight names to five; five names were already 4.5–14% LATE** while reading `false` that morning.

⚠ **AND THE `clock` GATE APPLIES TO `move`, NOT ONLY TO `highest_close`.** `move` reads the
in-progress bar — demonstrated 11-18, when a 15:25 call returned `to_close` **150.87** for NVDA
while the 07:03 seat had read **155.49**, the 11-17 close: the window had silently rolled onto
an unfinished bar. **Check `clock` before every `move` call and know which session the window
ends on.** This seat did so at 07:04:37 and its one reading is clean:
**NVDA `from_close` 173.85 → `to_close` 150.86, −13.22%, `priced_in: true`** — matching the
11-18 post-bell reading (150.87 / −13.22%) to a cent, which is what a finished bar looks like.

⚠ **AND THE FILTER IS DIRECTION-BLIND, WHICH IS NOT A LICENCE.** It tests `abs(move) > 4`, so
**NVDA reads `true` today by having FALLEN 13.22%.** A name that moves into `true` by collapsing
has not become more attractive. "The filter is direction-blind, therefore buy the faller" is
averaging into weakness in a costume, and **§7 forbids averaging down.** For the human to fix in
code; **no run may grant itself this override.**

---

## SELL intents

**NONE — and §5 had NO OPERAND, which is not the same as §5 passing.**

`positions.md` lists **zero satellite positions** and `alpaca.py positions` returns **one row,
VOO 99.046311231 sh @ 706.74**, the designated §2 core, which is **§5-exempt** and deliberately
not tracked in `positions.md`. **The two agree; there was nothing to reconcile.**

All four sell rules are **ABSENT, NOT PASSING**:

| Rule | Status | Why |
|---|---|---|
| §5.1 thesis invalidation | **ABSENT** | No invalidation string exists, because no thesis has ever been accepted. **No per-name news check was run or owed** — there is no name to check. |
| §5.2 time stop | **ABSENT** | No timing window and no deadline exist. |
| §5.3 hard stop (−7% from entry) | **ABSENT** | No entry price exists. |
| §5.4 trailing stop (−10% from `highest_close`) | **ABSENT** | No `highest_close` exists, and no mark was raised because there is nothing to raise. |

**95th consecutive absent seat; 81st absent date.** ⚠ The §5.4 staleness detector and the
`highest_close` backfill branch remain **UNPROVEN CODE** — the first satellite position will be
their first live test.

---

## REBALANCE intents

**NONE — core is in band. Do not place a rebalance order today.**

`alpaca.py sleeves` at 07:01 ET:

```
equity            97,318.81
cash              30,000.00
core  VOO         67,318.81   69.17%
satellite                 0    0.00%  (count 0)
cash_pct                       30.83%
core_in_band      true
rebalance_needed  false
core_target_value 68,123.17
rebalance_delta      804.36
```

**Core 69.17% sits inside §2's 65–75% band — 4.17pp above the floor, 5.83pp below the ceiling.
`rebalance_needed: false`. NO REBALANCE IS DUE.**

⚠⚠ **`rebalance_delta: 804.36` IS A DISTANCE READOUT, NOT AN ORDER.** It is the dollar gap to
the 70% *target*, which §2 only requires closing once the band is **breached**. A seat that
reads this field as an instruction will buy VOO for no reason. **The share count has been
unchanged since the 2026-09-03 fill and must stay unchanged today.**

⚠ **THIS SLEEVE READ IS ON A PRE-MARKET MARK AND THE OPEN SEAT MUST RE-READ IT.**
`positions.current_price` is **679.67** against a **671.26** official 11-18 close — a
**+1.253%** pre-market gap on thin volume, which is what carries equity from the 11-18
close-basis **$96,485.83** to the **$97,318.81** above. **The entire $832.98 difference is the
mark, not a flow:** cash is exactly $30,000.00 and the share count is identical.
**Re-run `sleeves` after the open and act on that, not on this.**

⚠ **ENDPOINT DISAGREEMENT, TWELFTH INSTANCE — AND THE NARROWEST YET, WHICH IS NOT A FIX.**
`positions.lastday_price` **671.31** vs official `bars` **671.26** for 11-18 =
**0.05 / 0.0074%**. Prior instances ran **0.10–0.42**. The spread has narrowed and widened
before; §5.4 still reads from the endpoint that is wrong. **Build P&L and stamp `highest_close`
from official `bars` closes only, one adjustment basis, one call.**

---

## What the open run should actually do today

1. **Check `plan_date` above is `2026-11-19`.** If it is not, this plan is stale — log it, alert,
   and go straight to the core/rebalance section.
2. **Re-run `alpaca.py sleeves` after the open.** The figures here are on a pre-market mark that
   gapped **+1.25%**. Core was **69.17%** and in band; confirm it still is on a real session
   print. **If and only if it is outside 65–75%, rebalance to 70% and log it.** Otherwise place
   no core order — and do not read `rebalance_delta` as one.
3. **Execute no BUY intents, because there are none.** Six theses, six rejected.
4. **Execute no SELL intents, because there are none and §5 has no operand.**
5. **If the open seat considers any candidate of its own, the priced-in test on today's catalyst
   is UNPERFORMED, not passed** — check `clock`, then re-run `move --sessions 5` on a window
   that contains the 11-19 session, and remember the filter is direction-blind.
6. **Confirm no order is non-terminal.** `orders --status all` has returned exactly one order in
   this account's entire history (the 2026-09-03 core fill, terminal). **§7 overnight exposure is
   structurally zero and should stay that way.**

---

## Carried to the open seat verbatim

- ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS ALREADY WITH THE HUMAN. DO NOT RE-SEND.** Across
  11-02 → 11-18, routine 2 has been able to execute on exactly **one** session (11-13, 10:43);
  on every other session the only run licensed to open positions fired into a closed market, and
  on 11-16 it did not fire at all. **It has not yet cost a trade — every one of those plans
  carried zero intents, as does this one — so the damage to date is zero and the exposure is
  entirely forward-looking.** Re-send only if the pattern changes in a way that changes what the
  human must fix. **A repeat pre-bell firing is not new information.** Per `control.md` this is
  **recorded, not diagnosed.**
- ⚠ **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED.** Verified 2026-11-13:
  adjusted and unadjusted closes identical to the cent on 259 of 260 sessions, across all four
  VOO ex-dividend dates. **Any review using the flag's output understates the benchmark and
  flatters the agent.** True 12-month VOO total return is **+14.615%**.
- ⚠ **The paper broker does not pay dividends.** Cash is exactly **$30,000.00**, not $30,180.52 —
  the 2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
  sleeve is structurally short **~1.07%/yr** against any honest total-return benchmark. **A run
  cannot fix this.**
- ⚠ **DO NOT MISREAD `delete-on-merge` AS A PUSH FAILURE.** An automation merges each session
  branch into `main` and deletes the branch, so `git ls-remote --heads origin` will show your
  branch gone on a **successful** run. **The correct check is
  `git merge-base --is-ancestor <sha> origin/main`**, not whether your branch still exists.
- ⚠ **DO NOT PUBLISH A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST, AND
  RANK OFF A CLOSE, NOT A PARTIAL BAR.** Two seats have published false superlatives; one reached
  ClickUp and needed a correction comment.
