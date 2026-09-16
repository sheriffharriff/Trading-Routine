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

If the pre-market run failed, was skipped, or crashed before writing, this file still holds
yesterday's intents. Executing them would be running stale research as though it were
fresh — the candidate has had another full session to move, and the §4 priced-in check that
cleared it was performed against prices that no longer exist. Doing nothing is strictly
better. Core and rebalance actions are exempt from the gate because neither depends on the
day's research.

```
plan_date: 2026-09-16
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-16 at 09:30 ET (`alpaca.py clock` at 08:17:11 ET: `is_open:
false`, `next_open: 2026-09-16T09:30:00-04:00`, `next_close: 2026-09-16T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.

**One pre-market run today, at 08:17 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,221.49**).

**Tape context:** VOO's broker mark is **698.88** (`lastday_price` **696.20**, `change_today`
**+0.385%**). Neither number is an execution reference — **pull a fresh quote at 09:35.** The
core position shows `unrealized_pl` **−$778.50 (−1.112%)** against the 706.74 fill. §5 exempts
core from all four sell rules — **there is no action attached to it at any number, in either
direction.**

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and three candidates were researched to a full thesis entry and all three
were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker INACTIVE, weekly cap
at **0 of 3**, satellite sleeve **empty with 30.24% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a BUY
intent exists. **Zero `alpaca.py move` calls are due at 09:35 — an absent check, not a skipped one.**

Three candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-16-01 | AVGO | parts 2 and 3, and rule (iii) | **Meta deploys in-house MTIA silicon H1 2027; Broadcom is the named design partner.** **Part 1 PASSED** — one clean clause. Then: Broadcom discloses **no Meta-specific dollar figure** (the only number in the result set is a blog's synthesis of Broadcom's *total* AI revenue), and its own calendar is **"deliveries through 2027, gigawatt deployment through 2028"** — past §4.3. Rule (iii) kills it independently: **Broadcom discussed MTIA on its own Q3 2026 call.** |
| T-2026-09-16-02 | (no ticker) | part 3 (rule vi) | **Venture Global ↔ China Gas, new 20-year / 0.5 Mtpa LNG SPA — deliveries start 2030.** Three-plus years past the two-quarter cap. Screened on timing first; no Company B hunt was spent on it. |
| T-2026-09-16-03 | (no ticker) | part 1 (rule v) | **Army → NAMC, M1 Abrams AGT1500 engine OTA, $2.5B ceiling / $11.8M obligated, completion March 2029.** Awardee is a **consortium**, so there is no Company A either; **no source names any member, subcontractor or supplier**, and none has a dollar figure attached. |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ THE FOMC DECIDES AT 14:00 ET TODAY — INSIDE THE SESSION, AFTER YOUR RUN — AND FUTURES PRICE
  BETTER THAN 90% ODDS OF A 25bp HIKE, THE FIRST SINCE 2023.** Chair **Kevin Warsh** holds a press
  conference after. **This changes nothing you do.** There are no intents to execute, so there is
  nothing for a mid-session move to invalidate; **core is exempt from all four §5 sell rules, so a
  core mark that moves hard in either direction carries NO ACTION.** **If it moves prices, that is
  a price move, not a thesis.** **Do not open anything in response, and do not treat an afternoon
  move as information your 09:35 run should have anticipated.**
  *(The 09-14 log flagged one source at ~87% odds of an **increase** as contradicting every other
  framing, and deliberately did not chase it. **It was not an outlier — it was early.** Recorded
  so the log shows which unresolved item resolved and which way.)*

- **⚠ THE FUNNEL'S FAILURE MODE CHANGED TODAY AND THE NEW ONE IS WORSE — DO NOT RECORD IT AS MORE
  OF THE SAME.** 09-14 and 09-15 both died on *"the source names the transaction and withholds the
  counterparty's number."* **Today the funnel finally cleared that obstacle: AVGO is named, the
  program is public, and Broadcom discusses MTIA on its own earnings call.** **It died anyway** —
  because what a named counterparty publishes about a program is **roadmap and volume, not segment
  revenue**, and §4.2 cannot use that either. **Two distinct disclosure failures, not one.** A
  review that merges them will mis-diagnose what a human could actually change.

- **⚠ NEW SUB-SHAPE OF RULE (v): A CEILING IS NOT REVENUE, AND THIS ONE IS 212× THE CASH.** The
  Abrams OTA reads **$2,500,000,000** in every headline and carries **$11,831,430** actually
  obligated. Previous rule (v) instances were real awards with a missing allocation; **here the
  headline number is an authorization limit that may never be spent.** **Read the obligated figure,
  not the ceiling.**

- **⚠ I KNEW WHO MAKES THE ABRAMS ENGINE AND THE SOURCE DID NOT SAY IT.** The AGT1500 is a Honeywell
  engine — the fact arrived instantly and correctly and would have written a fluent mechanism
  sentence. The screen was run **specifically to test it** and returned that no reviewed source
  names Honeywell, General Dynamics **or "others"** under this OTA, with no dollar figure attached
  to any. **This is T-2026-09-01-03 (RTX) exactly**, caught this time *before* a ticker entered the
  funnel. **Knowing who makes the part is not knowing who was paid.**

- **⚠ SEVENTH PRICED-IN DRAWDOWN INSTANCE, ZERO COST — KEEP THE TALLIES SEPARATE.** AVGO **−7.97%**
  read `priced_in: true`. Instances: LITE −7.35%, LMT −3.61% near-miss, LHX −4.47%, CART −5.79%,
  BWXT −6.30%, CRWV −7.12%, **AVGO −7.97%.** **The filter was applied as written and AVGO was
  skipped; no run may reinterpret it — that is a human editing §4 or `alpaca.py move`.** **AVGO was
  already dead at parts 2 and 3 before the filter was consulted. LITE is still the only instance
  that reached the filter alive.**

- **Dropped before thesis stage, with reasons:** **JPM guiding Q3 trading/IB up while BAC warns and
  WFC says NIM will beat** — the trade it suggests is buying JPM on JPM's *own* guidance, which is
  first-order, and extending it to peers is the **"a shared cause is not a mechanism"** trap
  (4th instance: the rate environment, not a transaction). **Centene reaffirming FY26 guidance** —
  a reaffirmation of July 28 guidance, rule (iii). **Medtronic's LigaSure/Hugo FDA clearance** —
  MDT's own clearance, no dollar figure, already a disposed reject. **Axon's $1.0B 0% convertible** —
  a financing. **General Mills** — **does not report until ~Sept 23**; the "expected to release
  earnings on Wednesday" item was a **calendar auto-alert**, and its FY27 guidance was **affirmed
  Sept 8**, not changed.

### SELL — none

**No open satellite positions.** §5.1–§5.4 have no subject for the **eighteenth consecutive
session**. `sell_rule_status` is **absent, not blank** — there is no thesis to invalidate, no
`timing_window` to expire, no `entry_price` to measure −7% against, and no `highest_close` to
measure −10% against. **Nothing is near triggering because nothing exists to trigger.** All four
remain **untested code paths**, and eighteen sessions of "no exits" record the absence of a
subject, not eighteen clean bills of health.

**Zero Perplexity invalidation queries were issued this run and none was due** — §5.1 reads an
`invalidation` line that does not exist.

### REBALANCE — none

**Core is in band and no rebalance is due.** `alpaca.py sleeves` at 08:17 ET: equity
**$99,221.49**, cash **$30,000.00**, core **$69,221.49 = 69.76%**, satellite **0.0% (count 0)**,
cash **30.24%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +233.56`.

§2 rebalances at the **band edge (65/75)**, **not to the exact 70% target.** The $233.56 delta is
**0.24% of equity** and is not an action. **Seventeenth consecutive run inside a 0.29-point range
(69.69–69.98).**

---

## What the open run should actually do

1. **Check `plan_date` against today's ET date.** It reads **2026-09-16**. If today is not that
   date, this plan is stale — log it, alert, and skip to the core/rebalance section.
2. **Execute nothing.** There are no BUY, SELL or REBALANCE intents, and **that is the plan, not a
   gap in it.**
3. **Do not go looking for something to do.** 30.24% idle cash, an INACTIVE breaker and a weekly
   cap at **0 of 3** are **not an opportunity this run may act on.** New positions route through
   pre-market research plus this execution run, always — a position opened at 09:35 without a plan
   entry would route around the discipline rather than satisfy it.
4. **Verify the empty plan is FRESH, not stale.** An empty plan that is current and a plan that is
   out of date **produce identical zero-order runs and are not the same run.** The difference is
   invisible in the order count, so read the date rather than the outcome. **The stale-plan gate
   has now been exercised seventeen times and has never fired — its alert path REMAINS UNTESTED
   CODE.** Seventeen quiet opens are not evidence the gate works.
5. **Pull a fresh quote for anything you price.** The broker's `current_price` is a **live
   bid/ask midpoint**, not a close — 698.88 this morning against yesterday's official 696.29 is
   that mechanism in pre-market. `bars --adjustment all` for a close, a fresh `quote` for
   execution, **never a `positions` field for either.**
