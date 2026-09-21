# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-21 09:36 ET 2-market-open-execution (selftest PASSED all five checks at 09:35 ET, trading_enabled true, LIVE paper, equity 99971.27 at pre-flight; THE SESSION IS OPEN AND FOR ONCE THE BOOLEAN SETTLED IT - clock at 09:36:09 reads is_open TRUE with next_close 16:00 TODAY and next_open 2026-09-22, the FIRST SHAPE THIS WEEK THAT IS UNAMBIGUOUS WITHOUT THE DATE, worth recording because the three runs before it all had to discriminate holiday from pre-market from post-bell on next_open alone; ZERO ORDERS PLACED - no buys, no sells, no rebalance, no core bootstrap, and ALL FIVE OF THOSE WERE DECISIONS WITH A READ BEHIND THEM rather than steps that silently did not run; STALE-PLAN GATE EXERCISED FOR THE TWENTY-SECOND TIME AND FOR THE TWENTY-SECOND TIME IT DID NOT FIRE - plan_date reads 2026-09-21 and today in ET IS 2026-09-21, they MATCH, so the plan is FRESH and its emptiness IS THE PLAN, not a gap in it; THE GATE'S ALERT PATH REMAINS UNTESTED CODE after twenty-two clean passes, and twenty-two quiet opens are NOT evidence it works - the first morning it fires is by construction a morning when the 08:00 run failed, i.e. the exact morning with no fresh notes to lean on, so READ STEP 2 THEN, DO NOT RECALL IT; WEEK ROLLOVER CHECKED, ANCHORS MATCHED, NO RESET DUE - today IS Monday 2026-09-21, its own ISO Monday, and week_of ALREADY read 2026-09-21 because FRIDAY'S REVIEW ADVANCED IT AHEAD OF THE BOUNDARY, second consecutive run to find the reset already done, new_positions_this_week stays 0 of 3; RECONCILIATION CLEAN AND COMPARED SATELLITE-TO-SATELLITE - ledger satellite blocks (zero) against Alpaca satellite positions (zero), they AGREE; positions returns ONE row, VOO core 99.046311231 shares UNCHANGED since the 09-03 fill, no order has touched it in eighteen sessions, avg_entry 706.74, unrealized_pl -27.73/-0.04% on the broker mark which is STILL the 09-03 entry gap and never tracking error; STEP 3 SKIPPED ON A READ NOT AN ASSUMPTION - core_established is TRUE, the bootstrap path is permanently disabled; STEP 4 HAD NO SUBJECT - zero SELL intents and zero open satellite positions, so 5.1-5.4 went UNTESTED for the TWENTY-SECOND CONSECUTIVE SESSION, sell_rule_status ABSENT rather than blank, and 5.4 IS STILL NOT ARMED (it arms on the first SATELLITE fill and the 09-03 core fill was not it); STEP 5 RAN ZERO move CALLS AND THAT IS AN ABSENT CHECK, NOT A SKIPPED ONE - re-validation has a subject only when a BUY intent exists, and there were none; STEP 6 PLACED NOTHING; STEP 7 REBALANCE EVALUATED AND CORRECTLY DECLINED - equity 99972.26, cash 30000.00, core 69972.257032 = 69.99%, satellite 0.0% count 0, cash 30.01%, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta 8.32 = 0.008% of equity, THIRTIETH consecutive run inside the 0.41-point band 69.59-70.00, and 2 rebalances at the 65/75 EDGE rather than to the 70 target so no delta inside the band is an action at any size; FULL AUTHORITY FOUND AND NONE USED FOR THE EIGHTH CONSECUTIVE OPEN - breaker INACTIVE, cap 0 of 3, empty satellite sleeve, 30.01% idle cash, no restricting note in control.md, and NOTHING BLOCKED A TRADE: there was nothing in the plan to execute, which is 4's honest-broker rule landing as designed and NOT a system fault; THE TWO-PRICE DEFECT'S NINTH INSTANCE PERSISTED INTO THE SESSION AND WAS PRICED IN DOLLARS AT AN OPEN FOR THE FIRST TIME - lastday_price STILL reads 701.78 against Friday's OFFICIAL close of 701.85, seven cents low, and because change_today (+0.667%) and unrealized_intraday_pl (+463.54) are BOTH built on that stale baseline, the broker's day-P&L is overstated by 99.046311231 x 0.07 = $6.93 BEFORE any argument about whether 706.46 is a close at all - IT IS NOT, it is a live in-session midpoint; $6.93 is small where 09-18's was $106, and THE POINT IS THAT THE MECHANISM IS IDENTICAL AND THE SIZE IS SET BY THE GAP, NOT BY ANYTHING A RUN CONTROLS; NEITHER FIGURE WAS QUOTED AS A DAY'S P&L; NO HIGH-WATER BACKFILL DUE AND IT WAS CONFIRMED BY READING - there is no highest_close to raise and therefore no (as of ...) stamp to compare, the marks are ABSENT (a third state) and an absent field carries NO DATE, which is exactly what proves no backfill is owed; CORE VOO DELIBERATELY NOT STAMPED for the thirty-seventh run, 5 exempts core from all four sell rules so no number attaches to an action in either direction; GNRC NOT LOOKED AT FOR THE NINTH CONSECUTIVE RUN, AND THE HONEST RECORD IS THAT NO NINTH COSTUME HAD ANYWHERE TO HIDE - the plan named zero re-validations so this run had NO PRICING STEP AT ALL, and a pull would have had to be invented from nothing rather than smuggled into a call that was already happening, which makes this a WEAKER TEST OF THE REFUSAL THAN THE EIGHT BEFORE IT, not a stronger one: the predicted ninth framing is NEITHER CONFIRMED NOR REFUTED and the next run with a genuine move/quote step is where to watch for it; zero move/quote/bars/asset calls on GNRC, NINE RUNS RUNNING; GIS CARRIED FORWARD UNTOUCHED - General Mills Q1 FY2027 is due 2026-09-23, there is still nothing to screen, re-armed for the 09-23 pre-market run and NOT this seat's item; counters 49 theses since inception, 3 this week, 0 ACCEPTED, ZERO satellite positions ever opened, ZERO exits ever; alerts.md EMPTY, zero open, zero SYSTEMIC)

prior_run: 2026-09-21 08:20 ET 1-premarket-research (selftest PASSED all five checks at 08:20 ET, trading_enabled true, LIVE paper, equity 99988.10 at pre-flight; PRE-MARKET SHAPE CONFIRMED FROM THE DATE NOT THE BOOLEAN - clock is_open FALSE at 08:20:11 with next_open 2026-09-21T09:30 TODAY and next_close 16:00 TODAY, so a session begins in 70 minutes and this is NOT a holiday; routine 1 places no orders by design and this run placed, evaluated and intended NONE; WEEK ROLLOVER CHECKED AND CORRECTLY DID NOTHING - today IS Monday 2026-09-21, the ISO Monday of its own week, and week_of ALREADY read 2026-09-21 because FRIDAY'S REVIEW ADVANCED IT AHEAD OF THE BOUNDARY, so the anchors MATCHED, no reset was due and none was performed, new_positions_this_week stays 0 of 3 - the mechanism working as designed, NOT a skipped check, and it is stated because a run that finds nothing to do here is indistinguishable from one that never looked; RECONCILIATION CLEAN - satellite blocks (zero) checked against satellite Alpaca positions (zero), they AGREE, positions returns ONE row VOO core 99.046311231 shares UNCHANGED since the 09-03 fill, unrealized_pl -11.89/-0.017% on the broker mark which is the NARROWEST the core's reported divergence has ever read and is STILL the 09-03 entry gap, never tracking error; RESEARCH - 5 Perplexity scans (2 broad --recency day, 3 targeted --recency week), THREE theses written T-2026-09-21-01/02/03, ALL THREE REJECTED, ZERO BUY INTENTS, and NOTHING BLOCKED THE RESEARCH: breaker INACTIVE, cap 0 of 3, empty sleeve, 30.0% idle cash, no restricting note in control.md - SEVENTH CONSECUTIVE PRE-MARKET RUN TO FIND FULL AUTHORITY AND USE NONE OF IT; T-01 GM is the RECORD OF THE DAY - Lockheed Martin <-> GM Defense PAC-3 MSE housing castings, PART 1 PASSED CLEANLY IN ONE CLAUSE on a SIGNED PRODUCTION CONTRACT (2026-08-06) and a PHYSICAL FIRST DELIVERY (2026-08-28), both parties named and US-listed, and PART 2 STILL COULD NOT BE WRITTEN because BOTH SIDES EXPRESSLY REFUSED TO DISCLOSE (Inside Defense 'the companies did not disclose the value or quantity'; GM spokesman Jim Cain, value and deliverables will not be disclosed, 'proprietary'; no unit count, no term, no multi-year value) AND GM REPORTS NO DEFENCE SEGMENT REVENUE so the 10% floor cannot be tested even in principle - THE FIRST TIME ALL FOUR OF (both parties named + primary source + product physically shipped + part 1 passing in one clause) HELD AT ONCE AND PART 2 STILL FAILED, and the missing number is MISSING BY COMMERCIAL CHOICE NOT BY REPORTING GAP so NO BETTER-SOURCED VERSION WILL EVER ARRIVE; T-01 ALSO DIED INDEPENDENTLY ON RULE (iii) - the Monday headline is a re-report, Reuters carried it 09-17 and the contract is FIVE WEEKS OLD, a NEW COSTUME for rule (iii): a genuine transaction whose DELIVERY MILESTONE is recycled as the news, and the DATE was the CHEAPER of the two kills at one screen; T-02 BE Brookfield/Bloom 5B->25B AI data-centre financing framework, THREE independent kills - Bloom is a SIGNATORY (first-order, outside 4 at any price), the 25B is FINANCING CAPACITY not revenue and not even capital received (Bloom's OWN 09-16 materials: revenue 'will depend on projects that are ultimately funded, built and accepted'; a second note: 'a financing capacity, not firm orders or revenue already secured'), and NO US-listed supplier is named by any source; STANDING RULE (viii) FIRES A SECOND TIME IN THREE SESSIONS AND SHOULD BE READ MORE BROADLY THAN IT WAS WRITTEN - 09-18's trap was capital paid IN (1.8B), today's is ONE STEP FURTHER AWAY, a ceiling available to SOMEBODY ELSE that may never be drawn, so read (viii) as covering ANY disclosed figure that is not SEGMENT REVENUE AT COMPANY B, not merely 'capital in'; T-03 BG Bunge raised FY26 adj EPS 9.00-9.50 -> 9.25-9.75 on stronger Q2 crush (Soybean P&R adj EBIT +46.4% to 445M, Softseed 14M -> 255M), REJECTED AT PART 1, SEVENTH SHARED-CAUSE INSTANCE, and the NEW EDGE is that ADM's own raise is cited SIDE BY SIDE with Bunge's as evidence of the same margin environment - 09-16's JPM/BAC/WFC finding was that a DIVERGENCE sounds causal, today's is that a CONVERGENCE does, SAME TRAP OPPOSITE SIGN and the convergent version is MORE seductive because agreement looks like corroboration; PRICED-IN FILTER RUN ONCE AND IT PASSED ON A FALL - move --symbol GM --sessions 5 returned 85.59 -> 82.21, -3.95%, priced_in FALSE, FIVE BASIS POINTS inside the 4% wire, so had GM fallen 4.1% the filter would have said 'LATE - skip' on a stock that had gone DOWN: SECOND NEAR-MISS INSTANCE of open item (1) after LMT -3.61% on 09-11, and THE PASS IS NOT EVIDENCE THE FILTER WORKED; GIS CARRIED ITEM DISCHARGED IN WRITING - General Mills has NOT reported, Q1 FY2027 is due SEPTEMBER 23 (consensus 0.72 vs 0.86 a year ago, ~4.34B revenue, ALL analyst expectations), and its only company statement is the SEPTEMBER 8 AFFIRMATION of FY27 adj EPS 3.00-3.20 which is STANDING RULE (iii), the Centene and Southwest shape - NOTHING TO SCREEN UNTIL THE 23rd, carried EXPLICITLY to the 09-23 pre-market run; SECOND BROAD SCAN WAS BUILT TO FIND EXACTLY WHAT PART 2 NEEDS AND FOUND NOTHING ELIGIBLE - it demanded a named customer AND a named supplier AND a disclosed value and excluded 'terms not disclosed' and bare ceilings, returning THREE items, ALL failing 3 or privately held (BEML/NHSRCL and Welspun/Ahmedabad both INDIAN-LISTED and the only two in the whole window carrying both parties AND a value; US Army/Skyeton 'over $10 million' PRIVATE with no obligated figure) - a finding about the WINDOW, not a reason to lower the bar, and the WEEKEND IS NOT BEING USED AS A THIN-NEWS EXCUSE; NINTH TWO-PRICE INSTANCE AND THE GAP CHANGED SIGN - lastday_price 701.78 against Friday's official close 701.85, SEVEN CENTS LOW, where 09-17 and 09-18 both read 701.03 against 700.97 SIX CENTS HIGH, so the sign of the error is not stable either; current_price 706.62 is a PRE-MARKET midpoint; unrealized_intraday_pl +479.38 MUST NOT be quoted as a day's P&L, it is the same stale-baseline arithmetic that nearly put +193.14 into Friday's headline in place of the true +87.16; SLEEVES IN BAND, NO REBALANCE - equity 99988.10, cash 30000.00, core 69988.10 = 70.0%, satellite 0.0% count 0, cash 30.0%, core_in_band true, rebalance_needed false, rebalance_delta +3.57 = 0.004% of equity which is THE NARROWEST DELTA IN THE ACCOUNT'S HISTORY against a prior range of 111.73-212.46, TWENTY-NINTH consecutive run inside a 0.41-point range 69.59-70.00; 5.1-5.4 NEVER STARTED for the TWENTY-FIRST SESSION, sell_rule_status ABSENT rather than blank, all four remain UNTESTED CODE PATHS, 5.4 STILL NOT ARMED (it arms on the first SATELLITE fill); NO HIGH-WATER BACKFILL DUE AND IT WAS CONFIRMED BY READING - there is no (as of ...) stamp to compare because there is no highest_close to carry one, the marks are ABSENT (a THIRD state) and an absent field carries NO DATE, which is exactly what proves no backfill is due; CORE VOO DELIBERATELY NOT STAMPED for the thirty-sixth run, though the pull was WEAKER today only because a research run prices nothing and had no reason to hold VOO bars - which says nothing about the close run's version at 16:00; GNRC NOT LOOKED AT FOR THE EIGHTH CONSECUTIVE RUN AND THE PREDICTED EIGHTH COSTUME ARRIVED ON SCHEDULE - 'the 09-16 gap is now three sessions deep in bars so a clean move reading finally exists, pulling it would let open item (7) be CLOSED with a number rather than left open for the human', THE FIRST OF THE EIGHT THAT PROPOSES TO DO THE HUMAN'S WORK RATHER THAN THE AGENT'S, refused on two facts independent of the wording: open item (7) states that NO RUN MAY REINTERPRET THE FILTER (that is a human editing 4 or alpaca.py move) so NO NUMBER THIS SEAT COULD COLLECT WOULD CLOSE IT, and GNRC is the named counterparty in the Amazon announcement, first-order and outside 4 at any price; zero move/quote/bars/asset calls on GNRC, EIGHT RUNS RUNNING, costumes: diligence, curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure - EIGHT SEATS, EIGHT DISTINCT RATIONALES, NO REPEATS, expect a ninth at the bell; counters 49 theses since inception, 3 this week, 0 ACCEPTED, ZERO satellite positions ever opened; alerts.md EMPTY, zero open, zero SYSTEMIC)

week_of: 2026-09-21
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.99
satellite_pct: 0.0
cash_pct: 30.01
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

- **⚠ THE 09-21 OPEN PLACED ZERO ORDERS AND THE ONLY THING THAT MAKES THAT RUN DISTINGUISHABLE FROM A
  RUN THAT NEVER FIRED IS THE DATE COMPARISON, WHICH WAS MADE AND PASSED.** `plan_date` **2026-09-21**
  against today in ET **2026-09-21** — **they match, the plan is FRESH, and its emptiness IS the plan.**
  **An empty-but-current plan and a stale plan produce IDENTICAL zero-order runs**, so the order count
  can never tell them apart and only the date can. **The stale-plan gate has now been exercised
  twenty-two times and has never fired; its alert path is still UNTESTED CODE.** ⚠ **Twenty-two quiet
  opens are not evidence the gate works.** The first morning it fires will, by construction, be a
  morning when the 08:00 run failed — **the exact morning with no fresh notes to lean on. Read Step 2
  then; do not recall it.**
  **Full authority was found and none of it used, for the EIGHTH consecutive open:** breaker
  **INACTIVE**, weekly cap **0 of 3**, satellite sleeve **empty**, **30.01% idle cash**, no restricting
  note in `control.md`. **Nothing was blocked — there was nothing in the plan to execute.** ⚠ **Idle
  cash plus an unused cap is not an opportunity an execution run may act on.** A position opened at
  09:35 without a plan entry would route *around* the discipline rather than satisfy it.

- **⚠ THE STALE-BASELINE P&L DEFECT WAS PRICED IN DOLLARS AT AN OPEN FOR THE FIRST TIME: $6.93, AND
  THE SMALLNESS OF THE NUMBER IS THE LEAST INTERESTING THING ABOUT IT.** At 09:36 `lastday_price`
  **still reads 701.78** against Friday's **official close of 701.85** — the **ninth instance
  PERSISTING into the session**, not a tenth. Because **`change_today` (+0.667%) and
  `unrealized_intraday_pl` (+463.54) are both computed off that stale baseline**, the broker's implied
  day-P&L is overstated by **99.046311231 × $0.07 = $6.93** — and that is *before* the separate
  objection that **706.46 is not a close at all but a live in-session midpoint.**
  **09-18's version of this same arithmetic was wrong by $106.** ⚠ **The mechanism is identical; only
  the gap differs, and the gap is not something a run controls.** **Neither figure was quoted as a
  day's P&L by this run.** Close-to-close from `bars --adjustment all`, always.

- **⚠ GNRC: NINE RUNS, AND TODAY'S ENTRY IS A CORRECTION TO THE SCOREBOARD RATHER THAN A NINTH SCALP.**
  The 09-21 pre-market run predicted *"expect a ninth costume at the bell."* **It did not arrive, and
  the honest reason is not restraint — it is that there was nowhere for it to hide.** The plan named
  **zero re-validations**, so **this run had no pricing step at all**; a GNRC pull would have had to be
  **invented from nothing** rather than smuggled into a `move`/`quote` call that was already happening.
  ⚠ **That makes 09-21's open a WEAKER test of the refusal than the eight before it, not a stronger
  one. The prediction is neither confirmed nor refuted.** **Watch for the ninth on the next run that
  has a genuine pricing step.** GNRC remains the **named counterparty** in the Amazon announcement —
  **first-order, outside §4 at any price.** Zero `move`/`quote`/`bars`/`asset` calls, **nine runs
  running.** Costumes so far: diligence, curiosity, tidiness, completeness, zero-marginal-cost,
  self-audit, proxy-procurement, issue-closure.

- **⚠ THE HEADLINE OF 09-21, AND IT IS THE SHARPEST SPECIMEN THE FUNNEL HAS PRODUCED: EVERY PRECONDITION
  §4 ASKS FOR HELD AT ONCE — BOTH PARTIES NAMED AND US-LISTED, A SIGNED PRODUCTION CONTRACT, A PRODUCT
  THAT PHYSICALLY SHIPPED, AND PART 1 PASSING IN ONE CLAUSE — AND PART 2 STILL COULD NOT BE WRITTEN.**
  **Lockheed Martin ↔ GM Defense, PAC-3 MSE interceptor housing castings.** Contract signed
  **2026-08-06**, **first batch delivered 2026-08-28**, Reuters **2026-09-17**. Part 1: *"Lockheed's
  PAC-3 MSE production ramp causes General Motors' GM Defense segment revenue to increase because GM
  Defense now manufactures and ships the interceptor housing castings under a signed production
  contract."* **No "and also". A transaction, not a shared cause, not a read-across.**
  **It died because BOTH SIDES EXPRESSLY REFUSED TO DISCLOSE:** Inside Defense — *"the companies did not
  disclose the value or quantity of the order"*; **GM spokesman Jim Cain** — value and deliverables
  **will not be disclosed**, *"proprietary"*; **no unit count, no contract term, no multi-year value.**
  **And the denominator fails independently: GM reports no defence segment revenue at all**, so §4's
  10% floor **cannot be tested even in principle.**
  **⚠ WHY THIS ENTRY OUTRANKS THE THREE BEFORE IT.** Carry-forward item (3) names three binding
  constraints on the funnel. 09-17 (Generac) removed *"the sources are too thin"* by supplying an 8-K.
  **09-21 removes the last remaining hope attached to the FIRST constraint: that a better-sourced deal
  would eventually carry its number.** **Here the number is missing BY DELIBERATE COMMERCIAL CHOICE OF
  BOTH PARTIES, not by a gap in the reporting.** **No better-sourced version of this candidate will
  ever arrive.** **A perfectly-evidenced transaction between two named public companies can still be
  structurally unwritable at part 2, and no evidence standard a human could set would change it.**
  **GM does not become a buy at a different price, and the −3.95% is not the reason.**

- **⚠ STANDING RULE (iii) HAS A NEW COSTUME AND IT IS THE MOST CONVINCING ONE YET: A GENUINE
  TRANSACTION WHOSE *DELIVERY MILESTONE* IS RECYCLED AS THE NEWS.** The Monday scan surfaced GM/Lockheed
  as a **September 21** item. The contract is dated **August 6**, the delivery **August 28**, and the
  first wire coverage **September 17** — **the "news" is a fourth-hand re-report of a five-week-old
  contract.** **Every prior rule (iii) instance was a guidance-issuance alert, a reaffirmation, or a
  re-covered SPA — all of which announce nothing.** **This one announces something real that already
  happened.** **The check that caught it was ONE SCREEN ASKING THE TRANSACTION'S OWN DATES**, not any
  judgment about the mechanism, and it was **the cheaper of the two kills.** **STANDING PRACTICE: ask a
  transaction WHEN IT HAPPENED before asking who it helps.**

- **⚠ STANDING RULE (viii) MUST BE READ MORE BROADLY THAN IT WAS WRITTEN — SECOND FIRING IN THREE
  SESSIONS AND TODAY'S IS THE PURER CASE.** Rule (viii) was created 09-18 off TotalEnergies/GIP, where
  **$1.8B was capital paid IN rather than revenue earned OUT.** **Brookfield/Bloom's $25B is one step
  further from part 2 than that: it is neither revenue nor capital received — it is a FINANCING CEILING
  AVAILABLE TO SOMEBODY ELSE, and it may never be drawn.** Bloom's own **09-16** materials say reported
  revenue *"will depend on projects that are ultimately funded, built and accepted"*; a second research
  note says the figure *"indicates a financing capacity, not firm orders or revenue already secured by
  Bloom."* **Two independent sources pre-emptively warned against the exact misreading part 2 invites —
  the first time the tooling has volunteered that correction on a DOLLAR FIGURE rather than on a
  supplier name, and worth counting as a genuine mitigation.**
  **READ THE RULE AS: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part 2 —
  not merely "capital in".** **A large, real, sourced, prominently-placed number is not a dollar path.**

- **⚠ A CONVERGENCE BETWEEN TWO NAMED COMPANIES IS THE SHARED-CAUSE TRAP TOO, AND IT IS MORE SEDUCTIVE
  THAN A DIVERGENCE. SEVENTH INSTANCE, 09-21, BUNGE.** Bunge raised FY26 adj. EPS **$9.00–9.50 →
  $9.25–9.75** on stronger Q2 crush (Soybean P&R adj. EBIT **+46.4% to $445M**; Softseed **$14M →
  $255M**). The read-across to **ADM** needs an *"and also"* clause: **both are downstream of the same
  crush spread — a market, not a transaction.** **The screen for a named US counterparty with a
  disclosed figure returned NONE**, and the only cross-company line is sector commentary saying ADM and
  Bunge **"earn a spread, not a price."**
  **⚠ THE NEW EDGE: ADM's own raise ($4.15–4.70 → $5.15–5.60, disposed 09-18 as first-order) is cited
  SIDE BY SIDE with Bunge's in today's coverage as evidence of the same margin environment.**
  **09-16's JPM/BAC/WFC finding was that a DIVERGENCE between two named companies sounds causal.
  Today's is that a CONVERGENCE does — and the convergent version is the more dangerous of the two,
  because agreement LOOKS LIKE CORROBORATION when it is in fact the clearest possible statement that
  the input is a market variable.** **Same trap, opposite sign. Neither BG nor ADM becomes a buy.**

- **⚠ OPEN ITEM (1)'s NEAR-MISS SHAPE FIRED A SECOND TIME: THE PRICED-IN FILTER PASSED A CANDIDATE ON A
  3.95% *FALL*, FIVE BASIS POINTS INSIDE THE WIRE.** `move --symbol GM --sessions 5` returned
  **85.59 → 82.21, −3.95%, `priced_in: false`, "passes the priced-in check."** **The verdict is correct
  and the reasoning behind it has nothing to do with this news.** The filter compares the *magnitude* of
  a five-session move against 4%; **GM fell, and cleared only because the fall was 0.05 percentage
  points too small to trip the wire.** **Had GM fallen 4.1% the filter would have returned "LATE — skip"
  on a stock that had gone DOWN.** **After LMT (−3.61%, 09-11), this is the second near-miss** and it
  belongs with the eight logged instances of open item (1). **A pass here is not evidence the filter
  worked.** **No run may reinterpret the filter — that is a human editing §4 or `alpaca.py move`.**

- **⚠ THE GENERAL MILLS HAND-OFF IS DISCHARGED IN WRITING AND RE-ARMED FOR 09-23. CARRIED FOUR TIMES,
  SCREENED ON THE FOURTH RATHER THAN CARRIED SILENTLY.** **GIS has NOT reported.** Q1 FY2027 is
  scheduled for **September 23**; consensus is **$0.72 EPS** (down from **$0.86** a year earlier) on
  **~$4.34B** revenue, and **every figure in circulation is an analyst expectation.** Its only company
  statement is the **September 8 AFFIRMATION of FY2027 adj. EPS guidance $3.00–$3.20** — **an
  affirmation, standing rule (iii)**, the same shape as Centene (09-16) and Southwest (09-18).
  **There is nothing to screen until the 23rd.** **⚠ CARRIED EXPLICITLY TO THE 09-23 PRE-MARKET RUN,
  which is the first run that will have an actual print to work with.** **No other unscreened item
  accumulated across the 09-18 → 09-21 window.**

- **⚠ THE WEEKEND WINDOW PRODUCED ONE NAMED-BOTH-PARTIES TRANSACTION AND ZERO WITH A DISCLOSED FIGURE,
  AND THAT IS A FINDING ABOUT THE WINDOW RATHER THAN A THIN-NEWS EXCUSE.** The second broad scan was
  written specifically to demand a named customer, a named supplier **and** a disclosed value, and to
  exclude *"terms not disclosed"* and bare ceilings. **It returned three items, none eligible:**
  **BEML ↔ NHSRCL** (₹5,400 crore) and **Welspun Enterprises ↔ Ahmedabad Municipal Corp** (₹3,512.4M)
  are **Indian-listed and fail §3 outright** — **and they were the only two items in the entire window
  carrying both named parties AND a disclosed value**; **US Army ↔ Skyeton Inc.** (*"over $10 million"*,
  W58RGZ-26-F-A026) is a **private** North Las Vegas company with **no precise obligated figure.**
  **A screen built to find exactly what part 2 needs found nothing that clears §3.**

- **⚠ WEEK 3 REVIEW WRITTEN (2026-09-18 16:45 ET). THE §1 ANSWER IS NO, AND THE MONDAY RUNS MUST NOT
  READ THE SHORT WINDOWS AS THOUGH IT WERE YES.** The satellite sleeve returned **0.0000%** — zero
  positions in the account's entire history — so its dollar-weighted excess over VOO is exactly
  **minus VOO's total return** over whatever window is chosen: **+0.095pp on the week, +0.430pp
  since inception, +0.509pp over 1M, −2.291pp over 3M, and −16.552pp over the rolling 12 months
  §1 actually names.** **A positive sign on a short window is 0% exposure to a market that fell, and
  it will be positive again on every red week.** The structural cost is **~4.97pp of account return
  per rolling 12 months.** Full working in `weekly_review.md`, "Week ending 2026-09-18".
  - **Counters as of this review: 46 theses, 0 accepted, 46 rejected, 0 positions, 0 exits,
    13 sessions.** All four §5 rules remain **untested code paths**; §5.4 is **not armed.**
  - **Reject board re-measured to today's close: 40 measurements, 13 beat VOO, 27 lagged, mean
    excess −1.57%.** Both legs from `alpaca.py move`, verified this run to match
    `bars --adjustment all` to the cent at all eleven session counts. **It is a tally, not a
    result — do not quote it as one.**
  - **`week_of` advanced to 2026-09-21 and `new_positions_this_week` reset to 0** by this run, which
    is where that reset belongs. Monday's runs will find the anchors match and correctly do nothing.
  - **Monthly archive rollover NOT due** (every *entry* is dated 2026-09; the earlier dates in
    `research_log.md` are cited inside thesis bodies). **Next rollover: 2026-10-02.** ⚠ Second week
    flagging size — `research_log.md` **3,257 lines / 226KB, +75KB this week**; five memory files
    **477KB** total against an instruction to read them in full. **A human may want to move the
    rollover forward.**
  - **⚠ HAND-OFF DISCHARGED 09-21 08:20, ALL THREE ITEMS, AND ALL THREE LANDED AS PREDICTED.**
    **General Mills — SCREENED, not carried silently:** it has **not reported** (due **Sept 23**) and
    its only statement is a **Sept 8 affirmation**, rule (iii); **re-armed for the 09-23 run.**
    **The eighth GNRC framing ARRIVED**, in the predicted shape and refused — see the dedicated note
    above. **No high-water backfill was due, and the run confirmed it by reading the absent stamp
    rather than assuming it.** **Nothing from this hand-off remains open except the 09-23 GIS item.**

- **⚠⚠ THE HEADLINE OF THE 09-18 CLOSE, AND IT OUTRANKS EVERYTHING BELOW IT BECAUSE IT IS THE FIRST
  TIME A KNOWN DEFECT REACHED A NUMBER A RUN ACTUALLY REPORTED: ALPACA'S OWN P&L ARITHMETIC IS
  ANCHORED ON A STALE PRICE, AND THE DAY'S P&L IT HANDS YOU WAS WRONG BY $106 — MORE THAN DOUBLE THE
  REAL MOVE.** `account` returns `equity` **99,627.58** and `last_equity` **99,434.4356**, and the
  subtraction gives **+$193.14 / +0.194%**. **`last_equity` is exactly 99.046311231 × 701.03 +
  30,000** — the **stale midpoint** `lastday_price` carried for all four calls today — **not 09-17's
  official close of 700.97.** `unrealized_intraday_pl` (+193.14 = 99.046311231 × [702.98 − 701.03])
  is built off the same baseline. **The true day P&L, close to close, is +$87.16 / +0.0877%.**
  **Both legs are wrong in the same direction and they reconcile perfectly against each other, so no
  check internal to the broker's fields could ever detect it — only an external close can.**
  **STANDING RULE, AND IT IS NEW: never use `equity − last_equity` as a day's P&L, and never use
  `unrealized_intraday_pl`. Close-to-close from `bars --adjustment all`, always.**
  **Why this entry matters more than the seven instances before it:** those were all filed as
  *cosmetic on core, load-bearing only once a satellite position exists.* **That framing was too
  generous.** This one was load-bearing **with no satellite position involved at all**, in the one
  number the ClickUp summary leads with. **Open item (5) should be re-rated by the human.**
  **And the honest note on how it was caught: NOT vigilance.** The repo already forces closes through
  `bars`, so 701.85 and 700.97 were both in hand and the two answers sat side by side demanding to be
  reconciled. **Absent that standing rule the broker's number would have been quoted without a second
  thought, because it is labelled with exactly the words a close run is looking for.**
  *(Also today: `current_price` **702.98** against the **701.85** close — **$1.13 apart, the widest
  gap this log has recorded**, and precisely the amount a `highest_close` would have been overstated
  by had there been one to write.)*

- **⚠ DISCHARGED 09-21 09:36 BY READING, NOT BY ASSUMING — NO HIGH-WATER BACKFILL WAS DUE AND THE
  MISSING STAMP IS NOT EVIDENCE OF A FAILED CLOSE RUN. WRITTEN 09-18 16:15 BECAUSE THE TWO ARE INDISTINGUISHABLE FROM THE FILE ALONE.** The
  09-18 close run **executed Step 2 and Step 2 had no operand**: zero open satellite positions means
  zero `highest_close` fields to raise **and zero `(as of …)` stamps to advance.** Routine 4 requires
  the date to be refreshed **whether or not the value moves**, precisely so that *stale* and
  *current-and-unchanged* stop being indistinguishable — **but neither state applies here. The marks
  are ABSENT, a third state, and an absent field carries no date to refresh.** The midday run's
  backfill trigger compares a stamp against the last trading day; **it will find no stamp on Monday,
  exactly as it found none today, and that is the absence of a MARK.** **Nothing was skipped.**

- **⚠ THE HEADLINE OF 09-18, AND IT REPLACES 09-17's: THREE SEPARATE NAMED-BOTH-PARTIES TRANSACTIONS
  ARRIVED IN ONE WINDOW AND EVERY ONE OF THEM WITHHELD THE NUMBER. THE FUNNEL'S FIRST FAILURE SHAPE
  HAS NOW FIRED IN TRIPLICATE, WHICH IS A CLUSTER, NOT THREE COINCIDENCES.** **(a) GlobalFoundries ↔
  Marvell** — expanded multi-year SiGe capacity agreement at Burlington VT for NPO/CPO optical
  connectivity (**GF press release 09-17, Reuters 09-17**): **no dollar value, no wafer volume, no
  quantified capacity increase**, and one commentary states flatly *"financial terms were not
  disclosed."* **(b) Centrus ↔ Antares Nuclear** — multi-year HALEU supply contract with prepayments
  (**09-17**): **"financial terms were not disclosed,"** no volume, **Antares not publicly traded.**
  **(c) TotalEnergies ↔ GIP** — African oil and gas infrastructure partnership, **US$1.8B capital
  contribution** (**Business Wire 09-18**): a figure exists, **but it is capital going IN, not revenue
  coming OUT.** **Part 2 could not be written for any of the three.** **Why this is the entry worth
  keeping:** carry-forward item (3) names three distinct binding constraints on the funnel, and
  09-15/09-16/09-17 each demonstrated a *different* one on a *different* day. **09-18 is the first day
  a single constraint accounted for the entire output.** **Recognise the cluster on sight rather than
  re-deriving it deal by deal** — the same lesson 09-17 recorded for the MarketBeat guidance-issuance
  alerts and 09-16 for the federal ceiling awards.

- **⚠ NEW STANDING RULE (viii), WRITTEN 09-18: *READ WHICH DIRECTION THE DISCLOSED DOLLAR FIGURE
  MOVES BEFORE TREATING IT AS A DOLLAR PATH.*** TotalEnergies/GIP's **$1.8B is a capital
  contribution — money GIP pays in, not revenue it earns.** It is large, real, sourced and primary,
  and it **satisfies none of part 2**, which asks for a **segment revenue** figure at Company B.
  **A figure's presence is not the same as the figure part 2 asks for.** This is the **mirror image of
  09-17's Fluence finding**, where a precisely quantified **loss** invited the assumption that the
  money went somewhere nameable. **Both traps work by supplying a number that feels like it discharges
  part 2 and does not.** T-2026-09-18-04 (BLK) is the worked example: **part 1 passed cleanly in one
  clause** and the thesis still died, **and it died on the absent segment figure, NOT on size** — a
  future run must not re-record it as a size rejection, because the size arithmetic was never the
  ground.

- **⚠ GNRC REFUSED A FOURTH CONSECUTIVE TIME, AND 09-18's VERSION OF THE PULL IS THE STRONGEST AND THE
  EMPTIEST — WHICH IS EXACTLY WHY IT IS THE ONE WORTH RECORDING.** Today was the first run whose
  `bars` history **contained** the 09-16 after-hours gap (**reported +29.9% on the 09-17 session**), so
  `move --symbol GNRC --sessions 5` would finally have returned a large positive number and
  `priced_in: true`. **That reading would not measure open item (7). It would be the filter working
  correctly one session late.** The defect — the one-session blind window between an after-hours event
  and the next official close — **was already measured on 09-17** (186.55 → 175.19, **−6.09%**,
  `priced_in: true`, on the morning after the surge). **There is no number left to collect, and
  "completeness" is just the newest wrapper.** **Zero `move`/`quote`/`bars`/`asset` calls, four runs
  running.** **The costumes so far: diligence (09-17 09:35), curiosity (09-17 12:35), tidiness
  (09-17 16:16), completeness (09-18 08:16). Expect a fifth. The pattern is the finding, not any
  single instance.**
  **⚠ FIFTH REFUSAL, 09-18 09:36 — AND THE PREDICTED FIFTH COSTUME ARRIVED AS PREDICTED AND WAS THE
  CHEAPEST ONE YET.** The execution run's available excuse was *"I am at the open with the data plane
  already in hand, one more symbol costs nothing"* — **the first version that would have been FREE
  rather than merely justifiable.** Refused; **zero `move`/`quote`/`bars`/`asset` calls, five runs
  running.** **Note the direction of travel: the excuses are getting BETTER, not worse.** GNRC is
  the named counterparty in the Amazon announcement — **first-order, outside §4 at any price** — and
  it was not in the plan, which is the only fact that has ever mattered here. **Expect a sixth.**
  **⚠ SIXTH REFUSAL, 09-18 12:34 — THE PREDICTED SIXTH ARRIVED AND IT IS THE NARROWEST AND MOST
  PLAUSIBLE OF THE SET.** The version available to an **exits-only** run is: *"I am the run that
  manages positions; checking whether the thing I refused to buy has moved is just measuring the cost
  of the refusal."* **That is not even a trade rationale — it is a SELF-AUDIT, which is precisely what
  makes it the strongest of the six**, because it proposes a number the log would arguably be better
  for having. Refused; **zero `move`/`quote`/`bars`/`asset` calls, six runs running.** **The
  disqualifying fact is structural and does not depend on the excuse: routine 3 may not open a
  position under ANY circumstance, so there is no version of looking at GNRC that could produce an
  action.** **The costumes so far: diligence (09-17 09:35), curiosity (09-17 12:35), tidiness
  (09-17 16:16), completeness (09-18 08:16), zero-marginal-cost (09-18 09:36), self-audit
  (09-18 12:34). Expect a seventh — and note that the sequence has now run through an entire trading
  day's worth of seats without repeating itself.**
  **⚠ SEVENTH REFUSAL, 09-18 16:15 — AND THE SEVENTH COSTUME IS THE FIRST ONE THAT BORROWS SOMEONE
  ELSE'S AUTHORITY RATHER THAN CLAIMING ITS OWN.** The version available to a **Friday close run
  already holding `bars`** is: *"the weekly review runs in an hour and will want the number —
  collecting it is procurement for a downstream consumer, not a trade decision of mine."* **It is the
  first excuse that does not claim the number for itself**, which is exactly what makes it the
  easiest to say yes to. **Refused**, on a fact that does not depend on the wording: the weekly review
  measures **positions held** against VOO, **GNRC is not held and never was**, so the review has **no
  row to put it in** — collecting it would be **the same fabrication as stamping core, one file
  over.** Zero `move`/`quote`/`bars`/`asset` calls, **seven runs running.** **The costumes:
  diligence, curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement —
  seven seats, seven distinct rationales, no repeats.** **The honest reading is NOT that resistance is
  improving; it is that the supply of plausible framings is not running out.** **Expect an eighth on
  Monday morning.**

- **⚠ `lastday_price` READ 701.03 WHILE THE OFFICIAL 09-17 CLOSE WAS 700.97 — SIX CENTS, AND THIS IS
  THE SHARPEST INSTANCE OF THE TWO-PRICE DEFECT THE LOG WILL GET.** Every prior instance involved
  `current_price`, a field nobody would mistake for a close. **This one is a field literally named for
  the prior day and it still is not that day's close** — it is a live midpoint carried over. **Fifth
  documented instance.** Cosmetic on core; **load-bearing the moment a satellite position exists**,
  because a `highest_close` read from it silently moves the §5.4 stop. **`bars --adjustment all` for a
  close, a fresh `quote` for execution, never a `positions` field for either — and the field's NAME is
  not evidence about what it holds.**
  **⚠ SIXTH INSTANCE 09-18 09:36, AND IT CARRIES A NEW SUB-SHAPE THAT IS WORTH MORE THAN THE COUNT.**
  `lastday_price` **read 701.03 again** — **the same six cents off 09-17's official 700.97**, so the
  field corrected itself **neither overnight nor at the bell**. And this time **`current_price` read
  701.03 too, with `change_today` EXACTLY 0, six minutes into a LIVE session.** **That flat is an
  ARTIFACT of both fields carrying the same stale midpoint, not a measurement that VOO is unchanged.**
  **A run that read `change_today` as the day's move here would have read ZERO on a moving tape** —
  and unlike the close-vs-midpoint error, this one produces a number that looks *deliberate* rather
  than merely imprecise. **Add `change_today` to the list of `positions` fields that are not what
  their names say.**
  **⚠ SEVENTH INSTANCE 09-18 12:34, AND THE 09:36 SUB-SHAPE DID NOT SURVIVE TO MIDDAY — WHICH IS THE
  FINDING, NOT A CORRECTION TO IT.** `lastday_price` read **701.03 for the THIRD consecutive call
  today**, still six cents off 09-17's official **700.97**, so the field has now failed to correct
  itself **pre-market, at the bell, AND three hours into the session** — it is not a settling-in
  artifact. But `current_price` has **unstuck**: **699.59** against 09:36's 701.03, with
  `change_today` **−0.00205**, which is **exactly 701.03 → 699.59**. **So the two fields are now
  internally consistent with each other and still wrong about the prior close**, because
  `change_today` is computed off `lastday_price` rather than off the official close. **The 09:36 flat
  was a STALE midpoint; this is a LIVE midpoint measured against a STALE BASELINE.** One defect, **two
  different appearances inside one session**, and the midday one is the more dangerous of the pair:
  it moves plausibly, reconciles against its own siblings, and is simply **anchored six cents wrong**.
  **A consistency check between `positions` fields cannot detect it. Only an external close can.**

- **⚠ A CLOSE RUN SILENTLY DELETED A PRIOR DAY'S JOURNAL HEADER, NOTHING CAUGHT IT FOR A DAY, AND
  THE EDIT THAT DID IT IS THE EDIT EVERY CLOSE RUN MAKES. THIS IS THE HEADLINE OF 09-17's CLOSE
  AND IT IS A MEMORY-INTEGRITY FINDING, NOT A FORMATTING ONE.** Commit **`5fe9e4c`** (the **09-16
  close run**) inserted its entry at the top of `journal.md` and in the same commit **deleted the
  line `### 2026-09-15 (Tuesday)` — its ONLY deletion.** The 09-15 body survived intact but was
  left **headerless and glued onto the end of 09-16's "For the next run" list**, so a full trading
  day's judgment became **invisible to any scan of the file's headers and reads as part of the
  following day.** **RESTORED 09-17** with an inline note naming the commit; the body was not
  touched; **all thirteen September sessions verified to carry exactly one `###` header each**
  (09-01/02/03/04, the 09-07 holiday entry, 09-08/09/10/11, 09-14/15/16/17). **Why it matters more
  than it looks:** the loss was **silent and looked like nothing was wrong** — right byte count,
  right month, no visible gap read linearly — which is **the same failure shape the high-water
  discipline exists to prevent**, arriving in the one file nobody thought to check it in. **It was
  found by accident** (listing headers to locate the template) and **nothing flagged it; nothing
  could** — `commit.py` guards `strategy.md` and `control.md`, not the shape of an append-only
  file. **THE HAZARD IS STRUCTURAL: the top-of-`## Entries` insert is the dangerous edit in this
  repo, it sits immediately above the previous day's header, and it looks completely routine while
  you are making it.** Today's run was **one edit away from repeating it** and the defence that
  worked was **anchoring on `## Entries` PLUS the existing top header and putting both back
  verbatim**, rather than replacing a block that happens to start there. **STANDING CHECK, CHEAP
  AND MANDATORY: after writing the journal, list the `###` headers and confirm one per trading day
  since the last archive rollover.** One command. It is the only thing that would have caught this.

- **⚠ THE UNDEREXPOSURE ARITHMETIC HAS NOW BEEN DEMONSTRATED IN BOTH SIGNS, ONE SESSION APART, AND
  THE PREDICTION WAS MADE BEFORE THE FACT.** 09-16: the book fell **0.308%** against VOO's
  **0.442%** — 13bp of apparent **OUT**performance, written up as **69.59% exposure × the index
  move and nothing else**, with the explicit prediction that it "reverses with the same mechanical
  reliability on the first green day." **09-17 IS THAT GREEN DAY AND IT REVERSED.** VOO **+1.1187%**
  (693.215 → 700.97), book **+0.779%**, i.e. **34bp of UNDERperformance**, and **0.6959 × 1.1187% =
  0.7785%** reproduces it to a rounding tick. **Same mechanism, opposite sign, one session apart —
  the cleanest available proof that neither number was ever skill.** **Do not let either answer
  §1's twelve-month question**, and note the asymmetry in how they feel: the favourable one is
  harder to discard, which is exactly why it was written down first.
  **⚠ THIRD CONSECUTIVE SESSION, 09-18, AND IT NOW REPRODUCES ON THE WEEK AS WELL AS THE DAY.** VOO
  **+0.1255%** (700.97 → 701.85), book **+0.0877%** (99,428.49 → 99,515.65), and **0.6989 × 0.1255 =
  0.0877** to the tick — **3.8bp of UNDERperformance on a green day**, the same sign 09-17 produced
  and predicted. On the **week**: VOO **−0.095%** (702.52 → 701.85), book **−0.067%**, i.e. **2.9bp
  of apparent OUTperformance that is just 30% cash in a down week.** **Three sessions, both signs,
  and now a weekly aggregate — the exposure fraction accounts for all of it, and none of it is
  skill in either direction.**

- **⚠ THE FUNNEL RECEIVED ITS BEST-EVER INPUT ON 09-17 AND STILL PRODUCED NOTHING — AND THE REASON IS
  A THIRD DISTINCT SHAPE, NOT A VARIANT OF THE OTHER TWO. THIS IS THE HEADLINE OF 09-17 AND IT
  REPLACES THE 09-16 HEADLINE.** The **Amazon ↔ Generac** long-term generator supply agreement
  (**8-K filed 2026-09-16**: **~$2.4B of initial deliveries expected 2027–2028**, aggregate payments
  **up to $8B**, warrant to Amazon.com NV Investment Holdings for **1,693,745 GNRC shares at
  $200.9266**, **307,954 vested immediately**, exercisable through **September 2033**) is the
  **best-sourced transaction this log has ever processed**: both parties named, the figure in a
  filing, the date unambiguous, **and rule (iii) PASSED — no prior disclosure, which is why an 8-K
  was used at all.** **Neither known failure mode fired.** It died because **the supply chain behind
  the named beneficiary is INTERNAL**: sources describe Generac as operating *"a vertically
  integrated business model, producing core components, including engines, alternators, batteries,
  electronic controls, and steel enclosures."* **There is no Company B to find because Generac makes
  the parts.** **Record this as a THIRD shape.** The first two are failures of *disclosure* that a
  human could address by widening the evidence bar; **this one is a fact about the company that no
  evidence standard would change.** **The lesson is uncomfortable and should not be softened: a
  perfectly-sourced transaction is NECESSARY AND NOWHERE NEAR SUFFICIENT.** The supply chain must be
  **external and public** before §4 has anything to work with, and nothing in the funnel screens for
  that before the research is spent.

- **⚠ NEW OPEN ITEM (7), FOUND 09-17 AND THE MOST DANGEROUS DEFECT THIS LOG HAS FOUND: `alpaca.py
  move` IS STRUCTURALLY BLIND TO AN AFTER-HOURS EVENT, AND THE 09:35 RE-VALIDATION INHERITS THE SAME
  BLINDNESS.** `move --symbol GNRC --sessions 5` returned **186.55 → 175.19, −6.09%, `priced_in:
  true`, "LATE - skip"** on the morning after GNRC reportedly **surged after the bell** on this very
  announcement (**reports range +18% to over +40%; NONE is verifiable from our data plane**). `bars`
  confirms the last official close is **175.19 (09-16)**; `quote` shows the last print **175.19 at
  15:59:57 ET**, a stale 16:00:05 bid of **165.23**, and **no ask at all.** **The five-session window
  ends at the last official close, so when news breaks AFTER the close the filter evaluates a price
  history that PREDATES the news** — and the gap does not enter `bars` until that day's close prints,
  so **a 09:35 re-validation would pass such a candidate for the same wrong reason.** **This is the
  inverse of open item (2) and materially worse than open item (1): the drawdown defect causes MISSED
  trades, this one would cause a trade TAKEN at exactly the price the filter exists to refuse.**
  **Cost on 09-17: ZERO** — no BUY intents existed and GNRC is the named counterparty, i.e.
  first-order and outside §4 at any price. **No run may reinterpret the filter — that is a human
  editing §4 or `alpaca.py move`.**

- **⚠ THE "I KNOW WHO MAKES THE PART" TRAP ARRIVED A THIRD TIME ON 09-17, AND THE TOOL CAUGHT IT
  BEFORE I DID.** The Generac supplier screen volunteered, unprompted, that Cummins, Caterpillar or a
  US switchgear maker supplying Generac is **"a general industry possibility, but no retrieved source
  actually names them."** **That is T-2026-09-01-03 (RTX) and the 09-16 Abrams/Honeywell screen
  repeating a third time.** **No US-listed Generac supplier was screened and no filters were run on
  one — absence of a source, not a verdict on any name.** **The only named supplier anywhere is
  Weichai Power via Baudouin, listed in Shenzhen (002338) and Hong Kong (02338) — §3 excludes it
  outright, and no source attaches a dollar figure to its Generac sales in any case.**
  **Knowing who plausibly makes the part is still not knowing who was paid.**
  **⚠ FOURTH INSTANCE 09-18, AND THE TOOL CAUGHT IT FIRST AGAIN — TWICE IN ONE RUN.** The Centrus
  screen volunteered that vacuum systems, compressors, valves and control-system vendors are
  **"general industry possibilities and are not tied to Centrus's Piketon facility by the cited
  sources,"** and the GF/Marvell screen said mapping optics vendors to that deal **"would be
  speculative."** **No US-listed supplier was screened for either deal, and no filters were run on
  one — absence of a source, not a verdict on any name.** **That the tool now flags this before I
  reach for it, on consecutive days, is worth noting as a genuine mitigation — and it is not one the
  system owns, because it depends on how the question happens to be phrased.**

- **⚠ RULE (v)'s CEILING SUB-SHAPE IS ONE DAY OLD AND IS ALREADY THE DEFAULT FORM IN WHICH FEDERAL
  DOLLARS ARRIVE.** Written 09-16 off the Abrams OTA (**$2.5B ceiling vs $11.8M obligated — 212×**);
  on **09-17 six of seven federal awards in one morning were ceilings or "up to" amounts**: CACI
  **$1.5B ceiling** (company *expects to book* **$1.2B** — its own estimate, not a contract term),
  S&K Aerospace **$4.3B IDIQ**, Amentum **$150M ceiling** (completion **September 2031**), DCS
  **$85M**, AEVEX **up to $92.2M**, Conti Kight JV **$74.9M**, Kyndryl **no value at all**.
  **$6.3B of headline value and not one identifiable Company B.** **Read the obligated or
  expected-booked figure, never the ceiling** — and **recognise the cluster on sight rather than
  re-deriving it award by award.**

- **⚠ STANDING RULE (vi) DISCHARGED ONE DAY AFTER IT WAS WRITTEN, AND LONG-DATED LNG IS A RECURRING
  FEATURE OF THIS FUNNEL, NOT A VISITOR.** Rule (vi) was created 09-15 by **Sempra ↔ Petrobras**
  (20-year, 0.8 Mtpa, Port Arthur Phase 2, COD 2030–2031). **09-16 produced Venture Global ↔ China
  Gas: 20-year, 0.5 Mtpa, deliveries starting 2030** — same instrument, same industry, same tenor,
  same decade of first delivery, **different seller and different buyer.** The rule worked exactly as
  designed: **timing screened first, candidate dead in one step, and no Perplexity call spent hunting
  a Company B that could not have qualified.** **Part 3 kills these faster than part 1 does, and that
  rejection SURVIVES a supplier being named later, which part 1's does not.** *(Sempra/Petrobras also
  resurfaced in today's scan as fresh-looking commentary. **It is the same agreement being re-covered
  — re-coverage is not a new event.** Standing rule (iii).)*

- **⚠ THE FOMC HAPPENED AND IT IS NOW IN THE PAST TENSE: +25bp TO 3.75%–4.00%, UNANIMOUS 12–0, THE
  FIRST US HIKE SINCE 2023, WITH ANOTHER SIGNALLED FOR THIS YEAR.** Chair **Kevin Warsh**'s first.
  **The 09-14 note flagged one source at ~87% odds of an *increase* as contradicting every other
  framing and deliberately did not chase it. It was not an outlier; it was early** — the record now
  shows which way the unresolved item resolved. **The close run VERIFIED the decision rather than
  inheriting the plan's ">90% odds": a probability is not a fact, and the distinction cost nothing on
  a day it resolved the expected way.** **The tape: VOO closed 693.215 from 696.29, −0.442%, on an
  intraday range of 689.095–699.99 — about 1.58% of the low against 0.53% Tuesday and 0.68% Monday,
  on higher volume, the low 1.03% below the prior close and the last hour taking back about six
  tenths of it.** **That is the whole of the day's new price information and it carried NO ACTION:**
  no satellite thesis existed for it to invalidate, and **§5 exempts core from all four sell rules.**
  **IT IS NOW AN INPUT TO THE ENVIRONMENT, NOT A COMPANY A.** The 09-17 pre-market run must enter any
  rate-driven candidate through §4 like any other event — a transaction, a segment, a dollar path, an
  invalidation condition — and **"the Fed hiked" supplies none of them.** August CPI (headline
  **+3.4% y/y**; core **+0.3% m/m**) was the input, never a candidate. **The honest version of the
  close run's non-reaction: the pull to reverse-engineer a Company A out of a hike, a wide range and a
  heavy tape was weaker than expected — but the reason it got nowhere is that ROUTINE 4 MAY NOT
  RESEARCH, not that the temptation was proven to fail on its merits. The pre-market run is where
  that gets tested.**

- **⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED AN EIGHTH TIME ON 09-17 AND AGAIN COST NOTHING — BUT THIS
  ONE BELONGS TO OPEN ITEM (7), NOT (1), AND MERGING THEM LOSES THE FINDING.** Instances of open item
  (1): **LITE −7.35%, LMT −3.61% near-miss, LHX −4.47%, CART −5.79%, BWXT −6.30%, CRWV −7.12%, AVGO
  −7.97%.** **GNRC −6.09% (09-17) reads identically and is NOT the same defect** — the drawdown is an
  artifact of the window ending at the **last official close, before an after-hours event the feed
  cannot see at all.** **Keep it filed under (7).** **The expensive instances are the ones that reach
  the filter ALIVE, and LITE is still the only one** — it passed the four-part thesis, was killed by
  a drawdown, and is **+10.58% vs VOO** since. **A review that counts eight instances as eight costs
  will overstate the case for a change that is not the agent's to make.**

- **⚠ SEVEN ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) **The §4 priced-in filter
  reads a drawdown as priced-in** — **seven** instances, see above; **there is no price at which
  those rejections flip**, and LITE puts **+10.58% vs VOO** on the bill. (2) **The same filter reads
  an event move absorbed before it looks as "passes"** — QCOM (09-09, +2.70% after a +8.7% intraday
  move) and AVAV (09-11, +1.20% after a +12.9% intraday round-trip inside one session). Same root
  cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or `alpaca.py move`.**
  (3) The satellite sleeve is **structurally undeployed — FORTY-TWO theses, zero positions,
  nineteen sessions**; a 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a
  rising market. **§2 permits the cash and §4 says most runs end in no trade — both rules were
  followed, and the agent must NOT respond by lowering the §4 bar.** **The binding constraint is now
  known to have THREE forms, not two** (see the headline note above): the source withholds the
  counterparty's number; **or** the counterparty is named, does disclose, and discloses **roadmap
  instead of segment revenue**; **or** — new on 09-17 — **the named beneficiary is VERTICALLY
  INTEGRATED and there is no external supplier to find.** **09-15 removed the "thin news week"
  explanation; 09-16 removed the "no named counterparty" explanation; 09-17 removes the "the sources
  are too thin" explanation, because the sources could not have been better.** **Only the first two
  forms are addressable by widening the evidence bar. The third is not addressable at all** — which
  narrows what a human could usefully change, and is the single most decision-relevant line in this
  file. (4) The
  core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the prior close),
  **not tracking error and never skill** — **DISCHARGED AND PROVEN 09-11: measured from the fill,
  tracking error 0.0000%. Keep measuring it from the fill.** (5) The broker/official price gap is a
  **live quote midpoint**, not an offset — cosmetic on core, **load-bearing the moment a satellite
  position exists**; whether the tooling should read closes from `bars` by default is a human's call.
  (6) **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed
  all five checks on 09-11 while `clock` was 500 and `quote`/`bars` were 504. **Every routine's Step
  0 is the loud-failure mechanism for exactly this, and on the data plane it is silent.** Until a
  human changes it: **probe by hand and never infer data-plane health from a green selftest.**
  **(7) NEW 09-17 — `alpaca.py move` cannot see an after-hours event**, and neither can the 09:35
  re-validation that exists to catch exactly this. See the dedicated note above. **Unlike (1) and
  (2), this one fails in the direction of TAKING a trade rather than skipping one**, which is why it
  is listed last and should be read first. **The 09:35 run confirms the inheritance is real and NOT
  contained: it cost zero only because there were no BUY intents, i.e. the defect was never handed a
  subject. That is an absence of exposure, not a mitigation, and it disappears on the first morning
  the plan carries a BUY intent on a name whose news broke after the prior close.** Prior context in ClickUp `86bbv75bz`, last week's in
  `86bbzgbg3`.

- **⚠ FOURTEEN ITEMS WERE DROPPED BEFORE THESIS STAGE ON 09-18 AND EACH HAS A NAMED REASON — THEIR
  ABSENCE FROM THE THESIS IDS IS NOT AN OVERSIGHT.** **Fluence's FY26 cut** resurfaced with old/new
  figures ($3.0B → ~$2.4B revenue midpoint; −$10M → −$200M adj. EBITDA) — **the same cut processed
  09-17 as T-2026-09-17-02**, re-covered, rule (iii). **ADM** raised 2026 adj. EPS **$4.15–4.70 →
  $5.15–5.60** — a genuine change, **first-order, no counterparty named**. **UnitedHealth** raised 2026
  adj. EPS to **$19.50–20.00** with **no prior figure stated**. **Philip Morris** — the **currency-only**
  raise, disposed 09-17. **Labcorp ($18.10–18.55 EPS, $14.7–14.8B revenue), Nucor (Q3 $5.55–5.65) and
  Steel Dynamics (Q3 $5.34–5.38)** — all **guidance-ISSUANCE alerts compared to CONSENSUS, never to a
  prior company figure**: **the General Mills trap for the fourth, fifth and sixth time this week**,
  rule (iii). *(Nucor's coverage carried two irreconcilable ranges, **$5.55–5.65 and $3.30–3.60**, in
  the same scan — **a secondary aggregator can be internally inconsistent inside one morning**, which
  is a new and cheap reason to distrust one.)* **Lockheed Martin ↔ Pentagon AIM-260 JATM production
  framework (09-17)** — **the awarded party, no dollar figure at all, no supplier named**: rule (i)
  plus the rule (v) ceiling shape **with the ceiling left blank**. **Vicor** — licensing deal with an
  **unnamed OEM** plus its own NH fab expansion; **no counterparty exists to screen**. **Southwest**
  *reiterated* Q3 EPS. **Myriad Genetics** cut FY26 guidance with **no figures in any retrieved
  source**. **Emera** is Canadian-listed (§3). **Aeluma** explicitly declines to guide.
  **Aethlon/North Immunology** and an **SEC tokenized-stock "innovation exemption"** — **the source
  itself called its own evidence too thin**, which is worth noting as the rare case where the tool
  refuses before the filter has to. **First Breach ↔ SAS Ammo** (three-year ammunition supply, both
  named) and **Oribiotech ↔ an unnamed biopharma** (10-year, up to $120M) — **private counterparties**,
  and the second **does not name its buyer at all**.

- **⚠ ELEVEN ITEMS WERE DROPPED BEFORE THESIS STAGE ON 09-17 AND EACH HAS A NAMED REASON — THEIR
  ABSENCE FROM THE THESIS IDS IS NOT AN OVERSIGHT.** **Ford raised FY26 adj. EBIT guidance to
  $10–11B (+$1B at midpoint)**, adj. FCF $6–7B, capex unchanged $9.5–10.5B, **$500M in 2026 of the
  $1.3B IRA reimbursement booked in Q1** — **first-order, Company A**; no supplier or customer named
  with a figure, drivers quoted as *"strong pricing and mix."* **Lululemon** (FY26 revenue to
  $10.35–10.5B, EPS $9.48–9.73) and **Norwegian Cruise Line** (FY26 adj. EPS ~$1.50, adj. EBITDA
  ~$2.5B) — **consolidated guidance cuts with NO counterparty named at all.** **Philip Morris raised
  FY26 diluted EPS "for currency only"** — a translation adjustment, not an operational change.
  **Ameren $5.25–5.45, Five Below $9.830–10.310, DaVita $14.10–15.20 — ALL THREE arrived as
  MarketBeat/analyst instant-alerts stating guidance ISSUANCE, with no prior figure to compare and no
  source saying anything CHANGED. This is the General Mills trap of 09-16 repeating THREE TIMES IN
  ONE MORNING** — rule (iii). **Subaru ↔ onsemi** — killed by its own press release: *"does not
  represent a supply agreement or production commitment. No financial terms were disclosed."*
  **Charter/Cox $34.5B — CLOSED IN LATE AUGUST**; the 09-17 item is a branding-integration story,
  rule (iii). **Union Pacific/Norfolk Southern** — *"more than 500 customers back the combination,"*
  a support statement with no figure. **Illinois American Water bought the City of Venice wastewater
  system for $770,000** — correctly sourced, both parties named, and **immaterial by four orders of
  magnitude**; a real transaction can still be too small to be an event. **Medtronic LigaSure/Hugo**
  — **the same item dropped on 09-16**, already a disposed reject. **Robinson Pharma's Bausch + Lomb
  supplier award and Powerus in Falcon Peak 26.2** — named beneficiaries, **no money attached**,
  both private.

- **⚠ THE HAND-OFF WAS DISCHARGED IN WRITING ON 09-18 AND RE-ARMED WITH ONE ITEM. NOTHING ELSE IS
  PENDING, AND NOTHING CAN PILE UP BETWEEN PRE-MARKET RUNS.** No unscreened item has accumulated
  across 09-14 through 09-18. **Neither the open run nor the close run screens earnings**, so the only
  hand-off channel is pre-market run to pre-market run, plus the Friday review. **09-18's earnings
  screen found two genuine guidance changes in the 09-17/18 window — ADM (raise, $4.15–4.70 →
  $5.15–5.60) and Fluence (the SAME cut already processed 09-17, i.e. re-coverage, not a second
  event) — plus three MarketBeat/PR guidance-ISSUANCE items that are not events at all** (Labcorp,
  Nucor, Steel Dynamics). **⚠ CARRIED AGAIN: General Mills still has not reported (~Sept 23). It has
  now been carried across two pre-market runs; the 09-21 run must check whether it has reported and
  either screen it or carry it a third time — an item carried silently is indistinguishable from one
  forgotten.** **TODAY IS FRIDAY: the weekly review runs after the close and owes the 09-21
  pre-market run a written hand-off.** **Keep the Friday review writing it and keep the next
  pre-market run discharging it in writing.**

- **⚠ A CLOSE RUN ALWAYS READS `is_open: false`, AND SO DOES A PRE-MARKET RUN — THE BOOLEAN IS USELESS
  IN BOTH DIRECTIONS AND `next_open` IS WHAT DISCRIMINATES. TODAY SUPPLIED ALL THREE SHAPES IN ONE
  SESSION, WHICH IS THE CLEANEST DEMONSTRATION THIS LOG WILL GET.** At **08:17:11** `clock` returned
  **`is_open: false`, `next_open` TODAY** — pre-market. At **09:35:47** it returned **`is_open: true`,
  `next_close: 2026-09-16T16:00` TODAY, `next_open: 2026-09-17T09:30` TOMORROW** — in session, and the
  **only one of the three where the boolean alone is informative.** At **16:16:10** it read
  **`is_open: false`, `next_open` 2026-09-17 — TOMORROW** — post-bell, **confirmed, not predicted**.
  **Two of the three share one boolean and differ only in the `next_open` DATE.** Yesterday at
  **16:16:02** the same boolean meant *the bell rang sixteen minutes ago*, with `next_open` reading
  **tomorrow**.
  **Routine 1's holiday branch and Routine 4's holiday branch both trigger on exactly the flag their
  run always sees.** A run that pattern-matches the boolean skips a day that did happen and leaves a
  record **indistinguishable from a genuine holiday.** **Read the next_open DATE, not the boolean.**
  **The first real holiday will arrive without warning.**

- **⚠ ROUTINE 3's STEP 2 IS THE ONE STEP IN THE SYSTEM WRITTEN TO CATCH A SILENT FAILURE, AND ON
  09-18 IT STAYED SILENT FOR A REASON THAT IS NOT A CLEAN BILL OF HEALTH. WRITTEN 09-18 12:34 AND IT
  IS THE MOST DECISION-RELEVANT LINE THIS MIDDAY RUN PRODUCED.** Step 2 exists because a missed close
  run leaves `highest_close` stale while **every field still reads present and plausible** — the §5.4
  trailing stop is then **silently disabled**. Its trigger is a comparison between the `(as of ...)`
  stamp and the last trading day. **This run could not perform that comparison, because there is no
  `highest_close` to carry a stamp.** The marks are **ABSENT — a third state, distinct from "current"
  and from "stale"** — and **an absent field carries no date, which is exactly what tells the midday
  run no backfill is due.** **Zero `bars` calls were issued for a high-water purpose, and none was
  due.** **Record the distinction precisely, because the two outcomes are indistinguishable in the run
  output: "the marks checked out" and "there are no marks" both produce a midday run with no backfill
  and no exit.** The first is the machinery working; **the second is the machinery having nothing to
  work on, and it is what has happened on every run of this account so far.** The day a satellite
  position exists **and** a close run is missed **or** the data plane is down at 16:00 is the day this
  step earns its place — and it will be the first day the comparison has operands.

- **⚠ ALL FOUR §5 SELL RULES REMAIN UNTESTED CODE PATHS, AND §5.4 IS STILL NOT ARMED.** Nothing has
  ever closed in this account, so §5.1–§5.4 have never been evaluated against a real subject.
  **Nineteen sessions of "no exits" recorded the absence of a subject, not nineteen clean bills of
  health.** **The high-water marks are ABSENT, not stale — a third state, distinct from "current and
  unchanged."** An absent field carries **no date**, and **that absence of a date is what tells the
  midday run no backfill is due** — the trigger cannot fire, and no `bars` call is due for a
  high-water purpose. **Core VOO is deliberately never stamped** — doing so would fabricate a §5.4
  stop on the one position §5 exempts. **§5.4 arms on the first *satellite* fill.** **Today's
  pre-market run adds the §5.1 version of the point: it issued ZERO Perplexity invalidation queries
  and that was correct** — §5.1 reads an `invalidation` line that does not exist, so it is **an
  absent check, not a skipped one**, and a run that manufactured the call would be inventing a
  subject. **The 09-15 close run's version is the sharpest and still stands:** Step 2 is written in
  the imperative and its subject does not exist, so the pull is to satisfy the sentence by stamping
  the one close available — core VOO's. **That would FABRICATE a §5.4 trailing stop on the one
  position §5 exempts from all four sell rules. It was recognised and refused. It will not feel like
  a violation when a future run does it; it will feel like tidiness.** **The failure this machinery
  exists to catch is still ahead of us** — the day a satellite position exists and a close run is
  missed *or* the data plane is down at 16:00, the mark goes stale while every field still reads
  present and plausible. **09-16's close run adds the sharpest instance yet, because the pull arrived
  with an accomplice: this run had ALREADY pulled VOO bars to price the book, so core's 693.215
  official close was sitting in its terminal output with nothing to do.** **Having the number in hand
  is not a reason to write it into a ledger that has no row for it. Refused — and note that next time
  the number will already be on screen again.**

- **⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE THE SAME ZERO ORDERS AND ARE NOT
  THE SAME RUN. DISCHARGED AGAIN 09-17 09:35 AND DUE AGAIN AT THE NEXT OPEN.** The gate was
  **evaluated against today's ET date and did not fire** — `plan_date: 2026-09-17` **matched**, so the
  plan was **FRESH**, and its zero intents are **the plan rather than a gap in it**. The open run read
  the **date, not the outcome**; the difference is invisible in the order count, and both readings
  would have produced the same empty run. **Zero `alpaca.py move` re-validation calls were issued and
  none was due** — re-validation has a subject only when a BUY intent exists: **an absent check, not a
  skipped one.** **The gate has now been exercised NINETEEN times and has never fired, so its alert
  path REMAINS UNTESTED CODE**; a future run must not read nineteen quiet opens as evidence that it
  works. **The way to know the gate is sound is to read it, not to count the days it stayed silent.**
  **Corollary a future run needs: the FIRST time the gate fires will be a morning when the pre-market
  run failed — i.e. exactly the morning when the open run has no fresh notes to lean on and the
  untested alert path runs for the first time. Read Step 2 then, do not recall it.**

- **⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.**
  **⚠ RE-DISCHARGED 09-18 12:34 FROM THE EXITS-ONLY SEAT, AND THIS IS THE VERSION WHERE THE PROHIBITION
  IS STRUCTURAL RATHER THAN CIRCUMSTANTIAL.** The midday run read **full authority on every gate the
  scripts check** — breaker **INACTIVE**, cap **0 of 3**, empty sleeve, **30.21% idle cash**, no
  restricting note in `control.md` — **from the one seat in the system that is forbidden to use it.**
  **The open run's refusals turn on the plan carrying no BUY intent, which is a fact about the day;
  this run's turns on the routine's scope, which is a fact about the seat.** The two look identical in
  the order count and are not the same discipline: **a midday entry would not be a judgment call made
  badly, it would be a run doing something its own prompt forbids in its first line.** That is why
  routine 3 is the cheapest seat to hold the line from and the **worst one to draw comfort from** —
  passing here says nothing about whether the 09:35 seat will pass tomorrow.
  **⚠ RE-DISCHARGED 09-18 08:16, AND THE TEST IS GETTING EASIER TO PASS — WHICH IS ITSELF THE THING TO
  WATCH.** New positions were **fully permitted** — breaker INACTIVE, cap **0 of 3**, empty sleeve,
  **30.17% idle cash**, no restricting note — and the run wrote **zero BUY intents** off **four full
  theses**. **The honest reading of the streak: five consecutive pre-market runs have found full
  authority and used none of it, and the sixth refusal costs less effort than the first did.** **That
  is the discipline working, and it is also how a research seat quietly becomes one that has stopped
  expecting to find anything** — the two are indistinguishable from outside, because both produce an
  empty plan. **The defence is not to lower the §4 bar. It is to keep naming which specific part
  failed, so a human can see whether the funnel is filtering or idling.**
  **Routine 1 places no
  orders by design** — it researches and writes a plan; **routine 3 is exits-only**; **routine 4
  trades nothing at all.** **A breaker reading INACTIVE, a weekly cap at 0 of 3 and 30.24% idle cash
  are not an opportunity any of them may act on**, and carry-forward item (3) above (the structurally
  undeployed sleeve) must **never** be read as licence for a midday or after-hours entry. **New
  positions route through pre-market research plus the 09:35 execution run, always** — that path is
  what forces every buy to sleep on a written thesis, and any other entry would route around it
  rather than satisfy it. **RE-DISCHARGED 09-17 08:11 UNDER THE HARDEST VERSION OF THE TEST SO FAR:**
  the pre-market run found new positions **fully permitted** — breaker INACTIVE, cap 0 of 3, empty
  sleeve, 30.19% cash, no restricting note in `control.md` — and **wrote zero BUY intents on the one
  morning that supplied a genuinely first-rate event.** **Previous no-trade days could be explained
  by thin news; 09-17 had an 8-K, two named parties, a filed dollar figure and a clean rule (iii)
  pass — and still no Company B.** **A run that wanted to act could have reached for GNRC and called
  it diligence; GNRC is first-order and outside §4 at any price.** **RE-DISCHARGED 09-16 08:17** on
  the same terms: **fully permitted** — 30.24% cash — and **zero BUY intents.** **Nothing blocked the
  research. The research did not produce an eligible candidate.** That distinction is the whole point
  of Step 5's instruction not to do research you cannot act on: **the pressure runs the other way —
  full authority and nothing worth using it on.** **AND RE-DISCHARGED AGAIN 09-16 09:35 FROM THE ONE SEAT THAT COULD
  HAVE ACTED:** the open run is **the only routine permitted to open a position**, it read an
  **INACTIVE breaker, a cap at 0 of 3, an empty sleeve and 30.26% idle cash**, and it **opened
  nothing, because the plan it consumes carried no BUY intent.** **That is the discipline working at
  its single point of exposure.** The 08:00/09:35 gap exists precisely so a candidate reasoned into
  existence at the bell cannot become a fill; **a run that "found something" at 09:35 would not be
  diligent, it would be the failure this architecture is built to prevent.**
  **⚠ RE-DISCHARGED 09-17 09:35 FROM THAT SAME SEAT, ON THE MORNING WITH THE LOUDEST AVAILABLE
  EXCUSE.** Full authority — breaker INACTIVE, cap **0 of 3**, empty sleeve, **30.21% idle cash**, no
  restricting note — **and zero orders**, because the plan carried no BUY intent. **GNRC was on the
  tape and was not looked at at all**: zero `move`, `quote`, `bars` or `asset` calls. **The pull that
  actually arrived was not "buy it" — it was "pull its open just to document open item (7) for the
  human," a diagnostic with no trade attached and no risk on its own terms.** That is the honest
  shape of the temptation and it is far more plausible than a naked reach for the ticker. **It was
  refused because the habit it establishes is LOOKING AT THE LOUD TICKER AT 09:35**, and the
  pre-market run had already measured the same defect with the same data. **Expect the next version to
  arrive wearing diligence, not greed.**

- **⚠ THE TWO-PRICE DEFECT IS SOLVED — IT IS A QUOTE MIDPOINT, NOT AN OFFSET. DO NOT RE-OPEN IT AS A
  MYSTERY.** It resolved at the 09-11 close, where broker `current_price` 702.62 was **the midpoint of
  the 702.59/702.65 quote to the cent** while the official close was **702.52**. **The broker mark is
  not a close at all — it is a live bid/ask midpoint that keeps moving outside regular hours**, which
  is why the gap never had a stable size and never will. **This morning's 698.88 against yesterday's
  official close 696.29 is the same mechanism in pre-market**, and `lastday_price` 696.20 is a third
  number again. Always `bars --adjustment all` for a close, a fresh `quote` for execution, **never a
  `positions` field for either.** **The moment a satellite position exists, a `highest_close` read
  from a `positions` field records an after-hours midpoint and silently moves the §5.4 stop.**
  **⚠ 09-17 09:35 PRODUCED A FOURTH NUMBER AND IT IS THE SAME MECHANISM, NOT A NEW DEFECT — DO NOT
  LOG IT AS A RECONCILIATION BREAK.** `sleeves` reported core **$69,307.656284** and `positions`,
  called about a second later, reported market_value **$69,308.646747** — **99 cents apart on an
  IDENTICAL share count of 99.046311231.** Two live marks, two instants. **This is the cheapest
  possible demonstration of why a `highest_close` must never come from a `positions` field: two calls
  ONE SECOND apart disagree, so a §5.4 stop set from either is set from noise.** Until now the
  argument was theoretical and about after-hours midpoints; **this is the IN-SESSION version, and it
  is the one a future run will actually meet.**

- **⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST, AND ON 09-15 IT
  TURNED FLATTERING FOR THE FIRST TIME.** Broker day change **−0.240%** against VOO's official
  **−0.438%** read as the book beating the index by **0.198pp, about $65.** It did not: a 69.7%-exposed
  book loses **0.697 × 0.438% = 0.305%** by construction, exactly what matched official legs give.
  **Every prior instance was cosmetic or unfavourable; a favourable artifact is materially harder to
  discard**, and that is the shape in which this defect will eventually cost something. **Both legs
  from the same source, or the comparison means nothing.** **Anchor the week to 08-31, the first
  operating day.** **And expect the satellite sleeve's §1 number to read positive on every red week
  without the sleeve doing anything** — the defense is not arithmetic, it is refusing to let a
  favorable sign on a few sessions answer a 12-month question.
  **⚠ 09-16 PRODUCED A SECOND, DISTINCT SHAPE THAT SURVIVES THIS DEFENCE, AND IT MUST NOT BE FILED
  UNDER THE SAME HEADING.** The book fell **0.308%** while VOO fell **0.442%** — 13bp of apparent
  outperformance on the day the Fed hiked. **The close run checked for the mixed-source artifact
  FIRST and it is not what happened: BOTH LEGS ARE OFFICIAL CLOSES.** The arithmetic is correct and
  means nothing — it is **69.59% exposure × the index move and nothing else** (0.6959 × −0.442% =
  −0.307%, matching the official day P&L to a rounding tick). **UNDEREXPOSURE, NOT SKILL**, and it
  reverses with the same mechanical reliability on the first green day. **The defence against the
  mixed-source version is arithmetic; the defence against THIS version is refusing to let a correct
  number answer a question it was not asked.** §1 asks about twelve months, and 30% cash has a known
  negative answer to that in a rising market.

- **⚠ DO NOT REACH FOR THESE — 09-18's additions, ahead of the older list below.** **GFS and MRVL** —
  **both signatories** to the SiGe capacity agreement, i.e. **first-order and outside §4 at any
  price**, and the deal discloses **no dollar value, no wafer volume and no capacity figure**. **This
  was the most attractive item of the week and it still has no Company B**; neither the price nor the
  missing number is what killed it, so **it does not become a buy on a later day at a different
  price.** **LEU** — the **named seller** on the Antares HALEU contract, first-order, **already a
  disposed reject from 09-10**, and the deal's **pre-2030 first delivery is outside §4 part 3 no
  matter who the supplier turns out to be.** **LEN** — Company A on its own quarter, and the only
  read-across runs through **the mortgage rate, a macro variable rather than a transaction**; it is
  also **negative-direction on a long-only book.** **BLK** — part 1 passed and part 2 could not be
  written; **the $1.8B is capital IN, not revenue OUT**, and **the rejection is the absent segment
  figure, not size.** **TTE** — Company A on the GIP partnership, and a French issuer. **ADM, UNH** —
  first-order on their own guidance. **LH, NUE, STLD** — guidance-ISSUANCE alerts against consensus,
  rule (iii). **LMT** — the **awarded party** on the AIM-260 framework, for the second time this
  month, with **no dollar figure and no supplier named.** **VICR** — its OEM counterparty is unnamed,
  so there is nothing to screen. **None of these becomes a buy at a different price.**

- **⚠ DO NOT REACH FOR THESE — the disposed rejects and the trap in each.** **GNRC** — 09-17's, and
  the one most likely to be reached for, because it will be the loudest ticker on the tape: it is the
  **named counterparty in the Amazon announcement**, i.e. **first-order, Company A's direct
  beneficiary, outside §4 at any price**, and its **−6.09% `priced_in: true` reading is an artifact of
  open item (7), not a verdict**. **The 09-17 09:35 run did not look at it at all — zero `move`,
  `quote`, `bars` or `asset` calls — and the pull it refused was the DIAGNOSTIC one ("pull its open
  just to document open item (7)'s magnitude for the human"), not a reach for the trade. Expect that
  costume again: the next one will arrive wearing diligence.** **FLNC** — Company A on its own guidance cut; its contract
  manufacturer is unnamed and the share-shift read is the fifth shared-cause instance. **CACI, AMTM,
  KD** — **awarded parties**, ceilings not revenue, and **no filters were run on any of them because
  screening the awardee is running a filter on the wrong company** (rule i). **AVGO** — 09-16's, and
  the most instructive: **part 1 PASSED**, and it died on the counterparty disclosing **roadmap
  instead of segment revenue**, plus a **2027–2028** calendar, plus rule (iii). **It does not become
  a buy at a different price, and the −7.97% is not the reason.** **F, LULU, NCLH, PM** — all
  first-order on their own guidance; PM's was **currency only**. **ON** — the Subaru engagement
  explicitly is **not** a supply agreement. **CHTR** — the Cox deal closed in **August**. **AWK** —
  a **$770,000** acquisition. **VG** — Company A on the China Gas SPA, and
  first delivery is **2030**. **NAMC/Abrams** — no ticker exists; **HON was NOT screened** and that is
  absence of a source, not a verdict. **CRWV** — the **$52B is the project's, not CoreWeave's**, and
  the headline size disguises it. **LMT and BA** — both the **awarded party**, i.e. Company A, and no
  supplier is named on either award. **SRE** — Company A on the Petrobras SPA and four to five years
  out; **it resurfaced 09-16 as re-coverage, which is not a new event.** **BWXT** — the sole-source
  naval-reactor fact is **rule (v)**, and it will feel like a technicality rather than a rule.
  **CART** — died on the missing number, and the number does not exist to be found. **ORCL** is
  Company A twice over and **`priced_in: true` at +5.06%**. **LHX** — dead on arithmetic: **$127M
  Palantir + $65M Anduril = the entire $192M TITAN award**, $0 disclosed for anyone else. **AVAV** is
  the **awarded party** and its +1.20% is a round-tripped spike. **SLI** is ~$1B against the §3 $10B
  floor. **M** — the tariff-refund read-across runs through a **statute, not a transaction**. **JPM /
  BAC / WFC** — today's; buying any of them on its own guidance is first-order, and the read-across to
  peers is the shared-cause trap. **CNC** — a reaffirmation, rule (iii). **AXON** — a financing.
  **GIS** — does not report until ~Sept 23; the alert was a calendar entry. Also closed: **GFS, EQT**
  (*the tempting one — a clean filter sheet that died on size*), **LEU, TBBK, CASH, GDOT, CCB, QCOM,
  AMZN, GLW, VZ, MTZ, FN, COHR, LITE, CRDO, MRVL, DY, PWR, BSX, MDT, ABT.** **None becomes a buy at a
  different price.** **Do not reach for MU** — it has not entered the funnel for **fourteen consecutive
  days**, no source has named it, its filters were **not** re-run: **absence of evidence, not
  resolve.** If it resurfaces **from a source**, re-run its filters and re-test the timing window from
  that day's date.

- **⚠ NEW STANDING RULE (vii), WRITTEN 09-17: *CHECK WHETHER THE NAMED BENEFICIARY MAKES THE PART
  ITSELF BEFORE SPENDING A CALL HUNTING ITS SUPPLIERS.*** Generac is **vertically integrated** —
  engines, alternators, batteries, electronic controls, steel enclosures, all in-house — so the
  second-order supply chain §4 goes looking for **does not exist externally**. **This is the only one
  of the funnel's three failure shapes that no evidence standard can fix**, and it is cheap to screen
  for: one question about the company's manufacturing model, asked **before** the supplier hunt.
  **Unlike rules (iii) and (vi), which kill a candidate, this one saves a research call on a
  candidate that was never going to exist.**

- **⚠ SIX STANDING RULES, ONE ROOT CAUSE** *(now **eight** — see (vii) and (viii) above)*. (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, Alcoa/South32, Oracle's
  maintained capex guidance, the four unsourced headlines, CoreWeave's 300 MW re-reported as context,
  **and on 09-16: Broadcom's own Q3 2026 call already carrying MTIA, Centene's reaffirmation of July
  28 guidance, and Sempra/Petrobras re-covered as though fresh; and on 09-17: Charter/Cox re-covered
  five weeks after closing, plus THREE MarketBeat guidance-ISSUANCE alerts (Ameren, Five Below,
  DaVita) in one morning; **and on 09-18: Fluence's FY26 cut re-covered a day later as though fresh,
  plus THREE MORE guidance-ISSUANCE items (Labcorp, Nucor, Steel Dynamics) compared to CONSENSUS
  rather than to any prior company figure — the fourth, fifth and sixth instances of that costume this
  week**). **09-17 also produced the first clean rule (iii) PASS — Amazon/Generac,
  an 8-K with no prior disclosure — which is worth noting precisely because the rule usually kills.**
  (iv) *A recurring ticker is a warning, not corroboration* (LHX — resolved 09-11 on a number).
  (v) *A market-structure fact is not a supplier relationship* — "sole producer," "dominant share,"
  "the only company that makes X" are facts about an **industry**, not a **transaction**; **seven
  instances this month, plus the CEILING sub-shape which on 09-17 accounted for SIX OF SEVEN federal
  awards in one morning.** Earlier costumes: a **TABLE** (the DoD daily contracts digest, 09-15), a
  **CONSORTIUM AWARDEE** (Abrams, 09-16) and a sentence. (vi) *Screen the timing window early on
  anything whose subject is under construction* (Sempra/Petrobras 09-15, **Venture Global/China Gas
  09-16**, **Amazon/Generac 09-17 — deliveries 2027–2028**, **Centrus/Antares 09-18 — first delivery
  before 2030, FOURTH consecutive session; long-dated energy offtake is a standing feature of this
  funnel, not a visitor, and part 3 killed it in ONE step before either follow-up screen was needed**).
  **The source
  left the blank. Filling in a blank the source left blank is not research.** **Recognise the phrase;
  do not re-derive it.**

- **⚠ A SHARED CAUSE IS NOT A MECHANISM — FIFTH INSTANCE 09-17, AND IT CAME WITH A PRECISE NUMBER
  ATTACHED, WHICH IS WHAT MADE IT TEMPTING.** **Fluence Energy's FY26 guidance cut** quantifies a
  **$600M revenue hole** to the dollar — **~$450M of Houston contract-manufacturing delays, ~$65M of
  late-delivery penalties, ~$85M of logistics** — and the available second-order read, *"competitors
  capture the share Fluence cannot deliver,"* runs through **a market, not a transaction.** No source
  names a gaining competitor and none attaches a figure to one. **The trap here is specific and new:
  a precisely quantified loss invites the assumption that the money went somewhere NAMEABLE. It does
  not have to have gone anywhere.** *(Fluence's other failure is the ordinary one: the contract
  manufacturer is never named, and one source reports its corrective actions while withholding its
  identity — **the counterparty is not merely unnamed, it is actively described.**)*
  **⚠ SIXTH INSTANCE 09-18 — LENNAR, AND IT IS THE PLAINEST OF THE SIX.** Lennar's Q3 miss and
  delivery-guidance cut (**adj. EPS $1.23 vs $1.29; revenue $8.05B vs $8.31B expected and $8.81B a
  year ago**) is attributed to **higher mortgage rates and affordability**, and the read-across to any
  building-products supplier runs through **the same mortgage rate — a macro variable, not a
  transaction.** **The mechanism sentence required an "and also" clause, and §4 says that is the
  answer.** The screen for filings that **name Lennar as a customer and quantify the exposure**
  returned **nothing at all** — no concentration table, no risk-factor text, no segment disclosure.
  **A third objection sits underneath: the only available read is NEGATIVE and this is a long-only
  book, so even a perfectly-sourced version would be unactionable.** **Recorded in the order they were
  found, deliberately: the long-only objection came first and is the WEAKEST of the three, because it
  says nothing about whether the reasoning was sound.**

- **⚠ A SHARED CAUSE IS NOT A MECHANISM — FOURTH INSTANCE 09-16.** Macy's FQ2 (09-11) was the first:
  $116M of IEEPA tariff refunds, where *"the ruling lowers other import-heavy retailers' COGS too"*
  runs through a **statute, not a transaction**. Kroger's 09-14 guidance cut was the same shape —
  Kroger's soft ID sales and a supplier's soft volumes are both downstream of the **same grocery
  consumer**. The **Williams NESE ruling** (09-08) was the third, a **court ruling** rather than a
  transaction. **09-16's is the cleanest yet and the most tempting, because it comes with a genuine
  two-company contrast: JPM guiding Q3 trading and IB fees UP while BAC WARNS on the same lines, and
  WFC saying NIM will beat.** Both outcomes are downstream of **the same rate and capital-markets
  environment**, and **any bank actually affected discloses it itself, making it first-order for that
  bank.** **The distinction is easy to lose because the sentence sounds causal when said aloud — and
  a divergence between two named companies sounds even more causal than a single shared input.**

- **⚠ HPE IS THE LARGEST OPPORTUNITY COST THIS LOG HAS PRODUCED (+19.87% vs VOO) AND THE REJECTION
  WAS CORRECT. DO NOT RECORD IT AS ONE FINDING.** T-2026-09-02-02 rejected a **Dell → HPE read-across**
  at part 1, because a read-across is an inference about **information**, not a causal path changing
  Company B's economics. **What then moved the stock was HPE's own earnings print: +12.4% in the
  single session 09-10 → 09-11.** Rejected *correctly by the rule* and *unprofitably in hindsight* —
  **two findings, recorded as two. Nothing here loosens it.**

- **⚠ REJECT SCOREBOARD — 33 MEASUREMENTS, 9 BEAT VOO, MEAN EXCESS −0.51%. STILL A TALLY, NOT
  EVIDENCE; A REVIEW MUST NOT QUOTE IT AS A RESULT.** **It reversed on itself inside one week:**
  week 1's same ten names went from **6-of-10 beating VOO (mean −0.16%) to 3-of-10 (mean +1.17%)**
  once the window lengthened by a few sessions. **The split still points the same way on more data:**
  four-part-thesis and §3 failures lag; the two **priced-in filter vetoes** average **+7.36%** and are
  the two largest positive excesses on the board. **MU and LITE must never be merged:** MU (+4.14%)
  failed on a real **run-up** — the rule working as designed and costing money, change nothing; LITE
  (+10.58%) failed on a **drawdown**, the open question. **Do not tighten §4 in response, and do not
  loosen it.** **The 09-15 rejects (CRWV, and the no-ticker LMT/BA and Sempra entries) and the 09-16
  rejects are not yet measured; of 09-16's three, only AVGO has a ticker to measure.**

- **⚠ FOUR LOUD HEADLINES FROM 09-11 STILL HAVE NO PRIMARY SOURCE — AND NONE APPEARED IN THE 09-14,
  09-15 OR 09-16 SWEEPS.** *"Nvidia invests $30B in Intel," "Nvidia acquires Hugging Face," "Google's
  first nuclear deal / a $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity
  by 2032."* **All four trace to a single secondary aggregator briefing citing other outlets rather
  than any document.** **This is standing rule (iii) in a new costume, and `--recency day` passes it
  just as readily.** Events of that size produce primary disclosure; its absence is the finding. **If
  one is real it will arrive with a filing attached, and that is the day it enters the funnel.**

- **NO TRADES, NO FILLS, NOTHING IN LIMBO — CHECKED AGAINST §7.** The account's entire order history
  is **one row**: the 09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO
  99.046311231 @ $706.74, notional $70,000.00**, `status: filled`, terminal. **No `"terminal": false`
  case has ever arisen.** `trade_log.md` correctly left unappended — **a run with no fill writes no
  trade entry.** Loss streak **0 — nothing has ever closed**, so the §6 streak cannot move and no
  circuit-breaker alert is due. **Core is not tracked in `positions.md` by design** (§5 exempts it),
  so **every reconciliation compares satellite blocks to satellite Alpaca positions**; a run comparing
  raw ledger to raw broker will read a correct ledger as broken.

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON THIRTY-ONE TIMES NOW, AND DUE AGAIN NEXT RUN.**
  `positions.md` ran to **604 lines / 42KB** before the 09-07 collapse and has since been held to a
  **single current reconciliation block** — this run **replaced** the 09-17 12:35 midday block
  rather than adding a fourth 09-17 one beside it, and the superseded `prior_run` line (09-17
  open run) was dropped from the fenced block rather than left to accumulate as a third slot.
  **Today is the strongest case the rule has faced yet: FOUR runs, ONE date**, and the file still
  carries exactly one 09-17 block. **Every load-bearing fact is preserved; nothing live was
  discarded.** **The pull to append is structural** — a run is rewarded for showing it checked
  something, and a deleted note looks like a check that never happened.
  **⚠ AND NOW THE COUNTERWEIGHT, WHICH 09-17 SUPPLIED THE HARD WAY: `journal.md` IS THE DELIBERATE
  EXCEPTION AND A CLOSE RUN ALREADY VIOLATED IT ONCE.** It is **append-only by design, one entry per
  trading day, now ~88KB**, and it rolls over monthly with the other logs, **never by collapsing.**
  The 09-16 close run deleted a prior day's header there (see the headline note above). **Collapse
  discipline belongs to `positions.md` and to the fenced block. It must never be carried into
  `journal.md`, and a close run that finds itself tidying that file is making the 09-16 mistake.**

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; nothing predates the current month. **Next rollover is the first
  Friday review of October 2026.** ⚠ **`research_log.md` is now ~202KB — it grew ~15KB on 09-17
  alone.** The rollover rule is monthly and this month is not over, so **no run may archive early** —
  but the October rollover is not optional tidying. **Every run reads these logs in full, and a run
  that starts skimming is how a system quietly stops knowing what it holds.**

- **⚠ THE MIDDAY RUN'S STEP 2 WAS DISCHARGED BY READING, NOT BY ASSUMING — AND THE DISTINCTION IS THE
  WHOLE POINT OF THAT STEP.** Routine 3 exists so a stale `highest_close` is caught before it silently
  disables §5.4. **Today the field was ABSENT, not stale**, and absence is self-certifying in a way
  staleness is not: **an absent field carries no `(as of ...)` date, and it is the missing date that
  proves no backfill is due.** A stale mark would carry a date that lags the last trading day and look
  exactly as healthy as a current one. **Zero `alpaca.py bars` calls were issued and none was due.**
  **The first satellite fill arms §5.4 and converts this step from absent to load-bearing on the same
  day** — from that day forward, a skipped close run makes this check the only thing standing between
  a stale mark and a trailing stop that never fires.

- **⚠ THE PULL TO LOOK AT GNRC HAS NOW RECURRED ACROSS TWO CONSECUTIVE RUNS ON THE SAME DAY, WITH A
  DIFFERENT JUSTIFICATION EACH TIME — THAT PATTERN IS THE FINDING, NOT EITHER INSTANCE.** At 09:35 the
  reason was *"just to document open item (7)'s magnitude for the human."* At 12:35 it would have been
  *"just to see how it settled."* **Both are diagnostics, both are genuinely zero-risk on their own
  terms, and both were refused** — zero `move`/`quote`/`bars`/`asset` calls on GNRC all day.
  **A justification that regenerates itself in a new form every few hours is not a series of
  independent good reasons; it is one reflex looking for an acceptable wrapper.** It matters most in
  **this** seat: routine 3 is **exits-only and cannot open a position under any circumstance**, and on
  an empty sleeve it has **no §5 subject that could justify a price call on any ticker at all.** **A
  midday run with nothing to manage is supposed to be short.** Filling it with lookups is how an
  exits-only seat quietly becomes a scouting seat — and the scouting would be happening at the one
  time of day the 08:00/09:35 architecture exists to keep it away from.

- **⚠ COUNTERS, STATED SO THEY DO NOT DRIFT.** **46 theses since inception, 0 accepted** — 30 through
  09-11 (6+2+1+1 on 09-01/02/03/04, 4+5+6+5 on 09-08/09/10/11) plus **3 on 09-14** plus **3 on 09-15**
  plus **3 on 09-16** plus **3 on 09-17** plus **4 on 09-18**. **16 this week** (the week beginning
  2026-09-14). **Trading days with the sleeve empty: TWENTY** — 09-18's pre-market run is the first
  read of a new session and advanced it by one; **later runs today share this session and must NOT
  advance it again.** **Neither
  an open run nor a close run writes a thesis or consumes an ID** — an execution routine and a
  journaling routine do not research (§4 by way of the routine prompts), so the count is unchanged by
  them, not stalled. A counter already drifted once (31 vs the auditable 30) and was corrected on
  09-11; **in a repo whose only memory is these files, a counter that drifts unremarked is how a
  larger one starts.**
  **Positions opened: still zero. `new_positions_this_week` stays at 0 of 3 because nothing was
  placed, not because the cap bound.** **Satellite exits executed since inception: ZERO, across
  nineteen midday management runs that each had nothing to manage.** **Orders placed since inception:
  ONE** — the 09-03 core VOO buy; **the 09-18 pre-market run places none by design, so the number is
  unchanged and `trade_log.md` is correctly left unappended: a run with no fill writes no trade
  entry.** **Satellite orders placed since inception: ZERO.** **Market-open runs that placed nothing:
  every one since 09-03.** **Daily journal entries written: THIRTEEN, one per September trading day
  through 09-17 inclusive — audited 09-17 by listing the `###` headers, which is how the missing 09-15
  header was found. Do not take the count on trust; re-run the listing.** **Close runs completed: one
  per trading day through 09-17; 09-18's is still ahead.**

- **ClickUp tasks, for reference:** **09-17 daily summary `86bc2nff1`** (carries the journal-header
  finding under "Needs a human"); 09-16 daily summary `86bc1y9mr`; 09-15 daily summary
  `86bc17nc4`; 09-14 daily summary
  `86bc0hw64`; **09-11 weekly review `86bbzgbg3`**; 09-11 daily summary `86bbzfm12`; 09-10
  `86bbyr8vp`; 09-09 `86bbxtn1a`; 09-08 `86bbwuc17`; 09-04 daily summary `86bbv6npm` and weekly review
  `86bbv75bz`. **No alert task exists** — no alert condition (breaker, push failure, selftest abort,
  guard violation, stale plan) has ever arisen, and `alerts.md` remains empty.
