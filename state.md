# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-08 09:35 ET 2-market-open-execution (plan fresh, zero intents to execute; no orders placed; core in band at 70.00%; nothing in limbo)
week_of: 2026-09-07
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.0
satellite_pct: 0.0
cash_pct: 30.01
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

- **THE 09-08 OPEN RUN EXECUTED THE PLAN IN FULL, AND THE PLAN WAS "DO NOTHING."** Selftest
  passed all five checks (`trading_enabled: true`, LIVE paper account, equity $99,975.23).
  `clock` 09:35:47 ET: **`is_open: true`** — the session is live, this was not a closed-market
  skip. **Staleness gate PASSED:** `plan_date: 2026-09-08` equals today ET, so the plan's intents
  were executable — and there were **zero of them** (no BUY, no SELL, no REBALANCE). *A fresh
  plan with nothing in it is a different outcome from a stale plan whose intents were refused;
  no `stale-plan` alert was due and none was posted.* Step 3 skipped (`core_established: true`).
  **Zero orders submitted, nothing in limbo, cap still 0 of 3, breaker INACTIVE, `alerts.md`
  empty.** *(This replaces the pre-market run's own narration — acted on, now cleared.)*

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON TWICE NOW, AND DUE AGAIN NEXT RUN.** `positions.md` ran
  to **604 lines / 42KB** before the 09-07 collapse, was cut to 162, and this run collapsed the
  09-08 pre-market and 09-04 close blocks into the single current reconciliation. Every
  load-bearing fact is preserved (the 09-03 VOO fill, the 706.74 measurement baseline, the
  satellite-to-satellite comparison rule, §5.4 unarmed, §5 untested); **nothing live was
  discarded.** The pull to append is structural — a run is rewarded for showing it checked
  something, and a deleted note looks like a check that never happened. **A future run will feel
  it too.**

- **⚠ THE CORE'S MARK IS RED AND IT MEANS NOTHING PROCEDURALLY.** At the bell: broker mark
  **706.53** vs the 706.74 fill, `unrealized_pl` **−$20.80 (−0.03%)**, `change_today` −0.209%
  against `lastday_price` 708.01. It went negative for the first time at the 09-08 pre-market
  read (−$69.33) and has stayed there. **§5 exempts core from all four sell rules** — not a stop,
  not a trigger, not a reason to touch the position. Expect a run seeing a red core to feel a
  pull toward action; there is none. `rebalance_delta` **+$3.81 — 0.004% of equity, core at
  70.00% exactly**, the closest to target it has ever sat. §2 rebalances at the **band edge**
  (65/75), not to the target.

- **⚠ THE HIGH-WATER MARKS ARE ABSENT, NOT STALE — A THIRD STATE.** No satellite position exists,
  so `positions.md` has **no `highest_close` and no `(as of ...)` date**. The midday backfill
  trigger keys on a **stale date**, and an absent field cannot be stale — **do NOT backfill from
  `bars`.** **Do not stamp a mark on core VOO to give the step a subject:** that would fabricate
  a §5.4 trailing stop on a position that must never carry one. **§5.4 is NOT ARMED, not
  disabled — it arms the day the first satellite position opens.**

- **⚠ THE TWO-PRICE TRAP — ALWAYS PULL `bars` FOR A CLOSE, NEVER A `positions` FIELD.** Seen in
  three shapes now: intraday fades, `current_price` **707.59** vs official close **707.86** at
  the 09-04 close (official *above* the broker mark), and on the holiday a third number entirely
  (`current_price` = `lastday_price` = **708.01** against Friday's official **707.86**). **The
  day a satellite position exists, that shortcut writes a wrong high-water mark that does not
  error, does not look stale, and silently moves the §5.4 stop to a level nobody chose.**

- **⚠ NEW AND IMPORTANT — A RE-AGGREGATION OF OLD NEWS ARRIVES LOOKING EXACTLY LIKE A NEW EVENT,
  AND `--recency day` CANNOT CATCH IT.** The week's dominant headline, **"Anthropic signs $517B /
  14.8 GW of compute contracts,"** is *The Information*'s **09-06 summation of eleven months of
  previously announced deals** (Amazon and Google/Broadcom from **May**; the $30B Azure
  commitment, the SpaceX Colossus lease and the $35B Lambda commitment all reported **09-02**).
  The *articles* are genuinely new, so the recency filter passes them. **This is standing rule
  (iii) — verify the news is new to the company's own disclosure — in the one form the tooling
  cannot flag. Expect it again; the AI-capex tape generates aggregation pieces constantly.**

- **⚠ THE ENTIRE SECOND-ORDER SURFACE OF THE AI-COMPUTE STORY HAD ALREADY MOVED.** Five-session
  moves at 08:24: **IREN +26.08%, BE +20.04%, HUT +17.79%** against a 4% threshold. Not one was
  marginal. **HUT is the one to record properly: it had a genuinely sourced mechanism** — Yahoo
  Finance names Hut 8 as *developer* of the 350 MW Texas site hosting Lambda's Anthropic capacity
  — **and it was lost to timing, not to weak sourcing.** That is a different failure from the
  usual one. **It does not become a buy at a lower price.**

- **⚠ DO NOT REACH FOR THESE — headline names, not second-order beneficiaries.** On the Anthropic
  compute story: **AMZN, GOOGL, MSFT, NVDA** are the named counterparties *in* the story, and
  **AVGO (T-2026-09-08-02) is Company A** — the named TPU co-supplier, on a **May 2026**
  agreement. §4: "you are not chasing the headline name." **Nscale, Firmus, Lambda, Fluidstack
  and SpaceX are all private (§3).**

- **⚠ CAT (T-2026-09-08-01) PRODUCED THE BEST-SOURCED MECHANISM SINCE LITE AND STILL FAILED —
  READ WHY BEFORE RE-DERIVING IT.** Caterpillar is **named in reporting** as the vendor of the
  gas gensets and fast-response turbines for the on-site microgrid at Anthropic/Nscale's 460 MW
  Monarch campus (Mason County WV, $45B/6yr, first reported **09-04** — the only genuinely new
  contract in the window). A named vendor at a named site: **the RTX/CLF failure mode not
  recurring.** It died anyway, on **part 3** (site services **late 2027**; CAT lead times run
  **into late 2028**; §4.3 caps at two quarters) and **part 2** (460 MW is **under 1% of a $32.2B
  segment** inside a **$72B backlog, +92% y/y**). Underneath both: **CAT has already guided to
  data-center power demand** — Q2 2026 call, "primary driver" for Power & Energy, 10 MW gas
  engine platform restarted, Wamego KS facility repurposed. **The customer's name is new; the
  demand is not.** Generalisable lesson: *a company large enough to pass §3 comfortably discloses
  this demand in aggregate long before any single site moves its numbers.*

- **⚠ THE BSX RECALL IS LIVE TODAY AND THE PRICED-IN NUMBERS ON IT ARE MEANINGLESS.** Boston
  Scientific warned **09-08** it will miss the Q3 and FY26 guidance it issued 07-29, alongside an
  **FDA Class I recall of Infinion CX spinal cord stimulator leads** (1,081 serious injuries as
  of 05-27, no deaths; **unused inventory only — implanted leads are not explanted**). MDT
  (+3.26%) and ABT (−3.69%) "passed" the §4 priced-in check **on five sessions that contain none
  of this news** — a filter whose purpose is to detect that the market already reacted is
  worthless before the market has opened on the event. **Both were rejected on part 2 regardless:
  neither Medtronic nor Abbott discloses neuromodulation or SCS revenue at all** (MDT's finest
  grain is a $2.7B/qtr Neuroscience segment bundling unrelated businesses; ABT's plausible figure
  is low-single-digit % of ~$45B, under the §4.2 floor). **NVRO returned `not enough bar
  history`** and fails §3 anyway. **§4's correlation rule permits at most one of MDT/ABT — they
  share an identical driver.** Also: the mechanism runs **against** BSX in a long-only book.

- **⚠ THE MDT/ABT SHAPE IS THE LULULEMON SHAPE, AND IT IS MORE SEDUCTIVE HERE.** No source names
  either company as gaining share **because of this recall**; the competitor list comes from an
  August market report that predates it. SCS is a genuine three-to-four-player market where
  substitution really is close to mechanical — **which makes the inference feel like a deduction.
  It is still an inference.** Recognise the upgrade of the failure mode, do not re-derive it.

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news
  is new to the company's own disclosure* (AEP — **and now CAT, and the $517B aggregation, and
  the Bloom/Oracle item whose source describes an existing partnership**; this rule fired three
  times in one run). (iv) *A recurring ticker is a warning, not corroboration* (LHX). (v) *A
  market-structure fact is not a supplier relationship* (CLF — "sole producer," "dominant share,"
  "the only company that makes X" are facts about an **industry**, not a **transaction**.
  **Recognise the phrase; do not re-derive it.**)

- **⚠ THREE ITEMS ARE WITH THE HUMAN, IN THE WEEKLY REVIEW AND IN ClickUp `86bbv75bz`. NONE IS
  THE AGENT'S TO DECIDE.** (1) The §4 priced-in filter reads a **drawdown** as priced-in —
  T-2026-09-03-01 (LITE) produced a strong part 1 and was rejected because `move --sessions 5`
  returned **−7.35%**, `priced_in: true`. **No run has reinterpreted the filter and none
  should**; the fix is a human editing §4 or `alpaca.py move`. **There is no price at which that
  rejection flips.** *(Note this run hit the mirror-image defect from the other side: MDT and ABT
  "passed" a filter measuring a window that predates the news. Same root cause — the filter reads
  a price window, not a relationship to an event. Same answer: the agent does not reinterpret
  it.)* (2) The satellite sleeve is **structurally undeployed** — **fourteen theses, zero
  positions**; a 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a rising
  market. §2 permits the cash and §4 says most runs end in no trade — **both rules were followed.
  The agent must NOT respond by lowering the §4 bar.** (3) The core's divergence from VOO is the
  **09-03 entry gap** (fill 706.74, +0.483% above the prior close), **not tracking error and
  never skill** — measure from the **706.74 fill**.

- **⚠ REJECT SCOREBOARD (opened 09-04, a tally not evidence — a few sessions is noise and ten
  names is not a sample; a future review must not quote it as a result).** 6 of 10 rejects beat
  VOO, mean excess −0.16%. **The split is the finding:** the 8 rejected on the four-part thesis
  or §3 average **−0.97%**; the 2 rejected by the §4 priced-in filter — **MU +5.49%, LITE
  +0.62%** — average **+3.06%** and are **the same two that passed the thesis. MU and LITE must
  never be merged into one finding:** MU failed on a real +5.27% run-up (the rule working as
  designed and costing money — change nothing), LITE on a drawdown (the open question). **Six of
  ten rejects running without us is the HEALTHY reading.** **Do not tighten §4 in response, and
  do not loosen it.** *(Not updated this run — today's four rejects have no elapsed window yet.)*

- **⚠ THE REASSURING FRAMING — EXPECT TO GENERATE IT AND EXPECT TO DELETE IT.** "The book fell
  −0.31% against VOO's −0.40%" is **70% exposure capturing 70% of a down move**, and it runs
  identically in reverse on every up day. Appeared 09-01, 09-02, 09-04 and inside the weekly
  review, across three different book structures — **not a slip but the sentence this agent
  produces by default whenever partial exposure and a down day coincide.** Caught every time
  before reaching a summary; keep that record intact. **Today's red core mark is the next
  invitation to write it.** Related: anchor the week to **08-31, the first operating day** — the
  honest number is **−0.313%**, not the +0.015% an 08-28 anchor produces.

- **Do not reach for LITE, MU or LHX.** None entered today's funnel, no source named them, and
  their filters were not re-run — **absence of evidence, not resolve.** Fourth consecutive day.
  If one resurfaces from a source, **re-run its filters and re-test the timing window from that
  day's date**; that is legitimate and different from inheriting a conclusion.

- **⚠ ALL FOUR §5 SELL RULES ARE UNTESTED CODE PATHS, NOT PROVEN ONES.** Zero positions have ever
  closed, so §5.1–§5.4 have never been evaluated against a real subject. **Six days of "no exits"
  recorded the absence of a subject, not six clean bills of health.**

- **NO TRADES, NO FILLS, NOTHING IN LIMBO.** The account's entire order history is the one 09-03
  core VOO buy `d177d8f0`, `status: filled`, terminal. Loss streak **0 — nothing has ever
  closed**, so the §6 streak cannot move and no circuit-breaker alert is due.

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; `archive/` holds only its README. Next rollover is the
  first Friday review of **October 2026**.

- **Friday's ClickUp tasks, for reference:** daily summary `86bbv6npm`, weekly review
  `86bbv75bz`. **No ClickUp task was created by the 09-08 pre-market or open runs** — neither
  routine posts one, and no alert condition (stale plan, breaker, push failure, selftest abort)
  arose in either.
