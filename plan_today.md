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
plan_date: 2026-11-06
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-06 at 09:30 ET** (`clock` 07:03:02 ET: `is_open: false`, `next_open`
`2026-11-06T09:30:00-05:00`, `next_close` `2026-11-06T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**

The plan this seat replaced was dated **2026-11-05** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

---

## ⚠⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Inherited, not re-verified this run** (`CronList` cannot read these triggers — it lists
only in-session `CronCreate` jobs, and its empty answer is evidence of nothing): the 11-02
seat read routine 2's **stored schedule** as `13:35:00 UTC`. That was `09:35 ET` under EDT
and is `08:35 ET` under EST. **US ET left DST on 2026-11-01.** Dispatches since: `08:47`
(11-02) · `08:36` (11-03) · `08:35` (11-04) · `08:37` (11-05) — **each read `is_open: false`
and placed nothing.** This seat dispatched at `07:03` against a nominal `08:00`: the same −1h.

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED,
CONFIRMED CONDITION — NOT A NEW FAULT AND NOT A HOLIDAY.** §7 forbids trading a closed
market, so **placing nothing is CORRECT.** The fault is not yours to fix and the schedule is
not yours to change. Record the firing time and `is_open` as your first line, log the skip,
commit. `control.md` forbids diagnosing a schedule fault **from a firing time**; the
stored-schedule reading plus the DST calendar is different evidence, and the cause cannot be
closed out from inside this repo.

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS WHAT
MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed seat over an
empty plan are byte-identical in output. The day this plan carries a BUY, the trade simply
will not happen, and nothing in the order count will say why.** **Fifth consecutive EST
session in that condition.**

---

## Intents

### BUY

**NONE.** Four Perplexity queries spent; five theses logged; **zero survived.**

New positions were **permitted** and the absence of intents is a research outcome, not a
block: breaker **INACTIVE 0/3** · `new_positions_this_week` **0 of 3** · satellite sleeve
**0.0% deployed** with **$30,000 cash** · `control.md` **Notes: (none)**. Nothing stopped a
buy except the candidates.

**The day's event was the tape itself**: S&P **−4.4%**, Nasdaq **−5.5%**, **SOX −12% (second-
largest on record)**, all 11 sectors lower, on the Democratic midterm sweep read as policy
risk to the data-center buildout plus a broad AI-capex reassessment. ⚠ **A repricing is not a
transaction and has no Company A.** A query asking specifically for §4's structure — named A,
named US-listed B, disclosed dollar value — returned **zero confirmed matches**. See
`research_log.md` `T-2026-11-06-01` … `-05`.

### SELL

**NONE — no operand.** `positions.md` satellite block count **0**; `alpaca.py positions`
returns **one row, core VOO only**. §5.1 and §5.2 were evaluated and have nothing to evaluate
against: all four sell rules are **ABSENT, NOT PASSING.** Core VOO is §5-exempt and was struck
from the working list rather than stamped as passing.

### REBALANCE

**NONE.** `sleeves` 07:03 ET: equity **$96,954.32** · core **VOO $66,954.32 = 69.06%** ·
satellite **$0 / 0.0% / count 0** · cash **$30,000 = 30.94%** · `core_in_band: true` ·
`rebalance_needed: false` · `rebalance_delta: 913.71`. **69.06% sits 4.06pp inside the 65%
edge** — a −4.37% session moved core_pct only −0.92pp, because the cash leg is inert and
scales nothing. ⚠ **The distance to §2's lower edge is −16.84% in VOO terms (≈$562.51), NOT
−6%; the −6% figure written by the 11-05 midday seat was wrong and is REPLACED, not carried.**
**NO REBALANCE DUE.**

---

## Revalidate

Nothing to revalidate — **no BUY intents.** The `revalidate` line names the specific number an
overnight gap could invalidate, and with no intent there is no number.

⚠ **One standing instruction that is NOT an intent:** if you execute nothing today, that is
correct and expected on this plan. Do **not** read an empty intent list as licence to
construct a trade at the point of execution — §4 requires the written thesis to pre-date the
order, and **no thesis dated today survived.**

⚠⚠ **A REAL EVENT LANDS BETWEEN THIS SEAT AND YOURS: the October employment report at 08:30
ET** (consensus +65k after +29k; UR 4.2%; wages 2.9%). This seat could not see it. **It is not
a reason to pre-position and it creates no intent** — but if the open seat finds the tape
violently different from the figures above, that is why, and the figures are stale rather
than wrong.

---

## Carry to the open seat

- **✅ 2026-11-05's OFFICIAL CLOSE IS NOW IN THE REPO AND THE PARTIAL BAR WAS WRONG BY $2.14.**
  **VOO 11-05 `c` 673.94** (`bars --adjustment all`; n 4,331 · v 170,486, ~2.5x the norm). The
  15:16 seat's **676.075** was a partial read, correctly flagged and never stamped. True session
  **−4.3731%** (704.76 → 673.94), not −4.04%. ⚠ **The partial understated the largest single-
  session decline in this repo's history by 8% of its own magnitude — item (12)/(15) priced in
  dollars for the first time. It cost nothing only because the sleeve is empty.**
- **Ledger reconciliation CLEAN, re-derived at this seat, not inherited:** three independent
  sides agree on zero satellites (`positions.md` count 0 · `sleeves satellite.count 0` ·
  `positions` core-only). Core VOO 99.046311231 sh @ 706.74, cost basis $69,999.99, unchanged
  since the 2026-09-03 fill; only the mark moves. Unrealised **−$3,045.67 / −4.351%**.
- **⚠⚠⚠ THE DIRECTION-BLIND `move` DEFECT NOW BLOCKS AN ENTIRE SECTOR, WHICH IS A BIGGER CLAIM
  THAN THE PREVIOUS EIGHT INSTANCES AND IS THE ONE NEW FINDING OF THIS RUN.** `alpaca.py move`
  thresholds **absolute** 5-session magnitude, so after an −12% SOX session it returns
  `priced_in: true` / *"LATE — skip"* on everything that fell: **NVDA −15.03% · MU −29.51% ·
  AMD −28.79% · QCOM −15.38%**, measured this run. Running tally **twelve "LATE" verdicts on
  twelve DECLINES across five sessions** (prior eight: INTC −24.36 · MU −7.77 · SNDK −14.40 ·
  STX −7.87 · WDC −4.96 · ON −7.69 · IREN −24.70 · NVDA −7.04). ⚠⚠ **CONSEQUENCE: until ~11-12,
  any genuine §4 candidate anywhere in semis dies at the hard filter before its thesis is read,
  on merit it never got to show.** ⚠ **OBEY IT ANYWAY — it fails safe, over-blocking and never
  wrongly permitting, and a seat must not reason past `priced_in: true` because the move was
  negative. Equally: NEVER quote such a reading as "the market has captured this upside"; it has
  now meant the reverse twelve times.** The fix is a signed threshold in `scripts/alpaca.py` —
  **script-level, NOT a seat's to install.** Human notified 11-03, 11-05, and again today
  because the *scope* changed from names to a sector.
