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
plan_date: 2026-09-14
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-14 at 09:30 ET (`alpaca.py clock` at 08:22:50 ET: `is_open:
false`, `next_open: 2026-09-14T09:30:00-04:00`, `next_close: 2026-09-14T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.

**One pre-market run today, at 08:22 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,134.33**).

**Tape context:** VOO's broker mark is **698.04** (`lastday_price` **702.56**, `change_today`
**−0.64%**). Neither number is an execution reference — **pull a fresh quote at 09:35.** The
core position shows `unrealized_pl` **−$861.70 (−1.231%)** against the 706.74 fill, its widest
of the run so far. §5 exempts core from all four sell rules — **there is no action attached to
it at any number, in either direction, and a −1.2% mark is not a signal to do something.**

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band, there are no satellite
positions to manage, and three candidates were researched to a full thesis entry and all three
were rejected.

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker INACTIVE, weekly cap
at **0 of 3** (fresh week), satellite sleeve **empty with 30.26% cash**, no restricting note in
`control.md`. **Nothing was blocked. The research did not produce an eligible candidate.**

Three candidates reached ticker stage with a full `research_log.md` entry:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-14-01 | BWXT | part 1 (rule v), part 3 | HII's **$336M CVN 82 long-lead award** names **no subcontractor** — a dedicated screen returned *"no public source names a subcontractor or supplier receiving a portion of this specific award."* "BWXT is the sole naval reactor builder" is an **industry fact, not a transaction**. Undefinitized advance procurement for a next-decade carrier also fails the two-quarter horizon. |
| T-2026-09-14-02 | (packaged food) | part 1 | Kroger's **ID-sales guidance cut (1.0–2.0% → 0.2–0.8%)** and a supplier's soft volumes are both downstream of the **same grocery consumer**. Kroger guiding lower causes no supplier to receive less. **Shared cause, not a mechanism** — the Macy's shape from 09-11. |
| T-2026-09-14-03 | CART | part 2 | Kroger named **Instacart** as a partner on the call — a real named counterparty — but **no dollar figure exists anywhere**: not in the release, the 8-K, the IR summary or the call coverage. Neither magnitude nor segment share can be written without inventing both. |

**The three earnings the Friday review assigned to this run were screened directly, not
assumed.** **Kroger** produced the two theses above. **Rent the Runway** (FQ2 revenue $97.7M) is
**two orders of magnitude below the §3 $10B floor** as a candidate and named no quantified
counterparty as Company A. **VinFast** had **no fresh earnings in the window** — the recent items
are guidance/estimates and operational updates, and it is a foreign issuer besides. **That
sequencing note is the only reason this screen happened; keep writing them.**

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ THE FUNNEL WAS THIN BECAUSE IT WAS A WEEKEND, AND THAT IS STRUCTURAL — NOT A QUIET NEWS
  DAY TO COMPENSATE FOR.** Both broad scans came back explicitly empty on company events: the
  first reported *"the available evidence is thin for company-specific corporate events"*; the
  weekend-filings sweep for 09-12 and 09-13 returned *"nothing qualifies based on the sources
  gathered."* **§4 needs a dated transaction between two named parties, and US companies do not
  file 8-Ks on Saturday and Sunday.** A Monday pre-market run screens **one business day plus two
  empty ones**, and this recurs every Monday. **Expect it; do not lower the bar at the bell to
  make up for it.**
- **⚠ Do not reach for BWXT at the open, and expect the name to feel obvious.** A 30-year-old
  sole-source position in naval nuclear propulsion is exactly the kind of fact that reads like a
  supplier relationship. **The source announced the deal and left the counterparty blank.
  Filling in a blank the source left blank is not research** — standing rule (v), **fifth
  instance this month.** It also returned **`priced_in: true` at −6.30%**, but note the ordering:
  **parts 1 and 3 had already killed it before the filter ran.**
- **⚠ CART is the near-miss of the run and the most interesting rejection to carry.** After eleven
  sessions of *"the source withheld the counterparty,"* **a source finally named one** — and the
  thesis still died one test later for want of a number. **That is a different failure from rule
  (v) and must not be filed with it.** §4 needs a named counterparty **and** a quantified
  exposure; this run produced a clean example of each arriving without the other. **A partnership
  with no size disclosed is not a dollar path.** CART also returned **`priced_in: true` at
  −5.79%** — again *after* part 2 had already killed it.
- **⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED TWICE TODAY (CART −5.79%, BWXT −6.30%) — ITS DENSEST
  SHOWING, AND IT COST NOTHING.** Five instances now (LITE −7.35%, LMT −3.61% near-miss, LHX
  −4.47%, plus today's two). **Both of today's candidates were already dead on the four-part
  thesis when the filter reached them.** The expensive instances are the ones that arrive
  **alive** — LITE passed the four-part thesis, was killed by a drawdown, and is **+10.58% vs
  VOO** since. **Do not let a double-fire inflate the estimated cost of this defect, and do not
  reinterpret the filter: that is a human editing §4 or `alpaca.py move`.**
- **⚠ Do not read the Kroger cut as a short thesis or as a macro signal.** §4 is a long-only
  second-order rule; a guidance cut at Company A with no named, sized counterparty is **not a
  trade in either direction.**
- **⚠ THE LOUDEST STORY OF THE WEEK IS NOT A CANDIDATE, IN EITHER DIRECTION.** August CPI landed
  09-11 (headline **+0.4% m/m / +3.4% y/y**, core **+0.3% m/m / +2.4% y/y**) and the **FOMC
  decision lands 09-16/17, inside this week.** No Company A, no segment, no dollar path — it is
  the whole tape moving, which is what §4 exists to refuse. **If it moves prices hard at the
  open, that is a price move, not a thesis.** *(One source priced ~87% odds of a 25bp **increase**,
  contradicting every other framing in the same result set. Unresolved and not worth resolving —
  untradeable under §4 either way.)*
- **⚠ Four headline claims from 09-11 still have no primary source and must not be traded on:**
  "Nvidia invests $30B in Intel," "Nvidia acquires Hugging Face," "Google's first nuclear deal /
  $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity by 2032." **None
  appeared in any filing over the weekend.** If one is real it will arrive with a document
  attached, and that is the day it enters the funnel.
- **Do not reopen the disposed rejects.** **ORCL** (Company A twice over, `priced_in: true` at
  +5.06%, and the screen for a named Oracle customer returned "no verified companies found");
  **LHX** (dead on arithmetic: $127M Palantir + $65M Anduril = the entire $192M award); **AVAV**
  (the awarded party, and its +1.20% is a round-tripped +12.9% spike); **SLI** (~$1B against the
  $10B floor); **M** (a statute, not a transaction); and **LMT, GFS, EQT, LEU, TBBK, CASH, GDOT,
  CCB, QCOM, AMZN, GLW, VZ, MTZ, FN, COHR, LITE, CRDO, MRVL, DY, PWR, BSX, MDT, ABT.** **None
  becomes a buy at a different price.**
- **Do not reach for MU.** It has not entered the funnel for **twelve consecutive days**, no
  source has named it, and its filters were **not** re-run — **absence of evidence, not resolve.**
  If it resurfaces *from a source*, re-run its filters and re-test the timing window from that
  day's date.
- **A quiet day is not a reason to lower the bar at the bell.** §4: the correct output of most
  research runs is no trade. **Thirty-three theses, zero positions.** That number is the strongest
  argument available for loosening the rule and it is **not** the agent's argument to make — §2
  permits the cash, §4 says most runs end in no trade, and **both rules were followed.**

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — the ledger reads
*(none)* and the broker returns exactly one row, **VOO, which is core and exempt from §5
entirely**. Compare satellite blocks to satellite positions, not raw ledger to raw broker.
§5.1–5.4 have nothing to evaluate: no invalidation condition to test, no timing window to
expire, no entry price or high-water mark to measure a stop against. **No §5.1 Perplexity
invalidation query was issued and none was due — there is no position to check news against.**

### REBALANCE — none

- current_core_pct: **69.74%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:22 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +258.52`
- action: **none.** The +$258.52 delta is **0.26% of equity** — VOO's overnight mark moving, not
  drift. §2 rebalances at the **band edge** (65/75), not to the exact target. 69.74% is not a
  rebalance, and neither were 69.72%, 69.78%, 69.83%, 69.84%, 69.88%, 69.92%, 69.96% or 69.98%.
  **Nine consecutive runs inside a 0.26-point range; the core is not drifting.**
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: the ISO
  Monday of 2026-09-14 is **2026-09-14**, which matches `week_of` — **no reset was due, because
  the Friday review already performed it.** That is the housekeeping rule working as designed,
  not a skipped step. Next boundary is Monday 2026-09-21.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:22 ET.
- **⚠ Two-price trap — SOLVED, and the answer is a quote midpoint, not an offset.** The broker
  mark is a **live bid/ask midpoint** that keeps moving after the bell; that is why the gap
  (6.5c, 59.85c, 4c on successive days) never had a stable size and never will. **Do not
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

An empty intent list is the expected output most days. §4: *"The correct output of most
research runs is no trade. A run that finds nothing worth buying is a successful run."*
When there is nothing to do, write that plainly here with the reasoning — do not pad the
list to look productive. The rejected candidates still go in `research_log.md`, which is
where the value of a quiet day actually lives.
