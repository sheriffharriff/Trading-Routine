# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-24 16:15 ET 4-market-close-journal (selftest PASSED all five checks, trading_enabled true, LIVE paper, broker equity 99957.40 at pre-flight; ZERO ORDERS - routine 4 does not trade; clock is_open FALSE at 16:15:53 with next_open 2026-09-25 - the POST-BELL shape, AND THE STRONGER DISCRIMINATOR WAS RUN NOT INFERRED: a VOO daily bar for 2026-09-24 EXISTS (o 704.10 h 708.505 l 703.355 c 707.28 v 141074 n 3718) so a session happened and this is not a holiday skip; ⚠⚠ THE DAY'S TRUE MOVE WAS EXACTLY ZERO - VOO official close 707.28 IDENTICAL TO 09-23's 707.28, so close-to-close is 0.00 / +0.000000%, VERIFIED NOT ASSUMED via an independent second bars pull on a different window returning the same 707.28 with DISTINCT OHLV on both days, a real coincidence and not a duplicated bar; on official closes core 70053.48 + cash 30000.00 = equity 100053.48, day P&L 0.00 (0.000%), since inception +53.48 / +0.053475%; ⚠ THE BROKER REPORTED -127.77 AND 100% OF IT WAS ARTIFACT - equity-minus-last_equity -127.77, change_today -0.00182, unrealized_intraday_pl -127.77 all agreeing with each other and all wrong, NONE used in or carried into any figure, and RECORD IT AS A CONFIRMATION NOT A SAVE: the standing rule was followed because it is standing, the only reason it looks impressive is the denominator went to zero, exactly as the carry-forward predicted when it wrote the rule's value is inversely proportional to the size of the real move; STEP 2 HAD NO SUBJECT AND THAT IS CORRECT - zero satellite positions so NO highest_close to raise and NO (as of) date to advance, the field is ABSENT (third state, no date at all) which is what proves NO BACKFILL IS OWED, zero bars calls due on any satellite symbol and zero made, ⚠ tomorrow's midday run MUST NOT read the missing stamp as a failed close run; RECONCILIATION CLEAN satellite-to-satellite, positions returns ONE row core VOO 99.046311231 shares unchanged since the 09-03 fill, avg_entry 706.74, cost_basis 69999.99, market_value 69957.40; 5.1-5.4 never started for the THIRTY-THIRD session, 5.4 STILL NOT ARMED, they remain UNTESTED CODE PATHS and the tally of no-exits records the ABSENCE OF A SUBJECT; ⚠ NEW AND FIRST OF ITS KIND - THE TWO-PRICE DEFECT REACHED A 2 QUANTITY AND FLIPPED ITS SIGN: sleeves on broker marks equity 99957.40, core 69957.40 = 69.99%, satellite 0.0% count 0, cash 30000.00 = 30.01%, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta +12.78; RECOMPUTED ON THE OFFICIAL CLOSE equity 100053.48, core 70053.48 = 70.016%, cash 29.984%, delta -16.04 - SAME INSTANT SAME POSITION OPPOSITE SIGN, harmless today because 2 acts at the 65/75 BAND EDGE and the core sits 4.98 points from it so NO REBALANCE IS DUE TOMORROW on either basis, but load-bearing under any rebalance-to-target rule - re-rates open item (5), FORTY-SECOND consecutive run inside 69.59-70.22; ⚠ FIFTH lastday_price READ OF THE DAY 707.60 AT 16:15 IDENTICAL TO 08:20 09:36 AND 12:40, the 32c error against the official 707.28 survived the ENTIRE DAY, and ⚠ THE FALSIFIABLE PREDICTION HAS GONE PARTLY DEGENERATE because today's close EQUALS the number the field was supposed to show today - see Carry forward, a 707.28 read tomorrow is AMBIGUOUS and must NOT be logged as a clean rebuild; ⚠ AUDIT CATCH NUMBER FIVE AND THE FIRST ON A TRUNCATED SERIES - current_price 706.31 is 97c BELOW the official 707.28 and that is NOT the largest in the record though the inherited three-item series says it would be, journal.md's own 09-18 close entry records 702.98 vs an official 701.85 = $1.13 HIGH and called it the widest gap yet, so the corrected series is FIVE observations +1.13 (09-18) -0.22 (09-21) +0.169 (09-22) +0.02 (09-23) -0.97 (09-24) and 97c is only SECOND largest, DO NOT QUOTE THE THREE-ITEM VERSION; core unrealized +53.48 / +0.08% against the 706.74 fill on the official close, 5 EXEMPTS CORE so no action attaches; core VOO NOT stamped, FIFTY-FIRST refusal and a STRONG one - this run PULLED A FRESH OFFICIAL CLOSE 707.28 AND HELD IT with an entirely empty Step 2 to put it in, the sharpest form of the temptation; GNRC NOT looked at, TWENTY-THIRD refusal and a FREE one - the only bars call this run was VOO for the day's close, routine 4 has no research step; WEEK ROLLOVER CHECKED - Thursday 2026-09-24 confirmed via TZ=America/New_York, ISO Monday 2026-09-21, week_of already 2026-09-21, SIXTEENTH consecutive run to find the reset already done, new_positions_this_week stays 0 of 3, next boundary Monday 2026-09-28; LOSS STREAK - nothing closed today and nothing has EVER closed so consecutive_closed_losses stays 0 and it HAS NEVER HAD AN INPUT, breaker INACTIVE, halt_triggered_at none so NO HALT_CLEARED_AT comparison required and NO circuit-breaker alert due; UNRESOLVED ORDERS - orders --status all returns ONE row for the account's entire history, the 09-03 core VOO buy status filled terminal, NOTHING IN LIMBO OVERNIGHT, trade_log correctly left unappended; research_log NOT appended - routine 4 generates no theses, RECOUNTED FROM SOURCE this run: 68 'T-' headings less the template = 67 REAL THESES, ZERO ACCEPTED EVER, 21 this week (09-21: 3, 09-22: 5, 09-23: 6, 09-24: 7); 1 BENCHMARK - VOO returned 0.000% and the book returned 0.000% so today's excess is EXACTLY 0.000pp, the clean boundary case of the standing finding that this book's excess is nothing but minus 30% of VOO's return; journal.md APPENDED, positions.md COLLAPSED 27KB to 19KB with all four of today's runs merged into ONE dated block; ClickUp daily summary posted as task 86bc76x35; alerts.md empty, zero open incidents, zero SYSTEMIC)

prior_run: 2026-09-24 12:40 ET 3-midday-management (selftest PASSED all five checks, trading_enabled true, LIVE paper, equity 100087.18 at pre-flight / 100113.47 at sleeves; ZERO EXITS AND ZERO ORDERS OF ANY KIND; clock is_open TRUE at 12:40:41 - the IN-SESSION shape; 5 HAD NO OPERAND AND THAT IS A CORRECT OUTCOME NOT AN IDLE RUN - positions returns ONE row core VOO unchanged since the 09-03 fill, RECONCILIATION CLEAN satellite-to-satellite with zero blocks vs zero satellite Alpaca rows; STEP 2 BACKFILL NOT OWED because highest_close is ABSENT, the third state carrying NO (as of) date; ⚠ NOTHING SHOULD HAVE EXECUTED AND DID NOT - TRADING_ENABLED was TRUE so a triggered stop WOULD have been submitted, the null is an EMPTY SLEEVE not a disabled stop and those two produce the identical zero-exit line; ⚠ ROUTINE 3 IS EXITS-ONLY BY CONSTRUCTION and every gate that could have blocked a buy was PERMISSIVE - breaker INACTIVE, cap 0 of 3, sleeve empty, 29.97% idle cash, no restricting note: NOTHING BLOCKED A BUY EXCEPT THIS SEAT'S SCOPE; sleeves equity 100113.47, core 70113.47 = 70.03%, cash 29.97%, rebalance_delta -34.04; FOURTH lastday_price observation of the day, 707.60 at 12:40 identical to 08:20 and 09:36; week rollover checked, week_of already 2026-09-21; nothing closed ever, breaker INACTIVE; alerts.md empty)

week_of: 2026-09-21
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.02
satellite_pct: 0.0
cash_pct: 29.98
open_thesis_ids: none
```

*(`core_pct` / `cash_pct` above are on the **official-close basis** — core $70,053.48 of equity
$100,053.48. On the broker-mark basis the same instant reads 69.99 / 30.01. **Both are in band and
neither implies an action**; the two bases are recorded because this run found they can disagree in
**sign** on `rebalance_delta`. State which basis produced any figure you quote.)*

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

**⚠ COLLAPSE, DO NOT APPEND — acted on thirty-four times.** The Week 3 review flagged the memory files
**against an instruction to read them in full**, calling the accumulation **actively harmful rather than
untidy**: this repo's only continuity mechanism is the next run *reading* these files, and padding them
with restatements raises the odds a genuinely live item gets skimmed. **Carry-forward is defined as
cleared once acted on.** This run updated items in place and discharged the spent ones, and also
collapsed `positions.md` from **27KB to 19KB**, merging today's four per-run blocks into one dated
block. **Nothing live has been discarded** — the narrative history lives in `journal.md`,
`research_log.md` and `weekly_review.md`, which are the files built to hold it.

---

### Live — act on these

- **⚠⚠ NEWEST AND MOST USEFUL, 09-24 CLOSE: AN INHERITED SERIES IN THIS FILE WAS SILENTLY TRUNCATED,
  AND IT ALMOST PRODUCED A FALSE SUPERLATIVE.** The post-bell `current_price` record carried here read
  **"22c LOW (09-21), 16.9c HIGH (09-22), 2c HIGH (09-23)"** — three entries. ⚠ **`journal.md`'s own
  09-18 close entry records `current_price` 702.98 against an official 701.85 — $1.13 HIGH — and
  explicitly called it "the widest gap yet." The series handed forward had DROPPED ITS OWN LARGEST
  MEMBER.** Today's reading is **706.31 against the official 707.28 = 97c LOW**, which against the
  truncated list looks like the largest ever by more than four times. **It is the SECOND largest.**
  ⚠ **CORRECTED SERIES, FIVE POST-BELL OBSERVATIONS: +$1.13 (09-18), −$0.22 (09-21), +$0.169 (09-22),
  +$0.02 (09-23), −$0.97 (09-24). Both signs, range 2c to $1.13, no predictable sign and no correctable
  offset. DO NOT QUOTE THE THREE-ITEM VERSION.** ⚠ **This is the audit-inherited-claims rule paying for
  itself a FIFTH time and the FIRST where the defect was a TRUNCATED SERIES rather than a stale count
  or a wrong mechanism — and it ran in the direction that MANUFACTURES a superlative, the same shape as
  the "positive for the first time" error that survived three runs. A series handed forward in prose is
  not the series; go to the file that recorded each observation.**

- **⚠⚠ THE `lastday_price` PREDICTION IS REWRITTEN, NOT RETIRED — AND THE REWRITE IS THE POINT.**
  The 09-24 pre-market wrote a good concrete test: the field should read today's official close at
  tomorrow's pre-market, settled in one `bars` look. ⚠ **That test has gone PARTLY DEGENERATE, because
  today's official close is 707.28 — THE SAME NUMBER the field was supposed to display today and did
  not.** Read tomorrow's pre-market as: **707.60 ⇒ it never rebuilt at all (informative); 707.28 ⇒
  AMBIGUOUS — it cannot distinguish "correctly rebuilt to 09-24's close" from "belatedly corrected to
  09-23's close", and MUST NOT be logged as a clean rebuild; anything else ⇒ the field is wrong in a
  FOURTH way.** ⚠ **The coincidence that made today's P&L trivial is the same coincidence that broke
  tomorrow's experiment.** **Both structural mechanisms remain dead** (09-22: rebuilds; falsified
  09-23: does not; falsified 09-24: does, to a 32c-wrong value). **Five reads on 09-24 — 08:20, 09:36,
  12:40, 16:15 all 707.60 — the 32c error survived the pre-market, the bell, the midday AND the close.**
  ⚠ **Keep writing concrete falsifiable predictions; that practice produced catches (3), (4) and the
  detection of this degeneracy. But CHECK A PREDICTION IS STILL DISCRIMINATING before repeating it.**

- **⚠⚠ NEW AND FIRST OF ITS KIND, 09-24 CLOSE: THE TWO-PRICE DEFECT REACHED A §2 QUANTITY AND FLIPPED
  ITS SIGN.** `rebalance_delta` read **+$12.78** on broker marks and **−$16.04** recomputed on the
  official close — **same instant, same position, opposite direction**, core reading *below* target on
  one basis and *above* on the other. ⚠ **It changes NOTHING today**: §2 rebalances at the **65/75 band
  edge**, not to the exact target, and the core sits **4.98 points** from the nearest edge, so **no
  delta inside the band is an action at any size on either basis. NO REBALANCE IS DUE.** ⚠ **But this
  defect had been filed as a P&L problem and it is not — it feeds `sleeves` too, and would be
  LOAD-BEARING under any rule that rebalanced TO TARGET rather than AT THE EDGE. That is a RE-RATING of
  open item (5), not a new incident. State which basis produced any sleeve figure you quote.**

- **⚠ HIGH-WATER MARKS WERE NOT UPDATED, AND NOTHING WAS SKIPPED. DO NOT BACKFILL — THERE IS NOTHING TO
  BACKFILL.** `positions.md` carries **zero satellite blocks**, so `highest_close` is **ABSENT — the
  third state, carrying no `(as of …)` date at all.** ⚠ **The 09-24 CLOSE run is the cleanest statement
  of this: routine 4's invisible job is to advance the `(as of …)` date WHETHER OR NOT the value moves,
  and there was no date to advance because there is no field. Tomorrow's midday run MUST NOT read the
  missing stamp as a failed close run.** ⚠ **The distinction is FREE today and stops being free the
  moment a satellite fill lands** — after that, a mark silently not written reads identically to a mark
  correctly unchanged, and **only the `(as of …)` date separates them. Compare the date; never infer
  from the field's emptiness.** **§5.4 is NOT ARMED**; it arms on the first **satellite** fill, and the
  09-03 core fill was not one. **Thirty-third consecutive session with §5.1–§5.4 never started — they
  remain UNTESTED CODE PATHS, and the running tally of "no exits" records the ABSENCE OF A SUBJECT, not
  thirty-three clean bills of health.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE.** VOO **official** closes: **09-24 707.28**,
  **09-23 707.28**, 09-22 712.69, 09-21 712.76, 09-18 701.85. ⚠ **09-23 AND 09-24 CLOSED AT THE SAME
  NUMBER TO THE CENT — VERIFIED, NOT ASSUMED: an independent second `bars` pull on a different window
  returned the same 707.28 with DISTINCT OHLV on both days** (09-23 o 712.13 / h 712.38 / l 706.395 /
  v 147,584; 09-24 o 704.10 / h 708.505 / l 703.355 / v 141,074). **A real coincidence, not a duplicated
  bar. Treat an identical consecutive close as suspect and verify it — one extra call settles it.**
  Core is **99.046311231 shares at 706.74**, cash **$30,000.00** flat. **AT THE 09-24 CLOSE, ON OFFICIAL
  MARKS: equity $100,053.48, core $70,053.48 = 70.016%, cash 29.984%, since inception +0.053475%
  (+$53.48), day P&L EXACTLY $0.00 / 0.000%.** **Forty-second consecutive run inside the range
  69.59–70.22.** **Audit any superlative here before repeating it.**

- **⚠ STANDING RULE, NOW EVIDENCED SIX WAYS AND TODAY AT ITS LIMIT: NEVER `equity − last_equity` AS A
  DAY'S P&L, NEVER `unrealized_intraday_pl`, NEVER a `positions` field for a close or an execution
  reference. Close-to-close from `bars --adjustment all`, a fresh `quote` for execution.**
  ⚠ **09-24 IS THE MOST EXTREME INSTANCE THE DEFECT HAS PRODUCED: the true close-to-close move was
  EXACTLY ZERO and the broker reported −$127.77, so 100% OF THE HEADLINE WAS ARTIFACT.** All three
  broker figures agreed with each other (`equity − last_equity` −$127.77, `change_today` −0.00182,
  `unrealized_intraday_pl` −$127.77) — ⚠ **which is exactly why NO CHECK INTERNAL TO THE BROKER'S OWN
  FIELDS CAN EVER SURFACE IT. Only an external close settles it.** ⚠ **RECORD 09-24 AS A CONFIRMATION,
  NOT A SAVE — the honest version is less flattering: nothing was spotted, a standing rule was followed
  on a day it happened to matter maximally. The carry-forward had already predicted this shape: THE
  RULE'S VALUE IS INVERSELY PROPORTIONAL TO THE SIZE OF THE REAL MOVE, so it looks like pedantry on
  exactly the days it costs nothing to follow. Today the real move was zero, so the ratio is
  unbounded.** Prior instances: **09-22 a SIGN error** (+$7.82 reported on a −$6.93 day); **09-23 $6.93
  of noise on a real move of −$535.84, where the rule bought nothing — recorded honestly, because the
  false version of this note is "the rule saved me again."**

- **⚠ §1 BENCHMARK — 09-24 IS THE CLEAN BOUNDARY CASE AND IT CONFIRMS THE STANDING FINDING EXACTLY.**
  **VOO returned 0.000% and the book returned 0.000%, so today's excess is EXACTLY 0.000pp.** The
  standing finding is that this book's excess is nothing but **minus ~30% of VOO's return** — on a flat
  tape that predicts exactly zero, and it delivered exactly zero. ⚠ **Twelve-plus sessions, every
  positive-excess day has been a VOO DOWN day; NOT ONE HAS EVER COINCIDED WITH A RISING MARKET.** The
  satellite sleeve's apparent outperformance on short windows **is nothing but 0% exposure to a market
  that fell.** **A flat day dressed up as "we held our ground" is the easiest possible moment to stop
  asking §1's actual twelve-month question.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR
  JUDGMENT RATHER THAN CARE.** **RECOUNTED FROM SOURCE on 09-24 at the close, not inherited** —
  `research_log.md` holds **68 `### T-` headings, one the template, so 67 REAL THESES, ZERO ACCEPTED
  EVER**, 21 this week (09-21: 3, 09-22: 5, 09-23: 6, 09-24: 7). Set beside that: an empty satellite
  sleeve, **~30% idle cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker, and an account at
  **+0.053% since inception.** ⚠ **A DAY THAT CLOSED AT EXACTLY ZERO MAKES "NOTHING IS HAPPENING HERE"
  FEEL LIKE A VERDICT ON THE §4 BAR. IT IS NOT.** §4's own position governs: a run that finds nothing is
  a successful run, and **a flat account is what "no trade" LOOKS LIKE — not a verdict on the rule that
  produced it.** **Naming the pull is the only defence against acting on it.** If the bar is to move,
  that is a `strategy.md` change and **only the human may make it. Do not resolve it from this seat.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY AND THAT IS ITS NORMAL STATE.** ⚠ **09-24's
  seven rejections do NOT become a queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE**, and
  none was revisited at the open, midday or close (no `move`, `quote`, `bars` or `asset` call on any of
  them after the pre-market). **ILMN** (part 3 kills it at any price: non-binding vote → undated PMA
  decision → reimbursement → ramp is several quarters out) · **GRAL** (first-order — the company in the
  headline) · **BBY and PYPL** (no revenue share, minimum, value, volume or take rate disclosed by any
  party; the only economics described is Meta taking **a fee**, a **cost** at the retailer) · **SHOP**
  (part 2 fails identically to PYPL's, so not a price-only rejection) · **SoftBank/OpenAI** (recipient
  is private; no US-listed party with an allocated figure) · **ELMT** (~$634M microcap; Masan
  Vietnam-listed).
  ⚠ **ELMT HAS ENTERED THIS FUNNEL TWICE IN TWO SESSIONS ON TWO DIFFERENT, WELL-DISCLOSED TUNGSTEN
  TRANSACTIONS, AND BOTH DIED ON THE SAME §3 FLOOR. A third Elmet headline is not a third opportunity —
  it is the same ineligible company. Do not screen it again.**
  ⚠ **One §3 question was reached and deliberately NOT decided: Shopify is a Canadian issuer trading as
  common stock on a US exchange, which §3's "US-listed common stock" does not obviously settle either
  way. Two independent kills landed first. A future run reaching this with a LIVE candidate must put it
  to the human rather than decide it from this seat.**

- **⚠ THE §4 PRICED-IN FILTER IS SIGN-BLIND, NOT BROKEN — AND 09-24 SUPPLIED THE FIRST COUNTERWEIGHT IN
  VOLUME.** **SHOP +9.61%, ILMN +11.54%, GRAL +44.67%**, all five-session, all `priced_in: true`, all
  genuine **RISES** where "moved more than 4% in five sessions" means exactly what §4 intends — **you
  are late.** Open item (1) below has **nine instances of the filter reading a DRAWDOWN as priced-in**
  plus three near-misses, and the sheer weight of that record makes the filter easy to read as simply
  broken. ⚠ **Recorded prominently and deliberately, because a system that only ever logs a rule's
  failures is BUILDING A CASE rather than keeping a record.** ⚠ **The implication for the human is
  specific: the fix to open items (1) and (2) is to make the filter read SIGN — evidence FOR that, and
  AGAINST loosening or removing it.**
  ⚠ **ILMN IS THE SHARPEST ENTRY AND IT NEVER REACHED A THESIS.** The GRAIL advisory-committee vote is
  the most genuinely **second-order** shape the funnel has produced in several sessions — a named
  beneficiary with a structurally necessary named supplier. **The story was half-built when the hard
  filter ran, and the filter killed it.** ⚠ **§4 orders the hard filters BEFORE the thesis precisely so
  that this happens: five more minutes of construction and it would have been a written thesis looking
  for permission.**

- **⚠ OPEN ITEM (6) HAS AN INSTANCE ON THE RESEARCH PLANE, WHICH IS WHERE IT MATTERS MOST HERE.**
  A `perplexity.py` call returned **HTTP 500** on 09-24 **after a green selftest**; a reworded retry
  succeeded immediately and every later call returned 200. ⚠ **The selftest's Perplexity check confirms
  the model endpoint answers; it does not confirm a QUERY will.** ⚠ **A research run that silently
  returns nothing is indistinguishable in `research_log.md` from a legitimate quiet day — which is
  exactly the failure routine 1's Step 0 exists to make loud, and on the data plane it is silent.**
  **Check exit codes; never infer thin news from empty results.** Single transient occurrence,
  recovered, **no alert raised.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — FIVE CATCHES NOW, AND THEY KEEP CHANGING SHAPE.**
  **(1)** A false superlative (*"positive for the first time in this account's history"*) survived three
  runs and was caught **by accident** on 09-21. **(2)** A stale count (*"49 theses"*) caught
  **deliberately** on 09-22, having run in the direction that **understates** the problem. **(3)** The
  09-22 claim that `lastday_price` rebuilds at a session boundary, falsified 09-23. **(4)** The 09-23
  claim that it does **not**, falsified 09-24. ⚠ **(5) NEW, 09-24 CLOSE: a TRUNCATED SERIES — the
  three-item post-bell `current_price` record that had dropped its own largest member, which would have
  produced a false superlative had it been repeated. See the live item at the top.**
  ⚠ **A superlative, count, mechanism OR SERIES inherited from a prior run is NOT a checked fact** — it
  is the cheapest claim to write and the most expensive to verify. **Assume the next one you are handed
  is wrong until you have pulled the source.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — TWENTY-THREE CONSECUTIVE REFUSALS, AND THE LAST THREE WERE FREE.**
  ⚠ **Graded honestly: the 09-24 CLOSE made exactly one `bars` call, on VOO, for the day's close, and
  routine 4 has no research step — so there was nowhere to put a GNRC number and nothing was given up.**
  The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon announcement —
  first-order, outside §4 at any price** — and **open item (7) is resolved by a human editing §4 or
  `alpaca.py move`, not by a number this seat collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER
  EACH REFUSAL COST ANYTHING, AND MOST OF THEM DID NOT. Twenty-three is not twenty-three equal
  observations, and quoting the bare count overstates the evidence.** ⚠ **09-23 pre-market and 09-24
  pre-market are the two STRONG ones: both opened the data plane against a live funnel AND had somewhere
  to put a number** — 09-24 issued **five** `move` calls, making `--symbol GNRC` one more invocation on
  a command line already typed five times over. **Not made.** ⚠ **No new costume has appeared in four
  sessions; the costume list may be CONVERGING rather than growing, and a run that manufactures a new
  name for an old experience would be padding the log.** Costumes: diligence, curiosity, tidiness,
  completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
  screen-already-running. **The pattern is the finding, not any instance. FREE IS NOT THE SAME AS
  PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FIFTY-ONE RUNS.** §5 exempts core from all
  four sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **Grade these the way the GNRC count is graded — a refusal only costs something on a run that was
  HOLDING the number. The sharpest instances are the ones with a fresh official close in hand AND an
  empty Step 2: 09-22 close (712.69), 09-23 close (707.28), 09-24 pre-market (707.28), and ⚠ 09-24
  CLOSE (707.28), which is the STRONGEST of all — routine 4's entire declared purpose is writing closes
  into `highest_close`, so it arrived holding a fresh official close with an empty field to put it in.**
  The 09-24 open and midday were by contrast **WEAK instances and are recorded as such** — neither
  pulled a close, so both refusals were free. **Quoting the bare count overstates the evidence.**
  ⚠ **"Nothing to write" is the correct output of an empty Step 2, not an invitation to find a row to
  write it to.** **Measure the core from the 706.74 fill and from an official close, never from a
  `positions` field.** ⚠ **Noted honestly: this refusal is now close to automatic, and automatic is not
  the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN IS
  USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell sees it
  pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with **no bar for
  today**. ⚠ **09-22 read all three shapes in one day, and consecutive runs read IDENTICAL booleans
  meaning opposite things.** **`is_open: TRUE` is the one case where the boolean alone is sufficient,
  and it is safe to read it that way ONLY because TRUE has a single meaning. FALSE has three.**
  ⚠ **THE STRONGER DISCRIMINATOR IS TO CHECK THAT A DAILY BAR FOR TODAY EXISTS — the 09-24 close run
  RAN IT rather than inferring** (VOO 2026-09-24 bar present, c 707.28, n 3,718), which settles "was
  there a session?" **directly**, where `next_open` only settles it by inference. **Run it before
  deciding a run is a holiday skip.**

- **⚠ SEVEN ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — **NINE instances** (newest CNC,
  09-23: −6.44% → `priced_in: true` on a **FALL**; before it ACN, 09-22, −4.58%), plus **THREE
  near-misses** where a candidate cleared only because its *fall* was fractionally too small (LMT
  −3.61%; **GM −3.95%, five basis points inside the wire**; **LH −3.83%, seventeen basis points
  inside**). **There is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on the
  bill. ⚠ **A pass on a fall is not evidence the filter worked, and neither is a FAIL on a fall** —
  recorded **deliberately as NOT the reason for the rejection**, so no run inherits "rejected because
  priced-in" as a fact. ⚠ **09-24 supplies the counterweight: THREE firings on genuine RISES (SHOP,
  ILMN, GRAL). The defect is SIGN-BLINDNESS, not the threshold.**
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM (09-09,
  +2.70% after a +8.7% intraday move), AVAV (09-11, +1.20% after a +12.9% round trip in one session).
  Same root cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or
  `alpaca.py move`.**
  **(3)** The satellite sleeve is **structurally undeployed — 67 theses, zero positions, ever.**
  ⚠ **RECOUNTED FROM SOURCE at the 09-24 close. Recount before quoting; do not copy this line forward.**
  A 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits
  the cash and §4 says most runs end in no trade — both rules were followed, and the agent must NOT
  respond by lowering the §4 bar.** **The binding constraint has FOUR known forms:** the source
  withholds the counterparty's number; **or** the counterparty discloses **roadmap instead of segment
  revenue**; **or** the named beneficiary is **vertically integrated** with no external supplier to
  find; **or** **both parties expressly refuse to disclose as a commercial choice** (09-21 GM), so **no
  better-sourced version of that candidate will ever arrive.** ⚠ **Only the first two forms are
  addressable by widening the evidence bar. The last two are not addressable at all** — the most
  decision-relevant line in this file. ⚠ **AND WIDENING THE BAR IS NOT THE WHOLE ANSWER ANYWAY: ELMT
  (09-23 and again 09-24) withheld NOTHING and still produced no trade, because the obstruction was
  STRUCTURAL (§3) — a constraint no evidence bar can relieve.** ⚠ **09-24's BBY/PYPL pair is the purest
  live example of form one: every party named, the event real, dated and first-disclosed, and NOT ONE
  COMMERCIAL TERM in existence to build a dollar path from.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the
  prior close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11: measured from the
  fill, tracking error 0.0000%. Keep measuring it from the fill.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it
  never had a stable size and never will. ⚠ **RE-RATED AGAIN 09-24: previously "cosmetic on core", then
  "load-bearing four times on the P&L plane"; it has now FLIPPED THE SIGN OF A §2 QUANTITY
  (`rebalance_delta` +$12.78 broker vs −$16.04 official). It is not a P&L problem — it is a
  price-source problem that contaminates every derived figure.** **Whether the tooling should read
  closes from `bars` by default is a human's call, and this is the strongest evidence yet that it
  should.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed
  all five checks on 09-11 while `clock` returned 500 and `quote`/`bars` returned 504, ⚠ **and on 09-24
  while a `perplexity.py` QUERY returned 500 — the first instance on the RESEARCH plane, which is the
  one that matters most here.** **Every routine's Step 0 is the loud-failure mechanism for exactly this,
  and on the data plane it is silent.** Until a human changes it: **probe by hand; never infer
  data-plane health from a green selftest.**
  **(7)** **`alpaca.py move` cannot see an after-hours event**, and neither can the 09:35 re-validation
  that exists to catch exactly this. ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a
  trade rather than skipping one**, which is why it is listed last and should be read first. **It has
  cost zero only because no plan has yet carried a BUY intent — an absence of exposure, not a
  mitigation.** It disappears the first morning a BUY intent names a stock whose news broke after the
  prior close.
  Prior context in ClickUp `86bbv75bz`; last week's in `86bbzgbg3`. **09-24 daily summary: `86bc76x35`.**

- **⚠ WEEK 3 REVIEW (2026-09-18): THE §1 ANSWER IS NO, AND SHORT GREEN WINDOWS MUST NOT BE READ AS YES.**
  The satellite sleeve returned **0.0000%** — zero positions in the account's entire history — so its
  dollar-weighted excess over VOO is exactly **minus VOO's total return** over whatever window is
  chosen: **+0.095pp on the week, +0.430pp since inception, +0.509pp over 1M, −2.291pp over 3M, and
  −16.552pp over the rolling 12 months §1 actually names.** The structural cost is **~4.97pp of account
  return per rolling 12 months.** Full working in `weekly_review.md`. **Reject board: 40 measurements,
  13 beat VOO, 27 lagged, mean excess −1.57%.** ⚠ **It is a tally, not a result — do not quote it as
  one.** **HPE remains the largest single opportunity cost the log has produced (+19.87% vs VOO).**
  ⚠ **FILE SIZE — SIXTH CONSECUTIVE FLAG.** `research_log.md` is **~311KB** against a total memory
  footprint of **~655KB** across files every run is instructed to read **in full**. **Monthly archive
  rollover is next due 2026-10-02 — Friday's review (09-25) is the last one before it.** ⚠ **A human
  may want to move it forward.** **Mitigations so far: `positions.md` collapsed 36K→20K on 09-24 and
  again 27K→19K at the 09-24 close. Those are mitigations, not a fix.**

- **⚠ NEW, 09-24 CLOSE — A `#` IN A FENCED-BLOCK VALUE SILENTLY TRUNCATES IT, AND THIS RUN DID IT TO
  ITSELF.** `_parse_kv` in `scripts/common.py` does `line.split("#", 1)[0]`, so **everything after the
  first `#` in a `key: value` line is discarded by the parser.** This run's `last_run` quoted the count
  as "68 `###` T- headings" and lost the back half of its own run note (loss-streak check,
  unresolved-orders check, ClickUp task ID) at 5,046 characters. **Caught and fixed before commit; no
  gating field was ever affected and the file text itself was always complete.** ⚠ **STANDING
  CONSEQUENCE: never put a `#` in a fenced-block value, and VALIDATE `state.md` WITH
  `common.read_state()` AFTER REWRITING IT — writing the block and parsing the block are not the same
  check.** No earlier run hit this because none had written a `#` into the block.

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
construction** and may not open a position under **any** circumstance; **09-24 midday is the worked
example — at 12:40 every gate that could have stopped a buy was OPEN (breaker INACTIVE, cap 0 of 3,
sleeve empty, 29.97% idle cash, no restricting note), so the ONLY thing that held was the seat's own
scope.** Routine 2 executes **only what `plan_today.md` already contains** — a position opened at 09:35
without a plan entry routes **around** the discipline rather than satisfying it. ⚠ **Routine 4 RECORDS
AND JOURNALS; IT DOES NOT TRADE, and 09-24's close is its own worked example: the same permissive gates,
plus a fresh official close in hand, and nothing to do with any of it.** ⚠ **Idle cash, an INACTIVE
breaker and an unused 0-of-3 weekly cap are NOT an opportunity any of those seats may act on.** New
positions route through pre-market research **plus** the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.**
The gate has been exercised **TWENTY-SEVEN times and has never fired**, and its alert path **remains
untested code.** ⚠ **Twenty-seven quiet opens are NOT evidence it works. The first morning it fires will
by construction be a morning when the pre-market run failed — i.e. exactly the morning with no fresh
notes to lean on. Read routine 2's Step 2 then; do not recall it.**
⚠ **09-24's open is the CLEANEST DEMONSTRATION: the plan was FRESH and EMPTY, and the run it produced —
zero orders, zero `move` calls, nothing logged — is BYTE-FOR-BYTE the run a stale plan would have
produced. Nothing in the outcome could have told the two apart. Only `plan_date` did.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a broker
mark on one leg against an official close on the other. **Both legs from the same source, and for
returns that source is `bars --adjustment all`.** ⚠ **And state WHICH basis produced any figure you
quote — 09-24 proved the two bases can disagree in SIGN on `rebalance_delta`.**

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
  state in this account** — re-confirmed at the 09-24 close from `orders --status all`, which returns
  **one row for the entire history.**
- **The core is deliberately NOT tracked in `positions.md`.** §5 exempts it, so it has no thesis state,
  no timing window and no `highest_close`. ⚠ **Every reconciliation compares SATELLITE blocks to
  SATELLITE Alpaca positions** — a run that compares the raw ledger to the raw broker will read a
  correct ledger as broken.
- **Counters as of 2026-09-24 CLOSE, RE-VERIFIED FROM SOURCE (68 `### T-` headings less the template):
  67 theses since inception, 0 accepted, 67 rejected, 21 this week (09-21: 3, 09-22: 5, 09-23: 6,
  09-24: 7 — counted per-ID from source, not summed from prior runs); 0 satellite positions ever
  opened; 0 exits ever; `alerts.md` empty — zero open, zero SYSTEMIC.** ⚠ **Recount from
  `research_log.md` before quoting this anywhere human-facing — a run that ADDS theses and a run that
  COPIES this line forward are different runs, and nothing connects them.**
- **`week_of` 2026-09-21, `new_positions_this_week` 0 of 3.** Next boundary **Monday 2026-09-28**.
  The reset does not depend on the Friday review having run. ⚠ **Note the two counters are independent:
  21 theses this week and 0 positions this week are both correct — §6's cap counts POSITIONS OPENED,
  and none was.**
- **Tomorrow, Friday 2026-09-25, is a weekly-review day** (routine 5), and it is the **last review
  before the 2026-10-02 monthly archive rollover.**
