# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-10-05 08:28 ET 1-premarket-research (selftest PASSED all five, trading_enabled true, LIVE paper; MONDAY PRE-MARKET CONFIRMED FROM THE DATE AND THE DATA PLANE - clock 08:28:54 is_open false with next_open 2026-10-05T09:30 pointing at TODAY, and bars returns a complete 2026-10-02 bar and NO bar dated today; NOT A HOLIDAY; THIS SEAT PLACES NO ORDERS, zero orders zero fills; LEDGER RECONCILES - one broker row core VOO 99.046311231 at 706.74 RAW against zero satellite blocks, THEY AGREE, and an agreeing ledger and an empty ledger are the same artifact so this is the ABSENCE OF A TEST not a clean bill; SEVEN THESES WRITTEN AND ALL SEVEN REJECTED, total 105 recounted from source as archive 87 plus live 18 with the template line excluded, ZERO EVER ACCEPTED; THE PLAN IS FRESH AND DELIBERATELY EMPTY, plan_date 2026-10-05, no BUY no SELL no REBALANCE; EVERY GATE WAS OPEN - breaker INACTIVE, weekly cap 0 of 3, sleeve 0 pct deployed, 30 pct idle cash, control notes none - so NOTHING STOPPED A BUY EXCEPT THE EVIDENCE; THE FINDING OF THE RUN IS A NEW COSTUME FOR RULE v - AN UNNAMED BIDDER WEARING A LEGAL PSEUDONYM, Synaptics filings call the competing bidder only PARTY A, one entity that definitely exists and acted on a dated day 2026-09-02 and is redacted on purpose, a blank with a shape a date and a motive and everything except a name, and the priors were instantly ready Microchip Skyworks Qorvo Renesas Infineon and NO GUESS WAS MADE; A REDACTION IS NOT A LEAD; SECOND FINDING - A WEEKEND WINDOW IS A WINDOW OF RE-REPORTING NOT OF EVENTS and recency day cannot tell the difference, the 5a scan returned a four-day-old 8-K as a weekend headline and rule iii caught it ONLY because the second query asked for the announcement DATE; THIRD - THE SECOND BROAD SCAN RETURNED ZERO NEW NAMES, every row already disposed or section 3 ineligible on sight and NOT ONE WAS RE-SCREENED; THREE VOLUNTEERED ABSENCES IN ONE RUN and FIVE CONSECUTIVE SESSIONS, reported with its count and NOT promoted to a new finding; ZERO move CALLS - the ABSENT state, the fourth, third instance after 09-29 and 10-02, and a decorative call was declined; I CAUGHT MY OWN SESSION COUNTER ERROR MID-RUN - wrote 24 and 21 for a weekend that adds no sessions, corrected to 23 and 20 IN FILE, catch 11 and catch 9 arriving together inside the run that holds them in its carry-forward; POSITIONS.MD COLLAPSED 68KB to 49KB minus 29 pct, eight per-run blocks from 10-01 and 10-02 folded to load-bearing facts, DISCHARGING human item 9; week_of 2026-10-05 VERIFIED as this ISO week's Monday from the date not inherited, new_positions_this_week 0; cash EXACTLY 30000.00 a NINETEENTH reading, VOO dividend DAY 6 OF 8 with TWO SESSIONS LEFT to 2026-10-07)

prior_run: 2026-10-02 16:46 ET 5-friday-weekly-review (FIFTH weekly review, ClickUp 86bcc4vph; THE SECTION 1 ANSWER IS NO - satellite 0.0000 pct against VOO total return PLUS 16.3118 pct over the rolling 12 months, excess MINUS 16.3118pp, sleeve 30000 cash for all 23 sessions; the weekly row went POSITIVE PLUS 0.2158pp and it is REFUTED NOT CELEBRATED because VOO FELL and week 4 predicted that in writing; account TR since inception PLUS 0.241168 pct vs VOO PLUS 0.608759 pct excess MINUS 0.367591pp; THE DIVIDEND NOW HAS A PRICE - 1.3254pp/yr, so the 70 pct core under-earns ~0.93pp/yr on top of the 4.89pp cash drag, a ~5.82pp ANNUAL HANDICAP BEFORE ANY DECISION; CATCH 13 - the 10-02 close run's LARGEST NEGATIVE EXCESS and BIGGEST UP-DAY are BOTH FALSE by more than 2x, 10-02 is 4th of 20 and 4th of 7 against 09-21's records, and the refuting number was already in week 4's own review; NEW STANDING RULE - a reject-board statistic may be REPORTED weekly and promoted to a FINDING only after holding across THREE consecutive reviews; MONTHLY ARCHIVE ROLLOVER, the first ever, live corpus 772KB to 212KB; daily separation 20 of 20 recomputed not inherited)

week_of: 2026-10-05
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.01
satellite_pct: 0.0
cash_pct: 29.99
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on forty-nine times.** **Everything below is LIVE. Nothing live was
discarded; settled items were folded to one line each and repeated emphasis was removed.**
⚠ **A run that adds nothing to this list is the normal case.**
⚠ **A correction REPLACES the claim it corrects — it does not sit beside it.**

---

### Live — act on these

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. DAY 6 OF 8, TWO SESSIONS LEFT (10-05, 10-06). CHECK `cash`
  EVERY RUN.** `cash` read **exactly $30,000.00** again at 10-05 08:28 — a **nineteenth** reading.
  ⚠ **Nineteen readings are ONE unresolved observation, and non-arrival this early is EXPECTED, not
  evidence — settlement runs on the PAY date.** ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE: `cash`
  should rise to about $30,180.76. IF IT HAS NOT BY 2026-10-07, the paper account does not model
  dividends at all.** The implied credit (**$1.825/share × 99.046311231**) is an **INFERENCE** — Alpaca
  does not publish it.
  ⚠⚠ **THE PRICE OF THE CONSEQUENCE, ESTABLISHED AND NOT RE-DERIVED: VOO's trailing 12 months is
  +16.3118% on `--adjustment all` against +14.9863% on `raw`, so DIVIDENDS ARE 1.3254pp/YEAR. If the
  account never collects them, the 70% core structurally under-earns ~0.93pp/yr, which on top of the
  4.89pp cash drag is a ~5.82pp ANNUAL HANDICAP BEFORE ANY DECISION.** ⚠ **A finding for the human,
  not something any seat can fix.** **The close run and tomorrow's pre-market are the last two seats
  that read `cash` before the test expires.**

- **⚠⚠ NEW COSTUME FOR RULE (v), AND IT IS THE MOST FILLABLE-LOOKING BLANK THIS FUNNEL HAS PRODUCED:
  AN UNNAMED *BIDDER* WEARING A LEGAL PSEUDONYM.** Synaptics' regulatory materials call the unsolicited
  competing bidder only **"Party A"** (proposal submitted **2026-09-02**; onsemi then restructured to
  all-cash $123/share, ~$5.7B, announced 10-01). ⚠ **Strictly worse than rule (v)'s unnamed SUPPLY
  BASE: a supply base is diffuse, but Party A is ONE entity that definitely exists, definitely acted on
  a dated day, and is definitely known to the filer and redacted ON PURPOSE. The blank has a shape, a
  date and a motive — everything except a name.**
  ⚠⚠ **THE PRIORS WERE INSTANTLY READY AND SPECIFIC, AS ALWAYS: Microchip, Skyworks, Qorvo, Renesas,
  Infineon. NO GUESS WAS MADE AND NONE IS RECORDED AS A CANDIDATE.** ⚠ **A REDACTION IS NOT A LEAD. If
  a future run meets "Party A", "Company X" or "a strategic party", the §4 answer is already written:
  there is no Company B until the filing names one.** *(Full entry: T-2026-10-05-01.)*

- **⚠⚠ A WEEKEND WINDOW IS A WINDOW OF RE-REPORTING, NOT OF EVENTS — AND `--recency day` CANNOT TELL
  THE DIFFERENCE. THE WORKED INSTANCE IS FROM THIS RUN.** The 5a scan, asked for "the last 24 hours
  (weekend of October 3-5)", returned the onsemi/Synaptics revision as a headline item; the targeted
  follow-up established it was **announced October 1** and merely re-reported Oct 2–5 — the source said
  so unprompted, in its first sentence. ⚠ **Rule (iii) caught it ONLY because the second query asked
  for the announcement DATE. The broad query's own framing presented a four-day-old 8-K as fresh.**
  ⚠⚠ **STANDING CONSEQUENCE, FOR EVERY MONDAY AND EVERY POST-HOLIDAY RUN: ASK FOR THE ANNOUNCEMENT DATE
  EXPLICITLY. A recency filter bounds when something was WRITTEN, never when it HAPPENED.**
  ⚠ **The companion Monday shape, also caught this run: a CORRECT `plan_today.md` arrives THREE calendar
  days old on a Monday. COMPARE `plan_date` TO THE LAST TRADING DAY, NOT TO THE CALENDAR — "not
  yesterday" is not evidence of a missed run.**

- **⚠⚠ CATCH (14) — I INCREMENTED A SESSION COUNTER FOR A WEEKEND, AND CAUGHT IT MYSELF MID-RUN. IT IS
  CATCH (11) AND CATCH (9) ARRIVING TOGETHER, INSIDE THE RUN THAT CARRIES BOTH IN ITS OWN
  CARRY-FORWARD.** This run first wrote **24 completed sessions / 21 post-fill** into `positions.md`,
  then corrected it **in file** to **23 / 20**. ⚠ **A WEEKEND ADDS NO SESSIONS.** The last completed
  session is 10-02, which Friday's close run already counted as the 23rd.
  ⚠⚠ **THE LESSON IS NOT "COUNT MORE CAREFULLY" — IT IS THAT READING THE WARNING DID NOT PREVENT THE
  ERROR. Catch (11) is stated verbatim three screens above where I wrote the wrong number, and catch
  (9)'s own note already says NAMING A FAILURE DOES NOT RETIRE IT. This is the second time that
  sentence has been proven by the run that read it** (week 4 was the first).
  ⚠ **The mechanism is specific and worth having: a counter advances on a COMPLETED SESSION, and the
  pull to advance it is strongest on the runs that add none — a pre-market seat and a Monday both
  stand in a period that feels like progress. CHECK WHAT THE UNIT IS BEFORE ADDING ONE.**
  **23 completed sessions since 2026-09-01, 20 post-fill, zero satellite positions ever.**

- **⚠⚠ THE SATELLITE SLEEVE IS STRUCTURALLY UNDEPLOYED — 23 SESSIONS, 105 THESES, ZERO POSITIONS EVER,
  AND THE PRESSURE TO LOWER THE §4 BAR IS THE ONLY ITEM HERE ASKING FOR JUDGMENT RATHER THAN CARE.**
  **Seven theses this run, all rejected; 105 total recounted from source (archive 87 + live 18, the
  template line excluded), ZERO EVER ACCEPTED.** Set beside: empty sleeve, **~30% idle cash**, weekly
  cap **0 of 3**, breaker INACTIVE, every gate open. **§2 permits the cash and §4 says most runs end in
  no trade — both rules were followed.**
  ⚠ **ONE SIDE OF THE ARGUMENT IS GONE: the book is NOT down, since inception is +0.2412% on a
  total-return basis, so "we are losing, deploy something" is unavailable — and it was never a §4
  argument.** ⚠ **The symmetric half is the stronger one: the identical structure lagged on all 7 up
  days and gained on all 12 down days. The sleeve has no effect in EITHER direction, and a run citing
  only the flattering half is quoting the flattering half.**
  ⚠⚠ **THE BINDING CONSTRAINT IS NOT THE EVIDENCE BAR — SEVEN KNOWN FORMS PLUS TWO SUB-SHAPES:** the
  source withholds the counterparty's number · the counterparty discloses **roadmap not segment
  revenue** · the beneficiary is **vertically integrated** (IOVA, and **EW this run**) · **both parties
  refuse to disclose commercially** (GM) · **the figure is disclosed and is the WRONG QUANTITY** (JBL
  $1.7B, 8-K-verbatim, capital paid in and repurchased at cost; **Morgan Stanley's $2.45B term loan
  this run**) · **THERE IS NO COUNTERPARTY AT ALL** (**Bayer's Ohio plant this run**) · **EVERYTHING IS
  DISCLOSED AND THE SPENDING LANDS TOO FAR OUT** (**Bayer's 2031/2034 now the record, roughly double
  Venture Global's 2030**). ⚠ **Sub-shapes: the transaction is in CAPACITY ALREADY BUILT (ORCL/Tencent);
  and the counterparty is NAMED BUT REDACTED ("Party A").**
  ⚠ **Only the first two are reachable by widening the bar; form five would be made WORSE by it; forms
  six and seven are untouched because the constraint is the CALENDAR or the absence of a second party.**
  **ABBV and ELMT are the standing proofs.** ⚠ **If the bar is to move, that is a `strategy.md` change
  and ONLY THE HUMAN may make it.**

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD — FIVE CONSECUTIVE SESSIONS,
  AND THREE VOLUNTEERED ABSENCES IN THIS RUN ALONE.** 09-29, 09-30, 10-01, 10-02 and 10-05 each
  returned one. **Today: the onsemi query answered "no identified third public-company revenue
  beneficiary or loser"; the regulatory query answered "No" for BOTH EW and BMY in its own table.**
  ⚠ **A volunteered absence is stronger than a silence.** ⚠⚠ **A run that then produces a Company B has
  supplied it from its own priors — verbatim the failure §4's honest-broker paragraph describes. THE
  PRIORS ARE ALWAYS READY AND ALWAYS SPECIFIC** (AMAT/LRCX/KLA for any fab headline; solid rocket
  motors for SM-6; GE Aerospace for F/A-XX; a valve-component supplier for EW; the GPU vendor for any
  AI-compute headline). ⚠ **Each is a fact about the INDUSTRY, not the TRANSACTION.**
  ⚠ **REPORTED WITH ITS COUNT AND NOT PROMOTED — this is a continuation of a standing item, not a new
  finding, and the three-consecutive-reviews rule governs promotion.**

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES AND A STANDING FOURTH STATE.**
  **Shape one — a DRAWDOWN misread as priced-in** (nine instances, newest CNC −6.44% → `true`; three
  near-misses cleared only because the *fall* was fractionally too small: LMT −3.61%, GM −3.95%, LH
  −3.83%). ⚠⚠ **LITE IS THE BILL: rejected on a −7.35% drawdown, it is +28.34pp vs VOO.** **Shape two —
  the filter working** on genuine news rises (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%). **Shape three —
  a genuine RISE UNRELATED TO THE NEWS swept up by the window** (JBL +4.97% on a grind whose news day
  moved it +0.63%). ⚠ **The defect is SIGN- and CAUSATION-BLINDNESS, not the threshold.**
  ⚠ **AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read `priced_in: false` at
  +3.19%** while its closes ran 104.53 → 117.435 (+12.35% in one session) → 110.44 (−6.74%) — a
  multi-session round trip netting to a passing figure. **HPE is a milder instance.**
  ⚠⚠ **THE FOURTH STATE — THE FILTER HAVING NOTHING TO FIRE ON — IS AS COMMON AS THE OTHERS. 09-29,
  10-02 AND 10-05 MADE ZERO `move` CALLS IN ANY SEAT.** ⚠ **That is an ABSENT check, not a skipped one,
  and the two look IDENTICAL in a run summary.** ⚠⚠ **10-05 ADDS THE REASON IT MUST STAY ABSENT: a
  decorative `move` call on a name with no mechanism would convert an honest absence into a fake
  exercise, and was declined for that reason. SYNA at +14.1% would have FAILED the filter had it
  reached it — shape two — and it never got there.** ⚠ **The EXERCISED-AND-NON-DECISIVE state also
  stands (09-30 ABBV/RARE; 10-01 AMD/HPE/MU).** ⚠ **A run reporting "priced-in: pass" must say WHICH
  state it means.** **Only a human may change §4 or `alpaca.py move`.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY. A REJECTION IS NOT A QUEUE.**
  ⚠⚠ **THE DISPOSED-REJECT CATALOGUE IS SPLIT: `archive/research_log/2026-09.md` holds 87 theses; the
  live `research_log.md` holds the 18 October entries. A run checking whether a name was already
  disposed MUST READ BOTH.**
  **10-05's seven, with the durable kill:** **onsemi/Synaptics + "Party A" + MS** (part 1 — no Company
  B; ON the acquirer and SYNA the target are both first-order, and buying a target at a fixed cash
  price is **merger arbitrage, which §4 does not contain a clause for**) · **Bayer $2.2B Ohio** (part 3
  — **2031/2034**) · **EW AUTUS valve** (part 1, volunteered absence, **vertically integrated**) ·
  **BMY Camzyos paediatric** (part 1, volunteered absence; **an EXPANDED INDICATION is the weakest
  approval shape — the drug is already being made, so no new line, no new supplier**) · **TSMC capex**
  (rule iii — an **earnings PREVIEW**, and the AMAT/LRCX/KLA chain already died 10-01) · **September
  payrolls** (no Company A) · **G7 diesel release** (source says **"not sufficiently verified"**; sign
  wrong for a long).
  ⚠⚠ **AND THE SECOND BROAD SCAN RETURNED ZERO NEW NAMES, WHICH IS A RESULT: every row was already
  disposed (Venture Global/ConocoPhillips 10-02, RTX SM-6 10-02, MTUS 10-01) or §3-ineligible on sight
  (Big Sky Industrial and Tiberius Aerospace — counterparty UNNAMED; Bharat Forge and Jindal Stainless —
  India-listed). NOT ONE WAS RE-SCREENED.**
  ⚠ **DO NOT REHABILITATE ANY EARLIER REJECT AT A DIFFERENT PRICE.** ⚠⚠ **ELMT IS THE LIVE TEST: it is
  +11.86pp vs VOO in six sessions and is STILL ineligible — §3 is a hard filter that does not weigh
  outcomes, and "but it went up" is a higher price, not new evidence. DO NOT SCREEN IT AGAIN.**
  ⚠ **One §3 question is reached-but-undecided: Shopify is a Canadian issuer trading as common stock on
  a US exchange. A future run reaching this with a LIVE candidate must put it to the human.**

- **⚠⚠ US DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE — FOUR INSTANCES, THREE PRIMES, THREE
  PROGRAMS. SETTLED, AND ACTED ON AS SETTLED FOR A THIRD SESSION.** 09-29 AMRAAM $20.7B (RTX) · 09-30
  F/A-XX >$20B (Boeing) · 10-02 SM-6 $24.4B (RTX, a **MAXIMUM POTENTIAL** value, not obligated).
  ⚠⚠ **THE MECHANISM IS DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below it
  is commercially confidential.** ⚠ **Spend ONE funnel query, then WRITE THE ANSWER DOWN AND STOP — do
  not re-word the query. NO RE-QUERY HAS EVER BEEN ISSUED; 09-30, 10-01, 10-02 and 10-05 all acted on
  this as written, and on 10-05 the SM-6 award returned in a scan and NO query was spent on it.**
  ⚠ **The prime is FIRST-ORDER and outside §4 at any price.**

- **⚠⚠ THE BROKER/OFFICIAL PRICE GAP IS A MOVING LIVE MIDPOINT, NOT AN OFFSET — SETTLED 10-02 BY A
  SAME-DAY PAIR.** At 16:16 `current_price` 707.82 sat **+$0.470** above the official 707.35; at 16:46
  it read **707.3246**, **−$0.0254** below it. **Same day, same official close, thirty minutes apart, a
  $0.4954/share swing that changed sign.** ⚠ **No fixed-offset reading survives that.**
  ⚠ **NEVER difference a broker mark against an official close. NEVER `equity − last_equity` as a day's
  P&L** (fully attributed: `last_equity` = qty × `lastday_price` + cash; on 10-02 it would have printed
  **+0.5441%** against the true **+0.5069%**, flattering the day). ⚠ **NEVER `unrealized_intraday_pl`
  or `change_today`.** **Close-to-close from `bars` on a COMPLETED session, adjustment STATED; a fresh
  `quote` for execution.** ⚠ **An equity figure is meaningless without its CALL and its TIMESTAMP.**
  ⚠ **Do NOT re-open WHY `lastday_price` differs from the close — four mechanisms falsified, both signs
  observed. STOP PREDICTING IT.**
  ⚠ **The PRE-MARKET gap is a DIFFERENT SERIES and must never be appended to the post-bell one. 10-05
  08:28 read `current_price` 707.13, −$0.22 against the official 707.35 — LOGGED AS PRE-MARKET AND NOT
  APPENDED.** ⚠ **This bites §6's 5% cap, computed against LIVE equity — 5% of the 08:28 mark is
  $5,001.93. It has no operand only because no plan has ever carried a buy intent.**

- **⚠⚠ EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
  VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close by **0.997432**; `raw` and
  `split` return the original series. **Both are correct; they are different bases.** 09-28 onward agree
  on both. ⚠ **10-02 is 707.35 on ALL THREE bases, so this week's fill-vs-close comparison is
  basis-clean — THAT IS A PROPERTY OF THIS WEEK, NOT A REPEAL. THE NEXT EX-DATE RESTORES THE TRAP.**
  ⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**
  ⚠⚠ **§5.4 IS THE REAL CASUALTY AND IT FAILS TOWARD SELLING:** a `highest_close` stamped pre-ex and
  compared against a post-ex adjusted close manufactures a **phantom drawdown equal to the dividend**.
  **THE FIX IS IN `positions.md`'s HEADER: same basis, same call — re-pull the whole window and take the
  max from that ONE pull.** ⚠ **The empty sleeve is the only reason this has cost nothing.**
  ⚠ **`voo_close_at_entry` is a LABEL, not a baseline.** ⚠ **A historical BOOK day-return is not exactly
  reproducible from a later pull once an ex-date intervenes (the cash leg does not rescale). Quote a
  day-return with its BASIS *and* its VINTAGE.**
  ⚠⚠ **AND THE §1 TRAP THE SAME-SOURCE RULE DOES NOT CATCH: comparing the book's PRICE basis against
  VOO's `--adjustment all`. BOTH LEGS CAN COME FROM `bars --adjustment all` AND STILL BE INCOMPARABLE,
  when the ACCOUNT and the BENCHMARK recognise the same cash on DIFFERENT DATES.** *(The 10-02 review is
  the worked instance: the mixed-basis week read −0.1152pp against the honest TR-vs-TR +0.0649pp.)*

- **⚠⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.
  TWO ROUTINES CAN PULL ONE: routine 2 at 09:35 and routine 3 at 12:30.**
  ⚠ **THE PRICE HALF IS CONFIRMED AND IS THE DANGEROUS HALF:** at 12:41 on 10-01 the partial bar's `c`
  700.35 equalled `latestTrade.p` to the cent. **A PARTIAL BAR'S CLOSE FIELD IS THE LAST TRADE SO FAR
  WEARING A CLOSE'S CLOTHES** — a plausible price carrying no warning. ⚠ **NO `bars` CLOSE MAY BE
  STAMPED AS A MARK BEFORE THE BELL ON ANY BASIS.**
  ⚠⚠ **THE `n`/`v` HALF IS NOW COMPLETE, AND 10-05 SUPPLIED THE MISSING SIDE: a completed bar's `n`/`v`
  drift SOMETIMES AND NOT ALWAYS.** 09-30 read 2050/61014 then 2053/61032 and 10-01 read 1633/51892
  then 1634/51893 (**closes held to the cent**), while **10-02 read 2,524/134,995 before and after a
  full weekend — identical.** ⚠⚠ **A FIELD THAT SOMETIMES MOVES ON A COMPLETE BAR IS UNUSABLE AS
  EVIDENCE IN EITHER DIRECTION: "it did not move this time" is not a validation any more than "it
  moved" was a refutation.**
  ⚠ **The FLOOR test ("is `n` below the trailing completed-session MINIMUM") is a corroborant on a
  moving ruler — the 12:41 partial's n/v were 47.8%/43.0% of the prior completed bar, i.e. NOT visibly
  tiny, and the floors themselves drift (1,450/43,730 → 1,560/45,031). A quiet, low-participation FULL
  session could land under the floor.** ⚠ **STATED LIMIT, STILL UNTESTED: the floor test MUST FAIL on a
  half-day session. The next early close is the test.**
  ⚠⚠ **THE CLOCK — PLUS, POST-BELL, A BAR DATED TODAY THAT EXISTS AND A ~15:59 `latestTrade` MATCHING
  ITS CLOSE — IS THE ONLY SOUND DISCRIMINATOR. The floor test is NEVER the primary.**
  ⚠ **`is_open: false` HAS THREE MEANINGS — pre-market, post-bell, holiday. READ `next_open`'s DATE,
  and prefer the data plane. `is_open: true` is the one case the boolean alone is sufficient.**

- **⚠⚠ STEP 2 HAVING NO OPERAND AND STEP 2 WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT. SIX
  CONSECUTIVE CLOSE RUNS.** The close routine stamps each open satellite position's official close into
  `highest_close`; routine 3's Step 2 **DETECTS** a missed write and backfills. **Every close run so far
  has had nothing to stamp, and "high-water marks updated" would have been FALSE. The honest form is:
  the job had NO OPERAND.** ⚠ **The every-day `(as of …)` date rule also has nothing to write, and the
  DETECTOR's entire input IS that date — so NO STALENESS COULD BE DETECTED AND NONE WAS RULED OUT. A
  detector handed no input returns the same silence as one finding everything healthy.**
  ⚠ **The only `highest_close` string in `positions.md` is the TEMPLATE PLACEHOLDER; the field is
  ABSENT, a third state carrying no date.** ⚠⚠ **BOTH SEATS HAVE A BLIND SPOT OF THE SAME SHAPE, NEITHER
  HAS EVER RUN AGAINST A REAL MARK, AND THE FIRST SATELLITE FILL ARMS BOTH AT ONCE.**
  ⚠ **THE BACKFILL PATH REMAINS UNEXERCISED CODE.** **09-28 proves that is not academic: it lost its
  close run, so with one position open 09-29's midday would have had to backfill ACROSS AN EX-DIVIDEND
  DATE.** ⚠ **DO NOT BACKFILL ANYTHING NOW — there is nothing to write.** ⚠ **When it arms: no backfill
  may take its max from a bar dated TODAY while the market is open, nor from a different basis than the
  one it is compared against.** ⚠ **After the first fill, a mark silently not written reads identically
  to one correctly unchanged; ONLY the `(as of …)` date separates them. COMPARE THE DATE.**
  **§5.1–§5.4 have never had an operand: 23 sessions since 2026-09-01, 20 post-fill, zero satellite
  positions ever.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — FOURTEEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  **(14) A COUNTER INCREMENTED FOR A WEEKEND, CAUGHT MID-RUN BY ITS OWN AUTHOR** — dedicated item above;
  it is (11) and (9) arriving together and it proves (9)'s own sentence for a second time.
  **(13) A FALSE SUPERLATIVE IN THE UNFLATTERING DIRECTION** — the 10-02 close run's "largest negative
  excess on record" and "biggest up-day" are both false by more than 2x (10-02 is 4th of 20 at
  −0.2186pp and 4th of 7 up days at +0.7255%; **09-21 holds both at −0.4694pp and +1.5542%**), and the
  refuting number was already in a file the run had read. ⚠⚠ **THE OPERATIVE RULE HAS NO DIRECTION IN
  IT: A SUPERLATIVE IS A CLAIM ABOUT A WHOLE SERIES AND REQUIRES THE WHOLE SERIES.** **(12) A FLATTERING
  SUPERLATIVE ABOUT THE BOOK'S OWN PERFORMANCE** (killed before publication). **(11) A COUNTER
  INCREMENTED FOR THE DAY THE RUN IS STANDING IN** — routines 1 and 2 are exposed. **(10) A NUMBER
  CORRECT ON A BASIS NOBODY NAMED.** **(9) A COUNTER WHOSE *UNIT* IS WRONG.** ⚠⚠ **NAMING A FAILURE
  DOES NOT RETIRE IT — proven twice now, by week 4 and by this run.** **(8) A MEASUREMENT PRESENTED AS
  A CALIBRATION.** **(7) A MISCOUNT INSIDE A VERIFICATION CLAIM.** **(6) A SCOPE CLAIM** — falsified by
  the run that read it. ⚠ **THE MOST DANGEROUS SHAPE, because no data call would ever contradict it. A
  CORRECT NUMBER REACHED BY AN UNCHECKED ROUTE IS NOT A CHECKED FACT.** **(5) A TRUNCATED SERIES.**
  **(1)–(4)** a false superlative surviving three runs; a stale thesis count; both halves of the
  `lastday_price` mechanism, asserted and falsified in turn.
  ⚠ **A superlative, count, mechanism, SERIES, CALIBRATION, BASIS or ALLOCATION inherited from a prior
  run is NOT a checked fact.** ⚠⚠ **NOTE THE FOUR THAT RUN AGAINST THE GRAIN: (12) flattering, (13)
  UNFLATTERING, (14) unflattering and self-caught, and 10-02's MICRON correction, where an inherited
  sense of scale failed toward DISMISSING a real event (FQ4 revenue $54.23B vs $11.32B a year earlier,
  FQ1 guided to $61.5B — recorded AS REPORTED and NOT disputed, because MU's own tape corroborated it).**

- **⚠ A REJECT-BOARD OR FUNNEL STATISTIC MAY BE *REPORTED* EVERY WEEK AND PROMOTED TO A *FINDING* ONLY
  AFTER IT HOLDS ACROSS THREE CONSECUTIVE REVIEWS.** Three reviews running promoted a one-week statistic
  and each broke within a week or two: **wk3 "the widening is the headline"** (refuted wk4) · **wk4 "the
  mean is the evidence the test discriminates"** (−2.04% → −1.00% on the SAME rows in five sessions) ·
  **wk4 "part 2 is dominant, nearly 2:1 over part 1"** (part 2 was 1 of 25) · **"part 3 remains the
  largest single category"** (refuted by a change of counting convention alone).
  ⚠ **The cause is not carelessness — every figure was computed correctly. A board of 80+ names over
  1–22 sessions does not contain a stable signal, and the review format asks for a headline every
  Friday.** ⚠ **The ONLY item currently qualifying for promotion is the theme-concentration finding
  (9 of the top 12), and it needs one more week.**
  **Reject board as last measured: 80 measurable rows, 32 beat VOO, 48 lagged, mean −1.08%, median
  −1.69%.** ⚠ **INHERITED, NOT RE-DERIVED THIS RUN.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — 39 CONSECUTIVE REFUSALS, AND THE COUNT DOES LESS WORK THAN IT
  LOOKS.** GNRC is the named counterparty in the Amazon announcement — **first-order, outside §4 at any
  price.** ⚠⚠ **GRADE EACH REFUSAL, DO NOT COUNT THEM: a midday seat is exits-only, a close seat does
  not trade, a weekly seat has no funnel — those refusals are FREE and some were STRUCTURALLY
  UNAVAILABLE TO VIOLATE.** The STRONG instances are PRE-MARKET seats, where a funnel exists and GNRC is
  reachable — **10-05 is one of those, and GNRC did not appear in any of three scans.** **No new costume
  in thirteen sessions — converging, not growing. FREE IS NOT THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — 70 RUNS.** §5 exempts core from all four sell
  rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy exempts**,
  which could eventually sell core on a drawdown — **§7 forbids that outright.** **Measure the core from
  the 706.74 fill (a RAW print) and from an official close, never from a `positions` field.**
  ⚠ **Graded, not counted: a pre-market seat writes no marks, so 10-05's refusal is the WEAK form. The
  close run's is load-bearing.** ⚠ **This refusal is close to automatic, and automatic is not sound.**

- **⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is **exits-only
  and may not open a position under ANY circumstance.** Routine 2 executes **only what `plan_today.md`
  already contains** — opening at 09:35 without a plan entry routes **around** the discipline. Routine 4
  **RECORDS AND JOURNALS; IT DOES NOT TRADE.** Routine 5 **MEASURES AND DOES NOT TRADE.** ⚠ **Idle cash,
  an INACTIVE breaker and an unused 0-of-3 cap are NOT an opportunity any of those seats may act on —
  and neither is a green day that lags the benchmark, nor a red week that beats it.**

- **⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS. READ
  `plan_date`, NEVER INFER FROM THE OUTCOME.** **Today's plan is FRESH (`plan_date: 2026-10-05`) and
  deliberately EMPTY.** The gate has been exercised **32 times and has never fired; its alert path
  remains UNTESTED CODE** (33 after today's open). ⚠⚠ **09-28 WAS THE MORNING IT WOULD FINALLY HAVE
  FIRED — `plan_today.md` genuinely carried `plan_date: 2026-09-25` — AND THE RUN CONTAINING THE GATE
  DID NOT EXECUTE.** ⚠ **The first morning it fires will by construction be a morning when the
  pre-market run failed. Read routine 2's Step 2 then; do not recall it.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat, cost_basis 69999.99.
  **OFFICIAL CLOSE BASIS (`bars`, the complete 2026-10-02 session: o 708.30 h 710.09 l 705.545 c 707.35
  — identical on `all`, `raw` and `split`; n 2,524 v 134,995, re-pulled 10-05 and UNCHANGED): equity
  $100,060.4082, core $70,060.4082 = 70.0181%, cash 29.9819%. TOTAL-RETURN basis carrying the inferred
  receivable: ~$100,241.17.** ⚠ **THE LAST COMPLETED SESSION IS STILL 10-02 — a Monday pre-market seat
  reads the same closing tape its predecessor read.**
  **Prior official closes: 10-01 $99,555.77 · 09-30 $99,392.34 · 09-29 $99,557.25 · 09-28 $99,688.98 ·
  09-25 $100,392.71 (on that day's RAW basis).**
  **VOO anchors (`--adjustment all`, pulled 10-02): 2025-10-02 608.15 · 2026-07-02 682.92 · 08-31 703.07
  · 09-02 701.54 · 09-25 708.88 · 10-02 707.35. RAW: 2025-10-02 615.16 · 09-25 710.705 · 10-02 707.35.**
  ⚠ **AUDIT ANY SUPERLATIVE BEFORE REPEATING IT — see catches (13) and (14).** **Post-fill day-return
  ranking: 09-21 +1.0848% · 09-17 +0.7774% · 09-11 +0.5833% · 10-02 +0.5069% (4TH).** **Since-inception
  positives: 09-21 +0.4150% · 09-22 +0.4081% · 09-03 and 09-25 +0.2119% · 10-02 +0.0604% (5TH of 21).**
  **Lows: 09-16 −1.3396% · 09-15 −1.0350% · 09-10 −0.9954%.** **Worst relative session: 09-21 −0.4694pp.**
  **NO REBALANCE IS DUE** — §2 acts at the **65/75 band edge** and core sits **5.01 points** inside the
  65 edge at the 10-05 08:28 mark (70.01%). ⚠ **`rebalance_delta: −$11.58` IS A DISTANCE READOUT, NOT AN
  INSTRUCTION**, negative only because core sits just above 70%. **Sixtieth consecutive run inside
  69.59–70.22%.**

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 20 OF 20 WITH NO EXCEPTION, RECOMPUTED FROM SOURCE ON 10-02 AND
  NOT INHERITED.** **12 VOO-down days, all positive excess (+0.0029 to +0.2265pp); 7 up days, all
  negative (−0.0380 to −0.4694pp); 1 flat day exactly 0.0000pp.** The satellite sleeve contributed
  **exactly 0.000000%** on every one. ⚠ **A TIGHT FIT IS NOT CONFIRMATION — the model fits to zero
  residual because there is NOTHING IN THE BOOK THE MODEL OMITS.** ⚠ **Neither direction is skill.**

- **⚠ NINE ITEMS REMAIN WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.** **(8) THE DIVIDEND — priced at ~0.93pp/yr on top of the 4.89pp cash drag;
  TWO SESSIONS LEFT on its test.** **(1)** the priced-in filter reads a drawdown as priced-in — **LITE
  at +28.34pp is the bill.** **(2)** the same filter reads an absorbed event move as a pass (QCOM, AVAV,
  AKAM). **(3)** the structurally undeployed sleeve — **105 theses, zero accepted.** **(6)**
  `selftest.py` certifies a healthy system without probing `clock` or market data — **it passed all five
  on 09-28 and 09-29 while three of 09-28's four routines had produced nothing.** **(7)** see (1) and
  (2) — only a human may change §4 or `alpaca.py move`. **(10)** the rollover rule says to move entries
  older than the current month out of `trade_log.md`; the 09-03 core fill was archived **AND RETAINED
  live**, because the position is OPEN and removing it would make the ledger read as an account that has
  never traded. **Overrule in `control.md` if that is wrong.**
  ⚠ **(4) IS DISCHARGED** (the core's divergence is the 09-03 entry gap, proven 09-11). ⚠ **(5) IS
  SETTLED AS A MECHANISM** — a moving live midpoint, not an offset.
  ⚠⚠ **(9) IS PARTLY DISCHARGED BY THIS RUN AND THE REST IS STILL THE HUMAN'S.** The item was that
  `positions.md` held 67KB with ZERO positions, `state.md` 72KB, together 66% of the live corpus, and
  **no seat owned collapsing either.** ⚠ **This pre-market run took `positions.md` from 68KB to 49KB
  (−29%) by folding the eight per-run blocks of 10-01 and 10-02 into their load-bearing facts — it
  writes `sell_rule_status`, so it owns that file.** ⚠ **STILL OPEN FOR THE HUMAN: `state.md` has no
  month boundaries and so no archivable unit, and the rollover rule excludes `positions.md` by design.
  That remains a prompt-level problem, not a discipline problem.**

---

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause: supplying the causal link yourself, then finding a source merely adjacent
to it.**

**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* **The most prolific rule.** Costumes:
guidance **issuance** vs **consensus** rather than the company's own prior figure (Ameren, Five Below,
DaVita, Labcorp, Nucor, Steel Dynamics) · **reaffirmations** (Centene, Southwest, General Mills,
McKesson) · **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence, Alcoa/South32) · **a DELIVERY
MILESTONE recycled as news** (GM/Lockheed) · **a PRE-IPO CONTRACT BOOK** (Nscale's $103B) · **a PRESS
RELEASE RESTATING AN ALREADY-FILED 8-K** (Akamai/Anthropic).
⚠⚠ **THE TEST IS CHEAP AND 09-29 GAVE A CLEAN PASS AND A CLEAN FAILURE ONE ENTRY APART, FROM THE SAME
QUERY: IOVA raised FY2026 guidance from ITS OWN $350–370M to $410–420M (PASS); AAR quoted 14–16% Q2
growth with NO PRIOR RANGE ANYWHERE IN THE SOURCE (FAIL — not establishable in either direction).**
**Did the source carry the company's OWN prior figure?**
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX, and 10-02 added RTX for the second
time in five sessions and Venture Global for the second time). ⚠ **Both re-entered on a genuinely new
transaction and both died on the SAME rule as the first time. A ticker that keeps arriving and keeps
dying the same death is telling you about its INDUSTRY'S DISCLOSURE PRACTICE, not about a candidate
maturing.**
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share,"
"the only company that makes X" are facts about an **industry**, not a **transaction** — plus the
**CEILING sub-shape** (RDW's "$980M" and MTUS's "$995M" multiple-award ceilings). Costumes: a **table**
(DoD contracts digest), a **consortium awardee**, a bare sentence, and an **UNNAMED SUPPLY BASE made to
look nameable by an exact figure and a named component category** ($1.7B of "memory components").
⚠ **A precise figure plus named COMPONENT CATEGORIES is the most fillable-looking blank this funnel
produces. THE SOURCE LEFT THE BLANK; FILLING IT IN IS NOT RESEARCH.**
⚠⚠ **AND THE 10-05 COSTUME, WHICH IS WORSE: AN UNNAMED *BIDDER* WEARING A LEGAL PSEUDONYM — Synaptics'
filings call the competing bidder only "PARTY A". A supply base is diffuse; Party A is ONE entity that
definitely exists, acted on a dated day (2026-09-02), and is known to the filer and redacted ON PURPOSE.
The blank has a shape, a date and a motive — everything except a name, and the priors arrive instantly
(Microchip, Skyworks, Qorvo, Renesas, Infineon).** ⚠ **A REDACTION IS NOT A LEAD. "Party A", "Company X"
and "a strategic party" are all the same object: there is no Company B until the filing names one.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.* Long-dated
energy offtake is a **standing feature of this funnel, not a visitor.** ⚠⚠ **THE CALIBRATION POINT:
Venture Global / ConocoPhillips, a 20-YEAR SPA with FIRST DELIVERY IN 2030 — ~16 quarters against §4's
two-quarter ceiling. Part 3 kills it in ONE step, before any funnel query is spent.** ⚠ **The REGULATORY
version (advisory vote → undated FDA decision → reimbursement → ramp) is the same shape in a lab coat;
so are CLINICAL COLLABORATIONS (SMMT/AZN) and PENDING-DEFINITIVE-AGREEMENT deals (CRK/SOCAR).**
**(vii)** *Check whether the named beneficiary makes the part itself.* Vertical integration leaves **no
external supplier to find** — IOVA is the cleanest instance and it killed the log's best rule (iii) pass.
⚠ **EW (10-05) is a fresh instance on the MEDICAL-DEVICE side: Edwards makes its own valves, so an FDA
approval of a new one names no external supplier.** ⚠⚠ **AND ITS COMPANION SUB-SHAPE, FROM THE SAME RUN:
AN *EXPANDED INDICATION* IS THE WEAKEST APPROVAL NEWS THIS FUNNEL CAN MEET.** A first approval at least
creates a product that did not exist and a supply chain that must be stood up; **a paediatric label
extension (BMY/Camzyos) creates no new manufacturing, no new supplier and no new line — the drug is
already being made.** ⚠ **The two 10-05 FDA items bracket the range and neither yields a Company B.**
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part 2.** Capital
paid **IN** (TotalEnergies/GIP $1.8B; SoftBank $11.1B; AstraZeneca's $2.0B convertible preferred, which
DILUTES rather than earns; SOCAR's $1.65B) · a **FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**
(Brookfield/Bloom $25B; Tesla's $30B) · capital paid **OUT** by the buyable leg (Royal Caribbean's ~$3B;
AWS paying SNPS) · a **COST dressed as a benefit** (BBY: Meta taking "a small fee") · a **SECONDARY-MARKET
SHARE PURCHASE** (FMC/Tessenderlo $403M) · ⚠⚠ **A MISS AGAINST CONSENSUS** (Cigna's $280.0B vs a $287.2B
consensus — **a $7.2B gap that belongs to NOBODY**, and the most seductive form because it arrives as two
exact figures and a clean subtraction).
⚠⚠ **THE DEFINITIVE INSTANCE IS JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K — AND
IT IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A
disclosed statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.**
**THIS IS THE WORKED EXAMPLE TO REACH FOR FIRST.**

**⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT WORKS IN BOTH SIGNS.** Two companies moving on the same
macro input is a **market**, not a **transaction**, and the giveaway is that part 1 needs an *"and
also."* ⚠ **A DIVERGENCE sounds causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge/ADM) — and the
convergent version is MORE DANGEROUS, because agreement LOOKS LIKE CORROBORATION when it is the clearest
statement that the input is a market variable.** ⚠ **The third and most respectable face is a
COMPETITOR'S EARNINGS PRINT read across** (AutoZone → GPC/ORLY/LKQ; Carnival, Vail, CarMax, CALM).
⚠⚠ **AND THE 10-02 SUB-SHAPE: AN EARNINGS *MISS* IS NOT A SECOND-ORDER CATALYST.** Nike missed FQ1 and
**a competitor's disappointment improves nobody's economics in any disclosed, dateable way — it only
invites a share-shift story THE READER SUPPLIES, and the channel direction has the WRONG SIGN for a
long.** ⚠ **Expect this shape every earnings season and kill it on part 1 each time.**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — THE MOST CONVINCING NON-EVENT THIS FUNNEL PRODUCES.** It is
the FOMC object in a better costume: **SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN INDUSTRY, MOVES THE
TAPE** — and it has **ONE party.** ⚠ **A long-only book cannot trade money being WITHDRAWN from a sector
unless some NAMED party receives it, and nobody does.** ⚠⚠ **THE MOST SEDUCTIVE COSTUME IS A
MARKET-IMPLIED PROBABILITY THAT MOVED** (CME FedWatch ~57% → ~70%, then back) — **a probability that
CHANGED reads like an event with a date. Same object: no named recipient, no transaction, one party.**
⚠ **SCALE MAKES IT MORE CONVINCING, NOT LESS.** ⚠ **Four consecutive sessions logged a macro/policy
complex in exactly this shape (09-25 rates, 09-29 Fed repricing, 09-30 tariffs, 10-02 the September
payrolls and the 25bp hike to 3.75–4.00% — the latter made IN SEPTEMBER and merely re-reported, so it
fails rule (iii) on top). THE FINDING IS THE PATTERN, NOT THE INSTANCE.** ⚠ **The counter-case stands
and must not be over-applied against: an FDA advisory vote ENABLES a named company's product and that
company has a named supplier — a real two-party chain. Do not over-apply this to approvals.**

**⚠ §3 IS A HARD FILTER AND IT DOES NOT WEIGH OUTCOMES.** ⚠⚠ **ELMT is the standing proof and it is
LIVE: it entered this funnel three times in three sessions, the third time carrying the disclosed price
($124.75M) whose absence killed the first two, and it is now +11.86pp vs VOO in six sessions. "But now
there is a number" and "but it went up" are the same pull wearing two coats. A microcap with a
Vietnam-listed counterparty is ineligible at every price and at every level of disclosure.**
⚠ **§3-FIRST IS A DISCIPLINE THAT WORKS AND HELD THREE SESSIONS RUNNING (RARE 09-30, MTUS 10-01): pull
the market cap BEFORE elaborating the thesis, so no effort goes into a story a single number was always
going to end.**
