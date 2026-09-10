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
plan_date: 2026-09-10
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-10 at 09:30 ET (`alpaca.py clock` at 08:23:47 ET: `is_open:
false`, `next_open: 2026-09-10T09:30:00-04:00`, `next_close: 2026-09-10T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.

**One pre-market run today, at 08:23 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,266.82**).

**Tape context:** VOO's broker mark is **699.3377** (`lastday_price` **700.87**,
`change_today` −0.219%). Neither number is an execution reference — **pull a fresh quote at
09:35.** The core position shows `unrealized_pl` **−$733.17 (−1.047%)** against the 706.74
fill, its sixth consecutive negative mark and the first past −1%. That is a price move, not
an error, and **§5 exempts core from all four sell rules** — there is no action attached to
it at any number.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and six candidates were researched to a full thesis entry and all six
were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker INACTIVE, weekly cap
at **0 of 3**, satellite sleeve **empty with 30.22% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

Six candidates reached ticker stage with a full `research_log.md` entry:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-10-01 | LMT | §4 headline name, part 3 | **No published source names any US-listed supplier or subcontractor** on JASSM/LRASM or MK 48. The only work-share disclosed is Lockheed's own facility split. Lockheed is Company A. |
| T-2026-09-10-02 | GFS | §4 priced-in, part 3, headline name | **+4.53%** in five sessions; volume production **early 2027**; and GlobalFoundries is a **named party** to the agreement. Three independent failures. |
| T-2026-09-10-03 | EQT | part 2 (magnitude), part 3 | **~1 TWh/yr ≈ 3.4 Bcf against 634 Bcfe in Q2 alone — about 0.14% of annual volume**, versus a 10% floor. Deliveries 2027–2036, deal not yet executed. |
| T-2026-09-10-04 | LEU | §3 universe, §4 priced-in, parts 2 and 3 | **~$3.4–3.8B market cap, below the $10B floor.** +7.76% in five sessions. Deliveries "before the end of the decade." |
| T-2026-09-10-05 | TBBK / CASH / GDOT / CCB | §3 universe | **All four are $0.7B–$2.8B**, far below the floor — and the Chime read-across is **negative**, which this long-only book cannot express anyway. |
| T-2026-09-10-06 | (no ticker) | no Company B, part 3 | Bayer–Neste canola: **no source names any US-listed beneficiary**; Bayer withholds the "newgold® network" partners. Hybrid launch **fall 2027**. |

**Four genuinely new, dated, sourced commercial events came through the funnel today and each
second-order branch died for a different reason.** Standing rule (iii) was run on all four and
all four are new to their companies' own disclosure:

| Event | Date | Confirmed by |
|---|---|---|
| DoD → Lockheed, **$826.0M** JASSM/LRASM large lot + **$257.3M** MK 48 MOD 7 | **09-09** | DoD daily contracts list (war.gov), contract numbers FA8682-24-C-B001 P00020 and N00024-23-C-6411 |
| Monolithic Power ↔ GlobalFoundries, MPWR process at GF **300mm Singapore**, volume **early 2027** | **09-09** | Investing.com 09-09, carried in 09-10 summaries |
| Ignitis ↔ EQT subsidiary, LNG **10 cargoes ~1 TWh each, 2027–2036**, HH/TTF-linked | **09-10** | Ignitis material-event notice; approvals still outstanding |
| Centrus ↔ Radiant, multi-year **HALEU** with prepayments, deliveries **before end of decade** | **09-09** | Centrus announcement via TipRanks |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ Do not reach for LMT at the bell, and expect its filter number to look inviting.** It
  returns **−3.61%, `priced_in: false`, "passes"** — on the same day it booked $1.08B of awards.
  It passes because a 3.61% **decline** fits inside a 4% band. **Lockheed is Company A (§4)**, and
  a falling price is not a second-order thesis. **The rejection does not flip at a lower price.**
- **⚠ Do not fill in the JASSM/LRASM supplier chain from memory.** A dedicated screen returned
  **no named US-listed supplier**. Solid-rocket-motor and energetics names will suggest
  themselves; naming one is **standing rule (v)** (industry fact dressed as a transaction),
  compounded by **rule (iv)** for the recurring one. The related **Nitradyn $581M IMX-104 award**
  was checked and dropped — Nitradyn is private, no listed energetics supplier is named.
- **⚠ Do not reach for GFS or MPWR.** GFS is a **named party** and **`priced_in: true` at
  +4.53%** — a marginal failure is still a failure, and **0.53 points past the threshold is not
  a rounding error to be reasoned away.** MPWR is the announcing party and *incurs* the cost.
- **⚠ EQT will be the tempting one, because everything except the size was clean.** Mechanism
  single-clause, correlation clear, **§3 clear at ~$34.5B**, and **`priced_in: false` at
  −1.72%.** It died on **arithmetic**: one ~1 TWh cargo a year is **~0.14% of annual volume**
  against §4.2's **10%** floor, and deliveries start **2027**. **A clean filter sheet is not a
  thesis.** Do not revisit it at the open.
- **⚠ Do not reach for LEU or the sponsor banks — both fail §3 on market cap.** LEU **~$3.4–3.8B**;
  TBBK **~$2.0–2.8B**, CASH **~$1.7B**, GDOT **~$0.76B**, CCB **~$0.7–0.8B**. **§3 is a floor, not
  a preference**, and no story outweighs it. **CCB additionally fell ~43% on 09-04/09-07 on
  "banking services issues" and is under securities-fraud investigation** — that is distress from
  outside today's window, not a catalyst.
- **The macro tape is loud and none of it is actionable.** **August PPI released this morning,
  August CPI tomorrow 09-11**; 10-year **4.85%**, highest since Nov 2023; **30-year auction
  today**; Treasury buyback of up to **$6B** of 10–20yr paper; mortgage rates **6.85%**, highest
  in over a year; MBA refinance index lowest since May 2025; **September hike odds ~59%** into
  the 09-15/16 FOMC. No segment, no dollar path, no §4 mechanism. **Not a reason to act at the
  open in either direction.** The read-across to housing runs the **wrong way** for a long book,
  which is not an invitation to reinterpret it as a short — this strategy has no short.
- **⚠ ORACLE AND ADOBE REPORT AFTER TODAY'S CLOSE; MACY'S THIS MORNING.** They landed **after**
  this survey closed and are **not** in today's funnel — that is a sequencing fact, not an
  oversight. **Oracle in particular carries an AI-capex read-across surface.** Whatever they
  print is **tomorrow's pre-market job**, not a reason to act at 09:35 today.
- **Do not reach for QCOM, AMZN, GLW, VZ, MTZ or FN.** Yesterday's rejects, all still rejected —
  QCOM and GLW on §4's headline-name rule, MTZ on parts 1/2/3, FN on an unsourced mechanism.
  **None becomes a buy at a different price.**
- **Do not reach for MU or LHX.** Neither entered today's funnel and their filters were not
  re-run — **absence of evidence, not resolve.** Seventh consecutive day. **LHX is the specific
  name the LMT supplier gap invites; that invitation is the reason this line is here.**
- **A quiet day is not a reason to lower the bar at the bell.** §4: the correct output of most
  research runs is no trade.

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — the ledger reads
*(none)* and the broker returns exactly one row, **VOO, which is core and exempt from §5
entirely**. Compare satellite blocks to satellite positions, not raw ledger to raw broker.
§5.1–5.4 have nothing to evaluate: no invalidation condition to test, no timing window to
expire, no entry price or high-water mark to measure a stop against. **No §5.1 Perplexity
invalidation query was issued and none was due — there is no position to check news against.**

### REBALANCE — none

- current_core_pct: **69.78%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:23 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +219.95`
- action: **none.** The +$219.95 delta is **0.22% of equity** — VOO's overnight mark moving, not
  drift. §2 rebalances at the **band edge** (65/75), not to the exact target. 69.78% is not a
  rebalance, and neither were 69.83%, 69.84%, 69.92%, 69.96% or 69.98%.
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: the ISO
  Monday of 2026-09-10 (Thursday) is **2026-09-07**, which matches `week_of` — **no reset was
  due**. Next boundary is Monday 2026-09-14.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:23 ET.
- **⚠ Two-price trap.** Use `bars --adjustment all` for any official close and a fresh `quote`
  for execution. Never a `positions` field for either. Today's shapes already differ: broker mark
  **699.3377**, `lastday_price` **700.87**, against yesterday's official close **700.805**.
- **⚠ Tomorrow, Friday 09-11, is a weekly-review day and August CPI lands the same morning.**
  The review **must not quote the reject scoreboard as a result** — ten names over a few sessions
  is noise, not a sample. CPI is macro with no segment and no dollar path: **not a §4 mechanism
  in either direction.**

---

## Template

```
### BUY — <TICKER>
- thesis_id:      T-YYYY-MM-DD-NN   (must already exist in research_log.md)
- asset_type:     stock | etf
- market_cap:     $00.0B  (stocks only; §3 floor is $10B)
- market_cap_src: <source>
- notional:       $0.00   (≤5% of account value, §6)
- driver:         <catalyst, checked against every open position's driver>
- revalidate:     <what would make this dead by the open — the specific number to re-check>

### SELL — <TICKER>
- thesis_id:      T-YYYY-MM-DD-NN
- rule:           §5.1 invalidation | §5.2 time stop | §5.3 hard stop | §5.4 trailing stop
- evidence:       <the observable fact that triggered it>

### REBALANCE — core
- current_core_pct: 0.0%
- action:           buy | sell to return core to 70% (§2)
- notional:         $0.00
```

---

## No-trade days

An empty intent list is the expected output most days. §4: *"The correct output of most
research runs is no trade. A run that finds nothing worth buying is a successful run."*
When there is nothing to do, write that plainly here with the reasoning — do not pad the
list to look productive. The rejected candidates still go in `research_log.md`, which is
where the value of a quiet day actually lives.
