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
plan_date: 2026-10-30
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-30 at 09:30 ET** (`alpaca.py clock` at 08:17:22 ET: `is_open:
false`, `next_open: 2026-10-30T09:30:00-04:00`, `next_close: 2026-10-30T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

The plan this run replaced was dated **2026-10-29** — one trading day old, the ordinary
midweek shape. It was fresh when consumed and carried **zero intents**.

---

## Tape context

**Pre-market readings, and every one of them is a LIVE MIDPOINT, not an official close — do
not stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 08:17: equity **$99,285.87** · core VOO **$69,285.87 / 69.78%** · satellite
  **$0 / 0.0%**, count **0** · cash **$30,000.00 / 30.22%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: 214.24`.
- `positions`: **ONE row, core VOO only** — 99.046311231 sh, `avg_entry_price` **706.74**,
  `cost_basis` **$69,999.989999** (unchanged since 2026-09-03 — **only the mark moving**),
  `current_price` **699.53** (live pre-market midpoint), `unrealized_pl` **−$714.12 /
  −1.02%**.
- ⚠ **`rebalance_delta: 214.24` IS A DISTANCE READOUT, NOT AN INSTRUCTION.** §2's band on
  this equity is **$64,535.82–$74,464.40**; core sits **$214.24 below** the 70% target,
  **$4,750.05 above the floor** and **$5,178.54 below the ceiling** = **4.78% of equity from
  the nearer edge, not 0.2%.** All of the movement is the mark moving under a **FIXED SHARE
  COUNT**.
- ⚠ **THE GAP-DOWN IS REAL THIS MORNING, AND IT IS THE THIRD DAY RUNNING THIS LINE HAS BEEN
  WRITTEN BUT THE FIRST TIME IT IS LARGE.** `lastday_price` **707.32** against
  `current_price` **699.53** = **−1.10%**. The two previous pre-market gap warnings (10-28,
  10-29) both failed — the mark rose instead. **This one is ~2.4× the size of either, and
  core's unrealised P&L has crossed from −$7.92 to −$714.12 in one session.** The open seat
  must re-read the band against **live equity at the open**; the band and the core value move
  together, and core had **4.78%** of room at 08:17.
- ⚠ **30TH SEAT ON THE BROKER-PAIR ITEM, re-stated not re-raised as new:** both ends of
  Alpaca's own P&L fields are live midpoints, so the broker/official gap is a **moving
  midpoint, not a fixed offset.** Use the official close basis for any P&L line that gets
  written down.
- ⚠ **Equity read $99,299.73 at pre-flight (08:16) and $99,285.87 at `sleeves` (08:17) —
  −$13.86 in one minute, from the same account. That is the moving-midpoint mechanism, not a
  discrepancy.**

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

Core **69.78%**, inside §2's **65–75%** band with **4.78% of equity** of room to the nearer
edge (the **floor**, for the first time in several sessions — the gap-down moved the nearer
edge from the ceiling side to the floor side). **No REBALANCE intent is queued.** The core
sleeve is §5-exempt and was **struck from the §5 working list rather than stamped against any
rule** — not stamping it is the correct action, not an omission.

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | Reading | Blocks a buy? |
|---|---|---|
| `circuit_breaker` | **INACTIVE**, `halt_triggered_at: none` | No |
| `new_positions_this_week` | **0 of 3** (week anchor 2026-10-26, re-derived with `isocalendar`, ISO 2026-W44, no rollover) | No |
| Satellite deployment | **0.0%**, count 0, **$30,000.00 idle** | No |
| `control.md` Notes | **EMPTY** | No |
| `control.md` `TRADING_ENABLED` | **true** (LIVE paper) | No |
| Open alerts | **ZERO**, nothing SYSTEMIC | No |
| 5% single-position cap (§6) | **$4,964.29** | **No operand** |

⚠⚠ **TODAY IS THE *EMPTY-PLAN* KIND OF ZERO, NOT THE *BLOCKED* KIND, AND THE TWO PRODUCE AN
IDENTICAL ORDER COUNT.** Research found nothing that could be written honestly. A buy was
permitted at every gate and was not available — §4's honest-broker paragraph says that is the
correct output of most research runs, and it is the output here for the **40th post-fill
session**.

---

## BUY intents

**NONE.**

Six theses written this morning (`T-2026-10-30-01` … `-06`), **six rejected, zero accepted.**
Nothing reached the four-part test with all four parts writable, so **there is no number for
the open seat to re-validate.** Full disposals are in `research_log.md` and are **not to be
re-litigated at 09:35.**

The one-line reasons, so the open seat does not have to go and read them:

| ID | Candidate | Died at |
|---|---|---|
| `-01` | **ASE Technology (ASX)** capex **$10.5B → $11.5B** → the assembly / advanced-packaging / test equipment tier | **Rule (v) / part 1 — THE SUPPLY TIER IS UNNAMED.** ⚠ **This is the day's finding and it is the opposite of what the last two sessions predicted: rule (iii) genuinely PASSED on the figure the mechanism runs on** (prior **$10.5B dated 2026-07-30**, itself a raise from $8.5B; new figure **2026-10-29**) **and the thesis still died one rung later.** ASE discloses the equipment split as **60% LEAP / 40% mainstream** and **names no vendor**; the source states outright that no US-listed supplier names ASE or quantifies ASE revenue, and that attributing one *"would be an inference, not a reported customer relationship."* |
| `-02` | **AMZN** FY2026 capex **~$220B** → the AI-infrastructure supply base | **Rule (iii) costume #1 — REAFFIRMED, not raised.** The fourth large AI-capex disclosure in two sessions that did not move up. **Part 2 independently**: increment is **$0**, and rule (v) — the supply base is unnamed. |
| `-03` | **BMRN** ← GC Biopharma / Hanmi, licence *"up to $475M"* ($70M upfront + $405M milestones) | **Part 1 — BMRN *IS* a named party**, so there is no Company B; a second-order drill would need a THIRD company and none is named. **Part 2 scale**: $70M upfront against BMRN's revenue base is ~2%, far under §4's 10% floor, before the direction of payment is even established. ⚠ **The funnel's self-exclusion was WRONG and is corrected here — it said "the two Korean companies are not US-listed"; BioMarin is the US-listed leg. A self-exclusion is a HINT, NOT A RULING** (the 10-13 Bloom lesson, second instance). |
| `-04` | **Orion Group Holdings** $250M October awards · **AEVEX** $41.6M | **§3 cap floor — both are far below $10B**, and both are **own-award announcements** (part 1, no second party). Disposed on a single number each. |
| `-05` | **RTX** — the 2026-10-13 award **RE-SERVED**, third consecutive session the funnel has re-served this log's own disposed rejects | **Rule (iv), and ZERO QUERIES SPENT.** Scan 2 volunteered the kill itself: *"refers to an RTX contract announced on October 13, not October 29 or 30."* ⚠ **Audit catch: the inherited count of "six appearances" undercounts by one — it omitted `T-2026-09-01-03` (RTX, died at part 1), which sits in the September archive. Re-derived from thesis headers: 09-01 · 09-29 · 10-02 · 10-09 · 10-12 · 10-14 · 10-20 = SEVEN prior. Today is the EIGHTH.** |
| `-06` | sweep of **thirteen** items — T1 Energy · Samsung Electro-Mechanics $659.3M · Critical One / SICC · Woodside / QatarEnergy · ABP / Dovecote (UK CMA) · ATI · RPC · Shell · Sterling Infrastructure · HII Q3 · General Dynamics Q3 · Exelon Q3 · Regeneron Q3 | **§3 ×4 · unnamed counterparty ×2 · no figure disclosed ×2 · own-results ×5.** Disposed as one, **zero drill queries spent.** |

### ⚠⚠ The one thing in this plan the open seat should carry forward

**DIRECTION WAS NEVER THE BINDING CONSTRAINT ON THE AI-CAPEX COMPLEX. NAMING IS.** For two
sessions this log has recorded that no capex figure moved up, as though an upward move were
the thing standing between it and a trade. **Today one moved up — ASE, +$1.0B, on the figure
that actually has a supplier chain hanging off it, with the company's own prior figure
present and dated in the source — and the thesis died anyway, at rule (v), because the
supplier tier is not named by anybody.** ⚠ **A capex raise is a necessary condition that was
never close to sufficient. If the 09:35 or 12:4x seat feels pull toward this complex, the
answer is written and needs no new query.**

### ⚠ Do not mint an ID for these

**AMZN's reaffirmation, ASE's suppliers, the RTX 10-13 re-serve, and VRT.** All four are
disposed above or in prior sessions. VRT died at part 1 on 10-28 and was +14.48% over five
sessions as of yesterday — structurally dead and mechanically late. **Do not re-litigate any
of them at 09:35.**

---

## SELL intents

**NONE — and this is the NO-OPERAND kind of none, not the nothing-breached kind.**

**Zero open satellite positions**, so §5.1–§5.4 had **no operand at any step**: no
`invalidation` string to test news against, no `timing_window` deadline to compare a date
to, no `entry_price` to measure −7% from, and **no `highest_close` has ever been written in
this repo** to measure −10% from. ⚠ **ZERO §5.1 news queries were run and ZERO were due — all
five Perplexity calls at this seat were §4 research. Do not read the call count as §5 work.**

⚠ **The §5 machinery — 5.1 through 5.4, `alpaca.py sell`, the breaker increment, the breaker
trip and the circuit-breaker alert path — remains UNTESTED CODE after 48 completed sessions
and 45 post-fill.** The first live satellite fill will exercise all of it at once.

---

## REBALANCE intents

**NONE.** Core **69.78%**, in band, `rebalance_needed: false`. See §2 above.

⚠ **But read the band at the open rather than inheriting this line.** The gap-down is −1.10%
and real; core is now nearer the **floor** than the ceiling for the first time in several
sessions. A further ~4.8% fall in VOO against unchanged cash would put core through the 65%
edge and make a REBALANCE genuinely due. **That is a distance, not a forecast.**

---

## What the open seat should actually do at 09:35

1. Read `plan_date` — it says **2026-10-30**, today. The plan is fresh.
2. Re-reconcile the ledger three-sided (`positions` / `positions.md` satellite header count /
   `sleeves`). ⚠ **Re-derive it; do not inherit this seat's reading.**
3. **Nothing to execute.** Zero BUY, zero SELL, zero REBALANCE. **There is no revalidation
   step today, because no intent carries a number.**
4. Re-check the §2 band against **live equity at the open** — see the gap-down note above.
5. Run the §7 limbo check (`orders --status all`) and confirm it still returns **exactly one
   order in the account's entire history** (`d177d8f0`, 2026-09-03, filled, already in
   `trade_log.md`). It did at 08:17 today.
6. ⚠ **Today is Friday — routine 5 runs after the close and owns the monthly rollover.**
   `research_log.md` is **437KB** and October's live entries are larger than September's
   whole archive. **That rollover is the only mechanism that reaches the file, and open item
   16 is live.** Not the open seat's job; recorded so it is not missed.
