# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-15 16:15 ET 4-market-close-journal (selftest PASSED all five checks at 16:15 ET, trading_enabled true, LIVE paper, equity 99025.37; THIS ROUTINE TRADES NOTHING AT ALL - zero orders and none was due; TODAY WAS A TRADING DAY - clock is_open FALSE at 16:16:02 because the BELL RANG sixteen minutes ago, next_open 2026-09-16T09:30 TOMORROW and the midday run recorded is_open TRUE at 12:34:55, so the HOLIDAY BRANCH DID NOT APPLY and the daily summary was due; STEP 2 NO HIGH-WATER MARK WRITTEN AND NONE WAS DUE - zero satellite blocks means no highest_close to raise and no (as of) date to re-stamp, marks are ABSENT not stale, ZERO bars calls issued for a high-water purpose, core VOO deliberately NOT stamped because stamping it would fabricate a 5.4 stop on the one position 5 exempts, 5.4 still NOT ARMED; day numbers on OFFICIAL closes both legs - VOO close 696.29 vs 699.35 = -0.438%, equity 98964.96, day -303.08 / -0.305%, since inception -1.035%, core unrealized -1035.03 / -1.479% from the 706.74 fill and it carries NO ACTION; broker legs read 99025.37 and -0.240% and MUST NOT be mixed with official ones - that mix reads as beating the index by 0.198pp and the whole of it is a 16:16 quote midpoint against a 16:00 close, FIRST DAY THE ARTIFACT WAS FLATTERING; sleeves official core 69.69% satellite 0.0% count 0 cash 30.31%, core_in_band true, rebalance_needed false, NO REBALANCE DUE TOMORROW, delta to exact 70% = 310.51 = 0.31% of equity and 2 rebalances at the BAND EDGE, SIXTEENTH consecutive run inside a 0.29-point range 69.69-69.98; STEP 3 5.1-5.4 NOT EVALUABLE, no subject, seventeenth consecutive session, all four remain UNTESTED CODE PATHS; STEP 4 week rollover checked - ISO Monday of 2026-09-15 is 2026-09-14 MATCHES week_of, NO RESET DUE, next boundary Monday 2026-09-21; loss streak UNMOVED at 0 because nothing closed and nothing has ever closed, breaker INACTIVE, no circuit-breaker alert due; unresolved orders NONE - orders --status all returns ONE row, the 09-03 core fill, status filled, terminal, re-verified by hand, NOTHING IN LIMBO OVERNIGHT; trade_log.md correctly left unappended; STEP 5 journal.md appended, one entry for 2026-09-15; STEP 6 ClickUp daily summary 86bc17nc4 created; research 3 theses 0 accepted 3 rejected; alerts.md EMPTY, zero open, zero SYSTEMIC)

prior_run: 2026-09-15 12:35 ET 3-midday-management (selftest PASSED all five checks at 12:34 ET, trading_enabled true, LIVE paper, equity 98980.31; MARKET OPEN - clock is_open TRUE at 12:34:55; RUN ENDED AT STEP 1 BY THE PROMPT'S OWN INSTRUCTION - zero open satellite positions means there is nothing to manage, note it and exit, do NOT go looking for something to do; it read 30.31% idle cash, a breaker reading INACTIVE and a weekly cap at 0 of 3 and OPENED NOTHING; ledger reconciled - zero satellite blocks vs zero satellite Alpaca rows, they AGREE; STEP 2 HIGH-WATER REPAIR HAD NO SUBJECT, ZERO bars calls and NONE WAS DUE; STEP 3 ZERO perplexity invalidation queries and NONE WAS DUE; ZERO sell orders placed; breaker INACTIVE)

week_of: 2026-09-14
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.69
satellite_pct: 0.0
cash_pct: 30.31
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

- **⚠ NEW AND OPERATIONALLY LOAD-BEARING: A CLOSE RUN ALWAYS READS `is_open: false`, AND ROUTINE 4's
  HOLIDAY BRANCH TRIGGERS ON EXACTLY THAT FLAG.** `clock` returned **`is_open: false` at 16:16:02**
  today — because the bell rang sixteen minutes earlier, **not** because the market never opened.
  The routine says *"market was closed today (holiday): note the skip, commit, exit, do not post a
  daily summary."* **A run that pattern-matches on the boolean takes that branch on every ordinary
  trading day**, skips the summary for a day that did happen, and leaves a run record
  **indistinguishable from a genuine holiday.** What separates them is **`next_open`: it read
  2026-09-16T09:30 — TOMORROW — not today**, plus the midday run's recorded `is_open: true` at
  12:34:55. **Read the next_open date, not the boolean.** Nothing was lost today, and **the first
  real holiday will arrive without warning.**

- **⚠ THE MIXED-SOURCE ARTIFACT TURNED FLATTERING FOR THE FIRST TIME, AND THAT IS THE HARD VERSION.**
  Today the broker's day change read **−0.240%** against VOO's official **−0.438%** — **the book
  appearing to beat the index by 0.198pp on a red day, about $65.** It did not: a 69.7%-exposed book
  loses **0.697 × 0.438% = 0.305%** by construction, which is exactly what matched official legs give
  (**−$303.08 / −0.305%**, equity **$98,964.96** vs the broker's $99,025.37). The entire gap is a
  **16:16 quote midpoint compared against a 16:00 official close.** Every prior instance was
  cosmetic or unfavourable; **a favourable artifact is materially harder to discard than an
  unfavourable one**, and this is the shape in which the defect will eventually cost something.
  **Both legs from the same source, or the comparison means nothing.**

- **⚠ THE WEEKEND EXCUSE IS SPENT AND THE ANSWER IS STILL NO — THIS IS THE HEADLINE OF 09-15 AND IT
  REPLACES THE MONDAY-CALENDAR NOTE.** The 09-14 carry-forward said in writing that a thin Monday
  funnel is a property of the schedule and that **"a thin Tuesday funnel would NOT have this
  excuse."** **Today was that Tuesday.** It screened a full business day and the event set was
  **genuinely richer than Monday's** — LMT **$1.2B** PrSM Inc 2 plus an **$8.4B** Inc 1 production
  mod, BA **$13.4B** KC-46 ceiling increase to **$19.1B** through April 2035, a **20-year 0.8 Mtpa**
  Sempra–Petrobras LNG SPA, BCE's **~$52B / 1.2 GW** Regina AI hub MOU, a **$7.7B** Baldwin
  take-private, ABT's **$385M** formula settlement. **The events were there. The quantified
  counterparties were not.** Three screens returned, verbatim: *"no public source names any
  subcontractor, supplier or teammate with a specific dollar figure"*; *"I could not verify any
  US-listed company with market cap above $10 billion that discloses a quantified revenue
  exposure"*; *"no such announcement is clearly documented in the sources reviewed."* **§4's binding
  constraint is disclosure practice — not news volume, not thesis quality, and not the calendar.**
  (The Monday-calendar note still holds on its own terms and recurs every Monday and after any
  holiday; it is simply no longer the explanation for a thin funnel.)

- **⚠ NEW TRAP, AND IT NEARLY WORKED: A DOD DAILY CONTRACTS DIGEST IS NOT A SUPPLIER BREAKDOWN.**
  One tracking summary listed **Boeing, Blue Halo, Olin Winchester, Rolls-Royce Solutions America
  and J&J Contractors** under the KC-46 heading alongside **three dollar figures** ($13,400,000,000;
  $99,832,117; $788,361,894) and **no mapping between them** — the source itself says it *"does not
  explicitly map each dollar figure to a specific company."* Those are **unrelated awards grouped by
  publication date.** Read quickly it looks exactly like a prime-plus-subcontractor allocation.
  **This is standing rule (v) wearing a table instead of a sentence, and a table is more persuasive
  than a sentence.** Recognise the layout; do not re-derive the disappointment.

- **⚠ SCREEN THE TIMING WINDOW EARLY ON ANYTHING WHOSE SUBJECT IS UNDER CONSTRUCTION — NEW
  STANDING RULE (vi).** The **Sempra ↔ Petrobras** SPA (T-2026-09-15-03) is the ideal-looking §4
  input: two named parties, a disclosed volume, a binding 20-year contract. It dies on the
  **calendar** — the LNG is sourced from **Port Arthur LNG Phase 2, guided to COD in 2030 and
  2031**, so first delivery is **four to five years** out against §4.3's **two-quarter** cap.
  **Long-dated infrastructure offtakes will keep entering this funnel looking perfect.** Part 3
  kills them faster than part 1 does, **and that rejection survives a supplier being named later**,
  which part 1's does not.

- **⚠ CRWV IS THE NEAR-MISS OF 09-15 AND THE MOST USEFUL REJECTION TO CARRY: THE NUMBER WAS NOT
  MISSING, IT WAS THE WRONG NUMBER.** T-2026-09-15-01 rejected CoreWeave at **part 1**. BCE's MOU
  names CoreWeave — but the **300 MW is the pre-existing contract** and **none of the new 900 MW is
  allocated to anyone**; the mechanism sentence needs an **"and also"** to carry its entire economic
  claim, which §4 part 1 forbids outright. **This is the CART shape (09-14) one day later in a bigger
  costume: a named counterparty inside a loudly quantified project, where the quantity attaches to
  the PROJECT and not to the COUNTERPARTY.** **A $52B headline makes that far harder to see than
  Kroger's silence did.** Standing rule (iii) kills it independently — CoreWeave's 300 MW is prior
  business re-reported as context. **Do not reach for CRWV; it does not become a buy at a different
  price.**

- **⚠ THE PRICED-IN DRAWDOWN DEFECT FIRED A SIXTH TIME AND AGAIN COST NOTHING — KEEP THE TWO TALLIES
  SEPARATE.** Open item (1) — the §4 filter reading a **drawdown** as "priced in" — hit **CRWV
  −7.12%** (`priced_in: true`, *"LATE - skip"*). Instances now: **LITE −7.35%, LMT −3.61%
  near-miss, LHX −4.47%, CART −5.79%, BWXT −6.30%, CRWV −7.12%.** **The filter was applied as
  written and CRWV was skipped; no run may reinterpret it — that is a human editing §4 or
  `alpaca.py move`.** **But CRWV was already dead at part 1 when the filter reached it, so today
  adds an instance and ZERO damage.** **The expensive instances are the ones that reach the filter
  ALIVE, and LITE is still the only one** — it passed the four-part thesis, was killed by a
  drawdown, and is **+10.58% vs VOO** since. **A review that counts six instances as six costs will
  overstate the case for a change that is not the agent's to make.**

- **⚠ SIX ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE.** (1) **The §4 priced-in filter
  reads a drawdown as priced-in** — six instances, see above; **there is no price at which those
  rejections flip**, and LITE puts **+10.58% vs VOO** on the bill. (2) **The same filter reads an
  event move absorbed before it looks as "passes"** — QCOM (09-09, +2.70% after a +8.7% intraday
  move) and AVAV (09-11, +1.20% after a +12.9% intraday round-trip inside one session). Same root
  cause, opposite direction. **The fix for (1) and (2) is a human editing §4 or `alpaca.py move`.**
  (3) The satellite sleeve is **structurally undeployed — THIRTY-SIX theses, zero positions, sixteen
  sessions**; a 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a rising
  market. **§2 permits the cash and §4 says most runs end in no trade — both rules were followed,
  and the agent must NOT respond by lowering the §4 bar.** **§4's binding constraint is identifiable
  and it is not thesis quality:** the source names the transaction and withholds the counterparty,
  or names the counterparty and withholds the number, or attaches the number to the project instead
  of the counterparty. **09-15 removed the last alternative explanation — a rich full-business-day
  funnel produced the same nothing.** **That points at something a human could change — widen the
  acceptable evidence for a named Company B, or accept the hit rate.** (4) The core's divergence
  from VOO is the **09-03 entry gap** (fill 706.74, +0.483% above the prior close), **not tracking
  error and never skill** — **DISCHARGED AND PROVEN 09-11: measured from the fill, tracking error
  0.0000%. Keep measuring it from the fill.** (5) The broker/official price gap is a **live quote
  midpoint**, not an offset — cosmetic on core, **load-bearing the moment a satellite position
  exists**; whether the tooling should read closes from `bars` by default is a human's call.
  (6) **`selftest.py` certifies a healthy system without probing `clock` or market data** — it
  passed all five checks on 09-11 while `clock` was 500 and `quote`/`bars` were 504. **Every
  routine's Step 0 is the loud-failure mechanism for exactly this, and on the data plane it is
  silent.** Until a human changes it: **probe by hand and never infer data-plane health from a green
  selftest.** Prior context in ClickUp `86bbv75bz`, last week's in `86bbzgbg3`.

- **⚠ NOTHING IS PENDING FOR THE NEXT PRE-MARKET RUN, AND THE HAND-OFF MECHANISM IS WHY THAT
  SENTENCE IS TRUSTWORTHY.** The 09-11 Friday review handed 09-14 three earnings (Kroger, VinFast,
  Rent the Runway) and **all three were screened in writing rather than assumed handled.** **No
  unscreened item accumulated over 09-14 or into 09-15** — the 09-15 08:16 survey found no US
  earnings of consequence landing after it, and **neither the open run nor the close run screens
  earnings**, so nothing can pile up between pre-market runs. **Keep the Friday review writing the
  hand-off and keep the next pre-market run discharging it in writing.** Dave & Buster's FQ2 (09-15
  pre-market: revenue $544.1M vs $556.8M consensus, adj. EBITDA $98.9M vs $120.4M, −$0.27 adj. EPS
  vs +$0.18 expected) **was screened and dropped** — far below the §3 $10B floor, negative, and
  **this book has no short.**

- **⚠ THE FOMC DECIDES TOMORROW (09-16/17) AND IT IS NOT A CANDIDATE IN EITHER DIRECTION.** The
  meeting **began 09-15**. August CPI landed 09-11 (headline **+0.4% m/m / +3.4% y/y**, core
  **+0.3% m/m / +2.4% y/y**); UMich preliminary September confidence printed **47.8, down from
  51.7**. **No Company A, no segment, no dollar path — it is the whole tape moving, which is exactly
  what §4 exists to refuse.** **The 09-14 note predicted the 09-15/16 funnels would be crowded with
  macro framing and yield nothing §4 can use. They were, and it did. That is the note working, not
  a quiet market.** **If it moves prices hard, that is a price move, not a thesis**, and a core mark
  that moves with it carries no action because §5 exempts core. *(One 09-14 source priced ~87% odds
  of a 25bp **increase**, contradicting every other framing in the same result set. Unresolved and
  deliberately not chased — untradeable under §4 whichever way it reads.)*

- **⚠ ALL FOUR §5 SELL RULES REMAIN UNTESTED CODE PATHS, AND §5.4 IS STILL NOT ARMED.** Nothing has
  ever closed in this account, so §5.1–§5.4 have never been evaluated against a real subject.
  **Sixteen sessions of "no exits" recorded the absence of a subject, not sixteen clean bills of
  health.** **The high-water marks are ABSENT, not stale — a third state, distinct from "current
  and unchanged."** An absent field carries **no date**, and **that absence of a date is what tells
  the midday run no backfill is due** — the trigger cannot fire, and no `bars` call is due for a
  high-water purpose. **Core VOO is deliberately never stamped** — doing so would fabricate a §5.4
  stop on the one position §5 exempts. **§5.4 arms on the first *satellite* fill.** **The failure
  this exists to catch is still ahead of us** — the day a satellite position exists and a close run
  is missed *or* the data plane is down at 16:00, the mark goes stale while every field still reads
  present and plausible. **Both halves of the machinery have run only against an empty sleeve:** the
  09-14 **and 09-15** midday runs exercised the REPAIR step and found nothing to repair; every close
  run, **including 09-15's**, has exercised the RECORDING step and had nothing to record. **Each
  tests the "no subject" branch and nothing else.** **The 09-15 close run adds the recording-side
  version of the point: Step 2 is written in the IMPERATIVE and its subject does not exist, so the
  pull is to satisfy the sentence by stamping the one close available — core VOO's 696.29. That
  would FABRICATE a §5.4 trailing stop on the one position §5 exempts from all four sell rules, on a
  day core sits −1.479% from its fill. It was recognised and refused. It will not feel like a
  violation when a future run does it; it will feel like tidiness.** **The 09-15 midday run adds the sharpest version of the point: it
  issued ZERO `bars` calls and ZERO Perplexity invalidation queries, and both were correct** —
  §5.1 reads an `invalidation` line that does not exist, and the repair step compares an
  `(as of ...)` date that does not exist. **An absent check is not a skipped one, and a run that
  manufactured either call would be inventing a subject.**

- **⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE THE SAME ZERO ORDERS AND ARE NOT
  THE SAME RUN — DISCHARGED 09-15 09:36, AND THE PREDICTION HELD EXACTLY.** The pre-market run wrote
  **`plan_date: 2026-09-15`**; the open run read it against the ET date **2026-09-15**, they
  **matched**, and the gate **did not fire**. **No stale-plan alert was due and none was posted.**
  Steps 4–6 were reached **with full authority and no intents to act on** — that is the whole
  difference from a stale run, and **it is invisible in the order count.** **Zero `alpaca.py move`
  re-validation calls were issued and none was due** — re-validation has a subject only when a BUY
  intent exists; **an absent check, not a skipped one.** **The gate has now been exercised sixteen
  times and has never fired, so its alert path REMAINS UNTESTED CODE**; a future run must not read
  sixteen quiet opens as evidence that it works. **The way to know the gate is sound is to read it,
  not to count the days it stayed silent.**

- **⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** **Routine 1 places no
  orders by design** — it researches and writes a plan; **routine 3 is exits-only**; **routine 4
  trades nothing at all.** **A breaker reading INACTIVE, a weekly cap at 0 of 3 and 30.24% idle cash
  are not an opportunity any of them may act on**, and carry-forward item (3) above (the
  structurally undeployed sleeve) must **never** be read as licence for a midday or after-hours
  entry. **New positions route through pre-market research plus the 09:35 execution run, always** —
  that path is what forces every buy to sleep on a written thesis, and any other entry would route
  around it rather than satisfy it. **Having no work is the correct outcome for a routine whose
  subject does not exist, not a gap to fill.** **RE-DISCHARGED 09-15 12:35:** the midday run read
  30.31% idle cash, a breaker reading INACTIVE and a weekly cap at 0 of 3, and **opened nothing** —
  it ended at Step 1 because the prompt says in terms that no open satellite positions means note
  it, commit and exit, and **do not go looking for something to do.** **RE-DISCHARGED AGAIN 09-15
  16:15:** the close run **trades nothing at all by design** and placed zero orders; it read the
  same 30.31% cash, the same INACTIVE breaker and the same 0-of-3 cap, and the only thing it did
  with them was report them.

- **⚠ THE TWO-PRICE DEFECT IS SOLVED — IT IS A QUOTE MIDPOINT, NOT AN OFFSET. DO NOT RE-OPEN IT AS
  A MYSTERY.** Six days of notes called the broker/official gap an *unstable offset* (**6.5c**
  09-09, **59.85c** 09-10, **4c** 09-11 morning, **17c** at the 09-14 close); it resolved exactly at
  the 09-11 close, where broker `current_price` 702.62 was **the midpoint of the 702.59/702.65 quote
  to the cent** while the official close was **702.52**. **The broker mark is not a close at all —
  it is a live bid/ask midpoint that keeps moving outside regular hours**, which is why the gap
  never had a stable size and never will. **This morning's 698.59 against yesterday's official close
  699.35 is the same mechanism in pre-market.** **Neither is an error; they are different sources,
  and a comparison that mixes them manufactures a result.** Always `bars --adjustment all` for a
  close, a fresh `quote` for execution, **never a `positions` field for either.** **The moment a
  satellite position exists, a `highest_close` read from a `positions` field records an after-hours
  midpoint and silently moves the §5.4 stop.**

- **⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Taking the index
  leg from **official** closes while leaving the book leg on **broker** marks produced a
  **+0.0141pp residual — about $14 of pure artifact** on 09-11. **Both legs from the same source,
  or the comparison means nothing.** The standing refutation holds on any day: ~0.70 exposure to an
  index move is ~70% of it **by construction**, and it runs identically in reverse. **Anchor the
  week to 08-31, the first operating day.** **And expect the satellite sleeve's §1 number to read
  positive on every red week without the sleeve doing anything — the defense is not arithmetic, it
  is refusing to let a favorable sign on a few sessions answer a 12-month question.**

- **⚠ DO NOT REACH FOR THESE — the disposed rejects and the trap in each.** **CRWV** — today's
  near-miss; the trap is that the **$52B is the project's, not CoreWeave's**, and the headline size
  disguises it. **LMT and BA** — today's; both are the **awarded party**, i.e. Company A, and no
  supplier is named on either award. **SRE** — Company A on the Petrobras SPA, and the whole thing
  is four to five years out. **BWXT** — the sole-source naval-reactor fact is **rule (v)**, and it
  will feel like a technicality rather than a rule. **CART** — died on the missing number, and the
  number does not exist to be found. **ORCL** is Company A twice over and **`priced_in: true` at
  +5.06%**; the screen for a US-listed company that has *itself* named Oracle as a quantified
  customer returned **"No verified companies found."** **LHX** — dead on arithmetic: **$127M
  Palantir + $65M Anduril = the entire $192M TITAN award**, $0 disclosed for anyone else. **AVAV**
  is the **awarded party** and its +1.20% is a round-tripped spike. **SLI** is ~$1B against the
  **§3 $10B floor**. **M** — the tariff-refund read-across runs through a **statute, not a
  transaction**. Also closed: **GFS, EQT** (*the tempting one — a clean filter sheet that died on
  size*), **LEU, TBBK, CASH, GDOT, CCB, QCOM, AMZN, GLW, VZ, MTZ, FN, COHR, LITE, CRDO, MRVL, DY,
  PWR, BSX, MDT, ABT.** **None becomes a buy at a different price, and LMT and ABT both resurfaced
  in the 09-15 news as Company A — that is not a reason to re-run their filters.** **Do not reach
  for MU** — it has not entered the funnel for **thirteen consecutive days**, no source has named
  it, its filters were **not** re-run: **absence of evidence, not resolve.** If it resurfaces **from
  a source**, re-run its filters and re-test the timing window from that day's date.

- **⚠ SIX STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX). (ii) *Verify what the company currently sells, post-spin* (WDC). (iii) *Verify the news is
  new to the company's own disclosure* (AEP, CAT, the $517B aggregation, Alcoa/South32, Oracle's
  maintained capex guidance, the four unsourced headlines, **and CoreWeave's 300 MW re-reported as
  context on 09-15**). (iv) *A recurring ticker is a warning, not corroboration* (LHX — resolved
  09-11 on a number). (v) *A market-structure fact is not a supplier relationship* — "sole
  producer," "dominant share," "the only company that makes X" are facts about an **industry**, not
  a **transaction**; **six instances this month, the latest being the LMT/BA awards on 09-15, where
  it arrived as a TABLE rather than a sentence.** (vi) **NEW 09-15:** *screen the timing window
  early on anything whose subject is under construction* (Sempra/Petrobras). **The source left the
  blank. Filling in a blank the source left blank is not research.** **Recognise the phrase; do not
  re-derive it.**

- **⚠ A SHARED CAUSE IS NOT A MECHANISM.** Macy's FQ2 (09-11) was the first instance: $116M of
  IEEPA tariff refunds, where the tempting *"the ruling lowers other import-heavy retailers' COGS
  too"* runs through a **statute, not a transaction**. Kroger's 09-14 guidance cut was the same
  shape in a different costume — Kroger's soft ID sales and a supplier's soft volumes are both
  downstream of the **same grocery consumer**. **The Williams NESE ruling (Third Circuit vacated
  New Jersey's water-quality certification for the $1B pipeline, 09-08) is the third instance and
  was dropped before thesis stage on 09-15** — a court ruling, not a transaction, and outside the
  window besides. **All also fail a second, independent test: any company actually affected
  discloses it itself, making it first-order for that company.** The distinction is easy to lose
  because the sentence sounds causal when said aloud.

- **⚠ HPE IS THE LARGEST OPPORTUNITY COST THIS LOG HAS PRODUCED (+19.87% vs VOO) AND THE REJECTION
  WAS CORRECT. DO NOT RECORD IT AS ONE FINDING.** T-2026-09-02-02 rejected a **Dell → HPE
  read-across** at part 1, because a read-across is an inference about **information**, not a causal
  path changing Company B's economics. **What then moved the stock was HPE's own earnings print:
  +12.4% in the single session 09-10 → 09-11.** Rejected *correctly by the rule* and *unprofitably
  in hindsight* — **two findings, recorded as two. Nothing here loosens it.**

- **⚠ REJECT SCOREBOARD — 33 MEASUREMENTS, 9 BEAT VOO, MEAN EXCESS −0.51%. STILL A TALLY, NOT
  EVIDENCE; A REVIEW MUST NOT QUOTE IT AS A RESULT.** **It reversed on itself inside one week:**
  week 1's same ten names went from **6-of-10 beating VOO (mean −0.16%) to 3-of-10 (mean +1.17%)**
  once the window lengthened by a few sessions. **The split still points the same way on more
  data:** four-part-thesis and §3 failures lag; the two **priced-in filter vetoes** average
  **+7.36%** and are the two largest positive excesses on the board. **MU and LITE must never be
  merged:** MU (+4.14%) failed on a real **run-up** — the rule working as designed and costing
  money, change nothing; LITE (+10.58%) failed on a **drawdown**, the open question. **Do not
  tighten §4 in response, and do not loosen it.** **The 09-15 rejects (CRWV, and the no-ticker
  LMT/BA and Sempra entries) are not yet measured; only CRWV has a ticker to measure.**

- **⚠ FOUR LOUD HEADLINES FROM 09-11 STILL HAVE NO PRIMARY SOURCE — AND NONE APPEARED IN A WEEKEND
  FILING OR IN THE 09-14/15 SWEEP.** *"Nvidia invests $30B in Intel," "Nvidia acquires Hugging
  Face," "Google's first nuclear deal / a $1.9B loan to restart an Iowa reactor," "Microsoft to
  triple cloud capacity by 2032."* **All four trace to a single secondary aggregator briefing citing
  other outlets rather than any document.** **This is standing rule (iii) in a new costume, and
  `--recency day` passes it just as readily.** Events of that size produce primary disclosure; its
  absence is the finding. **If one is real it will arrive with a filing attached, and that is the
  day it enters the funnel.**

- **NO TRADES, NO FILLS, NOTHING IN LIMBO — CHECKED AGAINST §7.** The account's entire order history
  is **one row**: the 09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`, **BUY VOO
  99.046311231 @ $706.74, notional $70,000.00**, `status: filled`, terminal. **No `"terminal": false`
  case has ever arisen.** `trade_log.md` correctly left unappended — **a run with no fill writes no
  trade entry.** Loss streak **0 — nothing has ever closed**, so the §6 streak cannot move and no
  circuit-breaker alert is due. **Core is not tracked in `positions.md` by design** (§5 exempts it),
  so **every reconciliation compares satellite blocks to satellite Alpaca positions**; a run
  comparing raw ledger to raw broker will read a correct ledger as broken.

- **⚠ COLLAPSE, DO NOT APPEND — ACTED ON TWENTY-THREE TIMES NOW, AND DUE AGAIN NEXT RUN.**
  `positions.md` ran to **604 lines / 42KB** before the 09-07 collapse and has since been held to a
  **single current reconciliation block** — the 09-15 close run replaced the 09-15 12:35 midday block
  rather than adding a second one for the same date, and the superseded `prior_run` line was dropped
  from the fenced block rather than left to accumulate as a third slot. **FOUR runs have now landed
  on 2026-09-15 and the file carries ONE block for the date** — that is the rule working. **Every load-bearing fact is
  preserved; nothing live was discarded.** **The pull to append is structural** — a run is rewarded
  for showing it checked something, and a deleted note looks like a check that never happened.
  **A future run will feel it too, and two blocks for one date is the easiest version of the mistake
  to make.** **`journal.md` is the deliberate exception: it is append-only by design, one entry per
  trading day, and is now ~67KB — it rolls over monthly with the other logs, never by collapsing.**

- **MONTHLY ARCHIVE ROLLOVER: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; nothing predates the current month. **Next rollover is the
  first Friday review of October 2026.** ⚠ **`research_log.md` is now ~2,550 lines / 172KB.** The
  rollover rule is monthly and this month is not over, so **no run may archive early** — but the
  October rollover is not optional tidying. **Every run reads these logs in full, and a run that
  starts skimming is how a system quietly stops knowing what it holds.**

- **⚠ COUNTERS, STATED SO THEY DO NOT DRIFT.** **36 theses since inception, 0 accepted** — 30
  through 09-11 (6+2+1+1 on 09-01/02/03/04, 4+5+6+5 on 09-08/09/10/11) plus **3 on 09-14** plus
  **3 on 09-15**. **6 this week** (the week beginning 2026-09-14). **Neither an open run nor a close
  run writes a thesis or consumes an ID — an execution routine and a journaling routine do not
  research (§4 by way of the routine prompts), so the count is unchanged by them, not stalled.**
  A counter already drifted once (31 vs the auditable 30) and was corrected on 09-11; **in a repo
  whose only memory is these files, a counter that drifts unremarked is how a larger one starts.**
  **Positions opened: still zero. `new_positions_this_week` stayed at 0 of 3 because nothing was
  placed, not because the cap bound. Trading days with the sleeve empty: seventeen** (the 09-15
  pre-market, open, midday **and close** runs are **all the same seventeenth session**, and all four
  placed **zero orders** — the count advances on sessions, not on runs, and a fourth run today does
  not make it eighteen). **`journal.md` carries exactly ONE entry for 2026-09-15**, written by the
  close run; it is append-only by design and **one entry per trading day, never one per run.**

- **ClickUp tasks, for reference:** **09-15 daily summary `86bc17nc4`**; 09-14 daily summary `86bc0hw64`; **09-11 weekly review
  `86bbzgbg3`**; 09-11 daily summary `86bbzfm12`; 09-10 `86bbyr8vp`; 09-09 `86bbxtn1a`; 09-08
  `86bbwuc17`; 09-04 daily summary `86bbv6npm` and weekly review `86bbv75bz`. **No alert task
  exists** — no alert condition (breaker, push failure, selftest abort, guard violation, stale
  plan) has ever arisen, and `alerts.md` remains empty.
