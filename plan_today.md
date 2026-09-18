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
plan_date: 2026-09-18
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-18 at 09:30 ET (`alpaca.py clock` at 08:16:15 ET: `is_open:
false`, `next_open: 2026-09-18T09:30:00-04:00`, `next_close: 2026-09-18T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.
**Read the date, not the boolean.**

**One pre-market run today, at 08:16 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,426.51**).

**Tape context:** VOO's broker mark is **700.90** (`lastday_price` **701.03**, `change_today`
**−0.019%**). **Neither number is an execution reference, and `lastday_price` 701.03 is NOT
yesterday's official close of 700.97** — it is six cents away, the same live-midpoint mechanism
this log has now documented five times. **Pull a fresh quote at 09:35.** The core position shows
`unrealized_pl` **−$578.43 (−0.826%)** against the 706.74 fill. §5 exempts core from all four sell
rules — **there is no action attached to it at any number, in either direction.**

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and four candidates were researched to a full thesis entry and all four
were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker INACTIVE, weekly cap
at **0 of 3**, satellite sleeve **empty with 30.17% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a BUY
intent exists. **Zero `alpaca.py move` calls are due at 09:35 — an absent check, not a skipped one.**

Four candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-18-01 | GFS / MRVL | part 2, and independently the §4 premise | **GlobalFoundries ↔ Marvell expanded multi-year SiGe capacity agreement, 09-17, Burlington VT, for NPO/CPO optical connectivity.** **No dollar value, no wafer volume, no quantified capacity increase in any source** — one commentary says flatly *"financial terms were not disclosed."* **Part 2 has no numerator.** Separately, **the only two companies any source names are the two signatories**; the dedicated second-order screen returned *"No other publicly traded U.S. company is named... as a direct counterparty or having direct revenue or cost exposure to this specific agreement."* **GFS is in GNRC's exact position from 09-17 — a named counterparty, first-order, outside §4 at any price.** |
| T-2026-09-18-02 | LEU | part 3 first, then part 2 | **Centrus ↔ Antares Nuclear multi-year HALEU supply contract, 09-17, with prepayments funding expansion.** **Deliveries begin "before the end of the decade / prior to 2030"** — **§4 part 3 caps the horizon at two quarters**, so rule (vi) killed it in one step. Then: **financial terms not disclosed**, **Antares is not publicly traded**, and **no source names any US-listed supplier to Piketon** — the only Piketon figure anywhere is a **$900M DOE task order with Centrus's own subsidiary**, i.e. the wrong direction. |
| T-2026-09-18-03 | (no ticker) | part 1 | **Lennar Q3 FY26, 09-17: adj. EPS $1.23 vs $1.29, revenue $8.05B vs $8.31B expected and $8.81B a year ago, annual delivery guidance cut on mortgage rates and affordability.** The mechanism sentence **needs an "and also" clause**, because Lennar's weakness and its suppliers' weakness are both downstream of **the same mortgage rate — a macro variable, not a transaction.** **Sixth shared-cause instance.** The screen for filings naming Lennar as a customer **with a quantified share returned nothing at all.** Also **negative-direction on a long-only book**, which is the weakest of the three objections and the one noticed first. |
| T-2026-09-18-04 | BLK | part 2 | **TotalEnergies ↔ Global Infrastructure Partners partnership, 09-18, African oil and gas infrastructure, US$1.8B capital contribution** (Business Wire). **Part 1 passes cleanly in one clause** — and part 2 dies because **the $1.8B is capital going OUT, not revenue coming IN.** **No source states BlackRock books any incremental revenue, names the segment, or gives a fee rate.** Sizing it would have required inventing a fee assumption. |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ THREE NAMED-BOTH-PARTIES TRANSACTIONS IN ONE WINDOW AND ALL THREE WITHHELD THE NUMBER.**
  GF↔Marvell, Centrus↔Antares and TotalEnergies↔GIP are all real, primary-sourced deals with both
  sides named. **Two say "financial terms were not disclosed" in so many words; the third discloses a
  capital contribution rather than a revenue figure.** **Part 2 could not be written for any of them.**
  This is carry-forward item (3)'s **first** binding form — the source withholds the counterparty's
  number — **firing three times in one morning.** **Recognise the cluster; do not re-derive it deal by
  deal.**

- **⚠ GNRC IS STILL NOT YOURS TO LOOK AT, AND TODAY THE PULL IS THE STRONGEST AND THE EMPTIEST YET.**
  Today is the first run whose `bars` history **contains** the 09-16 after-hours gap (**reported
  +29.9% on the 09-17 session**), so `move --symbol GNRC --sessions 5` would now return a large
  positive number and `priced_in: true`. **That is not a measurement of open item (7) — it is the
  filter working correctly one session late.** The defect itself was **already measured on 09-17**
  (186.55 → 175.19, −6.09%, `priced_in: true`). **There is no number left to collect.** This run made
  **zero** `move`/`quote`/`bars`/`asset` calls on GNRC — fourth consecutive refusal. **The previous
  costume was diligence; today's is completeness. Expect a new one.**

- **⚠ OPEN ITEM (7) IS UNCHANGED AND COSTS NOTHING AGAIN TODAY — BUT ONLY BECAUSE IT HAS NO SUBJECT.**
  `alpaca.py move`'s five-session window **ends at the last official close**, so a candidate whose news
  breaks after the bell is measured against prices that predate the news, **and your 09:35
  re-validation inherits this exactly.** **Zero BUY intents today means zero exposure — that is an
  absence of exposure, not a mitigation.** **Do not reinterpret the filter; that is a human editing §4
  or the script.**

- **⚠ THE "I KNOW WHO MAKES THE PART" TRAP ARRIVED A FOURTH TIME, AND THE TOOL CAUGHT IT FIRST AGAIN.**
  The Centrus screen volunteered that vacuum systems, compressors, valves and control-system vendors
  are **"general industry possibilities and are not tied to Centrus's Piketon facility by the cited
  sources,"** and the GF/Marvell screen said mapping optics vendors to that deal **"would be
  speculative."** **After RTX (09-01), Abrams/Honeywell (09-16) and Generac (09-17).** **No US-listed
  supplier was screened for either deal — absence of a source, not a verdict on any name.**

- **⚠ THE MARKETBEAT GUIDANCE-ISSUANCE TRAP TRIPLED AGAIN — FOURTH, FIFTH AND SIXTH INSTANCES THIS
  WEEK.** **Labcorp ($18.10–18.55 EPS, $14.7–14.8B revenue), Nucor (Q3 $5.55–5.65) and Steel Dynamics
  (Q3 $5.34–5.38)** all arrived as instant-alerts comparing new guidance to **consensus**, never to a
  **prior company figure**. Rule (iii). *(Nucor's coverage carried two irreconcilable ranges —
  $5.55–5.65 and $3.30–3.60 — inside the same scan. **A secondary aggregator can be internally
  inconsistent in one morning.**)*

- **⚠ A NEW TRAP WORTH A STANDING RULE: READ WHICH DIRECTION THE DISCLOSED DOLLAR FIGURE MOVES.**
  TotalEnergies/GIP's **$1.8B is a capital contribution — money paid in, not earned.** **A figure's
  presence is not the same as the figure part 2 asks for.** This is the mirror image of 09-17's
  Fluence finding, where a precisely quantified **loss** invited the assumption that the money went
  somewhere nameable.

- **Dropped before thesis stage, with reasons:** **Fluence Energy's FY26 cut** ($3.0B → ~$2.4B revenue
  midpoint; −$10M → −$200M adj. EBITDA) is **the same cut processed yesterday as T-2026-09-17-02**,
  re-covered — rule (iii). **ADM** raised 2026 adj. EPS **$4.15–4.70 → $5.15–5.60**: a genuine change,
  **first-order, no counterparty named.** **UnitedHealth** raised 2026 adj. EPS to **$19.50–20.00**
  with **no prior figure stated.** **Philip Morris** — the **currency-only** raise, disposed 09-17.
  **Lockheed Martin ↔ Pentagon AIM-260 JATM production framework (09-17)** — **the awarded party, no
  dollar figure at all, no supplier named**: rule (i) plus the rule (v) ceiling shape with the ceiling
  left blank. **Vicor** — licensing deal with an **unnamed OEM** plus its own NH fab expansion; **no
  counterparty exists to screen.** **Southwest** *reiterated* Q3 EPS. **Myriad Genetics** cut FY26
  guidance with **no figures in any source.** **Emera** is Canadian-listed (§3). **Aeluma** declines
  to guide. **Aethlon/North Immunology** and an **SEC tokenized-stock "innovation exemption"** —
  the source itself called the evidence too thin. **First Breach ↔ SAS Ammo** and **Oribiotech ↔ an
  unnamed biopharma (up to $120M)** — **private counterparties**, and the second does not name its
  buyer.

- **The FOMC remains settled and did not enter the funnel.** +25bp to **3.75–4.00%** on 09-16; major
  banks lifted prime **6.75% → 7.00%** effective 09-17. **That is an environment input with no Company
  A, no segment and no dollar path** — and a read-across from it to any bank is the **shared-cause
  trap**, because a bank actually affected discloses it itself and is first-order for that bank.

### SELL — none

**No open satellite positions.** §5.1–§5.4 have no subject for the **twentieth consecutive
session**. `sell_rule_status` is **absent, not blank** — there is no thesis to invalidate, no
`timing_window` to expire, no `entry_price` to measure −7% against, and no `highest_close` to
measure −10% against. **Nothing is near triggering because nothing exists to trigger.** All four
remain **untested code paths**, and twenty sessions of "no exits" record the absence of a
subject, not twenty clean bills of health.

**Zero Perplexity invalidation queries were issued this run and none was due** — §5.1 reads an
`invalidation` line that does not exist. **§5.4 is still NOT ARMED; it arms on the first satellite
fill.**

### REBALANCE — none

**Core is in band and no rebalance is due.** `alpaca.py sleeves` at 08:16 ET: equity
**$99,421.56**, cash **$30,000.00**, core **$69,421.56 = 69.83%**, satellite **0.0% (count 0)**,
cash **30.17%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +173.53`.

§2 rebalances at the **band edge (65/75)**, **not to the exact 70% target.** The $173.53 delta is
**0.17% of equity** and is not an action. **Twenty-fifth consecutive run inside a 0.39-point range
(69.59–69.98).**

---

## What the open run should actually do

1. **Check `plan_date` against today's ET date.** It reads **2026-09-18**. If today is not that
   date, this plan is stale — log it, alert, and skip to the core/rebalance section.
2. **Execute nothing.** There are no BUY, SELL or REBALANCE intents, and **that is the plan, not a
   gap in it.**
3. **Do not go looking for something to do.** 30.17% idle cash, an INACTIVE breaker and a weekly
   cap at **0 of 3** are **not an opportunity this run may act on.** New positions route through
   pre-market research plus this execution run, always — a position opened at 09:35 without a plan
   entry would route around the discipline rather than satisfy it.
4. **Verify the empty plan is FRESH, not stale.** An empty plan that is current and a plan that is
   out of date **produce identical zero-order runs and are not the same run.** The difference is
   invisible in the order count, so read the date rather than the outcome. **The stale-plan gate
   has now been exercised twenty times and has never fired — its alert path REMAINS UNTESTED
   CODE.** Twenty quiet opens are not evidence the gate works. **The first morning it fires will be
   a morning when this pre-market run failed — i.e. exactly the morning you have no fresh notes to
   lean on. Read Step 2 then; do not recall it.**
5. **Pull a fresh quote for anything you price.** The broker's `current_price` is a **live
   bid/ask midpoint**, not a close. **This morning supplies the cleanest example yet:
   `lastday_price` reads 701.03 while yesterday's official close was 700.97** — six cents apart,
   and the field is *named* for the prior day. `bars --adjustment all` for a close, a fresh `quote`
   for execution, **never a `positions` field for either.**
6. **GNRC is not yours to look at, and today the excuse is better than yesterday's.** Its gap is now
   inside `bars`, so a `move` call would finally return a "sensible" number. **That number measures
   nothing** — see the note above. **It is the named counterparty in the Amazon announcement,
   first-order, outside §4 at any price, and it is not in this plan.**
7. **Today is Friday.** The weekly review runs after the close and owes the **09-21 pre-market run**
   a written hand-off. **General Mills (~Sept 23 report) is carried forward again** — it still has
   not reported.
