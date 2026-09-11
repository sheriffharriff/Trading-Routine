# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-11 16:16 ET 4-market-close-journal (selftest PASSED all five checks at 16:16 ET, trading_enabled true, LIVE paper, equity 99591.92; MARKET WAS OPEN TODAY - a normal Friday session, NOT a holiday: clock reads is_open false with next_open Monday 2026-09-14 09:30 ET, change_today +0.857%, equity moved +591.31 off last_equity 99000.61; DAY P&L +591.31 = +0.597%, SINCE INCEPTION -408.08 = -0.41% against the 100000.00 start; ✅ THE ALPACA DATA-PLANE OUTAGE IS RESOLVED - probed BY HAND rather than inferred from the green selftest as yesterday's carry-forward required: clock 200 (was 500 x4 at midday), bars --adjustment all 200 (was 504), quote 200 (was 504), account/positions/sleeves 200; ⚠ BUT OPEN ITEM (6) SURVIVES THE OUTAGE - selftest still probes only env/account/perplexity/clickup/control and still does NOT probe clock or market data, so a green pre-flight still certifies nothing about the data plane; ⚠ STEP 2 HIGH-WATER UPDATE WROTE ZERO MARKS AND THAT IS CORRECT, NOT SKIPPED - there is no satellite block in positions.md so there is no highest_close and no (as of ...) date to advance, the marks are ABSENT not stale, and core VOO was deliberately NOT stamped because stamping it would fabricate a §5.4 stop on the one position §5 exempts; UNLIKE AT MIDDAY THE STAMP WOULD HAVE BEEN POSSIBLE - bars answered - so the data path was tested and the rule was not; §5.4 REMAINS NOT ARMED, it arms on the first satellite fill; NO EXITS and the reason is NO SUBJECT - zero satellite positions so §5.1-5.4 had nothing to run against for the twelfth consecutive day; NO TRADES AT ANY OF TODAY'S THREE RUNS - orders --status all returns ONE row, the 09-03 core fill, status filled and terminal, NOTHING IN LIMBO overnight so trade_log.md correctly left unappended; RESEARCH 5 theses today, 0 accepted 5 rejected (ORCL read-across no Company B, LHX dead on arithmetic, LOCUST X3 no named supplier, SLI below the §3 floor, M shared-cause-not-mechanism); sleeves equity 99591.92, core 69.88%, satellite 0.0% count 0, cash 30.12%, core_in_band true, rebalance_needed false, rebalance_delta +122.42 = 0.12% of equity - NO REBALANCE DUE TOMORROW; LEDGER RECONCILED - zero satellite blocks vs zero satellite Alpaca rows, they AGREE; week anchor 2026-09-07 matches today's ISO Monday, NO cap reset due, next boundary Monday 2026-09-14; consecutive_closed_losses stays 0 - NOTHING HAS EVER CLOSED, no §6 streak movement possible and no circuit-breaker alert due; breaker INACTIVE; core VOO unrealized -408.07 / -0.583% against the 706.74 fill, intraday +591.31 / +0.857%, NO ACTION - §5 exempts core; ⚠ THE TWO-PRICE DEFECT IS SOLVED AND IT IS NOT AN OFFSET - broker current_price 702.62 is EXACTLY the midpoint of the 702.59/702.65 quote, while the official close is 702.52, so the broker mark is a live after-hours quote midpoint and not a close at all; alerts.md empty, journal entry appended, ClickUp daily summary created)
week_of: 2026-09-07
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.88
satellite_pct: 0.0
cash_pct: 30.12
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

- **✅ RESOLVED AND CLOSED: THE ALPACA DATA-PLANE OUTAGE.** *(Folds in three midday bullets — the
  outage, the market-judged-open-by-inference concession, and the 09-11 open-run summary. All were
  read in full by this run and acted on; nothing live is dropped.)* At **16:16 ET** every endpoint
  answered **200**: `clock` (was 500 × 4), `bars --adjustment all` (was 504), `quote` (was 504),
  plus `account` / `positions` / `sleeves`. **They were probed by hand, not inferred from the green
  selftest** — which is exactly what the midday carry-forward instructed, and it is the only reason
  this run can state the recovery as a fact. **The inference concession is closed and did NOT become
  a precedent:** today's session was read from `clock` directly (`is_open: false`, `next_open`
  **Monday 2026-09-14 09:30 ET**). **§7 still forbids inferring a session in order to place an
  order.** The 09-11 open run is likewise done and disposed of: zero orders, a plan that passed its
  `plan_date` gate and simply carried no intents, core in band, no rebalance, no cap reset due.

- **⚠ THE TWO-PRICE DEFECT IS SOLVED — AND IT IS NOT AN OFFSET, IT IS A QUOTE MIDPOINT. THIS
  SUPERSEDES SIX DAYS OF "UNSTABLE GAP" NOTES.** Every prior note recorded the gap between the
  broker price and the official close as an unexplained, drifting number: **6.5c (09-09), 59.85c
  (09-10 close), 4c (09-11 morning)**. **Today it resolves exactly. Broker `current_price` =
  702.62. Latest quote = 702.59 / 702.65. Midpoint = 702.62, to the cent. Official close = 702.52**
  (last trade 15:59:57 ET; `bars --adjustment all` agrees). **The broker mark is not a stale or
  imprecise close — it is not a close at all.** It is a live bid/ask midpoint that keeps moving
  after the bell, which is why the gap never had a stable size and never will have one. **Do not
  re-derive this and do not re-open it as a mystery.** The consequence is unchanged but now
  sharp-edged: **the moment a satellite position exists, a `highest_close` read from a `positions`
  field records an after-hours quote midpoint and silently moves the §5.4 stop.** Always `bars
  --adjustment all` for a close, a fresh `quote` for execution, **never a `positions` field for
  either.**

- **⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST — TODAY'S NEAR-MISS,
  AND THE THING A WEEKLY REVIEW IS MOST LIKELY TO GET WRONG.** The predicted inverted framing
  arrived: VOO **+0.84%** official, the book **+0.597%**, i.e. *"we rose less than the index."* The
  refutation is **exact on broker terms**: core weight at yesterday's close **69.697%** × broker
  move **+0.857%** = **0.5973%**, which is the day's return to four decimals. **Residual: ZERO.**
  But taking the index leg from the **official** closes (+0.8368%) while leaving the book leg on
  **broker** marks yields a **+0.0141pp residual — about $14 of "excess return" that is pure
  two-price artifact.** **Both legs from the same source, or the comparison means nothing.** The
  standing refutation still holds on any day — ~0.70 exposure to an index move is ~70% of it **by
  construction**, and it runs identically in reverse. Anchor the week to **08-31**, the first
  operating day.

- **⚠ ALL FOUR §5 SELL RULES REMAIN UNTESTED CODE PATHS, AND §5.4 IS STILL NOT ARMED.** Nothing has
  ever closed in this account, so §5.1–§5.4 have never been evaluated against a real subject.
  **Twelve days of "no exits" recorded the absence of a subject, not twelve clean bills of health.**
  **The high-water marks are ABSENT, not stale — a third state, distinct from "current and
  unchanged."** An absent field carries **no date**, so the backfill trigger (a `highest_close`
  behind the last trading day) **cannot fire and no `bars` call is due for a high-water purpose.**
  **Core VOO is deliberately never stamped** — doing so would fabricate a §5.4 stop on the one
  position §5 exempts. **§5.4 arms on the first *satellite* fill.** **Today the stamp would have
  been possible (`bars` answered) and there was simply nothing to stamp: the data path was tested,
  the rule was not.** **The failure this exists to catch is still ahead of us** — the day a
  satellite position exists and a close run is missed *or* the data plane is down at 16:00, the mark
  goes stale while every field still reads present and plausible.

- **⚠ SIX ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) **The §4 priced-in filter
  reads a drawdown as priced-in** — LITE (−7.35%) fired 09-03, LMT (−3.61%) came 0.4% short 09-10,
  **LHX (−4.47%) fired 09-11.** **There is no price at which those rejections flip.** (2) **The same
  filter reads an event move absorbed before it looks as "passes"** — QCOM (09-09, +2.70% net after
  a +8.7% intraday event move) and **AVAV (09-11, +1.20% after a +12.9% intraday round-trip inside
  one session).** Same root cause, opposite direction. **The fix for (1) and (2) is a human editing
  §4 or `alpaca.py move`. No run may reinterpret the filter.** (3) The satellite sleeve is
  **structurally undeployed — thirty-one theses, zero positions**; a 70/30 cash book cannot beat the
  S&P over a rolling 12 months (§1) in a rising market. §2 permits the cash and §4 says most runs
  end in no trade — **both rules were followed. The agent must NOT respond by lowering the §4 bar.**
  (4) The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the
  prior close), **not tracking error and never skill** — measure from the **706.74 fill**. Prior
  context in ClickUp `86bbv75bz`. (5) **RESTATED, NOW WITH A MECHANISM:** the broker/official price
  gap is a **live quote midpoint**, not an offset (see the bullet above). Cosmetic on core; **it
  becomes load-bearing the moment a satellite position exists.** **Whether the tooling should read
  closes from `bars` by default is a human's call, not a run's.** (6) **`selftest.py` certifies a
  healthy system without probing the two endpoints the routines depend on to price anything.** It
  passed all five checks at 12:34 on 09-11 while `clock` was **500** and `quote`/`bars` were
  **504**. **The endpoints recovered on their own; the blind spot did not.** **Every routine's Step
  0 is the loud-failure mechanism for exactly this**, and on the data plane it is silent. **Whether
  the pre-flight should probe `clock` and `bars` is a human's call, not a run's** — a run must not
  edit its own guardrail into a different shape. Until then: **probe them by hand and never infer
  data-plane health from a green selftest.**

- **⚠ MONDAY 09-14 IS A WEEK BOUNDARY, AND MONDAY'S PRE-MARKET RUN OWNS THREE UNSCREENED EARNINGS.**
  `new_positions_this_week` resets to 0 and `week_of` becomes **2026-09-14** — **it is already 0, so
  the reset changes nothing this time.** **Kroger, VinFast and Rent the Runway reported at or after
  09-11's pre-market survey and are MONDAY's material: that run must screen them DIRECTLY, not
  assume a later run already did.** **This instruction is the only reason Oracle's FQ1 got screened
  at all** — the 09-10 close run wrote the equivalent note and the 09-11 pre-market run acted on it.
  **Keep writing them.**

- **⚠ THE ORACLE SCREEN IS COMPLETE AND PRODUCED NO COMPANY B. DO NOT RE-OPEN IT LOOKING FOR ONE.**
  Oracle FQ1 2027 (09-10 after the close) is the largest second-order surface this log has ever
  processed — **RPO $664B (+$209B YoY, +$26B QoQ), >$30B of new AI cloud bookings, OCI +121% to
  $7.4B, 850 MW and >300,000 GPUs delivered in one quarter, FY27 capex $90–95B** — and it yielded
  **nothing**, for three independent reasons (T-2026-09-11-01): **(i)** a dedicated screen for
  US-listed companies that have *themselves* disclosed Oracle as a named customer with a quantified
  revenue share returned **"No verified companies found"**; **(ii)** the **capex guidance was
  MAINTAINED, not raised** — *"We continue to anticipate $90 to $95 billion"* — **standing rule
  (iii)**; **(iii)** Oracle's own call says the new bookings are **prepay or bring-your-own-hardware**,
  need **no incremental Oracle capital**, and **do not affect capex or revenue until FY2028 or
  beyond** — past §4.3's two-quarter limit. **The biggest number in the release is the one furthest
  outside this strategy's horizon.**

- **⚠ DO NOT REACH FOR THESE — the disposed rejects and the trap in each.** **ORCL** is Company A
  twice over and **`priced_in: true` at +5.06%**; **the plausible Oracle supplier you can name from
  memory is rule (v), and it will feel like a technicality rather than a rule.** **LHX** — dead on
  arithmetic: **$127M Palantir + $65M Anduril = the entire $192M TITAN award, $0 disclosed for any
  other participant.** The nine-day "specifically invited name" warning is **CLOSED**, and it closed
  on a number rather than by avoidance, which is why it will not flip at a different price. *(Note
  what did not happen: Anduril's $65M is real second-order money and Anduril is private — the third
  time this month the identifiable beneficiary was not listed.)* **AVAV** is the **awarded party**
  and its +1.20% is a round-tripped spike. **The LOCUST X3 / E-HEL laser source, beam director and
  power subsystem have NO named supplier in any source** — rule (v), fourth instance this month.
  **SLI** is ~$1B against the **§3 $10B floor**, its counterparty is Korea-listed, and its 10-year
  offtake runs from a commercial production start that has not happened. **M** — the tariff-refund
  read-across runs through a **statute, not a transaction**. Also closed and not to be revived:
  **LMT, GFS, EQT** (*the tempting one — a clean filter sheet that died on size, ~0.14% of annual
  volume against a 10% floor*), **LEU, TBBK, CASH, GDOT, CCB, QCOM, AMZN, GLW, VZ, MTZ, FN, COHR,
  LITE, CRDO, MRVL, DY, PWR, BSX, MDT, ABT.** **None becomes a buy at a different price.** **Do not
  reach for MU** — it has not entered the funnel for **eleven consecutive days**, no source has
  named it, its filters were **not** re-run: **absence of evidence, not resolve.** If it resurfaces
  **from a source**, re-run its filters and re-test the timing window from that day's date.

- **⚠ A SHARED CAUSE IS NOT A MECHANISM (T-2026-09-11-05) — A PART-1 FAILURE SHAPE WORTH KEEPING.**
  Macy's FQ2 beat on **$116M of IEEPA tariff refunds**. The tempting sentence — *"the ruling lowers
  other import-heavy retailers' COGS too"* — **is not a §4 mechanism**: §4 requires news about
  Company A to change Company B's economics, and Macy's receiving $116M **causes no other company to
  receive anything.** Both are downstream of the **same statute** — correlation, not a causal path —
  and any company actually receiving refunds discloses them **itself**, making it **first-order for
  that company**. **Every prior part-1 rejection died because no counterparty was named; this one
  had a real, quantified, dated event with obvious read-across.** The distinction is easy to lose
  because the sentence sounds causal when said aloud.

- **⚠ FOUR LOUD HEADLINES FROM 09-11 HAVE NO PRIMARY SOURCE. DO NOT TRADE ON THEM, AND EXPECT MORE.**
  *"Nvidia invests $30B in Intel," "Nvidia acquires Hugging Face," "Google's first nuclear deal /
  a $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity by 2032."* **All
  four trace to a single secondary aggregator briefing citing other outlets rather than any
  document; a dedicated verification query found no SEC filing, no company press release and no
  major-press coverage for any of them.** **This is standing rule (iii) in a new costume — not a
  re-aggregation of old news but an unsourced claim, and `--recency day` passes it just as
  readily.** Events of that size produce primary disclosure; its absence is the finding. **If one is
  real it will arrive with a filing attached, and that is the day it enters the funnel.**

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, Alcoa/South32, Oracle's
  maintained capex guidance, the four unsourced headlines). (iv) *A recurring ticker is a warning,
  not corroboration* (LHX — resolved 09-11 on a number). (v) *A market-structure fact is not a
  supplier relationship* — "sole producer," "dominant share," "the only company that makes X" are
  facts about an **industry**, not a **transaction**. **Rule (v) fired three times on 09-11.** **The
  source left the blank. Filling in a blank the source left blank is not research.** **Recognise the
  phrase; do not re-derive it.**

- **⚠ REJECT SCOREBOARD (opened 09-04, a tally not evidence — a few sessions is noise and ten names
  is not a sample; a review must NOT quote it as a result).** 6 of 10 rejects beat VOO, mean excess
  −0.16%. **The split is the finding:** the 8 rejected on the four-part thesis or §3 average
  **−0.97%**; the 2 rejected by the §4 priced-in filter — **MU +5.49%, LITE +0.62%** — average
  **+3.06%** and are **the same two that passed the thesis. MU and LITE must never be merged into
  one finding:** MU failed on a real +5.27% run-up (the rule working as designed and costing money —
  change nothing), LITE on a drawdown (the open question). **Six of ten rejects running without us
  is the HEALTHY reading. Do not tighten §4 in response, and do not loosen it.** *(Not updated by
  this run: 09-10's six rejects have two sessions of elapsed window and 09-11's five have none.)*

- **⚠ THE 16:45 FRIDAY WEEKLY REVIEW HAS NOT RUN YET — IT IS THE NEXT RUN, AND IT INHERITS THREE
  TRAPS.** (a) It **must not quote the reject scoreboard as a result**. (b) It must carry the
  **refuted-with-arithmetic** book-vs-index sentence, **including the mixed-source $14 artifact
  above** — a weekly review is the single most likely place for that to be presented as
  outperformance. (c) It is the first review to weigh **a full week of five- and six-a-day rejection
  counts against zero positions**; the honest framing is that **§4 was applied as written, not that
  the bar needs moving.** **August CPI landed 09-11 morning and the September FOMC is 09-15/16:**
  macro, no segment, no dollar path, **not a §4 mechanism in either direction**, whatever it does to
  the tape.

- **NO TRADES, NO FILLS, NOTHING IN LIMBO.** The account's entire order history is **one row**: the
  09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO 99.046311231 @ $706.74,
  notional $70,000.00**, `status: filled`, terminal, re-verified at the 09-11 close via `orders
  --status all`. **No `"terminal": false` case has ever arisen** and no `alpaca.py order --id`
  re-check was owed. `trade_log.md` correctly left unappended — **a run with no fill writes no trade
  entry.** Loss streak **0 — nothing has ever closed**, so the §6 streak cannot move and no
  circuit-breaker alert is due. **Core is not tracked in `positions.md` by design** (§5 exempts it),
  so **every reconciliation compares satellite blocks to satellite Alpaca positions**; a run
  comparing raw ledger to raw broker will read a correct ledger as broken.

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON FIFTEEN TIMES NOW, AND DUE AGAIN NEXT RUN.** `positions.md`
  ran to **604 lines / 42KB** before the 09-07 collapse, was cut to 162, and has since been held to
  a **single current reconciliation block** — this run folded the 09-11 midday block into the close
  block, and folded three resolved carry-forward bullets (the outage, the inference concession, the
  09-11 open run) into one **RESOLVED** line rather than extending the list. **Every load-bearing
  fact is preserved; nothing live was discarded.** The pull to append is structural — a run is
  rewarded for showing it checked something, and a deleted note looks like a check that never
  happened. **A future run will feel it too.**

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; `archive/` holds only its README. Next rollover is the first
  Friday review of **October 2026**. **`research_log.md` is ~2,200 lines — worth watching, but the
  rollover rule is monthly and this month is not over.**

- **ClickUp tasks, for reference:** **09-11 daily summary `86bbzfm12`**; 09-10 `86bbyr8vp`; 09-09
  `86bbxtn1a`; 09-08 `86bbwuc17`; 09-04 daily summary `86bbv6npm` and weekly review `86bbv75bz`.
  **No alert task exists** — no alert condition (breaker, push failure, selftest abort, guard
  violation, stale plan) has arisen, and `alerts.md` remains empty.
