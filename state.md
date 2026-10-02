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
last_run: 2026-10-02 08:23 ET 1-premarket-research (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99865.29 at pre-flight 08:23; PRE-MARKET SHAPE CONFIRMED FROM THE DATE NOT THE BOOLEAN - clock 08:23:38 is_open FALSE with next_open 2026-10-02T09:30 pointing at TODAY, plus a complete 2026-10-01 bar and NO bar dated 2026-10-02, so this is not a holiday and not post-bell; NO ORDERS - a pre-market seat places none by design; RECONCILIATION CLEAN, one core row against zero satellite blocks, compared satellite-to-satellite; FOUR PERPLEXITY SCANS all exit 0, FIVE THESES WRITTEN AND ALL FIVE REJECTED, bringing the log to 98 real theses and ZERO EVER ACCEPTED; PLAN FOR 2026-10-02 WRITTEN AND DELIBERATELY EMPTY - no BUY, no SELL, no REBALANCE, and EVERY GATE WAS OPEN (breaker INACTIVE, week 0 of 3, sleeve empty, 30.04 pct idle cash, 4992.82 of headroom under the 5 pct cap, control notes none, TRADING_ENABLED true) so the emptiness is a RESULT not a block; THE DEFENCE-AWARD FINDING TOOK A FOURTH INSTANCE ACROSS THREE PRIMES - RTX SM-6 24.4B, one funnel query spent, the familiar volunteered absence returned, NO RE-QUERY ISSUED and the priors not written; TWO NEW SHAPES RECORDED - a transaction in CAPACITY ALREADY BUILT has no second tier to benefit (ORCL/Tencent lease), and AN EARNINGS MISS IS NOT A SECOND-ORDER CATALYST because it improves nobody's economics in any disclosed way (Nike); ONE SELF-CORRECTION RUNNING THE UNUSUAL DIRECTION - the reflex was to flag Micron's 54.23B quarter as corrupt source data and that rested on a STALE PRE-2026 PRIOR which MU at about 1070 per share already overruns, so the figures were recorded as reported and NOT disputed; ZERO move CALLS, an ABSENT check not a skipped one, second instance after 09-29; MU DELIBERATELY NOT RE-SCREENED, zero queries on the memory chain, AMAT/LRCX/KLA again not written; sell_rule_status written as ABSENT NOT PASSING for all four rules with distances UNDEFINED; session counter NOT advanced - 22/19 holds because today is not a completed session, catch 11 declined from the clock in one of the two seats it names; SIXTY-FIFTH refusal to stamp highest_close on core, graded FREE because this seat does not write marks; WEEK ROLLOVER NOT DUE - week_of 2026-09-28 equals this ISO week's Monday; cash EXACTLY 30000.00 for a FOURTEENTH reading, dividend DAY 5 OF 8; breaker INACTIVE, consecutive_closed_losses 0)

prior_run: 2026-10-01 16:16 ET 4-market-close-journal (selftest PASSED all five, trading_enabled true, LIVE paper; A FULL SESSION HAPPENED AND ZERO ORDERS WERE PLACED BY ANY OF THE DAY'S FOUR RUNS - zero fills, nothing opened, nothing closed, no realised P and L; POST-BELL CONFIRMED FROM DATES NOT THE BOOLEAN; OFFICIAL CLOSE BASIS bars --adjustment all VOO c 702.255 - equity 99555.77, core 69555.77 = 69.8661 pct, cash 30.1339 pct, day PLUS 163.43 / PLUS 0.1644 pct, since inception MINUS 444.23 / MINUS 0.4442 pct, total-return basis carrying the INFERRED 180.45 receivable about 99736.22 / MINUS 0.2638 pct; STEP 2 HIGH-WATER WRITE HAD NO OPERAND FOR A FIFTH CONSECUTIVE CLOSE RUN and the sentence it first reached for would have been FALSE; SECTION 1 SEPARATION 19 OF 19 with residual EXACTLY 0.00E+00 and the sign FLIPPED NEGATIVE, the same structural fact not a change in quality; the n/v FLOOR TEST got its first post-bell application and passed by only 12.6 pct, a CORROBORANT not a validation)

week_of: 2026-09-28
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.96
satellite_pct: 0.0
cash_pct: 30.04
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on forty-six times, and this run did a LARGE collapse.** This repo's
only continuity mechanism is the next run *reading* these files, and padding them with restatements raises
the odds a genuinely live item gets skimmed. **Carry-forward is defined as cleared once acted on.**
⚠ **This run compressed the Live section substantially: repeated emphasis was removed, and NOTHING LIVE WAS
DISCARDED. Where an item had accumulated three statements of the same fact, one survives.** ⚠ **A run that
adds nothing to this list is the normal case, not a gap in attention.** ⚠ **A correction REPLACES the claim
it corrects — it does not sit beside it.**

**What the 08:23 PRE-MARKET run of 10-02 adds:** **two new §4 structural shapes** (capacity-already-built;
earnings-miss), **a fourth defence-award instance**, **a second instance of the non-immutable `n`/`v` bar**,
**a second declined pre-market/post-bell basis trap**, and **one self-correction that runs the opposite way
from every other catch on this board** — the reflex to dismiss a real event because an inherited sense of a
company's scale was stale.

---

### Live — act on these

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. DAY 5 OF 8. CHECK `cash` EVERY RUN UNTIL IT RESOLVES.**
  `cash` read **exactly $30,000.00** again at **10-02 08:23** — a **fourteenth** reading, across the
  **fifth calendar day**. ⚠ **Fourteen readings across five days are ONE unresolved observation of an
  unpaid dividend, not fourteen data points.** ⚠ **NON-ARRIVAL THIS EARLY IS EXPECTED, NOT EVIDENCE —
  settlement runs on the PAY date, not the ex-date, and no reading's HOUR makes it stronger, because
  settlement does not run on the bell.** ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE AND STILL RUNNING:
  `cash` should rise to about $30,180.45. IF IT HAS NOT BY 2026-10-07, the paper account does not model
  dividends at all — in which case the book structurally under-earns its own benchmark by VOO's entire
  ~1.0% annual yield and §1's "beat the S&P TOTAL RETURN" is unwinnable BY CONSTRUCTION rather than by
  strategy.** ⚠ **That is a finding for the human, not something to fix from any seat.** The implied credit
  of **$180.26–$180.64** is an **INFERENCE** — Alpaca does not publish the figure — and must stay labelled
  as one.

- **⚠⚠ STEP 2 HAVING NO OPERAND AND STEP 2 WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT A RUN PRODUCES.**
  The close routine's headline invisible job is to stamp each open satellite position's official close into
  `highest_close`; routine 3's Step 2 is the seat that **DETECTS** a missed write and backfills it.
  **Five consecutive close runs have had nothing to stamp, and the sentence each first reached for —
  "high-water marks updated" — would have been FALSE. The honest form is: the job had NO OPERAND.**
  ⚠ **10-01 is the sharpest form on record because the seat held a complete, verified official close of
  702.255 at the moment it had nothing to stamp it onto.** ⚠⚠ **A SECOND DISCIPLINE ALSO PRODUCES NO
  ARTIFACT, AND THIS IS THE PART A FUTURE RUN WILL MISREAD: the routine says update the `(as of …)` date
  every day whether or not the value moves, precisely so a current mark is distinguishable from a skipped
  one. THERE IS NO FIELD, SO THERE IS NO DATE, SO THAT RULE HAS NOTHING TO WRITE EITHER.**
  ⚠⚠ **AND THE DETECTING SEAT IS IN THE SAME STATE: its entire input is an `(as of …)` date compared
  against the last trading day. No field, no date, so NO STALENESS COULD BE DETECTED AND NONE WAS RULED
  OUT. A detector handed no input returns the same silence as a detector finding everything healthy.**
  ⚠⚠ **BOTH THE WRITING SEAT AND THE DETECTING SEAT HAVE A CONFIRMED BLIND SPOT OF EXACTLY THE SAME SHAPE,
  NEITHER HAS EVER RUN AGAINST A REAL MARK, AND THE FIRST SATELLITE FILL ARMS BOTH AT ONCE.**
  ⚠ **THE BACKFILL PATH REMAINS UNEXERCISED CODE** — re-pull the window on a stated adjustment basis, take
  the max from that ONE pull. **09-28 proves that is not academic: that day lost its close run, so with one
  satellite position open, 09-29's midday run would have had to backfill ACROSS AN EX-DIVIDEND DATE, which
  this system has never done.** **The cost has been zero because the sleeve is empty. That is luck, not a
  control.** ⚠ **DO NOT BACKFILL ANYTHING NOW — there is no field, so there was nothing to write.**
  ⚠ **When it arms: no backfill may take its max from a bar dated TODAY while the market is open, nor from
  a different adjustment basis than the one it is compared against.** ⚠ **After the first fill, a mark
  silently not written reads identically to a mark correctly unchanged, and ONLY the `(as of …)` date
  separates them. COMPARE THE DATE; NEVER INFER FROM THE FIELD'S EMPTINESS.**
  **§5.1–§5.4 have never had an operand in this account's history: 22 completed sessions since 2026-09-01,
  19 after the 09-03 core fill, zero satellite positions ever.** ⚠ **10-02's pre-market seat DECLINED the
  increment correctly, from the CLOCK — catch (11) names routines 1 and 2 as the exposed seats, and a
  correct number reached by an unchecked route is not a checked fact (catch 6).**

- **⚠⚠ EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
  VOO went ex-dividend 09-28; `bars --adjustment all` rescaled every prior close by **0.997432**;
  `--adjustment raw` and `--adjustment split` return the original series to the cent. **Both series are
  correct; they are different bases.** ⚠ **09-28 onward agree to the cent on both bases — the divergence is
  entirely in the sessions BEFORE the ex-date.** **Raw, pre-ex:** 09-25 710.705, 09-24 707.28, 09-23
  707.28, 09-22 712.69, 09-21 712.76, 09-18 701.85. **`--adjustment all`, same sessions:** 708.88 / 705.47 /
  705.47 / 710.86 / 710.93 / 700.05. ⚠ **The 09-03 core fill at 706.74 is a RAW print; measuring it against
  an `--adjustment all` close MIXES BASES.** ⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE
  SENTENCE.**
  ⚠⚠ **§5.4 IS THE REAL CASUALTY AND IT FAILS TOWARD SELLING** — a `highest_close` stamped before an
  ex-date and compared against a post-ex adjusted close manufactures a **phantom drawdown equal to the
  dividend** (0.257% on 09-28). **THE FIX IS WRITTEN INTO `positions.md`'s HEADER: same basis, same call,
  re-pull the whole window and take the max from that one pull.** ⚠ **The empty sleeve is the only reason
  this has cost nothing.** **`voo_close_at_entry` is a LABEL, not a baseline.**
  ⚠ **The SECOND price-source axis — `quote`'s `prevDailyBar` vs `bars --adjustment all` on the same
  session — AGREED on 09-29 and after, and THAT IS NOT THE DEFECT RESOLVING: the 09-28 disagreement came
  from ex-dividend rescaling, and with no rescaling between the sessions there is nothing to disagree
  about. An agreement obtained by removing the cause teaches nothing about the cause. DO NOT REPORT THE
  AXIS AS CLOSED.**
  ⚠ **A historical BOOK day-return is not exactly reproducible from a later `--adjustment all` pull once an
  ex-date intervenes (~0.001pp; the cash leg does not rescale, and published rescaled closes are rounded).
  Friday's review will differ from the dailies in the FOURTH DECIMAL and NEITHER IS WRONG — a day-return
  must be quoted with its BASIS *and* its VINTAGE.** ⚠ **§5.4 is unaffected: it compares two numbers from
  the SAME pull, which is exactly why the rule is written as same-basis-same-call.**

- **⚠⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.
  TWO ROUTINES CAN PULL ONE: routine 2 at 09:35 and routine 3 at 12:30.**
  ⚠ **THE PRICE HALF IS CONFIRMED AND IT IS THE DANGEROUS HALF, WITH THE MECHANISM NOW VISIBLE RATHER THAN
  SUSPECTED:** at 12:41 on 10-01 the partial bar read **`c` 700.35 = `latestTrade.p` 700.35 to the cent.**
  **A PARTIAL BAR'S CLOSE FIELD IS THE LAST TRADE SO FAR WEARING A CLOSE'S CLOTHES**, and it is a wholly
  plausible price carrying no warning of any kind (26 cents from the prior official close, mid-range against
  a 691.44–710.93 band). **A §5.4 mark stamped from it records an intraday print as a high-water close and
  silently moves the stop.** ⚠ **NO `bars` CLOSE MAY BE STAMPED AS A MARK BEFORE THE BELL ON ANY BASIS.**
  ⚠ **THE `n`/`v` HALF IS REFUTED AS STATED AND REPLACED BY A FLOOR TEST — AND THE FLOOR TEST IS NOW KNOWN
  TO BE BUILT ON A MOVING RULER.** The 12:41 partial's n 982 / v 26,215 were **47.8%/43.0%** of the prior
  completed bar — **not "visibly tiny"**, so a glance would not have caught it; but they sat **below the
  trailing completed-session minimum on both fields** (floors 1,450 / 43,730). **The usable test is "is `n`
  below the trailing completed-session MINIMUM", a comparison against a distribution, not a glance.**
  ⚠ **Its first application to a bar believed COMPLETE passed by only 12.6% (`v` 18.7%) where the same day's
  partial sat 32.3% BELOW — the populations did not overlap, but the complete-side clearance is LESS THAN
  HALF the partial-side, so a quiet, low-participation FULL session could land under the floor without being
  partial at all. A CORROBORATING INSTANCE, NOT A VALIDATION.**
  ⚠⚠ **AND THE FLOOR TEST'S OWN INPUTS DRIFT: A COMPLETED DAILY BAR IS NOT IMMUTABLE IN `n` AND `v`. TWO
  CLEAN INSTANCES NOW.** 09-30's bar read n 2050/v 61014 then n 2053/v 61032; **10-01's read n 1633/v 51892
  at the close run and n 1634/v 51893 on 10-02's fresh pull — both times the CLOSE held to the cent.**
  Late-reported prints keep arriving after the bell. ⚠ **So `n`/`v` are weaker than a smell test: they are
  not even STABLE on a complete bar, and no run may use "v is low" or "v changed" as evidence in either
  direction.** ⚠ **STATED LIMIT, STILL UNTESTED AND FALSIFIABLE: the floor test MUST FAIL on a half-day
  session (day after Thanksgiving, Christmas Eve), where a COMPLETED bar legitimately carries roughly half
  the usual `n`/`v`. The next early close is the test.**
  ⚠⚠ **THE CLOCK REMAINS THE ONLY SOUND DISCRIMINATOR. The floor test is a corroborant, never the primary.**
  ⚠ **And low volume is not evidence of a partial bar any more than high volume is evidence of a complete
  one — 09-28 printed v 62,354 against Friday's 164,725 and is COMPLETE (`feed=iex` returns one venue's
  slice); 09-29 printed v 101,166, above 09-28's complete figure, and is ALSO complete.**
  ⚠ **The trap is usually MILD, which is the uncomfortable half — the 09-25 midday partial was fifteen cents
  off the official close. A loud warning whose observed instances are all mild teaches a future run that the
  shortcut is safe. It is not safe on a day with a 2% afternoon reversal.**

- **⚠ THE 09-28 GAP — CLOSED AS AN ONGOING FAILURE, STILL OPEN AS A QUESTION FOR THE HUMAN.**
  Three of four routines left **no committed output on 2026-09-28**. ⚠⚠ **A ONE-DAY, THREE-ROUTINE gap —
  all four routines committed on 09-29, 09-30 and 10-01, re-verified from `git log` on 10-02 (the 10-01
  close is `ffacda0`). It must NOT be reported as an ongoing failure.** ⚠ **The cause is not visible from
  inside a run and is NOT asserted.**
  ⚠⚠ **THE COST WAS ZERO TWICE OVER AND THAT IS LUCK: an empty sleeve gave routine 3 nothing to manage, an
  empty plan gave routine 2 nothing to execute. On a day with an open satellite position, a missing routine
  3 is an UNMANAGED §5 BOOK for a full session, and a missing routine 4 is a `highest_close` that never got
  written.**
  ⚠⚠ **AND THE GAP DESTROYED A PIECE OF EVIDENCE: 09-28 was the FIRST morning with a genuinely stale
  `plan_today.md` — word for word the setup the staleness gate had been waiting for — and the gate was not
  reached, because the run containing it did not execute. THE GATE REMAINS UNTESTED CODE; the 10-01 open
  exercised it for the thirty-first time and it did NOT fire, so its alert path is still never-run code.**
  ⚠⚠ **AND THE REASON IT MATTERS, LIVE AGAIN TODAY: A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A
  BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. 10-02's plan is fresh (`plan_date: 2026-10-02`) and deliberately
  empty. FRESHNESS MUST BE READ OFF `plan_date` AND NEVER INFERRED FROM THE OUTCOME.**

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD, AND THAT IS A RESULT RATHER THAN
  AN EMPTY SEARCH. FOUR SESSIONS IN FIVE NOW.** 09-29: four of five names returned *"No other company's
  revenue or costs are identified as directly affected in the available source material."* 09-30: the F/A-XX
  funnel **asked directly** and was told none had been named. 10-01: the Micron capex funnel got
  *"…Naming companies such as equipment manufacturers, engineering contractors, or materials suppliers
  based only on industry fit would be an inference, not an explicit source linkage."* **10-02: the SM-6
  funnel returned the same shape verbatim — *"Any attribution of SM-6 revenue to other defense companies
  would be an inference rather than a disclosed allocation"* — and the Tencent/Oracle funnel independently
  returned *"no such additional supplier has been publicly identified."***
  ⚠ **That is not an under-searched funnel. It is the source volunteering the absence of a Company B, and
  in three of the four cases volunteering the EPISTEMIC RULE as well.**
  ⚠⚠ **A run that then produces one has supplied it from its own priors, which is verbatim the failure §4's
  honest-broker paragraph describes. THE PRIORS ARE ALWAYS READY AND ALWAYS SPECIFIC** — Applied Materials,
  Lam Research and KLA for Micron; solid rocket motors and the Mk 72 booster for SM-6; the GPU vendor for
  any AI-compute headline. ⚠ **Each is a fact about the INDUSTRY, not about the TRANSACTION. Recognise this
  shape on sight: when the source says no counterparty is identified, the correct next action is to WRITE
  THAT DOWN, not to go looking for one in a differently-worded query. NO RE-QUERY HAS BEEN ISSUED ON ANY OF
  THE FOUR OCCASIONS.**

- **⚠⚠ US DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE — FOUR INSTANCES ACROSS THREE PRIMES, THREE
  PROGRAMS AND TWO SERVICES. TREAT IT AS SETTLED.**
  **09-29: $20.7B AMRAAM multiyear to RTX** — four named CONTRACT LINE CATEGORIES, not one subcontractor
  named or allocated a dollar. **09-30: >$20B F/A-XX full-scale development to Boeing** — the funnel asked
  DIRECTLY and the source answered that none had been named. **10-02: up to $24.4B SM-6 multiyear to
  RTX/Raytheon** — five years plus two option years, **quantities and delivery schedules expressly not
  specified**, the **$24.4B a MAXIMUM POTENTIAL value and not an amount reported as obligated**, and no
  supplier named or allocated anything.
  ⚠⚠ **THE MECHANISM IS DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below it is
  commercially confidential, so the dollars are never allocated to a named public company.**
  ⚠ **CONSEQUENCE FOR A FUTURE RUN: when a defence award appears in the 5a scan, expect this outcome. It is
  still worth ONE funnel query — the exception would be enormously valuable and the query is cheap — but a
  run that gets the now-familiar answer must WRITE IT DOWN AND STOP, not re-word the query.** ⚠ **10-01 and
  10-02 both acted on this item as written: 10-01 issued ZERO queries on the still-live F/A-XX award, and
  10-02 spent exactly ONE on SM-6 and did not re-query.** ⚠ **The prime itself is FIRST-ORDER and outside §4
  at any price. RTX has now appeared twice in five sessions — rule (iv), a recurring ticker is a warning,
  not corroboration.**

- **⚠⚠ TWO NEW §4 STRUCTURAL SHAPES FROM 10-02. BOTH ARE RECOGNITION RULES, AND BOTH ARE GRADED AS SINGLE
  INSTANCES RATHER THAN PATTERNS.**
  **(a) A TRANSACTION IN CAPACITY ALREADY BUILT HAS NO SECOND TIER TO BENEFIT.** Tencent leased access to
  **~100,000 AI chips ALREADY INSTALLED** in Oracle's Southeast Asia data centers, five years, **~$7B
  estimated, ~30% upfront.** ⚠ **A lease of EXISTING hardware generates NO new downstream procurement, so
  there is no supplier whose revenue line changes — whether or not anyone names one.** It resembles form six
  (no counterparty at all) but the mechanism differs: a second tier conceptually exists and the transaction
  simply does not touch it. ⚠ **CONSEQUENCE: AI-compute *lease* and *capacity-access* headlines are
  structurally weaker §4 material than *build* or *procurement* headlines, AND THE TWO READ ALMOST
  IDENTICALLY IN A NEWS SCAN.** ⚠ **Note the independent second kill: the ~$7B is a REPORTED ESTIMATE from
  unnamed sources with neither party commenting. An unconfirmed press figure may not carry part 2.**
  **(b) AN EARNINGS MISS IS NOT A SECOND-ORDER CATALYST.** Nike missed FQ1 (revenue $11.2B, Greater China
  −12%, NA direct −8%, wholesale $6.8B −1%). ⚠ **§4's structure is "A's news IMPROVES B's economics," and a
  competitor's disappointment improves nobody's economics in any disclosed, dateable way — it only invites a
  share-shift story THE READER SUPPLIES.** The mechanism sentence needs a second clause ("and the share went
  to *them*, rather than to a shrinking category, private label, or a non-US-listed rival"). ⚠ **And the
  channel direction has the WRONG SIGN for a long: a retailer's largest brand shipping less is a headwind,
  and 1% of $6.8B across Nike's entire global wholesale channel is immaterial against any retailer's own
  revenue.** ⚠ **A MISS-DRIVEN THESIS IS ALWAYS SELF-SUPPLIED. Expect this shape every earnings season and
  kill it on part 1 each time.**

- **⚠⚠ ONE SELF-CORRECTION FROM 10-02 THAT RUNS THE OPPOSITE WAY FROM EVERY OTHER CATCH ON THIS BOARD, AND
  IT IS THE MORE USEFUL DIRECTION TO LEARN: AN INHERITED SENSE OF "HOW BIG THIS COMPANY IS" FAILS TOWARD
  DISMISSING REAL EVENTS.**
  Micron reported **FQ4 revenue of $54.23B against $11.32B a year earlier** and guided FQ1 to **$61.5B and
  $38.15 EPS.** ⚠ **The reflex was to flag these as corrupt source data — a 4.8× year-over-year increase and
  a quarterly EPS that reads as garbled.** ⚠⚠ **THAT JUDGMENT RESTED ENTIRELY ON A PRE-2026 PRIOR ABOUT
  MICRON'S SCALE, AND THE TAPE HAS ALREADY OVERRUN IT: MU's own closes ran 1072.18 → 1066.85 over the five
  sessions to 10-01, i.e. ~$1,070 per share, which is CONSISTENT with a memory supercycle of exactly this
  magnitude.** ⚠ **The figures were recorded AS REPORTED and NOT disputed.** ⚠ **Every other catch on this
  board guards against inventing things that are not there. This one guards against dismissing things that
  are, and an unchecked prior about a company's scale is exactly as inherited as a superlative or a count.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR JUDGMENT
  RATHER THAN CARE. 98 REAL THESES, ZERO ACCEPTED EVER** (99 `### T-` headings less the template, counted
  from source on 10-02 with `grep -c`). **25 this week, ALL REJECTED.** Set beside that: an empty satellite
  sleeve, **~30% idle cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker, and an account at
  **−0.4442% since inception on official closes** (−0.2638% carrying the receivable).
  ⚠⚠ **A LOSING ACCOUNT RAISES THE PULL, AND THE DISTINCTION HOLDS: the book is down because it holds ~70%
  of a market that fell. AND THE OTHER HALF OF THAT ARGUMENT IS THE STRONGER ONE: on 10-01 the market ROSE
  and the identical structure LAGGED it by exactly the cash weight, nineteenth session in nineteen. The
  sleeve has no effect in EITHER direction, and a run that only ever cites the down-day half is quoting the
  flattering half.** ⚠ **"Deploy something" is not what these numbers argue for.**
  ⚠ **09-25 remains the sharpest evidence: the funnel finally produced the well-sourced, named-supplier,
  allocated-figure candidate that a month of rejections implied was the missing ingredient — AND IT WAS
  STILL NOT A TRADE. That is evidence the bar is not what is binding, NOT evidence the bar should move.**
  §4's own position governs: **a run that finds nothing is a successful run.** **Naming the pull is the only
  defence against acting on it.** If the bar is to move, that is a `strategy.md` change and **only the human
  may make it.**
  ⚠⚠ **10-01's OPEN AND 10-02's PRE-MARKET ARE BOTH SEATS WHERE EVERY GATE WAS OPEN AND NOTHING WAS
  BOUGHT** — breaker INACTIVE, week 0 of 3, sleeve empty, ~30% idle cash, **$4,992.82** of headroom under
  the 5% cap on 10-02, `control.md` notes (none), `TRADING_ENABLED: true`. ⚠ **"Nothing was blocked" and
  "nothing was bought" are both true, and the second follows from the RESEARCH and the PLAN, not from a
  guardrail.** ⚠ **A position opened at 09:35 without a plan entry routes AROUND the discipline rather than
  satisfying it.**
  ⚠ **WHERE THIS WEEK'S 25 DIED, BY THE DURABLE KILL: part 1 = 7, part 2 = 2, part 3 = 8, §3 = 3,
  premise/structure = 5.** ⚠ **PART 3 REMAINS THE LARGEST SINGLE CATEGORY. Do NOT read that as a trend — it
  reflects WHICH EVENTS the tape offered (a 2028 cleanroom, a 2030 LNG delivery, an undisclosed delivery
  schedule, a reactor framework), not a change in how the funnel screens.**
  **10-02's five: T-01 RTX/SM-6 part 1 (no counterparty) · T-02 ORCL/Tencent structure + capacity-already-
  built · T-03 Venture Global/COP part 3 (2030) · T-04 DKS/Nike part 1 + part 2 + wrong sign · T-05 MU
  reached and DECLINED, not re-screened.**
  ⚠⚠ **THE MOST DECISION-RELEVANT DATUM REMAINS T-2026-10-01-02 (AMD): THE FIRST ENTRY IN THIS LOG WHOSE
  PART 1 PASSED CLEANLY** — one clause, no "and also", a signed order, a disclosed figure, a named platform,
  a named US-listed beneficiary. ⚠ **It died on parts 2 and 3, and on being co-named in the headline.**
  ⚠ **Set beside JBL (09-25, killed by a disclosed ZERO MARGIN) and ABBV (09-30, killed by MAGNITUDE alone),
  that is three candidates clearing the evidence bar and failing on three DIFFERENT parts. The binding
  constraint is NOT the evidence bar, and the three failing differently is what makes the set informative
  rather than repetitive.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY.** ⚠ **10-02's five rejections do NOT become a
  queue, and 10-01's six, 09-30's eight and 09-29's six stay disposed too. DO NOT REHABILITATE ANY OF THEM
  AT A DIFFERENT PRICE.**
  **Today's five, with the durable kill on each:** **RTX / SM-6 $24.4B** (part 1 — no counterparty named
  anywhere; rule (v); RTX first-order and now a recurring ticker) · **ORCL / Tencent ~$7B chip lease**
  (structure — ORCL first-order; **capacity already built, so no second tier**; figure unconfirmed) ·
  **Venture Global / ConocoPhillips 20-yr LNG SPA, 1 Mtpa** (part 3 — **first delivery 2030**, ~16 quarters
  out; part 2 — no value disclosed; structure — seller and payer both named, no second party left) ·
  **DKS / Nike's competitors** (part 1's "and also" construction, part 2 immaterial, **sign wrong for a
  long**) · **MU FQ4/FQ1** (**not re-screened** — already disposed 10-01; the cost-line direction has the
  wrong sign for a long-only book, and cost-plus-pass-through fails part 1's one-clause test).
  ⚠ **NOTHING EARLIER WAS REHABILITATED EITHER** — zero `move`, `quote`, `bars` or `asset` calls on MU, any
  equipment name, JBL, AKAM, RDW, FLNC, IOVA, SMMT, CRK, AIR, ABBV, RARE, LLY, CI, AMD, HPE, Lenovo or any
  memory supplier. **A rejection is not a queue.**
  ⚠ **Also screened and not candidates: Nth Cycle/Glencore and Nth Cycle/Trafigura** (private, and signed
  late September — rule (iii), not new) · **Alpha Energy / Tennor Global** ($500M facility; microcap plus a
  private counterparty, §3) · **Hindalco / AluChem terminated acquisition** (Indian-listed, private target,
  no replacement buyer named) · **McKesson reaffirming FY2027 guidance** (rule (iii), a reaffirmation) ·
  **Saudi PPC $7.8B of PPAs** and **Air France-KLM SAF sourcing** (non-US) · **Lambda's $1B financing**
  (private issuer; the GPU vendor is the prior-supplied answer) · **Treasury/FinCEN action on the A7
  Network** (no US-company financial impact stated).
  ⚠ **THE SEPTEMBER PAYROLLS RELEASE AND THE FED's 25bp HIKE TO 3.75–4.00% ARE NOT §4 CANDIDATES AND WERE
  NOT WRITTEN AS THESES: a macro release has NO COMPANY A and no segment revenue line to size, and the hike
  was made IN SEPTEMBER and merely re-reported on 10-02, so it fails rule (iii) on top of that.**
  ⚠ **One §3 question remains reached-but-undecided: Shopify is a Canadian issuer trading as common stock on
  a US exchange, which §3's "US-listed common stock" does not obviously settle. A future run reaching this
  with a LIVE candidate must put it to the human rather than decide it from that seat.**

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES, AND A FOURTH STATE THAT IS NOW STANDING.**
  **Shape one: a DRAWDOWN misread as priced-in** (nine instances, newest CNC −6.44% → `true`), plus three
  near-misses that cleared only because the *fall* was fractionally too small (LMT −3.61%, GM −3.95%, LH
  −3.83%). **Shape two: the filter working** on genuine news rises (SHOP +9.61%, ILMN +11.54%, GRAL
  +44.67%). **Shape three (09-25, JBL): a genuine RISE UNRELATED TO THE NEWS that the window swept up** —
  +4.97% over five sessions on a grind whose largest day was +1.72% and whose **news day moved JBL +0.63%.**
  §4 conditions on having moved 4% "**on this news**"; the mechanized check cannot see causation.
  ⚠ **The defect is SIGN- AND CAUSATION-BLINDNESS, not the threshold. Only a human may change §4 or
  `alpaca.py move`.**
  ⚠ **AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read `priced_in: false` at +3.19%**
  while its closes ran **104.53 → 117.435 = +12.35% IN ONE SESSION**, then 118.33, 118.42, then **110.44 =
  −6.74%** — a +12.35% event move and a −6.74% give-back inside the SAME five-session window, netting to a
  passing +3.19%. ⚠ **Prior instances (QCOM, AVAV) were INTRADAY round trips; this one spans MULTIPLE
  SESSIONS, and no 09:35 re-validation would have surfaced it either.** ⚠ **HPE is a milder fresh instance
  (five sessions +2.50% while the news day alone ran +3.886%): the window hid ~1.4pp and changed NO verdict,
  recorded as mild because a loud warning whose instances are all mild teaches a future run the shortcut is
  safe.**
  ⚠⚠ **THE FOURTH STATE — THE FILTER HAVING NOTHING TO FIRE ON — IS NOW AS COMMON AS THE OTHERS AND MUST BE
  NAMED EXPLICITLY.** **09-29 and 10-02 both made ZERO `move` CALLS IN ANY SEAT**, because every candidate
  died on structure, part 1, part 2 or part 3 before an eligible ticker was reached. ⚠ **That is an ABSENT
  check, not a skipped one, and "the filter did not fire" and "the filter had nothing to fire on" look
  IDENTICAL in a run summary.** ⚠ **The separate EXERCISED-AND-NON-DECISIVE state also stands (09-30: ABBV
  −0.78%, RARE −1.83%; 10-01: AMD −0.52%, HPE +2.50%, MU −0.50% — all `false`, not one rejection turning on
  any of them).** ⚠ **A run reporting "priced-in: pass" must say WHICH of these states it means.**
  ⚠ **AMD is the one to remember: a name co-named in a $1.2B AI-order headline, printing −0.52% over five
  sessions, is precisely the reading that invites a "the market has not noticed" story. THAT STORY WAS NOT
  WRITTEN.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — AND NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat.
  **MOST RECENT OFFICIAL/PRICE BASIS (`bars --adjustment all`, the complete 2026-10-01 session:
  o 702.95 h 703.43 l 697.50 c 702.255): equity $99,555.77, core $69,555.77 = 69.8661%, cash 30.1339%,
  day +$163.43 / +0.1644% from 09-30's $99,392.34, since inception −$444.23 / −0.4442%. TOTAL-RETURN BASIS
  carrying the inferred ~$180.45 receivable: ~$99,736.22, since inception −0.2638%.**
  ⚠ **RE-DERIVED, NOT CARRIED: qty × 702.255 + $30,000 reproduces $99,555.767 and 69.8661% to the cent from
  a FRESH 10-02 `positions` pull, so these are CHECKED facts rather than inherited ones.**
  **BROKER MARK at 10-02 08:23 (PRE-MARKET, NOT A CLOSE): equity $99,856.37, core $69,856.37 = 69.96%,
  `current_price` 705.29, core `unrealized_pl` −$143.62 / −0.205% against the 706.74 RAW fill,
  `rebalance_delta` +$43.09 — an ELEVENTH consecutive positive reading and NOT the sign defect resolving
  (the same quantity disagreed in sign on 09-24).**
  ⚠ **The broker figure is a LIVE MIDPOINT and must never be differenced against a close figure.** **Prior
  closes for reference: 09-30 $99,392.34 / core 69.8166%; 09-29 $99,557.25; 09-28 $99,688.98.**
  ⚠⚠ **THE WORKED INSTANCE OF THE MIXED-BASIS TRAP, STILL THE ONE TO REACH FOR: differencing the BROKER
  $99,505.75 against 09-29's OFFICIAL $99,557.25 gave −$51.50 / −0.0517%, a THREEFOLD UNDERSTATEMENT of the
  true −$164.91 / −0.1656%.**
  ⚠⚠ **THE PRE-MARKET/POST-BELL SERIES TRAP WAS DECLINED FOR A SECOND CONSECUTIVE MORNING, WHICH MAKES IT A
  REPLICATION.** On 10-02 `current_price` read **705.29, i.e. +$3.035 above the 702.255 official close** —
  larger than 10-01's +$2.915 and roughly TRIPLE the largest of the ten catalogued POST-BELL gaps.
  ⚠ **IT WAS NOT APPENDED. Those ten are POST-BELL observations; this is a PRE-MARKET indication, and
  appending it would manufacture a spurious "largest gap on record" out of MIXING TWO TIMES OF DAY.**
  ⚠ **DIFFERENT HOUR, DIFFERENT SERIES.** ⚠ **And note what is NOT claimed: two consecutive large
  pre-market gaps are not a "pre-market series" either — two observations support no range.**
  ⚠ **Post-bell `current_price` minus official close, TEN observations: +$1.13, −$0.22, +$0.169, +$0.02,
  −$0.97, −$0.054, −$0.25, +$0.45, +$1.145 (09-30), +$0.485 (10-01). The largest is still +$1.145, and "the
  broker/official gap is widening" remains available, fluent and UNSUPPORTED.**
  ⚠ **A TENTH EQUITY-DRIFT INSTANCE: `selftest` read $99,865.29 at 08:23 and `sleeves` read $99,856.37
  seconds later — an $8.92 spread, well inside the established $1.97–$216.91 range and therefore NOT
  evidence of anything narrowing.** ⚠ **An equity figure is only meaningful with its CALL and its TIMESTAMP
  attached, and two figures from different calls must never be differenced.**
  ⚠⚠ **THIS BITES §6's 5% SIZING CAP, WHICH IS COMPUTED AGAINST LIVE EQUITY — 5% of the 08:23 mark is
  $4,992.82, against $4,977.79 on the official close. IT HAS NO OPERAND ONLY BECAUSE NO PLAN HAS EVER
  CARRIED A BUY INTENT.**
  **NO REBALANCE WAS DUE, NONE WAS PLACED, AND NONE IS DUE AT TODAY'S OPEN** — §2 acts at the **65/75 band
  edge** and core sat **4.96 points** inside the 65 edge on the 08:23 broker mark (**4.87** on the official
  close). ⚠ **`rebalance_delta: +$43.09` IS A DISTANCE READOUT, NOT AN INSTRUCTION.**
  ⚠ **Fifty-seventh consecutive run inside 69.59–70.22%.**
  ⚠ **AUDIT ANY SUPERLATIVE BEFORE REPEATING IT.** 10-01's **+0.1644%** is the **5th best of the 19
  post-fill sessions** (behind 09-21 +1.0848%, 09-17 +0.7774%, 09-11 +0.5833%, 09-25 +0.3382%) — **notable
  in no direction.** Since inception **−0.4442% is NOT a low** — 09-16 reached −1.3396%, 09-15 −1.0350%,
  09-10 −0.9954%. On **price** basis 09-28's −0.7010% IS the largest single-day loss on record; on **total
  return** it is **−0.5212%, SECOND**, behind 09-23's −0.5327%.
  *(Grounded from a 45-session pull whose rows before the 09-03 fill are **COUNTERFACTUAL** — the account
  held $100,000 cash — and must never be read as account history.)*

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`, NEVER a
  `positions` field for a close or an execution reference. Close-to-close from `bars` (⚠ a COMPLETED
  session's bar, ⚠ and STATE THE ADJUSTMENT), a fresh `quote` for execution.**
  ⚠⚠ **THE ARTIFACT IS NOW ATTRIBUTED EXACTLY, AND THIS PART IS SETTLED.** On 10-01, `last_equity`
  **99,417.59768935866** equals **qty × `lastday_price` 700.86 + cash** with a residual of **0E−11**; and
  `last_equity` minus the official-close equity (**99,392.340879994755**) is **$25.256809363905**, which is
  **exactly qty × the $0.255 gap between `lastday_price` and the official close.** ⚠⚠ **SO THE ARTIFACT IS
  NEITHER NOISE NOR IMPRECISION: IT IS `lastday_price` NOT BEING THE OFFICIAL CLOSE, PROPAGATED THROUGH ONE
  MULTIPLICATION. Every instance is that one substitution, at that day's gap, times the share count.**
  *(Measured instances: 09-28 −$736.91 against a real −$703.72; 09-30 −$70.32 against a real −$164.91, an
  artifact of −$94.59.)* ⚠ **The field stays UNUSABLE as a day's P&L — now for a NAMED reason, so a future
  run need not re-measure it.** ⚠ **`change_today` sits on the SAME broker basis for the SAME reason and is
  not a day return either.**
  ⚠⚠ **WHAT IS EXPRESSLY *NOT* CLAIMED: this does NOT re-open WHY `lastday_price` differs from the close.
  Four mechanisms are falsified and both signs are observed. STOP PREDICTING IT; DO NOT RE-OPEN IT.**
  **An arithmetic identity between two broker fields and a mechanism for one of their values are different
  claims; only the first is made, and it needs no mechanism to be true.** *(10-02's reading: `lastday_price`
  702.35 against the 702.255 official close, a +$0.095 gap — the same settled shape, not a new miss.)*
  ⚠ **Keep writing falsifiable predictions down in advance for LIVE questions** — there is one on the
  dividend credit, above.

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 19 OF 19 AND STILL HAS NO EXCEPTION.** **10-01: VOO +0.2355%
  (`--adjustment all`, completed closes), the book +0.1644% on the same basis, excess −0.071085pp — against
  −0.071085pp PREDICTED by holding 69.8167% core and the rest in idle cash. RESIDUAL EXACTLY 0.00E+00.**
  The satellite sleeve contributed **exactly 0.000000%**, as it has for the account's entire history.
  ⚠ **The sign flipped negative on 10-01 after four positive-excess down-days, and THAT IS THE SAME
  STRUCTURAL FACT, NOT A CHANGE IN QUALITY** — four consecutive write-ups of positive excess from a ~30%
  cash drag had begun to read like a book doing something right.
  ⚠ **It is the signature of ONE long position at ~70% weight with NO SECOND SOURCE OF RETURN. A TIGHT FIT
  IS NOT CONFIRMATION — the model fits to zero residual because there is NOTHING IN THE BOOK THE MODEL
  OMITS.** ⚠ **The 09-25 weekly review recomputed all 15 post-fill sessions from official closes and found
  PERFECT separation: every VOO-down day positive excess, every VOO-up day negative, one flat day exactly
  0.0000pp.** ⚠ **Neither direction is skill.**
  ⚠ **THE TRAP, and the standing same-source rule does NOT catch it: comparing the book's PRICE basis
  against VOO's `--adjustment all` gave a spurious +0.0438pp on 09-28, because one leg excluded the dividend
  and the other included it. BOTH LEGS WERE FROM `bars --adjustment all` — the mismatch is between the
  ACCOUNT and the BENCHMARK recognising the same cash on DIFFERENT DATES.** ⚠ **It does not bite on 09-29
  through 10-01. IT BITES AGAIN ON THE NEXT EX-DATE.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — ELEVEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  **(11) A COUNTER INCREMENTED FOR THE DAY THE RUN IS STANDING IN.** Writing `positions.md` on 09-30, a run
  advanced the session counter 20/17 → 21/18 because it reflexively counted the day it was in. ⚠ **At 08:23
  the market has not opened: today is NOT a completed session and the count must not advance. Routines 1 and
  2 are both exposed; routine 4 is not.** ⚠ **It shares a failure mode with (9): re-running the check
  REPRODUCES THE WRONG NUMBER, because the error is in the DEFINITION OF THE UNIT, not in the arithmetic.
  Only the clock exposes it.** *(10-02's pre-market seat declined the increment from the clock. 22/19 holds.)*
  **(10) A NUMBER THAT IS CORRECT ON A BASIS NOBODY NAMED.** The 09-28 close nearly wrote *"largest
  single-day loss on record"* off a series it had just pulled. ⚠ **The series was right and the sentence was
  still false. "Pull the source before writing the superlative" IS NOT SUFFICIENT WHEN THE SOURCE HAS TWO
  BASES: NAME THE BASIS IN THE SENTENCE, or do not write the sentence.**
  **(9) A COUNTER WHOSE *UNIT* IS WRONG.** Close journals reported §5.1–§5.4 untested for *"the Nth
  consecutive SESSION"* — 23, 26, 29, 33, 37 on consecutive trading days. ⚠ **It incremented by THREE OR
  FOUR per trading day; sessions increment by ONE. A RUN counter wearing a session label.** **Current
  figures, re-derived from a 45-session `bars` pull: 22 trading sessions since 2026-09-01, 19 AFTER the
  09-03 fill, zero satellite positions ever. Do not restart the old series.**
  **(8) A MEASUREMENT PRESENTED AS A CALIBRATION:** the 09-25 midday *"volume tracks elapsed session time
  almost exactly."* ⚠ **The DENOMINATOR was a prior-day mean, and a ratio against one LOOKS like a
  measurement of the current day and is not one.**
  **(7) A MISCOUNT IN A VERIFICATION CLAIM:** the 09-24 close wrote it had *"verified all TWELVE keys."*
  ⚠ **There are THIRTEEN.**
  **(6) A SCOPE CLAIM:** *"routine 2 is the ONLY routine that runs with `is_open: true`"* — falsified by the
  run that read it. ⚠ **THE MOST DANGEROUS SHAPE, because it was not a number to re-pull but a statement
  about the SYSTEM'S OWN SHAPE, which no data call would ever contradict.** ⚠ **Cleanest live instance: the
  09-30 close justified a counter increment with "catch (11) says routine 4 is not exposed" — a claim about
  the system's shape. What actually made it safe was that THE SESSION WAS COMPLETE, established from a bar
  that exists plus a 15:59:59 `latestTrade` matching its close. A CORRECT NUMBER REACHED BY AN UNCHECKED
  ROUTE IS NOT A CHECKED FACT.**
  **(5) A TRUNCATED SERIES (09-24):** the post-bell `current_price` record had silently dropped its own
  largest member. **(1)** A false superlative surviving three runs, caught **by accident** 09-21.
  **(2)** A stale count ("49 theses") caught deliberately 09-22, running in the direction that
  **understates** the problem. **(3)/(4)** Both halves of the `lastday_price` mechanism, asserted and
  falsified in turn.
  ⚠ **A superlative, count, mechanism, SERIES, CALIBRATION or BASIS inherited from a prior run is NOT a
  checked fact.** **Assume the next one you are handed is wrong until you have pulled the source — and then
  check which basis the source answered on.** *(10-02 recounted the thesis total from source: **99 `### T-`
  headings less the template = 98**.)*
  ⚠⚠ **AND NOTE THE ONE CATCH THAT RUNS THE OTHER WAY — 10-02's Micron correction, above. Every catch here
  guards against inventing what is not there; that one guards against DISMISSING what is.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — THIRTY-FIVE CONSECUTIVE REFUSALS, AND THE COUNT IS DOING LESS WORK
  THAN IT LOOKS.** The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon
  announcement — first-order, outside §4 at any price** — and **open item (7) is resolved by a human editing
  §4 or `alpaca.py move`, not by a number this seat collects.**
  ⚠⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER EACH REFUSAL COST ANYTHING, AND MOST DID NOT.** A midday
  seat is exits-only, a close seat does not trade, and an open seat has no funnel at all — so refusals from
  those seats are **FREE, and 10-01's was STRUCTURALLY UNAVAILABLE TO VIOLATE.** ⚠ **A refusal that could
  not have been violated is not evidence of restraint.** ⚠ **10-02's PRE-MARKET refusal is one of the STRONG
  instances, because a pre-market seat DOES have a funnel and GNRC was reachable — as are 09-23, 09-24 and
  09-25.** ⚠ **No new costume in eleven sessions; the list looks CONVERGING rather than growing.** Costumes:
  diligence, curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement,
  issue-closure, call-already-open, screen-already-running. **The pattern is the finding, not any instance.
  FREE IS NOT THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — SIXTY-FIVE RUNS.** §5 exempts core from all four
  sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **A CLOSE RUN IS THE STRONGEST INSTANCE THIS ITEM GETS, because it is the ONE SEAT THAT WRITES MARKS and
  it is holding a complete official close at the moment it declines to write one. 10-02's pre-market refusal
  is FREE by comparison and is logged as such.** **Measure the core from the 706.74 fill and from an official
  close, never from a `positions` field** ⚠ **— and the fill price is a RAW print, so measuring it against an
  `--adjustment all` close MIXES BASES.** ⚠ **Noted honestly: this refusal is close to automatic, and
  automatic is not the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN IS
  USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell sees it
  pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with **no bar for
  today**. ⚠ **`is_open: TRUE` is the one case where the boolean alone is sufficient, and only because TRUE
  has a single meaning. FALSE has three.** ⚠ **THE STRONGER DISCRIMINATOR IS THE DATA PLANE: post-bell,
  check that a daily bar for today EXISTS and its close matches the 15:59 `latestTrade`; pre-market, check
  that NO bar dated today exists yet.** *(10-02 08:23 did exactly that: `is_open: false`, `next_open`
  2026-10-02T09:30 pointing at TODAY, a complete 2026-10-01 bar present and no 2026-10-02 bar — the
  pre-market shape, confirmed not assumed.)* ⚠ **But with `is_open: true` that same bar is PARTIAL and is
  not a close.**

- **⚠ EIGHT ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A NUMBER A
  RUN COLLECTS.**
  ⚠⚠ **(8) THE ONLY ONE THAT COULD MAKE §1 UNWINNABLE BY CONSTRUCTION: DOES THE PAPER ACCOUNT PAY
  DIVIDENDS?** VOO went ex-dividend 2026-09-28; `cash` still reads **exactly $30,000.00** on 10-02, day 5 of
  8. **A falsifiable test with a 2026-10-07 deadline is on the record.** ⚠ **AND SEPARATELY: whether the
  TOOLING should read closes on a stated basis by default is a human's call; 09-28 is the strongest evidence
  yet that it should.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — nine instances plus three near-misses;
  **there is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on the bill.
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM, AVAV, and
  **AKAM, the first MULTI-SESSION round trip.** Same root cause as (1), opposite direction. **The fix for
  (1), (2) and shape three is a human editing §4 or `alpaca.py move`** — the suggestion on record is to make
  it **read SIGN and causation, not loosen or remove the threshold.**
  **(3)** The satellite sleeve is **structurally undeployed — 98 theses, zero positions, ever.** A 70/30
  cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits the cash and
  §4 says most runs end in no trade — both rules were followed, and the agent must NOT respond by lowering
  the §4 bar.** **The binding constraint now has SEVEN known forms, plus one sub-shape:** the source
  withholds the counterparty's number; **or** the counterparty discloses **roadmap instead of segment
  revenue**; **or** the named beneficiary is **vertically integrated**; **or** **both parties expressly
  refuse to disclose as a commercial choice** (GM); **or** **the figure is fully disclosed and is the WRONG
  QUANTITY** (JBL); **or** **THERE IS NO COUNTERPARTY AT ALL** (IOVA); **or** **EVERYTHING IS DISCLOSED AND
  THE SPENDING SIMPLY LANDS TOO FAR IN THE FUTURE** (Micron's late-2028 cleanrooms; **Venture Global's 2030
  first delivery is a far more extreme instance**). ⚠ **Sub-shape of form six, new 10-02: THE TRANSACTION IS
  IN CAPACITY ALREADY BUILT, so a second tier exists but is not touched** (ORCL/Tencent).
  ⚠ **Only the first two are addressable by widening the evidence bar. Forms three through seven are not;
  form five would be made WORSE by widening it; and form seven is untouched by it, because the constraint is
  the CALENDAR.** ⚠ **ELMT is the standing proof that evidence is not the constraint.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the prior
  close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11.** ⚠ **Keep measuring it from
  the fill — and the fill is a RAW print.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it never
  had a stable size. ⚠ **A PRICE-SOURCE problem that contaminates every derived figure.** It has flipped the
  sign of a §2 quantity (09-24) and was caught INTRA-run on 09-29 at 09:35. ⚠ **09-28 added a SECOND,
  INDEPENDENT axis — `quote` vs `bars --adjustment all` on the SAME session — which is not a midpoint problem
  at all, and which AGREED later only because no rescaling separated the two sessions.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed all
  five checks on 09-11 while `clock` returned 500, and on 09-24 while `perplexity.py` returned 500.
  ⚠ **AND IT PASSED ALL FIVE ON 09-28 AND 09-29 WHILE THREE OF 09-28's FOUR ROUTINES HAD PRODUCED NOTHING.
  A green pre-flight certifies THIS run's credentials, nothing about the schedule, the data plane, or whether
  yesterday's runs happened.**
  **(7)** See (1) and (2) — the mechanized priced-in check cannot see SIGN or CAUSATION, and only a human may
  change it.

---

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
been its third appearance). ⚠⚠ **10-02 ADDS TWO FRESH INSTANCES IN ONE SESSION: RTX for the SECOND TIME IN
FIVE SESSIONS (AMRAAM 09-29, SM-6 10-02) and VENTURE GLOBAL for the SECOND TIME (China Gas, then the
ConocoPhillips SPA).** ⚠ **Both re-entered the funnel through a genuinely new transaction and both died on
the SAME rule they died on the first time — RTX on (v), Venture Global on (vi). A ticker that keeps arriving
and keeps dying the same death is telling you about the DISCLOSURE PRACTICE OF ITS INDUSTRY, not about a
candidate maturing.**
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
Global/China Gas, Amazon/Generac, Centrus/Antares, Elmet/Tungsten West, NeoVolta/SK On.
⚠⚠ **10-02 SUPPLIES THE MOST EXTREME INSTANCE THIS RULE HAS EVER TAKEN, AND IT IS WORTH QUOTING AS THE
CALIBRATION POINT: Venture Global / ConocoPhillips, a 20-YEAR SPA for 1 Mtpa with FIRST DELIVERY IN 2030 —
roughly SIXTEEN QUARTERS against §4's two-quarter ceiling.** ⚠ **A long-dated offtake or SPA headline is
large, real, and NEVER §4 material. Part 3 kills it in ONE step, before any funnel query is spent.** ⚠ **The REGULATORY
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
has now been exercised **THIRTY times and has never fired, and will stand at THIRTY-ONE after today's open** *(10-01 pre-market wrote `plan_date: 2026-10-01` against an ET date of 2026-10-01 **computed, not
assumed**, so it will be **FRESH** at 09:35 and the gate will again correctly do nothing)*, and its alert path **remains untested code.**
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

⚠ **Added 10-02:** **RTX / SM-6 $24.4B** — the **fourth** defence-award instance across three primes; no
supplier named, and the **$24.4B is a MAXIMUM POTENTIAL value**, not an obligated amount. **ORCL / Tencent
~$7B chip lease** — ORCL first-order, the chips **already installed** so no second tier is touched, and the
figure is an **unconfirmed press estimate** with neither party commenting. **Venture Global / ConocoPhillips**
— **first delivery 2030**, the most extreme part-3 kill on record. **DKS / Nike's competitors** — an earnings
miss is not a second-order catalyst; part 1 needs an "and also", part 2 is immaterial, and the channel
direction has the **wrong sign for a long-only book**. **MU** — already disposed 10-01 and **deliberately not
re-screened**. ⚠ **Also screened and not candidates: Nth Cycle/Glencore and /Trafigura (private, and signed
in September — rule (iii)), Alpha Energy/Tennor (microcap plus private counterparty), Hindalco/AluChem
(Indian-listed, no replacement buyer), McKesson (a reaffirmation — rule (iii)), Saudi PPC and Air France-KLM
(non-US), Lambda's $1B financing (private issuer), Treasury/FinCEN's A7 Network action (no US-company impact
stated). THE FED's 25bp HIKE AND THE PAYROLLS RELEASE ARE NOT §4 CANDIDATES — no Company A, no segment
revenue line, and the hike happened IN SEPTEMBER and was merely re-reported.**

⚠ **Earlier disposed rejects (09-21 to 09-24) remain disposed and are NOT re-listed here.** **ILMN, GRAL,
BBY, PYPL, SHOP, SoftBank/OpenAI, GIS, LH, CNC/MOH/OSCR, LHX, GFS, ACN, GPC/ORLY/LKQ, GM, BE, BG** — see
`research_log.md` for the working on each. **A rejection is not a queue.**
