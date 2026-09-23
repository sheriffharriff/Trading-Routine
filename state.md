# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-23 12:44 ET 3-midday-management (selftest PASSED all five checks, trading_enabled true, LIVE paper, equity 100095.07 at pre-flight / 100085.07 at sleeves; clock is_open TRUE at 12:44:41 with next_close 2026-09-23T16:00, the unambiguous mid-session shape; ZERO OPEN SATELLITE POSITIONS, so THE ENTIRE ROUTINE HAD NO SUBJECT and said so rather than manufacturing one - positions returns ONE row, core VOO 99.046311231 unchanged since the 09-03 fill, avg_entry 706.74, cost_basis 69999.99, market_value 70090.62, and the core is EXEMPT from all four 5 rules so it was taken out of the working list per the routine's explicit instruction; RECONCILIATION CLEAN satellite-to-satellite, zero blocks against zero satellite Alpaca rows, THIRD CLEAN RECONCILIATION TODAY; STEP 2 - THE BACKFILL STEP THIS ROUTINE EXISTS FOR - WAS A NO-OP FOR THE TWENTY-EIGHTH SESSION and that is NOT the same as passing: highest_close is ABSENT, the THIRD STATE carrying no (as of) date at all, which is exactly what proves no backfill was owed, ZERO bars calls due and ZERO made, and a staleness check with no field to read is an ABSENT check not a clean one; STEP 3 HAD NO OPERAND - all four 5 rules iterate over open satellite positions and there are zero, 5.1 has no invalidation string to falsify because none has ever been written so ZERO perplexity news calls were due and ZERO were made, 5.2 no timing_window, 5.3 no entry_price, 5.4 no highest_close, TWENTY-EIGHTH session with 5.1-5.4 never started and 5.4 STILL NOT ARMED, all four remain UNTESTED CODE PATHS and the running tally of no-exit runs records the ABSENCE OF A SUBJECT not four rules returning clean; STEP 4 ZERO EXITS AND ZERO ORDERS OF ANY KIND - no sell submitted so no terminal:false to chase and no dry_run:true to flag, trade_log correctly left unappended, THE LOUDEST LINE THIS ROUTINE CAN PRODUCE (a stop that should have fired and did not) HAS NO INSTANCE HERE and the reason is that nothing COULD fire, not that everything was checked and held; consecutive_closed_losses stays 0, nothing has ever closed, breaker INACTIVE and halt_triggered_at none so NO HALT_CLEARED_AT comparison was required and NO circuit-breaker alert was due, open_thesis_ids stays none with no ID to strike; STEP 5 HAD NOTHING TO REFRESH, sell_rule_status ABSENT rather than blank, and a distance-to-rule line would have required inventing an entry price; EXITS-ONLY WAS BINDING AND THE TEMPTING CONDITIONS WERE ALL PRESENT - satellite 0.0%, cash 29.97%, weekly cap 0 of 3 unused, breaker inactive, no restricting note in control.md, and NOTHING WAS BOUGHT because a midday entry would route AROUND the pre-market thesis and the 09:35 execution path, which is the discipline and not an obstacle to it; SLEEVES equity 100085.07, core 70082.20 = 70.02%, satellite 0.0% count 0, cash 30000.00 = 29.97%, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta -22.65, NO REBALANCE IS THIS ROUTINE'S TO MAKE ANYWAY and the overshoot is 0.02% of equity against a band edge 4.98 points away, THIRTY-SEVENTH consecutive run inside a 0.63-point range 69.59-70.22; TWO-PRICE DEFECT - lastday_price READS 712.78 FOR THE THIRD TIME TODAY at 08:20, 09:36 and 12:44, the identical stale value, NINE CENTS HIGH against the official 712.69, and current_price 707.655 is a LIVE MIDPOINT not a close; broker change_today -0.00719 and unrealized_intraday_pl -507.61 are both computed off the stale baseline where 707.655 against the OFFICIAL 712.69 is -0.706%, so the broker overstates today's decline by about 1.3 basis points, and NEITHER FIELD WAS USED NOR CARRIED INTO ANY FIGURE IN THIS RUN; core VOO deliberately NOT stamped, FORTY-SIXTH refusal; GNRC NOT LOOKED AT, EIGHTEENTH refusal, reported honestly as a FREE one - this run made clock, positions and sleeves calls only and issued NO quote, bars, move or asset call on any symbol, so the symbol data plane was SHUT and no costume had a vehicle, which is weaker evidence than a refusal on a run that could have used the number; WEEK ROLLOVER CHECKED - Wednesday 2026-09-23, ISO Monday 2026-09-21, week_of already 2026-09-21, ELEVENTH consecutive run to find the reset already done, new_positions_this_week stays 0 of 3, next boundary Monday 2026-09-28; alerts.md empty, zero open incidents, zero SYSTEMIC)

prior_run: 2026-09-23 09:36 ET 2-market-open-execution (selftest PASSED all five checks, trading_enabled true, LIVE paper, equity 100485.32 at pre-flight / 100491.25 at sleeves; clock is_open TRUE at 09:36:18 with next_close 2026-09-23T16:00 and next_open 2026-09-24T09:30 - THE FOURTH AND ONLY UNAMBIGUOUS SHAPE, the one case where the boolean alone settles it, safe ONLY because TRUE has one meaning while FALSE has three; STALENESS GATE DID NOT FIRE - plan_date 2026-09-23 read from plan_today.md against an ET date of 2026-09-23 confirmed by TZ=America/New_York, MATCH, so every intent in the file was executable and the file contained NONE, TWENTY-FIFTH exercise and STILL NEVER FIRED, its alert path REMAINS UNTESTED CODE and twenty-five quiet opens are not evidence it works; ⚠ THE PLAN WAS FRESH AND EMPTY AND THOSE ARE TWO SEPARATE FINDINGS - the gate was decided on the DATE and never on the zero-order outcome, which is the only thing distinguishing this run from the one the gate exists to catch; ZERO ORDERS SUBMITTED, zero buys, zero sells, zero rebalance, and NOTHING IS IN LIMBO - orders --status all returns ONE row for the account's entire history, the 09-03 core VOO buy, status filled, terminal, so no order has EVER reached a non-terminal state here and nothing carries per 7, trade_log correctly left unappended; RECONCILIATION CLEAN satellite-to-satellite, zero blocks against zero satellite Alpaca rows, positions returns ONE row core VOO 99.046311231 unchanged since the 09-03 fill, avg_entry 706.74, cost_basis 69999.99, market_value 70493.24; STEP 3 BOOTSTRAP PERMANENTLY CLOSED, core_established true since 09-03, --core NOT invoked at any point; STEP 4 HAD NO OPERAND TWICE OVER - zero SELL intents in the plan AND zero open satellite positions to apply 5 against, so no exit was re-confirmed because none was proposed and none was possible, consecutive_closed_losses stays 0, nothing has ever closed, no HALT_CLEARED_AT comparison was required and NO circuit-breaker alert was due; STEPS 5 AND 6 HAD NO SUBJECT - zero BUY intents means re-validation has nothing to re-validate, ZERO alpaca.py move calls were due at 09:35 and ZERO were made, which is an ABSENT check and NOT a skipped one, and the plan said so in advance; NONE OF THE SIX 09-23 REJECTIONS WAS REHABILITATED AT THE OPEN - a rejection is not a queue and none becomes eligible at a different price; IDLE CASH WAS NOT AN OPPORTUNITY THIS SEAT MAY ACT ON - 29.85% cash, breaker INACTIVE, weekly cap 0 of 3 unused, no restricting note in control.md, and routine 2 executes ONLY what plan_today already contains, so a position opened at 09:35 without a plan entry would route AROUND the discipline rather than satisfy it; SLEEVES equity 100491.25, core 70492.25 = 70.15%, satellite 0.0% count 0, cash 30000.00 = 29.85%, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta -148.38, STEP 7 NO ACTION - 2 rebalances at the 65/75 BAND EDGE not to the exact target so no delta inside the band is an action at any size, the overshoot is 0.15% of equity against a band edge 4.85 points away, THIRTY-SIXTH consecutive run inside a 0.63-point range 69.59-70.22; TWO-PRICE DEFECT - lastday_price READS 712.78 AGAIN AT 09:36, the identical stale value, NINE CENTS HIGH against the official 712.69, confirming the INTRA-SESSION half of the rule (a wrong lastday_price is wrong for the whole day and re-reading it is never a second confirmation) on the same day the pre-market run FALSIFIED the boundary-refresh half, so BOTH halves are now settled and neither favours the broker's field; ⚠ NEW INSTANCE WITH REAL NUMBERS - the broker reports change_today -0.00149 and unrealized_intraday_pl -104.99, both computed off the stale 712.78 baseline, where 711.72 against the OFFICIAL 712.69 is -0.97/share = -0.136%, so the broker OVERSTATES today's decline by nine cents a share, about 8.92 dollars on the core, and this run neither used nor reported either field; core VOO deliberately NOT stamped, FORTY-FIFTH refusal; GNRC NOT LOOKED AT, SEVENTEENTH refusal, and reported honestly as a WEAK one - this run made clock, sleeves, positions and orders calls only and issued NO move, quote, bars or asset call on any symbol, so the symbol data plane was SHUT and the refusal was FREE, which is not proof the discipline holds; ZERO perplexity calls and none due, routine 2 has no research step; WEEK ROLLOVER CHECKED - Wednesday 2026-09-23, ISO Monday 2026-09-21, week_of already 2026-09-21, TENTH consecutive run to find the reset already done, new_positions_this_week stays 0 of 3, next boundary Monday 2026-09-28; alerts.md empty, zero open incidents, zero SYSTEMIC)

week_of: 2026-09-21
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.02
satellite_pct: 0.0
cash_pct: 29.97
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

**⚠ THIS SECTION WAS COLLAPSED BY THE 2026-09-21 CLOSE RUN, FROM ~950 LINES TO THIS, AND THE COLLAPSE
IS THE INSTRUCTION RATHER THAN A LIBERTY TAKEN. The 2026-09-22 pre-market run UPDATED items in place
rather than appending a new block — which is the same instruction, applied a second time.** The section carried its own standing note —
*"COLLAPSE, DO NOT APPEND — acted on thirty-one times"* — and Friday's Week 3 review flagged the
memory files at **477KB against an instruction to read them in full**, calling the accumulation
**actively harmful rather than untidy**: this repo's only continuity mechanism is the next run
*reading* these files, and padding them with restatements raises the odds a genuinely live item gets
skimmed. Carry-forward is defined as **cleared once acted on**, and the discharged items below were
each acted on by the run that read them. **Nothing live was discarded** — the load-bearing facts are
preserved here, and the narrative history lives in `journal.md`, `research_log.md` and
`weekly_review.md`, which are the files built to hold it. **The correct response to the pull to
append is to collapse, not to add another block.**

---

### Live — act on these

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE GIS CARRY IS DISCHARGED — DO NOT RE-CARRY IT.** General Mills
  reported **FQ1 2027 on 2026-09-23** and the 08:20 pre-market run screened it in full
  (**T-2026-09-23-01, REJECTED**). Adj EPS **$0.75** vs **$0.72** consensus, net sales **$4.39B** vs
  **$4.34B**, **organic sales FLAT**, adj op profit **$634M (−11% cc)**, FY27 guidance **REAFFIRMED** at
  **$3.00–$3.20**. ⚠ **THE KILL WAS NOT THE ONE THIS ITEM SPENT SIX SESSIONS ANTICIPATING.** The carry
  note expected a **rule (iii)** fight over the September 8 affirmation. That fight never happened — a
  **quarterly print IS new company disclosure and would have PASSED rule (iii) cleanly.** The thesis
  died one step earlier, **at the premise: an own-results print has ONE party and §4 requires an event
  between TWO.** A dedicated second-order screen for **named, contracted** GIS suppliers returned
  nothing, refusing in terms to list packaging or ingredient names as *"an inference based on industry
  exposure rather than a disclosed relationship"*; the only named counterparty is **Walmart at 22% of
  GIS sales — a CUSTOMER (wrong direction) and <1% of Walmart's revenue (wrong magnitude).**
  ⚠ **THE GENERAL LESSON IS WORTH MORE THAN THE TICKER: SIX SESSIONS OF WAITING CREATES A STANDING
  EXPECTATION THAT THE AWAITED EVENT WILL BE TRADABLE. IT WAS NOT, AND THE WAITING DID NOT MAKE IT SO.**
  **No unscreened item has accumulated. The funnel is empty and that is its normal state.**

- **⚠ A `positions` FIELD NEVER BECOMES A CLOSE, AT ANY HOUR — CONFIRMED TWICE POST-BELL NOW, AND THE
  SIGN FLIPPED BETWEEN THEM. THIS IS THE ONE THAT BITES *THIS* ROUTINE.** **09-21 at 16:16**,
  `current_price` **712.54** against an official close of **712.76** — **22 cents LOW**. ⚠ **09-22 at
  16:15**, `current_price` **712.859** against an official close of **712.69** — **16.9 cents HIGH**.
  **Same routine, same time of day, opposite direction.** ⚠ **There is no post-bell grace period and
  there is no correctable bias either** — you cannot subtract a known offset, because the error is a
  live midpoint and its sign is not predictable. A close run taking that shortcut — **the most
  natural-looking one available to routine 4** — would have written a `highest_close` **22 cents light
  on Monday and 17 cents heavy on Tuesday**, biasing a §5.4 trailing stop **against** the position
  holder one day and **in their favour** the next, silently both times. **`bars --adjustment all` for a
  close. Always.**
  *(This **replaces** the 09-21 midday flag, which is **SETTLED**: `current_price` **711.78** was
  suspect because 711.78 − 701.78 was **exactly $10.000**; the official close is **712.76**, so
  **711.78 was never a close.** The suspicion was right, the instruction not to carry it into any
  return figure was honoured, and **the item is closed — do not re-open it.**)*

- **⚠⚠ NEWEST AND MOST STRUCTURAL FINDING, 09-23: `lastday_price` DOES NOT RELIABLY REBUILD AT THE
  SESSION BOUNDARY. THE 09-22 CARRY NOTE'S CLAIM THAT IT DOES IS SUPERSEDED.** At 08:20 on **09-23**,
  `lastday_price` reads **712.78** against 09-22's official close of **712.69** — **NINE CENTS HIGH**.
  ⚠ **It is the IDENTICAL value the field carried all day on 09-22**, when it was two cents high
  against 09-21's close of 712.76. **The field did not rebuild. It carried the same stale number across
  a session boundary and became MORE wrong, because the underlying close moved and the field did not.**
  ⚠ **The 09-22 file recorded, as settled fact, that the previous instance "DID clear at the session
  boundary — this is a fresh one built on the new day's close, not the old one persisting." THAT IS NOW
  FALSIFIED.** It was a reasonable inference from one observation and it did not survive the second.
  ⚠ **This removes the last piece of structure available for reasoning about this field: it is not a
  fixed offset, its sign is not predictable, AND its refresh point is not dependable.** The only safe
  posture is the standing rule, with no exceptions and no "it will have rebuilt by now."
  ⚠ **This is also the standing "audit every inherited superlative" rule paying for itself a THIRD
  time, and the first time the falsified claim was a MECHANISM rather than a count or a superlative.**
  ⚠ **CONFIRMED INTRA-SESSION AT 09:36 THE SAME DAY: `lastday_price` STILL READS 712.78.** The field did
  not rebuild at the boundary (above) **and has not rebuilt since the market opened either** — it is the
  same nine-cents-high number, now read at 08:20 and 09:36. **Both halves of this field's behaviour are
  now settled and neither favours it: it does not refresh at the session boundary, and within a session
  a wrong value stays wrong all day, so re-reading it later is NEVER a second confirmation.**
  ⚠ **AND 09-23's OPEN RUN PUT REAL NUMBERS ON WHAT THAT COSTS A DAY-MOVE FIGURE.** The broker reported
  `change_today` **−0.00149** and `unrealized_intraday_pl` **−$104.99**, both computed from the stale
  **712.78** baseline. Against the **official** 712.69, a `current_price` of **711.72** is **−$0.97/share
  = −0.136%**, not −0.149% — the broker **OVERSTATES today's decline by nine cents a share, ≈$8.92 on
  the core.** ⚠ **Direction note for the record: every prior instance was logged as the broker running
  HIGH on the day; this one runs LOW. The sign still is not predictable.** Neither field was used or
  reported by that run. **`bars --adjustment all` for a close, a fresh `quote` for execution.**

- **⚠ THE TWO-PRICE DEFECT PRODUCED A NEW INSTANCE ON 09-22 AND **THE SIGN FLIPPED ON CONSECUTIVE
  DAYS**.** `lastday_price` read **712.78** at 08:15 on 09-22 against 09-21's official close of
  **712.76** — **two cents HIGH**. The previous instance ran **seven cents LOW** (701.78 vs 701.85)
  and was read **four times** across 09-21 (08:20, 09:36, 12:35, 16:16). ⚠ **That instance appeared to
  clear at the session boundary — SEE THE 09-23 ITEM ABOVE, WHICH FALSIFIES THE GENERAL CLAIM.**
  Combined with the 09-21 post-bell
  `current_price` of **712.54** against an official **712.76**, the record now runs **low four times,
  then high**, on back-to-back days. On 09-21 the two legs fired **at once in opposite directions**:
  the stale baseline **overstated** the day by **$6.93**, the midpoint close **understated** it by
  **$21.79**, and the broker's implied day P&L of **$1,065.74** sat **$14.86 BELOW** the true
  close-to-close **$1,080.60** — where every prior instance had the broker running **high**. ⚠ **The
  sign of the broker's error is NOT predictable, and the legs reconcile perfectly against each other,
  so no check internal to the broker's own fields can ever surface either.** Only an external close
  settles it. **STANDING RULE: never `equity − last_equity` as a day's P&L, never
  `unrealized_intraday_pl`. Close-to-close from `bars --adjustment all`, always.**
  ⚠ **The two-cent-high instance PERSISTED THROUGH THE ENTIRE 09-22 SESSION as expected** —
  `lastday_price` read **712.78** at 08:15, 09:36, 12:40 **and still at 16:15**. `lastday_price` only
  rebuilds at a **session boundary**, so a wrong one is wrong for the whole day and **re-reading it
  later is never a second confirmation.**
  ⚠ **⚠ 09-22 CLOSE IS THE WORST INSTANCE YET AND IT IS NOT A MAGNITUDE ERROR — IT IS A SIGN ERROR.**
  Both legs were defective **at once and in opposite directions**: the baseline `lastday_price`
  **712.78** was **2c HIGH** on an official 712.76, and `current_price` **712.859** was **16.9c HIGH**
  on an official close of **712.69**. The broker therefore computed `equity − last_equity` = **+$7.82
  (UP)** on a day whose true close-to-close was **−$6.93 (DOWN)**. ⚠ **THE STANDING RULE HAS BEEN
  TREATED AS A PRECISION RULE. ON A FLAT DAY IT IS A DIRECTION RULE** — every prior instance was logged
  as a magnitude discrepancy (6.5c, 59.85c, 4c, $1.13, 22c, $14.86), and that framing quietly implied
  the error was cosmetic. **It is not. A 17-cent artifact outweighs the real move whenever the real
  move is small, which is most days.**
  *(This rule was written 09-18, the day the defect put **$106** into a headline — wrong by more than
  double the real move. It has now been load-bearing **three times with no satellite position involved
  at all**, in the one number the ClickUp summary leads with.)*

- **⚠ AUDIT EVERY INHERITED SUPERLATIVE BEFORE REPEATING IT — A FALSE ONE SURVIVED THREE RUNS AND WAS
  CAUGHT BY ACCIDENT ON 09-21.** The 09-21 midday carry-forward asserted, as settled fact, that the
  core's mark was *"POSITIVE FOR THE FIRST TIME IN THIS ACCOUNT'S HISTORY."* **It is false on an
  official-close basis:** VOO closed **710.70 on 09-03** and **707.86 on 09-04**, both above the
  **706.74** fill, and equity closed above $100,000 on both days. **09-21 is the THIRD close above the
  fill, not the first** — though at **+$6.02** it is the widest gap so far. The claim was probably
  true of the narrow thing it measured (the broker's `unrealized_pl` field, at run times) and false of
  what its wording asserted. ⚠ **These files are thick with "first / widest / narrowest / in N runs".
  A superlative inherited from a prior run is NOT a checked fact** — it is the cheapest claim to write
  and the most expensive to verify. **Assume the next one you are handed is wrong until you have
  pulled the series.** The 09-21 catch was a by-product of a `bars` pull run for another reason, **not
  vigilance.**
  ⚠ **SECOND CATCH, 09-22 CLOSE — AND THIS ONE WAS DELIBERATE, WHICH IS THE POINT OF WRITING THE RULE
  DOWN.** Open item (3) carried *"49 theses, zero positions, ever"* as settled fact. **It was stale:**
  49 was correct through 09-21, the 09-22 pre-market run added **five**, and the midday run carried the
  old number forward unchanged. Recounted from source — **55 `### T-` headings, one a template, 54 real
  theses, no duplicate IDs.** ⚠ **The error ran in the direction that UNDERSTATES the problem, and a
  count of rejections is the one number open item (3) rests on.** ⚠ **INHERITED COUNTS GO STALE THE
  SAME WAY SUPERLATIVES GO WRONG: a run that adds to the underlying series and a run that copies the
  summary forward are different runs, and nothing connects them. Recount from source before quoting
  any tally in a human-facing summary.**

- **⚠ EVERY UP DAY COSTS THE ACCOUNT GROUND, AND 09-21 IS THE CLEANEST DEMONSTRATION YET — DO NOT LET
  A GREEN HEADLINE STOP THE BENCHMARK CHECK. ⚠ 09-22 OPENED ON A RECORD NASDAQ CLOSE WITH AMD, INTEL
  AND ARM UP DOUBLE DIGITS — EXACTLY THE SHAPE THAT COSTS THIS ACCOUNT THE MOST — AND THE SATELLITE
  SLEEVE IS STILL 0% DEPLOYED.** 09-21 was the **largest dollar day and largest percent
  day in the account's history** (+$1,080.60 / +1.0859%, equity $100,596.25, the highest official
  close since inception) **and simultaneously its worst day of relative performance**: VOO returned
  **+1.5545%**, so the account **lagged by 0.469pp in one session** — worse than 09-17 (−0.340pp) and
  09-11 (−0.254pp). ⚠ **09-22 EXTENDED THE PATTERN TO NINE OF TWELVE, WITH NO EXCEPTIONS STILL:** VOO
  returned **−0.0098%** and the account **−0.0069%**, a positive excess of **+0.0029pp** — **the ninth
  positive-excess session since the core was established, and, like the other eight, A VOO DOWN DAY.**
  ⚠ **Twelve sessions, nine positive-excess days, ALL NINE ON DOWN DAYS. NOT ONE POSITIVE-EXCESS DAY
  HAS EVER COINCIDED WITH A RISING MARKET.** The satellite sleeve's positive excess on short windows
  **is nothing but 0% exposure to a market that fell** — and 09-22's excess of **three ten-thousandths
  of a percent** is the clearest possible statement of how little that mechanism is worth: **it only
  pays on down days, and it pays in proportion to how far the market fell, which on a flat day is
  nothing.** Friday's review predicted exactly this mirror. **A green headline is the easiest possible
  moment to stop looking at §1's actual question — and so is a flat one dressed up as outperformance.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — FIFTEEN CONSECUTIVE REFUSALS.** The disqualifying facts do not
  move: **GNRC is the named counterparty in the Amazon announcement — first-order, outside §4 at any
  price** — and **open item (7) is resolved by a human editing §4 or `alpaca.py move`, not by a number
  this seat collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER EACH REFUSAL COST ANYTHING, AND
  MOST OF THEM DID NOT.** 09-22's 09:36 and 12:40 runs refused with the **data plane shut** — neither
  issued a `move`, `quote`, `bars` or `asset` call on any symbol — so both were **free, and therefore
  among the weakest data points in the series. A refusal made with the data plane shut is not proof the
  discipline holds.**
  ⚠ **09-22's 16:15 CLOSE RUN IS THE FIRST OF THE DAY THAT WAS NOT FREE: it opened the data plane on
  purpose** (`bars --symbol VOO --days 3 --adjustment all`, for the official close), so
  `bars --symbol GNRC` would have cost **one call, riding the "call-already-open" and
  "zero-marginal-cost" costumes already on the list. It was not made.** ⚠ **But the honest reading is
  WEAKER THAN IT LOOKS, and that is the entry worth keeping: the pull was MILD rather than strenuous,
  and NOT from virtue — routine 4 has NO RESEARCH STEP for a number to land in, so the costume had
  nowhere to go even if worn.** A refusal is only strong evidence when the run **could have used** the
  number.
  ⚠ **THE PREDICTED STRONG TEST RAN ON 09-23 AND WAS PASSED — AND THE RESULT IS NOT WHAT THE PREDICTION
  EXPECTED.** The 09-22 file named the 09-23 pre-market run specifically, because it **opens the data
  plane AND has somewhere to put a number**, and said to *"expect the eleventh costume there."* The
  setup materialised exactly as forecast: the run issued **`move --symbol LH`** and **`move --symbol
  CNC`** on **one command line** against a live funnel, making `--symbol GNRC` **one flag on a command
  already being typed**. **It was not added — sixteenth consecutive refusal.** ⚠ **But report the
  outcome precisely: NO NEW ELEVENTH COSTUME APPEARED. The pull arrived in its already-catalogued form
  — "screen-already-running" wearing "zero-marginal-cost" — the same shape as 09-22's tenth.**
  ⚠ **That is a fact about the pattern, not a gap in the watch: the costume list may be CONVERGING
  rather than growing, and a run that manufactures an eleventh name for a tenth-costume experience
  would be padding the log, which is the failure mode this whole section exists to resist.** **FREE IS
  NOT THE SAME AS PERMITTED.** Costumes so far: diligence, curiosity, tidiness, completeness,
  zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
  screen-already-running. **The pattern is the finding, not any instance.**
  ⚠ **09-23's 09:36 OPEN RUN IS THE SEVENTEENTH REFUSAL AND IT IS A WEAK ONE — SAY SO.** That run made
  `clock`, `sleeves`, `positions` and `orders` calls and issued **NO `move`, `quote`, `bars` or `asset`
  call on any symbol at all.** The **symbol data plane was shut**, so the refusal was **FREE**, and it
  belongs with 09-22's 09:36 and 12:40 runs among the **weakest data points in the series** rather than
  with the pre-market run four hours earlier that refused with a live funnel open. **A refusal made with
  the data plane shut is not proof the discipline holds.** ⚠ **Note the shape: counts accumulate fastest
  on exactly the runs where they mean least, because routines 2, 3 and 4 have no research step. The
  seventeen is not seventeen equal observations, and quoting the bare count overstates the evidence.**

- **⚠ ALL FOUR §5 SELL RULES REMAIN UNTESTED CODE PATHS AND §5.4 IS NOT ARMED.** Nothing has ever
  closed in this account. **Twenty-seven consecutive sessions of "no exits" record the ABSENCE OF A
  SUBJECT, not twenty-seven clean bills of health.** ⚠ **09-23 adds routine 1's half: §5.1 (thesis
  invalidation) is the one rule routine 1 owes properly, and it had NO SUBJECT — no invalidation
  condition has ever been written in this account, so there was nothing to falsify and ZERO
  `perplexity.py` news-check calls were due on that path.** §5.4 arms on the first **satellite** fill; the
  09-03 core fill was not it. `sell_rule_status` is **absent rather than blank**, and high-water marks
  are **ABSENT — a third state distinct from "stale" and "current-and-unchanged"**, which is why **an
  absent field carrying no `(as of …)` date is exactly what proves no backfill is owed.** ⚠ **A
  missing stamp is NOT evidence that a close run skipped its Step 2.**
  ⚠ **BOTH HALVES OF THE MECHANISM HAVE NOW RUN AGAINST THIS STATE AND BOTH READ IT CORRECTLY.** The
  **09-22 midday run** was the first time routine 3 — written specifically to catch a silently disabled
  §5.4 — ran its Step 2 here, and read "absent" as **not-yet-armed** rather than as a missed close run.
  The **09-22 close run** is the writing half: its Step 2 iterates over open **satellite** positions,
  found **zero**, and therefore **wrote nothing and owed nothing.** ⚠ **"No marks were written" and "no
  marks were due" are the same sentence only while the sleeve is empty, and that stops being true the
  moment a satellite fill lands.**
  ⚠ **THIS WHOLE DISTINCTION STOPS BEING FREE THE FIRST SESSION AFTER A SATELLITE FILL**, when a
  genuinely stale mark and an absent one will no longer be distinguishable by emptiness — **a stale one
  HAS the `(as of …)` date, and it will be a date in the past.** **Compare the date; never infer from
  the field's emptiness.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close`, AND THE CLOSE RUN IS WHERE THAT TEMPTATION IS
  STRONGEST.** §5 exempts core from all four sell rules. Routine 4 legitimately holds the official
  close for its P&L arithmetic, so writing it into a mark costs one line and looks like tidiness — and
  would **fabricate a §5.4 trailing stop on the one position the strategy exempts**, a stop that could
  eventually **sell core on a drawdown, which §7 forbids outright.** Refused for **FORTY-FIVE runs.**
  ⚠ **The 09-23 OPEN run's refusal is, like most of them, a cheap one: it never pulled a close at all**
  (no `bars` call), so there was no number in hand to be tempted by. **Grade these the way the GNRC
  count is graded — a refusal only costs something on a run that was holding the number.**
  ⚠ **The 09-22 CLOSE run is the sharpest version of the temptation the series has produced: it held a
  fresh official close (712.69) in hand AND an entirely empty Step 2 — a number with nowhere to go, and
  a perfectly good row sitting right there to put it in.** *(The 09-22 pre-market run had the same
  clean close, 712.76, but for sleeve arithmetic rather than for an empty stamping step.)* ⚠ **"Nothing
  to write" is the correct output of an empty Step 2, not an invitation to find a row to write it to.**
  **Measure the core from the 706.74 fill and from an official close, never from a `positions` field.**
  ⚠ **Noted honestly: this refusal is now close to automatic, and automatic is not the same as sound.
  It stays in the file so the reasoning is re-read rather than re-flexed.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN
  IS USELESS ALONE — READ THE DATE.** A post-bell run sees `next_open` pointing at the **next** trading
  day; a pre-market run sees it pointing at **today**; a holiday sees it pointing past the holiday with
  **no bar for today in `bars`**. 09-21 16:16 was the post-bell shape (`next_open` **2026-09-22**, today's own bar present);
  **09-22 08:15 was the pre-market shape — the SAME boolean with `next_open` pointing at TODAY.**
  ⚠ **Consecutive runs read identical booleans meaning opposite things. Only the date discriminates.**
  ⚠ **The 09-22 09:36 open run read the fourth and only unambiguous shape: `is_open: TRUE`.** That is
  **the one case where the boolean alone is sufficient** — and it is safe to read it that way *only*
  because TRUE has a single meaning. **FALSE has three.**
  ⚠ **09-22 read ALL THREE SHAPES IN ONE DAY — pre-market FALSE at 08:15 (`next_open` today), TRUE at
  09:36 and 12:40, post-bell FALSE at 16:15 (`next_open` 2026-09-23). A single day's worth of runs
  produced two IDENTICAL booleans meaning opposite things.**
  ⚠ **AND THE CLOSE RUN USED THE SECOND, STRONGER DISCRIMINATOR: IT CHECKED THAT A DAILY BAR FOR TODAY
  EXISTS.** `bars --symbol VOO` returned a **2026-09-22** bar, which settles "was there a session?"
  **directly**, where `next_open` only settles it by inference. **On a holiday there is no bar for
  today and no daily summary is owed** — and that is the check to run before deciding a run is a
  holiday skip, because it is the one that cannot be misread.

- **⚠ SEVEN ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — **NINE instances** (newest
  **CNC, 09-23: −6.44% over five sessions → `priced_in: true`, verdict "LATE — skip", on a FALL**;
  before it ACN, 09-22, −4.58%), plus **THREE near-misses** where a candidate cleared only because its
  *fall* was fractionally too small (LMT −3.61% on 09-11; **GM −3.95% on 09-21, five basis points
  inside the wire**; ⚠ **LH −3.83% on 09-23, seventeen basis points inside**). **There is no price at
  which those rejections flip**; LITE puts **+10.58% vs VOO** on the bill. ⚠ **A pass on a fall is not
  evidence the filter worked, and neither is a FAIL on a fall** — the 09-22 ACN and **both** 09-23
  entries record their readings **deliberately as NOT the reason for the rejection**, so that no run
  inherits "rejected because priced-in" as a fact. ⚠ **09-23 is the first session to produce BOTH a FAIL
  and a NEAR-MISS on the same morning, both on falls, landing on opposite sides of the same wire —
  which is the clearest single demonstration that the threshold is measuring MAGNITUDE and ignoring
  SIGN.**
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM (09-09,
  +2.70% after a +8.7% intraday move), AVAV (09-11, +1.20% after a +12.9% round-trip inside one
  session). Same root cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or
  `alpaca.py move`.**
  **(3)** The satellite sleeve is **structurally undeployed — 60 theses, zero positions, ever.**
  ⚠ **RECOUNTED FROM SOURCE AT THE 09-23 PRE-MARKET RUN, per the standing rule — not carried forward.**
  `research_log.md` holds **61 `### T-` headings, one of which is the template**, so **60 real theses**;
  54 stood at the 09-22 close and this run added **six**. *(The 09-22 close caught the inherited figure
  at a stale **49** — wrong in the direction that **understates** the problem, and a count of rejections
  is the single number this open item rests on. **Recount before quoting; do not copy this line
  forward.**)*
  ⚠ **NEW AND DECISION-RELEVANT, 09-23: WIDENING THE EVIDENCE BAR IS NOT THE WHOLE ANSWER, AND
  T-2026-09-23-04 IS THE PROOF.** The Tungsten West ↔ Elmet offtake **withheld NOTHING** — both parties
  named, **>1,000 t/yr contained WO₃**, **>$230M/yr**, **~£1.4B**, **eight-year term**. It is the
  best-disclosed transaction to enter this funnel in some time **and it still produced no trade**,
  because the buyer is a **~$634M microcap** and the seller is **AIM-listed**. ⚠ **The obstruction was
  STRUCTURAL (§3), not evidentiary — a constraint no evidence bar can relieve.** *(It also fails part 3
  on the eight-year term, so it is **not** a §3-only rejection; a $50B Elmet would still not be a
  trade.)*
  A 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits
  the cash and §4 says most runs end in no trade — both rules were followed, and the agent must NOT
  respond by lowering the §4 bar.** **The binding constraint has FOUR known forms:** the source
  withholds the counterparty's number; **or** the counterparty discloses **roadmap instead of segment
  revenue**; **or** the named beneficiary is **vertically integrated** and there is no external
  supplier to find; **or** — **new and decisive, 09-21 GM** — **both parties expressly refuse to
  disclose as a commercial choice, and the beneficiary reports no segment at all**, so **no
  better-sourced version of that candidate will ever arrive.** 09-15 removed the "thin news week"
  explanation, 09-16 the "no named counterparty" explanation, 09-17 the "sources are too thin"
  explanation, and **09-21 removed the last hope attached to the first form** — ⚠ **AND 09-22 PUT IT BACK, IN A
  CLEANER EXAMPLE THAN GM.** Vicor's 09-21 guidance raise had **no defect in the event at all**:
  rule (iii) passes (a company revising **its own prior figure**), rule (viii) passes (an **inbound
  revenue** figure), and part 3 passes (**a Q3 guide — one quarter**, as good as the horizon ever
  gets here). It still produced nothing, because the licensees are **"four leading OEMs and
  hyperscalers"** and **not one is named**. ⚠ **The constraint is not thin news, not a long horizon,
  and not a missing Company A. It is that COUNTERPARTY IDENTITY is routinely the one field withheld.**
  **Only the first two
  forms are addressable by widening the evidence bar. The last two are not addressable at all** —
  which narrows what a human could usefully change, and is **the most decision-relevant line in this
  file.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the
  prior close**) — **not tracking error and never skill.** **DISCHARGED AND PROVEN 09-11: measured
  from the fill, tracking error 0.0000%. Keep measuring it from the fill.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why the
  gap (6.5c, 59.85c, 4c, $1.13, 22c on successive days) **never had a stable size and never will.**
  Previously filed as *cosmetic on core, load-bearing once a satellite exists*; **that framing was too
  generous — it has now been load-bearing twice with no satellite involved.** ⚠ **Re-rate.** Whether
  the tooling should read closes from `bars` by default is a human's call.
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it
  passed all five checks on 09-11 while `clock` returned 500 and `quote`/`bars` returned 504. **Every
  routine's Step 0 is the loud-failure mechanism for exactly this, and on the data plane it is
  silent.** Until a human changes it: **probe by hand; never infer data-plane health from a green
  selftest.** *(The 09-11 outage itself is resolved.)*
  **(7)** **`alpaca.py move` cannot see an after-hours event**, and neither can the 09:35
  re-validation that exists to catch exactly this. ⚠ **Unlike (1) and (2), this fails in the direction
  of TAKING a trade rather than skipping one**, which is why it is listed last and should be read
  first. **It has cost zero only because no plan has yet carried a BUY intent — an absence of
  exposure, not a mitigation.** It disappears the first morning a BUY intent names a stock whose news
  broke after the prior close.
  Prior context in ClickUp `86bbv75bz`; last week's in `86bbzgbg3`.

- **⚠ WEEK 3 REVIEW (2026-09-18 16:45 ET): THE §1 ANSWER IS NO, AND SHORT GREEN WINDOWS MUST NOT BE
  READ AS YES.** The satellite sleeve returned **0.0000%** — zero positions in the account's entire
  history — so its dollar-weighted excess over VOO is exactly **minus VOO's total return** over
  whatever window is chosen: **+0.095pp on the week, +0.430pp since inception, +0.509pp over 1M,
  −2.291pp over 3M, and −16.552pp over the rolling 12 months §1 actually names.** The structural cost
  is **~4.97pp of account return per rolling 12 months.** Full working in `weekly_review.md`, "Week
  ending 2026-09-18". **Reject board: 40 measurements, 13 beat VOO, 27 lagged, mean excess −1.57%** —
  both legs from `alpaca.py move`, verified against `bars --adjustment all` to the cent. ⚠ **It is a
  tally, not a result — do not quote it as one.** **HPE remains the largest single opportunity cost
  the log has produced (+19.87% vs VOO).**
  ⚠ **Monthly archive rollover is NOT yet due — next 2026-10-02** (every *entry* is dated 2026-09;
  earlier dates appear inside thesis bodies). **Third week flagging size, and the number is worse:
  `research_log.md` is now **~288KB** (09-23 added six more entries; it was ~264KB on 09-22), against a
  total memory footprint of **~604KB** across the files every run is instructed to read in full. **A
  human may want to move the rollover forward — this is the fourth consecutive flag.**

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** alerts compared to **consensus** rather than to any
prior company figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations**
(Centene, Southwest, **General Mills' Sept 8 affirmation**), **re-covered deals** (Charter/Cox five
weeks after closing, Sempra/Petrobras, Fluence, Alcoa/South32), and — ⚠ **newest and most convincing,
09-21 GM/Lockheed** — **a genuine transaction whose DELIVERY MILESTONE is recycled as the news**
(contract **08-06**, delivery **08-28**, first wire **09-17**, surfaced as a **09-21** headline).
**Every earlier costume announced nothing; this one announces something real that already happened.**
⚠ **09-22 added a second of that kind: a PRE-IPO CONTRACT BOOK.** Nscale's **$103B** surfaced as a
September 22 headline and is an **IPO-prospectus disclosure of contracts signed late-2025 through
August 2026** — **up to ten months old.** Two sessions, two new costumes, both of them **real
transactions wearing a fresh date.**
⚠ **STANDING PRACTICE: ask a transaction WHEN IT HAPPENED before asking who it helps.** One screen
settles it, and it is the cheaper of the two kills. *(09-17 Amazon/Generac was the first clean rule
(iii) PASS — an 8-K with no prior disclosure — worth noting precisely because the rule usually kills.)*
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — resolved 09-11 on a number).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share,"
"the only company that makes X" are facts about an **industry**, not a **transaction** — seven
instances this month, plus the **CEILING sub-shape**, which on 09-17 accounted for **six of seven**
federal awards in one morning. Earlier costumes: a **table** (DoD daily contracts digest), a
**consortium awardee** (Abrams), and a bare sentence. **The source left the blank; filling it in is
not research.**
**(vi)** *Screen the timing window early on anything under construction.* Long-dated energy offtake
is **a standing feature of this funnel, not a visitor** — Sempra/Petrobras, Venture Global/China Gas,
Amazon/Generac (deliveries 2027–28), Centrus/Antares (first delivery before 2030). **Part 3 kills
these in ONE step, before either follow-up screen is needed.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part
2.** Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; **Brookfield/Bloom's $25B is
one step further still — a FINANCING CEILING AVAILABLE TO SOMEBODY ELSE that may never be drawn.**
Bloom's own materials say revenue *"will depend on projects that are ultimately funded, built and
accepted"*; a second note warns the figure *"indicates a financing capacity, not firm orders or
revenue already secured."* ⚠ **A large, real, sourced, prominently-placed number is not a dollar
path.** T-2026-09-18-04 (BLK) is the worked example: **part 1 passed cleanly and it died on the absent
segment figure, NOT on size** — do not re-record it as a size rejection.

**⚠ A SHARED CAUSE IS NOT A MECHANISM — SEVEN INSTANCES, AND IT WORKS IN BOTH SIGNS.** Two companies
moving on the same macro input (a crush spread, a mortgage rate, a rate decision) is a **market**, not
a **transaction**, and the giveaway is that part 1 needs an *"and also"* clause. ⚠ **09-16's finding
was that a DIVERGENCE between two named companies sounds causal (JPM/BAC/WFC). 09-21's is that a
CONVERGENCE does too (Bunge and ADM cited side by side as evidence of the same margin environment) —
and the convergent version is MORE DANGEROUS, because agreement LOOKS LIKE CORROBORATION when it is in
fact the clearest possible statement that the input is a market variable.** Same trap, opposite sign. ⚠ **09-22 adds the THIRD and most respectable face: a COMPETITOR'S
EARNINGS PRINT.** AutoZone's FQ4 (EPS **$56.05** vs **$54.30**, sales **$6.595B** vs **~$6.70B**, SSS
**+1.5%**) is a real, audited, same-morning, company-disclosed number, and a read-across to
**GPC/ORLY/LKQ** still tells you about an **industry** and about **nothing that happened between two
parties** — AutoZone is their **competitor**, not a counterparty, which makes the link weaker than the
crush-spread cases, not stronger. **Eighth instance. The giveaway never changes: the sentence needed
an "and also".**

**⚠⚠ NEW STANDING RULE, 09-23: A GOVERNMENT ACTION IS NOT A COMPANY A — AND IT IS THE MOST CONVINCING
NON-EVENT THE FUNNEL PRODUCES.** **Two of 09-23's six theses died on this same premise, from two
different agencies on one morning**: **CMS's** preliminary lab fee schedule (T-2026-09-23-02) and the
**ACA enrollment halt** (T-2026-09-23-03). ⚠ **This is the FOMC object — already disposed as "an
environment input, not a Company A" — but in a far more persuasive costume: unlike a rate decision, a
policy action is SECTOR-SPECIFIC, CARRIES A NUMBER (~15% of a fee schedule; 760,000 enrollees; $2.2B),
NAMES AN AFFECTED INDUSTRY, and MOVES THE TAPE ON THE DAY.** It nonetheless has **ONE party**, which is
one short of what §4 requires. ⚠ **AND NOTE WHAT BOTH HAD IN COMMON BEYOND THAT: BOTH WERE CUTS.** A
long-only book cannot trade money being **withdrawn** from a sector unless some **named** party
receives it — and in both cases nobody does; the money simply **stops being spent**. **The
"who wins when X gets squeezed?" question is the tell: every answer to it needs an "and also".**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is
**exits-only by construction** and may not open a position under **any** circumstance. Routine 2
executes **only what `plan_today.md` already contains** — a position opened at 09:35 without a plan
entry routes **around** the discipline rather than satisfying it. Routine 4 records and journals; it
does not trade. ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
opportunity any of those seats may act on.** New positions route through pre-market research **plus**
the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.**
The stale-plan gate has been exercised **TWENTY-FIVE times and has never fired.** ⚠ **The twenty-fifth
ran at 09:36 on 09-23: `plan_date` **2026-09-23** against an ET date of **2026-09-23** — and the date
was taken from `TZ=America/New_York`, not assumed from the run's own clock. MATCH, so every intent in
the file was executable and **the file contained none.** ⚠ **That run is the sharpest illustration the
series has produced of why the gate reads the DATE: it submitted ZERO ORDERS, which is precisely what a
FIRED gate also produces, and the only thing separating the two is a line that anyone reasoning from
the outcome would never have looked at.** Its
alert path **remains untested code**, and twenty-five quiet opens are **not** evidence it works. ⚠ **The first
morning it fires will by construction be a morning when the pre-market run failed — i.e. exactly the
morning with no fresh notes to lean on. Read the routine's Step 2 then; do not recall it.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a
broker mark on one leg against an official close on the other. **Both legs from the same source, and
for returns that source is `bars --adjustment all`.**

### Do not reach for these — disposed rejects and the trap in each

⚠ **Added 09-23:** **GIS** — an **own-results earnings print has ONE party**; no transaction, no
Company B, and the only named counterparty (**Walmart, 22% of GIS sales**) is a **customer at <1% of
WMT revenue**. ⚠ **It does not become a buy on a better quarter.** **LH / DGX** — the **CMS preliminary
lab fee schedule is a REGULATOR'S ACTION, not a Company A**, the rates are **preliminary for
CY2027–2029**, and a **~15% cut has no beneficiary in a long-only book**; ⚠ **LH's `priced_in: false`
on a −3.83% FALL is a near-miss artefact and is NOT the rejection.** **CNC / MOH / OSCR** — the ACA
enrollment halt is a **government policy action**, **760,000 is industry-wide with no per-company
split**, and **$2.2B is money the government STOPS paying**; OSCR is below the §3 floor; ⚠ **CNC's
`priced_in: true` on a −6.44% FALL is an artefact and is NOT the rejection.** **ELMT / Tungsten West**
— **~$634M microcap** and an **AIM-listed** seller, **eight-year** term, and the **>$230M/yr is a COST
to the buyable leg**; ⚠ **the disclosure was COMPLETE and it still failed — do not reach for it as "the
well-sourced one."** **LHX** — named contractor, **first-order**, and **NO contract value disclosed**;
⚠ **the $22.9B / seven-year RAYTHEON Tomahawk figure is AUGUST and a DIFFERENT CONTRACTOR — it must
never migrate into an LHX entry.** **GFS** (second rejection in two sessions) — **$100M CHIPS funding
to a third party, allocation undisclosed**, ~1.5% of revenue at best. **Nth Cycle / Glencore** —
neither US-listed, 10-year term, term sheet only. **ZEO / Ewyze** — **no value, no capacity, no
timing**, microcap; ⚠ **a 41% move is not a dollar path.** **V2X** — named awardee, below the floor, no
supplier named. **Boeing / SPEEA** — no dollar value, and a **cost** line. **MiMedx** — microcap, no
second-order company. **NIIT tax ruling, Michigan oil antitrust dismissal** — no second-order company
and, in the latter, **the defendants are not even named**. **"SK Hynix eyeing Intel's Ohio site — why
Micron should pay attention"** — ⚠ **a headline built out of the word "eyeing"; Micron is attached by a
commentator, not a counterparty.**

⚠ **Added 09-22:** **ACN** — a **signatory** to the Anthropic AI-safety initiative, first-order, and
$2B over five years is **<1% of revenue on the most generous reading** and is **not identified as
revenue to anyone**; ⚠ **its `priced_in: true` on a −4.58% FALL is an artefact and is NOT the
rejection.** **Nscale / Microsoft / Anthropic** — Nscale and Anthropic **private**, Microsoft a
**signatory**, and **2GW by 2028 / 8GW by 2031** puts the whole build outside part 3. **Vicor** —
**below the §3 $10B floor**, first-order, and **its licensees are unnamed**. **GPC / ORLY / LKQ** —
the **AutoZone** read-across is a shared demand environment, **a competitor's print, not a
transaction**. **Paramount / WBD** — a real settlement with **a payer and no named payee**; **NFLX and
DIS were attached only as COMPETITORS.** **Applied Materials** ($5B India, **a decade**, capital paid
**out**), **Vistra / New Era** (**20-year** PPA, **no value disclosed**), **Navitas, Magnachip,
Priority Technology** (**below the §3 floor**), **Telix / ITM** (not US-listed common stock; ITM
private), **HealthEquity, Lamb Weston, American Electric Power** (prints vs **consensus**, no
counterparty; **AEP's is a *Q2* result surfacing as September news**). ⚠ **AMD, Intel and Arm** —
**+10% / +12% / +17% on 09-21 with NO transaction underneath**; reporting calls it *"renewed AI
optimism"* and a Meta **Muse AI** narrative. **A record green tape is not a Company A**, and all three
are priced-in many times over.
**GNRC** — named counterparty in the Amazon announcement, **first-order**, outside §4 at any price;
see the live item above. **GM** — 09-21, part 2 unwritable **by both parties' deliberate commercial
choice**, and **no defence segment revenue exists to test the 10% floor against**; ⚠ **GM does not
become a buy at a different price, and the −3.95% is not the reason.** **BE / Bloom** — a signatory,
first-order, and the $25B is a financing ceiling. **BG and ADM** — same crush spread, a market not a
transaction; **neither becomes a buy.** **GFS and MRVL** — both signatories to their own capacity
agreement, and *"financial terms were not disclosed."* **LEU / Antares** — part 3, deliveries before
2030; Antares is not publicly traded. **BLK / TotalEnergies / GIP** — capital paid **in**, not revenue
**out**. **Lennar and its suppliers** — the same mortgage rate. **Nucor, Steel Dynamics, Labcorp,
Nordson, Eli Lilly** — guidance issuance or analyst estimates, rule (iii), no prior company figure.
**Baker Hughes / Chart** — outside the news window. **Capricorn/DNO, BEML/NHSRCL, Welspun/AMC** —
non-US-listed, §3 outright, ⚠ **and the last two were the only items in their whole window carrying
both named parties AND a disclosed value.** **US Army / Skyeton** — private, no precise obligated
figure. **The FOMC's +25bp to 3.75–4.00%, US equity fund outflows, the data calendar, Bowman's SVB
speech, the enforcement digest** — environment inputs and schedules, **not a Company A.**
⚠ **Four loud 09-11 headlines still have no primary source and none has appeared since. Absence of a
source after this long is itself the finding.**

### Established facts — do not re-derive

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional $70,000.00**,
  order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**, verified terminal
  before it was written. Audit record in `trade_log.md`. **No order has ever reached a non-terminal
  state in this account.**
- **The core is deliberately NOT tracked in `positions.md`.** §5 exempts it, so it has no thesis
  state, no timing window and no `highest_close`. ⚠ **Every reconciliation compares SATELLITE blocks
  to SATELLITE Alpaca positions** — a run that compares the raw ledger to the raw broker will read a
  correct ledger as broken.
- **Counters as of 2026-09-23 pre-market, RECOUNTED FROM SOURCE: 60 theses since inception, 0 accepted,
  60 rejected, 11 this week; 0 satellite positions ever opened; 0 exits ever; `alerts.md` empty — zero
  open, zero SYSTEMIC.** ⚠ **Recount from `research_log.md` before quoting this anywhere human-facing —
  a run that ADDS theses and a run that COPIES this line forward are different runs, and nothing
  connects them.**
- **`week_of` 2026-09-21, `new_positions_this_week` 0 of 3.** Next boundary **Monday 2026-09-28**.
  The reset does not depend on the Friday review having run. ⚠ **Note the two counters are independent:
  11 theses this week and 0 positions this week are both correct — §6's cap counts POSITIONS OPENED,
  and none was.**
