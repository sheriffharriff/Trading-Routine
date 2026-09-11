# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-11 16:46 ET 5-friday-weekly-review (selftest PASSED all five checks at 16:46 ET, trading_enabled true, LIVE paper, equity 99591.92 broker / 99582.01 on official closes; TODAY IS FRIDAY - confirmed, the review fired on the correct day and the weekly series is intact; NO TRADING IN THIS RUN by design; ⚠ THE §1 ANSWER IS NOT THE NUMBER THAT LOOKS LIKE IT - satellite sleeve 0.00% vs VOO -0.7544% on the week = +0.75pp "ahead", and +0.33pp since inception, REVERSING last week's -0.42pp WITHOUT THE SLEEVE DOING ANYTHING: it held 30,000 cash for all 8 sessions, opened nothing, closed nothing; the entire swing is VOO falling; the honest §1 read is the ROLLING 12-MONTH one - VOO 12M total return +17.59%, cash returns 0%, so a permanently idle sleeve gives up ~17.6pp on sleeve capital / ~5.3pp on the account, clearly labeled a PROJECTION of the current structure not a measurement; CORE tracking error is ZERO measured from the 706.74 fill (-0.5971% vs VOO -0.5971% over the identical window) - last review's instruction DISCHARGED, the -0.56% from an inception anchor is the permanent 09-03 entry gap; ACCOUNT week -0.5283% vs VOO -0.7544%, apparent +0.2261pp excess REFUTED EXACTLY: core weight 70.0332% at the 09-04 close x -0.7544% = -0.5283%, residual ZERO; since-inception account -0.4180% vs VOO -0.3341% = -0.0839pp BEHIND, the honest column; BOTH LEGS FROM bars --adjustment all throughout, never the broker mark; ZERO trades closed this week - §5.1-5.4 still untested code paths, §5.4 still not armed; THESES 20 written this week, 0 accepted, 20 rejected; 30 since inception, 0 accepted; REJECT SCOREBOARD 33 measurements, 9 beat VOO, mean -0.51% - and WEEK 1's TEN REVERSED from 6-of-10 beating VOO to 3-of-10 on a longer window, which is the noise caveat proving itself inside one week; HPE +19.87% excess is the largest opportunity cost this log has produced and the rejection was CORRECT (read-across rejected at part 1; the stock then rose 12.4% on ITS OWN earnings print 09-10->09-11); LITE +10.58% excess is the priced-in-drawdown defect firing expensively; RECURRING ERRORS NAMED: (1) the reassuring framing, second week running, all four sessions, and THIS WEEK IT REACHED THE REVIEW'S OWN §1 HEADLINE as a correctly-computed single-source number; (2) the two-price trap, second week, mechanism SOLVED as a quote midpoint, exposure unchanged; (3) the unnamed second-order counterparty, 8+ instances, named as the BINDING CONSTRAINT on §4 rather than an agent error; (4) the sleeve structurally undeployed, second week; HOUSEKEEPING week_of 2026-09-07 -> 2026-09-14 and new_positions_this_week 0 (already 0, nothing opened), monthly archive rollover NOT DUE - all entries are 2026-09, next is the first Friday review of October; alerts.md EMPTY, zero open, zero SYSTEMIC, no guard violation has ever occurred so no prompt is steering at a protected file; review appended to weekly_review.md and posted to ClickUp as its own task)

prior_run: 2026-09-11 16:16 ET 4-market-close-journal (selftest PASSED all five checks at 16:16 ET, trading_enabled true, LIVE paper, equity 99591.92; MARKET WAS OPEN TODAY - a normal Friday session, NOT a holiday: clock reads is_open false with next_open Monday 2026-09-14 09:30 ET, change_today +0.857%, equity moved +591.31 off last_equity 99000.61; DAY P&L +591.31 = +0.597%, SINCE INCEPTION -408.08 = -0.41% against the 100000.00 start; ✅ THE ALPACA DATA-PLANE OUTAGE IS RESOLVED - probed BY HAND rather than inferred from the green selftest as yesterday's carry-forward required: clock 200 (was 500 x4 at midday), bars --adjustment all 200 (was 504), quote 200 (was 504), account/positions/sleeves 200; ⚠ BUT OPEN ITEM (6) SURVIVES THE OUTAGE - selftest still probes only env/account/perplexity/clickup/control and still does NOT probe clock or market data, so a green pre-flight still certifies nothing about the data plane; ⚠ STEP 2 HIGH-WATER UPDATE WROTE ZERO MARKS AND THAT IS CORRECT, NOT SKIPPED - there is no satellite block in positions.md so there is no highest_close and no (as of ...) date to advance, the marks are ABSENT not stale, and core VOO was deliberately NOT stamped because stamping it would fabricate a §5.4 stop on the one position §5 exempts; UNLIKE AT MIDDAY THE STAMP WOULD HAVE BEEN POSSIBLE - bars answered - so the data path was tested and the rule was not; §5.4 REMAINS NOT ARMED, it arms on the first satellite fill; NO EXITS and the reason is NO SUBJECT - zero satellite positions so §5.1-5.4 had nothing to run against for the twelfth consecutive day; NO TRADES AT ANY OF TODAY'S THREE RUNS - orders --status all returns ONE row, the 09-03 core fill, status filled and terminal, NOTHING IN LIMBO overnight so trade_log.md correctly left unappended; RESEARCH 5 theses today, 0 accepted 5 rejected (ORCL read-across no Company B, LHX dead on arithmetic, LOCUST X3 no named supplier, SLI below the §3 floor, M shared-cause-not-mechanism); sleeves equity 99591.92, core 69.88%, satellite 0.0% count 0, cash 30.12%, core_in_band true, rebalance_needed false, rebalance_delta +122.42 = 0.12% of equity - NO REBALANCE DUE TOMORROW; LEDGER RECONCILED - zero satellite blocks vs zero satellite Alpaca rows, they AGREE; week anchor 2026-09-07 matches today's ISO Monday, NO cap reset due, next boundary Monday 2026-09-14; consecutive_closed_losses stays 0 - NOTHING HAS EVER CLOSED, no §6 streak movement possible and no circuit-breaker alert due; breaker INACTIVE; core VOO unrealized -408.07 / -0.583% against the 706.74 fill, intraday +591.31 / +0.857%, NO ACTION - §5 exempts core; ⚠ THE TWO-PRICE DEFECT IS SOLVED AND IT IS NOT AN OFFSET - broker current_price 702.62 is EXACTLY the midpoint of the 702.59/702.65 quote, while the official close is 702.52, so the broker mark is a live after-hours quote midpoint and not a close at all; alerts.md empty, journal entry appended, ClickUp daily summary created)
week_of: 2026-09-14
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
  §4 or `alpaca.py move`. No run may reinterpret the filter.** **(1) NOW HAS A PRICE ON IT: LITE,
  rejected at −7.35%, is +10.58% vs VOO over five sessions — the second-largest excess on the
  board.** (3) The satellite sleeve is
  **structurally undeployed — THIRTY theses, zero positions, eight sessions**; a 70/30 cash book
  cannot beat the S&P over a rolling 12 months (§1) in a rising market. §2 permits the cash and §4
  says most runs end in no trade — **both rules were followed. The agent must NOT respond by lowering
  the §4 bar.** **NEW 09-11 — §4's BINDING CONSTRAINT IS NOW IDENTIFIABLE AND IT IS NOT THESIS
  QUALITY:** eight-plus times in nine sessions the source **announced the transaction and withheld
  the counterparty** (Lockheed ×2, Oracle, AeroVironment, Bayer, GF/MPWR, Samsung Biologics, Anduril,
  CLF). **§4 asks for information that public disclosure supplies rarely.** That is a specific answer
  to "thirty theses, zero positions" and a better one than *"the bar is too high"*, because it points
  at something a human could actually change — **widen the acceptable evidence for a named Company B,
  or accept the hit rate. It is not grounds for a run to change anything.**
  (4) The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the
  prior close), **not tracking error and never skill** — measure from the **706.74 fill**.
  **DISCHARGED AND PROVEN 09-11: measured from the fill, core = −0.5971% against VOO −0.5971% over
  the identical window — tracking error 0.0000%.** The −0.56% that appears from an inception anchor
  is a permanent level offset in the cost basis. **Keep measuring it from the fill.** Prior
  context in ClickUp `86bbv75bz`, this week's in `86bbzgbg3`. (5) **RESTATED, NOW WITH A MECHANISM:** the broker/official price
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

- **✅ THE WEEK-BOUNDARY RESET IS DONE — but MONDAY'S PRE-MARKET RUN STILL OWNS THREE UNSCREENED
  EARNINGS.** This review performed the §6 housekeeping: `week_of` **2026-09-07 → 2026-09-14** and
  `new_positions_this_week` **→ 0** (it was already 0 — nothing opened this week, so the reset
  changed nothing). **Monday's runs will re-check, find the anchors match, and correctly do
  nothing — that is not a skipped step.** **Kroger, VinFast and Rent the Runway reported at or after
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

- **⚠ REJECT SCOREBOARD — REBUILT 09-11 ON 33 MEASUREMENTS, AND IT REVERSED ON ITSELF INSIDE ONE
  WEEK. STILL A TALLY, NOT EVIDENCE; A REVIEW MUST NOT QUOTE IT AS A RESULT.** Across all 33
  reject-measurements: **9 beat VOO, 24 lagged, mean excess −0.51%.** **The reversal is the finding
  about the scoreboard itself:** week 1's same ten names went from **6-of-10 beating VOO (mean
  −0.16%) to 3-of-10 (mean +1.17%)** once the window lengthened by a few sessions. **Last review's
  "a few sessions is noise and ten names is not a sample" caveat proved itself in seven days.**
  Week 2's 23 names: 6 beat VOO, mean −1.24%; **the eight one-session rows are not measurements**
  and a future review must re-measure rather than quote them. **The split still points the same way
  on more data:** four-part-thesis and §3 failures lag (week 1 ex-HPE **−3.27%**, week 2 non-§3
  **−1.85%**); the two **priced-in filter vetoes** average **+7.36%** and remain the two largest
  positive excesses on the board **and the same two candidates that passed the four-part thesis.**
  **MU and LITE must never be merged:** MU (+4.14%) failed on a real +5.27% run-up — the rule working
  as designed and costing money, change nothing; LITE (+10.58%) failed on a **drawdown**, the open
  question, and is now the most expensive instance of it. **Do not tighten §4 in response, and do not
  loosen it.** *(LITE was also rejected a SECOND time on 09-09 at 988.08 on parts 1/2 and has since
  fallen −6.44% vs VOO. One ticker, two rejections, opposite outcomes — which is why one window
  proves nothing.)*

- **⚠ HPE IS THE LARGEST OPPORTUNITY COST THIS LOG HAS PRODUCED (+19.87% vs VOO) AND THE REJECTION
  WAS CORRECT. DO NOT RECORD IT AS ONE FINDING.** T-2026-09-02-02 rejected a **Dell → HPE
  read-across** at part 1, because a read-across is an inference about **information**, not a causal
  path changing Company B's economics. **What then moved the stock was HPE's own earnings print:
  +12.4% in the single session 09-10 → 09-11** (51.84 → 56.05 over four sessions, then 55.23 →
  62.08). **The rejected thesis's underlying prediction came true, and the stock moved for a reason
  the thesis correctly identified as not a §4 mechanism.** Rejected *correctly by the rule* and
  *unprofitably in hindsight* — **two findings, recorded as two.** The read-across screen is the most
  frequently exercised filter in this system and has now produced its first large bill. **Both
  statements survive. Nothing here loosens it.**

- **✅ THE 16:45 FRIDAY WEEKLY REVIEW HAS RUN — 2026-09-11, ON THE CORRECT DAY, AND ALL THREE
  INHERITED TRAPS WERE HANDLED.** (a) The reject scoreboard is **not** quoted as a result and its
  one-week reversal is recorded above. (b) The book-vs-index sentence is carried **refuted with exact
  arithmetic**, and the review takes **both legs from `bars --adjustment all`** throughout — the
  mixed-source $14 artifact is named in the review rather than committed. (c) **The trap that was NOT
  anticipated is the one that landed:** with VOO **−0.75% on the week**, the satellite sleeve's
  §1 number came out **+0.75pp AHEAD**, reversing last week's −0.42pp **without the sleeve doing
  anything at all.** For the first time the reassuring framing was not a sentence to delete from a
  journal — it was a **correctly computed, single-source, arithmetically sound figure in the row §1
  cares most about.** **The defense is no longer arithmetic; it is refusing to let a favorable sign
  on 8 sessions answer a 12-month question.** **Every future review should expect this number to be
  positive whenever the week is red, and should expect to refute it every time.** **August CPI landed
  09-11 morning and the September FOMC is 09-15/16:** macro, no segment, no dollar path, **not a §4
  mechanism in either direction**, whatever it does to the tape.

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

- **MONTHLY ARCHIVE ROLLOVER: CHECKED 09-11 BY THE WEEKLY REVIEW — NOT DUE.** Every entry in
  `research_log.md`, `trade_log.md` and `journal.md` is dated **2026-09**; nothing predates the
  current month, so nothing moves and no archive index line is written. `archive/` holds only its
  README. **Next rollover is the first Friday review of October 2026.** ⚠ **`research_log.md` is now
  ~2,200 lines / 151KB and grew ~90KB this week alone on 20 theses.** The rollover rule is monthly
  and this month is not over, so **no run may archive early** — but the October rollover is not
  optional tidying. **Every run reads these logs in full, and a run that starts skimming the trade
  log is how a system quietly stops knowing what it holds.**

- **⚠ A COUNTER DRIFTED AND WAS CORRECTED: THE THESIS COUNT IS 30, NOT 31.** This state file's
  carry-forward and the 09-11 journal both said *"thirty-one theses."* `research_log.md` contains
  **thirty** IDs — 6 + 2 + 1 + 1 on 09-01/02/03/04 and 4 + 5 + 6 + 5 on 09-08/09/10/11. **Thirty is
  the auditable number and the weekly review uses it.** Small in itself; recorded because in a repo
  whose only memory is these files, **a counter that drifts unremarked is how a larger one starts.**

- **ClickUp tasks, for reference:** **09-11 weekly review `86bbzgbg3`**; 09-11 daily summary
  `86bbzfm12`; 09-10 `86bbyr8vp`; 09-09 `86bbxtn1a`; 09-08 `86bbwuc17`; 09-04 daily summary
  `86bbv6npm` and weekly review `86bbv75bz`. **No alert task exists** — no alert condition (breaker,
  push failure, selftest abort, guard violation, stale plan) has arisen, and `alerts.md` remains
  empty. **One condition this week deliberately did NOT alert and that is correct:** the 09-11 midday
  Alpaca data-plane outage (`clock` 500 ×4, `quote`/`bars` 504) is **not one of the four alertable
  incidents**, and it resolved by 16:16 ET. **The blind spot it exposed did not resolve — that is
  open item (6), and it is the human's call.**
