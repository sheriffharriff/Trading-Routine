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
plan_date: 2026-11-05
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-11-05 at 09:30 ET** (`alpaca.py clock` at 07:02:39 ET: `is_open:
false`, `next_open: 2026-11-05T09:30:00-05:00`, `next_close: 2026-11-05T16:00:00-05:00`).
**NOT a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

The plan this run replaced was dated **2026-11-04** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

---

## ⚠⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run:** the 2026-11-02 seat read routine 2's **stored
schedule** as `13:35:00 UTC`. `13:35 UTC` was `09:35 ET` under EDT (UTC−4) and is `08:35 ET`
under EST (UTC−5). **US ET left DST on 2026-11-01.** Observed dispatches since: `08:47`
(11-02) · `08:36` (11-03) · `08:35` (11-04) — each read `is_open: false` and placed nothing.
**This pre-market seat dispatched at 07:02 ET against a nominal 08:00, the same −1h.**

⚠ **This run could NOT re-read the stored schedule: `CronList` returns "No scheduled jobs",
because these routines are not CronCreate jobs. The 13:35 UTC figure is the 11-02 seat's
reading, carried forward and labelled as inherited.** `control.md` forbids diagnosing a
schedule fault **from run timestamps**; the stored-schedule reading plus the DST calendar is
a different kind of evidence, and the honest position is that the *cause* is consistent with
a fixed-UTC schedule and cannot be closed out from inside this repo.

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED,
CONFIRMED CONDITION, NOT A NEW FAULT AND NOT A HOLIDAY.** §7 forbids trading a closed
market. **Placing nothing is CORRECT. The fault is not yours to fix and the schedule is not
yours to change.** Record the firing time and `is_open` as the first line of your run, log
the skip, commit.

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS
EXACTLY WHAT MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed
seat over an empty plan are byte-identical in output. The day this plan carries a BUY, the
trade will simply not happen, and nothing in the order count will say why.** **This is the
FOURTH consecutive EST session in that condition.**

---

## Intents

### BUY

**NONE.** Six Perplexity queries spent; five candidates logged; **zero survived.** §4's
honest-broker rule is explicit that this is the correct output of most research runs, and it
is the 58th consecutive seat with an empty satellite sleeve.

New positions were **permitted** this run and the absence of intents is a research outcome,
not a block: breaker **INACTIVE** · `new_positions_this_week` **0 of 3** · satellite sleeve
**0.0% deployed** with **$30,000 cash** · `control.md` **Notes: (none)**. Nothing stopped a
buy except the candidates.

The day's tape was **macro-dominated with no second-order transaction anywhere in it**: a US
midterm result read as divided government, ADP +86k, ISM services 54.5, a $105B September
trade deficit, a Cleveland Fed PCE nowcast, and the **October 28** FOMC hold re-reported. A
mega-cap tech rally (MSFT +6.68%, AMZN +6.12%, AAPL +5.31%) with **no company-specific
catalyst in any source**. Every named two-party transaction found was a §3-dead microcap or
carried no dollar figure. See `research_log.md` `T-2026-11-05-01` … `-05`.

### SELL

**NONE — no operand.** `positions.md` satellite block count is **0** and
`alpaca.py positions` returns **one row, core VOO only**. §5.1 and §5.2 were evaluated and
have **nothing to evaluate against**: all four sell rules are **ABSENT, NOT PASSING.** Core
VOO is exempt from all four per §5 and was struck from the working list rather than stamped
as passing.

### REBALANCE

**NONE.** `alpaca.py sleeves` at 07:02 ET: equity **$99,923.72** · core **VOO $69,923.72 =
69.98%** · satellite **$0 = 0.0%, count 0** · cash **30.02%** · `core_in_band: true` ·
`rebalance_needed: false` · `rebalance_delta: 22.88`. 69.98% sits ~0.02pp off the 70% target
and **5pp inside each edge** of §2's 65–75% band. The $22.88 delta is fractional-share
residue against a moving mark, not drift.

---

## Revalidate

Nothing to revalidate — **no BUY intents.** The `revalidate` line exists to name the specific
number an overnight gap could invalidate, and with no intent there is no number.

⚠ **For the open seat, one standing instruction that is NOT an intent:** if you execute
nothing today, that is correct and expected on this plan. Do **not** read an empty intent
list as a reason to construct a trade at the point of execution — §4 requires the written
thesis to pre-date the order, and there is no thesis in `research_log.md` dated today that
survived.

---

## Carry to the open seat

- **2026-11-04 HAS NO OFFICIAL CLOSE IN THIS REPO** and this seat judged the backfill to be
  **substantively empty**, which is the useful finding rather than a task left undone. The
  ledger held **zero satellite positions**, so there was **no `highest_close` to stamp** and
  the §5.4 trailing stop had no operand; core VOO is §5-exempt. **For the record, from
  `alpaca.py bars --adjustment all`: VOO's 2026-11-04 official close was `704.76`** (broker
  `lastday_price` read `704.78` at 07:02 — an adjusted-bar vs. broker-field difference of
  2 cents, not a discrepancy). **Nothing was lost on 11-04. The empty sleeve is the only
  reason that is true.**
- **Ledger reconciliation is CLEAN and was re-derived at this seat, not inherited:** three
  independent sides agree on zero satellites — `positions.md` block count `0`, `sleeves`
  `satellite.count 0`, and `positions` returning core VOO only (99.046311231 sh @ 706.74,
  cost basis $69,999.99, unchanged since the 2026-09-03 fill; only the mark moves).
- **THE DIRECTION-BLIND `move` DEFECT FIRED AGAIN — FOURTH CONSECUTIVE SESSION, SEVENTH AND
  EIGHTH NAMES.** ⚠ **This is NOT a new finding and this seat's first draft wrongly called it
  one; the claim is REPLACED rather than left beside its correction.** `alpaca.py move` is a
  MAGNITUDE test, not a DIRECTION test: **IREN `-24.7%` and NVDA `-7.04%` both returned
  `priced_in: true` / "LATE — skip per strategy.md section 4".** Running tally: **INTC −24.36%
  (11-02) · MU −7.77% · SNDK −14.40% · STX −7.87% · WDC −4.96% (11-03) · ON −7.69% (11-04) ·
  IREN −24.70% · NVDA −7.04% (11-05)** — **eight "LATE" verdicts on eight DECLINES across four
  sessions.** ⚠ **OBEYED ANYWAY, and that is the rule: the filter fails safe — it over-blocks
  and can never wrongly PERMIT — so a seat must not reason past a `priced_in: true` because
  the move was negative.** ⚠ **Both candidates died independently on part 2 and on §3, so
  nothing turned on it this run.** ⚠ **The fix is a signed threshold in `scripts/alpaca.py`,
  which is SCRIPT-LEVEL AND NOT A SEAT'S TO INSTALL.** Reported to the human 2026-11-03;
  **re-notified 11-05 only because the tally has doubled since, not because the status
  changed.**
