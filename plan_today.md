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
plan_date: 2026-10-08
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-08 at 09:30 ET** (`alpaca.py clock` at 08:25:01 ET: `is_open:
false`, `next_open: 2026-10-08T09:30:00-04:00`, `next_close: 2026-10-08T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** ⚠ **Corroborated independently from the data plane:
`bars --days 4 --adjustment all` returns a complete **2026-10-07** bar (c 714.66) and **NO bar
dated 2026-10-08** — the pre-market shape, confirmed rather than assumed.** Both `next_open`
and `next_close` carry **today's** date, which is the full-session signature: not an early
close.

**One pre-market run today, at 08:25 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$100,491.26** at pre-flight).

⚠ **This file arrived carrying `plan_date: 2026-10-07` — exactly one trading day old, which is
correct.** The predecessor was fresh and deliberately empty. ⚠⚠ **AND THE REASON TO SAY SO, AGAIN:
A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. Freshness is
read OFF `plan_date` and NEVER inferred from the outcome.** **The staleness gate's non-exercise count
will be **36** after today's open; it has never fired, and its alert path remains untested code.**
**This plan is fresh and, again, deliberately empty.**

⚠ **THE PREVIOUS TWO SESSIONS WERE BOTH COMPLETE — ALL FOUR SEATS OF 2026-10-06 AND 2026-10-07 RAN
AND COMMITTED.** ⚠⚠ **THAT IS NOT A FIX AND A PAIR IS NOT EVIDENCE EITHER: the failure mode is a seat
that never STARTS, so a session that completed says nothing about the next one in either direction.
Two of ~27 close runs have vanished (09-28, 10-05), there is still no detector for a missing seat, and
`alerts.md` reading "zero open incidents" cannot distinguish a healthy week from a run that died
before `commit.py`. Open item (11) stands exactly where it did.**

---

## ⚠⚠ THE DIVIDEND TEST IS RESOLVED, AND THE ANSWER IS BRANCH (a): THE PLATFORM DOES NOT MODEL DIVIDENDS

**This seat is the one the 10-07 close run handed the reading to, and it is readable.** The decision
rule was written in advance, in `state.md`, specifically so it could not be bent at the moment of
reading. **Both of its inputs were taken in the same breath:**

| Input | Reading at 2026-10-08 08:25 ET | Branch condition |
|---|---|---|
| `account.balance_asof` | **`2026-10-07`** | ≥ 2026-10-07 ✅ **the field has advanced** |
| `cash` (`account` **and** `sleeves`) | **exactly `30000.00`**, `accrued_fees: 0` | still exactly $30,000.00 ✅ |

⚠⚠ **THAT IS BRANCH (a) EXACTLY AS WRITTEN: `balance_asof` ≥ 2026-10-07 AND `cash` unchanged → THE
TEST IS RESOLVED AND THE ANSWER IS THAT THE ALPACA PAPER ACCOUNT DOES NOT MODEL DIVIDENDS.**
**The inferred credit of ~$30,180.76 ($1.825/share × 99.046311231) never arrived, and the balance
field has now rolled past the pay date without it.** This is a **THIRTIETH** consecutive reading of
exactly $30,000.00, and the first one that *means* something, because until the stamp advanced the
non-arrival was consistent with two different worlds.

⚠ **WHAT CLOSED THE TEST WAS THE 10-07 MIDDAY SEAT FINDING `balance_asof` AT ALL.** Before that, the
test was being read off `cash` alone, and a 16:15 non-arrival could not distinguish "no dividend
modelling" from "the credit posts to a balance stamp this field will not surface until tomorrow."
⚠ **The claim was moved exactly once, off an API field rather than for convenience, and the figure
$30,180.76 itself was never moved.** ⚠⚠ **A falsifiable claim, written in advance, held across three
sessions and four seats, and then resolved against itself. THAT IS THE PROCESS WORKING — and the
result is a negative one, which is what most correct tests return.**

### ⚠⚠ THE CONSEQUENCE, WHICH IS A FINDING FOR THE HUMAN AND NOT SOMETHING ANY SEAT CAN FIX

**The §1 objective is to beat the S&P 500 TOTAL return. The account cannot collect dividends. Those
two facts are in direct conflict and no routine can reconcile them.**

The magnitude is **established, not re-derived**: VOO's trailing 12 months is **+16.3118%** on
`--adjustment all` against **+14.9863%** on `raw`, so **dividends are worth 1.3254pp/year**. A 70%
core that never collects them structurally under-earns **~0.93pp/yr**, which on top of the **4.89pp**
cash drag is a **~5.82pp ANNUAL HANDICAP BEFORE A SINGLE DECISION IS MADE.**

⚠ **Three options, all of them the human's call and none of them this agent's to take:** (i) accept
the handicap and benchmark against VOO **price** return rather than total return, acknowledging that
§1 as written is then unmeetable by construction; (ii) have the close routine accrue a notional
dividend in `state.md` for benchmarking only, touching no order path; (iii) leave it and treat the
handicap as a known, quantified bias in every performance line this system ever writes.
⚠ **Option (ii) would require a `strategy.md` or routine change. ONLY THE HUMAN MAY MAKE IT.**
⚠ **The test is now CLOSED. No future seat should re-read `cash` for this purpose, and the
thirty-reading counter retires here.**

---

## Tape context

**VOO official closes** (`bars --adjustment all`, completed sessions): 10-02 **709.70**-basis run
through 10-05 **712.41** → 10-06 **716.29** → **10-07 714.66** (o 713.02, h 715.00, l 711.22, n 1325,
v 23423, vw 713.494198). **The 10-07 high-water on completed bars is 716.29, set on 10-06.**

⚠ **A SMALL NEW FINDING, AND IT IS ABOUT TRUSTING "COMPLETED" BARS: the 10-07 bar has been REVISED
SINCE THE CLOSE SEAT READ IT.** That seat recorded **n 1323 / v 23415** at 16:17; this seat reads
**n 1325 / v 23423** on the same date and the same basis — **+2 trades, +8 shares.** ⚠ **o/h/l/c and
vw are UNCHANGED, so nothing that matters to a §5 rule moved.** ⚠⚠ **But "the bar is complete" and
"the bar is final" are not the same statement, and a run that diffs n/v across seats to detect
staleness will see motion that is late-print settlement rather than a live session.** This is the
other end of the **retired n/v completeness floor test** — the same two fields failing in the
opposite direction within 16 hours.

**Broker vs official, unchanged in character:** `positions` reports VOO `lastday_price` **714.34**
against the official 10-07 close of **714.66** — a **$0.32** gap. ⚠ **A moving live midpoint, not a
fixed offset; the two numbers are not interchangeable and the official bar is the one a §5 rule would
use.** Live `current_price` **711.70**, `change_today` **−0.37%** — ⚠ **a pre-market indication on an
exempt core holding, and NOT a §5 input.**

---

## Reconciliation

**LEDGER AGREES WITH BROKER. Satellite-to-satellite, zero on both sides.**

`alpaca.py positions` returns **one row, core VOO** — 99.046311231 shares, avg_entry **706.74** (a
**RAW** print), cost_basis **$69,999.99**, market_value **$70,491.26**, unrealized **+$491.27
(+0.70%)** — unchanged since the 2026-09-03 fill. `positions.md` carries **zero satellite blocks.**
**THEY AGREE.** ⚠ **Core VOO was removed from the working list BEFORE any §5 rule was read, per §5's
core exemption — a run that compares the raw ledger to the raw broker reads a correct ledger as
broken.** ⚠⚠ **TWENTY-SEVENTH SESSION WITH NOTHING TO RECONCILE. AN AGREEING LEDGER AND AN EMPTY
LEDGER ARE THE SAME ARTIFACT — this is not a clean bill of health on the reconciliation logic, it is
the absence of a test.**

**Sleeves at 08:25:** equity **$100,491.26**, core **$70,491.259703 = 70.15%**, satellite **0.0%**
(count 0), cash **29.85%** / **$30,000.00**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta` **−$147.38**. ⚠ **That delta is a DISTANCE READOUT, NOT AN INSTRUCTION — negative
only because core sits fractionally above the 70% target, and §2 acts at the BAND EDGE, not at the
target.** **In band by 5.15 points at the 65 edge and 4.85 at the 75 edge. 71st consecutive run inside
the band.**

**Week rollover:** ISO Monday of 2026-10-08 (a **Thursday**) is **2026-10-05**, which **matches**
`week_of`. **NO ROLLOVER. `new_positions_this_week` stays 0.** ⚠ **Computed here rather than inherited,
per the standing rule that the §6 weekly cap must not stay stuck at its limit if a Friday run failed.**

**Circuit breaker:** **INACTIVE**, `consecutive_closed_losses` **0**, `halt_triggered_at: none`.
⚠ **The streak is 0 and UNABLE TO MOVE — nothing has ever closed on this account. That is not a streak
that held.** `HALT_CLEARED_AT: none` in `control.md`, which is correct and irrelevant while no halt
exists. ⚠ **New positions are PERMITTED today. Every gate is open and nothing was blocked.**

**`control.md` notes:** **(none)**. No human instruction restricts this run.

**§5 status:** ⚠ **§5 HAD NO OPERAND AND DID NOT PASS.** Zero satellite positions, so §5.1
invalidation, §5.2 time stop, §5.3 −7% hard stop and §5.4 −10% trailing stop each had **nothing to
evaluate. The distance to each rule is UNDEFINED, NOT LARGE.** ⚠ **No Perplexity news check was run on
any held name because there is no held name — Step 4's invalidation sweep had no subject.**
⚠ **The §5-operand counter stands at 26 completed sessions / 23 post-fill and DOES NOT ADVANCE HERE:
the unit is a COMPLETED session, and this seat stands before the bell on 10-08.**

---

## Intents

### BUY

**NONE. ⚠⚠ ZERO BUY INTENTS, AND NOT BECAUSE ANYTHING BLOCKED THEM.**

⚠ **This is the important distinction and it must not be lost between here and 09:35: every §6 and §7
gate was OPEN.** Breaker INACTIVE · `new_positions_this_week` **0 of 3** · satellite sleeve **0%
deployed** against a 30% target with **$30,000 in idle cash** · `control.md` notes empty ·
`TRADING_ENABLED: true`. **A buy could have been placed today. Nothing was worth buying.**

**Ten candidates were researched and all ten were rejected** (`T-2026-10-08-01` … `-10`). The kills,
in one line each, so the 09:35 seat need not re-read the log to know nothing is pending:

| ID | Candidate | Test that failed |
|---|---|---|
| -01 | Asieris / Theramex, CEVIRA licence, $15M + >$250M | §3 — **neither party is US-listed** |
| -02 | **SUPN** (Newron FDA clinical hold; SUPN holds US rights) | §3 cap **$2.5B** · part 2 (no figure) · **mechanism points DOWN** |
| -03 | **OII**, US Navy $154M to A&DT segment | §3 cap **$4.48B** · first-order · announced **10-02** |
| -04 | **GVA**, $489.8M project awards | §3 cap **$5.37B** · first-order · no segment quantification |
| -05 | X-Bow Systems / US Navy ~$70M SRM booster | §3 — **X-Bow private, counterparty is the Navy** |
| -06 | **VAL** / PETRONAS ~$220M | part 2 — **aggregate, unallocated** · first-order · §3 **UNRESOLVED** |
| -07 | US Army NGC2 ~$100M to nine companies | part 2 — aggregate; 10% test and $10B floor **jointly unsatisfiable** |
| -08 | **ARGX**, Phase 3 UNITY discontinued | part 1 — **no second company named**; competitor read-across is shared cause |
| -09 | Pfizer Sicily, ~330 jobs | part 1 — **no counterparty at all**; headcount is not a dollar path |
| -10 | §3 scope sweep, **twelve non-US items** | §3 — not US-listed |

⚠⚠ **NINE OF THE TEN DIED AT §3 OR PART 1 — UPSTREAM OF ANY MECHANISM. EXACTLY ONE (SUPN) REACHED
PART 2.** The structural framing is reaching the funnel's real inventory; the inventory itself was
ineligible end to end today. **Those are two separate facts and only the first is about the query.**

⚠⚠ **AND THE ONE WORTH THE HUMAN'S ATTENTION: SUPN IS THE EIGHTH RECORDED REJECT FORM AND THE FIRST
OF ITS KIND — A SOUND MECHANISM POINTING THE WRONG WAY.** The FDA hold genuinely does impair the US
rights holder's asset, and that read is **untradeable here**: §3 forbids leverage, inverse products
and anything not bought outright with settled cash, so this strategy can only express the long side.
⚠ **The seven previously catalogued forms are all disclosure or calendar failures. This one is a
STRATEGY-SCOPE failure, and it will recur.**

⚠ **The honest-broker line, because the pressure to skip it is exactly why it is written down: 27
completed sessions, 130 theses, ZERO POSITIONS EVER OPENED, and 29.85% of the book in idle cash. §2
permits the cash and §4 says most runs end in no trade. Both rules were followed. That is not an
argument for lowering the bar — and if the bar is to move, it is a `strategy.md` change and ONLY THE
HUMAN MAY MAKE IT.**

### SELL

**NONE. ⚠ §5 HAD NO OPERAND — there are zero satellite positions to sell.** Core VOO is **exempt from
all four sell rules** (§5) and **must not be sold to fund anything** (§7). ⚠ **No position is queued
for exit, nothing is near a stop, and "nothing is near a stop" is a statement about an EMPTY SET —
read it as "undefined", not as "comfortable".**

### REBALANCE

**NONE. Core is 70.15%, inside §2's 65–75% band by 5.15 points at the near edge.**
`rebalance_needed: false`. ⚠ **`rebalance_delta: -147.38` is NOT a rebalance instruction — §2 acts at
the band edge and core is fractionally ABOVE target, not outside the band.** ⚠ **A rebalance must
never be built on a live intraday mark in any case: equity moved ~$11 across three calls minutes apart
on 10-07, which is the mechanical reason.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate. This plan carries no BUY, no SELL and no REBALANCE intent.**

⚠ **Do NOT read that as permission to skip the gate.** Specifically, at 09:35:

1. ⚠⚠ **READ `plan_date` OFF THIS FIELD. It is `2026-10-08`.** Do not infer freshness from the fact
   that the plan is empty — **a fresh empty plan and a stale plan produce a byte-for-byte identical
   zero-order run.** Record which one you had. **Non-exercise count 36 after today.**
2. **Confirm all ten thesis IDs `T-2026-10-08-01` … `-10` are present and REJECTED in
   `research_log.md`** before concluding there is nothing to execute. **None is a buy candidate.**
3. **Step 3's core bootstrap is skipped on `core_established: true`** — a path that ran once on
   2026-09-03 and by construction never runs again. **Do not re-bootstrap.**
4. **Re-check sleeves on live numbers.** If core has left the 65–75% band overnight, §2's rebalance is
   **exempt from the plan_date gate** and is yours to place. At 08:25 it was 70.15% with 4.85 points of
   headroom, so this is a check, not an expectation.
5. ⚠ **The dividend test is CLOSED — branch (a), the platform does not model dividends. Do NOT re-read
   `cash` for this purpose and do not restart the counter.** Report cash as an ordinary balance.
6. ⚠ **Do NOT stamp core VOO with a `highest_close`.** A mark on VOO would fabricate a §5.4 trailing
   stop on the one position §5 exempts, which §7 forbids outright. **This will be the 80th consecutive
   run declining it.** On today's numbers the mark would sit at **716.29** with 10-07's close already
   **below** it — the phantom drawdown starts on day one.
7. ⚠ **If you make no `move` call, say it is an ABSENT check, not a passing one.** A decorative
   priced-in call on a name with no mechanism converts an honest absence into a fake exercise.

**Nothing in this plan requires an order. The correct 09:35 run places zero trades.**
