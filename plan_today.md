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
plan_date: 2026-09-30
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-09-30 at 09:30 ET** (`alpaca.py clock` at 08:23:04 ET: `is_open:
false`, `next_open: 2026-09-30T09:30:00-04:00`, `next_close: 2026-09-30T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.**

**One pre-market run today, at 08:23 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$99,598.85** at pre-flight).

⚠ **THIS FILE ARRIVED CARRYING `plan_date: 2026-09-29` — ONE CALENDAR DAY OLD AND CORRECTLY
SO,** because yesterday's pre-market run wrote it and yesterday's other three routines all
committed. **Verified from inside this run:** `git log` shows 09-29 commits for the
pre-market, open, midday (3e856bb) and close (903f715) routines. ⚠ **So the 09-28 gap was a
ONE-DAY, THREE-ROUTINE event and is NOT reported as ongoing.**
⚠ **THE STALENESS GATE STILL HAS NOT BEEN TESTED. The count is 29, not 30** — the gate is
exercised once per market-open run and has never fired, because it has never met a plan
whose date was not today. **Its alert path remains untested code.**

---

## Tape context

Yesterday's **official** VOO close, from `bars --adjustment all` on a **completed** session,
is **702.27** (o 704.865, h 704.865, l 700.83, n 3337, v 101166). The two prior sessions on
the same basis: **09-28 703.60**, **09-25 708.88**.

⚠⚠ **EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT
INTERCHANGEABLE.** VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close
by **0.997432**, while `--adjustment raw` and `--adjustment split` return the original prints.
⚠ **09-28 and 09-29 agree to the cent on both bases, because the ex-date lies at or before
both — the divergence is entirely in the sessions BEFORE it.** ⚠ **The 09-03 core fill at
706.74 is a RAW print. NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**

⚠⚠ **AND THIS RUN PRODUCED A FRESH INSTANCE OF THE INTRADAY-DRIFT ITEM, INSIDE ITS OWN
PRE-MARKET WINDOW.** `sleeves` at ~08:23 returned **equity $99,598.85**; `account` a few
minutes later returned **equity $99,815.76** — **a $216.91 spread between two calls in the
same run**, consistent with VOO drifting ~$2.19/share in thin pre-market trade across
99.046311231 shares. ⚠ **An intraday equity figure is only meaningful with its CALL and its
TIMESTAMP attached, and two figures from different calls must never be differenced.**
⚠ **This matters for §6's 5% sizing cap, which is computed against live equity — but it has
NO OPERAND today, because there are no BUY intents.**

**`cash` reads EXACTLY $30,000.00** on both `sleeves` and `account`. ⚠ **The VOO dividend
remains UNPAID — day 3 of 8 on the falsifiable test. Non-arrival this early is EXPECTED, not
evidence; settlement runs on the PAY date, not the ex-date.**

---

## Sleeves and the rebalance question

From `alpaca.py sleeves` at 08:23 ET (broker marks, pre-market):

| Sleeve | Value | % | Target | In band? |
|---|---|---|---|---|
| **Core (VOO)** | $69,598.85 | **69.88%** | 70% | **YES** (65–75%) |
| **Satellite** | $0.00 | **0.00%** | 30% | empty, 0 positions |
| **Cash** | $30,000.00 | **30.12%** | — | — |

**Core holding:** 99.046311231 shares, avg_entry **706.74** (a **RAW** print), cost_basis
$69,999.99, `unrealized_pl` −$401.14 / −0.573% on the 08:23 mark.

**`rebalance_needed: false`. `rebalance_delta: +120.34`.**
⚠ **DO NOT ACT ON `rebalance_delta`.** §2 rebalances at the **65/75 band edge**, and core sits
**4.88 points** inside the nearest edge. ⚠ **The delta being positive for a fourth consecutive
run is NOT the sign-instability defect resolving — the same quantity disagreed in sign on
09-24, and a run that checks one basis and finds agreement learns nothing.**

---

## Position review — §5

**ZERO SATELLITE POSITIONS. §5 HAS NO OPERAND.**

**Reconciliation, 2026-09-30 08:23 ET: `positions.md` carries zero satellite blocks;
`alpaca.py positions` returns one row, core VOO. THEY AGREE.** Core is exempt from all four
sell rules (§5) and is deliberately not tracked in `positions.md`.

⚠ **Each rule's status, stated as ABSENT rather than as PASSING, because those are different
things and they look identical in a run summary:**

| Rule | Status |
|---|---|
| **5.1** thesis invalidation | **NO OPERAND** — no thesis is held. Zero Perplexity news checks on holdings were due or run. |
| **5.2** time stop | **NO OPERAND** — no `timing_window` deadline exists. |
| **5.3** hard stop −7% | **DISTANCE UNDEFINED, not large.** No entry price exists to measure from. |
| **5.4** trailing stop −10% | **NOT ARMED.** No `highest_close` field exists — the **third state**, carrying no `(as of …)` date at all. |

⚠⚠ **§5.1–§5.4 HAVE NEVER HAD AN OPERAND IN THIS ACCOUNT'S ENTIRE HISTORY.** The high-water
backfill path **remains unexercised code**, and 09-28 is the proof that is not academic: that
day lost its close run, so with one satellite position open, the next run would have had to
backfill **across an ex-dividend date**, which this system has never done. ⚠ **The cost has
been zero because the sleeve is empty. That is luck, not a control.**

⚠ **CORE VOO IS NOT STAMPED WITH A `highest_close`, AND WILL NOT BE.** A mark on VOO would
fabricate a §5.4 trailing stop on the one position §5 exempts — a stop that could eventually
sell core on a drawdown, which §7 forbids outright.

---

## Intents

### BUY

**NONE.**

⚠ **Every gate that could have blocked a buy was OPEN, and nothing was blocked.** Circuit
breaker **INACTIVE** (`halt_triggered_at: none`); `new_positions_this_week` **0 of 3**;
satellite sleeve **empty** with **~30% idle cash**; `control.md` notes **(none)**;
`TRADING_ENABLED: true`. **Research ran in full and produced no eligible candidate.** Per §4,
that is a successful run, not a failed one.

**Eight candidates reached a `research_log.md` entry and all eight were rejected:**

| ID | Candidate | Killed by |
|---|---|---|
| T-2026-09-30-01 | **F/A-XX supplier chain** (no ticker) | **Part 1** — Boeing is the awardee (first-order); the source, asked directly, states **no subcontractor has been publicly named**. Rule (v). |
| T-2026-09-30-02 | **Ultium Cells LMR supply chain** (no ticker) | **Part 1 + part 3 + §3** — no US-listed supplier named; **retrofit completes 2028**, far outside two quarters; every adjacent name is Korean-listed or private. |
| T-2026-09-30-03 | **HTS tape / fusion chain** (no ticker) | **§3 + parts 1/2/3** — **CFS is private, Fujikura is Tokyo-listed**; Fujikura is also first-order; **price expressly undisclosed**. |
| T-2026-09-30-04 | **ABBV** (AbbVie) | **Part 2** — a dry-eye asset AbbVie held only an **unexercised option** on cannot reach 10% of AbbVie's revenue, and **no dollar figure is disclosed**. Part 1 also describes a non-event. |
| T-2026-09-30-05 | **RARE** (Ultragenyx) | **§3 OUTRIGHT — market cap $1.42B against a $10B floor**, seven times below. Also part 2 (no figure) and part 3 (no establishable quarter). |
| T-2026-09-30-06 | **LLY** / GLP-1 injectable chain | **Part 3** — verified: **no FDA action occurred**; it was a Phase 3 readout and the **BLA is planned for Q1 2027**. Part 1 also: the only Company B was self-supplied. |
| T-2026-09-30-07 | pharmaceutical-tariff complex (no ticker) | **Premise** — environment input, **ONE party**, no disclosed figure, and the tariffs are only **potential**. |
| T-2026-09-30-08 | **CI** (Cigna) | **Part 1 + part 2** — a $7.2B **miss against consensus** with **no stated cause**, therefore no causal path and no second party. |

⚠⚠ **THE FINDING OF THIS RUN: THE SOURCE VOLUNTEERED THE ABSENCE OF A COMPANY B THREE TIMES,
IN ITS OWN WORDS.** *"No publicly traded U.S. company has been explicitly identified … as an
F/A-XX supplier, subcontractor, or Boeing partner."* *"No publicly traded U.S.-listed company
has been explicitly named as a supplier for the specific Ultium Cells prismatic LMR battery
program."* *"No qualifying item can be confirmed."* ⚠ **That is the funnel answering §4's
question directly and in the negative — not an under-searched funnel. The 09-29 carry-forward
told this seat to WRITE THAT DOWN rather than re-query in different words, and NO RE-QUERY WAS
ISSUED on either event.**

⚠⚠ **AND THE PULL IS NAMED, BECAUSE NAMING IT IS THE ONLY DEFENCE.** On F/A-XX the sentence
*"GE makes the F414, so GE gets the F/A-XX engine"* was available and fluent, and the source
explicitly closes it: GE's *"excited to see this program advance"* statement **does not
identify GE as a supplier**, and no engine award was disclosed. **On the LMR funnel the source
pre-emptively named LG Chem, Redwood and Cirba and then warned they should not be attributed
to this program — reaching for one would have been reading a warning as a shopping list.**
**Both were declined.**

⚠ **THE PRICED-IN FILTER HAD AN OPERAND TODAY AND DECIDED NOTHING.** Two `move` calls:
**ABBV −0.78% → `priced_in: false`**; **RARE −1.83% → `priced_in: false`**. ⚠⚠ **Both passed
by FALLING, not by the news being unpriced — sign-blindness in its mild form. And both
candidates died on the four-part thesis regardless. The filter was EXERCISED and
NON-DECISIVE, which is a third state distinct from "fired" and "had nothing to fire on."**

⚠ **THE CORRELATION CHECK HAD NO OPERAND — ABSENT, NOT PASSING.** Zero satellite blocks means
there is no `driver` field anywhere to collide with. **A candidate cannot fail §4's
correlation test in this account today.**

### SELL

**NONE.** No satellite positions exist. §5 has no operand — see the table above, where each
rule's status is recorded as ABSENT rather than as passing.

### REBALANCE

**NONE.** Core is **69.88%** on the 08:23 broker mark, inside the 65–75% band by **4.88
points**. ⚠ **Do not act on `rebalance_delta: +120.34` — §2 rebalances at the band edge, not
toward the 70% target.**

---

## For the market-open run

**Zero BUY intents, so ZERO `move` re-validation calls are due. That is an ABSENT check, not
a skipped one** — record it that way.

⚠ **The staleness gate: this plan is dated 2026-09-30 and today's ET date is 2026-09-30, so
it is FRESH.** ⚠ **But note what that does and does not tell you: a FRESH EMPTY plan and a
STALE plan produce a byte-for-byte identical zero-order run. Read `plan_date`, never the
outcome.** The gate will have been exercised **thirty times without ever firing** after
today's open; its alert path **remains untested code**. The first morning it does fire will by
construction be a morning when the pre-market run failed — i.e. the morning with no fresh
notes to lean on. **Read routine 2's Step 2 then; do not recall it.**

**⚠ CHECK `cash`.** It read **exactly $30,000.00** at 08:23 today. It should read **$30,000.00**
if the VOO dividend still has not been paid, or **~$30,180.45** if it has. **Either reading is
informative; record which one you saw, and record that it is day 3 of 8.**

**⚠ TWO EQUITY FIGURES ALREADY DISAGREE BY $216.91 INSIDE THIS RUN'S OWN WINDOW** ($99,598.85
from `sleeves`, $99,815.76 from `account`, minutes apart). ⚠ **Attach the call and the
timestamp to any equity number you write, and never difference two of them.**

**Bootstrap is permanently closed** (`core_established: true`). **Do not re-run it.**

⚠ **A BAR DATED TODAY IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU
OTHERWISE. THE RELIABLE DISCRIMINATOR IS THE CLOCK.** Routine 2 reads `is_open: true` and can
pull a live partial bar. **Low volume is not evidence of a partial bar any more than high
volume is evidence of a complete one** — `feed=iex` returns one venue's slice. 09-28 printed
v 62,354 against Friday's 164,725 and is **complete**; 09-29 printed v 101,166 and is **also
complete**.

⚠ **ROUTINE 2 EXECUTES ONLY WHAT THIS FILE CONTAINS.** This file contains no BUY. Idle cash,
an INACTIVE breaker and an unused 0-of-3 weekly cap are **not** an opportunity the 09:35 seat
may act on — a position opened at 09:35 without a plan entry routes **around** the discipline
rather than satisfying it.

⚠ **GNRC IS NOT YOURS TO LOOK AT.** It is the **named counterparty** in the Amazon
announcement — **first-order, outside §4 at any price** — and no number the 09:35 seat could
collect would change that. Open item (7) is resolved by a human editing §4 or `alpaca.py
move`, not by a quote.
