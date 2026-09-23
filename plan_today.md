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
plan_date: 2026-09-23
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-09-23 at 09:30 ET** (`alpaca.py clock` at 08:20:08 ET: `is_open:
false`, `next_open: 2026-09-23T09:30:00-04:00`, `next_close: 2026-09-23T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. **Read the date, not the boolean.** *(Yesterday's 16:15 close run read the
identical `is_open: false` with `next_open` pointing at **2026-09-23**. Same boolean,
opposite meaning; only the date discriminates.)*

**One pre-market run today, at 08:20 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$100,504.14**).

**Tape context.** Yesterday's **official** VOO close, from `bars --adjustment all`, is
**712.69** (09-21: 712.76; 09-18: 701.85). The broker's pre-market `positions` row reads
`current_price` **711.83** and `lastday_price` **712.78**.

⚠ **THE TWO-PRICE DEFECT DID NOT CLEAR AT THE SESSION BOUNDARY THIS TIME — AND THAT IS A NEW
SHAPE, NOT A NEW INSTANCE.** `lastday_price` reads **712.78**, which is **NINE CENTS ABOVE**
yesterday's official close of **712.69**. ⚠ **It is the IDENTICAL value the field carried all
day yesterday**, when it was two cents high against 09-21's close of 712.76. **The field did
not rebuild — it carried the same stale number across a session boundary and got MORE wrong,
because the underlying close moved and the field did not.** ⚠ **Yesterday's carry-forward
recorded that the previous instance "DID clear at the session boundary." Today's did not.
The session boundary is therefore NOT a reliable refresh point**, which removes the last
structure anyone might have leaned on to reason about this field. Neither `current_price` nor
`lastday_price` is an execution reference or a close. **`bars --adjustment all` for a close, a
fresh `quote` for execution, never a `positions` field for either, and never
`equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

The core shows `unrealized_pl` **+$504.15 / +0.72%** against the 706.74 fill. **§5 exempts
core from all four sell rules, so there is no action attached to that number in either
direction**, and it is a broker mark in any case.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band at **70.15%**, there are **no
satellite positions to manage**, and **six candidates were researched to a full thesis entry
and all six were rejected.**

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker **INACTIVE**, weekly
cap at **0 of 3**, satellite sleeve **empty with 29.85% cash**, no restricting note in
`control.md`. ⚠ **Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a
BUY intent exists. ⚠ **Zero `alpaca.py move` calls are due at 09:35 — an ABSENT check, not a
skipped one.** *(Two `move` calls were made **at this run**, on LH and CNC, as §4 hard filters
against live candidates. Neither produced an intent, so neither carries forward to 09:35.)*

Six candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-23-01 | **GIS** | **part 1 — the premise** | **General Mills FQ1 2027, reported this morning.** Adj EPS **$0.75** vs **$0.72** consensus, net sales **$4.39B** vs **$4.34B**, **organic sales FLAT**, adj op profit **$634M (−11% cc)**, FY27 guidance **REAFFIRMED** at $3.00–$3.20. ⚠ **An own-results print has ONE party; §4 requires an event between TWO.** A dedicated second-order screen for **named, contracted** GIS suppliers returned **nothing** — explicitly refusing to list packaging, ingredient or logistics names as *"an inference based on industry exposure rather than a disclosed relationship."* The only named counterparty is **Walmart at 22% of GIS sales** — **a CUSTOMER (wrong direction) and <1% of Walmart's revenue (wrong magnitude)**. ⚠ **The six-session carry item is DISCHARGED.** |
| T-2026-09-23-02 | **LH** | **premise**, then **part 3** | **CMS preliminary Clinical Lab Fee Schedule rates for 2027–2029, ~15% cuts, 09-21.** ⚠ **A REGULATOR IS NOT A COMPANY A** — the same object as the FOMC's +25bp, already disposed, but more seductive because it is sector-specific and carries a number. ⚠ **And the sign is wrong: a 15% cut has no beneficiary in a long-only book.** Part 3 kills it independently — the rates are **PRELIMINARY** and apply to **CY2027–2029**, past two quarters, with a comment period still to run (rule (vi)). Labcorp itself **maintained its 2026–2029 outlook.** |
| T-2026-09-23-03 | **CNC** / MOH / OSCR | **part 1**, then **part 2** | **ACA enrollment halted for >760,000 enrollees, $2.2B estimated taxpayer saving, 09-22.** ⚠ **Second government-policy premise failure of the same morning, from a different agency.** The only buy-direction sentence — *"removing fraudulent enrollees lifts margin"* — **needs an "and also" the moment it is written.** Part 2 fails outright: the reporting *"does not quantify the revenue or membership impact"*, **760,000 is industry-wide with no per-company split**, and **$2.2B is money the government STOPS paying**, not revenue to anyone (rule (viii)). **OSCR also fails §3 on cap.** |
| T-2026-09-23-04 | **ELMT** | **§3**, then **part 3** | **Tungsten West ↔ Elmet, eight-year binding tungsten-concentrate offtake, 09-22/23.** ⚠ **The best-disclosed transaction to enter this funnel in some time — both parties named, >1,000 t/yr WO₃, >$230M/yr, ~£1.4B, eight-year term. NOTHING is withheld.** It fails anyway: **ELMT is a ~$634M microcap** against a **$10B** floor, and **Tungsten West is AIM-listed**. The **>$230M/yr is revenue to the ineligible party and COST to the buyable one** (rule (viii)). **Eight years kills part 3 regardless.** |
| T-2026-09-23-05 | **LHX** | **part 2**, plus **premise** | **US Navy (NAWCWD China Lake) ↔ L3Harris, multi-year Tomahawk component agreement, 09-23.** **LHX is the named contractor — first-order.** ⚠ **NO CONTRACT VALUE, no start date, no end date, no scope detail.** Part 2 unwritable. ⚠ **A separate $22.9B / seven-year RAYTHEON Tomahawk contract appears in the same search — AUGUST, different contractor, different contract. DO NOT let that number migrate into this entry.** Rule (v) blocks the supplier route: not one supplier is named. Rule (iv) — **LHX is a recurring ticker.** |
| T-2026-09-23-06 | **GFS** | **part 2**, plus **premise** | **Quantinuum's $100M CHIPS Act award, 09-23, naming GlobalFoundries and Monarch Quantum as operational partners.** **GFS is a named partner — first-order.** ⚠ **$100M is FEDERAL FUNDING TO A THIRD PARTY, not segment revenue at GFS** (rule (viii)), **and the source "did not specify how the funding would be allocated between them."** Even on the impossible reading that all $100M lands at GFS as revenue, it is **~1.5% against a 10% floor.** ⚠ **Second GFS rejection in two sessions on two unrelated events, both on an UNALLOCATED HEADLINE NUMBER.** |

⚠ **THE PATTERN OF THE DAY, STATED ONCE: TWO OF SIX THESES DIED ON THE SAME PREMISE — "A
GOVERNMENT ACTION IS NOT A COMPANY A" — FROM TWO DIFFERENT AGENCIES ON ONE MORNING.** A policy
action is dated, sourced, quantified and market-moving, which makes it **feel** like a
corporate event. It still has **one party**, which is one short of what §4 requires. ⚠ **And
both were CUTS: a long-only book cannot trade money being withdrawn from a sector unless some
named party receives it, and in neither case does anyone.**

### SELL — none

⚠ **NO SUBJECT EXISTS.** `positions.md` holds **zero satellite blocks** and
`alpaca.py positions` returns **one row, core VOO**. §5.1 (thesis invalidation) and §5.2 (time
stop) were **not evaluated because there is nothing to evaluate** — no invalidation condition
has ever been written in this account, so there is nothing to falsify. **Zero `perplexity.py`
news-check calls were due on the §5.1 path and zero were made.**

⚠ **Read that precisely: this is the ABSENCE OF A SUBJECT, not a clean bill of health.** §5.1
through §5.4 remain **untested code paths**, twenty-seventh consecutive session. **§5.4 is not
armed** — it arms on the first **satellite** fill, and the 09-03 core fill was not one.

**Core VOO is not a candidate for any sell rule and is not listed here.** §5 exempts it.

### REBALANCE — none

**Core is IN BAND.** `alpaca.py sleeves` at 08:20 ET: equity **$100,504.14**, core
**$70,504.14 = 70.15%**, satellite **$0 = 0.0% (count 0)**, cash **$30,000.00 = 29.85%**,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: −151.24`.

⚠ **§2 rebalances at the 65/75 BAND EDGE, not to the exact 70% target, so no delta inside the
band is an action at any size.** The overshoot is **0.15% of equity against a band edge 4.85
points away.** **Thirty-fifth consecutive run inside a 0.63-point range (69.59–70.22).**

---

## Notes for the 09:35 run

- ⚠ **This plan is FRESH and EMPTY, and those are TWO SEPARATE FINDINGS.** A fresh empty plan
  and a stale plan produce an **identical zero-order run**, which is why the §2 gate is decided
  on **`plan_date`** and never on the outcome. **Check the date. Do not infer freshness from
  the fact that there was nothing to do.**
- ⚠ **The staleness gate has now been exercised 24 times and has NEVER fired; its alert path
  remains UNTESTED CODE.** Twenty-four quiet opens are **not** evidence it works. **The first
  morning it fires will, by construction, be a morning when the pre-market run failed — i.e.
  exactly the morning with no fresh notes to lean on. Read routine 2's Step 2 then; do not
  recall it.**
- **`core_established: true`** since 09-03. **Step 3's bootstrap path is permanently closed.**
  Do not invoke `--core`.
- ⚠ **Idle cash of 29.85%, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
  opportunity routine 2 may act on.** Routine 2 executes **only what this file contains**. A
  position opened at 09:35 without a plan entry routes **around** the discipline rather than
  satisfying it. **There are no BUY intents. That is the instruction.**
- ⚠ **DO NOT REHABILITATE ANY OF TODAY'S SIX REJECTIONS AT THE OPEN. A rejection is not a
  queue.** None of them becomes eligible at a different price: GIS has no second party, LH and
  CNC have no beneficiary, ELMT is a microcap, LHX and GFS have no allocated figure.
- ⚠ **`lastday_price` reads 712.78 against an official 712.69 and DID NOT REBUILD OVERNIGHT —
  it is yesterday's stale value, carried across a session boundary and now nine cents wrong.**
  Use `bars --adjustment all` for any close and a fresh `quote` for any execution reference.
- **`alerts.md` is empty — zero open incidents, zero SYSTEMIC.** Nothing operational needs
  flagging to the human today beyond the standing open items in `state.md`.
