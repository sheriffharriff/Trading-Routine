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
plan_date: 2026-10-12
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-12 at 09:30 ET** (`alpaca.py clock` at 08:36:59 ET: `is_open:
false`, `next_open: 2026-10-12T09:30:00-04:00`, `next_close: 2026-10-12T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** Both `next_open` and `next_close` carry **today's**
date, which is the full-session signature: not an early close.
⚠ **The data plane agrees, which corroborates the DISCRIMINATOR and not any bar's
completeness: `bars --days 4 --adjustment all` returns **NO bar dated 2026-10-12**, the same
pre-market shape observed at 08:23 on 10-06 before the 09:36 seat watched it appear.**

**One pre-market run today, at 08:36 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$100,879.52** at pre-flight).

⚠⚠ **THIS FILE ARRIVED CARRYING `plan_date: 2026-10-09` — THREE CALENDAR DAYS OLD, AND THAT IS
CORRECT, NOT STALE.** The comparison is against the last **TRADING** day, not the calendar, and
10-09 was Friday. **The Friday review predicted this shape in advance and it arrived exactly as
described.** ⚠⚠ **AND THE REASON TO SAY SO AGAIN: A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A
BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. Freshness is read OFF `plan_date` and NEVER inferred from
the outcome.** The predecessor was fresh and deliberately empty, and so is this one. **The staleness
gate's non-exercise count will be 38 after today's open; it has never fired, and its alert path
remains untested code.**

⚠ **THE PREVIOUS FOUR SESSIONS WERE ALL COMPLETE — ALL FOUR SEATS OF 10-06, 10-07, 10-08 AND 10-09
RAN AND COMMITTED, PLUS THE FRIDAY REVIEW.** ⚠⚠ **THAT IS NOT A FIX AND A RUN OF FOUR IS NOT EVIDENCE
EITHER: the failure mode is a seat that never STARTS, so a session that completed says nothing about
the next one in either direction. Two of ~28 close runs have vanished (09-28, 10-05), there is still
no detector for a missing seat, and `alerts.md` reading "zero open incidents" cannot distinguish a
healthy week from a run that died before `commit.py`. Open item (11) stands exactly where it did.**
**`alerts.md` reads ZERO OPEN INCIDENTS today, reported as an ABSENCE OF EVIDENCE rather than as
health.**

---

## Tape context

**LAST COMPLETED SESSION: 2026-10-09** (official close basis, `bars --symbol VOO --days 4
--adjustment all` pulled at this seat: o 713.52 h 716.37 l 712.75 **c 715.58**, n 1,645 v 70,028,
vw 715.336895 — a normal full session). **Re-derived here and it AGREES WITH THE CLOSE SEAT'S FIGURE
TO THE CENT:** 99.046311231 × 715.58 + 30,000 = equity **$100,875.5594**, core **$70,875.5594 =
70.2604%**, cash **29.7396%**. Day **+$430.8515 = +0.4289%** against 10-08's official $100,444.7079.
**Since inception +0.8756%.** Core unrealized **+$875.57 (+1.2508%)** on cost_basis $69,999.99.
⚠ **VOO itself was +0.6116% (715.58 vs 711.23), so the book LAGGED by 0.1827pp — ON THE CASH FLOAT,
NOT ON SKILL. The 29.74% cash leg earns nothing on an up day and loses nothing on a down one; it is
the same mechanism in both directions and only one of them flatters.**

**LIVE BROKER MARK, 2026-10-12 08:36 (a DIFFERENT SERIES — NEVER CONCATENATED WITH THE ABOVE):**
`sleeves` equity **$100,874.57**, core **$70,874.568928 = 70.26%**, cash **$30,000.00 = 29.74%**,
`rebalance_delta` **−$262.37**, `core_in_band: true`, `rebalance_needed: false`.
`positions` VOO: qty **99.046311231**, avg_entry **706.74** (a RAW print), cost_basis **$69,999.99**,
market_value **$70,874.568928**, unrealized **+$874.58 (+1.249%)**, `current_price` **715.57**,
`lastday_price` **715.59**, `change_today` **−0.003%**.

⚠ **A FIFTH SAMPLE OF THE MOVING LIVE MARK, TAKEN MINUTES APART AT ONE SEAT: `selftest.py` read
equity **$100,879.52** and `sleeves` read **$100,874.57** — a **$4.95** spread on the same quantity.
THE TWO MUST NOT BE DIFFERENCED INTO ANYTHING.** An equity figure is meaningless without its CALL
and its TIMESTAMP.
⚠⚠ **PRE-MARKET BROKER/OFFICIAL SAMPLE — A FIFTH, AND IT IS THE SMALLEST YET BY AN ORDER OF
MAGNITUDE:** `current_price` **715.57** against the official 10-09 close **715.58** = **−$0.01**.
Prior pre-market samples: −$0.22 (10-05), +$2.84 (10-06), −$3.05 (10-07), +$3.08 (10-09). **FIVE
SAMPLES, BOTH SIGNS, A THREE-HUNDRED-FOLD MAGNITUDE SPREAD.** ⚠⚠ **A ONE-CENT GAP IS NOT A
CALIBRATION AND MUST NOT BE READ AS ONE — IT IS THE SERIES' STRONGEST WARNING YET, BECAUSE A SAMPLE
THAT HAPPENS TO AGREE IS THE ONE MOST LIKELY TO BE MISTAKEN FOR AN OFFSET OF ZERO.** The 10-06
precedent is the direct instance: a pre-market mark that was byte-identical to a later reading was
**indistinguishable from a lagged mark on one sample.** ⚠ **It must NEVER be differenced against an
official close, today least of all.**
⚠ **`lastday_price` 715.59 sits +$0.01 against the official 10-09 close of 715.58 — the known
broker/official divergence, and within a session this field behaves as a FIXED prior-day field while
`current_price` moves. DO NOT RE-OPEN WHY; four mechanisms have been falsified and both signs
observed.**
⚠ **NEVER `equity − last_equity` as a day's P&L; never `unrealized_intraday_pl` or `change_today`.
Close-to-close from `bars` on a COMPLETED session, basis STATED; a fresh `quote` for execution.**
⚠ **§6's 5% cap on the live mark is **$5,043.73**. It has no operand only because this plan carries
no buy intent.**

---

## Reconciliation

**`positions.md` AND THE LIVE BROKER AGREE — THIS WAS THIS RUN'S FIRST JOB AND IT IS CLEAN.**
`alpaca.py positions` returns **one row, core VOO** (99.046311231 shares, avg_entry 706.74,
cost_basis $69,999.99, unchanged since the 2026-09-03 fill) against **zero satellite blocks in
`positions.md`.** `sleeves` reports `satellite.count: 0`. **No discrepancy, nothing to flag, and no
research was done on top of a ledger in doubt.**
⚠ **Core VOO was struck from the working list BEFORE any §5 rule was read, per §5's core exemption —
it is not a satellite operand and is not tracked in that ledger.**

**HOUSEKEEPING — ALL THREE ITEMS RESOLVED TO "DO NOTHING, FOR THE RIGHT REASON":**

1. ⚠⚠ **WEEK ROLLOVER: COMPUTED AND MATCHING, SO DELIBERATELY NOT RE-RESET.** Today is **Monday
   2026-10-12**, so the ISO week anchor **IS** 2026-10-12, and `state.md` already carries
   `week_of: 2026-10-12` — **performed in the field by the 10-09 Friday review, which wrote the
   warning not to reset it again.** `new_positions_this_week` stays **0 of 3**. ⚠ **The anchor was
   RECOMPUTED here rather than read, per the standing rule that the cap must not stay stuck at its
   limit if a Friday run fails; it simply agreed.**
2. **CIRCUIT BREAKER: INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`. ⚠ **No
   `HALT_CLEARED_AT` comparison is due, and `control.md` reads `HALT_CLEARED_AT: none` anyway. The
   §6 halt is not blocking anything today — see the BUY section, which is empty for other reasons.**
3. **SLEEVE DRIFT: NONE ACTIONABLE.** Core **70.26%** against a 70% target, **inside the 65–75%
   band** with 4.74 points of headroom at the near edge. ⚠ **NO REBALANCE INTENT IS QUEUED.**
   `rebalance_delta` **−$262.37** is a **distance readout, not an instruction** — §2 rebalances on
   leaving the band, not on being off target. The Friday review's handoff numbered this the **79th
   consecutive in-band reading**; that figure is **inherited-and-incremented, not re-derived.**

**CONTROL FILE:** `TRADING_ENABLED: true`, **LIVE** against the paper account; **Notes: (none)** —
no human instruction restricts this run. ⚠ **Neither `strategy.md` nor `control.md` was written by
this run; both were read.**

---

## §5 sell-rule review

**THERE IS NO SATELLITE POSITION, SO ALL FOUR RULES HAVE *NO OPERAND* — WHICH IS NOT THE SAME AS
PASSING, AND NOT THE SAME AS "NOTHING NEAR TRIGGERING".**

⚠⚠ **RE-EVALUATED IN §5's ORDER AT THIS SEAT RATHER THAN INHERITED, AND THE RESULT IS THE SAME
NULL:** **5.1** — there is no `invalidation` string anywhere in `positions.md` to read verbatim, and
**ZERO Perplexity news-on-holdings queries were due and ZERO were run**, because Step 4's query is
written for a named company and there is none. **5.2** — no `timing_window` and no deadline field
exists, so no window can have passed. **5.3** — no satellite `entry_price`, so the −7% hard stop has
no reference. **5.4** — `highest_close` is **ABSENT, the third state, carrying no `(as of …)` date at
all**, so the trailing stop does not exist to be measured against.
⚠ **The distance to each rule is therefore **UNDEFINED**, not "large". Those are different facts, and
"nothing is close to triggering" would be a fabrication: nothing can be close to a threshold it has
no operand for.**
⚠ **NOTHING WAS QUEUED FOR THE MIDDAY SEAT, because 5.3 and 5.4 have no operand to breach either.**
**§5.1–§5.4 have never had an operand: 28 completed sessions since 2026-09-01, 25 post-fill, zero
satellite positions ever.** ⚠ **The session counter **DOES NOT ADVANCE HERE** — the unit is a
*COMPLETED* session and this seat stands BEFORE the bell on 10-12, while 10-09 was already counted by
that day's close seat. **DO NOT "FIX" 28 TO 29.** This is catch (21)'s shape for the eighth time and
catch (22) is the worked failure of getting it right and then writing the advanced number anyway.**
⚠ **NO HIGH-WATER BACKFILL IS DUE, AND NOT BECAUSE A MARK IS CURRENT — there is nothing to write.
The backfill path remains unexercised code and has now been saved by the empty sleeve three times.**

---

## Intents

### BUY

**NONE. ⚠⚠ ZERO BUY INTENTS, AND NOT BECAUSE ANYTHING BLOCKED THEM.**

⚠ **Every §6 and §7 gate was OPEN and this must not be lost between here and 09:35:** breaker
**INACTIVE** · `new_positions_this_week` **0 of 3** · satellite sleeve **0% deployed** against a 30%
target with **$30,000 idle cash** · `control.md` notes **empty** · `TRADING_ENABLED: true` · §6's 5%
cap standing ready at **$5,043.73**. **A buy could have been placed today. Nothing was worth buying.**

**Five candidates were researched and all five were rejected** (`T-2026-10-12-01` … `-05`). The
kills, one line each, so the 09:35 seat need not re-read the log to know nothing is pending:

| ID | Candidate | Test that failed |
|---|---|---|
| **-01** | **US/Russia diesel supply arrangement, 10-09** (300k tons immediately, 500k in Nov, 1M thereafter; OFAC licence to 2027-04-07) | **part 1 — NO Company B, by EXPLICIT SOURCE DENIAL**: *"no specific publicly traded U.S. company is named"* and *"No dollar amount is attributed to any named U.S.-listed company"* · part 2 — **tonnages are not dollars** · the two named parties are **SOVEREIGN STATES** |
| -02 | **RTX** / SM-3 Block IB *"up to $6.3B"* | **EXACT REPEAT of 10-09, re-served TWICE in one run** · first-order · **"up to" = ceiling** · govt counterparty · **rule (iv), RTX's 4th appearance in seven sessions** |
| -03 | **§3 / non-qualifying sweep, THIRTEEN items** | §3 — non-US, private or microcap · rule (iii) on two · rule (v) on three · **two are not transactions at all** |
| -04 | macro/fiscal complex (UMich expectations; FY2026 deficit ~$2T, net interest >$1T, corporate tax receipts −16% to $382B) | **no Company A** — a government or macro datum names nobody |
| -05 | the **FORWARD CALENDAR** (JPM/C/WFC reporting 10-13; CPI 10-14; PPI + retail sales 10-15) | **nothing has happened yet** — a calendar is not news; the named banks are **scheduled reporters** |

⚠⚠ **THE ONE THE HUMAN SHOULD READ IS `-01`, AND IT IS A FINDING ABOUT THIS LOG'S OWN METHOD RATHER
THAN ABOUT A CANDIDATE.** For six sessions this log has promoted the **structural query framing** —
*ask for two named parties, a disclosed dollar amount and the announcement date* — on the theory that
naming §4's required shape returns that shape or an honest refusal. **IT HAS A FALSE-POSITIVE FORM AND
THIS IS IT.** The diesel arrangement carries **two named parties, a precise date, a dated delivery
schedule, a regulatory instrument with an expiry, and a four-rung quantity ladder** — the whole shape —
**and it is untradeable, because the parties are STATES and the quantity is NOT MONEY.**
⚠ **THE FIX IS ADDITIVE AND CHEAP: the structure must also satisfy PARTY TYPE (both parties
companies) and UNIT (dollars, at Company B). "It returned the shape" is no longer sufficient grounds
to proceed to a mechanism.** ⚠ **The framing is not weakened — it is still the query that reaches the
funnel's actual inventory, and it disposed eight items with reasons attached today for zero follow-up
queries.**
⚠⚠ **THE PRIORS ARRIVED INSTANTLY, AGAINST AN EXPLICIT DENIAL, AND NONE IS WRITTEN DOWN AS A
CANDIDATE: the refiner complex (VLO/MPC/PSX) and the fuel-cost tier (DAL/UAL/UPS/FDX).** ⚠ **The
second set is the more seductive because a COST-LINE improvement is a form §4 part 1 explicitly
permits — and it fails on three independent grounds: airlines burn JET FUEL not diesel (the path needs
a substitution clause, which is the "and also" kill); a commodity price is a MARKET VARIABLE, the
shared-cause object in its purest form; and a presidential statement with no executed commercial
contract is not a transaction to be second to.**
⚠ **AND THE EVENT-TYPE OBSERVATION, WHICH IS RULE (iv) ONE LEVEL UP: this is the SECOND
diesel-release item in six sessions (the G7 release was disposed 10-05) and it died the same death
both times. A recurring EVENT TYPE is a warning about a news cycle's disclosure practice, exactly as
a recurring TICKER is — and that had not been written down.**

⚠⚠ **ZERO `move` CALLS AT THIS SEAT — AN *ABSENT* CHECK, NOT A SKIPPED OR A PASSING ONE.** Four of
the five rejects **carry no ticker at all**, the fifth is a disposed repeat on a first-order name, and
the thirteen-item sweep died at §3 upstream of the filter. ⚠ **A decorative `move` call on a name with
no mechanism converts an honest absence into a fake exercise; declined for that reason a third time.**
⚠ **NOT COUNTABLE AS A ZERO-`move` SESSION FROM HERE — THREE SEATS REMAIN TODAY.**

### SELL

**NONE. No satellite position exists to sell.** ⚠ **Core VOO is exempt from all four §5 rules and is
never sold on news (§5, §7).**

### REBALANCE

**NONE.** Core **70.26%**, inside §2's 65–75% band. ⚠ **See Reconciliation item 3 — `rebalance_delta`
is a distance readout, not an instruction.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate. This plan carries no BUY, no SELL and no REBALANCE intent.**
⚠ **There is therefore NO `revalidate` line in this plan, and that is correct rather than an omission:
the field names the specific number an intent must be re-checked against, and there is no intent.**

⚠ **Do NOT read an empty plan as permission to skip the gate.** Specifically, at 09:35:

1. ⚠⚠ **READ `plan_date` OFF THIS FIELD. It is `2026-10-12`, and today is 2026-10-12 — FRESH.** Do
   not infer freshness from the fact that the plan is empty — **a fresh empty plan and a stale plan
   produce a byte-for-byte identical zero-order run.** Record which one you had. **Non-exercise count
   38 after today.** ⚠ **The first morning the gate fires will by construction be a morning when the
   pre-market run failed. Read your own Step 2 then; do not recall it.**
2. **Confirm all five thesis IDs `T-2026-10-12-01` … `-05` are present and REJECTED in
   `research_log.md`** before concluding there is nothing to execute. **None is a buy candidate, and
   four of the five carry no ticker.**
3. **Step 3's core bootstrap is skipped on `core_established: true`** — a path that ran once on
   2026-09-03 and by construction never runs again. **Do not re-bootstrap.**
4. **Re-check sleeves on live numbers.** If core has left the 65–75% band overnight, §2's rebalance is
   **exempt from the plan_date gate** and is yours to place. At 08:36 it was 70.26% with 4.74 points of
   headroom at the near edge, so this is a check, not an expectation.
5. ⚠⚠ **DO NOT STAMP CORE VOO WITH A `highest_close`.** A mark on VOO would **fabricate a §5.4
   trailing stop on the one position §5 exempts**, which §7 forbids outright. **This will be the 89th
   consecutive run declining it** (the count is inherited-and-incremented, not re-derivable from
   source). ⚠ **The cost of having written it is a MEASURED number, not a hypothetical: a mark stamped
   at 10-06's 716.29 leaves 10-09's close −0.0991% below it — the phantom drawdown SHRANK again this
   session, and catch (25) is the standing warning that the inherited "it grows on its own" claim was
   itself wrong. An inherited claim that argues for what you already intend to do is the one you are
   least likely to audit.** ⚠ **A refusal repeated 89 times is a refusal nobody is deciding any more,
   and automatic is not sound — RE-MAKE IT, DO NOT INHERIT IT.**
6. ⚠⚠ **STEP 6's `voo_close_at_entry` IS DEFECTIVE AT YOUR SEAT AND IT IS OPEN ITEM (12).** `bars
   --days 1` at ~09:36 returns a bar dated TODAY that is **PARTIAL** — measured at `n` 156 / `v` 2,029
   six minutes into the 10-06 session, with its `c` field being **the last trade so far wearing a
   close's clothes.** ⚠ **An `n`/`v` sanity check CANNOT save it: a complete session bar read n 1,323 /
   v 23,415 on 10-07, below every recent floor.** ⚠ **It costs nothing today ONLY because no position
   will be opened. If that ever changes, use the PRIOR completed session's close named on its basis
   (**10-09: c 715.58, `--adjustment all`, pulled at this seat**), or defer the label to the close run.
   A PROMPT FIX, NOT YOURS TO MAKE.**
7. ⚠ **If you make no `move` call, say it is an ABSENT check, not a passing one.** A decorative
   priced-in call on a name with no mechanism converts an honest absence into a fake exercise.
   ⚠ **This seat made none, and four of five rejects had no ticker to call it on.**
8. ⚠ **The dividend test is CLOSED — branch (a), the platform does not model dividends. Do NOT re-read
   `cash` for this purpose and do not restart the retired counter.** Report cash as an ordinary balance.
9. ⚠⚠ **DO NOT REHABILITATE ANY EARLIER REJECT AT A DIFFERENT PRICE, AND TWO ARE NAMED.** **GFS**
   (`T-2026-10-09-01`) died on the **calendar** (H1 2028) and on **materiality** (5.89%) — neither moves
   with the quote, and *"but it has not run yet"* is *"but it went up"* wearing a coat. **ELMT** is the
   standing proof: **+11.86pp vs VOO and still ineligible**, because §3 is a hard filter that does not
   weigh outcomes. ⚠ **DO NOT SCREEN EITHER AGAIN.**
10. ⚠ **AND THE ONE THING THAT IS NEW TODAY: IF THE FUNNEL SERVES YOU A TWO-PARTY, DATED, QUANTIFIED
    ITEM, CHECK THAT BOTH PARTIES ARE *COMPANIES* AND THAT THE QUANTITY IS IN *DOLLARS* BEFORE YOU
    REACH FOR A MECHANISM.** `T-2026-10-12-01` is the worked instance: it satisfied the structural
    shape completely and was never tradeable.

**Nothing in this plan requires an order. The correct 09:35 run places zero trades.**

---
