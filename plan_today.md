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
plan_date: 2026-09-17
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-17 at 09:30 ET (`alpaca.py clock` at 08:11:40 ET: `is_open:
false`, `next_open: 2026-09-17T09:30:00-04:00`, `next_close: 2026-09-17T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.
**Read the date, not the boolean.**

**One pre-market run today, at 08:11 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,376.99**).

**Tape context:** VOO's broker mark is **700.45** (`lastday_price` **693.24**, `change_today`
**+1.04%**). Neither number is an execution reference — **pull a fresh quote at 09:35.** The
core position shows `unrealized_pl` **−$623.00 (−0.89%)** against the 706.74 fill. §5 exempts
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
at **0 of 3**, satellite sleeve **empty with 30.19% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a BUY
intent exists. **Zero `alpaca.py move` calls are due at 09:35 — an absent check, not a skipped one.**

Three candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-17-01 | (no ticker) | part 1, plus §3 and part 3 | **Amazon ↔ Generac 8-K, 09-16: ~$2.4B of generator deliveries expected 2027–2028, up to $8B aggregate, plus a 1,693,745-share warrant at $200.9266.** The best-sourced event this log has seen — **and there is no Company B.** The only named supplier is **Weichai/Baudouin, Shenzhen- and HK-listed (§3 FAIL)**, with no dollar figure tied to Generac; **Generac is vertically integrated**, making its own engines, alternators, controls and enclosures; and deliveries are **2027–2028**, past §4.3. **GNRC itself is the named counterparty — first-order, not a §4 candidate at any price.** |
| T-2026-09-17-02 | (no ticker) | part 1 | **Fluence Energy cut FY26 guidance 09-16: revenue ~$3.0B → ~$2.4B, adj. EBITDA −$10M → −$200M**, from **~$450M of delays at its Houston contract manufacturing facility** plus **~$65M of late-delivery penalties**. **The contract manufacturer is never named** — one source even reports its corrective actions while withholding its identity. The penalized customers are unnamed too. The alternative read, *"competitors take the share,"* is the **shared-cause trap (5th instance)**. |
| T-2026-09-17-03 | (no ticker) | part 1 (rule v, rule i) | **Seven federal awards, 09-16/17, $6.3B of headline value: CACI $1.5B ceiling ($1.2B expected booked), S&K Aerospace $4.3B IDIQ, Amentum $150M ceiling (completion 2031), DCS $85M, AEVEX up to $92.2M, Conti Kight JV $74.9M, Kyndryl no value.** **Every named party is the awardee — Company A.** No subcontractor is named under any of them; **six of seven figures are ceilings.** |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ `alpaca.py move` IS STRUCTURALLY BLIND TO AN AFTER-HOURS EVENT, AND THAT MATTERS TO YOUR
  RE-VALIDATION STEP SPECIFICALLY — NEW OPEN ITEM (7).** `move --symbol GNRC --sessions 5` returned
  **186.55 → 175.19, −6.09%, `priced_in: true`** this morning, on the one name every source was
  discussing, **the morning after it reportedly surged after the bell on the Amazon deal** (reports
  range **+18% to over +40%**; **none is verifiable from our data plane**). `bars` confirms the last
  official close is **175.19**; `quote` shows the last print **175.19 at 15:59:57 ET**, a stale
  16:00:05 bid of **165.23** and **no ask at all**. **The five-session window ends at the last
  official close, so a candidate whose news breaks AFTER the close is measured against prices that
  predate the news.** **Your 09:35 re-validation inherits this exactly** — the gap does not enter
  `bars` until tonight's close prints, so a re-validation would pass such a candidate for the same
  wrong reason the pre-market check did. **Nothing is at risk today: there are no BUY intents, and
  GNRC is first-order.** **Do not reinterpret the filter — that is a human editing §4 or the script.**

- **⚠ THE FUNNEL GOT ITS BEST-EVER INPUT AND STILL PRODUCED NOTHING, FOR A THIRD DISTINCT REASON.**
  09-14/09-15 died on *"the source names the transaction and withholds the counterparty's number."*
  09-16 died on *"the counterparty is named, does disclose, and discloses roadmap not segment
  revenue."* **09-17's Amazon/Generac died because the supply chain is INTERNAL — Generac makes its
  own engines, alternators, batteries, controls and enclosures.** **File it as a third shape, not a
  variant.** The first two are disclosure failures a human could address by widening the evidence
  bar; **this one is a fact about the company that no evidence standard would change.**

- **⚠ THE "I KNOW WHO MAKES THE PART" TRAP ARRIVED A THIRD TIME AND THE TOOL CAUGHT IT FIRST.** The
  supplier screen volunteered that Cummins, Caterpillar or a US switchgear maker supplying Generac is
  **"a general industry possibility, but no retrieved source actually names them."** **That is RTX
  (09-01) and the Abrams/Honeywell screen (09-16) repeating.** **No US-listed Generac supplier was
  screened, and that is absence of a source, not a verdict on any name.**

- **⚠ RULE (v)'s CEILING SUB-SHAPE IS ONE DAY OLD AND IS ALREADY THE DEFAULT FORM.** Six of seven
  federal figures today are ceilings or "up to" amounts. **CACI's $1.2B "expected to book" is the
  only figure with commitment behind it, and it is the company's own estimate, not a contract term.**

- **⚠ THREE MARKETBEAT-STYLE "GUIDANCE" ALERTS IN ONE MORNING — THE GENERAL MILLS TRAP, TRIPLED.**
  **Ameren $5.25–5.45, Five Below $9.830–10.310, DaVita $14.10–15.20** all arrived as instant-alerts
  stating guidance **issuance**, with **no prior figure and no source saying anything changed.**
  Rule (iii). **An alert worded to read like an event is still not an event.**

- **⚠ TWO PERPLEXITY RESULTS DISAGREED ON WHETHER AEVEX IS LISTED AT ALL** (one said listing status
  is not established, the other reported "NYSE: AVEX"). Immaterial today — AEVEX is the awardee and
  the figure is a ceiling — but **a listing status read off a news snippet is not a §3 check.**
  **`alpaca.py asset` is.**

- **Dropped before thesis stage, with reasons:** **Ford** raised FY26 adj. EBIT guidance to
  **$10–11B (+$1B at midpoint)** — **first-order, Company A**, no counterparty named. **Lululemon**
  and **Norwegian Cruise Line** — consolidated guidance cuts, **no counterparty at all**. **Philip
  Morris** — EPS raised **"for currency only"**, a translation adjustment, not an operational change.
  **Subaru ↔ onsemi** — the release itself says *"does not represent a supply agreement or production
  commitment. No financial terms were disclosed."* **Charter/Cox $34.5B** — **closed in late August**;
  the 09-17 item is a branding-integration story, rule (iii). **Union Pacific/Norfolk Southern** — a
  customer-support statement, no figure. **Illinois American Water / City of Venice, $770,000** —
  correctly sourced and **immaterial by four orders of magnitude**. **Medtronic LigaSure/Hugo** — the
  same item dropped 09-16, already a disposed reject. **Robinson Pharma, Powerus** — named, private,
  no money attached.

- **The FOMC is settled and did not enter the funnel.** +25bp to **3.75–4.00%** on 09-16, unanimous,
  first US hike since 2023, one more signalled; projections 2026 GDP **2.3%**, PCE **3.7%**,
  unemployment **4.1%**; 10-year reported at **5.03%**. **No Company A, no segment, no dollar path.**
  **It is an input to the environment, and VOO's +1.04% pre-market mark is a price move, not a
  thesis.**

### SELL — none

**No open satellite positions.** §5.1–§5.4 have no subject for the **nineteenth consecutive
session**. `sell_rule_status` is **absent, not blank** — there is no thesis to invalidate, no
`timing_window` to expire, no `entry_price` to measure −7% against, and no `highest_close` to
measure −10% against. **Nothing is near triggering because nothing exists to trigger.** All four
remain **untested code paths**, and nineteen sessions of "no exits" record the absence of a
subject, not nineteen clean bills of health.

**Zero Perplexity invalidation queries were issued this run and none was due** — §5.1 reads an
`invalidation` line that does not exist.

### REBALANCE — none

**Core is in band and no rebalance is due.** `alpaca.py sleeves` at 08:11 ET: equity
**$99,376.99**, cash **$30,000.00**, core **$69,376.99 = 69.81%**, satellite **0.0% (count 0)**,
cash **30.19%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +186.90`.

§2 rebalances at the **band edge (65/75)**, **not to the exact 70% target.** The $186.90 delta is
**0.19% of equity** and is not an action — **the smallest delta recorded in this range so far.**
**Twenty-first consecutive run inside a 0.39-point range (69.59–69.98).**

---

## What the open run should actually do

1. **Check `plan_date` against today's ET date.** It reads **2026-09-17**. If today is not that
   date, this plan is stale — log it, alert, and skip to the core/rebalance section.
2. **Execute nothing.** There are no BUY, SELL or REBALANCE intents, and **that is the plan, not a
   gap in it.**
3. **Do not go looking for something to do.** 30.19% idle cash, an INACTIVE breaker and a weekly
   cap at **0 of 3** are **not an opportunity this run may act on.** New positions route through
   pre-market research plus this execution run, always — a position opened at 09:35 without a plan
   entry would route around the discipline rather than satisfy it.
4. **Verify the empty plan is FRESH, not stale.** An empty plan that is current and a plan that is
   out of date **produce identical zero-order runs and are not the same run.** The difference is
   invisible in the order count, so read the date rather than the outcome. **The stale-plan gate
   has now been exercised eighteen times and has never fired — its alert path REMAINS UNTESTED
   CODE.** Eighteen quiet opens are not evidence the gate works.
5. **Pull a fresh quote for anything you price.** The broker's `current_price` is a **live
   bid/ask midpoint**, not a close — 700.45 this morning against yesterday's official 693.215 is
   that mechanism in pre-market. `bars --adjustment all` for a close, a fresh `quote` for
   execution, **never a `positions` field for either.**
6. **GNRC is not yours to look at.** It will likely gap hard at the open on the Amazon deal. **It is
   the named counterparty in that announcement — Company A's direct beneficiary, first-order, and
   outside §4 at any price.** It is **not in this plan**, and a name moving on the tape is not an
   intent. **Do not let the one loud ticker of the morning become a trade at 09:35.**
