# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **NEVER PUT A `#` IN A FENCED-BLOCK VALUE** — `_parse_kv` does `line.split("#", 1)[0]` and
silently discards everything after it. **Validate with `common.read_state()` after rewriting.**

```
last_run: 2026-09-30 09:35 ET 2-market-open-execution (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99792.98 at pre-flight; THIS RUN PLACED ZERO ORDERS - zero buys, zero sells, zero rebalance, and it is the ONLY seat that may open a position; clock at 09:35:57 is_open TRUE which is the ONE boolean value with a single meaning, next_close 2026-09-30T16:00; THE STALENESS GATE WAS EXERCISED FOR THE THIRTIETH TIME AND DID NOT FIRE - plan_date 2026-09-30 read from plan_today.md against an ET date of 2026-09-30 computed not assumed, so the plan is FRESH and its intents were eligible to execute; the plan contained NONE, so THIS RUN IS A FRESH-EMPTY ZERO-ORDER RUN AND A STALE-PLAN RUN WOULD HAVE LOOKED BYTE-FOR-BYTE IDENTICAL IN ORDER COUNT - the gate's alert path REMAINS UNTESTED CODE and no alert was posted because none was due; HOUSEKEEPING ALL CONFIRMATIONS NOT CHANGES - ISO Monday of 2026-09-30 computed not assumed is 2026-09-28 and MATCHES week_of so NO ROLLOVER was due, nothing closed so consecutive_closed_losses stays 0 and the breaker stays INACTIVE, new_positions_this_week stays 0 of 3; RECONCILIATION CLEAN - zero satellite blocks in positions.md against zero satellite rows from the broker, compared satellite-to-satellite never raw ledger against raw broker, core VOO one row 99.046311231 shares avg_entry 706.74 a RAW print cost_basis 69999.99 unchanged since the 09-03 fill; STEP 3 BOOTSTRAP PERMANENTLY CLOSED core_established true, not re-run; STEP 4 EXITS HAD NO OPERAND - zero SELL intents and zero satellite positions, so sections 5.1 and 5.2 had nothing to check, 5.3 distance is UNDEFINED not large, 5.4 is NOT ARMED with no highest_close field at all; STEP 5 RE-VALIDATION WAS ABSENT NOT SKIPPED - zero BUY intents means zero move calls were DUE and zero were made, and that is the state the carry-forward warns looks identical to a filter that did not fire; STEP 7 NO REBALANCE - core 69.94 pct on the 09:35:57 sleeves mark sits 4.94 points inside the 65 edge and 5.06 inside the 75 edge, and rebalance_delta +61.51 must NOT be acted on because section 2 acts at the BAND EDGE not toward the 70 pct target; the delta is positive for a FIFTH consecutive run and that is still NOT the sign-instability defect resolving, the same quantity disagreed in sign on 09-24; cash reads EXACTLY 30000.00 on sleeves, a SEVENTH reading and the THIRD calendar day, VOO dividend STILL UNPAID day 3 of 8, falsifiable test deadline 2026-10-07, and non-arrival this early is EXPECTED not evidence; THE INTRADAY-DRIFT ITEM PRODUCED ITS SMALLEST INSTANCE YET INSIDE THIS RUN - selftest equity 99792.98 and sleeves equity 99794.95 seconds apart, a 1.97 spread against yesterday's 216.91, and A SMALL SPREAD IS A PROPERTY OF A QUIET MINUTE NOT OF A FIXED DEFECT, with NO OPERAND again because there are no BUY intents; IDLE CASH AN INACTIVE BREAKER AND AN UNUSED 0-OF-3 CAP ARE NOT AN OPPORTUNITY THIS SEAT MAY ACT ON - a position opened at 09:35 without a plan entry routes AROUND the discipline rather than satisfying it, and that was declined; zero research theses this seat by design, zero Perplexity calls, zero quote or move or asset calls on any rejected name, GNRC not looked at for a THIRTY-FIRST time though this seat had no funnel so the refusal was close to FREE; prior last_run preserved below)

prior_run: 2026-09-30 08:23 ET 1-premarket-research (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99598.85 at pre-flight on sleeves then 99815.76 on account MINUTES LATER a 216.91 SPREAD; THAT RUN PLACED NO ORDERS BY DESIGN - it researched and planned; HOUSEKEEPING ALL CONFIRMATIONS NOT CHANGES - ISO Monday 2026-09-28 matched week_of so no rollover, breaker INACTIVE, core 69.88 pct so NO REBALANCE and rebalance_delta +120.34 NOT acted on; RECONCILIATION CLEAN zero satellite blocks vs zero satellite rows; SECTION 5 HAD NO OPERAND ON ALL FOUR RULES which is ABSENT not PASSING; RESEARCH RAN IN FULL - four Perplexity scans all exit 0, EIGHT theses T-2026-09-30-01 through 08 and ALL EIGHT REJECTED, cumulative 87 real theses and 0 ACCEPTED EVER, 14 this week all rejected; THE HEADLINE FINDING IS THAT THE SOURCE VOLUNTEERED THE ABSENCE OF A COMPANY B THREE SEPARATE TIMES IN ITS OWN WORDS and NO RE-QUERY WAS ISSUED; THE PULL WAS NAMED TWICE - GE Aerospace on F/A-XX and the LMR source's own LG Chem Redwood Cirba warning - and both DECLINED; PRICED-IN FILTER EXERCISED AND NON-DECISIVE a THIRD STATE - ABBV -0.78 pct and RARE -1.83 pct both priced_in false and BOTH PASSED BY FALLING; SECTION 3 WAS THE DECISIVE KILL ON TWO FULL ENTRIES; ABBV IS THE MOST INSTRUCTIVE REJECTION, the ONLY candidate BOTH source-named AND section 3 eligible, killed by materiality alone; cash EXACTLY 30000.00, VOO dividend STILL UNPAID day 3 of 8, deadline 2026-10-07; plan_today.md written with plan_date 2026-09-30, ZERO BUY ZERO SELL ZERO REBALANCE)


week_of: 2026-09-28
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.94
satellite_pct: 0.0
cash_pct: 30.06
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on forty-two times.** This repo's only continuity mechanism is the next
run *reading* these files, and padding them with restatements raises the odds a genuinely live item gets
skimmed. **Carry-forward is defined as cleared once acted on.** ⚠ **The 09:35 open run added NO new items and CLOSED none — it placed zero orders and had no operand on
every check it owns.** It updated four existing items in place (the dividend reading, the staleness-gate
count, the tape facts, and the intraday-drift instance) and **wrote one new observation into the drift item:
its SMALLEST spread on record, $1.97, which is a property of a quiet minute and NOT the defect resolving.**
⚠ **A run that adds nothing to this list is the normal case, not a gap in attention.** ⚠ **A correction replaces the claim it corrects — it does
not sit beside it.** **Nothing live has been discarded.**

---

### Live — act on these

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. DAY 3 OF 8. CHECK `cash` EVERY RUN UNTIL IT RESOLVES.**
  `cash` read **exactly $30,000.00** again at **09:35:57 on 09-30** on `sleeves`, after the same reading at
  08:23 on both `account` and `sleeves` — a **seventh** reading, and still the **third calendar day**.
  ⚠ **Seven readings across three days are ONE unresolved observation of an unpaid dividend, not seven data
  points. DAY 3 OF 8.** ⚠ **A reading taken with the market OPEN is not a stronger reading than a pre-market
  one; settlement does not run on the bell.** ⚠ **NON-ARRIVAL THIS EARLY IS EXPECTED, NOT EVIDENCE — settlement runs
  on the PAY date, which is not the ex-date. Do not read $30,000.00 as the test resolving in either
  direction.** ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE AND STILL RUNNING: `cash` should rise to about
  $30,180.45. IF IT HAS NOT BY 2026-10-07, the paper account does not model dividends at all — in which case
  the book structurally under-earns its own benchmark by VOO's entire ~1.0% annual yield and §1's "beat the
  S&P TOTAL RETURN" is unwinnable BY CONSTRUCTION rather than by strategy.** ⚠ **That is a finding for the
  human, not something to fix from this seat.** The implied credit of **$180.26–$180.64** is an
  **INFERENCE** — Alpaca does not publish the figure — and must stay labelled as one.

- **⚠⚠ NEW ON 09-29 16:16, AND IT IS THIS ROUTINE'S OWN BLIND SPOT: STEP 2 HAVING NO OPERAND AND STEP 2
  WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT A RUN PRODUCES.** The close routine's headline invisible
  job is to stamp each open satellite position's official close into `highest_close`. **This run had nothing
  to stamp, and the sentence it first reached for was "high-water marks updated," which would have been
  FALSE.** ⚠ **The honest form is: the job had NO OPERAND.** ⚠⚠ **THE BACKFILL PATH REMAINS UNEXERCISED
  CODE** — re-pull the window on a stated adjustment basis, take the max from that ONE pull — **and 09-28 is
  the proof that is not academic: that day lost its close run, so with ONE satellite position open, 09-29's
  midday run would have had to backfill across an ex-dividend date, which this system has never done.**
  **The cost has been zero because the sleeve is empty. That is luck, not a control.** ⚠ **Do not read a
  clean close run as a passing test of the mark machinery.**

- **⚠⚠ EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
  VOO went ex-dividend 09-28; `bars --adjustment all` rescaled every prior close by **0.997432**;
  `--adjustment raw` and `--adjustment split` return the original series to the cent. **Both series are
  correct; they are different bases.** ⚠ **09-28 AND 09-29 AGREE TO THE CENT ON BOTH BASES (703.60 and
  702.27), because the ex-date lies at or before both — the divergence is entirely in the sessions BEFORE
  it.** **Raw, pre-ex:** 09-25 710.705, 09-24 707.28, 09-23 707.28, 09-22 712.69, 09-21 712.76, 09-18
  701.85. **`--adjustment all`, same sessions:** 708.88 / 705.47 / 705.47 / 710.86 / 710.93 / 700.05.
  ⚠ **The 09-03 core fill at 706.74 is a RAW print; measuring it against an `--adjustment all` close MIXES
  BASES.** ⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**
  ⚠⚠ **§5.4 IS THE REAL CASUALTY AND IT FAILS TOWARD SELLING** — a `highest_close` stamped before an ex-date
  and compared against a post-ex adjusted close manufactures a **phantom drawdown equal to the dividend**
  (0.257% on 09-28). **THE FIX IS WRITTEN INTO `positions.md`'s HEADER, where it will be read before the next
  mark is stamped: same basis, same call, re-pull the whole window and take the max from that one pull.**
  ⚠ **The empty sleeve is the only reason this has cost nothing.** **`voo_close_at_entry` is a LABEL, not a
  baseline — re-derive the benchmark leg from a fresh pull at review time.**
  ⚠⚠ **AND THE SECOND PRICE-SOURCE AXIS — `quote`'s `prevDailyBar` vs `bars --adjustment all` ON THE SAME
  SESSION — AGREED TODAY (both 703.60), AND THAT IS NOT THE DEFECT RESOLVING.** The 09-28 disagreement came
  from ex-dividend rescaling, and today there is no rescaling between the two sessions to disagree about.
  ⚠ **An agreement obtained by removing the cause teaches nothing about the cause. DO NOT REPORT THE AXIS AS
  CLOSED.**

- **⚠ HIGH-WATER MARKS: NOTHING TO RECORD AND NOTHING WAS SKIPPED — CONFIRMED AT THE 09-29 CLOSE.**
  `positions.md` carries **zero satellite blocks**, so `highest_close` is **ABSENT — the third state, carrying
  no `(as of …)` date at all.** ⚠ **Do not read a missing stamp as a failed close run: there is no field, so
  there was nothing to write. DO NOT BACKFILL ANYTHING.** **§5.4 is NOT ARMED**; it arms on the first
  **satellite** fill, and the 09-03 core fill was not one. §5.3's distance is **UNDEFINED, not large.**
  ⚠ **The distinction is FREE today and stops being free the moment a satellite fill lands** — after that, a
  mark silently not written reads identically to a mark correctly unchanged, and **only the `(as of …)` date
  separates them. Compare the date; never infer from the field's emptiness.** ⚠ **AND WHEN IT ARMS, NO
  BACKFILL MAY TAKE ITS MAX FROM A BAR DATED TODAY WHILE THE MARKET IS OPEN, NOR FROM A DIFFERENT ADJUSTMENT
  BASIS THAN THE ONE IT IS COMPARED AGAINST.** **§5.1–§5.4 have never had an operand in this account's entire
  history.**

- **⚠ THE 09-28 GAP — CLOSED AS AN ONGOING FAILURE, STILL OPEN AS A QUESTION FOR THE HUMAN.**
  Three of four routines left **no committed output on 2026-09-28**. ⚠⚠ **RE-VERIFIED FROM `git log` ON
  09-30: all four routines committed on 09-29 AND the pre-market run committed on 09-30. So 09-28 stands as
  a ONE-DAY, THREE-ROUTINE gap — a real gap and a question for the human, and it must NOT be reported as an
  ongoing failure.** ⚠ **The cause is not visible from inside a run and is NOT asserted.**
  ⚠⚠ **THE COST WAS ZERO TWICE OVER AND THAT IS LUCK: an empty sleeve gave routine 3 nothing to manage, an
  empty plan gave routine 2 nothing to execute. On a day with an open satellite position, a missing routine 3
  is an UNMANAGED §5 BOOK for a full session, and a missing routine 4 is a `highest_close` that never got
  written.** ⚠ **AND THE GAP DESTROYED A PIECE OF EVIDENCE: 09-28 was the FIRST morning with a genuinely
  stale `plan_today.md` — word for word the setup the staleness gate had been waiting for — and the gate was
  not reached, because the run containing it did not execute. THE GATE REMAINS UNTESTED CODE, and after
  today's open it will have been exercised THIRTY times without ever firing.**

- **⚠⚠ THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE, OUT LOUD, AND THAT IS A RESULT RATHER THAN AN EMPTY
  SEARCH.** The 09-29 guidance-and-capacity scan returned five US-listed names and printed, for **four of the
  five**, the phrase *"No other company's revenue or costs are identified as directly affected in the
  available source material."* ⚠ **That is not an under-searched funnel. It is the source volunteering the
  absence of a Company B.** ⚠⚠ **A run that then produces one has supplied it from its own priors, which is
  verbatim the failure §4's honest-broker paragraph describes.** ⚠ **Recognise this shape on sight: when the
  source says no counterparty is identified, the correct next action is to WRITE THAT DOWN, not to go looking
  for one in a differently-worded query.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR JUDGMENT
  RATHER THAN CARE. 87 REAL THESES, ZERO ACCEPTED EVER** (88 `### T-` headings less the template, recounted
  from source on 09-30 with `grep -c`). **14 this week, ALL REJECTED.** Set beside that: an empty satellite sleeve, **~30%
  idle cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker, and an account at **−0.4427% since
  inception on official closes** (−0.2623% carrying the receivable). ⚠⚠ **A LOSING ACCOUNT RAISES THE PULL IN
  A NEW WAY AND THE DISTINCTION STILL HOLDS: the book is down because it holds ~70% of a market that fell,
  and it BEAT that market again today, by exactly the cash weight. "Deploy something" is not what these
  numbers argue for; they argue that the sleeve has no effect in EITHER direction.** ⚠ **09-25 remains the
  sharpest evidence: the funnel finally produced the well-sourced, named-supplier, allocated-figure candidate
  that a month of rejections implied was the missing ingredient — AND IT WAS STILL NOT A TRADE. That is
  evidence the bar is not what is binding, NOT evidence the bar should move.** §4's own position governs: a
  run that finds nothing is a successful run. **Naming the pull is the only defence against acting on it.**
  If the bar is to move, that is a `strategy.md` change and **only the human may make it.**
  ⚠ **WHERE THIS WEEK'S 14 DIED, BY THE DURABLE KILL: part 1 = 5, part 2 = 2, part 3 = 2, §3 = 2,
  premise = 2, with one (SMMT) dying three times over.** **09-30's eight: T-01 F/A-XX part 1 · T-02 Ultium
  LMR part 3 (2028 completion, durable even if a supplier is named later) · T-03 fusion/HTS §3 (CFS private,
  Fujikura Tokyo-listed) · T-04 ABBV part 2 · T-05 RARE §3 ($1.42B vs a $10B floor) · T-06 LLY part 3 (BLA
  planned Q1 2027) · T-07 tariffs premise · T-08 CI part 1 (no stated cause).**
  ⚠⚠ **§3 WAS THE DECISIVE KILL ON TWO FULL ENTRIES TODAY, WHICH IT WAS NOT ON ANY OF 09-29'S SIX.** ⚠ **Do
  NOT read that as a trend — it is a one-day observation, and it reflects WHICH EVENTS the tape offered
  (a private fusion developer and a $1.4B biotech), not a change in how the funnel screens.**
  ⚠⚠ **AND THE SINGLE MOST DECISION-RELEVANT DATUM THIS WEEK: T-2026-09-30-04 (ABBV) IS THE ONLY CANDIDATE
  IN THE LOG THAT WAS BOTH EXPLICITLY NAMED BY A SOURCE AND §3-ELIGIBLE — the two things every other
  candidate lacked — AND MATERIALITY KILLED IT ON ITS OWN.** ⚠ **That is direct evidence the binding
  constraint is NOT the evidence bar. It sits beside 09-25's JBL as the second independent instance, and the
  two fail on DIFFERENT parts (JBL on disclosed zero margin, ABBV on magnitude), which is what makes the pair
  informative rather than repetitive.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY.** ⚠ **09-30's eight rejections do NOT become a
  queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE.** **F/A-XX supplier chain** (rule (v) — the
  source was asked directly and stated no subcontractor has been named; **and the answer this run nearly
  supplied from its own priors was GE AEROSPACE, on the strength of the F414 and a press statement of
  enthusiasm — the source explicitly closes that door**) · **Ultium Cells LMR chain** (no US-listed supplier
  named; **retrofit completes 2028**, outside the horizon; the source's own warning about LG Chem / Redwood /
  Cirba must not be read as a candidate list) · **CFS / Fujikura HTS tape** (§3 — CFS **private**, Fujikura
  **Tokyo-listed**; price expressly undisclosed; and **AMSC is a competitor that did NOT win the order**, and
  below the §3 floor) · **ABBV** (part 2 — an **unexercised option** on a single dry-eye asset cannot reach
  10% of AbbVie's revenue) · **RARE** (§3 — **$1.42B against a $10B floor**) · **LLY / GLP-1 injectable
  chain** (part 3 — **BLA planned Q1 2027**; and the only Company B, West Pharmaceutical, was **self-supplied
  and never queried**) · **the pharmaceutical-tariff complex** (environment input, ONE party, tariffs only
  *potential*) · **CI** (a **$7.2B miss against consensus** with no stated cause — rule (viii) in a new dress).
  ⚠ **AND 09-29'S AND 09-25'S REJECTIONS WERE NOT REHABILITATED EITHER** — zero `move`, `quote`, `bars` or
  `asset` calls on JBL, AKAM, RDW, FLNC, IOVA, SMMT, CRK, AIR, Lenovo or any memory supplier, in any seat on
  09-30. **A rejection is not a queue.** ⚠ **One §3 question remains reached-but-undecided: Shopify is a
  Canadian issuer trading as common stock on a US exchange, which §3's "US-listed common stock" does not
  obviously settle. A future run reaching this with a LIVE candidate must put it to the human rather than
  decide it from this seat.**

- **⚠⚠ NEW ON 09-30, AND IT IS A STRUCTURAL FINDING ABOUT THE FUNNEL RATHER THAN ABOUT A CANDIDATE: US
  DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE, AND TWO CONSECUTIVE SESSIONS NOW SAY SO.**
  **09-29: a $20.7B AMRAAM multiyear award to RTX — four named CONTRACT LINE CATEGORIES, not one
  subcontractor named or allocated a dollar. 09-30: a >$20B F/A-XX full-scale-development award to Boeing —
  the funnel asked DIRECTLY whether any US-listed supplier had been named, and the source answered that none
  had.** ⚠ **Different prime, different program, different service, same kill.** ⚠⚠ **THE MECHANISM IS
  DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below it is commercially
  confidential, so the dollars are never allocated to a named public company.** ⚠ **CONSEQUENCE FOR A FUTURE
  RUN: when a defence award appears in the 5a scan, expect this outcome. It is still worth ONE funnel query —
  because the exception would be enormously valuable and the query is cheap — but a run that gets the
  now-familiar answer must WRITE IT DOWN and stop, not re-word the query.** ⚠ **The industry answer is always
  sitting in the reader's priors (Aerojet Rocketdyne for AMRAAM, GE for the F/A-XX engine) and that is exactly
  what makes this funnel dangerous rather than merely unproductive.**

- **⚠⚠ THE MOST DECISION-RELEVANT REJECTION ON THE BOARD REMAINS JBL (09-25).** Anthropic committed **~$11.6B
  over seven years** to **Akamai**; Akamai's 8-K then **named a US-listed supplier and allocated a specific
  dollar figure to it** — a Build Request authorizing **Jabil (JBL)** to procure **~$1.7 billion of memory
  components**. ⚠ **And it is not revenue: Akamai pays "all corresponding supplier invoice amounts," Jabil
  holds the components "IN CONSIGNMENT AS BAILEE," and Akamai "will REPURCHASE such components from the
  Company AT COST."** A disclosed statement of **zero margin**. The only figure that would satisfy part 2 —
  Jabil's assembly fee — **is disclosed by nobody.** ⚠⚠ **A FIFTH form of open item (3)'s binding constraint
  and the ONLY one no widening of the evidence bar would relieve — widening it would have let this THROUGH.**
  ⚠ **Do not reach for this chain again, and not at a lower price — the price was never the problem.** Full
  working in **T-2026-09-25-01**. ⚠ **09-29 ADDS A SIXTH FORM, AND IT IS THE ONE WIDENING THE BAR HELPS
  LEAST: THERE IS NO COUNTERPARTY AT ALL.** IOVA raised guidance on its own product, made in its own
  facility, and **names no external supplier** — T-2026-09-29-02. **No withheld figure exists to widen a bar
  toward.**

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES.** **Shape one: a DRAWDOWN misread as priced-in**
  (nine instances, newest CNC −6.44% → `true`), plus three near-misses that cleared only because the *fall*
  was fractionally too small (LMT −3.61%, GM −3.95%, LH −3.83%). **Shape two: the filter working** on genuine
  news rises (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%). **Shape three (09-25, JBL): a genuine RISE UNRELATED
  TO THE NEWS that the window swept up** — +4.97% over five sessions on a grind whose largest day was
  **+1.72%** and whose **news day moved JBL +0.63%.** §4 conditions on having moved 4% "**on this news**"; the
  mechanized check cannot see causation. ⚠ **The defect is SIGN- AND CAUSATION-BLINDNESS, not the threshold.**
  ⚠⚠ **AND THE AGENT DID NOT ACT ON IT, DELIBERATELY — that is the part to carry forward.** ⚠ **Only a human
  may change §4 or `alpaca.py move`.**
  **⚠ AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read `priced_in: false` at +3.19%**
  while its closes ran **104.53 → 117.435 = +12.35% IN ONE SESSION**, then 118.33, 118.42, then **110.44 =
  −6.74%** — a +12.35% event move and a −6.74% give-back inside the SAME five-session window, netting to a
  passing +3.19%. ⚠ **Prior instances (QCOM, AVAV) were INTRADAY round trips; this one spans MULTIPLE
  SESSIONS, and no 09:35 re-validation would have surfaced it either.**
  ⚠ **09-29 MADE ZERO `move` CALLS IN ANY SEAT. That is an ABSENT check, not a skipped one — every candidate
  died before an eligible ticker was reached. "The filter did not fire" and "the filter had nothing to fire
  on" look identical in a run summary and are not the same thing.**
  ⚠⚠ **AND 09-30 SUPPLIES THE THIRD STATE, WHICH IS NEW AND WHICH NEITHER OF THOSE TWO LABELS COVERS:
  EXERCISED AND NON-DECISIVE.** Two `move` calls were made — **ABBV 265.29 → 263.22 = −0.78%** and
  **RARE 15.60 → 15.315 = −1.83%**, both `priced_in: false` — **and neither rejection turned on them**; ABBV
  died at part 2 and RARE at §3. ⚠ **So the filter ran, returned a verdict, and decided nothing.**
  ⚠⚠ **WORSE, BOTH PASSED BY FALLING.** A `false` verdict obtained from a DOWN move carries no information
  about whether the news is in the price — **it is defect shape one (sign-blindness) in its mild, passing
  form, where the nine catalogued instances were all the loud, failing form.** ⚠ **RARE is the one to
  remember: a name whose licensed product had just been APPROVED, printing −1.83% over five sessions, is
  precisely the reading that invites a "the market has not noticed" story. That story was not written.**
  ⚠ **A run reporting "priced-in: pass" must say WHICH of the three states it means.**

- **⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.**
  Two routines read `is_open: true` and can pull a live partial bar: **routine 2 at 09:35 and routine 3 at
  12:30.** ⚠ **The midday case is the dangerous one: at 12:41 on 09-25 the partial read c 710.555, n 1,731,
  v 69,713 — half a session of real volume, a plausible OHLC and a close inside the range. It does NOT look
  like a stub.** ⚠⚠ **YOU CANNOT JUDGE A BAR'S COMPLETENESS FROM `v` AGAINST A PRIOR-DAY MEAN.**
  ⚠ **Held in the opposite direction on 09-28:** that session printed **v 62,354 against Friday's 164,725 —
  38%** — and it is a **COMPLETE** session; `feed=iex` returns **one venue's slice** of consolidated volume.
  ⚠ **AND TODAY IS THE CONVERSE INSTANCE: 09-29 printed v 101,166, well above 09-28's complete 62,354, and
  it is ALSO complete. LOW VOLUME IS NOT EVIDENCE OF A PARTIAL BAR ANY MORE THAN HIGH VOLUME IS EVIDENCE OF
  A COMPLETE ONE. `n` and `v` are a SMELL TEST; THE RELIABLE DISCRIMINATOR IS THE CLOCK — and post-bell, the
  confirming check is that a bar for today EXISTS and its close matches the 15:59 `latestTrade`.**
  ⚠ **And the trap is usually MILD, which is the uncomfortable half** — the 09-25 midday partial was
  **fifteen cents** off the official close. **A loud warning whose observed instances are all mild teaches a
  future run that the shortcut is safe. It is not safe on a day with a 2% afternoon reversal.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — AND NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat.
  **ON THE 09-29 CLOSE, OFFICIAL/PRICE BASIS (`bars --adjustment all`, VOO c 702.27, complete session):
  equity $99,557.25, core $69,557.25 = 69.8666%, cash 30.1334%, day −$131.73 / −0.1321% from 09-28's
  $99,688.98, since inception −$442.75 / −0.4427%. TOTAL-RETURN BASIS carrying the inferred ~$180.45
  receivable: ~$99,737.70, day −0.1319%, since inception −0.2623%.** **BROKER MARK at 16:16:45: equity
  $99,601.82, core $69,601.82 = 69.88%, cash 30.12%, core `unrealized_pl` −$398.17 / −0.569% against the
  706.74 RAW fill.** ⚠ **The broker figure is a LIVE MIDPOINT and must never be differenced against a close
  figure.** **Prior session for reference: 09-28 close equity $99,688.98, core 69.9064%.**
  **ON THE 09-30 PRE-MARKET (08:23, BROKER MARKS, NOT CLOSES): `sleeves` equity $99,598.85, core
  $69,598.85 = 69.88%, cash $30,000.00 = 30.12%, `unrealized_pl` −$401.14 / −0.573% against the 706.74 RAW
  fill, `rebalance_delta` +$120.34.**
  **ON THE 09-30 OPEN (09:35:57, BROKER MARKS, MARKET OPEN, NOT CLOSES): `sleeves` equity $99,794.95, core
  $69,794.95 = 69.94%, cash $30,000.00 = 30.06%, `rebalance_delta` +$61.51; `positions` at the same minute
  gives core `current_price` 704.6699, `unrealized_pl` −$205.04 / −0.293% against the 706.74 RAW fill, and
  `lastday_price` 702.46 against an official 09-29 close of 702.27 on BOTH bases.** ⚠ **That `lastday_price`
  gap is the CLOSED question — do not re-open it, and do not difference it against anything.**
  ⚠ **NONE of these open-run figures is a close. Fifty-first consecutive run inside 69.59–70.22.**
  ⚠⚠ **STANDING CONSEQUENCE OF OPEN ITEM (5), AND 09-30 PRODUCED THE LARGEST INSTANCE YET — INSIDE ONE
  PRE-MARKET RUN: `sleeves` returned equity $99,598.85 and `account` returned $99,815.76 MINUTES LATER, a
  $216.91 SPREAD** (consistent with VOO drifting ~$2.19/share in thin pre-market trade across 99.046311231
  shares). ⚠ **That is twenty-three times the $9.41 spread caught at 09:35 on 09-29, and it is PRE-MARKET,
  where the book is thinnest.**
  ⚠⚠ **AND 09-30's OPEN RUN SUPPLIES THE SMALLEST INSTANCE ON RECORD, WHICH IS THE ONE MOST LIKELY TO BE
  MISREAD: `selftest` reported equity $99,792.98 and `sleeves` returned $99,794.95 seconds later — a spread
  of $1.97.** ⚠ **A SMALL SPREAD IS A PROPERTY OF A QUIET MINUTE, NOT OF A FIXED DEFECT. The range across
  four recorded instances is now $1.97 to $216.91 with no stable size, exactly like the broker/official gap
  in open item (5), and for the same reason: both are live midpoints.** ⚠ **Do not report a small spread as
  the drift narrowing.** ⚠ **An intraday equity figure is only meaningful with its CALL and its
  TIMESTAMP attached, and two figures from different calls must never be differenced.** ⚠⚠ **THIS BITES
  §6's 5% SIZING CAP, WHICH IS COMPUTED AGAINST LIVE EQUITY — a notional sized off an 08:23 `sleeves` read
  and submitted at 09:35 is sized against a number that no longer exists. IT HAS NO OPERAND ONLY BECAUSE NO
  PLAN HAS EVER CARRIED A BUY INTENT.** **Fiftieth consecutive run inside 69.59–70.22.** ⚠ **`rebalance_delta` is POSITIVE on BOTH
  bases for the third consecutive run (+$132.82 official, +$119.45 broker) and the bases AGREE. NOT the
  defect resolving; the same quantity disagreed in SIGN on 09-24. A run that checks one basis and finds
  agreement learns nothing.** **NO REBALANCE IS DUE** — §2 acts at the **65/75 band edge** and core sits
  **4.87 points** inside it.
  ⚠ **AUDIT ANY SUPERLATIVE BEFORE REPEATING IT.** On **price**, 09-28's −0.7010% **IS** the largest
  single-day loss on record; on **total return** it is **−0.5212%, SECOND**, behind 09-23's −0.5327%.
  **Today's −0.1321% is not notable in either direction.** Since inception **−0.4427% is NOT a low** — 09-16
  reached −1.3396%, 09-15 −1.0350%, 09-10 −0.9954%. *(Grounded from a 45-session pull whose rows before the
  09-03 fill are **COUNTERFACTUAL** — the account held $100,000 cash — and must never be read as account
  history.)*

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`, NEVER a
  `positions` field for a close or an execution reference. Close-to-close from `bars` (⚠ a COMPLETED
  session's bar, ⚠ and STATE THE ADJUSTMENT), a fresh `quote` for execution.** ⚠ **09-28: broker
  `equity − last_equity` = −$736.91 against a real price-basis move of −$703.72 — artifact −$33.19. On 09-29
  `last_equity` reads 99,689.97504524391 against an official prior-close equity of 99,688.98 — close, and
  STILL NOT THE SAME NUMBER. The field is UNUSABLE, not imprecise.**
  ⚠ **`lastday_price` is CLOSED as a question — four falsified mechanisms, both signs observed. It reads
  **703.61** on 09-29 against an actual 09-28 close of 703.60 on BOTH bases; that is the SAME reading the
  morning runs saw, so it is the same observation and NOT a new miss. STOP PREDICTING IT; DO NOT RE-OPEN
  IT.** **Post-bell `current_price` minus official close, EIGHT observations: +$1.13, −$0.22, +$0.169,
  +$0.02, −$0.97, −$0.054, −$0.25, and +$0.45 on 09-29 (702.72 at 16:16:45 against a 702.27 close).**
  **Both signs, no predictable sign, no correctable offset.** **Keep writing falsifiable predictions down in
  advance for LIVE questions** — there is one on the dividend credit, above.

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 17 OF 17 AND STILL HAS NO EXCEPTION.** **09-29: VOO −0.1890%
  (`--adjustment all`, completed closes, and no dividend sits inside this window because the ex-date preceded
  both sessions), the book −0.1321% on the same basis, excess +0.0569pp — against +0.0569pp PREDICTED by
  holding ~69.9% core and the rest in idle cash. Agreement to 0.0000pp.** The satellite sleeve contributed
  **exactly 0.0000%**, as it has for the account's entire history. ⚠⚠ **The 09-25 weekly review recomputed
  all 15 post-fill sessions from official closes and found PERFECT separation: every VOO-down day positive
  excess, every VOO-up day negative, one flat day exactly 0.0000pp. 09-28 was the TENTH VOO-down day and
  09-29 is the ELEVENTH — 17 of 17 sessions.** ⚠ **That is not a performance statistic — it is the signature
  of a book with ONE long position at ~70% weight and NO SECOND SOURCE OF RETURN.** ⚠⚠ **A TIGHT FIT IS NOT
  CONFIRMATION: the model fits to 0.0000pp because there is nothing in the book the model omits.** ⚠⚠ **AND
  THE TWO READINGS ARE THE SAME FACT: on 09-25 a good day in dollars was a bad day against the benchmark; on
  09-28 and 09-29 a LOSING day in dollars was a POSITIVE-EXCESS day. Neither is skill.**
  ⚠ **THE TRAP, and the standing same-source rule does NOT catch it: comparing the book's PRICE basis against
  VOO's `--adjustment all` gave a spurious +0.0438pp on 09-28, because one leg excluded the dividend and the
  other included it. BOTH LEGS WERE FROM `bars --adjustment all` — the mismatch is between the ACCOUNT and the
  BENCHMARK recognising the same cash on DIFFERENT DATES.** ⚠ **It does NOT bite on 09-29, because no
  dividend falls inside the 09-28→09-29 window on either leg. It bites again on the next ex-date.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — ELEVEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  ⚠⚠ **(11) NEW ON 09-30, AND IT IS THE FIRST ONE COMMITTED BY THE RUN THAT CAUGHT IT RATHER THAN INHERITED.**
  Writing `positions.md`, this run advanced the session counter from **20/17** to **21/18** — because it was
  running *on* 09-30 and reflexively counted the day it was standing in. ⚠ **At 08:23 the market has not
  opened: today is NOT a completed session and the count must not advance.** It was caught and reverted in
  the same run, and the correction is written into `positions.md` beside the figure.
  ⚠ **THE GENERAL FORM IS WORTH MORE THAN THE INSTANCE: a counter is only safe to increment from a COMPLETED
  session, and a PRE-MARKET seat has none of today's to add. Routines 1 and 2 are both exposed to this;
  routine 4 is not.** ⚠ **And note the failure mode this one shares with catch (9): re-running the check
  REPRODUCES THE WRONG NUMBER, because the error is in the definition of the unit, not in the arithmetic.
  Only the clock exposes it.**
  ⚠⚠ **(10) A NUMBER THAT IS CORRECT ON A BASIS NOBODY NAMED.** The 09-28 close nearly wrote *"largest
  single-day loss on record"* off a 30-session series it had **just pulled**. ⚠ **The series was right and
  the sentence was still false.** ⚠⚠ **"Pull the source before writing the superlative" IS NOT SUFFICIENT
  WHEN THE SOURCE HAS TWO BASES. New rule: NAME THE BASIS IN THE SENTENCE, or do not write the sentence.**
  ⚠ **(9) A COUNTER WHOSE *UNIT* IS WRONG.** Close journals reported §5.1–§5.4 untested for *"the Nth
  consecutive **SESSION**"* — **23, 26, 29, 33, 37 on consecutive trading days.** ⚠ **It increments by THREE
  OR FOUR per trading day; sessions increment by ONE. It is a RUN counter wearing a session label.**
  ⚠ **Re-running the check REPRODUCES THE SAME NUMBER — only the CALENDAR exposes it.** **Calendar figures
  re-derived from a 45-session `bars` pull on 09-29: 20 trading sessions since 2026-09-01, 17 AFTER the 09-03
  fill (18 inclusive), zero satellite positions ever. Do not restart the old series.**
  **(8) A MEASUREMENT PRESENTED AS A CALIBRATION:** the 09-25 midday *"volume tracks elapsed session time
  almost exactly."* ⚠ **The DENOMINATOR was a prior-day mean, and a ratio against one LOOKS like a
  measurement of the current day and is not one.**
  **(7) A MISCOUNT IN A VERIFICATION CLAIM:** the 09-24 close wrote it had *"verified all TWELVE keys."*
  ⚠ **There are THIRTEEN.**
  **(6) A SCOPE CLAIM:** *"routine 2 is the ONLY routine that runs with `is_open: true`"* — falsified by the
  run that read it. ⚠ **The most dangerous shape, because it was not a number to re-pull but a statement
  about the SYSTEM'S OWN SHAPE, which no data call would ever contradict.**
  **(5) A TRUNCATED SERIES (09-24):** the post-bell `current_price` record had silently dropped its own
  largest member. **(1)** A false superlative surviving three runs, caught **by accident** 09-21.
  **(2)** A stale count ("49 theses") caught deliberately 09-22, running in the direction that
  **understates** the problem. **(3)/(4)** Both halves of the `lastday_price` mechanism, asserted and
  falsified in turn.
  ⚠ **A superlative, count, mechanism, SERIES, CALIBRATION or BASIS inherited from a prior run is NOT a
  checked fact.** **Assume the next one you are handed is wrong until you have pulled the source — and then
  check which basis the source answered on.** *(09-29 recounted the thesis total from source twice: **80
  `### T-` headings less the template = 79**.)*

- **⚠ GNRC IS NOT YOURS TO LOOK AT — THIRTY-ONE CONSECUTIVE REFUSALS.** ⚠ **Graded honestly: the 09-30 open
  run made ZERO `move` and ZERO `quote` calls on GNRC, but it is an EXECUTION seat with no funnel and no BUY
  intent to validate, so the refusal was close to FREE — a WEAK instance, the same grade as the 09-29 close.** The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon
  announcement — first-order, outside §4 at any price** — and **open item (7) is resolved by a human editing
  §4 or `alpaca.py move`, not by a number this seat collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER
  EACH REFUSAL COST ANYTHING, AND MOST DID NOT. Quoting the bare count overstates the evidence.** The strong
  instances are the pre-market runs of 09-23, 09-24 and 09-25. ⚠ **No new costume in ten sessions; the list
  looks CONVERGING rather than growing.** Costumes: diligence, curiosity, tidiness, completeness,
  zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
  screen-already-running. **The pattern is the finding, not any instance. FREE IS NOT THE SAME AS
  PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FIFTY-NINE RUNS.** §5 exempts core from all four
  sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **09-29's CLOSE RUN IS THE STRONGEST INSTANCE THIS ITEM HAS EVER HAD, because it is the ONE SEAT THAT
  ACTUALLY WRITES MARKS and it was holding a complete, official 702.27 close at the moment it decided not to
  write one.** **Measure the core from the 706.74 fill and from an official close, never from a `positions`
  field** ⚠ **— and note that the fill price is a RAW print, so measuring it against an `--adjustment all`
  close MIXES BASES.** ⚠ **Noted honestly: this refusal is close to automatic, and automatic is not the same
  as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN IS
  USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell sees it
  pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with **no bar for
  today**. ⚠ **`is_open: TRUE` is the one case where the boolean alone is sufficient, and only because TRUE
  has a single meaning. FALSE has three.** ⚠ **THE STRONGER DISCRIMINATOR FOR A POST-BELL FALSE IS TO CHECK
  THAT A DAILY BAR FOR TODAY EXISTS — and to check its close against the 15:59 `latestTrade`.**
  *(09-29 16:16 did exactly that: `is_open: false`, `next_open: 2026-09-30T09:30`, a 2026-09-29 bar present
  with c 702.27, and a 15:59:57 ET `latestTrade` of 702.27. The post-bell shape, confirmed not assumed.)*
  ⚠ **But with `is_open: true` that same bar is PARTIAL and is not a close.**

- **⚠ EIGHT ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A NUMBER A
  RUN COLLECTS.**
  ⚠⚠ **(8) THE ONLY ONE THAT COULD MAKE §1 UNWINNABLE BY CONSTRUCTION: DOES THE PAPER ACCOUNT PAY
  DIVIDENDS?** VOO went ex-dividend 2026-09-28; `cash` still reads **exactly $30,000.00** at the 09-29 close.
  **A falsifiable test with a 2026-10-07 deadline is on the record.** ⚠ **AND SEPARATELY: whether the TOOLING
  should read closes on a stated basis by default is a human's call; 09-28 is the strongest evidence yet that
  it should.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — nine instances plus three near-misses;
  **there is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on the bill.
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM, AVAV, and
  **AKAM, the first MULTI-SESSION round trip.** Same root cause as (1), opposite direction. **The fix for
  (1), (2) and shape three is a human editing §4 or `alpaca.py move`** — the suggestion on record is to make
  it **read SIGN and causation, not loosen or remove the threshold.**
  **(3)** The satellite sleeve is **structurally undeployed — 79 theses, zero positions, ever.** A 70/30 cash
  book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits the cash and §4 says
  most runs end in no trade — both rules were followed, and the agent must NOT respond by lowering the §4
  bar.** **The binding constraint now has SIX known forms:** the source withholds the counterparty's number;
  **or** the counterparty discloses **roadmap instead of segment revenue**; **or** the named beneficiary is
  **vertically integrated**; **or** **both parties expressly refuse to disclose as a commercial choice**
  (GM); **or** **the figure is fully disclosed and is the WRONG QUANTITY** (JBL); **or** **THERE IS NO
  COUNTERPARTY AT ALL** (IOVA: own product, own facility, no external supplier named anywhere). ⚠ **Only the
  first two are addressable by widening the evidence bar. Forms three through six are not, and form five
  would be made WORSE by widening it.** ⚠ **ELMT is the standing proof that evidence is not the constraint.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the prior
  close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11.** ⚠ **Keep measuring it from
  the fill — and the fill is a RAW print.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it never
  had a stable size. ⚠ **A PRICE-SOURCE problem that contaminates every derived figure.** It has flipped the
  sign of a §2 quantity (09-24) and was caught INTRA-run on 09-29 at 09:35. ⚠ **09-28 added a SECOND,
  INDEPENDENT axis — `quote` vs `bars --adjustment all` on the SAME session — which is not a midpoint problem
  at all, and which AGREED on 09-29 only because no rescaling separated the two sessions.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed all
  five checks on 09-11 while `clock` returned 500, and on 09-24 while `perplexity.py` returned 500.
  ⚠ **AND IT PASSED ALL FIVE ON 09-28 AND 09-29 WHILE THREE OF 09-28's FOUR ROUTINES HAD PRODUCED NOTHING.
  A green pre-flight certifies THIS run's credentials, nothing about the schedule, the data plane, or whether
  the other routines ran.** **Probe by hand; CHECK EXIT CODES.**
  **(7)** **`alpaca.py move` cannot see an after-hours event, and neither can the 09:35 re-validation that
  exists to catch exactly this.** ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a trade.**
  ⚠ **AKAM generalises it: the blindness is to ANY event move the window later cancels.** **It has cost zero
  only because no plan has yet carried a BUY intent — an absence of exposure, not a mitigation.**
  Prior context in ClickUp `86bbv75bz`; week-prior `86bbzgbg3`. **09-25 daily summary: `86bc7vgbw`; 09-25
  weekly review: `86bc7vzam`; 09-28 daily summary: `86bc8yrz0`; 09-29 daily summary: `86bc9q3t5`.**

- **⚠⚠ WEEK 4 REVIEW (2026-09-25) — RAN, POSTED `86bc7vzam`. THE §1 ANSWER IS NO, AND EVERY WINDOW SAYS SO.**
  Satellite **0.0000%**, so its dollar-weighted excess is exactly **minus VOO's total return**: **−1.262pp
  week, −0.827pp since inception, −0.974pp 1M, −5.444pp 3M, −18.571pp rolling 12M.** ⚠ **Week 3's first three
  rows were POSITIVE. The market rose and the whole column inverted with NO rule change and no change in the
  sleeve. DO NOT RE-INHERIT THE PLEASANT VERSION; it was a property of a falling tape.** Structural cost now
  **~5.57pp per rolling 12M**, up from 4.97pp **because the BENCHMARK improved, not because the sleeve got
  worse.** **Reject board: 65 names, 20 beat VOO, 45 lagged, mean −2.04%, median −2.47%.** ⚠ **A tally, not a
  result.** **CRDO is the largest opportunity cost at +24.28pp**; HPE +20.67pp, MU +14.42pp, QCOM +13.11pp,
  LITE +11.16pp. ⚠ **Six of the top six excesses are ONE THEME (AI/data-centre hardware and semis) rejected
  under FIVE DIFFERENT §4 rules, every rejection individually correct.** ⚠ **A CORRECTION TO WEEK 3'S
  HEADLINE: it promoted the board's "widening" as the finding. Dispersion grows with elapsed time
  MECHANICALLY. The MEAN is the evidence.**
  ⚠ **FILE SIZE — THIRTEENTH CONSECUTIVE FLAG.** `research_log.md` **~350KB**, `journal.md` **~180KB** (grew
  this run), `state.md` **~50KB**, `weekly_review.md` **147KB**. ⚠ **THE 2026-10-02 REVIEW MOVES THE WHOLE
  SEPTEMBER CORPUS IN ONE DESIGNED OPERATION AND IS TWO SESSIONS AWAY (09-30, 10-01, then 10-02). Do not
  re-litigate this weekly; a human who disagrees should say so in `control.md`.**

- **⚠ A `#` IN A FENCED-BLOCK VALUE SILENTLY TRUNCATES IT.** `_parse_kv` in `scripts/common.py` does
  `line.split("#", 1)[0]`, so **everything after the first `#` in a `key: value` line is discarded by the
  parser.** ⚠ **STANDING CONSEQUENCE: never put a `#` in a fenced-block value, and VALIDATE `state.md` WITH
  `common.read_state()` AFTER REWRITING IT — writing the block and parsing the block are not the same
  check.**
  ⚠⚠ **AND ON 09-29 AT 09:35 THE TRAP ACTUALLY FIRED, FOR THE FIRST TIME ON RECORD — ON THIS SYSTEM'S OWN
  WRITE, NOT A HYPOTHETICAL.** The market-open run wrote a phrase containing a literal triple-hash into
  `last_run`, describing `positions.md`'s template, and `_parse_kv` **silently discarded everything from that
  point onward** — roughly **half the entry**, including the reconciliation result, the rebalance finding and
  the dividend check. ⚠ **The file on disk looked completely normal. Nothing errored. The only thing that
  exposed it was `common.read_state()` and printing the value's TAIL.**
  ⚠⚠ **THE LESSON IS SHARPER THAN THE OLD WARNING: THE `#` DOES NOT ARRIVE AS A COMMENT MARKER — IT ARRIVES
  INSIDE A MARKDOWN QUOTATION, WHICH IS EXACTLY WHAT A RUN DESCRIBING ITS OWN FILES WILL WRITE.**
  ⚠ **VALIDATING IS NOT ENOUGH; YOU MUST READ THE TAIL OF EVERY LONG VALUE BACK, because a truncated value
  parses cleanly and counts as one key. Key count did not change: 13 before, 13 after.**
  *(Done again at the 09-29 close: **13 keys**, no `#` anywhere in the block, and `last_run` / `prior_run`
  compared character-for-character against the file, tails included.)*

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** compared to **consensus** rather than to any prior company
figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations** (Centene, Southwest,
General Mills), **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence, Alcoa/South32, Nocera/E-PRO),
**a genuine transaction whose DELIVERY MILESTONE is recycled as the news** (GM/Lockheed), **a PRE-IPO
CONTRACT BOOK** (Nscale's $103B), and **a FORMAL PRESS RELEASE RESTATING AN ALREADY-FILED 8-K**
(Akamai/Anthropic). ⚠ **STANDING PRACTICE: ask a transaction WHEN IT HAPPENED before asking who it helps —
and WHEN THE SOURCES DISAGREE ON THE DATE, THE PRICE SERIES IS THE CHEAPER WITNESS.**
⚠⚠ **09-29 PRODUCED A CLEAN PASS AND A CLEAN FAILURE ONE ENTRY APART, FROM THE SAME QUERY, AND THE
DIFFERENCE IS THE WHOLE TEST: IOVA raised FY2026 guidance from ITS OWN prior $350–370M to $410–420M (PASS —
a company number against the same company's earlier number); AAR quoted 14–16% Q2 growth with NO PRIOR
RANGE ANYWHERE IN THE SOURCE (FAIL — whether that is a raise, a cut or a reiteration is not
establishable).** ⚠ **The test is cheap: did the source carry the company's OWN prior figure?**
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — and 09-29's AMRAAM chain would have
been its third appearance).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share," "the
only company that makes X" are facts about an **industry**, not a **transaction** — plus the **CEILING
sub-shape**. Costumes: a **table** (DoD daily contracts digest), a **consortium awardee** (Abrams), a bare
sentence, a **MULTIPLE-AWARD CEILING across fifteen vendors** (RDW's "$980M"), and an **UNNAMED SUPPLY BASE
made to look nameable by an exact figure and a named component category** ($1.7B of "memory components").
⚠⚠ **09-29 ADDS THE LARGEST INSTANCE YET: a $20,699,334,581 not-to-exceed AMRAAM award that NAMES FOUR
CONTRACT LINE CATEGORIES — "All Up Rounds, Guidance Sections, Direct Charge, FMS Offsets" — AND ALLOCATES
NONE OF IT TO ANY SUBCONTRACTOR.** ⚠ **The only supplier language in any source is "small and mid-sized
suppliers across the country."** ⚠ **A precise figure plus named COMPONENT CATEGORIES is the most fillable-
looking blank this funnel produces, because the industry answer (Aerojet Rocketdyne, now inside L3Harris) is
sitting right there in the reader's priors. THE SOURCE LEFT THE BLANK; FILLING IT IN IS NOT RESEARCH.**
⚠⚠ **09-30 ADDS THE CLEANEST INSTANCE THIS RULE WILL EVER GET, AND IT IS A DIFFERENT SHAPE: the F/A-XX funnel
did not merely find a blank — it ASKED WHETHER ONE EXISTED, and the source AFFIRMATIVELY STATED that no
US-listed supplier, subcontractor or partner has been named.** ⚠ **A volunteered absence is stronger evidence
than a silence, and it removes the last excuse for re-wording the query.** ⚠ **Two consecutive sessions of
defence awards dying here is now a STRUCTURAL finding about this funnel — see the carry-forward item.**
⚠ **And the priors were ready again: GE Aerospace, on the strength of the F414 and a press statement of
enthusiasm. The source closes that door explicitly.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.* Long-dated
energy offtake is **a standing feature of this funnel, not a visitor** — Sempra/Petrobras, Venture
Global/China Gas, Amazon/Generac, Centrus/Antares, Elmet/Tungsten West, NeoVolta/SK On. ⚠ **The REGULATORY
version: a non-binding advisory vote → an undated FDA decision → reimbursement → commercial ramp (ILMN) is
the same shape wearing a lab coat.** ⚠ **09-29 adds the CLINICAL-COLLABORATION version (SMMT/AZN on
ivonescimab) and the PENDING-DEFINITIVE-AGREEMENT version (CRK/SOCAR, where the PSA is not even signed).**
**Part 3 kills these in ONE step.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
⚠⚠ **09-29's IOVA IS THE CLEANEST INSTANCE ON RECORD and it killed the day's best rule (iii) pass: a
cell-therapy maker that manufactures Amtagvi itself and names no external CMO or supplier anywhere.**
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part 2.**
Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; Brookfield/Bloom's **$25B** is a
**FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**; SoftBank's **$11.1B** is **capital paid IN to a private
recipient**; Royal Caribbean's **~$3B** for Sandals is **capital paid OUT by the buyable leg**; BBY's only
disclosed economics was **Meta taking "a small fee" — a COST at the candidate, described in language that
reads like a partnership benefit**; FMC/Tessenderlo's **$403M is a SECONDARY-MARKET SHARE PURCHASE.**
⚠ **09-29 ADDS TWO MORE, BOTH CAPITAL PAID IN: AstraZeneca's $2.0B for Summit CONVERTIBLE PREFERRED (equity
issuance — it DILUTES rather than earns) and SOCAR's $1.65B into Comstock's Haynesville (and the paying leg
is a state oil company that cannot be bought).**
⚠⚠ **09-30 ADDS A COSTUME NOT SEEN BEFORE IN THIS DRESS: A MISS AGAINST CONSENSUS.** Cigna guided FY2026
revenue to **~$280.0B against a $287.2B consensus** — **a $7.2B gap that belongs to NOBODY.** ⚠ **It is the
most seductive form of this error precisely because it arrives as two exact figures and a clean subtraction,
so it LOOKS like the quantified dollar path part 2 asks for.** ⚠ **It is not revenue at any Company B, and it
is not even Cigna's revenue declining — it is Cigna's revenue growing less than strangers expected.** ⚠ **Note
the overlap with rule (iii), whose most prolific costume is a guidance ISSUANCE measured against CONSENSUS
rather than against the company's own prior figure: the same sentence can fail both rules at once.**
⚠⚠ **AND THE DEFINITIVE INSTANCE, JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K — AND IT
IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A disclosed
statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.** ⚠ **A large,
real, sourced, prominently-placed number is not a dollar path. THIS IS THE WORKED EXAMPLE TO REACH FOR
FIRST.** T-2026-09-18-04 (BLK) remains the other: **part 1 passed cleanly and it died on the absent segment
figure, NOT on size.**

**⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT WORKS IN BOTH SIGNS.** Two companies moving on the same macro
input (a crush spread, a mortgage rate, a rate decision) is a **market**, not a **transaction**, and the
giveaway is that part 1 needs an *"and also"* clause. ⚠ **A DIVERGENCE between two named companies sounds
causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge and ADM) — and the convergent version is MORE DANGEROUS,
because agreement LOOKS LIKE CORROBORATION when it is in fact the clearest possible statement that the input
is a market variable.** ⚠ **The third and most respectable face is a COMPETITOR'S EARNINGS PRINT**
(AutoZone's FQ4 read across to GPC/ORLY/LKQ). **The giveaway never changes: the sentence needed an "and
also".** ⚠ **09-29's CRK/SOCAR is the CAPITAL-EXPENDITURE face: "an investment funds drilling AND ALSO some
unnamed service company wins the work."**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — AND IT IS THE MOST CONVINCING NON-EVENT THE FUNNEL PRODUCES.**
⚠ **This is the FOMC object — an environment input — but in a far more persuasive costume: a policy action
is SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN AFFECTED INDUSTRY, and MOVES THE TAPE ON THE DAY.** It
nonetheless has **ONE party.** ⚠ **A long-only book cannot trade money being WITHDRAWN from a sector unless
some NAMED party receives it — and nobody does.** ⚠⚠ **09-29 SUPPLIES THE NEWEST AND MOST SEDUCTIVE COSTUME:
A MARKET-IMPLIED PROBABILITY THAT MOVED.** CME FedWatch went from ~57% to **~70%** odds of an October hike
in a week, alongside the 10-year at ~5.25% and the 30-year at ~5.56–5.57%. ⚠ **A probability that CHANGED
reads like an event with a date, which is exactly why it is more tempting than a bare yield level. It is the
same object: no named recipient, no transaction, one party.** ⚠ **SCALE MAKES IT MORE CONVINCING, NOT LESS.
Every "who wins from higher rates / higher oil" answer needs an "and also".** ⚠ **The counter-case still
stands and must not be over-applied against: an FDA advisory vote (ILMN/GRAIL) ENABLES a named company's
product and that company has a named supplier — a real two-party chain. Do not over-apply this rule to
approvals.**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is **exits-only by
construction** and may not open a position under **any** circumstance. Routine 2 executes **only what
`plan_today.md` already contains** — a position opened at 09:35 without a plan entry routes **around** the
discipline rather than satisfying it. Routine 4 **RECORDS AND JOURNALS; IT DOES NOT TRADE.** ⚠ **Idle cash,
an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an opportunity any of those seats may act on** —
⚠ **and neither is a green day that still lags the benchmark.** New positions route through pre-market
research **plus** the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT THE
SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.** The gate
has now been exercised **THIRTY times and has never fired** *(09-30 09:35: `plan_date` 2026-09-30 against an
ET date of 2026-09-30 **computed, not assumed** — **FRESH**, so the gate correctly did nothing and no alert
was due)*, and its alert path **remains untested code.**
⚠⚠ **AND 09-30's OPEN RUN IS THE SHARPEST ILLUSTRATION OF THE ITEM ITSELF: the plan was FRESH and EMPTY, so
the run placed zero orders — the EXACT order count a stale plan would have produced. Nothing in the fills,
the ledger or the sleeve percentages distinguishes the two. ONLY `plan_date` DOES.** ⚠⚠ **AND 09-28 WAS THE MORNING IT WOULD FINALLY HAVE FIRED — `plan_today.md` genuinely carried
`plan_date: 2026-09-25` — AND THE RUN CONTAINING THE GATE DID NOT EXECUTE. The prediction was right about
the setup and the test STILL DID NOT HAPPEN.** ⚠ **Twenty-eight quiet opens are NOT evidence it works. The
first morning it fires will by construction be a morning when the pre-market run failed — i.e. exactly the
morning with no fresh notes to lean on. Read routine 2's Step 2 then; do not recall it.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a broker mark
on one leg against an official close on the other. **Both legs from the same source, and for returns that
source is `bars --adjustment all`** ⚠ **— on a COMPLETED session.** ⚠ **And state WHICH basis produced any
figure you quote.** ⚠ **09-28 showed the rule is NECESSARY BUT NOT SUFFICIENT: two legs can both come from
`bars --adjustment all` and still be incomparable, when the ACCOUNT and the BENCHMARK recognise the same
cash on different dates.**

### Do not reach for these — disposed rejects and the trap in each

⚠ **Added 09-30:** **F/A-XX supplier chain** — ⚠ **rule (v)'s cleanest instance yet, because the source was
asked DIRECTLY and answered that no US-listed supplier, subcontractor or partner has been named.** Boeing is
first-order. ⚠⚠ **DO NOT FILL THE BLANK WITH GE AEROSPACE. The F414 on the F/A-18 is a fact about the PAST,
and GE's "excited to see this program advance" is a press statement, not a workshare — the source says
explicitly that GE "should not be counted as a publicly named F/A-XX supplier."** **Ultium Cells prismatic
LMR chain** — no US-listed supplier named; **retrofit completes 2028**, so part 3 kills it even if one is
named later; ⚠ **the source volunteered LG Chem / Redwood / Cirba AND warned they must not be attributed to
this program — that is a warning, not a shopping list**, and all three fail §3 anyway (Korean-listed,
private, private). **CFS / Fujikura HTS tape** — **§3 outright: Commonwealth Fusion is PRIVATE and Fujikura is
TOKYO-LISTED**; Fujikura is also first-order; **price expressly undisclosed**, and 10,000 km is a VOLUME not a
revenue figure. ⚠ **AMSC is not the way in: it is a competitor that did NOT win this order, and it is far
below the §3 floor.** **ABBV** — ⚠ **the second-most-important entry on this board, beside JBL: the ONLY
candidate ever logged that was both source-named AND §3-eligible, killed by part 2 alone.** An **unexercised
option** on a single dry-eye asset cannot reach 10% of AbbVie's revenue, and no dollar figure is disclosed.
⚠ **Do not reach for it if the appeal succeeds — the materiality ceiling does not move.** **RARE** —
**§3 outright, market cap $1.42B against a $10B floor** (CompaniesMarketCap 09-28, corroborated by Trefis and
Yahoo). ⚠ **A §3-FIRST SUCCESS: the cap was pulled BEFORE the thesis was elaborated, which is why no effort
went into a story a single number was always going to end.** **LLY / GLP-1 injectable chain** — part 3, the
**BLA is planned for Q1 2027**; ⚠ **and West Pharmaceutical was SELF-SUPPLIED from priors and never queried —
declining to ask is the correct action once the candidate is known to be self-supplied.** **The
pharmaceutical-tariff complex** — environment input, ONE party, no figure, and the tariffs are only
**potential**. **CI (Cigna)** — ⚠ **a NEW COSTUME for rule (viii): a $280.0B guide against a $287.2B
consensus. A consensus miss LOOKS quantitative — two precise figures and a clean subtraction — and it is the
purest form of a number that belongs to NOBODY.** No stated cause, therefore no causal path, therefore no
second party. **HII** ($5.1B Truman refuelling, prime is first-order, no subcontractor named) · **Petrobras /
Cheniere** (0.8 mtpa over 22 years, Cheniere is the direct counterparty and the volume is immaterial against
its capacity) · **TOYO** (second consecutive session, customers still unnamed, §3) · **Avio USA** (Italian
parent, no offtake counterparty, **production begins 2029**) · **Attalon** (~$13M, no counterparty) ·
**Lyntris** (first-order, no value disclosed, orders under a **2023** agreement so rule (iii) cannot clear) ·
**Tesla** ($30B of credit lines — a financing ceiling available to Tesla itself) · **the AI self-governance
accord** (signatories not enumerated, no cost quantified) · **Carnival / Vail / CarMax** (⚠ **earnings prints;
the only figures disclosed are the company's OWN lines, and a competitor reading across is a COMPARABLE, not
a second-order catalyst**).

⚠ **Added 09-29:** **AMRAAM component suppliers** — ⚠ **rule (v)'s largest instance: $20.7B, four named
CONTRACT LINE CATEGORIES, and not one subcontractor named or allocated a dollar.** RTX is first-order. **Do
not fill the blank from priors; "Aerojet Rocketdyne / L3Harris" is an industry answer, not a disclosure —
and LHX would be its THIRD appearance in this log (rule iv).** **IOVA** — ⚠ **the best rule (iii) pass in
weeks, killed by rule (vii): Iovance makes Amtagvi itself and names no external supplier. A SIXTH form of
open item (3) — no counterparty exists at all, so no widening of the evidence bar reaches it.** **SMMT /
AstraZeneca** — the $2.0B is **capital paid IN for convertible preferred** (rule viii); SMMT is first-order;
a clinical collaboration is years, not quarters (rule vi). **CRK / SOCAR** — $1.65B **capital paid in** by a
**non-US-listed state oil company**; the second-order sentence needs an **"and also"**; the PSA is not even
signed. **AIR / MRO Holdings** — the only Company B is **private**, and **AAR's own prior guidance is absent
from the sources, so rule (iii) cannot be cleared in either direction.** **The rate / Fed-repricing
complex** — ⚠ **environment input, ONE party; a probability that MOVED (57% → 70%) is the most seductive
costume yet and changes nothing.** **TOYO** ($240M, customers unnamed) · **Megaport** (A$978.6M,
counterparties unnamed, ASX-listed) · **Draganfly / Unusual Machines** (microcaps, co-investor unnamed) ·
**Uniserve** ("an enterprise client", ~$3.15M) · **Newgen Software** ("a US-based health insurer", $5.475M,
Indian-listed) · **Exascale Labs** ($14.8M revenue, §3) · **Uranium Energy Corp** (a clean rule (iii) pass
with **no second party anywhere in the disclosure**) · **Sangoma** (Canadian; purchaser, value and terms all
undisclosed).

⚠ **Added 09-25:** **JBL** — ⚠ **the most important entry on this board.** Part 1 passes **cleanly**, every
party is named, the instrument is signed and filed, and the figure is **$1.7 billion in an 8-K** — **and
part 2 fails outright**, because the money is Akamai's, the components are held **in consignment as bailee**,
and the repurchase is **expressly at cost**. ⚠ **Do not reach for this at a lower price; the price was never
the problem.** **AKAM** — **first-order**; and its `priced_in: false` at +3.19% is an **artefact of a +12.35%
jump and a −6.74% give-back inside one window**, ⚠ **NOT a clean pass.** **Memory suppliers to the Akamai
build** — **no manufacturer named in any disclosure**, rule (v). **Lenovo** — **§3 outright**, HK-listed with
only an OTC ADR. **RDW** — the **$980M is a multiple-award CEILING across 15 vendors**; first-order; below
the §3 floor. **FLNC / EVE Power** — **no value or volume disclosed**; EVE is Shenzhen-listed. **FMC /
Tessenderlo** ($403M **secondary share purchase**) · **LLY / InnoCare** (no value disclosed) · **NOC
$123.8M, RTX $50.1M, Stark $114.0M, Southern $22.0M, RGAS $23.6M** (DoD digest, rule (v)) · **Blue Cloud
Softech / IBM** (Indian-listed) · **FingerMotion** (offtakers unnamed) · **Everforth, Endovia, Algorhythm**
(private or microcap) · **Amazon's $100M Greenwood plant** (immaterial) · **Welspun** (§3, buyer unnamed).

⚠ **ELMT — DO NOT SCREEN IT AGAIN.** It entered this funnel **three times in three sessions** and the third
time carried a **disclosed price ($124.75M)** — exactly the material whose absence killed the first two.
⚠ **"But now there is a number" is the purest form of the pull to re-open a §3 kill on evidence §3 does not
weigh. A microcap with a Vietnam-listed counterparty is ineligible at every price and at every level of
disclosure.**

⚠ **Earlier disposed rejects (09-21 to 09-24) remain disposed and are NOT re-listed here.** **ILMN, GRAL,
BBY, PYPL, SHOP, SoftBank/OpenAI, GIS, LH, CNC/MOH/OSCR, LHX, GFS, ACN, GPC/ORLY/LKQ, GM, BE, BG** — see
`research_log.md` for the working on each. **A rejection is not a queue.**
