# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-10 08:23 ET 1-premarket-research (selftest PASSED all five checks; clock is_open false with next_open 2026-09-10 09:30 ET - PRE-MARKET on a normal trading day, NOT a holiday; equity 99266.82, core VOO unrealized -733.17 / -1.047% against the 706.74 fill, sixth straight negative mark and first past -1%, NO ACTION - §5 exempts core; ledger reconciled - zero satellite blocks vs zero satellite Alpaca positions, they AGREE; high-water marks ABSENT not stale, no backfill owed, §5.4 still NOT ARMED; §5 had no subject, no invalidation query due; SIX theses written T-2026-09-10-01..06, ALL SIX REJECTED, zero accepted, NO BUY INTENT; plan_today.md written and dated 2026-09-10 - do-nothing plan, no BUY no SELL no REBALANCE; week anchor 2026-09-07 matches today's ISO Monday, no cap reset due; breaker INACTIVE, weekly count 0 of 3; core 69.78% in band, rebalance_delta +219.95 = 0.22% of equity, NOT due at the open)
week_of: 2026-09-07
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.78
satellite_pct: 0.0
cash_pct: 30.22
open_thesis_ids: none
```

---

## Field meanings

**`week_of`** — the Monday of the current ISO week. Every run compares today's week anchor
to this value; if they differ, reset `new_positions_this_week` to 0 and update this field.
The reset deliberately does not depend on the Friday review having run, so a skipped Friday
cannot leave the §6 weekly cap stuck at its limit.

**`new_positions_this_week`** — satellite positions *opened* this week. §6 caps it at 3.
Exits do not count.

**`consecutive_closed_losses`** — incremented when a satellite position is closed at a loss,
reset to 0 when one closes at a gain. At 3, set `circuit_breaker: ACTIVE` and record
`halt_triggered_at` as today.

**`circuit_breaker`** — `ACTIVE` or `INACTIVE`. While ACTIVE: no new positions of any kind
(§7). Existing positions are still managed per §5, research and journaling continue, and the
halt is flagged prominently in the ClickUp summary (§6). Core rebalancing is still permitted —
§6 halts *new positions*, and restoring the core sleeve to its 70% target is neither a new
position nor a satellite trade.

**`halt_triggered_at`** — date the breaker tripped. Compared against `HALT_CLEARED_AT` in
`control.md`; the halt lifts only when the clearance date is strictly later. If the breaker
is ACTIVE and this field is `none`, the halt stays active — an unknown trigger date is not
grounds to start trading.

**`core_established`** — `false` until the VOO core sleeve exists. The market-open routine
bootstraps it on the first trading day and this flips to `true`, which disables the
bootstrap path permanently.

**`core_pct` / `satellite_pct` / `cash_pct`** — sleeve allocation as of the last run, in
percent of total account value. §2 rebalance band is core 65–75%.

**`open_thesis_ids`** — comma-separated thesis IDs for currently open satellite positions.
Cross-check against `positions.md`; if they disagree, `positions.md` and the live Alpaca
position list win, and the discrepancy goes in the journal.

---

## Carry forward

Anything the next run must not lose. Cleared once acted on.

- **⚠ THE 09-10 PRE-MARKET RUN PRODUCED SIX THESES AND ZERO BUYS. NOTHING BLOCKED IT.** Breaker
  INACTIVE, weekly cap **0 of 3**, satellite sleeve **empty with 30.22% cash**, `control.md` notes
  empty. **New positions were fully permitted and the research did not produce an eligible
  candidate** — that is §4 working, not a gate firing. Selftest passed all five checks at 08:23 ET
  (`trading_enabled: true`, LIVE paper, equity **$99,266.82**). `clock` 08:23:47 ET: `is_open:
  false`, `next_open: 2026-09-10 09:30 ET` — **pre-market on a normal trading day, not a holiday;
  `next_open` being *today* is the test.** Sleeves: core **69.78%**, satellite **0.0% (count 0)**,
  cash 30.22%, `rebalance_delta: +219.95` (**0.22% of equity — no rebalance due at the open**).
  Ledger reconciled: **zero satellite blocks vs zero satellite Alpaca positions, they agree.**
  Week anchor `2026-09-07` matches today's ISO Monday, **no cap reset due.** `plan_today.md`
  written and dated **2026-09-10** — do-nothing plan, no BUY / SELL / REBALANCE.

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON EIGHT TIMES NOW, AND DUE AGAIN NEXT RUN.**
  `positions.md` ran to **604 lines / 42KB** before the 09-07 collapse, was cut to 162, and has
  since been held to a **single current reconciliation block** — this run folded the 09-09 close
  block into today's pre-market block, exactly as the seven runs before it did. Every load-bearing
  fact is preserved (the 09-03 VOO fill, the 706.74 measurement baseline, the
  satellite-to-satellite comparison rule, §5.4 unarmed, §5 untested); **nothing live was
  discarded.** The pull to append is structural — a run is rewarded for showing it checked
  something, and a deleted note looks like a check that never happened. **A future run will feel
  it too.**

- **⚠ THE FUNNEL FAILED FOUR DIFFERENT WAYS TODAY, AND ONE OF THEM WAS NEW: ARITHMETIC.** Four
  genuinely new, dated, sourced commercial events came through, all four new to their companies'
  own disclosure (standing rule (iii) run on each): **DoD→Lockheed $826.0M JASSM/LRASM + $257.3M
  MK 48 (09-09)**; **Monolithic Power↔GlobalFoundries, MPWR process at GF's 300mm Singapore fab,
  volume early 2027 (09-09)**; **Ignitis↔EQT subsidiary LNG, 10 cargoes ~1 TWh each 2027–2036
  (09-10)**; **Centrus↔Radiant HALEU, deliveries before end of decade (09-09)**. Each
  second-order branch died differently: **LMT** — no published source names *any* US-listed
  supplier on either program, only Lockheed's own facility work-share (Liverpool 57 / Clearwater
  37 / Braintree 6); **GFS** — named party, `priced_in: true` at +4.53%, and early-2027 timing;
  **EQT** — **part 2 on a number I could actually compute**; **LEU** — §3 floor breach at
  ~$3.4–3.8B. **T-2026-09-10-03 (EQT) is the first part-2 rejection in this log that died on
  arithmetic rather than on an absent disclosure:** ~1 TWh/yr ≈ **3.4 Bcf** against **634 Bcfe of
  Q2-2026 sales volume alone** — roughly **0.14% of annual volume** against §4.2's **10%** floor.
  Every prior part-2 rejection failed because the company does not break the segment out. **This
  one failed because the segment is real, disclosed, and the event is trivial next to it.**
  **Standing lesson: when a source describes a contract in units the company does not report in —
  TWh against Bcfe, miles of fiber against segment dollars — convert first and write second.**

- **⚠ DO NOT REACH FOR THESE — today's rejects and the specific traps in each.** **LMT** returns
  **−3.61%, `priced_in: false`, "passes"** on the day it booked $1.08B — it passes because a 3.61%
  **decline** fits inside a 4% band, and **Lockheed is Company A**. **Do not fill in the
  JASSM/LRASM supplier chain from memory** — SRM and energetics names will suggest themselves and
  naming one is **rule (v)** compounded by **rule (iv)**; the related **Nitradyn $581M IMX-104
  award** was checked and dropped (private, no listed energetics supplier named). **GFS** is a
  named party and **`priced_in: true` at +4.53% — 0.53 points past the threshold is a failure, not
  a rounding error.** **MPWR** is the announcing party and *incurs* the cost. **EQT is the
  tempting one**: mechanism single-clause, correlation clear, §3 clear at ~$34.5B,
  `priced_in: false` at −1.72% — **a clean filter sheet is not a thesis; it died on size.**
  **LEU (~$3.4–3.8B), TBBK (~$2.0–2.8B), CASH (~$1.7B), GDOT (~$0.76B), CCB (~$0.7–0.8B)** all
  breach the §3 $10B floor — **a floor, not a preference.** **None of these becomes a buy at a
  different price.**

- **⚠ A CORRECTLY IDENTIFIED SECOND-ORDER EFFECT THAT IS UNTRADEABLE IS A DIFFERENT OUTCOME FROM
  FINDING NOTHING, AND THE LOG NOW DISTINGUISHES THEM.** T-2026-09-10-05: **Chime's $590M
  acquisition of Stride Bank (09-09)** removes sponsor-bank economics from the BaaS group. The
  chain is short, needs no "and" clause, and is **visible in the tape** — **TBBK set a 52-week low
  on 09-10**, with a wire item framing it as exactly that. It is untradeable twice over: **every
  affected name is below the §3 floor**, and **the sign is negative on a book with no short.**
  Noted and not pursued: **CCB fell ~43% on 09-04/09-07 on "banking services issues" and is under
  securities-fraud investigation** — outside the window, below the floor, and **a stock that has
  fallen 43% is not a catalyst.**

- **⚠ CARRY-FORWARD CLOSED: THE QCOM / VERIZON–CORNING EVENTS OF 09-08 ARE DISPOSED OF.** QCOM,
  AMZN, GLW, VZ were the **named counterparties**; **MTZ** died on parts 1/2/3 and **FN** on an
  unsourced mechanism at a deceptively clean +0.83%. **COHR +8.64%, LITE +7.01%, CRDO −25.74%,
  MRVL +6.56%, DY +4.11%, PWR +5.32%** were all `priced_in: true`. **None re-enters the funnel
  without a fresh event of its own**, and none becomes a buy at a different price. The
  **BSX/MDT/ABT** item closed on 09-09 and **must not be reopened** — MDT and ABT died on part 2
  (no SCS/neuromodulation revenue disclosed at a tradeable grain), and a new price window does not
  create a disclosure that does not exist.

- **⚠ THE MACRO TAPE IS LOUD AND IS NOT ACTIONABLE UNDER THIS STRATEGY.** **August PPI released
  09-10 morning, August CPI 09-11**; 10-year **4.85%**, highest since Nov 2023; 30-year auction
  09-10; Treasury buyback of up to **$6B** of 10–20yr paper; mortgage rates **6.85%**, highest in
  over a year; MBA refinance index lowest since May 2025; **September hike odds ~59%** into the
  **09-15/16 FOMC**. Brent still **above $100** on US–Iran escalation and Hormuz risk, with the
  only reporting attaches — **PBR, EC, YPF, VIST** — all **foreign issuers (§3)** and
  **first-order** commodity exposure regardless. **No segment, no dollar path, no §4 mechanism in
  either direction.** The rates read-across to housing runs the **wrong way** for a long book,
  which is not an invitation to reinterpret it as a short — **this strategy has no short.**

- **⚠ ORACLE AND ADOBE REPORT AFTER THE 09-10 CLOSE; MACY'S REPORTED 09-10 MORNING.** They land
  **after** the 09-10 pre-market survey closed and are **not** in that funnel — a sequencing fact,
  not an oversight. **Oracle carries the AI-capex read-across surface.** They are the **09-11
  pre-market run's** material, and that run should screen them rather than assume a later run
  already did.

- **⚠ A RE-AGGREGATION OF OLD NEWS ARRIVES LOOKING EXACTLY LIKE A NEW EVENT, AND `--recency day`
  CANNOT CATCH IT.** The 09-06/09-08 headline **"Anthropic signs $517B / 14.8 GW of compute
  contracts"** is *The Information*'s **summation of eleven months of previously announced deals**
  (Amazon and Google/Broadcom from **May**; the $30B Azure commitment, the SpaceX Colossus lease
  and the $35B Lambda commitment all reported **09-02**). The *articles* are genuinely new, so the
  recency filter passes them. **This is standing rule (iii) in the one form the tooling cannot
  flag. Expect it again; the AI-capex tape generates aggregation pieces constantly.** All four of
  09-10's events were checked against exactly this test; **three passed cleanly and one failed it —
  Alcoa's $2.6B notes pricing (09-09) is financing for a *previously announced* South32
  acquisition, and was dropped before any ticker work.** **The test works, run it every time.**

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, the Bloom/Oracle item,
  **Alcoa/South32 on 09-09**). (iv) *A recurring ticker is a warning, not corroboration* (LHX).
  (v) *A market-structure fact is not a supplier relationship* (CLF — "sole producer," "dominant
  share," "the only company that makes X" are facts about an **industry**, not a **transaction**).
  **Rule (v) fired three times on 09-10** — the unnamed JASSM/LRASM and MK 48 supplier chain, the
  unnamed equipment supplier into GF's Singapore fab, and Bayer's undisclosed **"newgold® network"
  value-chain partners. That last one is the purest instance yet: the source left a blank, and
  filling in a blank the source left blank is not research.** **Recognise the phrase; do not
  re-derive it.**

- **⚠ FOUR ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) The §4 priced-in filter
  reads a **drawdown** as priced-in — T-2026-09-03-01 (LITE) produced a strong part 1 and was
  rejected because `move --sessions 5` returned **−7.35%**. **There is no price at which that
  rejection flips**, and no run has reinterpreted the filter or should. **09-10 added evidence, not
  a fifth item: LMT returned −3.61%, `priced_in: false`, "passes" — on the day it booked $1.08B of
  awards. Another 0.4% of drawdown and the filter would have rejected a stock for falling.** Same
  shape as LITE, caught 0.4% from firing. (2) The same filter reads an **event-day pop absorbed by
  a prior drawdown** as "passes" — the QCOM item (09-09, +2.70% net after a +8.7% intraday event
  move). Same root cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or
  `alpaca.py move`. No run may reinterpret the filter.** (3) The satellite sleeve is **structurally
  undeployed** — **twenty-nine theses, zero positions**; a 70/30 cash book cannot beat the S&P over
  a rolling 12 months (§1) in a rising market. §2 permits the cash and §4 says most runs end in no
  trade — **both rules were followed. The agent must NOT respond by lowering the §4 bar.** (4) The
  core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the prior
  close), **not tracking error and never skill** — measure from the **706.74 fill**. Prior context
  in ClickUp `86bbv75bz`.

- **⚠ REJECT SCOREBOARD (opened 09-04, a tally not evidence — a few sessions is noise and ten names
  is not a sample; a future review must not quote it as a result).** 6 of 10 rejects beat VOO, mean
  excess −0.16%. **The split is the finding:** the 8 rejected on the four-part thesis or §3 average
  **−0.97%**; the 2 rejected by the §4 priced-in filter — **MU +5.49%, LITE +0.62%** — average
  **+3.06%** and are **the same two that passed the thesis. MU and LITE must never be merged into
  one finding:** MU failed on a real +5.27% run-up (the rule working as designed and costing money —
  change nothing), LITE on a drawdown (the open question). **Six of ten rejects running without us
  is the HEALTHY reading.** **Do not tighten §4 in response, and do not loosen it.** *(Not updated
  this run — the 09-09 rejects have one session of elapsed window and today's six have none.
  **Tomorrow's weekly review must not quote this scoreboard as a result.**)*

- **⚠ THE REASSURING FRAMING — EXPECT TO GENERATE IT AND EXPECT TO DELETE IT.** The sentence is
  *"the book fell less than the index"* — e.g. 09-09's **book −0.303% vs VOO −0.477%**. It is
  **not a result**: it is **~70% exposure capturing ~70% of a down move**, and it runs identically
  in reverse on the first green day. Appeared 09-01, 09-02, 09-04, inside the weekly review, in the
  09-08 close run's first draft, and a **sixth** time on 09-09 — **not a slip but the sentence this
  agent produces by default whenever partial exposure and a down day coincide.** Caught and deleted
  every time; keep that record intact. **A seventh invitation is now standing: the core is through
  −1% for the first time (−$733.17 / −1.047% against the 706.74 fill, six straight negative marks),
  and a red core with an empty satellite sleeve is the exact setup that produces both this sentence
  and the urge to lower the §4 bar to put *something* on.** Neither is a reason to act; **§5 exempts
  core from all four sell rules and a round number is not a threshold.** Related: anchor the week to
  **08-31, the first operating day**.

- **Do not reach for MU or LHX.** Neither entered the 09-10 funnel, no source named them, and their
  filters were not re-run — **absence of evidence, not resolve.** Seventh consecutive day. **LHX is
  now the specifically invited name**: the LMT award (T-2026-09-10-01) has an unfilled supplier
  chain, and LHX is what memory offers to fill it. **That is rule (iv) and rule (v) at once — the
  invitation is the reason to be more careful, not less.** LITE died on its own fresh filter on
  09-09 at +7.01%, `priced_in: true` — a new rejection, **not** a revival and **not** a resolution
  of the open human question above. If any of them resurfaces **from a source**, **re-run its
  filters and re-test the timing window from that day's date**; that is legitimate and different
  from inheriting a conclusion.

- **⚠ ALL FOUR §5 SELL RULES ARE UNTESTED CODE PATHS, NOT PROVEN ONES.** Zero positions have ever
  closed, so §5.1–§5.4 have never been evaluated against a real subject. **Eight days of "no exits"
  recorded the absence of a subject, not eight clean bills of health.** §5.4 is **NOT ARMED, not
  disabled** — it arms the day the first *satellite* position opens.

- **⚠ THE HIGH-WATER MARKS ARE ABSENT, NOT STALE — A THIRD STATE.** No satellite position exists,
  so `positions.md` has **no `highest_close` and no `(as of ...)` date**. The midday backfill
  trigger keys on a **stale date**, and an absent field cannot be stale — **do NOT backfill from
  `bars`.** **Do not stamp a mark on core VOO to give the step a subject:** that would fabricate a
  §5.4 trailing stop on a position that must never carry one.

- **⚠ THE TWO-PRICE TRAP — A SEVENTH SHAPE.** Always pull `bars --adjustment all` for a close and a
  fresh `quote` for execution; **never a `positions` field for either.** At 09-10 pre-market: broker
  `current_price` **699.3377** and `lastday_price` **700.87** against 09-09's official close
  **700.805** — **the broker's "last day" figure is 6.5 cents above the official close it purports
  to be.** Prior shapes: 09-09's three numbers for one day (700.805 / 701.02 / 704.07); 09-04
  official 707.86 *above* broker mark 707.59; the holiday's third number 708.01; and 09-08, where a
  $0.15/share stale baseline moved reported day P&L by $38. **The gaps are small, which is exactly
  when the shortcut gets taken.** The day a satellite position exists, that shortcut writes a wrong
  high-water mark that does not error, does not look stale, and silently moves the §5.4 stop to a
  level nobody chose.

- **NO TRADES, NO FILLS, NOTHING IN LIMBO.** The account's entire order history is the one 09-03
  core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO 99.046311231 @ $706.74, notional
  $70,000.00**, `status: filled`, terminal. Loss streak **0 — nothing has ever closed**, so the §6
  streak cannot move and no circuit-breaker alert is due.

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; `archive/` holds only its README. Next rollover is the first
  Friday review of **October 2026**.

- **ClickUp tasks, for reference:** 09-09 daily summary `86bbxtn1a`; 09-08 daily summary
  `86bbwuc17`; Friday's daily summary `86bbv6npm` and weekly review `86bbv75bz`. **This
  pre-market run created no ClickUp task and none was due** — the daily summary is the close run's
  job. **No alert task exists** — no alert condition (breaker, push failure, selftest abort, guard
  violation) has arisen, and `alerts.md` remains empty.

- **⚠ TOMORROW, FRIDAY 09-11, IS A WEEKLY-REVIEW DAY AND AUGUST CPI LANDS THE SAME MORNING.** The
  review **must not quote the reject scoreboard as a result** (see the scoreboard note above) —
  ten names over a few sessions is noise, not a sample. CPI is macro with no segment and no dollar
  path — **not a §4 mechanism in either direction.** The review will also be the first to weigh a
  **full week of six-a-day rejection counts against zero positions**; the honest framing is that
  §4 was applied as written, **not that the bar needs moving.**
