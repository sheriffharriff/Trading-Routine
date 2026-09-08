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
plan_date: 2026-09-08
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-08 at 09:30 ET (`alpaca.py clock` at 08:24:02 ET: `is_open:
false`, `next_open: 2026-09-08T09:30:00-04:00`, `next_close: 2026-09-08T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.
**This is the first live session of the week**; Monday 2026-09-07 was Labor Day.

**One pre-market run today, at 08:24 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity $99,930.66).

**Tape context:** VOO's broker mark is **706.04** (`lastday_price` **708.01**,
`change_today` −0.278%). Neither number is an execution reference — **pull a fresh quote at
09:35.** The core position shows `unrealized_pl` **−$69.33 (−0.099%)** against the 706.74
fill, its first negative mark; that is a price move, not an error.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and four candidates were researched to a full thesis entry and all four
were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker INACTIVE, weekly cap
at **0 of 3**, satellite sleeve **empty with 30.02% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

Four candidates reached ticker stage with a full `research_log.md` entry:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-08-01 | CAT | parts 2 and 3 | Named vendor of the gas gensets at Anthropic/Nscale's 460 MW West Virginia campus — a genuinely sourced link. But the site services **late 2027**, CAT lead times run **into late 2028**, and one 460 MW order is **under 1% of a $32.2B segment** sitting inside a **$72B backlog**. CAT has **already guided** to data-center power demand — the customer's name is new, the demand is not. |
| T-2026-09-08-02 | AVGO | part 1 (structure) | **Broadcom is Company A**, the named TPU supplier in the story. And the Google/Broadcom 5 GW agreement is from **May 2026**, re-reported 09-06. |
| T-2026-09-08-03 | MDT | part 2 | Medtronic **does not disclose neuromodulation or SCS revenue**. Finest grain is a $2.7B/qtr Neuroscience segment bundling unrelated businesses. Part 2 not writable without guessing. Part 1 also unsourced. |
| T-2026-09-08-04 | ABT | part 2 | Same, worse — no SCS line disclosed, and any plausible figure is **low single-digit % of ~$45B revenue, under the §4.2 10% floor**. |

**The AI-compute complex had already moved before this run reached it.** Every name with a
sourced link to the week's dominant story failed the §4 priced-in check outright:

| Ticker | 5-session move | Verdict |
|---|---|---|
| IREN | **+26.08%** | LATE |
| BE | **+20.04%** | LATE |
| HUT | **+17.79%** | LATE |

Roughly twenty further items were dropped before thesis stage — full funnel in
`research_log.md`. Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ The "$517 billion / 14.8 GW Anthropic compute contracts" headline is NOT a new event.**
  It is *The Information*'s **09-06 aggregation of eleven months of previously announced deals**
  (Amazon and Google/Broadcom from May; the $30B Azure commitment, the SpaceX Colossus lease and
  the Lambda commitment all reported 09-02). It will still be circulating at the bell and it
  will still look new, because the *articles* are new. **Do not treat it as a catalyst.**
- **⚠ Do not reach for AMZN, GOOGL, MSFT or NVDA on it.** They are the **headline counterparties**
  named in the story, which is the one thing §4 says explicitly not to chase.
- **⚠ HUT is not a "watch for a dip."** It had a real sourced mechanism — Yahoo Finance names
  Hut 8 as the developer of the 350 MW Texas site hosting Lambda's Anthropic capacity — and it
  was lost to **timing, +17.79% in five sessions**. That is a different failure from the usual
  unsourced one, and it does not become a buy at a lower price today.
- **⚠ Nscale, Firmus, Lambda, Fluidstack and SpaceX are all private (§3).** The Nscale West
  Virginia deal is the only genuinely new contract in the window and there is no listed way to
  express it that survives §4.
- **⚠ The BSX recall breaks TODAY, pre-market — the priced-in numbers on MDT (+3.26%) and ABT
  (−3.69%) cover five sessions that contain NONE of this news.** Those passes are not
  clearance; the filter is measuring a window that predates the event. Both are rejected on
  part 2 regardless, and **§4's correlation rule would permit at most one of them** in any case.
  **Do not revisit either at the bell because the tape moves on the recall.**
- **⚠ Do not short, and do not reach for BSX itself.** The mechanism runs *against* Boston
  Scientific, and this is a long-only book.
- **The August payrolls print (+162k vs +56k), the ~58% September hike probability, PPI
  Thursday and CPI Friday are macro with no segment and no dollar path.** No intent attaches to
  any of them. They are **not** a reason to act at the open.
- **Do not reach for LITE, MU or LHX.** None entered today's funnel, no source named them, and
  their filters were not re-run. **Absence of evidence, not resolve** — fourth consecutive day.
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

- current_core_pct: **69.98%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:24 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +20.80`
- action: **none.** The +$20.80 delta is **0.02% of equity** — the closest to target the core
  has sat since it was established, and it is VOO's overnight mark moving, not drift. §2
  rebalances at the band edge, not to the exact target.
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: the ISO
  Monday of 2026-09-08 (Tuesday) is **2026-09-07**, which matches `week_of` — **no reset was
  due**. Next boundary is Monday 2026-09-14.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:24 ET.
- **⚠ Two-price trap.** Use `bars --adjustment all` for any official close and a fresh `quote`
  for execution. Never a `positions` field for either.

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
