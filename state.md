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
last_run: 2026-10-01 12:41 ET 3-midday-management (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99370.06 at pre-flight 12:41; EXITS-ONLY SEAT WITH NO OPERAND - zero orders, zero fills, nothing closed, no realised P and L, and NOTHING OPENED BECAUSE THIS SEAT MAY NOT OPEN, section 4 routing every entry through pre-market research and the 09:35 execution run so that a midday entry would BYPASS the written thesis rather than satisfy it; MARKET OPEN CONFIRMED - clock 12:41:34 is_open TRUE, next_close 2026-10-01T16:00 next_open 2026-10-02T09:30; NO OPEN SATELLITE POSITIONS, SO PER THE ROUTINE ITSELF THE RUN NOTES THE ABSENCE AND STOPS RATHER THAN LOOKING FOR SOMETHING TO DO; RECONCILIATION CLEAN - positions returns ONE row, core VOO 99.046311231 sh avg_entry 706.74 a RAW print, cost_basis 69999.99 unchanged since the 09-03 fill, against ZERO satellite blocks in positions.md, compared satellite-to-satellite and never raw ledger against raw broker, and core was REMOVED FROM THE WORKING LIST before any section 5 rule was read; orders --status open EMPTY and orders --status all ONE ROW for the account's entire history, so section 7 has nothing unverified anywhere; STEP 2 HIGH-WATER REPAIR NO OPERAND FOR A FOURTH CONSECUTIVE DAY WHICH IS NOT THE SAME AS IT WORKING - the detector's entire input is an as-of date compared against the last trading day, there is NO highest_close field so there is NO date, so NO STALENESS WAS DETECTED AND NONE WAS RULED OUT, and the backfill path remains UNEXERCISED CODE; sections 5.1-5.4 ALL ABSENT WHICH IS NOT PASSING - 5.1 and 5.2 NO OPERAND with ZERO Perplexity news-on-holdings queries due and zero run, 5.3 DISTANCE UNDEFINED not comfortably far, 5.4 NOT ARMED; consecutive_closed_losses stays 0 CONFIRMED not recomputed, breaker INACTIVE via common.halt_active() False with empty reason, halt_triggered_at none so NO HALT_CLEARED_AT comparison was required; THE FINDING OF THIS RUN IS THAT THE PARTIAL-BAR WARNING WAS FINALLY TESTED BY THE SEAT EVERY PRIOR INSTANCE NAMED AS THE DANGEROUS ONE, AND ITS TWO HALVES GRADED OPPOSITELY - at 3h12m into a 6.5h session the PRICE HALF IS CONFIRMED AND IS THE DANGEROUS HALF, c 700.35 sitting 26 cents from 09-30's official 700.605 and mid-range against a trailing 691.44-710.93 band, a WHOLLY PLAUSIBLE CLOSE CARRYING NO WARNING, and THE MECHANISM IS NOW VISIBLE RATHER THAN SUSPECTED because c 700.35 EQUALS latestTrade p 700.35 TO THE CENT, i.e. the partial bar's close field is THE LAST TRADE SO FAR WEARING A CLOSE'S CLOTHES; but THE n/v HALF IS REFUTED AS STATED - n 982 and v 26215 are NOT visibly tiny, being 47.8 pct and 43.0 pct of 09-30's completed bar - AND IS REPLACED BY A SHARPER DISCRIMINATOR, because across the 24 COMPLETED sessions in the trailing 25-day window the MINIMUM n is 1450 and the MINIMUM v is 43730, so today's partial sits BELOW THE FLOOR OF EVERY COMPLETED SESSION ON BOTH FIELDS, making the usable test NOT is-n-small but IS-n-BELOW-THE-TRAILING-COMPLETED-MINIMUM, a comparison against a distribution rather than a glance; THE LIMIT IS STATED AND FALSIFIABLE - the floor test MUST FAIL ON A HALF-DAY SESSION where a COMPLETED bar legitimately carries about half the usual n/v, the next early close is the test, and THE CLOCK REMAINS THE ONLY SOUND DISCRIMINATOR with the floor test a corroborant and never the primary; THE last_equity IDENTITY RECONFIRMED UNINHERITED FROM A FRESH PULL - qty times lastday_price 700.86 plus cash EQUALS last_equity 99417.59768935866 with a residual of 0E-11, BUT THE SAME IDENTITY DOES NOT HOLD INTRADAY, qty times current_price 700.19 plus cash being 99351.2367 against equity 99349.75, a 1.49 residual which also exactly explains why equity minus last_equity at -67.85 differs from qty times lastday-minus-current at -66.36; GRADED HONESTLY THAT IS NOT A WITHIN-RESPONSE CONTRADICTION because positions and account were TWO SEPARATE HTTP CALLS seconds apart, so the 1.49 is the established intraday-drift item in a NEW COSTUME and not a new defect, and unrealized_intraday_pl -66.361028 is on the BROKER basis not the official-close basis and was not used as a day return; INTRADAY-DRIFT ITEM NINTH INSTANCE - selftest 99370.06 against sleeves and account both 99349.75, a 20.31 spread, well inside the established 1.97 to 216.91 range and therefore NOT evidence of anything narrowing, and it bites section 6's 5 pct sizing cap which is 4967.49 on this mark with NO OPERAND because this seat may not buy; CASH READS EXACTLY 30000.00 - a TWELFTH reading on the FOURTH calendar day, VOO dividend STILL UNPAID, day 4 of 8, falsifiable deadline 2026-10-07, and NON-ARRIVAL THIS EARLY IS EXPECTED NOT EVIDENCE because settlement runs on the PAY date not the ex-date, and the HOUR of the reading adds nothing since settlement does not run on the bell; NO REBALANCE DUE - core 69.8051 pct on the 12:41 broker mark, 4.805 points inside the 65 edge and 5.195 from the 75 edge, and section 2 acts at the BAND EDGE not toward the 70 pct target; rebalance_delta +195.07 is a TENTH CONSECUTIVE POSITIVE READING AND NOT THE SIGN DEFECT RESOLVING, the same quantity having disagreed in sign on 09-24; FIFTY-SIXTH consecutive run inside 69.59-70.22; THIS SEAT IS NOT THE REBALANCING SEAT - section 2 rebalances at the next MARKET-OPEN run, so the band reading here is a RECORD and not a declined action; HOUSEKEEPING ALL CONFIRMATIONS NOT CHANGES - week_anchor computed via common.week_anchor() is 2026-09-28 and MATCHED week_of so NO ROLLOVER was due, next boundary 2026-10-05; new_positions_this_week stays 0 of 3 and open_thesis_ids stays none; NOTHING was appended to trade_log.md because no order reached a terminal state, and NOTHING to research_log.md because this seat writes no theses; control.md notes read (none); alerts.md carries ZERO open incidents and NO alert of any kind was posted; SESSION COUNTER DELIBERATELY NOT ADVANCED - it stays 21/18 because at 12:41 TODAY IS IN PROGRESS AND NOT A COMPLETED SESSION, which is the SAME trap the partial bar sets one layer down and catch (11) names this seat as exposed; 93 cumulative theses and 0 EVER ACCEPTED, ZERO written this seat by design, 6 on 10-01, 20 this week all rejected; EVERY GATE THAT COULD HAVE BLOCKED AN EXIT WAS OPEN AND THERE WAS NOTHING TO EXIT; state.md VALIDATED with common.read_state(), 13 keys, zero hash characters in the fenced block; prior last_run preserved below)

prior_run: 2026-10-01 09:37 ET 2-market-open-execution (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99625.59 at pre-flight 09:36; ZERO ORDERS PLACED - zero buys, zero sells, no rebalance, nothing opened, nothing closed, no realised P and L - AND THAT IS THE PLAN EXECUTED FAITHFULLY, NOT A SEAT THAT FAILED TO ACT: plan_today.md carried ZERO BUY ZERO SELL ZERO REBALANCE intents and this seat is forbidden to generate one; MARKET OPEN CONFIRMED - clock 09:37:08 is_open TRUE, the ONE boolean sufficient alone because TRUE has a single meaning while FALSE has three, next_close 2026-10-01T16:00 next_open 2026-10-02T09:30, and corroborated from the DATA PLANE by a bar DATED TODAY now EXISTING (c 703.15 o 702.95 h 703.335 l 701.85 n 72 v 2529) where the 08:24 pre-market run found NONE; THAT BAR IS PARTIAL AND WAS NOT USED AS A CLOSE - a fresh quote was used for reference (latestTrade 703.15 at 09:37:30, bid/ask 702.73/703.74); PARTIAL-BAR WARNING GRADED HONESTLY AND THIS INSTANCE DOES NOT TEST IT - at 09:37, seven minutes in, n 72 against 2053 and v 2529 against 61032 ARE visibly tiny, so the n/v half of the warning is untested here and the dangerous seat remains routine 3 at 12:30; BUT THE PRICE HALF DOES HOLD - c 703.15 sits INSIDE yesterday's 700.605 to 707.20 range and gives no warning whatsoever, which is the half that would fool a reader; STALENESS GATE EXERCISED FOR THE THIRTY-FIRST TIME AND DID NOT FIRE - plan_date 2026-10-01 compared against et_today 2026-10-01 COMPUTED via common.et_today() NOT ASSUMED, so the plan is FRESH, every intent was ELIGIBLE for execution and there were none; NO stale-plan alert was posted because the gate did not fire, and ITS ALERT PATH REMAINS UNTESTED CODE; THE PLAN'S OWN WARNING IS THE LOAD-BEARING ONE AND IT WAS HONORED - a FRESH EMPTY plan and a STALE plan produce a BYTE-FOR-BYTE IDENTICAL zero-order run, so freshness was read OFF plan_date and NEVER inferred from the outcome; RECONCILIATION CLEAN - positions returns ONE row, core VOO 99.046311231 sh avg_entry 706.74 a RAW print, cost_basis 69999.99 unchanged since the 09-03 fill, against ZERO satellite blocks in positions.md, compared satellite-to-satellite and never raw ledger against raw broker, and core was REMOVED FROM THE WORKING LIST before any section 5 rule was read; STEP 3 CORE BOOTSTRAP SKIPPED ON core_established TRUE - the flag was READ not assumed and this path never runs again; STEP 4 EXITS NO OPERAND - zero SELL intents and zero satellite positions, sections 5.1-5.4 ALL ABSENT WHICH IS NOT PASSING, 5.3 UNDEFINED not large, 5.4 NOT ARMED, consecutive_closed_losses stays 0 CONFIRMED not recomputed, breaker stays INACTIVE; STEP 5 RE-VALIDATION ZERO move CALLS DUE - ABSENT NOT SKIPPED, and this is a THIRD AND DIFFERENT STATE of the priced-in filter from the pre-market's EXERCISED-AND-NON-DECISIVE three hours earlier; the same filter was NON-DECISIVE at 08:24 on AMD, HPE and MU and had NO OPERAND AT ALL at 09:37, and reporting both as priced-in pass would erase the distinction; STEP 6 ZERO BUYS - new_positions_this_week stays 0 of 3, open_thesis_ids stays none, and NOTHING was appended to trade_log.md or research_log.md because no order reached a terminal state and no intent was skipped on a filter; AN EMPTY APPEND IS CORRECT HERE, NOT AN OMISSION; STEP 7 NO REBALANCE DUE - core 69.8922 pct on the 09:37 broker mark (69641.937584 of 99641.94), 4.892 points inside the 65 edge and 5.108 from the 75 edge, and section 2 acts at the BAND EDGE not toward the 70 pct target; rebalance_delta +107.42 is a NINTH CONSECUTIVE POSITIVE READING AND NOT THE SIGN DEFECT RESOLVING - the same quantity disagreed in sign on 09-24; FIFTY-FIFTH consecutive run inside 69.59-70.22; THIS WAS THE REBALANCING SEAT AND IT DECLINED ON THE BAND, WHICH IS THE ONLY ACTION SECTION 2 AUTHORISES HERE; ORDERS NOT IN LIMBO - orders --status all returns ONE ROW for the account's ENTIRE history, the 09-03 core VOO buy, status filled, terminal, and orders --status open returns EMPTY, so section 7 has nothing unverified anywhere; THE FINDING OF THIS RUN IS THAT equity MINUS last_equity IS NOW FULLY ATTRIBUTED, EXACTLY, TO A NAMED FIELD - last_equity 99417.59768935866 EQUALS qty 99.046311231 times lastday_price 700.86 plus cash 30000 with a residual of 0E-11, i.e. to ELEVEN DECIMAL PLACES, and last_equity minus the official-close equity 99392.340879994755 is 25.256809363905 which is EXACTLY qty times the 0.255 gap between lastday_price 700.86 and the 700.605 official close; SO THE ARTIFACT IS NEITHER NOISE NOR IMPRECISION - IT IS lastday_price NOT BEING THE OFFICIAL CLOSE, PROPAGATED THROUGH ONE MULTIPLICATION, and the standing item moves from MEASURED to ATTRIBUTED; WHAT IS EXPRESSLY NOT CLAIMED - this does NOT re-open WHY lastday_price reads 700.86, four mechanisms for that are already falsified and the carry-forward says stop predicting it; an ARITHMETIC IDENTITY between two broker fields and a MECHANISM for one of their values are DIFFERENT CLAIMS and only the first is made; THE SAME ARITHMETIC ALSO SUPPLIED AN UNINHERITED CONFIRMATION - qty times the 700.605 official close plus cash reproduces 99392.34 to the cent from a FRESH positions pull, so the 09-30 close run's equity figure is a CHECKED FACT this run rather than a carried one; consequence for change_today, which prints 0.00323 - it is computed against lastday_price 700.86 and is therefore on the BROKER basis, not the official-close basis, and was not used as a day return; INTRADAY-DRIFT ITEM EIGHTH INSTANCE - selftest 99625.59 at 09:36 against sleeves and account both 99641.94 at 09:37, a 16.35 spread, well inside the established 1.97 to 216.91 range and therefore NOT evidence of anything narrowing; it bites section 6's 5 pct sizing cap, which is 4982.10 on the 09:37 mark, and HAS NO OPERAND only because no plan has ever carried a BUY intent; CASH READS EXACTLY 30000.00 - an ELEVENTH reading on the FOURTH calendar day, VOO dividend STILL UNPAID, day 4 of 8, falsifiable deadline 2026-10-07, and NON-ARRIVAL THIS EARLY IS EXPECTED NOT EVIDENCE because settlement runs on the PAY date not the ex-date; the hour of the reading adds nothing, pre-market and market-open are the same observation; SESSION COUNTER DELIBERATELY NOT ADVANCED - it stays 21/18 because at 09:37 TODAY IS IN PROGRESS AND NOT A COMPLETED SESSION, and a market-open seat has none of today's to add; catch (11) names routines 1 and 2 as BOTH exposed and this is ROUTINE 2's FIRST OPPORTUNITY TO GET IT RIGHT, taken from the CLOCK rather than from the inherited sentence, which is the distinction catch (6) is about; HOUSEKEEPING ALL CONFIRMATIONS NOT CHANGES - week_anchor computed via common.week_anchor() is 2026-09-28 and MATCHED week_of so NO ROLLOVER was due, next boundary 2026-10-05; common.halt_active() returns False with an empty reason so the breaker is INACTIVE and halt_triggered_at none means NO HALT_CLEARED_AT comparison was required; control.md notes read (none); alerts.md carries ZERO open incidents and NO alert of any kind was posted; GNRC NOT LOOKED AT a THIRTY-FOURTH time but GRADED WEAK AND FREE - this seat has NO FUNNEL AT ALL, it executes a plan it is forbidden to add to, so the refusal cost nothing and the count is doing less work than it looks; 93 cumulative theses (94 T- headings less the template) and 0 EVER ACCEPTED, ZERO written this seat by design, 6 on 10-01, 20 this week all rejected; EVERY GATE THAT COULD HAVE BLOCKED A BUY WAS OPEN AND NOTHING WAS BLOCKED - breaker INACTIVE, week 0 of 3, sleeve EMPTY with 30.11 pct idle cash, 4982.10 of headroom under the 5 pct cap, control.md notes none, TRADING_ENABLED true - AND NOTHING WAS BOUGHT BECAUSE NOTHING WAS PLANNED; idle cash, an inactive breaker and an unused 0-of-3 cap are NOT an opportunity this seat may act on, because a position opened at 09:37 without a plan entry routes AROUND the discipline rather than satisfying it; state.md VALIDATED with common.read_state(), 13 keys, zero hash characters in the fenced block, and both long values read back TAIL-FIRST; prior last_run preserved below)


week_of: 2026-09-28
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.81
satellite_pct: 0.0
cash_pct: 30.20
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on forty-four times.** This repo's only continuity mechanism is the next
run *reading* these files, and padding them with restatements raises the odds a genuinely live item gets
skimmed. **Carry-forward is defined as cleared once acted on.** ⚠ **The 12:41 MIDDAY run placed ZERO ORDERS and produced ONE GENUINELY NEW FINDING, AND IT IS A CORRECTION
TO A STANDING WARNING RATHER THAN A NEW DEFECT: THE PARTIAL-BAR TEST WAS FINALLY RUN BY THE SEAT THAT WAS
NAMED AS EXPOSED TO IT, AND THE `n`/`v` HALF OF THAT WARNING IS REFUTED AS STATED WHILE THE PRICE HALF IS
CONFIRMED WITH ITS MECHANISM NOW IDENTIFIED. See the new item below; it REPLACES the old form.**
⚠ **The 09:37 MARKET-OPEN run placed ZERO ORDERS, CLOSED one item's loudest open question and
added ONE new observation — and the new one is a CLOSURE BY ATTRIBUTION rather than a new defect: `equity −
last_equity` IS NOW EXACTLY ACCOUNTED FOR. `last_equity` = qty × `lastday_price` + cash to ELEVEN decimal
places, so the artifact that has been MEASURED five times is simply `lastday_price` not being the official
close, run through one multiplication.** ⚠ **It did NOT re-open the separate, already-closed question of WHY
`lastday_price` reads what it reads — an arithmetic identity and a mechanism are different claims.**
⚠ **The 08:25 pre-market run's two BASIS observations stand unchanged: (1) A NEW SHAPE OF THE
MIXED-BASIS TRAP, DECLINED — core `current_price` 703.52 sat **+$2.915** above the 700.605 official close,
nearly TRIPLE the largest of the nine catalogued post-bell gaps, and appending it to that series would have
manufactured a "largest gap on record" that is purely an artifact of mixing PRE-MARKET with POST-BELL
readings; (2) A COMPLETED DAILY BAR IS NOT IMMUTABLE IN `n`/`v` — the 09-30 bar read 2050/61014 to the close
run and 2053/61032 on the pre-market pull while its CLOSE held at 700.605 to the cent, so `n`/`v` are even
weaker completeness evidence than the standing warning claims.** ⚠ **The pre-market run also recorded the
sharpest instance yet of the honest-broker failure (own priors naming AMAT/LRCX/KLA against a source that
volunteered the absence) and the first entry in this log whose PART 1 PASSED CLEANLY (T-2026-10-01-02, AMD).**
⚠ **A run that adds nothing to this list is the normal case, not a gap in attention.** ⚠ **A correction
replaces the claim it corrects — it does not sit beside it.** **Nothing live has been discarded.**

---

### Live — act on these

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. DAY 4 OF 8. CHECK `cash` EVERY RUN UNTIL IT RESOLVES.**
  `cash` read **exactly $30,000.00** again at the **10-01 MIDDAY RUN (12:41)** — a **twelfth** reading,
  across the **fourth calendar day**. ⚠ **Twelve readings across four days are ONE unresolved observation of
  an unpaid dividend, not eleven data points. DAY 4 OF 8.** ⚠ **NON-ARRIVAL THIS EARLY IS EXPECTED, NOT EVIDENCE —
  settlement runs on the PAY date, which is not the ex-date. Do not read $30,000.00 as the test resolving in
  either direction, and note that no reading's HOUR makes it stronger: pre-market, midday and post-bell are
  all the same observation, because settlement does not run on the bell.** ⚠ **THE FALSIFIABLE TEST, WRITTEN
  IN ADVANCE AND STILL RUNNING: `cash` should rise to about $30,180.45. IF IT HAS NOT BY 2026-10-07, the
  paper account does not model dividends at all — in which case the book structurally under-earns its own
  benchmark by VOO's entire ~1.0% annual yield and §1's "beat the S&P TOTAL RETURN" is unwinnable BY
  CONSTRUCTION rather than by strategy.** ⚠ **That is a finding for the human, not something to fix from any
  seat.** The implied credit of **$180.26–$180.64** is an **INFERENCE** — Alpaca does not publish the figure
  — and must stay labelled as one.

- **⚠⚠ STEP 2 HAVING NO OPERAND AND STEP 2 WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT A RUN PRODUCES —
  AND 09-30's CLOSE IS THE FOURTH CONSECUTIVE CLOSE RUN TO REPORT IT.** The close routine's headline
  invisible job is to stamp each open satellite position's official close into `highest_close`. **This run
  had nothing to stamp, and the sentence it first reached for was "high-water marks updated," which would
  have been FALSE.** ⚠ **The honest form is: the job had NO OPERAND.** ⚠⚠ **THE BACKFILL PATH REMAINS
  UNEXERCISED CODE** — re-pull the window on a stated adjustment basis, take the max from that ONE pull —
  **and 09-28 is the proof that is not academic: that day lost its close run, so with ONE satellite position
  open, 09-29's midday run would have had to backfill across an ex-dividend date, which this system has
  never done.** **The cost has been zero because the sleeve is empty. That is luck, not a control.**
  ⚠ **Do not read a clean close run as a passing test of the mark machinery.**
  ⚠⚠ **AND THE OTHER HALF OF THE MACHINERY IS IN THE SAME STATE, WHICH IS THE SHARPER HALF: THE CLOSE
  ROUTINE *WRITES* THE MARK, BUT ROUTINE 3's STEP 2 IS THE SEAT THAT *DETECTS* A MISSED WRITE AND BACKFILLS
  IT — AND IT HAS NOW REACHED THAT STEP AND SKIPPED IT, WITH NO OPERAND on a **FOURTH** CONSECUTIVE DAY
  (10-01 12:41, the detector's own seat).** ⚠ **The detector's entire input is a `(as of …)` date compared against the last
  trading day. There is no field, so there is no date, so NO STALENESS COULD BE DETECTED AND NONE WAS RULED
  OUT.** ⚠⚠ **A detector handed no input returns the same silence as a detector finding everything healthy —
  so BOTH THE WRITING SEAT AND THE DETECTING SEAT HAVE A CONFIRMED BLIND SPOT OF EXACTLY THE SAME SHAPE, AND
  NEITHER HAS EVER RUN AGAINST A REAL MARK. THE FIRST SATELLITE FILL ARMS BOTH AT ONCE.**

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

- **⚠ HIGH-WATER MARKS: NOTHING TO RECORD AND NOTHING WAS SKIPPED — BUT 10-01's MIDDAY SEAT IS THE DETECTOR
  ITSELF, AND ITS SILENCE IS THE LEAST INFORMATIVE OF ALL BECAUSE IT WAS HANDED NO INPUT.** The detector
  reads an `(as of …)` date against the last trading day; there is no field, so no date, so **no staleness
  was detected and none was ruled out.**
  *(The strongest statement of this item remains the 09-30 CLOSE's: the WRITING seat, holding a complete
  official 700.605 close at the moment it had nothing to stamp it onto.)*

- **⚠⚠ THE PARTIAL-BAR WARNING HAS NOW BEEN TESTED BY THE SEAT THAT EVERY PRIOR INSTANCE NAMED AS THE
  DANGEROUS ONE — ROUTINE 3 AT MIDDAY — AND ITS TWO HALVES GRADED OPPOSITELY. THIS REPLACES THE OLD "a
  partial bar does not look like a stub" FORM; A CORRECTION REPLACES THE CLAIM IT CORRECTS.**
  Read at **12:41, ~3h12m into a 6.5h session**, on VOO.
  ⚠ **THE PRICE HALF IS CONFIRMED AND IT IS THE DANGEROUS HALF:** today's partial bar read **`c` 700.35** —
  **26 cents** from 09-30's official **700.605**, mid-range against a trailing **691.44–710.93** band. **A
  wholly plausible close carrying no warning of any kind.**
  ⚠⚠ **AND THE MECHANISM IS NOW VISIBLE RATHER THAN SUSPECTED: `c` 700.35 EQUALS `latestTrade.p` 700.35 TO
  THE CENT. THE PARTIAL BAR'S CLOSE FIELD IS THE LAST TRADE SO FAR WEARING A CLOSE'S CLOTHES.** A §5.4 mark
  stamped from it records an intraday print as a high-water close and silently moves the stop.
  ⚠ **THE `n`/`v` HALF IS REFUTED AS STATED AND REPLACED BY A SHARPER DISCRIMINATOR.** `n` **982** / `v`
  **26,215** are **NOT "visibly tiny"** — they are **47.8%** and **43.0%** of 09-30's completed bar, so the
  09:37-seat version of the test (a glance) would **not** have caught this. But across the **24 completed
  sessions** in the trailing 25-day window the **minimum `n` is 1,450** and the **minimum `v` is 43,730**, so
  today's partial sat **BELOW THE FLOOR OF EVERY COMPLETED SESSION ON BOTH FIELDS.** ⚠ **The usable test is
  therefore NOT "is `n` small" but "IS `n` BELOW THE TRAILING COMPLETED-SESSION MINIMUM" — a comparison
  against a distribution, not a glance.**
  ⚠⚠ **STATED LIMIT, AND IT IS FALSIFIABLE: THE FLOOR TEST MUST FAIL ON A HALF-DAY SESSION** (day after
  Thanksgiving, Christmas Eve), where a **completed** bar legitimately carries roughly half the usual `n`/`v`
  and would read as partial. **The next early close is the test.** ⚠ **THE CLOCK REMAINS THE ONLY SOUND
  DISCRIMINATOR. The floor test is a corroborant, never the primary — and no `bars` close may be stamped as
  a mark before the bell on any basis.**

  `positions.md` carries **zero satellite blocks**, so `highest_close` is **ABSENT — the third state, carrying
  no `(as of …)` date at all.** ⚠ **Do not read a missing stamp as a failed close run: there is no field, so
  there was nothing to write. DO NOT BACKFILL ANYTHING.** **§5.4 is NOT ARMED**; it arms on the first
  **satellite** fill, and the 09-03 core fill was not one. §5.3's distance is **UNDEFINED, not large.**
  ⚠ **The distinction is FREE today and stops being free the moment a satellite fill lands** — after that, a
  mark silently not written reads identically to a mark correctly unchanged, and **only the `(as of …)` date
  separates them. Compare the date; never infer from the field's emptiness.** ⚠ **AND WHEN IT ARMS, NO
  BACKFILL MAY TAKE ITS MAX FROM A BAR DATED TODAY WHILE THE MARKET IS OPEN, NOR FROM A DIFFERENT ADJUSTMENT
  BASIS THAN THE ONE IT IS COMPARED AGAINST.** **§5.1–§5.4 have never had an operand in this account's entire
  history: 21 completed sessions since 2026-09-01, 18 after the 09-03 core fill, zero satellite positions
  ever** *(re-derived from a fresh 45-session `bars` pull at the 09-30 close)*. ⚠⚠ **NEITHER 10-01 SEAT ADVANCED THE COUNTER AND BOTH DECLINED FOR THE SAME REASON: at 08:24 the market had
  not opened and at 09:37 today was IN PROGRESS — in neither case is today a COMPLETED session, and neither
  seat has any of today's to add. It stays 21/18.** ⚠⚠ **THE 09:37 DECLINE IS THE ONE WORTH RECORDING,
  BECAUSE CATCH (11) NAMES ROUTINES 1 AND 2 AS BOTH EXPOSED AND 10-01 IS THE FIRST TIME ROUTINE 2 REACHED
  THAT DECISION. It was taken from the CLOCK, not from the inherited sentence — which is exactly the
  distinction catch (6) is about: the right number by an unchecked route is not a checked fact.**

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
  not reached, because the run containing it did not execute. THE GATE REMAINS UNTESTED CODE — the 10-01 open
  exercised it for the THIRTY-FIRST time (plan_date 2026-10-01 against a COMPUTED et_today 2026-10-01) and it
  did NOT fire, so its alert path is still never-run code.** ⚠⚠ **AND THE 10-01 OPEN NAMED THE REASON THAT
  MATTERS: A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. Freshness
  must be read OFF `plan_date` and NEVER inferred from the outcome.**

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD, AND THAT IS A RESULT RATHER THAN
  AN EMPTY SEARCH. THREE SESSIONS IN FOUR NOW.** 09-29: four of five names returned *"No other company's
  revenue or costs are identified as directly affected in the available source material."* 09-30: the F/A-XX
  funnel **asked directly** whether a US-listed supplier had been named and was told none had. **10-01: the
  Micron capex funnel got the strongest wording yet — *"no publicly traded U.S. semiconductor-equipment
  supplier, construction company, or materials vendor was explicitly named as a direct beneficiary… Naming
  companies such as equipment manufacturers, engineering contractors, or materials suppliers based only on
  industry fit would be an inference, not an explicit source linkage."***
  ⚠ **That is not an under-searched funnel. It is the source volunteering the absence of a Company B — and
  in 10-01's case, volunteering the EPISTEMIC RULE as well.**
  ⚠⚠ **A run that then produces one has supplied it from its own priors, which is verbatim the failure §4's
  honest-broker paragraph describes.** ⚠⚠ **AND 10-01 IS THE SHARPEST INSTANCE ON RECORD BECAUSE THE PRIORS
  WERE READY AND SPECIFIC: APPLIED MATERIALS, LAM RESEARCH, KLA.** ⚠ **Each is a fact about the INDUSTRY,
  not about this transaction. Recognise this shape on sight: when the source says no counterparty is
  identified, the correct next action is to WRITE THAT DOWN, not to go looking for one in a differently-worded
  query. NO RE-QUERY WAS ISSUED on any of the three occasions.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR JUDGMENT
  RATHER THAN CARE. 93 REAL THESES, ZERO ACCEPTED EVER** (94 `### T-` headings less the template, recounted
  from source on 10-01 with `grep -c`). **20 this week, ALL REJECTED.** Set beside that: an empty satellite
  sleeve, **~30% idle cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker, and an account at
  **−0.6077% since inception on official closes** (−0.4272% carrying the receivable). ⚠⚠ **A LOSING ACCOUNT
  RAISES THE PULL IN A NEW WAY AND THE DISTINCTION STILL HOLDS: the book is down because it holds ~70% of a
  market that fell, and it BEAT that market again on 09-30, by exactly the cash weight, for the eighteenth
  session in eighteen. "Deploy something" is not what these numbers argue for; they argue that the sleeve has
  no effect in EITHER direction.** ⚠ **09-25 remains the sharpest evidence: the funnel finally produced the
  well-sourced, named-supplier, allocated-figure candidate that a month of rejections implied was the missing
  ingredient — AND IT WAS STILL NOT A TRADE. That is evidence the bar is not what is binding, NOT evidence
  the bar should move.** §4's own position governs: a run that finds nothing is a successful run. **Naming the
  pull is the only defence against acting on it.** If the bar is to move, that is a `strategy.md` change and
  **only the human may make it.**
  ⚠⚠ **AND 10-01's OPEN IS WHERE THAT PRESSURE ACTUALLY HAD TEETH, FOR THE FIRST TIME IN A SEAT THAT COULD
  HAVE SUBMITTED AN ORDER: every gate was OPEN — breaker INACTIVE, week 0 of 3, sleeve empty, 30.11% idle
  cash, $4,982.10 of headroom under the 5% cap, `control.md` notes (none), `TRADING_ENABLED: true` — and
  ZERO ORDERS WERE PLACED, because the plan carried no intent and this seat may not generate one.**
  ⚠ **"Nothing was blocked" and "nothing was bought" are both true, and the second follows from the PLAN, not
  from a guardrail. A position opened at 09:37 without a plan entry routes AROUND the discipline rather than
  satisfying it.**
  ⚠ **WHERE THIS WEEK'S 20 DIED, BY THE DURABLE KILL: part 1 = 5, part 2 = 2, part 3 = 7, §3 = 3,
  premise/structure = 3**, with one (SMMT) dying three times over. ⚠⚠ **PART 3 IS NOW THE LARGEST SINGLE
  CATEGORY THIS WEEK, AND 10-01 IS WHY — FOUR OF ITS SIX DIED THERE.** ⚠ **Do NOT read that as a trend: it
  reflects WHICH EVENTS the tape offered (a 2028 cleanroom, an undisclosed delivery schedule, a reactor
  framework, an FY2028 capacity plan), not a change in how the funnel screens.**
  **10-01's six: T-01 Micron capex part 3 · T-02 AMD part 3 (not establishable) · T-03 SNPS/AWS structure ·
  T-04 US–Korea reactors part 3 · T-05 MTUS §3 · T-06 CALM part 3.**
  ⚠⚠ **AND THE SINGLE MOST DECISION-RELEVANT DATUM THIS WEEK IS NOW T-2026-10-01-02 (AMD), WHICH DISPLACES
  NOTHING BUT ADDS A THIRD INDEPENDENT INSTANCE: IT IS THE FIRST ENTRY IN THIS LOG WHOSE PART 1 PASSED
  CLEANLY.** One clause, no "and also", a signed order, a disclosed figure, a named platform, a named
  US-listed beneficiary. ⚠ **It died on parts 2 and 3 — and, noticed LATE, on being co-named in the
  headline.** ⚠ **Set beside JBL (09-25, killed by a disclosed ZERO MARGIN) and ABBV (09-30, killed by
  MAGNITUDE alone), that is three candidates clearing the evidence bar and failing on three DIFFERENT parts.
  The binding constraint is NOT the evidence bar, and the three failing differently is what makes the set
  informative rather than repetitive.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY.** ⚠ **10-01's six rejections do NOT become a
  queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE, and 09-30's eight and 09-29's six stay
  disposed too.** **Micron FY2027 capex chain** (part 3 — majority **construction** capex to accelerate
  **cleanroom availability in late calendar 2028 and beyond**, durable even if a supplier is named later;
  rule (v) second — ⚠ **and the answer this run nearly supplied from its own priors was AMAT, LRCX and KLA,
  which the source closes explicitly**) · **AMD / the HPE-Vultr $1.2B Helios order** (part 3 **not
  establishable** — no delivery schedule, duration or recognition timing anywhere; part 2 second — AMD's
  share of the $1.2B disclosed by nobody; ⚠ **and AMD is CO-NAMED IN THE HEADLINE, so it is not obviously a
  Company B at all**) · **SNPS / AWS $1B+** (structure — SNPS is the named beneficiary and **Amazon is the
  PAYER**, so no second party remains) · **US–Korea eight-reactor framework** (part 3, rule (vi) — a
  framework *contemplating* reactors; Westinghouse is not independently US-listed and **CCJ is not the way
  in**) · **MTUS** (§3 outright, **~$0.79B against a $10B floor**, plus rule (v)'s **ceiling** sub-shape) ·
  **CALM** (part 3 — through **H1 fiscal 2028**; part 2 — no figure of any kind; ⚠ **§3 ATTEMPTED AND
  UNRESOLVED, so §3 is UNDECIDED on CALM in either direction and must not be inherited as passing**).
  ⚠ **AND NOTHING EARLIER WAS REHABILITATED EITHER** — zero `move`, `quote`, `bars` or `asset` calls on JBL
  (which appeared in a citation at **−6.68%** and was not reached for), AKAM, RDW, FLNC, IOVA, SMMT, CRK,
  AIR, ABBV, RARE, LLY, CI, Lenovo or any memory supplier. **A rejection is not a queue.** ⚠ **One §3
  question remains reached-but-undecided: Shopify is a Canadian issuer trading as common stock on a US
  exchange, which §3's "US-listed common stock" does not obviously settle. A future run reaching this with a
  LIVE candidate must put it to the human rather than decide it from that seat.**

- **⚠⚠ NEW ON 09-30, AND IT IS A STRUCTURAL FINDING ABOUT THE FUNNEL RATHER THAN ABOUT A CANDIDATE: US
  DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE, AND TWO CONSECUTIVE SESSIONS NOW SAY SO.**
  **09-29: a $20.7B AMRAAM multiyear award to RTX — four named CONTRACT LINE CATEGORIES, not one
  subcontractor named or allocated a dollar. 09-30: a >$20B F/A-XX full-scale-development award to Boeing —
  the funnel asked DIRECTLY whether any US-listed supplier had been named, and the source answered that none
  had.** ⚠ **Different prime, different program, different service, same kill.** ⚠⚠ **THE MECHANISM IS
  DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below it is commercially
  confidential, so the dollars are never allocated to a named public company.** ⚠⚠ **10-01 IS THE FIRST SESSION TO ACT ON THIS ITEM AS WRITTEN: the F/A-XX award was still in the
  overnight scan, and ZERO Perplexity queries were issued on it. The item was USED, not merely re-read.**
  ⚠ **CONSEQUENCE FOR A FUTURE
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
  ⚠⚠ **THE THIRD STATE — EXERCISED AND NON-DECISIVE — HAS NOW HAPPENED TWICE RUNNING, SO IT IS A STANDING
  STATE AND NOT A ONE-DAY CURIOSITY.** 09-30: **ABBV −0.78%** and **RARE −1.83%**, both `false`, neither
  rejection turning on them. **10-01: THREE calls — AMD −0.52% (614.84 → 611.65), HPE +2.50% (62.34 →
  63.90), MU −0.50% (1072.18 → 1066.85) — all three `false`, and NOT ONE rejection turned on any of them.**
  ⚠ **AMD and MU BOTH PASSED BY FALLING, which is defect shape one (sign-blindness) in its mild, passing
  form.** ⚠ **AMD is the one to remember: a name co-named in a $1.2B AI-order headline, printing −0.52% over
  five sessions, is precisely the reading that invites a "the market has not noticed" story. THAT STORY WAS
  NOT WRITTEN.** ⚠ **A run reporting "priced-in: pass" must say WHICH of the three states it means.**
  ⚠⚠ **AND HPE IS A FRESH INSTANCE OF OPEN ITEM (2) — THE WINDOW MASKING AN EVENT MOVE — GRADED HONESTLY AS
  MILD.** Five sessions read **+2.50%**, while the **news day alone ran 61.51 → 63.90 = +3.886%** and the
  window swept up a prior **−3.187%** slide (09-24 63.535 → 09-29 61.51). ⚠ **This is WEAKER than AKAM:
  even the uncancelled event move (+3.886%) was still BELOW the 4% threshold, so the filter would have passed
  HPE on the news day too. The window hid ~1.4pp and changed NO verdict.** ⚠ **Recorded as mild, because a
  loud warning whose instances are all mild teaches a future run that the shortcut is safe.**

- **⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.**
  Two routines read `is_open: true` and can pull a live partial bar: **routine 2 at 09:35 and routine 3 at
  12:30.**
  ⚠⚠ **10-01's OPEN SUPPLIES AN INSTANCE AND IT IS HONESTLY GRADED AS *NOT* TESTING THE WARNING, WHICH IS
  THE POINT OF RECORDING IT.** At **09:37** the today-bar read **c 703.15, n 72, v 2529** against the 09-30
  bar's 2053/61032 — **seven minutes in, `n` and `v` ARE visibly tiny, so the "it does not look like a stub"
  half of this warning was never under strain here.** ⚠ **The dangerous seat is still routine 3 at 12:30, and
  no number from a 09:37 seat may be read as evidence about it.**
  ⚠ **BUT THE OTHER HALF DID HOLD, AND IT IS THE HALF THAT WOULD FOOL A READER: `c` 703.15 sits INSIDE
  yesterday's 700.605–707.20 range and is a completely plausible price. THE PRICE CARRIES NO WARNING AT ALL.**
  ⚠ **Its one legitimate use was taken: the bar's EXISTENCE, where the 08:24 pre-market run found none,
  corroborated `is_open: true` from the data plane. Existence is evidence about the SESSION; the close field
  is not evidence about the PRICE until the bell.** ⚠ **The midday case is the dangerous one: at 12:41 on 09-25 the partial read c 710.555, n 1,731,
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
  **MOST RECENT OFFICIAL/PRICE BASIS (`bars --adjustment all`, the complete 2026-09-30 session,
  RE-PULLED FRESH ON 10-01: o 704.52 h 707.20 l 700.605 c 700.605 n 2053 v 61032): equity $99,392.34,
  core $69,392.34 = 69.8166%, cash 30.1834%, day −$164.91 / −0.1656% from 09-29's $99,557.25, since
  inception −$607.66 / −0.6077%. TOTAL-RETURN BASIS carrying the inferred ~$180.45 receivable:
  ~$99,572.79, since inception −0.4272%.**
  **BROKER MARK at 10-01 09:37 (MARKET OPEN, NOT A CLOSE): equity $99,641.94, core $69,641.937584 =
  69.8922%, cash 30.1078%, `current_price` 703.125, core `unrealized_pl` −$358.05 / −0.512% against the
  706.74 RAW fill, `rebalance_delta` +$107.42 — a NINTH consecutive positive reading and NOT the sign defect
  resolving (the same quantity disagreed in sign on 09-24).** *(Earlier the same day, 08:24 PRE-MARKET:
  equity $99,681.06, core 69.9040%, `rebalance_delta` +$95.68. ⚠ **Two broker marks from the same day are
  still two different calls at two different times and must not be differenced against each other either.**)*
  ⚠ **The broker figure is a LIVE MIDPOINT and must never be differenced against a close figure.** **Prior
  closes for reference: 09-29 $99,557.25 / core 69.8666%; 09-28 $99,688.98 / core 69.9064%.**
  ⚠⚠ **THE WORKED INSTANCE OF THE MIXED-BASIS TRAP, FROM THE 09-30 CLOSE AND STILL THE ONE TO REACH FOR:
  differencing the BROKER $99,505.75 against 09-29's OFFICIAL $99,557.25 gave −$51.50 / −0.0517%, a
  THREEFOLD UNDERSTATEMENT of the true −$164.91 / −0.1656%.**
  ⚠⚠ **AND 10-01 SUPPLIES A SECOND, DIFFERENT SHAPE OF THE SAME TRAP, DECLINED: core `current_price` reads
  703.52 at 08:24, i.e. **+$2.915 above the 700.605 official close** — NEARLY TRIPLE the largest of the nine
  catalogued POST-BELL gaps (range −$0.97 to +$1.145). IT WAS NOT APPENDED TO THAT SERIES.** ⚠ **Those nine
  are all post-bell; this is a PRE-MARKET indication on a morning when a softer August PCE lifted futures.
  Appending it would have produced a spurious "largest gap on record" by nearly 3x — an artifact of mixing
  two TIMES OF DAY, not evidence of any widening.** ⚠ **DIFFERENT HOUR, DIFFERENT SERIES. The post-bell
  series still has NINE members and its largest is still +$1.145.**
  ⚠⚠ **`equity − last_equity` REMAINS UNUSABLE, NOT IMPRECISE — its largest artifact on record is 09-30's
  −$94.59 (−$70.32 printed against a real −$164.91), nearly three times 09-28's −$33.19.**
  ⚠ **Fifty-fifth consecutive run inside 69.59–70.22.**
  ⚠⚠ **THE INTRADAY-DRIFT ITEM GOT AN EIGHTH INSTANCE: `selftest` reported $99,625.59 at 09:36 and `sleeves`
  and `account` BOTH returned $99,641.94 at 09:37 — a $16.35 spread.** ⚠ **Well inside the established
  $1.97–$216.91 range, so it is NOT evidence of anything narrowing, and the range still has no stable size.**
  ⚠ **An intraday equity figure is only meaningful with its CALL and its TIMESTAMP attached, and two figures
  from different calls must never be differenced.** ⚠⚠ **THIS BITES §6's 5% SIZING CAP, WHICH IS COMPUTED
  AGAINST LIVE EQUITY — 5% of the 09:37 mark is $4,982.10. IT HAS NO OPERAND ONLY BECAUSE NO PLAN HAS EVER
  CARRIED A BUY INTENT.**
  **NO REBALANCE WAS DUE AND NONE WAS PLACED** — §2 acts at the **65/75 band edge** and core sat **4.892
  points** inside the 65 edge and **5.108** from the 75 edge at 09:37 (4.82 inside on the 09-30 official
  close). ⚠⚠ **§2 NAMES THE MARKET-OPEN RUN AS THE SEAT THAT REBALANCES, AND THE 10-01 OPEN *WAS* THAT SEAT:
  it reached the decision with the authority to act and declined ON THE BAND. That is the only action §2
  authorises there — declining because the band holds is a DECISION, not an omission.**
  ⚠ **AUDIT ANY SUPERLATIVE BEFORE REPEATING IT.** On **price**, 09-28's −0.7010% **IS** the largest
  single-day loss on record; on **total return** it is **−0.5212%, SECOND**, behind 09-23's −0.5327%.
  **09-30's −0.1656% is not notable in either direction.** Since inception **−0.6077% is NOT a low** — 09-16
  reached −1.3396%, 09-15 −1.0350%, 09-10 −0.9954%. *(Grounded from a 45-session pull whose rows before the
  09-03 fill are **COUNTERFACTUAL** — the account held $100,000 cash — and must never be read as account
  history.)*

- **⚠⚠ NEW ON 10-01: A COMPLETED DAILY BAR IS NOT IMMUTABLE IN `n` AND `v`, WHICH MAKES AN ALREADY-WEAK
  SIGNAL WEAKER STILL.** The 2026-09-30 bar read **n 2050 / v 61014** to the 16:16 close run and reads
  **n 2053 / v 61032** on 10-01's fresh pull — **while its CLOSE held at 700.605 to the cent.**
  ⚠ **Late-reported prints keep arriving after the bell, so `n`/`v` drift on a bar that is genuinely
  complete.** ⚠⚠ **CONSEQUENCE: the standing warning said `n`/`v` are only a SMELL TEST for completeness.
  They are weaker than that — they are not even STABLE on a complete bar, so a run cannot use "v changed"
  or "v is low" as evidence in either direction.** ⚠ **The CLOSE is the stable field. The CLOCK is the
  reliable discriminator, and post-bell the confirming check is that a bar for today EXISTS and its close
  matches the 15:59 `latestTrade`.**

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`, NEVER a
  `positions` field for a close or an execution reference. Close-to-close from `bars` (⚠ a COMPLETED
  session's bar, ⚠ and STATE THE ADJUSTMENT), a fresh `quote` for execution.** ⚠ **09-28: broker
  `equity − last_equity` = −$736.91 against a real price-basis move of −$703.72 — artifact −$33.19.**
  ⚠⚠ **09-30 IS THE LARGEST INSTANCE ON RECORD AND NEARLY TRIPLES IT: −$70.32 against a real −$164.91, an
  artifact of −$94.59, with `last_equity` reading 99,576.07178732826 against an official prior-close equity
  of 99,557.25. The field is UNUSABLE, not imprecise.**
  ⚠⚠ **AND ON 10-01 AT 09:37 THE ARTIFACT STOPPED BEING MEASURED AND BECAME *ATTRIBUTED*, EXACTLY. THIS IS
  THE ONE PIECE OF THIS ITEM THAT IS NOW SETTLED.** `last_equity` **99,417.59768935866** equals
  **qty 99.046311231 × `lastday_price` 700.86 + cash 30,000** with a residual of **0E−11** — i.e. to eleven
  decimal places, exactly. And `last_equity` minus the official-close equity (qty × 700.605 + cash =
  **99,392.340879994755**) is **$25.256809363905**, which is **exactly qty × the $0.255 gap between
  `lastday_price` 700.86 and the 700.605 official close.** ⚠⚠ **SO THE ARTIFACT IS NEITHER NOISE NOR
  IMPRECISION: IT IS `lastday_price` NOT BEING THE OFFICIAL CLOSE, PROPAGATED THROUGH ONE MULTIPLICATION.
  Every instance in the series above is that one substitution, at that day's gap, times the share count.**
  ⚠ **CONSEQUENCE, AND IT IS THE SAME CONCLUSION BY A CHECKED ROUTE: the field stays UNUSABLE as a day's P&L
  — but it is now unusable for a NAMED reason, so a future run need not re-measure it.** ⚠ **`change_today`
  (0.00323 at 09:37) sits on the SAME broker basis for the SAME reason and is not a day return either.**
  ⚠⚠ **WHAT IS EXPRESSLY *NOT* CLAIMED, AND THE DISTINCTION IS THE WHOLE DISCIPLINE: this does NOT re-open
  WHY `lastday_price` reads 700.86. Four mechanisms for that are already falsified and the item below says
  STOP PREDICTING IT. AN ARITHMETIC IDENTITY BETWEEN TWO BROKER FIELDS AND A MECHANISM FOR ONE OF THEIR
  VALUES ARE DIFFERENT CLAIMS; only the first is made, and it needs no mechanism to be true.**
  ⚠ **The same arithmetic also returned an UNINHERITED CONFIRMATION: qty × 700.605 + cash reproduces the
  09-30 close run's **$99,392.34** to the cent from a FRESH `positions` pull, so that figure is a CHECKED
  fact rather than a carried one.**
  ⚠ **`lastday_price` is CLOSED as a question — four falsified mechanisms, both signs observed. It reads
  **702.46** all day on 09-30 against an actual 09-29 close of 702.27 on BOTH bases; that is the SAME
  reading every 09-30 seat saw, so it is one observation and NOT a new miss. STOP PREDICTING IT; DO NOT
  RE-OPEN IT.** **Post-bell `current_price` minus official close, NINE observations: +$1.13, −$0.22,
  +$0.169, +$0.02, −$0.97, −$0.054, −$0.25, +$0.45, and +$1.145 on 09-30 (701.75 at 16:16:08 against a
  700.605 close).** ⚠⚠ **+$1.145 IS THE LARGEST OF THE NINE BY ONE AND A HALF CENTS, WHICH IS NOISE. "The
  broker/official gap is widening" was available, fluent and UNSUPPORTED, and was declined.**
  **Both signs, no predictable sign, no correctable offset.** **Keep writing falsifiable predictions down in
  advance for LIVE questions** — there is one on the dividend credit, above.

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 18 OF 18 AND STILL HAS NO EXCEPTION.** **09-30: VOO −0.2371%
  (`--adjustment all`, completed closes, and no dividend sits inside this window because the 09-28 ex-date
  preceded both sessions), the book −0.1656% on the same basis, excess +0.0714pp — against +0.0714pp
  PREDICTED by holding 69.8666% core and the rest in idle cash. Agreement to 0.0000pp.** The satellite sleeve
  contributed **exactly 0.0000%**, as it has for the account's entire history. ⚠⚠ **The 09-25 weekly review
  recomputed all 15 post-fill sessions from official closes and found PERFECT separation: every VOO-down day
  positive excess, every VOO-up day negative, one flat day exactly 0.0000pp. 09-30 is the TWELFTH VOO-down
  day — 18 of 18 sessions.** ⚠ **That is not a performance statistic — it is the signature of a book with ONE
  long position at ~70% weight and NO SECOND SOURCE OF RETURN.** ⚠⚠ **A TIGHT FIT IS NOT CONFIRMATION: the
  model fits to 0.0000pp because there is nothing in the book the model omits.** ⚠⚠ **AND A LOSING DAY IN
  DOLLARS BEING A POSITIVE-EXCESS DAY IS THE SAME FACT AS 09-25's GOOD DAY BEING A NEGATIVE-EXCESS ONE.
  Neither is skill.**
  ⚠ **THE TRAP, and the standing same-source rule does NOT catch it: comparing the book's PRICE basis against
  VOO's `--adjustment all` gave a spurious +0.0438pp on 09-28, because one leg excluded the dividend and the
  other included it. BOTH LEGS WERE FROM `bars --adjustment all` — the mismatch is between the ACCOUNT and the
  BENCHMARK recognising the same cash on DIFFERENT DATES.** ⚠ **It does NOT bite on 09-29 or 09-30, because no
  dividend falls inside either window on either leg. It bites again on the next ex-date.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — ELEVEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  ⚠⚠ **09-30's CLOSE ADDS NO TWELFTH CATCH BUT SUPPLIES THE CLEANEST LIVE INSTANCE OF (6)'s SHAPE:** that run
  advanced the session counter **20/17 → 21/18**, and the justification it first reached for was *"catch (11)
  says routine 4 is not exposed to the pre-market increment error."* ⚠ **That is a claim about the SYSTEM'S
  OWN SHAPE, which is precisely catch (6) — the shape no data call ever contradicts.** **What actually makes
  the increment safe is that the SESSION IS COMPLETE**, established from a 2026-09-30 bar that exists plus a
  15:59:59 `latestTrade` matching its close; the figures were then **re-derived from a fresh 45-session
  `bars` pull.** ⚠ **The conclusion was right and the reason was not. A correct number reached by an
  unchecked route is not a checked fact.**
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

- **⚠ GNRC IS NOT YOURS TO LOOK AT — THIRTY-FOUR CONSECUTIVE REFUSALS.**
  ⚠ **10-01's OPEN IS THE WEAKEST INSTANCE THE COUNT HAS EVER TAKEN AND IT IS LOGGED AS SUCH: this seat has
  NO FUNNEL AT ALL — it may only execute intents written before the bell — so the refusal was not merely free,
  it was STRUCTURALLY UNAVAILABLE. A refusal that could not have been violated is not evidence of restraint.** ⚠ **Graded honestly: the 09-30 MIDDAY and CLOSE runs both made ZERO `move` and ZERO `quote` calls on GNRC,
  but neither seat has a funnel — routine 3 is exits-only and routine 4 does not trade at all — so both
  refusals were FREE. TWO MORE WEAK INSTANCES, and the count is doing less work than it looks.** The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon
  announcement — first-order, outside §4 at any price** — and **open item (7) is resolved by a human editing
  §4 or `alpaca.py move`, not by a number this seat collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER
  EACH REFUSAL COST ANYTHING, AND MOST DID NOT. Quoting the bare count overstates the evidence.** The strong
  instances are the pre-market runs of 09-23, 09-24 and 09-25. ⚠ **No new costume in ten sessions; the list
  looks CONVERGING rather than growing.** Costumes: diligence, curiosity, tidiness, completeness,
  zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
  screen-already-running. **The pattern is the finding, not any instance. FREE IS NOT THE SAME AS
  PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — SIXTY RUNS.** §5 exempts core from all four
  sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **A CLOSE RUN IS THE STRONGEST INSTANCE THIS ITEM GETS, because it is the ONE SEAT THAT ACTUALLY WRITES
  MARKS and it is holding a complete, official close at the moment it declines to write one — 09-30's
  700.605 is the second consecutive close to be held and declined.** **Measure the core from the 706.74 fill and from an official close, never from a `positions`
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
  **(3)** The satellite sleeve is **structurally undeployed — 93 theses, zero positions, ever.** A 70/30 cash
  book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits the cash and §4 says
  most runs end in no trade — both rules were followed, and the agent must NOT respond by lowering the §4
  bar.** **The binding constraint now has SIX known forms:** the source withholds the counterparty's number;
  **or** the counterparty discloses **roadmap instead of segment revenue**; **or** the named beneficiary is
  **vertically integrated**; **or** **both parties expressly refuse to disclose as a commercial choice**
  (GM); **or** **the figure is fully disclosed and is the WRONG QUANTITY** (JBL); **or** **THERE IS NO
  COUNTERPARTY AT ALL** (IOVA: own product, own facility, no external supplier named anywhere); ⚠⚠ **or —
  SEVENTH, NEW ON 10-01 — EVERYTHING IS DISCLOSED AND THE SPENDING SIMPLY LANDS TOO FAR IN THE FUTURE**
  (Micron: a clean rule (iii) pass, $22B → $32B of its own commitments and ~$100B → ~$150B of its own RPO,
  with the capex aimed at **cleanroom availability in late calendar 2028 and beyond**). ⚠ **Only the first
  two are addressable by widening the evidence bar. Forms three through seven are not; form five would be
  made WORSE by widening it; and form seven is untouched by it, because the constraint is the CALENDAR.** ⚠ **ELMT is the standing proof that evidence is not the constraint.**
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
  weekly review: `86bc7vzam`; 09-28 daily summary: `86bc8yrz0`; 09-29 daily summary: `86bc9q3t5`;
  09-30 daily summary: `86bcak6yf`.**

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
  ⚠⚠ **FILE SIZE — FIFTEENTH CONSECUTIVE FLAG, AND THE REVIEW THAT FIXES IT IS TOMORROW.**
  `research_log.md` **~398KB** (grew this run), `journal.md` **~196KB**, `state.md` **~81KB**,
  `weekly_review.md` **147KB**. ⚠ **THE 2026-10-02 FRIDAY REVIEW MOVES THE WHOLE SEPTEMBER CORPUS INTO
  `archive/` IN ONE DESIGNED OPERATION AND IS NOW THE NEXT REVIEW DUE.** ⚠ **It is also the first monthly
  rollover this system has ever run, so its archive path is UNEXERCISED CODE — do not read fifteen quiet
  flags as evidence the rollover works.** **Do not re-litigate the sizes weekly; a human who disagrees
  should say so in `control.md`.**

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

⚠ **Earlier disposed rejects (09-21 to 09-24) remain disposed and are NOT re-listed here.** **ILMN, GRAL,
BBY, PYPL, SHOP, SoftBank/OpenAI, GIS, LH, CNC/MOH/OSCR, LHX, GFS, ACN, GPC/ORLY/LKQ, GM, BE, BG** — see
`research_log.md` for the working on each. **A rejection is not a queue.**
