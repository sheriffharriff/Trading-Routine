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
plan_date: 2026-11-27
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-27 at 09:30 ET and closes at 13:00 ET** (`clock` 07:01:51 ET:
`is_open: false`, `next_open` `2026-11-27T09:30:00-05:00`, `next_close`
`2026-11-27T13:00:00-05:00`). **NOT a holiday** — closed because it is pre-market, and
**both** fields carry **today's** date, the pre-market signature.
⚠ **Read off the DATES, not the boolean: FALSE has three meanings — holiday, pre-market,
post-bell — and TRUE has one.**

### ⚠⚠⚠ READ THIS BEFORE ANYTHING ELSE, ROUTINE 2 — TODAY IS THE EARLY-CLOSE EDGE CASE

**THE 13:00 EARLY CLOSE IS NOW BROKER-CONFIRMED, NOT INHERITED.** Five prior seats could only
carry it forward from an unverified calendar; **this seat read `next_close: 2026-11-27T13:00`
directly off `clock`.** Today's session is **three and a half hours long, 09:30–13:00.**

⚠⚠ **THE POLL APPLIES TODAY. BOTH `clock` DATES READ 2026-11-27 = TODAY.** If you fire before
09:30 (the recorded pattern is **~08:36 for the 09:35 slot, four times, 11-23→11-26**), you will
read `is_open: false` **in the pre-market sense**. Your prompt says *"If the market is closed, log
the skip, commit, and exit successfully"* — ⚠ **READ LITERALLY THAT WOULD THROW AWAY A WHOLE
SESSION, and today it is a session you cannot make up, because 13:00 leaves no second chance.**
**Poll `clock` to `is_open: true`, then execute.**

⚠ **THE POLL IS DATE-GATED, NOT BOOLEAN-GATED, AND THE GATE IS WHAT MAKES IT SAFE.** Apply it
**only** when both `next_open` and `next_close` carry **today's** date — as they do now. On
2026-11-26 both carried a *later* date (the holiday shape) and polling to `true` would have hung
until the harness killed the run. **Check the dates before you poll.**

⚠ **Note for routine 4 (close journaling), whose edge case today INVERTS:** a ~15:15 fire lands
**two hours fifteen minutes AFTER** the 13:00 bell, so `clock` will read `is_open: false` with both
dates on **Monday's** session — **which is the holiday signature, but today WAS a session.** The
discriminator is *"did today ever open?"*, not *"are the next dates later?"* **Moot only while the
satellite sleeve is empty, as it is now — there is no `highest_close` to stamp.**

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT, NOT INHERITED.**
`week_anchor(2026-11-27)` → **2026-11-23** (imported from `common.py`, not hand-computed);
inherited `week_of` **2026-11-23**. They match, so `new_positions_this_week` stays at **0 of 3**.
⚠ The reset is done here rather than trusted to the Friday review, so a failed Friday run cannot
leave the §6 weekly cap stuck at its limit. ⚠ **This week's cap now expires unused** — Monday and
Tuesday produced no qualifying candidate, Wednesday produced five rejections, Thursday was the
holiday and today is a half session. **An unused cap is not a cost. It is not a reason to spend it
in three and a half hours.**

**Selftest 5/5, exit 0.** `trading_enabled: true`, LIVE against the paper account.

⚠ **This seat fired ~07:02 for an 08:00 slot (~58 min early), the same offset recorded on 11-24,
11-25 and 11-26.** Per `control.md`, manual "Run now" invocations are indistinguishable from
scheduled ones in run logs, so this is **recorded, not diagnosed as a schedule fault.** **It is
benign for this routine** — routine 1 places no orders and the only cost is that the "last 24
hours" research window starts an hour earlier. ⚠ **It is NOT benign for routine 2**; see the box
above, which is this item's worst case.

---

## Gate state — every §6 / §7 gate open, and no intent written anyway

| Gate | Reading | Blocks a buy? |
|---|---|---|
| §6 circuit breaker | **INACTIVE**, `consecutive_closed_losses` **0 of 3**, `halt_triggered_at: none` | No |
| §6 weekly cap | **0 of 3** new positions this week | No |
| §2 satellite sleeve | **0.00% deployed**, **$30,000.00** cash available | No |
| `control.md` `TRADING_ENABLED` | **true** | No |
| `control.md` `HALT_CLEARED_AT` | **none** — and none is needed, the breaker is inactive | No |
| `control.md` Notes | **(none)** | No |
| `alerts.md` open incidents | **(none)** — nothing SYSTEMIC to flag | No |

⚠⚠ **THIS IS THE UNHALTED ZERO, AND THE DISTINCTION IS THE WHOLE POINT.** Nothing structural
prevented a position today. **Five theses were written and five were rejected on §3 and §4's own
tests.** A plan that is empty because the breaker is active and a plan that is empty because
nothing qualified are different facts about the system, and only one of them is a successful run.
**This is the second kind.**

---

## Account snapshot (pre-market mark — said once, not repeated per section)

- Equity **$96,217.41** · core **VOO** 99.046311231 sh @ 706.74 · market value **$66,217.41** ·
  unrealized **−$3,782.58 / −5.404%** · cash **$30,000.00**.
- Sleeves: **core 68.82% · satellite 0.00% · cash 31.18%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: 1134.78`.
- ⚠ **These are read off `current_price` 668.55 at 07:02 — a PRE-MARKET PRINT, not a close**
  (**+1.469%** on `lastday_price` 658.87, matching the broker's own `change_today: 0.01469`).
  They will move before the bell. **The §2 band verdict is robust to that:** the 65% floor breaks
  at VOO **562.51** and the 75% ceiling at **908.67** — **re-solved at this seat, not copied**
  (19500 = 0.35 × 99.046311231 × P; 22500 = 0.25 × 99.046311231 × P). ⚠ These two prices are
  **invariant while cash is exactly $30,000 and the share count is unchanged**, which is why they
  reproduce Wednesday's figures exactly — **that is arithmetic, not a copied value.** The floor is
  a further **−15.87%** from the pre-market mark.
- ⚠⚠ **CORE −5.404% IS NOT A §5 EVENT, AND IT HAS NARROWED.** Against **−6.773%** at every seat on
  11-26 it has narrowed by **1.369pp**; against **−8.307%** on 11-25, by **2.903pp**. ⚠ **Direction
  computed before being written, per the standing rule about superlatives and intent-written
  numbers** — the 11-25 seat caught itself asserting "narrowed" when the figure had widened.
  **Today it genuinely narrowed.** Either way: **§5 exempts core outright and §2 says core is not
  sold on news. There is no hard stop and no trailing stop on core. DO NOT SELL CORE.**
- ⚠ **ENDPOINT DISAGREEMENT — NO NEW INSTANCE TODAY AND NONE CLAIMED.** `lastday_price` **658.87**
  is the **same stale mark the four 11-26 seats read**, because 11-26 was not a session. **The
  recorded count stays at 18 distinct sessions; re-reading one closed session is not a 19th
  measurement.** ⚠ **No `bars` call was spent** — none was owed, and one must not be spent merely
  to extend a tally. ⚠⚠ **Routine 4 must stamp any `highest_close` from official `bars` closes
  only, never from the broker's `current_price`**, or §5.4 trails a number from the wrong endpoint.

---

## §2 REBALANCE — none due

`rebalance_needed: false`. Core **68.82%** sits inside the 65–75% band; `rebalance_delta` of
**$1,134.78** is the distance to the 70% *target*, not a breach of the band, and §2 rebalances on
the band, not the target. **No REBALANCE intent.** ⚠ The core is below target because it is down
5.4% from entry, not from drift worth chasing — buying to target here would be adding to the core
on weakness, which §2 does not ask for.

⚠ **RE-READ THE BAND OFF LIVE PRICES AT THE OPEN ANYWAY.** The verdict here survives a −15.9% move
in VOO, so it will not flip today, **but the band is a live test and the open seat owns it.**

---

## SELL intents — none, and the reason is that there is nothing to sell

**Zero open satellite positions — 87th consecutive session.** `positions.md`
`grep -ci 'status: *open'` → **0**; `alpaca.py positions` returns **one** row, VOO
99.046311231 sh @ 706.74, the designated §2 core, **§5-exempt and deliberately untracked**
in `positions.md`. **The ledger and the broker agree; there was no disagreement to reconcile.**

⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING.** No entry price, no `highest_close`, no deadline and
no invalidation string exists anywhere in `positions.md`. **Step 4 therefore had NO OPERAND** —
no sell rule was evaluated because there is nothing to evaluate it against, which is **not** the
same as every rule having been checked and cleared. The midday seat must not read this as a
clean §5 pass. **No `perplexity` call was spent on §5.1** — it needs an invalidation condition to
test and none exists.

**No order is in limbo (§7).** `orders --status all` returns **exactly one order in the account's
entire history** — the 2026-09-03 VOO core buy, `filled`, already in `trade_log.md`. **Nothing
from the last session, nothing non-terminal.** Checked, not assumed.

---

## BUY intents — NONE

**Five theses written, five rejected.** `T-2026-11-27-01` through `-05` are in `research_log.md`
with the specific test that killed each. **There is no `revalidate` line in this plan because
there is no intent to revalidate.**

| Thesis | Candidate | Killed by |
|---|---|---|
| `T-2026-11-27-01` | **SCCO · TECK · FCX · HL** ← Nyrstar's 315 kt/yr Budel zinc smelter halt | **Part 1** — the mechanism needs **two clauses with opposite signs** for an integrated miner, **and the sourcing contradicts itself** on the sign of the treatment-charge leg. **Part 2 independently** — no §3-eligible name has a **sourced** zinc share ≥10%: SCCO **3.9%**, HL **9.3%** *and* ~$7.2B cap, TECK **unsourceable**, FCX priced-in `true` −5.62%. |
| `T-2026-11-27-02` | **PTC** ← FTC early termination of HSR for Schneider Electric's bid | **Part 1** — PTC is the **target**, i.e. the first-order leg; Schneider is Euronext-listed (§3); merger arbitrage is not a §4 structure; **no source names a second-order party.** |
| `T-2026-11-27-03` | the **US AI-accelerator / cloud complex** ← BIS Entity List additions + NVIDIA's SE-Asia shipment suspension | **Part 1** — the **standing government-action object, 4th appearance in 9 sessions**; no beneficiary named; **the only measurable direction is NEGATIVE, and §3 permits no shorts, inverse products or derivatives.** |
| `T-2026-11-27-04` | the **macro / policy complex** (Q3 GDP 4.3% · Oct PCE 3.8% / core 3.3% · proposed tariffs on 14 economies · Beige Book · Q3 profits $206B) | **Part 1 — no Company A.** A data print is not a transaction. ⚠ The tariff leg is a **proposal, not a decision**, and names no recipient. |
| `T-2026-11-27-05` | sweep — **nine** remaining items (Air Liquide/Airgas · CF/MOS re-serve · Givaudan · Stellantis · USAR · Megaspeed et al. · Xinde · Wanhua re-serve) | **§3 and part 2**, item by item in the table. **Zero extra drill queries.** |

⚠⚠ **THE ONE WORTH THE HUMAN'S ATTENTION IS `-01`, AND SPECIFICALLY WHY IT DIED.** **TECK passed
every mechanised gate** — §3 cap ~$27.8B, `us_equity`/NYSE/tradable/active, priced-in **−1.68%
`false`** — and the correlation check passes by vacancy. **It died because two queries could not
return an eligible filing figure for zinc's share of its revenue, and this seat declined to supply
that figure from its own general knowledge.** `alpaca.py buy` **could not have caught that**: the
trading-ops note is explicit that the script *"cannot tell whether a market cap figure is correct,
only that it is present."* **The guardrail that held here was §4 part 2 read honestly, not code.**

⚠ **AND A NOTE THAT CUTS AGAINST THREE SESSIONS OF THIS LOG'S OWN COMPLAINT:** carry-forward item 1
holds that the §4 priced-in filter is really a volatility filter and has been doing most of the
killing. **Today it killed one name of four — three passed it.** **The thesis parts did the work.**
That is the **third consecutive observation** pointing away from the filter being the binding
constraint (11-24 died on part-2 materiality, 11-25 on the filter, 11-27 on parts 1 and 2).
**No calibration was changed and no seat may change one.**

---

## What the open run should do

1. ⚠⚠ **Check the `clock` dates first. If both read 2026-11-27 and `is_open` is false, POLL to
   `true` — do not exit on the boolean.** See the box at the top. **The 13:00 close leaves no
   second chance.**
2. **Re-read `sleeves` off live prices** and confirm `core_in_band: true`. It will not flip today
   (the band survives a −15.9% move in VOO), but the §2 band is a live test and it is yours.
3. **Execute nothing.** There are **no BUY, no SELL and no REBALANCE intents.** ⚠ **An empty plan
   is a complete instruction, not a missing one** — this plan is dated today and was written by a
   selftest-clean run. **Do not go looking for something to do inside a three-and-a-half-hour
   session.** §4: *"The correct output of most research runs is no trade."*
4. **Confirm `plan_date` above reads 2026-11-27** before concluding there is nothing to execute,
   so "no intents" is distinguished from "stale plan refused."
5. **Commit, whatever happens.** A gap in git is indistinguishable from a run that never fired.

---

## Carry forward to the midday and close runs

- **Satellite sleeve is empty.** §5 has **no operand** — not a clean pass. Nothing to stop out,
  nothing to time-stop, **no `highest_close` to stamp.**
- **Today is a 13:00 close.** The midday run (~11:41 observed) lands **79 minutes inside** it and
  is fine. **The close run's ~15:15 fire lands 2h15m AFTER the bell** and will see the holiday
  signature on a day that *was* a session — **read it as "did today open?", not "are the next
  dates later?"**
- **Friday is also weekly-review day (routine 5).** ⚠ `research_log.md` grew by ~26 KB today;
  **the monthly rollover is the review's job** and `state.md` carry-forward item 9 is the standing
  systemic finding on corpus growth. **November entries stay — the rollover moves entries older
  than the current month.**
