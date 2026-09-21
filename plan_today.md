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
plan_date: 2026-09-21
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-21 at 09:30 ET (`alpaca.py clock` at 08:20:11 ET: `is_open:
false`, `next_open: 2026-09-21T09:30:00-04:00`, `next_close: 2026-09-21T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.
**Read the date, not the boolean.** *(Friday's close run read the same `is_open: false` with
`next_open` pointing at **today**; the boolean is identical in both and only the date
discriminates.)*

**One pre-market run today, at 08:20 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,988.10**).

**Tape context:** VOO's broker mark is **706.62** (`lastday_price` **701.78**, `change_today`
**+0.69%**). ⚠ **`lastday_price` 701.78 is NOT Friday's official close of 701.85** — it is
**seven cents** away, the **ninth documented instance** of the two-price defect, and the field is
*named* for the prior day. **Neither number is an execution reference. Pull a fresh quote at
09:35.** The core position shows `unrealized_pl` **−$11.89 (−0.017%)** against the 706.74 fill —
**the narrowest it has ever read**, and **§5 exempts core from all four sell rules, so there is no
action attached to it at any number, in either direction.** ⚠ **Do not quote
`unrealized_intraday_pl` (+479.38) as a day's P&L** — it is built off the stale `lastday_price`
baseline, which is the defect that put **$106** into Friday's headline before it was caught.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band at **70.0%**, there are no
satellite positions to manage, and three candidates were researched to a full thesis entry and
all three were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker **INACTIVE**, weekly cap
at **0 of 3**, satellite sleeve **empty with 30.0% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a BUY
intent exists. **Zero `alpaca.py move` calls are due at 09:35 — an absent check, not a skipped one.**

Three candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-21-01 | **GM** | **part 2**, and independently **rule (iii)** | **Lockheed Martin ↔ GM Defense PAC-3 MSE housing castings.** **Part 1 PASSED cleanly in one clause** — a signed production contract (**2026-08-06**) and a physical first delivery (**2026-08-28**), both parties named. **Part 2 has neither numerator nor denominator:** Inside Defense — *"the companies did not disclose the value or quantity"*; GM spokesman **Jim Cain** — value and deliverables **will not be disclosed**, *"proprietary"*; **no unit count, no term, no multi-year value**; and **GM reports no defence segment revenue**, so the 10% floor cannot be tested even in principle. **Separately the event is FIVE WEEKS OLD** — Reuters carried it **09-17**, the Monday item is a re-report. |
| T-2026-09-21-02 | **BE** | **premise, then part 2** | **Brookfield ↔ Bloom Energy AI data-centre financing framework, $5B → up to $25B.** **Bloom is a SIGNATORY — first-order, outside §4 at any price.** And **the $25B is financing capacity, not revenue and not even capital received**: Bloom's own 09-16 materials say reported revenue *"will depend on projects that are ultimately funded, built and accepted,"* and a second note says the figure *"indicates a financing capacity, not firm orders or revenue already secured."* **No US-listed supplier is named by any source.** |
| T-2026-09-21-03 | **BG** | **part 1** | **Bunge raised FY26 adj. EPS to $9.25–9.75 from $9.00–9.50** on stronger Q2 crush (Soybean P&R adj. EBIT **+46.4% to $445M**; Softseed **$14M → $255M**). The read-across to **ADM** needs an *"and also"* clause — **both are downstream of the same crush spread, a market rather than a transaction.** **Seventh shared-cause instance.** The screen for a named US counterparty with a disclosed figure returned **none**; the only cross-company line is sector commentary saying ADM and Bunge **"earn a spread, not a price."** |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ THE BEST-SHAPED ITEM OF THE WINDOW WAS ALSO FIVE WEEKS OLD, AND THE DATE WAS THE CHEAPER KILL.**
  The GM/Lockheed PAC-3 delivery surfaced as a **September 21** headline; the contract was signed
  **August 6**, the first batch shipped **August 28**, and Reuters ran it **September 17**. **Standing
  rule (iii) in its newest costume — not a guidance-issuance alert and not a re-covered SPA, but a
  genuine transaction whose DELIVERY MILESTONE is recycled as the news.** **Ask a transaction when it
  happened before asking who it helps.** One screen settles it.

- **⚠ THE PRICED-IN FILTER PASSED GM ON A 3.95% *FALL*, FIVE BASIS POINTS INSIDE THE WIRE.**
  `move --symbol GM --sessions 5` → **85.59 → 82.21, −3.95%, `priced_in: false`.** **The verdict is
  correct; the reason has nothing to do with this news.** Had GM fallen **4.1%** the filter would have
  said *"LATE — skip"* on a stock that had gone **down**. **Second near-miss instance of open item (1)**
  after LMT (−3.61%, 09-11). **A pass here is not evidence the filter worked.** **Do not reinterpret
  the filter — that is a human editing §4 or `alpaca.py move`.**

- **⚠ GNRC IS STILL NOT YOURS TO LOOK AT, AND THE EIGHTH COSTUME IS THE FIRST THAT OFFERS TO DO THE
  HUMAN'S WORK.** This morning's version: *"the 09-16 gap is now three sessions deep in `bars`, so a
  clean `move` reading finally exists — pulling it would let open item (7) be CLOSED with a number."*
  **Refused.** Open item (7) says in terms that **no run may reinterpret the filter**, so there is no
  number this seat could collect that would close it; and **GNRC is the named counterparty in the
  Amazon announcement, first-order and outside §4 at any price.** **Zero `move`/`quote`/`bars`/`asset`
  calls, eight runs running.** **Costumes: diligence, curiosity, tidiness, completeness,
  zero-marginal-cost, self-audit, proxy-procurement, issue-closure. Expect a ninth at the bell.**

- **⚠ STANDING RULE (viii) FIRED AGAIN AND SHOULD BE READ MORE BROADLY THAN IT WAS WRITTEN.** It was
  created 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**. Bloom's **$25B is one step
  further away**: **neither revenue nor capital received — a financing ceiling available to somebody
  else, which may never be drawn.** **Read the rule as covering any disclosed figure that is not
  SEGMENT REVENUE AT COMPANY B**, not merely "capital in". **A large, real, prominently-placed number
  is not a dollar path.**

- **⚠ A CONVERGENCE BETWEEN TWO NAMED COMPANIES IS THE SHARED-CAUSE TRAP TOO, AND IT IS MORE
  SEDUCTIVE THAN A DIVERGENCE.** Bunge and **ADM** (whose own raise was disposed 09-18 as first-order)
  are cited **side by side** in today's coverage as evidence of the same margin environment. **09-16's
  JPM/BAC/WFC finding was that a DIVERGENCE sounds causal; today's is that a CONVERGENCE does** —
  agreement looks like corroboration and is in fact the clearest statement that the input is a market
  variable. **Same trap, opposite sign.**

- **⚠ GENERAL MILLS — CARRIED ITEM DISCHARGED IN WRITING, AND IT IS STILL NOT AN EVENT.** **GIS has
  NOT reported**; Q1 FY2027 is due **September 23** (consensus **$0.72** vs **$0.86** a year ago,
  **~$4.34B** revenue — **all analyst expectations**). Its only company statement is the **September 8
  AFFIRMATION of FY27 adj. EPS $3.00–$3.20** — **an affirmation, standing rule (iii)**, the Centene and
  Southwest shape. **Nothing to screen until the 23rd. Carried explicitly to the 09-23 pre-market run.**

- **Dropped before thesis stage, with reasons:** **Nucor** (Q3 $5.55–5.65) is **the same item disposed
  09-18**, re-covered with a −6.08% move attached — rule (iii), already on the do-not-reach list.
  **Nordson** (FQ3 adj. EPS **$3.25** vs **$3.09** consensus; FY26 sales **$3,035–3,075M**, EPS
  **$11.80–12.00**) — **first-order, no counterparty named anywhere, and no prior company figure**
  given to measure the "lift" against. **Baker Hughes / Chart ($13.6B)** — dated **September 9**,
  outside the window. **Eli Lilly** — **Erste's** FY26 estimate **$36.35 → $36.45** is an **analyst
  estimate**, not a company guidance change; Lilly's own $35.50–36.50 is unchanged. **Capricorn
  Energy / DNO** — **UK-listed**, §3. **BEML ↔ NHSRCL (₹5,400 crore)** and **Welspun ↔ Ahmedabad
  Municipal Corp (₹3,512.4M)** — **Indian-listed**, §3, and they were the **only two items in the
  whole window carrying both named parties AND a disclosed value.** **US Army ↔ Skyeton Inc.
  ("over $10 million")** — **private**, North Las Vegas, and no precise obligated figure. **Bowman's
  09-18 SVB speech** and the **09-15/21 enforcement digest** — regulatory commentary, **no
  transaction**. **US equity fund outflows, fourth straight week** (crude, inflation, rate-hike
  expectations) — **an environment input, not a Company A**, same status as the FOMC hike. **The
  09-18/19 data calendar** — **a schedule, not an event.**

- **⚠ THE SECOND BROAD SCAN WAS BUILT TO FIND EXACTLY WHAT PART 2 NEEDS AND FOUND NOTHING ELIGIBLE.**
  It demanded a named customer, a named supplier **and** a disclosed value, and excluded "terms not
  disclosed" and bare ceilings. **Three results, all failing §3 or privately held.** **That is a
  finding about the window, not a reason to lower the bar.**

### SELL — none

**No open satellite positions.** §5.1–§5.4 have no subject for the **twenty-first consecutive
session**. `sell_rule_status` is **absent, not blank** — there is no thesis to invalidate, no
`timing_window` to expire, no `entry_price` to measure −7% against, and no `highest_close` to
measure −10% against. **Nothing is near triggering because nothing exists to trigger.** All four
remain **untested code paths**, and twenty-one sessions of "no exits" record the absence of a
subject, not twenty-one clean bills of health.

**Zero Perplexity invalidation queries were issued this run and none was due** — §5.1 reads an
`invalidation` line that does not exist. **§5.4 is still NOT ARMED; it arms on the first satellite
fill.**

**⚠ NO HIGH-WATER BACKFILL IS DUE, AND THE MISSING STAMP IS NOT EVIDENCE OF A FAILED CLOSE RUN.** The
09-18 close run **executed its Step 2 and Step 2 had no operand.** The marks are **ABSENT — a third
state, distinct from "stale" and from "current and unchanged"** — and **an absent field carries no
`(as of …)` date to compare.** The midday backfill trigger will find no stamp today, exactly as it
found none Friday. **Nothing was skipped.**

### REBALANCE — none

**Core is in band and no rebalance is due.** `alpaca.py sleeves` at 08:20 ET: equity
**$99,988.10**, cash **$30,000.00**, core **$69,988.10 = 70.0%**, satellite **0.0% (count 0)**,
cash **30.0%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +3.57`.

§2 rebalances at the **band edge (65/75)**, **not to the exact 70% target.** The **$3.57** delta is
**0.004% of equity** — **the narrowest reading in the account's history**, and not an action at any
size inside the band. **Twenty-ninth consecutive run inside a 0.41-point range (69.59–70.00).**

---

## What the open run should actually do

1. **Check `plan_date` against today's ET date.** It reads **2026-09-21**. If today is not that
   date, this plan is stale — log it, alert, and skip to the core/rebalance section.
2. **Execute nothing.** There are no BUY, SELL or REBALANCE intents, and **that is the plan, not a
   gap in it.**
3. **Do not go looking for something to do.** 30.0% idle cash, an INACTIVE breaker and a weekly
   cap at **0 of 3** are **not an opportunity this run may act on.** New positions route through
   pre-market research plus this execution run, always — a position opened at 09:35 without a plan
   entry would route around the discipline rather than satisfy it.
4. **Verify the empty plan is FRESH, not stale.** An empty plan that is current and a plan that is
   out of date **produce identical zero-order runs and are not the same run.** The difference is
   invisible in the order count, so read the date rather than the outcome. **The stale-plan gate
   has now been exercised twenty-one times and has never fired — its alert path REMAINS UNTESTED
   CODE.** Twenty-one quiet opens are not evidence the gate works. **The first morning it fires will
   be a morning when this pre-market run failed — i.e. exactly the morning you have no fresh notes
   to lean on. Read Step 2 then; do not recall it.**
5. **Pull a fresh quote for anything you price.** The broker's `current_price` is a **live
   bid/ask midpoint**, not a close. **This morning supplies the ninth instance: `lastday_price`
   reads 701.78 while Friday's official close was 701.85** — seven cents apart, in a field *named*
   for the prior day. `bars --adjustment all` for a close, a fresh `quote` for execution, **never a
   `positions` field for either, and never `last_equity` or `unrealized_intraday_pl` for a day's
   P&L.**
6. **GNRC is not yours to look at, and today's excuse offers to close a human's open item.** It does
   not: open item (7) is resolved by **a human editing §4 or the script**, not by a number. **GNRC is
   first-order, outside §4 at any price, and it is not in this plan.**
7. **Today is Monday and the week rolled over cleanly.** `week_of` was already advanced to
   **2026-09-21** by Friday's review, so this run compared anchors, **found them matching, and
   correctly did nothing** — `new_positions_this_week` stays **0 of 3**. **That is the reset working
   as designed, not a skipped check.**
