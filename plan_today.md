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
plan_date: 2026-10-29
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-29 at 09:30 ET** (`alpaca.py clock` at 08:14:15 ET: `is_open:
false`, `next_open: 2026-10-29T09:30:00-04:00`, `next_close: 2026-10-29T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

The plan this run replaced was dated **2026-10-28** — one trading day and one calendar day
old, the ordinary midweek shape. It was fresh when consumed and carried **zero intents**.

---

## Tape context

**Pre-market readings, and every one of them is a LIVE MIDPOINT, not an official close — do
not stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 08:14: equity **$99,992.07** · core VOO **$69,992.07 / 70.0%** · satellite
  **$0 / 0.0%**, count **0** · cash **$30,000.00 / 30.0%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: +2.38`.
- `positions`: **ONE row, core VOO only** — 99.046311231 sh, `avg_entry_price` **706.74**,
  `cost_basis` **$69,999.989999**, `current_price` **706.66** (live pre-market midpoint),
  `unrealized_pl` **−$7.92 / −0.011%**.
- ⚠ **`rebalance_delta: +2.38` IS A DISTANCE READOUT, NOT AN INSTRUCTION.** §2's band on
  this equity is **$64,994.85–$74,994.05**; core sits **$2.38 BELOW** the 70% target,
  **$4,997.22 above the floor** and **$5,001.98 below the ceiling** = **5.00% of equity from
  the nearer edge, not 0.002%.** All of the movement is the mark moving under a **FIXED SHARE
  COUNT** — no shares have changed since 2026-09-03. ⚠ **The sign flipped positive overnight;
  that is the mark crossing back below target, nothing more.**
- ⚠ **29TH SEAT ON THE BROKER-PAIR ITEM, re-stated not re-raised as new:** `positions`
  reports `lastday_price` **709.90** against yesterday's official `--adjustment all` close
  **710.00** recorded by the close seat — **−0.10 below.** Both ends of Alpaca's own P&L
  fields are live midpoints, so this is a moving midpoint and not a fixed offset.
  **Use the official close basis for any P&L line that gets written down.**
- **Pre-market `current_price` 706.66 is −0.46% against yesterday's official 710.00.** The
  open seat must re-read the band against **live equity at the open**, not against the figure
  above — an open-bar gap moves the band and the core value together.

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

Core **70.0%**, inside §2's **65–75%** band with **5.00% of equity** of room to the nearer
edge. **No REBALANCE intent is queued.** The core sleeve is §5-exempt and was **struck from
the §5 working list rather than stamped against any rule** — not stamping it is the correct
action, not an omission.

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | Reading | Blocks a buy? |
|---|---|---|
| `circuit_breaker` | **INACTIVE**, `halt_triggered_at: none` | No |
| `new_positions_this_week` | **0 of 3** (week anchor 2026-10-26, re-derived, no rollover) | No |
| Satellite deployment | **0.0%**, count 0, **$30,000.00 idle** | No |
| `control.md` Notes | **EMPTY** | No |
| `control.md` `TRADING_ENABLED` | **true** (LIVE paper) | No |
| Open alerts | **ZERO**, nothing SYSTEMIC | No |
| 5% single-position cap (§6) | **$4,999.60** | **No operand** |

⚠⚠ **TODAY IS THE *EMPTY-PLAN* KIND OF ZERO, NOT THE *BLOCKED* KIND, AND THE TWO PRODUCE AN
IDENTICAL ORDER COUNT.** Research found nothing that could be written honestly. A buy was
permitted at every gate and was not available — §4's honest-broker paragraph says that is the
correct output of most research runs, and it is the output here for the **39th post-fill
session**.

---

## BUY intents

**NONE.**

Six theses written this morning (`T-2026-10-29-01` … `-06`), **six rejected, zero accepted.**
Nothing reached the four-part test with all four parts writable, so **there is no number for
the open seat to re-validate.** Full disposals are in `research_log.md` and are **not to be
re-litigated at 09:35.**

The one-line reasons, so the open seat does not have to go and read them:

| ID | Candidate | Died at |
|---|---|---|
| `-01` | **GOOGL** → datacenter / power / optical supplier tier | **Part 1** (mechanism needs three added clauses) and **part 2** (increment is $0). ⚠ **Rule (iii) is the deeper kill: FY2026 capex $195–205B is a REAFFIRMATION — the raise happened in JULY. FY2027 is *"increase significantly"*, which is not a number.** |
| `-02` | **MSFT** → third-party capacity providers | **Part 1 on the SIGN** — an underspend ($45.2B vs its own $50B) is revenue nobody recognised; CY figure revised **down** ~$175B→~$170B. Rule (v): *"delayed third-party capacity deliveries"* names nobody. ⚠ **Sources also disagree on the figures ($118.1B vs ~$170B), which is independently disqualifying.** |
| `-03` | **TSLA** → supplier tier | **Part 1 on the SIGN, cleanest form yet** — 2026 capex **cut to ~$20B from >$25B**. A withdrawal of spending cannot be a long thesis and there is no short leg in this strategy. |
| `-04` | **MU** ← SK Hynix record quarter | **Part 1** — competitor read-across = shared-cause object; **part 2** (no figure attaches); **and priced-in FAIL at +7.59%.** |
| `-05` | **ORCL** | **Part 3** — FY2030 is **~16 quarters** vs §4's two; **part 2** twice (own revenue; the $20B is a FINANCING CEILING). |
| `-06` | sweep of **fifteen** items — FedEx · Ford · Robinhood · EnSilica · Gaon Cable · Taihan · Woodside · Critical One · Kongsberg · SK pharmteco · UMC · Eldorado · AdvanSix · Alume Bio · FOMC + yields | **§3 ×9 · government counterparty ×2 · own-results ×3 · one macro object.** Disposed as one, **zero drill queries spent.** |

### ⚠ The one thing in this plan the open seat should carry forward

**No disclosed capital-spending figure in last night's window moved UP against the company's
own prior figure.** Alphabet's was **unchanged** (raised in July), Microsoft's moved **down**,
Tesla's moved **down**. The tape is moving hard on AI capex this morning and **the direction
of every disclosed number is wrong for a long-only second-order book.** If the 09:35 or 12:4x
seat feels pull toward this complex, the answer is already written and needs no new query.

### ⚠ VRT: no new ID, and the number is why

`T-2026-10-28-01` disposed VRT at part 1 yesterday and the carry-forward forbids re-opening a
disposal on the same event. **Recorded only because the figure is new:** `move --sessions 5`
returns **+14.48%**, so VRT is now **mechanically LATE** as well as structurally dead. **Do
not re-litigate it at 09:35.**

---

## SELL intents

**NONE — and this is the NO-OPERAND kind of none, not the nothing-breached kind.**

**Zero open satellite positions**, so §5.1–§5.4 had **no operand at any step**: no
`invalidation` string to test news against, no `timing_window` deadline to compare a date
to, no `entry_price` to measure −7% from, and **no `highest_close` has ever been written in
this repo** to measure −10% from. ⚠ **ZERO §5.1 news queries were run and ZERO were due.**

⚠ **The §5 machinery — 5.1 through 5.4, `alpaca.py sell`, the breaker increment, the breaker
trip and the circuit-breaker alert path — remains UNTESTED CODE after 45 completed sessions
and 42 post-fill.** That is the standing risk in this system and it does not shrink by being
re-stated; **the first live satellite fill will exercise all of it at once.**

---

## REBALANCE intents

**NONE.** Core **70.0%**, in band, `rebalance_needed: false`. See §2 above.

---

## What the open seat should actually do at 09:35

1. Read `plan_date` — it says **2026-10-29**, today. The plan is fresh.
2. Re-reconcile the ledger three-sided (`positions` / `positions.md` satellite header count /
   `sleeves`). ⚠ **Re-derive it; do not inherit this seat's reading.**
3. **Nothing to execute.** Zero BUY, zero SELL, zero REBALANCE. **There is no revalidation
   step today, because no intent carries a number.**
4. Re-check the §2 band against **live equity at the open**. Pre-market VOO is **−0.46%**
   against yesterday's official close, so expect a gap-down open bar; the band and the core
   value move together and core had **5.00%** of room at 08:14.
5. Run the §7 limbo check (`orders --status all`) and confirm it still returns **exactly one
   order in the account's entire history** (`d177d8f0`, 2026-09-03, filled, already in
   `trade_log.md`).
6. ⚠ **Do not mint a thesis ID for the FOMC hold, for the AI-capex complex, or for VRT.** All
   three are disposed above with the reasons written out.
