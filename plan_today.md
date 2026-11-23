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
plan_date: 2026-11-23
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens **2026-11-23 at 09:30 ET** (`clock` 07:01:19 ET: `is_open: false`, `next_open`
`2026-11-23T09:30:00-05:00`, `next_close` `2026-11-23T16:00:00-05:00`). **NOT a holiday** —
closed because it is pre-market, and **both** fields carry **today's** date, the full-session
signature. ⚠ **Read off the DATES, not the boolean: FALSE has three meanings, TRUE has one.**
Monday, an ordinary full session.

The plan this seat replaced was dated **2026-11-20** — the previous trading day, the ordinary
shape. It carried **zero intents**. **Nothing was lost: a plan with no intents has no
execution to perform.**

**WEEK ROLLOVER — NO RESET DUE, RE-DERIVED AT THIS SEAT, NOT INHERITED.** `week_anchor(2026-11-23)`
→ **2026-11-23**; inherited `week_of` **2026-11-23**. They match, so `new_positions_this_week`
stays at **0**. ⚠ The reset is done here rather than trusted to the Friday review, so a failed
Friday run cannot leave the §6 weekly cap stuck at its limit. ⚠ The 11-20 review warned that a
weekend run would see the anchor return **2026-11-16** and reset `week_of` backwards; **no run
fired over the weekend, so it did not happen**, and from today anchor and value agree.

**Selftest 5/5, exit 0.** `trading_enabled: true`, LIVE against the paper account.

---

## Gate state — every §6 / §7 gate open, and no intent written anyway

| Gate | Reading | Blocks a buy? |
|---|---|---|
| §6 circuit breaker | **INACTIVE**, `consecutive_closed_losses` **0 of 3**, `halt_triggered_at: none` | No |
| §6 weekly cap | **0 of 3** new positions this week | No |
| §2 satellite sleeve | **0.00% deployed**, **$30,000.00** cash available | No |
| `control.md` `TRADING_ENABLED` | **true** | No |
| `control.md` Notes | **(none)** | No |
| `alerts.md` open incidents | **(none)** — nothing SYSTEMIC to flag | No |

⚠⚠ **THIS IS THE UNHALTED ZERO, AND THE DISTINCTION IS THE WHOLE POINT.** Nothing structural
prevented a position today. **Six candidates were researched and six were rejected on §3 and §4's
own tests.** A plan that is empty because the breaker is active and a plan that is empty because
nothing qualified are different facts about the system, and only one of them is a successful run.
**This is the second kind.**

---

## Account snapshot (pre-market mark — said once, not repeated per section)

- Equity **$94,598.00** · core **VOO** 99.046311231 sh @ 706.74 · market value **$64,598.00** ·
  unrealized **−$5,401.99 / −7.717%** · cash **$30,000.00**.
- Sleeves: **core 68.29% · satellite 0.00% · cash 31.71%** · `core_in_band: true` ·
  `rebalance_needed: false` · `rebalance_delta: 1620.60`.
- ⚠ **These are read off `current_price` 652.20 at 07:01 — a PRE-MARKET PRINT, not a close**
  (+2.70% on Friday's official `bars` close of **635.01**). They will move before the bell.
  **The §2 band verdict is robust to that:** core reads **68.29%** pre-market and **67.71%** on
  Friday's close, both well inside 65–75%. The 65% floor breaks at VOO **562.51** — solved, not
  assumed (19500 = 0.35 × 99.046311231 × P), a further **−13.7%** from the pre-market mark.
- ⚠ **Endpoint disagreement, 14th distinct instance:** `positions.lastday_price` **635.54** vs
  official `bars` **635.01** for 2026-11-20 = **0.53 / 0.0835%**. Build P&L and stamp
  `highest_close` from official `bars` closes only.

---

## BUY intents

**NONE.** Six theses were written and all six were rejected — `T-2026-11-23-01` through `-06` in
`research_log.md`. In §4's own ordering, **every one died on part 1 or part 3, both of which
precede the hard filters**, so no candidate reached the priced-in check and **no `move` call was
spent.** Recorded so the absent `move` readings are not mistaken for a skipped check.

| Thesis | Object | The test that killed it |
|---|---|---|
| `T-2026-11-23-01` | CrowdStrike / Zscaler, ~$43.9B all-stock, announced today | **Part 3** — closes 2H CRWD FY2028, ~7+ quarters. Part 1 independently: no source names any affected third party. |
| `T-2026-11-23-02` | BIS remote-access AI-chip rule; NVDA H200 halt; TSMC ≤16nm suspension | **Part 1** — no named beneficiary; the only measurable direction is **negative**, inexpressible long-only. Third appearance in five sessions. |
| `T-2026-11-23-03` | Sila / Panasonic silicon-anode offtake, ">$1B over time" | **§3** — Sila private, Panasonic Japan-listed. **No US-listed party exists in the transaction.** |
| `T-2026-11-23-04` | Venture Global / China Gas, +1.0 MTPA LNG, 20 yr | **Part 3** — deliveries begin **2030**, ~16 quarters. First-order leg. **Fifth appearance, fifth rejection.** |
| `T-2026-11-23-05` | Macro complex — UMich 51.5, Nasdaq −5%, PCE/GDP/PMI ahead | **No Company A.** A market is not a transaction. |
| `T-2026-11-23-06` | Sweep of nine: Intuit/Mailchimp, Textron Industrial, MasTec/Murphy, Capricor, Vanda, Beren, Apple re-serve, Moog, NVDA re-serve | §3, part 1 or wrong-direction on each. Two are **re-serves of already-disposed objects**. |

**Nothing is to be bought today.** If the open run finds this plan dated **2026-11-23**, there is
still no BUY to validate — the correct behaviour is to proceed to the §5 and §2 sections and place
no order.

---

## SELL intents

**NONE — AND THERE IS NO OPERAND, WHICH IS NOT THE SAME AS "ALL RULES PASS."**

The satellite sleeve holds **zero positions** and always has. `positions.md` "Open positions" is
`*(none)*`; `alpaca.py positions` returns **one row, VOO**, the designated §2 core, which §5
exempts. §5.1 invalidation, §5.2 time stop, §5.3 hard stop and §5.4 trailing stop are therefore
**ABSENT, NOT PASSING**: no entry price, no `highest_close`, no deadline and no invalidation string
exists anywhere to evaluate.

⚠⚠ **Core VOO's −7.717% is NOT a §5.3 reading and its drawdown is NOT a §5.4 reading.** Core is
exempt from all four rules and is not sold on news (§2, §5). That is a rule, not a judgment call,
and it is restated here because the magnitude now sits past both thresholds and a fresh-clone seat
reading only the P&L line could mistake it for a trigger. **The §5 machinery remains unproven code
— 81 days old and never once executed against a real position.**

---

## REBALANCE intent

**NONE.** `sleeves` reports `core_in_band: true`, `rebalance_needed: false`, core **68.29%** against
the §2 65–75% band. `rebalance_delta` is **$1,620.60** to the 70% target — inside the band, so §2
requires no action and none is authorized. ⚠ Re-check after the open: the figures above are a
pre-market mark, and the band test belongs to the open run on live numbers.

---

## For the open run, in order

1. **Confirm `plan_date` reads 2026-11-23.** If it does not, this plan is stale — log it, alert,
   and go straight to the §2 section.
2. **Re-read `clock`.** Place nothing while `is_open` is false. ⚠⚠ **The standing schedule defect:
   nine of ten recorded routine-2 seats fired ~50 minutes BEFORE the bell. The ask is already with
   the human — do not re-send it.** There is nothing to execute today either way, so the defect
   costs nothing again this session.
3. **Re-derive the week anchor** rather than trusting `week_of`.
4. **Nothing to execute.** Zero BUY intents, zero SELL intents, zero REBALANCE. Log the null and
   commit.
