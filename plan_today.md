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
plan_date: 2026-10-19
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-19 at 09:30 ET** (`alpaca.py clock` at 08:13:13 ET: `is_open:
false`, `next_open: 2026-10-19T09:30:00-04:00`, `next_close: 2026-10-19T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean.**

⚠ **THE MONDAY SHAPE ARRIVED EXACTLY AS FRIDAY'S REVIEW PREDICTED, AND IT IS NOT A FAULT.**
The plan this run replaced was dated **2026-10-16** — **three CALENDAR days but ONE TRADING
day** old. **Compared against the last trading day, not the calendar. Noted; nothing done.**

---

## Tape context

**Pre-flight selftest: 5/5** (env · Alpaca ACTIVE `trading_blocked=False` · Perplexity
`sonar-pro` · ClickUp · `control.md` LIVE). `TRADING_ENABLED: true`, **LIVE paper**,
`control.md` **Notes empty**. **Zero open alerts** (`alerts.md` Open incidents: *(none)*).
**Zero non-terminal orders** — the whole account history is still **ONE order** (the
2026-09-03 core fill, `filled`, terminal), so §7's order-limbo warning has **no operand**
rather than a clean bill.

**Numbers, each with its call and its basis — never differenced across calls.**

| Reading | Value | Call / basis |
|---|---|---|
| Account equity | **$99,852.41** | `sleeves` 08:13, live broker mark |
| Cash | **$30,000.00** exactly | `sleeves` — ~**36th** consecutive unchanged reading |
| Core VOO | **$69,852.410996** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:13 |
| Core % | **69.96%** | `sleeves`, live-mark basis |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **30.04%** | `sleeves` |
| Unrealized P&L on core | **−$147.579003 / −0.211%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **705.25** | `positions` `current_price`, 08:13 — a **pre-market indicative mark, NOT a close** |
| VOO official 10-16 close | **701.745** | `bars --days 6 --adjustment all`, **this run's own pull** (o 710.78 = the high, l 699.53) |
| VOO `lastday_price` | **701.61** | ⚠ **NOT the official close. See the warning below.** |
| §6 5% cap | **$4,992.62** | 99,852.41 × 5%, **with no operand** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (0.00519), OR
`unrealized_intraday_pl` (+$360.528573) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **701.61** against the official 10-16 close of **701.745**
confirmed by this run's own `bars` pull.
⚠⚠ **AND THE STALE-`lastday_price` SERIES DID SOMETHING NEW THIS MORNING: THE GAP FLIPPED
SIGN AND WIDENED.** Four prior seats carried **+$0.06** (709.43 against 709.37). Today it is
**−$0.135** (701.61 against 701.745) — **more than double the magnitude, opposite direction.**
⚠ **A sixth consecutive seat on a defective field, and the defect is NOT a fixed offset that
could be corrected for. Never difference the two.**

---

## Reconciliation

1. **LEDGER RECONCILED FIRST, BEFORE ANY RESEARCH AND BEFORE ANY SELL RULE WAS READ. THREE
   SIDES AGREE.** `positions.md` holds **zero satellite blocks** · `alpaca.py positions`
   returns **one row, VOO**, 99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999**,
   **unchanged since 2026-09-03** · `sleeves` reports `satellite.count: 0`.
   ⚠ **No discrepancy. Nothing was researched on top of a ledger in doubt.**
   ⚠ **GREP TRAP, so the next seat does not re-raise it: `entry_price` / `highest_close` /
   `invalidation` return hits in `positions.md` that are ALL INSIDE `## Template`. That is the
   expected reading of an EMPTY ledger, not a position.**
2. **WEEK ROLLOVER — RECOMPUTED FROM SOURCE, NOT READ OFF THE FIELD.**
   `America/New_York` → **2026-10-19, Monday, ISO week 43, weekday 1, Monday anchor
   2026-10-19.** That **MATCHES** `week_of: 2026-10-19`, which Friday's review had already
   advanced. So `new_positions_this_week` was **NOT re-reset** — it stands at **0 of 3**
   because nothing has been opened, not because this run zeroed it. ⚠ **The distinction
   matters: a run that resets a counter it did not need to reset would mask a §6 breach.**
3. **CIRCUIT BREAKER — INACTIVE.** `consecutive_closed_losses: 0`, `halt_triggered_at: none`.
   ⚠ **Because `halt_triggered_at` is `none`, the `HALT_CLEARED_AT` comparison in `control.md`
   has no operand — there is nothing to clear, and `HALT_CLEARED_AT: none` is therefore
   CORRECT and not an oversight. New positions are NOT barred by §6's halt.**
4. **§5 HAS NO OPERAND.** Zero satellite positions → rules 5.1–5.4 are **ABSENT, not passing**,
   and `highest_close` does not exist as a field. **No Perplexity invalidation checks were run
   on holdings, because there are no holdings.** Core VOO was struck from the working list
   **before** any §5 rule was read, per §5's core exemption.

---

## Sleeve check (§2)

**Core 69.96%, IN BAND** (65–75%), **4.96pp above the lower edge and 5.04pp below the upper.**
`core_in_band: true`, `rebalance_needed: false`.
⚠ **`rebalance_delta: +44.28` is a NINTH reading and a DISTANCE READOUT, NOT AN INSTRUCTION.**
It is the dollar distance to a perfect 70.00%, driven by VOO's own mark moving under a fixed
share count. **$44 on a $69,852 position is 0.06%. No rebalance is due and none is queued.**

---

## Intents

### BUY — none

**ZERO BUY INTENTS. This is the output §4 says most research runs should produce, and it is
not a failed run.**

New positions were **permitted** this morning on every gate — breaker inactive,
`new_positions_this_week` **0 of 3**, satellite sleeve **entirely undeployed** ($30,000 and
29.3% of §6 headroom unused), `control.md` notes empty. ⚠ **So the absence of a buy is a
RESEARCH result, not a permission result. Nothing was blocked; nothing qualified.**

**Five theses written, all five rejected** — `T-2026-10-19-01` through `-05`. Where they died:

| ID | Object | Killed by |
|---|---|---|
| `-01` | Russia sanctions suspension → airline/refiner fuel cost | **part 1** (one party, no Company B) · rule (viii) · rule (vi) |
| `-02` | Friday bank cohort TRV·TFC·MTB·RF·CFG | **part 1** — no cross-company disclosure in five releases |
| `-03` | Data-centre delays / CoreWeave distress → suppliers | **rule (v)** (no named project or supplier) · rule (viii) (analyst estimate) |
| `-04` | 44.01 / Frontier $11.7M carbon offtake | **§3 both legs** · part 2 by 3 orders of magnitude · rule (vi) |
| `-05` | Sweep of nine (§3, rule iii/iv/v/viii, part 1) | disposed as one, zero drill queries |

⚠⚠ **THE ONE THING THE OPEN RUN SHOULD CARRY FROM THE RESEARCH: THE BINDING CONSTRAINT MOVED
FROM PART 1 TO §3 FOR THE FIRST TIME.** Five sessions running, theses died because **no
Company B existed.** Today the funnel produced **three genuine two-party transactions with
disclosed figures — the most ever — and all three were killed by §3 before part 1 was
reached** (44.01/Frontier, NOVONIX/PowerCo, Orion/Glencore). ⚠ **Company B now EXISTS and is
NOT US-LISTED. One session is not a finding; it is recorded for the next three reviews to
test and it changes nothing today.**

⚠ **NO `revalidate` LINES EXIST BECAUSE THERE IS NOTHING TO REVALIDATE.** The template asks
for the specific number the open run should re-check against an overnight gap. **With zero BUY
intents there is no candidate, no priced-in figure, and no number.** ⚠ **A `revalidate` line
invented for an empty plan would be the open seat's most dangerous possible inheritance.**

### SELL — none

**§5 has no operand** — zero satellite positions, so rules 5.1–5.4 are **ABSENT, not passing**.
Core VOO is **exempt** by §5 and was struck from the working list before the rules were read.

### REBALANCE — none

Core **69.96%**, in band. See **Sleeve check** above. `rebalance_needed: false`.

---

## Carried from the research — for the open seat

- ⚠ **DO NOT re-litigate any of `T-2026-10-19-01`…`-05`.** All five are disposed with named
  reasons in `research_log.md`.
- ⚠ **THE 10-16 DEFERRAL IS DISCHARGED.** `T-2026-10-16-04` deferred the five bank prints
  because they reported after that run. **They reported, they were screened, they died at
  part 1** (`T-2026-10-19-02`). **Do not carry them forward again as a pending lead.**
- ⚠ **`T-2026-10-19-02` IS A REJECTION ON ABSENCE OF EVIDENCE, AND IT SAYS SO.** The source
  stated the primary releases were not in its result set. The decision is unchanged — §4
  requires a disclosed mechanism before a buy — but **the next seat must not quote it as
  "the banks disclosed nothing."**
- ⚠ **LS ELECTRIC WILL BE BACK — rule (iv).** Third appearance (10-13 Bloom $138.5M, 10-15
  re-serve, 10-19 a new $125M US data-centre deal). **Korea-listed with an unnamed US
  counterparty every time. The answer is already written.**
- ⚠⚠ **DO NOT TREAT FRIDAY'S WEEKLY-REVIEW AI-UNWIND FINDING AS A REASON TO TRADE.** The
  funnel served that unwind back this morning as a buyable idea (`T-2026-10-19-03`). It is a
  **tape observation filed as the promotion rule's RESULT**, the press narrative names no
  party, and §3 forbids expressing the short side at all. **A finding is not a thesis.**
- ⚠ **ZERO `move` CALLS AND ZERO MARKET CAPS SOURCED, SIXTH CONSECUTIVE SESSION — CORRECT, NOT
  OMITTED.** Nothing reached the priced-in filter; every kill was upstream of price.
