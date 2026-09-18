# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-18 09:36 ET 2-market-open-execution (selftest PASSED all five checks at 09:36 ET, trading_enabled true, LIVE paper, equity 99435.43 at pre-flight; MARKET OPEN AND CONFIRMED OPEN - clock is_open TRUE at 09:36:21 with next_close 2026-09-18T16:00 TODAY and next_open 2026-09-21T09:30 MONDAY, the INTRADAY shape and the ONLY one of the four run-shapes that needs no date to disambiguate, because is_open true is unambiguous where is_open false is shared by pre-market and post-bell; ⚠ STALENESS GATE CHECKED AND DID NOT FIRE - plan_date reads 2026-09-18 and today's ET date IS 2026-09-18, so the plan is FRESH and its emptiness IS the plan rather than a gap in it, which matters because a fresh empty plan and a stale plan produce IDENTICAL zero-order runs and the difference is invisible in the order count; TWENTY-FIRST consecutive non-firing, the alert path REMAINS UNTESTED CODE, and the first morning it fires will be a morning the pre-market run failed - i.e. exactly the morning with no fresh notes to lean on, so READ STEP 2 THEN, DO NOT RECALL IT; ZERO ORDERS PLACED OF ANY KIND - zero buys, zero sells, zero core, zero rebalance, and NOT ONE of them was blocked: the plan carried zero intents of all three kinds while breaker was INACTIVE, weekly cap 0 of 3, sleeve empty, 30.17% idle cash and control.md carried no restricting note - NOTHING PREVENTED A TRADE, THERE WAS SIMPLY NOTHING THE PLAN AUTHORISED; ledger reconciled - zero satellite blocks vs zero satellite Alpaca rows, they AGREE (satellite compared to satellite, never raw ledger to raw broker), one row VOO core 99.046311231 sh UNCHANGED since 09-03, avg_entry 706.74 cost_basis 69999.99 mv 69434.44 unrealized -565.55 / -0.808%; ⚠ SIXTH DOCUMENTED TWO-PRICE INSTANCE AND IT CARRIES A NEW SUB-SHAPE WORTH MORE THAN THE COUNT - lastday_price READ 701.03 AGAIN while 09-17's OFFICIAL close was 700.97, the SAME six cents as the 08:16 read, so the field corrected itself NEITHER overnight NOR at the bell; and current_price READ 701.03 TOO, with change_today EXACTLY 0, SIX MINUTES INTO A LIVE SESSION - that flat is an ARTIFACT of both fields carrying the same stale midpoint, NOT a measurement that VOO is unchanged, and a run reading change_today as the day's move here would have read ZERO on a moving tape; bars --adjustment all for a close, a fresh quote for execution, NEVER a positions field for either, and the field's NAME is not evidence about what it holds; STEP 3 CORE BOOTSTRAP SKIPPED PERMANENTLY - core_established true, the path is disabled for the life of the account and was not evaluated further; STEP 4 EXITS HAD NO SUBJECT - zero SELL intents and zero satellite positions, the 5.1-5.4 ordered evaluation never started, sell_rule_status ABSENT rather than blank, STILL THE TWENTIETH session with an empty sleeve because the count advances on SESSIONS not RUNS and this is the SECOND read of 09-18 (it is not a twenty-first), all four remain UNTESTED CODE PATHS, 5.4 STILL NOT ARMED because it arms on the first SATELLITE fill, loss streak UNMOVED at 0 because nothing has ever closed in this account, no HALT_CLEARED_AT comparison required, NO circuit-breaker alert due; STEP 5 RE-VALIDATION HAD NO SUBJECT - ZERO alpaca.py move calls and none due, an ABSENT check and not a skipped one, and open item (7) cost nothing again for precisely the reason it cost nothing yesterday: IT HAS NO SUBJECT, which is an absence of exposure and NOT a mitigation - the 09:35 re-validation inherits move's blindness to an after-hours event in full the moment one BUY intent exists; STEP 7 REBALANCE NOT DUE - sleeves equity 99434.44 cash 30000.00 core 69434.44 = 69.83% satellite 0.0% count 0 cash 30.17% core_in_band true rebalance_needed false rebalance_delta +169.67 = 0.17% of equity, SMALLER than the 08:16 read of +173.53, and §2 acts at the BAND EDGE 65/75 not at the target so the delta is not an action at any size inside the band, TWENTY-SIXTH consecutive run inside a 0.39-point range 69.59-69.98; orders --status all STILL RETURNS ONE ROW for the account's entire history (09-03 core VOO buy, filled, terminal), NOTHING IN LIMBO per §7, and no order from this run exists to resolve because none was placed, so trade_log.md was correctly left unappended; week rollover checked - ISO Monday of 2026-09-18 (Friday) is 2026-09-14 which MATCHES week_of, NO RESET DUE, next boundary Monday 2026-09-21; new_positions_this_week stays 0 of 3, open_thesis_ids stays none; NO RESEARCH AND NO THESIS WRITTEN - an execution run does not research, and a buy that was not researched before the bell does not get made after it, counter stays 46 since inception with 16 this week and 0 accepted, research_log.md correctly left unappended because the Step 5 skip log has a subject only when a BUY intent exists; ⚠ GNRC NOT LOOKED AT FOR THE FIFTH CONSECUTIVE RUN - zero move/quote/bars/asset calls, and the plan PREDICTED a fifth costume by name before this run started: the one actually available was "I am at the open with the data plane already in hand, one more symbol costs nothing", which is the CHEAPEST version yet and the first that would have been FREE rather than merely justifiable - REFUSED, and note that the excuses are getting better rather than worse, which is the finding; it remains the named counterparty in the Amazon announcement, first-order, outside §4 at any price, and it was not in the plan; TODAY IS FRIDAY - the weekly review runs after the close and owes the 09-21 pre-market run a written hand-off, and General Mills (~Sept 23 report) is still carried forward; alerts.md EMPTY, zero open, zero SYSTEMIC)

prior_run: 2026-09-18 08:16 ET 1-premarket-research (selftest PASSED all five checks at 08:15 ET, trading_enabled true, LIVE paper, equity 99426.51 at pre-flight; PRE-MARKET NOT A HOLIDAY - clock is_open FALSE at 08:16:15 with next_open 2026-09-18T09:30 TODAY and next_close 2026-09-18T16:00, the PRE-MARKET shape, and a pre-market run and a close run BOTH read is_open false so only the next_open DATE discriminates; TODAY IS FRIDAY, the weekly review runs after the close and owes the 09-21 pre-market run a written hand-off; ledger reconciled - zero satellite blocks vs zero satellite Alpaca rows, they AGREE, one row VOO core 99.046311231 sh UNCHANGED since 09-03, avg_entry 706.74 mv 69421.56 unrealized -578.43 / -0.826% change_today -0.019%; ⚠ lastday_price READ 701.03 WHILE YESTERDAY'S OFFICIAL CLOSE WAS 700.97 - six cents apart in a field NAMED for the prior day, the cleanest instance yet of the live-midpoint mechanism and the FIFTH documented, cosmetic on core and LOAD-BEARING the moment a satellite position exists; sleeves equity 99421.56 cash 30000.00 core 69421.56 = 69.83% satellite 0.0% count 0 cash 30.17% core_in_band true rebalance_needed false rebalance_delta +173.53 = 0.17% of equity, NO REBALANCE DUE AT TODAY'S OPEN (§2 acts at the BAND EDGE 65/75 not at the target), TWENTY-FIFTH consecutive run inside a 0.39-point range 69.59-69.98; week rollover checked - ISO Monday of 2026-09-18 (Friday) is 2026-09-14 MATCHES week_of, NO RESET DUE, next boundary Monday 2026-09-21; loss streak UNMOVED at 0 because nothing has ever closed, breaker INACTIVE, no HALT_CLEARED_AT comparison required, NO circuit-breaker alert due; 5.1-5.4 had NO SUBJECT and the ordered evaluation never started, sell_rule_status ABSENT rather than blank, ZERO perplexity invalidation queries and none due (an ABSENT check not a skipped one), TWENTIETH session with an empty sleeve (count advances on SESSIONS not RUNS, this is the first read of 09-18), all four remain UNTESTED CODE PATHS, 5.4 STILL NOT ARMED; CORE VOO DELIBERATELY NOT STAMPED and this run did not even HAVE the number - ZERO alpaca.py bars calls for any purpose, so unlike 09-16 and 09-17 no close was sitting in terminal output with nothing to do; NEW POSITIONS FULLY PERMITTED AND ZERO BUY INTENTS WRITTEN - breaker INACTIVE, cap 0 of 3, empty sleeve, 30.17% idle cash, no restricting note in control.md, NOTHING BLOCKED THE RESEARCH, the research did not produce an eligible candidate; FOUR THESES WRITTEN, FOUR REJECTED, counter now 46 since inception with 16 this week, 0 accepted - T-2026-09-18-01 GFS/MRVL (part 2 plus the §4 first-order premise), -02 LEU (part 3 then part 2), -03 no-ticker LEN read-across (part 1), -04 BLK (part 2); ⚠ HEADLINE - THREE NAMED-BOTH-PARTIES TRANSACTIONS IN ONE WINDOW AND ALL THREE WITHHELD THE NUMBER (GlobalFoundries↔Marvell SiGe Burlington VT, Centrus↔Antares HALEU, TotalEnergies↔GIP $1.8B), two saying 'financial terms were not disclosed' in so many words and the third disclosing capital IN rather than revenue, so part 2 could not be written for ANY of them - carry-forward item (3)'s FIRST binding form firing THREE TIMES IN ONE MORNING; ZERO alpaca.py move CALLS and none due - no candidate reached second-order ticker stage, GFS/MRVL/LEU/LEN are all signatories or the reporting company itself and screening the named party is running a filter on the WRONG company (rule i); GNRC NOT LOOKED AT FOR THE FOURTH CONSECUTIVE RUN - zero move/quote/bars/asset calls, and today's pull was the STRONGEST AND EMPTIEST yet because the 09-16 gap is NOW INSIDE bars so move would return a large positive number and priced_in true, WHICH WOULD BE THE FILTER WORKING CORRECTLY ONE SESSION LATE rather than a measurement of open item (7), already measured 09-17 - THERE IS NO NUMBER LEFT TO COLLECT, yesterday's costume was diligence and today's was completeness; plan_today.md rewritten with plan_date 2026-09-18 and ZERO intents of all three kinds; alerts.md EMPTY, zero open, zero SYSTEMIC)

week_of: 2026-09-14
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.83
satellite_pct: 0.0
cash_pct: 30.17
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
