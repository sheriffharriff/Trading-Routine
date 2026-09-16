# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-16 16:16 ET 4-market-close-journal (selftest PASSED all five checks at 16:16 ET, trading_enabled true, LIVE paper, equity 98658.80; THIS ROUTINE TRADES NOTHING AT ALL - zero orders, and the 30.41% idle cash it sees is NOT an opportunity it may act on; clock is_open FALSE at 16:16:10 with next_open 2026-09-17T09:30 TOMORROW - the POST-BELL shape, NOT a holiday, today supplied all four shapes (08:17 false/next_open TODAY, 09:35 true, 12:35 true, 16:16 false/next_open TOMORROW) and TWO of the four share one boolean and differ only in the next_open DATE - READ THE DATE NOT THE BOOLEAN, this routine's holiday branch triggers on exactly the flag it always sees; STEP 2 HIGH-WATER MARKS - NONE WRITTEN AND NONE WAS DUE, THIS IS STEP 2 COMPLETING NOT BEING SKIPPED: no satellite block exists so there is no highest_close to raise and no (as of ...) date to refresh, ABSENT is a THIRD STATE carrying NO DATE and that missing date is what tells TOMORROW'S MIDDAY RUN no backfill is due, ZERO bars calls issued for a high-water purpose (the VOO bars pulled priced the book and stamped nothing), CORE VOO DELIBERATELY NOT STAMPED and today the pull had an accomplice - its 693.215 close was already in the terminal output with nothing to do, writing it would FABRICATE a 5.4 stop on the one position 5 exempts and it would feel like TIDINESS not a violation, REFUSED; ledger reconciled - zero satellite blocks vs zero satellite Alpaca rows, they AGREE, one row VOO core 99.046311231 sh avg_entry 706.74 mv 68658.80 unrealized -1341.19 / -1.916%; broker current_price 693.199 is a LIVE QUOTE MIDPOINT not a close, official close today 693.215, same field read 698.88/698.08/698.41 earlier - FOUR READS ONE DAY FOUR NUMBERS, NEVER MIX SOURCES; DAY NUMBERS on OFFICIAL closes equity 98660.39, day -304.57 / -0.308%, since inception -1.340% (broker legs: 98658.80, -297.24 / -0.300%, -1.341% - DO NOT MIX LEGS); VOO closed 693.215 from 696.29 = -0.442% on an intraday range 689.095-699.99 (1.58% of the low vs 0.53% yesterday and 0.68% Monday) on higher volume; core tracking error 0.0000% (core -1.914% from the 706.74 fill, VOO -1.914% from the same price) - the 09-03 ENTRY GAP is the whole divergence, keep measuring from the fill; sleeves equity 98658.80 cash 30000.00 core 69.59% satellite 0.0% count 0 cash 30.41%, core_in_band true, rebalance_needed false, rebalance_delta +402.36 = 0.41% of equity, NO REBALANCE DUE TOMORROW (band edge 65/75, market-open run), TWENTIETH consecutive run inside a 0.39-point range 69.59-69.98 and today is the LOWEST of the twenty - a drifting mark on an unchanged share count, not a position being reduced; 5.1-5.4 NOT EVALUABLE, no subject, EIGHTEENTH consecutive session (count advances on SESSIONS not runs - today's four runs are ONE increment), all four remain UNTESTED CODE PATHS, 5.4 NOT ARMED; UNRESOLVED ORDERS CHECKED - orders --status all returns ONE ROW for the account's entire history, the 09-03 core VOO buy d177d8f0, status filled, terminal, NOTHING IN LIMBO OVERNIGHT (7); week rollover checked - ISO Monday of 2026-09-16 is 2026-09-14 MATCHES week_of, NO RESET DUE, next boundary Monday 2026-09-21; loss streak UNMOVED at 0 because nothing has ever closed, breaker INACTIVE, no HALT_CLEARED_AT comparison required, NO circuit-breaker alert due; open_thesis_ids stays none; NO RESEARCH AND NO THESIS - a journaling routine does not research, counter stays 39 with 9 this week; FOMC RESOLVED 14:00 ET - +25bp to 3.75-4.00%, UNANIMOUS 12-0, first US hike since 2023, another signalled this year, VERIFIED not inherited from the plan's >90% odds because a probability is not a fact - it is a PRICE MOVE NOT A THESIS and carries no action at any number; journal.md entry written, ClickUp daily summary 86bc1y9mr created; alerts.md EMPTY, zero open, zero SYSTEMIC)

prior_run: 2026-09-16 12:35 ET 3-midday-management (selftest PASSED at 12:35 ET, equity 99169.04; ZERO EXITS AND NONE WAS DUE - exits-only routine, may not open a position; clock is_open TRUE mid-session; ledger reconciled, zero satellite blocks vs zero satellite rows, they AGREE; sleeves core 69.75% cash 30.25%, core_in_band true, no rebalance due and this routine could not execute one anyway; STEP 2 NO BACKFILL DUE AND IT WAS READ NOT ASSUMED - no highest_close field at all, ABSENT not stale, ZERO bars calls; 5.1-5.4 NOT EVALUABLE, no subject, ZERO perplexity invalidation queries - an ABSENT check not a skipped one; week rollover checked, no reset; breaker INACTIVE, streak 0; no research, counter 39; alerts.md EMPTY)

week_of: 2026-09-14
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.59
satellite_pct: 0.0
cash_pct: 30.41
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

- **⚠ THE FUNNEL'S FAILURE MODE CHANGED TODAY AND THE NEW ONE IS WORSE — THIS IS THE HEADLINE OF
  09-16 AND IT REPLACES THE "WEEKEND EXCUSE IS SPENT" NOTE.** 09-14 and 09-15 both died on one shape:
  *"the source names the transaction and withholds the counterparty's number."* **Today the funnel
  finally cleared that obstacle.** T-2026-09-16-01 had a **named counterparty (Broadcom, Meta's MTIA
  design partner), a public program, and the counterparty discussing it on its OWN Q3 2026 earnings
  call.** **Part 1 PASSED — the first part-1 pass in three sessions.** **It died anyway**, because
  what a named counterparty publishes about a program is **roadmap and volume** — *"production
  shipments of their custom MTIA accelerator," "multiple generations of MTIA XPUs," "deliveries
  through 2027, gigawatt deployment through 2028"* — **and not segment revenue, which is the only
  thing §4.2 can use.** The one dollar figure in the whole result set, **"$20B+ 2026 AI revenue,"**
  is a **third-party blog's synthesis of Broadcom's TOTAL AI revenue**, not a Broadcom-quoted
  Meta-only number. **These are TWO DISTINCT DISCLOSURE FAILURES, not one, and a review that merges
  them will mis-diagnose what a human could actually change.** Widening the acceptable evidence for a
  *named* Company B would not have saved AVGO; nothing would have, short of Broadcom breaking out a
  customer.

- **⚠ NEW SUB-SHAPE OF STANDING RULE (v): A CEILING IS NOT REVENUE, AND THIS ONE WAS 212× THE CASH.**
  The Army's **M1 Abrams AGT1500 engine OTA** reads **$2,500,000,000** in every headline and carries
  **$11,831,430** of FY26 RDT&E actually obligated at award, completion **March 2029**. Every prior
  rule (v) instance was a **real award with a missing allocation**; **here the headline number is an
  authorization limit that may never be spent at all.** **Read the obligated figure, not the
  ceiling.** Seventh instance of rule (v) this month, and the first where **the trap is inside the
  number rather than beside it.** **Second costume on the same award: the awardee is the National
  Advanced Mobility Consortium — a CONSORTIUM, not a company — so there is no Company A to look past,
  let alone a Company B.**

- **⚠ I KNEW WHO MAKES THE ABRAMS ENGINE AND THE SOURCE DID NOT SAY IT — SECOND INSTANCE, FIRST ONE
  CAUGHT BEFORE A TICKER ENTERED THE FUNNEL.** The AGT1500 is a **Honeywell** engine. That fact
  arrived instantly, unbidden and **correct**, and would have written a fluent mechanism sentence.
  **A dedicated screen was run specifically to test it** and returned that **no reviewed source names
  Honeywell — or General Dynamics, or "others" — in connection with this OTA, and attaches no dollar
  figure to any of them.** **This is T-2026-09-01-03 (RTX) repeating exactly: a true industry fact
  volunteering itself as a sourced transaction.** T-2026-09-01-03 was caught *after* the ticker was
  screened in; this one was caught *before*. **HON was NOT screened and its filters were NOT run —
  absence of a source, not a verdict on the name.** **Knowing who makes the part is not knowing who
  was paid, and the gap between those two is invisible from the inside.**

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

- **⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED A SEVENTH TIME AND AGAIN COST NOTHING — KEEP THE TWO
  TALLIES SEPARATE.** Open item (1) — the §4 filter reading a **drawdown** as "priced in" — hit
  **AVGO −7.97%** (`priced_in: true`, *"LATE - skip"*). Instances now: **LITE −7.35%, LMT −3.61%
  near-miss, LHX −4.47%, CART −5.79%, BWXT −6.30%, CRWV −7.12%, AVGO −7.97%.** **The filter was
  applied exactly as written and AVGO was skipped; no run may reinterpret it — that is a human
  editing §4 or `alpaca.py move`.** **But AVGO was already dead at parts 2 AND 3 before the filter
  was consulted, so today adds an instance and ZERO damage.** **The expensive instances are the ones
  that reach the filter ALIVE, and LITE is still the only one** — it passed the four-part thesis, was
  killed by a drawdown, and is **+10.58% vs VOO** since. **A review that counts seven instances as
  seven costs will overstate the case for a change that is not the agent's to make.**

- **⚠ SIX ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) **The §4 priced-in filter
  reads a drawdown as priced-in** — **seven** instances, see above; **there is no price at which
  those rejections flip**, and LITE puts **+10.58% vs VOO** on the bill. (2) **The same filter reads
  an event move absorbed before it looks as "passes"** — QCOM (09-09, +2.70% after a +8.7% intraday
  move) and AVAV (09-11, +1.20% after a +12.9% intraday round-trip inside one session). Same root
  cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or `alpaca.py move`.**
  (3) The satellite sleeve is **structurally undeployed — THIRTY-NINE theses, zero positions,
  eighteen sessions**; a 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a
  rising market. **§2 permits the cash and §4 says most runs end in no trade — both rules were
  followed, and the agent must NOT respond by lowering the §4 bar.** **The binding constraint is now
  known to have TWO forms, not one** (see the headline note above): the source withholds the
  counterparty's number, **or** the counterparty is named, does disclose, and discloses **roadmap
  instead of segment revenue.** **09-15 removed the "thin news week" explanation; 09-16 removes the
  "no named counterparty" explanation.** **That points harder than before at something a human could
  change — widen the acceptable evidence for a named Company B, or accept the hit rate.** (4) The
  core's divergence from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the prior close),
  **not tracking error and never skill** — **DISCHARGED AND PROVEN 09-11: measured from the fill,
  tracking error 0.0000%. Keep measuring it from the fill.** (5) The broker/official price gap is a
  **live quote midpoint**, not an offset — cosmetic on core, **load-bearing the moment a satellite
  position exists**; whether the tooling should read closes from `bars` by default is a human's call.
  (6) **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed
  all five checks on 09-11 while `clock` was 500 and `quote`/`bars` were 504. **Every routine's Step
  0 is the loud-failure mechanism for exactly this, and on the data plane it is silent.** Until a
  human changes it: **probe by hand and never infer data-plane health from a green selftest.** Prior
  context in ClickUp `86bbv75bz`, last week's in `86bbzgbg3`.

- **⚠ FIVE ITEMS WERE DROPPED BEFORE THESIS STAGE TODAY AND EACH HAS A NAMED REASON — THEIR ABSENCE
  FROM THE THESIS IDS IS NOT AN OVERSIGHT.** **JPM guided Q3 trading and IB fees UP while BAC warned
  on the same lines and WFC said NIM will beat** — tempting because it is a genuine, dated,
  two-company contrast, but **the trade it suggests is buying JPM on JPM's OWN guidance: first-order,
  Company A, not §4 at all**, and extending it to peers is the **"a shared cause is not a mechanism"**
  trap (**fourth instance** — a rate environment, not a transaction). **Centene reaffirmed FY26
  guidance (GAAP EPS >$3.11, adj. >$4.80)** — a **reaffirmation of July 28 guidance**, standing rule
  (iii), first-order besides. **Medtronic's LigaSure RAS / Hugo FDA clearance** — MDT's own clearance,
  no dollar figure, no counterparty, and MDT is already a disposed reject. **Axon priced $1.0B of 0%
  convertible notes due 2031** — a financing; no counterparty's economics change. **General Mills —
  SCREENED AND FOUND NOT TO EXIST:** the first broad scan surfaced a MarketBeat auto-alert reading
  *"GIS expected to release earnings on Wednesday."* **It does not report until ~Sept 23**, and its
  FY27 guidance of $3.00–$3.20 was **affirmed Sept 8**, not changed. **An earnings-calendar alert is
  not an earnings event, and this one was worded to read like one.**

- **⚠ NOTHING IS PENDING FOR THE NEXT PRE-MARKET RUN, AND NOTHING CAN PILE UP BETWEEN THEM.** The
  09-11 Friday review handed 09-14 three earnings and **all three were screened in writing rather
  than assumed handled**; no unscreened item has accumulated across 09-14, 09-15 or 09-16. **Neither
  the open run nor the close run screens earnings**, so the only hand-off channel is pre-market run
  to pre-market run, plus the Friday review. **Today's earnings screen found no US earnings of
  consequence in the 09-15/16 window** — Centene was a reaffirmation, Dave & Buster's was 09-14 and
  already dropped (far below the §3 $10B floor, negative, and this book has no short), and General
  Mills is not until ~Sept 23. **Keep the Friday review writing the hand-off and keep the next
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
  **Eighteen sessions of "no exits" recorded the absence of a subject, not eighteen clean bills of
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
  THE SAME RUN. DISCHARGED 09-16 09:35 AND DUE AGAIN AT THE NEXT OPEN.** The gate was **evaluated
  against today's ET date and did not fire** — `plan_date: 2026-09-16` **matched**, so the plan was
  **FRESH**, and its zero intents are **the plan rather than a gap in it**. The open run read the
  **date, not the outcome**; the difference is invisible in the order count, and both readings would
  have produced the same empty run. **Zero `alpaca.py move` re-validation calls were issued and none
  was due** — re-validation has a subject only when a BUY intent exists: **an absent check, not a
  skipped one.** **The gate has now been exercised eighteen times and has never fired, so its alert
  path REMAINS UNTESTED CODE**; a future run must not read eighteen quiet opens as evidence that it
  works. **The way to know the gate is sound is to read it, not to count the days it stayed silent.**

- **⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** **Routine 1 places no
  orders by design** — it researches and writes a plan; **routine 3 is exits-only**; **routine 4
  trades nothing at all.** **A breaker reading INACTIVE, a weekly cap at 0 of 3 and 30.24% idle cash
  are not an opportunity any of them may act on**, and carry-forward item (3) above (the structurally
  undeployed sleeve) must **never** be read as licence for a midday or after-hours entry. **New
  positions route through pre-market research plus the 09:35 execution run, always** — that path is
  what forces every buy to sleep on a written thesis, and any other entry would route around it
  rather than satisfy it. **RE-DISCHARGED 09-16 08:17:** the pre-market run found new positions
  **fully permitted** — breaker INACTIVE, cap 0 of 3, empty sleeve, 30.24% cash, no restricting note
  in `control.md` — and **wrote zero BUY intents.** **Nothing blocked the research. The research did
  not produce an eligible candidate.** That distinction is the whole point of Step 5's instruction not
  to do research you cannot act on: **today the pressure ran the other way — full authority and
  nothing worth using it on.** **AND RE-DISCHARGED AGAIN 09-16 09:35 FROM THE ONE SEAT THAT COULD
  HAVE ACTED:** the open run is **the only routine permitted to open a position**, it read an
  **INACTIVE breaker, a cap at 0 of 3, an empty sleeve and 30.26% idle cash**, and it **opened
  nothing, because the plan it consumes carried no BUY intent.** **That is the discipline working at
  its single point of exposure.** The 08:00/09:35 gap exists precisely so a candidate reasoned into
  existence at the bell cannot become a fill; **a run that "found something" at 09:35 would not be
  diligent, it would be the failure this architecture is built to prevent.**

- **⚠ THE TWO-PRICE DEFECT IS SOLVED — IT IS A QUOTE MIDPOINT, NOT AN OFFSET. DO NOT RE-OPEN IT AS A
  MYSTERY.** It resolved at the 09-11 close, where broker `current_price` 702.62 was **the midpoint of
  the 702.59/702.65 quote to the cent** while the official close was **702.52**. **The broker mark is
  not a close at all — it is a live bid/ask midpoint that keeps moving outside regular hours**, which
  is why the gap never had a stable size and never will. **This morning's 698.88 against yesterday's
  official close 696.29 is the same mechanism in pre-market**, and `lastday_price` 696.20 is a third
  number again. Always `bars --adjustment all` for a close, a fresh `quote` for execution, **never a
  `positions` field for either.** **The moment a satellite position exists, a `highest_close` read
  from a `positions` field records an after-hours midpoint and silently moves the §5.4 stop.**

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

- **⚠ DO NOT REACH FOR THESE — the disposed rejects and the trap in each.** **AVGO** — today's, and the
  most instructive: **part 1 PASSED**, and it died on the counterparty disclosing **roadmap instead of
  segment revenue**, plus a **2027–2028** calendar, plus rule (iii). **It does not become a buy at a
  different price, and the −7.97% is not the reason.** **VG** — Company A on the China Gas SPA, and
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

- **⚠ SIX STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, Alcoa/South32, Oracle's
  maintained capex guidance, the four unsourced headlines, CoreWeave's 300 MW re-reported as context,
  **and on 09-16: Broadcom's own Q3 2026 call already carrying MTIA, Centene's reaffirmation of July
  28 guidance, and Sempra/Petrobras re-covered as though fresh**). (iv) *A recurring ticker is a
  warning, not corroboration* (LHX — resolved 09-11 on a number). (v) *A market-structure fact is not
  a supplier relationship* — "sole producer," "dominant share," "the only company that makes X" are
  facts about an **industry**, not a **transaction**; **seven instances this month, the latest being
  the Abrams AGT1500 OTA on 09-16, where it arrived as a CONSORTIUM AWARDEE plus a CEILING 212× the
  obligated cash.** Earlier costumes: a **TABLE** (the DoD daily contracts digest, 09-15) and a
  sentence. (vi) *Screen the timing window early on anything whose subject is under construction*
  (Sempra/Petrobras 09-15, **Venture Global/China Gas 09-16 — same instrument, different seller, one
  day later**). **The source left the blank. Filling in a blank the source left blank is not
  research.** **Recognise the phrase; do not re-derive it.**

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

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON TWENTY-SEVEN TIMES NOW, AND DUE AGAIN NEXT RUN. TODAY HAD
  FOUR RUNS TO TEMPT FOUR BLOCKS AND LEFT ONE.**
  `positions.md` ran to **604 lines / 42KB** before the 09-07 collapse and has since been held to a
  **single current reconciliation block** — this run **replaced** the 09-16 12:35 midday block
  rather than adding a second 09-16 one beside it, and the superseded `prior_run` line (09-16 open)
  was dropped from the fenced block rather than left to accumulate as a third slot. **Two blocks for
  one date is the easiest version of the mistake to make, and today was the day with two runs to
  tempt it.** **Every load-bearing fact is preserved;
  nothing live was discarded.** **The pull to append is structural** — a run is rewarded for showing
  it checked something, and a deleted note looks like a check that never happened. **A future run will
  feel it too, and two blocks for one date is the easiest version of the mistake to make.**
  **`journal.md` is the deliberate exception: it is append-only by design, one entry per trading day,
  and is now ~75KB — it rolls over monthly with the other logs, never by collapsing.**

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; nothing predates the current month. **Next rollover is the first
  Friday review of October 2026.** ⚠ **`research_log.md` is now ~187KB.** The rollover rule is monthly
  and this month is not over, so **no run may archive early** — but the October rollover is not
  optional tidying. **Every run reads these logs in full, and a run that starts skimming is how a
  system quietly stops knowing what it holds.**

- **⚠ THE MIDDAY RUN'S STEP 2 WAS DISCHARGED BY READING, NOT BY ASSUMING — AND THE DISTINCTION IS THE
  WHOLE POINT OF THAT STEP.** Routine 3 exists so a stale `highest_close` is caught before it silently
  disables §5.4. **Today the field was ABSENT, not stale**, and absence is self-certifying in a way
  staleness is not: **an absent field carries no `(as of ...)` date, and it is the missing date that
  proves no backfill is due.** A stale mark would carry a date that lags the last trading day and look
  exactly as healthy as a current one. **Zero `alpaca.py bars` calls were issued and none was due.**
  **The first satellite fill arms §5.4 and converts this step from absent to load-bearing on the same
  day** — from that day forward, a skipped close run makes this check the only thing standing between
  a stale mark and a trailing stop that never fires.

- **⚠ COUNTERS, STATED SO THEY DO NOT DRIFT.** **39 theses since inception, 0 accepted** — 30 through
  09-11 (6+2+1+1 on 09-01/02/03/04, 4+5+6+5 on 09-08/09/10/11) plus **3 on 09-14** plus **3 on 09-15**
  plus **3 on 09-16**. **9 this week** (the week beginning 2026-09-14). **Neither an open run nor a
  close run writes a thesis or consumes an ID** — an execution routine and a journaling routine do not
  research (§4 by way of the routine prompts), so the count is unchanged by them, not stalled. A
  counter already drifted once (31 vs the auditable 30) and was corrected on 09-11; **in a repo whose
  only memory is these files, a counter that drifts unremarked is how a larger one starts.**
  **Positions opened: still zero. `new_positions_this_week` stayed at 0 of 3 because nothing was
  placed, not because the cap bound. Trading days with the sleeve empty: eighteen** — the count
  advances on **sessions**, not on runs, so **none of the 09-16 open, midday or close runs advanced it
  past the 09-16 pre-market run's reading; FOUR RUNS, ONE SESSION, ONE INCREMENT.**
  **Satellite exits executed since inception: ZERO, across nineteen midday management runs that each
  had nothing to manage.** **Orders placed since inception: ONE** — the 09-03 core VOO buy.
  **Satellite orders placed since inception: ZERO.** **Daily journal entries written: one per trading
  day, 09-16's included.**

- **ClickUp tasks, for reference:** **09-16 daily summary `86bc1y9mr`**; 09-15 daily summary
  `86bc17nc4`; 09-14 daily summary
  `86bc0hw64`; **09-11 weekly review `86bbzgbg3`**; 09-11 daily summary `86bbzfm12`; 09-10
  `86bbyr8vp`; 09-09 `86bbxtn1a`; 09-08 `86bbwuc17`; 09-04 daily summary `86bbv6npm` and weekly review
  `86bbv75bz`. **No alert task exists** — no alert condition (breaker, push failure, selftest abort,
  guard violation, stale plan) has ever arisen, and `alerts.md` remains empty.
