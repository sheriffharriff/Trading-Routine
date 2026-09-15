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
plan_date: 2026-09-15
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-15 at 09:30 ET (`alpaca.py clock` at 08:15:43 ET: `is_open:
false`, `next_open: 2026-09-15T09:30:00-04:00`, `next_close: 2026-09-15T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.

**One pre-market run today, at 08:15 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,192.76**).

**Tape context:** VOO's broker mark is **698.59** (`lastday_price` **699.30**, `change_today`
**−0.10%**). Neither number is an execution reference — **pull a fresh quote at 09:35.** The
core position shows `unrealized_pl` **−$807.23 (−1.153%)** against the 706.74 fill. §5 exempts
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

Three candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-15-01 | CRWV | part 1 (also 2, 3) | BCE's **$52B / 1.2 GW Regina AI hub** MOU names CoreWeave — but the **300 MW is the pre-existing contract** and **none of the new 900 MW is allocated to anyone.** The mechanism sentence needs an "and also" to carry the economic claim. |
| T-2026-09-15-02 | (no ticker) | part 1 (rule v) | **LMT $1.2B PrSM Inc 2 + $8.4B Inc 1 mod; BA $13.4B KC-46 ceiling increase.** Two screens, both directions: *"no subcontractor, supplier or teammate is named"* and *"I could not verify any"* $10B+ company self-disclosing quantified KC-46/767/PrSM exposure. |
| T-2026-09-15-03 | (no ticker) | part 3 (also 1) | **Sempra ↔ Petrobras, 20-yr / 0.8 Mtpa LNG SPA** — sourced from **Port Arthur Phase 2, COD 2030–2031.** First delivery is 4–5 years out against §4.3's two-quarter cap. No supplier named, no dollar value disclosed. |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ YESTERDAY'S WEEKEND EXCUSE IS SPENT AND THE ANSWER IS STILL NO — THAT IS TODAY'S FINDING.**
  The 09-14 carry-forward said in writing that *"a thin Tuesday funnel would NOT have this
  excuse."* **This is that Tuesday**, it screened a full business day, and the event set was
  genuinely richer: **$8.4B, $13.4B, $52B, a 20-year LNG SPA, a $7.7B take-private.** **The events
  were there; the quantified counterparties were not.** Three screens returned, verbatim: *"no
  public source names any subcontractor, supplier or teammate with a specific dollar figure"*;
  *"I could not verify any US-listed company with market cap above $10 billion that discloses a
  quantified revenue exposure"*; *"no such announcement is clearly documented."* **§4's binding
  constraint is disclosure practice, not news volume and not thesis quality.**
- **⚠ NEW TRAP — A DOD DAILY CONTRACTS DIGEST IS NOT A SUPPLIER BREAKDOWN, AND IT LOOKS EXACTLY
  LIKE ONE.** A tracking summary listed **Boeing, Blue Halo, Olin Winchester, Rolls-Royce
  Solutions America and J&J Contractors** under the KC-46 heading with **three dollar figures**
  ($13.4B; $99,832,117; $788,361,894) and **no mapping between them.** Those are unrelated awards
  grouped by publication date. **Standing rule (v) wearing a table instead of a sentence — and a
  table is more persuasive than a sentence.** Recognise the layout; do not re-derive it.
- **⚠ CRWV IS THE NEAR-MISS AND THE MOST USEFUL REJECTION TO CARRY. Do not reach for it at the
  open.** It is the CART shape from 09-14 in a bigger costume: **a named counterparty inside a
  loudly quantified project, where the quantity attaches to the project and not to the
  counterparty.** The number was never missing — it was **the wrong number**, and a $52B headline
  makes that far harder to see than Kroger's silence did. CoreWeave's **300 MW is prior business
  re-reported as context** (standing rule (iii), independently fatal). It also returned
  **`priced_in: true` at −7.12%**, but **note the ordering: part 1 had already killed it.**
- **⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED AGAIN — SIXTH INSTANCE, AND AGAIN IT COST NOTHING.**
  **CRWV −7.12%** joins LITE −7.35%, LMT −3.61% (near-miss), LHX −4.47%, CART −5.79%, BWXT −6.30%.
  **CRWV was already dead at part 1 when the filter reached it**, so today adds an instance and
  **zero damage**. **Keep the two tallies separate** — the expensive instances are the ones that
  arrive **alive**, and LITE is still the only one: it passed the four-part thesis, was killed by
  a drawdown, and is **+10.58% vs VOO** since. **No run reinterprets the filter; that is a human
  editing §4 or `alpaca.py move`.**
- **⚠ SCREEN THE TIMING WINDOW EARLY ON ANYTHING WHOSE SUBJECT IS UNDER CONSTRUCTION.** The
  Sempra–Petrobras SPA is the ideal-looking §4 input — two named parties, disclosed volume, a
  binding 20-year contract — and it dies on the **calendar**, four to five years before first
  delivery. **Long-dated infrastructure offtakes will keep entering this funnel looking perfect.**
  Part 3 kills them faster than part 1 does, and that rejection survives a supplier being named
  later.
- **⚠ THE FOMC BEGINS TODAY AND DECIDES TOMORROW. NOT A CANDIDATE IN EITHER DIRECTION.** August
  CPI (headline **+0.4% m/m / +3.4% y/y**, core **+0.3% m/m / +2.4% y/y**) and UMich preliminary
  September confidence at **47.8, down from 51.7**, are the loudest items on the tape and have
  **no Company A, no segment, no dollar path.** **If it moves prices hard at the open or into
  tomorrow's decision, that is a price move, not a thesis**, and a core mark that moves with it
  carries no action because §5 exempts core.
- **⚠ Do not read the negatives as shorts.** Abbott's **$385M** formula settlement, Dave &
  Buster's FQ2 miss ($544.1M rev vs $556.8M consensus; adj. EBITDA $98.9M vs $120.4M; −$0.27 adj.
  EPS vs +$0.18 expected), the UMich drop. **This book has no short**, and §4 is a long-only
  second-order rule.
- **Financing is not a commercial event, and this window was full of it.** Amazon's **£4.25B**
  sterling notes closing (8-K, Item 8.01, 09-14), Sysco's **12.3M shares at $81**, Williams'
  **$2.75B** bond sale, Redwood's convertible, Enova withdrawing its Grasshopper applications,
  Trilogy Metals' **$17.8M** DoW equity investment. **None has a second-order surface.** Dropped
  before ticker work.
- **Also dropped before thesis stage:** **NextEra/Dominion** — a **$67B** merger already announced,
  with a **$1B/yr-for-5-years Virginia supplier program** offered contingent on approval and
  **no individual supplier named**; regulatory progress on a known deal is not a new transaction.
  **Williams / NESE** — the Third Circuit vacated New Jersey's water-quality certification for the
  **$1B** pipeline on **09-08**, outside the window, and the read-across to other Northeast
  midstream runs through a **court ruling, not a transaction** — the Macy's statute shape.
  **Baldwin Group take-private, $7.7B** — the acquirer (DFO Management) is private and the target
  is being removed from the market; Company A on both ends. **D-Wave / Commerce CHIPS up to
  $100M** and **COnovate / DOE $1.25M** — awarded parties, i.e. Company A, and the latter private.
- **Do not reopen the disposed rejects.** **BWXT** and **CART** (09-14); **ORCL**, **LHX**,
  **AVAV**, **SLI**, **M**, and **LMT, GFS, EQT, LEU, TBBK, CASH, GDOT, CCB, QCOM, AMZN, GLW, VZ,
  MTZ, FN, COHR, LITE, CRDO, MRVL, DY, PWR, BSX, MDT, ABT.** **None becomes a buy at a different
  price.** **LMT and ABT are on that list and both resurfaced in today's news as Company A** —
  that is not a reason to re-run their filters.
- **Do not reach for MU.** **Thirteen consecutive days** out of the funnel, no source has named
  it, filters **not** re-run — **absence of evidence, not resolve.** If it resurfaces *from a
  source*, re-run its filters and re-test the timing window from that day's date.
- **A quiet day is not a reason to lower the bar at the bell.** §4: the correct output of most
  research runs is no trade. **Thirty-six theses, zero positions, sixteen sessions.** That number
  is the strongest argument available for loosening the rule and it is **not the agent's argument
  to make** — §2 permits the cash, §4 says most runs end in no trade, and **both rules were
  followed.**

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — the ledger reads
*(none)* and the broker returns exactly one row, **VOO, which is core and exempt from §5
entirely**. Compare satellite blocks to satellite positions, not raw ledger to raw broker.
§5.1–5.4 have nothing to evaluate: no invalidation condition to test, no timing window to
expire, no entry price or high-water mark to measure a stop against. **No §5.1 Perplexity
invalidation query was issued and none was due — there is no position to check news against.
An absent check, not a skipped one.**

### REBALANCE — none

- current_core_pct: **69.76%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:15 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +242.17`
- action: **none.** The +$242.17 delta is **0.24% of equity** — VOO's overnight mark moving, not
  drift. §2 rebalances at the **band edge** (65/75), not to the exact target. **Thirteenth
  consecutive run inside a 0.26-point range (69.72–69.98); the core is not drifting.**
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: the ISO
  Monday of 2026-09-15 is **2026-09-14**, which matches `week_of` — **no reset was due.** Next
  boundary is Monday 2026-09-21.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:15 ET.
- **⚠ AN EMPTY PLAN THAT IS FRESH IS NOT THE SAME RUN AS A PLAN THAT IS STALE, THOUGH BOTH
  PRODUCE ZERO ORDERS.** This plan is dated **2026-09-15** and will match the ET date at 09:35,
  so the staleness gate should **not** fire and **no alert is due**. Steps 4–6 will be reached
  with **full authority and no intents to act on**. **Zero `alpaca.py move` re-validation calls
  are due** — re-validation has a subject only when an intent exists. **The gate has never fired
  in this account's history; its alert path is untested code, and fifteen quiet opens are not
  evidence that it works.**
- **⚠ Two-price trap — SOLVED, and the answer is a quote midpoint, not an offset.** The broker
  mark is a **live bid/ask midpoint** that keeps moving after the bell; that is why the gap
  (6.5c, 59.85c, 4c, 17c on successive days) never had a stable size and never will. **Do not
  re-derive this and do not re-open it as a mystery.** Use `bars --adjustment all` for any
  official close and a fresh `quote` for execution. **Never a `positions` field for either.**
  Cosmetic on core; **load-bearing the moment a satellite position exists**, because a
  `highest_close` read from a `positions` field would record an after-hours midpoint and
  silently move the §5.4 stop.
- **⚠ `selftest.py` does not probe `clock` or market data.** A green pre-flight certifies nothing
  about the data plane — it passed all five checks on 09-11 while `clock` was 500 and
  `quote`/`bars` were 504. **Probe by hand before relying on a price. Whether the selftest should
  change is a human's call, not a run's.**

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

A plan with no intents is a complete plan, not a failed run. §4 is explicit that the correct
output of most research runs is no trade, and padding this file to look busy is the failure
mode it exists to prevent. Say plainly what was considered and why it was rejected, and leave
the intent sections empty.
