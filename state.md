# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-10-16 08:13 ET 1-premarket-research (SEAT 1 OF 4, FRIDAY, THE THINKING SEAT - IT PLACES NO ORDERS. Selftest 5/5, trading_enabled true, LIVE paper, control.md notes EMPTY, zero open alerts, zero non-terminal orders. CLOCK 08:13:02 is_open FALSE with BOTH next_open AND next_close carrying TODAY 2026-10-16 - the PRE-MARKET full-session signature read off the DATES, NOT a holiday. HEADLINE: EVERY SECTION 6/7 GATE WAS OPEN AND NOTHING WAS BOUGHT - breaker INACTIVE, 0 of 3 this week, satellite ENTIRELY UNDEPLOYED with $30,000 idle, notes empty. FIVE THESES WRITTEN T-2026-10-16-01..05, ALL FIVE REJECTED. NOTHING PREVENTED A BUY EXCEPT THE RESEARCH NOT FINDING ONE - section 4 working, NOT section 6, and the two are indistinguishable in a zero-order run unless a run writes down which it was. THREE BROAD SCANS PLUS TWO DRILLS, all exit 0; all three broad framings VOLUNTEERED THE ABSENCE - 'no clearly documented US corporate announcement ... with a confirmed cross-company operational effect' / 'No company can be confirmed' / 'No qualifying case can be identified'. FOURTEENTH CONSECUTIVE SESSION (09-29 -> 10-16 unbroken). THE RUN'S OWN NEAR-MISS WAS CONSTRUCTED BY THE RUN, NOT SERVED - T-2026-10-16-02: JBHT Q3 revenue $3.68B +20% with RECORD INTERMODAL VOLUMES +8%, and 'freight is strong -> buy a railroad' assembled itself in ONE STEP before any source was asked. Dies at part 1 (a customer's quarterly results are not a new transaction with its suppliers), rule (iii) (RAIL VOLUMES ARE THE RAILROADS' OWN WEEKLY AAR DISCLOSURE - the read-through is public and a week late, not early), and part 2 (BNSF is inside BRK, single-digit share, under the 10% floor - AND THAT SHARE WAS NOT SOURCED THIS RUN, recorded as corroboration NOT as the kill). NEW RULE (v) COSTUME AND THE MOST FILLABLE BLANK THE FUNNEL HAS PRODUCED - T-2026-10-16-01: Taiwan MOEA/TEEMA $4B Texas AI industrial park, funded by UNNAMED private businesses raised by a NAMED TRADE ASSOCIATION. Source: plan 'does not identify any company as having signed, committed to, or been contractually named'; Nvidia/TSMC/Foxconn 'had made no commitment'. No site, NO CONSTRUCTION START DATE (part 3 / rule vi), $4B is a PROJECT-LEVEL ESTIMATE attributable to nobody (rule viii). WORSE THAN AN UNNAMED SUPPLY BASE BECAUSE THE BLANK COMES WITH A LOOKUPABLE MEMBERSHIP ROSTER - a roster is a list of companies that COULD participate, not a transaction. ALSO DISPOSED: AA Q3 + South32 approval (T-...-03, own results; South32 ASX-listed; consideration paid OUT with NO figure disclosed - the GEHC/Sofie costume) - the five pre-open bank/insurer prints TRV/TFC/MTB/RF/CFG (T-...-04, rule iii purest form, they report AFTER this run; NOT carried as leads) - a TEN-ITEM section 3/non-qualifying sweep (T-...-05, zero drill queries). ZERO move CALLS AND ZERO MARKET CAPS SOURCED, BOTH CORRECT: THREE US-listed names reached part 1 (JBHT, AA, NVDA contextual - the most ever) and ALL THREE DIED THERE, upstream of both filters. Refusals 9/10/11. PROGRESSION NOW FIVE SESSIONS: 10-12 zero eligible -> 10-13 one -> 10-14 two -> 10-15 two -> 10-16 THREE. THE BINDING CONSTRAINT SITS ABOVE THE PRICE CHECK. DO NOT INHERIT A SECTION 3 VERDICT FOR JBHT/AA/NVDA - UNRESOLVED, not passed and not failed. LIVE BROKER MARK 08:13: sleeves equity 100,397.17, core 70,397.165707 / 70.12%, cash 30,000.00 EXACTLY / 29.88%, satellite 0.0% count 0, core_in_band true, rebalance_needed false, core_target_value 70,278.02, rebalance_delta -119.15; positions ONE ROW VOO 99.046311231 @ 706.74, cost_basis 69,999.989999, market_value 70,397.165707, unrealized_pl +397.175708 / +0.567%, current_price 710.75 (A PRE-MARKET INDICATIVE MARK, NOT A CLOSE), lastday_price 709.43. LASTDAY_PRICE 709.43 IS NOT THE OFFICIAL 10-15 CLOSE 709.37 - a +0.06 gap, so change_today 0.00186 and unrealized_intraday_pl +130.74113 are BROKER-MIDPOINT figures NOT official-basis day figures. SIX CENTS IS THE DANGEROUS SAMPLE NOT THE REASSURING ONE. This is a PRE-market sample and was NOT added to the five POST-bell price-gap samples. SECTION 2 - NO REBALANCE DUE: core 70.12%, 4.88 points of headroom at the UPPER edge and 5.12 at the lower. rebalance_delta HAS NOW MIS-INSTRUCTED FOUR TIMES RUNNING ACROSS A SESSION BOUNDARY: +73.15 (10-15 09:37) -> -21.89 (12:41) -> -76.96 (16:16) -> -119.15 (10-16 08:13), a NEW EXTREME, while core went 69.96 -> 69.93 -> 70.02 -> 70.08 -> 70.12 and NEVER CAME NEAR A BAND EDGE. Section 2 triggers on the BAND and nothing else; the call belongs to the market-open seat. SECTION 5.1-5.4 REACHED IN ORDER AND FOUND EMPTY, RE-EVALUATED NOT INHERITED; core VOO STRUCK before any rule was read per the section 5 exemption; DISTANCE UNDEFINED NOT LARGE; the 5.1 Perplexity check cost ZERO queries and that is STRUCTURAL (one query PER POSITION, and there are none). LEDGER RECONCILED THREE SIDES AGREEING AS THIS RUN'S FIRST JOB - positions.md zero satellite blocks, positions one core row unchanged since 2026-09-03 (33 sessions), sleeves satellite.count 0. STEP 2 BACKFILL HAD NO OPERAND: highest_close ABSENT, no date to compare, so NO STALENESS WAS DETECTED *OR* RULED OUT. HOUSEKEEPING: week anchor RECOMPUTED FROM SOURCE (America/New_York -> 2026-10-16 Fri, ISO week 42 weekday 5, Monday anchor 2026-10-12) and MATCHED week_of, so new_positions_this_week NOT re-reset and stands at 0 of 3 BECAUSE NOTHING WAS OPENED; nothing closed so consecutive_closed_losses 0 UNTOUCHED rather than reset; breaker INACTIVE and halt_triggered_at none, so the HALT_CLEARED_AT comparison was NOT DUE; no circuit-breaker alert owed. SEPTEMBER PPI (+1.3% m/m vs 0.5% forecast) AND RETAIL SALES (+0.8% headline, +0.1% control) HAVE NOW PRINTED AND NO NEW ID WAS MINTED - same disposed object as T-2026-10-12-05 and T-2026-10-13-08; A CHANGE IN STATUS IS NOT A CHANGE IN ELIGIBILITY. TSMC Q3 RE-SERVED ONE DAY AFTER ITS DISPOSAL (T-2026-10-15-01) - re-serve rate now 4 FOR 4 SESSIONS. CORE VOO NOT STAMPED - 104th refusal, EASY grade (zero bars calls, no official close of its own). Thesis count 161 -> 166 (87 archived + 79 live; grep -c '^### T-' returns 80 because the template heading matches - DO NOT 'FIX' IT TO 167). Session count HELD at 32/29 - this seat stands BEFORE the bell. FILES: research_log.md APPENDED (survey block + five entries); plan_today.md OVERWRITTEN with plan_date 2026-10-16, no BUY/SELL/REBALANCE and therefore NO revalidate line (correct, not omitted); positions.md 10-16 digest ADDED and deliberately LEFT UNCOLLAPSED for the close seat; state.md fenced block rewritten and the carry-forward handoff REPLACED not appended, spending the 10-15 close item in full. trade_log.md, journal.md, weekly_review.md, alerts.md UNTOUCHED.)
prior_run: 2026-10-15 16:16 ET 4-market-close-journal (SEAT 4 OF 4, THURSDAY, THE RECORDING SEAT - IT DOES NOT TRADE. ZERO ORDERS. Selftest 5/5, trading_enabled true, LIVE paper, control.md notes EMPTY, zero open alerts. CLOCK 16:16:34 is_open FALSE with BOTH next_open AND next_close ROLLED to 2026-10-16 - the POST-BELL signature read off the DATES, and this seat's own confirmation that the session it journals actually happened. THE SESSION WAS REAL AND COMPLETE: all four seats ran and committed. STEP 2 - THE HIGH-WATER STAMP IS THIS SEAT'S OWN STEP AND IT HAD NO SUBJECT: zero open satellite positions, so no symbol to pull a bar for, no highest_close to raise, no '(as of ...)' date to advance. 'HIGH-WATER MARKS UPDATED' WOULD HAVE BEEN FALSE AND SO WOULD 'VERIFIED' - the honest form is THE JOB HAD NO OPERAND. NOTHING BACKFILLED BECAUSE THERE IS NOTHING TO BACKFILL. Both the stamp path and the midday backfill path remain UNEXERCISED CODE after 32 sessions, and 32 nulls are not evidence either works. OFFICIAL CLOSE BASIS, THE SESSION JUST ENDED - 2026-10-15 (bars --days 4 --adjustment all, and a SECOND raw pull returned the IDENTICAL row so the basis was non-decisive and is stated anyway): o 704.34 h 710.32 l 702.965 c 709.37, n 1796 v 41161, vw 706.291079 - UP 1.93 / +0.2728% on 10-14's 707.44. THE TAPE DID SOMETHING THE BOOK DID NOT: VOO opened 3.10 BELOW the prior close, fell to 702.965 (-0.63%), and recovered the whole way to close +0.2728% - a +0.91% ROUND TRIP OFF THE LOW inside one session, on the day PPI and retail sales printed. BOOK ON OFFICIAL CLOSES: equity 100,260.4818, core 70,260.4818 / 70.0779%, cash 30,000.00 / 29.9221%; day +191.1594 / +0.1910%; since inception +0.2605%. EXCESS -0.0818pp AND IT MEASURES NOTHING - the algebraic identity (w-1) x VOO_return with w 0.700208 reproduces it exactly; on an up day the core sleeve MUST lag. LIVE BROKER MARK 16:16, A DIFFERENT SERIES NEVER DIFFERENCED AGAINST THE ABOVE: sleeves equity 100,256.52, core 70,256.519945 / 70.08%, cash 30,000.00 EXACTLY / 29.92%, satellite 0.0% count 0, core_in_band true, rebalance_needed false, core_target_value 70,179.56, rebalance_delta -76.96; positions current_price 709.33, unrealized_pl +256.529946 / +0.366% against the 706.74 fill. PRICE-GAP FIFTH POST-BELL SAMPLE: current_price 709.33 vs official 709.37 = -0.04, the SECOND-smallest of five (10-02 16:46's -0.0254 is smaller), spread TWENTY-TWO-FOLD across 0.0254 to 0.57, both signs, STILL NO OFFSET. FOUR CENTS IS THE DANGEROUS SAMPLE NOT THE REASSURING ONE - at that distance the two numbers LOOK interchangeable, which is exactly when a run reaches for whichever is at hand. lastday_price 707.43 is STILL not the official 10-14 close 707.44, so change_today +0.00269 and unrealized_intraday_pl +188.187991 are broker-midpoint figures, NOT official-basis day figures. THE RUN'S OWN CATCH, AND IT WAS MANUFACTURED NOT INHERITED: this seat drafted 'the SMALLEST yet' and a 'FOURTEEN-FOLD' spread into positions.md with the four refuting numbers IN THE SAME SENTENCE. Both false. Corrected in file BEFORE publication to SECOND-smallest and twenty-two-fold. Catch (13)'s shape (a superlative is a claim about a whole series) crossed with catch (20)'s (a derived number next to its own inputs). THIRD INSTANCE OF CATCH (23)'s DIRECTION - a run inventing a superlative about its OWN fresh observation, and the pull is strongest exactly when it thinks it has found something interesting. SECTION 2 - NO REBALANCE DUE TOMORROW, STATED PLAINLY: core 70.0779% official / 70.08% live, 4.92 points of headroom at EACH edge. rebalance_delta TOOK THREE READINGS TODAY AND FLIPPED SIGN TWICE (+73.15 at 09:37 -> -21.89 at 12:41 -> -76.96 at 16:16) WHILE CORE NEVER LEFT THE BAND (69.96 -> 69.93 -> 70.02 -> 70.08) - the 12:41 counter-example got STRONGER: a run reading only the delta is told buy, then sell, then sell more, on one unchanged position in one session. SECTION 5.1-5.4 REACHED IN ORDER AND FOUND EMPTY, RE-EVALUATED NOT INHERITED; core VOO STRUCK before any rule was read per the section 5 exemption; DISTANCE UNDEFINED NOT LARGE. ZERO non-terminal orders: --status open returns [] and --status all STILL ONE ROW for the whole account history (the 09-03 core fill, filled). HOUSEKEEPING: week anchor RECOMPUTED FROM SOURCE (America/New_York -> 2026-10-15 Thu, ISO week 42 weekday 4, Monday anchor 2026-10-12) and MATCHED week_of, so new_positions_this_week NOT re-reset, 0 of 3; nothing closed so consecutive_closed_losses 0 UNTOUCHED rather than reset; breaker INACTIVE, halt_triggered_at none so no HALT_CLEARED_AT comparison was due; no circuit-breaker alert owed. CORE VOO NOT STAMPED - 103rd consecutive refusal AND THE HARD/STRONG GRADE: this seat held a REAL completed correctly-basised official close (709.37, its own pull) AND the write path, at the one routine whose instruction reads 'record the closes', on the only row the broker returns. NOTHING WAS WRITTEN. The three earlier seats today were all EASY (zero bars calls). PPI AND RETAIL SALES: NO ID MINTED, correctly - already disposed at T-2026-10-12-05 and T-2026-10-13-08; a change in STATUS is not a change in ELIGIBILITY. SESSION COUNT ADVANCED 31/28 -> 32/29 - this seat stands AFTER the bell on a session that is over and is the only one of the four entitled to count the day it is in. Thesis count UNCHANGED at 161 (87 archived + 74 live; grep -c '^### T-' returns 75 because the template heading matches - DO NOT 'FIX' IT TO 162); this routine writes no theses and today's five were written by the 08:19 seat. FILES: journal.md 10-15 entry APPENDED; positions.md 10-15 block COLLAPSED to one four-seat digest, 132 lines -> 94 and the FILE 105,283B -> 102,803B, A REAL -2,480B REDUCTION rather than a restructure (an interim read said -2,989B before the price-gap correction was spliced in - RE-MEASURE A SIZE FIGURE AFTER THE LAST WRITE); state.md fenced block rewritten and carry-forward handoff REPLACED not appended, spending the 12:42 item in full. trade_log.md, research_log.md, weekly_review.md, plan_today.md, alerts.md UNTOUCHED - no fills, no thesis, no incidents, and routine 4 is not the author of the last three.)
week_of: 2026-10-12
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

## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on fifty times.** **Everything below is LIVE. Nothing live was
discarded; settled items were folded to one line each and repeated emphasis was removed.**
⚠ **A run that adds nothing to this list is the normal case.**
⚠ **A correction REPLACES the claim it corrects — it does not sit beside it.**

---

### Live — act on these

- **⚠ 2026-10-16 PRE-MARKET HANDOFF — WRITTEN BY THE 08:13 SEAT (SEAT 1 OF 4, THE THINKING SEAT, WHICH
  PLACES NO ORDERS), WHICH SPENDS THE 10-15 CLOSE HANDOFF IN FULL.**
  *(That item is **REPLACED, not kept beside this one.** Where its pieces went: the 10-15 official close
  basis (**709.37**), the four-seat §5 table, the 16:16 broker mark and the fifth price-gap sample are
  **settled in the dated 10-15 `sell_rule_status` digest in `positions.md`**, which is where dated
  material belongs · the §2 no-rebalance call for 10-16 is **re-derived below from this seat's own
  reading, not inherited** · the clock-signature, price-gap, staleness-gate, counter and corpus warnings
  sit in **the standing items that own them**, not here. **Nothing live discarded.**)*

  ⚠⚠ **THE RUN'S HEADLINE: EVERY §6 AND §7 GATE WAS OPEN AND NOTHING WAS BOUGHT.** Breaker **INACTIVE**
  · `new_positions_this_week` **0 of 3** · satellite sleeve **entirely undeployed with $30,000 idle** ·
  `TRADING_ENABLED: true` · `control.md` **Notes empty** · **zero open alerts** · **zero non-terminal
  orders.** **Five theses written (`T-2026-10-16-01` … `-05`), ALL FIVE REJECTED.** ⚠ **NOTHING
  PREVENTED A BUY THIS MORNING EXCEPT THE RESEARCH NOT FINDING ONE. THAT IS §4 WORKING, NOT §6 — and
  the two are indistinguishable in a zero-order run unless someone writes down which one it was.**

  **SELFTEST 5/5**, broker equity **$100,397.17** at pre-flight. `clock` **08:13:02**, `is_open: false`,
  **both** `next_open` **2026-10-16T09:30** and `next_close` **2026-10-16T16:00** carrying **today's**
  date — the **pre-market full-session signature, read off the DATES. Not a holiday.**

  **LIVE BROKER MARK 08:13 — ONE SERIES, NEVER DIFFERENCED AGAINST THE OFFICIAL BASIS.** `sleeves`
  equity **$100,397.17** · core **$70,397.165707 / 70.12%** · cash **$30,000.00 exactly / 29.88%** ·
  satellite **0.0%, `count 0`** · `core_in_band: true` · `rebalance_needed: false` ·
  `core_target_value` **$70,278.02** · `rebalance_delta` **−$119.15**. `positions`: one row, **VOO**
  99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999**, `market_value` **$70,397.165707**,
  `unrealized_pl` **+$397.175708 / +0.567%**, `current_price` **710.75**, `lastday_price` **709.43**.
  ⚠ **`current_price` 710.75 IS A PRE-MARKET INDICATIVE MARK, NOT A CLOSE.** ⚠⚠ **`lastday_price`
  709.43 IS NOT THE OFFICIAL 10-15 CLOSE OF 709.37 — a +$0.06 gap, so `change_today` 0.00186 and
  `unrealized_intraday_pl` +$130.74113 are BROKER-MIDPOINT FIGURES, NOT OFFICIAL-BASIS DAY FIGURES.
  SIX CENTS IS THE DANGEROUS SAMPLE, NOT THE REASSURING ONE — at that distance the two numbers look
  interchangeable, which is exactly when a run reaches for whichever is at hand. THE RULE DOES NOT
  RELAX AS THE GAP NARROWS.** ⚠ **This is a PRE-market sample and the five catalogued samples are all
  POST-bell; it is NOT a sixth member of that series and was not added to it.**

  ⚠⚠ **§2 — NO REBALANCE DUE, AND `rebalance_delta` HAS NOW MIS-INSTRUCTED FOUR TIMES RUNNING.** Core
  **70.12%**, **4.88 points of headroom at the UPPER edge, 5.12 at the lower.** The delta series:
  **+$73.15 (10-15 09:37) → −$21.89 (12:41) → −$76.96 (16:16) → −$119.15 (10-16 08:13)**, a **new
  extreme**, against core **69.96% → 69.93% → 70.02% → 70.08% → 70.12% — NEVER ONCE NEAR A BAND EDGE.**
  ⚠ **A run reading only the delta has been told "buy VOO", "sell VOO", "sell more", "sell more still",
  on ONE UNCHANGED POSITION ACROSS TWO SESSIONS. The counter-example is now four readings long and
  spans a session boundary, which is STRONGER than four readings inside one day. §2 TRIGGERS ON THE
  BAND AND NOTHING ELSE; §2's call belongs to the market-open seat.**

  **§5.1–5.4 REACHED IN ORDER AND FOUND EMPTY — RE-EVALUATED AT THIS SEAT, NOT INHERITED.** Core VOO
  struck before any rule was read, per §5's exemption. ⚠ **DISTANCE IS UNDEFINED, NOT LARGE.** ⚠ **The
  §5.1 Perplexity invalidation check cost ZERO queries and that is STRUCTURAL — it costs one query PER
  OPEN POSITION and there are none.** **LEDGER RECONCILED, THREE SIDES AGREEING, AS THIS RUN'S FIRST
  JOB:** `positions.md` zero satellite blocks · `positions` one core row, **unchanged since 2026-09-03
  (33 sessions)** · `sleeves` `satellite.count: 0`.

  ⚠⚠ **THE RUN'S OWN NEAR-MISS, AND IT WAS *CONSTRUCTED BY ME*, NOT SERVED BY A SOURCE — `T-2026-10-16-02`.**
  **J.B. Hunt** printed Q3 **revenue $3.68B, +20%**, with **record intermodal volumes +8%**, and the
  chain *"freight is strong → buy a railroad"* assembled itself in ONE STEP before any source was
  asked. ⚠ **It dies three ways: part 1 (a customer's quarterly results are NOT a new transaction with
  its suppliers — the haulage arrangement is ongoing and unchanged), rule (iii) (RAIL VOLUMES ARE THE
  RAILROADS' OWN WEEKLY PUBLIC DISCLOSURE via the AAR, so the read-through is not early, it is public
  and a week late), and part 2 (JBHT's intermodal haulage runs over BNSF, which is NOT SEPARATELY
  BUYABLE — it sits inside BRK at a single-digit share of revenue, under §4's 10% floor).**
  ⚠ **THE BNSF/BRK SHARE WAS **NOT SOURCED THIS RUN** AND IS RECORDED AS A CORROBORATING ESTIMATE, NOT
  AS THE KILL. THE KILL IS PART 1.** ⚠⚠ **This is the honest-broker failure §4 describes, arriving in
  its most ordinary costume: a strong customer earnings print makes its suppliers look like a
  discovery. The 10-15 carry-forward predicted the read-across would arrive and it did.**

  ⚠⚠ **NEW RULE (v) COSTUME, AND IT IS THE MOST FILLABLE BLANK THIS FUNNEL HAS EVER PRODUCED —
  `T-2026-10-16-01`.** Taiwan's MOEA plans US AI-supply-chain industrial parks, **first one in Texas at
  up to $4B**, each park **$2–4B**, **funded by unnamed private businesses and raised by a NAMED TRADE
  ASSOCIATION (TEEMA)**. ⚠ **Source, verbatim: the plan *"does not identify any company as having
  signed, committed to, or been contractually named as a participant"*, and *"Nvidia, TSMC, and Foxconn
  had made no commitment."* No city, no site, NO CONSTRUCTION START DATE — part 3 kills it in one step
  (rule (vi)). The $4B is a PROJECT-LEVEL ESTIMATE attributable to nobody (rule (viii)).**
  ⚠⚠ **WHY IT IS WORSE THAN AN UNNAMED SUPPLY BASE: THE BLANK COMES WITH A LOOKUPABLE MEMBERSHIP
  ROSTER. TEEMA's members are published and many are listed, so a run can build a candidate list in one
  search and FEEL IT HAS BEEN SOURCED. A ROSTER IS A LIST OF COMPANIES THAT *COULD* PARTICIPATE; IT IS
  NOT A TRANSACTION, AND THE DISTANCE BETWEEN THE TWO IS THE WHOLE OF §4.** ⚠ **The priors arrive
  unbidden — Texas industrial REITs, ETN/EMR/PWR/VRT, E&C — and NOT ONE is named in the source.**

  ⚠⚠ **ZERO `move` CALLS AND ZERO MARKET CAPS SOURCED — BOTH CORRECT, NEITHER AN OMISSION.** The funnel
  delivered **THREE US-listed names into part 1 — `JBHT`, `AA`, `NVDA` (contextual) — the most it has
  ever delivered — and ALL THREE DIED AT PART 1**, upstream of both the priced-in filter and §3.
  ⚠ **A `move` would have been DECORATIVE (refusals 9, 10, 11) and so would sourcing a market cap: a §3
  figure exists to make an ACCEPTED thesis auditable and there is no accepted thesis.**
  ⚠⚠ **PROGRESSION, NOW FIVE SESSIONS: 10-12 ZERO eligible tickers at part 1 · 10-13 ONE · 10-14 TWO ·
  10-15 TWO · 10-16 THREE. THE BINDING CONSTRAINT SITS ABOVE THE PRICE CHECK, AND THE FUNNEL GETTING
  BETTER AT DELIVERING BIG ELIGIBLE TICKERS HAS BOUGHT NOTHING.**
  ⚠ **DO NOT INHERIT A §3 VERDICT FOR `JBHT`, `AA` OR `NVDA` — all three are UNRESOLVED, not passed and
  not failed (the VAL / GFS / VIR / HNRG precedent).**

  ⚠ **THE FIVE PRE-OPEN PRINTS (TRV · TFC · MTB · RF · CFG) LAND BETWEEN THIS SEAT AND THE 09:35 SEAT —
  `T-2026-10-16-04`, rule (iii) in its purest form. A SCHEDULED RELEASE IS NOT AN EVENT, and they are
  NOT carried as leads: five bank/insurer results are FIRST-ORDER and §4 buys Company B. If one
  discloses a named counterparty with a figure, that is Monday's window — not a licence to reason a
  position into existence at the moment of execution, which is the precise failure `plan_today.md`
  exists to prevent.**

  ⚠ **SEPTEMBER PPI (+1.3% m/m vs a 0.5% forecast) AND RETAIL SALES (+0.8% headline, +0.1% control
  group) HAVE NOW *PRINTED* AND NO NEW ID WAS MINTED** — same disposed object as `T-2026-10-12-05` and
  `T-2026-10-13-08`, following the 10-14 and 10-15 precedent exactly. **A CHANGE IN STATUS IS NOT A
  CHANGE IN ELIGIBILITY.** ⚠ **TSMC's Q3 print was RE-SERVED ONE DAY AFTER ITS DISPOSAL
  (`T-2026-10-15-01`) — the re-serve rate is now 4 FOR 4 SESSIONS.**

  **HOUSEKEEPING:** week anchor **RECOMPUTED FROM SOURCE** (America/New_York → 2026-10-16 Fri, ISO week
  42 weekday 5, Monday anchor **2026-10-12**) and **MATCHED** `week_of`, so `new_positions_this_week`
  was **NOT re-reset** and stands at **0 of 3 because nothing was opened** · nothing closed, so
  `consecutive_closed_losses` **0 UNTOUCHED rather than reset** · breaker INACTIVE and
  `halt_triggered_at: none`, so the `HALT_CLEARED_AT` comparison was **NOT DUE** and was not performed
  · no circuit-breaker alert owed. **CORE VOO NOT STAMPED — 104th refusal, EASY grade: this seat made
  zero `bars` calls and held no official close of its own.** **Thesis count 161 → 166** (87 archived +
  79 live; ⚠ `grep -c '^### T-'` returns **80** because the template heading matches — **DO NOT "FIX"
  IT TO 167**). **Session count HELD at 32 / 29** — only a seat standing after the bell may count the
  day it is in, and this seat stands before it. **FILES:** `research_log.md` **APPENDED** (one survey
  block + five entries) · `plan_today.md` **OVERWRITTEN**, `plan_date: 2026-10-16`, **no BUY, no SELL,
  no REBALANCE, and therefore NO `revalidate` line — correct rather than omitted** · `positions.md`
  10-16 digest **ADDED and deliberately LEFT UNCOLLAPSED for the close seat** · `state.md` fenced block
  rewritten and this handoff **REPLACING** the 10-15 one. `trade_log.md`, `journal.md`,
  `weekly_review.md`, `alerts.md` **UNTOUCHED** — no fills, no incidents, and routine 1 authors none of
  the last three.

- **⚠⚠ GFS/TSMC CLEARED EVERY FILTER AND DIED ON THE *THESIS PARTS* — `T-2026-10-09-01`, STILL THE MOST
  INFORMATIVE REJECTION THIS LOG HAS PRODUCED.** *(Collapsed 2026-10-14 08:21: the item is SETTLED five
  sessions on, so the per-part arithmetic and the repair narrative are folded to the two killing numbers
  and the lessons that outlive it. Nothing live discarded; the full entry is `research_log.md`.)*
  GlobalFoundries' **own dated release, 2026-10-08**: GF will manufacture **silicon interposers** for
  **TSMC** (CoWoS) at **Malta, New York** — **$2B over an initial five-year term.** **WHAT IT CLEARED:**
  two named parties · an official company-issued release · a dollar figure attributed to the US-listed
  leg · no rule (iii) problem · `asset` returns us_equity/NASDAQ/tradable · **and `move` passed on BOTH
  bases, +1.48% over five sessions and +2.72% on the news day itself.**
  **IT DIED THREE TIMES OVER, BOTH KILLING NUMBERS OUT OF GF'S OWN RELEASE IN ONE STEP EACH:** **PART 3**
  — *"Volume production is expected to begin ramping … during the first half of 2028"*, **six quarters
  minimum** against §4's **two** · **PART 2** — $2B / 5yr ≈ **$400M/yr** on FY2025 revenue **$6.791B** =
  **5.89%**, under the 10% floor, ⚠ **and that is the MOST GENEROUS reading: GF assigned the deal to NO
  reporting segment, so the true share is not small, it is NOT CALCULABLE** · **PART 1** — **GFS IS THE
  HEADLINE NAME**, and the genuine second-order question returned a **verbatim denial**.
  ⚠ **§3's CAP IS *UNRESOLVED*, NOT PASSED — DO NOT INHERIT A §3 VERDICT FROM THIS ENTRY** (the VAL
  precedent). It never needed resolving.
  ⚠⚠ **THE LESSON THAT OUTLIVES IT, AND IT CUTS THE OTHER WAY FROM MOST OF THIS FILE: a clean
  one-sentence mechanism, a real transaction, a named counterparty and a stock that has not moved is the
  most buyable-looking object §4 can meet. THE RULES STOPPED IT; THE JUDGMENT DID NOT HAVE TO.** ⚠ **AMD
  (`T-2026-10-01-02`) did it first on 10-01 with the same primary kill — PART 3 killed both, so "first"
  was never the fact; the PATTERN is.**
  ⚠ **DO NOT REHABILITATE IT AT A DIFFERENT PRICE — it did not die on price, and neither the calendar nor
  the 5.89% moves with the quote. "But it has not run yet" is "but it went up" wearing a coat.** ⚠ **The
  pull was felt and refused at BOTH seats that could have acted (10-09 09:36, holding a live `buy` path
  with every §6 gate open and $30,000 idle, and 10-09 12:41) — both pulled no quote at all. DECLINING TO
  LOOK IS STRONGER THAN LOOKING AND RESISTING.**
  ⚠ **AND THE LESSON FROM ITS REPAIR — CATCH (24): a correction was published as "corrected in ALL THREE
  FILES" and there were FOUR. The defect was AN ENUMERATION THAT SOUNDED EXHAUSTIVE AND WAS NOT, and the
  harm is that it is SELF-CERTIFYING — it reads as closure and suppresses the next re-check. ⚠ NEVER
  WRITE A CORRECTION'S SCOPE AS A COUNT. `grep` the phrase repo-wide, then name the files it returned.**
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
  ⚠⚠ **2026-10-06 THROUGH 2026-10-15 WERE ALL COMPLETE SESSIONS — ALL FOUR SEATS RAN AND COMMITTED ON EACH,
  AND EACH DAY'S CLOSE SEAT IS THE ONE ENTITLED TO SAY SO ABOUT ITS OWN DAY, BECAUSE IT *IS* THE SEAT
  THAT WOULD HAVE BEEN MISSING.** ⚠⚠ **EIGHT IN A ROW IS NOT A FIX AND MUST NOT BE READ AS ONE:
  the failure mode is a run that never STARTS, so a session that completed is not evidence about the next
  one in either direction, and a RUN OF EIGHT is not evidence either. ⚠ Each added session makes the
  streak longer and the DETECTOR no closer to existing. Two of 32 close runs have vanished and THE DETECTION GAP IS UNCHANGED — there is still no
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
  **IT HAS NOW PAID FIVE CONSECUTIVE SESSIONS, AND WHAT IT PAYS IS *EXCLUSIONS WITH REASONS ATTACHED* —
  work the run would otherwise do itself, for ZERO follow-up queries:** 10-07 four qualifying against
  four self-excluded · 10-08 one against **NINE** · 10-09 one against **NINE** · **10-13 ONE against
  FOUR** (LS Electric/Bloom mis-excluded as *"both are non-US companies"* — ⚠ **the one time the funnel's
  own exclusion was WRONG, and the drill corrected it: Bloom Energy IS US-listed, which is how
  `T-2026-10-13-01` was reached at all. A self-exclusion is a HINT, NOT A RULING**) · **10-12 ZERO against
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
  ⚠ **The companion Monday shape stands with it: a CORRECT `plan_today.md` arrives THREE calendar days
  old on a Monday — COMPARE `plan_date` TO THE LAST TRADING DAY, NOT TO THE CALENDAR.** *(Collapsed
  2026-10-14 close: the standalone duplicate of this rule is removed; it said the same thing twice.)*
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
  ⚠⚠ **AND AS OF 10-14 THE 10-12 CALENDAR IS SPENT, WHICH IS THE OTHER HALF OF THE LESSON: the bank
  prints landed 10-13 and **SEPTEMBER CPI LANDS INSIDE THE 10-14 SESSION**, with PPI and retail sales
  10-15 and ASML/TSMC later.** ⚠ **A CHANGE IN STATUS IS NOT A CHANGE IN ELIGIBILITY: a macro print has
  ONE party and no transaction, so it is the government-action object whether it is scheduled, printing
  or printed.** ⚠ **The 10-14 seat declined to mint a third ID for it** — already disposed at
  `T-2026-10-12-05` and `T-2026-10-13-08`, and a third entry for one rejection would inflate the thesis
  count rather than record anything. **NOTE THE DATES AND DO NOTHING.**

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

- **⚠⚠ THE SATELLITE SLEEVE IS STRUCTURALLY UNDEPLOYED — **32 COMPLETED SESSIONS** (29 post-fill,
  advanced by the 10-15 **16:16** close seat, which stands after the bell on a session that is over),
  **166 THESES** (87 archived + 79 live headings; the **10-16** pre-market seat advanced this count by
  its five and HELD the session count, the opposite call to the close seat's and equally correct),
  ZERO POSITIONS EVER, AND THE PRESSURE TO LOWER THE §4 BAR IS THE ONLY ITEM HERE ASKING
  FOR JUDGMENT RATHER THAN CARE.** *(Collapsed 10-09 16:17: six retellings of the same counter trap folded
  to the rule. Nothing live discarded.)*
  ⚠⚠ **BOTH RESOLUTIONS HAPPENED ON 2026-10-12, IN OPPOSITE DIRECTIONS, AND THE PAIR IS THE CLEANEST
  WORKED EXAMPLE THIS ITEM WILL EVER GET.** The **08:36** pre-market seat advanced the THESIS count
  138 → 143 and **HELD** the session count at 28 / 25 (it stands BEFORE the bell, and 10-09 was already
  counted by its own close seat) — catch (21)'s shape for the EIGHTH time. The **16:17** close seat then
  advanced the SESSION count **28 / 25 → 29 / 26** and **HELD** the thesis count at 143 (the close
  routine writes no theses, and today's five were already written). ⚠ **ONE DAY, TWO COUNTERS, TWO
  OPPOSITE CALLS, BOTH CORRECT. DO NOT "FIX" 29 BACK TO 28 AND DO NOT "FIX" 143 TO 144.**
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

- **⚠⚠ THE FUNNEL KEEPS ANSWERING §4's QUESTION IN THE NEGATIVE, OUT LOUD — **FOURTEEN** CONSECUTIVE
  SESSIONS, 09-29 THROUGH 10-16 UNBROKEN, AND **10-16 IS THE FIFTH IN WHICH *EVERY* BROAD SCAN PRODUCED
  ONE — ALL THREE FRAMINGS, VERBATIM: *"no clearly documented US corporate announcement … with a
  confirmed cross-company operational effect"* · *"No company can be confirmed"* · *"No qualifying case
  can be identified from the available reports."*** ⚠⚠ **AND THE RE-SERVE RATE IS NOW 4 FOR 4 SESSIONS,
  WITH 10-16's RE-SERVE ONLY *ONE DAY* OLD: TSMC's Q3 print came back under a 10-16 dateline, disposed
  the previous session at `T-2026-10-15-01`.** ⚠ **10-15's form: *"no company can be confirmed as meeting all of the requested
  criteria."* Both framings asked, the STRUCTURAL one FIRST, the announcement date demanded inside
  every prompt — which is how Ocugen's 10-13 signing date and LS Electric's 10-13 original date
  arrived volunteered rather than hunted.** ⚠⚠ **AND THE RE-SERVE RATE IS NOW 3 SESSIONS FOR 3: 10-15
  re-served EnergyX/Trafigura (`T-2026-10-13-02`) and LS Electric/Bloom (`T-2026-10-13-01`,
  re-stamped 10-15 over a 10-13 announcement), both only TWO DAYS OLD. TREAT THE RE-SERVE AS THE
  DEFAULT, NOT THE EXCEPTION — reading the log before the tape cost one `grep` and saved two drills.**
  ⚠⚠ **10-14 ADDED A FORM THE ELEVEN BEFORE IT DID NOT HAVE, AND IT IS THE MOST USEFUL ONE YET: THE
  STRUCTURAL FRAMING RETURNED **SIX ITEMS AND SELF-EXCLUDED ALL SIX IN A TABLE, WITH A NAMED FAILURE
  AGAINST EACH** — *"no announcement can be confirmed as meeting all criteria simultaneously."* ⚠ **The
  earlier eleven volunteered an ABSENCE; this one volunteered an ADJUDICATION, which is strictly more
  work done for free.** Two of the six reasons were rule (iii) dates the source supplied unasked (Alpha
  Compute signed 10-09, FFAI 10-12). **The segment-quantification framing then added *"the evidence
  provided does not establish any US-listed company with market capitalization above $10 billion that
  satisfies all requested criteria."***
  ⚠⚠ **10-13 IS THE STRONGEST SINGLE INSTANCE ON RECORD AND IT TOOK ONE QUERY: four qualifying events
  returned, and *"No second publicly traded US company is named by the source as directly affected"*
  written out FOUR TIMES, once each for ENVX, BP, EQX and ARREF.** ⚠ **The segment-quantification framing
  added the sentence that matters most: *"the evidence provided supports **zero confirmed matches**,
  rather than a constructed list of likely candidates"* — THE SOURCE DECLINING TO MANUFACTURE CANDIDATES
  IN THE SAME BREATH IN WHICH §4's HONEST-BROKER PARAGRAPH WARNS ME NOT TO.** *(Collapsed 10-12 08:36: four sessions of verbatim denial quotes are folded to the
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
  ⚠⚠ **AND THE FOURTH STATE'S MOST INSTRUCTIVE FORM IS NOT "NO TICKER EXISTED" BUT "A TICKER EXISTED AND
  THE FUNNEL'S OWN STRUCTURE KILLED IT BEFORE PRICE COULD MATTER" — FOUR CONSECUTIVE PRE-MARKET SEATS,
  EACH ONE RUNG HIGHER.** *(Collapsed 2026-10-15 08:19: the 10-13 and 10-14 per-session narratives are
  folded to this one paragraph with 10-15 added. Nothing live discarded; the full entries are in
  `research_log.md`.)*
  **10-12** — no eligible ticker at all (four of five rejects carry NO ticker; a 13-item sweep died at
  §3). **10-13** — **ONE** eligible ticker: `BE`, a genuine NASDAQ name in a dated transaction with a
  figure to the cent, dead at **PART 1 because BE is the PAYER.** **10-14** — **TWO**: `HRL` (`asset` →
  `us_equity`/NYSE/tradable, pulled from source) is the headline name **and** the payer; `AMD` is a
  **named party**. **10-15** — **TWO AGAIN, AND THEY ARE THE WIDEST §3 MARGINS THIS FUNNEL HAS EVER
  DELIVERED:** `GEV` **~$250.31B** and `BKR` **~$56.0B**, both **named parties** to the Venture Global
  frame agreements and therefore the headline rather than Company B.
  ⚠⚠ **EVERY ONE OF THESE KILLS IS UPSTREAM OF THE FILTER, SO A `move` ON ANY OF THEM WOULD HAVE BEEN
  DECORATIVE — DECLINED EIGHT TIMES NOW** (SYNA 10-05, CEREBRAS 10-06, no-eligible-ticker 10-12, BE
  10-13, HRL 10-14, AMD 10-14, **GEV 10-15, BKR 10-15**). ⚠⚠ **THE PROGRESSION IS THE FINDING AND IT
  POINTS ONE WAY: CLEARING §3 BY A FACTOR OF TWENTY-FIVE BUYS NOTHING. THE BINDING CONSTRAINT SITS
  ABOVE THE PRICE CHECK, AND FOUR SESSIONS OF RISING MARKET CAPS DYING AT THE SAME RUNG IS EVIDENCE
  ABOUT WHERE THE STRATEGY ACTUALLY BITES.**

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
  **10-14's FIVE, and the two to read are `-01` and `-02`:** **LMT/Avio** merchant SRM capacity for ER
  GMLRS/PrSM, Avio disclosing *">$500M"* of US capacity investment (**§3 — `asset` returns 404 on AVIO,
  established not inherited**; part 1 — LMT is the headline name and the BUYER; part 2 — the figure is
  Avio's own CAPEX; **the 13th defence instance and the first killed by the beneficiary being NAMED AND
  FOREIGN**) · **AMD/Fermi credit support** (part 1 — AMD is a NAMED PARTY; part 2 — *"a figure for AMD
  is not disclosed"*; part 3 — the only figure is Fermi's revenue over FIFTEEN YEARS; **rule (viii)'s
  first GUARANTEE costume**) · **HRL/Brakebush $1.055B** (part 1 — headline name AND payer, seller
  private so **no Company B exists**; form five, the GEHC/Sofie shape; **§3 cap UNRESOLVED, do not
  inherit a verdict**) · **RTX USAF NWC *"up to $8B"*** (rule (iv), 5th appearance in 8 sessions; ZERO
  queries spent) · a **§3 / non-qualifying sweep of NINE** (Galderma/ZO **SIX-listed** · Chemring/Roke
  **LSE** + unnamed prime · Alpha Compute **$81.7M**, unnamed customer, signed 10-09 · FFR/FFAI
  microcaps · Aegis/Tristar **Indian** · Moreld/**Norwegian MoD** · BigBear.ai below floor with
  *"options and ceilings rather than earned revenue"* · **LS Electric/Bloom $138,458,284 — AN EXACT
  ONE-SESSION-OLD RE-SERVE of `T-2026-10-13-01`, same parties and figure to the cent, disposed on the
  LOG and not on the tape** · the macro complex incl. CPI).
  **10-13's EIGHT, and the one to read is `-01`:** **BE/LS Electric $138,458,284** switchgear order
  (part 1 — the one US-listed party is the **PAYER**; part 2 — **form five, capital paid OUT**; rule (v)
  — the data-centre owner is **an unnamed "major U.S. technology company"**, a NEW costume: an unnamed
  **CUSTOMER** with a map pin, a delivery schedule and a product spec) · **EnergyX/Trafigura** $2B
  lithium offtake (**§3 — both parties PRIVATE**; the structural framing's **second** false positive) ·
  **ENVX** prelim Q3 + $19M Korea (source denied any Company B; **$19M is JOINTLY UNSATISFIABLE**) ·
  **BP** $3–4.5B impairment (**mechanism points DOWN**, which §3 cannot express; the competitor flip is
  the shared-cause object and was NOT taken) · **EQX** South Railroad permits (**ounces not dollars**, no
  contractor named — form six) · **Technip Energies/HPCL** €250–500M (**§3 non-US**; a **BAND**; and
  **BACKLOG IS NOT SEGMENT REVENUE**, the source's own words) · a **§3 sweep of ELEVEN** (ARREF **OTC** ·
  Torm · Bachem · Aequs/Safran · IRCON · BEL · Hiteck/Visara *"up to"* · Bluejay/Toray · Saudi Steel
  Pipe/Aramco · Al-Yamamah · ADSB) · the **FORWARD CALENDAR** again (bank prints 10-13, CPI 10-14, PPI and
  retail sales 10-15, ASML/TSMC later in the week — **rule (iii) at its earliest possible failure point**).
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

- **⚠⚠ US DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE — FOURTEEN INSTANCES, AND AS OF 10-14
  THE RULE HAS **TWO** MECHANISMS, ONLY ONE OF WHICH BETTER QUESTIONS COULD EVER REACH.**
  ⚠⚠ **THE THIRTEENTH IS THE NEW DOOR: `T-2026-10-14-01`, LOCKHEED MARTIN / **AVIO S.p.A.** (announced
  2026-10-13 — access to Avio's **merchant solid-rocket-motor** capacity for **ER GMLRS / PrSM**, with
  Avio disclosing **">$500M"** of new **US** capacity investment). **IT IS THE FIRST INSTANCE WHERE THE
  TIER BELOW THE PRIME *IS* NAMED, THE FIGURE *IS* REAL AND DATED, AND THE KILL IS SIMPLY THAT THE
  BENEFICIARY IS NOT LISTED HERE** — `asset --symbol AVIO` returns **404**, established from source that
  run rather than inherited from Avio's 10-07 disposal (the GFS/VAL lesson). ⚠ **Mechanism one, the
  previous twelve: the tier below the prime is COMMERCIALLY CONFIDENTIAL — reachable by asking better
  questions, and the reason the catalogue exists. Mechanism two, this one: the tier below the prime is
  NAMED AND FOREIGN — unreachable by any question, because §3 is the binding constraint.**
  ⚠⚠ **AND ITS PRIOR POINTED THE WRONG WAY, WHICH IS WORTH MORE THAN THE INSTANCE: the reflex is the SRM
  tier (NOC/Orbital ATK, L3Harris/Aerojet), but Lockheed is buying *merchant Italian* capacity PRECISELY
  BECAUSE the US incumbents' capacity is constrained — so the honest read-across is NEGATIVE for them,
  §3 permits only the long side, and the "competitor loses relative standing" flip is the shared-cause
  object. NOT TAKEN. A prior that is wrong in SIGN is a new failure mode for this list, which has only
  ever recorded priors that were unnamed.**
  ⚠ **The FOURTEENTH is `T-2026-10-14-04`: RTX, *"up to $8B"* from the USAF Nuclear Weapons Center
  (10-13) — see rule (iv) below; ZERO queries spent.**
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

- **⚠⚠ THE BROKER/OFFICIAL PRICE GAP IS A MOVING LIVE MIDPOINT, NOT AN OFFSET — ON EVERY SERIES.**
  *(Collapsed 2026-10-14 08:21 — eleven per-sample narrations across four series are folded to the
  counts and the rules they establish. Nothing live discarded; the samples are in git history.)*
  ⚠⚠ **NO FIXED OFFSET SURVIVES ON ANY SERIES AND NO DIRECTION IS READABLE.** **Post-bell: four
  samples, both signs, a twenty-two-fold spread** (10-02 at 16:16 **+$0.470** and at 16:46
  **−$0.0254** — same day, same official close, thirty minutes apart, a SIGN CHANGE; 10-06 **+$0.1207**;
  10-08 **+$0.57**). **Pre-market: three samples, both signs, a fourteen-fold spread** (10-05
  **−$0.22**, 10-06 **+$2.84**, 10-07 **−$3.0487**). ⚠ **"It is roughly X" is unavailable in either
  direction on both.**
  ⚠ **FOUR SERIES EXIST — post-bell broker/official, pre-market, the intraday live mark (10-05 09:36,
  708.33) and `positions.current_price` against the live quote plane — AND NONE MAY BE CONCATENATED.**
  ⚠⚠ **THE RULES, WHICH ARE WHAT SURVIVES THE SAMPLES:** **NEVER** difference a broker mark against an
  official close · **NEVER** use `equity − last_equity` as a day's P&L (fully attributed:
  `last_equity` = qty × `lastday_price` + cash, reconfirmed to the cent on 10-06) · **NEVER**
  `unrealized_intraday_pl` or `change_today` · **close-to-close from `bars` on a COMPLETED session,
  adjustment STATED, for the record; a fresh `quote` for execution.** ⚠ **An equity figure is
  meaningless without its CALL and its TIMESTAMP — one 10-06 morning read $100,848.82, $100,842.87,
  $100,838.91 and $100,842.87 for the same quantity.** ⚠⚠ **AND TWO CALLS AGREEING IS NOT A
  CALIBRATION: `sleeves` and `account` agreed to the cent on 10-06, `sleeves` and `selftest` agreed to
  the cent on 10-13 AND AGAIN ON 10-14 — three agreements and they validate nothing, being samples of a
  moving mark that happened to coincide.**
  ⚠ **`lastday_price` IS THE EXCEPTION AND MUST BE KEPT OUT OF THE MOVING-MIDPOINT CLAIM: it read
  714.34 at ALL FOUR SEATS of 10-08, byte-identical end to end across a complete session, while
  `current_price` moved 716.29 → 712.28. WITHIN a session it is a FIXED PRIOR-DAY FIELD — but it still
  disagrees with the official close by an unpredictable amount (−$0.09 on 10-06, −$0.32 on 10-08,
  **+$0.12 on 10-14**) and still must NEVER be differenced against one.**
  ⚠ **Do NOT re-open WHY it differs — four mechanisms falsified, both signs observed. STOP PREDICTING
  IT.** ⚠ **This bites §6's 5% cap, computed against LIVE equity ($5,050.36 on the 10-14 pre-bell
  mark). It has no operand only because no plan has ever carried a buy intent.**

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
  THE CLOCK, READ OFF `next_open`'s DATE, IS THE *ONLY* MARKET-STATE DISCRIMINATOR LEFT STANDING.**
  *(Collapsed 2026-10-14 08:21 — the item is SETTLED and both corroborants are RETIRED, so twelve
  per-instance narrations are folded to the rule, the counts, and the ONE live exposure. Nothing live
  discarded; the full observations are in git history.)*
  ⚠ **THE PRICE HALF IS CONFIRMED AND IS THE DANGEROUS HALF: A PARTIAL BAR'S `c` IS THE LAST TRADE SO
  FAR WEARING A CLOSE'S CLOTHES** — a plausible price carrying no warning (10-01 12:41, `c` 700.35 =
  `latestTrade.p` to the cent; **10-06 09:36 is the extreme case: a bar dated 2026-10-06 with `n` 156 /
  `v` 2,029 — six minutes of a session in a complete bar's shape**). ⚠ **NO `bars` CLOSE MAY BE STAMPED
  AS A MARK BEFORE THE BELL ON ANY BASIS.**
  ⚠⚠ **BOTH CORROBORANTS FAILED ON A *COMPLETE* BAR AND ARE RETIRED, NOT DOWNGRADED.** The `n`/`v`
  FLOOR test got a demonstrated false positive on 2026-10-07 (**n 1,323 / v 23,415**, below every
  trailing floor, on a session the clock proved complete). The `latestTrade`-MATCHING leg failed the
  same session (714.53 at 16:00:52 against the daily `c` **714.66**, the minute bar agreeing with the
  TRADE). ⚠ **A corroborant that disagrees with a correct close is worse than no corroborant.**
  ⚠ **`n`/`v` SOMETIMES DRIFT ON A COMPLETE BAR AND SOMETIMES DO NOT — six instances, both outcomes,
  including a drift across a shut market (10-06's bar read 3,734/86,983 then 3,735/86,985) and a
  weekend with no drift at all. A FIELD THAT SOMETIMES MOVES ON A BAR THAT CANNOT HAVE CHANGED IS
  UNUSABLE AS EVIDENCE IN EITHER DIRECTION.**
  ⚠ **`is_open: false` HAS THREE MEANINGS — pre-market, post-bell, holiday. READ `next_open`'s DATE.
  `is_open: true` is the one case the boolean alone is sufficient.** ⚠ **10-06 is the clean worked pair
  73 minutes apart: no bar dated today at 08:23, a bar dated today at 09:36, the clock moving in step
  both times — which corroborates the DISCRIMINATOR, not any bar's completeness.**
  ⚠⚠ **THE ONE LIVE EXPOSURE, AND IT IS OPEN ITEM (12) FOR THE HUMAN: ROUTINE 2's STEP 6 INSTRUCTS
  `bars --days 1` TO CAPTURE `voo_close_at_entry` AT 09:35, WHERE IT WILL MEET THE PARTIAL FORM EVERY
  TIME — stamping a minutes-old partial `c` into the §1 baseline of a position that might be held for
  months.** ⚠ **It has cost nothing only because no position has ever been opened: LUCK, NOT DESIGN.**
  **The sound substitute is the PRIOR completed session's close (`prevDailyBar`, or `bars --days 2`
  taking the dated-yesterday row), named on its basis — or defer the label to the close run. A
  PROMPT-LEVEL FIX, NOT THE AGENT'S TO MAKE.**

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
  **§5.1–§5.4 have never had an operand: 32 completed sessions since 2026-09-01, 29 post-fill, zero
  satellite positions ever.**
  ⚠⚠ **ADVANCED 28/25 → 29/26 BY THE 10-12 **16:17** CLOSE SEAT, WHICH MAY DO SO BECAUSE IT STANDS AFTER
  THE BELL ON A SESSION THAT IS OVER (`clock` 16:17:05, `is_open: false`, `next_open` AND `next_close`
  both dated 2026-10-13). The 08:36, 09:37 and 12:42 seats all correctly HELD it at 28/25 — right at
  those seats, superseded now rather than contradicted.** ⚠ **The 08:36 seat is the one catch (22) names
  as exposed, so its hold was deliberate.** ⚠ **It also RE-DATED the
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

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — TWENTY-SIX CATCHES, AND THEY KEEP CHANGING
  SHAPE.** ⚠⚠ **THE HEADER READ "TWENTY-THREE" WHILE (24) AND (25) WERE ALREADY WRITTEN BELOW IT, AND
  (26) LANDED TODAY — RECOUNTED FROM THE LIST AND CORRECTED 2026-10-15. THAT IS CATCH (19)'s OWN SHAPE
  RECURRING INSIDE THE CATCH SECTION FOR THE SECOND TIME: THE HEADER IS THE ONE LINE NOBODY
  RECOMPUTES, BECAUSE THE ITEMS BELOW IT ARE WHERE THE WORK IS. COUNT THE LIST.**
  ⚠⚠ **(26) A FALSE SUPERLATIVE AND A WRONG DERIVED SPREAD, MANUFACTURED BY A RUN ABOUT ITS OWN FRESH
  OBSERVATION, WITH THE REFUTING NUMBERS IN THE SAME SENTENCE — CAUGHT BEFORE PUBLICATION.** The 10-15
  16:16 close seat drafted the day's broker/official price gap (**−$0.04**) into `positions.md` as
  *"the SMALLEST yet"* with a *"FOURTEEN-FOLD"* sample spread. **Both false: 10-02 16:46's −$0.0254 is
  smaller, and the spread across the five samples is TWENTY-TWO-FOLD (0.0254 → 0.57) — and all four
  prior samples were listed in the same sentence.** **Corrected in file to SECOND-smallest and
  twenty-two-fold.** ⚠ **Catch (13)'s shape (a superlative is a claim about a whole series) crossed
  with catch (20)'s (a derived number sitting next to its own inputs); recomputing cost one line.**
  ⚠⚠ **IT IS THE THIRD INSTANCE OF (23)'s DIRECTION — NOT INHERITED, MANUFACTURED, ABOUT THE RUN'S OWN
  WORK, IN THE SAME BREATH AS DOING IT.** ⚠ **AND CUTTING IT DOWN LEFT A REAL FINDING BEHIND, AS (23)
  SAID IT USUALLY DOES: FOUR CENTS IS THE *DANGEROUS* SAMPLE, NOT THE REASSURING ONE — at that distance
  the broker mark and the official close look interchangeable, which is exactly when a run reaches for
  whichever is at hand.**
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

- **⚠ GNRC IS NOT YOURS TO LOOK AT — 41 CONSECUTIVE REFUSALS, AND THE COUNT DOES LESS WORK THAN IT
  LOOKS.** GNRC is the named counterparty in the Amazon announcement — **first-order, outside §4 at any
  price.** ⚠⚠ **GRADE EACH REFUSAL, DO NOT COUNT THEM: a midday seat is exits-only, a close seat does
  not trade, a weekly seat has no funnel — those refusals are FREE and some were STRUCTURALLY
  UNAVAILABLE TO VIOLATE.** The STRONG instances are PRE-MARKET seats, where a funnel exists and GNRC
  is reachable — **10-05 and 10-06 are both of those, and GNRC appeared in none of the seven scans
  across the two.** **No new costume in fourteen sessions — converging, not growing. FREE IS NOT THE
  SAME AS PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — 104 RUNS, AND THE *GRADE* IS THE POINT, NOT
  THE COUNT.** *(Collapsed 10-12 09:37: the per-seat grading narrative for 10-05 through 10-12 08:36 is
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

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — NOTE THE BASIS ON EVERY ONE.** *(Collapsed
  2026-10-14 08:21: the stale 10-09/10-12 readings are REPLACED by the current pair rather than kept
  beside them — a superseded live mark is not a durable fact — and the duplicated price-gap narration is
  removed, because the item above now owns it. Nothing live discarded.)*
  Core is **99.046311231 shares at 706.74 (a RAW print)**, cash **$30,000.00** flat, cost_basis
  **$69,999.989999**. **Unchanged since 2026-09-03, the only fill in this account's history.**
  **OFFICIAL CLOSE BASIS, THE LATEST COMPLETED SESSION — 2026-10-15** (`bars --adjustment all`, pulled
  by the 10-15 **16:16** close seat; ⚠ **a second `--adjustment raw` pull returned the IDENTICAL row for
  both 10-14 and 10-15, so the basis was non-decisive — recorded anyway, because the next ex-date
  restores the trap**): o **704.34** h **710.32** l **702.965** **c 709.37**, n **1,796** v **41,161**,
  vw **706.291079** — **up $1.93 / +0.2728%** on 10-14's **707.44**.
  ⚠ **THE TWO SESSIONS BEFORE IT, ON THE SAME BASIS AND THE SAME PULL, BECAUSE THE PAIR IS THE CONTEXT:
  10-13 c **715.08**, 10-14 c **707.44 (−$7.64 / −1.068%, the largest single-session fall in this
  record)**. 10-15 recovered **$1.93 of it.**** ⚠⚠ **AND THE INTRASESSION SHAPE, WHICH THE CLOSE ALONE
  HIDES: 10-15 OPENED AT 704.34, $3.10 BELOW THE PRIOR CLOSE, FELL TO 702.965 (−0.63%), AND CLOSED
  +0.2728% — A +0.91% ROUND TRIP OFF THE LOW IN ONE SESSION, on the day PPI and retail sales printed.**
  **BOOK ON THAT BASIS:** equity **$100,260.4818**, core **$70,260.4818 = 70.0779%**, cash **29.9221%**;
  day **+$191.1594 / +0.1910%**; **since inception +0.2605%**; excess **−0.0818pp**, ⚠ **which is the
  algebraic identity `(w − 1) × VOO_return` at `w` = 0.700208 and measures nothing.**
  **LIVE BROKER MARK, 2026-10-15 16:16 (A DIFFERENT SERIES, NEVER CONCATENATED WITH THE ABOVE):**
  `sleeves` equity **$100,256.52**, core **$70,256.519945 = 70.08%**, cash **29.92%**,
  `rebalance_delta` **−$76.96**, `core_in_band: true`, `rebalance_needed: false`. `positions`:
  `current_price` **709.33**, `lastday_price` **707.43**, unrealized **+$256.529946 (+0.366%)**.
  ⚠ **`current_price` 709.33 vs the official 709.37 is the FIFTH post-bell price-gap sample at
  −$0.04 — second-smallest of five, spread twenty-two-fold, both signs. `lastday_price` 707.43 is
  STILL not the official 10-14 close 707.44.**
  ⚠ **§6's 5% cap on this live mark is **$5,012.83**, and it must be RE-COMPUTED at the seat that uses
  it. It has no operand only because no plan has ever carried a buy intent.**
  ⚠ **DO NOT CARRY A CORE-WEIGHT *RANGE*: 10-06 repaired one at 08:22 and refuted the repair at 12:42,
  four hours apart inside one session. A range over a live moving mark goes stale by construction. §2
  never needed it — STATE THE LIVE READING AND THE TWO EDGES (10-15 16:16: 70.08%, passing by 5.08 and 4.92).**
  ⚠ **`is_open: false` HAS THREE MEANINGS — pre-market, post-bell, holiday. READ `next_open`'s DATE.
  `is_open: true` is the one case the boolean alone is sufficient.** ⚠ **THE NEXT `next_open` LINE TO BE
  SPENT IS FRIDAY 2026-10-16 — an ordinary overnight gap, so tomorrow's pre-market `plan_date`
  comparison reads ONE trading day and ONE calendar day.** ⚠ **2026-10-16 IS A FRIDAY: routine 5's
  weekly review stands that day, and the month is not over, so no archive rollover is due.**

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
  commit and no alert; 09-28 was the first instance. **Two of 31 close runs have now vanished; 10-06 through 10-14 all executed — NINE IN A ROW, WHICH IS NOT A FIX AND MUST NOT BE READ AS ONE.**
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
  **(3)** the structurally undeployed sleeve — **156 theses over 31 completed sessions, zero accepted, ~$30,000 in cash since inception.**
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
  ⚠⚠ **MEASURED AS A *TREND* FOR THE FIRST TIME AT THE 2026-10-15 PRE-MARKET SEAT — FROM `git show` ON
  PAST COMMITS RATHER THAN FROM A SINGLE SNAPSHOT — AND THE ANSWER IS THAT ITEM (9) IS NOT HOLDING.**
  The four files every run must read in full (`state.md` + `positions.md` + `research_log.md` +
  `journal.md`) measured, as-of each date: **10-08 378,205B → 10-10 428,373B → 10-12 449,725B → 10-14
  515,427B.** ⚠⚠ **THAT IS ~+23KB PER SESSION, +36% IN SIX SESSIONS, AND THE PER-SESSION INCREMENT IS
  RISING (+50KB, +21KB, +66KB across the three intervals) — NOT A PLATEAU AND NOT A CURVE BENDING.**
  Plus `weekly_review.md` **234,838B**, `plan_today.md` ~**18KB**, `trade_log.md` **4,573B**,
  `alerts.md` **2,632B**. ⚠ **PREVIOUS RUNS ASSERTED THIS QUALITATIVELY AND SOME ASSERTED IMPROVEMENT
  FROM A SINGLE FILE SHRINKING. A ONE-FILE SNAPSHOT CANNOT SEE A FOUR-SEAT TREND, WHICH IS WHY THE
  COLLAPSE DEMONSTRATIONS READ AS PROGRESS AND THE MEASURED SERIES DOES NOT.**
  ⚠⚠ **AND THIS SEAT ADDED TO IT, MEASURED AND REPORTED RATHER THAN OMITTED.** ⚠ **Quoted on the THREE
  files that are not this one, because a byte count of `state.md` written inside `state.md` falsifies
  itself as it is typed (see the next line): `positions.md` + `research_log.md` + `journal.md` went
  **387,881B → 411,342B, +23,461B FROM ONE SEAT**, of which **~+20.8KB is `research_log.md`** — five
  rejections whose value IS their reasoning. **`state.md`'s own delta is in `git diff --stat` on this
  commit**; it grew by roughly the same ~+2.5KB *after* collapsing the 10-14 handoff (−1.3KB), the
  priced-in narratives and the item-(9) body, because the two new standing-rule findings cost more than
  the three collapses saved. ⚠ **THE HONEST STATEMENT IS THAT COLLAPSING WORKS AND IS TOO SMALL: three
  collapses netted roughly −2KB against +3.7KB of genuinely new findings, and that is before the other
  three seats write today.** ⚠⚠ **THE TRADE-OFF IS NOW EXPLICIT AND IT IS THE HUMAN'S TO SETTLE, NOT A
  DISCIPLINE PROBLEM A SEAT CAN SOLVE: on a no-trade day the only thing of value a run produces IS the
  rejection reasoning, and the rejection reasoning IS the growth. A cap that bites would have to either
  bound `research_log.md` per-entry, pull the monthly rollover forward, or accept that the corpus is
  write-only beyond some date.**
  ⚠ ⚠ **`state.md`'s own byte count is deliberately NOT quoted here: a file-size claim
  inside the file it measures is self-referential and falsifies itself as it is written. It is in
  `git diff --stat` on each commit and in the close run's `journal.md` entry, which are the only places
  it is stable.**
  ⚠⚠ **THE TWO FASTEST-GROWING FILES ARE THE TWO WITH NO ARCHIVABLE UNIT PLUS THE ONE WHOSE GROWTH IS
  ITS VALUE: `weekly_review.md` (largest in the corpus, written by one seat a week, no month boundary)
  and `state.md` (no month boundary, rewritten in full every run), with `research_log.md` the fastest
  per-run and growing FASTEST ON A NO-TRADE DAY — a rejection's value IS its reasoning and the
  reasoning is the bytes. It is now ~200KB against September's whole 87-thesis archive, and the monthly
  rollover is the only mechanism that reaches it.**
  ⚠⚠ **AND THE 10-14 CLOSE SEAT IS THE FIRST COUNTEREXAMPLE TO "NO SEAT CAN SHRINK IT", WHICH IS WHY IT
  IS RECORDED AS A DEMONSTRATION AND NOT A FIX: it collapsed `positions.md`'s 176-line three-seat 10-14
  digest into a shorter FOUR-seat one (**96,566B → 94,318B**) and rewrote this file smaller than it
  found it, discarding nothing live. ⚠ ONE SEAT COLLAPSING ONCE A DAY CANNOT OUTRUN FOUR SEATS
  APPENDING, and the saving is paid for out of the collapsing seat's own block. THE CAP ON WHAT A SEAT
  MAY APPEND WHEN THE NULL IS UNCHANGED IS STILL A RULE ONLY `control.md` OR THE ROUTINE PROMPTS CAN
  CARRY.**
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
⚠⚠ **NEW 10-15 AND IT IS A DEFECT IN *HOW THE TEST IS APPLIED*, NOT A NEW COSTUME: ONE RELEASE CAN
CARRY A GENUINE PASS AND A GENUINE FAIL ON TWO DIFFERENT FIGURES.** `T-2026-10-15-01` — TSMC's Q3 print
**RAISED** its own FY2026 USD revenue-growth outlook to **~44% from its own prior ~40%** (a clean rule
(iii) **PASS**, the prior figure present in the source) **and in the same release REITERATED FY2026
capex at US$60–64B — old range and new range IDENTICAL**, which is **reaffirmation, costume #1 on this
list.** ⚠⚠ **AND THE SIGNS ARE THE WRONG WAY ROUND FOR §4: THE FIGURE THAT MOVED (revenue) HAS NO
SUPPLIER CHAIN HANGING OFF IT, AND THE FIGURE WITH THE SUPPLIER CHAIN (capex) DID NOT MOVE.** So the
attempted mechanism — *"TSMC's raised outlook lifts AMAT/LRCX/KLA"* — is **contradicted by its own
source document** and needs an *"and also TSMC will eventually have to spend more"* to stand up.
⚠ **THE RULE: APPLY RULE (iii) TO THE FIGURE THE MECHANISM ACTUALLY RUNS ON, NOT TO THE RELEASE. A
reader who tests the release and stops at the first "yes" proceeds on the wrong number.** ⚠ *(Companion:
TSMC capex was disposed at `T-2026-10-05-05` ten days ago at the same $60–64B. **That the figure has not
moved IS the rule (iii) answer** — and it was RE-DERIVED from today's source, not inherited.)*
⚠ **The 10-15 sweep gave a clean PASS one line away, and it is a §3 kill: Antofagasta raised FY2026
cash-cost guidance to $2.60–2.70/lb from its OWN $2.40–2.60/lb — LSE-listed. A clean pass on one filter
is not progress toward a trade.**

**(iv)** *A recurring ticker is a warning, not corroboration* (LHX, and 10-02 added RTX for the second
time in five sessions and Venture Global for the second time). ⚠⚠ **VENTURE GLOBAL REACHED ITS THIRD
APPEARANCE ON 10-15 AND DIED ON PART 3 / RULE (vi) ALL THREE TIMES** (10-02 the ConocoPhillips 20-year
SPA with first delivery 2030; 10-15 the GEV/BKR frame agreements running to 2034). ⚠ **That is a fact
about its INDUSTRY'S CONTRACTING HORIZON — LNG and merchant power are STRUCTURALLY long-dated — not
about a candidate maturing. Expect this issuer again; the answer is already written.** ⚠⚠ **RTX IS NOW AT **FIVE APPEARANCES IN
EIGHT SESSIONS ACROSS FOUR DISTINCT AWARDS** (09-29 AMRAAM $20.7B · 10-02 SM-6 *"up to"* $24.4B · 10-09
SM-3 *"up to"* $6.3B · 10-12 the SM-3 award RE-SERVED TWICE IN ONE RUN · 10-14 USAF Nuclear Weapons
Center *"up to"* $8B) — AND IT DIED THE SAME DEATH EVERY TIME.** ⚠ **10-14 IS THE STRONGER FORM OF THE
WARNING, NOT THE WEAKER ONE: 10-12's re-serve could be dismissed as the funnel repeating itself, but the
10-14 award is genuinely new, genuinely large and genuinely dated and is STILL structurally dead. A
FRESH TRANSACTION IS NOT FRESH EVIDENCE WHEN THE KILL IS STRUCTURAL.** ⚠ **Both re-entered on a genuinely new
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
⚠⚠ **NEW 10-14 AND IT IS THE FIRST *GUARANTEE* ON THIS LIST: A CREDIT BACKSTOP.** `T-2026-10-14-02` —
**AMD** signed a **credit support agreement** standing behind **Fermi's** phase-one Project Matador lease
(222 MW, framework to 650 MW, announced 2026-10-13). ⚠⚠ **A BACKSTOP IS A CONTINGENT LIABILITY ASSUMED
BY THE BUYABLE LEG — THE OPPOSITE SIGN FROM REVENUE — AND IT READS AS A STRONG COMMERCIAL SIGNAL BECAUSE
THE MARKET PRICED *FERMI* UP ON IT.** ⚠ **The amount attributable to AMD is UNDISCLOSED (source: *"a
figure for AMD is not disclosed"*), and if it is ever quantified it appears as a RISK, not a sale.** ⚠ **The
only dollar figure in the story, ~$6.5B, is FERMI's expected revenue over a FIFTEEN-YEAR term — wrong
company and ~60 quarters.** ⚠ **Every other entry on this list is money that MOVED in the wrong direction
or belonged to the wrong party; this one is money that has not moved at all and may never.**
⚠⚠ **THE DEFINITIVE INSTANCE IS JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K — AND
IT IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A
disclosed statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.**
**THIS IS THE WORKED EXAMPLE TO REACH FOR FIRST.**
⚠⚠ **NEW 10-15 — A CONTINGENT AGGREGATE CEILING SPANNING MULTIPLE AGREEMENTS AND MULTIPLE RECIPIENTS,
AND IT IS THE LARGEST NUMBER THIS FUNNEL HAS EVER PRODUCED.** `T-2026-10-15-02` — Venture Global's
10-15 8-K announced *"power and grid frame agreements"* with **GE Vernova** and **Baker Hughes** for up
to **16 × 720 MW** power islands. **The announcement disclosed NO dollar value for that agreement and
NEITHER supplier stated a segment value.** The **~$17.2B** in circulation fails on **four counts at
once**: **CONDITIONAL** (*"if all contemplated purchase orders under both frame agreements are executed,
subject to adjustments"*) · **AGGREGATED ACROSS TWO FRAME AGREEMENTS PLUS GE Grid equipment**, i.e.
broader than the announced deal · **UNALLOCATED between the two buyable legs**, so neither has a figure
· and **PAID OUT BY VENTURE GLOBAL**, the non-candidate leg. ⚠ **It is rule (v)'s CEILING sub-shape
crossed with rule (viii)'s WRONG-PARTY shape, and its SCALE is the whole of its persuasive force.**
⚠⚠ **$17.2B split between two companies over nine years, contingent on orders nobody has placed, is not
a dollar path — it is a PRESS-RELEASE MAXIMUM.** ⚠ **A FRAME AGREEMENT IS NOT AN ORDER: the filing says
equipment is supplied *"once Venture Global elects to proceed with a particular order"*, and the
companion "Initial Unit Manufacturing Reservation Agreement" for eight units is explicitly **not** a
purchase order either.** ⚠ **Part 3 kills it independently and needed no query: first PO *"by end of
2026"*, reservation POs *"early 2027"*, power available **late 2028/early 2029**, delivery schedule
**through 2034** — ~8 to ~32 quarters against §4's TWO.**


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

**⚠⚠ MERGER ARBITRAGE IS NOT IN §4 — THREE DEALS IN TWO SESSIONS AND THE ANSWER NEEDS NO QUERY.** *(The duplicate of this item in **Live** was removed 2026-10-14 close — same content, two places. This is the copy to read; it belongs here, in recognise-on-sight.)*
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
