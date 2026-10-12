# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-10-12 12:42 ET 3-midday-management (SEAT 3 OF 4, MONDAY. THE EXITS-ONLY SEAT WITH NOTHING TO EXIT - and that is the whole run. selftest PASSED all five, trading_enabled true, LIVE paper, equity 100,856.74 at pre-flight / 100,859.71 at `sleeves`. CLOCK 12:42:05 is_open TRUE with next_close TODAY 16:00 and next_open 2026-10-13 - the mid-session signature; the closed-skip path was not taken. ZERO OPEN SATELLITE POSITIONS, so §5.1-5.4 AGAIN HAD NO OPERAND and the routine's own instruction applies verbatim: there is nothing to manage, note it and exit, DO NOT GO LOOKING FOR SOMETHING TO DO. All four rules were RE-EVALUATED IN §5's ORDER AND REACHED, NOT INHERITED - no `invalidation` string to read verbatim, no `timing_window`, no satellite `entry_price` for the -7% hard stop, no `highest_close` so 5.4 is NOT ARMED; distance to each is UNDEFINED, NOT LARGE. Core VOO struck from the working list BEFORE any rule was read, per §5's exemption. ⚠ STEP 2, THE ONE THIS SEAT OWNS ALONE, DID NOT RUN - FOR THE RIGHT REASON, WHICH IS NOT PASSING: `highest_close` is ABSENT (the third state, no `(as of ...)` date at all), so the staleness comparison had NO LEFT-HAND SIDE and 'high-water marks verified' would have been FALSE; the backfill path remains UNEXERCISED CODE and arms on the first SATELLITE fill. ⚠ ONE `bars` CALL WAS MADE - `--days 4 --adjustment all`, to establish the last trading day's official close (2026-10-09 c 715.58) as the comparison's RIGHT-hand side - AND THE FIRST DRAFT OF THE positions.md PARAGRAPH SAID 'ZERO bars CALLS', CORRECTED BEFORE PUBLICATION: the call establishes the REFERENCE, not a repair, and 'I pulled bars for Step 2' reads as a backfill that did not happen. The same pull returned a PARTIAL 2026-10-12 bar (c 715.28, n 526, v 11,409) and its `c` was NOT stamped as anything. ZERO quote calls (Step 1's per-ticker list is EMPTY and a decorative quote on the exempt core would fake an exercise), ZERO Perplexity (5.1's query is written for a named company and there is none), ZERO sell calls, ZERO orders - EVERY ONE AN ABSENT CHECK, NOT A PASSING ONE. NOTHING SHOULD HAVE EXECUTED AND NOTHING DID; TRADING_ENABLED true, so no exit was suppressed into a dry-run intent and there is no suppressed-stop line to lead with. ⚠⚠ CATCH (25) - A STALE BODY UNDER A FRESHLY RE-DATED HEADING, THE MIRROR IMAGE OF THE ONE ERROR THAT SECTION'S OWN WARNING NAMES: the 09:37 seat re-dated positions.md's `sell_rule_status` heading to 2026-10-12 and left the body reading 'THE THESIS COUNT ... STAYS AT 138 - the 08:27 pre-market seat already wrote today's eight into it ... DO NOT FIX 138 TO 146'. Every number there is 2026-10-09's: today's pre-market was 08:36, it wrote FIVE theses, and the count it left was 143. A stale date on a null table was the error that section guarded against; a FRESH DATE OVER A STALE BODY is strictly worse, because the date is what a reader uses to decide the numbers beneath it are current. ⚠ 143 WAS RE-DERIVED FROM SOURCE BY AN INDEPENDENT ROUTE rather than inherited: 87 archived (`archive/research_log/2026-09.md`) + 56 live `### T-` headings = 143, confirming the pre-market figure - AND BOTH OBVIOUS SHORTCUTS ARE WRONG IN OPPOSITE DIRECTIONS, which is the part to carry: `grep -c '^### T-'` returns 57 because the file's own TEMPLATE heading matches (144, looks like a off-by-one worth 'fixing' - DO NOT), while distinct `T-20..` IDs return 59 because of 3 prose CROSS-REFERENCES to disposed IDs. The thesis count does NOT move at this seat; routine 3 writes no theses. SLEEVES: core 70,859.711981 / 100,859.71 = 70.26%, IN BAND by 5.26 and 4.74 points, 81st consecutive run, satellite 0.0% (count 0), cash 30,000.00 = 29.74%; rebalance_delta -257.91 NARROWED from -279.70 at 09:37 purely because VOO fell back (715.42 vs 716.1532) - a third consecutive sample arguing against differencing successive readings - and IT IS NOT THIS SEAT'S TO ACT ON IN ANY CASE, routine 3 holds no buy path. ⚠ `lastday_price` 715.59 is NOT 10-09's official close 715.58 from the 08:36 bars pull - a 1c disagreement between the broker's prior-day field and the completed bar on the SAME session, reported rather than reconciled away. HOUSEKEEPING, ALL 'DO NOTHING FOR THE RIGHT REASON': week anchor RECOMPUTED (today IS Monday, ISO anchor IS 2026-10-12) and found matching week_of, DELIBERATELY NOT RE-RESET, 0 of 3 weekly; breaker INACTIVE with halt_triggered_at none so NO HALT_CLEARED_AT comparison was due; control.md notes EMPTY; consecutive_closed_losses 0 and THE UPDATE WAS NEVER REACHED - zero exits means an UNTOUCHED counter, not a reset one, and the increment plus `clickup.py alert --key circuit-breaker` paths remain UNTESTED CODE. Session counter HOLDS at 28 completed / 25 post-fill - 10-12 is mid-session at this seat and ROUTINE 3 MAY NEVER ADVANCE IT (catch (21)'s shape, declined deliberately for the tenth time). `orders --status all` still returns ONE ROW FOR THE WHOLE ACCOUNT HISTORY (the 09-03 core fill, terminal), so §7's limbo warning has NO OPERAND rather than a clean bill. CORE VOO NOT STAMPED WITH A `highest_close` FOR A 90th RUN, AND THIS SEAT'S INSTANCE IS THE STRONGEST FORM AVAILABLE TO IT: it HELD a real completed official close (10-09 715.58, correct basis) AND owns a Step 2 WRITE PATH into the field, on the ONLY row the broker returns, and declined - writing it would ARM §5.4 ON THE ONE POSITION §5 EXEMPTS, a trailing stop that could eventually sell core, which §7 forbids outright. FILE SIZES - A REAL REDUCTION AND IT IS REPORTED AS AN OFFSET THAT WAS OWED, NOT A VIRTUE: positions.md 99,088B -> 85,955B, a NET -13,133B, arrived at by ADDING ~3.2KB (catch (25), the midday fold into today's block, the bars-call correction) and then COLLAPSING 2026-10-06's FOUR PER-SEAT SECTIONS to one digest (275 lines -> 79) - 10-06 was the LAST date still carrying raw per-seat narrative, 10-07 and 10-08 being digests already. Every durable 10-06 finding was carried: open item (12)'s partial-bar defect with its numbers, the 10-05 lost close run, the partial bar observed end-to-end (156/2,029 -> 3,734/86,983), catches (17)+(18), the three-way `highest_close` grading this seat's own grade comes from, the three price series and the destroyed offsets, the four-marks-in-one-minute item, `last_equity`'s attribution, and Step 1's empty-symbol-list rule. state.md went the OTHER way, 125,763B -> about 127.5KB (+1.7KB), so NET ACROSS THE SET about -11.4KB with plan_today.md, research_log.md, trade_log.md and journal.md UNTOUCHED - this seat writes no theses, had no fills to log and skipped nothing on priced-in grounds. ⚠ AND THE 10-12 BLOCK IN positions.md IS NOW THE LARGEST IN THAT FILE AT 161 LINES because folding a third seat into it grew it: collapsing an old date and folding a new seat push in OPPOSITE directions, so the debt moves to the front of the file rather than clearing. ⚠ ITEM (9) STILL STANDS: this paragraph is itself ~3.5KB of the kind of recording that eats such savings, and the right fix remains a prompt-level archivable unit rather than more discipline)
prior_run: 2026-10-12 09:37 ET 2-market-open-execution (SEAT 2 OF 4, THE ONLY SEAT THAT OPENS POSITIONS, AND IT OPENED NONE - zero orders with NOT ONE GATE BLOCKING: breaker INACTIVE, 0 of 3 weekly, satellite 0.0% against a 30% target, $30,000 IDLE, 5% cap $5,046.62, TRADING_ENABLED true, control notes empty. An empty plan is a complete instruction, not a gap to fill. STALENESS GATE EXERCISED BY THE SEAT THAT HOLDS IT: plan_date READ OFF THE FIELD = 2026-10-12 against the CLOCK's ET date - FRESH, so it did not fire; non-exercise count 38, STILL NEVER FIRED, alert path UNTESTED. ⚠ THE PLAN WAS FRESH *AND* EMPTY, which is the case where freshness cannot be inferred from the outcome - a fresh empty plan and a stale plan produce a byte-identical zero-order run, so the record of WHICH is the only thing separating them: FRESH, fifth consecutive such morning. Reconciliation clean and done FIRST (one row core VOO 99.046311231 at 706.74 against zero satellite blocks). Step 3 skipped on core_established true; Step 4 had no operand so the loss-streak update was never reached; Steps 5-6 had no input, and all five of T-2026-10-12-01..-05 were CONFIRMED PRESENT AND REJECTED before concluding it. GFS and ELMT NOT re-screened. Core 70.28% live, in band, 80th run, rebalance_delta -$279.70 a DISTANCE READOUT NOT AN INSTRUCTION. Zero `move` calls - ABSENT, not passing. ⚠ THIS SEAT LEFT CATCH (25) BEHIND IT: it re-dated positions.md's `sell_rule_status` heading to today and left 10-09's thesis numbers in the body, found and corrected by the 12:42 seat)
week_of: 2026-10-12
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.26
satellite_pct: 0.0
cash_pct: 29.74
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

- **⚠ TUESDAY 2026-10-13 HANDOFF — WRITTEN BY THE 10-12 OPEN SEAT, WHICH SPENT THE MONDAY ITEM IN FULL.**
  *(The Monday handoff and its own answer are REPLACED by this one line each, not kept side by side: the
  plan was FRESH, the gate did not fire, core stayed in band, no backfill was due, and all three of the
  Monday item's "do nothing, for the right reason" calls came out as written.)*
  ⚠⚠ **10-12 PLACED ZERO ORDERS AT THE ONE SEAT THAT CAN OPEN A POSITION, AND NOT ONE GATE BLOCKED IT.**
  The plan was **FRESH (`plan_date: 2026-10-12`, read off the field and compared to the CLOCK's ET date)
  AND EMPTY**, while breaker was **INACTIVE**, weekly count **0 of 3**, satellite **0% deployed with
  $30,000 idle**, `TRADING_ENABLED` **true** and the §6 cap standing at **$5,046.62**. **A buy was
  placeable all morning. Nothing was worth buying, and an empty plan is a complete instruction rather
  than a gap to fill.**
  ⚠ **TOMORROW'S GATE READS THE ORDINARY SHAPE: the comparison is against **2026-10-12** — ONE trading
  day and ONE calendar day back, not Monday's three.** **Non-exercise count stands at 38; the gate has
  STILL never fired and its alert path is STILL untested code.**
  **Core 70.28% live at 09:37 (70,932.332736 / 100,932.33), IN BAND with 4.72 points of headroom, 80th
  consecutive run — NO REBALANCE DUE.** `rebalance_delta` −$279.70 is a distance readout, not an
  instruction, and it **widened** from −$262.37 at 08:36 only because VOO rose intraday.
  ⚠ **Nothing is unresolved: zero open alerts, zero non-terminal orders, zero satellite positions,
  breaker INACTIVE with `halt_triggered_at: none` so no `HALT_CLEARED_AT` comparison is due, and
  `control.md` notes empty.** **Ledger reconciled against the broker at this seat: one VOO row,
  99.046311231 at 706.74, against zero satellite blocks.**
  ⚠⚠ **ALL FIVE 10-12 THESES WERE CONFIRMED PRESENT AND REJECTED IN `research_log.md` BY THIS SEAT
  BEFORE IT CONCLUDED THERE WAS NOTHING TO EXECUTE — `T-2026-10-12-01` … `-05`, four of them carrying no
  ticker at all. Thesis count HOLDS at 143; nothing was skipped on priced-in grounds, so the open seat
  added no line to the research log.**
  ⚠ **THE SESSION COUNTER HOLDS AT 28 COMPLETED / 25 POST-FILL. The unit is a COMPLETED session and
  10-12 was still mid-session when the open seat ran. DO NOT "FIX" 28 TO 29 — catch (21)'s shape for the
  NINTH time, and catch (22) is the worked failure of stating the rule correctly and then writing the
  advanced number anyway.**
  **— APPENDED BY THE 12:42 MIDDAY SEAT, WHICH SPENT ITS HALF OF THIS ITEM AND ADDS THREE THINGS.**
  ⚠⚠ **(a) CATCH (25) IS RECORDED AND FIXED IN FILE — A FRESH DATE OVER A STALE BODY.** The open seat
  re-dated `positions.md`'s `sell_rule_status` heading to 2026-10-12 and left 10-09's numbers under it
  (thesis count **138**, "today's **eight**", "DO NOT FIX 138 TO 146"). **The heading is what a reader
  trusts to decide the body is current, so this is worse than the stale date the section warned about.**
  ⚠ **THE GENERAL FORM FOR TOMORROW: WHEN YOU RE-DATE A SECTION, YOU HAVE ADOPTED EVERY NUMBER IN IT.
  Re-date the body or do not re-date the heading.**
  ⚠ **(b) `positions.md` IS 85,955B, DOWN FROM 99,088B — and 2026-10-06 WAS THE LAST DATE CARRYING RAW
  PER-SEAT NARRATIVE. IT IS NOW A DIGEST; DO NOT COLLAPSE IT AGAIN.** **The remaining long blocks,
  MEASURED RATHER THAN GUESSED: 2026-09-28 at line ~630 is 160 LINES FOR A SINGLE RUN (the largest
  per-line-per-run ratio in the file) and 2026-09-24 at line ~812 is 131 lines for four runs; everything
  else is already a digest.**
  ⚠⚠ **AND THE UNCOMFORTABLE MEASUREMENT: TODAY'S OWN 10-12 BLOCK IS NOW THE LARGEST IN THE FILE AT 161
  LINES, BECAUSE FOLDING A THIRD SEAT INTO IT GREW IT.** **Collapsing an old date and folding a new seat
  push in opposite directions, so the collapse DEBT MOVES TO THE FRONT OF THE FILE RATHER THAN CLEARING —
  item (9)'s mechanism, measured on a date rather than on a paragraph.** ⚠ **Only a LATER seat can fairly
  collapse today's block; this one could not, having just written part of it.**
  ⚠ **(c) STEP 2 HAS NOW BEEN HANDED ABSENT INPUT AT FOUR CONSECUTIVE MIDDAY SEATS.** `highest_close`
  carries no `(as of …)` date, so the detector neither passed nor failed. ⚠⚠ **A DETECTOR WITH NO INPUT
  RETURNS THE SAME SILENCE AS ONE FINDING EVERYTHING HEALTHY, and that silence is now four runs long.
  IT ARMS ON THE FIRST SATELLITE FILL — and on that day open item (12) fires in the same morning, since
  routine 2's Step 6 would write a partial bar's `c` into `voo_close_at_entry`.**

- **⚠⚠ GFS/TSMC CLEARED EVERY FILTER AND DIED ON THE *THESIS PARTS* — `T-2026-10-09-01`, STILL THE
  MOST INFORMATIVE REJECTION THIS LOG HAS PRODUCED.** *(Collapsed 10-12 08:36: the catch (23)/(24)
  correction saga is SETTLED AND FIXED and is kept below as its one-line lesson rather than as the
  narrative of its own repair. Nothing live discarded.)*
  GlobalFoundries' **own dated release, 2026-10-08**: GF will manufacture **silicon interposers** for
  **TSMC** (CoWoS) at **Malta, New York** — **$2B over an initial five-year term** (Reuters, Bloomberg).
  **WHAT IT CLEARED:** two named parties · an official company-issued release · a dollar figure
  attributed to the US-listed leg · no rule (iii) problem · `asset` returns us_equity/NASDAQ/tradable ·
  **and `move` passed on BOTH bases, +1.48% over five sessions (48.65 → 49.37) and +2.72% on the news
  day itself (48.065 → 49.37).**
  **IT DIED THREE TIMES OVER, AND BOTH KILLING NUMBERS CAME OUT OF GF'S OWN RELEASE IN ONE STEP EACH:**
  **PART 3 (primary, not a judgment call)** — GF's words: *"Volume production is expected to begin
  ramping … during the first half of 2028."* From Q4 2026 that is **SIX QUARTERS MINIMUM** against §4's
  **TWO-QUARTER** ceiling, and revenue recognition is later and undisclosed. **Standing rule (vi) in
  its cleanest form.** **PART 2 (independent, arithmetic)** — $2B / 5yr = **~$400M/yr** on FY2025
  revenue **$6.791B** = **5.89%**, under the 10% floor; ⚠ **and that is the MOST GENEROUS reading — GF
  assigned the deal to NO reporting segment, so the true share is not small, it is NOT CALCULABLE.**
  **PART 1 (independent, structural)** — **GFS IS THE HEADLINE NAME**, so §4's premise does not apply;
  the genuine second-order question (*who supplies the Malta expansion?*) returned a **verbatim
  denial**, and the only Company B on offer was the reflexive AMAT/LRCX/KLA prior. **NOT WRITTEN DOWN.**
  ⚠ **§3's CAP IS *UNRESOLVED*, NOT PASSED** — the funnel declined a sourced figure twice. **DO NOT
  INHERIT A §3 VERDICT FROM THIS ENTRY** (the VAL precedent). It never needed resolving.
  ⚠⚠ **IT IS THE *SECOND* CANDIDATE TO CLEAR §3's INSTRUMENT TESTS AND THE PRICED-IN FILTER AND THEN DIE
  ON §4's PARTS — AMD (`T-2026-10-01-02`) DID IT FIRST ON 10-01, with a STRONGER §3 pass and the same
  primary kill. ⚠ THE NON-SUPERLATIVE OBSERVATION IS THE USEFUL ONE: PART 3 KILLED BOTH, and part 2 was
  failing in both. "First" was not a fact; the pattern is.** **Not a new reject form — it is form seven
  ("everything disclosed, the spending lands too far out") in its strongest instance.**
  ⚠⚠ **THE LESSON TO CARRY, AND IT CUTS THE OTHER WAY FROM MOST OF THIS FILE: a clean one-sentence
  mechanism, a real transaction, a named counterparty and a stock that has not moved is the most
  buyable-looking object §4 can meet. THE RULES STOPPED IT; THE JUDGMENT DID NOT HAVE TO.**
  ⚠ **DO NOT REHABILITATE IT AT A DIFFERENT PRICE — it did not die on price, and neither the calendar
  nor the 5.89% moves with the quote. "But it has not run yet" is "but it went up" wearing a coat.**
  ⚠⚠ **THE PULL WAS FELT AND REFUSED AT BOTH SEATS THAT COULD HAVE ACTED (10-09 09:36, the only seat
  holding a live `buy` path with every §6 gate open and $30,000 idle, and 10-09 12:41) — BOTH DECLINED
  AND PULLED NO QUOTE AT ALL. Declining to LOOK is stronger than looking and resisting.**
  ⚠ **THE LESSON FROM ITS REPAIR, WHICH OUTLIVES THE ITEM — CATCH (24): a correction was published as
  "corrected in ALL THREE FILES" and there were FOUR. The defect was not a false statement about a
  file, it was **AN ENUMERATION THAT SOUNDED EXHAUSTIVE AND WAS NOT**, and the harm is that it is
  **SELF-CERTIFYING** — it reads as closure and suppresses the next re-check. ⚠ **NEVER WRITE A
  CORRECTION'S SCOPE AS A COUNT. `grep` the phrase repo-wide, then name the files the grep returned.**
  *(Fixed 10-09 12:41.)*

- **⚠⚠ TWO CLOSE RUNS HAVE VANISHED — 2026-09-28 AND 2026-10-05 — AND THIS IS THE DURABLE FORM.**
  `git log` for 10-05 holds premarket `4277aae`, open `2effdf1`, midday `d50219c` and **no close
  commit**; the newest close commit before 10-06 was **`748a3e7`, dated 2026-10-02.** **THE 10-05 AND
  09-28 JOURNAL ENTRIES ARE GONE AND UNRECOVERABLE.**
  ⚠⚠ **NO ALERT FIRED AND NONE COULD HAVE: a run that dies before `commit.py` leaves no trace by
  construction, so `alerts.md` reading "zero open incidents" is NOT evidence that every seat ran.**
  ⚠ **It cost nothing in the ledger ONLY because the sleeve is empty. LUCK, NOT DESIGN.**
  ⚠ **DO NOT RECONSTRUCT EITHER MISSING JOURNAL ENTRY from a later vantage point — that manufactures a
  record rather than recovers one. The recording is discharged; the QUESTION stays with the human as
  open item (11).**
  ⚠⚠ **2026-10-06, 10-07, 10-08 AND NOW 10-09 WERE ALL COMPLETE SESSIONS — ALL FOUR SEATS RAN AND
  COMMITTED ON EACH, THE FIRST RUN OF FOUR SINCE 10-02, AND THE 10-09 CLOSE SEAT IS THE ONE ENTITLED TO
  SAY SO ABOUT 10-09 BECAUSE IT *IS* THE SEAT THAT WOULD HAVE BEEN MISSING.** ⚠⚠ **FOUR IN A ROW IS NOT A
  FIX AND MUST NOT BE READ AS ONE: the failure mode is a run that never STARTS, so a session that
  completed is not evidence about the next one in either direction, and a RUN OF FOUR is not evidence
  either. Two of 28 close runs have vanished and THE DETECTION GAP IS UNCHANGED — there is still no
  detector for a missing seat, and `alerts.md` reading "zero open incidents" still cannot distinguish a
  healthy week from a seat that died before `commit.py`.**
- **⚠⚠ ASK THE FUNNEL FOR THE *STRUCTURE* §4 REQUIRES, NOT FOR *IMPORTANCE* — AND AS OF 10-12 THE RULE
  HAS A KNOWN FALSE-POSITIVE FORM, WHICH IS THE PART TO READ.** *(Collapsed 10-12 08:36: the 10-06,
  10-07 and 10-09 worked examples are folded to the mechanism plus their counts. Nothing live
  discarded.)*
  ⚠⚠ **THE MECHANISM: A QUERY ABOUT "SIGNIFICANCE" INVITES THE SOURCE TO EDITORIALISE, AND IT
  EDITORIALISES TOWARD THE MACRO COMPLEX — THE ONE OBJECT §4 CAN NEVER USE.** The 10-06 paired test is
  the proof: same day, same window, scan 1 ("the most significant … news events") returned **four
  macroeconomic non-events**, volunteering *"the most clearly documented events were macroeconomic"*;
  scan 2 (**"announcements involving TWO NAMED PARTIES and a disclosed dollar amount"**) returned
  **seven dated transactions, including two multi-billion-dollar acquisitions scan 1 never mentioned.**
  ⚠ **Scan 1's framing would have produced a no-trade day with an EMPTY LOG; scan 2's produced eight
  auditable rejections.** ⚠ **Routine 1's Step 5a prompt is written in scan 1's voice. USE THE
  STRUCTURAL FRAMING AS THE *FIRST* QUERY EVERY RUN.**
  **IT HAS NOW PAID FOUR CONSECUTIVE SESSIONS, AND WHAT IT PAYS IS *EXCLUSIONS WITH REASONS ATTACHED* —
  work the run would otherwise do itself, for ZERO follow-up queries:** 10-07 four qualifying against
  four self-excluded · 10-08 one against **NINE** · 10-09 one against **NINE** · **10-12 ZERO against
  EIGHT** (Fortem/MBDA no figure *and* a 2024 collaboration · Blend Labs' lender unnamed · HITT/NIST
  *"up to $600M"* · RTX unverifiable pending a primary source · Ascenty/Casa dos Ventos *"previously
  announced in January 2026"* · Bimergen a growth **strategy** · New River Valley a contract **NOT
  finalised** · IPA Capital Markets parties unidentified).
  ⚠⚠ **AND THE SECOND FRAMING IS COMPLEMENTARY, NOT REDUNDANT — ASK BOTH, EVERY RUN.** "Two parties and
  a dollar amount" finds **TRANSACTIONS**; **"who WON it and what did they say it was worth to their own
  SEGMENT"** targets the **PART 2 EVIDENCE**, the most common killer in this log. 10-07 is the proof:
  the Boeing/Lockheed PAC-3 MSE award (**$14.7B, two named US-listed parties above $10B**) appeared
  **only** under the second framing. **10-12 is the proof it still earns its place for a different
  reason: it stated the part-2 gap outright** — RTX *"does not report RTX's own quantified revenue
  impact for the Raytheon segment"* — **the source applying the kill before I did.**
  ⚠⚠ **NEW 10-12 AND IT IS THE LIMIT OF THE WHOLE RULE: THE STRUCTURAL FRAMING SCREENS FOR *STRUCTURE*,
  NOT FOR *PARTY TYPE* OR *UNIT*, AND `T-2026-10-12-01` IS THE FALSE POSITIVE.** The 10-09 US/Russia
  diesel arrangement carries **two named parties, a precise announcement date, a dated delivery schedule,
  a named regulatory instrument with an expiry (the OFAC licence to 2027-04-07) and a four-rung quantity
  ladder (300k / 500k / 1M / 3M tons)** — **the entire shape the framing exists to find** — ⚠⚠ **AND IT
  IS UNTRADEABLE, BECAUSE THE TWO NAMED PARTIES ARE *SOVEREIGN STATES* AND THE DISCLOSED QUANTITY IS
  *NOT MONEY*.** ⚠ **THE FIX IS ADDITIVE AND CHEAP: the structure must ALSO satisfy PARTY TYPE (both
  parties companies) and UNIT (dollars, at Company B). "IT RETURNED THE SHAPE" IS NO LONGER SUFFICIENT
  GROUNDS TO PROCEED TO A MECHANISM.** ⚠ **This does not weaken the framing — it is still the query that
  reaches the funnel's actual inventory, and on the same run it disposed eight items for free.**
  ⚠⚠ **AND ASK FOR THE ANNOUNCEMENT DATE ON EVERY RUN, NOT JUST ON MONDAYS. A recency filter bounds when
  something was WRITTEN, never when it HAPPENED.** 10-05 is the worked failure (an onsemi/Synaptics
  revision presented as fresh weekend news was a four-day-old 8-K, caught only because a second query
  asked); 10-06 is the worked success (September payrolls returned with *"announced October 2, 2026, not
  October 5"* volunteered in its own first clause — the rule (iii) trap defused by framing rather than by
  a follow-up query). **The cost of asking in the first query is one sentence.**
  ⚠⚠ **AND READ THE LOG BEFORE THE TAPE — THE FUNNEL RE-SERVES THIS LOG'S OWN DISPOSED REJECTS, TWO
  SESSIONS RUNNING, THREE EACH TIME.** 10-09: MTUS $995M (eight sessions old, same ticker, programme and
  figure) · Voyager $22.4M (**re-stamped with a fresh 10-09 date**) · Elevra/LG. **10-12: RTX's SM-3
  *"up to $6.3B"* TWICE IN ONE RUN by two differently-framed queries · Samsung Electro-Mechanics ₩290B
  verbatim · KEC with a fresh ₹1,030 crore figure.** ⚠⚠ **AND THE 10-12 INSTANCE CARRIES THE WARNING THE
  10-09 ONE DID NOT: QUERY 2 CALLED THE DISPOSED RTX AWARD *"THE CLOSEST APPARENT MATCH"* OF THE WHOLE
  RUN. A DISPOSED REJECT CAN ARRIVE DRESSED AS A RUN'S BEST CANDIDATE, AND THE ONLY THING THAT STOPPED
  IT BEING RE-ELABORATED FROM SCRATCH WAS READING THE LOG FIRST.** ⚠ **Reading the log cost one grep and
  saved three drills.**

- **⚠⚠ NEW 10-12 — THE FORWARD CALENDAR IS A NON-EVENT SHAPE SPECIFIC TO THE MONDAY PRE-MARKET SEAT,
  WHICH IS WHY IT HAS NOT BEEN SEEN BEFORE.** `T-2026-10-12-05`. A weekend window contains no trading
  and little corporate disclosure, **so the funnel fills the space with the WEEK AHEAD** — on 10-12 the
  third broad scan's largest single block was JPM/C/WFC reporting **10-13**, September CPI **10-14**
  (consensus cited at +0.6% m/m, +3.7% y/y headline, +0.2% m/m core), PPI and retail sales **10-15**.
  ⚠⚠ **IT IS THE MOST DANGEROUS EMPTY OBJECT THIS FUNNEL PRODUCES, BECAUSE IT ARRIVES CARRYING
  EVERYTHING §4 ASKS FOR EXCEPT THE EVENT: named US-listed companies above $10B, precise dates, and even
  CONSENSUS NUMBERS a fast reader can mistake for DISCLOSED ones.** ⚠ **The source named the exclusion
  itself: *"Scheduled earnings events, not reported earnings surprises."***
  ⚠⚠ **IT IS ALSO THE PUREST FORM OF RULE (iii): THE EARLIEST POSSIBLE FAILURE OF "IS THIS NEW TO THE
  COMPANY'S OWN DISCLOSURE?" IS AN EVENT NOBODY HAS DISCLOSED BECAUSE IT HAS NOT HAPPENED.** ⚠ **The
  correct response is to note the dates and do nothing — an earnings print on 10-13 is for the 10-13
  seat to meet, and §4 would kill the read-across anyway as the competitor's-earnings-print shared-cause
  object.** ⚠ **Expect this shape on EVERY Monday pre-market seat.**

- **✅⚠⚠ THE DIVIDEND TEST IS **RESOLVED AND CLOSED** — BRANCH (a): **THE ALPACA PAPER ACCOUNT DOES
  NOT MODEL DIVIDENDS.** *(Resolved 2026-10-08 08:25. This REPLACES the three-branch decision rule and
  the 30-reading counter; neither is live any more.)*
  **Both inputs read in the same breath, as the pre-written rule required: `account.balance_asof`
  **`2026-10-07`** — the field has ADVANCED past the pay date — and `cash` **exactly $30,000.00** from
  `account` and `sleeves` with `accrued_fees: 0`.** The inferred **~$30,180.76** credit
  ($1.825/share × 99.046311231) **never arrived.**
  ⚠ **DO NOT RE-READ `cash` FOR THIS PURPOSE AND DO NOT RESTART THE COUNTER. The test is spent.**
  ⚠ **Worth preserving as process, not as trivia: a falsifiable claim written in advance, moved
  exactly ONCE (off an API field, not for convenience), held across three sessions and five seats, and
  then resolved against itself. The result is NEGATIVE, which is what most correct tests return.**
  ⚠⚠ **WHAT REMAINS LIVE IS THE CONSEQUENCE, AND IT IS THE HUMAN'S DECISION, NOT ANY SEAT'S:
  dividends are worth **1.3254pp/yr** on VOO (TTM +16.3118% `--adjustment all` vs +14.9863% `raw`), so
  a 70% core that never collects them under-earns **~0.93pp/yr**, which on top of the **4.89pp** cash
  drag is a **~5.82pp ANNUAL HANDICAP BEFORE ANY DECISION** — against a §1 objective of beating the
  S&P 500 **TOTAL** return. ⚠ **§1 as written is unmeetable by construction on this platform.**
  **Three options, written out in full in `plan_today.md` (2026-10-08): (i) benchmark against VOO
  PRICE return and say so; (ii) accrue a notional dividend in `state.md` for benchmarking only,
  touching no order path; (iii) leave it and treat the handicap as a known, quantified bias in every
  performance line. Option (ii) needs a `strategy.md` or routine change — ONLY THE HUMAN MAY MAKE IT.**

- **⚠⚠ NEW 10-08, THE EIGHTH REJECT FORM AND THE FIRST THAT IS NOT A DISCLOSURE OR CALENDAR FAILURE:
  THE MECHANISM IS SOUND AND POINTS DOWNWARD.** **SUPN** (`T-2026-10-08-02`): Newron's 10-08 release
  **names Supernus as the holder of US marketing rights to evenamide**, and the FDA clinical hold on
  ENIGMA-TRS 2 genuinely impairs that asset. ⚠ **That read is UNTRADEABLE HERE — §3 forbids leverage,
  inverse products and anything not bought outright with settled cash, so this strategy can only
  express the LONG side.** ⚠⚠ **THE TEMPTING MOVE IS TO FLIP IT INTO A "COMPETITOR BENEFITS" LONG.
  THAT IS THE SHARED-CAUSE OBJECT: no competitor's revenue or cost line changed, only its relative
  standing, and NO COMPETITOR WAS NAMED IN ANY SOURCE. NOT TAKEN, AND IT WILL BE OFFERED AGAIN.**
  ⚠ **The seven known forms are all about what the source WITHHELD or WHEN the money lands. This one
  is about what §3 PERMITS, so widening the evidence bar would not touch it.** *(SUPN also failed §3's
  cap floor at ~$2.5B and part 2 for want of any disclosed figure — three independent kills.)*

- **⚠⚠ NEW 10-08 — A "COMPLETE" BAR IS NOT A "FINAL" BAR, AND THIS IS THE OTHER END OF THE RETIRED
  n/v TEST.** The **2026-10-07** bar read **n 1323 / v 23415** at the 16:17 close seat and **n 1325 /
  v 23423** at the 10-08 08:25 seat — **+2 trades, +8 shares, same date, same basis, 16 hours apart.**
  ⚠ **`o`/`h`/`l`/`c` and `vw` were UNCHANGED, so nothing any §5 rule reads actually moved.**
  ⚠⚠ **BUT: a staleness detector that diffs `n`/`v` across seats WILL see motion that is late-print
  settlement rather than a live session.** ⚠ **The n/v completeness FLOOR test was retired on 10-07 for
  false-positiving a quiet full session; this is the same two fields failing in the OPPOSITE direction
  inside a day. THE CLOCK REMAINS THE ONLY WORKING MARKET-STATE DISCRIMINATOR.**

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

- **⚠⚠ THE SATELLITE SLEEVE IS STRUCTURALLY UNDEPLOYED — **28 COMPLETED SESSIONS** (25 post-fill),
  **143 THESES**, ZERO POSITIONS EVER, AND THE PRESSURE TO LOWER THE §4 BAR IS THE ONLY ITEM HERE ASKING
  FOR JUDGMENT RATHER THAN CARE.** *(Collapsed 10-09 16:17: six retellings of the same counter trap folded
  to the rule. Nothing live discarded.)*
  ⚠⚠ **THE 10-12 08:36 PRE-MARKET SEAT ADVANCED THE THESIS COUNT 138 → 143 AND *HELD* THE SESSION COUNT
  AT 28 / 25 — catch (21)'s shape for the EIGHTH time, resolved the same way and in the OPPOSITE
  direction to 10-09's: here the THESIS unit passed (this seat wrote today's five) and the SESSION unit
  did not (it stands BEFORE the bell on 10-12, and 10-09 was already counted by its own close seat).
  DO NOT "FIX" 28 TO 29.** ⚠ **The 10-09 16:17 close seat is the mirror instance: it advanced 27 → 28
  and HELD the thesis count, because the 08:27 seat had already written that day's eight.**
  ⚠ **THE RULE, SO THE NEXT SEVEN SEATS NEED NOT RE-DERIVE IT: THE UNIT IS A *COMPLETED* SESSION.
  Routines 1 and 2 may never count the day they stand in; routine 3 may NEVER advance it at all; routine
  4 always may. CHECK A COUNTER AGAINST THE ROUTE THAT PRODUCED IT, NOT AGAINST TODAY'S REALITY — catch
  (22) is the worked failure, where a seat stated the rule correctly and then wrote the advanced number
  forty-four lines later in another file.**
  ⚠ **THE SESSION COUNT IS INHERITED-AND-INCREMENTED, NOT RE-DERIVED, AND IT *CANNOT* BE RE-DERIVED FROM
  `journal.md`: the 09-28 and 10-05 entries are missing, so the journal under-counts sessions by exactly
  the two close runs that vanished.** ⚠ **The THESIS count CAN be re-derived from source and was, by the
  10-09 08:27 seat: `archive/research_log/2026-09.md` **87** + live October **43** (6 on 10-01 · 5 on
  10-02 · 7 on 10-05 · 8 on 10-06 · 7 on 10-07 · 10 on 10-08, counted by date) = **130**, + **8** on
  10-09 = **138**, + **5** on 10-12 = **143**. ⚠ **The 10-12 leg is INHERITED-AND-INCREMENTED, not
  re-derived from headings; the next Friday review should rebuild it from source as 10-09's did.**
  ⚠⚠ **AND THE ONE THING 10-09 CHANGES ABOUT THE ARGUMENT, WHICH CUTS *AGAINST* LOWERING THE BAR: for the
  first time a candidate (GFS) reached §4's PARTS with every filter behind it, and the PARTS killed it on
  two numbers out of the company's own release. THE BAR WAS LOAD-BEARING FOR THE FIRST TIME, AND IT HELD.
  142 of the 143 never got that far.**
  ⚠⚠ **AND THE ONE THING 10-12 ADDS, WHICH CUTS *NEITHER* WAY AND IS WORTH SAYING FOR THAT REASON: NOT
  ONE OF ITS FIVE GOT NEAR THE BAR, SO THE DAY IS EVIDENCE ABOUT THE *WINDOW* AND NOT ABOUT THE BAR.**
  A weekend plus a Monday pre-market is the thinnest window this routine ever screens — the funnel's
  entire US corporate inventory for it was **one sovereign supply announcement, one disposed repeat, a
  forward calendar and two macro aggregates.** ⚠ **A no-trade Monday is the EXPECTED shape of a Monday.
  Do not read it as the bar biting, and do not read it as the bar failing.**
  Set beside: empty sleeve, **29.74% idle cash**, weekly cap **0 of 3**, breaker INACTIVE, every gate
  open. **§2 permits the cash and §4 says most runs end in no trade — both rules were followed.**
  ⚠ **ONE SIDE OF THE ARGUMENT IS GONE: the book is NOT down, so "we are losing, deploy something" is
  unavailable — and it was never a §4 argument.** ⚠ **The symmetric half is the stronger one: the sleeve
  has no effect in EITHER direction (see the §1 benchmark item — five sessions from source, satellite
  contributing exactly 0.000000% on every one), and a run citing only the flattering half is quoting the
  flattering half.**
  ⚠⚠ **THE BINDING CONSTRAINT IS NOT THE EVIDENCE BAR — IT IS DISCLOSURE PRACTICE. SEVEN KNOWN FORMS PLUS
  THREE SUB-SHAPES:** the source withholds the counterparty's number · the counterparty discloses
  **roadmap not segment revenue** · the beneficiary is **vertically integrated** (IOVA; EW; GEHC's own
  cyclotrons) · **both parties refuse to disclose commercially** (GM) · **the figure is disclosed and is
  the WRONG QUANTITY** (JBL $1.7B; MS's $2.45B term loan; CHRW's $300M run-rate synergy; GEHC's $945M paid
  OUT) · **THERE IS NO COUNTERPARTY AT ALL** (Bayer's Ohio plant; BDX's $3B) · **EVERYTHING IS DISCLOSED
  AND THE SPENDING LANDS TOO FAR OUT** (Bayer's 2031/2034 holds the record; **GFS's H1 2028 is the
  strongest instance**).
  ⚠ **Sub-shapes: capacity ALREADY BUILT (ORCL/Tencent); NAMED BUT REDACTED ("Party A"); and **COMPANY A
  IS TOO SMALL FOR ANY ELIGIBLE COMPANY B TO CLEAR PART 2** (Blaize, FY revenue $32–36M; the "Genesis
  Mission" $218M-each aggregate) — part 2's 10% test and §3's $10B floor are then JOINTLY UNSATISFIABLE,
  so the supplier search is pointless before it starts. **A free one-step screen.**
  ⚠ **Only the first two forms are reachable by widening the bar; form five would be made WORSE by it;
  forms six and seven are untouched because the constraint is the CALENDAR or the absence of a second
  party.** **ABBV and ELMT are the standing proofs.** ⚠ **If the bar is to move, that is a `strategy.md`
  change and ONLY THE HUMAN may make it.**

- **⚠⚠ MERGER ARBITRAGE IS NOT IN §4, AND THE FUNNEL NOW OFFERS IT EVERY OTHER SESSION — THREE DEALS
  IN TWO SESSIONS.** onsemi/Synaptics $5.7B (10-05) · **Schneider Electric/PTC $22.6B at $205/share
  cash, close Q3 2027** (10-06) · **C.H. Robinson/RXO $5.8B cash-and-stock, close H1 2027** (10-06).
  ⚠⚠ **THE ANSWER IS ALREADY WRITTEN AND NEEDS NO FUNNEL QUERY: §4 ASKS WHOSE *ECONOMICS* CHANGE, AND
  A TARGET WHOSE PRICE IS CONTRACTUALLY PINNED HAS NO ECONOMICS LEFT TO CHANGE. The acquirer is
  first-order too.** ⚠ **AND PART 3 KILLS THE MERGER-CONTINGENT VERSION INDEPENDENTLY: both 10-06
  closings are ~4 quarters out against a two-quarter ceiling.** ⚠ **The competitor read-across
  (Autodesk/Dassault; Landstar/XPO/GXO) is the "shared cause is not a mechanism" object — and on 10-06
  the SOURCE stated that exclusion before I applied it.**

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD — **TEN** CONSECUTIVE
  SESSIONS, 09-29 THROUGH 10-12 UNBROKEN, AND 10-12 IS THE **THIRD** IN WHICH **EVERY** BROAD SCAN
  PRODUCED ONE.** *(Collapsed 10-12 08:36: four sessions of verbatim denial quotes are folded to the
  mechanism, the count, and ONE worked example per shape. Nothing live discarded — the finding was never
  any single quote.)*
  ⚠⚠ **THE FINDING IS THE PATTERN, NOT THE INSTANCE, AND IT HAS ONE MECHANISM: THE TIER BELOW A NAMED
  PARTY IS COMMERCIALLY CONFIDENTIAL, SO THE SOURCE *VOLUNTEERS THE ABSENCE* WHEN ASKED FOR A SECOND
  COMPANY.** A volunteered absence is stronger than a silence.
  **ONE WORKED EXAMPLE PER FRAMING, IN THE SOURCE'S OWN WORDS:** the won-a-contract/quantified-to-its-
  own-segment framing → *"No company identified in the available evidence meets the full screen"*
  (10-09) and *"No company can be confirmed to meet the full screen from the information gathered"*
  (10-12) · the named-second-company framing → *"no qualifying case can be verified … there is no
  verified qualifying announcement to report"* (10-09) · a **drill** on a live candidate → GF's own
  release *"does not name any specific publicly traded equipment supplier, construction contractor,
  engineering firm, or materials vendor"* and *"no dollar amount is attributed to one"* (10-09) · and
  **10-12's drill, the most complete denial on record**: *"no specific publicly traded U.S. company is
  named"* … *"it does not identify a commercial buyer, U.S. importer of record, vessel operator,
  refinery, distributor, storage-terminal operator, or other corporate counterparty"* … **"No dollar
  amount is attributed to any named U.S.-listed company."**
  ⚠⚠ **THE PRIORS ARE ALWAYS READY, ALWAYS SPECIFIC, AND ARRIVE *AGAINST* THE DENIAL — AND NOT ONE HAS
  EVER BEEN WRITTEN DOWN AS A CANDIDATE.** AMAT/LRCX/KLA for any fab headline (**10-09's is the most
  reflexive in this whole file: it arrived against an EXPLICIT denial, on the one session where a
  buyable, un-priced-in Company A was actually on the table**) · the GPU vendor for any AI-compute
  headline · the solid-rocket-motor tier for any missile award · BWXT/Curtiss-Wright/Fluor for nuclear
  uprates · Williams/ONEOK/Targa for Bakken midstream · Albemarle/Livent/Piedmont for cathode inputs ·
  Lantheus for radiopharma · the subsea-flexibles tier for FTI/Petrobras · **and 10-12's two: the
  refiner complex (VLO/MPC/PSX) and the fuel-cost tier (DAL/UAL/UPS/FDX).**
  ⚠⚠ **10-12's SECOND SET IS THE MOST SEDUCTIVE PRIOR THIS ITEM HAS EVER RECORDED, AND THE REASON IS
  WORTH KEEPING: A COST-LINE IMPROVEMENT IS A FORM §4 PART 1 *EXPLICITLY PERMITS*, so the prior arrives
  already wearing the rule's own clothes.** It fails on three independent grounds anyway: **airlines burn
  JET FUEL, not diesel**, so the causal path needs a product-substitution clause — the *"and also"* kill;
  **a commodity price is a MARKET VARIABLE**, the shared-cause object in its purest form; and **a
  presidential statement with no executed commercial contract is not a transaction to be second to.**
  ⚠⚠ **A RUN THAT PRODUCES A COMPANY B HERE HAS SUPPLIED IT FROM ITS OWN PRIORS — VERBATIM THE FAILURE
  §4's HONEST-BROKER PARAGRAPH DESCRIBES. EACH PRIOR IS A FACT ABOUT AN INDUSTRY, NOT ABOUT A
  TRANSACTION.** ⚠ **REPORTED WITH ITS COUNT AND NOT PROMOTED — the three-consecutive-reviews rule
  governs promotion.**

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES, A STANDING FOURTH STATE, AND A FIFTH ADDED
  10-09.** *(Collapsed 10-12 08:36: the per-session zero-`move` accounting — which sessions were
  countable at which seat, restated five times — is folded to the rule and the count. Nothing live
  discarded.)*
  **Shape one — a DRAWDOWN misread as priced-in** (nine instances, newest CNC −6.44% → `true`; three
  near-misses cleared only because the *fall* was fractionally too small: LMT −3.61%, GM −3.95%, LH
  −3.83%). ⚠⚠ **LITE IS THE BILL: rejected on a −7.35% drawdown, it is +29.34pp vs VOO.**
  **Shape two — the filter working by REJECTING**, on genuine news rises (SHOP +9.61%, ILMN +11.54%,
  GRAL +44.67%). **Shape three — a genuine RISE UNRELATED TO THE NEWS swept up by the window** (JBL
  +4.97% on a grind whose news day moved it +0.63%). ⚠ **The defect is SIGN- and CAUSATION-BLINDNESS,
  not the threshold.** ⚠ **AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read
  `priced_in: false` at +3.19%** while its closes ran 104.53 → 117.435 (+12.35% in one session) →
  110.44 (−6.74%) — a multi-session round trip netting to a passing figure. **HPE is a milder instance.**
  **Shape five, NEW 10-09 — THE FILTER WORKING BY *ACCEPTING*, WHICH THE LIST WAS MISSING.** **GFS**
  reached it carrying a real mechanism and a real disclosed figure — **not decorative** — and passed on
  **BOTH bases: +1.48% over five sessions and +2.72% on the news day itself.** ⚠⚠ **EVERY PRIOR "FILTER
  WORKING" INSTANCE WAS IT WORKING BY *REJECTING*. THIS IS THE FIRST RECORDED INSTANCE OF A GENUINE
  NEWS-DAY MOVE BEING CORRECTLY LET THROUGH — and the trade then died on §4's PARTS, which is exactly
  why the filters run BEFORE the parts rather than instead of them.** ⚠ **STATED WITH ITS LIMIT, WHICH
  IS REAL: 10-08 traded to 51.42 (+6.98% over the prior close) and closed −3.99% off that high. A
  close-to-close filter cannot see that excursion; had the close held near the high, the same news would
  have FAILED. A PASSING INSTANCE, NOT A CALIBRATION.**
  ⚠⚠ **THE FOURTH STATE — THE FILTER HAVING NOTHING TO FIRE ON — IS AS COMMON AS THE OTHERS: SIX
  COMPLETE SESSIONS OF IT WITH ZERO `move` CALLS IN EVERY SEAT (09-29, 10-02, 10-05, 10-06, 10-07,
  10-08), BROKEN BY 10-09's SINGLE LEGITIMATE CALL ON GFS.** ⚠ **10-08's zero has the cleanest cause
  recorded: NINE OF TEN CANDIDATES DIED AT §3 OR PART 1, UPSTREAM OF THE FILTER. 10-12's pre-market zero
  has a cleaner one still: FOUR OF FIVE REJECTS CARRY NO TICKER AT ALL** (two macro aggregates, a
  forward calendar and a Company-B-less sovereign arrangement), **the fifth is a disposed repeat on a
  first-order name, and a thirteen-item sweep died at §3.**
  ⚠⚠ **THE COUNTING RULE, SO IT NEED NOT BE RE-DERIVED AT EVERY SEAT: THE HONEST UNIT IS THE SESSION
  AND A SESSION IS ONLY COUNTABLE ONCE IT IS OVER.** A seat standing mid-session may say only "not yet
  countable — N seats remain"; writing the completed count early is catch (11)'s shape, and it has been
  declined at 10-06 08:22/09:36, 10-08 08:25/12:41 and 10-12 08:36 for exactly that reason.
  ⚠ **AN ABSENT CHECK AND A SKIPPED ONE LOOK IDENTICAL IN A RUN SUMMARY, so a run reporting
  "priced-in: pass" MUST SAY WHICH STATE IT MEANS.** ⚠⚠ **A DECORATIVE `move` CALL ON A NAME WITH NO
  MECHANISM CONVERTS AN HONEST ABSENCE INTO A FAKE EXERCISE, AND HAS NOW BEEN DECLINED FOR THAT REASON
  THREE TIMES** — SYNA at +14.1% (10-05) and CEREBRAS at +9.1% (10-06) would **both** have FAILED the
  filter had they reached it (shape two) and neither got there; 10-12 declined it with no eligible
  ticker to call it on at all. ⚠ **The EXERCISED-AND-NON-DECISIVE state also stands (09-30 ABBV/RARE;
  10-01 AMD/HPE/MU).** **Only a human may change §4 or `alpaca.py move`.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY. A REJECTION IS NOT A QUEUE.**
  *(Collapsed 10-12 08:36: 10-05 through 10-09's per-day narratives are folded to ONE LINE PER DAY
  carrying only the durable kill. The full entries live in `research_log.md`, which is where a run
  checking whether a name was disposed should look. Nothing live discarded.)*
  ⚠⚠ **THE DISPOSED-REJECT CATALOGUE IS SPLIT: `archive/research_log/2026-09.md` holds 87 theses; the
  live `research_log.md` holds the October entries. A RUN CHECKING WHETHER A NAME WAS ALREADY DISPOSED
  MUST READ BOTH.**
  **10-12's FIVE, and FOUR OF THEM CARRY NO TICKER:** **US/Russia diesel** (part 1 — **no Company B by
  explicit source denial**; tonnages are not dollars; the two named parties are **STATES** — the
  structural framing's false positive, see that item) · **RTX** SM-3 *"up to $6.3B"* (**exact repeat of
  10-09, re-served TWICE in one run**; first-order; a ceiling; govt counterparty; rule (iv), **4th
  appearance in seven sessions**) · a **§3 / non-qualifying sweep of THIRTEEN items** disposed as one
  (Samsung Electro-Mechanics ₩290B **and** KEC — both repeats · SEPC · MHI · Tialis · Thruvision ·
  Acuity RM · MBDA · Fortem · HITT · Bimergen · Ascenty · New River Valley) · the **macro/fiscal
  complex** (no Company A) · the **FORWARD CALENDAR** (nothing has happened yet — see its own item).
  **10-09's EIGHT:** **GFS**/TSMC $2B (part 3 H1 2028 · part 2 5.89% · part 1 headline name — see its
  own item) · **RTX** SM-3 (settled defence pattern) · **RIG** (§3 cap ~$6.19B; ⚠ **one release carried
  a $62M NEW leg and a $1.0B PREVIOUSLY ANNOUNCED one, ~16:1 in favour of the STALE figure — the most
  legible rule (iii) instance on record, and a reader skimming for the largest number takes the one that
  fails**) · **MTUS** $995M (exact repeat of 10-01) · Voyager $22.4M (exact repeat of 10-06, re-stamped
  with a fresh date) · "Genesis Mission" $2.4B/11 companies (govt action; ~$218M each, so **part 2's 10%
  test and §3's $10B floor are JOINTLY UNSATISFIABLE — a free one-step screen**) · **FTI**/Petrobras
  (part 2 — *"significant"* is a self-defined **$75–250M BAND**, not a figure) · a **§3 sweep of eleven**.
  **10-08's TEN:** Asieris/Theramex (§3 — **neither party US-listed**, and it was the day's best-disclosed
  figure) · **SUPN** (§3 cap ~$2.5B · part 2 · **mechanism points DOWN** — see the eighth-form item) ·
  **OII** (§3 · announced 10-02, rule (iii)) · **GVA** (§3 · no segment quantification) · X-Bow
  (private) · **VAL** (form five, aggregate unallocated; **§3 UNRESOLVED — do not inherit a verdict**) ·
  US Army NGC2 ~$100M/nine companies (**jointly unsatisfiable, free screen**) · **ARGX** (part 1) ·
  Pfizer Sicily (**no counterparty at all**; ⚠ **a HEADCOUNT is not a dollar path**) · a **§3 sweep of
  twelve non-US items** (⚠ **Alstom/Riyadh was a QUALIFYING two-party disclosed-value contract excluded
  purely on US scope, and the source excluded it before I did**).
  **10-07's SEVEN:** Google/CEG $4.3B (part 1 volunteered absence; part 3 — first capacity 2028) ·
  **Lockheed→Boeing PAC-3 MSE $14.7B** (part 1 below Boeing; **undefinitized action pricing an April
  2026 framework — a NEW rule (iii) costume**) · Chevron/Hess Midstream $200M (**paid OUT by the buyable
  leg**, rule viii) · POSCO/Samsung SDI KRW 6T (§3; an **amendment** to a 2023 agreement) ·
  Clarivate/Altaris + HD Construction/ERock + Emera + Alvotech (**four items, ZERO queries spent**) ·
  Fortuna + Avio + Lamb Weston · **BWXT** $189M (**no Company A — an unnamed government counterparty**).
  **10-06's EIGHT:** Schneider/PTC + CHRW/RXO (merger arb, part 1 volunteered absence) · **BDX $19B/$3B**
  (part 1 + part 3 — unnamed contractors) · **GEHC/Sofie $945M** (part 2 — capital paid OUT, target
  PRIVATE, GEHC vertically integrated) · Blaize/NeoTensr (**jointly unsatisfiable on a $32–36M company**)
  · S&K PROS 7 + Powerus + Voyager (§3) · the macro complex · OpenAI/Cerebras (no transaction).
  **10-05's SEVEN:** onsemi/Synaptics + "Party A" + MS · Bayer $2.2B Ohio (**2031/2034, the record
  holder for form seven**) · EW AUTUS valve · BMY Camzyos paediatric · TSMC capex (an earnings PREVIEW)
  · September payrolls · **the G7 diesel release** — ⚠ **now the FIRST of two diesel items, see rule (iv)
  at the event-type level.**
  ⚠ **`--recency day` returns a GLOBAL tape — roughly half of each run's raw funnel output is non-US.
  That is not a defect in the query; it is why §3 is applied before a mechanism is attempted.**
  ⚠ **DO NOT REHABILITATE ANY EARLIER REJECT AT A DIFFERENT PRICE.** ⚠⚠ **ELMT IS THE LIVE TEST: it is
  +11.86pp vs VOO and is STILL ineligible — §3 is a hard filter that does not weigh outcomes, and "but
  it went up" is a higher price, not new evidence. DO NOT SCREEN IT AGAIN.**
  ⚠ **One §3 question is reached-but-undecided: Shopify is a Canadian issuer trading as common stock on
  a US exchange. A future run reaching this with a LIVE candidate must put it to the human.**

- **⚠⚠ US DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE — TWELVE INSTANCES, AND 10-07 STILL
  HOLDS THE ONE THAT TESTED THE RULE PROPERLY.**
  ⚠ **COUNTED, NOT INHERITED: the header read SEVEN, 10-08 numbered X-Bow the 8th and US Army NGC2 the
  9th, 10-09 added RTX's SM-3 (10th) and BAE/USMC $230.1M (11th), and 10-12 adds HITT/NIST *"up to
  $600M"* (12th — a PRIVATE prime against an unnamed government body, so it fails on §3 and rule (v)
  at once). TWELVE.**
  ⚠⚠ **AND 10-12 RE-SERVED THE TENTH, TWICE IN ONE RUN BY TWO DIFFERENTLY-FRAMED QUERIES, MAKING RTX's
  FOURTH APPEARANCE IN SEVEN SESSIONS AND ITS *SECOND ON THIS IDENTICAL AWARD*. ⚠ A ticker re-arriving
  on the SAME award with the SAME figure is the strongest form of rule (iv)'s warning, because nothing
  about it has changed at all — and query 2 called it *"the closest apparent match"* of the whole run.
  ZERO QUERIES SPENT; the answer was already written down, which is what the catalogue is for.**
  ⚠⚠ **THE TENTH IS THE PUREST RULE (iv) INSTANCE IN THE LOG: RTX's SM-3 Block IB
  *"up to $6.3B"*, which makes RTX's THIRD appearance in six sessions (09-29 AMRAAM $20.7B · 10-02 SM-6
  *"up to"* $24.4B · 10-09 SM-3 *"up to"* $6.3B) — AND IT DIED THE SAME DEATH ALL THREE TIMES.**
  ⚠ **A recurring ticker is a WARNING, not corroboration: RTX arriving every third session is telling me
  about the defence sector's DISCLOSURE PRACTICE, not about a candidate maturing.** ⚠ **ZERO queries
  spent on it — the answer was already written down, which is what the catalogue is for. AND THE FUNNEL
  RE-SERVED THE 10-02 SM-6 AWARD ALONGSIDE THE NEW ONE, so the log must be read BEFORE the tape.** 09-29 AMRAAM $20.7B (RTX) · 09-30 F/A-XX >$20B (Boeing) · 10-02
  SM-6 $24.4B (RTX, a MAXIMUM POTENTIAL value) · **10-06 S&K Aerospace PROS 7 $4.3B (an unlisted
  prime), Powerus $82M and Voyager $22.4M (both microcaps)** · **10-07 BWXT $189M naval reactor fuel
  (counterparty a government body the source did not even name)**.
  ⚠⚠ **AND 10-07's PAC-3 MSE AWARD IS THE INSTANCE THAT MATTERS, BECAUSE IT IS THE FIRST WHERE THE
  NAMED RECIPIENT IS A BUYABLE SUB-PRIME RATHER THAN THE PRIME: Lockheed Martin awarded **Boeing**
  $14.7B for PAC-3 MSE seekers — the tier below the prime IS named, IS US-listed and IS above $10B.
  THE PATTERN HELD ANYWAY, because the question simply moves one level further down and the same
  commercial confidentiality applies: no supplier below Boeing is named.** ⚠⚠ **THAT STRENGTHENS THE
  RULE RATHER THAN WEAKENING IT — the mechanism is DISCLOSURE PRACTICE, not the primes' size. NAMING
  THE SUB-PRIME DOES NOT CREATE A SECOND-ORDER CANDIDATE; IT CREATES A NEW FIRST-ORDER NAME.**
  ⚠⚠ **THE MECHANISM IS DISCLOSURE PRACTICE, NOT LUCK: a prime announces the award and the tier below
  it is commercially confidential.** ⚠ **Spend ONE funnel query, then WRITE THE ANSWER DOWN AND STOP.
  NO RE-QUERY HAS EVER BEEN ISSUED; 09-30, 10-01, 10-02, 10-05 and 10-06 all acted on this as
  written.** ⚠ **The prime is FIRST-ORDER and outside §4 at any price.** ⚠ **Powerus adds a rule (iii)
  costume: a "second order under an existing contract" is a DELIVERY MILESTONE RECYCLED AS NEWS.**

- **⚠⚠ THE BROKER/OFFICIAL PRICE GAP IS A MOVING LIVE MIDPOINT, NOT AN OFFSET — AND 10-06 PROVED THE
  SAME IS TRUE OF THE PRE-MARKET SERIES.** Post-bell: at 16:16 on 10-02 `current_price` 707.82 sat
  **+$0.470** above the official 707.35; at 16:46 it read **707.3246**, **−$0.0254** below it — same
  day, same official close, thirty minutes apart, a sign change. ⚠⚠ **A FOURTH POST-BELL SAMPLE, 10-08 16:16, AND IT IS THE LARGEST MAGNITUDE YET:
  `current_price` **711.80** against the official **711.23** — **+$0.57**, more than twenty times the
  smallest sample and the THIRD of four to carry a POSITIVE sign. FOUR SAMPLES, BOTH SIGNS, A
  TWENTY-TWO-FOLD SPREAD — no offset survives and no direction is readable.**
  ⚠⚠ **A THIRD POST-BELL SAMPLE, 10-06
  16:17: `current_price` **716.4107** against the official **716.29**, **+$0.1207** — a THIRD value and
  the SECOND sign, an order of magnitude apart from the first. THREE SAMPLES, NO OFFSET, AND THE SERIES
  IS NOW LARGE ENOUGH THAT "IT IS ROUGHLY X" IS UNAVAILABLE IN EITHER DIRECTION.**
  ⚠⚠ **PRE-MARKET, NOW THREE SAMPLES, AND THEY FINISH OFF THE IDEA OF A PRE-MARKET OFFSET: 10-05 08:28
  read 707.13 against the official 707.35 (**−$0.22**); 10-06 08:23 read 715.25 against the official
  712.41 (**+$2.84**); 10-07 08:24 read **713.2413** against the official **716.29** (**−$3.0487**).
  BOTH SIGNS, A FOURTEEN-FOLD SPREAD IN MAGNITUDE, AND THE SERIES IS NOW AS LARGE AS THE POST-BELL ONE.**
  ⚠ **No fixed-offset reading survives on either series, and "it is roughly X" is unavailable in either
  direction on both.**
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
  ⚠⚠ **BUT DO KEEP `lastday_price` OUT OF THE MOVING-MIDPOINT CLAIM — 10-08 SEPARATED THEM AND THE 08:25
  SEAT HAD WRITTEN THEM AS ONE THING.** `lastday_price` read **714.34 at ALL FOUR SEATS of 10-08 — 08:25, 09:37, 12:41 and 16:16**,
  byte-identical **end to end across a complete session**, against an official 10-07 close of **714.66** (−$0.32) — so within a
  session it behaves as a **FIXED PRIOR-DAY FIELD**, while `current_price` moved 716.29 → **712.28** over
  the same span. ⚠ **The moving midpoint is a property of the LIVE mark ONLY. The gap's SIZE is still
  unpredictable run to run (−$0.32 on 10-08, −$0.09 on 10-06) and it still must NEVER be differenced
  against an official close — this narrows WHICH series moves, it does not license using either.**
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
  ⚠⚠ **A FIFTH INSTANCE ARRIVED FREE ON 10-07 AND IT IS THE CLEANEST OF THE DRIFTING KIND: the
  COMPLETE 2026-10-06 bar read `n` 3,734 / `v` 86,983 at 16:17 and `n` 3,735 / `v` 86,985 at 08:24 the
  next morning — THE MARKET WAS SHUT FOR THE ENTIRE INTERVAL — with `c` holding to the cent at
  716.29.** ⚠ **It CONFIRMS the established conclusion rather than changing it, and that is the whole
  value: the fields move on a bar that cannot possibly have changed, so no reading of them is evidence
  of anything.**
  ⚠⚠ **A FIELD THAT SOMETIMES MOVES ON A COMPLETE BAR IS UNUSABLE AS EVIDENCE IN EITHER DIRECTION: "it
  did not move this time" is not a validation any more than "it moved" was a refutation.**
  ⚠⚠ **THE `n`/`v` FLOOR TEST IS NOW RETIRED, NOT DOWNGRADED — 10-07 GAVE IT A DEMONSTRATED FALSE
  POSITIVE AND IT IS THE *COMPLETE* BAR THAT FAILED.** The 2026-10-07 session closed at **n 1,323 /
  v 23,415** — **BELOW EVERY trailing completed-session floor** (10-06 3,735/86,985 · 10-05 1,802/60,541
  · 10-02 2,524/134,995 · 10-01 1,634/51,893), a factor of **3.7 below yesterday on volume** — and the
  clock read `is_open: false` with `next_open` dated **2026-10-08**, so the bar was complete beyond
  question. ⚠ **THE LIMIT HAD BEEN WRITTEN DOWN AS THEORETICAL ("a quiet, low-participation FULL session
  could land under them") AND IT IS NOW AN INSTANCE. The floor test would have called today's finished
  session a partial bar.** ⚠ **It was never the primary and must not be used as a corroborant either:
  a test with a live false positive adds nothing to a discriminator that already works.** ⚠ **The
  separately stated half-day failure remains unobserved and is now moot.**
  ⚠⚠ **THE CLOCK, READ OFF `next_open`'s DATE, IS THE DISCRIMINATOR — AND AS OF 10-07 IT IS THE *ONLY*
  LEG LEFT STANDING. BOTH CORROBORANTS HAVE NOW FAILED ON A COMPLETE BAR.** The floor test failed as
  above. **AND THE `latestTrade`-MATCHING LEG FAILED THE SAME SESSION, BENIGNLY BUT REALLY: at 16:17 on
  10-07 `latestTrade` printed **714.53** at 16:00:52 against the daily bar's **c 714.66** — a 13-cent
  gap — and the 20:00Z minute bar agreed with the TRADE (714.53), not the close.** ⚠ **The explanation
  is innocent (a 600-share post-bell print on one venue is not the closing auction, and the daily `c` is
  the consolidated close), which is exactly why it is a defect in the RULE and not a doubt about the
  close: the leg was written as though a match were the normal case, and on an ordinary complete bar it
  did not hold.** ⚠ **A corroborant that disagrees with a correct close is worse than no corroborant.
  USE THE CLOCK. A bar dated today existing post-bell is confirmation that the session ended, nothing
  more.**
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
  **§5.1–§5.4 have never had an operand: 28 completed sessions since 2026-09-01, 25 post-fill, zero
  satellite positions ever.**
  ⚠⚠ **HELD AT 28/25 BY THE 10-12 08:36 PRE-MARKET SEAT, WHICH RE-EVALUATED ALL FOUR RULES IN ORDER AND
  FOUND NO OPERAND FOR ANY — AND WHICH MAY NOT ADVANCE THE COUNTER, because it stands BEFORE the bell on
  10-12 and 10-09 was already counted by that day's close seat. ⚠ THAT SEAT IS THE ONE CATCH (22) NAMES
  AS EXPOSED, SO THE HOLD IS DELIBERATE, NOT AN OVERSIGHT — the eighth time this seat has had to make
  it.** ⚠ **It also RE-DATED the
  `sell_rule_status` table rather than leaving it, because a table left untouched and a table
  re-evaluated to the same answer are indistinguishable to the next reader — the same way an ABSENT
  check and a PASSING one are. THE DATE IS THE ONLY THING THAT SEPARATES THEM.** ⚠⚠ **ADVANCED 26→27 BY THE 10-08 **16:16** SEAT AND BY NO EARLIER SEAT THAT
  DAY — and the 08:25 pre-market seat reached 27 anyway, which is CATCH (22) below.** ⚠⚠ **ADVANCED 25→26 BY THE 10-07 **16:17** SEAT AND BY NO EARLIER SEAT THAT
  DAY: the unit is a COMPLETED session, and only a seat standing AFTER the bell may count the day it is in.
  Routines 1 and 2 never may; routine 3 at 12:41 could not either. THE INCREMENT IS A FUNCTION OF THE
  SEAT'S POSITION RELATIVE TO THE BELL, NOT OF THE DATE. See catch (21).**
  ⚠⚠ **10-08 16:16 IS THE THIRD CONSECUTIVE CLOSE-SEAT NULL AND THE WEAKEST OF THE THREE AS EVIDENCE:
  the same null, the same conditions, a third time. SIX NULLS ACROSS THREE SESSIONS FROM BOTH THE STAMP
  SEAT AND THE DETECTOR SEAT STILL DO NOT TEST EITHER PATH, AND THE ONLY THING A FOURTH WOULD ADD IS A
  FOURTH.**
  ⚠⚠ **AND THE 10-07 16:17 CLOSE SEAT IS THE SECOND CONSECUTIVE CLOSE-SEAT NULL ON STEP 2 — WHICH MAKES
  IT WEAKER EVIDENCE, NOT STRONGER. It is the same null under the same conditions as 10-06 16:17. The only
  thing it adds is that the stamp seat and the detector seat have now BOTH recorded their own null on two
  consecutive sessions, and four nulls across two sessions still do not test either path.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — TWENTY-THREE CATCHES, AND THEY KEEP CHANGING
  SHAPE.**
  ⚠⚠ **(23) A FALSE SUPERLATIVE ABOUT THE RUN'S OWN HEADLINE FINDING, CAUGHT BEFORE PUBLICATION, WITH
  THE REFUTING ENTRY IN A FILE THE RUN HAD ALREADY READ.** The 10-09 seat wrote that **GFS** was *"the
  FIRST candidate in the live log to clear §3's instrument tests AND the priced-in filter and then die
  on the thesis parts rather than upstream of them"* — **and had already written it into `state.md`,
  `plan_today.md` AND `research_log.md` as the run's one real finding.**
  ⚠⚠ **IT IS FALSE. `T-2026-10-01-02` (AMD), eight sessions earlier, records
  `priced_in: false` (−0.52% over five sessions), `Universe (§3): PASSES — market cap far above the $10B`
  floor, and `REJECTED on part 3 … with part 2`. AMD CLEARED MORE THAN GFS DID — GFS's §3 cap is
  UNRESOLVED — AND DIED THE SAME WAY.** **Corrected in all three files to "the SECOND".**
  ⚠⚠ **THE NEW PART IS *WHERE IT CAME FROM*: this is the first catch in the series that is NOT an
  inherited claim. The run MANUFACTURED it, about its own work, in the same breath as doing the work —
  and a superlative is most tempting exactly when a run has finally produced something it thinks is
  interesting.** ⚠ **It is catch (12)'s direction (flattering, about the book's own output) wearing
  catch (13)'s mechanism (a claim about a whole series, refuted by a file already read).**
  ⚠⚠ **WHAT SURVIVED THE CORRECTION IS THE TEST THAT MATTERS: the narrower claim — that GFS is the first
  priced-in PASS on a GENUINE NEWS DAY, where AMD's was a −0.52% non-event drift — IS TRUE and is worth
  more than the false one was. CUTTING A SUPERLATIVE DOWN USUALLY LEAVES A REAL FINDING BEHIND.**
  ⚠ **AND THE PLAIN OBSERVATION THAT NEEDED NO SUPERLATIVE AT ALL: PART 3 KILLED BOTH OF THE TWO
  CANDIDATES THAT HAVE EVER REACHED §4's PARTS WITH THE FILTERS BEHIND THEM.**
  ⚠⚠ **(22) ONE RUN STATED THE RULE CORRECTLY AND BROKE IT FORTY-FOUR LINES LATER IN THE SAME FILE —
  AND THE WRONG NUMBER HAD ALREADY BECOME THE RIGHT ONE BY THE TIME ANYONE COULD CHECK IT.**
  `plan_today.md` **line 171**, written by the 10-08 08:25 pre-market seat: *"The §5-operand counter
  stands at 26 completed sessions / 23 post-fill and DOES NOT ADVANCE HERE: the unit is a COMPLETED
  session, and this seat stands before the bell on 10-08."* **Line 215, same file, same seat:** *"27
  completed sessions, 130 theses, ZERO POSITIONS EVER OPENED."* ⚠ **The thesis count was right (120 +
  today's ten); the session count was wrong by the rule the same seat had just written out in full —
  catch (11)'s exact shape recurring in the seat the rule names as exposed.**
  ⚠⚠ **THE NEW PART IS NOT THE ARITHMETIC, IT IS THE HALF-LIFE: "27" IS THE CORRECT FIGURE FROM THE
  16:16 SEAT, BY A COMPLETELY DIFFERENT ROUTE, SO THE FILE NOW READS AS CONSISTENT AND THE ERROR WOULD
  HAVE BEEN INVISIBLE WITHIN ONE SESSION.** ⚠ **Checking the number against today's reality would have
  CONFIRMED it. Only checking it against the reasoning that produced it catches this. That is catch
  (6) — A CORRECT NUMBER REACHED BY AN UNCHECKED ROUTE IS NOT A CHECKED FACT — at its cheapest and
  most literal: the route was wrong, the destination was right, and the window to notice was one day.**
  ⚠ **(19)'s companion rule is what found it: COUNT THE LIST, AND RECOMPUTE THE HEADER. Here it was
  two figures in ONE document, and the pull was to reconcile them against each other rather than each
  against its unit. DO NOT RECONCILE TWO FIGURES AGAINST EACH OTHER — RECOMPUTE BOTH AGAINST THE UNIT.**
  ⚠⚠ **(21) TWO COUNTERS OVER THE SAME DATE THAT *LEGITIMATELY DISAGREE* — CAUGHT BEFORE PUBLICATION,
  AND A NEW SHAPE.** This run first wrote **"26 completed sessions, 23 post-fill"** into
  `plan_today.md` and corrected it to **25 / 22**: the unit is a **COMPLETED** session and a
  pre-market seat stands **BEFORE** the bell, so 10-07 is not countable from here — catch (11)/(15)'s
  exact shape, recurring in the seat the rule names as exposed.
  ⚠⚠ **BUT THE NEW PART IS WHAT SITS NEXT TO IT: `positions.md` SIMULTANEOUSLY AND CORRECTLY SAYS
  "TWENTY-SIXTH SESSION WITH NOTHING TO RECONCILE", WHICH *DOES* INCLUDE TODAY — because that unit is
  a reconciliation PERFORMED, and this seat performed one. TWO COUNTERS, TWO UNITS, ONE DATE, AND THEY
  DISAGREE BY DESIGN.** ⚠ **The pull is to "fix" whichever one looks out of step with the other, and
  doing so would have broken a correct counter. AGREEMENT BETWEEN TWO COUNTERS IS NOT A VALIDITY CHECK
  AND DISAGREEMENT IS NOT AN ERROR SIGNAL — only the UNIT decides. Both are now stated with their unit
  named in the same breath, which is the only form that survives the next reader.**
  ⚠⚠ **AND IT RECURRED AT THE VERY NEXT SEAT, FROM THE OTHER SIDE: the 09:37 open run reached for a
  "TWENTY-SEVENTH reconciliation" and had to put it back. The reconciliation unit is a SESSION IN
  WHICH ONE WAS PERFORMED, 10-07 was already counted by the 08:24 seat, and a second reconciliation
  inside the same session advances NOTHING. The `cash`-reading counter DID advance 26→27 over the same
  two seats, correctly, because ITS unit is a reading. TWO COUNTERS, SAME TWO SEATS, ONE ADVANCES AND
  ONE DOES NOT — and only the unit says which.**
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

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — 89 RUNS, AND THE *GRADE* IS THE POINT, NOT THE
  COUNT.** *(Collapsed 10-12 09:37: the per-seat grading narrative for 10-05 through 10-12 08:36 is
  folded to the rule it produced plus the two instances that still carry information. Nothing live
  discarded.)*
  **THE REFUSAL, RE-DERIVED AND NOT INHERITED:** §5 exempts core from all four sell rules. A
  `highest_close` on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, which could eventually sell core on a drawdown — **§7 forbids that outright.** **Measure
  core from the 706.74 fill (a RAW print) and from an official close, never from a `positions` field.**
  ⚠⚠ **GRADED, NOT COUNTED — A SEAT THAT NEVER FETCHED THE DATA AND A SEAT THAT FETCHED IT AND REFUSED
  LOOK IDENTICAL IN A RUN SUMMARY, AND ONLY THE SECOND IS EVIDENCE OF ANYTHING.** **STRONG** = the seat
  held the NUMBER *and* a WRITE PATH (the close run, whose Step 2 *is* the stamp; and routine 3's Step 2
  backfill). **WEAK** = no write path, or no `bars` call, so no number was ever in hand to decline.
  ⚠⚠ **THE STRONGEST ON RECORD IS 10-09 16:17: a real completed official close — **715.58**, from its own
  `bars --days 4 --adjustment all` pull — AND the write path, on the only row the broker returns, at the
  one routine whose own instruction reads *"record the closes"*. NOTHING WAS WRITTEN.** *(10-12 08:36 was
  the STRONG-on-number grade at a pre-market seat for the first time, holding the same 715.58 with no
  write path.)*
  ⚠⚠ **THE 89th IS 10-12 09:37, AND IT IS THE **WEAK** GRADE ON BOTH LEGS — STATED THAT WAY RATHER THAN
  COUNTED AS A WIN. That seat made **NO `bars` call**, so it never held an official close to decline, and
  it opened no position, so its Step 6 write path was never live either.** ⚠ **The 716.1532 it did hold
  is a **LIVE BROKER MIDPOINT** out of `positions`, and DECLINING TO STAMP A NUMBER THAT IS NOT A CLOSE
  IS NOT THE SAME ACT AS DECLINING A CLOSE.**
  ⚠⚠ **THE PHANTOM DRAWDOWN TRACKS THE TAPE IN BOTH DIRECTIONS — catch (25) confirming itself: against a
  716.29 mark, the figure has moved −0.7064% → −0.0991% across three sessions. A fabricated mark produces
  a drawdown that MOVES WITH THE MARKET; the danger is not that it only ever grows.**
  ⚠ **A REFUSAL REPEATED 89 TIMES IS A REFUSAL NOBODY IS DECIDING ANY MORE, AND AUTOMATIC IS NOT SOUND.
  RE-MAKE IT ON ITS MERITS EVERY RUN; DO NOT INHERIT IT.**

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
  `plan_date`, NEVER INFER FROM THE OUTCOME.** *(Collapsed 10-12 09:37 by the seat that HOLDS the gate:
  the per-morning narratives for 10-05 through 10-09 are folded to the count and the rule, since a
  superseded reading of a field that is overwritten daily is not a durable fact. Nothing live discarded.)*
  ⚠⚠ **UPDATED 10-12 09:37 — READ OFF THE FIELD AND COMPARED TO THE *CLOCK'S* ET DATE (not a shell
  date): `plan_date: 2026-10-12` against today 2026-10-12 — **FRESH**, and the morning it produced was
  the **FIFTH consecutive indistinguishable zero-order one**.**
  **THE GATE HAS NOW BEEN EXERCISED 38 TIMES AND HAS NEVER FIRED; ITS ALERT PATH REMAINS UNTESTED CODE.**
  ⚠ **EVERY EXERCISE SO FAR *PASSED* — IT DID NOT FIRE, AND "PASSED" AND "FIRED" ARE OPPOSITE OUTCOMES OF
  THE SAME CHECK. Do not write that the gate has been tested.**
  ⚠⚠ **09-28 WAS THE MORNING IT WOULD HAVE FIRED — the plan genuinely carried `plan_date: 2026-09-25` —
  AND THE RUN CONTAINING THE GATE DID NOT EXECUTE. The gate's one real opportunity was lost to a missing
  run, not survived.**
  ⚠ **The first morning it fires will by construction be a morning when the pre-market run failed. Read
  routine 2's Step 2 then; do not recall it.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — NOTE THE BASIS ON EVERY ONE.** *(Collapsed 10-12
  08:36: the 10-08 and 10-09 per-seat readings and the spent `next_open` lines are REPLACED by the
  current pair rather than kept beside it. A superseded live mark is not a durable fact.)*
  Core is **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat, cost_basis
  **$69,999.99**.
  **OFFICIAL CLOSE BASIS, THE LATEST COMPLETED SESSION — 2026-10-09** (`bars --days 4 --adjustment all`,
  pulled by the 10-12 08:36 seat: o 713.52 h 716.37 l 712.75 **c 715.58**, n 1,645 v 70,028, vw
  715.336895 — a normal full session): equity **$100,875.5594**, core **$70,875.5594 = 70.2604%**, cash
  **29.7396%**. Day **+$430.8515 = +0.4289%** against 10-08's official $100,444.7079; **since inception
  +0.8756%.** Core unrealized **+$875.57 (+1.2508%)**. VOO itself was **+0.6116%** (715.58 vs 711.23),
  so the book **LAGGED by 0.1827pp — ON THE CASH FLOAT, NOT ON SKILL.** ⚠ **The 29.74% cash leg earns
  nothing on an up day and loses nothing on a down one; it is the SAME mechanism in both directions and
  only one of them flatters.** ⚠ **Re-derived at the 10-12 seat and agreeing with the 10-09 close seat
  TO THE CENT — which confirms the arithmetic and NOT the route, since it is the same route (catch (6)).**
  **LIVE BROKER MARK, 2026-10-12 08:36 (a DIFFERENT SERIES, NEVER CONCATENATED): `sleeves` equity
  $100,874.57, core $70,874.568928 = 70.26%, cash 29.74%, `rebalance_delta` −$262.37, `core_in_band:
  true`. `positions`: `current_price` 715.57, `lastday_price` 715.59, `change_today` −0.003%,
  unrealized +$874.58 (+1.249%).**
  ⚠ **A FIFTH SAMPLE OF THE MOVING MARK AT ONE SEAT: `selftest.py` read $100,879.52 and `sleeves` read
  $100,874.57 minutes later — a $4.95 spread on the same quantity. TWO CALLS MINUTES APART MUST NOT BE
  DIFFERENCED INTO ANYTHING. An equity figure is meaningless without its CALL and its TIMESTAMP.**
  ⚠⚠ **THE BROKER/OFFICIAL GAP IS A MOVING LIVE MIDPOINT, NOT AN OFFSET, ON BOTH SERIES — AND 10-12
  SUPPLIES THE SERIES' STRONGEST WARNING BY *AGREEING*.** **PRE-MARKET, five samples:** −$0.22 (10-05) ·
  +$2.84 (10-06) · −$3.05 (10-07) · +$3.08 (10-09) · **−$0.01 (10-12: `current_price` 715.57 against the
  official 715.58).** **POST-BELL, five samples:** +$0.470 and −$0.0254 (10-02, thirty minutes apart, a
  SIGN CHANGE on one official close) · +$0.1207 (10-06) · +$0.57 (10-08) · +$0.15 (10-09).
  ⚠⚠ **A ONE-CENT GAP IS NOT A CALIBRATION AND MUST NOT BE READ AS ONE — IT IS THE MOST DANGEROUS
  SAMPLE IN EITHER SERIES, BECAUSE A READING THAT HAPPENS TO AGREE IS THE ONE MOST LIKELY TO BE MISTAKEN
  FOR AN OFFSET OF ZERO.** The 10-06 precedent is the direct instance: a pre-market mark byte-identical
  to a later reading was **indistinguishable from a lagged mark on one sample.** ⚠ **BOTH SIGNS, A
  THREE-HUNDRED-FOLD MAGNITUDE SPREAD ON THE PRE-MARKET SERIES — NO OFFSET SURVIVES AND NO DIRECTION IS
  READABLE. NEVER difference a broker mark against an official close.**
  ⚠ **A THIRD SERIES (the INTRADAY LIVE MARK) AND A FOURTH (`positions.current_price` against the live
  quote plane, ~5–7 cents below the tape on its one sample) EXIST, AND NONE OF THE FOUR MAY BE
  CONCATENATED.**
  ⚠⚠ **BUT KEEP `lastday_price` OUT OF THE MOVING-MIDPOINT CLAIM — IT IS A DIFFERENT OBJECT.** Within a
  session it behaves as a **FIXED PRIOR-DAY FIELD**: it read **714.34 at all four seats of 10-08** and
  **711.28 at all four seats of 10-09**, byte-identical end to end, while `current_price` moved across
  the same spans. ⚠ **Its GAP to the official close is still unpredictable run to run (−$0.32 on 10-08,
  −$0.09 on 10-06, +$0.05 on 10-09, +$0.01 on 10-12) and it still must NEVER be differenced against one.
  This narrows WHICH series moves; it does not license using either.** ⚠ **Do NOT re-open WHY it differs
  — four mechanisms falsified, both signs observed. STOP PREDICTING IT.**
  ⚠ **NEVER `equity − last_equity` as a day's P&L** (fully attributed: `last_equity` = qty ×
  `lastday_price` + cash, reconfirmed to the last digit on three separate sessions). ⚠ **NEVER
  `unrealized_intraday_pl` or `change_today`.** **Close-to-close from `bars` on a COMPLETED session,
  adjustment STATED; a fresh `quote` for execution.**
  ⚠ **§6's 5% cap on the 10-12 live mark is **$5,043.73**. It has no operand only because no plan has
  ever carried a buy intent.**
  ⚠⚠ **THE NEXT `next_open` LINE TO BE SPENT IS TUESDAY 2026-10-13 — an ordinary overnight gap, so the
  next pre-market seat's `plan_date` comparison reads ONE trading day and ONE calendar day. 10-12's
  weekend shape (three calendar days, one trading day) is spent and must not be re-applied.**
  ⚠ **`is_open: false` HAS THREE MEANINGS — pre-market, post-bell, holiday. READ `next_open`'s DATE.
  `is_open: true` is the one case the boolean alone is sufficient. THE CLOCK IS THE ONLY WORKING
  MARKET-STATE DISCRIMINATOR; both corroborants (the `n`/`v` floor test and `latestTrade`-matching)
  FAILED on complete bars and are RETIRED.**
  ⚠ **DO NOT CARRY A CORE-WEIGHT *RANGE*: 10-06 repaired one at 08:22 and refuted the repair at 12:42,
  four hours apart inside one session. A range over a live moving mark goes stale by construction. §2
  never needed it — STATE THE LIVE READING AND THE TWO EDGES (10-12: 70.26%, passing by 5.26 and 4.74).**

- **✅⚠⚠ §1 BENCHMARK — THE "N OF N" DAILY SEPARATION IS **RETIRED, NOT EXTENDED**: IT IS AN ALGEBRAIC
  IDENTITY, NOT AN EMPIRICAL STREAK.** *(Resolved 2026-10-09 weekly review. This REPLACES the inherited
  "20 of 20" table, the per-session re-derivation task, and every "21 of 21 … 25 of 25" caveat. None of
  them is live any more.)*
  **All 25 post-fill sessions were re-derived from one 260-session `--adjustment all` pull: 10 VOO-up
  days (all negative excess), 14 down (all positive), 1 flat (exactly 0.0000pp). 25 of 25, no exception.**
  ⚠⚠ **AND NO EXCEPTION CAN EXIST. With the book equal to `shares × VOO + fixed cash`,
  `book_return = w × VOO_return` EXACTLY (`w` = prior close's core weight) — verified to machine
  precision, max residual **1.3 × 10⁻¹⁶** across all 25. Since `w < 1`, `excess = (w − 1) × VOO_return`
  always carries the opposite sign to the benchmark's move.**
  ⚠ **SO DO NOT SPEND ANOTHER CLOSE RUN "ADDING A SESSION" TO THIS SERIES, AND DO NOT RE-DERIVE IT.
  Six weeks of seats treated a theorem as evidence-gathering. The caution about superlatives was right;
  the thing it was applied to was never a claim about a series.** ⚠ **What survives, and it is the only
  part that was ever load-bearing: NEITHER DIRECTION IS SKILL, and a tight fit is not confirmation —
  the model fits to zero residual because there is NOTHING IN THE BOOK THE MODEL OMITS. It becomes a
  real empirical question again on the FIRST satellite fill, and not before.**
  **Worst excess on record 2026-09-21 −0.4694pp (VOO +1.5542%); best 2026-09-23 +0.2265pp (VOO −0.7582%).**

- **⚠⚠ NEW 10-09 REVIEW — THE CORE SLEEVE DOES *NOT* TRACK THE BENCHMARK, AND FIVE REVIEWS REPORTED
  0.0000% BECAUSE THEY MEASURED AGAINST THE WRONG THING.** §1 names S&P 500 **TOTAL** return and this
  paper account does not model dividends (settled 10-08). Measured from the 09-03 fill print 706.74 to
  the 10-09 close 715.58: **core actual +1.2508%** against **VOO total return +1.5090%** (incl. the
  $1.825/sh that went ex 09-28 and never arrived — **$180.76** on 99.046311231 shares) =
  **−0.2583pp, and ~1.03%/yr of the sleeve going forward.**
  ⚠ **On a PRICE basis the divergence really is 0.0000% and that statement was not false — it was
  answering a question §1 does not ask.** ⚠ **Report BOTH bases and name them. The divergence is the
  platform, NOT tracking error and NOT skill.** Combined annual handicap re-derived at this week's
  benchmark: **cash drag 29.7396% × 17.3486% = 5.1594pp + dividend 70.2604% × 1.3356pp = 0.9384pp =
  6.0978pp/yr BEFORE ANY DECISION** (up from ~5.82pp, because the benchmark's trailing year improved).

- **⚠⚠ NEW 10-09 REVIEW — A PERFORMANCE FIGURE THAT DEPENDS ON A CONVENTION MUST STATE THE CONVENTION
  *AND* THE ALTERNATIVE VALUE, EVERY WEEK. THE §1 HEADLINE HAS TWO DEFENSIBLE VALUES 1.31pp APART.**
  Since-inception excess is **−1.5932pp** from 2026-09-01 (the book's first session, $100k all cash,
  VOO base 698.34) or **−0.2830pp** from the 2026-09-03 close (when the 70/30 split was funded, VOO base
  708.88). **The spread is exactly the two sessions the book sat in 100% cash while VOO rose — a real
  cost the second convention excludes by construction.** The review reports the 09-01 form as the
  headline and both in the table. ⚠⚠ **THIS IS WEEK 5's "statistic promoted before it is stable"
  DEFECT ARRIVING IN THE §1 ANSWER ITSELF RATHER THAN ON THE REJECT BOARD, WHICH IS WORSE.**
  ⚠ **AND WEEK 5's INHERITED SINCE-INCEPTION VOO LEG (+0.6088%) IS RETIRED: its base date cannot be
  recovered from a fresh 260-session pull on EITHER basis. DO NOT CARRY IT FORWARD.**

- **⚠⚠ NEW 10-09 REVIEW — THE THEME-CONCENTRATION ITEM REACHED ITS THIRD REVIEW AND **WEAKENED**, SO IT
  WAS **NOT PROMOTED**. WEEK 5's COUNTER-DISCIPLINE CAUGHT THE ITEM WEEK 5 NOMINATED.** AI /
  data-centre hardware & semis among the top excesses: **6 of 6 (wk 4) → 9 of 12 (wk 5) → 7 of 12
  (wk 6)**, with PBR, SHOP, ACN, GRAL and OSCR taking five of the top twelve on four unrelated drivers.
  ⚠ **The structural argument is unchanged and still plausible; a mechanism that sounds right is not a
  finding. KEEP THE THREE-REVIEW RULE — this is the evidence it is worth keeping.**
  ⚠⚠ **AND THE CLEANEST INSTANCE THE INSTABILITY ITEM WILL EVER GET: on a ROW-FOR-ROW IDENTICAL subset
  (rejected ≤ 09-24, n=64, beat=26 — identical to week 5 on both) the MEAN moved −2.04% → −1.00% →
  −1.30% across three weeks. Composition demonstrably did not change. The counts are stable; the
  moments are not. On the full board mean and median moved in OPPOSITE directions.**

- **⚠ NEW 10-09 REVIEW — THE SCOREBOARD'S ONE LOAD-BEARING FIELD HAS NO ENFORCED FORMAT.** The ten
  10-08 entries write `**Outcome: REJECTED …**` instead of `**Outcome:** REJECTED …`; a count keyed on
  the week 1–5 delimiter silently drops **10 of 40** and reports a clean-looking 30. **Not a content
  defect — use a tolerant match (`^\**Outcome:?\**`) and state the entry count.** ⚠ **Also: "40
  theses" counts HEADINGS, not candidates — four entries this week disposed of 12, 11, 4 and 3 items
  each, so ~64 items were screened under 40 headings. Keep the heading convention for continuity and
  state the ambiguity.**

- **⚠ TEN ITEMS REMAIN WITH THE HUMAN — RECOUNTED FROM THE LIST BELOW BY THE 10-12 08:36 SEAT, WHICH
  DISCHARGED NOTHING AND ADDED NOTHING.** *(Collapsed 10-12: three seats' identical "discharged nothing,
  added nothing" statements folded to one. Nothing live discarded.)*
  **THE COUNT, RECOMPUTED AGAINST THE UNIT RATHER THAN READ OFF THE HEADER (catch (19), and catch (22)
  is the worked failure of reconciling two figures against each other instead):** twelve numbered items
  are listed below — (12), (11), (8), (1), (2), (3), (6), (7), (10), (4), (5), (9). **(4) is DISCHARGED**
  (the core's divergence is the 09-03 entry gap, proven 09-11) and **(5) is SETTLED AS A MECHANISM** (a
  moving live midpoint, not an offset, on both the post-bell and pre-market series). **Twelve minus two
  = TEN.**
  ⚠ **(8) IS *SPENT* RATHER THAN OPEN — the dividend test resolved on 10-08, branch (a) — BUT IT STAYS
  IN THE COUNT, because its CONSEQUENCE (§1 unmeetable by construction on this platform) was always the
  human's and is unanswered.** ⚠⚠ **(9) IS PARTLY DISCHARGED AND STILL OPEN: THE DIAGNOSIS IS SETTLED,
  ONLY THE FIX IS MISSING — and the 10-12 seat supplied the sharpest instance yet of why it is
  prompt-level rather than discipline-level. See its file-size paragraph.**
  ⚠ **NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A NUMBER A RUN COLLECTS.**
  **(12) NEW 10-06 09:36 — ROUTINE 2's STEP 6 SOURCES `voo_close_at_entry` FROM A BAR THAT IS PARTIAL
  AT THE MOMENT IT IS CALLED.** `bars --days 1` at 09:36 returned a bar dated TODAY with `n` 156 and
  `v` 2,029 — **six minutes of a session** — and the routine instructs that this call supply the §1
  baseline a position is measured against for its whole holding window. ⚠⚠ **AND 10-07 16:17 REMOVES THE ONE CHEAP MITIGATION ANYONE MIGHT HAVE PROPOSED FOR THIS: an `n`/`v`
  SANITY CHECK AT THE MOMENT OF THE CALL. A COMPLETE SESSION BAR READ n 1,323 / v 23,415 THAT DAY, BELOW
  EVERY RECENT FLOOR — so routine 2 cannot tell a six-minute partial from a quiet full session by
  participation either. THE FIX HAS TO BE THE SOURCE OF THE NUMBER (prior completed session's close, or
  defer the label to the close run), NOT A GUARD ON IT.**
  ⚠ **It has cost nothing because
  no position has ever been opened; it becomes wrong on the FIRST fill.** ⚠ **A prompt fix, not the
  agent's to make. See the partial-bar item above for the sound substitutes.**
  ⚠⚠ **CONFIRMED FROM BOTH SIDES OF THE BELL ON THE SAME SESSION: the identical call returned `n` 3,734
  / `v` 86,983 at 16:17. THE DEFECT IS NOT A MISREAD — the bar really is partial at 09:36 and really
  does complete. THAT MAKES THE ITEM MORE CERTAIN, NOT LESS URGENT, and the 16:17 observation CANNOT
  FIX IT, because the defective call happens at 09:35 and will meet the partial form every time.**
  **(11) A ROUTINE CAN SIMPLY NOT RUN, AND NOTHING NOTICES.** The 10-05 close run produced no
  commit and no alert; 09-28 was the first instance. **Two of ~28 close runs have now vanished; 10-06, 10-07 and 10-08 all executed.**
  ⚠ **This and (6) are one blind spot seen from two sides.** ⚠⚠ **THE 10-06 CLOSE RUN DID EXECUTE, AND
  THAT CHANGES NOTHING ABOUT THIS ITEM: the failure mode is a run that never starts, so a run that
  started is not evidence about it in either direction. THERE IS STILL NO MECHANISM THAT NOTICES A
  MISSING SEAT.** ⚠ **What it DID buy is specific and is spent: (8)'s last pre-deadline reading was
  taken by a seat that ran, so this item is no longer load-bearing for that one.**
  **(8) THE DIVIDEND — THE DEADLINE PASSED, THE CREDIT NEVER CAME, AND THE ANSWER DID *NOT* LAND IN THAT
  SESSION. THE READING IS NOW THE FIRST 10-08 SEAT'S.** Priced at ~0.93pp/yr on top of the 4.89pp cash
  drag; a **twenty-ninth** unchanged reading of **$30,000.00** at **10-07 16:17**, the **third taken after
  the bell on the pay date**, from two call paths with `accrued_fees: 0`.
  ⚠⚠ **THIS ITEM PREVIOUSLY SAID, IN ADVANCE AND CORRECTLY, THAT NON-ARRIVAL AT 16:15 WOULD BE A PLATFORM
  FINDING AND "NOT A REASON TO EXTEND THE DEADLINE." THE DEADLINE WAS EXTENDED ANYWAY, AND THE HUMAN SHOULD
  SEE THE REASON AND JUDGE IT RATHER THAN HAVE IT PRESENTED AS SETTLED.** The reason is one API field:
  `account.balance_asof` read **2026-10-06 at 16:17**, seventeen minutes after the close of the pay date,
  having not moved from 08:24 through 16:17 — so the cash figure is a **prior-day snapshot**, and a
  non-arrival against a balance stamped *before* the pay date tests nothing about dividends.
  ⚠⚠ **AND THE SHAPE IS HONESTLY NAMED: AN AGENT DEFERRING A TEST IT SET IN ADVANCE, ON THE SEAT THAT WAS
  TOLD IT HAD NO SUCCESSOR, IS EXACTLY WHAT A SOFTENING LOOKS LIKE. The only thing separating the two is
  that the field was READ rather than reasoned, and that a COLLAPSE CONDITION WAS WRITTEN BEFORE THE FACT:
  had `balance_asof` advanced to 2026-10-07 while cash stayed at $30,000.00, the refinement would have
  failed and the platform finding would have been due that night.** ⚠ **The falsifiable claim ($30,180.76)
  is UNCHANGED and has been moved exactly ONCE. The three-branch decision rule for 10-08 is written out in
  full in the dividend item above. IF THE HUMAN THINKS THE EXTENSION WAS WRONG, SAY SO IN `control.md` AND
  THE NEXT SEAT WILL READ THE NON-ARRIVAL AS THE ANSWER.**
  **(1)** the priced-in filter reads a drawdown as priced-in — **LITE at +28.34pp is the bill.**
  **(2)** the same filter reads an absorbed event move as a pass (QCOM, AVAV, AKAM).
  **(3)** the structurally undeployed sleeve — **143 theses over 28 completed sessions, zero accepted, ~$30,000 in cash since inception.**
  **(6)** `selftest.py` certifies a healthy system without probing `clock` or market data — **it passed
  all five on 09-28 and 09-29 while three of 09-28's four routines had produced nothing, and it passed
  all five on 10-06 the morning after a close run vanished.**
  **(7)** see (1) and (2) — only a human may change §4 or `alpaca.py move`.
  **(10)** the rollover rule says to move entries older than the current month out of `trade_log.md`;
  the 09-03 core fill was archived **AND RETAINED live**, because the position is OPEN and removing it
  would make the ledger read as an account that has never traded. **Overrule in `control.md` if wrong.**
  ⚠ **(4) IS DISCHARGED** (the core's divergence is the 09-03 entry gap, proven 09-11). ⚠ **(5) IS
  SETTLED AS A MECHANISM** — a moving live midpoint, not an offset, on BOTH the post-bell and
  pre-market series. ⚠⚠ **(9) IS PARTLY DISCHARGED AND STILL OPEN. THE DIAGNOSIS IS SETTLED; ONLY THE FIX IS MISSING.**
  *(Collapsed 10-09 weekly review: three per-seat retellings of the SAME mechanism folded to the
  mechanism plus the measured history. Nothing live discarded.)*
  **LEAVING THE 10-12 PRE-MARKET SEAT: `state.md` 128,756B · `positions.md` 97,981B ·
  `research_log.md` 158,313B · `weekly_review.md` 234,838B · `journal.md` 63,283B · `trade_log.md`
  4,573B — ~690KB read IN FULL every run.**
  ⚠⚠⚠ **THE 10-12 SEAT'S NET, AND IT IS THIS ITEM'S OWN MECHANISM CAUGHT IN THE ACT: THE COLLAPSE WAS
  REAL, AND THE RUN'S OWN RECORDING SPENT IT.** Five carry-forward items were genuinely collapsed — the
  SPENT Monday handoff, the GFS correction narrative, the funnel-framing worked examples, four sessions
  of verbatim denial quotes, and the per-day reject narratives — and after them `state.md` stood at
  **122,950B, a genuine −3,858B against the 126,808B it arrived at.** ⚠⚠ **IT THEN WENT BACK UP TO
  128,756B — +1,948B ON THE RUN — BECAUSE OF THE COUNTER UPDATES AND, LARGELY, *THIS VERY PARAGRAPH*.
  THE SAVING WAS NOT CANCELLED BY ANOTHER FILE THIS TIME; IT WAS CANCELLED BY THE ACT OF WRITING DOWN
  THAT IT HAD HAPPENED.** ⚠ **That is the sharpest instance the item will get, and it is an argument for
  the PROMPT-LEVEL fix (an archivable unit) rather than for more discipline: there is no amount of care
  that makes a run record its own work for free.**
  ⚠⚠ **AND THE FILE SET GREW REGARDLESS, BY ~22,111B — `research_log.md` +18,327B AND `plan_today.md`
  +2,151B AGAINST `positions.md`'s −315B. REPORTING ONLY THE COLLAPSE WOULD BE THE FLATTERING HALF.**
  ⚠ **THE NEWLY NAMED PART: `research_log.md` IS THE FASTEST-GROWING FILE IN THE CORPUS PER RUN, AND IT
  GROWS *FASTEST ON A NO-TRADE DAY* — five rejections cost 18KB, because a rejection's value IS its
  reasoning and the reasoning is the bytes. ⚠⚠ THAT IS A DIRECT TENSION WITH §8's "rejected theses are
  the most useful data you generate", AND IT IS NOT THE AGENT'S TO RESOLVE: the monthly rollover is the
  only mechanism that reaches this file, it fires once a month, and October's live entries are already
  larger than September's whole archive.**
  ⚠⚠ **THE MECHANISM, WHICH IS WHY THIS IS PROMPT-LEVEL AND NOT DISCIPLINE-LEVEL: every seat is
  instructed to RECORD, and only some files have anywhere for the records to go.** `positions.md` has a
  collapsible unit (the per-seat block) and an owner; `journal.md` is month-scoped with
  `archive/journal/` as its unit; `research_log.md` and `trade_log.md` likewise. **`state.md` has NO
  month boundaries and therefore NO archivable unit — `last_run`/`prior_run` must be rewritten in full
  every run and the carry-forward has no unit at all, so EVERY seat grows it by construction and NO seat
  can shrink it. The rule "collapse, do not append" CANNOT REACH THE FILE THAT GROWS FASTEST.**
  ⚠ **`weekly_review.md` is now the LARGEST file in the corpus (190,907B) and the Friday seat is the
  only one that writes there — so it has the same unbounded shape as `state.md`, and nobody has named
  that before.**
  **Measured history, honestly signed:** real collapses have happened — `positions.md` 68KB → ~53KB,
  then 113KB → 107KB, then the 10-09 08:27 seat's **107KB → 87KB (−20KB, largest single reduction on
  record)** — **and every one was more than cancelled by growth elsewhere.** ⚠ **THREE CONSECUTIVE
  SEATS IN ONE SESSION netted UP (08:27 −20/+12 down, 12:41 −1.2/+6.3 up, 16:17 −0.2/+16.2 up, the
  worst single-run net on record). THREE INSTANCES IN ONE SESSION IS EVIDENCE OF THE MECHANISM, NOT OF
  INDISCIPLINE** — the 16:17 close seat is structurally heaviest because it is the ONLY seat that writes
  a journal entry, and one entry cost 10.5KB.
  ⚠⚠ **AND THE RULE IS UPGRADED 10-09: ONE RE-READ IS NOT ENOUGH — A SELF-REFERENTIAL CLAIM MUST BE
  ITERATED TO CONVERGENCE, BECAUSE THE CORRECTION IS ITSELF PART OF THE THING MEASURED.** The 10-09
  review hit this three times in a row on one sentence: a correct pre-write measurement (-4,095B) was
  falsified by writing it (+266B), the first correction (-3,829B) was falsified by correcting it (+2B),
  and only the third was self-consistent. **State the number ONLY once the file size and the claimed
  size are equal, and prefer a LENGTH-PRESERVING edit when fixing one.**
  ⚠ **A FILE-SIZE CLAIM INSIDE THE FILE IT MEASURES IS SELF-REFERENTIAL AND MUST BE RE-READ AFTER THE
  WRITE, NOT BEFORE IT** — a draft of that very sentence claimed −2.9KB and then added ~1.9KB, making
  itself false as written. Measure in BYTES, not rounded KB.
  ⚠⚠ **THE CONCRETE SUGGESTION, NOW SIX RUNS OLD AND UNANSWERED: give `state.md` an archivable unit by
  making a DISCHARGED carry-forward item movable. There is currently an instruction to MARK an item
  discharged and NONE to MOVE it out, so discharged items accumulate forever beside live ones — items
  (4) and (5) are marked DISCHARGED/SETTLED and are STILL being read in full by every seat of every
  run. THAT is the unit, and no routine owns moving it. The rollover rule excludes `positions.md` by
  design and reaches neither `state.md` nor `weekly_review.md`.**
---

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause: supplying the causal link yourself, then finding a source merely adjacent
to it.**

**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* **The most prolific rule.**
⚠⚠ **THE 10-07 COSTUME AND IT IS THE BEST ONE YET: AN UNDEFINITIZED CONTRACT ACTION *PRICING* A
PREVIOUSLY ANNOUNCED FRAMEWORK.** Boeing's **$14.7B** PAC-3 MSE seeker award from Lockheed Martin
(announced 10-05) **formalises and prices a seven-year framework agreement Boeing and the DoD had
ALREADY announced in April 2026, intent to triple seeker output included.** ⚠ **THE DOLLAR FIGURE IS
GENUINELY NEW WHILE THE ECONOMIC EVENT IS SIX MONTHS OLD — the one combination that reads as fresh
news to any reader and to every filter.** ⚠ **"Undefinitized" also means final pricing is not
complete, so the headline figure is not even a fixed revenue number.** ⚠ **Caught only because the
drill query asked for the disclosure history explicitly; the cost was one clause.**
⚠ **A quieter 10-07 instance in the same run: POSCO Future M's KRW 6T "new" LFP deal is an
**AMENDMENT to the parties' 2023 supply agreement**, volunteered by the source.**
**Other costumes:**
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
