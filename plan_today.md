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
plan_date: 2026-09-11
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-11 at 09:30 ET (`alpaca.py clock` at 08:19:54 ET: `is_open:
false`, `next_open: 2026-09-11T09:30:00-04:00`, `next_close: 2026-09-11T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.

**One pre-market run today, at 08:20 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,456.23**).

**Tape context:** VOO's broker mark is **701.25** (`lastday_price` **696.65**, `change_today`
**+0.66%**). Neither number is an execution reference — **pull a fresh quote at 09:35.** The
core position shows `unrealized_pl` **−$543.76 (−0.777%)** against the 706.74 fill. That is
still negative, but note the direction: **the mark is up $455.61 on the session's indication
after nine straight negative closes.** §5 exempts core from all four sell rules — **there is
no action attached to it at any number, in either direction.**

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
| T-2026-09-11-01 | (no ticker) — Oracle read-across | no Company B, rule (iii), part 3 | **No US-listed company discloses Oracle as a quantified customer** — a dedicated screen returned "no verified companies found." The **$90–95B FY27 capex guidance was maintained, not raised**. Oracle's own call says the new bookings are prepay/BYOH and **do not touch capex or revenue until FY2028+**. |
| T-2026-09-11-02 | LHX | part 2 (arithmetic), part 3 | The **$192M TITAN award is fully allocated: $127M Palantir + $65M Anduril (private) = $192M.** LHX is named as a program participant with **$0 disclosed from this award**. 18-month delivery. |
| T-2026-09-11-03 | (no ticker) — LOCUST X3 supply chain | no Company B | **No published source names any supplier** of the laser source, beam director or power subsystem, and no dollar is broken out below AVAV's own $464.8M. |
| T-2026-09-11-04 | SLI | §3 universe, part 3 | **SLI is ~$1B against a $10B floor**; LG Energy Solution is Korea-listed. The 10-year offtake runs **from the start of commercial production**, which has not begun. |
| T-2026-09-11-05 | M | part 1 | The tariff-refund read-across runs through a **statute, not a transaction** — Macy's receiving $116M causes no other company to receive anything. **Shared exposure to a common cause is a correlation, not a mechanism.** |

**The headline event of the week was screened directly, as yesterday's carry-forward required.**
Oracle's FQ1 2027 (09-10 after the close) is the largest second-order surface this log has ever
processed — **RPO $664B (+$209B YoY), OCI +121% to $7.4B, 850 MW and >300,000 GPUs delivered in
one quarter, FY27 capex $90–95B** — and it produced **no Company B at all**, for three
independent reasons stated in the table. **That sequencing note yesterday is the only reason this
screen happened; keep writing them.**

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ Do not reach for an Oracle supplier at the bell, and expect the names to arrive
  unprompted.** The screen asking which US-listed companies have *themselves* named Oracle as a
  customer with a quantified revenue share returned **"No verified companies found."** Oracle's
  release, its 8-K and the retrievable call text name **no hardware supplier, no colocation
  partner, no data-center developer** — while discussing megawatts, GPUs and $90B+ of capex at
  length. **The plausible name you can think of is standing rule (v), and it will feel like a
  technicality rather than a rule. It is not.** **ORCL itself is `priced_in: true` at +5.06% and
  is Company A twice over.**
- **⚠ Do not reach for LHX — and read *why* before deciding it is settled.** A source named it
  today, so its filters were legitimately re-run rather than inherited. **It died on arithmetic:
  $127M + $65M = the entire $192M award, leaving nothing for any other participant.** The
  rejection does not flip at a different price. **Anduril's $65M is the real second-order money
  here and Anduril is private** — the third time this month the identifiable beneficiary was not
  listed.
- **⚠ LHX also returned `priced_in: true` at −4.47%, i.e. the filter's stated reason to skip it is
  that it fell.** That is open human question #1 **firing for real**, after LITE (−7.35%) and LMT
  (−3.61%, 0.4% short). **It cost nothing today — part 2 had already killed the thesis. No run
  reinterprets the filter.**
- **⚠ Do not fill in the LOCUST X3 / E-HEL supplier chain from memory.** A dedicated screen
  returned **no named supplier at all**. A 30 kW directed-energy weapon has a short, famous
  vendor list and every name on it will suggest itself; naming one is **standing rule (v)**,
  fourth instance this month. **AVAV passes the priced-in check at +1.20% and is Company A** — the
  awarded party — so §4's headline-name rule rejects it regardless of the number.
- **⚠ Distrust the +1.20% on AVAV as a description of what happened.** `bars --adjustment all`:
  **09-10 high 159.23, close 147.06** — a **+12.9% intraday event move that round-tripped**, read
  by the five-session filter as a quiet +1.20%. Same shape as the 09-09 QCOM case, except the
  absorbing happened **inside one session**. **Evidence for the human's open question #2, not a
  new item and not a reason to act.**
- **⚠ Four headline claims circulating this morning have no primary source and must not be traded
  on:** "Nvidia invests $30B in Intel," "Nvidia acquires Hugging Face," "Google's first nuclear
  deal / $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity by 2032."
  **All four trace to a single secondary aggregator briefing; a verification query found no
  filing, no press release and no major-press coverage for any of them.** If one is real it will
  arrive with a document attached, and that is the day it enters the funnel.
- **The macro tape is loud and none of it is actionable.** **August PPI +5.4% YoY (09-10) vs 5.3%
  expected; core PPI +4.6%; August CPI this morning; September hike odds up to ~72% from ~61%**
  into the 09-15/16 FOMC; jobless claims 206k. **No segment, no dollar path, no §4 mechanism in
  either direction.** Fourth consecutive day with the same disposition. **A CPI print this morning
  is not a reason to act at 09:35** — and if it moves the tape hard, that is a price move, not a
  thesis.
- **Do not reach for MU.** It did not enter today's funnel, no source named it, and its filters
  were **not** re-run — **absence of evidence, not resolve.** Tenth consecutive day.
- **Do not reopen yesterday's rejects: LMT, GFS, EQT, LEU, TBBK/CASH/GDOT/CCB.** All still
  rejected, none becomes a buy at a different price. **EQT remains the tempting one — a clean
  filter sheet that died on size (~0.14% of volume against a 10% floor).**
- **Do not reopen QCOM, AMZN, GLW, VZ, MTZ, FN, COHR, LITE, CRDO, MRVL, DY, PWR, BSX, MDT or
  ABT.** Disposed of on 09-08/09-09 and **not revived by the Corning–Verizon item resurfacing in
  a 09-10 article** — that deal was announced **09-08** and is outside the window.
- **A quiet day is not a reason to lower the bar at the bell.** §4: the correct output of most
  research runs is no trade. **Thirty-one theses, zero positions — and today the single largest
  event available was screened properly and still produced nothing.** That is the rule working.

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — the ledger reads
*(none)* and the broker returns exactly one row, **VOO, which is core and exempt from §5
entirely**. Compare satellite blocks to satellite positions, not raw ledger to raw broker.
§5.1–5.4 have nothing to evaluate: no invalidation condition to test, no timing window to
expire, no entry price or high-water mark to measure a stop against. **No §5.1 Perplexity
invalidation query was issued and none was due — there is no position to check news against.**

### REBALANCE — none

- current_core_pct: **69.84%** (target 70%, §2 band 65–75% — **inside the band**)
- `alpaca.py sleeves` 08:20 ET: `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +163.14`
- action: **none.** The +$163.14 delta is **0.16% of equity** — VOO's overnight mark moving, not
  drift. §2 rebalances at the **band edge** (65/75), not to the exact target. 69.84% is not a
  rebalance, and neither were 69.72%, 69.78%, 69.83%, 69.92%, 69.96% or 69.98%.
- **⚠ `core_established: true`. The bootstrap path is closed permanently — do not re-run it.**

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first *satellite* position opens. The core VOO holding does **not** arm it: core is exempt
  from §5 entirely and is deliberately absent from `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover checked this run: the ISO
  Monday of 2026-09-11 (Friday) is **2026-09-07**, which matches `week_of` — **no reset was
  due**. Next boundary is Monday 2026-09-14.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:19 ET.
- **⚠ Two-price trap.** Use `bars --adjustment all` for any official close and a fresh `quote`
  for execution. Never a `positions` field for either. Today's numbers already differ: broker
  mark **701.25** against `lastday_price` **696.65**, versus yesterday's official close
  **696.69** — a **4-cent** gap this morning against **59.85 cents** at last night's close. **The
  gap is not stable from day to day, which is the whole reason the shortcut is unsafe.**
- **⚠ Today is Friday 09-11 — a weekly-review day.** The 16:15 review **must not quote the reject
  scoreboard as a result**; ten names over a few sessions is noise, not a sample. It will also be
  the first review to weigh **a full week of five-and-six-a-day rejection counts against zero
  positions** — the honest framing is that §4 was applied as written, **not that the bar needs
  moving.**

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
