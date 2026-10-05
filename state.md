# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-10-05 16:17 ET 4-market-close-journal (selftest PASSED all five, trading_enabled true, LIVE paper, pre-flight equity 100532.86; SESSION COMPLETE AND CONFIRMED THREE WAYS - clock 16:17:29 is_open FALSE with next_open 2026-10-06T09:30 (post-bell shape read off the DATE), a VOO bar dated 2026-10-05 exists and is COMPLETE (o 707.52 h 713.82 l 707.52 c 712.41 n 1800 v 60535), and the 15:59:59 ET latestTrade prints 712.41 matching that close to the cent; OFFICIAL-CLOSE EQUITY 100561.5826 = 99.046311231 x 712.41 + 30000.00, DAY +501.17 / +0.5009 pct from 10-02's 100060.4082, both legs official and same-basis (712.41 identical on all and raw, no ex-date since 09-28); SINCE INCEPTION +0.5616 pct price basis, +0.7423 pct total-return carrying the inferred receivable; ZERO TRADES - this seat records and journals and does not trade, and all four of today's seats placed zero orders, orders --status all still returns ONE ROW for the account's entire history, filled and terminal, so NOTHING IS IN LIMBO OVERNIGHT; STEP 2 HAD NO OPERAND - zero satellite positions means no highest_close to raise and NO (as of ...) date to advance, "high-water marks updated" would have been FALSE, SEVENTH consecutive close run by the count this record keeps and the condition has held on EVERY close run ever; NO MARK WRITTEN ON CORE VOO - 72nd run, and this seat held the raw material because Step 3's P and L required a bars pull that returned a complete 712.41, one arithmetic step from a trailing max that would have armed 5.4 on the exempt position; CATCH (17) - THE RECORD HAS HAD 09-28 EXACTLY BACKWARDS FOR THREE RUNS: 09-28 did NOT lose its close run, the close run is the ONLY routine that ran that day (git log returns two commits, the close plus its merge; the commit says routines 1-3 left no output; 09-29 pre-market verified it independently), so what 09-28 lost was routines 1, 2 and 3 INCLUDING THE DETECTOR, and A MISSING DETECTOR IS HARDER TO NOTICE THAN A MISSING WRITER because a missing writer at least leaves a stale date behind; CATCH (18) - catch (16) corrected a countdown's HORIZON and committed the counting family's ORIGINAL error on its MAGNITUDE in the same two sentences, both halves off by exactly one because the writing seat excluded itself from the period it stood in, and the generalisable half is that A COUNTDOWN INHERITED VERBATIM IS A DIFFERENT OBJECT FROM A COUNT-UP; NEARLY WROTE A FALSE SUPERLATIVE AND KILLED IT FROM SOURCE - today is the THIRD-highest official close of 24 on the as-printed basis behind 09-21 100596.25 and 09-22 100589.32, and only the --adjustment all vintage makes it look like the highest; CASH READ EXACTLY 30000.00 A TWENTY-SECOND TIME, VOO dividend STILL UNPAID with EIGHT seats left; SECTION 1 SEPARATION 21 OF 21, excess -0.2144pp against -0.2144pp predicted from the core weight alone; NO REBALANCE DUE TOMORROW - core 70.1675 pct, 5.17 points inside the 65 edge, 63rd consecutive run inside 69.59-70.22 pct; week_of 2026-10-05 matched the computed ISO Monday on the ONE day a rollover could have been due, so it was done not skipped, new_positions_this_week 0; COUNTERS ADVANCED 23/20 to 24/21 BY THIS SEAT AND ONLY THIS SEAT, soundly, because the session is COMPLETE; ClickUp daily summary 86bcdauyg)

prior_run: 2026-10-05 12:41 ET 3-midday-management (ZERO OPEN SATELLITE POSITIONS so the run's whole job had no operand - zero quote, bars, perplexity or order calls, nothing exited; STEP 2 RAN ITS DETECTOR WITH NO INPUT - highest_close is ABSENT, the third state carrying no date, and the detector's entire input IS that date, so no staleness could be detected and none was ruled out; SS5.1-5.4 have STILL never had an operand; its catch (16) correctly caught the 09:36 seat's horizon error but mis-stated the magnitude by one in both directions - see catch (18); cash 30000.00 a twenty-first reading; core 70.15 pct, no rebalance and none available to an exits-only seat whose restraint is the FREE form)

week_of: 2026-10-05
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.17
satellite_pct: 0.0
cash_pct: 29.83
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on fifty times.** **Everything below is LIVE. Nothing live was
discarded; settled items are folded to one line each and repeated emphasis removed.**
⚠ **A run that adds nothing to this list is the normal case.**
⚠ **A correction REPLACES the claim it corrects — it does not sit beside it.**

---

### Live — act on these

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID, AND AS OF TODAY IT IS THE ONLY THING STANDING BETWEEN THIS BOOK
  AND ITS ALL-TIME HIGH. EIGHT SEATS LEFT BEFORE THE 10-07 TEST DATE — 10-06 r1–r4 and 10-07 r1–r4
  (routine 5 is Friday-only; 10-09 is past it). RE-ENUMERATED 10-05 16:17 FROM THAT SEAT. CHECK `cash`
  EVERY RUN.** `cash` read **exactly $30,000.00** at 10-05 16:17 post-bell — a **twenty-second** reading,
  on the fourth trading day after the 09-28 ex-date.
  ⚠ **Twenty-two readings are ONE unresolved observation, and non-arrival is EXPECTED, not evidence —
  settlement runs on the PAY date.** ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE: `cash` should rise to
  about $30,180.76. IF IT HAS NOT BY 2026-10-07, the paper account does not model dividends at all.** The
  implied credit (**$1.825/share × 99.046311231 = $180.7595**) is an **INFERENCE** — Alpaca does not
  publish it — but $1.825/share is **independently corroborated by the ex-date adjustment factor**
  (710.705 raw × 0.002568 = 1.8251), so the 09-28 close run's **"~$180.45" was a slip**.
  ⚠⚠ **THE CONSEQUENCE IS NOW CONCRETE AND NOT MERELY ANNUALISED. Today's official close is $100,561.58
  and the account's all-time high is 09-21's $100,596.25 — SHORT BY $34.67, WHICH IS 19% OF THE UNPAID
  DIVIDEND. If the credit lands by 10-07, today is a new high-water mark on EVERY basis. If it never
  lands, 09-21 stands and the ~$180.76 is a PERMANENT UNCOMPENSATED STEP-DOWN in the equity curve — the
  §5.4 phantom-drawdown defect applied to the BOOK rather than to a position.**
  ⚠ **The annualised price, established and not re-derived: VOO's trailing 12 months is +16.3118% on
  `--adjustment all` against +14.9863% on `raw`, so dividends are 1.3254pp/yr. A 70% core that never
  collects them under-earns ~0.93pp/yr, which on top of the 4.89pp cash drag is a ~5.82pp ANNUAL HANDICAP
  BEFORE ANY DECISION.** ⚠ **A finding for the human; no seat can fix it.**

- **⚠⚠ TODAY'S EQUITY IS THE THIRD-HIGHEST OF 24 ON THE BASIS THE ACCOUNT ACTUALLY LIVED, AND THE
  SUPERLATIVE WAS AVAILABLE, FLUENT AND FALSE. NAME THE BASIS OR DO NOT WRITE THE SENTENCE.**
  As-printed official-close equity: **09-21 $100,596.25 · 09-22 $100,589.32 · 10-05 $100,561.58** (3rd,
  and the highest of the nine sessions since 09-22). On **`--adjustment all`** the two higher readings
  rescale down by ~$180 and today reads **highest on record**; on the **total-return** basis carrying the
  receivable today is **$100,742.34** and clears 09-21 by $146.09.
  ⚠⚠ **TWO OF THREE BASES SAY "NEW HIGH"; THE ONE THE ACCOUNT LIVED SAYS THIRD. The `--adjustment all`
  basis does not merely complicate the comparison — IT MANUFACTURES THE SUPERLATIVE, by lowering the past
  by exactly the amount the account may never have received.** ⚠ **Catch (10) (a number correct on a basis
  nobody named) and catch (13) (the refuting figure already sat in a file this run had opened — the week-4
  weekly-review table carries 09-21 +0.5962% and 09-22 +0.5893% as-printed against the carry-forward's
  adjusted +0.4150%/+0.4081%).** **Verified from the archived journal headers, not from the inherited list.**

- **⚠⚠ NEW COSTUME FOR RULE (v): AN UNNAMED *BIDDER* WEARING A LEGAL PSEUDONYM.** Synaptics' regulatory
  materials call the unsolicited competing bidder only **"Party A"** (proposal 2026-09-02; onsemi then
  restructured to all-cash $123/share, ~$5.7B, announced 10-01). ⚠ **Strictly worse than rule (v)'s
  unnamed SUPPLY BASE: a supply base is diffuse, but Party A is ONE entity that definitely exists,
  definitely acted on a dated day, and is definitely known to the filer and redacted ON PURPOSE. The blank
  has a shape, a date and a motive — everything except a name.**
  ⚠⚠ **THE PRIORS WERE INSTANTLY READY AND SPECIFIC: Microchip, Skyworks, Qorvo, Renesas, Infineon. NO
  GUESS WAS MADE AND NONE IS RECORDED AS A CANDIDATE.** ⚠ **A REDACTION IS NOT A LEAD. If a future run
  meets "Party A", "Company X" or "a strategic party", the §4 answer is already written: there is no
  Company B until the filing names one.** *(Full entry: T-2026-10-05-01.)*

- **⚠⚠ A WEEKEND WINDOW IS A WINDOW OF RE-REPORTING, NOT OF EVENTS — AND `--recency day` CANNOT TELL THE
  DIFFERENCE.** The 10-05 5a scan, asked for "the last 24 hours (weekend of October 3–5)", returned the
  onsemi/Synaptics revision as a headline item; the targeted follow-up established it was **announced
  October 1** and merely re-reported Oct 2–5 — the source said so unprompted, in its first sentence.
  ⚠ **Rule (iii) caught it ONLY because the second query asked for the announcement DATE.**
  ⚠⚠ **STANDING CONSEQUENCE FOR EVERY MONDAY AND POST-HOLIDAY RUN: ASK FOR THE ANNOUNCEMENT DATE
  EXPLICITLY. A recency filter bounds when something was WRITTEN, never when it HAPPENED.**
  ⚠ **Companion Monday shape: a CORRECT `plan_today.md` arrives THREE calendar days old on a Monday.
  COMPARE `plan_date` TO THE LAST TRADING DAY, NOT TO THE CALENDAR.**

- **⚠⚠ THE SATELLITE SLEEVE IS STRUCTURALLY UNDEPLOYED — 24 SESSIONS, 105 THESES, ZERO POSITIONS EVER,
  AND THE PRESSURE TO LOWER THE §4 BAR IS THE ONLY ITEM HERE ASKING FOR JUDGMENT RATHER THAN CARE.**
  **105 recounted from source (archive 87 + live 18, template line excluded), ZERO EVER ACCEPTED.** Set
  beside: empty sleeve, **~30% idle cash**, weekly cap **0 of 3**, breaker INACTIVE, every gate open.
  **§2 permits the cash and §4 says most runs end in no trade — both rules were followed.**
  ⚠ **ONE SIDE OF THE ARGUMENT IS GONE: the book is not down — since inception is +0.5616% price /
  +0.7423% total-return — so "we are losing, deploy something" is unavailable, and it was never a §4
  argument.** ⚠ **The symmetric half is stronger: the identical structure lagged on all 8 up days and
  gained on all 12 down days. The sleeve has no effect in EITHER direction, and a run citing only the
  flattering half is quoting the flattering half.**
  ⚠⚠ **THE BINDING CONSTRAINT IS NOT THE EVIDENCE BAR — SEVEN KNOWN FORMS PLUS TWO SUB-SHAPES:** the
  source withholds the counterparty's number · the counterparty discloses **roadmap not segment revenue**
  · the beneficiary is **vertically integrated** (IOVA, EW) · **both parties refuse to disclose
  commercially** (GM) · **the figure is disclosed and is the WRONG QUANTITY** (JBL $1.7B; Morgan Stanley's
  $2.45B term loan) · **THERE IS NO COUNTERPARTY AT ALL** (Bayer's Ohio plant) · **EVERYTHING IS DISCLOSED
  AND THE SPENDING LANDS TOO FAR OUT** (Bayer's 2031/2034, the record, roughly double Venture Global's
  2030). ⚠ **Sub-shapes: the transaction is in CAPACITY ALREADY BUILT (ORCL/Tencent); the counterparty is
  NAMED BUT REDACTED ("Party A").**
  ⚠ **Only the first two are reachable by widening the bar; form five would be made WORSE by it; forms six
  and seven are untouched because the constraint is the CALENDAR or the absence of a second party.**
  **ABBV and ELMT are the standing proofs.** ⚠ **If the bar is to move, that is a `strategy.md` change and
  ONLY THE HUMAN may make it.**

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD — FIVE CONSECUTIVE SESSIONS,
  AND THREE VOLUNTEERED ABSENCES IN 10-05 ALONE.** 09-29, 09-30, 10-01, 10-02 and 10-05 each returned one.
  **10-05: the onsemi query answered "no identified third public-company revenue beneficiary or loser";
  the regulatory query answered "No" for BOTH EW and BMY in its own table.**
  ⚠ **A volunteered absence is stronger than a silence.** ⚠⚠ **A run that then produces a Company B has
  supplied it from its own priors — verbatim the failure §4's honest-broker paragraph describes. THE PRIORS
  ARE ALWAYS READY AND ALWAYS SPECIFIC** (AMAT/LRCX/KLA for any fab headline; solid rocket motors for SM-6;
  GE Aerospace for F/A-XX; a valve-component supplier for EW; the GPU vendor for any AI-compute headline).
  ⚠ **Each is a fact about the INDUSTRY, not the TRANSACTION.** ⚠ **Reported with its count and NOT
  promoted — a continuation of a standing item; the three-consecutive-reviews rule governs promotion.**

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES AND A STANDING FOURTH STATE.**
  **Shape one — a DRAWDOWN misread as priced-in** (nine instances, newest CNC −6.44% → `true`; three
  near-misses cleared only because the *fall* was fractionally too small: LMT −3.61%, GM −3.95%, LH
  −3.83%). ⚠⚠ **LITE IS THE BILL: rejected on a −7.35% drawdown, it is +28.34pp vs VOO.** **Shape two —
  the filter working** on genuine news rises (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%). **Shape three — a
  genuine RISE UNRELATED TO THE NEWS swept up by the window** (JBL +4.97% on a grind whose news day moved
  it +0.63%). ⚠ **The defect is SIGN- and CAUSATION-BLINDNESS, not the threshold.**
  ⚠ **AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read `priced_in: false` at +3.19%**
  while its closes ran 104.53 → 117.435 (+12.35% in one session) → 110.44 (−6.74%) — a multi-session round
  trip netting to a passing figure. **HPE is a milder instance.**
  ⚠⚠ **THE FOURTH STATE — THE FILTER HAVING NOTHING TO FIRE ON — IS AS COMMON AS THE OTHERS. 09-29, 10-02
  AND 10-05 MADE ZERO `move` CALLS IN ANY SEAT, WHICH IS THREE SESSIONS AND NOT FOUR.** ⚠ **That is an
  ABSENT check, not a skipped one, and the two look IDENTICAL in a run summary.** ⚠⚠ **10-05 adds the
  reason it must stay absent: a decorative `move` call on a name with no mechanism would convert an honest
  absence into a fake exercise, and was declined for that reason. SYNA at +14.1% would have FAILED the
  filter had it reached it — shape two — and it never got there.** ⚠ **The EXERCISED-AND-NON-DECISIVE state
  also stands (09-30 ABBV/RARE; 10-01 AMD/HPE/MU).** ⚠ **A run reporting "priced-in: pass" must say WHICH
  state it means.** **Only a human may change §4 or `alpaca.py move`.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY. A REJECTION IS NOT A QUEUE.**
  ⚠⚠ **THE DISPOSED-REJECT CATALOGUE IS SPLIT: `archive/research_log/2026-09.md` holds 87 theses; the live
  `research_log.md` holds the 18 October entries. A run checking whether a name was already disposed MUST
  READ BOTH.**
  **10-05's seven, with the durable kill:** **onsemi/Synaptics + "Party A" + MS** (part 1 — no Company B;
  ON the acquirer and SYNA the target are both first-order, and buying a target at a fixed cash price is
  **merger arbitrage, which §4 does not contain a clause for**) · **Bayer $2.2B Ohio** (part 3 —
  **2031/2034**) · **EW AUTUS valve** (part 1, volunteered absence, **vertically integrated**) · **BMY
  Camzyos paediatric** (part 1, volunteered absence; **an EXPANDED INDICATION is the weakest approval shape
  — the drug is already being made, so no new line, no new supplier**) · **TSMC capex** (rule iii — an
  **earnings PREVIEW**, and the AMAT/LRCX/KLA chain already died 10-01) · **September payrolls** (no
  Company A) · **G7 diesel release** (source says **"not sufficiently verified"**; sign wrong for a long).
  ⚠⚠ **AND THE SECOND BROAD SCAN RETURNED ZERO NEW NAMES, WHICH IS A RESULT: every row was already disposed
  (Venture Global/ConocoPhillips 10-02, RTX SM-6 10-02, MTUS 10-01) or §3-ineligible on sight (Big Sky
  Industrial and Tiberius Aerospace — counterparty UNNAMED; Bharat Forge and Jindal Stainless —
  India-listed). NOT ONE WAS RE-SCREENED.**
  ⚠ **DO NOT REHABILITATE ANY EARLIER REJECT AT A DIFFERENT PRICE.** ⚠⚠ **ELMT IS THE LIVE TEST: it is
  +11.86pp vs VOO in six sessions and is STILL ineligible — §3 is a hard filter that does not weigh
  outcomes, and "but it went up" is a higher price, not new evidence. DO NOT SCREEN IT AGAIN.**
  ⚠ **One §3 question is reached-but-undecided: Shopify is a Canadian issuer trading as common stock on a
  US exchange. A future run reaching this with a LIVE candidate must put it to the human.**

- **⚠⚠ US DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE — FOUR INSTANCES, THREE PRIMES, THREE
  PROGRAMS. SETTLED, AND ACTED ON AS SETTLED FOR A THIRD SESSION.** 09-29 AMRAAM $20.7B (RTX) · 09-30
  F/A-XX >$20B (Boeing) · 10-02 SM-6 $24.4B (RTX, a **MAXIMUM POTENTIAL** value, not obligated).
  ⚠⚠ **THE MECHANISM IS DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below it is
  commercially confidential.** ⚠ **Spend ONE funnel query, then WRITE THE ANSWER DOWN AND STOP — do not
  re-word the query. NO RE-QUERY HAS EVER BEEN ISSUED.** ⚠ **The prime is FIRST-ORDER and outside §4 at any
  price.**

- **⚠⚠ THE BROKER/OFFICIAL PRICE GAP IS A MOVING LIVE MIDPOINT, NOT AN OFFSET — SETTLED, AND 10-05 ADDS A
  THIRD POST-BELL READING.** 10-02 16:16 `current_price` 707.82 sat **+$0.470** above the official 707.35;
  10-02 16:46 read **707.3246**, **−$0.0254** below it; **10-05 16:17 read 712.15 against the official
  712.41, −$0.26.** ⚠ **No fixed-offset reading survives that.** ⚠ **One observation and NOT a mechanism:
  10-05's 712.15 also equals the 16:01 `latestQuote` midpoint (bp 712.12 / ap 712.19 → 712.155) to the
  cent. The standing instruction is to STOP PREDICTING these fields; this is logged, not asserted.**
  ⚠ **NEVER difference a broker mark against an official close. NEVER `equity − last_equity` as a day's
  P&L.** Fully attributed again on 10-05: `last_equity` 100079.22704838174 = qty × `lastday_price` 707.54 +
  cash, exactly. ⚠⚠ **AND ITS DIRECTION IS NOT STABLE: on 10-05 it would have printed +0.4562% against the
  true +0.5009%, UNDERSTATING by 0.0446pp, where on 10-02 it FLATTERED by 0.0372pp.** ⚠ **NEVER
  `unrealized_intraday_pl` or `change_today`.** **Close-to-close from `bars` on a COMPLETED session,
  adjustment STATED; a fresh `quote` for execution.** ⚠ **An equity figure is meaningless without its CALL
  and its TIMESTAMP.** ⚠ **Do NOT re-open WHY `lastday_price` differs from the close — four mechanisms
  falsified, both signs observed. STOP PREDICTING IT.**
  ⚠ **THREE SERIES EXIST AND NONE MAY BE CONCATENATED: post-bell (above), PRE-MARKET (10-05 08:28 read
  707.13, −$0.22 against 707.35) and INTRADAY LIVE (10-05 09:36 read 708.33).** ⚠ **This bites §6's 5% cap,
  computed against LIVE equity — 5% of the 10-05 official close is $5,028.08. It has no operand only
  because no plan has ever carried a buy intent.**

- **⚠⚠ EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
  VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close by **0.997432**; `raw` and
  `split` return the original series. **Both are correct; they are different bases.** 09-28 onward agree on
  both — **10-02 is 707.35 and 10-05 is 712.41 on ALL THREE bases, so this week's comparisons are
  basis-clean. THAT IS A PROPERTY OF THIS WEEK, NOT A REPEAL. THE NEXT EX-DATE RESTORES THE TRAP.**
  ⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**
  ⚠⚠ **§5.4 IS THE REAL CASUALTY AND IT FAILS TOWARD SELLING:** a `highest_close` stamped pre-ex and
  compared against a post-ex adjusted close manufactures a **phantom drawdown equal to the dividend.**
  **THE FIX IS IN `positions.md`'s HEADER: same basis, same call — re-pull the whole window and take the max
  from that ONE pull.** ⚠ **The empty sleeve is the only reason this has cost nothing.**
  ⚠⚠ **AND 10-05 SUPPLIED THE SAME DEFECT APPLIED TO THE *BOOK*: the adjustment lowers every pre-ex equity
  reading by the dividend, which is what manufactured today's "highest since inception". The position-level
  and book-level instances are one defect with two operands.**
  ⚠ **`voo_close_at_entry` is a LABEL, not a baseline.** ⚠ **A historical BOOK day-return is not exactly
  reproducible from a later pull once an ex-date intervenes (the cash leg does not rescale). Quote a
  day-return with its BASIS *and* its VINTAGE.**
  ⚠⚠ **AND THE §1 TRAP THE SAME-SOURCE RULE DOES NOT CATCH: comparing the book's PRICE basis against VOO's
  `--adjustment all`. BOTH LEGS CAN COME FROM `bars --adjustment all` AND STILL BE INCOMPARABLE, when the
  ACCOUNT and the BENCHMARK recognise the same cash on DIFFERENT DATES.** *(The 10-02 review is the worked
  instance: the mixed-basis week read −0.1152pp against the honest TR-vs-TR +0.0649pp.)*

- **⚠⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.
  TWO ROUTINES CAN PULL ONE: routine 2 at 09:35 and routine 3 at 12:30.**
  ⚠ **THE PRICE HALF IS CONFIRMED AND IS THE DANGEROUS HALF:** at 12:41 on 10-01 the partial bar's `c`
  700.35 equalled `latestTrade.p` to the cent. **A PARTIAL BAR'S CLOSE FIELD IS THE LAST TRADE SO FAR
  WEARING A CLOSE'S CLOTHES** — a plausible price carrying no warning. ⚠ **NO `bars` CLOSE MAY BE STAMPED
  AS A MARK BEFORE THE BELL ON ANY BASIS.**
  ⚠⚠ **THE `n`/`v` HALF IS COMPLETE: a completed bar's `n`/`v` drift SOMETIMES AND NOT ALWAYS.** 09-30 read
  2050/61014 then 2053/61032 and 10-01 read 1633/51892 then 1634/51893 (**closes held to the cent**), while
  **10-02 read 2,524/134,995 before and after a full weekend — identical.** ⚠⚠ **A FIELD THAT SOMETIMES
  MOVES ON A COMPLETE BAR IS UNUSABLE AS EVIDENCE IN EITHER DIRECTION.**
  ⚠ **The FLOOR test ("is `n` below the trailing completed-session MINIMUM") is a corroborant on a moving
  ruler — the floors drift (1,450/43,730 → 1,560/45,031) and 10-05's COMPLETE session printed n 1,800 /
  v 60,535, well inside them. A quiet, low-participation FULL session could land under the floor.**
  ⚠ **STATED LIMIT, STILL UNTESTED: the floor test MUST FAIL on a half-day session. The next early close is
  the test.**
  ⚠⚠ **THE CLOCK — PLUS, POST-BELL, A BAR DATED TODAY THAT EXISTS AND A ~15:59 `latestTrade` MATCHING ITS
  CLOSE — IS THE ONLY SOUND DISCRIMINATOR, AND ALL THREE WERE RUN ON 10-05 AT 16:17 AND AGREED.** The floor
  test is NEVER the primary. ⚠ **`is_open: false` HAS THREE MEANINGS — pre-market, post-bell, holiday. READ
  `next_open`'s DATE, and prefer the data plane. `is_open: true` is the one case the boolean alone settles.**

- **⚠⚠ STEP 2 HAVING NO OPERAND AND STEP 2 WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT. SEVEN
  CONSECUTIVE CLOSE RUNS BY THE COUNT THIS RECORD KEEPS — AND THE CONDITION HAS HELD ON *EVERY* CLOSE RUN
  IN THE ACCOUNT'S HISTORY, SINCE NO SATELLITE POSITION HAS EVER EXISTED. THE COUNT MEASURES HOW LONG THE
  FINDING HAS BEEN *NAMED*, NOT HOW LONG IT HAS BEEN *TRUE*.** The close routine stamps each open satellite
  position's official close into `highest_close`; routine 3's Step 2 **DETECTS** a missed write and
  backfills. **"High-water marks updated" would have been FALSE on all of them. The honest form is: the job
  had NO OPERAND.** ⚠ **The every-day `(as of …)` date rule also has nothing to write, and the DETECTOR's
  entire input IS that date — so NO STALENESS COULD BE DETECTED AND NONE WAS RULED OUT. A detector handed no
  input returns the same silence as one finding everything healthy.**
  ⚠ **The only `highest_close` string in `positions.md` is the TEMPLATE PLACEHOLDER; the field is ABSENT, a
  third state carrying no date.** ⚠⚠ **BOTH SEATS HAVE A BLIND SPOT OF THE SAME SHAPE, NEITHER HAS EVER RUN
  AGAINST A REAL MARK, AND THE FIRST SATELLITE FILL ARMS BOTH AT ONCE.** ⚠ **THE BACKFILL PATH REMAINS
  UNEXERCISED CODE.**
  ⚠⚠ **CATCH (17) REPLACES THE WORKED INSTANCE THIS ITEM USED TO CARRY, AND POINTS THE OTHER WAY. The old
  claim — "09-28 lost its close run, so with one position open 09-29's midday would have had to backfill
  ACROSS AN EX-DIVIDEND DATE" — IS EXACTLY INVERTED. 09-28's close run is the ONLY routine that ran that
  day** (`git log` 2026-09-28 returns two commits, the close run and its merge; the commit text says
  *"routines 1-3 left NO committed output today"*; 09-29's pre-market verified it from inside that run; the
  archived journal carries a full 09-28 close entry with a 16:16:24 `clock` read).
  ⚠⚠ **SO WHAT 09-28 LOST WAS ROUTINES 1, 2 AND 3 — INCLUDING THE DETECTOR. A MISSING WRITER LEAVES
  EVIDENCE: a stale `(as of …)` date for the next detector to find. A MISSING DETECTOR LEAVES NOTHING AT ALL
  — it is silent by construction, and its absence is indistinguishable from its finding everything healthy.
  09-28 IS A WORKED INSTANCE OF THE HARDER FAILURE, NOT THE EASIER ONE, AND THE RECORD CARRIED IT BACKWARDS
  FOR THREE RUNS.** ⚠ **The shape claim stands; the HISTORY is corrected: the WRITING seat has never been
  missed, the DETECTING seat has, once.**
  ⚠ **10-05 12:41 remains the detector's own worked instance of having NO INPUT.** ⚠ **DO NOT BACKFILL
  ANYTHING NOW — there is nothing to write.** ⚠ **When it arms: no backfill may take its max from a bar
  dated TODAY while the market is open, nor from a different basis than the one it is compared against.**
  ⚠ **After the first fill, a mark silently not written reads identically to one correctly unchanged; ONLY
  the `(as of …)` date separates them. COMPARE THE DATE.**
  **§5.1–§5.4 have never had an operand: 24 completed sessions since 2026-09-01, 21 post-fill, zero
  satellite positions ever.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — EIGHTEEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  ⚠⚠ **(18) A CORRECTION THAT FIXED A COUNTDOWN'S *HORIZON* AND COMMITTED THE COUNTING FAMILY'S *ORIGINAL*
  ERROR ON ITS *MAGNITUDE*, IN THE SAME TWO SENTENCES.** Catch (16) rightly caught that the 09:36 seat's
  *"three seats remain"* stopped at tomorrow morning instead of at the 10-07 deadline its own sentence
  named. But its replacement — *"NINE seats stand between that claim and it (10-05 close; 10-06 r1–r4;
  10-07 r1–r4)"* — **omits the 10-05 midday seat it was itself sitting in** (the right answer from 09:36 was
  **ten**), and its *"EIGHT REMAIN AFTER THIS RUN"* is one low for the same reason (after midday, **nine**
  remained). ⚠⚠ **Both halves off by exactly one, same direction, same cause: a seat excluding itself from
  a period it was standing in — catch (11)/(15)'s mechanism arriving INSIDE the correction that named the
  counting family. FOURTH CONSECUTIVE PROOF OF (9): NAMING A FAILURE DOES NOT RETIRE IT.**
  ⚠⚠ **THE GENERALISABLE HALF, AND THE REASON THIS IS NOT JUST ANOTHER MISCOUNT: A COUNTDOWN INHERITED
  VERBATIM IS A DIFFERENT AND MORE DANGEROUS OBJECT THAN A COUNT-UP.** A count-up ("24 completed sessions")
  is right or wrong independent of its reader; a countdown ("eight seats remain") is true only at the
  instant it was written and silently becomes true or false as seats pass. **"Eight" was WRONG when written
  and is RIGHT now, so inheriting it unchanged would have produced the correct number BY ACCIDENT with no
  signal that anything had been checked.** ⚠ **WRITE A COUNTDOWN WITH THE SEAT IT WAS WRITTEN FROM, OR
  WRITE THE DEADLINE AND MAKE THE NEXT READER COUNT.**
  ⚠⚠ **(17) AN INHERITED CLAIM THAT INVERTED *WHICH SEAT WENT MISSING*, REPEATED ACROSS THREE RUNS, PROPPING
  UP A WORKED INSTANCE THAT IS IMPOSSIBLE AS WRITTEN** — dedicated item above. ⚠ **It is catch (6)'s family
  (a scope claim no data call would contradict) and catch (13)'s feature (the refutation sat in files this
  run had already opened — `git log`, the 09-28 commit text, the archived journal). A CORRECT-SOUNDING
  CLAIM REACHED BY AN UNCHECKED ROUTE IS NOT A CHECKED FACT.**
  **(16) A COUNT WHOSE *UNIT* WAS RIGHT AND WHOSE *HORIZON* WAS WRONG** — the 09:36 carry-forward's "three
  seats remain" stopped at the next morning rather than at the 10-07 date the same sentence named. ⚠ **The
  family question has two halves: ask what the UNIT is, THEN ask what the BOUND is, and check the bound
  against the one written in the same sentence.** ⚠ **It failed toward URGENCY, not comfort.**
  **(15) A COUNTER INCREMENTED FOR A SECOND *SEAT* IN THE SAME SESSION** — "twenty-fifth session" corrected
  to twenty-fourth in file, one session after (14) did the same for a weekend. **(14) A COUNTER INCREMENTED
  FOR A WEEKEND, CAUGHT MID-RUN BY ITS OWN AUTHOR.** ⚠ **The generalised mechanism, now in four costumes: a
  counter advances on a COMPLETED SESSION, and the pull to advance it is strongest wherever something ELSE
  has advanced — a new weekday, a weekend, a new SEAT, a new run. ASK WHAT THE UNIT IS, THEN WHETHER ONE OF
  *THAT* HAS PASSED.** **10-05's close run advanced 23/20 → 24/21 soundly, because the session is COMPLETE
  and three discriminators confirmed it.**
  **(13) A FALSE SUPERLATIVE IN THE UNFLATTERING DIRECTION** — 10-02's "largest negative excess on record"
  and "biggest up-day" were both false by more than 2x, and the refuting number was already in a file the
  run had read. ⚠⚠ **THE OPERATIVE RULE HAS NO DIRECTION IN IT: A SUPERLATIVE IS A CLAIM ABOUT A WHOLE
  SERIES AND REQUIRES THE WHOLE SERIES.** ⚠ **10-05 is the first run to kill one by pulling the whole series
  from source first — see the equity high-water item above.** **(12) A FLATTERING SUPERLATIVE ABOUT THE
  BOOK'S OWN PERFORMANCE** (killed before publication). **(11) A COUNTER INCREMENTED FOR THE DAY THE RUN IS
  STANDING IN** — routines 1 and 2 are exposed. **(10) A NUMBER CORRECT ON A BASIS NOBODY NAMED** — and
  10-05 supplied its sharpest instance yet. **(9) A COUNTER WHOSE *UNIT* IS WRONG.** ⚠⚠ **NAMING A FAILURE
  DOES NOT RETIRE IT — proven four times.** **(8) A MEASUREMENT PRESENTED AS A CALIBRATION.** **(7) A
  MISCOUNT INSIDE A VERIFICATION CLAIM.** **(6) A SCOPE CLAIM** — falsified by the run that read it.
  ⚠ **THE MOST DANGEROUS SHAPE, because no data call would ever contradict it.** **(5) A TRUNCATED SERIES.**
  **(1)–(4)** a false superlative surviving three runs; a stale thesis count; both halves of the
  `lastday_price` mechanism, asserted and falsified in turn.
  ⚠ **A superlative, count, COUNTDOWN, mechanism, SERIES, CALIBRATION, BASIS, ALLOCATION or SCOPE CLAIM
  inherited from a prior run is NOT a checked fact — and (14)/(15) add that a count a run computes FOR
  ITSELF is not one either.** ⚠⚠ **NOTE THE FIVE THAT RUN AGAINST THE GRAIN: (12) flattering, (13)
  unflattering, (14) unflattering and self-caught, (16) toward urgency, and 10-02's MICRON correction, where
  an inherited sense of scale failed toward DISMISSING a real event. A SELF-FLATTERING DIRECTION IS NOT WHAT
  DISTINGUISHES THESE.**

- **⚠ A REJECT-BOARD OR FUNNEL STATISTIC MAY BE *REPORTED* EVERY WEEK AND PROMOTED TO A *FINDING* ONLY
  AFTER IT HOLDS ACROSS THREE CONSECUTIVE REVIEWS.** Three reviews running promoted a one-week statistic and
  each broke within a week or two: **wk3 "the widening is the headline"** (refuted wk4) · **wk4 "the mean is
  the evidence the test discriminates"** (−2.04% → −1.00% on the SAME rows in five sessions) · **wk4 "part 2
  is dominant, nearly 2:1 over part 1"** (part 2 was 1 of 25) · **"part 3 remains the largest single
  category"** (refuted by a change of counting convention alone).
  ⚠ **The cause is not carelessness — every figure was computed correctly. A board of 80+ names over 1–22
  sessions does not contain a stable signal, and the review format asks for a headline every Friday.**
  ⚠ **The ONLY item currently qualifying for promotion is the theme-concentration finding (9 of the top 12),
  and it needs one more week.**
  **Reject board as last measured: 80 measurable rows, 32 beat VOO, 48 lagged, mean −1.08%, median −1.69%.**
  ⚠ **INHERITED, NOT RE-DERIVED.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — 40 CONSECUTIVE REFUSALS, AND THE COUNT DOES LESS WORK THAN IT LOOKS.**
  GNRC is the named counterparty in the Amazon announcement — **first-order, outside §4 at any price.**
  ⚠⚠ **GRADE EACH REFUSAL, DO NOT COUNT THEM: a midday seat is exits-only, a close seat does not trade, a
  weekly seat has no funnel — those refusals are FREE and some were STRUCTURALLY UNAVAILABLE TO VIOLATE.**
  The STRONG instances are PRE-MARKET seats, where a funnel exists and GNRC is reachable — **10-05's 08:28
  is one of those, and GNRC did not appear in any of three scans.** **No new costume in thirteen sessions —
  converging, not growing. FREE IS NOT THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — 72 RUNS.** §5 exempts core from all four sell
  rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy exempts**,
  which could eventually sell core on a drawdown — **§7 forbids that outright.** **Measure the core from the
  706.74 fill (a RAW print) and from an official close, never from a `positions` field.**
  ⚠⚠ **GRADED, NOT COUNTED. THE CLOSE SEAT IS THE LOAD-BEARING FORM AND 10-05 SHOWS WHY: Step 3's day P&L
  REQUIRES a `bars --symbol VOO` pull, so this seat ends every run holding a complete official close —
  712.41 on 10-05 — with a trailing maximum ONE ARITHMETIC STEP AWAY. The step was not taken and no mark
  was written.** ⚠ **That is true of EVERY close run, so 10-05 is not a new or stronger instance and is not
  claimed as one.** ⚠ **The 12:41 MIDDAY seat also holds a write path (Step 2's backfill) but made ZERO
  `bars` calls, so it never held the operand.** ⚠ **A pre-market seat writes no marks at all — the WEAK
  form.** ⚠ **This refusal is close to automatic, and automatic is not sound.**

- **⚠⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH, AND 10-05 09:36 IS THE FIRST
  *LOAD-BEARING* INSTANCE IN THE RECORD.** Routine 3 is **exits-only and may not open a position under ANY
  circumstance.** Routine 2 executes **only what `plan_today.md` already contains** — opening at 09:35
  without a plan entry routes **around** the discipline. Routine 4 **RECORDS AND JOURNALS; IT DOES NOT
  TRADE.** Routine 5 **MEASURES AND DOES NOT TRADE.**
  ⚠⚠ **GRADE THESE REFUSALS, DO NOT COUNT THEM. A midday, close or weekly seat CANNOT open a position, so
  its restraint is STRUCTURALLY UNAVAILABLE TO VIOLATE and therefore FREE. ROUTINE 2 IS THE EXCEPTION AND
  10-05 09:36 IS ITS WORKED INSTANCE: the market was OPEN, the plan was FRESH, and EVERY GATE WAS OPEN —
  breaker INACTIVE, weekly cap 0 of 3, sleeve 0.0% deployed, ~30% idle cash, `TRADING_ENABLED: true`,
  control notes none, §6's 5% cap $5,007.87 standing ready WITH NO OPERAND. NOTHING STOPPED A BUY EXCEPT
  THE ABSENCE OF AN INTENT.** ⚠ **That is what the 08:00/09:35 handoff is FOR.**
  ⚠⚠ **THE SAME SESSION SUPPLIED THE CONTRAST TWICE OVER: the 12:41 midday seat and the 16:17 close seat
  both faced the IDENTICAL open gates — same INACTIVE breaker, same 0-of-3 cap, same 0.0% sleeve, same ~30%
  idle cash, notes none, 5% caps of $5,024.34 and $5,028.08 — and NEITHER restraint is worth anything,
  because neither seat could have opened a position whatever it concluded. THREE SEATS, ONE SESSION, ONE
  IDENTICAL SET OF CONDITIONS, AND ONLY ONE OF THE THREE REFUSALS IS EVIDENCE OF ANYTHING.**
  ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 cap are NOT an opportunity any of those seats may
  act on — and neither is a green day that lags the benchmark, nor a red week that beats it.**

- **⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS. READ
  `plan_date`, NEVER INFER FROM THE OUTCOME.** **10-05's plan WAS FRESH — `plan_date: 2026-10-05`, compared
  against today's ET date by the 09:36 seat — and deliberately EMPTY. THE ZERO-ORDER MORNING IT PRODUCED IS
  BYTE-FOR-BYTE WHAT A STALE PLAN WOULD HAVE PRODUCED.** The gate has been exercised **33 times and has
  never fired; its alert path remains UNTESTED CODE**, and no stale-plan alert was posted on 10-05 because
  none was due. ⚠⚠ **09-28 WAS THE MORNING IT WOULD FINALLY HAVE FIRED — `plan_today.md` genuinely carried
  `plan_date: 2026-09-25` — AND THE RUN CONTAINING THE GATE DID NOT EXECUTE** (routines 1–3 all failed that
  day; see catch (17)). ⚠ **The first morning it fires will by construction be a morning when the pre-market
  run failed. Read routine 2's Step 2 then; do not recall it.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat, cost_basis 69999.99.
  **OFFICIAL CLOSE BASIS (`bars`, the complete 2026-10-05 session: o 707.52 h 713.82 l 707.52 c 712.41 —
  identical on `all` and `raw`; n 1,800 v 60,535): equity $100,561.5826, core $70,561.5826 = 70.1675%,
  cash 29.8325%, unrealized core P&L +$561.59 (+0.8023%). TOTAL-RETURN basis carrying the inferred
  receivable: $100,742.34.** ⚠ **THE LAST COMPLETED SESSION IS 10-05.**
  **Official-close equity, THE WHOLE SERIES, as-printed (this is the series a superlative needs):** 09-01
  100,000.00 · 09-02 100,000.00 · 09-03 100,367.46 · 09-04 100,084.18 · *(09-07 holiday)* · 09-08
  99,721.67 · 09-09 99,433.45 · 09-10 99,063.85 · 09-11 99,591.92 · 09-14 99,268.04 · 09-15 98,964.96 ·
  09-16 98,660.39 · 09-17 99,428.49 · 09-18 99,515.65 · **09-21 100,596.25 (HIGH)** · **09-22 100,589.32
  (2nd)** · 09-23 100,053.48 · 09-24 100,053.48 · 09-25 100,392.71 · *(09-28 ex-div)* · 09-28 99,688.98 ·
  09-29 99,557.25 · 09-30 99,392.34 · 10-01 99,555.77 · 10-02 100,060.41 · **10-05 100,561.58 (3rd)**.
  ⚠ **09-21 and 09-22 are PRE-EX readings; on `--adjustment all` they rescale ~$180 lower and 10-05 reads
  highest. STATE THE BASIS.**
  **VOO anchors (`--adjustment all`): 2025-10-02 608.15 · 2026-07-02 682.92 · 08-31 703.07 · 09-02 701.54 ·
  09-25 708.88 · 09-29 702.27 · 09-30 700.605 · 10-01 702.255 · 10-02 707.35 · 10-05 712.41. RAW:
  2025-10-02 615.16 · 09-25 710.705 · 10-02 707.35 · 10-05 712.41.**
  **Post-fill day-return ranking (inherited top four, NOT re-derived): 09-21 +1.0848% · 09-17 +0.7774% ·
  09-11 +0.5833% · 10-02 +0.5069% — 10-05's +0.5009% sits just below the fourth.** **Lows: 09-16 −1.3396% ·
  09-15 −1.0350% · 09-10 −0.9954%.** **Worst relative session: 09-21 −0.4694pp.**
  **NO REBALANCE IS DUE** — §2 acts at the **65/75 band edge** and core sits **5.17 points** inside the 65
  edge on the official close. ⚠ **`rebalance_delta: −$160.75` IS A DISTANCE READOUT, NOT AN INSTRUCTION**,
  negative only because core sits just above 70%; 10-05's four readings ran **−$11.58 (08:28) → −$47.24
  (09:36) → −$146.04 (12:41) → −$160.75 (16:17)** and ⚠⚠ **THE FOUR MUST NOT BE DIFFERENCED INTO A TREND —
  they are four samples of a MOVING mark on a day with no order in it, and the "widening" is VOO rising
  against a fixed share count, nothing else.** **SIXTY-THIRD consecutive RUN inside 69.59–70.22% — and RUN
  is the unit that was checked, which is why this one advances where the session counters do not.**
  ⚠ **§2 rebalances at the market-OPEN run; no other seat may.**

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 21 OF 21 WITH NO EXCEPTION.** **12 VOO-down days, all positive
  excess (+0.0029 to +0.2265pp); 8 up days, all negative (−0.0380 to −0.4694pp); 1 flat day exactly
  0.0000pp.** **10-05: VOO +0.7153%, book +0.5009%, excess −0.2144pp against −0.2144pp PREDICTED from the
  70.0181% core weight alone — agreement to 0.0000pp, and inside 10-02's −0.2186pp, so NOT a superlative.**
  The satellite sleeve contributed **exactly 0.000000%** on every one of the 21. ⚠ **A TIGHT FIT IS NOT
  CONFIRMATION — the model fits to zero residual because there is NOTHING IN THE BOOK THE MODEL OMITS.**
  ⚠ **Neither direction is skill.**

- **⚠ NINE ITEMS REMAIN WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A NUMBER
  A RUN COLLECTS.** **(8) THE DIVIDEND — now the sharpest of the nine, because it is the difference between
  an all-time high and a third-place close: ~0.93pp/yr on top of the 4.89pp cash drag, deadline 10-07 with
  EIGHT seats left, and a TWENTY-SECOND unchanged reading of $30,000.00 at 16:17 on 10-05.** **(1)** the
  priced-in filter reads a drawdown as priced-in — **LITE at +28.34pp is the bill.** **(2)** the same filter
  reads an absorbed event move as a pass (QCOM, AVAV, AKAM). **(3)** the structurally undeployed sleeve —
  **105 theses, zero accepted.** **(6)** `selftest.py` certifies a healthy system without probing `clock` or
  market data — ⚠ **AND CATCH (17) SHARPENS THIS ITEM RATHER THAN THE OLD VERSION OF IT: on 09-28 routines
  1, 2 and 3 all produced nothing while the selftest regime reported health, and the seat that went missing
  was the DETECTOR, whose absence leaves no artifact at all.** **(7)** see (1) and (2) — only a human may
  change §4 or `alpaca.py move`. **(10)** the rollover rule says to move entries older than the current
  month out of `trade_log.md`; the 09-03 core fill was archived **AND RETAINED live**, because the position
  is OPEN and removing it would make the ledger read as an account that has never traded. **Overrule in
  `control.md` if that is wrong.**
  ⚠ **(4) IS DISCHARGED** (the core's divergence is the 09-03 entry gap, proven 09-11). ⚠ **(5) IS SETTLED
  AS A MECHANISM** — a moving live midpoint, not an offset.
  ⚠⚠ **(9) IS PARTLY DISCHARGED AND THE REST IS STILL THE HUMAN'S.** The item was that `positions.md` held
  67KB with ZERO positions and `state.md` 72KB, and **no seat owned collapsing either.** **10-05's
  pre-market run took `positions.md` 68KB → 49KB; this close run collapsed the day's four seats into one
  block rather than appending a fourth, and rewrote this file rather than growing it.** ⚠ **STILL OPEN FOR
  THE HUMAN: `state.md` has no month boundaries and so no archivable unit, and the rollover rule excludes
  `positions.md` by design. That remains a prompt-level problem, not a discipline problem.**

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
RELEASE RESTATING AN ALREADY-FILED 8-K** (Akamai/Anthropic) · **an EARNINGS PREVIEW** (TSMC capex).
⚠⚠ **THE TEST IS CHEAP AND 09-29 GAVE A CLEAN PASS AND A CLEAN FAILURE ONE ENTRY APART, FROM THE SAME
QUERY: IOVA raised FY2026 guidance from ITS OWN $350–370M to $410–420M (PASS); AAR quoted 14–16% Q2
growth with NO PRIOR RANGE ANYWHERE IN THE SOURCE (FAIL — not establishable in either direction).**
**Did the source carry the company's OWN prior figure?**
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX; RTX twice in five sessions; Venture
Global twice). ⚠ **Both re-entered on a genuinely new transaction and both died on the SAME rule as the
first time. A ticker that keeps arriving and keeps dying the same death is telling you about its
INDUSTRY'S DISCLOSURE PRACTICE, not about a candidate maturing.**
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share," "the
only company that makes X" are facts about an **industry**, not a **transaction** — plus the **CEILING
sub-shape** (RDW's "$980M" and MTUS's "$995M" multiple-award ceilings). Costumes: a **table** (DoD
contracts digest), a **consortium awardee**, a bare sentence, and an **UNNAMED SUPPLY BASE made to look
nameable by an exact figure and a named component category** ($1.7B of "memory components").
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
two-quarter ceiling. Part 3 kills it in ONE step, before any funnel query is spent.** ⚠ **Bayer's Ohio
plant (2031 drug substance / 2034 finished product, ~20–32 quarters) is now the record.** ⚠ **The
REGULATORY version (advisory vote → undated FDA decision → reimbursement → ramp) is the same shape in a lab
coat; so are CLINICAL COLLABORATIONS (SMMT/AZN) and PENDING-DEFINITIVE-AGREEMENT deals (CRK/SOCAR).**
**(vii)** *Check whether the named beneficiary makes the part itself.* Vertical integration leaves **no
external supplier to find** — IOVA is the cleanest instance and it killed the log's best rule (iii) pass.
⚠ **EW is a fresh instance on the MEDICAL-DEVICE side: Edwards makes its own valves, so an FDA approval of
a new one names no external supplier.** ⚠⚠ **AND ITS COMPANION SUB-SHAPE: AN *EXPANDED INDICATION* IS THE
WEAKEST APPROVAL NEWS THIS FUNNEL CAN MEET.** A first approval at least creates a product that did not
exist and a supply chain that must be stood up; **a paediatric label extension (BMY/Camzyos) creates no new
manufacturing, no new supplier and no new line — the drug is already being made.**
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part 2.** Capital
paid **IN** (TotalEnergies/GIP $1.8B; SoftBank $11.1B; AstraZeneca's $2.0B convertible preferred, which
DILUTES rather than earns; SOCAR's $1.65B) · a **FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**
(Brookfield/Bloom $25B; Tesla's $30B; **Morgan Stanley's $2.45B onsemi term loan**) · capital paid **OUT**
by the buyable leg (Royal Caribbean's ~$3B; AWS paying SNPS) · a **COST dressed as a benefit** (BBY: Meta
taking "a small fee") · a **SECONDARY-MARKET SHARE PURCHASE** (FMC/Tessenderlo $403M) · ⚠⚠ **A MISS
AGAINST CONSENSUS** (Cigna's $280.0B vs a $287.2B consensus — **a $7.2B gap that belongs to NOBODY**, and
the most seductive form because it arrives as two exact figures and a clean subtraction).
⚠⚠ **THE DEFINITIVE INSTANCE IS JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K — AND IT
IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A disclosed
statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.** **THIS IS THE
WORKED EXAMPLE TO REACH FOR FIRST.**

**⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT WORKS IN BOTH SIGNS.** Two companies moving on the same
macro input is a **market**, not a **transaction**, and the giveaway is that part 1 needs an *"and also."*
⚠ **A DIVERGENCE sounds causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge/ADM) — and the convergent
version is MORE DANGEROUS, because agreement LOOKS LIKE CORROBORATION when it is the clearest statement
that the input is a market variable.** ⚠ **The third and most respectable face is a COMPETITOR'S EARNINGS
PRINT read across** (AutoZone → GPC/ORLY/LKQ; Carnival, Vail, CarMax, CALM). ⚠⚠ **AND THE SUB-SHAPE: AN
EARNINGS *MISS* IS NOT A SECOND-ORDER CATALYST.** Nike missed FQ1 and **a competitor's disappointment
improves nobody's economics in any disclosed, dateable way — it only invites a share-shift story THE READER
SUPPLIES, and the channel direction has the WRONG SIGN for a long.** ⚠ **Expect this shape every earnings
season and kill it on part 1 each time.**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — THE MOST CONVINCING NON-EVENT THIS FUNNEL PRODUCES.** It is
the FOMC object in a better costume: **SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN INDUSTRY, MOVES THE
TAPE** — and it has **ONE party.** ⚠ **A long-only book cannot trade money being WITHDRAWN from a sector
unless some NAMED party receives it, and nobody does.** ⚠⚠ **THE MOST SEDUCTIVE COSTUME IS A
MARKET-IMPLIED PROBABILITY THAT MOVED** (CME FedWatch ~57% → ~70%, then back) — **a probability that
CHANGED reads like an event with a date. Same object: no named recipient, no transaction, one party.**
⚠ **SCALE MAKES IT MORE CONVINCING, NOT LESS.** ⚠ **Five consecutive sessions logged a macro/policy complex
in exactly this shape (09-25 rates, 09-29 Fed repricing, 09-30 tariffs, 10-02 the September payrolls and
the 25bp hike to 3.75–4.00%, 10-05 the payrolls print again and the G7 diesel release). THE FINDING IS THE
PATTERN, NOT THE INSTANCE.** ⚠ **The counter-case stands and must not be over-applied against: an FDA
advisory vote ENABLES a named company's product and that company has a named supplier — a real two-party
chain. Do not over-apply this to approvals.**

**⚠ §3 IS A HARD FILTER AND IT DOES NOT WEIGH OUTCOMES.** ⚠⚠ **ELMT is the standing proof and it is LIVE:
it entered this funnel three times in three sessions, the third time carrying the disclosed price
($124.75M) whose absence killed the first two, and it is now +11.86pp vs VOO in six sessions. "But now
there is a number" and "but it went up" are the same pull wearing two coats. A microcap with a
Vietnam-listed counterparty is ineligible at every price and at every level of disclosure.**
⚠ **§3-FIRST IS A DISCIPLINE THAT WORKS AND HELD THREE SESSIONS RUNNING (RARE 09-30, MTUS 10-01): pull the
market cap BEFORE elaborating the thesis, so no effort goes into a story a single number was always going
to end.** ⚠ **SYNA's ~$5.7B deal value is below the $10B floor too — the target was never eligible.**
