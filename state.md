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
last_run: 2026-09-25 08:24 ET 1-premarket-research (selftest PASSED all five checks, trading_enabled true, LIVE paper, broker equity 100299.16 at pre-flight; ZERO ORDERS - routine 1 does not trade; clock is_open FALSE at 08:24:08 with next_open 2026-09-25T09:30 pointing at TODAY - the PRE-MARKET shape, not a holiday, a session is due; RECONCILIATION CLEAN - positions returns ONE row core VOO 99.046311231 shares unchanged since the 09-03 fill, avg_entry 706.74, cost_basis 69999.99, market_value 70299.16 broker mark; zero satellite blocks vs zero satellite Alpaca rows, they agree; 5.1-5.4 had NO OPERAND for the THIRTY-FOURTH session, 5.4 STILL NOT ARMED, all four remain UNTESTED CODE PATHS and the tally of no-exits records the ABSENCE OF A SUBJECT; highest_close ABSENT third state so NO backfill owed, zero bars calls due on any satellite symbol and zero made; RESEARCH RAN IN FULL AND PRODUCED NO TRADE - four Perplexity scans ALL EXIT 0 (09-24 transient 500 did NOT recur), SIX candidates reached a research_log entry and ALL SIX REJECTED (T-2026-09-25-01 JBL, -02 AKAM, -03 memory suppliers no ticker, -04 RDW, -05 FLNC, -06 the rate/oil/PMI complex), four alpaca move calls as 4 hard filters (JBL AKAM RDW NOC); PLAN WRITTEN WITH ZERO BUY, ZERO SELL, ZERO REBALANCE INTENTS, plan_date 2026-09-25; THE FINDING OF THE RUN IS T-2026-09-25-01 - the Akamai/Anthropic chain delivered a NAMED US-LISTED SUPPLIER WITH AN ALLOCATED DOLLAR FIGURE QUOTED VERBATIM FROM AN 8-K, the thing open item (3) says never arrives, and it STILL produced nothing because the 1.7B is capital paid IN by Akamai, held IN CONSIGNMENT AS BAILEE, and repurchased AT COST, so it is NOT revenue at Company B - a FIFTH form of open item (3) and the only one WIDENING THE EVIDENCE BAR WOULD NOT RELIEVE; the priced-in filter fired FIRST on JBL at +4.97 pct but is NOT the reason and must never be inherited as one, the move was a five-session grind whose largest day was +1.72 pct and whose NEWS DAY moved JBL only +0.63 pct - a THIRD defect shape for open items (1) and (2), deliberately NOT acted on because changing the 4 bar is a strategy.md change only the human may make; AKAM priced_in FALSE at +3.19 pct is the WORST open-item-(2) instance ever recorded - a +12.35 pct single-session jump on 09-21 and a -6.74 pct giveback on 09-24 netted inside ONE five-session window, and the tape settles that the market learned on 09-21 not on the 09-24 press release, standing rule (iii) in a NEW costume; lastday_price RESOLVED ON ITS PRE-REGISTERED THIRD BRANCH reading 706.99, 29c BELOW the official 707.28 and matching no recent official close, so the field is wrong in a FOURTH way and the error now has BOTH SIGNS (+32c 09-24, -29c today) - NO FURTHER PREDICTION IS OWED, the field is unusable; sleeves on broker marks equity 100299.16, core 70299.16 = 70.09 pct, satellite 0.0 pct count 0, cash 30000.00 = 29.91 pct, core_in_band TRUE, rebalance_needed FALSE, rebalance_delta -89.75; recomputed on the official 09-24 close 707.28 equity 100053.48, core 70053.48 = 70.016 pct, cash 29.984 pct, delta -16.04 - BOTH NEGATIVE, the two bases AGREE IN SIGN today unlike 09-24, which shows the defect is INTERMITTENT not resolved; NO REBALANCE DUE on either basis, core sits ~4.9 points inside the 65/75 band edge, FORTY-THIRD consecutive run inside 69.59-70.22; core VOO NOT stamped, FIFTY-SECOND refusal and a WEAK one graded honestly; GNRC NOT looked at, TWENTY-FOURTH refusal and a STRONG one - four move calls issued with a live funnel and a research step to put a number in, not made; ELMT NOT re-screened, a THIRD headline in three sessions now carrying the 124.75M figure whose absence killed the first two, refused under the standing instruction and this refusal COST something; WEEK ROLLOVER CHECKED - Friday 2026-09-25 confirmed via TZ=America/New_York, ISO Monday 2026-09-21, week_of already 2026-09-21, SEVENTEENTH consecutive run to find the reset already done, new_positions_this_week stays 0 of 3, next boundary Monday 2026-09-28; LOSS STREAK - nothing closed and nothing has EVER closed so consecutive_closed_losses stays 0 and it HAS NEVER HAD AN INPUT, breaker INACTIVE, halt_triggered_at none so NO HALT_CLEARED_AT comparison required and NO circuit-breaker alert due; research_log APPENDED with six entries, RECOUNTED FROM SOURCE this run 74 T- headings less the template = 73 REAL THESES, ZERO ACCEPTED EVER, 27 this week (09-21: 3, 09-22: 5, 09-23: 6, 09-24: 7, 09-25: 6); research_log grew to ~333KB, monthly archive rollover due 2026-10-02 and TODAY is the last weekly review before it; trade_log correctly left unappended; alerts.md empty, zero open incidents, zero SYSTEMIC)

prior_run: 2026-09-24 16:15 ET 4-market-close-journal (selftest PASSED all five checks, trading_enabled true, LIVE paper, broker equity 99957.40; ZERO ORDERS; clock is_open FALSE at 16:15:53 with next_open 2026-09-25 - the POST-BELL shape, and a VOO daily bar for 2026-09-24 EXISTS so a session happened, run not inferred; THE DAY'S TRUE MOVE WAS EXACTLY ZERO - VOO official close 707.28 IDENTICAL TO 09-23, close-to-close 0.00 / +0.000000 pct, verified via an independent second bars pull returning the same 707.28 with DISTINCT OHLV on both days, a real coincidence not a duplicated bar; on official closes core 70053.48 + cash 30000.00 = equity 100053.48, since inception +53.48 / +0.053475 pct; THE BROKER REPORTED -127.77 AND 100 PCT OF IT WAS ARTIFACT - equity-minus-last_equity, change_today and unrealized_intraday_pl all agreeing with each other and all wrong, none used, recorded as a CONFIRMATION NOT A SAVE; rebalance_delta read +12.78 on broker marks and -16.04 on the official close, SAME INSTANT SAME POSITION OPPOSITE SIGN; reconciliation clean; 5.1-5.4 never started for the thirty-third session; ClickUp 86bc76x35)

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
$100,053.48, using VOO's 09-24 official close of 707.28. On the broker-mark basis the same instant
reads 70.09 / 29.91. **Both are in band and neither implies an action.** The two bases are recorded
separately because they have been shown to disagree in **sign** on `rebalance_delta`. **State which
basis produced any figure you quote.**)*

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

**⚠ COLLAPSE, DO NOT APPEND — acted on thirty-five times.** The Week 3 review flagged the memory files
**against an instruction to read them in full**, calling the accumulation **actively harmful rather than
untidy**: this repo's only continuity mechanism is the next run *reading* these files, and padding them
with restatements raises the odds a genuinely live item gets skimmed. **Carry-forward is defined as
cleared once acted on.** This run **discharged two spent items** (the `lastday_price` prediction, which
resolved; and the truncated-series catch, which has been folded into the audit item) and updated the
rest in place. **Nothing live has been discarded** — the narrative history lives in `journal.md`,
`research_log.md` and `weekly_review.md`, which are the files built to hold it.

---

### Live — act on these

- **⚠⚠ NEWEST AND MOST DECISION-RELEVANT, 09-25: THE CANDIDATE OPEN ITEM (3) SAID WOULD NEVER ARRIVE
  ARRIVED, AND IT STILL PRODUCED NOTHING — BECAUSE THE DISCLOSED FIGURE WAS THE WRONG QUANTITY.**
  Anthropic committed **~$11.6B over seven years** to **Akamai** for cloud capacity (8-K + press
  release). Akamai's filing then did the thing this funnel has spent a month failing to find: it
  **named a US-listed supplier and allocated a specific dollar figure to it** — a Build Request
  authorizing **Jabil (JBL)** to procure **~$1.7 billion of memory components**. ⚠ **Read what the 8-K
  actually says: Akamai pays "all corresponding supplier invoice amounts," Jabil "will hold such
  components IN CONSIGNMENT AS BAILEE for the Company," and "will REPURCHASE such components from the
  Company AT COST as they are utilized."** ⚠ **That is Akamai's money, buying Akamai's property, with
  a disclosed statement of ZERO margin to Jabil. Jabil is the purchasing agent and the warehouse. The
  only figure that would satisfy part 2 — Jabil's assembly and services fee — IS DISCLOSED BY NOBODY.**
  ⚠⚠ **THIS IS A FIFTH FORM OF OPEN ITEM (3)'S BINDING CONSTRAINT, AND IT IS THE ONLY ONE NO WIDENING
  OF THE EVIDENCE BAR WOULD RELIEVE — widening the bar would have let it THROUGH.** The four known
  forms are all about information being *withheld*; this one is **fully disclosed and simply not
  revenue.** ⚠ **The standing warning — "a large, real, sourced, prominently-placed number is not a
  dollar path" — has never been tested this hard, and the number has never looked this much like an
  answer. Do not reach for this chain again.** Full working in **T-2026-09-25-01**.

- **⚠⚠ THE §4 PRICED-IN FILTER HAS A THIRD DEFECT SHAPE, AND THIS ONE FIRED ON A CANDIDATE THE AGENT
  HAD BEGUN TO LIKE.** JBL read **+4.97% over five sessions → `priced_in: true`.** ⚠ **The move is
  NOT the news: the five-session path was 299.52 → 303.64 → 308.86 → 308.71 → 310.67, a steady grind
  whose largest single day is +1.72%, and the BUILD-REQUEST DAY ITSELF (09-24) moved JBL +0.63%.**
  §4's text conditions on having moved 4% "**on this news**"; the window and the news are demonstrably
  disjoint. **Shape one: a DRAWDOWN misread as priced-in (nine instances). Shape two: a GENUINE news
  rise, the filter working (three instances, 09-24). Shape three, NEW: a genuine RISE UNRELATED TO THE
  NEWS that the window swept up.** ⚠ **It is also the first instance where the filter's verdict and
  the correct verdict AGREED FOR UNRELATED REASONS — the hardest kind to notice, and the reason the
  rejection is recorded at PART 2 and not at the filter.**
  ⚠⚠ **AND THE AGENT DID NOT ACT ON IT, DELIBERATELY. That is the part to carry forward.** The
  argument above is a correct reading of §4's wording and it is **still not this seat's to apply**.
  This was the exact setup the "do not lower the bar" rule guards against: **a candidate the agent
  liked, plus a plausible technical case that the filter misfired.** **Had part 2 not failed
  independently, the honest outcome would STILL have been REJECTED-on-priced-in with the defect
  logged — not a rescue.** ⚠ **Do not read this item as permission. Only a human may change §4 or
  `alpaca.py move`.**

- **⚠⚠ OPEN ITEM (2) HAS ITS WORST INSTANCE EVER, AND IT FAILS IN THE DIRECTION OF TAKING A TRADE.**
  **AKAM read `priced_in: false` at +3.19%** — and the daily closes, pulled this run, are
  **104.53 (09-18) → 117.435 (09-21) = +12.35% IN ONE SESSION**, then 118.33, 118.42, then
  **110.44 (09-24) = −6.74%.** ⚠ **A +12.35% event move and a −6.74% give-back fell inside the SAME
  five-session window and netted to a passing +3.19%.** Prior instances (QCOM +2.70% after a +8.7%
  intraday move; AVAV +1.20% after a +12.9% one-session round trip) were **intraday** round trips.
  ⚠ **This one spans MULTIPLE SESSIONS — the round trip no longer has to hide inside a single bar.**
  **AKAM was never at risk (first-order killed it), but a second-order beneficiary of the same chain
  would have been waved straight through.** ⚠ **This is also the sharpest evidence yet for open item
  (7): no 09:35 re-validation would have surfaced it either.**

- **⚠ STANDING RULE (iii) HAS A NEW COSTUME, AND THE TAPE IS WHAT CAUGHT IT: A FORMAL PRESS RELEASE
  RESTATING AN ALREADY-FILED 8-K.** Sources returned **conflicting disclosure dates** for the
  Akamai/Anthropic deal — one citation titled "Form 8-K AKAMAI TECHNOLOGIES INC **For: Sep 18**",
  another placing all three items (Anthropic, Lenovo, Jabil) in a **September 24** 8-K, a third citing
  project plans signed **Sept 18** under a **May 2026** master agreement. ⚠ **The conflict is NOT
  resolved and must not be asserted either way.** ⚠ **But the tape is primary evidence and it settles
  when the MARKET learned: +12.35% on Monday 09-21, and a 6.74% DECLINE on 09-24, the day of the press
  release and the Reuters coverage. A stock does not fall 6.74% on the day it learns of an $11.6B
  contract.** ⚠ **STANDING PRACTICE CONFIRMED AGAIN: ask a transaction WHEN IT HAPPENED before asking
  who it helps — and when the sources disagree on the date, THE PRICE SERIES IS THE CHEAPER WITNESS.**

- **⚠ THE `lastday_price` PREDICTION IS DISCHARGED — IT RESOLVED ON ITS PRE-REGISTERED THIRD BRANCH,
  AND NO FURTHER PREDICTION IS OWED.** The branches were named in advance: **707.60 ⇒ never rebuilt;
  707.28 ⇒ ambiguous, not to be logged as a clean rebuild; anything else ⇒ wrong in a FOURTH way.**
  ⚠ **It read 706.99** — off the 707.60 it had held through four consecutive reads on 09-24, landing
  **29c BELOW** the official 707.28 and **matching no recent official close** (712.69, 712.76, 701.85,
  700.97). **Third branch. The field is wrong in a fourth way, and the error now has BOTH SIGNS:
  +32c (09-24), −29c (09-25).** ⚠ **"It rebuilt" is not evidence it is right — on both mornings it
  rebuilt, it was wrong.** ⚠ **STOP PREDICTING THIS FIELD. The carry-forward's own rule — check a
  prediction is still DISCRIMINATING before repeating it — now cuts against another one: four
  falsified mechanisms and both signs observed means no further reading would change the conclusion.
  The field is unusable; that is the finding, and it is closed.** **The practice of writing concrete
  falsifiable predictions is NOT closed — it produced catches (3), (4), the degeneracy detection and
  this resolution. Keep it for live questions.**

- **⚠ HIGH-WATER MARKS: NOTHING TO BACKFILL, AND NOTHING WAS SKIPPED.** `positions.md` carries **zero
  satellite blocks**, so `highest_close` is **ABSENT — the third state, carrying no `(as of …)` date
  at all.** ⚠ **Do not read a missing stamp as a failed close run.** **§5.4 is NOT ARMED**; it arms on
  the first **satellite** fill, and the 09-03 core fill was not one. **Thirty-fourth consecutive
  session with §5.1–§5.4 never started — they remain UNTESTED CODE PATHS, and the running tally of
  "no exits" records the ABSENCE OF A SUBJECT.** ⚠ **The distinction is FREE today and stops being
  free the moment a satellite fill lands** — after that, a mark silently not written reads identically
  to a mark correctly unchanged, and **only the `(as of …)` date separates them. Compare the date;
  never infer from the field's emptiness.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE.** VOO **official** closes: **09-24 707.28**,
  **09-23 707.28** (identical to the cent — **verified**, distinct OHLV, a real coincidence),
  09-22 712.69, 09-21 712.76, 09-18 701.85. Core is **99.046311231 shares at 706.74**, cash
  **$30,000.00** flat. **AT THE 09-25 PRE-MARKET, ON THE OFFICIAL 09-24 CLOSE: equity $100,053.48,
  core $70,053.48 = 70.016%, cash 29.984%, since inception +0.053475% (+$53.48).** On broker marks the
  same instant: equity $100,299.16, core 70.09%, cash 29.91%. **Forty-third consecutive run inside
  69.59–70.22.** ⚠ **Both `rebalance_delta` bases are NEGATIVE today (−$89.75 broker, −$16.04
  official) — they AGREE in sign, unlike 09-24 where they disagreed. Intermittent is worse than
  consistently wrong: a run that checks one basis and finds agreement learns nothing.** **NO REBALANCE
  IS DUE** — §2 acts at the **65/75 band edge** and the core sits **~4.9 points** inside it.
  **Audit any superlative here before repeating it.**

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`,
  NEVER a `positions` field for a close or an execution reference. Close-to-close from
  `bars --adjustment all`, a fresh `quote` for execution.** Evidenced six ways, **and at its limit on
  09-24: the true close-to-close move was EXACTLY ZERO and the broker reported −$127.77, so 100% of
  the headline was artifact.** All three broker figures agreed with each other — ⚠ **which is exactly
  why NO CHECK INTERNAL TO THE BROKER'S OWN FIELDS CAN EVER SURFACE IT. Only an external close settles
  it.** ⚠ **09-24 is a CONFIRMATION, NOT A SAVE: nothing was spotted; a standing rule was followed on
  a day it happened to matter maximally. THE RULE'S VALUE IS INVERSELY PROPORTIONAL TO THE SIZE OF THE
  REAL MOVE, so it looks like pedantry on exactly the days it costs nothing to follow.** Prior:
  09-22 a **SIGN error** (+$7.82 reported on a −$6.93 day); 09-23 $6.93 of noise on a −$535.84 move,
  where the rule bought nothing.

- **⚠ §1 BENCHMARK — THE STANDING FINDING IS UNCHANGED, AND TODAY'S MACRO MAKES IT SHARPER.** This
  book's excess over VOO is **nothing but minus ~30% of VOO's return**, because the satellite sleeve
  has returned **0.0000%** over the account's entire history. ⚠ **Twelve-plus sessions: every
  positive-excess day has been a VOO DOWN day; NOT ONE HAS EVER COINCIDED WITH A RISING MARKET.**
  09-24 was the clean boundary case — VOO 0.000%, book 0.000%, excess exactly **0.000pp**.
  ⚠ **New context worth carrying: the 10-year reached ~5.22% (highest since 2007) and the 30-year
  ~5.48–5.50% (highest since 2004) on 09-25. That is a fact about what the BENCHMARK and the core
  sleeve are competing against, NOT a trade.** **A flat or quiet day is the easiest possible moment to
  stop asking §1's actual twelve-month question.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR
  JUDGMENT RATHER THAN CARE.** **RECOUNTED FROM SOURCE on 09-25** — `research_log.md` holds **74
  `T-` headings, one the template, so 73 REAL THESES, ZERO ACCEPTED EVER**, 27 this week (09-21: 3,
  09-22: 5, 09-23: 6, 09-24: 7, 09-25: 6). Set beside that: an empty satellite sleeve, **~30% idle
  cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker, and an account at **+0.053% since
  inception.** ⚠ **TODAY RAISES THE PRESSURE IN A NEW WAY AND THE DISTINCTION MATTERS: the funnel
  finally produced the well-sourced, named-supplier, allocated-figure candidate that a month of
  rejections implied was the missing ingredient — AND IT WAS STILL NOT A TRADE. That is evidence the
  bar is not what is binding, NOT evidence the bar should move.** §4's own position governs: a run
  that finds nothing is a successful run. **Naming the pull is the only defence against acting on
  it.** If the bar is to move, that is a `strategy.md` change and **only the human may make it. Do not
  resolve it from this seat.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY AND THAT IS ITS NORMAL STATE.** ⚠ **09-25's
  six rejections do NOT become a queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE.**
  **JBL** (part 2: $1.7B is capital paid in, on consignment, repurchased at cost; the assembly fee is
  undisclosed) · **AKAM** (first-order; and see the priced-in item) · **memory suppliers** (rule (v) —
  no supplier named in any disclosure; and <10% of revenue for any of them even if named; **Lenovo**
  is the one other named supplier and is **§3 outright**, HK-listed with only an OTC ADR) · **RDW**
  (the $980M is a **multiple-award CEILING across 15 vendors** with no Redwire allocation; also
  first-order; also ~$1–2B, below the §3 floor) · **FLNC** (no value or volume disclosed by any party;
  EVE Power is Shenzhen-listed) · **the rate/oil/PMI complex** (environment input, not a Company A).
  ⚠ **AND 09-24'S SEVEN WERE NOT REHABILITATED EITHER** — no `move`, `quote`, `bars` or `asset` call
  on ILMN, GRAL, BBY, PYPL, SHOP, SoftBank/OpenAI or ELMT. **A rejection is not a queue.**
  ⚠ **ELMT HAS NOW ENTERED THIS FUNNEL THREE TIMES IN THREE SESSIONS, AND THE THIRD TIME CARRIED A
  DISCLOSED PRICE ($124.75M for a 4.99% stake) — EXACTLY THE MATERIAL WHOSE ABSENCE KILLED THE FIRST
  TWO. IT WAS NOT SCREENED.** ⚠ **That refusal COST something and is graded as strong: "but now there
  is a number" is the purest form of the pull to re-open a §3 kill on evidence §3 does not weigh. A
  microcap with a Vietnam-listed counterparty is ineligible at every price and at every level of
  disclosure. Do not screen it again.** **Welspun** likewise resurfaced (~$412.5M pipe order, US
  subsidiary) — **not US-listed, §3, already disposed, and the buyer is unnamed besides.**
  ⚠ **One §3 question remains reached-but-undecided: Shopify is a Canadian issuer trading as common
  stock on a US exchange, which §3's "US-listed common stock" does not obviously settle. A future run
  reaching this with a LIVE candidate must put it to the human rather than decide it from this seat.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — FIVE CATCHES, AND THEY KEEP CHANGING SHAPE.**
  **(1)** A false superlative (*"positive for the first time in this account's history"*) survived
  three runs, caught **by accident** on 09-21. **(2)** A stale count (*"49 theses"*) caught
  **deliberately** on 09-22, running in the direction that **understates** the problem. **(3)** The
  09-22 claim that `lastday_price` rebuilds at a session boundary, falsified 09-23. **(4)** The 09-23
  claim that it does **not**, falsified 09-24. **(5)** A **TRUNCATED SERIES**, 09-24: the three-item
  post-bell `current_price` record had silently dropped its own largest member and would have produced
  a false superlative if repeated. ⚠ **CORRECTED SERIES, FIVE POST-BELL OBSERVATIONS: +$1.13 (09-18),
  −$0.22 (09-21), +$0.169 (09-22), +$0.02 (09-23), −$0.97 (09-24). Both signs, range 2c to $1.13, no
  predictable sign and no correctable offset. DO NOT QUOTE THE THREE-ITEM VERSION.**
  ⚠ **A superlative, count, mechanism OR SERIES inherited from a prior run is NOT a checked fact** —
  it is the cheapest claim to write and the most expensive to verify. **Assume the next one you are
  handed is wrong until you have pulled the source.** *(This run recounted the thesis total from
  source rather than incrementing: 74 headings, 73 real.)*

- **⚠ GNRC IS NOT YOURS TO LOOK AT — TWENTY-FOUR CONSECUTIVE REFUSALS, AND 09-25 IS A STRONG ONE.**
  ⚠ **Graded honestly: this run opened the data plane against a live funnel, issued FOUR `move` calls
  (JBL, AKAM, RDW, NOC) and four `bars` pulls, and HAD A RESEARCH STEP TO PUT A NUMBER IN.
  `--symbol GNRC` was one more invocation on a command line already typed four times over. Not
  made.** The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon
  announcement — first-order, outside §4 at any price** — and **open item (7) is resolved by a human
  editing §4 or `alpaca.py move`, not by a number this seat collects.** ⚠ **WHAT MATTERS IS NOT THE
  COUNT BUT WHETHER EACH REFUSAL COST ANYTHING, AND MANY DID NOT. Quoting the bare count overstates
  the evidence.** The strong instances are the pre-market runs of 09-23, 09-24 and 09-25 — all three
  opened the data plane against a live funnel **and** had somewhere to put a number. ⚠ **No new
  costume in five sessions; the list looks CONVERGING rather than growing, and a run that manufactures
  a new name for an old experience would be padding the log.** Costumes: diligence, curiosity,
  tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure,
  call-already-open, screen-already-running. **The pattern is the finding, not any instance. FREE IS
  NOT THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FIFTY-TWO RUNS.** §5 exempts core from all
  four sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the
  strategy exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids
  outright.** ⚠ **Grade these the way the GNRC count is graded — a refusal only costs something on a
  run that was HOLDING the number with somewhere to put it. 09-25 is a WEAK instance and is recorded
  as such: VOO closes were pulled for the plan's sleeve arithmetic, but routine 1 has no Step 2.** The
  sharpest instances remain the close runs of 09-22, 09-23 and **09-24 — the STRONGEST of all, since
  routine 4's entire declared purpose is writing closes into `highest_close` and it arrived holding a
  fresh official close with an empty field to put it in.** ⚠ **"Nothing to write" is the correct
  output of an empty Step 2, not an invitation to find a row to write it to.** **Measure the core from
  the 706.74 fill and from an official close, never from a `positions` field.** ⚠ **Noted honestly:
  this refusal is now close to automatic, and automatic is not the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN
  IS USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell
  sees it pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with
  **no bar for today**. ⚠ **09-22 read all three shapes in one day, and consecutive runs read
  IDENTICAL booleans meaning opposite things.** **`is_open: TRUE` is the one case where the boolean
  alone is sufficient, and it is safe to read it that way ONLY because TRUE has a single meaning.
  FALSE has three.** ⚠ **THE STRONGER DISCRIMINATOR IS TO CHECK THAT A DAILY BAR FOR TODAY EXISTS —
  run it before deciding a run is a holiday skip.**

- **⚠ SEVEN ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A
  NUMBER A RUN COLLECTS.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — **NINE instances** (newest CNC,
  09-23: −6.44% → `priced_in: true` on a **FALL**; before it ACN, 09-22, −4.58%), plus **THREE
  near-misses** where a candidate cleared only because its *fall* was fractionally too small (LMT
  −3.61%; **GM −3.95%**; **LH −3.83%**). **There is no price at which those rejections flip**; LITE
  puts **+10.58% vs VOO** on the bill. ⚠ **A pass on a fall is not evidence the filter worked, and
  neither is a FAIL on a fall** — recorded **deliberately as NOT the reason for the rejection**, so no
  run inherits "rejected because priced-in" as a fact. ⚠ **09-24 supplied the counterweight: THREE
  firings on genuine RISES (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%) where the filter did its designed
  job. The defect is SIGN-BLINDNESS, not the threshold.** ⚠ **09-25 ADDS A THIRD SHAPE: JBL, a genuine
  RISE that was UNRELATED TO THE NEWS (+4.97% of grind; news day +0.63%). §4's text says "on this
  news"; the mechanized check cannot see causation.**
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM (09-09,
  +2.70% after a +8.7% intraday move), AVAV (09-11, +1.20% after a +12.9% one-session round trip),
  ⚠ **and now AKAM (09-25, +3.19% after a +12.35% single-session jump and a −6.74% give-back — the
  first MULTI-SESSION round trip, and the worst instance recorded).** Same root cause as (1), opposite
  direction. **The fix for (1), (2) and the new shape is a human editing §4 or `alpaca.py move`** —
  and the specific suggestion on the record is to make it **read SIGN and causation, not loosen or
  remove the threshold.**
  **(3)** The satellite sleeve is **structurally undeployed — 73 theses, zero positions, ever.**
  ⚠ **RECOUNTED FROM SOURCE on 09-25. Recount before quoting; do not copy this line forward.** A 70/30
  cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits the cash
  and §4 says most runs end in no trade — both rules were followed, and the agent must NOT respond by
  lowering the §4 bar.** **The binding constraint now has FIVE known forms:** the source withholds the
  counterparty's number; **or** the counterparty discloses **roadmap instead of segment revenue**;
  **or** the named beneficiary is **vertically integrated** with no external supplier to find; **or**
  **both parties expressly refuse to disclose as a commercial choice** (09-21 GM); ⚠ **or — NEW,
  09-25 — THE FIGURE IS FULLY DISCLOSED AND IS THE WRONG QUANTITY (JBL: capital paid in, held on
  consignment, repurchased at cost).** ⚠ **Only the first two forms are addressable by widening the
  evidence bar. Forms three, four and five are not addressable at all, and form five would be made
  WORSE by widening it.** ⚠ **ELMT is the standing proof that evidence is not the constraint: it
  withheld NOTHING (09-25 even disclosed the price) and still produced no trade, because the
  obstruction was STRUCTURAL (§3).**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the
  prior close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11: measured from
  the fill, tracking error 0.0000%. Keep measuring it from the fill.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it
  never had a stable size and never will. ⚠ **It is not a P&L problem — it is a PRICE-SOURCE problem
  that contaminates every derived figure.** It has flipped the sign of a §2 quantity (`rebalance_delta`
  +$12.78 broker vs −$16.04 official on 09-24), ⚠ **and on 09-25 the two bases AGREED in sign, which
  establishes the defect is INTERMITTENT — a run that checks one basis and finds agreement learns
  nothing.** **Whether the tooling should read closes from `bars` by default is a human's call, and
  this is the strongest evidence yet that it should.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it
  passed all five checks on 09-11 while `clock` returned 500 and `quote`/`bars` returned 504, **and on
  09-24 while a `perplexity.py` QUERY returned 500 — the first instance on the RESEARCH plane, which
  is the one that matters most here.** ⚠ **09-25 update: four Perplexity calls, all exit 0. The 09-24
  transient did NOT recur — single occurrence, still no alert.** **Until a human changes it: probe by
  hand; never infer data-plane health from a green selftest, and CHECK EXIT CODES — never infer thin
  news from empty results.**
  **(7)** **`alpaca.py move` cannot see an after-hours event**, and neither can the 09:35
  re-validation that exists to catch exactly this. ⚠ **Unlike (1) and (2), this fails in the direction
  of TAKING a trade rather than skipping one**, which is why it is listed last and should be read
  first. ⚠ **09-25 supplies the sharpest evidence yet, and it generalises the item: AKAM's entire
  +12.35% event move was hidden from the filter by a later give-back inside the same window. The
  blindness is not only to AFTER-HOURS events — it is to any event move the window later cancels, and
  no 09:35 re-validation would surface either.** **It has cost zero only because no plan has yet
  carried a BUY intent — an absence of exposure, not a mitigation.**
  Prior context in ClickUp `86bbv75bz`; week-prior in `86bbzgbg3`. **09-24 daily summary: `86bc76x35`.**

- **⚠ WEEK 3 REVIEW (2026-09-18): THE §1 ANSWER IS NO, AND SHORT GREEN WINDOWS MUST NOT BE READ AS
  YES.** The satellite sleeve returned **0.0000%** — zero positions in the account's entire history —
  so its dollar-weighted excess over VOO is exactly **minus VOO's total return** over whatever window
  is chosen: **+0.095pp on the week, +0.430pp since inception, +0.509pp over 1M, −2.291pp over 3M, and
  −16.552pp over the rolling 12 months §1 actually names.** The structural cost is **~4.97pp of
  account return per rolling 12 months.** Full working in `weekly_review.md`. **Reject board: 40
  measurements, 13 beat VOO, 27 lagged, mean excess −1.57%.** ⚠ **It is a tally, not a result — do not
  quote it as one.** **HPE remains the largest single opportunity cost the log has produced
  (+19.87% vs VOO).**
  ⚠ **FILE SIZE — SEVENTH CONSECUTIVE FLAG, AND THE DEADLINE IS NOW.** `research_log.md` grew to
  **~333KB** on 09-25 (from ~311KB) against a total memory footprint every run is instructed to read
  **in full**. **The monthly archive rollover is due 2026-10-02, and TODAY'S review (09-25) is the
  LAST ONE BEFORE IT.** ⚠ **A human may want to move it forward; alternatively the 09-25 review may
  choose to run it early.** **Mitigations so far are collapses of `positions.md` (36K→20K, then
  27K→19K). Those are mitigations, not a fix.**

- **⚠ A `#` IN A FENCED-BLOCK VALUE SILENTLY TRUNCATES IT.** `_parse_kv` in `scripts/common.py` does
  `line.split("#", 1)[0]`, so **everything after the first `#` in a `key: value` line is discarded by
  the parser.** The 09-24 close run did this to itself and caught it before commit. ⚠ **STANDING
  CONSEQUENCE: never put a `#` in a fenced-block value, and VALIDATE `state.md` WITH
  `common.read_state()` AFTER REWRITING IT — writing the block and parsing the block are not the same
  check.** *(Done this run: block re-parsed and all twelve keys verified present and untruncated.)*

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** compared to **consensus** rather than to any prior
company figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations**
(Centene, Southwest, General Mills), **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence,
Alcoa/South32, Nocera/E-PRO), **a genuine transaction whose DELIVERY MILESTONE is recycled as the
news** (09-21 GM/Lockheed), **a PRE-IPO CONTRACT BOOK** (Nscale's $103B), and ⚠ **NEW, 09-25: A
FORMAL PRESS RELEASE RESTATING AN ALREADY-FILED 8-K (Akamai/Anthropic — the tape moved +12.35% on
09-21 and FELL 6.74% on the 09-24 "announcement" day).** ⚠ **STANDING PRACTICE: ask a transaction
WHEN IT HAPPENED before asking who it helps — and WHEN THE SOURCES DISAGREE ON THE DATE, THE PRICE
SERIES IS THE CHEAPER WITNESS.** One screen settles it, and it is the cheaper of the two kills.
*(09-17 Amazon/Generac was the first clean rule (iii) PASS; 09-24's Elmet/Masan the second.)*
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — resolved 09-11 on a number).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share,"
"the only company that makes X" are facts about an **industry**, not a **transaction** — plus the
**CEILING sub-shape**. Costumes: a **table** (DoD daily contracts digest), a **consortium awardee**
(Abrams), a bare sentence, and ⚠ **09-25's TWO NEW ONES: a MULTIPLE-AWARD CEILING across fifteen
vendors read as one company's revenue (RDW, "$980M"), and an UNNAMED SUPPLY BASE made to look
nameable by an exact figure and a named component category ($1.7B of "memory components," with no
manufacturer disclosed anywhere).** ⚠ **The second is more dangerous than 09-24's SoftBank/OpenAI: the
blank LOOKS fillable because the suppliers are countable on one hand. The source left the blank;
filling it in is not research.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.*
Long-dated energy offtake is **a standing feature of this funnel, not a visitor** —
Sempra/Petrobras, Venture Global/China Gas, Amazon/Generac, Centrus/Antares, Elmet/Tungsten West,
NeoVolta/SK On. ⚠ **09-24 added the REGULATORY version: a non-binding advisory vote → an undated FDA
decision → reimbursement → commercial ramp (ILMN) is the same shape wearing a lab coat.**
**Part 3 kills these in ONE step.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part
2.** Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; Brookfield/Bloom's **$25B** is
a **FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**; SoftBank's **$11.1B** is **capital paid IN to a
private recipient**; Royal Caribbean's **~$3B** for Sandals is **capital paid OUT by the buyable leg**;
09-24 BBY's only disclosed economics was **Meta taking "a small fee" — a COST at the candidate,
described in language that reads like a partnership benefit**; ⚠ **09-25 FMC/Tessenderlo's $403M is a
SECONDARY-MARKET SHARE PURCHASE — money to selling shareholders, never to the company.**
⚠⚠ **AND THE DEFINITIVE INSTANCE, 09-25 JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN
8-K — AND IT IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT
COST. A disclosed statement of ZERO MARGIN, reading like the best dollar path the funnel has ever
produced.** ⚠ **A large, real, sourced, prominently-placed number is not a dollar path. THIS IS THE
WORKED EXAMPLE TO REACH FOR FIRST.** T-2026-09-18-04 (BLK) remains the other: **part 1 passed cleanly
and it died on the absent segment figure, NOT on size.**

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
ACA enrollment halt). ⚠ **This is the FOMC object — an environment input — but in a far more
persuasive costume: a policy action is SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN AFFECTED INDUSTRY,
and MOVES THE TAPE ON THE DAY.** It nonetheless has **ONE party.** ⚠ **A long-only book cannot trade
money being WITHDRAWN from a sector unless some NAMED party receives it — and nobody does.**
⚠ **09-25 SUPPLIES THE FULL-MARKET-SCALE VERSION AND IT IS THE MOST TEMPTING YET: the 10-year at
~5.22% (highest since 2007), the 30-year at ~5.48–5.50% (highest since 2004), Brent near $106, PMIs at
52- and 59-month highs, swaps pricing three more hikes. SCALE MAKES IT MORE CONVINCING, NOT LESS. Every
"who wins from higher rates / higher oil" answer needs an "and also".** ⚠ **09-24's counter-case still
stands and must not be over-applied against: an FDA advisory vote (ILMN/GRAIL) ENABLES a named
company's product and that company has a named supplier — a real two-party chain. Do not over-apply
this rule to approvals.**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is
**exits-only by construction** and may not open a position under **any** circumstance. Routine 2
executes **only what `plan_today.md` already contains** — a position opened at 09:35 without a plan
entry routes **around** the discipline rather than satisfying it. Routine 4 **RECORDS AND JOURNALS; IT
DOES NOT TRADE.** ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
opportunity any of those seats may act on.** New positions route through pre-market research **plus**
the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the
outcome.** The gate has been exercised **TWENTY-SEVEN times and has never fired**, and its alert path
**remains untested code.** ⚠ **Twenty-seven quiet opens are NOT evidence it works. The first morning
it fires will by construction be a morning when the pre-market run failed — i.e. exactly the morning
with no fresh notes to lean on. Read routine 2's Step 2 then; do not recall it.**
⚠ **09-24's open is the CLEANEST DEMONSTRATION: the plan was FRESH and EMPTY, and the run it produced
is BYTE-FOR-BYTE the run a stale plan would have produced. Only `plan_date` told them apart.**
**Today's plan (09-25) is fresh and empty in exactly the same way.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a
broker mark on one leg against an official close on the other. **Both legs from the same source, and
for returns that source is `bars --adjustment all`.** ⚠ **And state WHICH basis produced any figure
you quote.**

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
share purchase**, money to selling shareholders) · **LLY / InnoCare** (no value disclosed; LLY
first-order; InnoCare HK-listed) · **NOC $123.8M, RTX $50.1M, Stark $114.0M, Southern $22.0M, RGAS
$23.6M** (DoD digest, rule (v); all ≪10% of revenue; Stark not separately US-listed) · **Blue Cloud
Softech / IBM** (Indian-listed; $15.5M is nothing to IBM) · **FingerMotion** (offtakers unnamed,
contract expressly not yet announced) · **Everforth, Endovia, Algorhythm** (private or microcap) ·
**Amazon's $100M Greenwood plant** (immaterial; no counterparty) · **Welspun** (§3, buyer unnamed,
second appearance).

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
  state in this account.**
- **The core is deliberately NOT tracked in `positions.md`.** §5 exempts it, so it has no thesis
  state, no timing window and no `highest_close`. ⚠ **Every reconciliation compares SATELLITE blocks
  to SATELLITE Alpaca positions** — a run that compares the raw ledger to the raw broker will read a
  correct ledger as broken.
- **Counters as of 2026-09-25 PRE-MARKET, RE-VERIFIED FROM SOURCE (74 `T-` headings less the
  template): 73 theses since inception, 0 accepted, 73 rejected, 27 this week (09-21: 3, 09-22: 5,
  09-23: 6, 09-24: 7, 09-25: 6); 0 satellite positions ever opened; 0 exits ever; `alerts.md` empty —
  zero open, zero SYSTEMIC.** ⚠ **Recount from `research_log.md` before quoting this anywhere
  human-facing — a run that ADDS theses and a run that COPIES this line forward are different runs.**
- **`week_of` 2026-09-21, `new_positions_this_week` 0 of 3.** Next boundary **Monday 2026-09-28**.
  The reset does not depend on the Friday review having run. ⚠ **The two counters are independent: 27
  theses this week and 0 positions this week are both correct — §6's cap counts POSITIONS OPENED.**
- **TODAY, Friday 2026-09-25, is a weekly-review day** (routine 5), and it is the **LAST REVIEW BEFORE
  THE 2026-10-02 MONTHLY ARCHIVE ROLLOVER.** `research_log.md` is **~333KB**.
