# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-24 08:20 ET 1-premarket-research (selftest PASSED all five checks, trading_enabled true, LIVE paper, equity 99776.15; clock is_open FALSE at 08:20:51 with next_open 2026-09-24T09:30 - THE PRE-MARKET SHAPE, next_open points at TODAY, and yesterday's 16:16 close run read the IDENTICAL boolean with next_open pointing at 2026-09-24, so only the date discriminates - NOT a holiday, plan owed; RECONCILIATION CLEAN satellite-to-satellite, zero blocks vs zero satellite Alpaca rows, positions returns ONE row core VOO 99.046311231 shares unchanged since the 09-03 fill, avg_entry 706.74, cost_basis 69999.99, market_value 69776.15; STEP 4 HAD NO OPERAND - all four 5 rules iterate over open satellite positions and there are zero, 5.1 no invalidation string has EVER been written so ZERO perplexity news-check calls were due on that path and zero made, 5.2 no timing_window, 5.3 no entry_price, 5.4 no highest_close, THIRTIETH session with 5.1-5.4 never started, 5.4 STILL NOT ARMED, sell_rule_status ABSENT rather than blank and highest_close ABSENT - the third state carrying no (as of) date at all, which is exactly what proves NO BACKFILL IS OWED; ⚠⚠ THE TWO-PRICE DEFECT PRODUCED THE MOST INFORMATIVE INSTANCE IN THE SERIES AND FALSIFIED AN INHERITED MECHANISM FOR THE SECOND TIME IN THREE DAYS - yesterday's file made a CONCRETE FALSIFIABLE PREDICTION ("if lastday_price still reads 712.78 tomorrow morning it is $5.50 WRONG") and IT CAME OUT THE OTHER WAY: lastday_price reads 707.60, THE FIELD DID REBUILD at this session boundary, falsifying the 09-23 finding that it does not rebuild which had itself falsified the 09-22 finding that it does - BOTH GENERALISATIONS ARE DEAD, two consecutive runs each drew a confident structural rule from ONE observation and each was wrong; ⚠ AND IT REBUILT TO A WRONG NUMBER - 32 CENTS HIGH against the official 707.28, THE LARGEST lastday_price ERROR IN THE RECORD, prior series 7c low / 2c high / 9c high so 32c is more than THREE TIMES the worst, and READ TOGETHER THE CONCLUSION IS WORSE THAN EITHER ALONE: REBUILDING IS NOT A SIGN OF CORRECTNESS, the one morning the field refreshed is the morning it was furthest off; broker change_today -0.00441 and unrealized_intraday_pl -309.02 both computed off the 707.60 baseline, NEITHER USED NOR CARRIED INTO ANY FIGURE, current_price 704.48 is a PRE-MARKET MIDPOINT not a close; RESEARCH RAN IN FULL AND PRODUCED NO TRADE - new positions FULLY PERMITTED (breaker INACTIVE, cap 0 of 3, sleeve empty, no restricting note), FIVE perplexity scans, SEVEN theses all REJECTED (T-2026-09-24-01 ILMN, -02 GRAL, -03 BBY, -04 PYPL, -05 SHOP, -06 SoftBank/OpenAI, -07 ELMT), FIVE alpaca move calls as 4 hard filters on PYPL BBY SHOP ILMN GRAL; ⚠⚠ THE FINDING OF THE DAY IS NOT A THESIS - THE 4 PRICED-IN FILTER FIRED ON THREE GENUINE RISES (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%) AND THAT IS THE FIRST TIME IN VOLUME THE RECORD SHOWS IT DOING ITS DESIGNED JOB, open item (1) has NINE instances of it reading a DRAWDOWN as priced-in and the weight of that record makes it easy to read the filter as BROKEN - IT IS NOT BROKEN, IT IS SIGN-BLIND, and today is the same defect seen from the WORKING side, so the fix is to make it read SIGN not to loosen or remove it; ⚠ ILMN IS THE SHARPEST ENTRY AND IT NEVER REACHED A THESIS - the GRAIL advisory vote is the most genuinely SECOND-ORDER shape in several sessions (named beneficiary with a structurally necessary named supplier), THE STORY WAS HALF-BUILT WHEN THE FILTER RAN AND THE FILTER KILLED IT, which is exactly why 4 orders the hard filters BEFORE the thesis; ⚠ A PERPLEXITY CALL RETURNED HTTP 500 AFTER A GREEN SELFTEST, recovered on a reworded retry, every later call 200 - OPEN ITEM (6) NOW HAS ITS FIRST INSTANCE ON THE RESEARCH PLANE WHICH IS WHERE IT MATTERS MOST because a silently empty research run reads EXACTLY like a quiet news day, single transient occurrence, NO ALERT RAISED; ⚠ CUMULATIVE COUNT RECOUNTED FROM SOURCE NOT INHERITED - 68 ### T- headings of which ONE IS THE TEMPLATE = 67 REAL THESES (60 at yesterday's close plus 7), no duplicate IDs, ZERO ACCEPTED EVER; SLEEVES equity 99776.15, core 69776.15 = 69.93%, satellite 0.0% count 0, cash 30000.00 = 30.07%, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta +67.16, NO REBALANCE DUE - 2 rebalances at the 65/75 BAND EDGE not to the exact target so no delta inside the band is an action at any size, shortfall 0.07% of equity against a band edge 4.93 points away, THIRTY-NINTH consecutive run inside a 0.63-point range 69.59-70.22, ⚠ AND THE SIGN OF rebalance_delta FLIPPED - every recent run carried a NEGATIVE delta (core above target), today's is POSITIVE (core below), which is the core falling with the tape NOT drift requiring action, and it is the SMALLEST absolute delta in the series; ZERO ORDERS, nothing in limbo, no order has EVER reached a non-terminal state here so trade_log correctly left unappended; NOTHING CLOSED EVER so consecutive_closed_losses stays 0 and it HAS NEVER HAD AN INPUT, breaker INACTIVE, halt_triggered_at none so NO HALT_CLEARED_AT comparison was required and NO circuit-breaker alert was due, open_thesis_ids stays none; core VOO deliberately NOT stamped, FORTY-EIGHTH refusal, and this run HELD A CLEAN OFFICIAL CLOSE (707.28) in hand for tape context which is the pre-market version of the temptation; GNRC NOT LOOKED AT, TWENTIETH refusal and A STRONG ONE - this run issued FIVE move calls against a live funnel WITH a research step for a sixth to land in, so --symbol GNRC was one more invocation on a command line already typed five times over and it was NOT MADE, no new costume, the pull arrived in the catalogued screen-already-running / zero-marginal-cost form; WEEK ROLLOVER CHECKED - Thursday 2026-09-24 confirmed via TZ=America/New_York, ISO Monday 2026-09-21, week_of already 2026-09-21, THIRTEENTH consecutive run to find the reset already done, new_positions_this_week stays 0 of 3, next boundary Monday 2026-09-28; positions.md COLLAPSED the 09-22 and 09-23 per-run blocks (8 runs, ~350 lines of one null result) per the file's own standing instruction, 36K to 20K, nothing live discarded; alerts.md empty, zero open incidents, zero SYSTEMIC)

prior_run: 2026-09-23 16:16 ET 4-market-close-journal (selftest PASSED, equity 100055.46; post-bell shape confirmed by BOTH next_open 2026-09-24 AND a VOO daily bar for 09-23 existing, the stronger discriminator; Step 2 high-water was a NO-OP for the twenty-ninth session and that is NOT the same as passing - zero satellite blocks, highest_close ABSENT, and the sentence "high-water marks updated, nothing moved" was CAUGHT IN DRAFT as the wrong one, since it is true of a book whose closes did not exceed their marks and FALSE here where there are NO marks; DAY P&L close-to-close from official bars - VOO 707.28 vs 712.69, -0.759%, core -535.84, equity -0.533%, SINCE INCEPTION +0.053%, the LARGEST single-day decline in dollars and percent since the core was established 09-03, grounded from a pulled 25-session series; broker equity-last_equity -542.77 vs true -535.84 and the 6.93 gap DECOMPOSES PERFECTLY - 99.046311231 x 0.09 stale baseline minus 99.046311231 x 0.02 high midpoint = 8.91 - 1.98 = 6.93, BOTH LEGS WRONG AT ONCE IN OPPOSITE DIRECTIONS RECONCILING AGAINST EACH OTHER, which is why no check internal to the broker's fields can ever surface either; 6 theses 0 accepted 6 rejected; zero orders; journal appended; ClickUp summary 86bc6dhzq)

week_of: 2026-09-21
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.93
satellite_pct: 0.0
cash_pct: 30.07
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

**⚠ COLLAPSE, DO NOT APPEND — acted on thirty-three times.** The Week 3 review flagged the memory files
at 477KB **against an instruction to read them in full**, calling the accumulation **actively harmful
rather than untidy**: this repo's only continuity mechanism is the next run *reading* these files, and
padding them with restatements raises the odds a genuinely live item gets skimmed. **Carry-forward is
defined as cleared once acted on.** This run updated items in place and discharged the spent ones.
**Nothing live has been discarded** — the narrative history lives in `journal.md`, `research_log.md`
and `weekly_review.md`, which are the files built to hold it.

---

### Live — act on these

- **⚠ HIGH-WATER MARKS WERE NOT UPDATED, AND NOTHING WAS SKIPPED. DO NOT BACKFILL — THERE IS NOTHING TO
  BACKFILL.** `positions.md` carries **zero satellite blocks**, so `highest_close` is **ABSENT — the
  third state, carrying no `(as of …)` date at all.** ⚠ **The distinction is FREE today and stops being
  free the moment a satellite fill lands** — after that, a mark silently not written reads identically
  to a mark correctly unchanged, and **only the `(as of …)` date separates them. Compare the date;
  never infer from the field's emptiness.** **§5.4 is NOT ARMED**; it arms on the first **satellite**
  fill, and the 09-03 core fill was not one. **Thirtieth consecutive session with §5.1–§5.4 never
  started — they remain UNTESTED CODE PATHS, and the running tally of "no exits" records the ABSENCE OF
  A SUBJECT, not thirty clean bills of health.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE.** VOO **official** closes: **09-23 707.28**,
  09-22 712.69, 09-21 712.76, 09-18 701.85. Core is **99.046311231 shares at 706.74**, cash
  **$30,000.00** flat. Core **69.93%**, `rebalance_delta` **+$67.16**, **NO REBALANCE DUE** — §2
  rebalances at the **65/75 band edge**, not to the exact target, so no delta inside the band is an
  action at any size, and the core sits **4.93 points** from the nearest edge. ⚠ **The delta's SIGN
  FLIPPED (core is now BELOW target for the first time in this series) and it is the SMALLEST absolute
  delta yet — that is the core falling with the tape, not drift.** **Audit any superlative here before
  repeating it.**

- **⚠⚠ NEWEST AND MOST USEFUL, 09-24: `lastday_price` HAS NO RELIABLE STRUCTURE AT ALL, AND THE TWO
  COMPETING MECHANISMS ARE BOTH NOW DEAD.** 09-22 concluded the field **rebuilds** at a session
  boundary. 09-23 falsified that and concluded it **does not**, and made a concrete prediction:
  *"today's official close is 707.28 — if `lastday_price` still reads 712.78 tomorrow morning it is
  $5.50 WRONG."* ⚠ **09-24 read 707.60. The field DID rebuild, so the 09-23 mechanism is falsified in
  turn.** ⚠ **Two consecutive runs each drew a confident structural rule from ONE observation and each
  was wrong — that is the pattern, not either rule.**
  ⚠ **AND IT REBUILT TO A WRONG NUMBER: 707.60 vs the official 707.28 is 32 CENTS HIGH, the LARGEST
  error this field has produced** (prior series: 7c low, 2c high, 9c high — **32c is more than three
  times the worst**). ⚠ **Read together, the conclusion is worse than either fact alone: REBUILDING IS
  NOT A SIGN OF CORRECTNESS. The one morning the field refreshed is the morning it was furthest off.**
  There is **no offset to correct, no refresh point to rely on, no sign to predict.** **The only safe
  posture is the standing rule below, with no exceptions and no "it will have rebuilt by now."**

- **⚠ STANDING RULE, EVIDENCED FIVE WAYS NOW: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER
  `unrealized_intraday_pl`, NEVER a `positions` field for a close or an execution reference.**
  **Close-to-close from `bars --adjustment all`, a fresh `quote` for execution.** The defect has been
  load-bearing **four times with no satellite position involved at all**, in the one number the ClickUp
  summary leads with. ⚠ **On 09-22 it was a SIGN error** (broker reported **+$7.82 UP** on a **−$6.93
  DOWN** day, both legs wrong at once in opposite directions). ⚠ **On 09-23 it was $6.93 of noise on a
  real move of −$535.84 — 1.3% of the headline, invisible in the rounding, and the rule bought nothing
  that day. RECORDED HONESTLY, because the false version of this note is "the rule saved me again."**
  ⚠ **THE RULE'S VALUE IS INVERSELY PROPORTIONAL TO THE SIZE OF THE REAL MOVE**, so it looks like
  pedantry on exactly the days it costs nothing to follow — **and a 17-cent artifact outweighs the real
  move whenever the real move is small, which is most days.** ⚠ **The legs reconcile perfectly against
  each other, which is why NO CHECK INTERNAL TO THE BROKER'S OWN FIELDS CAN EVER SURFACE EITHER. Only
  an external close settles it.**
  **Post-bell `current_price` record: 22c LOW (09-21), 16.9c HIGH (09-22), 2c HIGH (09-23)** — same
  routine, same minute of the day, **no predictable sign and no correctable offset.** A close run
  taking that shortcut would bias a §5.4 trailing stop **against** the holder one day and **in their
  favour** the next, silently every time.

- **⚠⚠ NEW AND DECISION-RELEVANT, 09-24: THE §4 PRICED-IN FILTER FIRED ON THREE GENUINE RISES, AND THAT
  IS EVIDENCE THE ACCUMULATED NARRATIVE IN THESE FILES HAS BEEN ONE-SIDED.** **SHOP +9.61%, ILMN
  +11.54%, GRAL +44.67%**, all five-session, all `priced_in: true`. Open item (1) below has **nine
  instances of the filter reading a DRAWDOWN as priced-in** plus three near-misses, and the sheer weight
  of that record makes the filter easy to read as simply broken. ⚠ **It is not broken; it is
  SIGN-BLIND.** On a **rise**, "moved more than 4% in five sessions" means exactly what §4 intends —
  **you are late.** ⚠ **Recorded prominently and deliberately, because a system that only ever logs a
  rule's failures is BUILDING A CASE rather than keeping a record.** ⚠ **The implication for the human
  is specific: the fix to open items (1) and (2) is to make the filter read SIGN — evidence FOR that,
  and AGAINST loosening or removing it.**
  ⚠ **ILMN IS THE SHARPEST ENTRY AND IT NEVER REACHED A THESIS.** The GRAIL advisory-committee vote is
  the most genuinely **second-order** shape the funnel has produced in several sessions — a named
  beneficiary with a structurally necessary named supplier. **The story was half-built when the hard
  filter ran, and the filter killed it.** ⚠ **§4 orders the hard filters BEFORE the thesis precisely so
  that this happens: five more minutes of construction and it would have been a written thesis looking
  for permission.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR
  JUDGMENT RATHER THAN CARE.** Recounted from source on 09-24, **not inherited** — `research_log.md`
  holds **68 `### T-` headings, one the template, so 67 REAL THESES, no duplicate IDs, ZERO ACCEPTED
  EVER.** Set beside that: an empty satellite sleeve, **30.07% idle cash**, a weekly cap unused at
  **0 of 3**, an INACTIVE breaker, and an account at **+0.053% since inception** (09-23 official close).
  ⚠ **EVERY ONE OF THOSE FACTS READS AS AN ARGUMENT THAT THE FILTER IS TOO TIGHT, AND NOT ONE OF THEM IS
  EVIDENCE ABOUT ANY INDIVIDUAL THESIS.** §4's own position governs: a run that finds nothing is a
  successful run, and **a flat account is what "no trade" LOOKS LIKE — not a verdict on the rule that
  produced it.** **Naming the pull is the only defence against acting on it.** If the bar is to move,
  that is a `strategy.md` change and **only the human may make it.** **Do not resolve it from this seat.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY AND THAT IS ITS NORMAL STATE.** ⚠ **Today's
  seven rejections do NOT become a queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE.**
  **ILMN** (part 3 kills it at any price: non-binding vote → undated PMA decision → reimbursement → ramp
  is several quarters out) · **GRAL** (first-order — the company in the headline) · **BBY and PYPL**
  (no revenue share, minimum, value, volume or take rate disclosed by any party; and the only economics
  described is Meta taking **a fee**, a **cost** at the retailer) · **SHOP** (part 2 fails identically
  to PYPL's, so not a price-only rejection) · **SoftBank/OpenAI** (recipient is private; no US-listed
  party has an allocated figure) · **ELMT** (~$634M microcap; Masan Vietnam-listed).
  ⚠ **ELMT HAS NOW ENTERED THIS FUNNEL TWICE IN TWO SESSIONS ON TWO DIFFERENT, WELL-DISCLOSED TUNGSTEN
  TRANSACTIONS, AND BOTH DIED ON THE SAME §3 FLOOR. A third Elmet headline is not a third opportunity —
  it is the same ineligible company. Do not screen it again.**
  ⚠ **One §3 question was reached and deliberately NOT decided: Shopify is a Canadian issuer trading as
  common stock on a US exchange, which §3's "US-listed common stock" does not obviously settle either
  way. Two independent kills landed first. A future run reaching this with a LIVE candidate must put it
  to the human rather than decide it from this seat.**

- **⚠ OPEN ITEM (6) NOW HAS AN INSTANCE ON THE RESEARCH PLANE, WHICH IS WHERE IT MATTERS MOST HERE.**
  A `perplexity.py` call returned **HTTP 500** on 09-24 **after a green selftest**; a reworded retry
  succeeded immediately and every later call returned 200. ⚠ **The selftest's Perplexity check confirms
  the model endpoint answers; it does not confirm a QUERY will.** ⚠ **A research run that silently
  returns nothing is indistinguishable in `research_log.md` from a legitimate quiet day — which is
  exactly the failure routine 1's Step 0 exists to make loud, and on the data plane it is silent.**
  **Check exit codes; never infer thin news from empty results.** Single transient occurrence,
  recovered, **no alert raised.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — FOUR CATCHES NOW, AND THE LAST TWO WERE
  MECHANISMS RATHER THAN COUNTS.** **(1)** A false superlative (*"positive for the first time in this
  account's history"*) survived three runs and was caught **by accident** on 09-21 — VOO closed above
  the 706.74 fill on 09-03 and 09-04 too. **(2)** A stale count (*"49 theses"*) was caught
  **deliberately** on 09-22, having run in the direction that **understates** the problem. **(3)** The
  09-22 claim that `lastday_price` rebuilds at a session boundary, falsified 09-23. **(4)** The 09-23
  claim that it does **not**, falsified 09-24. ⚠ **A superlative, count or mechanism inherited from a
  prior run is NOT a checked fact** — it is the cheapest claim to write and the most expensive to
  verify. **Assume the next one you are handed is wrong until you have pulled the series.** ⚠ **Note
  what made catches (3) and (4) possible: the prior run wrote down a CONCRETE, FALSIFIABLE PREDICTION.
  Keep doing that — it is what turns a guess into something the next run can settle in one look.**

- **⚠ EVERY UP DAY COSTS THE ACCOUNT GROUND — DO NOT LET A GREEN HEADLINE STOP THE BENCHMARK CHECK.**
  09-21 was the **largest dollar and percent day in the account's history** (+$1,080.60 / +1.0859%)
  **and simultaneously its worst day of relative performance**: VOO returned **+1.5545%**, so the
  account **lagged by 0.469pp in one session.** ⚠ **Twelve sessions, nine positive-excess days, ALL NINE
  ON VOO DOWN DAYS. NOT ONE POSITIVE-EXCESS DAY HAS EVER COINCIDED WITH A RISING MARKET.** The satellite
  sleeve's positive excess on short windows **is nothing but 0% exposure to a market that fell** — it
  only pays on down days, and in proportion to how far the market fell, which on a flat day is nothing.
  **A green headline is the easiest possible moment to stop looking at §1's actual question — and so is
  a flat one dressed up as outperformance.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — TWENTY CONSECUTIVE REFUSALS.** The disqualifying facts do not move:
  **GNRC is the named counterparty in the Amazon announcement — first-order, outside §4 at any price** —
  and **open item (7) is resolved by a human editing §4 or `alpaca.py move`, not by a number this seat
  collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER EACH REFUSAL COST ANYTHING, AND MOST OF
  THEM DID NOT.** A refusal made with the **symbol data plane shut** — no `move`, `quote`, `bars` or
  `asset` call on any symbol — is **FREE, and free is not proof the discipline holds.** ⚠ **The count
  accumulates fastest on exactly the runs where it means least, because routines 2, 3 and 4 have no
  research step. Twenty is not twenty equal observations, and quoting the bare count overstates the
  evidence.** ⚠ **09-23 pre-market and 09-24 pre-market are the two STRONG ones: both opened the data
  plane against a live funnel AND had somewhere to put a number** — 09-24 issued **five** `move` calls,
  making `--symbol GNRC` one more invocation on a command line already typed five times over. **Not
  made.** ⚠ **No new costume has appeared in three sessions; the pull keeps arriving in the catalogued
  "screen-already-running" / "zero-marginal-cost" form. The costume list may be CONVERGING rather than
  growing, and a run that manufactures a new name for an old experience would be padding the log.**
  Costumes: diligence, curiosity, tidiness, completeness, zero-marginal-cost, self-audit,
  proxy-procurement, issue-closure, call-already-open, screen-already-running. **The pattern is the
  finding, not any instance. FREE IS NOT THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FORTY-EIGHT RUNS.** §5 exempts core from all
  four sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **Grade these the way the GNRC count is graded — a refusal only costs something on a run that was
  HOLDING the number.** The sharpest instances are the ones with a fresh official close in hand **and**
  an empty Step 2: **09-22 close (712.69), 09-23 close (707.28), 09-24 pre-market (707.28).** ⚠ **"Nothing
  to write" is the correct output of an empty Step 2, not an invitation to find a row to write it to.**
  **Measure the core from the 706.74 fill and from an official close, never from a `positions` field.**
  ⚠ **Noted honestly: this refusal is now close to automatic, and automatic is not the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN IS
  USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell sees it
  pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with **no bar for
  today**. ⚠ **09-22 read all three shapes in one day, and consecutive runs read IDENTICAL booleans
  meaning opposite things.** ⚠ **`is_open: TRUE` is the one case where the boolean alone is sufficient,
  and it is safe to read it that way ONLY because TRUE has a single meaning. FALSE has three.**
  ⚠ **The STRONGER discriminator is to check that a daily bar for today EXISTS** — that settles "was
  there a session?" **directly**, where `next_open` only settles it by inference. **Run it before
  deciding a run is a holiday skip.**

- **⚠ SEVEN ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — **NINE instances** (newest CNC,
  09-23: −6.44% → `priced_in: true` on a **FALL**; before it ACN, 09-22, −4.58%), plus **THREE
  near-misses** where a candidate cleared only because its *fall* was fractionally too small (LMT
  −3.61%; **GM −3.95%, five basis points inside the wire**; **LH −3.83%, seventeen basis points
  inside**). **There is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on the
  bill. ⚠ **A pass on a fall is not evidence the filter worked, and neither is a FAIL on a fall** — those
  readings are recorded **deliberately as NOT the reason for the rejection**, so no run inherits
  "rejected because priced-in" as a fact. ⚠ **09-24 supplies the counterweight and it is the first of
  its kind in volume: THREE firings on genuine RISES (SHOP, ILMN, GRAL), where the filter did exactly
  what §4 built it to do. The defect is SIGN-BLINDNESS, not the threshold — see the live item above.**
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM (09-09,
  +2.70% after a +8.7% intraday move), AVAV (09-11, +1.20% after a +12.9% round trip in one session).
  Same root cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or
  `alpaca.py move`.**
  **(3)** The satellite sleeve is **structurally undeployed — 67 theses, zero positions, ever.**
  ⚠ **RECOUNTED FROM SOURCE at the 09-24 pre-market run, per the standing rule. Recount before quoting;
  do not copy this line forward.** A 70/30 cash book cannot beat the S&P over a rolling 12 months (§1)
  in a rising market. **§2 permits the cash and §4 says most runs end in no trade — both rules were
  followed, and the agent must NOT respond by lowering the §4 bar.** **The binding constraint has FOUR
  known forms:** the source withholds the counterparty's number; **or** the counterparty discloses
  **roadmap instead of segment revenue**; **or** the named beneficiary is **vertically integrated** with
  no external supplier to find; **or** **both parties expressly refuse to disclose as a commercial
  choice** (09-21 GM), so **no better-sourced version of that candidate will ever arrive.** ⚠ **Only the
  first two forms are addressable by widening the evidence bar. The last two are not addressable at all**
  — the most decision-relevant line in this file. ⚠ **AND WIDENING THE BAR IS NOT THE WHOLE ANSWER
  ANYWAY: ELMT (09-23 and again 09-24) withheld NOTHING and still produced no trade, because the
  obstruction was STRUCTURAL (§3) — a constraint no evidence bar can relieve.** ⚠ **09-24's BBY/PYPL
  pair is the purest live example of form one: every party named, the event real, dated and
  first-disclosed, and NOT ONE COMMERCIAL TERM in existence to build a dollar path from.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the
  prior close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11: measured from the
  fill, tracking error 0.0000%. Keep measuring it from the fill.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it
  never had a stable size and never will. Previously filed as *cosmetic on core*; **that framing was too
  generous — it has now been load-bearing FOUR times with no satellite involved.** ⚠ **Re-rate.**
  Whether the tooling should read closes from `bars` by default is a human's call.
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed
  all five checks on 09-11 while `clock` returned 500 and `quote`/`bars` returned 504. ⚠ **AND ON 09-24
  IT PASSED WHILE A `perplexity.py` QUERY RETURNED 500 — the first instance on the RESEARCH plane, which
  is the one that matters most here.** **Every routine's Step 0 is the loud-failure mechanism for exactly
  this, and on the data plane it is silent.** Until a human changes it: **probe by hand; never infer
  data-plane health from a green selftest.**
  **(7)** **`alpaca.py move` cannot see an after-hours event**, and neither can the 09:35 re-validation
  that exists to catch exactly this. ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a
  trade rather than skipping one**, which is why it is listed last and should be read first. **It has
  cost zero only because no plan has yet carried a BUY intent — an absence of exposure, not a
  mitigation.** It disappears the first morning a BUY intent names a stock whose news broke after the
  prior close.
  Prior context in ClickUp `86bbv75bz`; last week's in `86bbzgbg3`.

- **⚠ WEEK 3 REVIEW (2026-09-18): THE §1 ANSWER IS NO, AND SHORT GREEN WINDOWS MUST NOT BE READ AS YES.**
  The satellite sleeve returned **0.0000%** — zero positions in the account's entire history — so its
  dollar-weighted excess over VOO is exactly **minus VOO's total return** over whatever window is
  chosen: **+0.095pp on the week, +0.430pp since inception, +0.509pp over 1M, −2.291pp over 3M, and
  −16.552pp over the rolling 12 months §1 actually names.** The structural cost is **~4.97pp of account
  return per rolling 12 months.** Full working in `weekly_review.md`. **Reject board: 40 measurements,
  13 beat VOO, 27 lagged, mean excess −1.57%.** ⚠ **It is a tally, not a result — do not quote it as
  one.** **HPE remains the largest single opportunity cost the log has produced (+19.87% vs VOO).**
  ⚠ **FILE SIZE — FIFTH CONSECUTIVE FLAG AND THE NUMBER KEEPS RISING.** `research_log.md` is now
  **~304KB** (09-24 added seven entries; ~288KB on 09-23, ~264KB on 09-22), against a total memory
  footprint of **~640KB** across files every run is instructed to read **in full**. **Monthly archive
  rollover is next due 2026-10-02.** ⚠ **A human may want to move it forward — this is the fifth
  consecutive flag, and `positions.md` was collapsed 36K→20K on 09-24 to make room, which is a
  mitigation, not a fix.**

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** compared to **consensus** rather than to any prior
company figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations**
(Centene, Southwest, General Mills), **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence,
Alcoa/South32, **Nocera/E-PRO's August 26 allocation surfacing 09-23**), and — **a genuine transaction
whose DELIVERY MILESTONE is recycled as the news** (09-21 GM/Lockheed: contract 08-06, delivery 08-28,
first wire 09-17, headline 09-21), and **a PRE-IPO CONTRACT BOOK** (Nscale's $103B, contracts signed up
to ten months earlier). **Every earlier costume announced nothing; the last two announce something real
that already happened.** ⚠ **STANDING PRACTICE: ask a transaction WHEN IT HAPPENED before asking who it
helps.** One screen settles it, and it is the cheaper of the two kills. *(09-17 Amazon/Generac was the
first clean rule (iii) PASS — an 8-K with no prior disclosure. **09-24's Elmet/Masan is the second**:
checked and genuinely new, a different counterparty and structure from 09-23's Tungsten West deal — it
died on §3 instead.)*
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — resolved 09-11 on a number).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share,"
"the only company that makes X" are facts about an **industry**, not a **transaction** — seven instances
this month, plus the **CEILING sub-shape**. Earlier costumes: a **table** (DoD daily contracts digest),
a **consortium awardee** (Abrams), and a bare sentence. ⚠ **09-24's SoftBank/OpenAI is the newest and
most tempting: $11.1B raised, an obvious compute-supplier inference available, and NOT ONE US-listed
recipient named with an allocation.** **The source left the blank; filling it in is not research.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.* Long-dated
energy offtake is **a standing feature of this funnel, not a visitor** — Sempra/Petrobras, Venture
Global/China Gas, Amazon/Generac (2027–28), Centrus/Antares (before 2030), Elmet/Tungsten West (eight
years), NeoVolta/SK On (2027–31). ⚠ **09-24 adds the REGULATORY version: a non-binding advisory vote →
an undated FDA decision → reimbursement → commercial ramp (ILMN) is the same shape wearing a lab coat.**
**Part 3 kills these in ONE step, before either follow-up screen is needed.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part 2.**
Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; Brookfield/Bloom's **$25B** is a
**FINANCING CEILING AVAILABLE TO SOMEBODY ELSE** that may never be drawn; SoftBank's **$11.1B** (09-24)
is **capital paid IN to a private recipient**; Royal Caribbean's **~$3B** for Sandals is **capital paid
OUT by the buyable leg**. ⚠ **A large, real, sourced, prominently-placed number is not a dollar path.**
⚠ **AND THE SUBTLEST VERSION, 09-24 BBY: the only economics disclosed was Meta taking "a small fee from
transactions" — a COST at the candidate, described in language that reads like a partnership benefit.**
T-2026-09-18-04 (BLK) is the worked example: **part 1 passed cleanly and it died on the absent segment
figure, NOT on size** — do not re-record it as a size rejection.

**⚠ A SHARED CAUSE IS NOT A MECHANISM — EIGHT INSTANCES, AND IT WORKS IN BOTH SIGNS.** Two companies
moving on the same macro input (a crush spread, a mortgage rate, a rate decision) is a **market**, not a
**transaction**, and the giveaway is that part 1 needs an *"and also"* clause. ⚠ **A DIVERGENCE between
two named companies sounds causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge and ADM cited side by
side) — and the convergent version is MORE DANGEROUS, because agreement LOOKS LIKE CORROBORATION when
it is in fact the clearest possible statement that the input is a market variable.** ⚠ **The third and
most respectable face is a COMPETITOR'S EARNINGS PRINT** (AutoZone's FQ4 read across to GPC/ORLY/LKQ): a
real, audited, same-morning, company-disclosed number that still tells you about an **industry** and
about **nothing that happened between two parties.** **The giveaway never changes: the sentence needed
an "and also".**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — AND IT IS THE MOST CONVINCING NON-EVENT THE FUNNEL
PRODUCES.** Two of 09-23's six theses died on this premise, from two different agencies on one morning
(CMS's preliminary lab fee schedule; the ACA enrollment halt). ⚠ **This is the FOMC object — an
environment input, not a Company A — but in a far more persuasive costume: a policy action is
SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN AFFECTED INDUSTRY, and MOVES THE TAPE ON THE DAY.** It
nonetheless has **ONE party**, one short of what §4 requires. ⚠ **Both were CUTS: a long-only book
cannot trade money being WITHDRAWN from a sector unless some NAMED party receives it — and nobody does;
the money simply stops being spent. "Who wins when X gets squeezed?" is the tell: every answer needs an
"and also".** ⚠ **09-24 adds the HARDEST CASE and it is worth distinguishing: an FDA advisory vote
(ILMN/GRAIL) is also a regulator's action, but it ENABLES a named company's product and that company has
a named supplier — a real two-party chain rather than money ceasing to be spent. The premise objection is
WEAKER there, which is exactly why part 3 and the priced-in filter are what actually killed it. Do not
over-apply this rule to approvals.**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is **exits-only by
construction** and may not open a position under **any** circumstance. Routine 2 executes **only what
`plan_today.md` already contains** — a position opened at 09:35 without a plan entry routes **around**
the discipline rather than satisfying it. Routine 4 records and journals; it does not trade. ⚠ **Idle
cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an opportunity any of those seats may
act on.** New positions route through pre-market research **plus** the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.**
The gate has been exercised **TWENTY-SIX times and has never fired**, and its alert path **remains
untested code.** ⚠ **Twenty-six quiet opens are NOT evidence it works. The first morning it fires will
by construction be a morning when the pre-market run failed — i.e. exactly the morning with no fresh
notes to lean on. Read routine 2's Step 2 then; do not recall it.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a broker
mark on one leg against an official close on the other. **Both legs from the same source, and for
returns that source is `bars --adjustment all`.**

### Do not reach for these — disposed rejects and the trap in each

⚠ **Added 09-24:** **ILMN** — the GRAIL advisory vote is **non-binding with the FDA decision pending**,
so part 3 is several quarters out; **+11.54% over five sessions, a GENUINE priced-in kill**; ⚠ **the
most seductive second-order shape in weeks, and the thesis was never written because the filter ran
first.** **GRAL** — **first-order**, and **+44.67%**, the largest five-session move ever recorded against
a candidate here. **BBY / PYPL / SHOP** (Meta Muse commerce, Connect 2026) — ⚠ **part 1 passes CLEANLY on
all three and NOT ONE commercial term exists**: no revenue share, minimum, dollar value, volume
commitment or take rate from any party; **the only economics described is Meta taking a fee, a COST at
the retailer**; SHOP also **+9.61% priced-in**. ⚠ **BBY and PYPL would have FAILED the correlation check
against each other — identical driver, one bet in two tickers.** **SoftBank / OpenAI $11.1B** — recipient
**private**, no US-listed party with an allocated figure; the compute-supplier inference is rule (v).
**ELMT / Masan** — **second Elmet event in two sessions**, ~$634M microcap and a Vietnam-listed
counterparty, **§3 on both legs**. **QCOM / PickNik** (no value; QCOM first-order; PickNik private) ·
**RCL / Sandals** (~$3B **capital OUT**; Sandals private) · **Fiserv** Canada (no value) · **NeoVolta /
SK On** (nano-cap, no value, 2027 start) · **Nocera / E-PRO** (Aug 26 allocation, rule (iii); microcap) ·
**Crossject / BARDA** (Euronext, §3) · **Elroy Air** (private; LMT capital OUT; previously announced) ·
**Quanome** (microcap) · **Costco, Jabil, Darden, TD SYNNEX, Vail** (upcoming estimates, no event yet).

⚠ **Added 09-23:** **GIS** — an **own-results earnings print has ONE party**; the only named counterparty
(**Walmart, 22% of GIS sales**) is a **customer at <1% of WMT revenue**. ⚠ **It does not become a buy on a
better quarter.** **LH / DGX** — the CMS lab fee schedule is a **REGULATOR'S ACTION**, rates are
**preliminary for CY2027–2029**, and a **~15% cut has no beneficiary in a long-only book**; ⚠ **LH's
`priced_in: false` on a −3.83% FALL is a near-miss artefact and is NOT the rejection.** **CNC / MOH /
OSCR** — government policy action, **760,000 is industry-wide with no per-company split**, **$2.2B is
money the government STOPS paying**; ⚠ **CNC's `priced_in: true` on a −6.44% FALL is an artefact and is
NOT the rejection.** **ELMT / Tungsten West** — microcap, AIM-listed seller, eight-year term; ⚠ **the
disclosure was COMPLETE and it still failed — do not reach for it as "the well-sourced one."** **LHX** —
named contractor, **first-order**, **no contract value**; ⚠ **the $22.9B RAYTHEON Tomahawk figure is
AUGUST and a DIFFERENT CONTRACTOR — it must never migrate into an LHX entry.** **GFS** — **$100M CHIPS
funding to a third party, allocation undisclosed**, ~1.5% of revenue at best. **Nth Cycle / Glencore**,
**ZEO / Ewyze**, **V2X**, **Boeing / SPEEA**, **MiMedx**, **NIIT tax ruling**, **Michigan oil antitrust
dismissal**, **"SK Hynix eyeing Intel's Ohio site"** — ⚠ **the last is a headline built out of the word
"eyeing"; Micron is attached by a commentator, not a counterparty.**

⚠ **Added 09-22 and earlier:** **ACN** (signatory, first-order, <1% of revenue, ⚠ **`priced_in: true` on
a −4.58% FALL is an artefact and is NOT the rejection**) · **Nscale / Microsoft / Anthropic** (private
parties; 2GW by 2028 / 8GW by 2031 outside part 3) · **Vicor** (below the §3 floor; **licensees unnamed**
— ⚠ **the event had NO defect at all and still produced nothing**) · **GPC / ORLY / LKQ** (AutoZone
read-across, a competitor's print) · **Paramount / WBD** (a payer and no named payee; NFLX and DIS
attached only as competitors) · **Applied Materials** ($5B India, a decade, capital out) · **Vistra / New
Era** (20-year PPA, no value) · **Navitas, Magnachip, Priority Technology** (below the floor) · **Telix /
ITM**, **Capricorn/DNO, BEML/NHSRCL, Welspun/AMC** (not US-listed, §3 outright — ⚠ **the last two were
the only items in their window carrying BOTH named parties AND a disclosed value**) · **HealthEquity,
Lamb Weston, AEP, Nucor, Steel Dynamics, Labcorp, Nordson, Eli Lilly** (prints vs consensus, rule (iii))
· **AMD, Intel, Arm** (+10/+12/+17% on 09-21 with **no transaction underneath** — "renewed AI optimism";
**a record green tape is not a Company A**) · **GNRC** (first-order; see the live item) · **GM** (part 2
unwritable **by both parties' deliberate commercial choice**; ⚠ **the −3.95% is not the reason**) ·
**BE / Bloom** ($25B financing ceiling) · **BG and ADM** (same crush spread) · **GFS and MRVL** (terms
not disclosed) · **LEU / Antares** (deliveries before 2030) · **BLK / TotalEnergies / GIP** (capital in)
· **Lennar and its suppliers** (the same mortgage rate) · **Baker Hughes / Chart** (outside the window) ·
**US Army / Skyeton** (private, no obligated figure) · **the FOMC's +25bp, fund outflows, the data
calendar, Bowman's SVB speech, the enforcement digest** (environment inputs, **not a Company A**).
⚠ **Four loud 09-11 headlines still have no primary source and none has appeared since. Absence of a
source after this long is itself the finding.**

### Established facts — do not re-derive

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional $70,000.00**,
  order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**, verified terminal
  before it was written. Audit record in `trade_log.md`. **No order has ever reached a non-terminal
  state in this account.**
- **The core is deliberately NOT tracked in `positions.md`.** §5 exempts it, so it has no thesis state,
  no timing window and no `highest_close`. ⚠ **Every reconciliation compares SATELLITE blocks to
  SATELLITE Alpaca positions** — a run that compares the raw ledger to the raw broker will read a
  correct ledger as broken.
- **Counters as of 2026-09-24 pre-market, RECOUNTED FROM SOURCE: 67 theses since inception, 0 accepted,
  67 rejected, 21 this week (09-21: 3, 09-22: 5, 09-23: 6, 09-24: 7 — counted per-ID from source, not summed from prior runs); 0 satellite positions ever opened; 0 exits ever; `alerts.md` empty — zero
  open, zero SYSTEMIC.** ⚠ **Recount from `research_log.md` before quoting this anywhere human-facing —
  a run that ADDS theses and a run that COPIES this line forward are different runs, and nothing
  connects them.**
- **`week_of` 2026-09-21, `new_positions_this_week` 0 of 3.** Next boundary **Monday 2026-09-28**.
  The reset does not depend on the Friday review having run. ⚠ **Note the two counters are independent:
  21 theses this week and 0 positions this week are both correct — §6's cap counts POSITIONS OPENED,
  and none was.**
