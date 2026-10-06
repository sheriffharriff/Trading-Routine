# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-10-06 08:22 ET 1-premarket-research (selftest PASSED all five, trading_enabled true, LIVE paper, pre-flight equity 100842.87; PRE-MARKET and confirmed as such from the DATE not the boolean - clock 08:23:42 is_open FALSE with next_open 2026-10-06T09:30 pointing at TODAY, corroborated from the data plane by a complete 2026-10-05 bar and NO bar dated 2026-10-06; NOT a holiday; EIGHT THESES WRITTEN, ALL EIGHT REJECTED, 113 lifetime and ZERO EVER ACCEPTED; FOUR Perplexity scans all exit 0, ZERO move calls - the ABSENT fourth state, declined deliberately as a decorative exercise; ZERO quote calls; ZERO orders, nothing opened or closed; plan_today.md OVERWRITTEN with plan_date 2026-10-06 and NO BUY, NO SELL, NO REBALANCE intent; THE FINDING OF THE RUN IS ABOUT THE FUNNEL, NOT THE TAPE - scan 1 asked for 'the most significant events with knock-on effects' and returned FOUR MACRO NON-EVENTS saying so itself, while scan 2 asked for 'announcements with TWO NAMED PARTIES and a disclosed dollar amount' and returned SEVEN DATED TRANSACTIONS INCLUDING TWO MULTI-BILLION ACQUISITIONS SCAN 1 NEVER MENTIONED, so ASK FOR THE STRUCTURE SS4 REQUIRES NOT FOR IMPORTANCE; SECOND FINDING AND IT IS INFRASTRUCTURE - THE 2026-10-05 CLOSE RUN NEVER COMMITTED, git log for 10-05 holds premarket/open/midday and no close, newest close commit is 748a3e7 dated 10-02, THE 10-05 JOURNAL ENTRY IS GONE AND UNRECOVERABLE, second lost close run after 09-28, NO ALERT FIRED AND NONE COULD HAVE; cash read EXACTLY 30000.00 a TWENTY-SECOND time from TWO independent calls, dividend still unpaid with SEVEN seats left to the 10-07 test; the inherited band range 69.59-70.22 pct is NOW WRONG and corrected in file to 69.59-70.25 pct by today's 70.25 pct live reading; 24 completed sessions since 09-01 and 21 post-fill, the counter advancing because 10-05 COMPLETED, with 10-06 EXCLUDED because this run stands inside it)

prior_run: 2026-10-05 12:41 ET 3-midday-management (ZERO OPEN SATELLITE POSITIONS so the run's whole job had no operand; Step 2's staleness detector RAN WITH NO INPUT - highest_close is ABSENT and the detector's entire input IS its (as of ...) date, so the check DID NOT PASS, IT DID NOT RUN; the backfill path remains UNEXERCISED CODE; SS5.1-5.4 have STILL never had an operand; catch (16) - an inherited seat count whose UNIT was right and whose BOUND was wrong, stopping at the next morning instead of the 10-07 deadline the same sentence named. NOTE: the 10-05 CLOSE run that should have followed this one produced NO COMMIT - see last_run.)

week_of: 2026-10-05
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.25
satellite_pct: 0.0
cash_pct: 29.75
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

- **⚠⚠ NEW AND IT IS AN INFRASTRUCTURE FAILURE, NOT A DISCIPLINE ONE: THE 2026-10-05 CLOSE RUN
  (ROUTINE 4) NEVER COMMITTED.** `git log` for 10-05 holds **premarket `4277aae`, open `2effdf1`,
  midday `d50219c` — and no close commit**; the newest close commit in the repository is **`748a3e7`,
  dated 2026-10-02**, and `state.md`'s `last_run` was still the 12:41 midday seat, which corroborates
  it from the other side. **THE 2026-10-05 JOURNAL ENTRY IS GONE AND IS NOT RECOVERABLE.**
  ⚠ **SECOND LOST CLOSE RUN IN THE RECORD (09-28 was the first).** ⚠⚠ **NO ALERT FIRED AND NONE COULD
  HAVE: a run that dies before `commit.py` leaves no trace by construction, so `alerts.md` reading
  "zero open incidents" is NOT evidence that every seat ran.** ⚠ **It cost nothing in the ledger ONLY
  because the sleeve is empty — with one position open, the missed `highest_close` stamp would have
  forced routine 3 to backfill across it. LUCK, NOT DESIGN.**
  ⚠ **DO NOT RECONSTRUCT THE MISSING JOURNAL ENTRY from a later vantage point — that manufactures a
  record rather than recovers one.** ⚠⚠ **FOR THE HUMAN (open item 11): this and open item 6
  (`selftest.py` certifying a healthy system) are THE SAME BLIND SPOT FROM TWO SIDES — nothing in this
  system can notice a seat that never started.**

- **⚠⚠ NEW, AND THE MOST ACTIONABLE THING 10-06 PRODUCED: ASK THE FUNNEL FOR THE *STRUCTURE* §4
  REQUIRES, NOT FOR *IMPORTANCE*.** Two broad scans, same day, same window. Scan 1 asked for "the most
  significant US corporate and macroeconomic news events… with knock-on effects" and returned **four
  macroeconomic non-events**, volunteering *"the most clearly documented events were macroeconomic."*
  Scan 2 asked for **"announcements involving TWO NAMED PARTIES and a disclosed dollar amount"** and
  returned **seven dated transactions, including two multi-billion-dollar acquisitions scan 1 never
  mentioned at all.**
  ⚠⚠ **THE MECHANISM: A QUERY ABOUT "SIGNIFICANCE" INVITES THE SOURCE TO EDITORIALISE, AND IT
  EDITORIALISES TOWARD THE MACRO COMPLEX — THE ONE OBJECT §4 CAN NEVER USE.** A query naming the shape
  §4 needs (two parties, a dollar figure, a date) returns that shape or says it cannot.
  ⚠ **Scan 1's framing would have produced a no-trade day with an empty log. Scan 2's produced eight
  auditable rejections.** ⚠ **Routine 1's Step 5a prompt is written in scan 1's voice. USE SCAN 2's
  FRAMING AS THE SECOND QUERY EVERY RUN — it is the one that reaches the funnel's actual inventory.**

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. SEVEN SEATS LEFT BEFORE THE 10-07 TEST DATE. CHECK `cash`
  EVERY RUN.** `cash` read **exactly $30,000.00** again at 10-06 08:23 — a **twenty-second** reading,
  taken from **two independent calls** (`sleeves` and `account`).
  ⚠ **Twenty-two readings are ONE unresolved observation, and non-arrival before the pay date is
  EXPECTED, not evidence.** ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE AND NOT MOVED: `cash` should
  rise to about $30,180.76. IF IT HAS NOT BY 2026-10-07, the paper account does not model dividends at
  all.** The implied credit (**$1.825/share × 99.046311231**) is an **INFERENCE** — Alpaca does not
  publish it.
  ⚠ **SEATS COUNTED TO THE DEADLINE THE SAME SENTENCE NAMES, PER CATCH (16): 10-06 r2/r3/r4 and 10-07
  r1/r2/r3/r4 — SEVEN** (routine 5 is Friday-only; 10-07 is a Wednesday). **Ask what the UNIT is, then
  what the BOUND is.**
  ⚠⚠ **THE PRICE OF THE CONSEQUENCE, ESTABLISHED AND NOT RE-DERIVED: VOO's trailing 12 months is
  +16.3118% on `--adjustment all` against +14.9863% on `raw`, so DIVIDENDS ARE 1.3254pp/YEAR. If the
  account never collects them, the 70% core structurally under-earns ~0.93pp/yr, which on top of the
  4.89pp cash drag is a ~5.82pp ANNUAL HANDICAP BEFORE ANY DECISION.** ⚠ **A finding for the human,
  not something any seat can fix.**

- **⚠⚠ ASK FOR THE ANNOUNCEMENT DATE ON EVERY RUN, NOT JUST ON MONDAYS — 10-06 UPGRADED THIS FROM A
  MONDAY RULE TO A STANDING ONE AND IT PAID IMMEDIATELY.** A recency filter bounds when something was
  **WRITTEN**, never when it **HAPPENED**. Both 10-06 broad scans demanded the announcement date in the
  prompt itself, and scan 1 returned the September payrolls report with **"announced October 2, 2026,
  not October 5"** volunteered in its own first clause — the rule (iii) trap defused by framing rather
  than by a follow-up query. ⚠ **10-05 is the worked failure case: the onsemi/Synaptics revision was
  presented as fresh weekend news and was a four-day-old 8-K, caught only because a SECOND query asked
  for the date. The cost of asking in the first query is one sentence.**
  ⚠ **The companion Monday shape still stands: a CORRECT `plan_today.md` arrives THREE calendar days
  old on a Monday. COMPARE `plan_date` TO THE LAST TRADING DAY, NOT TO THE CALENDAR.**

- **⚠⚠ RULE (v)'s TWO LIVE COSTUMES, BOTH MORE FILLABLE THAN THE UNNAMED SUPPLY BASE THEY CAME FROM.**
  **(a) AN UNNAMED *BIDDER* WEARING A LEGAL PSEUDONYM** — Synaptics' filings call the competing bidder
  only **"Party A"** (proposal dated **2026-09-02**). ⚠ **A supply base is diffuse; Party A is ONE
  entity that definitely exists, definitely acted on a dated day, and is known to the filer and
  redacted ON PURPOSE. The blank has a shape, a date and a motive — everything except a name.**
  **(b) NEW 10-06 — A CAPEX BLANK CARRYING A DOLLAR FIGURE, A MAP PIN AND A PRODUCT LINE:** BDX's
  **$3B** US manufacturing commitment names **Nebraska (>$1B)**, **Columbus, Nebraska ($110M)** and
  **prefillable syringes** — and **no contractor, engineer or equipment supplier whatsoever.** The
  funnel said so in those words when asked.
  ⚠⚠ **THE PRIORS WERE INSTANTLY READY AND SPECIFIC IN BOTH CASES — Microchip/Skyworks/Qorvo/Renesas/
  Infineon for Party A; Jacobs/AECOM/Fluor/Fortive/Danaher for BDX. NO GUESS WAS MADE AND NONE IS
  RECORDED AS A CANDIDATE.** ⚠ **A REDACTION IS NOT A LEAD AND NEITHER IS A MAP PIN. There is no
  Company B until the source names one.** *(Entries: T-2026-10-05-01, T-2026-10-06-03.)*

- **⚠⚠ THE SATELLITE SLEEVE IS STRUCTURALLY UNDEPLOYED — 24 SESSIONS, 113 THESES, ZERO POSITIONS EVER,
  AND THE PRESSURE TO LOWER THE §4 BAR IS THE ONLY ITEM HERE ASKING FOR JUDGMENT RATHER THAN CARE.**
  **Eight theses on 10-06, all rejected; 113 total recounted from source (archive 87 + live 26, the
  template line excluded), ZERO EVER ACCEPTED.** Set beside: empty sleeve, **~29.8% idle cash**, weekly
  cap **0 of 3**, breaker INACTIVE, every gate open. **§2 permits the cash and §4 says most runs end in
  no trade — both rules were followed.**
  ⚠ **ONE SIDE OF THE ARGUMENT IS GONE: the book is NOT down, so "we are losing, deploy something" is
  unavailable — and it was never a §4 argument.** ⚠ **The symmetric half is the stronger one: the
  identical structure lagged on all 7 up days and gained on all 12 down days. The sleeve has no effect
  in EITHER direction, and a run citing only the flattering half is quoting the flattering half.**
  ⚠⚠ **THE BINDING CONSTRAINT IS NOT THE EVIDENCE BAR — SEVEN KNOWN FORMS PLUS THREE SUB-SHAPES:** the
  source withholds the counterparty's number · the counterparty discloses **roadmap not segment
  revenue** · the beneficiary is **vertically integrated** (IOVA; EW; **GEHC's own cyclotrons, 10-06**)
  · **both parties refuse to disclose commercially** (GM) · **the figure is disclosed and is the WRONG
  QUANTITY** (JBL $1.7B; Morgan Stanley's $2.45B term loan; **CHRW's $300M run-rate synergy and GEHC's
  $945M paid OUT, 10-06**) · **THERE IS NO COUNTERPARTY AT ALL** (Bayer's Ohio plant; **BDX's $3B,
  10-06**) · **EVERYTHING IS DISCLOSED AND THE SPENDING LANDS TOO FAR OUT** (Bayer's 2031/2034 holds
  the record). ⚠ **Sub-shapes: capacity ALREADY BUILT (ORCL/Tencent); NAMED BUT REDACTED ("Party A");
  and NEW 10-06 — **COMPANY A IS TOO SMALL FOR ANY ELIGIBLE COMPANY B TO CLEAR PART 2** (Blaize, total
  FY revenue $32–36M: part 2's 10% test and §3's $10B floor are JOINTLY UNSATISFIABLE, so the supplier
  search is pointless before it starts — a free one-step screen).**
  ⚠ **Only the first two forms are reachable by widening the bar; form five would be made WORSE by it;
  forms six and seven are untouched because the constraint is the CALENDAR or the absence of a second
  party.** **ABBV and ELMT are the standing proofs.** ⚠ **If the bar is to move, that is a
  `strategy.md` change and ONLY THE HUMAN may make it.**

- **⚠⚠ MERGER ARBITRAGE IS NOT IN §4, AND THE FUNNEL NOW OFFERS IT EVERY OTHER SESSION — THREE DEALS
  IN TWO SESSIONS.** onsemi/Synaptics $5.7B (10-05) · **Schneider Electric/PTC $22.6B at $205/share
  cash, close Q3 2027** (10-06) · **C.H. Robinson/RXO $5.8B cash-and-stock, close H1 2027** (10-06).
  ⚠⚠ **THE ANSWER IS ALREADY WRITTEN AND NEEDS NO FUNNEL QUERY: §4 ASKS WHOSE *ECONOMICS* CHANGE, AND
  A TARGET WHOSE PRICE IS CONTRACTUALLY PINNED HAS NO ECONOMICS LEFT TO CHANGE. The acquirer is
  first-order too.** ⚠ **AND PART 3 KILLS THE MERGER-CONTINGENT VERSION INDEPENDENTLY: both 10-06
  closings are ~4 quarters out against a two-quarter ceiling.** ⚠ **The competitor read-across
  (Autodesk/Dassault; Landstar/XPO/GXO) is the "shared cause is not a mechanism" object — and on 10-06
  the SOURCE stated that exclusion before I applied it.**

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD — SIX CONSECUTIVE SESSIONS.**
  09-29, 09-30, 10-01, 10-02, 10-05 and 10-06 each returned at least one. **10-06's two:** the M&A
  query returned *"no third publicly traded U.S. company with direct contractual exposure is
  identified"* for **both** deals, adding unprompted that *"companies that compete with, sell to, or
  operate in the same industrial-software market do not meet the requested standard"*; the BDX query
  returned *"no engineering firm, construction contractor, or equipment supplier has been named."*
  ⚠ **A volunteered absence is stronger than a silence.** ⚠⚠ **A run that then produces a Company B
  has supplied it from its own priors — verbatim the failure §4's honest-broker paragraph describes,
  and on 10-06 it would have been against an EXPLICIT DENIAL. THE PRIORS ARE ALWAYS READY AND ALWAYS
  SPECIFIC** (AMAT/LRCX/KLA for any fab headline; the GPU vendor for any AI-compute headline — the
  10-06 OpenAI/Cerebras pull; solid rocket motors for SM-6; Lantheus for radiopharma).
  ⚠ **Each is a fact about the INDUSTRY, not the TRANSACTION.** ⚠ **REPORTED WITH ITS COUNT AND NOT
  PROMOTED — the three-consecutive-reviews rule governs promotion.**

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
  10-02 AND 10-05 MADE ZERO `move` CALLS IN ANY SEAT; 10-06's PRE-MARKET SEAT MADE ZERO AND THREE OF
  ITS SEATS HAVE NOT RUN, SO IT IS NOT A FOURTH SESSION YET** — ⚠ **do not write "four sessions" from
  inside the fourth one; that is catch (11)'s shape.** ⚠ **That is an ABSENT check, not a skipped one,
  and the two look IDENTICAL in a run summary.** ⚠⚠ **A decorative `move` call on a name with no
  mechanism converts an honest absence into a fake exercise and has now been declined for that reason
  twice. SYNA at +14.1% (10-05) and CEREBRAS at +9.1% (10-06) would BOTH have FAILED the filter had
  they reached it — shape two — and neither got there.** ⚠ **The EXERCISED-AND-NON-DECISIVE state also
  stands (09-30 ABBV/RARE; 10-01 AMD/HPE/MU).** ⚠ **A run reporting "priced-in: pass" must say WHICH
  state it means.** **Only a human may change §4 or `alpaca.py move`.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY. A REJECTION IS NOT A QUEUE.**
  ⚠⚠ **THE DISPOSED-REJECT CATALOGUE IS SPLIT: `archive/research_log/2026-09.md` holds 87 theses; the
  live `research_log.md` holds the 26 October entries. A run checking whether a name was already
  disposed MUST READ BOTH.**
  **10-06's eight, with the durable kill:** **Schneider/PTC** and **CHRW/RXO** (part 1, volunteered
  absence — merger arb, see above) · **BDX $19B/$3B** (part 1 + part 3 — unnamed contractors, no dated
  milestone) · **GEHC/Sofie $945M** (part 2 — capital paid OUT, target PRIVATE, GEHC vertically
  integrated) · **Blaize/NeoTensr** (part 2 — §3 and part 2 jointly unsatisfiable on a $32–36M company)
  · **S&K PROS 7 $4.3B + Powerus $82M + Voyager $22.4M** (§3 — none buyable; defence pattern) ·
  **the macro complex** (no Company A) · **OpenAI/Cerebras** (no transaction).
  **10-05's seven:** onsemi/Synaptics + "Party A" + MS · Bayer $2.2B Ohio (2031/2034) · EW AUTUS valve
  · BMY Camzyos paediatric · TSMC capex (earnings PREVIEW) · September payrolls · G7 diesel release.
  ⚠ **DO NOT REHABILITATE ANY EARLIER REJECT AT A DIFFERENT PRICE.** ⚠⚠ **ELMT IS THE LIVE TEST: it is
  +11.86pp vs VOO and is STILL ineligible — §3 is a hard filter that does not weigh outcomes, and "but
  it went up" is a higher price, not new evidence. DO NOT SCREEN IT AGAIN.**
  ⚠ **One §3 question is reached-but-undecided: Shopify is a Canadian issuer trading as common stock on
  a US exchange. A future run reaching this with a LIVE candidate must put it to the human.**

- **⚠⚠ US DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE — FIVE INSTANCES, AND 10-06 SPENT ZERO
  QUERIES ON THREE OF THEM AT ONCE.** 09-29 AMRAAM $20.7B (RTX) · 09-30 F/A-XX >$20B (Boeing) · 10-02
  SM-6 $24.4B (RTX, a MAXIMUM POTENTIAL value) · **10-06 S&K Aerospace PROS 7 $4.3B (an unlisted
  prime), Powerus $82M and Voyager $22.4M (both microcaps).**
  ⚠⚠ **THE MECHANISM IS DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below
  it is commercially confidential.** ⚠ **Spend ONE funnel query, then WRITE THE ANSWER DOWN AND STOP.
  NO RE-QUERY HAS EVER BEEN ISSUED; 09-30, 10-01, 10-02, 10-05 and 10-06 all acted on this as
  written.** ⚠ **The prime is FIRST-ORDER and outside §4 at any price.** ⚠ **Powerus adds a rule (iii)
  costume: a "second order under an existing contract" is a DELIVERY MILESTONE RECYCLED AS NEWS.**

- **⚠⚠ THE BROKER/OFFICIAL PRICE GAP IS A MOVING LIVE MIDPOINT, NOT AN OFFSET — AND 10-06 PROVED THE
  SAME IS TRUE OF THE PRE-MARKET SERIES.** Post-bell: at 16:16 on 10-02 `current_price` 707.82 sat
  **+$0.470** above the official 707.35; at 16:46 it read **707.3246**, **−$0.0254** below it — same
  day, same official close, thirty minutes apart, a sign change.
  ⚠⚠ **PRE-MARKET, NOW TWO SAMPLES AND THEY DESTROY THE IDEA OF A PRE-MARKET OFFSET TOO: 10-05 08:28
  read 707.13 against the official 707.35 (−$0.22); 10-06 08:23 read 715.25 against the official 712.41
  (+$2.84). OPPOSITE SIGN, ~13x THE MAGNITUDE.** ⚠ **No fixed-offset reading survives on either series.**
  ⚠ **THREE SERIES EXIST — post-bell broker/official, PRE-MARKET, and the INTRADAY LIVE MARK (10-05
  09:36, 708.33) — AND NONE OF THEM MAY BE CONCATENATED.**
  ⚠ **NEVER difference a broker mark against an official close. NEVER `equity − last_equity` as a day's
  P&L** (fully attributed: `last_equity` = qty × `lastday_price` + cash — reconfirmed to the cent on
  10-06: 99.046311231 × 712.32 + 30,000 = $100,552.66843 against a reported
  $100,552.66841606592). ⚠ **NEVER `unrealized_intraday_pl` or `change_today`.** **Close-to-close from
  `bars` on a COMPLETED session, adjustment STATED; a fresh `quote` for execution.** ⚠ **An equity
  figure is meaningless without its CALL and its TIMESTAMP — 10-06 read $100,842.87 (`sleeves`) and
  $100,838.91 (`account`) minutes apart, and THE TWO MUST NOT BE DIFFERENCED INTO ANYTHING.**
  ⚠ **Do NOT re-open WHY `lastday_price` differs from the official close — four mechanisms falsified,
  both signs observed, and 10-06 adds another instance (712.32 vs 712.41, −$0.09). STOP PREDICTING IT.**
  ⚠ **This bites §6's 5% cap, computed against LIVE equity — ~$5,042 on the 08:23 mark. It has no
  operand only because no plan has ever carried a buy intent.**

- **⚠⚠ EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
  VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close by **0.997432**; `raw` and
  `split` return the original series. **Both are correct; they are different bases.** 09-28 onward agree
  on all three. ⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE. THE NEXT EX-DATE
  RESTORES THE TRAP.**
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
  ⚠⚠ **THE `n`/`v` HALF IS COMPLETE: a completed bar's `n`/`v` drift SOMETIMES AND NOT ALWAYS.** 09-30
  read 2050/61014 then 2053/61032 and 10-01 read 1633/51892 then 1634/51893 (**closes held to the
  cent**), while **10-02 read 2,524/134,995 before and after a full weekend — identical.**
  ⚠⚠ **A FIELD THAT SOMETIMES MOVES ON A COMPLETE BAR IS UNUSABLE AS EVIDENCE IN EITHER DIRECTION: "it
  did not move this time" is not a validation any more than "it moved" was a refutation.**
  ⚠ **The FLOOR test ("is `n` below the trailing completed-session MINIMUM") is a corroborant on a
  moving ruler — the floors themselves drift, and a quiet, low-participation FULL session could land
  under them. STATED LIMIT, STILL UNTESTED: the floor test MUST FAIL on a half-day session.**
  ⚠⚠ **THE CLOCK — PLUS, POST-BELL, A BAR DATED TODAY THAT EXISTS AND A ~15:59 `latestTrade` MATCHING
  ITS CLOSE — IS THE ONLY SOUND DISCRIMINATOR. The floor test is NEVER the primary.**
  ⚠ **`is_open: false` HAS THREE MEANINGS — pre-market, post-bell, holiday. READ `next_open`'s DATE,
  and prefer the data plane. `is_open: true` is the one case the boolean alone is sufficient.**

- **⚠⚠ STEP 2 HAVING NO OPERAND AND STEP 2 WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT — AND THE
  10-05 CLOSE RUN'S DISAPPEARANCE MAKES THAT WORSE, NOT BETTER.** The close routine stamps each open
  satellite position's official close into `highest_close`; routine 3's Step 2 **DETECTS** a missed
  write and backfills. **Every close run so far has had nothing to stamp, and "high-water marks
  updated" would have been FALSE. The honest form is: the job had NO OPERAND.**
  ⚠ **The every-day `(as of …)` date rule also has nothing to write, and the DETECTOR's entire input IS
  that date — so NO STALENESS COULD BE DETECTED AND NONE WAS RULED OUT. A detector handed no input
  returns the same silence as one finding everything healthy.**
  ⚠ **The only `highest_close` string in `positions.md` is the TEMPLATE PLACEHOLDER; the field is
  ABSENT, a third state carrying no date.** ⚠⚠ **10-05 12:41 IS THE MIDDAY SEAT'S OWN WORKED INSTANCE,
  FROM THE SEAT THAT OWNS THE DETECTOR: STEP 2 RAN AND ITS INPUT WAS ABSENT — the check did not pass,
  IT DID NOT RUN.** ⚠⚠ **AND NOW ADD THAT THE *NEXT* SEAT, THE 10-05 CLOSE RUN, NEVER EXECUTED AT ALL:
  WITH ONE POSITION OPEN, 10-06's MIDDAY WOULD HAVE HAD TO BACKFILL ACROSS A MISSING STAMP. 09-28 WAS
  THE FIRST SUCH GAP AND IT STRADDLED AN EX-DIVIDEND DATE. THE BACKFILL PATH IS STILL UNEXERCISED
  CODE, AND IT HAS NOW HAD TWO CHANCES TO MATTER AND BEEN SAVED BY THE EMPTY SLEEVE BOTH TIMES.**
  ⚠ **DO NOT BACKFILL ANYTHING NOW — there is nothing to write.** ⚠ **When it arms: no backfill may
  take its max from a bar dated TODAY while the market is open, nor from a different basis than the one
  it is compared against.** ⚠ **After the first fill, a mark silently not written reads identically to
  one correctly unchanged; ONLY the `(as of …)` date separates them. COMPARE THE DATE.**
  **§5.1–§5.4 have never had an operand: 24 completed sessions since 2026-09-01, 21 post-fill, zero
  satellite positions ever.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — SEVENTEEN CATCHES, AND THEY KEEP CHANGING
  SHAPE.**
  ⚠⚠ **(17) AN INHERITED *RANGE* THAT HAD GONE STALE — CAUGHT BEFORE PUBLICATION, NOT AFTER.** The
  carry-forward said core had held inside **69.59–70.22%** for sixty-two consecutive runs. **10-06's
  live reading is 70.25%, which is OUTSIDE that range**, so the sentence was false the moment it was
  inherited. **Corrected in file to 69.59–70.25% rather than repeated.** ⚠ **It is catch (5)'s family
  — A RANGE IS A CLAIM ABOUT A WHOLE SERIES — and the first instance where the refuting number was
  produced by the very run doing the inheriting. The band test still passes by 4.75 points; only the
  summary statistic was wrong.** ⚠ **A STALE SUMMARY STATISTIC IS THE EASIEST THING IN THIS FILE TO
  REPEAT, BECAUSE IT READS AS BACKGROUND RATHER THAN AS A CLAIM.**
  **(16) A COUNT WHOSE *UNIT* WAS RIGHT AND WHOSE *HORIZON* WAS WRONG** — an inherited seat count that
  stopped at the next morning instead of at the 10-07 deadline the same sentence named (nine seats
  stood between). ⚠ **Ask what the UNIT is, THEN what the BOUND is, and check the bound against the one
  written in the same sentence.** ⚠ **It failed toward URGENCY, not comfort.**
  **(15) A COUNTER INCREMENTED FOR A SECOND *SEAT* IN THE SAME SESSION** — "twenty-fifth session"
  corrected to twenty-fourth in file, one session after (14) did the same for a weekend, **by a run
  that had just read (14) three screens above.**
  **(14) A COUNTER INCREMENTED FOR A WEEKEND, CAUGHT MID-RUN BY ITS OWN AUTHOR.**
  ⚠⚠ **(14)+(15) ARE THE THIRD AND FOURTH PROOFS OF (9)'s SENTENCE: NAMING A FAILURE DOES NOT RETIRE
  IT.** ⚠ **The generalised mechanism, now in three costumes: a counter advances on a COMPLETED
  SESSION, and the pull to advance it is strongest wherever something ELSE has advanced — a new
  weekday, a weekend, a new SEAT, a new run. ASK WHAT THE UNIT IS, THEN WHETHER ONE OF *THAT* HAS
  PASSED.** ⚠ **10-06 is the counter-instance: a completed session HAD passed (10-05), so 23/20 → 24/21
  is correct, and 10-06 itself is excluded because the run stands inside it.**
  **(13) A FALSE SUPERLATIVE IN THE UNFLATTERING DIRECTION** — "largest negative excess on record" and
  "biggest up-day", both false by more than 2x, with the refuting number already in a file the run had
  read. ⚠⚠ **THE OPERATIVE RULE HAS NO DIRECTION IN IT: A SUPERLATIVE IS A CLAIM ABOUT A WHOLE SERIES
  AND REQUIRES THE WHOLE SERIES.** **(12) A FLATTERING SUPERLATIVE ABOUT THE BOOK'S OWN PERFORMANCE**
  (killed before publication). **(11) A COUNTER INCREMENTED FOR THE DAY THE RUN IS STANDING IN** —
  routines 1 and 2 are exposed. **(10) A NUMBER CORRECT ON A BASIS NOBODY NAMED.** **(9) A COUNTER
  WHOSE *UNIT* IS WRONG.** **(8) A MEASUREMENT PRESENTED AS A CALIBRATION.** **(7) A MISCOUNT INSIDE A
  VERIFICATION CLAIM.** **(6) A SCOPE CLAIM** — falsified by the run that read it. ⚠ **THE MOST
  DANGEROUS SHAPE, because no data call would ever contradict it. A CORRECT NUMBER REACHED BY AN
  UNCHECKED ROUTE IS NOT A CHECKED FACT.** **(5) A TRUNCATED SERIES.** **(1)–(4)** a false superlative
  surviving three runs; a stale thesis count; both halves of the `lastday_price` mechanism, asserted
  and falsified in turn.
  ⚠ **A superlative, count, mechanism, SERIES, RANGE, CALIBRATION, BASIS or ALLOCATION inherited from a
  prior run is NOT a checked fact — and (14)/(15) add that a count a run computes FOR ITSELF is not one
  either.** ⚠⚠ **NOTE THE FIVE THAT RUN AGAINST THE GRAIN: (12) flattering, (13) UNFLATTERING, (14)
  unflattering and self-caught, (16) toward urgency, and 10-02's MICRON correction, where an inherited
  sense of scale failed toward DISMISSING a real event. A SELF-FLATTERING DIRECTION IS NOT WHAT
  DISTINGUISHES THESE.**

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
  −1.69%.** ⚠ **INHERITED, NOT RE-DERIVED — and see catch (17) for what a stale inherited statistic
  costs.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — 40 CONSECUTIVE REFUSALS, AND THE COUNT DOES LESS WORK THAN IT
  LOOKS.** GNRC is the named counterparty in the Amazon announcement — **first-order, outside §4 at any
  price.** ⚠⚠ **GRADE EACH REFUSAL, DO NOT COUNT THEM: a midday seat is exits-only, a close seat does
  not trade, a weekly seat has no funnel — those refusals are FREE and some were STRUCTURALLY
  UNAVAILABLE TO VIOLATE.** The STRONG instances are PRE-MARKET seats, where a funnel exists and GNRC
  is reachable — **10-05 and 10-06 are both of those, and GNRC appeared in none of the seven scans
  across the two.** **No new costume in fourteen sessions — converging, not growing. FREE IS NOT THE
  SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — 72 RUNS.** §5 exempts core from all four sell
  rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy exempts**,
  which could eventually sell core on a drawdown — **§7 forbids that outright.** **Measure the core from
  the 706.74 fill (a RAW print) and from an official close, never from a `positions` field.**
  ⚠⚠ **GRADED, NOT COUNTED. The STRONG instances are the seats holding a WRITE PATH into the field: the
  close run (load-bearing) and routine 3's Step 2 backfill — 10-05 12:41 is the worked instance, where a
  `bars` pull on the only row the broker returned would have produced a perfectly real maximum close and
  writing it would have armed §5.4 on the exempt position. NO CALL WAS MADE AND NO MARK WAS WRITTEN.**
  ⚠ **10-06's pre-market instance is the WEAK form — no write path — but it is a step stronger than
  10-05's, because this run DID pull `bars --symbol VOO --days 7` for the tape context and declined to
  stamp its maximum. Pulling the data and not writing it is the distinction that matters.**
  ⚠ **This refusal is close to automatic, and automatic is not sound.**

- **⚠⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH ~30% CASH.** Routine 1 **RESEARCHES
  AND PLANS; IT PLACES NO ORDERS.** Routine 3 is **exits-only and may not open a position under ANY
  circumstance.** Routine 2 executes **only what `plan_today.md` already contains** — opening at 09:35
  without a plan entry routes **around** the discipline. Routine 4 **RECORDS AND JOURNALS; IT DOES NOT
  TRADE.** Routine 5 **MEASURES AND DOES NOT TRADE.**
  ⚠⚠ **GRADE THESE REFUSALS, DO NOT COUNT THEM. ROUTINE 2 IS THE ONLY SEAT WHOSE RESTRAINT IS
  LOAD-BEARING, AND 10-05 09:36 IS ITS WORKED INSTANCE: the market was OPEN, the plan was FRESH, and
  EVERY GATE WAS OPEN — breaker INACTIVE, weekly cap 0 of 3, sleeve 0.0% deployed, ~30% idle cash,
  `TRADING_ENABLED: true`, control notes none, §6's 5% cap $5,007.87 standing ready WITH NO OPERAND.
  NOTHING STOPPED A BUY EXCEPT THE ABSENCE OF AN INTENT.** ⚠ **That is what the 08:00/09:35 handoff is
  FOR.** ⚠⚠ **AND THE SAME SESSION SUPPLIED THE CONTRAST: the 12:41 midday seat faced the IDENTICAL
  gates with a LARGER cap ($5,024.34) and its restraint is worth NOTHING, because routine 3 is
  exits-only. Two seats, one session, one identical set of conditions, and only ONE of the two refusals
  is evidence of anything.**
  ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 cap are NOT an opportunity any seat may act
  on — and neither is a green day that lags the benchmark, nor a red week that beats it.**

- **⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS. READ
  `plan_date`, NEVER INFER FROM THE OUTCOME.** **10-06's plan is FRESH (`plan_date: 2026-10-06`) and
  deliberately EMPTY, as 10-05's was. THE ZERO-ORDER MORNING IT WILL PRODUCE IS BYTE-FOR-BYTE WHAT A
  STALE PLAN WOULD HAVE PRODUCED, AND ONLY `plan_date` SEPARATES THEM.** The gate has been exercised
  **33 times and has never fired; its alert path remains UNTESTED CODE**, and the count will be **34**
  after today's open. ⚠⚠ **09-28 WAS THE MORNING IT WOULD FINALLY HAVE FIRED — `plan_today.md`
  genuinely carried `plan_date: 2026-09-25` — AND THE RUN CONTAINING THE GATE DID NOT EXECUTE.**
  ⚠ **The first morning it fires will by construction be a morning when the pre-market run failed. Read
  routine 2's Step 2 then; do not recall it.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat, cost_basis 69,999.99.
  **OFFICIAL CLOSE BASIS (`bars --adjustment all`, the complete 2026-10-05 session: o 707.52 h 713.82
  l 707.52 c 712.41, n 1,802 v 60,541, vw 710.32828): equity $100,561.5826, core $70,561.5826 =
  70.1675%, cash 29.8325%.** **10-05 is +0.7168% close-to-close against 10-02 on that basis.**
  ⚠ **THE LAST COMPLETED SESSION IS 2026-10-05.**
  **Prior official closes (`--adjustment all`): 10-02 707.35 (o 708.30 h 710.09 l 705.545; n 2,524
  v 134,995; identical on `all`/`raw`/`split`) · 10-01 702.255 · 09-30 707.20h/… c per bars.**
  **Prior official EQUITY: 10-02 $100,060.4082 · 10-01 $99,555.77 · 09-30 $99,392.34 · 09-29
  $99,557.25 · 09-28 $99,688.98 · 09-25 $100,392.71 (that day's RAW basis).**
  **VOO anchors (`--adjustment all`, pulled 10-02): 2025-10-02 608.15 · 2026-07-02 682.92 · 08-31
  703.07 · 09-02 701.54 · 09-25 708.88 · 10-02 707.35. RAW: 2025-10-02 615.16 · 09-25 710.705 ·
  10-02 707.35.**
  ⚠ **AUDIT ANY SUPERLATIVE BEFORE REPEATING IT — see catches (13) and (17).** **Post-fill day-return
  ranking: 09-21 +1.0848% · 09-17 +0.7774% · 09-11 +0.5833% · 10-02 +0.5069%.** **Since-inception
  positives: 09-21 +0.4150% · 09-22 +0.4081% · 09-03 and 09-25 +0.2119% · 10-02 +0.0604%.**
  **Lows: 09-16 −1.3396% · 09-15 −1.0350% · 09-10 −0.9954%.** **Worst relative session: 09-21
  −0.4694pp.** ⚠ **These rankings PREDATE the 10-05 session, which no close run measured. They are
  incomplete, not wrong — do not quote them as covering 10-05.**
  **NO REBALANCE IS DUE** — §2 acts at the **65/75 band edge** and core sits **5.25 points** inside the
  65 edge (**70.25%** on the 08:23 live mark: equity $100,842.87, core $70,842.874108, cash 29.75%).
  ⚠ **`rebalance_delta: −$252.87` IS A DISTANCE READOUT, NOT AN INSTRUCTION**, negative only because
  core sits just above 70%. ⚠⚠ **DO NOT DIFFERENCE SUCCESSIVE `rebalance_delta` READINGS INTO A TREND —
  they are samples of a MOVING mark on days with no order in them, and any "widening" is VOO rising
  against a fixed share count, nothing else.** **SIXTY-THIRD consecutive run inside the band, observed
  range now 69.59–70.25% (CORRECTED THIS RUN — see catch (17)); RUN is the unit that was checked, which
  is why this one advances where the session counters do not.**

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 20 OF 20 WITH NO EXCEPTION, RECOMPUTED FROM SOURCE ON 10-02 AND
  NOT INHERITED.** **12 VOO-down days, all positive excess (+0.0029 to +0.2265pp); 7 up days, all
  negative (−0.0380 to −0.4694pp); 1 flat day exactly 0.0000pp.** The satellite sleeve contributed
  **exactly 0.000000%** on every one. ⚠ **A TIGHT FIT IS NOT CONFIRMATION — the model fits to zero
  residual because there is NOTHING IN THE BOOK THE MODEL OMITS.** ⚠ **Neither direction is skill.**
  ⚠ **10-05 is NOT in this series: no close run measured it. The next review must add it from source.**

- **⚠ TEN ITEMS REMAIN WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.**
  **(11) NEW — A ROUTINE CAN SIMPLY NOT RUN, AND NOTHING NOTICES.** The 10-05 close run produced no
  commit and no alert; 09-28 was the first instance. **Two of ~25 close runs have now vanished.**
  ⚠ **This and (6) are one blind spot seen from two sides.**
  **(8) THE DIVIDEND** — priced at ~0.93pp/yr on top of the 4.89pp cash drag; deadline **10-07** with
  **SEVEN seats left**, and a **twenty-second** unchanged reading of $30,000.00 at 10-06 08:23.
  **(1)** the priced-in filter reads a drawdown as priced-in — **LITE at +28.34pp is the bill.**
  **(2)** the same filter reads an absorbed event move as a pass (QCOM, AVAV, AKAM).
  **(3)** the structurally undeployed sleeve — **113 theses, zero accepted.**
  **(6)** `selftest.py` certifies a healthy system without probing `clock` or market data — **it passed
  all five on 09-28 and 09-29 while three of 09-28's four routines had produced nothing, and it passed
  all five on 10-06 the morning after a close run vanished.**
  **(7)** see (1) and (2) — only a human may change §4 or `alpaca.py move`.
  **(10)** the rollover rule says to move entries older than the current month out of `trade_log.md`;
  the 09-03 core fill was archived **AND RETAINED live**, because the position is OPEN and removing it
  would make the ledger read as an account that has never traded. **Overrule in `control.md` if wrong.**
  ⚠ **(4) IS DISCHARGED** (the core's divergence is the 09-03 entry gap, proven 09-11). ⚠ **(5) IS
  SETTLED AS A MECHANISM** — a moving live midpoint, not an offset, on BOTH the post-bell and
  pre-market series. ⚠⚠ **(9) IS PARTLY DISCHARGED: `positions.md` is down from 68KB to ~53KB across
  two collapses by this seat (which owns the file, since it writes `sell_rule_status`). STILL OPEN FOR
  THE HUMAN: `state.md` has no month boundaries and so no archivable unit, and the rollover rule
  excludes `positions.md` by design. That remains a prompt-level problem, not a discipline problem.**

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
approval of a new one names no external supplier.** ⚠⚠ **AND GEHC (10-06) ON THE IMAGING SIDE: GE
HealthCare buying a radiopharmacy network (Sofie Biosciences, $945M) names no equipment beneficiary
BECAUSE GEHC MAKES ITS OWN CYCLOTRONS AND SCANNERS — and the non-integrated cyclotron makers (IBA,
Siemens Healthineers) are BELGIAN- and GERMAN-LISTED, so §3 kills them before a mechanism is needed.
THREE DOORS, ALL CLOSED BY THE SAME ACQUISITION.** ⚠⚠ **AND ITS COMPANION SUB-SHAPE, FROM THE SAME RUN:
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
exact figures and a clean subtraction) · ⚠⚠ **AN ACQUIRER'S OWN SYNERGY ESTIMATE** (CHRW's **$300M
annual run-rate cost synergies** on RXO, 10-06 — a precise, quotable, allocated number that is a claim
about the ACQUIRER'S FUTURE COST BASE, not revenue at any Company B) · **ACQUISITION CONSIDERATION PAID
OUT BY THE BUYABLE LEG TO A PRIVATE SELLER** (GEHC's **$945M** for Sofie, 10-06 — the money leaves the
only listed party and the receiving leg cannot be bought at any price).
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

**⚠⚠ MERGER ARBITRAGE IS NOT IN §4 — THREE DEALS IN TWO SESSIONS AND THE ANSWER NEEDS NO QUERY.**
onsemi/Synaptics $5.7B (10-05) · Schneider Electric/PTC $22.6B at a fixed $205/share (10-06) ·
C.H. Robinson/RXO $5.8B (10-06). ⚠ **§4 asks whose ECONOMICS change, and a target whose price is
contractually pinned has no economics left to change; the acquirer is first-order too.** ⚠ **PART 3
KILLS THE MERGER-CONTINGENT VERSION INDEPENDENTLY — both 10-06 closings are ~4 quarters out against a
two-quarter ceiling.** ⚠ **The competitor read-across it invites is the shared-cause object above.**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — THE MOST CONVINCING NON-EVENT THIS FUNNEL PRODUCES.** It is
the FOMC object in a better costume: **SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN INDUSTRY, MOVES THE
TAPE** — and it has **ONE party.** ⚠ **A long-only book cannot trade money being WITHDRAWN from a sector
unless some NAMED party receives it, and nobody does.** ⚠⚠ **THE MOST SEDUCTIVE COSTUME IS A
MARKET-IMPLIED PROBABILITY THAT MOVED** (CME FedWatch ~57% → ~70%, then back) — **a probability that
CHANGED reads like an event with a date. Same object: no named recipient, no transaction, one party.**
⚠ **SCALE MAKES IT MORE CONVINCING, NOT LESS.**
⚠⚠ **10-06 SUPPLIED THE MOST EXTREME INSTANCE YET AND IT CHANGES NOTHING: implied October hike odds fell
from ~70–78% to ~20–24% IN A WEEK, alongside the 10-year Treasury at ~5.31–5.35% (highest since APRIL
2002) and the 30-year at ~5.66–5.70% (highest since MAY 2002). A 23-YEAR EXTREME AND A ~50-POINT
PROBABILITY SWING ARE STILL ONE PARTY AND NO TRANSACTION.** ⚠ **Four consecutive sessions logged a macro/policy
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
