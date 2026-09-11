# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-11 09:36 ET 2-market-open-execution (selftest PASSED all five checks at 09:36 ET, trading_enabled true, LIVE paper, equity 99728.60; clock is_open TRUE at 09:36:29 ET with next_close 2026-09-11 16:00 ET - market OPEN, a regular session; ZERO ORDERS PLACED - not because anything was blocked but because today's plan contains no intent of any kind; STALENESS GATE PASSED - plan_date 2026-09-11 equals today's ET date, so the plan was executable and its contents, not its age, are why nothing happened; STEP 3 SKIPPED - core_established true, the bootstrap path is closed permanently; STEP 4 NO SELL INTENTS and no satellite position exists to sell, §5.1-5.4 again had NO SUBJECT; STEP 5/6 NO BUY INTENTS - the pre-market run researched 5 theses and rejected all 5, so there was nothing to re-validate, NO alpaca.py move call was due or made, and the weekly cap 0 of 3 was never approached; STEP 7 NO REBALANCE - sleeves at 09:36 read core 69.92%, core_in_band true, rebalance_needed false, rebalance_delta +82.20 = 0.08% of equity, well inside the §2 65-75% band; LEDGER RECONCILED AT THE OPEN - zero satellite blocks vs zero satellite Alpaca rows, they AGREE, broker returns exactly one row and it is core VOO; week anchor 2026-09-07 matches today's ISO Monday, NO cap reset due, next boundary Monday 2026-09-14; consecutive_closed_losses stays 0 - NOTHING HAS EVER CLOSED; breaker INACTIVE, NEW POSITIONS WERE FULLY PERMITTED AND NOTHING WAS GATED; core VOO unrealized -273.38 / -0.391% against the 706.74 fill, intraday +725.99 / +1.05% on the session, NO ACTION in either direction - §5 exempts core from all four rules and a green tape is not a reason to act any more than a red one was; high-water marks ABSENT not stale, no backfill due, core VOO again deliberately NOT stamped, §5.4 still NOT ARMED; alerts.md empty, no stale-plan alert due, no ClickUp task created and none was due from this routine)
week_of: 2026-09-07
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.92
satellite_pct: 0.0
cash_pct: 30.08
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

- **⚠ 09-11 MARKET OPEN IS DONE: ZERO ORDERS, AND THE REASON IS AN EMPTY PLAN, NOT A BLOCKED ONE.**
  *(This bullet replaces the 09-11 pre-market bullet, read in full by this run; nothing live is
  dropped.)* Selftest passed all five checks at **09:36 ET** (`trading_enabled: true`, LIVE paper,
  equity **$99,728.60**). `clock` 09:36:29: **`is_open: true`, `next_close: 16:00 ET` — a regular
  open session.** **The staleness gate PASSED: `plan_date: 2026-09-11` equals today's ET date**, so
  the plan was fully executable and **its contents, not its age, are why nothing happened** — no
  stale-plan alert was due and none was posted. Step 3 skipped (`core_established: true`). Step 4:
  no SELL intents, no satellite position to sell. Steps 5–6: **no BUY intents, so no `move`
  re-validation was due and none was made** — there was nothing to re-validate. Step 7: **core
  69.92%, `core_in_band: true`, `rebalance_needed: false`, delta +$82.20 = 0.08% of equity — no
  rebalance.** Ledger reconciled **satellite-to-satellite: zero blocks vs zero satellite Alpaca
  rows, they agree**; the broker's one row is core VOO. Week anchor `2026-09-07` matches today's ISO
  Monday — **no cap reset due**; next boundary **Monday 09-14**. Breaker INACTIVE, weekly cap
  **0 of 3**, satellite sleeve **empty with 30.08% cash**, `control.md` notes empty, `alerts.md`
  empty. **New positions were FULLY PERMITTED at the bell. Nothing was gated. A run that places no
  order because the research found nothing is §4 working, not a rule firing** — and **the open run
  is explicitly forbidden from generating an idea to fill the gap.**

- **⚠ THE GREEN-TAPE MIRROR IMAGE ARRIVED, EXACTLY AS PREDICTED — AND IT CHANGES NOTHING.** VOO
  opened up: core mark **703.98**, **intraday +$725.99 / +1.05%**, and the unrealized loss against
  the **706.74 fill** narrowed to **−$273.38 / −0.391%** from −$543.76 at 08:20. **This is the day
  the "we lagged the index" inversion of the reassuring sentence becomes available**, and it is
  wrong for the same two reasons the falling version was: ~0.70 exposure returns ~70% of an index
  move **by construction**, and both ends of the broker's day P&L are broker marks. **§5 exempts
  core from all four sell rules — there is no action attached to the core at any number, in either
  direction.** The paired danger is the live one: **an empty satellite sleeve on a green open is
  the exact setup that produces the urge to put *something* on.** Nothing was put on.

- **⚠ THE ORACLE SCREEN HAPPENED *ONLY* BECAUSE YESTERDAY'S RUN WROTE A SEQUENCING NOTE. KEEP
  WRITING THEM.** The 09-10 close run recorded that Oracle, Adobe and Macy's had landed *after* the
  09-10 pre-market survey closed, and instructed this run to screen them **directly rather than
  assume a later run already had**. It did. **Oracle FQ1 2027 (09-10 after the close) is the
  largest second-order surface this log has ever processed — RPO $664B (+$209B YoY, +$26B QoQ),
  >$30B of new AI cloud bookings, OCI +121% to $7.4B, 850 MW and >300,000 GPUs delivered in one
  quarter, FY27 capex $90–95B — and it produced NO Company B at all**, for three independent
  reasons (T-2026-09-11-01): **(i)** a dedicated screen for US-listed companies that have
  *themselves* disclosed Oracle as a named customer with a quantified revenue share returned **"No
  verified companies found"**; **(ii)** the **capex guidance was MAINTAINED, not raised** — *"We
  continue to anticipate $90 to $95 billion"* — **standing rule (iii)**; **(iii)** Oracle's own call
  says the new bookings are **prepay or bring-your-own-hardware**, require **no incremental Oracle
  capital**, and **do not affect capex or revenue until FY2028 or beyond** — past §4.3's two-quarter
  limit. **The biggest number in the release is the one furthest outside this strategy's horizon.**
  **Today's equivalents: Kroger, VinFast and Rent the Runway reported at or after this morning's
  survey and are MONDAY's material — that run must screen them directly, not assume.**

- **⚠ THE LHX WARNING IS NOW CLOSED, AND HOW IT CLOSED IS THE POINT.** Nine days of carry-forward
  flagged **LHX** as "the specifically invited name" — what memory offers whenever a defense award
  has an unfilled supplier chain (**rule (iv)** compounded by **rule (v)**). **Today a source named
  it properly, so re-running its filters was legitimate rather than inheriting a conclusion — and it
  died on arithmetic: the $192M TITAN award is fully allocated, $127M Palantir + $65M Anduril =
  $192M, leaving $0 disclosed for LHX or any other named program participant.** That is a better
  outcome than avoiding the name, because it is auditable and it does not flip at a different price.
  **Note what did not happen: Anduril's $65M is real second-order money and Anduril is private —
  the third time this month the identifiable beneficiary was not listed.** **MU is the remaining
  invited name: it did not enter today's funnel, no source named it, its filters were NOT re-run —
  absence of evidence, not resolve. Tenth consecutive day.** If it resurfaces **from a source**,
  re-run its filters and re-test the timing window from that day's date.

- **⚠ THE PRICED-IN FILTER FIRED IN BOTH KNOWN DEFECT SHAPES ON THE SAME MORNING. EVIDENCE, NOT NEW
  ITEMS — AND NO RUN REINTERPRETS THE FILTER.** **Shape (1), the LITE shape — the filter rejects a
  stock for FALLING — did not merely come close this time, it fired: LHX returned −4.47%,
  `priced_in: true`, "LATE - skip per strategy.md section 4."** Sequence now: **LITE fired at
  −7.35% (09-03); LMT came within 0.4% at −3.61% (09-10); LHX crossed it (09-11).** **Shape (2),
  the QCOM shape — an event-day move absorbed before the filter reads it — appeared with the
  absorbing happening INSIDE a single session: AVAV printed a high of 159.23 on 09-10 and closed at
  147.06 (`bars --adjustment all`), a +12.9% intraday round-trip, read five sessions later as a
  quiet +1.20%, `priced_in: false`, "passes."** **Neither cost anything today** — LHX was already
  dead on part 2, AVAV is Company A. **The fix for both is a human editing §4 or `alpaca.py move`.**

- **⚠ FOUR LOUD HEADLINES THIS MORNING HAVE NO PRIMARY SOURCE. DO NOT TRADE ON THEM, AND EXPECT
  MORE OF THEM.** *"Nvidia invests $30B in Intel," "Nvidia acquires Hugging Face," "Google's first
  nuclear deal / a $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity by
  2032."* **All four trace to a single secondary aggregator briefing dated 09-11 that cites other
  outlets rather than any document. A dedicated verification query found no SEC filing, no company
  press release and no major-press coverage for any of them.** **This is standing rule (iii) in a
  new costume — not a re-aggregation of old news but an unsourced claim, and `--recency day` passes
  it just as readily.** Events of that size produce primary disclosure; its absence is the finding.
  **If one is real it will arrive with a filing attached, and that is the day it enters the funnel.**

- **⚠ A SHARED CAUSE IS NOT A MECHANISM — A NEW PART-1 FAILURE SHAPE, LOGGED AS T-2026-09-11-05.**
  Macy's FQ2 (09-10) beat on **$116M of IEEPA tariff refunds** ($84M pre-tax, $0.23/share, 180bp of
  gross margin). The tempting sentence — *"the refund ruling lowers other import-heavy retailers'
  COGS too"* — **is not a §4 mechanism.** §4 requires that **news about Company A changes Company
  B's economics**; Macy's receiving $116M **causes no other company to receive anything.** Both are
  downstream of the **same statute**, which is **correlation, not a causal path** — and any company
  actually receiving refunds discloses them **itself**, making it **first-order for that company**.
  **Every prior part-1 rejection in this log died because no counterparty was named. This one had a
  real, quantified, dated event with obvious read-across, and the read-across runs through a law
  rather than a transaction.** The distinction is easy to lose because the sentence sounds causal
  when said aloud.

- **⚠ DO NOT REACH FOR THESE — today's rejects and the trap in each.** **ORCL** is Company A twice
  over and **`priced_in: true` at +5.06%**; **the plausible Oracle supplier you can name from
  memory is rule (v), and it will feel like a technicality rather than a rule.** **LHX** — see
  above, dead on arithmetic. **AVAV** is the **awarded party** and its +1.20% is a round-tripped
  spike. **The LOCUST X3 / E-HEL laser source, beam director and power subsystem have NO named
  supplier in any source** — a 30 kW directed-energy weapon has a short, famous vendor list and
  every name on it arrives unprompted; **that is rule (v), fourth instance this month.** **SLI**
  is ~$1B against the **§3 $10B floor**, its counterparty is Korea-listed, and its 10-year offtake
  runs **from a commercial production start that has not happened.** **M** — see the shared-cause
  bullet. **None of these becomes a buy at a different price.**

- **⚠ CARRY-FORWARD CLOSED: 09-10's REJECTS ARE DISPOSED OF AND MUST NOT BE REOPENED.** **LMT** (no
  US-listed supplier named on JASSM/LRASM or MK 48; Lockheed is Company A; **−3.61% reads as
  "passes" because a decline fits in a 4% band**), **GFS** (named party, `priced_in: true` at
  **+4.53% — 0.53 points past the threshold is a failure, not a rounding error**), **EQT** (**the
  tempting one: clean mechanism, clean correlation, §3 clear at ~$34.5B, `priced_in: false` at
  −1.72% — and it died on size, ~0.14% of annual volume against a 10% floor; a clean filter sheet is
  not a thesis**), **LEU (~$3.4–3.8B), TBBK, CASH, GDOT, CCB** (all breach the §3 floor). Also
  closed and not to be revived: **QCOM, AMZN, GLW, VZ, MTZ, FN, COHR, LITE, CRDO, MRVL, DY, PWR,
  BSX, MDT, ABT.** **The Corning–Verizon deal resurfacing in a 09-10 article does not reopen it —
  it was announced 09-08 and is outside the window.**

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, Alcoa/South32 — **and now
  Oracle's maintained capex guidance, plus the four unsourced headlines above**). (iv) *A recurring
  ticker is a warning, not corroboration* (LHX, resolved today on a number). (v) *A market-structure
  fact is not a supplier relationship* — "sole producer," "dominant share," "the only company that
  makes X" are facts about an **industry**, not a **transaction**. **Rule (v) fired three times
  today** (the Oracle supplier chain, the LOCUST X3 subsystems, the listed comps to Blackstone's
  private liquid-cooling target). **The source left the blank. Filling in a blank the source left
  blank is not research.** **Recognise the phrase; do not re-derive it.**

- **⚠ FIVE ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) **The §4 priced-in filter
  reads a drawdown as priced-in** — LITE (−7.35%) fired 09-03, LMT (−3.61%) came 0.4% short 09-10,
  **LHX (−4.47%) fired today.** **There is no price at which those rejections flip.** (2) **The same
  filter reads an event move absorbed before it looks as "passes"** — QCOM (09-09, +2.70% net after
  a +8.7% intraday event move) and **AVAV today (+1.20% after a +12.9% intraday round-trip inside
  one session).** Same root cause, opposite direction. **The fix for (1) and (2) is a human editing
  §4 or `alpaca.py move`. No run may reinterpret the filter.** (3) The satellite sleeve is
  **structurally undeployed — thirty-one theses, zero positions**; a 70/30 cash book cannot beat
  the S&P over a rolling 12 months (§1) in a rising market. §2 permits the cash and §4 says most
  runs end in no trade — **both rules were followed. The agent must NOT respond by lowering the §4
  bar.** (4) The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above
  the prior close), **not tracking error and never skill** — measure from the **706.74 fill**. Prior
  context in ClickUp `86bbv75bz`. (5) **The broker/official price gap is not a stable offset:** 6.5
  cents (09-09), **59.85 cents (09-10 close)**, **4 cents this morning.** Cosmetic on core; **it
  becomes load-bearing the moment a satellite position exists**, because the same shortcut then
  writes a wrong `highest_close` and moves the §5.4 stop with nothing reading as wrong. **Whether
  the tooling should read closes from `bars` by default is a human's call, not a run's.**

- **⚠ REJECT SCOREBOARD (opened 09-04, a tally not evidence — a few sessions is noise and ten names
  is not a sample; a review must NOT quote it as a result).** 6 of 10 rejects beat VOO, mean excess
  −0.16%. **The split is the finding:** the 8 rejected on the four-part thesis or §3 average
  **−0.97%**; the 2 rejected by the §4 priced-in filter — **MU +5.49%, LITE +0.62%** — average
  **+3.06%** and are **the same two that passed the thesis. MU and LITE must never be merged into
  one finding:** MU failed on a real +5.27% run-up (the rule working as designed and costing money —
  change nothing), LITE on a drawdown (the open question). **Six of ten rejects running without us
  is the HEALTHY reading. Do not tighten §4 in response, and do not loosen it.** *(Not updated by
  this run: 09-10's six rejects have one session of elapsed window and today's five have none.)*

- **⚠ THE REASSURING FRAMING — REFUTED WITH ARITHMETIC. USE THESE NUMBERS RATHER THAN RE-DERIVING
  THE ARGUMENT, AND WATCH FOR ITS MIRROR IMAGE TODAY.** The sentence is *"the book fell less than
  the index."* It has appeared nine times (09-01, 09-02, 09-04, the weekly review, the 09-08 close
  run's first draft, 09-09, 09-10) and is **not a result**, for two separate reasons: **(1)** ~0.70
  exposure to an index move is ~70% of it **by construction** — the gap is a cash weighting §2
  mandates, **and it runs identically in reverse on a green day**; **(2)** the residual is a
  **measurement artifact** — both ends of the broker's day P&L are broker marks (on 09-10 the entire
  ~5bp residual was **$52.84** of two-price gap). **The refutation works on any day: substitute the
  day's exposure and index move.** **⚠ THE INVERSION IS NO LONGER A PREDICTION — VOO opened green
  (+1.05% on the core mark at 09:36), so today's close run and this afternoon's weekly review will
  meet the sentence as "the book rose less than the index" / "we lagged," and it is wrong for
  exactly the same two reasons.** The paired impulse is the dangerous one: **an empty satellite
  sleeve is the setup that produces both this sentence and the urge to lower the §4 bar to put
  *something* on.** Neither is a reason to act. Anchor the week to **08-31, the first operating
  day**.

- **⚠ ALL FOUR §5 SELL RULES ARE UNTESTED CODE PATHS, NOT PROVEN ONES — AND §5.4 IS NOT ARMED.**
  Zero positions have ever closed, so §5.1–§5.4 have never been evaluated against a real subject.
  **Ten days of "no exits" recorded the absence of a subject, not ten clean bills of health.**
  **The high-water marks are ABSENT, not stale — a third state, distinct from "current and
  unchanged."** The backfill rule fires when a `highest_close` is *behind* the last trading day; an
  absent field carries **no date**, so the trigger cannot fire, and **no `bars` call is due for a
  high-water purpose.** (One `bars --adjustment all` call was made this run — **for AVAV, as
  research** into whether a +1.20% reading described a quiet tape or a round-tripped spike.) **Core
  VOO is deliberately never stamped**, because doing so would fabricate a §5.4 stop on the one
  position §5 exempts. **§5.4 arms on the first *satellite* fill.** **The failure this exists to
  catch is still ahead of us:** the day a satellite position exists and a close run is missed, the
  mark goes stale while every field still reads present and plausible.

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON THIRTEEN TIMES NOW, AND DUE AGAIN NEXT RUN.** `positions.md`
  ran to **604 lines / 42KB** before the 09-07 collapse, was cut to 162, and has since been held to
  a **single current reconciliation block** — this run folded today's pre-market block into the
  open-run block, and this carry-forward list was rewritten rather than extended. Every
  load-bearing fact is preserved; **nothing live was discarded.** The pull to append is structural —
  a run is rewarded for showing it checked something, and a deleted note looks like a check that
  never happened. **A future run will feel it too.**

- **NO TRADES, NO FILLS, NOTHING IN LIMBO.** The account's entire order history is **one row**: the
  09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO 99.046311231 @ $706.74,
  notional $70,000.00**, `status: filled`, terminal, verified at the 09-10 close via `orders
  --status all`. **This routine places no orders by design**, so no `"terminal": false` case arose
  and no `alpaca.py order --id` re-check was owed. `trade_log.md` correctly left unappended — **a
  run with no fill writes no trade entry.** Loss streak **0 — nothing has ever closed**, so the §6
  streak cannot move and no circuit-breaker alert is due. **Core is not tracked in `positions.md`
  by design** (§5 exempts it), so **every reconciliation compares satellite blocks to satellite
  Alpaca positions**; a run comparing raw ledger to raw broker will read a correct ledger as broken.

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; `archive/` holds only its README. Next rollover is the first
  Friday review of **October 2026**. **`research_log.md` is now ~2,200 lines — worth watching, but
  the rollover rule is monthly and this month is not over.**

- **⚠ TODAY IS FRIDAY 09-11 — THE WEEKLY REVIEW RUNS THIS AFTERNOON.** It **must not quote the
  reject scoreboard as a result** (see above). It will be the first review to weigh **a full week of
  five- and six-a-day rejection counts against zero positions**; the honest framing is that **§4 was
  applied as written, not that the bar needs moving.** It must carry the **refuted-with-arithmetic**
  version of the book-vs-index sentence — a weekly review is the single most likely place for that
  framing to reappear as a "result," **and today it will arrive inverted if VOO closes green.**
  **August CPI landed this morning:** macro, no segment, no dollar path, **not a §4 mechanism in
  either direction**, whatever it does to the tape.

- **ClickUp tasks, for reference:** 09-10 daily summary `86bbyr8vp`; 09-09 `86bbxtn1a`; 09-08
  `86bbwuc17`; 09-04 daily summary `86bbv6npm` and weekly review `86bbv75bz`. **This run created no
  task and none was due** — the daily summary is the close run's job. **No alert task exists** — no
  alert condition (breaker, push failure, selftest abort, guard violation, stale plan) has arisen,
  and `alerts.md` remains empty.
