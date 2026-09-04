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
plan_date: 2026-09-04
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-04 at 09:30 ET (`alpaca.py clock`: `is_open: false`,
`next_open: 2026-09-04T09:30:00-04:00`, timestamp `08:27:46 ET`). **Not a holiday** — the market
is closed because it is pre-market, and `next_open` is today.

**One pre-market run today, at 08:27 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account).

**Tape context:** VOO's broker mark is **710.94** (`lastday_price` 710.72). The official
`bars --adjustment all` close for 09-03 was **710.70**; the two are not interchangeable and
neither is a pre-market execution reference. Pull a fresh quote at 09:35.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and the day's research produced no eligible candidate.

---

## Intents

### BUY — none

No buy intents. New positions were fully permitted this run — breaker INACTIVE, weekly cap at
**0 of 3**, satellite sleeve **empty with 29.88% cash**, no restricting note in `control.md`.
Nothing was blocked. **The research simply did not produce an eligible candidate.**

One candidate reached ticker stage and was rejected four ways:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-04-01 | CLF | part 1, part 2, part 3 **and** §3 | Surfaced as "the only domestic producer of GOES" against a cluster of US transformer capacity expansions (Eaton, Siemens, Southwire, HSP US, Niagara). **No source ties Cliffs to any of those projects** — a sole-producer fact is market structure, not a supplier relationship. Electrical-steel revenue is **not disclosed anywhere** in the 10-K/10-Q. The projects complete **2028**. And market cap is **$7.01B, below the §3 $10B floor** — `alpaca.py buy` would have refused it. |

**Fourteen further items were dropped before thesis stage.** The three that matter, because all
three are cases where a dedicated sourced screen came back **explicitly empty**:

- **Lululemon −18% on a second consecutive guidance cut.** No source names a publicly traded US
  company gaining share. The two names sources do cite — **Alo Yoga and Vuori — are private**.
- **Snowflake beat and raise, +16.55%.** No source names a US-listed supplier or partner whose
  revenue rises with Snowflake consumption.
- **The grid/transformer capacity cluster.** No source names a US-listed supplier to any of the
  five announced projects.

The rest: Ionis' ZANVASTRO approval (only partner is **Italy-listed Recordati**; $295M peak
*global* sales, ex-US filings **in 2027**), Nscale–Figure $3.5B (**both private**), AEVEX, Curia,
Calumet (**private**; the TTM reference is a **June 2026** facility, three months stale),
Cipla/Qilu (non-US, and the mechanism runs **against** Merck in a long-only book), LG Energy
Solution / Smackover Lithium (Korea-listed buyer, sub-floor US parent), UpSolv/NexKemia,
Unusual Machines/Altana, the Caltrain contract (**consultant's name is blank in the source**),
Modular Medical, and the ISM / claims / payrolls / Waller macro items. Full funnel in
`research_log.md`.

Notes for the open run, carried so nothing is re-derived at 09:35:

- **Nothing here is queued, deferred, or waiting for a better entry.** CLF is not a "watch for
  a dip" — it fails §3 on market cap, which no price move fixes in the right direction, and it
  had no sourced mechanism to begin with.
- **⚠ Do not reach for NKE, DECK, ONON, UAA, GPS/Athleta or any athletic-apparel name on the
  Lululemon story.** The screen named **only private companies** as share-takers. Every listed
  peer is an ecosystem read-through with no sourced connection — that is the RTX failure, and
  it is the single most fluent sentence available on the tape today.
- **⚠ Do not reach for a hyperscaler on the Snowflake story**, and do not reach for ETN, PWR,
  GEV, HUBB, NVT, AMRC or any grid name on the capacity cluster. Same reason: no sourced
  supplier relationship, and Eaton is Company A announcing its own capex.
- **Do not reach for LITE, MU or LHX.** None entered today's funnel, no source named them, and
  their filters were not re-run. Third consecutive day recording that this is *absence of
  evidence*, not resolve.
- **A quiet day is not a reason to lower the bar at the bell.** §4: the correct output of most
  research runs is no trade.

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — the ledger reads
*(none)* and the broker returns exactly one row, **VOO, which is core and exempt from §5
entirely**. Compare satellite blocks to satellite positions, not raw ledger to raw broker.
§5.1–5.4 have nothing to evaluate: no invalidation condition to test, no timing window to
expire, no entry price or high-water mark to measure a stop against.

### REBALANCE — none

- current_core_pct:  **70.12%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:27 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: −124.80`
- action: **none.** The −$124.80 delta is 0.12% of equity and is VOO's overnight mark moving,
  not drift. §2 rebalances at the band edge, not to the exact target.
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: ISO Monday
  of 2026-09-04 (Friday) is **2026-08-31**, which matches `week_of` — no reset was due. **Next
  boundary is Monday 2026-09-07.**
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:27 ET.
- **August payrolls print this morning** (consensus +56k, unemployment 4.1%). It is a macro
  release with no intent attached to it in this plan. It is **not** a reason to act at the open.

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
