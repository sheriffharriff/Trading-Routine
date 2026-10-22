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
plan_date: 2026-10-22
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-22 at 09:30 ET** (`alpaca.py clock` at 08:07:02 ET: `is_open:
false`, `next_open: 2026-10-22T09:30:00-04:00`, `next_close: 2026-10-22T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean.**

The plan this run replaced was dated **2026-10-21** — one calendar day and one trading day
old. Correct and current; nothing to note.

---

## Tape context

**Pre-flight selftest: 5/5** (env · Alpaca ACTIVE `trading_blocked=False` · Perplexity
`sonar-pro` · ClickUp · `control.md` LIVE). `TRADING_ENABLED: true`, **LIVE paper**,
`control.md` **Notes empty**. **Zero open alerts** (`alerts.md` Open incidents: *(none)*).

**Numbers, each with its call and its basis — never differenced across calls.**

| Reading | Value | Call / basis |
|---|---|---|
| Account equity | **$99,723.50** | `sleeves` 08:07, live broker mark |
| Cash | **$30,000.00** exactly | `sleeves` — ~**45th** consecutive unchanged reading |
| Core VOO | **$69,723.502222** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:07 |
| Core % | **69.92%** | `sleeves`, live-mark basis — **IN BAND** |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **30.08%** | `sleeves` |
| Unrealized P&L on core | **−$276.487777 / −0.395%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **703.9485** | `positions` `current_price`, 08:07 — a **pre-market indicative mark, NOT a close** |
| VOO official 10-21 close | **710.70** | carried from the 10-21 close seat (`bars --adjustment all` on a session the clock proved complete) |
| VOO `lastday_price` | **710.72** | ⚠ **NOT the official close. See below.** |
| §6 5% cap | **$4,986.18** | 99,723.50 × 5%, **with no operand today** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (−0.00953), OR
`unrealized_intraday_pl` (−$670.692096) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **710.72** against the official 10-21 close of **710.70**.
⚠ **EIGHTEENTH CONSECUTIVE SEAT ON THIS STANDING ITEM; the gap is +$0.02, the smallest
recorded. It is a MOVING LIVE MIDPOINT, NOT AN OFFSET — frozen within a session, moving
across them — so the small reading is a coincidence of a moving mark, not a convergence.
STANDING ITEM, NOT RE-DERIVED AND NOT RE-RAISED AS NEW.**

⚠ **The pre-market mark 703.9485 is **−6.75 (−0.95%)** against the official 10-21 close of
710.70. That is an indicative pre-bell quote on thin volume and **is not a close**; it is
recorded as context and used for nothing. The 09:35 seat must re-pull its own numbers.**

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

`sleeves` 08:07: core **69.92%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: 82.95`, `core_target_value: $69,806.45`.

⚠ **`rebalance_delta` is a DISTANCE READOUT, NOT AN INSTRUCTION — standing item, not
re-derived.** $82.95 on $69,723 is **0.12%**, all of it the mark moving under a **fixed
share count**. §2's band is **65–75%** and 69.92% is near the middle of it.
**NO REBALANCE INTENT.** ⚠ **Re-compute at 09:35; do not inherit this figure.**

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | State | Source |
|---|---|---|
| Circuit breaker (§6/§7) | **INACTIVE** | `state.md` `circuit_breaker: INACTIVE`, `halt_triggered_at: none` |
| New positions this week (§6, max 3) | **0 of 3** | `state.md` `new_positions_this_week: 0`, `week_of: 2026-10-19` |
| Satellite sleeve (§2) | **ENTIRELY UNDEPLOYED** — $0.00 / 0.0% / count 0, **$30,000.00 idle** | `sleeves` |
| `control.md` Notes | **EMPTY** — no restriction | `control.md` |
| 5% position cap (§6) | **$4,986.18** | computed, **no operand** |

⚠⚠ **A BUY WAS PERMITTED ALL RUN AND NOTHING IS BOUGHT. THAT IS A RESEARCH RESULT, NOT A
PERMISSION RESULT** — and today it is the strongest instance on record, because the funnel
finally produced a fully-documented candidate and §4 killed it on three independent parts.
**See `T-2026-10-22-01`.**

---

## Week rollover (§6)

Today is **Thursday 2026-10-22**; ISO week **2026-W43**; Monday of this ISO week is
**2026-10-19**. `state.md` `week_of` reads **2026-10-19** — **MATCH, no rollover, counter
stays at 0 of 3.** ⚠ **Computed from the date, not inherited from the field it was checked
against.**

---

## Intents

### BUY — **NONE**

⚠⚠⚠ **ZERO BUY INTENTS, AND THIS IS THE RUN WHERE THAT SENTENCE COSTS SOMETHING, SO IT IS
WORTH BEING EXPLICIT ABOUT WHY.** The research produced **the best-documented candidate in
this log's history** — **Amkor Technology (AMKR)**, carrying a **primary-source company
release**, a **named counterparty (NVIDIA)**, a **dated announcement (2026-10-21)**, a
**$1.3 billion figure attributed to the buyable leg BY the buyable leg**, a **one-clause
mechanism**, `us_equity`/NASDAQ/`tradable`, and a `move` verdict that printed **"passes"**.

**It was rejected on three independent grounds, each sufficient** (full statement at
`T-2026-10-22-01`):

1. **Part 1 — AMKR *is* the headline name.** §4's opening sentence is *"you look for
   Company B… You are not chasing the headline name."* The headline is "NVIDIA and Amkor
   announce agreement." **This is the GFS kill repeating verbatim.**
2. **Part 2 — the $1.3B is `prepayments`, in Amkor's own word.** Capital paid **IN** by the
   customer, a deferred-revenue liability until the work is performed — **rule (viii), the
   JBL worked example.** The release **expressly declines to call it revenue or give a
   recognition schedule**, and names **no segment and no revenue share**, so §4's
   10%-of-revenue test is **not computable**.
3. **Part 3 — the only date in the document is "by the END OF 2028"** (~9 quarters against
   §4's two), **and no revenue-contribution date is stated at all.** Part 3 is not merely
   too long; it is **unwriteable from the disclosure.**

⚠⚠ **AND THE PRICED-IN FILTER FAILS IT ON THE BASIS §4's WORDS DESCRIBE, WHICH THE SCRIPT
DOES NOT MEASURE.** Five-session: **−2.37%, `priced_in: false`, "passes."** News-day:
**+4.87%** (10-20 **41.69** → 10-21 **43.72**, volume **183,526** vs ~115–125k preceding).
**§4 says "more than 4% … ON THIS NEWS" → the candidate is LATE.** ⚠ **The five-session
pass is manufactured by arithmetic cancellation — a **−6.9%** sector drawdown against the
**+4.87%** news pop, two legs with DIFFERENT CAUSES netting to a clean-looking figure.
Index control over the identical window: `VOO` **+0.46%**, `priced_in: false`.** ⚠ **This is
the RECORDED `AKAM` netting sub-shape of shape three — **NOT** a new shape seven. The
`grep` the carry-forward demands was run first and it changed the answer.**

⚠ **The pull to buy it was real: the sleeve has been undeployed since inception, $30,000 has
earned nothing for 39 sessions, and every §6 gate is open. That is exactly the configuration
§4's honest-broker rule describes, and the answer is still no.** ⚠ **DO NOT REHABILITATE IT
AT A DIFFERENT PRICE AT 09:35 — it did not die on price, and neither the end-2028 date, the
word "prepayments", nor Amkor's position in the headline moves with the quote.**

**No `revalidate` line is owed, because there is no intent to revalidate.** ⚠ **If a later
seat finds itself constructing one for AMKR, that is the softening §7 forbids — the three
kills above are the record, and they are not price-dependent.**

### SELL — **NONE**

**No operand.** `positions` returns **ONE** row — core **VOO**, 99.046311231 sh @ **706.74**,
`cost_basis` **$69,999.989999**, unchanged since 2026-09-03 — and §5 **exempts core**
(*"Core positions are exempt from all four"*). **Zero satellite positions**, so §5.1–5.4 have
nothing to evaluate. See the §5 table below.

### REBALANCE — **NONE**

Core **69.92%** is inside §2's **65–75%** band. `core_in_band: true`,
`rebalance_needed: false`.

---

## §5 sell-rule evaluation — ALL FOUR RULES **ABSENT, NOT PASSING**

⚠ **The distinction is load-bearing: a rule with no operand and a rule that was checked and
passed are different states, and they are indistinguishable in a table that just says "ok".**

| Rule | State | Why |
|---|---|---|
| **5.1** thesis invalidation | **ABSENT — no operand** | No `invalidation` field on any satellite row. **ZERO Perplexity news queries run and ZERO DUE** — there is no position to check news against. |
| **5.2** time stop | **ABSENT — no operand** | No `timing_window` and no deadline on any satellite row. |
| **5.3** hard stop (−7% from entry) | **ABSENT — NOT COMPUTABLE** | No satellite `entry_price`. ⚠ **Distance to the rule is NOT COMPUTABLE, which differs from "far away".** The 706.74 core fill is **§5-exempt**, not an operand. |
| **5.4** trailing stop (−10% from `highest_close`) | **ABSENT — no operand** | No satellite `highest_close` anywhere. ⚠ **Core VOO is NEVER stamped — 96th consecutive refusal: stamping the one position §5 EXEMPTS would ARM a §5.4 stop against it.** |

**Ledger reconciliation — done FIRST, three sides, all agreeing.** `positions.md`
satellite block-header pattern `grep -cE` = **0** · Alpaca `positions` = **one row, core VOO
only** · `sleeves` `satellite.count: 0`. **NO DISCREPANCY.** ⚠ **GREP TRAP, documented and
not re-raised: the single `entry_price` hit in `positions.md` is line 45, inside
`## Template`.**

---

## For the 09:35 seat

1. **Re-pull your own numbers.** Equity, sleeves and `rebalance_delta` all move with the
   mark; nothing in the table above is inheritable.
2. **Re-check the week anchor from the date**, not from `state.md`'s field.
3. **There is nothing to execute.** No BUY, no SELL, no REBALANCE. A zero-order run today is
   the correct outcome, not a failure to act. ⚠ **An empty plan that is FRESH and a plan that
   is STALE produce identical zero-order runs — the `plan_date` above reads **2026-10-22**,
   so confirm the match and post **no** `stale-plan` alert. Posting one on a fresh plan is
   the mirror failure of missing a stale one.**
4. ⚠⚠ **DO NOT RE-LITIGATE `T-2026-10-22-01`…`-04`.** A midday or post-bell entry routes
   around the path that forces every buy to sleep on a written thesis. If AMKR looks
   attractive at 09:35, the reason it was rejected is written above and none of it is about
   the price.
5. ⚠ **Known defect inherited, not fixed (open human item (12)):** Routine 2's Step 6 sources
   `voo_close_at_entry` from `bars --days 1`, which at 09:36 returns a **PARTIAL** bar dated
   today. **It has cost nothing because no position has ever been opened, and it is still
   wrong on the first fill.** Not the agent's to fix.
