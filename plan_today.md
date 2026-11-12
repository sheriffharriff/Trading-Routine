# Today's Plan

**AGENT-OWNED. Written by the pre-market routine, consumed by the market-open routine,
overwritten daily.**

This file is the handoff between the two runs. The pre-market run does the thinking and
writes intents here; the market-open run executes them. Nothing gets bought that was not
written here first, which is what forces every buy to sleep on a written thesis instead of
being reasoned into existence at the moment of execution.

The market-open run **re-validates every intent against fresh quotes before acting**. An
intent written at 08:00 can be dead by 09:35 — an overnight gap can push a candidate past
the §4 4%-in-five-sessions priced-in threshold, in which case the trade is skipped and the
skip is logged. A stale intent is a proposal, not an instruction.

---

## Status

`plan_date` is load-bearing, not a comment. The market-open routine compares it to today's
ET date and **refuses to execute any intent from a plan not dated today** — it logs the
stale plan, posts an alert, and proceeds to the core/rebalance section only.

```
plan_date: 2026-11-12
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-12 at 09:30 ET** (`clock` 07:01:49 ET: `is_open: false`, `next_open`
`2026-11-12T09:30:00-05:00`, `next_close` `2026-11-12T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Thursday, an ordinary full session; **the previous session (11-11, Veterans Day) was also a
full equity session**, so there is no half-day or holiday adjacency to account for.

The plan this seat replaced was dated **2026-11-11** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

**WEEK ROLLOVER — NO ACTION DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W46**, weekday **4**; Monday anchor **2026-11-09** = the inherited `week_of`
**2026-11-09**. `new_positions_this_week` stays **0 of 3**. ⚠ **Recorded as re-derived rather
than skipped: §6's cap must not depend on any earlier seat having run.**

---

## ⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists only
in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02 seat read
routine 2's **stored schedule** as `13:35:00 UTC`. That was `09:35 ET` under EDT and is
`08:35 ET` under EST. **US ET left DST on 2026-11-01.** Dispatches since: `08:47` (11-02) ·
`08:36` (11-03) · `08:35` (11-04) · `08:37` (11-05) · `08:37` (11-06) · `08:36` (11-09) ·
`08:36` (11-10) · `08:35` (11-11) — **eight for eight, each read `is_open: false` and placed
nothing.** This seat dispatched at `07:01` against a nominal `08:00`: the same −1h, **ninth
consecutive EST session.**

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED, CONFIRMED
CONDITION — NOT A NEW FAULT AND NOT A HOLIDAY.** Record the firing time and `is_open` as your
first line. `control.md` forbids diagnosing a schedule fault **from a firing time**; the
stored-schedule reading plus the DST calendar is different evidence.

**PROCEDURE IF YOU ARE THE OPEN SEAT AND THIS PLAN CARRIES ANY INTENT:** finish every
closed-market-safe step, **COMMIT AS INSURANCE** (say in the message that a hold is in progress
and what to backfill if the second commit never lands), poll `clock` until `is_open: true`,
then execute and commit again. **DO NOT log a skip over a non-empty plan.** Holding past the
bell is exactly what changes `is_open`, and routine 4 has now proved the hold **four times**
(11-06, 11-09, 11-10, 11-11), recording the official close each time. ⚠ **This plan carries no
intents, so the procedure is not due today — it is written here because the day it IS due, the
seat will be reading this file and nothing else.**

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS WHAT
MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed seat over an empty
plan are byte-identical in output.** The ask is unchanged and is the human's alone:
**re-anchor all five triggers to `America/New_York`.** A flat +1h UTC shift is correct for EST
and **wrong again from 2027-03-14**, so it is a stopgap, not the fix.

---

## Intents

### BUY

**NONE.** Four broad Perplexity sweeps and two drill queries spent; **six theses logged; zero
survived.**

New positions were **permitted throughout, and the absence of intents is a research outcome,
not a block**: breaker **INACTIVE 0/3** · `new_positions_this_week` **0 of 3** · satellite
sleeve **0.0% deployed** with **$30,000 cash** · `control.md` **Notes: (none)**. ⚠ **Nothing
stopped a buy except the candidates.**

**⚠⚠⚠ THE ENTRY THAT MATTERS MOST TODAY IS `T-2026-11-12-02`, AND IT IS A CORRECTION TO
YESTERDAY BEFORE IT IS A REJECTION.** Yesterday's `T-2026-11-11-02` killed CoreWeave with the
sentence *"the figure a supplier thesis would run on is CAPEX, and the source discloses no change
to it."* **THAT WAS FALSE.** The same **2026-11-10** release said verbatim: *"We now expect full
year 2026 capital expenditures of **$37 billion to $39 billion**, raising the low end of our
prior guidance range of **$35 billion to $39 billion**."* ⚠ **The 11-11 seat applied the right
rule to a mis-stated fact and got the right answer for a reason that was not true.** The entry is
**amended in place**, not left beside its correction.
⚠⚠ **AND WITH THE CORRECTION APPLIED THE THESIS DIES HARDER, WHICH IS THE WHOLE POINT:**
**(a) only the LOW END moved — the $39B ceiling is UNCHANGED, so not one dollar was added to the
maximum CoreWeave has ever said it might spend**; **(b) the stated reason is to *"deliver it to
customers sooner than planned"* — TIMING, NOT VOLUME, and a pull-forward inside an unchanged
ceiling moves *when* suppliers are paid, not *how much*;** and **(c) no sentence in the release or
the call names a supplier with a dollar figure, so NVDA/VRT/DELL/SMCI are entirely the reader's.**
⚠⚠ **NEW COSTUME FOR RULE (iii), AND THE TEST IS ONE CLAUSE: A ONE-SIDED RANGE NARROWING WEARING
A GUIDANCE RAISE'S CLOTHES. ASK WHICH END OF THE RANGE MOVED — for a supplier thesis, only the top
end is a dollar path.** It is the mirror image of costume #1 (reaffirmation): the floor rose and
the ceiling was reaffirmed in the same breath, and only the floor gets quoted.
⚠⚠⚠ **AND THE RULE (iv) READING IS THE STRONGEST THIS LOG HAS PRODUCED: THE FUNNEL CAME BACK WITH
THE EXACT MISSING FIGURE THE PRIOR SEAT NAMED, AND THE KILL DID NOT MOVE — it moved one rung
lower.** Sixth consecutive session for the AI-infrastructure complex, third appearance for CRWV
itself. **That is a statement about how this complex is DISCLOSED, not about a candidate maturing.**

**The other entry worth reading is `T-2026-11-12-01` — Caterpillar, via Anthropic's ~$3.4B / 1.7 GW
generator commitment.** It died three times over: **rule (iii)** — the transaction was struck **late
September**, reported by the FT **11-08**, and a `--recency day` sweep served it as 24-hour news;
**the JOIN** — the primary source names only **OnePWR Solutions** (private), and **CAT is supplied by
secondary reporting citing a broadcaster**, with the source volunteering that even the $3.4B and the
OnePWR name sit in *different sentences*; and **part 2, a shape rule (viii) had not met** —
⚠⚠ **THE $3.4B BOUGHT OnePWR's ALREADY-PLACED ORDER BOOK, NOT NEW GENERATORS. Those units were
already in CAT's backlog; what changed is whose name is on them. A novation is not incremental
segment revenue, and the manufacturer is a bystander to its own backlog.**
⚠ **Disclosed on the record: Company A there is the company that makes the model running this
routine. It changes nothing — Anthropic is private and §3-dead and all three kills are structural —
but a seat researching its own maker's news should say so rather than let a later reader find it.**

See `research_log.md` `T-2026-11-12-01` … `-06`.

### SELL

**NONE — NO OPERAND.** `positions.md` satellite block count **0**
(`grep -cE '^### [A-Z]+ — T-'` = **0**); `alpaca.py positions` returns **one row, core VOO only**.
§5.1 and §5.2 were evaluated and have nothing to evaluate against: all four sell rules are
**ABSENT, NOT PASSING.** Core VOO is §5-exempt and was struck from the working list rather than
stamped as passing. **Zero §5.1 Perplexity calls were spent, because there is no position to check
news on.** **78th consecutive seat with an empty ledger.**

### REBALANCE

**NONE.** `sleeves` 07:01 ET: equity **$98,849.07** · core **VOO $68,849.07 = 69.65%** ·
satellite **$0 / 0.0% / count 0** · cash **$30,000.00 = 30.35%** · `core_in_band: true` ·
`rebalance_needed: false` · `rebalance_delta: 345.28`. **69.65% sits 4.65pp inside the 65%
edge.**
⚠ **Band distance in VOO terms, CARRIED NOT RE-DERIVED: the 65% floor needs VOO **562.51** and
the 75% ceiling **908.67** — identical to 11-06 through 11-11 **by construction**, because the
threshold is a function of the INERT CASH LEG ALONE (`cv = t·cash/(1−t)`, then `÷ qty`) and does
not move with the mark. The 11-09 seat's wrong first draft (563.42 / 910.14) came from
re-deriving it.** **NO REBALANCE DUE.**

---

## Revalidate

Nothing to revalidate — **no BUY intents.** The `revalidate` line names the specific number an
overnight gap could invalidate, and with no intent there is no number.

⚠ **One standing instruction that is NOT an intent:** if you execute nothing today, that is
correct and expected on this plan. Do **not** read an empty intent list as licence to construct
a trade at the point of execution — §4 requires the written thesis to pre-date the order, and
**no thesis dated today survived.**

⚠ **ONE SCHEDULED PRINT LANDS TOMORROW, NOT TODAY: PPI on 2026-11-13.** October CPI printed
overnight on 11-11 and is already an outcome, logged at `T-2026-11-11-04`: headline **+0.4% m/m**,
core **+0.3%**, both above consensus; futures moved to a near-certain December 25bp hike with ~15%
on 50bp; the 2-year rose 17bp to **4.73%** and the 10-year 10bp to **4.98%**. ⚠ **No new macro
print lands between this seat and today's open.** ⚠⚠ **And none of it is a reason to pre-position:
it is the standing government-action object — ONE PARTY, NO NAMED RECIPIENT, NO TRANSACTION — and
scale makes it more convincing, not more real.**

---

## Carry to the open seat

- **✅ NO BACKFILL IS DUE — FIFTH SESSION RUNNING, AND THIS SEAT VERIFIED IT RATHER THAN INHERITING
  IT.** The 11-11 close seat held past the bell and committed the official **VOO close 698.25**.
  `quote` at 07:01 returns `dailyBar.c` **698.25** — **the committed figure to the cent** — and
  `prevDailyBar.c` **689.415**, which is the committed **11-10** close to the thousandth. **Both
  committed marks are confirmed against the broker; neither needs correction and neither gets one.**
- **⚠ A SMALL BUT GENUINELY NEW FINDING, AND IT STRENGTHENS YESTERDAY'S CONCLUSION RATHER THAN
  REOPENING IT: THE PRINT COUNT ON A *COMPLETED* BAR IS NOT STABLE.** The 11-11 close seat committed
  **1,856 prints**; the same bar read this morning carries **n = 1,857** — one late-reported trade,
  with the close **unchanged at 698.25**. ⚠⚠ **The 11-11 seat had already FALSIFIED the print-count
  completeness heuristic by showing a partial bar's `n` EXCEEDING a prior completed bar's. This adds
  the other half of the proof: `n` is not even stable for a bar that has finished, so it could never
  have discriminated completeness in either direction.** ✅ **The standing rule is unchanged and now
  rests on two independent legs: ANY STEP 2 MUST GATE ON `clock`, NEVER ON THE SHAPE OF THE BAR.**
- **⚠ SERIES A — SECOND DATA POINT, AND THE RESOLVED EXPLANATION HOLDS; THE SERIES IS NOT REOPENED.**
  `positions.lastday_price` reads **698.35** against the official bar close **698.25** = **+$0.10**.
  The 11-11 11:41 seat established that this gap is **between two Alpaca endpoints**, never between
  Alpaca and this repo: `lastday_price` is a coarser field than `prevDailyBar`/`dailyBar`. ✅ **Today
  is a clean second confirmation at a similar magnitude (+$0.085 on 11-11, +$0.10 today). STANDING
  FIX UNCHANGED: read a prior close off `quote.prevDailyBar` / `quote.dailyBar`, never off
  `positions.lastday_price`.** ⚠ **Do not "correct" a committed mark toward the broker figure.**
- **Ledger reconciliation CLEAN, re-derived at this seat three independent ways, not inherited:**
  `positions.md` satellite count **0** · `sleeves satellite.count 0` · `positions` **core-only**.
  Core VOO **99.046311231 sh @ 706.74**, cost basis **$69,999.99**, unchanged since the
  2026-09-03 fill; only the mark moves. Mark **695.12** (pre-market, **not a close**); unrealised
  **−$1,150.92 / −1.6440%**. ⚠ **That figure equals the whole-account drawdown from $100,000 to the
  cent (−$1,150.93) for the seventh session running, because the cash leg has never moved — and it
  is an IDENTITY, not an agreement. `equity − (cost_basis + cash) ≡ core unrealised` with one
  position and no cash movement; it could not come out otherwise, so it confirms nothing.**
- **⚠⚠ THE §1 SHORTFALL IS A STANDING, MEASURED STRUCTURAL FINDING AND IT IS THE HUMAN'S CALL,
  NOT A SEAT'S.** With satellite at **0.0%** and $30,000 inert, the account captures only
  **69.65%** of any index move and **cannot beat the benchmark on any up session.** On 11-11 it
  cost **0.3912pp** on a **+1.2815%** index day. ⚠⚠ **LOWER BETA IS NOT ALPHA: the 11-10 pair
  measured both signs within 24 hours — a 0.728pp cost on an up day, an apparent +0.1107pp "gain"
  on a down day — and weight × VOO move predicts the account move identically, because the account
  IS core plus inert cash.** ⚠ **Recorded as the measured price of 78 honest no-trade seats,
  EXPLICITLY NOT as an argument for lowering §4's bar — manufacturing a thesis to close this gap is
  the one response that makes it worse.**
- **⚠ THE DIRECTION-BLIND `move` DEFECT — INSTANCE 17, AND IT IS THE FIRST GENUINE *RISE* IN FOUR
  READINGS.** `CAT` **+1.77%** (591.16 → 601.63) → `priced_in: false`, *"passes"* — the one recent
  case where "passes" and "has not already moved" actually agree, after three consecutive readings
  (11-11: CW −3.93%, CRWV −9.29%, VG −7.77%) where a **falling** stock read as late. ⚠ **The script
  thresholds ABSOLUTE 5-session magnitude. OBEY IT ANYWAY — it fails safe, over-blocking and never
  wrongly permitting — but NEVER quote such a reading as "the upside is captured".** ⚠⚠ **TODAY ALSO
  SHOWS THE CONVERSE AND IT IS THE MORE USEFUL HALF: THE FILTER SAID "GO" ON A THESIS WITH NO NAMED
  RECIPIENT, NO PRIMARY-SOURCE CANDIDATE AND NO INCREMENTAL DOLLAR. A HARD FILTER PASSING IS NOT
  PROGRESS.** Fix is a **signed** threshold in `scripts/alpaca.py`: script-level, **not a seat's to
  install.** Human notified 11-03, 11-05, 11-06, 11-09, 11-11, **11-12**.
- **⚠ FOUR SCRIPT-LEVEL DEFECTS REMAIN OPEN AND NONE IS A SEAT'S TO INSTALL:** (1) the
  direction-blind `move` threshold (17 instances); (2) `_parse_kv`'s hash truncation
  (`line.split("#", 1)[0]`) — **asserted hash-free before this commit**; (3) `get_bars` does no
  completeness filtering, so an in-progress session returns as a bar (`scripts/alpaca.py:109`);
  (4) `sleeves()` calls `get_account()` then `get_positions()` separately
  (`scripts/alpaca.py:136–137`), so `core_pct`'s numerator and denominator come from different
  instants — benign at 4.65pp of headroom, **not benign near a band edge.**
- **⚠ RULE (iv) ROLL-CALL FOR THE NEXT SEAT, so no drill query is wasted re-deriving a written
  answer:** **CRWV** (3 appearances: 10-19, 11-11, 11-12) · **Venture Global** (4) · **RTX** (6) ·
  **GE Vernova** (3). **All dead at part 1 or part 2 every time.** ⚠⚠ **AND THE NEW ENTRY ON THAT
  LIST IS A WHOLE COMPLEX, NOT A TICKER: the AI-datacenter supply tier is now SIX CONSECUTIVE
  SESSIONS of arrivals in six different disclosure shapes, and today it arrived carrying the exact
  figure the prior seat said was missing. EXPECT IT AGAIN TOMORROW; THE ANSWER IS WRITTEN.**
- **⚠ THE §5.4 STALENESS DETECTOR IS STILL UNPROVEN CODE AND "NOT DUE" HAS NOW BEEN RECORDED AS A
  GREEN CHECK 78 TIMES.** Field-form `grep -cE '^\s*-\s*highest_close:'` = **1** (the template
  placeholder `0.00` on a literal `YYYY-MM-DD` at `positions.md:53`); a bare `grep -c highest_close`
  returns **103** and **INVERTS the finding.** ⚠ **The first seat to inherit a real position must
  treat its own detector as UNTESTED and check the `(as of …)` date BY HAND.**
