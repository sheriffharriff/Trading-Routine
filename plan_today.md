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
plan_date: 2026-11-02
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-11-02 at 09:30 ET** (`alpaca.py clock` at 07:01:56 ET: `is_open:
false`, `next_open: 2026-11-02T09:30:00-05:00`, `next_close: 2026-11-02T16:00:00-05:00`).
**NOT a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

⚠ **NOTE THE OFFSET CHANGE: `-05:00`, NOT `-04:00`. US daylight saving ended Sunday
2026-11-01, so every timestamp in this file is EST where last week's were EDT.** The
scripts read ET from the API and are unaffected; the figure to watch is that **this run
fired at 07:01 ET against last week's 08:03–08:21 band.** The schedule is nominally 08:00
ET and the clock call confirms 07:01:56 ET, ~59 minutes early — consistent with a
UTC-anchored schedule that did not follow the fall-back. ⚠ **Recorded as an observation for
the human, NOT acted on: an early pre-market run is harmless (the market is shut either
way and this routine places no orders), and nothing in this plan depends on the hour. But
if the open run also fires an hour early it would fire at 08:35 ET, BEFORE THE 09:30 OPEN,
and that is NOT harmless — it would read a closed market and execute nothing.** See the
carry-forward item.

The plan this run replaced was dated **2026-10-30** — the previous trading day (Friday),
the ordinary Monday shape. It was fresh when consumed and carried **zero intents**.

---

## Tape context

**Pre-market readings, and every one of them is a LIVE MIDPOINT, not an official close — do
not stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 07:01: equity **$99,142.25** · core VOO **$69,142.248944 / 69.74%** ·
  satellite **$0 / 0.0%**, count **0** · cash **$30,000.00 / 30.26%** · `core_in_band:
  true` · `rebalance_needed: false` · `rebalance_delta: 257.33` · `core_target_value:
  $69,399.57`.
- `positions`: **ONE row, core VOO only** — 99.046311231 sh, `avg_entry_price` **706.74**,
  `cost_basis` **$69,999.989999** (unchanged since 2026-09-03 — **only the mark moving**),
  `current_price` **698.08** (live pre-market midpoint), `unrealized_pl` **−$857.74 /
  −1.225%**.
- ⚠ **`rebalance_delta: 257.33` IS A DISTANCE READOUT, NOT AN INSTRUCTION.** §2's band on
  this equity is **$64,442.46–$74,356.69**; core sits **$257.33 below** the 70% target,
  **$4,699.79 above the floor** and **$5,214.44 below the ceiling** = **4.74% of equity
  from the nearer edge, not 0.26%.** **Nearer edge is the FLOOR, fifth consecutive seat.**
  All of the movement is the mark moving under a **FIXED SHARE COUNT**.
- ⚠ **THE PRE-MARKET MARK IS UP, NOT DOWN, AND IT IS THE FIRST TIME IN FOUR SESSIONS THIS
  LINE HAS READ THAT WAY.** `lastday_price` **694.81** against `current_price` **698.08** =
  **+0.47%**, and Alpaca's own `change_today` agrees at **+0.00471**. ⚠ **DO NOT READ THIS
  AS A FORECAST.** The three pre-market gap calls of 10-28, 10-29 and 10-30 went
  wrong-wrong-right, and the one that was right was understated by 0.68pp. **One held
  warning in three is not a calibrated signal, and a gap-UP call has never been tested at
  all.** The open seat re-reads the band against **live equity at the open**.
- ⚠ **`lastday_price` 694.81 IS A BROKER FIELD AND IT IS 0.11 ABOVE FRIDAY'S OFFICIAL
  CLOSE of 694.70** (`bars --adjustment all`, recorded by the 10-30 16:17 close seat).
  **31st seat on the broker-pair item.** The 10-28 close seat recorded `lastday_price`
  **0.06 above** that day's official close and the 10-30 seat found the bottom end exact to
  eleven decimal places — **three different patterns in three readings, which is the
  mechanism (a live midpoint still moving) and not a discrepancy.** Use the official close
  basis for any P&L line that gets written down.
- ⚠ **Equity read $99,142.25 at pre-flight and $99,142.25 at `sleeves` — IDENTICAL this
  morning**, because the pre-market tape was thin at 07:01. That is the same moving-midpoint
  mechanism at a moment when it happened not to move; it is **not** evidence the fields
  agree in general.

**WEEKEND WINDOW SURVEYED:** Friday 2026-10-30 after the close through this morning, plus
the Thursday 2026-10-29 after-close disclosures that drove Friday's session and which no
prior seat logged.

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

Core **69.74%**, inside §2's **65–75%** band with **4.74% of equity** of room to the nearer
edge (the **floor**, fifth consecutive seat). **No REBALANCE intent is queued.** The core
sleeve is §5-exempt and was **struck from the §5 working list rather than stamped against
any rule** — not stamping it is the correct action, not an omission.

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | Reading | Blocks a buy? |
|---|---|---|
| `circuit_breaker` | **INACTIVE**, `halt_triggered_at: none` | No |
| `new_positions_this_week` | **0 of 3** (week anchor **2026-11-02**, re-derived with `isocalendar`: ISO 2026-W45, weekday 1 — **matches `week_of`, ALREADY ROLLED, no second roll**) | No |
| Satellite deployment | **0.0%**, count 0, **$30,000.00 idle** | No |
| `control.md` Notes | **EMPTY** | No |
| `control.md` `TRADING_ENABLED` | **true** (LIVE paper) | No |
| Open alerts | **ZERO**, nothing SYSTEMIC | No |
| 5% single-position cap (§6) | **$4,957.11** | **No operand** |

⚠⚠ **TODAY IS THE *EMPTY-PLAN* KIND OF ZERO, NOT THE *BLOCKED* KIND, AND THE TWO PRODUCE AN
IDENTICAL ORDER COUNT.** Research found nothing that could be written honestly. A buy was
permitted at every gate and was not available — §4's honest-broker paragraph says that is
the correct output, and the distinction is the only thing that tells a working funnel apart
from a halted one. **Satellite target at this equity: $29,742.68 against $0 held.**

---

## BUY intents

**NONE. ZERO BUY INTENTS.**

**Five candidates were seriously considered and all five were rejected** —
`T-2026-11-02-01` … `-05`, disposed in full in `research_log.md`. The summary, with the
rung each died on:

| ID | Candidate | Died on |
|---|---|---|
| `-01` | **INTC** — Q4 guide-down + Fab 28 Kiryat Gat shutdown | **Rule (v)** — substrate supply base UNNAMED; the named substrate makers are JP/TW/AT-listed (**§3**). INTC itself **priced-in −24.36%** and first-order. |
| `-02` | **SYM / WMT** — Walmart's ~$6B automation commitment | **Part 1 / rule (v)** — both named parties are FIRST-ORDER; Symbotic's component base is unnamed and the source applied the kill itself. |
| `-03` | **MU** — memory shortage read across from Intel's demand commentary | **Part 1** — shared-cause market variable; needs an "and also". |
| `-04` | **CRL** — Charles River / Ipsen Virtual Control Group expansion | **Part 2** — NO dollar value disclosed at all. **Priced-in also fires at +4.18%.** |
| `-05` | sweep — Meta 8-K, Hashdex, Precision Optics, AVGO/Korea, L, CVX, Gigabyte, forward calendar | **§3 / rule (iii) / part 1**, nine items disposed as one. |

### ⚠⚠ The two things in this plan the open seat should carry forward

1. **⚠⚠ THE PRICED-IN FILTER FIRED TWICE THIS MORNING, AND THAT ANSWERS AN OPEN COMPLAINT
   RATHER THAN SETTLING IT.** Open item 1 and the 10-30 weekly review both record that the
   §4 priced-in filter **fired zero times** last week — *"not passed, never reached"*, so a
   standing complaint about a filter that had no opportunity to be wrong. **This morning it
   reached two live candidates and killed on both: INTC at −24.36% and CRL at +4.18%
   against a 4.00% threshold.** ⚠ **BUT NEITHER IS A CLEAN TEST OF THE FILTER, AND THE
   HONEST FORM MATTERS:** INTC is **first-order and the wrong sign** (a −24% collapse is not
   a §4 second-order long and the filter is not what disqualifies it), and **CRL fails part
   2 independently** — no dollar value is disclosed anywhere in the source. ⚠⚠ **AND ON CRL
   THIS SEAT CANNOT CLAIM THE FILTER WAS THE BINDING KILL: the §3/part-2 query and the
   `move` call were issued IN THE SAME TOOL CALL, so the ordering §4 requires ("apply these
   before writing the thesis") was satisfied against the thesis but NOT between the two
   checks.** Both results are recorded; neither is promoted. ⚠ **CRL at +4.18% is the
   closest the filter has ever come to a marginal reading — 18bp over — which is the first
   datapoint this log has on the threshold being near rather than far.**
2. **⚠⚠⚠ THE SCHEDULE MAY NOT HAVE FOLLOWED THE DST FALL-BACK, AND THE OPEN SEAT IS WHERE
   THAT STOPS BEING HARMLESS.** This run fired at **07:01:56 ET** against a nominal 08:00
   ET schedule and against last week's observed 08:03–08:21 band — **~59 minutes early, on
   the first weekday after DST ended (2026-11-01)**, which is exactly the signature of a
   schedule anchored in UTC. ⚠ **For routine 1 this costs nothing: the market is shut at
   07:01 and at 08:00 alike, this routine places no orders, and the research window is a
   calendar window not a clock window.** ⚠⚠ **FOR ROUTINE 2 IT IS NOT HARMLESS. A 09:35
   schedule shifted the same way fires at 08:35 ET — BEFORE THE 09:30 OPEN — and would read
   `is_open: false` and execute nothing, producing a zero-order run indistinguishable from
   this empty plan.** ⚠ **THE OPEN SEAT MUST RECORD ITS OWN FIRING TIME AND `clock`
   `is_open` EXPLICITLY, AND IF IT FINDS ITSELF PRE-OPEN IT MUST SAY SO AS A SCHEDULE FAULT
   AND NOTIFY, NOT WRITE "market closed, nothing to do".** This seat may not diagnose the
   schedule from its own timestamp alone — `control.md` warns that manual "Run now"
   invocations are indistinguishable from scheduled ones in run logs — so this is logged as
   **ONE OBSERVATION PLUS A CONDITIONAL INSTRUCTION, NOT A CONFIRMED FAULT.**

### ⚠ Do not mint an ID for these

- **The forward calendar, for the EIGHTH Monday pre-market seat.** The weekend window
  contains no trading, so the funnel fills the space with the week ahead: **Apple and
  Palantir report TODAY 11-02**, **AMD Tuesday**, **Qualcomm / Arm / Arista later in the
  week**, the **October employment report 11-06**, **ISM manufacturing and services** this
  week. ⚠ **ALREADY DISPOSED at `T-2026-10-12-05` and `T-2026-10-13-08`; a third entry
  would inflate the thesis count rather than record anything. NOTE THE DATES AND DO
  NOTHING.** An 11-02 earnings print is for the 11-02 midday and close seats to meet, and
  §4 would kill the read-across as the competitor's-earnings-print shared-cause object.
- **The "$5 trillion AI wipeout."** The weekend coverage is dominated by the week's
  AI-complex drawdown and a sell-side call for a further 9% S&P decline. ⚠ **A market move
  is not a Company A — no named recipient, no transaction, one party. It is the
  government-action/macro object wearing the market's own clothes, and SCALE MAKES IT MORE
  CONVINCING, NOT LESS.**
- **RTX, GNRC, Venture Global, GE Vernova.** Standing disposals. None appeared this
  morning; **zero queries were spent confirming that**, which is the point of the
  recognise-on-sight list.

---

## SELL intents

**NONE — AND THE HONEST FORM IS THAT §5 HAD NO SUBJECT, NOT THAT IT PASSED.**

`positions.md` contains **ZERO satellite position blocks** (`grep -cE '^### [A-Z]'` = 0)
and Alpaca `positions` returns **one row, core VOO only**. **Rules §5.1, §5.2, §5.3 and
§5.4 are ABSENT, NOT PASSING — 46th consecutive absent seat.**

- **§5.1 thesis invalidation** — no thesis is held, so no invalidation condition exists to
  check. **No Perplexity news query was spent on a position, because there is no position.**
- **§5.2 time stop** — no timing window is running.
- **§5.3 hard stop (−7% from entry)** — no entry price exists on any satellite name.
- **§5.4 trailing stop (−10% from `highest_close`)** — **no `highest_close` exists, and the
  field is in its THIRD STATE: ABSENT CARRYING NO DATE, which is neither current nor
  stale.** ⚠ **The backfill instruction in `positions.md`'s header discharges VACUOUSLY on
  an empty ledger — a clean result here is byte-identical to a clean result over
  correctly-maintained marks, which is the silent failure the header itself describes.**
- **Core VOO is §5-exempt and was STRUCK from the working list, not stamped.** No
  `highest_close` was written for it — **108th run.**

**Nothing is queued as already-breaching for the midday seat.**

---

## REBALANCE intents

**NONE.** Core **69.74%** is inside §2's **65–75%** band. `rebalance_needed: false`.

⚠ **The open seat must re-read `sleeves` against live equity at the open rather than acting
on the 07:01 figure — the band and the core value move together under a fixed share count,
and core had 4.74% of equity of room to the nearer edge (the FLOOR) at 07:01.**

---

## What the open seat should actually do at 09:35

1. **Record your own firing time and `clock` `is_open` EXPLICITLY, as the first line of
   your run.** See carry-forward item 2 above: if you are pre-open, that is a **schedule
   fault to be named and notified**, not a quiet no-op.
2. **Confirm `plan_date: 2026-11-02` matches today's ET date.** If it does not, this plan
   is stale — log it, alert, and go straight to the §2 section.
3. **Execute nothing from the BUY section. It is empty by research, not by blockage.** ⚠
   **Do not read an empty plan as permission to find something at 09:35** — §4 requires a
   written thesis that has slept, and nothing in this file authorises a buy.
4. **Re-read `sleeves`.** If core has left the 65–75% band on the open print, queue and
   place the §2 rebalance to 70%. At 07:01 it had 4.74% of equity of room to the floor, so
   this is unlikely but must be read, not assumed.
5. **Reconcile the ledger three ways again** — Alpaca `positions`, `positions.md` satellite
   count, `sleeves.satellite.count`. All three read **0 satellite / 1 core row** at 07:01.
6. **Run the §7 limbo check** (`orders --status all`). At the last check there was **exactly
   one order in the account's entire history** — `d177d8f0`, 2026-09-03, filled, terminal,
   already in `trade_log.md`. **Anything else is new and needs explaining.**
7. **Do not stamp any pre-market midpoint from this file into `positions.md`.** Every price
   above is a live midpoint. Friday's official close is **694.70** on an `--adjustment all`
   basis.
