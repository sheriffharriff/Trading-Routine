# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-10-06 16:17 ET 4-market-close-journal (THE SESSION IS COMPLETE AND THIS SEAT RAN - which is the first thing worth recording, because the 10-05 and 09-28 close runs did not and left no trace; selftest PASSED all five, trading_enabled true, LIVE paper, pre-flight equity 100957.84; MARKET CLOSED, POST-BELL - clock 16:17:01 is_open FALSE with next_open 2026-10-07T09:30 pointing at TOMORROW, read off the DATE not the boolean, and corroborated from the data plane; NOT A HOLIDAY, today WAS a trading session; STEP 2 HAD NO OPERAND - zero open satellite positions, so no highest_close to raise and no (as of) date to advance, and 'high-water marks updated' would be FALSE as would 'verified' - THE JOB HAD NO SUBJECT, and routine 3's staleness detector will be handed ABSENT input again tomorrow; THE LOAD-BEARING REFUSAL OF THE RUN, AND THE STRONGEST INSTANCE IN THE RECORD - bars --days 3 --adjustment all was pulled at this seat and returned today's COMPLETED official close 716.29, a real same-basis maximum, from the ONE seat that owns the write path, on the ONLY row the broker returns, and it was NOT written onto core VOO because that would ARM SECTION 5.4 ON THE POSITION SECTION 5 EXEMPTS, which section 7 forbids - 75th consecutive run, and the FIRST time the close seat has held BOTH the number and the path (12:42 held the path and made zero bars calls; 08:22 held a 7-day pull and had no path); DAY NUMBERS on the official close basis, VOO c 716.29 against 10-05's 712.41 - equity 100945.8823, day +384.2997 (+0.3822 pct), since inception +0.9459 pct, highest official close since inception; VOO itself +0.5446 pct, so the book LAGGED by 0.1625pp and the satellite sleeve contributed EXACTLY 0.000000 pct as always - 70 pct of an up day is 0.38 pct and there is no decision in it; core 70.2811 pct on that basis and 70.28 pct on the broker's live mark, IN BAND by 5.28 points at the 65 edge and 4.72 at the 75 edge, 66th consecutive RUN inside it, rebalance_delta -287.35 a distance readout; NO REBALANCE DUE TOMORROW; ZERO ORDERS and NOTHING UNRESOLVED OVERNIGHT - orders --status all still returns ONE ROW for the whole account history, the 09-03 core fill, terminal since 2026-09-03, so section 7's limbo-order warning has NO OPERAND rather than a clean bill; 8 theses today, 0 accepted 8 rejected, 113 lifetime recounted from source this run (87 archived + 26 live October, template excluded) with ZERO ever accepted; cash read EXACTLY 30000.00 a TWENTY-FIFTH time from TWO independent calls on THE LAST TRADING SEAT BEFORE THE 10-07 TEST - and the carry-forward's flagged risk is DISCHARGED, because the pre-deadline reading was taken by a seat that RAN rather than read off a missing run's silence; FOUR seats left, ALL of them tomorrow's; A CLEAN DATA-PLANE FINDING THAT CLOSES THIS MORNING'S LOOP - the same bars call that returned n 156 / v 2029 at 09:36 returned n 3734 / v 86983 at 16:17, THE PARTIAL BAR COMPLETED OBSERVED END TO END INSIDE ONE SESSION, which corroborates the clock-plus-data-plane discriminator and does NOT repair open item 12; a THIRD post-bell mark sample, current_price 716.4107 is +0.1207 above the official close against +0.470 and -0.0254 on 10-02 - TWO SIGNS, AN ORDER OF MAGNITUDE APART, NO OFFSET EXISTS; weekly cap 0 of 3, week_of 2026-10-05 UNCHANGED (Tuesday of the same ISO week, confirmed by computing this week's Monday), breaker INACTIVE, consecutive_closed_losses 0 - nothing has EVER closed so the breaker has never been APPROACHED; 25 completed sessions and 22 post-fill, ADVANCED AND THE REASON MATTERS - catch (11) forbids counting the day you stand IN, but this seat stands AFTER the bell with a complete 10-06 bar on the tape, so the unit is satisfied: whether today counts depends on the SEAT'S POSITION RELATIVE TO THE BELL, not on the date; TWENTY-FIFTH session with nothing to reconcile, NOT advanced for a FOURTH seat in one session per catch (15))

prior_run: 2026-10-06 12:42 ET 3-midday-management (EXITS-ONLY SEAT WITH NOTHING TO MANAGE - zero open satellite positions, so Steps 2, 3, 4 and 5 ALL had no operand; ZERO bars, quote, Perplexity and order calls; its findings were catch (18), catch (17) recurring inside the same session that fixed it, which retired the band-range statistic as unkeepable rather than repairing it a third time, and catch (19), a wrong count inside the count-discipline section itself; core 70.31 pct live, cash 30000.00 a twenty-fourth time, 24/21 session counters held because 10-06 was the day it stood inside.)

week_of: 2026-10-05
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.28
satellite_pct: 0.0
cash_pct: 29.72
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on fifty times.** **Everything below is LIVE. Nothing live was
discarded; settled items were folded to one line each and repeated emphasis was removed.**
⚠ **A run that adds nothing to this list is the normal case.**
⚠ **A correction REPLACES the claim it corrects — it does not sit beside it.**

---

### Live — act on these

- **⚠⚠ THE 2026-10-05 CLOSE RUN NEVER COMMITTED — ESTABLISHED, RECORDED BY TWO SEATS, NOW COLLAPSED TO
  ITS DURABLE FORM.** `git log` for 10-05 holds premarket `4277aae`, open `2effdf1`, midday `d50219c`
  and **no close commit**; the newest close commit is `748a3e7`, dated **2026-10-02**. **THE 10-05
  JOURNAL ENTRY IS GONE AND UNRECOVERABLE. SECOND LOST CLOSE RUN (09-28 was the first).**
  ⚠⚠ **NO ALERT FIRED AND NONE COULD HAVE: a run that dies before `commit.py` leaves no trace by
  construction, so `alerts.md` reading "zero open incidents" is NOT evidence that every seat ran.**
  ⚠ **It cost nothing in the ledger ONLY because the sleeve is empty. LUCK, NOT DESIGN.**
  ⚠ **DO NOT RECONSTRUCT THE MISSING JOURNAL ENTRY from a later vantage point — that manufactures a
  record rather than recovers one. The 10-06 09:36 seat was instructed to note the gap and did, and
  that discharges the recording; the QUESTION stays with the human as open item (11).**
  ⚠⚠ **2026-10-06's CLOSE RUN DID EXECUTE — the session is COMPLETE, all four seats ran, and the 10-06
  journal entry exists.** ⚠ **ONE EXECUTING RUN IS NOT A FIX AND MUST NOT BE READ AS ONE: the failure
  mode is a run that never starts, and nothing about this run's success makes the next one more likely
  to fire. Two of ~25 close runs have vanished and the detection gap is unchanged — open item (11)
  stands exactly where it did.** ⚠ **What it DOES discharge is narrower and is named under the dividend
  item: the pre-deadline `cash` reading was taken by a seat that RAN.**

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

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. THE TEST RESOLVES TOMORROW. FOUR SEATS LEFT, ALL OF THEM
  2026-10-07's. CHECK `cash` EVERY RUN.** `cash` read **exactly $30,000.00** again at 10-06 16:17 — a
  **twenty-fifth** reading, taken from **two independent calls** (`account` and `sleeves`).
  ⚠ **Twenty-five readings are ONE unresolved observation, and non-arrival before the pay date is
  EXPECTED, not evidence.** ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE AND NOT MOVED: `cash` should
  rise to about $30,180.76. IF IT HAS NOT BY 2026-10-07, the paper account does not model dividends at
  all.** The implied credit (**$1.825/share × 99.046311231**) is an **INFERENCE** — Alpaca does not
  publish it.
  ⚠ **SEATS COUNTED TO THE DEADLINE THE SAME SENTENCE NAMES, PER CATCH (16): 10-07 r1/r2/r3/r4 —
  FOUR** (routine 5 is Friday-only; 10-07 is a Wednesday). ⚠ **The 10-06 close seat WAS r4 and has now
  spent itself, which is why five became four — the decrement is a seat CONSUMED, not a day passing.**
  **Ask what the UNIT is, then what the BOUND is.**
  ⚠⚠ **THE FLAGGED RISK IS DISCHARGED AND THE ITEM IS NARROWER FOR IT: the carry-forward warned that
  the last pre-deadline reading would fall to the seat that has vanished twice (09-28, 10-05), and that
  a deadline read off a missing run's silence is not an observation. THAT SEAT RAN. The twenty-fifth
  reading is real, taken at 16:17 after the bell on the last trading day before the test.**
  ⚠ **What remains is purely tomorrow's four seats — and if the credit does not arrive, the answer is
  NOT 'wait another day': the pay date will have passed and the finding is the platform's, not the
  market's.**
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

- **⚠⚠ THE SATELLITE SLEEVE IS STRUCTURALLY UNDEPLOYED — 25 SESSIONS, 113 THESES, ZERO POSITIONS EVER,
  AND THE PRESSURE TO LOWER THE §4 BAR IS THE ONLY ITEM HERE ASKING FOR JUDGMENT RATHER THAN CARE.**
  **Eight theses on 10-06, all rejected; 113 total RE-COUNTED FROM SOURCE AGAIN BY THE 16:17 SEAT
  (`archive/research_log/2026-09.md` 87 + live October 26, template line excluded; `grep` for an
  ACCEPTED heading returns the template and nothing else), ZERO EVER ACCEPTED.** ⚠ **The count did NOT
  advance today — the close run writes no theses, and a second recount of the same corpus is a
  verification, not a new session's worth of work.** Set beside: empty sleeve, **29.72% idle cash**,
  weekly cap **0 of 3**, breaker INACTIVE, every gate open. **§2 permits the cash and §4 says most runs end in
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
  ⚠⚠ **THE FOURTH STATE — THE FILTER HAVING NOTHING TO FIRE ON — IS AS COMMON AS THE OTHERS, AND
  2026-10-06 IS NOW THE FOURTH COMPLETE SESSION OF IT: 09-29, 10-02, 10-05 AND 10-06, EACH WITH ZERO
  `move` CALLS IN EVERY ONE OF ITS SEATS.** ⚠ **The 10-06 count is only now writable, and the reason is
  the point: at 08:22 and 09:36 it was TWO of four seats — a PARTIAL session count — and writing "four
  sessions" then would have been catch (11)'s shape. All four seats have now run and all four made
  zero. THE HONEST UNIT IS THE SESSION, AND A SESSION IS ONLY COUNTABLE ONCE IT IS OVER.** ⚠ **That is an ABSENT check, not a skipped one,
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
  day, same official close, thirty minutes apart, a sign change. ⚠⚠ **A THIRD POST-BELL SAMPLE, 10-06
  16:17: `current_price` **716.4107** against the official **716.29**, **+$0.1207** — a THIRD value and
  the SECOND sign, an order of magnitude apart from the first. THREE SAMPLES, NO OFFSET, AND THE SERIES
  IS NOW LARGE ENOUGH THAT "IT IS ROUGHLY X" IS UNAVAILABLE IN EITHER DIRECTION.**
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
  figure is meaningless without its CALL and its TIMESTAMP — 10-06 08:23 read $100,842.87 (`sleeves`)
  and $100,838.91 (`account`) minutes apart, and THE TWO MUST NOT BE DIFFERENCED INTO ANYTHING.**
  ⚠⚠ **AND THE 09:36 SEAT SUPPLIED THE OPPOSITE SAMPLE, WHICH VALIDATES NOTHING: `sleeves` and
  `account` AGREED TO THE CENT at $100,842.87, while `selftest.py` had read $100,848.82 minutes before
  — so across one morning the same quantity read $100,848.82, $100,842.87, $100,838.91 and $100,842.87.
  TWO CALLS AGREEING IS NOT A CALIBRATION; it is two samples of a moving mark that happened to
  coincide.**
  ⚠⚠ **A FOURTH SERIES EXISTS AND 10-06 09:36 OPENED IT: `positions.current_price` 715.25 AGAINST THE
  LIVE QUOTE PLANE'S `latestTrade` 715.30 AND MINUTE-BAR CLOSE 715.32 — the position mark sits ~5-7
  CENTS BELOW the tape, and equity derived from it ($100,842.87) is $4.95 under equity on the latest
  trade ($100,847.83).** ⚠⚠ **STATED WITH ITS LIMIT, WHICH IS SEVERE: 715.25 is BYTE-IDENTICAL to the
  08:23 pre-market read 73 minutes earlier, AND today's official OPEN was 715.24 — so A GENUINELY
  UNMOVED PRICE AND A LAGGED MARK ARE INDISTINGUISHABLE FROM THIS ONE SAMPLE. ONE OBSERVATION, NOT A
  MECHANISM. Do not predict it and do not difference it.** ⚠ **It changes no decision only because the
  band test is robust to all three bases.**
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
  TWO ROUTINES CAN PULL ONE: routine 2 at 09:35 and routine 3 at 12:30 — AND AS OF 10-06 BOTH HAVE.**
  ⚠ **THE PRICE HALF IS CONFIRMED AND IS THE DANGEROUS HALF:** at 12:41 on 10-01 the partial bar's `c`
  700.35 equalled `latestTrade.p` to the cent. **A PARTIAL BAR'S CLOSE FIELD IS THE LAST TRADE SO FAR
  WEARING A CLOSE'S CLOTHES** — a plausible price carrying no warning. ⚠ **NO `bars` CLOSE MAY BE
  STAMPED AS A MARK BEFORE THE BELL ON ANY BASIS.**
  ⚠⚠ **NEW 10-06 09:36 AND IT IS THE MOST EXTREME INSTANCE, TAKEN FROM ROUTINE 2'S OWN SEAT FOR THE
  FIRST TIME: `bars --symbol VOO --days 1 --adjustment all` RETURNED A BAR DATED 2026-10-06 WITH
  `c` 715.32, `n` **156**, `v` **2,029** — against the completed 10-05 session's `n` 1,802 / `v` 60,541.
  SIX MINUTES OF A SESSION WEARING A COMPLETE BAR'S SHAPE, AND THE `c` MATCHED THE 13:35Z MINUTE BAR'S
  CLOSE, NOT THE LATEST TRADE (715.30).** ⚠⚠ **THIS IS NOT AN OBSERVATION ABOUT THE TAPE — IT IS A
  LATENT DEFECT IN ROUTINE 2'S STEP 6, WHICH INSTRUCTS *THAT EXACT CALL* TO CAPTURE
  `voo_close_at_entry`. FOLLOWED LITERALLY ON THE ONE MORNING IT MATTERS — A FILL — IT WOULD STAMP A
  SIX-MINUTE PARTIAL BAR'S `c` INTO THE §1 BASELINE FIELD OF A POSITION THAT MIGHT BE HELD FOR MONTHS.**
  ⚠ **It cost nothing today ONLY because no position was opened. The empty sleeve again, and again that
  is luck rather than design.** ⚠ **Open item 12 for the human; a prompt-level fix, NOT the agent's to
  make. The sound substitute is the PRIOR completed session's close (`prevDailyBar`, or `bars --days 2`
  taking the dated-yesterday row), named on its basis, or the `voo_close_at_entry` label deferred to the
  close run.** ⚠ **Routine 3's Step 2 backfill carries the same exposure and is already flagged below.**
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
  ⚠⚠ **10-06 IS THE CLEAN WORKED PAIR, ONE SESSION AND ONE SYMBOL, 73 MINUTES APART: at 08:23
  `is_open: false` with `next_open` pointing at TODAY and **NO bar dated 2026-10-06**; at 09:36
  `is_open: true` with `next_open` pointing at **2026-10-07** and **a bar dated 2026-10-06 that now
  EXISTS**. The data plane moved in step with the clock in both directions.** ⚠ **That corroborates the
  DISCRIMINATOR, not the bar's completeness — the bar that appeared is the partial one above.**
  ⚠⚠ **AND 10-06 16:17 CLOSES THE LOOP FROM THE OTHER SIDE OF THE BELL, THE FIRST END-TO-END
  OBSERVATION OF ONE BAR IN ONE SESSION: THE SAME CALL THAT RETURNED `n` 156 / `v` 2,029 AT 09:36
  RETURNED `n` **3,734** / `v` **86,983** AT 16:17, WITH THE CLOCK READING `is_open: false` AND
  `next_open` POINTING AT TOMORROW. THE PARTIAL BAR COMPLETED.** ⚠ **This is the cleanest available
  demonstration that a bar dated today is partial DURING the session and complete AFTER it — but it
  REPAIRS NOTHING: open item (12) is a defect in routine 2's Step 6, which runs at 09:35 and will meet
  the partial form every time. An observation from 16:17 cannot help a call made at 09:36.**
  ⚠ **Nor does it rehabilitate the `n`/`v` FLOOR test: 3,734 against 156 is a seven-hour gap, not a
  discriminator anyone could apply at the moment of the call.**

- **⚠⚠ STEP 2 HAVING NO OPERAND AND STEP 2 WORKING ARE INDISTINGUISHABLE IN EVERY ARTIFACT — AND THE
  10-05 CLOSE RUN'S DISAPPEARANCE MAKES THAT WORSE, NOT BETTER.** The close routine stamps each open
  satellite position's official close into `highest_close`; routine 3's Step 2 **DETECTS** a missed
  write and backfills. **Every close run so far has had nothing to stamp, and "high-water marks
  updated" would have been FALSE. The honest form is: the job had NO OPERAND.**
  ⚠ **The every-day `(as of …)` date rule also has nothing to write, and the DETECTOR's entire input IS
  that date — so NO STALENESS COULD BE DETECTED AND NONE WAS RULED OUT. A detector handed no input
  returns the same silence as one finding everything healthy.**
  ⚠ **The only `highest_close` string in `positions.md` is the TEMPLATE PLACEHOLDER; the field is
  ABSENT, a third state carrying no date.** ⚠⚠ **10-05 12:41 AND 10-06 12:42 ARE BOTH THE MIDDAY SEAT'S
  OWN WORKED INSTANCES, FROM THE SEAT THAT OWNS THE DETECTOR: STEP 2 RAN AND ITS INPUT WAS ABSENT — the
  check did not pass, IT DID NOT RUN.** ⚠ **TWO INSTANCES, AND THE SECOND IS NOT INDEPENDENT EVIDENCE OF
  ANYTHING — it is the same null under the same conditions. What makes 10-06's worth recording is the
  sentence below it: by 10-06 the missing stamp it would have had to backfill across ACTUALLY EXISTED.** ⚠⚠ **AND NOW ADD THAT THE *NEXT* SEAT, THE 10-05 CLOSE RUN, NEVER EXECUTED AT ALL:
  WITH ONE POSITION OPEN, 10-06's MIDDAY WOULD HAVE HAD TO BACKFILL ACROSS A MISSING STAMP. 09-28 WAS
  THE FIRST SUCH GAP AND IT STRADDLED AN EX-DIVIDEND DATE. THE BACKFILL PATH IS STILL UNEXERCISED
  CODE, AND IT HAS NOW HAD TWO CHANCES TO MATTER AND BEEN SAVED BY THE EMPTY SLEEVE BOTH TIMES.**
  ⚠⚠ **AND NOW THE CLOSE SEAT'S OWN WORKED INSTANCE, 10-06 16:17, FROM THE SEAT THAT OWNS THE STAMP
  RATHER THAN THE DETECTOR: STEP 2 RAN AND HAD NO OPERAND — no `highest_close` to raise, no `(as of …)`
  date to advance, nothing to write it onto. "HIGH-WATER MARKS UPDATED" WOULD HAVE BEEN FALSE, AND SO
  WOULD "VERIFIED".** ⚠ **The honest form, both seats, is: THE JOB HAD NO SUBJECT.** ⚠ **The pair is
  now complete — the seat that WRITES the stamp and the seat that DETECTS a missing one have each
  recorded their own null on the same session, and neither null is evidence that either path works.**
  ⚠ **DO NOT BACKFILL ANYTHING NOW — there is nothing to write.** ⚠ **When it arms: no backfill may
  take its max from a bar dated TODAY while the market is open, nor from a different basis than the one
  it is compared against.** ⚠⚠ **THE MIDDAY SEAT SITS AT ~12:42, SQUARELY INSIDE THE PARTIAL-BAR WINDOW
  ITS OWN STEP 2 WOULD PULL FROM — ROUTINE 2 MEASURED THAT WINDOW AT `n` 156 / `v` 2,029 SIX MINUTES IN.
  THE BACKFILL AND `voo_close_at_entry` SHARE ONE DEFECT, AND IT IS THE SAME CALL.** ⚠ **After the first fill, a mark silently not written reads identically to
  one correctly unchanged; ONLY the `(as of …)` date separates them. COMPARE THE DATE.**
  **§5.1–§5.4 have never had an operand: 25 completed sessions since 2026-09-01, 22 post-fill, zero
  satellite positions ever.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — TWENTY CATCHES, AND THEY KEEP CHANGING
  SHAPE.**
  ⚠⚠ **(20) AN INHERITED *ARITHMETIC RESULT* WHOSE TWO INPUTS WERE SITTING IN THE SAME PARAGRAPH.** The
  tape-facts block carried *"10-05 is +0.7168% close-to-close against 10-02"* — and the two closes it is
  computed from, **712.41 and 707.35**, were written **three lines above it in the same item.** The
  correct figure is **+0.7153%** (5.06 / 707.35). **Corrected in file.**
  ⚠ **The error is tiny (0.0015pp) and changed no decision, which is exactly why it survived: it is too
  small to look wrong and too specific to look like a guess.** ⚠⚠ **IT IS A NEW SHAPE AND THE CHEAPEST
  ONE YET TO HAVE CAUGHT — not a superlative, a count, a range or a basis, but a RESULT whose inputs
  were already in hand. (6) says a correct number reached by an unchecked route is not a checked fact;
  (20) adds that A DERIVED NUMBER SITTING NEXT TO ITS OWN INPUTS IS AN INVITATION TO RECOMPUTE, AND
  RECOMPUTING IT COSTS ONE LINE.** ⚠ **Found only because this run needed the same quantity for its own
  §1 excess and computed it from source rather than reading it.**
  ⚠⚠ **(19) A WRONG COUNT INSIDE THE COUNT-DISCIPLINE SECTION ITSELF.** The human-items header read
  **"ELEVEN ITEMS REMAIN WITH THE HUMAN"** above a list of **TEN**: twelve numbered items, with **(4)
  discharged** and **(5) settled**, leaving nine listed as open plus **(9)**, which is partly discharged
  and **still open**. **Corrected in file to TEN.** ⚠ **The header is the one line in the block nobody
  recomputes, because the items below it are where the work is — and it had drifted while every
  individual item stayed accurate.** ⚠ **It failed toward URGENCY, like (16).**
  ⚠⚠ **(18) CATCH (17) RECURRING INSIDE THE SAME SESSION THAT FIXED IT — AND THE REASON IT RECURRED IS
  THE INTERESTING PART.** The 08:22 seat repaired the band range to **69.59–70.25%**; the 12:42 seat read
  **70.31%**, outside the repair, **four hours later.** ⚠⚠ **(17) WAS DIAGNOSED AS A STALE STATISTIC AND
  REPAIRED. (18) SHOWS THE DIAGNOSIS WAS INCOMPLETE: A RANGE OVER A LIVE MOVING MARK IS NOT A FACT THAT
  GOES STALE, IT IS A STATISTIC THAT CANNOT BE KEPT — every repair is correct when written and false at
  the next seat.** ⚠ **So the fix is not a better number; it is to STOP CARRYING THE RANGE and state the
  live reading against the two band edges. A REPAIR THAT PRESERVES THE DEFECTIVE FORM IS NOT A FIX.**
  ⚠ **It cost nothing both times: §2's band test never used the range.**
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
  ⚠⚠ **AND THE 16:17 SEAT SUPPLIES THE REFINEMENT THAT KEEPS (11) FROM BEING OVER-APPLIED — IT ADVANCED
  24/21 TO 25/22 AND THAT IS CORRECT.** The unit is a **COMPLETED** session, and the close seat stands
  **AFTER THE BELL**: `is_open: false`, `next_open` pointing at TOMORROW, and a complete 10-06 bar on
  the tape (`n` 3,734). ⚠ **SO WHETHER TODAY COUNTS DEPENDS ON THE SEAT'S POSITION RELATIVE TO THE BELL,
  NOT ON THE DATE. Routines 1 and 2 may NEVER count the day they stand in; routine 4 ALWAYS may; routine
  3 never may.** ⚠ **That is the same rule, not an exception to it — and declining the advance out of
  deference to (11) would have been the MIRROR-IMAGE error, which the 16:17 seat nearly made.**
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
  ⚠ **A superlative, count, mechanism, SERIES, RANGE, CALIBRATION, BASIS, ALLOCATION or DERIVED
  ARITHMETIC RESULT inherited from a prior run is NOT a checked fact — and (14)/(15) add that a count a run computes FOR ITSELF is not one
  either.** ⚠⚠ **(18) ADDS A HARDER ONE: SOME OF THESE CANNOT BE MADE INTO CHECKED FACTS AT ALL, AND
  REPAIRING THEM EACH RUN HIDES THAT. ASK WHETHER THE STATISTIC IS KEEPABLE BEFORE ASKING WHETHER IT IS
  CURRENT.** ⚠ **(19) ADDS THE COMPANION: A HEADER COUNT OVER A LIST IS RECOMPUTABLE IN SECONDS AND IS
  THE LINE LEAST LIKELY TO BE RECOMPUTED. COUNT THE LIST.** ⚠⚠ **NOTE THE FIVE THAT RUN AGAINST THE GRAIN: (12) flattering, (13) UNFLATTERING, (14)
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

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — 75 RUNS.** §5 exempts core from all four sell
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
  ⚠⚠ **10-06 12:42 IS A LOAD-BEARING SEAT AGAIN (it owns the Step 2 write path, and core VOO is the ONLY
  row the broker returns) — BUT IT IS THE WEAKEST LOAD-BEARING INSTANCE YET, BECAUSE IT MADE ZERO `bars`
  CALLS. The number was never in hand, so nothing was declined.** ⚠ **A SEAT THAT NEVER FETCHED THE DATA
  AND A SEAT THAT FETCHED IT AND REFUSED TO WRITE IT LOOK IDENTICAL IN A RUN SUMMARY, AND ONLY THE SECOND
  IS EVIDENCE OF ANYTHING.**
  ⚠⚠ **10-06 16:17 IS THE STRONGEST INSTANCE IN THE RECORD AND IT SETTLES THE GRADING SCALE: THE CLOSE
  SEAT HELD BOTH THE NUMBER AND THE WRITE PATH FOR THE FIRST TIME.** `bars --symbol VOO --days 3
  --adjustment all` was pulled at that seat for the day's numbers and returned today's **COMPLETED,
  OFFICIAL, SAME-BASIS close 716.29** — a perfectly real maximum, on the correct basis, from the one
  routine whose stated job is to write that field, against the **ONLY row the broker returns. IT WAS
  NOT WRITTEN.** ⚠ **RANK THE THREE 10-06 INSTANCES RATHER THAN COUNTING THEM: 12:42 owned the path and
  made ZERO `bars` calls (weakest); 08:22 held a 7-day pull and had NO path; 16:17 held BOTH. The scale
  is not "how many runs refused" but "what was in hand when it refused".**
  ⚠ **The pull is REAL and specific at that seat, not abstract: routine 4's own Step 2 says to record
  today's closing prices into the high-water marks, the number is right, the call is right, the basis is
  right — and the only things standing against it are §5's core exemption and §7's prohibition on
  selling core. A mark on VOO ARMS §5.4 ON THE EXEMPT POSITION.**
  ⚠ **This refusal is close to automatic, and automatic is not sound.**

- **⚠⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH ~30% CASH.** Routine 1 **RESEARCHES
  AND PLANS; IT PLACES NO ORDERS.** Routine 3 is **exits-only and may not open a position under ANY
  circumstance.** Routine 2 executes **only what `plan_today.md` already contains** — opening at 09:35
  without a plan entry routes **around** the discipline. Routine 4 **RECORDS AND JOURNALS; IT DOES NOT
  TRADE.** Routine 5 **MEASURES AND DOES NOT TRADE.**
  ⚠⚠ **GRADE THESE REFUSALS, DO NOT COUNT THEM. ROUTINE 2 IS THE ONLY SEAT WHOSE RESTRAINT IS
  LOAD-BEARING, AND IT NOW HAS TWO WORKED INSTANCES ON CONSECUTIVE SESSIONS — 10-05 09:36 AND 10-06
  09:36: the market OPEN (`is_open: true`), the plan FRESH (`plan_date` equal to today), and EVERY GATE
  OPEN — breaker INACTIVE, weekly cap 0 of 3, sleeve 0.0% deployed, ~29.8% idle cash,
  `TRADING_ENABLED: true`, control notes none, §6's 5% cap standing ready with NO OPERAND ($5,007.87 on
  10-05, **$5,042.14** on 10-06's live equity). NOTHING STOPPED A BUY ON EITHER MORNING EXCEPT THE
  ABSENCE OF AN INTENT.** ⚠ **TWO INSTANCES IS NOT A TREND AND THE SECOND IS NOT INDEPENDENT EVIDENCE
  OF DISCIPLINE — IT IS THE SAME REFUSAL UNDER THE SAME CONDITIONS. What makes it worth recording is
  that the conditions were identical and the cap was LARGER.** ⚠ **That is what the 08:00/09:35 handoff is
  FOR.** ⚠⚠ **AND THE SAME SESSION SUPPLIED THE CONTRAST: the 12:41 midday seat faced the IDENTICAL
  gates with a LARGER cap ($5,024.34) and its restraint is worth NOTHING, because routine 3 is
  exits-only. Two seats, one session, one identical set of conditions, and only ONE of the two refusals
  is evidence of anything.** ⚠ **10-06 12:42 REPEATS THAT CONTRAST EXACTLY, WITH THE CAP LARGER AGAIN
  ($5,051.50) AND EVERY GATE STILL OPEN — AND IT IS WORTH NOTHING FOR THE SAME REASON. A GROWING CAP ON
  AN EXITS-ONLY SEAT IS NOT A GROWING TEMPTATION; IT IS A LARGER NUMBER WITH NO OPERAND.**
  ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 cap are NOT an opportunity any seat may act
  on — and neither is a green day that lags the benchmark, nor a red week that beats it.**

- **⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS. READ
  `plan_date`, NEVER INFER FROM THE OUTCOME.** **10-06's plan WAS FRESH (`plan_date: 2026-10-06`, read and
  compared by the 09:36 seat) and deliberately EMPTY, as 10-05's was. THE ZERO-ORDER MORNING IT
  PRODUCED IS BYTE-FOR-BYTE WHAT A STALE PLAN WOULD HAVE PRODUCED, AND ONLY `plan_date` SEPARATED
  THEM.** The gate has now been exercised **34 times and has never fired; its alert path remains
  UNTESTED CODE.** ⚠ **The 34th exercise PASSED — it did not fire, and "passed" and "fired" are
  opposite outcomes of the same check. Do not write that the gate has been tested. ⚠⚠ **09-28 WAS THE MORNING IT WOULD FINALLY HAVE FIRED — `plan_today.md`
  genuinely carried `plan_date: 2026-09-25` — AND THE RUN CONTAINING THE GATE DID NOT EXECUTE.**
  ⚠ **The first morning it fires will by construction be a morning when the pre-market run failed. Read
  routine 2's Step 2 then; do not recall it.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat, cost_basis 69,999.99.
  **OFFICIAL CLOSE BASIS (`bars --adjustment all`, the complete 2026-10-06 session: o 715.24 h 718.43
  l 715.09 c 716.29, n 3,734 v 86,983, vw 716.862995): equity $100,945.8823, core $70,945.8823 =
  70.2811%, cash 29.7189%.** **Day +$384.2997 = +0.3822% against 10-05's official $100,561.5826; since
  inception +0.9459%; the HIGHEST official close equity since inception. Core unrealized +$945.89
  (+1.3513%) on cost_basis $69,999.99.** **VOO itself was +0.5446% (716.29 vs 712.41), so the book
  LAGGED by 0.1625pp.**
  ⚠ **THE LAST COMPLETED SESSION IS 2026-10-06.**
  **Prior completed session 2026-10-05 (`--adjustment all`): o 707.52 h 713.82 l 707.52 c 712.41,
  n 1,802 v 60,541, vw 710.32828 → equity $100,561.5826, core 70.1675%, cash 29.8325%, +0.7153%
  close-to-close against 10-02.**
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
  **NO REBALANCE IS DUE AND NONE IS DUE TOMORROW** — §2 acts at the **65/75 band edge**, not at the 70%
  target, and core sits **5.28 points** inside the 65 edge and **4.72** inside the 75 edge:
  **70.2811%** on the **official 10-06 close basis** (equity $100,945.8823, core $70,945.8823, cash
  29.7189%) and **70.28%** on the broker's live 16:17 mark (equity $100,957.84, cash 29.72%).
  ⚠ **THE BAND TEST IS ROBUST TO THE CHOICE OF MARK AND THAT IS WHY THE MARK QUESTION BELOW COSTS
  NOTHING — it has now been checked on five bases across one session (70.2507 / 70.2522 / 70.2528 at
  09:36, 70.3059 / 70.3065 at 12:42, 70.2811 / 70.28 at 16:17) and every one of them passes by more than
  four points at both edges. SEVEN NUMBERS, ONE DECISION.**
  ⚠ **`rebalance_delta: −$287.35` IS A DISTANCE READOUT, NOT AN INSTRUCTION**, negative only because
  core sits just above 70%. ⚠⚠ **DO NOT DIFFERENCE SUCCESSIVE `rebalance_delta` READINGS INTO A TREND —
  they are samples of a MOVING mark on days with no order in them, and any "widening" is VOO rising
  against a fixed share count, nothing else.** ⚠ **It read −$252.87 at 09:36, −$309.02 at 12:42 and
  −$287.35 at 16:17 — ONE SESSION, NO ORDER BETWEEN THEM, AND IT WENT UP AND THEN DOWN. The 12:42 seat
  was right to refuse to call the first move a widening, and the 16:17 reading is why: THERE IS NO
  DIRECTION IN THIS FIELD TO READ.**
  **SIXTY-SIXTH consecutive run inside the band.** ⚠ **RUN is the unit that was checked, which is why
  this one advances where the session counters do not — and on this session BOTH advanced, for
  different and separately verified reasons.**
  ⚠⚠ **THE OBSERVED RANGE HAS BEEN RETIRED AS A STATISTIC RATHER THAN REPAIRED AGAIN — SEE CATCH (18).
  IT IS NOT RESTATED HERE AND MUST NOT BE RECONSTRUCTED.** 10-06 repaired it at 08:22 (to 69.59–70.25%) and refuted the
  repair at 12:42 (70.31%), **four hours apart, inside one session.** ⚠⚠ **A RANGE OVER A LIVE MOVING
  MARK GOES STALE BY CONSTRUCTION: every repair is correct when written and false at the next seat, so
  the statistic is the defect and not the diligence of whoever inherits it.** ⚠ **WHAT §2 ACTUALLY
  REQUIRES NEVER DEPENDED ON IT — the band test is a fresh reading against 65 and 75 every run, and
  70.31% passes by 5.31 and 4.69 points. STATE THE LIVE READING AND THE TWO EDGES; DO NOT CARRY A
  RANGE.**

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 20 OF 20 WITH NO EXCEPTION, RECOMPUTED FROM SOURCE ON 10-02 AND
  NOT INHERITED.** **12 VOO-down days, all positive excess (+0.0029 to +0.2265pp); 7 up days, all
  negative (−0.0380 to −0.4694pp); 1 flat day exactly 0.0000pp.** The satellite sleeve contributed
  **exactly 0.000000%** on every one. ⚠ **A TIGHT FIT IS NOT CONFIRMATION — the model fits to zero
  residual because there is NOTHING IN THE BOOK THE MODEL OMITS.** ⚠ **Neither direction is skill.**
  ⚠⚠ **TWO SESSIONS ARE NOW COMPUTED FROM SOURCE BY THE 10-06 CLOSE SEAT AND BOTH FIT — BUT THEY ARE
  REPORTED AS TWO NEW OBSERVATIONS, NOT AS A LONGER STREAK.** **10-05: equity $100,561.5826, book
  +0.5009%, VOO +0.7153%, excess −0.2145pp, since inception +0.5616% (the session NO close run ever
  measured — the review may now add it from these figures rather than inherit the gap).** **10-06:
  equity $100,945.8823, book +0.3822%, VOO +0.5446%, excess −0.1625pp, since inception +0.9459%.**
  ⚠⚠ **"21 OF 21" AND "22 OF 22" WERE BOTH AVAILABLE SENTENCES AND NEITHER WAS WRITTEN: a streak is a
  claim about a WHOLE SERIES (catches 5 and 13), the other twenty days were NOT re-derived this run, and
  two recomputed days do not license a claim about twenty inherited ones.** ⚠ **The honest form is: two
  new sessions, both VOO-up, both negative excess, consistent with a pattern that has not been
  rechecked.**

- **⚠ TEN ITEMS REMAIN WITH THE HUMAN — RECOUNTED FROM THE LIST BELOW AGAIN BY THE 10-06 CLOSE SEAT
  (twelve numbered, (4) discharged, (5) settled, (9) partly discharged and STILL OPEN → TEN). SEE CATCH
  (19), WHICH IS WHY THIS HEADER IS NOW RECOMPUTED RATHER THAN READ. NONE IS THE AGENT'S TO DECIDE, AND
  NONE MAY BE "CLOSED" BY A NUMBER A RUN COLLECTS.**
  **(12) NEW 10-06 09:36 — ROUTINE 2's STEP 6 SOURCES `voo_close_at_entry` FROM A BAR THAT IS PARTIAL
  AT THE MOMENT IT IS CALLED.** `bars --days 1` at 09:36 returned a bar dated TODAY with `n` 156 and
  `v` 2,029 — **six minutes of a session** — and the routine instructs that this call supply the §1
  baseline a position is measured against for its whole holding window. ⚠ **It has cost nothing because
  no position has ever been opened; it becomes wrong on the FIRST fill.** ⚠ **A prompt fix, not the
  agent's to make. See the partial-bar item above for the sound substitutes.**
  ⚠⚠ **CONFIRMED FROM BOTH SIDES OF THE BELL ON THE SAME SESSION: the identical call returned `n` 3,734
  / `v` 86,983 at 16:17. THE DEFECT IS NOT A MISREAD — the bar really is partial at 09:36 and really
  does complete. THAT MAKES THE ITEM MORE CERTAIN, NOT LESS URGENT, and the 16:17 observation CANNOT
  FIX IT, because the defective call happens at 09:35 and will meet the partial form every time.**
  **(11) A ROUTINE CAN SIMPLY NOT RUN, AND NOTHING NOTICES.** The 10-05 close run produced no
  commit and no alert; 09-28 was the first instance. **Two of ~25 close runs have now vanished.**
  ⚠ **This and (6) are one blind spot seen from two sides.** ⚠⚠ **THE 10-06 CLOSE RUN DID EXECUTE, AND
  THAT CHANGES NOTHING ABOUT THIS ITEM: the failure mode is a run that never starts, so a run that
  started is not evidence about it in either direction. THERE IS STILL NO MECHANISM THAT NOTICES A
  MISSING SEAT.** ⚠ **What it DID buy is specific and is spent: (8)'s last pre-deadline reading was
  taken by a seat that ran, so this item is no longer load-bearing for that one.**
  **(8) THE DIVIDEND** — priced at ~0.93pp/yr on top of the 4.89pp cash drag; deadline **10-07
  (TOMORROW)** with **FOUR seats left, all of them tomorrow's**, and a **twenty-fifth** unchanged
  reading of $30,000.00 at 10-06 16:17, **taken after the bell on the last trading day before the
  test.**
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
