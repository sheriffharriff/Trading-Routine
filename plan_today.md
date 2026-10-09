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

If the pre-market run failed, was skipped, or crashed before writing, this file still holds
yesterday's intents. Executing them would be running stale research as though it were
fresh — the candidate has had another full session to move, and the §4 priced-in check that
cleared it was performed against prices that no longer exist. Doing nothing is strictly
better. Core and rebalance actions are exempt from the gate because neither depends on the
day's research.

```
plan_date: 2026-10-09
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-09 at 09:30 ET** (`alpaca.py clock` at 08:27:45 ET: `is_open:
false`, `next_open: 2026-10-09T09:30:00-04:00`, `next_close: 2026-10-09T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** Both `next_open` and `next_close` carry **today's**
date, which is the full-session signature: not an early close.

**One pre-market run today, at 08:27 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$100,743.83** at pre-flight).

⚠ **This file arrived carrying `plan_date: 2026-10-08` — exactly one trading day old, which is
correct.** The predecessor was fresh and deliberately empty. ⚠⚠ **AND THE REASON TO SAY SO AGAIN:
A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. Freshness is
read OFF `plan_date` and NEVER inferred from the outcome.** **The staleness gate's non-exercise count
will be **37** after today's open; it has never fired, and its alert path remains untested code.**
⚠ **A correct `plan_date` is one TRADING day old, not one calendar day — today is Friday, so
tomorrow's comparison is against Monday's and will legitimately read three calendar days.**

⚠ **THE PREVIOUS THREE SESSIONS WERE ALL COMPLETE — ALL FOUR SEATS OF 10-06, 10-07 AND 10-08 RAN AND
COMMITTED.** ⚠⚠ **THAT IS NOT A FIX AND A RUN OF THREE IS NOT EVIDENCE EITHER: the failure mode is a
seat that never STARTS, so a session that completed says nothing about the next one in either
direction. Two of ~28 close runs have vanished (09-28, 10-05), there is still no detector for a
missing seat, and `alerts.md` reading "zero open incidents" cannot distinguish a healthy week from a
run that died before `commit.py`. Open item (11) stands exactly where it did.**

---

## Tape context

**LAST COMPLETED SESSION: 2026-10-08** (official close basis, inherited from the 16:16 close seat's own
`bars --days 3 --adjustment all` pull, **not re-derived here**): VOO **c 711.23**, equity
**$100,444.7079**, core **70.1328%**, day **−0.3371%**, since inception **+0.4447%**.

**LIVE BROKER MARK, 2026-10-09 08:27 (a DIFFERENT SERIES — NEVER CONCATENATED WITH THE ABOVE):**
`sleeves` equity **$100,749.77**, core **$70,749.770575 = 70.22%**, cash **$30,000.00 = 29.78%**,
`rebalance_delta` **−$224.93**, `core_in_band: true`, `rebalance_needed: false`.
`positions` VOO: qty **99.046311231**, avg_entry **706.74** (a RAW print), cost_basis **$69,999.99**,
market_value **$70,749.770575**, unrealized **+$749.78 (+1.071%)**, `current_price` **714.31**,
`lastday_price` **711.28**, `change_today` **+0.426%**.

⚠ **`lastday_price` 711.28 sits +$0.05 against the official 10-08 close of 711.23 — the known
broker/official divergence. DO NOT RE-OPEN WHY; four mechanisms have been falsified and both signs
observed. It must NEVER be differenced against an official close.**
⚠ **NEVER `equity − last_equity` as a day's P&L; never `unrealized_intraday_pl` or `change_today`.
Close-to-close from `bars` on a COMPLETED session, basis STATED; a fresh `quote` for execution.**
⚠ **§6's 5% cap on the live mark is **$5,037.49**. It has no operand only because this plan carries no
buy intent.**

**PRE-MARKET BROKER/OFFICIAL SAMPLE — A FOURTH, AND IT CHANGES NOTHING:** `current_price` **714.31**
against the official 10-08 close **711.23** = **+$3.08**. Prior pre-market samples: −$0.22 (10-05),
+$2.84 (10-06), −$3.05 (10-07). **FOUR SAMPLES, BOTH SIGNS, A FOURTEEN-FOLD MAGNITUDE SPREAD — NO
OFFSET SURVIVES AND NO DIRECTION IS READABLE.** ⚠ **Reported as a sample, not as a calibration.**

---

## Reconciliation

**`positions.md` AND THE LIVE BROKER AGREE.** `alpaca.py positions` returns **one row, core VOO**
(99.046311231 shares, avg_entry 706.74, unchanged since the 2026-09-03 fill) against **zero satellite
blocks in `positions.md`.** ⚠ **Core VOO was struck from the working list BEFORE any §5 rule was read,
per §5's core exemption — it is not a satellite operand and is not tracked in that ledger.**
⚠ **This is the session's FIRST reconciliation, so the reconciliation counter advances; the
§5-operand session counter does NOT — see the counters note below.**

**WEEK ROLLOVER: NOT DUE.** Computed ISO Monday of **2026-10-09** (Friday, ISO week 41, weekday 5) is
**2026-10-05**, which **MATCHES** `week_of` in `state.md`. **`new_positions_this_week` stays 0.**
⚠ **Checked here rather than relying on the Friday review, so a failed Friday run cannot leave the §6
weekly cap stuck at its limit.**

**CIRCUIT BREAKER: INACTIVE.** `consecutive_closed_losses: 0`, `halt_triggered_at: none` — so **no
`HALT_CLEARED_AT` comparison was due** and none was made. ⚠ **The streak CANNOT MOVE while the sleeve
is empty: the increment path and the circuit-breaker alert path both remain UNTESTED CODE.**

**ALERTS: ZERO OPEN INCIDENTS.** ⚠⚠ **AND THAT IS NOT EVIDENCE EVERY SEAT RAN — a run that dies before
`commit.py` leaves no trace by construction. The file cannot report what never started.**

**COUNTERS, EACH STATED WITH ITS UNIT IN THE SAME BREATH (catch 21/22):**
- **§5-operand counter: 27 completed sessions / 24 post-fill — AND IT DOES NOT ADVANCE HERE.** The unit
  is a **COMPLETED** session and **this seat stands BEFORE the bell on 10-09**, so today is not
  countable from here. The last completed session is 2026-10-08, already counted by that day's 16:16
  seat. ⚠⚠ **THIS IS THE EXACT TRAP CATCH (22) RECORDS: the 10-08 08:25 pre-market seat stated this rule
  correctly and then wrote "27 completed sessions" forty-four lines later in this same file, and the
  number happened to become correct by a different route within one session, so the error was invisible
  after a day. 27 IS THE FIGURE AND IT IS NOT ADVANCING. Routines 1 and 2 may NEVER count the day they
  stand in; routine 4 always may; routine 3 never may.**
- **Thesis counter: 138 — AND IT DOES ADVANCE HERE, because its unit is a thesis WRITTEN and this seat
  wrote eight.** **RE-DERIVED FROM SOURCE RATHER THAN INHERITED:** `archive/research_log/2026-09.md`
  **87** + live October **43** (6 on 10-01 · 5 on 10-02 · 7 on 10-05 · 8 on 10-06 · 7 on 10-07 · 10 on
  10-08, counted by date from the file) = **130**, + **8** written today = **138**. ⚠ **Two counters
  over one date, one advancing and one not, and only the UNIT says which. DO NOT RECONCILE THEM AGAINST
  EACH OTHER — RECOMPUTE EACH AGAINST ITS OWN UNIT.**
- **Band counter: 75th consecutive run inside §2's band.** Unit is a RUN, which is why it advances
  where the session counter does not.

---

## Intents

### BUY

**NONE. ⚠⚠ ZERO BUY INTENTS, AND NOT BECAUSE ANYTHING BLOCKED THEM.**

⚠ **Every §6 and §7 gate was OPEN and this must not be lost between here and 09:35:** breaker
**INACTIVE** · `new_positions_this_week` **0 of 3** · satellite sleeve **0% deployed** against a 30%
target with **$30,000 idle cash** · `control.md` notes **empty** · `TRADING_ENABLED: true` · §6's 5%
cap standing ready at **$5,037.49**. **A buy could have been placed today. Nothing was worth buying.**

**Eight candidates were researched and all eight were rejected** (`T-2026-10-09-01` … `-08`). The
kills, one line each, so the 09:35 seat need not re-read the log to know nothing is pending:

| ID | Candidate | Test that failed |
|---|---|---|
| **-01** | **GFS / TSMC $2B silicon interposers** | **part 3 — H1 2028 ramp, SIX quarters vs a two-quarter ceiling** · part 2 — ~$400M/yr on $6.791B rev = **5.89%**, under the 10% floor · part 1 — **GFS is the headline name**, no Company B named |
| -02 | **RTX** / DoD SM-3 Block IB "up to $6.3B" | settled defence pattern (10th instance) · first-order · **"up to" = ceiling** · govt counterparty · **rule (iv), RTX's 3rd appearance** |
| -03 | **RIG** / Norske Shell $62M + Equinor $1.0B | §3 cap **~$6.19B** · first-order · **the $1.0B leg is PREVIOUSLY ANNOUNCED (rule iii)** |
| -04 | **MTUS** $995M DLA ceiling | **exact repeat of `T-2026-10-01-05`** · ceiling not a figure · first-order · §3 |
| -05 | Voyager / SCO $22.4M | **exact repeat of `T-2026-10-06-06`** · re-report with a fresh date (rule iii) · §3 · govt counterparty |
| -06 | White House "Genesis Mission" $2.4B / 11 cos | **no Company A** (govt action) · aggregate ~$218M each — 10% test and $10B floor **jointly unsatisfiable** |
| -07 | **FTI** / Petrobras subsea flexibles | part 2 — **"significant" = a self-defined $75–250M BAND, not a figure** · first-order |
| -08 | §3 scope sweep, **eleven items** | §3 — non-US, private or microcap; nine excluded by the source itself |

⚠⚠ **THE ONE THE HUMAN SHOULD READ IS `-01`, AND IT IS THE MOST BUYABLE-LOOKING OBJECT THIS FUNNEL HAS
PRODUCED IN WEEKS.** GlobalFoundries' own dated press release · two named parties · **$2B attributed to
the US-listed leg by Reuters and Bloomberg** · **no rule (iii) problem** (no earlier GF disclosure of a
TSMC interposer agreement exists) · **every §3 instrument test passed** · **and the priced-in filter
passed on BOTH bases** (+1.48% over five sessions; **+2.72% on the news day itself**, 48.065 → 49.37).
⚠⚠ **CORRECTED BEFORE PUBLICATION — CATCH (23).** This section first called GFS the **FIRST** candidate
to clear §3's instrument tests and the priced-in filter and then die on §4's parts. **THAT IS FALSE.**
**IT IS THE *SECOND* CANDIDATE TO CLEAR §3's INSTRUMENT TESTS AND THE PRICED-IN FILTER AND THEN DIE ON §4's PARTS — **AMD** (`T-2026-10-01-02`) DID IT FIRST ON 10-01, WITH A *STRONGER* §3 PASS (cap "far above the $10B" floor, where GFS's is UNRESOLVED) AND THE SAME PRIMARY KILL, PART 3.** ⚠ **The refuting entry was in `research_log.md`, a file this run had already read —
catch (13)'s exact shape, and it would have shipped as this run's headline finding in three files.**
⚠⚠ **WHAT SURVIVES IS NARROWER AND IS THE PRICED-IN HALF: AMD's pass was on a −0.52% NON-EVENT drift;
GFS's is on a GENUINE NEWS DAY (4x trades, 6x volume, a real transaction). THAT is first of its kind.**
⚠ **And the non-superlative observation is the useful one: PART 3 KILLED BOTH. Of the two candidates
ever to reach §4's parts with the filters behind them, the TIMING WINDOW killed both.**
⚠ **Both of GFS's killing numbers came out of the company's own release in one step each. §4's parts did
the work; no judgment call was required.**

⚠⚠ **AND THE PRICED-IN FILTER WAS GENUINELY EXERCISED THIS RUN — THE FIRST `move` CALL IN SEVEN
SESSIONS, AND IT WAS NOT DECORATIVE.** GFS reached the filter carrying a real mechanism and a real
disclosed figure, which is precisely the case the filter exists for. ⚠ **It is also the FIRST RECORDED
INSTANCE OF THE FILTER WORKING BY *ACCEPTING* A GENUINE NEWS-DAY MOVE** — every prior "filter working"
instance (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%) was it working by REJECTING. ⚠ **Stated with its
limit, which matters: 10-08 traded to **51.42, +6.98% over the prior close**, and closed **−3.99% off
that high.** A close-to-close filter cannot see that excursion, and had the close held near the high the
same news would have FAILED the filter. **The filter was right here and not by a wide margin.**

⚠ **THREE OF THE EIGHT WERE DISPOSED REJECTS RETURNING** — MTUS ($995M, from 10-01), Voyager ($22.4M,
from 10-06) and Elevra/LG (from 10-08's sweep). **The funnel is now re-serving its own disposed items,
which is a reason to read the log BEFORE the tape. Reading it cost one grep and saved three queries.**

⚠ **The honest-broker line, because the pressure to skip it is exactly why it is written down: 27
completed sessions, 138 theses, ZERO POSITIONS EVER OPENED, and 29.78% of the book in idle cash. §2
permits the cash and §4 says most runs end in no trade. Both rules were followed. That is not an
argument for lowering the bar — and if the bar is to move, it is a `strategy.md` change and ONLY THE
HUMAN MAY MAKE IT.**

### SELL

**NONE. ⚠ §5 HAD NO OPERAND — there are zero satellite positions to sell.** Core VOO is **exempt from
all four sell rules** (§5) and **must not be sold to fund anything** (§7). ⚠ **No position is queued
for exit, nothing is near a stop, and "nothing is near a stop" is a statement about an EMPTY SET —
read it as "UNDEFINED", not as "comfortable".** ⚠ **Zero Perplexity news-on-holdings queries were due
and zero were run: Step 4.1's query is written for a named company and there is none.**

### REBALANCE

**NONE. Core is 70.22% on the live 08:27 mark — inside §2's 65–75% band by 5.22 points at the lower
edge and 4.78 at the upper.** `rebalance_needed: false`.
⚠ **`rebalance_delta: −$224.93` is a DISTANCE READOUT, NOT AN INSTRUCTION** — §2 acts at the band
**edge**, not at the 70% target, and core sits fractionally ABOVE target rather than outside the band.
⚠⚠ **DO NOT DIFFERENCE SUCCESSIVE `rebalance_delta` READINGS INTO A TREND. Thirteen readings now span
10-06 through today with NO ORDER ANYWHERE IN THE INTERVAL and the sign of the change has flipped nine
times. There is no direction in this field to read.**
⚠ **State the live reading against the two edges. DO NOT CARRY A RANGE (catch 18) — a range over a live
moving mark is correct when written and false at the next seat.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate. This plan carries no BUY, no SELL and no REBALANCE intent.**
⚠ **There is therefore NO `revalidate` line in this plan, and that is correct rather than an omission:
the field names the specific number an intent must be re-checked against, and there is no intent.**

⚠ **Do NOT read an empty plan as permission to skip the gate.** Specifically, at 09:35:

1. ⚠⚠ **READ `plan_date` OFF THIS FIELD. It is `2026-10-09`.** Do not infer freshness from the fact
   that the plan is empty — **a fresh empty plan and a stale plan produce a byte-for-byte identical
   zero-order run.** Record which one you had. **Non-exercise count 37 after today.**
2. **Confirm all eight thesis IDs `T-2026-10-09-01` … `-08` are present and REJECTED in
   `research_log.md`** before concluding there is nothing to execute. **None is a buy candidate.**
3. **Step 3's core bootstrap is skipped on `core_established: true`** — a path that ran once on
   2026-09-03 and by construction never runs again. **Do not re-bootstrap.**
4. **Re-check sleeves on live numbers.** If core has left the 65–75% band overnight, §2's rebalance is
   **exempt from the plan_date gate** and is yours to place. At 08:27 it was 70.22% with 4.78 points of
   headroom at the near edge, so this is a check, not an expectation.
5. ⚠⚠ **DO NOT STAMP CORE VOO WITH A `highest_close`.** A mark on VOO would **fabricate a §5.4 trailing
   stop on the one position §5 exempts**, which §7 forbids outright. **This will be the 84th
   consecutive run declining it.** ⚠ **The cost of having written it is now a MEASURED number, not a
   hypothetical: a mark stamped at 10-06's 716.29 leaves 10-08's close −0.7064% below it, three
   sessions of phantom drawdown already accrued toward §5.4's −10%.** ⚠ **A refusal repeated 84 times
   is a refusal nobody is deciding any more, and automatic is not sound — re-make it, do not inherit it.**
6. ⚠⚠ **STEP 6's `voo_close_at_entry` IS DEFECTIVE AT YOUR SEAT AND IT IS OPEN ITEM (12).** `bars
   --days 1` at ~09:36 returns a bar dated TODAY that is **PARTIAL** — measured at `n` 156 / `v` 2,029
   six minutes into the 10-06 session, with its `c` field being **the last trade so far wearing a
   close's clothes.** ⚠ **An `n`/`v` sanity check CANNOT save it: a complete session bar read n 1,323 /
   v 23,415 on 10-07, below every recent floor.** ⚠ **It costs nothing today ONLY because no position
   will be opened. If that ever changes, use the PRIOR completed session's close named on its basis, or
   defer the label to the close run. A PROMPT FIX, NOT YOURS TO MAKE.**
7. ⚠ **If you make no `move` call, say it is an ABSENT check, not a passing one.** A decorative
   priced-in call on a name with no mechanism converts an honest absence into a fake exercise.
   ⚠ **Today's seat DID make one, on GFS, and it was legitimate — a reached candidate with a mechanism
   and a figure. That is the distinction.**
8. ⚠ **The dividend test is CLOSED — branch (a), the platform does not model dividends. Do NOT re-read
   `cash` for this purpose and do not restart the retired counter.** Report cash as an ordinary balance.
9. ⚠ **DO NOT REHABILITATE `T-2026-10-09-01` (GFS) AT A DIFFERENT PRICE.** It did not die on price — it
   died on the **calendar** (H1 2028) and on **materiality** (5.89%), and neither moves with the quote.
   ⚠ **"But it has not run yet" is the same pull as "but it went up", which ELMT is the standing proof
   against.**

**Nothing in this plan requires an order. The correct 09:35 run places zero trades.**

---
