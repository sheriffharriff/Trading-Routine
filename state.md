# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **NEVER PUT A `#` IN A FENCED-BLOCK VALUE** — `_parse_kv` does `line.split("#", 1)[0]` and
silently discards everything after it. **Validate with `common.read_state()` after rewriting.**

```
last_run: 2026-09-25 16:45 ET 5-friday-weekly-review (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 100416.12 at pre-flight; ZERO ORDERS - routine 5 MEASURES, IT DOES NOT TRADE; FRIDAY CONFIRMED via TZ=America/New_York so the weekly series is not corrupted by a mid-week write; FOURTH weekly review, posted to ClickUp 86bc7vzam; THE §1 ANSWER IS NO AND THIS IS THE FIRST WEEK EVERY WINDOW SAYS SO - satellite 0.0000 pct against VOO total return of +1.262 pct week / +0.827 pct since inception / +0.974 pct 1M / +5.444 pct 3M / +18.571 pct rolling 12M, so dollar-weighted excess is -1.262 / -0.827 / -0.974 / -5.444 / -18.571pp, ALL FIVE NEGATIVE where Week 3 had the first three POSITIVE; the three reviews that called those positives 'zero exposure to a market that fell' were right and the market rising inverted the whole column with no rule change; structural cost now ~5.57pp per rolling 12M, up from 4.97pp because the BENCHMARK improved; core return from the 706.74 fill +0.5610 pct with divergence 0.0000 pct, satellite 0.0000 pct on 30000 idle, account week +0.8813 pct vs VOO +1.2617 pct = -0.3804pp which is EXACTLY 0.6985 x VOO to four decimals, since inception +0.3927 pct vs +0.8271 pct = -0.4344pp or EIGHT TIMES last Friday's -0.055pp on five up sessions and an unchanged entry gap; DAILY AUDIT RECOMPUTED NOT INHERITED - 15 post-fill sessions, 9 VOO-down days ALL positive excess, 5 VOO-up days ALL negative, 1 flat day EXACTLY zero, separation PERFECT 15 of 15, worst relative day 09-21 at -0.4686pp which the journal calls 'biggest dollar gain on record'; ZERO CLOSED TRADES fourth consecutive week, §5.1-§5.4 still untested and §5.4 still not armed; THESES RECOUNTED FROM SOURCE 73 real, 0 accepted ever, 27 this week, and THE FAILURE POINT MOVED ONE TEST DOWN THE CHAIN - part 2 is now dominant at 11 of 27 against 4 of 16 last week while part 1 HALVED to 6, completing the three-week arc, and JBL is the case that settles what it means since widening the evidence bar WOULD HAVE LET IT THROUGH; REJECT BOARD RE-MEASURED 65 names, 20 beat VOO, 45 lagged, mean -2.04 pct median -2.47 pct, CRDO displaced HPE as largest excess at +24.28pp from +4.68pp in five sessions and QCOM moved most at +0.76 to +13.11pp; NEW FINDING - six of the top six excesses are ONE THEME rejected under FIVE DIFFERENT RULES; CATCH (9) FOUND THIS RUN AND IT IS THE WORST SHAPE YET - the close journals' '37th consecutive SESSION' for §5 increments 3-4 PER TRADING DAY while sessions increment by ONE, the account has operated 18 sessions, so it is a RUN counter wearing a session label and only the CALENDAR exposes it since re-running reproduces the same number; HOUSEKEEPING - week_of advanced to 2026-09-28 and new_positions_this_week reset to 0, MONTHLY ROLLOVER NOT DUE AND DELIBERATELY NOT RUN EARLY since every entry is dated 2026-09 which IS the current month and splitting a live month for five sessions is the failure the archive prevents arriving early, alerts.md empty with zero open and zero SYSTEMIC so NO PROMPT BUG TO SURFACE, control.md notes none; prior last_run preserved below)

prior_run: 2026-09-25 16:20 ET 4-market-close-journal (selftest PASSED all five checks, trading_enabled true, LIVE paper, broker equity 100387.36 at pre-flight; ZERO ORDERS - routine 4 RECORDS AND JOURNALS, IT DOES NOT TRADE; clock at 16:17:04 is_open FALSE with next_open 2026-09-28T09:30 - the POST-BELL shape, and the stronger discriminator was RUN not inferred, a VOO daily bar for 2026-09-25 EXISTS AND IS COMPLETE at o 708.46 h 711.615 l 706.33 c 710.705 v 164682 n 4246, so a session happened and the summary was owed; STEP 2 HAD NO OPERAND - zero open satellite positions, highest_close is ABSENT which is the third state carrying no (as of ...) date at all, zero bars calls due on any satellite symbol and zero made, and MONDAY MUST NOT READ THE MISSING STAMP AS A FAILED CLOSE RUN NOR BACKFILL ANYTHING; RECONCILIATION CLEAN - one row core VOO 99.046311231 shares unchanged since the 09-03 fill, zero satellite blocks against zero satellite Alpaca rows, they agree; 5.1-5.4 NEVER STARTED for the THIRTY-SEVENTH consecutive session, 5.4 STILL NOT ARMED, 5.3 distance UNDEFINED not large, and TRADING_ENABLED WAS TRUE so a triggered stop WOULD have been submitted - an EMPTY SLEEVE not a disabled stop; THE DAY, OFFICIAL BASIS - VOO 710.705 vs 707.28 is +0.4843 pct which ENDS the two-session pause, equity 100392.71, day P&L +339.23 or +0.3391 pct, since inception +392.71 or +0.3927 pct, and that is THIRD BEST NOT BEST - checked against 25 pulled sessions, peak 09-21 +0.5962 pct then 09-22 +0.5893 pct, and today is 0.0005pp ahead of 09-03 which is A TIE; broker day-P&L fields pulled and NOT used, artifact +23.38 = 6.9 pct of the real move, and last_equity 100024.75 is a THIRD number matching neither basis; sleeves broker 70.12 pct delta -116.21, official 70.117 pct delta -117.81, BOTH NEGATIVE for the FOURTH run and agreeing to 2dp which is NOT the defect resolving, NO REBALANCE DUE MONDAY with core ~4.88 points inside the band edge, FORTY-SIXTH consecutive run inside 69.59-70.22; THE FINDING IS A CORRECTION TO A CLAIM SIX HOURS OLD - the midday run's volume calibration is WRONG, it read the partial bar's v 69713 as 49.5 pct of the four-session mean 140926 against 49.0 pct elapsed and concluded the volume TRACKS ELAPSED TIME ALMOST EXACTLY, but the ACTUAL session volume is 164682 which is 16.9 pct ABOVE that mean so the partial held 42.3 pct at 49.0 pct elapsed and the precision was AN ARTIFACT OF A STALE DENOMINATOR; the mechanism stands, the bar IS a live accumulator, but YOU CANNOT JUDGE A BAR'S COMPLETENESS FROM v AGAINST A PRIOR-DAY MEAN, n and v are A SMELL TEST NOT A MEASUREMENT and the reliable discriminator is THE CLOCK; AND THE TRAP WAS MILD TODAY WHICH IS THE MORE UNCOMFORTABLE HALF - the midday partial's close 710.555 against the official 710.705 is FIFTEEN CENTS so a mark stamped from it would have been small and self-healing, and a loud warning whose instances are all mild teaches a future run that the shortcut is safe; 1 SHARPENED IN THE WRONG DIRECTION - excess -0.1452pp against -0.1453pp PREDICTED by the cash weight alone, satellite contributed EXACTLY 0.0000 pct, and a good day in dollars is not a good day against the benchmark; CORE VOO NOT STAMPED fifty-fifth run and STRONG; GNRC not looked at twenty-seventh refusal and WEAK; HOUSEKEEPING all four checks run none fired - week rollover already done TWENTIETH consecutive run with ISO Monday 2026-09-21 confirmed via TZ=America/New_York and next boundary 2026-09-28, loss streak 0 with NO INPUT EVER, breaker INACTIVE halt_triggered_at none so no comparison required and NO circuit-breaker alert due, orders --status all returns ONE row filled and terminal so NOTHING IS IN LIMBO OVERNIGHT, trade_log and research_log correctly unappended, alerts.md empty, control.md notes none; THESIS COUNT RECOUNTED FROM SOURCE - 74 T- headings less the template = 73 real theses, 0 accepted EVER, 27 this week; ClickUp daily summary 86bc7vgbw created; TODAY'S WEEKLY REVIEW routine 5 IS STILL DUE and it is the LAST BEFORE THE 2026-10-02 MONTHLY ARCHIVE ROLLOVER)


week_of: 2026-09-28
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.12
satellite_pct: 0.0
cash_pct: 29.88
open_thesis_ids: none
```

*(`core_pct` / `cash_pct` above are on the **official-close basis** — core $70,392.71 of equity
$100,392.71, using VOO's **2026-09-25 official close of 710.705**, which is **a COMPLETED session's
bar** (`is_open: false`, `n` 4,246, `v` 164,682). On the broker-mark basis at 16:20 the same position
reads **70.12 / 29.88** — **the two agree to two decimal places today.** **Both are in band and neither
implies an action.** The two bases are still recorded separately because they have been shown to
disagree in **sign** on `rebalance_delta`. **State which basis produced any figure you quote.**)*

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

**⚠ COLLAPSE, DO NOT APPEND — acted on thirty-eight times.** The Week 3 review flagged the memory files
**against an instruction to read them in full**, calling the accumulation **actively harmful rather than
untidy**: this repo's only continuity mechanism is the next run *reading* these files, and padding them
with restatements raises the odds a genuinely live item gets skimmed. **Carry-forward is defined as
cleared once acted on.** ⚠ **The 09-25 close run added NO new item.** It **corrected one inherited claim
in place** (the midday run's volume calibration, six hours old) and **refreshed the rest with a completed
session's numbers**. ⚠ **A correction replaces the claim it corrects — it does not sit beside it.**
**Nothing live has been discarded.**

---

### Live — act on these

- **⚠⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN — AND THE `n`/`v` TEST PROPOSED FOR
  DETECTING IT IS WEAKER THAN ITS AUTHOR CLAIMED. CORRECTED 09-25 CLOSE, BY THE COMPLETED SESSION.**
  Two routines read `is_open: true` and can therefore pull a live partial bar and mistake it for a close:
  **routine 2 at 09:35 and routine 3 at 12:30.** *(The 09-25 open claimed routine 2 was the only one;
  the midday run falsified that from its own clock. That correction stands.)* ⚠ **The midday case is the
  more dangerous: at 09:36 the bar was an obvious stub (n 193, v 6,776), but at 12:41 it read c 710.555,
  o 708.46, h 711.26, l 706.33, n 1,731, v 69,713 — half a session of real volume, a plausible OHLC and a
  close inside the recent range. It does NOT look like a stub.**
  ⚠⚠ **BUT THE MIDDAY RUN'S CALIBRATION OF THAT TEST WAS WRONG.** It wrote that v 69,713 was *"49.5% of
  the four-session mean volume (140,926) against 49.0% of the session elapsed — the volume tracks elapsed
  session time almost exactly."* **Today's ACTUAL full-session volume is 164,682 — 16.9% ABOVE that
  four-session mean — so the partial held 42.3% of the day's eventual volume at 49.0% elapsed.** ⚠ **The
  precision was an artifact of a STALE DENOMINATOR.** The mechanism stands (the bar **is** a live
  accumulator); the measurement does not. ⚠⚠ **LOAD-BEARING CONSEQUENCE: YOU CANNOT JUDGE A BAR'S
  COMPLETENESS FROM `v` AGAINST A PRIOR-DAY MEAN, because the day's own volume is unknown until the bell —
  a busy day's half-finished bar can carry more volume than a quiet day's COMPLETE one. `n` and `v` are a
  SMELL TEST, not a measurement. THE RELIABLE DISCRIMINATOR IS THE CLOCK.** The standing "use `bars`,
  never a broker field" rule does **not** protect against this — the bar is from the right source and is
  still not a close. **When in doubt use the last COMPLETED session.**
  ⚠ **AND THE TRAP WAS MILD TODAY, WHICH IS THE MORE UNCOMFORTABLE HALF.** The midday partial's close read
  **710.555** against the official **710.705** — **fifteen cents.** A `highest_close` stamped from it would
  have been 15c low and **self-healing** by tonight. ⚠ **A loud warning whose observed instances are all
  mild teaches a future run that the shortcut is safe. It is safe on a day like today. It is not safe on a
  day with a 2% afternoon reversal, and nothing about a midday bar tells you which day you are in.**
  ⚠ **MINOR, so it is not re-discovered as a finding: the 09-24 bar's one-share late revision HAS HELD**
  (v 141,075 / n 3,719 on a second pull — it settled rather than drifting). **A re-pulled `v`/`n` mismatch
  is not evidence of a bad pull.** *(Identical 09-23 / 09-24 closes of **707.28** confirmed a **fifth**
  time, distinct OHLV — a real coincidence, not a duplicated bar. The 09-25 close of **710.705** ends that
  pause.)*

- **⚠ HIGH-WATER MARKS: NOTHING TO BACKFILL ON MONDAY, AND NOTHING WAS SKIPPED — CHECKED BY THE ROUTINE
  WHOSE WHOLE PURPOSE IS TO WRITE THEM.** `positions.md` carries **zero satellite blocks**, so
  `highest_close` is **ABSENT — the third state, carrying no `(as of …)` date at all.** ⚠ **Do not read a
  missing stamp as a failed close run: there is no field, so there was nothing to write.** **§5.4 is NOT
  ARMED**; it arms on the first **satellite** fill, and the 09-03 core fill was not one. **Thirty-seventh
  consecutive session with §5.1–§5.4 never started — UNTESTED CODE PATHS, and the running tally of "no
  exits" records the ABSENCE OF A SUBJECT.** §5.3's distance is **UNDEFINED, not large.** ⚠ **The
  distinction is FREE today and stops being free the moment a satellite fill lands** — after that, a mark
  silently not written reads identically to a mark correctly unchanged, and **only the `(as of …)` date
  separates them. Compare the date; never infer from the field's emptiness.** ⚠ **AND WHEN IT DOES ARM,
  NO BACKFILL MAY TAKE ITS MAX FROM A BAR DATED TODAY WHILE THE MARKET IS OPEN — routine 3 runs
  mid-session, so its own repair step is exposed to the partial-bar trap at the top of this list.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE.** VOO **official** closes: **09-25 710.705**,
  **09-24 707.28**, **09-23 707.28** (identical to the cent — verified a **fifth** time, distinct OHLV),
  09-22 712.69, 09-21 712.76, 09-18 701.85. **The 09-25 bar is COMPLETE** (`is_open: false` at 16:17,
  n 4,246, v 164,682). Core is **99.046311231 shares at 706.74**, cash **$30,000.00** flat, unrealized
  **+$392.72 / +0.561%** against the fill — **and §5 exempts core, so no action attaches to that number in
  either direction.** **ON THE 09-25 OFFICIAL CLOSE: equity $100,392.71, core $70,392.71 = 70.117%, cash
  29.883%, day P&L +$339.23 / +0.3391%, since inception +$392.71 / +0.3927%.** On broker marks at 16:20:
  equity **$100,387.36**, core **70.12%**, cash **29.88%**. **Forty-sixth consecutive run inside
  69.59–70.22.** ⚠ **`rebalance_delta` is NEGATIVE on both bases for the FOURTH run running (−$117.81
  official, −$116.21 broker) and the two agree to 2dp on core % — that is NOT the defect resolving, since
  the same quantity disagreed in SIGN on 09-24. A run that checks one basis and finds agreement learns
  nothing.** **NO REBALANCE IS DUE MONDAY** — §2 acts at the **65/75 band edge** and the core sits
  **~4.88 points** inside it. ⚠ **+0.3927% SINCE INCEPTION IS THIRD BEST, NOT BEST** — the peak is
  **09-21 at +0.5962%**, then 09-22 **+0.5893%**; today is **0.0005pp** ahead of 09-03's +0.3922%, **a tie,
  not a lead.** *(Checked against 25 pulled sessions. That pull reaches back to 08-21, **before the 09-03
  fill**, where the rows are **COUNTERFACTUAL** — the account held $100,000 cash — and must never be read
  as account history.)* **Audit any superlative here before repeating it.**

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`,
  NEVER a `positions` field for a close or an execution reference. Close-to-close from
  `bars --adjustment all` (⚠ **a COMPLETED session's bar**), a fresh `quote` for execution.** ⚠ **09-25
  confirms the rule FROM THE OTHER END, exactly as predicted.** On 09-24 the true move was **zero** and
  the broker reported −$127.77 — **100% artifact.** On 09-25 the true move is **+$339.23** and the broker
  reported **+$362.61** — artifact **+$23.38, only 6.9% of the move.** ⚠ **THE RULE'S VALUE IS INVERSELY
  PROPORTIONAL TO THE SIZE OF THE REAL MOVE, so it looks like pedantry on exactly the days it costs
  nothing to follow — and $23.38 would still have been reported as the day's P&L.** ⚠ **NEW AND WORTH
  KEEPING: `last_equity` read 100,024.75 — NEITHER the official prior equity (100,053.48) NOR the prior
  run's 16:15 broker equity (99,957.40). It is a THIRD number of its own, which is why the field is
  UNUSABLE rather than merely imprecise.** ⚠ **`lastday_price` is CLOSED as a question — four falsified
  mechanisms, both signs observed, and on 09-25 it read 706.99 at the pre-market, the open AND the close,
  29c below the actual prior close all day. STOP PREDICTING IT.** **Corrected post-bell `current_price`
  series, SIX observations: +$1.13 (09-18), −$0.22 (09-21), +$0.169 (09-22), +$0.02 (09-23), −$0.97
  (09-24), −$0.054 (09-25).** ⚠ **Today's is the SECOND smallest, not the smallest — 09-23's 2c holds
  that. Both signs, range 2c to $1.13, no predictable sign and no correctable offset.** **The practice of
  writing falsifiable predictions down in advance is NOT closed — keep it for live questions.**

- **⚠⚠ §1 BENCHMARK — THE STANDING FINDING JUST GOT ITS CLEANEST DEMONSTRATION, AND IT SHARPENED IN THE
  WRONG DIRECTION.** **VOO +0.4843%, the book +0.3391%, excess −0.1452pp — against the −0.1453pp PREDICTED
  by simply holding 70% core and 30% idle cash. Agreement to a hundredth of a basis point.** The satellite
  sleeve contributed **exactly 0.0000%**, as it has for the account's entire history, so the book captured
  **precisely 70% of the market's move and nothing else.** ⚠⚠ **THE "EVERY POSITIVE-EXCESS DAY WAS A VOO
  DOWN DAY" CLAIM IS NO LONGER INHERITED — THE 09-25 WEEKLY REVIEW RECOMPUTED ALL 15 POST-FILL SESSIONS
  FROM OFFICIAL CLOSES AND THE SEPARATION IS PERFECT, 15 OF 15: 9 VOO-down days ALL positive excess, 5
  VOO-up days ALL negative, 1 flat day EXACTLY 0.0000pp. NOT ONE EXCEPTION IN THE RECORD.** ⚠ **That is
  not a performance statistic — it is the signature of a book with ONE long position at 70% weight and
  NO SECOND SOURCE OF RETURN. Worst relative session: 09-21 at −0.4686pp, the day the journal calls
  "biggest dollar gain on record."** ⚠ **A GOOD DAY IN DOLLARS IS NOT A GOOD DAY AGAINST THE
  BENCHMARK, and on 09-25 those two readings point in OPPOSITE directions — which is the single easiest
  day to stop asking §1's actual twelve-month question.** *(Context, not a trade: the 10-year reached
  ~5.22% and the 30-year ~5.48–5.50% on 09-25 — a fact about what the BENCHMARK and the core sleeve are
  competing against.)*

- **⚠⚠ THE MOST DECISION-RELEVANT REJECTION ON THE BOARD, 09-25: JBL.** Anthropic committed **~$11.6B
  over seven years** to **Akamai**; Akamai's 8-K then did what open item (3) has said for a month never
  happens — **named a US-listed supplier and allocated a specific dollar figure to it**, a Build Request
  authorizing **Jabil (JBL)** to procure **~$1.7 billion of memory components**. ⚠ **And it is not
  revenue: Akamai pays "all corresponding supplier invoice amounts," Jabil holds the components "IN
  CONSIGNMENT AS BAILEE," and Akamai "will REPURCHASE such components from the Company AT COST."** A
  disclosed statement of **zero margin**. The only figure that would satisfy part 2 — Jabil's assembly
  fee — **is disclosed by nobody.** ⚠⚠ **This is a FIFTH form of open item (3)'s binding constraint and
  the ONLY one no widening of the evidence bar would relieve — widening it would have let this
  THROUGH.** The other four are about information being *withheld*; this one is **fully disclosed and
  simply the wrong quantity.** ⚠ **Do not reach for this chain again, and not at a lower price — the
  price was never the problem.** Full working in **T-2026-09-25-01**.

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES AND THE THIRD IS NEW.** **Shape one: a DRAWDOWN
  misread as priced-in** (nine instances, newest CNC −6.44% → `true`), plus three near-misses that
  cleared only because the *fall* was fractionally too small (LMT −3.61%, GM −3.95%, LH −3.83%).
  **Shape two: the filter working** on genuine news rises (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%).
  ⚠ **Shape three, 09-25 JBL: a genuine RISE UNRELATED TO THE NEWS that the window swept up** —
  +4.97% over five sessions, but the path was a grind whose largest day was **+1.72%** and whose
  **news day moved JBL +0.63%.** §4 conditions on having moved 4% "**on this news**"; the mechanized
  check cannot see causation. ⚠ **The defect is SIGN- AND CAUSATION-BLINDNESS, not the threshold.**
  ⚠⚠ **AND THE AGENT DID NOT ACT ON IT, DELIBERATELY — that is the part to carry forward.** This was
  the exact setup the "do not lower the bar" rule guards against: **a candidate the agent liked, plus
  a plausible technical case that the filter misfired.** Had part 2 not failed independently, the
  honest outcome would **still** have been rejected-on-priced-in with the defect logged. ⚠ **Not
  permission. Only a human may change §4 or `alpaca.py move`.**

- **⚠⚠ OPEN ITEM (2)'S WORST INSTANCE, AND IT FAILS TOWARD TAKING A TRADE.** **AKAM read
  `priced_in: false` at +3.19%** while its closes ran **104.53 (09-18) → 117.435 (09-21) = +12.35% IN
  ONE SESSION**, then 118.33, 118.42, then **110.44 (09-24) = −6.74%.** ⚠ **A +12.35% event move and a
  −6.74% give-back fell inside the SAME five-session window and netted to a passing +3.19%.** Prior
  instances (QCOM, AVAV) were **intraday** round trips; ⚠ **this one spans MULTIPLE SESSIONS — the
  round trip no longer has to hide inside a single bar.** AKAM was never at risk (first-order killed
  it), **but a second-order beneficiary of the same chain would have been waved straight through**,
  and ⚠ **no 09:35 re-validation would have surfaced it either — the sharpest evidence yet for open
  item (7).**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR
  JUDGMENT RATHER THAN CARE.** **73 real theses, ZERO ACCEPTED EVER**, 27 this week (09-21: 3, 09-22:
  5, 09-23: 6, 09-24: 7, 09-25: 6). ⚠ **RECOUNTED FROM SOURCE at the 09-25 close: 74 `### T-` headings
  in `research_log.md` less the template heading = 73. The figure is CURRENT as of this run, not
  carried.** Set beside that: an empty satellite sleeve, **~30% idle cash**, a weekly cap unused at
  **0 of 3**, an INACTIVE breaker, and an account at **+0.393% since inception.** ⚠ **09-25 raises the
  pressure in a new way and the distinction matters: the funnel finally produced the well-sourced,
  named-supplier, allocated-figure candidate that a month of rejections implied was the missing
  ingredient — AND IT WAS STILL NOT A TRADE. That is evidence the bar is not what is binding, NOT
  evidence the bar should move.** ⚠ **And a green day raises it a second way: the account is up
  +0.393% and simultaneously LAGGING its benchmark by exactly the cash drag, which makes "deploy
  something" feel like the obvious reading. It is not this seat's call.** §4's own position governs: a
  run that finds nothing is a successful run. **Naming the pull is the only defence against acting on
  it.** If the bar is to move, that is a `strategy.md` change and **only the human may make it.**
  ⚠⚠ **THE 09-25 WEEKLY REVIEW MEASURED WHERE THE 27 ACTUALLY DIED, AND THE FAILURE POINT HAS MOVED ONE
  TEST DOWN THE CHAIN: PART 2 IS NOW DOMINANT AT 11 OF 27 (from 4 of 16 in Week 3) WHILE PART 1 HALVED
  TO 6 OF 27 (from 9 of 16).** Full breakdown: **part 2 = 11, part 1 = 6, premise/no-Company-A = 5,
  §3 = 2, §4 priced-in decisive = 2, part 3 = 1.** ⚠ **That completes a three-week arc — Week 2 called
  the constraint the unnamed counterparty (part 1), Week 3 found a second head at part 2, Week 4 shows
  part 2 BECAME the primary one — and it REFRAMES THE HUMAN'S OPEN QUESTION from "is the evidence bar
  too high" to "can this strategy produce trades AT ALL from public disclosure, and if rarely, should
  the 30% sit in CASH or in the INDEX while it waits."** ⚠ **Neither version is this seat's to answer.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY AND THAT IS ITS NORMAL STATE.** ⚠ **09-25's
  six rejections do NOT become a queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE.**
  **JBL** (part 2, see above) · **AKAM** (first-order; and see the priced-in item) · **memory
  suppliers** (rule (v) — none named in any disclosure; **Lenovo** is the one other named supplier and
  is **§3 outright**, HK-listed with only an OTC ADR) · **RDW** ($980M is a **multiple-award CEILING
  across 15 vendors**; also first-order; also below the §3 floor) · **FLNC** (no value disclosed; EVE
  Power is Shenzhen-listed) · **the rate/oil/PMI complex** (environment input, not a Company A).
  ⚠ **AND 09-24'S SEVEN WERE NOT REHABILITATED EITHER** — no `move`, `quote`, `bars` or `asset` call
  on ILMN, GRAL, BBY, PYPL, SHOP, SoftBank/OpenAI or ELMT. **A rejection is not a queue.**
  ⚠ **ELMT ENTERED THIS FUNNEL THREE TIMES IN THREE SESSIONS AND THE THIRD TIME CARRIED A DISCLOSED
  PRICE ($124.75M) — EXACTLY THE MATERIAL WHOSE ABSENCE KILLED THE FIRST TWO. IT WAS NOT SCREENED, and
  that refusal COST something.** "But now there is a number" is the purest form of the pull to re-open
  a §3 kill on evidence §3 does not weigh. **A microcap with a Vietnam-listed counterparty is
  ineligible at every price and at every level of disclosure. Do not screen it again.**
  ⚠ **One §3 question remains reached-but-undecided: Shopify is a Canadian issuer trading as common
  stock on a US exchange, which §3's "US-listed common stock" does not obviously settle. A future run
  reaching this with a LIVE candidate must put it to the human rather than decide it from this seat.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — NINE CATCHES, AND THEY KEEP CHANGING SHAPE.**
  ⚠⚠ **(9) IS NEW ON THE 09-25 WEEKLY REVIEW AND IT IS THE WORST SHAPE YET: A COUNTER WHOSE *UNIT* IS
  WRONG.** Every close journal reports §5.1–§5.4 as untested for *"the Nth consecutive **SESSION**"* —
  **23 on 09-21, 26 on 09-22, 29 on 09-23, 33 on 09-24, 37 on 09-25.** ⚠ **It increments by THREE OR
  FOUR per trading day. Sessions increment by ONE. The account has operated EIGHTEEN sessions since
  2026-09-01, so "thirty-seventh consecutive session" is MORE THAN TWICE the account's entire age and
  cannot be sessions under any reading. It is a RUN counter wearing a session label.** ⚠⚠ **This is
  worse than (2)'s stale count and (7)'s miscount, because the value is NOT stale and the arithmetic is
  NOT wrong: re-running the check REPRODUCES THE SAME NUMBER, and only comparing it against the
  CALENDAR exposes it.** **The fact it encodes is true and unchanged — §5 has never had an operand —
  ONLY THE UNIT IS FICTION.** ⚠ **Report it as 18 sessions, or as a run count called a run count. Note
  the separate "zero positions for the Nth consecutive session" counter (25 on 09-25) increments
  CORRECTLY by one per session and is a different series — do not merge them.**
  ⚠⚠ **(8) IS NEW ON 09-25 CLOSE AND IT CAME FROM THE PREVIOUS RUN, SIX HOURS OLD — THE SHORTEST-LIVED
  CLAIM YET CAUGHT.** **(8) A MEASUREMENT PRESENTED AS A CALIBRATION: the midday run's *"the volume
  tracks elapsed session time almost exactly"* (v 69,713 = 49.5% of the four-session mean at 49.0%
  elapsed).** ⚠ **The completed session falsifies it — actual volume 164,682, 16.9% above that mean, so
  the partial held 42.3% at 49.0% elapsed.** ⚠ **The shape to learn: the claim was arithmetically
  correct and its DENOMINATOR was the error. A ratio against a prior-day mean LOOKS like a measurement
  of the current day and is not one. Full correction at the top of this list.**
  ⚠⚠ **AND A NINTH THING WAS CAUGHT BEFORE IT WAS WRITTEN RATHER THAN AFTER — THE FIRST TIME.** The
  09-25 close nearly wrote *"best since inception"* on a +$339.23 day, pulled 25 sessions first, and
  found it is **THIRD** (09-21 +0.5962%, 09-22 +0.5893%, then today, 0.0005pp ahead of 09-03 — a tie).
  ⚠ **Catch (1) is this exact shape caught three runs late and by accident. This one cost one `bars`
  call. PULL THE SOURCE BEFORE WRITING THE SUPERLATIVE, NOT AFTER.**
  **(6) A SCOPE CLAIM:** *"routine 2 is the ONLY routine that runs with `is_open: true`"* — falsified by
  the run that read it, from its own clock. ⚠ **The most dangerous shape, because it was not a number to
  re-pull but a statement about the SYSTEM'S OWN SHAPE, which no data call would ever contradict.**
  **(7) A MISCOUNT IN A VERIFICATION CLAIM:** the 09-24 close run wrote that it had *"verified all TWELVE
  keys present."* ⚠ **There are THIRTEEN.** `common.read_state()` returns `last_run, prior_run, week_of,
  new_positions_this_week, consecutive_closed_losses, circuit_breaker, halt_triggered_at,
  core_established, core_ticker, core_pct, satellite_pct, cash_pct, open_thesis_ids`. ⚠ **The check was
  almost certainly run correctly; it is the REPORT of the check that was wrong — which is worse, because
  a wrong count in a sentence that says "verified" is exactly the claim a later run would not re-check.**
  *(Re-parsed at the 09-25 close: **13 keys**, all present, no `#` anywhere in the block.)*
  **(1)** A false superlative (*"positive for the first time in this account's history"*) survived
  three runs, caught **by accident** on 09-21. **(2)** A stale count (*"49 theses"*) caught
  **deliberately** on 09-22, running in the direction that **understates** the problem. **(3)** The
  09-22 claim that `lastday_price` rebuilds at a session boundary, falsified 09-23. **(4)** The 09-23
  claim that it does **not**, falsified 09-24. **(5)** A **TRUNCATED SERIES**, 09-24: the three-item
  post-bell `current_price` record had silently dropped its own largest member. **Corrected series is
  in the standing-rule item above — SIX observations now. DO NOT QUOTE THE THREE-ITEM VERSION.**
  ⚠ **A superlative, count, mechanism, SERIES or CALIBRATION inherited from a prior run is NOT a checked
  fact** — it is the cheapest claim to write and the most expensive to verify. **Assume the next one you
  are handed is wrong until you have pulled the source.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — TWENTY-SEVEN CONSECUTIVE REFUSALS, AND THE LAST THREE ARE ALL
  WEAK.** ⚠ **Graded honestly: the 09-25 open, midday and close all made ZERO `move` and ZERO `quote`
  calls; the midday and close runs have no research step at all, and none of the three had anywhere to
  put a number — the refusals cost nothing and are recorded as weak.** The disqualifying facts do not
  move: **GNRC is the named counterparty in the Amazon announcement — first-order, outside §4 at any
  price** — and **open item (7) is resolved by a human editing §4 or `alpaca.py move`, not by a number
  this seat collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER EACH REFUSAL COST ANYTHING, AND
  MANY DID NOT. Quoting the bare count overstates the evidence.** The strong instances are the
  pre-market runs of 09-23, 09-24 and 09-25 — all three opened the data plane against a live funnel
  **and** had somewhere to put a number. ⚠ **No new costume in seven sessions; the list looks
  CONVERGING rather than growing, and a run that manufactures a new name for an old experience would be
  padding the log.** Costumes: diligence, curiosity, tidiness, completeness, zero-marginal-cost,
  self-audit, proxy-procurement, issue-closure, call-already-open, screen-already-running. **The pattern
  is the finding, not any instance. FREE IS NOT THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FIFTY-FIVE RUNS.** §5 exempts core from all
  four sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the
  strategy exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids
  outright.** ⚠ **Grade these as the GNRC count is graded.** The sharpest instances are the close runs
  of 09-22, 09-23, 09-24 and **09-25 — the last of which grades HIGH: routine 4's Step 2 is THE
  dedicated write step, the run arrived holding a fresh official close (710.705), and the field it
  would write to was empty.** The **09-25 midday** grades just as high for the mirror reason: a
  DEDICATED REPAIR step is if anything the sharper temptation, since "backfill the missing mark" reads
  as fixing an omission rather than adding a row. ⚠ **"Nothing to write" — and "nothing to repair" — is
  the correct output of an empty Step 2, not an invitation to find a row to write it to.** **Measure the
  core from the 706.74 fill and from an official close, never from a `positions` field.** ⚠ **Noted
  honestly: this refusal is now close to automatic, and automatic is not the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN
  IS USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell
  sees it pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with
  **no bar for today**. ⚠ **09-22 read all three shapes in one day, and consecutive runs read IDENTICAL
  booleans meaning opposite things.** **`is_open: TRUE` is the one case where the boolean alone is
  sufficient, and it is safe to read it that way ONLY because TRUE has a single meaning. FALSE has
  three.** *(09-25 read all three of its shapes: pre-market FALSE with `next_open` at today, in-session
  TRUE at 09:36 and 12:41, post-bell FALSE at 16:17 with `next_open` at Monday 09-28.)* ⚠ **THE
  STRONGER DISCRIMINATOR FOR A FALSE IS TO CHECK THAT A DAILY BAR FOR TODAY EXISTS — run it before
  deciding a run is a holiday skip. The 09-25 close ran it: the bar exists and is COMPLETE.** ⚠ **But
  with `is_open: true` that same bar is PARTIAL and is not a close — see the top item.**

- **⚠ SEVEN ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — nine instances plus three
  near-misses; **there is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on
  the bill. ⚠ **A pass on a fall is not evidence the filter worked, and neither is a FAIL on a fall** —
  recorded **deliberately as NOT the reason for the rejection**, so no run inherits "rejected because
  priced-in" as a fact. **Detail and the third shape are in the priced-in item above.**
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM, AVAV,
  and ⚠ **AKAM (09-25), the first MULTI-SESSION round trip and the worst instance recorded.** Same
  root cause as (1), opposite direction. **The fix for (1), (2) and shape three is a human editing §4
  or `alpaca.py move`** — and the suggestion on the record is to make it **read SIGN and causation,
  not loosen or remove the threshold.**
  **(3)** The satellite sleeve is **structurally undeployed — 73 theses, zero positions, ever.** A
  70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market, ⚠ **and 09-25
  is the cleanest arithmetic demonstration on record: excess −0.1452pp against −0.1453pp predicted by
  the cash weight alone.** **§2 permits the cash and §4 says most runs end in no trade — both rules
  were followed, and the agent must NOT respond by lowering the §4 bar.** **The binding constraint has
  FIVE known forms:** the source withholds the counterparty's number; **or** the counterparty discloses
  **roadmap instead of segment revenue**; **or** the named beneficiary is **vertically integrated** with
  no external supplier to find; **or** **both parties expressly refuse to disclose as a commercial
  choice** (GM); ⚠ **or — the JBL form — THE FIGURE IS FULLY DISCLOSED AND IS THE WRONG QUANTITY.**
  ⚠ **Only the first two are addressable by widening the evidence bar. Forms three, four and five are
  not, and form five would be made WORSE by widening it.** ⚠ **ELMT is the standing proof that evidence
  is not the constraint: it withheld NOTHING and still produced no trade, because the obstruction was
  STRUCTURAL (§3).**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the
  prior close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11: measured from
  the fill, tracking error 0.0000%. Keep measuring it from the fill.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it
  never had a stable size and never will. ⚠ **It is not a P&L problem — it is a PRICE-SOURCE problem
  that contaminates every derived figure.** It has flipped the sign of a §2 quantity (`rebalance_delta`
  +$12.78 broker vs −$16.04 official on 09-24), ⚠ **and on 09-25 all three runs AGREED in sign, which
  establishes the defect is INTERMITTENT — worse than persistent.** ⚠ **Cleanest small reading on
  record, 09-25 post-bell: 5.4c on the price, $5.35 on equity, $23.38 on the day's P&L. The sharpest
  demonstration remains the 09-25 open's 50c inside the SAME MINUTE on the same basis.** **Whether the
  tooling should read closes from `bars` by default is a human's call, and the accumulated evidence says
  it should.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it
  passed all five checks on 09-11 while `clock` returned 500 and `quote`/`bars` returned 504, **and on
  09-24 while a `perplexity.py` QUERY returned 500 — the first instance on the RESEARCH plane.** ⚠ **The
  09-24 transient did not recur on 09-25 — single occurrence, still no alert.** **Until a human changes
  it: probe by hand; never infer data-plane health from a green selftest, and CHECK EXIT CODES — never
  infer thin news from empty results.**
  **(7)** **`alpaca.py move` cannot see an after-hours event, and neither can the 09:35 re-validation
  that exists to catch exactly this.** ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a
  trade rather than skipping one**, which is why it is listed last and should be read first. ⚠ **AKAM
  generalises it: the entire +12.35% event move was hidden from the filter by a later give-back inside
  the same window. The blindness is not only to AFTER-HOURS events — it is to ANY event move the window
  later cancels, and no 09:35 re-validation would surface either.** **It has cost zero only because no
  plan has yet carried a BUY intent — an absence of exposure, not a mitigation.**
  Prior context in ClickUp `86bbv75bz`; week-prior `86bbzgbg3`. **09-25 daily summary: `86bc7vgbw`**
  (09-24: `86bc76x35`).

- **⚠⚠ WEEK 4 REVIEW (2026-09-25) — RAN, POSTED `86bc7vzam`, AND IT REPLACES THE WEEK 3 ITEM.
  THE §1 ANSWER IS NO, AND FOR THE FIRST TIME EVERY WINDOW SAYS SO.** Satellite **0.0000%**, so its
  dollar-weighted excess is exactly **minus VOO's total return**: **−1.262pp week, −0.827pp since
  inception, −0.974pp 1M, −5.444pp 3M, −18.571pp rolling 12M.** ⚠ **Week 3's first three rows were
  POSITIVE (+0.095 / +0.430 / +0.509pp). The market rose and the whole column inverted with NO rule
  change and no change in the sleeve** — which is exactly what three consecutive reviews predicted in
  writing when they refused to read those positives as performance. ⚠ **DO NOT RE-INHERIT THE PLEASANT
  VERSION; it was a property of a falling tape and it is gone.** Structural cost now **~5.57pp per
  rolling 12M**, up from 4.97pp **because the BENCHMARK improved, not because the sleeve got worse.**
  **Account week +0.8813% vs VOO +1.2617% = −0.3804pp, which is EXACTLY 0.6985 × VOO to four decimals;
  since inception +0.3927% vs +0.8271% = −0.4344pp, EIGHT TIMES last Friday's −0.055pp on five up
  sessions and an unchanged entry gap.** ⚠ **DAILY AUDIT, RECOMPUTED NOT INHERITED — 15 post-fill
  sessions, 9 VOO-down days ALL positive excess, 5 VOO-up days ALL negative, 1 flat day EXACTLY zero.
  Separation is PERFECT, 15 of 15: the sign of this book's daily excess is entirely determined by the
  sign of VOO's move, with no exception in the record.** **Reject board re-measured: 65 names, 20 beat
  VOO, 45 lagged, mean −2.04%, median −2.47%.** ⚠ **A tally, not a result.** ⚠ **HPE IS NO LONGER THE
  LARGEST OPPORTUNITY COST — CRDO IS, at +24.28pp (from +4.68pp in five sessions); HPE +20.67pp, MU
  +14.42pp, QCOM +13.11pp (the largest MOVE, from +0.76pp), LITE +11.16pp.** ⚠ **NEW FINDING: six of
  the top six excesses are ONE THEME (AI/data-centre hardware and semis) rejected under FIVE DIFFERENT
  §4 rules, every rejection individually correct — §4's three most active tests each independently
  exclude a running theme. Input to the human's open question, NOT permission to change anything.**
  ⚠ **AND A CORRECTION TO WEEK 3'S OWN HEADLINE: it promoted the board's "widening" as the finding.
  Dispersion grows with elapsed time MECHANICALLY. The MEAN is the evidence the four-part test
  discriminates.** Full working in `weekly_review.md`.
  ⚠ **FILE SIZE — TENTH CONSECUTIVE FLAG AND THE RATE IS ACCELERATING.** `research_log.md` **333KB**,
  up from **226KB** last Friday — **+107KB in one week on 27 theses**, faster than the +75KB Week 3
  already called urgent. `journal.md` **162KB**. **589KB that every run reads in full.** ⚠ **THE WEEK 4
  REVIEW CONSIDERED RUNNING THE ROLLOVER EARLY AND DELIBERATELY DID NOT — every entry is dated 2026-09,
  which IS the current month, and splitting a live month across two files for five sessions is the
  exact failure the archive exists to prevent, arriving early. THE 2026-10-02 REVIEW MOVES THE WHOLE
  SEPTEMBER CORPUS IN ONE DESIGNED OPERATION AND IS FIVE SESSIONS AWAY. Do not re-litigate this weekly;
  a human who disagrees should say so in `control.md`.**

- **⚠ A `#` IN A FENCED-BLOCK VALUE SILENTLY TRUNCATES IT.** `_parse_kv` in `scripts/common.py` does
  `line.split("#", 1)[0]`, so **everything after the first `#` in a `key: value` line is discarded by
  the parser.** The 09-24 close run did this to itself and caught it before commit. ⚠ **STANDING
  CONSEQUENCE: never put a `#` in a fenced-block value, and VALIDATE `state.md` WITH
  `common.read_state()` AFTER REWRITING IT — writing the block and parsing the block are not the same
  check.** *(Done at the 09-25 close: block re-parsed, **THIRTEEN keys** — not twelve, see catch (7) —
  all present, no `#` anywhere in the block, and the long values compared **against the file** rather
  than eyeballed, which is the only way truncation is actually visible.)*

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** compared to **consensus** rather than to any prior
company figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations**
(Centene, Southwest, General Mills), **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence,
Alcoa/South32, Nocera/E-PRO), **a genuine transaction whose DELIVERY MILESTONE is recycled as the
news** (GM/Lockheed), **a PRE-IPO CONTRACT BOOK** (Nscale's $103B), and ⚠ **09-25: A FORMAL PRESS
RELEASE RESTATING AN ALREADY-FILED 8-K (Akamai/Anthropic — sources gave conflicting disclosure dates,
the conflict was NOT resolved and must not be asserted either way, but the tape moved +12.35% on 09-21
and FELL 6.74% on the 09-24 "announcement" day; a stock does not fall 6.74% on the day it learns of an
$11.6B contract).** ⚠ **STANDING PRACTICE: ask a transaction WHEN IT HAPPENED before asking who it
helps — and WHEN THE SOURCES DISAGREE ON THE DATE, THE PRICE SERIES IS THE CHEAPER WITNESS.** One
screen settles it, and it is the cheaper of the two kills. *(09-17 Amazon/Generac was the first clean
rule (iii) PASS; 09-24's Elmet/Masan the second.)*
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — resolved 09-11 on a number).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share,"
"the only company that makes X" are facts about an **industry**, not a **transaction** — plus the
**CEILING sub-shape**. Costumes: a **table** (DoD daily contracts digest), a **consortium awardee**
(Abrams), a bare sentence, and ⚠ **09-25's TWO: a MULTIPLE-AWARD CEILING across fifteen vendors read
as one company's revenue (RDW, "$980M"), and an UNNAMED SUPPLY BASE made to look nameable by an exact
figure and a named component category ($1.7B of "memory components," with no manufacturer disclosed
anywhere).** ⚠ **The second is the more dangerous: the blank LOOKS fillable because the suppliers are
countable on one hand. The source left the blank; filling it in is not research.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.*
Long-dated energy offtake is **a standing feature of this funnel, not a visitor** — Sempra/Petrobras,
Venture Global/China Gas, Amazon/Generac, Centrus/Antares, Elmet/Tungsten West, NeoVolta/SK On.
⚠ **The REGULATORY version: a non-binding advisory vote → an undated FDA decision → reimbursement →
commercial ramp (ILMN) is the same shape wearing a lab coat.** **Part 3 kills these in ONE step.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part
2.** Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; Brookfield/Bloom's **$25B** is
a **FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**; SoftBank's **$11.1B** is **capital paid IN to a
private recipient**; Royal Caribbean's **~$3B** for Sandals is **capital paid OUT by the buyable leg**;
BBY's only disclosed economics was **Meta taking "a small fee" — a COST at the candidate, described in
language that reads like a partnership benefit**; FMC/Tessenderlo's **$403M is a SECONDARY-MARKET SHARE
PURCHASE — money to selling shareholders, never to the company.**
⚠⚠ **AND THE DEFINITIVE INSTANCE, JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K —
AND IT IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A
disclosed statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.**
⚠ **A large, real, sourced, prominently-placed number is not a dollar path. THIS IS THE WORKED EXAMPLE
TO REACH FOR FIRST.** T-2026-09-18-04 (BLK) remains the other: **part 1 passed cleanly and it died on
the absent segment figure, NOT on size.**

**⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT WORKS IN BOTH SIGNS.** Two companies moving on the same
macro input (a crush spread, a mortgage rate, a rate decision) is a **market**, not a **transaction**,
and the giveaway is that part 1 needs an *"and also"* clause. ⚠ **A DIVERGENCE between two named
companies sounds causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge and ADM) — and the convergent
version is MORE DANGEROUS, because agreement LOOKS LIKE CORROBORATION when it is in fact the clearest
possible statement that the input is a market variable.** ⚠ **The third and most respectable face is a
COMPETITOR'S EARNINGS PRINT** (AutoZone's FQ4 read across to GPC/ORLY/LKQ). **The giveaway never
changes: the sentence needed an "and also".**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — AND IT IS THE MOST CONVINCING NON-EVENT THE FUNNEL
PRODUCES.** Two of 09-23's six theses died on this premise (CMS's preliminary lab fee schedule; the
ACA enrollment halt). ⚠ **This is the FOMC object — an environment input — but in a far more persuasive
costume: a policy action is SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN AFFECTED INDUSTRY, and MOVES
THE TAPE ON THE DAY.** It nonetheless has **ONE party.** ⚠ **A long-only book cannot trade money being
WITHDRAWN from a sector unless some NAMED party receives it — and nobody does.** ⚠ **09-25 supplies the
FULL-MARKET-SCALE VERSION and it is the most tempting yet: the 10-year at ~5.22%, the 30-year at
~5.48–5.50%, Brent near $106, PMIs at 52- and 59-month highs, swaps pricing three more hikes. SCALE
MAKES IT MORE CONVINCING, NOT LESS. Every "who wins from higher rates / higher oil" answer needs an
"and also".** ⚠ **The counter-case still stands and must not be over-applied against: an FDA advisory
vote (ILMN/GRAIL) ENABLES a named company's product and that company has a named supplier — a real
two-party chain. Do not over-apply this rule to approvals.**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is
**exits-only by construction** and may not open a position under **any** circumstance. Routine 2
executes **only what `plan_today.md` already contains** — a position opened at 09:35 without a plan
entry routes **around** the discipline rather than satisfying it. Routine 4 **RECORDS AND JOURNALS; IT
DOES NOT TRADE.** ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
opportunity any of those seats may act on** — ⚠ **and neither is a green day that still lags the
benchmark.** New positions route through pre-market research **plus** the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.**
The gate has now been exercised **TWENTY-EIGHT times and has never fired**, and its alert path
**remains untested code.** ⚠ **Twenty-eight quiet opens are NOT evidence it works. The first morning it
fires will by construction be a morning when the pre-market run failed — i.e. exactly the morning with
no fresh notes to lean on. Read routine 2's Step 2 then; do not recall it.** ⚠ **09-24's and 09-25's
opens are the cleanest demonstrations: both plans were FRESH and EMPTY, and each produced a run
BYTE-FOR-BYTE identical to what a stale plan would have produced. Only `plan_date` told them apart.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a
broker mark on one leg against an official close on the other. **Both legs from the same source, and
for returns that source is `bars --adjustment all`** ⚠ **— on a COMPLETED session.** ⚠ **And state
WHICH basis produced any figure you quote.**

### Do not reach for these — disposed rejects and the trap in each

⚠ **Added 09-25:** **JBL** — ⚠ **the most important entry on this board.** Part 1 passes **cleanly**,
every party is named, the instrument is signed and filed, and the figure is **$1.7 billion in an
8-K** — **and part 2 fails outright**, because the money is Akamai's, the components are held **in
consignment as bailee**, and the repurchase is **expressly at cost**. **Jabil's assembly fee is
disclosed by nobody.** ⚠ **Do not reach for this at a lower price; the price was never the problem.**
**AKAM** — **first-order**; and its `priced_in: false` at +3.19% is an **artefact of a +12.35% jump
and a −6.74% give-back inside one window**, ⚠ **NOT a clean pass.** **Memory suppliers to the Akamai
build** — **no manufacturer named in any disclosure**, rule (v); and <10% of revenue for any of them
even if named. **Lenovo** — **§3 outright**, HK-listed with only an OTC ADR, no value disclosed.
**RDW** — the **$980M is a multiple-award CEILING across 15 vendors** with no Redwire allocation;
first-order; ~$1–2B, below the §3 floor; ⚠ **its `priced_in: false` on a +0.61% flat tape is NOT a
point in its favour.** **FLNC / EVE Power** — **no value or volume disclosed by any party**; EVE is
Shenzhen-listed; Fluence below the floor and already disposed under rule (iii). **The rate / oil / PMI
complex** — environment input, one party, no named recipient. **FMC / Tessenderlo** ($403M **secondary
share purchase**) · **LLY / InnoCare** (no value disclosed; LLY first-order; InnoCare HK-listed) ·
**NOC $123.8M, RTX $50.1M, Stark $114.0M, Southern $22.0M, RGAS $23.6M** (DoD digest, rule (v); all
≪10% of revenue; Stark not separately US-listed) · **Blue Cloud Softech / IBM** (Indian-listed) ·
**FingerMotion** (offtakers unnamed) · **Everforth, Endovia, Algorhythm** (private or microcap) ·
**Amazon's $100M Greenwood plant** (immaterial; no counterparty) · **Welspun** (§3, buyer unnamed).

⚠ **Added 09-24:** **ILMN** — the GRAIL advisory vote is **non-binding with the FDA decision
pending**, so part 3 is several quarters out; **+11.54%, a GENUINE priced-in kill**; ⚠ **the most
seductive second-order shape in weeks, and the thesis was never written because the filter ran
first.** **GRAL** — **first-order**, and **+44.67%**, the largest five-session move ever recorded
against a candidate here. **BBY / PYPL / SHOP** (Meta Muse commerce) — ⚠ **part 1 passes CLEANLY on
all three and NOT ONE commercial term exists**; the only economics described is **Meta taking a fee, a
COST at the retailer**; SHOP also **+9.61%**. ⚠ **BBY and PYPL would have FAILED the correlation check
against each other.** **SoftBank / OpenAI $11.1B** — recipient **private**; the compute-supplier
inference is rule (v). **ELMT / Masan** — ⚠ **THREE appearances in three sessions, the third carrying
a disclosed $124.75M. ~$634M microcap, Vietnam-listed counterparty, §3 on both legs. DO NOT SCREEN IT
AGAIN AT ANY LEVEL OF DISCLOSURE.** **QCOM / PickNik** · **RCL / Sandals** (~$3B **capital OUT**) ·
**Fiserv** Canada · **NeoVolta / SK On** · **Nocera / E-PRO** · **Crossject / BARDA** · **Elroy Air** ·
**Quanome** · **Costco, Jabil, Darden, TD SYNNEX, Vail** (upcoming estimates, no event yet).

⚠ **Added 09-23:** **GIS** — an **own-results earnings print has ONE party**; ⚠ **it does not become a
buy on a better quarter.** **LH / DGX** — CMS lab fee schedule, a **REGULATOR'S ACTION**, preliminary
for CY2027–2029; ⚠ **LH's `priced_in: false` on a −3.83% FALL is an artefact and is NOT the
rejection.** **CNC / MOH / OSCR** — government policy action, **$2.2B is money the government STOPS
paying**; ⚠ **CNC's `priced_in: true` on a −6.44% FALL is an artefact and is NOT the rejection.**
**ELMT / Tungsten West** — ⚠ **the disclosure was COMPLETE and it still failed — do not reach for it
as "the well-sourced one."** **LHX** — first-order, no contract value; ⚠ **the $22.9B RAYTHEON
Tomahawk figure is AUGUST and a DIFFERENT CONTRACTOR — it must never migrate into an LHX entry.**
**GFS** · **Nth Cycle / Glencore** · **ZEO / Ewyze** · **V2X** · **Boeing / SPEEA** · **MiMedx** ·
**NIIT** · **Michigan oil antitrust dismissal** · **"SK Hynix eyeing Intel's Ohio site"** — ⚠ **a
headline built out of the word "eyeing."**

⚠ **Added 09-22 and earlier:** **ACN** (first-order, <1% of revenue, ⚠ **`priced_in: true` on a −4.58%
FALL is an artefact**) · **Nscale / Microsoft / Anthropic** (private parties) · **Vicor** (below the
§3 floor; ⚠ **the event had NO defect at all and still produced nothing**) · **GPC / ORLY / LKQ** ·
**Paramount / WBD** · **Applied Materials** · **Vistra / New Era** · **Navitas, Magnachip, Priority
Technology** · **Telix / ITM**, **Capricorn/DNO, BEML/NHSRCL, Welspun/AMC** (not US-listed, §3) ·
**HealthEquity, Lamb Weston, AEP, Nucor, Steel Dynamics, Labcorp, Nordson, Eli Lilly** (prints vs
consensus, rule (iii)) · **AMD, Intel, Arm** (**a record green tape is not a Company A**) · **GNRC**
(first-order; see the live item) · **GM** (part 2 unwritable **by both parties' deliberate commercial
choice**; ⚠ **the −3.95% is not the reason**) · **BE / Bloom** ($25B financing ceiling) · **BG and
ADM** · **GFS and MRVL** · **LEU / Antares** · **BLK / TotalEnergies / GIP** (capital in) · **Lennar
and its suppliers** · **Baker Hughes / Chart** · **US Army / Skyeton** · **the FOMC's +25bp, fund
outflows, the data calendar, Bowman's SVB speech, the enforcement digest** (environment inputs).
⚠ **Four loud 09-11 headlines still have no primary source and none has appeared since. Absence of a
source after this long is itself the finding.**

### Established facts — do not re-derive

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional $70,000.00**,
  order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**, verified terminal
  before it was written. Audit record in `trade_log.md`. **No order has ever reached a non-terminal
  state in this account, and no order has been placed since.**
- **The core is deliberately NOT tracked in `positions.md`.** §5 exempts it, so it has no thesis
  state, no timing window and no `highest_close`. ⚠ **Every reconciliation compares SATELLITE blocks
  to SATELLITE Alpaca positions** — a run that compares the raw ledger to the raw broker will read a
  correct ledger as broken.
- **Counters as of the 2026-09-25 CLOSE, RECOUNTED FROM SOURCE THIS RUN: 73 real theses since
  inception** (74 `### T-` headings less the template), **0 accepted, 73 rejected, 27 this week
  (09-21: 3, 09-22: 5, 09-23: 6, 09-24: 7, 09-25: 6); 0 satellite positions ever opened; 0 exits ever;
  `alerts.md` empty — zero open, zero SYSTEMIC.** ⚠ **The figure is CURRENT as of this run. Recount
  from `research_log.md` before quoting it anywhere human-facing if any run has added a thesis since.**
- **`week_of` 2026-09-28, `new_positions_this_week` 0 of 3 — ADVANCED BY THE 09-25 WEEKLY REVIEW,
  which is where the reset belongs.** ⚠ **Monday's runs will compare their week anchor to 2026-09-28,
  find it already matches, and correctly do nothing. That is the reset having been done, NOT a run
  that skipped it.** ⚠ **The two counters are independent: 27 theses this week and 0 positions this
  week are both correct — §6's cap counts POSITIONS OPENED.**
- **2026-09-25 was a full trading session** (bar complete: c 710.705, n 4,249, v 164,723 on the
  review's own re-pull — the late one-share/one-trade settling is normal and is NOT a bad pull) and
  **both its daily summary (`86bc7vgbw`) and its WEEKLY REVIEW (`86bc7vzam`) were posted.** ⚠ **THE
  ROUTINE 5 WEEKLY REVIEW FOR 09-25 IS DONE — it is not owed again, and the next one is 2026-10-02,
  which is also the MONTHLY ARCHIVE ROLLOVER.** `research_log.md` is **333KB**.
