# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-22 16:15 ET 4-market-close-journal (selftest PASSED all five checks, trading_enabled true, LIVE paper, equity 100606.05 broker mark at pre-flight; clock is_open FALSE at 16:15:55 with next_open 2026-09-23T09:30 - the POST-BELL shape, and the boolean is IDENTICAL on a holiday, so the date discriminated and the THIRD discriminator was checked directly: a VOO daily bar for 2026-09-22 EXISTS, so a session happened and the summary was owed; STEP 2 - RECORD THE CLOSES - HAD NO OPERAND AND THAT IS THE FINDING: zero open satellite positions, so ZERO high-water marks were written and ZERO were due, and the marks remain ABSENT, a THIRD STATE distinct from stale and from current-and-unchanged, carrying no (as of) date, which is exactly what PROVES no backfill is owed to tomorrow's runs; 5.4 STILL NOT ARMED, twenty-sixth session with 5.1-5.4 never started, sell_rule_status ABSENT rather than blank, all four still untested code paths; core VOO deliberately NOT stamped, forty-third run, refused at the close which is where the pull is strongest because this is the run holding a fresh official close with nowhere to put it; DAY NUMBERS ON OFFICIAL CLOSES BOTH LEGS - VOO closed 712.69 against 712.76, DOWN 7 cents -0.0098%, equity 100589.32, day P&L -6.93 (-0.0069%), since inception +589.32 (+0.589%), core unrealized +589.33 (+0.842%) from the 706.74 fill; THE BROKER SAID THE DAY WAS UP AND IT WAS DOWN - equity minus last_equity reads +7.82 because BOTH LEGS ARE DEFECTIVE AT ONCE, current_price 712.859 is an after-hours MIDPOINT 16.9c ABOVE the official close and lastday_price 712.78 is the stale two-cents-high value that persisted all session, and the two compound into a FLIPPED SIGN rather than a magnitude error; HAD A SATELLITE POSITION EXISTED, stamping current_price would have written 712.859 instead of 712.69 and handed the position 17c of free room on its 5.4 stop, silently and in its favour - the first time that risk has been shown with real numbers; SLEEVES on the official close equity 100589.32, core 70589.32 = 70.18%, satellite 0.0% count 0, cash 30000.00 = 29.82%, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta -181.82, NO REBALANCE DUE TOMORROW - 0.18% of equity above target against a band edge 4.82 points away, and 2 rebalances at the BAND EDGE not to the exact target, thirty-fourth consecutive run inside a 0.63-point range 69.59-70.22; PLAN VERSUS OUTCOME MATCH EXACTLY - plan_today carried zero BUY, zero SELL, zero REBALANCE intents and zero orders were submitted at any of today's four runs; ZERO ORDERS, NOTHING IN LIMBO - orders --status all returns ONE row for the account's entire history, the 09-03 core VOO buy, status filled, terminal, and no order is in a non-terminal state anywhere in this account's history, so nothing carries overnight per 7; trade_log correctly left unappended, a run with no fill writes no trade entry; NOTHING CLOSED TODAY AND NOTHING HAS EVER CLOSED so consecutive_closed_losses stayed 0, no HALT_CLEARED_AT comparison was required and NO circuit-breaker alert was due; week_of 2026-09-21 matched today's Monday anchor, EIGHTH consecutive run to find the reset already done, new_positions_this_week stays 0 of 3, next boundary Monday 2026-09-28; journal.md entry appended; ClickUp daily summary task 86bc5e1j9 created; GNRC NOT LOOKED AT, FIFTEENTH refusal, and TODAY'S THIRD IS THE FIRST THAT WAS NOT FREE because this run OPENED THE DATA PLANE ON PURPOSE for bars --symbol VOO - but reported honestly the pull was MILD not strenuous and not from virtue, because routine 4 has no research step for the number to land in, so the costume had nowhere to go; zero perplexity calls)

prior_run: 2026-09-22 12:40 ET 3-midday-management (selftest PASSED, equity 100558.61; clock is_open TRUE at 12:40:50 - the INTRADAY shape, the only one of the four where the boolean alone is sufficient; ZERO SATELLITE POSITIONS THEREFORE NOTHING TO MANAGE and the run stopped there, steps 2-5 each had NO OPERAND; zero perplexity calls and zero quote/bars/move/asset calls on any symbol - 5.1 has a subject only when an invalidation condition exists to falsify; THIS RUN MAY NOT OPEN A POSITION AND 29.83% IDLE CASH IS NOT AN ARGUMENT THAT IT SHOULD, routine 3 is EXITS ONLY and the binding constraint was THE ABSENCE OF AN ELIGIBLE CANDIDATE which that routine may not relieve; reconciliation clean satellite-to-satellite; ROUTINE 3's STEP 2 - the step written to catch a silently disabled trailing stop - found the disabled-looking state and CORRECTLY READ IT AS NOT-YET-ARMED. BEFORE IT, 09:36 ET 2-market-open-execution: plan FRESH (plan_date matched, staleness gate exercised for the TWENTY-FOURTH time and DID NOT FIRE, its alert path REMAINS UNTESTED CODE) and EMPTY - two separate findings, since a fresh empty plan and a stale plan produce an IDENTICAL zero-order run, which is why the gate is decided on the DATE and never on the outcome; zero orders; core_established TRUE so Step 3 bootstrap is PERMANENTLY CLOSED. BEFORE THAT, 08:15 ET 1-premarket-research: 5 THESES, 0 ACCEPTED 5 REJECTED - T-2026-09-22-01 Paramount/WBD settlement died at PART 2, the mandated ~300M/yr of US production spend has A PAYER AND NO NAMED PAYEE; T-2026-09-22-02 ACN died at the PREMISE, ACN IS A SIGNATORY and therefore FIRST-ORDER, and independently at PART 2 (~400M/yr against >60B, under 1% vs the 10% floor) and PART 3 (five years); T-2026-09-22-03 Nscale's ~103B pre-IPO contract book died at PART 3 IN ONE STEP per standing rule (vi), contracts up to TEN MONTHS OLD; T-2026-09-22-04 Vicor died at PART 1 on rule (v), licensees NOT ONE NAMED - THE MOST INSTRUCTIVE REJECTION OF THE DAY because THE EVENT HAD NO DEFECT AT ALL and it still produced nothing, since THE ONE FIELD THAT WOULD MAKE IT TRADABLE IS THE FIELD THE SOURCE WITHHOLDS; T-2026-09-22-05 GPC/ORLY/LKQ off the AutoZone print died at PART 1, EIGHTH shared-cause instance and a NEW SUB-SHAPE, a COMPETITOR'S PRINT; EIGHTH instance of open item (1), move --symbol ACN returned priced_in TRUE on a -4.58% FALL, recorded deliberately as NOT the reason for the rejection)

week_of: 2026-09-21
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.18
satellite_pct: 0.0
cash_pct: 29.82
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

- **⚠ THE ONLY LIVE RESEARCH ITEM: GENERAL MILLS Q1 FY2027 PRINTS **TOMORROW MORNING**, 2026-09-23 —
  AND TOMORROW'S 08:15 PRE-MARKET RUN IS THE ONE THIS HAS BEEN CARRIED TO FOR SIX SESSIONS. DO NOT LET
  IT SLIDE AGAIN.** GIS has **not reported**; consensus is **$0.72 EPS** (against **$0.86** a year
  earlier) on **~$4.34B** revenue, and **every figure in circulation is an analyst expectation**. Its
  only company statement is the **September 8 affirmation** of FY27 adj. EPS $3.00–$3.20 — **an
  affirmation, standing rule (iii)**, the Centene and Southwest shape. **Nothing was screenable until
  the print; tomorrow it is.** ⚠ **All three of 09-22's later runs (09:36 open, 12:40 midday, 16:15
  close) correctly declined to touch it** — **none of the three generates ideas**, routine 3 is **exits
  only**, and routine 4 is furthest downstream of all; a GIS position opened at the bell, at lunchtime
  or off a close run's arithmetic would be exactly the routing-around that the 08:00/09:35 gap exists
  to prevent. ⚠ **The print is an ITEM TO SCREEN, NOT A POSITION IMPLIED.** It enters the §4 funnel on
  the same terms as anything else and the expected output is still no trade. **No other unscreened item
  has accumulated.**

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

- **⚠ THE TWO-PRICE DEFECT PRODUCED A NEW INSTANCE ON 09-22 AND **THE SIGN FLIPPED ON CONSECUTIVE
  DAYS**.** `lastday_price` read **712.78** at 08:15 on 09-22 against 09-21's official close of
  **712.76** — **two cents HIGH**. The previous instance ran **seven cents LOW** (701.78 vs 701.85)
  and was read **four times** across 09-21 (08:20, 09:36, 12:35, 16:16). ⚠ **That instance DID clear
  at the session boundary — this is a fresh one built on the new day's close, not the old one
  persisting — but it did NOT clear into correctness.** Combined with the 09-21 post-bell
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
  ⚠ **THE TEST THAT COUNTS IS TOMORROW'S 09-23 PRE-MARKET GIS SCREEN — it opens the data plane AND has
  somewhere to put a number. Expect the eleventh costume there.** The 09-22 08:15 run was the last such
  test and it was passed strongly: it issued **`move --symbol ACN`** and **`bars --symbol VOO`** with a
  live funnel being screened, making `--symbol GNRC` **one flag on a command already being typed**. ⚠
  **The tenth costume arrived there as *"you are already screening a candidate's five-session move, so
  screening one more costs nothing"* — zero-marginal-cost wearing a LIVE FUNNEL as cover, the most
  plausible version yet. Refused. FREE IS NOT THE SAME AS PERMITTED.** Costumes so far: diligence,
  curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure,
  call-already-open, screen-already-running. **The pattern is the finding, not any instance.**

- **⚠ ALL FOUR §5 SELL RULES REMAIN UNTESTED CODE PATHS AND §5.4 IS NOT ARMED.** Nothing has ever
  closed in this account. **Twenty-six consecutive sessions of "no exits" record the ABSENCE OF A
  SUBJECT, not twenty-six clean bills of health.** §5.4 arms on the first **satellite** fill; the
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
  eventually **sell core on a drawdown, which §7 forbids outright.** Refused for **forty-three runs.**
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
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — **EIGHT instances** (newest
  **ACN, 09-22: −4.58% over five sessions → `priced_in: true`, verdict "LATE — skip", on a FALL**),
  plus **two near-misses** where a candidate cleared only because its *fall* was fractionally too small (LMT
  −3.61% on 09-11; **GM −3.95% on 09-21, five basis points inside the wire**). **There is no price at
  which those rejections flip**; LITE puts **+10.58% vs VOO** on the bill. ⚠ **A pass on a fall is not evidence the filter worked, and neither is a FAIL on a fall** — the
  09-22 ACN entry records its FAIL **deliberately as NOT the reason for the rejection**, so that no
  run inherits "rejected because priced-in" as a fact.
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM (09-09,
  +2.70% after a +8.7% intraday move), AVAV (09-11, +1.20% after a +12.9% round-trip inside one
  session). Same root cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or
  `alpaca.py move`.**
  **(3)** The satellite sleeve is **structurally undeployed — 54 theses, zero positions, ever.**
  ⚠ **THE INHERITED FIGURE WAS 49 AND IT WAS STALE — RECOUNTED FROM SOURCE AT THE 09-22 CLOSE.** 49 was
  correct **through 09-21**; the 09-22 pre-market run wrote **five more** and the midday run carried
  "49" forward unchanged. Verified: `research_log.md` holds **55 `### T-` headings, one of which is the
  template**, so **54 real theses**, and the per-date tally sums to 54 with **no duplicate IDs**.
  **This is the standing "audit every inherited superlative" rule paying for itself — the count was
  wrong in the direction that understates the problem, and a count of rejections is the single number
  this open item rests on.**
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
  earlier dates appear inside thesis bodies). **Third week flagging size: `research_log.md` is
  **~264KB and still growing (09-22 added five more entries). A human may want to move the rollover
  forward.**

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

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is
**exits-only by construction** and may not open a position under **any** circumstance. Routine 2
executes **only what `plan_today.md` already contains** — a position opened at 09:35 without a plan
entry routes **around** the discipline rather than satisfying it. Routine 4 records and journals; it
does not trade. ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
opportunity any of those seats may act on.** New positions route through pre-market research **plus**
the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.**
The stale-plan gate has been exercised **twenty-three times and has never fired**; its alert path
**remains untested code**, and twenty-three quiet opens are **not** evidence it works. ⚠ **The first
morning it fires will by construction be a morning when the pre-market run failed — i.e. exactly the
morning with no fresh notes to lean on. Read the routine's Step 2 then; do not recall it.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a
broker mark on one leg against an official close on the other. **Both legs from the same source, and
for returns that source is `bars --adjustment all`.**

### Do not reach for these — disposed rejects and the trap in each

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
- **Counters as of 2026-09-22 pre-market: 54 theses since inception, 0 accepted, 54 rejected, 5 this
  week; 0 satellite positions ever opened; 0 exits ever; `alerts.md` empty — zero open, zero
  SYSTEMIC.**
- **`week_of` 2026-09-21, `new_positions_this_week` 0 of 3.** Next boundary **Monday 2026-09-28**.
  The reset does not depend on the Friday review having run.
