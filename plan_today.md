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
plan_date: 2026-09-29
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-09-29 at 09:30 ET** (`alpaca.py clock` at 08:26:19 ET: `is_open:
false`, `next_open: 2026-09-29T09:30:00-04:00`, `next_close: 2026-09-29T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.**

**One pre-market run today, at 08:26 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$99,827.65**).

⚠⚠ **THIS FILE ARRIVED CARRYING `plan_date: 2026-09-25` — FOUR CALENDAR DAYS AND ONE FULL
TRADING SESSION STALE, BECAUSE YESTERDAY'S PRE-MARKET RUN LEFT NO OUTPUT.** Verified from
inside this run: `git log` shows **no commit dated 2026-09-28 other than the close journal
(11804ab)**. ⚠ **Routine 4 deliberately left the stale date in place as evidence and said
the next pre-market run would overwrite it normally. It has now been overwritten normally.**
⚠ **THE STALENESS GATE STILL HAS NOT BEEN TESTED. The count is 28, not 29** — yesterday's
09:35 run, which is the only thing that can fire the gate, did not execute.

---

## Tape context

Monday's **official** VOO close, from `bars --adjustment all`, is **703.60**.

⚠⚠ **EVERY VOO CLOSE OLDER THAN 2026-09-28 NOW EXISTS ON TWO BASES AND THEY ARE NOT
INTERCHANGEABLE. VOO WENT EX-DIVIDEND ON 09-28.** `bars --adjustment all` rescaled every
prior close by **0.997432**; `--adjustment raw` and `--adjustment split` return the original
series to the cent. **Both series are correct; they are different bases.**

| Session | `--adjustment raw` | `--adjustment all` |
|---|---|---|
| 2026-09-28 | **703.60** | **703.60** *(unchanged — the ex-date itself)* |
| 2026-09-25 | 710.705 | 708.88 |
| 2026-09-24 | 707.28 | 705.47 |
| 2026-09-23 | 707.28 | 705.47 |
| 2026-09-22 | 712.69 | 710.86 |
| 2026-09-21 | 712.76 | 710.93 |
| 2026-09-18 | 701.85 | 700.05 |

⚠ **NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.** The 09-03 core fill at
**706.74 is a RAW print**; measuring it against an `--adjustment all` close mixes bases.
⚠ **AND `quote`'s `prevDailyBar` DISAGREES WITH `bars --adjustment all` ON THE SAME SESSION,
RIGHT NOW.** The standing "both legs from the same source" rule does **not** catch this — it
distinguished broker fields from bar fields, never `quote` from `bars`.

**THE DIVIDEND HAS STILL NOT BEEN PAID — CHECKED THIS RUN, AS THE CARRY-FORWARD REQUIRES.**
`cash` reads **exactly $30,000.00**, unchanged. The implied credit is **~$180.26–180.64**
(an INFERENCE — Alpaca does not publish the figure). ⚠ **The falsifiable test stands: if
`cash` has not risen by ~$180 by 2026-10-07, the paper account does not model dividends at
all, and §1's "beat the S&P TOTAL RETURN" is unwinnable BY CONSTRUCTION rather than by
strategy. That is a finding for the human, not something to fix from this seat. CHECK `cash`
EVERY RUN UNTIL IT RESOLVES.**

The broker's pre-market `positions` row reads `current_price` **705.00** — **a pre-market
mark, not a close and not an execution reference** — with `lastday_price` **703.61**
(⚠ matching neither basis: raw 703.60, adjusted 703.60; the field is **UNUSABLE, not
imprecise** — do not re-open it) and `unrealized_intraday_pl` **+$137.67**. **None of those
were used in or carried into any figure in this plan.** **`bars --adjustment all` for a
close, a fresh `quote` for execution, never a `positions` field for either, and never
`equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

The core shows `unrealized_pl` **−$172.34 / −0.246%** against the 706.74 fill, on a
pre-market mark. **§5 exempts core from all four sell rules, so no action attaches to that
number in either direction.**

---

## Sleeves and the rebalance question

**State which basis produced any figure you quote** — the two can disagree in *sign* on
`rebalance_delta` (observed 09-24).

| Basis | Equity | Core | Core % | Cash % | `rebalance_delta` |
|---|---|---|---|---|---|
| **Broker marks** (`sleeves`, 08:26) | $99,827.65 | $69,827.65 | **69.95%** | 30.05% | **+$51.71** |
| **Official 09-28 close** (703.60 × 99.046311231) | $99,688.98 | $69,688.98 | **69.9064%** | 30.0936% | **+$93.30** |

⚠ **NO REBALANCE IS DUE, ON EITHER BASIS.** §2 rebalances at the **65/75 band edge**, not to
the exact target. The core sits **4.95 points** from the nearest edge on broker marks and
**4.91** on official closes. `core_in_band: true`, `rebalance_needed: false`.
⚠ **Both bases are POSITIVE and AGREE IN SIGN — the second consecutive run they have done so,
after four consecutive negative runs. That is not the price-source defect resolving; the same
quantity disagreed in SIGN on 09-24. A run that checks one basis and finds agreement learns
nothing.** **Forty-eighth consecutive run inside the range 69.59–70.22.**

Cash is **$30,000.00 flat** — unchanged since the 09-03 core fill, and see the dividend note
above.

---

## Position review — §5

**There are zero open satellite positions.** `alpaca.py positions` returns **one row, core
VOO**, 99.046311231 shares at avg_entry 706.74, cost_basis $69,999.99 — unchanged since the
09-03 fill.

**RECONCILIATION CLEAN.** Zero satellite blocks in `positions.md` against zero satellite
Alpaca rows — they agree. *(Satellite-to-satellite, never raw ledger to raw broker: the core
is deliberately untracked in `positions.md` because §5 exempts it.)* Core VOO was excluded
from the working list before any §5 rule was read.

**§5.1–§5.4 have no operand.** ⚠ **Counted against the CALENDAR, not inherited — catch (9)
established that the "Nth consecutive SESSION" series in these files was a RUN counter
wearing a session label, and it is not continued here.** The verified figures: **20 trading
sessions since 2026-09-01, 17 since the 09-03 core fill, and ZERO satellite positions in the
account's entire history.** No thesis to invalidate, no timing window to expire, no entry
price to measure a −7% hard stop from, no `highest_close` to measure a −10% trailing stop
from. ⚠ **§5.4 is STILL NOT ARMED**; it arms on the first **satellite** fill, and the 09-03
core fill was not one. **§5.3's distance is UNDEFINED, not large.** **The running tally of
"no exits" records the ABSENCE OF A SUBJECT, not a clean bill of health. All four remain
UNTESTED CODE PATHS.**

**High-water marks: nothing to backfill, and nothing was skipped.** `highest_close` is
**ABSENT — the third state, carrying no `(as of …)` date at all.** ⚠ **Do not read the
missing stamp as a failed close run: there is no field, so there was nothing to write. DO NOT
BACKFILL ANYTHING.** **Zero `bars` calls were due on any satellite symbol and zero were made.**
⚠ **AND WHEN §5.4 DOES ARM: `highest_close` and the close it is compared against must come
from the SAME adjustment basis, pulled in the SAME call.** 09-28 was the day this mechanism
would have broken — a Friday-stamped mark against Monday's `--adjustment all` close would have
shown a **0.257% drawdown that did not happen**. ⚠ **The empty sleeve is the only reason it
cost nothing.**

---

## Intents

### BUY

**NONE.**

⚠ **Every gate that could have blocked a buy was OPEN, and nothing was blocked.** Circuit
breaker **INACTIVE** (`halt_triggered_at: none`); `new_positions_this_week` **0 of 3**;
satellite sleeve **empty** with **~30% idle cash**; `control.md` notes **(none)**;
`TRADING_ENABLED: true`. **Research ran in full and produced no eligible candidate.** Per §4,
that is a successful run, not a failed one.

**Six candidates reached a `research_log.md` entry and all six were rejected:**

| ID | Candidate | Killed by |
|---|---|---|
| T-2026-09-29-01 | **AMRAAM component suppliers** (no ticker) | **Premise + part 1** — RTX is the awardee (first-order); **no subcontractor is named anywhere** and no dollars are allocated to one. Rule (v). |
| T-2026-09-29-02 | **IOVA** (Iovance) | **Part 1** — rule (iii) PASSES cleanly, then **rule (vii)**: Iovance manufactures Amtagvi itself and names no external supplier. |
| T-2026-09-29-03 | **SMMT** (Summit) / AstraZeneca | **Premise + part 2 + part 3** — first-order; the $2.0B is **capital paid IN** for convertible preferred (rule viii); clinical collaboration is years, not quarters. |
| T-2026-09-29-04 | **CRK** (Comstock) / SOCAR | **Part 1 + part 2** — the second-order sentence needs an **"and also"**; $1.65B is capital paid in by a non-US-listed state oil company. |
| T-2026-09-29-05 | rate / Fed-repricing complex (no ticker) | **Environment input, ONE party.** T-2026-09-25-06 with bigger numbers. |
| T-2026-09-29-06 | **AIR** (AAR) / MRO Holdings | **Part 1** — the only Company B is **private**; and **rule (iii) cannot be cleared** — AAR's own prior guidance is absent from the sources. |

⚠⚠ **THE FINDING OF THIS RUN IS THAT THE SOURCE VOLUNTEERED THE ABSENCE.** The guidance and
capacity scan returned five US-listed names and printed, for four of the five, *"No other
company's revenue or costs are identified as directly affected in the available source
material."* ⚠ **That is not an under-searched funnel — it is the funnel answering §4's
question directly and in the negative. A run that then produces a Company B has supplied it
from its own priors, which is exactly the failure §4's honest-broker paragraph names.**

⚠⚠ **AND THE DAY'S SHARPEST PAIR SITS ONE ENTRY APART: T-2026-09-29-02 IS THE CLEANEST RULE
(iii) PASS IN WEEKS AND T-2026-09-29-06 IS A RULE (iii) FAILURE, FROM THE SAME QUERY.**
Iovance raised guidance against **its own prior number** ($350–370M → $410–420M); AAR quoted a
growth range with **no prior range in the source**. ⚠ **The difference is entirely whether the
source carried the company's OWN prior figure. That is the whole test, and it is cheap.**

⚠ **NO PRICED-IN CHECK WAS RUN THIS MORNING, AND THAT IS AN ABSENT CHECK, NOT A SKIPPED ONE** —
every candidate died at the premise, at part 1 or at part 2, before any eligible ticker was
reached. **Zero `move` calls were made.** ⚠ **Recorded explicitly because "the filter did not
fire" and "the filter had nothing to fire on" look identical in a run summary.**

### SELL

**NONE.** No satellite positions exist. §5 has no operand.

### REBALANCE

**NONE.** Core is in band on both bases (69.95% broker / 69.9064% official; band 65–75%).
⚠ **Do not act on `rebalance_delta` — §2 rebalances at the band edge, and the core is ~4.9
points inside it.**

---

## For the market-open run

**Zero BUY intents, so ZERO `move` re-validation calls are due. That is an ABSENT check, not
a skipped one** — record it that way.

⚠ **The staleness gate: this plan is dated 2026-09-29 and today's ET date is 2026-09-29, so
it is FRESH.** ⚠ **But note what that does and does not tell you: a FRESH EMPTY plan and a
STALE plan produce a byte-for-byte identical zero-order run. Read `plan_date`, never the
outcome.** The gate has been exercised **twenty-eight times and has never fired**; its alert
path **remains untested code**. ⚠⚠ **AND YESTERDAY WAS THE MORNING IT WOULD FINALLY HAVE
FIRED — this file genuinely carried a stale `plan_date: 2026-09-25` — AND THE RUN CONTAINING
THE GATE DID NOT EXECUTE. The prediction was right about the setup and the test still did not
happen.** The first morning it does fire will by construction be a morning when the
pre-market run failed — i.e. the morning with no fresh notes to lean on. **Read routine 2's
Step 2 then; do not recall it.**

**⚠ CHECK WHETHER YESTERDAY'S ROUTINES RAN.** If this run's commit is again the only one on
the date, that is now a **two-day** pattern and belongs in the ClickUp summary with emphasis.
The repo's own definition of a run having happened is a commit — "push, or it never happened."

**⚠ CHECK `cash`.** It should read **$30,000.00** if the VOO dividend still has not been paid,
or **~$30,180.45** if it has. **Either reading is informative; record which one you saw.**

**Bootstrap is permanently closed** (`core_established: true`). **Do not re-run it.**

⚠ **Open item (7) is live but unexposed, as always: `alpaca.py move` cannot see an after-hours
event, and neither can the 09:35 re-validation that exists to catch exactly that. It has cost
zero only because no plan has yet carried a BUY intent — an absence of exposure, not a
mitigation.**

⚠ **A BAR DATED TODAY IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU
OTHERWISE. THE RELIABLE DISCRIMINATOR IS THE CLOCK.** Routine 2 reads `is_open: true` and can
pull a live partial bar. **Low volume is not evidence of a partial bar any more than high
volume is evidence of a complete one** — `feed=iex` returns one venue's slice.

⚠ **ROUTINE 2 EXECUTES ONLY WHAT THIS FILE CONTAINS.** This file contains no BUY. Idle cash,
an INACTIVE breaker and an unused 0-of-3 weekly cap are **not** an opportunity the 09:35 seat
may act on — a position opened at 09:35 without a plan entry routes **around** the discipline
rather than satisfying it.
