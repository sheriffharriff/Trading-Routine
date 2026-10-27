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
plan_date: 2026-10-27
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-27 at 09:30 ET** (`alpaca.py clock` at 08:20:09 ET: `is_open:
false`, `next_open: 2026-10-27T09:30:00-04:00`, `next_close: 2026-10-27T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

**The plan this run replaced was dated 2026-10-26 — ONE trading day and ONE calendar day
old, which is the ordinary Tuesday shape and not the Monday three-calendar-day shape the
carry-forward warns about.** It was fresh, consumed at 09:40 yesterday, and carried zero
intents. ⚠ **Irrelevant to execution either way: the 09:35 seat reads the date, not the
age.**

---

## Tape context

**Pre-market readings, and every one of them is a LIVE MIDPOINT, not an official close — do
not stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 08:20: equity **$99,928.68** · core VOO **$69,928.68 / 69.98%** · satellite
  **$0 / 0.0%**, count **0** · cash **$30,000.00 / 30.02%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: 21.40`.
- `positions`: **ONE row, core VOO only** — 99.046311231 sh, `avg_entry_price` **706.74**,
  `cost_basis` **$69,999.989999**, `current_price` **706.02** (live pre-market midpoint),
  `unrealized_pl` **−$71.31 / −0.102%**.
- ⚠ **`rebalance_delta: 21.40` IS A DISTANCE READOUT, NOT AN INSTRUCTION.** §2's band on
  today's equity is **$64,953.64–$74,946.51**; core sits **$21.40 below** the 70% target and
  **$4,975.04 above** the floor = **4.98% of equity from the nearer edge, not 0.02%**. All of
  the movement is the mark moving under a **FIXED SHARE COUNT** — no shares have changed
  since 2026-09-03.
- ⚠ **26TH SEAT ON THE `lastday_price` ITEM, re-stated not re-raised as new:** `positions`
  reports `lastday_price` **703.41** against yesterday's official `--adjustment all` close
  **703.435**. **Both ends of Alpaca's own P&L fields are live midpoints, which is a moving
  midpoint and not a fixed offset.** Use the official close basis for any P&L line that gets
  written down.

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

Core **69.98%**, inside §2's **65–75%** band with **4.98% of equity** of room to the nearer
edge. **No REBALANCE intent is queued.** The core sleeve is §5-exempt and was struck from
the §5 working list rather than stamped against any rule.

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | Reading | Blocks a buy? |
|---|---|---|
| `circuit_breaker` | **INACTIVE**, `halt_triggered_at: none` | No |
| `new_positions_this_week` | **0 of 3** | No |
| Satellite deployment | **0.0%**, count 0, **$30,000.00 idle** | No |
| `control.md` Notes | **EMPTY** | No |
| `control.md` `TRADING_ENABLED` | **true** (LIVE paper) | No |
| Open alerts | **ZERO**, nothing SYSTEMIC | No |
| 5% single-position cap (§6) | **$4,996.43** | **No operand** |

⚠⚠ **TODAY IS THE *EMPTY-PLAN* KIND OF ZERO, NOT THE *BLOCKED* KIND, AND THE TWO PRODUCE AN
IDENTICAL ORDER COUNT.** Research found nothing that could be written honestly. **A buy was
permitted at this seat and will be permitted at 09:35.** ⚠ **§4: "The correct output of most
research runs is no trade. A run that finds nothing worth buying is a successful run."**

---

## Week rollover (§6)

**Re-derived with `isocalendar()` from the date, not inherited from the field it was checked
against:** 2026-10-27 is a **Tuesday**, ISO **2026-W44**, weekday **2** → Monday anchor
**2026-10-26**. `state.md` `week_of` already reads **2026-10-26** → **MATCH. No rollover
performed. `new_positions_this_week` stays 0 of 3.**

⚠ **It stays at 0 because nothing was bought, not because a cap refused anything.**
⚠ **A match here means the 10-23 Friday review already did the forward roll — the §3
safety net was exercised and was not needed.** Monthly rollover not due until **2026-11-06**.

---

## Intents

### BUY — **NONE**

**Five theses written, five rejected, zero accepted** (`T-2026-10-27-01` … `-05`, with
seventeen individually-named items disposed across them). Full reasoning is in
`research_log.md`; it is **not to be re-litigated at 09:35**, and ⚠ **none of the five is
price-dependent, so no 09:35 quote or `move` call could revive any of them. Do not pull one
to try.**

The two that reached a named, eligible, above-$10B US-listed name:

- **`T-2026-10-27-01` — VZ / Amazon AWS, $2.0B+ AI-infrastructure fiber agreement** (Verizon's
  own dated 2026-10-26 Q3 release — ⚠ **provenance PASSES, this is not a rule (iii) failure**).
  Dead at **part 1** — VZ is a named party, so the drill asked for a THIRD company and got
  *"no source … identifies a specific third publicly traded equipment, optical-component,
  fiber, or construction supplier … with a dollar amount attributed to that company"* — and
  independently at **part 2**: the release calls the figure the **value of the agreement**,
  assigns it to **no reporting segment** and states **no term**, so no revenue share is
  calculable at all.
- **`T-2026-10-27-02` — GLW (Corning) / Verizon, 80M+ miles of fiber, 2027–2032.** Dead at
  **rule (iii)** — the agreement was announced **2026-09-08**, **seven weeks ago**, and reached
  this funnel only because Verizon's new 10-26 earnings release recapped it as *"last month."*
  Independently dead at **part 2's magnitude half**: ⚠ **no dollar value was ever disclosed by
  either party — "multi-billion dollar" is an adjective, and 80 million MILES is not money.**

The other three: **`-03`** UPS and Centene own-results/guidance (part 1 — a company's own
print is not a second-order catalyst; the read-across is the shared-cause object) ·
**`-04`** the **pending** 10-28 FOMC decision plus Treasury yields and the AI-financing theme
(no Company A; ⚠ **the decision has not happened yet, which is rule (iii) at its earliest
possible point** — and ⚠ **no second ID will be minted for it tomorrow when it has**) ·
**`-05`** an eleven-item sweep (unnamed counterparty, non-US listing, wrong quantity, no
figure, own results), **zero drill queries spent.**

### SELL — **NONE**

**There are no satellite positions to sell.** §5.1–5.4 are **ABSENT, NOT PASSING** — see
below. Core VOO is **§5-exempt** and is not a candidate for any sell rule.

### REBALANCE — **NONE**

Core **69.98%**, in band. See §2 above.

---

## Revalidation instructions for the 09:35 seat

**There is nothing to revalidate.** No BUY intent exists, so no `revalidate` line is owed and
none is written. ⚠ **This is the ABSENT state, not a skipped step — and a run summary cannot
tell those apart unless it says which it means. It is the absent kind.**

What the 09:35 seat still owes, none of it conditional on this plan:

1. **Reconcile the ledger three-sidedly BEFORE any order path** — Alpaca `positions` vs
   `positions.md` satellite header count vs `sleeves.satellite.count`. Expect **1 core row /
   0 / 0**.
2. **Re-read the §2 band against LIVE equity**, not against the 69.98% written here. ⚠ **The
   band is a statistic over a moving mark and cannot be carried — state the live reading
   against the two band edges rather than inheriting a range.**
3. **Skip the Step 3 core bootstrap** — `core_established: true`.
4. **Check `orders --status all` for anything in limbo** (§7). Expect the single 2026-09-03
   core fill, `filled`, already in `trade_log.md`. ⚠ **A check that was RUN and came back
   clean is a different statement from having nothing to check. Say which.**
5. ⚠ **Do not advance the session counter.** Routine 2 stands **before** the bell and may
   never count the day it is in. **Routine 4 is the only seat that may.**
6. ⚠ **Step 6's `voo_close_at_entry` is open human item (12) and is wrong on the first fill** —
   it sources the figure from a bar that is **partial at the moment it is called**. Costless
   today because there is no fill to write.

---

## §5 sell-rule status — ALL FOUR ABSENT, NOT PASSING (31st consecutive seat)

Counted forward from the 2026-10-26 close seat's **30th** in the same breath.

| Rule | Status at this seat | Why |
|---|---|---|
| **5.1** invalidation | **ABSENT** | No invalidation string exists, so **ZERO §5 news queries were DUE and none was run.** |
| **5.2** time stop | **ABSENT** | No deadline exists. |
| **5.3** hard stop (−7%) | **NOT COMPUTABLE** | No entry price. ⚠ **Different from "far from the stop."** |
| **5.4** trailing stop (−10%) | **NOT COMPUTABLE** | ⚠ **No `highest_close` has ever been written in this repo.** |

⚠⚠ **THE §5.4 TEMPTATION BY THE BACK DOOR WAS NOT OFFERED AT THIS SEAT AND NO BARS PULL WAS
MADE FOR P&L, SO NO WINDOW MAXIMUM LANDED ON SCREEN BESIDE A LIVE PRICE.** ⚠ **Core is
§5-exempt anyway, and a window maximum is not a since-entry trailing maximum.**

⚠⚠ **`consecutive_closed_losses` STAYS 0 — UNTOUCHED, NOT CHECKED-AND-CLEAN.** Nothing has
ever closed, so the §6 breaker increment, the breaker trip and the `circuit-breaker` alert
path have **never been exercised.** ⚠ **§5.1–5.4 and `alpaca.py sell` remain untested code
after 39 completed sessions — the 10-23 review's largest named exposure, now one more
session old.**

---

## Open items for the human — FIFTEEN, unchanged this run

No item was discharged and none was added. See `weekly_review.md` (week ending 2026-10-23)
for (1)–(14) in full and the 2026-10-26 `state.md` block for (15).

**(1)** the priced-in filter reads a **drawdown** as priced-in — `alpaca.py:177` tests
`abs(move)`; the one-line fix is to test the **signed** move. ⚠ **Sixteen instances. 10-21 is
the decisive sample: seven of seven candidates blocked while VOO over the identical window
returned −1.22% / `false`.** · **(2)** the same filter reads an **absorbed** event move as a
pass (AKAM). · **(3)** the structurally undeployed sleeve — **193 theses, 39 sessions, zero
accepted, $30,000 idle since inception.** · **(6)** `selftest.py` certifies a healthy system
without probing `clock` or market data. · **(7)** only a human may change §4 or
`alpaca.py move`. · **(8)** §1 as written is **unmeetable by construction** — the paper
account does not model dividends; ⚠ **and the 10-23 addition: choosing option (i) without
also switching the 704.83 since-inception reference to the RAW close is a no-op that looks
like a fix.** · **(9)** **file growth — see Housekeeping below.** · **(10)** the retained core
fill in `trade_log.md`. · **(11)** a routine can simply not run and nothing notices — ⚠ **the
subset detector now EXISTS and is FLAGGED, NOT RUNNING.** · **(12)** routine 2's Step 6
sources `voo_close_at_entry` from a **partial** bar — wrong on the first fill; the fix must
be the **source** of the number, not a guard on it. · **(13)** the since-inception excess has
two defensible conventions that **disagree in sign.** · **(14)** the reject board's rows are
**not persisted**, so each review **re-discovers** rather than **re-prices** them. ·
**(15)** routine 4's Output spec asks for *"high-water marks updated"*, **which is FALSE on
an empty ledger** and becomes a real misreport on the first fill.

---

## ⚠ Housekeeping — the corpus, measured from the commit

**Read from `HEAD` as the 10-26 close seat instructed, not from the working tree:**
`git show HEAD:state.md HEAD:positions.md HEAD:research_log.md HEAD:journal.md | wc -c` =
**905,501B** at the 10-26 close commit.

The committed series, all on the same post-commit basis: **515,427** (10-14) → **619,565**
(10-16) → **698,793** (10-20) → **870,403** (10-23) → **905,501** (10-26).

⚠⚠ **TWO READINGS, AND THE SECOND ONE MATTERS MORE THAN THE FIRST.** Over the eight sessions
10-14 → 10-26 the rate is **+48.8KB/session**, which confirms the 10-23 finding: **roughly
double** the +23KB/session recorded on 10-14. ⚠ **But the 10-26 session alone added
+35,098B, BELOW that average — and per this file's own rule, ONE SESSION'S DELTA IS NOT A
TREND IN EITHER DIRECTION. It is reported because omitting the unflattering-to-the-narrative
half would be the same selectivity the corpus logs against.**

⚠ **ONE PREDICTION TO CORRECT RATHER THAN REPEAT: the 10-26 block said "the corpus crosses
1MB this week." On the tracked four-file measure IT HAS NOT — 905,501B, i.e. 94,499B short,
about two sessions at the current rate.** *(The all-markdown working-tree figure is larger,
but that is a different measure and mixing them is the basis defect this repo keeps logging.)*

⚠ **NO SELF-MEASURING FIGURE FOR THIS RUN IS QUOTED ANYWHERE IN THIS FILE, AND THAT IS THE
FINDING, NOT AN OMISSION.** Three honest drafts on 10-26 produced three wrong numbers because
a figure about a run's own work changes as the run writes it down. **Tonight's close seat
reads this run's delta from `git diff --stat HEAD~1`, not from a sentence written here.**

⚠⚠ **WHAT THIS SEAT DID WITHIN ITS OWN AUTHORITY, STATED AS A CHOICE AND NOT AS A FIX: it
wrote its own entries DELIBERATELY TERSER than the recent average** — five rejections carrying
one genuinely new finding, with the shared reasoning referenced by rule name rather than
re-derived, and seventeen sweep items disposed in one entry. ⚠ **That is not the structural
cap. The cap is still the human's: bound `research_log.md` per entry, pull the monthly
rollover forward, or accept that the corpus is write-only beyond some date — and NEITHER a
seat nor this plan may invent it.** ⚠ **One seat writing tersely once a day cannot outrun
four seats appending.**

---

## ⚠ One correction this run made to itself

⚠⚠ **A FIRST DRAFT OF THIS RUN WROTE *"FIFTEENTH CONSECUTIVE SESSION"* FOR THE FUNNEL'S
NEGATIVE-ANSWER STREAK. THAT INHERITED-AND-INCREMENTED A COUNTER THAT IS STALE AT FOURTEEN /
2026-10-16 AND HAS NOT BEEN ADVANCED SINCE.** The seven sessions between are not cheaply
re-derivable, and ⚠ **10-20 is a CANDIDATE BREAK — `MMM` reached the priced-in filter that day, so
the funnel DID produce a candidate.** ⚠⚠ **A COUNTER REACHED BY AN UNCHECKED ROUTE IS NOT A CHECKED
FACT: recurring error 4, caught inside this run's own draft, in the very paragraph reporting on the
funnel.** **The tracked figure stays FOURTEEN; today is recorded as an INSTANCE, not an ordinal.**
⚠ **The companion figure a draft also reached for — "eleventh session in which the two framings
disagreed" — is NOT QUOTED anywhere, for want of a re-derivation.** ⚠ **The correction REPLACES the
claim in `state.md` and `research_log.md` rather than sitting beside it.**

---

## ⚠ Agenda for tonight's close run

1. ⚠⚠ **STEP 2 WILL HAVE NO OPERAND AND THE HONEST FORM IS *THE JOB HAD NO SUBJECT*** — zero
   satellite rows, so there is no `highest_close` to raise and no `(as of …)` date to advance.
   **Do NOT write "high-water marks updated"** (open item 15). **No backfill is owed: a mark
   that does not exist cannot be stale.**
2. **Advance the session counter to 40 completed / 37 post-fill** — ⚠ **the close seat is the
   only seat entitled to count the day it stands in.** Re-derive from a `bars --days 90` pull
   and ⚠ **EXCLUDE TODAY'S DATE ONLY IF THE PULL IS MADE BEFORE THE BELL; after the bell
   today's bar is a finished session row and belongs in the count.**
3. **Hold the thesis count at 198** (87 archived + 111 live) — the close routine writes no
   theses and today's five are already written. ⚠ **Re-derive by `grep` on unique IDs; do not
   inherit-and-increment.** ⚠ **The plain `grep -cE '^### T-'` returns one more because of the
   heading inside `## Template`.**
4. **Read the corpus size and this commit's line delta FROM THE COMMIT** (`git show …`,
   `git diff --stat HEAD~1`). ⚠ **Quote no figure this run computes about its own work.**
5. **Collapse the 2026-10-27 date block in `state.md` and `positions.md`** — ⚠ **the close
   seat is the only seat entitled to collapse what three earlier seats wrote**, and ⚠ **report
   the collapse figure MEASURED AFTER THE FACT, never from intent.**
6. **Day P&L on the official close basis** (`bars --days 5 --adjustment all`), not on
   `account`'s own fields — ⚠ **both ends of those are live midpoints.**
