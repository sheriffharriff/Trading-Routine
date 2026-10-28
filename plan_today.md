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
plan_date: 2026-10-28
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-28 at 09:30 ET** (`alpaca.py clock` at 08:04:26 ET: `is_open:
false`, `next_open: 2026-10-28T09:30:00-04:00`, `next_close: 2026-10-28T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

**The plan this run replaced was dated 2026-10-27 — ONE trading day and ONE calendar day
old, the ordinary midweek shape, not the Monday three-calendar-day shape the carry-forward
warns about.** It was fresh, consumed at 09:39 yesterday, and carried **zero intents**.
⚠ **Irrelevant to execution either way: the 09:35 seat reads the date, not the age.**

---

## ⚠ ONE THING TODAY IS NOT ORDINARY: THE FOMC DECISION LANDS AT 14:00 ET

This is **context for the open seat, not an intent and not a reason to act.** Consensus is
an unchanged hold. **It is NOT a §4 catalyst** — `T-2026-10-27-04` disposed it yesterday in
**both** the pending and the decided state, and no new thesis ID has been minted for it
today. It is recorded here for one operational reason only: **the 12:4x midday seat will be
sitting in front of a tape that may move sharply after 14:00, and a mark that moves is not a
thesis.** Core VOO is **§5-exempt** and is not to be touched on it. There is nothing in the
satellite sleeve for it to move.

---

## Tape context

**Pre-market readings, and every one of them is a LIVE MIDPOINT, not an official close — do
not stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 08:04: equity **$100,166.39** · core VOO **$70,166.39 / 70.05%** · satellite
  **$0 / 0.0%**, count **0** · cash **$30,000.00 / 29.95%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: −49.91`.
- `positions`: **ONE row, core VOO only** — 99.046311231 sh, `avg_entry_price` **706.74**,
  `cost_basis` **$69,999.989999**, `current_price` **708.42** (live pre-market midpoint),
  `unrealized_pl` **+$166.40 / +0.238%**.
- ⚠ **`rebalance_delta: −49.91` IS A DISTANCE READOUT, NOT AN INSTRUCTION.** §2's band on
  today's equity is **$65,108.15–$75,124.79**; core sits **$49.91 ABOVE** the 70% target,
  **$5,058.23 above the floor** and **$4,958.40 below the ceiling** = **4.95% of equity from
  the nearer edge, not 0.05%.** All of the movement is the mark moving under a **FIXED SHARE
  COUNT** — no shares have changed since 2026-09-03. ⚠ **The sign has been negative since
  yesterday's midday seat; that is the mark sitting above target, nothing more.**
- ⚠ **27TH SEAT ON THE BROKER-PAIR ITEM, re-stated not re-raised as new:** `positions`
  reports `lastday_price` **707.52** against yesterday's official `--adjustment all` close
  **707.46** (re-pulled at this seat, not inherited) — **+0.06 above, a THIRD distinct sign
  pattern in three sessions.** Monday both ends deflated, Tuesday both inflated, today the
  bottom end alone sits high. **Both ends of Alpaca's own P&L fields are live midpoints, so
  this is a moving midpoint and not a fixed offset. Use the official close basis for any P&L
  line that gets written down.**

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

Core **70.05%**, inside §2's **65–75%** band with **4.95% of equity** of room to the nearer
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
| 5% single-position cap (§6) | **$5,008.32** | **No operand** |

⚠⚠ **TODAY IS THE *EMPTY-PLAN* KIND OF ZERO, NOT THE *BLOCKED* KIND, AND THE TWO PRODUCE AN
IDENTICAL ORDER COUNT.** Research found nothing that could be written honestly. **A buy was
permitted at every gate and was not available** — §4's honest-broker paragraph says that is
the correct output of most research runs, and it is the output here for the 38th post-fill
session.

---

## BUY intents

**NONE.**

Six theses written this morning (`T-2026-10-28-01` … `-06`), **six rejected, zero accepted.**
Nothing reached the four-part test with all four parts writable, so nothing reached a
priced-in check, and **there is no number for the open seat to re-validate.** Full disposals
are in `research_log.md` and are **not to be re-litigated at 09:35.**

The one-line reasons, so the open seat does not have to go and read them:

| ID | Candidate | Died at |
|---|---|---|
| `-01` | **VRT** (Vertiv Q3, FY guide +$650M) | **Part 1** — mechanism needs an "and also"; the figure that moved is Company A's own revenue, which has no supplier chain. Then part 2: drill confirmed **no named counterparty with a dollar figure**. ⚠ **The day's most attractive item and the one I wanted to work.** |
| `-02` | **GEV** / Trench Group $9.0B | **Merger arb is outside §4** · rule (viii) money paid **out** by the buyable leg · §3 — **target not established as publicly traded.** GEV's **4th** appearance, first as an acquisition, same death. |
| `-03` | **AMAT / LRCX / KLA** (SK hynix record quarter) | **Parts 1, 2 and 3 independently.** "Demand exceeds supply **through 2030**" = ~16 quarters vs §4's two. Same chain and same three names as `T-2026-10-15-01`. |
| `-04` | **ENPH** (weak resi solar, guide down) | **Part 1 on the SIGN** — wrong direction for a long-only book; the only improving story is a reader-supplied share shift. |
| `-05` | **ELVA** / Janus, $26M orders | **§3, at the first number pulled** — market cap **C$366M ≈ US$0.26B** vs a **$10B** floor. ⚠ **The funnel's best-formed transaction of the day, and ineligible.** |
| `-06` | sweep: QBTS/LG CNS · Samsung Bio/AZN · consumer confidence · durable goods · FOMC | **§3 ×2 · rule (viii) wrong-party · two one-party macro objects · one standing refusal honoured with no new ID.** |

---

## SELL intents

**NONE — and this is the NO-OPERAND kind of none, not the nothing-breached kind.**

**Zero open satellite positions**, so §5.1–§5.4 had **no operand at any step**: no
`invalidation` string to test news against, no `timing_window` deadline to compare a date
to, no `entry_price` to measure −7% from, and **no `highest_close` has ever been written in
this repo** to measure −10% from. ⚠ **ZERO §5.1 news queries were run and ZERO were due.**

⚠ **The §5 machinery — 5.1 through 5.4, `alpaca.py sell`, the breaker increment, the breaker
trip and the circuit-breaker alert path — remains UNTESTED CODE after 41 completed sessions
and 38 post-fill.** That is the standing risk in this system and it does not shrink by being
re-stated; **the first live satellite fill will exercise all of it at once.**

---

## REBALANCE intents

**NONE.** Core **70.05%**, in band, `rebalance_needed: false`. See §2 above.

---

## What the open seat should actually do at 09:35

1. Read `plan_date` — it says **2026-10-28**, today. The plan is fresh.
2. Re-reconcile the ledger three-sided (`positions` / this file's satellite header count /
   `sleeves`). ⚠ **Re-derive it; do not inherit this seat's reading.**
3. **Nothing to execute.** Zero BUY, zero SELL, zero REBALANCE. **There is no revalidation
   step today, because there is no intent carrying a number.**
4. Re-check the §2 band against **live equity at the open**, not against the $100,166.39
   above — an open-bar move changes the band and the core value together.
5. Run the §7 limbo check (`orders --status all`) and confirm it still returns **exactly one
   order in the account's entire history** (`d177d8f0`, 2026-09-03, filled, already in
   `trade_log.md`).
6. ⚠ **Do not mint a thesis ID for the 14:00 FOMC decision.** `-04` yesterday disposes it
   decided as well as pending.
