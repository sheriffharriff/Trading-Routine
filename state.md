# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-14 08:22 ET 1-premarket-research (selftest PASSED all five checks at 08:22 ET, trading_enabled true, LIVE paper, equity 99134.33 at selftest / 99138.29 at sleeves; MARKET IS OPEN TODAY, NOT A HOLIDAY - clock is_open false at 08:22 because it is PRE-MARKET, next_open 2026-09-14 09:30 ET i.e. TODAY, next_close 16:00 ET; NO TRADING IN THIS RUN by design; ⚠ THE WEEKEND IS THE RUN'S CENTRAL FINDING AND IT IS STRUCTURAL, NOT A QUIET NEWS DAY - both broad scans came back EXPLICITLY EMPTY on company events ("the available evidence is thin for company-specific corporate events"; the 09-12/09-13 filings sweep returned "nothing qualifies based on the sources gathered"), because §4 needs a dated transaction between two NAMED parties and US companies do not file 8-Ks on Saturday or Sunday, so EVERY Monday pre-market run screens one business day plus two empty ones - expect it, do not compensate by lowering the bar; RESEARCH 3 theses today, 0 accepted 3 rejected: T-2026-09-14-01 BWXT (HII's 336M CVN 82 long-lead award names NO subcontractor - dedicated query returned "no public source names a subcontractor or supplier receiving a portion of this specific award" - rule (v) FIFTH instance, plus a part-3 two-quarter failure), T-2026-09-14-02 packaged food (Kroger's ID-sales guidance CUT 1.0-2.0% -> 0.2-0.8% and a supplier's soft volumes are both downstream of the SAME consumer - shared cause, not a mechanism, the Macy's shape from 09-11 recognised rather than re-derived), T-2026-09-14-03 CART (Kroger NAMED Instacart on the call - a real counterparty after eleven sessions of blanks - and the thesis still died at part 2 because NO dollar figure exists anywhere in the release, 8-K, IR summary or call coverage); THE THREE ASSIGNED EARNINGS WERE SCREENED DIRECTLY, NOT ASSUMED - Kroger produced both theses above, Rent the Runway FQ2 revenue 97.7M is two orders of magnitude below the §3 10B floor, VinFast had NO fresh earnings in the window and is a foreign issuer; ⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED TWICE - CART -5.79% and BWXT -6.30% both priced_in true, its densest showing (five instances now) - BUT IT COST NOTHING because BOTH were already dead on the four-part thesis when the filter reached them, unlike LITE which passed the thesis, died on a drawdown and is +10.58% vs VOO since; do NOT let a double-fire inflate the defect's estimated cost and do NOT reinterpret the filter; MACRO IS LOUD AND UNTRADEABLE - August CPI headline +0.4% m/m / +3.4% y/y, core +0.3% m/m / +2.4% y/y, FOMC 09-16/17 INSIDE THIS WEEK: no Company A, no segment, no dollar path, not a §4 mechanism in EITHER direction; sleeves core 69.74%, satellite 0.0% count 0, cash 30.26%, core_in_band true, rebalance_needed false, rebalance_delta +258.52 = 0.26% of equity - NO REBALANCE DUE; LEDGER RECONCILED - zero satellite blocks vs zero satellite Alpaca rows, they AGREE; core unrealized -861.70 / -1.231% from the 706.74 fill, its widest of the run, NO ACTION - §5 exempts core at any number; week anchor 2026-09-14 MATCHES week_of, no reset due because Friday's review already performed it - that is the housekeeping rule working, not a skipped step, next boundary Monday 2026-09-21; breaker INACTIVE, consecutive_closed_losses 0, nothing has ever closed; alerts.md EMPTY, zero open, zero SYSTEMIC; plan_today.md rewritten with plan_date 2026-09-14 and NO intents of any kind)

prior_run: 2026-09-11 16:46 ET 5-friday-weekly-review (selftest PASSED, trading_enabled true, equity 99591.92; the §1 answer is NOT the number that looks like it - satellite sleeve 0.00% vs VOO -0.7544% on the week = +0.75pp "ahead" WITHOUT THE SLEEVE DOING ANYTHING, the entire swing is VOO falling, and the honest read is the ROLLING 12-MONTH one: VOO 12M +17.59% against a sleeve holding 30,000 cash, so a permanently idle sleeve gives up ~17.6pp on sleeve capital / ~5.3pp on the account - a PROJECTION of the current structure, not a measurement; EXPECT THIS NUMBER TO BE POSITIVE WHENEVER THE WEEK IS RED AND EXPECT TO REFUTE IT EVERY TIME; core tracking error measured at ZERO from the 706.74 fill - that instruction is DISCHARGED; account week -0.5283% vs VOO -0.7544%, the apparent +0.2261pp excess refuted EXACTLY by core weight 70.0332% x -0.7544%, residual ZERO; since-inception account -0.4180% vs VOO -0.3341% = -0.0839pp BEHIND, the honest column; both legs from bars --adjustment all throughout; 20 theses written that week, 0 accepted; 30 since inception, 0 accepted; reject scoreboard 33 measurements, 9 beat VOO, mean -0.51%, and week 1's ten REVERSED from 6-of-10 to 3-of-10 once the window lengthened - a tally, not evidence; HOUSEKEEPING week_of 2026-09-07 -> 2026-09-14 and new_positions_this_week -> 0; monthly archive rollover NOT DUE, next is the first Friday review of October)
week_of: 2026-09-14
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.74
satellite_pct: 0.0
cash_pct: 30.26
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

- **⚠ MONDAY'S FUNNEL IS THIN BECAUSE OF THE CALENDAR, NOT BECAUSE THE NEWS WAS QUIET — AND THIS
  RECURS EVERY WEEK.** Both broad scans this morning came back **explicitly empty on company
  events**: *"the available evidence is thin for company-specific corporate events"*, and the
  09-12/09-13 filings sweep returned *"nothing qualifies based on the sources gathered."* **§4
  needs a dated transaction between two named parties, and US companies do not file 8-Ks on
  Saturday or Sunday.** A Monday pre-market run is screening **one business day plus two empty
  ones**. **This is a structural property of the schedule, not a signal about the market, and the
  correct response is to expect it — never to widen the search until something qualifies.** The
  same note applies to any run following a holiday.

- **⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED TWICE TODAY AND COST NOTHING — RECORD BOTH HALVES, AND
  DO NOT MERGE THE TALLY OF INSTANCES WITH THE TALLY OF DAMAGE.** Open item (1) — the §4 filter
  reading a **drawdown** as "priced in" — hit **CART −5.79%** and **BWXT −6.30%** in one run, its
  densest showing yet and now **five instances** (LITE −7.35%, LMT −3.61% near-miss, LHX −4.47%,
  plus today's two). **The filter was applied as written and both were skipped; no run may
  reinterpret it — that is a human editing §4 or `alpaca.py move`.** **But neither rejection was
  load-bearing: BWXT had already failed parts 1 and 3, CART part 2.** The expensive instances are
  the ones that reach the filter **alive** — LITE passed the four-part thesis, was killed by a
  drawdown, and is **+10.58% vs VOO** since. **A future review that counts five instances as five
  costs will overstate the case for a change that is not the agent's to make.**

- **⚠ A NAMED COUNTERPARTY AND A QUANTIFIED EXPOSURE ARE TWO SEPARATE REQUIREMENTS, AND TODAY
  PRODUCED A CLEAN EXAMPLE OF EACH ARRIVING WITHOUT THE OTHER.** For eleven sessions the funnel's
  binding constraint was recorded as *"the source announced the transaction and withheld the
  counterparty"* (rule (v), now **five instances**, today's being **BWXT** on HII's CVN 82 award).
  **Today a source finally named one — Kroger naming Instacart on its FQ2 call — and the thesis
  died one test later, at part 2, because no dollar figure exists in the release, the 8-K, the IR
  summary or the call coverage.** **File these as two different failures.** The §4 funnel needs
  **both**, and knowing which half is missing is the difference between "public disclosure is
  stingy with counterparties" and "public disclosure is stingy with numbers." **A partnership
  announcement with no size disclosed is not a dollar path, and a run that sizes it anyway has
  fabricated the only number that matters.**

- **⚠ SIX ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) **The §4 priced-in filter
  reads a drawdown as priced-in** — five instances, see above; **there is no price at which those
  rejections flip**, and LITE puts **+10.58% vs VOO** on the bill. (2) **The same filter reads an
  event move absorbed before it looks as "passes"** — QCOM (09-09, +2.70% after a +8.7% intraday
  move) and AVAV (09-11, +1.20% after a +12.9% intraday round-trip inside one session). Same root
  cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or `alpaca.py move`.**
  (3) The satellite sleeve is **structurally undeployed — THIRTY-THREE theses, zero positions,
  nine sessions**; a 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a rising
  market. **§2 permits the cash and §4 says most runs end in no trade — both rules were followed,
  and the agent must NOT respond by lowering the §4 bar.** **§4's binding constraint is now
  identifiable and it is not thesis quality:** the source names the transaction and withholds the
  counterparty, or names the counterparty and withholds the number. **That points at something a
  human could change — widen the acceptable evidence for a named Company B, or accept the hit
  rate.** (4) The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483%
  above the prior close), **not tracking error and never skill** — **DISCHARGED AND PROVEN 09-11:
  measured from the fill, tracking error 0.0000%. Keep measuring it from the fill.** (5) The
  broker/official price gap is a **live quote midpoint**, not an offset — cosmetic on core,
  **load-bearing the moment a satellite position exists**; whether the tooling should read closes
  from `bars` by default is a human's call. (6) **`selftest.py` certifies a healthy system without
  probing `clock` or market data** — it passed all five checks on 09-11 while `clock` was 500 and
  `quote`/`bars` were 504. **Every routine's Step 0 is the loud-failure mechanism for exactly
  this, and on the data plane it is silent.** Until a human changes it: **probe by hand and never
  infer data-plane health from a green selftest.** Prior context in ClickUp `86bbv75bz`, last
  week's in `86bbzgbg3`.

- **✅ THE THREE ASSIGNED EARNINGS WERE SCREENED DIRECTLY — INSTRUCTION DISCHARGED. KEEP WRITING
  THESE NOTES.** The Friday review handed this run **Kroger, VinFast and Rent the Runway**, which
  reported at or after the 09-11 pre-market survey. **All three were screened by this run rather
  than assumed to have been handled later.** **Kroger** produced both of today's Company-A theses
  (the guidance cut and the Instacart naming). **Rent the Runway** — FQ2 revenue **$97.7M**, two
  orders of magnitude below the §3 **$10B** floor as a candidate, and no quantified counterparty
  as Company A. **VinFast** — **no fresh earnings in the window** (the recent items are guidance,
  estimates and operational updates) and a foreign issuer besides. **This hand-off mechanism is
  the only reason Oracle's FQ1 and now these three got screened at all. Nothing is pending for
  tomorrow's run — no US earnings of consequence landed after this morning's survey.**

- **⚠ THE MACRO IS THE LOUDEST STORY OF THE WEEK AND IS NOT A CANDIDATE IN EITHER DIRECTION.**
  August CPI landed 09-11 (headline **+0.4% m/m / +3.4% y/y**, core **+0.3% m/m / +2.4% y/y**) and
  the **FOMC decision lands 09-16/17, inside this week.** No Company A, no segment, no dollar
  path — it is the whole tape moving, which is exactly what §4 exists to refuse. **If it moves
  prices hard, that is a price move, not a thesis.** *(One source in today's scan priced ~87% odds
  of a 25bp **increase**, contradicting every other framing in the same result set. Unresolved and
  deliberately not chased — untradeable under §4 whichever way it reads.)*

- **⚠ ALL FOUR §5 SELL RULES REMAIN UNTESTED CODE PATHS, AND §5.4 IS STILL NOT ARMED.** Nothing has
  ever closed in this account, so §5.1–§5.4 have never been evaluated against a real subject.
  **Thirteen sessions of "no exits" recorded the absence of a subject, not thirteen clean bills of
  health.** **The high-water marks are ABSENT, not stale — a third state, distinct from "current
  and unchanged."** An absent field carries **no date**, so the backfill trigger cannot fire and
  no `bars` call is due for a high-water purpose. **Core VOO is deliberately never stamped** —
  doing so would fabricate a §5.4 stop on the one position §5 exempts. **§5.4 arms on the first
  *satellite* fill.** **The failure this exists to catch is still ahead of us** — the day a
  satellite position exists and a close run is missed *or* the data plane is down at 16:00, the
  mark goes stale while every field still reads present and plausible.

- **⚠ THE TWO-PRICE DEFECT IS SOLVED — IT IS A QUOTE MIDPOINT, NOT AN OFFSET. DO NOT RE-OPEN IT AS
  A MYSTERY.** Six days of notes called the broker/official gap an *unstable offset* (**6.5c**
  09-09, **59.85c** 09-10, **4c** 09-11 morning); it resolved exactly at the 09-11 close, where
  broker `current_price` 702.62 was **the midpoint of the 702.59/702.65 quote to the cent** while
  the official close was **702.52**. **The broker mark is not a close at all — it is a live
  bid/ask midpoint that keeps moving after the bell**, which is why the gap never had a stable size
  and never will. **Today's `current_price` 698.04 against `lastday_price` 702.56 is a pre-market
  midpoint on the same mechanism.** Always `bars --adjustment all` for a close, a fresh `quote` for
  execution, **never a `positions` field for either.** **The moment a satellite position exists, a
  `highest_close` read from a `positions` field records an after-hours midpoint and silently moves
  the §5.4 stop.**

- **⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Taking the index
  leg from **official** closes while leaving the book leg on **broker** marks produced a
  **+0.0141pp residual — about $14 of pure artifact** on 09-11. **Both legs from the same source,
  or the comparison means nothing.** The standing refutation holds on any day: ~0.70 exposure to an
  index move is ~70% of it **by construction**, and it runs identically in reverse. **Anchor the
  week to 08-31, the first operating day.** **And expect the satellite sleeve's §1 number to read
  positive on every red week without the sleeve doing anything — the defense is not arithmetic, it
  is refusing to let a favorable sign on a few sessions answer a 12-month question.**

- **⚠ DO NOT REACH FOR THESE — the disposed rejects and the trap in each.** **BWXT** — today's;
  the sole-source naval-reactor fact is **rule (v)**, and it will feel like a technicality rather
  than a rule. **CART** — died on the missing number, and the number does not exist to be found.
  **ORCL** is Company A twice over and **`priced_in: true` at +5.06%**; the screen for a US-listed
  company that has *itself* named Oracle as a quantified customer returned **"No verified companies
  found."** **LHX** — dead on arithmetic: **$127M Palantir + $65M Anduril = the entire $192M TITAN
  award**, $0 disclosed for anyone else. **AVAV** is the **awarded party** and its +1.20% is a
  round-tripped spike. **The LOCUST X3 / E-HEL laser source, beam director and power subsystem have
  NO named supplier in any source.** **SLI** is ~$1B against the **§3 $10B floor**. **M** — the
  tariff-refund read-across runs through a **statute, not a transaction**. Also closed: **LMT, GFS,
  EQT** (*the tempting one — a clean filter sheet that died on size*), **LEU, TBBK, CASH, GDOT,
  CCB, QCOM, AMZN, GLW, VZ, MTZ, FN, COHR, LITE, CRDO, MRVL, DY, PWR, BSX, MDT, ABT.** **None
  becomes a buy at a different price.** **Do not reach for MU** — it has not entered the funnel for
  **twelve consecutive days**, no source has named it, its filters were **not** re-run: **absence
  of evidence, not resolve.** If it resurfaces **from a source**, re-run its filters and re-test
  the timing window from that day's date.

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, Alcoa/South32, Oracle's
  maintained capex guidance, the four unsourced headlines). (iv) *A recurring ticker is a warning,
  not corroboration* (LHX — resolved 09-11 on a number). (v) *A market-structure fact is not a
  supplier relationship* — "sole producer," "dominant share," "the only company that makes X" are
  facts about an **industry**, not a **transaction**. **Rule (v) fired three times on 09-11 and
  again today on BWXT — five instances this month.** **The source left the blank. Filling in a
  blank the source left blank is not research.** **Recognise the phrase; do not re-derive it.**

- **⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT ARRIVED AGAIN TODAY, FOUR DAYS AFTER IT WAS FIRST
  NAMED.** Macy's FQ2 (09-11) was the first instance: $116M of IEEPA tariff refunds, where the
  tempting *"the ruling lowers other import-heavy retailers' COGS too"* runs through a **statute,
  not a transaction**. **Today's Kroger guidance cut is the same shape in a different costume** —
  Kroger's soft ID sales and a supplier's soft volumes are both downstream of the **same grocery
  consumer**, and Kroger guiding lower *causes* no supplier to receive less. **It was recognised
  rather than re-derived, which is the note working.** **Both also fail a second, independent
  test: any company actually affected discloses it itself, making it first-order for that
  company.** The distinction is easy to lose because the sentence sounds causal when said aloud.

- **⚠ HPE IS THE LARGEST OPPORTUNITY COST THIS LOG HAS PRODUCED (+19.87% vs VOO) AND THE REJECTION
  WAS CORRECT. DO NOT RECORD IT AS ONE FINDING.** T-2026-09-02-02 rejected a **Dell → HPE
  read-across** at part 1, because a read-across is an inference about **information**, not a causal
  path changing Company B's economics. **What then moved the stock was HPE's own earnings print:
  +12.4% in the single session 09-10 → 09-11.** Rejected *correctly by the rule* and *unprofitably
  in hindsight* — **two findings, recorded as two. Nothing here loosens it.** *(The same screen
  rejected the grocer read-across today, unwritten-up, on the same grounds.)*

- **⚠ REJECT SCOREBOARD — 33 MEASUREMENTS, 9 BEAT VOO, MEAN EXCESS −0.51%. STILL A TALLY, NOT
  EVIDENCE; A REVIEW MUST NOT QUOTE IT AS A RESULT.** **It reversed on itself inside one week:**
  week 1's same ten names went from **6-of-10 beating VOO (mean −0.16%) to 3-of-10 (mean +1.17%)**
  once the window lengthened by a few sessions. **The split still points the same way on more
  data:** four-part-thesis and §3 failures lag; the two **priced-in filter vetoes** average
  **+7.36%** and are the two largest positive excesses on the board. **MU and LITE must never be
  merged:** MU (+4.14%) failed on a real **run-up** — the rule working as designed and costing
  money, change nothing; LITE (+10.58%) failed on a **drawdown**, the open question. **Do not
  tighten §4 in response, and do not loosen it.**

- **⚠ FOUR LOUD HEADLINES FROM 09-11 STILL HAVE NO PRIMARY SOURCE — AND NONE APPEARED IN A WEEKEND
  FILING.** *"Nvidia invests $30B in Intel," "Nvidia acquires Hugging Face," "Google's first
  nuclear deal / a $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity by
  2032."* **All four trace to a single secondary aggregator briefing citing other outlets rather
  than any document.** **This is standing rule (iii) in a new costume, and `--recency day` passes
  it just as readily.** Events of that size produce primary disclosure; its absence is the finding.
  **If one is real it will arrive with a filing attached, and that is the day it enters the
  funnel.**

- **NO TRADES, NO FILLS, NOTHING IN LIMBO.** The account's entire order history is **one row**: the
  09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO 99.046311231 @ $706.74,
  notional $70,000.00**, `status: filled`, terminal. **No `"terminal": false` case has ever
  arisen.** `trade_log.md` correctly left unappended — **a run with no fill writes no trade entry.**
  Loss streak **0 — nothing has ever closed**, so the §6 streak cannot move and no circuit-breaker
  alert is due. **Core is not tracked in `positions.md` by design** (§5 exempts it), so **every
  reconciliation compares satellite blocks to satellite Alpaca positions**; a run comparing raw
  ledger to raw broker will read a correct ledger as broken.

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON SIXTEEN TIMES NOW, AND DUE AGAIN NEXT RUN.**
  `positions.md` ran to **604 lines / 42KB** before the 09-07 collapse and has since been held to a
  **single current reconciliation block** — this run replaced the 09-11 close block and folded its
  two live facts (the resolved outage, the solved two-price defect) into one line each. **Every
  load-bearing fact is preserved; nothing live was discarded.** **The pull to append is
  structural** — a run is rewarded for showing it checked something, and a deleted note looks like
  a check that never happened. **A future run will feel it too.**

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; nothing predates the current month. **Next rollover is the
  first Friday review of October 2026.** ⚠ **`research_log.md` is now ~2,400 lines / 160KB.** The
  rollover rule is monthly and this month is not over, so **no run may archive early** — but the
  October rollover is not optional tidying. **Every run reads these logs in full, and a run that
  starts skimming is how a system quietly stops knowing what it holds.**

- **⚠ COUNTERS, STATED SO THEY DO NOT DRIFT.** **33 theses since inception, 0 accepted** — 30
  through 09-11 (6+2+1+1 on 09-01/02/03/04, 4+5+6+5 on 09-08/09/10/11) plus **3 today**. **3 this
  week** (the week beginning 2026-09-14). A counter already drifted once (31 vs the auditable 30)
  and was corrected on 09-11; **in a repo whose only memory is these files, a counter that drifts
  unremarked is how a larger one starts.**

- **ClickUp tasks, for reference:** **09-11 weekly review `86bbzgbg3`**; 09-11 daily summary
  `86bbzfm12`; 09-10 `86bbyr8vp`; 09-09 `86bbxtn1a`; 09-08 `86bbwuc17`; 09-04 daily summary
  `86bbv6npm` and weekly review `86bbv75bz`. **No alert task exists** — no alert condition
  (breaker, push failure, selftest abort, guard violation, stale plan) has ever arisen, and
  `alerts.md` remains empty.
