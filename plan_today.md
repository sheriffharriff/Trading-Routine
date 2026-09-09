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
plan_date: 2026-09-09
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-09 at 09:30 ET (`alpaca.py clock` at 08:26:53 ET: `is_open:
false`, `next_open: 2026-09-09T09:30:00-04:00`, `next_close: 2026-09-09T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.

**One pre-market run today, at 08:26 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,460.43**).

**Tape context:** VOO's broker mark is **701.29** (`lastday_price` **704.07**,
`change_today` −0.395%). Neither number is an execution reference — **pull a fresh quote at
09:35.** The core position shows `unrealized_pl` **−$539.56 (−0.771%)** against the 706.74
fill, its fifth consecutive negative mark. That is a price move, not an error, and **§5
exempts core from all four sell rules** — there is no action attached to it at any number.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and five candidates were researched to a full thesis entry and all five
were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker INACTIVE, weekly cap
at **0 of 3**, satellite sleeve **empty with 30.16% cash**, no restricting note in `control.md`.
**Nothing was blocked. The research did not produce an eligible candidate.**

Five candidates reached ticker stage with a full `research_log.md` entry:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-09-01 | QCOM | §4 headline name | Every thesis part writable, all three filters pass — and **Qualcomm is Company A**. Buying the press release is not a second-order trade. |
| T-2026-09-09-02 | FN / COHR / LITE / CRDO | part 1, and part 2 | The 1.6T optical piece traces to **Alphawave IP Qualcomm already owns** — the supplier opportunity is the part Qualcomm internalised. No source names any of the four. Mechanism needs two "and" clauses. |
| T-2026-09-09-03 | GLW | §4 priced-in, part 3, headline name | **+11.63%** in five sessions; supply runs **2027–2032**; and Corning is a **named party** to the announcement. Three independent failures. |
| T-2026-09-09-04 | MTZ | parts 1, 2 and 3 | **No reporting names any construction contractor** for Verizon's fiber build. Verizon's share of MasTec revenue is undisclosed. Work begins **2027** — beyond two quarters. |
| T-2026-09-09-05 | PBR / EC / YPF / VIST | §3 universe | All foreign issuers. No US-listed producer was named by any source, and crude exposure is **first-order** anyway. |

**Two genuinely new, well-sourced, US-listed events came through the funnel today and neither
produced a tradeable second-order name.** Both are confirmed against company disclosure, not an
aggregator — standing rule (iii) satisfied for the first time this month on an AI-capex item:

| Event | Date | Confirmed by |
|---|---|---|
| Qualcomm–Amazon custom AI silicon + 1.6T optical | **09-08** | Qualcomm press release + 8-K; warrant 25M sh @ $161.26 vs up to **$60B** of purchases |
| Verizon–Corning fiber supply, **80M+ miles**, 2027–2032 | **09-08** | Corning press release; "multi-billion dollar," terms undisclosed |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ Do not reach for QCOM at the bell, and be ready for it to look cheap.** It **gapped to
  180.46 and touched 183.44 (+8.7%) on 09-08, then faded to close at 174.08 (+3.15%)**. A stock
  that gave back most of an event pop is the most inviting thing on this tape. **It is still the
  headline name (§4).** The rejection does not flip at a lower price.
- **⚠ The §4 priced-in filter returns `false` for QCOM (+2.70% over five sessions) and that
  number is misleading.** Four drifting-down sessions absorbed a 9% event-day pop. **This is a
  new defect shape — the mirror of the LITE one — and it is with the human. Do not reinterpret
  the filter, and do not treat its "pass" as clearance for QCOM or anything else today.**
- **⚠ Do not reach for AMZN or VZ either.** Both are named counterparties in the two events —
  the one thing §4 says explicitly not to chase.
- **⚠ FN (Fabrinet) passed the priced-in check at +0.83% and that is not corroboration.** Its
  mechanism had no source at all. A clean filter number on an unsourced mechanism is the shape
  to distrust, not the shape to act on.
- **⚠ The BSX/MDT/ABT item does not reopen today.** The five-session window now genuinely
  contains the 09-08 recall — **MDT +1.90%, now `priced_in: false`, "passes."** It changes
  nothing: **both were rejected on part 2**, because neither company discloses SCS or
  neuromodulation revenue at a grain that permits a dollar path, and a new price window does not
  create a disclosure. Filters re-run for the record only. **Do not read that "pass" as an
  opening.**
- **The macro tape is loud and none of it is actionable.** Brent near **$100** on US–Iran
  escalation and Hormuz risk; August payrolls **+162k vs ~56k consensus**; September hike odds
  **~58.4%**; 10-year **~4.8%**; **August CPI Friday 09-11**. No segment, no dollar path, no §4
  mechanism. **Not a reason to act at the open in either direction.**
- **Do not reach for LITE, MU or LHX.** LITE surfaced today only inside the rejected optical
  sweep (T-2026-09-09-02) and died with it at **+7.01%, `priced_in: true`** — that is a fresh
  rejection on its own filter, not a revival and not a resolution of the open human question.
  MU and LHX did not enter the funnel at all. **Absence of evidence, not resolve** — sixth
  consecutive day.
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

- current_core_pct: **69.84%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:26 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +161.88`
- action: **none.** The +$161.88 delta is **0.16% of equity** — VOO's overnight mark moving, not
  drift. §2 rebalances at the **band edge** (65/75), not to the exact target. 69.84% is not a
  rebalance, and neither were 69.92%, 69.96% or 69.98%.
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: the ISO
  Monday of 2026-09-09 (Wednesday) is **2026-09-07**, which matches `week_of` — **no reset was
  due**. Next boundary is Monday 2026-09-14.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:26 ET.
- **⚠ Two-price trap.** Use `bars --adjustment all` for any official close and a fresh `quote`
  for execution. Never a `positions` field for either. Today's shapes already differ: broker mark
  **701.29**, `lastday_price` **704.07**, against yesterday's official close **704.16**.

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
