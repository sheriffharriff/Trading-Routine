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
last_run: 2026-09-29 09:35 ET 2-market-open-execution (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99694.43 at pre-flight; ZERO ORDERS PLACED AND ZERO WERE DUE; clock at 09:35:56 is_open TRUE which is the one boolean reading that is sufficient alone, market genuinely open and the run genuinely in its window; THE STALENESS GATE DID NOT FIRE AND THIS IS EXERCISE 29 NOT A PASS - plan_date read 2026-09-29 against today's ET date 2026-09-29 so the plan was FRESH, and a FRESH EMPTY plan and a STALE plan produce a byte-for-byte identical zero-order run so the outcome proves nothing, read plan_date never the order count, THE ALERT PATH REMAINS UNTESTED CODE FOR THE 29TH TIME; THE PLAN CARRIED ZERO BUY AND ZERO SELL INTENTS so step 4 step 5 and step 6 all had NO OPERAND, ZERO move calls were due and ZERO were made which is an ABSENT re-validation NOT a skipped one, and ZERO orders of any kind were submitted; RECONCILIATION CLEAN - positions returns ONE row core VOO 99.046311231 shares avg_entry 706.74 cost_basis 69999.99 unchanged since the 09-03 fill, and positions.md carries ZERO satellite blocks (its only T-dash heading is the TEMPLATE) against ZERO satellite Alpaca rows, they AGREE; BOOTSTRAP NOT RUN - core_established was already true so step 3 was permanently closed and was not re-entered; HOUSEKEEPING all three checks run none fired - week anchor Monday 2026-09-28 MATCHES week_of so NO ROLLOVER was due, breaker INACTIVE with halt_triggered_at none and consecutive_closed_losses 0 so new positions were PERMITTED and nothing blocked them, weekly cap UNUSED at 0 of 3, core 69.91 pct broker / 69.9064 pct official BOTH INSIDE the 65-75 band so NO REBALANCE was due under step 7; THE LAST COMPLETED CLOSE WAS PULLED FRESH NOT INHERITED - bars --adjustment all gives 09-28 at 703.60 and the 09-29 bar EXISTS AND IS PARTIAL (n 293, v 11042) with is_open TRUE, which is the clock discriminating correctly where n and v could not; A THIRD EQUITY NUMBER APPEARED INSIDE THIS ONE RUN SECONDS APART - sleeves read 99687.00 and account read 99685.02 and the pre-flight read 99694.43, three live midpoints not three errors, open item (5) observed INTRA-RUN for the first time; CASH READS EXACTLY 30000.00 - the VOO dividend is STILL UNPAID on day 2 of the 8-day window and non-arrival remains EXPECTED NOT EVIDENCE; AND THE 09-28 GAP DID NOT CONTINUE - git log shows 73aab79 the 09-29 premarket commit dated TODAY, so yesterday stands as a ONE-DAY three-routine gap and NOT a two-day pattern, checked from source as the plan required; prior last_run preserved below)

prior_run: 2026-09-29 08:26 ET 1-premarket-research (ZERO ORDERS - routine 1 THINKS, IT DOES NOT TRADE; RESEARCH RAN IN FULL, four Perplexity scans all exit 0, SIX candidates reached a thesis entry and ALL SIX WERE REJECTED, theses now 79 real RECOUNTED FROM SOURCE, 0 ACCEPTED EVER, 6 this week; THE FINDING WAS THAT THE SOURCE VOLUNTEERED THE ABSENCE - the guidance and capacity scan returned five US-listed names and printed for FOUR OF THE FIVE the phrase no other company's revenue or costs are identified as directly affected, the funnel answering section 4's question IN THE NEGATIVE, and a run that then produces a Company B has supplied it from its own priors; the sharpest PAIR is one entry apart and from the SAME query - IOVA is the cleanest rule (iii) PASS in weeks and died one step later at rule (vii) vertical integration, while AIR is a rule (iii) FAILURE because the source carried NO prior AAR guidance at all; the 20.7B AMRAAM award names four CONTRACT LINE CATEGORIES and not one subcontractor, rule (v)'s largest instance yet; wrote plan_today.md for 2026-09-29 with ZERO intents)


week_of: 2026-09-28
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.91
satellite_pct: 0.0
cash_pct: 30.09
open_thesis_ids: none
```

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on forty times.** This repo's only continuity mechanism is the next
run *reading* these files, and padding them with restatements raises the odds a genuinely live item gets
skimmed. **Carry-forward is defined as cleared once acted on.** ⚠ **This run added ONE new item (the
funnel's negative answer being volunteered by the source) and COLLAPSED the ex-dividend write-up, whose
operative rules now live in `positions.md`'s header and `plan_today.md`'s tape section where they will be
read at the moment they bind.** ⚠ **A correction replaces the claim it corrects — it does not sit beside
it.** **Nothing live has been discarded.**

---

### Live — act on these

- **⚠⚠ THE VOO DIVIDEND IS STILL UNPAID. DAY 2 OF 8. CHECK `cash` EVERY RUN UNTIL IT RESOLVES.**
  `cash` read **exactly $30,000.00** at **09:35 on 09-29** — checked a second time today, from `sleeves`
  and from `account`, both flat, unchanged from the 09-28 close. ⚠ **NON-ARRIVAL ON EX-DATE+1 IS EXPECTED,
  NOT EVIDENCE — settlement runs on the PAY date, which is not the ex-date. Do not read $30,000.00 as the
  test resolving in either direction.** ⚠ **Two checks on the same day are ONE observation of an unpaid
  dividend, not two — do not let the repetition read as accumulating evidence.**
  ⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE AND STILL RUNNING: `cash` should rise to about
  $30,180.45. IF IT HAS NOT BY 2026-10-07, the paper account does not model dividends at all — in which
  case the book structurally under-earns its own benchmark by VOO's entire ~1.0% annual yield and §1's
  "beat the S&P TOTAL RETURN" is unwinnable BY CONSTRUCTION rather than by strategy.** ⚠ **That is a
  finding for the human, not something to fix from this seat.** The implied credit of **$180.26–$180.64**
  is an **INFERENCE** — Alpaca does not publish the figure — and must stay labelled as one.

- **⚠⚠ EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
  VOO went ex-dividend 09-28; `bars --adjustment all` rescaled every prior close by **0.997432**;
  `--adjustment raw` and `--adjustment split` return the original series to the cent. **Both series are
  correct; they are different bases.** **Raw:** 09-28 **703.60**, 09-25 710.705, 09-24 707.28, 09-23
  707.28, 09-22 712.69, 09-21 712.76, 09-18 701.85. **`--adjustment all`:** 703.60 / 708.88 / 705.47 /
  705.47 / 710.86 / 710.93 / 700.05. ⚠ **The 09-03 core fill at 706.74 is a RAW print; measuring it
  against an `--adjustment all` close MIXES BASES.**
  ⚠ **`quote`'s `prevDailyBar` and `bars --adjustment all` DISAGREE ON THE SAME SESSION — a SECOND,
  INDEPENDENT price-source axis, and the standing "both legs from the same source" rule does NOT catch
  it, because it distinguished broker fields from bar fields, never `quote` from `bars`.**
  ⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**
  ⚠ **§5.4 IS THE REAL CASUALTY AND IT FAILS TOWARD SELLING** — a `highest_close` stamped before an
  ex-date and compared against a post-ex adjusted close manufactures a **phantom drawdown equal to the
  dividend** (0.257% on 09-28). **THE FIX IS WRITTEN INTO `positions.md`'s HEADER, where it will be read
  before the next mark is stamped: same basis, same call, re-pull the whole window and take the max from
  that one pull.** ⚠ **The empty sleeve is the only reason this has cost nothing.** **`voo_close_at_entry`
  is a LABEL, not a baseline — re-derive the benchmark leg from a fresh pull at review time.**

- **⚠⚠ THREE OF FOUR ROUTINES LEFT NO COMMITTED OUTPUT ON 2026-09-28. VERIFIED FROM INSIDE THIS RUN, NOT
  INHERITED.** `git log` shows the newest pre-today commit is **11804ab, the 09-28 close journal**, with
  **no premarket, open or midday commit dated 2026-09-28**; `plan_today.md` arrived carrying
  **`plan_date: 2026-09-25`**. ⚠ **The repo's own definition of a run having happened is a commit —
  "push, or it never happened."** ⚠ **`control.md` warns against diagnosing schedule faults from run
  TIMESTAMPS; this is the ABSENCE of committed output, a different claim. THE CAUSE IS NOT VISIBLE FROM
  INSIDE A RUN AND IS NOT ASSERTED. IT IS A QUESTION FOR THE HUMAN.**
  ⚠⚠ **THE COST HAS BEEN ZERO TWICE OVER AND THAT IS LUCK, NOT DESIGN** — an empty sleeve gave routine 3
  nothing to manage, an empty plan gave routine 2 nothing to execute. ⚠ **On a day with an open satellite
  position, a missing routine 3 is an UNMANAGED §5 BOOK for a full session.**
  ⚠⚠ **ANSWERED 09-29 09:35, FROM SOURCE: IT IS NOT A TWO-DAY PATTERN.** `git log` shows **73aab79, the
  09-29 pre-market commit, dated TODAY**, and this market-open run committed as well. **Routines 1 and 2
  both produced committed output on 09-29.** ⚠ **So 09-28 stands as a ONE-DAY, THREE-ROUTINE gap — still
  a real gap and still a question for the human, but NOT an ongoing failure, and it must not be reported
  as one.** ⚠ **The remaining test is routines 3 and 4 today; a run that checks only the morning has
  checked half the day.**
  ⚠ **AND THE GAP DESTROYED A PIECE OF EVIDENCE: 09-28 was the FIRST morning with a GENUINELY STALE
  `plan_today.md` — word for word the setup the staleness gate had been waiting for — and the gate was
  not reached, because the run containing it did not execute. THE GATE REMAINS UNTESTED CODE AND THE
  COUNT IS 28, NOT 29.** **This run overwrote `plan_today.md` normally, as routine 4 said it would.**

- **⚠⚠ NEW ON 09-29 — THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE, OUT LOUD, AND THAT IS A RESULT
  RATHER THAN AN EMPTY SEARCH.** The guidance-and-capacity scan returned five US-listed names and printed,
  for **four of the five**, the phrase *"No other company's revenue or costs are identified as directly
  affected in the available source material."* ⚠ **That is not an under-searched funnel. It is the source
  volunteering the absence of a Company B.** ⚠⚠ **A run that then produces one has supplied it from its
  own priors, which is verbatim the failure §4's honest-broker paragraph describes — "you will always be
  able to construct a plausible-sounding connection."** ⚠ **Recognise this shape on sight: when the source
  says no counterparty is identified, the correct next action is to WRITE THAT DOWN, not to go looking for
  one in a differently-worded query.** *(The AMRAAM query on 09-29 was deliberately written to make the
  absence explicit rather than to find a name, and it returned a list of the companies the evidence does
  NOT support naming. That is the right shape for this query.)*

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR JUDGMENT
  RATHER THAN CARE. 79 REAL THESES, ZERO ACCEPTED EVER** (80 `### T-` headings less the template,
  **recounted from source** on 09-29; 73 + this run's 6). **6 this week, all rejected.** Set beside that:
  an empty satellite sleeve, **~30% idle cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker,
  and an account at **−0.17% since inception on broker marks** — ⚠ **negative, where every version of this
  item before 09-28 said positive.** ⚠⚠ **A LOSING ACCOUNT RAISES THE PULL IN A NEW WAY AND THE
  DISTINCTION STILL HOLDS: the book is down because it holds 70% of a market that fell, and it BEAT that
  market on the day it fell, by exactly the cash weight. "Deploy something" is not what these numbers
  argue for; they argue that the sleeve has no effect in EITHER direction.** ⚠ **09-25 remains the
  sharpest evidence: the funnel finally produced the well-sourced, named-supplier, allocated-figure
  candidate that a month of rejections implied was the missing ingredient — AND IT WAS STILL NOT A TRADE.
  That is evidence the bar is not what is binding, NOT evidence the bar should move.** §4's own position
  governs: a run that finds nothing is a successful run. **Naming the pull is the only defence against
  acting on it.** If the bar is to move, that is a `strategy.md` change and **only the human may make it.**
  ⚠ **WHERE THIS WEEK'S 6 DIED: part 1 = 3 (T-01 AMRAAM, T-02 IOVA, T-06 AIR), premise/no-Company-A = 1
  (T-05 rates), part 2 = 1 decisive (T-04 CRK, part 1 also), part 3 = 0 decisive (T-03 SMMT died three
  times over: premise, part 2 and part 3).** ⚠ **Part 1 is dominant again after Week 4 saw part 2 take
  over — a ONE-DAY sample and NOT a trend. Do not report it as one.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY.** ⚠ **09-29's six rejections do NOT become a
  queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT PRICE.** **AMRAAM suppliers** (rule (v) — no
  subcontractor named, no dollars allocated; and RTX is first-order) · **IOVA** (rule (vii) — vertically
  integrated, no external supplier to find) · **SMMT/AZN** (first-order; $2.0B is capital paid IN for
  convertible preferred; clinical timeline beyond two quarters) · **CRK/SOCAR** (the second-order sentence
  needs an "and also"; $1.65B is capital paid in by a non-US-listed state oil company) · **the rate /
  Fed-repricing complex** (environment input, ONE party) · **AIR/MRO Holdings** (the only Company B is
  private; AAR's own prior guidance absent from the sources).
  ⚠ **AND 09-25'S SIX WERE NOT REHABILITATED EITHER** — no `move`, `quote`, `bars` or `asset` call was
  made on JBL, AKAM, RDW, FLNC, Lenovo or any memory supplier. **A rejection is not a queue.**
  ⚠ **One §3 question remains reached-but-undecided: Shopify is a Canadian issuer trading as common stock
  on a US exchange, which §3's "US-listed common stock" does not obviously settle. A future run reaching
  this with a LIVE candidate must put it to the human rather than decide it from this seat.**

- **⚠⚠ THE MOST DECISION-RELEVANT REJECTION ON THE BOARD REMAINS JBL (09-25).** Anthropic committed
  **~$11.6B over seven years** to **Akamai**; Akamai's 8-K then did what open item (3) says never happens —
  **named a US-listed supplier and allocated a specific dollar figure to it**, a Build Request authorizing
  **Jabil (JBL)** to procure **~$1.7 billion of memory components**. ⚠ **And it is not revenue: Akamai pays
  "all corresponding supplier invoice amounts," Jabil holds the components "IN CONSIGNMENT AS BAILEE," and
  Akamai "will REPURCHASE such components from the Company AT COST."** A disclosed statement of **zero
  margin**. The only figure that would satisfy part 2 — Jabil's assembly fee — **is disclosed by nobody.**
  ⚠⚠ **A FIFTH form of open item (3)'s binding constraint and the ONLY one no widening of the evidence bar
  would relieve — widening it would have let this THROUGH.** ⚠ **Do not reach for this chain again, and not
  at a lower price — the price was never the problem.** Full working in **T-2026-09-25-01**.
  ⚠ **09-29 ADDS A SIXTH FORM, AND IT IS THE ONE WIDENING THE BAR HELPS LEAST: THERE IS NO COUNTERPARTY AT
  ALL.** IOVA raised guidance on its own product, made in its own facility, and **names no external
  supplier** — T-2026-09-29-02. **No withheld figure exists to widen a bar toward.**

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES.** **Shape one: a DRAWDOWN misread as priced-in**
  (nine instances, newest CNC −6.44% → `true`), plus three near-misses that cleared only because the *fall*
  was fractionally too small (LMT −3.61%, GM −3.95%, LH −3.83%). **Shape two: the filter working** on
  genuine news rises (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%). **Shape three (09-25, JBL): a genuine RISE
  UNRELATED TO THE NEWS that the window swept up** — +4.97% over five sessions on a grind whose largest day
  was **+1.72%** and whose **news day moved JBL +0.63%.** §4 conditions on having moved 4% "**on this
  news**"; the mechanized check cannot see causation. ⚠ **The defect is SIGN- AND CAUSATION-BLINDNESS, not
  the threshold.** ⚠⚠ **AND THE AGENT DID NOT ACT ON IT, DELIBERATELY — that is the part to carry forward.**
  ⚠ **Only a human may change §4 or `alpaca.py move`.**
  **⚠ AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read `priced_in: false` at +3.19%**
  while its closes ran **104.53 → 117.435 = +12.35% IN ONE SESSION**, then 118.33, 118.42, then **110.44 =
  −6.74%** — a +12.35% event move and a −6.74% give-back inside the SAME five-session window, netting to a
  passing +3.19%. ⚠ **Prior instances (QCOM, AVAV) were INTRADAY round trips; this one spans MULTIPLE
  SESSIONS, and no 09:35 re-validation would have surfaced it either.**
  ⚠ **09-29 MADE ZERO `move` CALLS. That is an ABSENT check, not a skipped one — every candidate died
  before an eligible ticker was reached. "The filter did not fire" and "the filter had nothing to fire on"
  look identical in a run summary and are not the same thing.**

- **⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.**
  Two routines read `is_open: true` and can pull a live partial bar: **routine 2 at 09:35 and routine 3 at
  12:30.** ⚠ **The midday case is the dangerous one: at 12:41 on 09-25 the partial read c 710.555, n 1,731,
  v 69,713 — half a session of real volume, a plausible OHLC and a close inside the range. It does NOT look
  like a stub.** ⚠⚠ **YOU CANNOT JUDGE A BAR'S COMPLETENESS FROM `v` AGAINST A PRIOR-DAY MEAN.**
  ⚠ **RE-EXERCISED AND HELD ON 09-28 IN THE OPPOSITE DIRECTION:** that session printed **v 62,354 against
  Friday's 164,725 — 38%** — and it is a **COMPLETE** session. `feed=iex` returns **one venue's slice** of
  consolidated volume. ⚠ **LOW VOLUME IS NOT EVIDENCE OF A PARTIAL BAR ANY MORE THAN HIGH VOLUME IS
  EVIDENCE OF A COMPLETE ONE. `n` and `v` are a SMELL TEST; THE RELIABLE DISCRIMINATOR IS THE CLOCK.**
  ⚠ **09-29 09:35 IS THE CLEANEST INSTANCE YET AND IT WENT THE EASY WAY: the 09-29 bar existed five
  minutes into the session reading c 703.70, n 293, v 11,042 — this one DOES look like a stub, and that is
  precisely why it teaches nothing. The 12:30 seat is where the same bar stops looking like one.**
  ⚠ **And the trap is usually MILD, which is the uncomfortable half** — the 09-25 midday partial was
  **fifteen cents** off the official close. **A loud warning whose observed instances are all mild teaches a
  future run that the shortcut is safe. It is not safe on a day with a 2% afternoon reversal.**

- **⚠ HIGH-WATER MARKS: NOTHING TO BACKFILL AND NOTHING WAS SKIPPED.** `positions.md` carries **zero
  satellite blocks**, so `highest_close` is **ABSENT — the third state, carrying no `(as of …)` date at
  all.** ⚠ **Do not read a missing stamp as a failed close run: there is no field, so there was nothing to
  write. DO NOT BACKFILL ANYTHING.** **§5.4 is NOT ARMED**; it arms on the first **satellite** fill, and the
  09-03 core fill was not one. §5.3's distance is **UNDEFINED, not large.** ⚠ **The distinction is FREE
  today and stops being free the moment a satellite fill lands** — after that, a mark silently not written
  reads identically to a mark correctly unchanged, and **only the `(as of …)` date separates them. Compare
  the date; never infer from the field's emptiness.** ⚠ **AND WHEN IT ARMS, NO BACKFILL MAY TAKE ITS MAX
  FROM A BAR DATED TODAY WHILE THE MARKET IS OPEN, NOR FROM A DIFFERENT ADJUSTMENT BASIS THAN THE ONE IT IS
  COMPARED AGAINST.** **§5.1–§5.4 have never had an operand in this account's entire history.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — AND NOTE THE BASIS ON EVERY ONE.** Core is
  **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat. **ON THE 09-28 CLOSE, PRICE
  BASIS: equity $99,688.98, core $69,688.98 = 69.9064%, cash 30.0936%, day −$703.72 / −0.7010%, since
  inception −$311.02 / −0.3110%. TOTAL-RETURN BASIS carrying the ~$180.45 receivable: ~$99,869.4, day
  −0.5212%, since inception −0.1306%.** **At 08:26 on 09-29 on broker pre-market marks: equity
  $99,827.65, core $69,827.65 = 69.95%, cash 30.05%, `unrealized_pl` −$172.34 / −0.246%.**
  ⚠ **That is a PRE-MARKET MIDPOINT, not a close and not an execution reference.**
  **AT 09:35 ON 09-29, MARKET OPEN, BROKER MARKS: `sleeves` equity $99,687.00, core $69,687.00 = 69.91%,
  cash 30.09%; core `unrealized_pl` −$312.99 / −0.447% against the 706.74 RAW fill.** **On the last
  COMPLETED close (09-28, `--adjustment all`, 703.60, re-pulled this run): equity $99,688.98, core
  $69,688.98 = 69.9064% — unchanged from the pre-market figure, because the completed close did not
  change.**
  ⚠⚠ **NEW AND OBSERVED INSIDE A SINGLE RUN: THREE DIFFERENT EQUITY NUMBERS, SECONDS APART.** Pre-flight
  **$99,694.43**, `sleeves` **$99,687.00**, `account` **$99,685.02** — a spread of **$9.41** across three
  calls in one minute. ⚠ **These are not three errors; they are three live midpoints of a moving quote,
  which is open item (5) stated exactly. Previously it was seen ACROSS runs; this is the first time it has
  been caught WITHIN one.** ⚠ **STANDING CONSEQUENCE: an intraday equity figure is only meaningful with
  its CALL and its TIMESTAMP attached, and two figures from different calls must never be differenced.**
  **Forty-ninth consecutive run inside 69.59–70.22.** ⚠ **`rebalance_delta` is POSITIVE on BOTH bases for
  the second consecutive run (+$51.71 broker, +$93.30 official) and the bases AGREE. NOT the defect
  resolving; the same quantity disagreed in SIGN on 09-24. A run that checks one basis and finds agreement
  learns nothing.** **NO REBALANCE IS DUE** — §2 acts at the **65/75 band edge** and core sits **~4.95
  points** inside it.
  ⚠ **AUDIT ANY SUPERLATIVE BEFORE REPEATING IT.** On **price**, 09-28's −0.7010% **IS** the largest
  single-day loss on record; on **total return** it is **−0.5212%, SECOND**, behind 09-23's −0.5327%.
  Since inception −0.3110% is **NOT** a low — 09-16 reached −1.3396%, 09-15 −1.0350%, 09-10 −0.9954%.
  *(Grounded from a 30-session pull whose rows before the 09-03 fill are **COUNTERFACTUAL** — the account
  held $100,000 cash — and must never be read as account history.)*

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`, NEVER a
  `positions` field for a close or an execution reference. Close-to-close from `bars` (⚠ a COMPLETED
  session's bar, ⚠ and STATE THE ADJUSTMENT), a fresh `quote` for execution.** ⚠ **09-28: broker
  `equity − last_equity` = −$736.91 against a real price-basis move of −$703.72 — artifact −$33.19; and
  `last_equity` read 100,401.13, a FOURTH distinct number matching neither the official prior equity nor
  Friday's broker equity. The field is UNUSABLE, not imprecise.**
  ⚠ **`lastday_price` is CLOSED as a question — four falsified mechanisms, both signs observed. On 09-29 it
  reads **703.61**, which matches NEITHER basis (raw 703.60, adjusted 703.60) — an EIGHTH distinct miss and
  the first on a session where the two bases AGREE, so the ex-dividend rescaling cannot explain it.
  STOP PREDICTING IT; DO NOT RE-OPEN IT.** **Post-bell `current_price` series, SEVEN observations: +$1.13,
  −$0.22, +$0.169, +$0.02, −$0.97, −$0.054, −$0.25.** **Both signs, no predictable sign, no correctable
  offset.** **Keep writing falsifiable predictions down in advance for LIVE questions** — there is one on
  the dividend credit, above.

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS 16 OF 16 AND STILL HAS NO EXCEPTION.** **09-28 (total-return
  basis): VOO −0.7448%, the book −0.5212%, excess +0.2240pp — against +0.2227pp PREDICTED by simply holding
  ~70% core and the rest in idle cash. Agreement to 0.0013pp.** The satellite sleeve contributed **exactly
  0.0000%**, as it has for the account's entire history. ⚠⚠ **The 09-25 weekly review recomputed all 15
  post-fill sessions from official closes and found PERFECT separation: 9 VOO-down days ALL positive
  excess, 5 VOO-up days ALL negative, 1 flat day EXACTLY 0.0000pp. 09-28 is a TENTH VOO-down day with a
  POSITIVE excess — 16 of 16.** ⚠ **That is not a performance statistic — it is the signature of a book
  with ONE long position at ~70% weight and NO SECOND SOURCE OF RETURN.** ⚠⚠ **AND THE TWO READINGS ARE THE
  SAME FACT: on 09-25 a good day in dollars was a bad day against the benchmark; on 09-28 a LOSING day in
  dollars was a POSITIVE-EXCESS day. Neither is skill.**
  ⚠ **THE TRAP, and the standing same-source rule does NOT catch it: comparing the book's PRICE basis
  against VOO's `--adjustment all` gives a spurious +0.0438pp, because one leg excludes the dividend and
  the other includes it. BOTH LEGS ARE FROM `bars --adjustment all` — the mismatch is between the ACCOUNT
  and the BENCHMARK recognising the same cash on DIFFERENT DATES.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — TEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  ⚠⚠ **(10) A NUMBER THAT IS CORRECT ON A BASIS NOBODY NAMED.** The 09-28 close nearly wrote *"largest
  single-day loss on record"* off a 30-session series it had **just pulled**. ⚠ **The series was right and
  the sentence was still false.** ⚠⚠ **"Pull the source before writing the superlative" IS NOT SUFFICIENT
  WHEN THE SOURCE HAS TWO BASES. New rule: NAME THE BASIS IN THE SENTENCE, or do not write the sentence.**
  ⚠ **(9) A COUNTER WHOSE *UNIT* IS WRONG.** Close journals reported §5.1–§5.4 untested for *"the Nth
  consecutive **SESSION**"* — **23, 26, 29, 33, 37 on consecutive trading days.** ⚠ **It increments by
  THREE OR FOUR per trading day; sessions increment by ONE. It is a RUN counter wearing a session label.**
  ⚠ **Re-running the check REPRODUCES THE SAME NUMBER — only the CALENDAR exposes it.** **The 09-28 and
  09-29 runs report calendar figures instead: 20 trading sessions since 2026-09-01, 17 since the 09-03
  fill, zero satellite positions ever. Do not restart the old series.**
  **(8) A MEASUREMENT PRESENTED AS A CALIBRATION:** the 09-25 midday *"volume tracks elapsed session time
  almost exactly."* ⚠ **The DENOMINATOR was a prior-day mean, and a ratio against one LOOKS like a
  measurement of the current day and is not one.**
  **(7) A MISCOUNT IN A VERIFICATION CLAIM:** the 09-24 close wrote it had *"verified all TWELVE keys."*
  ⚠ **There are THIRTEEN.**
  **(6) A SCOPE CLAIM:** *"routine 2 is the ONLY routine that runs with `is_open: true`"* — falsified by the
  run that read it. ⚠ **The most dangerous shape, because it was not a number to re-pull but a statement
  about the SYSTEM'S OWN SHAPE, which no data call would ever contradict.**
  **(5) A TRUNCATED SERIES (09-24):** the post-bell `current_price` record had silently dropped its own
  largest member. **(1)** A false superlative surviving three runs, caught **by accident** 09-21.
  **(2)** A stale count ("49 theses") caught deliberately 09-22, running in the direction that
  **understates** the problem. **(3)/(4)** Both halves of the `lastday_price` mechanism, asserted and
  falsified in turn.
  ⚠ **A superlative, count, mechanism, SERIES, CALIBRATION or BASIS inherited from a prior run is NOT a
  checked fact.** **Assume the next one you are handed is wrong until you have pulled the source — and then
  check which basis the source answered on.** *(09-29 recounted the thesis total from source: **80 `### T-`
  headings less the template = 79**, consistent with 73 + this run's 6.)*

- **⚠ GNRC IS NOT YOURS TO LOOK AT — TWENTY-NINE CONSECUTIVE REFUSALS.** ⚠ **Graded honestly: 09-29 made
  ZERO `move` and ZERO `quote` calls on GNRC and ran zero Perplexity queries naming it. It had a live funnel
  and an open data plane, so the refusal was NOT free — but no candidate's thesis wanted a Generac number,
  so it is a MEDIUM instance, not a strong one.** The disqualifying facts do not move: **GNRC is the named
  counterparty in the Amazon announcement — first-order, outside §4 at any price** — and **open item (7) is
  resolved by a human editing §4 or `alpaca.py move`, not by a number this seat collects.** ⚠ **WHAT MATTERS
  IS NOT THE COUNT BUT WHETHER EACH REFUSAL COST ANYTHING, AND MANY DID NOT. Quoting the bare count
  overstates the evidence.** The strong instances are the pre-market runs of 09-23, 09-24 and 09-25.
  ⚠ **No new costume in nine sessions; the list looks CONVERGING rather than growing.** Costumes: diligence,
  curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure,
  call-already-open, screen-already-running. **The pattern is the finding, not any instance. FREE IS NOT
  THE SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FIFTY-SEVEN RUNS.** §5 exempts core from all four
  sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **09-29 grades LOW: routine 1 has no write step for high-water marks and held only a pre-market
  midpoint, which is not a close and could not have been stamped even in error.** **Measure the core from
  the 706.74 fill and from an official close, never from a `positions` field** ⚠ **— and note that the fill
  price is a RAW print, so measuring it against an `--adjustment all` close MIXES BASES.**
  ⚠ **Noted honestly: this refusal is close to automatic, and automatic is not the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN IS
  USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today** *(09-29 did: `is_open:
  false`, `next_open: 2026-09-29T09:30` — the pre-market shape, correctly NOT read as a holiday)*; post-bell
  sees it pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with **no
  bar for today**. ⚠ **`is_open: TRUE` is the one case where the boolean alone is sufficient, and only
  because TRUE has a single meaning. FALSE has three.** ⚠ **THE STRONGER DISCRIMINATOR FOR A POST-BELL
  FALSE IS TO CHECK THAT A DAILY BAR FOR TODAY EXISTS.** ⚠ **But with `is_open: true` that same bar is
  PARTIAL and is not a close.**

- **⚠ EIGHT ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A NUMBER A
  RUN COLLECTS.**
  ⚠⚠ **(8) THE ONLY ONE THAT COULD MAKE §1 UNWINNABLE BY CONSTRUCTION: DOES THE PAPER ACCOUNT PAY
  DIVIDENDS?** VOO went ex-dividend 2026-09-28; `cash` still reads **exactly $30,000.00** on 09-29.
  **A falsifiable test with a 2026-10-07 deadline is on the record.** ⚠ **AND SEPARATELY: whether the
  TOOLING should read closes on a stated basis by default is a human's call; 09-28 is the strongest
  evidence yet that it should.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — nine instances plus three near-misses;
  **there is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on the bill.
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM, AVAV, and
  **AKAM, the first MULTI-SESSION round trip.** Same root cause as (1), opposite direction. **The fix for
  (1), (2) and shape three is a human editing §4 or `alpaca.py move`** — the suggestion on record is to make
  it **read SIGN and causation, not loosen or remove the threshold.**
  **(3)** The satellite sleeve is **structurally undeployed — 79 theses, zero positions, ever.** A 70/30
  cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits the cash and
  §4 says most runs end in no trade — both rules were followed, and the agent must NOT respond by lowering
  the §4 bar.** **The binding constraint now has SIX known forms:** the source withholds the counterparty's
  number; **or** the counterparty discloses **roadmap instead of segment revenue**; **or** the named
  beneficiary is **vertically integrated**; **or** **both parties expressly refuse to disclose as a
  commercial choice** (GM); **or** **the figure is fully disclosed and is the WRONG QUANTITY** (JBL); **or —
  new on 09-29 — THERE IS NO COUNTERPARTY AT ALL** (IOVA: own product, own facility, no external supplier
  named anywhere). ⚠ **Only the first two are addressable by widening the evidence bar. Forms three through
  six are not, and form five would be made WORSE by widening it.** ⚠ **ELMT is the standing proof that
  evidence is not the constraint.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the prior
  close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11.** ⚠ **Keep measuring it from
  the fill — and the fill is a RAW print.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it never
  had a stable size. ⚠ **A PRICE-SOURCE problem that contaminates every derived figure.** It has flipped the
  sign of a §2 quantity (09-24). ⚠ **09-28 added a SECOND, INDEPENDENT axis — `quote` vs `bars --adjustment
  all` on the SAME session — which is not a midpoint problem at all.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed all
  five checks on 09-11 while `clock` returned 500, and on 09-24 while `perplexity.py` returned 500.
  ⚠ **AND IT PASSED ALL FIVE ON 09-28 AND 09-29 WHILE THREE OF 09-28's FOUR ROUTINES HAD PRODUCED NOTHING.
  A green pre-flight certifies THIS run's credentials, nothing about the schedule, the data plane, or
  whether the other routines ran.** **Probe by hand; CHECK EXIT CODES.**
  **(7)** **`alpaca.py move` cannot see an after-hours event, and neither can the 09:35 re-validation that
  exists to catch exactly this.** ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a trade.**
  ⚠ **AKAM generalises it: the blindness is to ANY event move the window later cancels.** **It has cost zero
  only because no plan has yet carried a BUY intent — an absence of exposure, not a mitigation.**
  Prior context in ClickUp `86bbv75bz`; week-prior `86bbzgbg3`. **09-25 daily summary: `86bc7vgbw`; 09-25
  weekly review: `86bc7vzam`; 09-28 daily summary: `86bc8yrz0`.**

- **⚠⚠ WEEK 4 REVIEW (2026-09-25) — RAN, POSTED `86bc7vzam`. THE §1 ANSWER IS NO, AND EVERY WINDOW SAYS SO.**
  Satellite **0.0000%**, so its dollar-weighted excess is exactly **minus VOO's total return**: **−1.262pp
  week, −0.827pp since inception, −0.974pp 1M, −5.444pp 3M, −18.571pp rolling 12M.** ⚠ **Week 3's first
  three rows were POSITIVE. The market rose and the whole column inverted with NO rule change and no change
  in the sleeve. DO NOT RE-INHERIT THE PLEASANT VERSION; it was a property of a falling tape.** Structural
  cost now **~5.57pp per rolling 12M**, up from 4.97pp **because the BENCHMARK improved, not because the
  sleeve got worse.** **Reject board: 65 names, 20 beat VOO, 45 lagged, mean −2.04%, median −2.47%.**
  ⚠ **A tally, not a result.** **CRDO is the largest opportunity cost at +24.28pp**; HPE +20.67pp, MU
  +14.42pp, QCOM +13.11pp, LITE +11.16pp. ⚠ **Six of the top six excesses are ONE THEME (AI/data-centre
  hardware and semis) rejected under FIVE DIFFERENT §4 rules, every rejection individually correct.**
  ⚠ **A CORRECTION TO WEEK 3'S HEADLINE: it promoted the board's "widening" as the finding. Dispersion grows
  with elapsed time MECHANICALLY. The MEAN is the evidence.**
  ⚠ **FILE SIZE — TWELFTH CONSECUTIVE FLAG.** `research_log.md` now **~346KB** (grew this run),
  `journal.md` ~**170KB**, `state.md` ~**45KB**, `weekly_review.md` **147KB**. ⚠ **THE 2026-10-02 REVIEW
  MOVES THE WHOLE SEPTEMBER CORPUS IN ONE DESIGNED OPERATION AND IS THREE SESSIONS AWAY. Do not re-litigate
  this weekly; a human who disagrees should say so in `control.md`.**

- **⚠ A `#` IN A FENCED-BLOCK VALUE SILENTLY TRUNCATES IT.** `_parse_kv` in `scripts/common.py` does
  `line.split("#", 1)[0]`, so **everything after the first `#` in a `key: value` line is discarded by the
  parser.** ⚠ **STANDING CONSEQUENCE: never put a `#` in a fenced-block value, and VALIDATE `state.md` WITH
  `common.read_state()` AFTER REWRITING IT — writing the block and parsing the block are not the same
  check.** *(Done at the 09-29 pre-market: **13 keys**, no `#` anywhere in the block, and `last_run` /
  `prior_run` compared **character-for-character against the file**. Eyeballing does not make truncation
  visible; the comparison does.)*
  ⚠⚠ **AND ON 09-29 AT 09:35 THE TRAP ACTUALLY FIRED, FOR THE FIRST TIME ON RECORD — ON THIS SYSTEM'S OWN
  WRITE, NOT A HYPOTHETICAL.** The market-open run wrote the phrase *"its only `###` heading is the
  TEMPLATE"* into `last_run`, describing `positions.md`'s template, and `_parse_kv` **silently discarded
  everything from that `###` onward** — roughly **half the entry**, including the reconciliation result,
  the rebalance finding and the dividend check. ⚠ **The file on disk looked completely normal. Nothing
  errored. The only thing that exposed it was `common.read_state()` and printing the value's TAIL.**
  ⚠⚠ **THE LESSON IS SHARPER THAN THE OLD WARNING: THE `#` DOES NOT ARRIVE AS A COMMENT MARKER — IT
  ARRIVES INSIDE A MARKDOWN QUOTATION, WHICH IS EXACTLY WHAT A RUN DESCRIBING ITS OWN FILES WILL WRITE.**
  ⚠ **VALIDATING IS NOT ENOUGH; YOU MUST READ THE TAIL OF EVERY LONG VALUE BACK, because a truncated value
  parses cleanly and counts as one key. Key count did not change: 13 before, 13 after.** *(Fixed by
  rewriting the phrase without the character; re-validated to 13 keys, no `#`, both long values matched
  character-for-character against the file.)*

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** compared to **consensus** rather than to any prior company
figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations** (Centene, Southwest,
General Mills), **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence, Alcoa/South32, Nocera/E-PRO),
**a genuine transaction whose DELIVERY MILESTONE is recycled as the news** (GM/Lockheed), **a PRE-IPO
CONTRACT BOOK** (Nscale's $103B), and **a FORMAL PRESS RELEASE RESTATING AN ALREADY-FILED 8-K**
(Akamai/Anthropic). ⚠ **STANDING PRACTICE: ask a transaction WHEN IT HAPPENED before asking who it helps —
and WHEN THE SOURCES DISAGREE ON THE DATE, THE PRICE SERIES IS THE CHEAPER WITNESS.**
⚠⚠ **09-29 PRODUCED A CLEAN PASS AND A CLEAN FAILURE ONE ENTRY APART, FROM THE SAME QUERY, AND THE
DIFFERENCE IS THE WHOLE TEST: IOVA raised FY2026 guidance from ITS OWN prior $350–370M to $410–420M (PASS —
a company number against the same company's earlier number); AAR quoted 14–16% Q2 growth with NO PRIOR
RANGE ANYWHERE IN THE SOURCE (FAIL — whether that is a raise, a cut or a reiteration is not
establishable).** ⚠ **The test is cheap: did the source carry the company's OWN prior figure?**
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — and 09-29's AMRAAM chain would have
been its third appearance).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share," "the
only company that makes X" are facts about an **industry**, not a **transaction** — plus the **CEILING
sub-shape**. Costumes: a **table** (DoD daily contracts digest), a **consortium awardee** (Abrams), a bare
sentence, a **MULTIPLE-AWARD CEILING across fifteen vendors** (RDW's "$980M"), and an **UNNAMED SUPPLY BASE
made to look nameable by an exact figure and a named component category** ($1.7B of "memory components").
⚠⚠ **09-29 ADDS THE LARGEST INSTANCE YET: a $20,699,334,581 not-to-exceed AMRAAM award that NAMES FOUR
CONTRACT LINE CATEGORIES — "All Up Rounds, Guidance Sections, Direct Charge, FMS Offsets" — AND ALLOCATES
NONE OF IT TO ANY SUBCONTRACTOR.** ⚠ **The only supplier language in any source is "small and mid-sized
suppliers across the country."** ⚠ **A precise figure plus named COMPONENT CATEGORIES is the most fillable-
looking blank this funnel produces, because the industry answer (Aerojet Rocketdyne, now inside L3Harris) is
sitting right there in the reader's priors. THE SOURCE LEFT THE BLANK; FILLING IT IN IS NOT RESEARCH.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.* Long-dated
energy offtake is **a standing feature of this funnel, not a visitor** — Sempra/Petrobras, Venture
Global/China Gas, Amazon/Generac, Centrus/Antares, Elmet/Tungsten West, NeoVolta/SK On. ⚠ **The REGULATORY
version: a non-binding advisory vote → an undated FDA decision → reimbursement → commercial ramp (ILMN) is
the same shape wearing a lab coat.** ⚠ **09-29 adds the CLINICAL-COLLABORATION version (SMMT/AZN on
ivonescimab) and the PENDING-DEFINITIVE-AGREEMENT version (CRK/SOCAR, where the PSA is not even signed).**
**Part 3 kills these in ONE step.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
⚠⚠ **09-29's IOVA IS THE CLEANEST INSTANCE ON RECORD and it killed the day's best rule (iii) pass: a
cell-therapy maker that manufactures Amtagvi itself and names no external CMO or supplier anywhere.**
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part 2.**
Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; Brookfield/Bloom's **$25B** is a
**FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**; SoftBank's **$11.1B** is **capital paid IN to a private
recipient**; Royal Caribbean's **~$3B** for Sandals is **capital paid OUT by the buyable leg**; BBY's only
disclosed economics was **Meta taking "a small fee" — a COST at the candidate, described in language that
reads like a partnership benefit**; FMC/Tessenderlo's **$403M is a SECONDARY-MARKET SHARE PURCHASE.**
⚠ **09-29 ADDS TWO MORE, BOTH CAPITAL PAID IN: AstraZeneca's $2.0B for Summit CONVERTIBLE PREFERRED (equity
issuance — it DILUTES rather than earns) and SOCAR's $1.65B into Comstock's Haynesville (and the paying leg
is a state oil company that cannot be bought).**
⚠⚠ **AND THE DEFINITIVE INSTANCE, JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K — AND IT
IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A disclosed
statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.** ⚠ **A large,
real, sourced, prominently-placed number is not a dollar path. THIS IS THE WORKED EXAMPLE TO REACH FOR
FIRST.** T-2026-09-18-04 (BLK) remains the other: **part 1 passed cleanly and it died on the absent segment
figure, NOT on size.**

**⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT WORKS IN BOTH SIGNS.** Two companies moving on the same macro
input (a crush spread, a mortgage rate, a rate decision) is a **market**, not a **transaction**, and the
giveaway is that part 1 needs an *"and also"* clause. ⚠ **A DIVERGENCE between two named companies sounds
causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge and ADM) — and the convergent version is MORE DANGEROUS,
because agreement LOOKS LIKE CORROBORATION when it is in fact the clearest possible statement that the input
is a market variable.** ⚠ **The third and most respectable face is a COMPETITOR'S EARNINGS PRINT**
(AutoZone's FQ4 read across to GPC/ORLY/LKQ). **The giveaway never changes: the sentence needed an "and
also".** ⚠ **09-29's CRK/SOCAR is the CAPITAL-EXPENDITURE face: "an investment funds drilling AND ALSO some
unnamed service company wins the work."**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — AND IT IS THE MOST CONVINCING NON-EVENT THE FUNNEL PRODUCES.**
⚠ **This is the FOMC object — an environment input — but in a far more persuasive costume: a policy action
is SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN AFFECTED INDUSTRY, and MOVES THE TAPE ON THE DAY.** It
nonetheless has **ONE party.** ⚠ **A long-only book cannot trade money being WITHDRAWN from a sector unless
some NAMED party receives it — and nobody does.** ⚠⚠ **09-29 SUPPLIES THE NEWEST AND MOST SEDUCTIVE COSTUME:
A MARKET-IMPLIED PROBABILITY THAT MOVED.** CME FedWatch went from ~57% to **~70%** odds of an October hike
in a week, alongside the 10-year at ~5.25% and the 30-year at ~5.56–5.57%. ⚠ **A probability that CHANGED
reads like an event with a date, which is exactly why it is more tempting than a bare yield level. It is the
same object: no named recipient, no transaction, one party.** ⚠ **SCALE MAKES IT MORE CONVINCING, NOT LESS.
Every "who wins from higher rates / higher oil" answer needs an "and also".** ⚠ **The counter-case still
stands and must not be over-applied against: an FDA advisory vote (ILMN/GRAIL) ENABLES a named company's
product and that company has a named supplier — a real two-party chain. Do not over-apply this rule to
approvals.**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is **exits-only by
construction** and may not open a position under **any** circumstance. Routine 2 executes **only what
`plan_today.md` already contains** — a position opened at 09:35 without a plan entry routes **around** the
discipline rather than satisfying it. Routine 4 **RECORDS AND JOURNALS; IT DOES NOT TRADE.** ⚠ **Idle cash,
an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an opportunity any of those seats may act on** —
⚠ **and neither is a green day that still lags the benchmark.** New positions route through pre-market
research **plus** the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT THE
SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.** The gate
has now been exercised **TWENTY-NINE times and has never fired** *(09-29 09:35: `plan_date` 2026-09-29
against ET date 2026-09-29 — **FRESH**, so the gate correctly did nothing)*, and its alert path **remains
untested code.** ⚠⚠ **AND 09-28 WAS THE MORNING IT WOULD FINALLY HAVE FIRED — `plan_today.md` genuinely carried
`plan_date: 2026-09-25` — AND THE RUN CONTAINING THE GATE DID NOT EXECUTE. The prediction was right about
the setup and the test STILL DID NOT HAPPEN.** ⚠ **Twenty-eight quiet opens are NOT evidence it works. The
first morning it fires will by construction be a morning when the pre-market run failed — i.e. exactly the
morning with no fresh notes to lean on. Read routine 2's Step 2 then; do not recall it.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a broker mark
on one leg against an official close on the other. **Both legs from the same source, and for returns that
source is `bars --adjustment all`** ⚠ **— on a COMPLETED session.** ⚠ **And state WHICH basis produced any
figure you quote.** ⚠ **09-28 showed the rule is NECESSARY BUT NOT SUFFICIENT: two legs can both come from
`bars --adjustment all` and still be incomparable, when the ACCOUNT and the BENCHMARK recognise the same
cash on different dates.**

### Do not reach for these — disposed rejects and the trap in each

⚠ **Added 09-29:** **AMRAAM component suppliers** — ⚠ **rule (v)'s largest instance: $20.7B, four named
CONTRACT LINE CATEGORIES, and not one subcontractor named or allocated a dollar.** RTX is first-order. **Do
not fill the blank from priors; "Aerojet Rocketdyne / L3Harris" is an industry answer, not a disclosure —
and LHX would be its THIRD appearance in this log (rule iv).** **IOVA** — ⚠ **the best rule (iii) pass in
weeks, killed by rule (vii): Iovance makes Amtagvi itself and names no external supplier. A SIXTH form of
open item (3) — no counterparty exists at all, so no widening of the evidence bar reaches it.** **SMMT /
AstraZeneca** — the $2.0B is **capital paid IN for convertible preferred** (rule viii); SMMT is first-order;
a clinical collaboration is years, not quarters (rule vi). **CRK / SOCAR** — $1.65B **capital paid in** by a
**non-US-listed state oil company**; the second-order sentence needs an **"and also"**; the PSA is not even
signed. **AIR / MRO Holdings** — the only Company B is **private**, and **AAR's own prior guidance is absent
from the sources, so rule (iii) cannot be cleared in either direction.** **The rate / Fed-repricing
complex** — ⚠ **environment input, ONE party; a probability that MOVED (57% → 70%) is the most seductive
costume yet and changes nothing.** **TOYO** ($240M, customers unnamed) · **Megaport** (A$978.6M,
counterparties unnamed, ASX-listed) · **Draganfly / Unusual Machines** (microcaps, co-investor unnamed) ·
**Uniserve** ("an enterprise client", ~$3.15M) · **Newgen Software** ("a US-based health insurer", $5.475M,
Indian-listed) · **Exascale Labs** ($14.8M revenue, §3) · **Uranium Energy Corp** (a clean rule (iii) pass
with **no second party anywhere in the disclosure**) · **Sangoma** (Canadian; purchaser, value and terms all
undisclosed).

⚠ **Added 09-25:** **JBL** — ⚠ **the most important entry on this board.** Part 1 passes **cleanly**, every
party is named, the instrument is signed and filed, and the figure is **$1.7 billion in an 8-K** — **and
part 2 fails outright**, because the money is Akamai's, the components are held **in consignment as bailee**,
and the repurchase is **expressly at cost**. ⚠ **Do not reach for this at a lower price; the price was never
the problem.** **AKAM** — **first-order**; and its `priced_in: false` at +3.19% is an **artefact of a +12.35%
jump and a −6.74% give-back inside one window**, ⚠ **NOT a clean pass.** **Memory suppliers to the Akamai
build** — **no manufacturer named in any disclosure**, rule (v). **Lenovo** — **§3 outright**, HK-listed with
only an OTC ADR. **RDW** — the **$980M is a multiple-award CEILING across 15 vendors**; first-order; below
the §3 floor. **FLNC / EVE Power** — **no value or volume disclosed**; EVE is Shenzhen-listed. **FMC /
Tessenderlo** ($403M **secondary share purchase**) · **LLY / InnoCare** (no value disclosed) · **NOC
$123.8M, RTX $50.1M, Stark $114.0M, Southern $22.0M, RGAS $23.6M** (DoD digest, rule (v)) · **Blue Cloud
Softech / IBM** (Indian-listed) · **FingerMotion** (offtakers unnamed) · **Everforth, Endovia, Algorhythm**
(private or microcap) · **Amazon's $100M Greenwood plant** (immaterial) · **Welspun** (§3, buyer unnamed).

⚠ **ELMT — DO NOT SCREEN IT AGAIN.** It entered this funnel **three times in three sessions** and the third
time carried a **disclosed price ($124.75M)** — exactly the material whose absence killed the first two.
⚠ **"But now there is a number" is the purest form of the pull to re-open a §3 kill on evidence §3 does not
weigh. A microcap with a Vietnam-listed counterparty is ineligible at every price and at every level of
disclosure.**

⚠ **Earlier disposed rejects (09-21 to 09-24) remain disposed and are NOT re-listed here.** **ILMN, GRAL,
BBY, PYPL, SHOP, SoftBank/OpenAI, GIS, LH, CNC/MOH/OSCR, LHX, GFS, ACN, GPC/ORLY/LKQ, GM, BE, BG** — see
`research_log.md` for the working on each. **A rejection is not a queue.**
