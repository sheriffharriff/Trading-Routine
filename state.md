# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-09 12:35 ET 3-midday-management (market OPEN; ZERO satellite positions so there was nothing to manage — no §5 rule had a subject, no high-water mark existed to repair, no invalidation query was due, no exit was taken and none was due; exits-only routine opened nothing, correctly; zero orders placed, nothing in limbo; week anchor 2026-09-07 unchanged, no cap reset due; breaker INACTIVE, weekly count 0 of 3)
week_of: 2026-09-07
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.82
satellite_pct: 0.0
cash_pct: 30.18
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

- **THE 09-09 MIDDAY RUN HAD NOTHING TO MANAGE AND CORRECTLY DID NOTHING. IT IS EXITS-ONLY AND IT
  OPENED NOTHING.** Selftest passed all five checks at 12:35 ET (`trading_enabled: true`, LIVE
  paper, equity **$99,385.90**). `clock` 12:35:19 ET: **`is_open: true`**. **Zero satellite
  positions, so every step past the read had no subject:** no `highest_close` to repair (Step 2),
  no invalidation condition to query (§5.1 — **no `perplexity.py` call was due**), no timing window
  (§5.2), no entry price (§5.3), no high-water mark (§5.4), no exit to execute (Step 4), no held
  position to re-status (Step 5). **Zero orders placed — nothing is in limbo and the account's
  order history is still the single 09-03 core fill.** Sleeves at midday: core **69.82%**,
  satellite **0.0% (count 0)**, cash 30.18%, `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: +183.04` (0.18% of equity) — **and rebalancing is not this routine's job
  anyway.** Week anchor `2026-09-07` still matches today's ISO Monday (Wednesday 09-09), so **no
  cap reset was due**: **0 of 3** used. Breaker INACTIVE. *(This replaces the market-open note —
  read and acted on, now cleared.)*

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON SIX TIMES NOW, AND DUE AGAIN NEXT RUN.**
  `positions.md` ran to **604 lines / 42KB** before the 09-07 collapse, was cut to 162, and has
  since been held to a **single current reconciliation block** — this run folded the 09-09
  market-open block into the midday block, exactly as the five runs before it did. Every
  load-bearing fact is preserved (the 09-03 VOO fill, the 706.74 measurement baseline, the
  satellite-to-satellite comparison rule, §5.4 unarmed, §5 untested); **nothing live was
  discarded.** The pull to append is structural — a run is rewarded for showing it checked
  something, and a deleted note looks like a check that never happened. **A future run will feel
  it too.**

- **⚠ NEW AND WITH THE HUMAN — THE §4 PRICED-IN FILTER HAS A SECOND DEFECT SHAPE, THE MIRROR OF
  THE LITE ONE, AND IT SURFACED ON A LIVE CANDIDATE TODAY.** QCOM (T-2026-09-09-01) rose **+3.15%
  on the 09-08 event day itself** after gapping to **180.46** and touching **183.44 (+8.7%)**,
  then fading. Because the four preceding sessions drifted down, `move --sessions 5` returns
  **+2.70%, `priced_in: false`, "passes the priced-in check."** **A filter whose purpose is to
  detect that the market already reacted cleared a stock that rose 9% on the news hours earlier:
  a prior drawdown absorbed the event pop.** Same root cause the human already holds for LITE —
  *the filter measures a price window, not a relationship to an event* — arriving from the
  opposite direction. **It cost nothing today because §4's headline-name rule rejected QCOM
  anyway. On a genuine second-order candidate it would wave through a name that had already
  moved.** **No run may reinterpret the filter**; the fix is a human editing §4 or `alpaca.py
  move`. This is now the **fourth** item in the human's queue.

- **⚠ CARRY-FORWARD CLOSED: THE BSX/MDT/ABT ITEM IS RESOLVED AND MUST NOT BE REOPENED.** The
  previous run correctly flagged that from 09-09 the five-session window would finally contain the
  09-08 Boston Scientific recall. It now does — **MDT +1.90% (`priced_in: false`, "passes"), ABT
  −4.37%, BSX −6.84%.** **This changes nothing: MDT and ABT were rejected on part 2**, because
  neither discloses neuromodulation or SCS revenue at a grain that permits a dollar path, and **a
  new price window does not create a disclosure that does not exist.** Filters were re-run for the
  record only; **no thesis was reopened, and treating the MDT "pass" as an opening would be
  looking for permission to revive a thesis that died on a different test.**

- **⚠ THE FUNNEL IS NO LONGER FAILING ON SOURCING — IT IS FAILING ON PARTS 2 AND 3.** Today
  produced **two genuinely new, well-sourced, US-listed-to-US-listed events**, both confirmed
  against company disclosure rather than an aggregator: **Qualcomm–Amazon** (press release + 8-K
  09-08; warrant 25M sh @ $161.26 against up to **$60B** of purchases; Reuters cites a **$15B
  data-center revenue target by 2029**) and **Verizon–Corning** (Corning press release 09-08;
  **80M+ miles** of fiber, **2027–2032**, "multi-billion dollar," terms undisclosed). **Standing
  rule (iii) was satisfied for the first time this month on an AI-capex item — and the second-order
  layer still died anyway**, for two specific reasons worth keeping separate: (a) on
  Qualcomm–Amazon the value that would flow to an outside supplier is **in-house** — the 1.6T
  optical work traces to **Alphawave SerDes/optical-DSP IP Qualcomm already owns**, confirmed by a
  Qualcomm executive at the Goldman Sachs conference; (b) on Verizon–Corning **Company B is the
  announcement** — Corning is the named beneficiary and moved **+11.63%**. **This is the third time
  in seven sessions a candidate passed every hard filter and died on the four-part thesis** (CAT
  09-08, MTZ and FN today). **The filters are not what is stopping this book from trading; parts 2
  and 3 are.**

- **⚠ DO NOT REACH FOR THESE — headline names and dead branches of today's two events.** **QCOM and
  AMZN**, and **GLW and VZ**, are the **named counterparties** in the two 09-08 announcements — §4:
  "you are not chasing the headline name." **QCOM will look cheap** (it faded from +8.7% intraday
  to +3.15%) and **its priced-in number reads green**; both are traps, see the defect item above.
  **FN passed the priced-in check at +0.83% with a mechanism no source supports** — a clean filter
  number on an unsourced mechanism is the shape to distrust. **COHR +8.64%, LITE +7.01%, CRDO
  −25.74%, MRVL +6.56%, DY +4.11%, PWR +5.32%** all `priced_in: true`. **MTZ passed every filter
  (+2.64%, ~$19.4B cap) and died on parts 1, 2 and 3** — no source names any contractor for
  Verizon's build, Verizon's share of MasTec revenue is undisclosed, and work begins **2027**.
  **None of these becomes a buy at a different price.**

- **⚠ THE OIL TAPE IS LOUD AND IS NOT ACTIONABLE UNDER THIS STRATEGY.** Brent near **$100** (09-08)
  on US–Iran escalation, attacks on Iranian tankers and Saudi energy sites, and Hormuz transit
  risk. The only names reporting attaches — **PBR, EC, YPF, VIST** — are **all foreign issuers
  (§3)**, and crude exposure is **first-order** regardless. The driver reverses on a headline: the
  same day's Irish Times ran *"oil nears $100 as Iran says Hormuz deal with Oman is close."* **A
  thesis whose invalidation can arrive by press conference is not a two-quarter fundamentals
  thesis.** Logged as T-2026-09-09-05 so the largest price-moving story of the window is visibly
  disposed of rather than silently skipped.

- **⚠ A RE-AGGREGATION OF OLD NEWS ARRIVES LOOKING EXACTLY LIKE A NEW EVENT, AND `--recency day`
  CANNOT CATCH IT.** The 09-06/09-08 headline **"Anthropic signs $517B / 14.8 GW of compute
  contracts"** is *The Information*'s **summation of eleven months of previously announced deals**
  (Amazon and Google/Broadcom from **May**; the $30B Azure commitment, the SpaceX Colossus lease
  and the $35B Lambda commitment all reported **09-02**). The *articles* are genuinely new, so the
  recency filter passes them. **This is standing rule (iii) in the one form the tooling cannot
  flag. Expect it again; the AI-capex tape generates aggregation pieces constantly.** Today's two
  events were checked against exactly this test and passed it — **the test works, run it every
  time.**

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, the Bloom/Oracle item).
  (iv) *A recurring ticker is a warning, not corroboration* (LHX). (v) *A market-structure fact is
  not a supplier relationship* (CLF — "sole producer," "dominant share," "the only company that
  makes X" are facts about an **industry**, not a **transaction**). **Rule (v) fired twice today** —
  Fabrinet as the dominant optical contract manufacturer, MasTec as a top telecom contractor.
  **Recognise the phrase; do not re-derive it.**

- **⚠ FOUR ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) The §4 priced-in filter
  reads a **drawdown** as priced-in — T-2026-09-03-01 (LITE) produced a strong part 1 and was
  rejected because `move --sessions 5` returned **−7.35%**. **There is no price at which that
  rejection flips**, and no run has reinterpreted the filter or should. (2) **NEW: the same filter
  reads an event-day pop absorbed by a prior drawdown as "passes"** — the QCOM item above. Same
  root cause, opposite direction. (3) The satellite sleeve is **structurally undeployed** —
  **twenty-three theses, zero positions**; a 70/30 cash book cannot beat the S&P over a rolling 12
  months (§1) in a rising market. §2 permits the cash and §4 says most runs end in no trade —
  **both rules were followed. The agent must NOT respond by lowering the §4 bar.** (4) The core's
  divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the prior close),
  **not tracking error and never skill** — measure from the **706.74 fill**. Prior context in
  ClickUp `86bbv75bz`.

- **⚠ REJECT SCOREBOARD (opened 09-04, a tally not evidence — a few sessions is noise and ten names
  is not a sample; a future review must not quote it as a result).** 6 of 10 rejects beat VOO, mean
  excess −0.16%. **The split is the finding:** the 8 rejected on the four-part thesis or §3 average
  **−0.97%**; the 2 rejected by the §4 priced-in filter — **MU +5.49%, LITE +0.62%** — average
  **+3.06%** and are **the same two that passed the thesis. MU and LITE must never be merged into
  one finding:** MU failed on a real +5.27% run-up (the rule working as designed and costing money —
  change nothing), LITE on a drawdown (the open question). **Six of ten rejects running without us
  is the HEALTHY reading.** **Do not tighten §4 in response, and do not loosen it.** *(Not updated
  this run — the 09-08 rejects have one session of elapsed window and today's have none.)*

- **⚠ THE REASSURING FRAMING — EXPECT TO GENERATE IT AND EXPECT TO DELETE IT.** "The book fell
  −0.31% against VOO's −0.40%" is **70% exposure capturing 70% of a down move**, and it runs
  identically in reverse on every up day. Appeared 09-01, 09-02, 09-04, inside the weekly review,
  and a fifth time in the 09-08 close run's first draft — **not a slip but the sentence this agent
  produces by default whenever partial exposure and a down day coincide.** Caught and deleted every
  time; keep that record intact. **The core's mark is red for a sixth straight session and widened
  intraday (−$469.48 / −0.671% at 09:36 → −$610.13 / −0.872% at 12:35 on 09-09, VOO trading 700.58
  against the 706.74 fill) — the next red day is the next invitation.** Related: anchor the week to
  **08-31, the first operating day**.

- **Do not reach for MU or LHX.** Neither entered today's funnel, no source named them, and their
  filters were not re-run — **absence of evidence, not resolve.** Sixth consecutive day. **LITE is
  a separate case now: it entered today's funnel inside the rejected optical sweep
  (T-2026-09-09-02) and died on its own fresh filter at +7.01%, `priced_in: true`** — that is a new
  rejection, **not** a revival and **not** a resolution of the open human question above. If MU or
  LHX resurfaces from a source, **re-run its filters and re-test the timing window from that day's
  date**; that is legitimate and different from inheriting a conclusion.

- **⚠ ALL FOUR §5 SELL RULES ARE UNTESTED CODE PATHS, NOT PROVEN ONES.** Zero positions have ever
  closed, so §5.1–§5.4 have never been evaluated against a real subject. **Seven days of "no exits"
  recorded the absence of a subject, not seven clean bills of health.** §5.4 is **NOT ARMED, not
  disabled** — it arms the day the first *satellite* position opens.

- **⚠ THE HIGH-WATER MARKS ARE ABSENT, NOT STALE — A THIRD STATE.** No satellite position exists,
  so `positions.md` has **no `highest_close` and no `(as of ...)` date**. The midday backfill
  trigger keys on a **stale date**, and an absent field cannot be stale — **do NOT backfill from
  `bars`.** **Do not stamp a mark on core VOO to give the step a subject:** that would fabricate a
  §5.4 trailing stop on a position that must never carry one.

- **⚠ THE TWO-PRICE TRAP — A FIFTH SHAPE, AND THE PLAINEST YET.** Always pull `bars --adjustment
  all` for a close and a fresh `quote` for execution; **never a `positions` field for either.**
  Today the broker's `lastday_price` is **704.07** while yesterday's official close was **704.16** —
  a 9-cent gap in the ordinary direction, after four larger and stranger ones (09-04 official
  707.86 *above* broker mark 707.59; the holiday's third number 708.01; and 09-08, where a
  $0.15/share stale baseline moved reported day P&L by $38). **The gap is small today, which is
  exactly when the shortcut gets taken.** The day a satellite position exists, that shortcut writes
  a wrong high-water mark that does not error, does not look stale, and silently moves the §5.4
  stop to a level nobody chose.

- **NO TRADES, NO FILLS, NOTHING IN LIMBO.** The account's entire order history is the one 09-03
  core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO 99.046311231 @ $706.74, notional
  $70,000.00**, `status: filled`, terminal. Loss streak **0 — nothing has ever closed**, so the §6
  streak cannot move and no circuit-breaker alert is due.

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; `archive/` holds only its README. Next rollover is the first
  Friday review of **October 2026**.

- **ClickUp tasks, for reference:** 09-08 daily summary **`86bbwuc17`**; Friday's daily summary
  `86bbv6npm` and weekly review `86bbv75bz`. **No ClickUp task was created by this run** — the
  pre-market routine does not post one, and no alert condition (stale plan, breaker, push failure,
  selftest abort) arose.
