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
plan_date: 2026-10-23
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-23 at 09:30 ET** (`alpaca.py clock` at 08:03:12 ET: `is_open:
false`, `next_open: 2026-10-23T09:30:00-04:00`, `next_close: 2026-10-23T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean.**

The plan this run replaced was dated **2026-10-22** — one calendar day and one trading day
old. Correct and current; nothing to note. ⚠ **Compared to the last TRADING day, not to the
calendar — the Monday shape (a correct plan arriving three calendar days old) does not
apply today, but the comparison is made the same way every run.**

**Today is Friday — the weekly review (routine 5) runs after the close.** Four items are
already open for it and are listed at the foot of this file.

---

## Tape context

**Pre-flight selftest: 5/5** (env · Alpaca ACTIVE `trading_blocked=False` · Perplexity
`sonar-pro` · ClickUp · `control.md` LIVE). `TRADING_ENABLED: true`, **LIVE paper**,
`control.md` **Notes empty**. **Zero open alerts** (`alerts.md` Open incidents: *(none)*).

**Numbers, each with its call and its basis — never differenced across calls.**

| Reading | Value | Call / basis |
|---|---|---|
| Account equity | **$99,376.99** | `sleeves` 08:03, live broker mark |
| Cash | **$30,000.00** exactly | `account` + `sleeves`, `accrued_fees: 0` — ~**49th** consecutive unchanged reading |
| Core VOO | **$69,376.988702** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:03 |
| Core % | **69.81%** | `sleeves`, live-mark basis — **IN BAND** |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **30.19%** | `sleeves` |
| Unrealized P&L on core | **−$623.001297 / −0.89%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **700.45** | `positions` `current_price`, 08:03 — a **pre-market indicative mark, NOT a close** |
| VOO official 10-22 close | **702.02** | `bars --days 7 --adjustment all`, re-pulled at this seat — **not inherited** |
| VOO `lastday_price` | **702.30** | ⚠ **NOT the official close. See below.** |
| §6 5% cap | **$4,968.85** | 99,376.99 × 5%, **with no operand today** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (−0.00263), OR
`unrealized_intraday_pl` (−$183.235676) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **702.30** against the official 10-22 close of **702.02**.
⚠ **NINETEENTH CONSECUTIVE SEAT ON THIS STANDING ITEM; the gap is +$0.28. It is a MOVING
LIVE MIDPOINT, NOT AN OFFSET — frozen within a session, moving across them — so neither a
small nor a large reading means anything. STANDING ITEM, NOT RE-DERIVED AND NOT RE-RAISED AS
NEW.** ⚠ **Note also that `equity` itself moved across three calls in three minutes —
$99,378.54 (selftest 08:02) · $99,376.99 (`sleeves` 08:03) · $99,339.35 (`account` 08:05).
Each figure above is tagged with its call for that reason.**

⚠ **The pre-market mark 700.45 is **−1.57 (−0.2236%)** against the official 10-22 close of
702.02. That is an indicative pre-bell quote on thin volume and **is not a close**; it is
recorded as context and used for nothing. The 09:35 seat must re-pull its own numbers.**

**Yesterday's tape, carried as context and used for nothing:** VOO closed **702.02** vs
**710.70**, **−1.2213%**, on volume **62,938** against a recent **24–32k** range (**2.5×**)
and `n` **2,597**. ⚠ **A genuine high-participation down day. §2 holds core permanently and
does not trade it on news, so there is no action behind that sentence.**

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

`sleeves` 08:03: core **69.81%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: 186.90`, `core_target_value: $69,563.89`.

⚠ **`rebalance_delta` is a DISTANCE READOUT, NOT AN INSTRUCTION — standing item, not
re-derived.** $186.90 on $69,377 is **0.27%**, all of it the mark moving under a **fixed
share count — no shares have moved since 2026-09-03.** §2's band is **65–75%** and 69.81%
sits comfortably inside it. ⚠ **Core has WALKED DOWN the band 70.12% → 69.86% → 69.81%
across three seats purely because a falling mark acts on a fixed share count. A drifting
percentage with no transaction behind it is not drift that §2 asks anyone to correct.**
**NO REBALANCE INTENT.** ⚠ **Re-compute at 09:35; do not inherit this figure.**

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | State | Source |
|---|---|---|
| Circuit breaker (§6/§7) | **INACTIVE** | `state.md` `circuit_breaker: INACTIVE`, `halt_triggered_at: none`, `consecutive_closed_losses: 0` |
| New positions this week (§6, max 3) | **0 of 3** | `state.md` `new_positions_this_week: 0`, `week_of: 2026-10-19` |
| Satellite sleeve (§2) | **ENTIRELY UNDEPLOYED** — $0.00 / 0.0% / count 0, **$30,000.00 idle across 34 post-fill sessions** | `sleeves` |
| `control.md` Notes | **EMPTY** — no restriction | `control.md` |
| 5% position cap (§6) | **$4,968.85** | computed, **no operand** |

⚠⚠ **A BUY WAS PERMITTED ALL RUN AND NOTHING IS BOUGHT. THAT IS A RESEARCH RESULT, NOT A
PERMISSION RESULT.**

---

## Week rollover (§6)

Today is **Friday 2026-10-23**; ISO week **2026-W43**; Monday of this ISO week is
**2026-10-19**. `state.md` `week_of` reads **2026-10-19** — **MATCH, no rollover, counter
stays at 0 of 3.** ⚠ **Computed from the date, not inherited from the field it was checked
against.** The rollover lands **Monday 2026-10-26**.

---

## Intents

### BUY — **NONE**

**Four theses written, zero accepted, four rejected** — `T-2026-10-23-01` through `-04`.
**Three broad scans, one drill query, zero quotes pulled on any ticker.**

⚠⚠ **THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE IN ALL THREE SCANS, IN ITS OWN
WORDS** — *"the available results do not establish any qualifying item involving two named
corporate entities…"* · *"No company can be confirmed to meet all of the stated criteria…"*
· *"no qualifying example in which a second publicly traded company was both explicitly
identified as directly affected in its revenue or cost lines and assigned a dollar amount."*
**The structural framing returned eight items and self-excluded all eight in a table, with a
named failure against each.**

**The one item that deserved a drill was Lockheed Martin** (`T-2026-10-23-01`): a real
agreement with the Department of War covering **at least 850 F-35 aircraft over 10 years**
across **Lots 21–30** at **156 aircraft/yr**, announced **2026-10-22**, alongside a **clean
rule (iii) pass** — LMT raised its own FY2026 revenue outlook to **$80–82B from its own
prior $79.75–81.75B**. **It was rejected on three independent grounds, each sufficient:**

1. **Part 1 — there is no Company B, and the source says so when asked.** *"No publicly
   traded supplier company or named supplier reporting segment is identified in the cited
   primary releases … it does not name a supplier company or assign any dollar amount to
   one."* ⚠ **The priors arrived instantly and specifically — RTX/Pratt & Whitney, Northrop
   Grumman, L3Harris, Honeywell, BAE. NO GUESS WAS MADE AND NONE IS RECORDED AS A CANDIDATE.
   Rule (v): the source left the blank, and filling it in is not research.**
2. **Part 3 — the framework is contingent on CONGRESSIONAL AUTHORIZATION AND APPROPRIATIONS,
   pricing and delivery schedules are not finalised, and NO first-delivery or first-revenue
   date exists in the primary materials at all.** ⚠ **Rule (vi)'s pending-definitive-agreement
   shape with the gate moved from a counterparty to a LEGISLATURE. Lots 21–30 is ~40 quarters
   against §4's two.**
3. **Rule (viii), new costume — the only dollar figure in the story is the $7 billion
   Lockheed commits to SELF-FUND**, unallocated, with no named recipient; and the
   **framework's own total value is never disclosed anywhere.** ⚠ **A figure the buyable leg
   promises to spend on itself is the wrong direction AND the wrong party at once.**

⚠⚠ **THE LESSON IS THE 10-15 TSMC SPLIT IN A SHARPER FORM: APPLY RULE (iii) TO THE FIGURE
THE MECHANISM ACTUALLY RUNS ON. On 10-15 the figure that moved had no supplier chain and the
figure with the supplier chain did not move. HERE THE FIGURE WITH THE SUPPLIER CHAIN WAS
NEVER DISCLOSED AT ALL** — so a reader who tests the release, finds the guidance pass, and
stops, proceeds on a number no supplier touches.

**The day's only two-named-public-company item was BioNTech/Gilead** (`T-2026-10-23-03`) —
pumitamig + Trodelvy into **Phase 3 Rosetta Breast-01**, Gilead named as the ADC supplier. ⚠
**It is the shape this funnel has failed to produce for fifteen consecutive sessions, and it
has a mechanism sentence that needs no second clause — and part 3 kills it anyway (a Phase 3
oncology trial reports in years; rule (vi) names clinical collaborations explicitly, SMMT/AZN
precedent), with part 2 failing independently for want of any figure at either leg.**
⚠⚠ **THAT MATTERS FOR THE STANDING ARGUMENT ABOUT THE §4 BAR: the binding constraint on the
day's best-shaped candidate was NOT disclosure practice and NOT the evidence bar. It was the
CALENDAR — a rule no amount of widening would touch.**

**Also rejected:** Lam Research's **$300–400M** of shortage-delayed deliveries
(`T-2026-10-23-02` — unnamed suppliers, and the only reachable Company B is a competitor,
which is the shared-cause object; the honest reading points DOWN and §3 permits only the long
side), and a **twenty-one-item sweep** (`T-2026-10-23-04`) disposed as one for zero drill
queries: six government or municipal counterparties (**RTX's $394M ceiling increase is its
SEVENTH appearance, dead at the same rung**), seven §3 failures (**Zymeworks/Roche is the
cheapest — $55M + $40M + up to $718M disclosed, and ZYME is ~$1.5B against a $10B floor while
Roche is SIX-listed**), two wrong-direction transactions, four own-results prints, three FDA
decisions with no second party, and **Cheniere/QatarEnergy's 4 Mtpa through 2054 — no dollar
figure, a volume rather than money, and ~112 quarters.**

**No `revalidate` line is owed, because there is no intent to revalidate.** ⚠ **None of the
four rejections is price-dependent.** ⚠⚠ **DO NOT REHABILITATE `T-2026-10-23-01` IF CONGRESS
APPROPRIATES: appropriation would fix part 3's GATE and change neither the missing Company B
nor the missing deal value, and a Lots 21–30 schedule cannot land inside two quarters however
it is funded.**

### SELL — **NONE**

**No operand.** `positions` returns **ONE** row — core **VOO**, 99.046311231 sh @ **706.74**,
`cost_basis` **$69,999.989999**, unchanged since 2026-09-03 — and §5 **exempts core**
(*"Core positions are exempt from all four"*). **Zero satellite positions**, so §5.1–5.4 have
nothing to evaluate. See the §5 table below.

### REBALANCE — **NONE**

Core **69.81%** is inside §2's **65–75%** band. `core_in_band: true`,
`rebalance_needed: false`.

---

## §5 sell-rule evaluation — ALL FOUR RULES **ABSENT, NOT PASSING** (23rd consecutive seat)

⚠ **The distinction is load-bearing: a rule with no operand and a rule that was checked and
passed are different states, and they are indistinguishable in a table that just says "ok".**

| Rule | State | Why |
|---|---|---|
| **5.1** thesis invalidation | **ABSENT — no operand** | No `invalidation` field on any satellite row. **ZERO Perplexity news queries run and ZERO DUE** — Step 4.1 has no invalidation string to test. |
| **5.2** time stop | **ABSENT — no operand** | No `timing_window` and no deadline on any satellite row. |
| **5.3** hard stop (−7% from entry) | **ABSENT — NOT COMPUTABLE** | No satellite `entry_price`. ⚠ **Distance to the rule is NOT COMPUTABLE, which differs from "far away".** The 706.74 core fill is **§5-exempt**, not an operand. |
| **5.4** trailing stop (−10% from `highest_close`) | **ABSENT — no operand** | No satellite `highest_close` anywhere. ⚠ **Core VOO is NEVER stamped — 99th consecutive refusal.** VOO's trailing max close is **716.29 (2026-10-06)** and 702.02 is **−1.99%** from it, so a §5.4 stop would be nowhere near triggering — ⚠ **WHICH IS EXACTLY WHAT MAKES STAMPING IT FEEL HARMLESS. It is harmless TODAY. Arming a trailing stop against the one sleeve §5 exempts and §2 holds permanently is not a thing to do on a quiet day.** |

**Ledger reconciliation — done FIRST, before any research, three sides, all agreeing.**
`positions.md` satellite header `grep -cE '^### [A-Z]{1,5} '` = **0** · Alpaca `positions` =
**one row, core VOO only** · `sleeves` `satellite.count: 0`. **NO DISCREPANCY.** ⚠ **GREP
TRAP, documented and not re-raised: the single `entry_price` hit in `positions.md` is line
45, inside `## Template`.**

---

## For the 09:35 seat

1. **Re-pull your own numbers.** Equity, sleeves and `rebalance_delta` all move with the
   mark — and `equity` moved three times in three minutes at this seat. Nothing in the table
   above is inheritable.
2. **Re-check the week anchor from the date**, not from `state.md`'s field.
3. **There is nothing to execute.** No BUY, no SELL, no REBALANCE. A zero-order run today is
   the correct outcome, not a failure to act. ⚠ **An empty plan that is FRESH and a plan that
   is STALE produce identical zero-order runs — the `plan_date` above reads **2026-10-23**,
   so confirm the match and post **no** `stale-plan` alert. Posting one on a fresh plan is
   the mirror failure of missing a stale one.**
4. ⚠⚠ **DO NOT RE-LITIGATE `T-2026-10-23-01`…`-04`.** A midday or post-bell entry routes
   around the path that forces every buy to sleep on a written thesis. The reasons are
   written above and in `research_log.md`, and none of them is about the price.
5. ⚠ **Known defect inherited, not fixed (open human item (12)):** Routine 2's Step 6 sources
   `voo_close_at_entry` from `bars --days 1`, which at 09:36 returns a **PARTIAL** bar dated
   today. **It has cost nothing because no position has ever been opened, and it is still
   wrong on the first fill.** Not the agent's to fix.

---

## For tonight's weekly review (routine 5) — FIVE items

⚠ **The count was written as "four" in this file's first draft and FIVE items are listed below.**
**Corrected here rather than left beside its correction** — it is catch (24)'s shape (*an
enumeration that sounds exhaustive and is not*) arriving in a heading, and the standing rule is
to count the list, not to write the count from intent.

1. ⚠⚠ **THE THESIS COUNTER IN `state.md`'s CARRY-FORWARD WENT STALE FOR FOUR CONSECUTIVE
   SESSIONS AND THIS SEAT RE-DERIVED IT FROM SOURCE.** The item read **166** (87 archived +
   79 live) — correct as of **10-16** and never advanced by the 10-19, 10-20, 10-21 or 10-22
   seats. True figure at the start of today: **185** (87 archived + **98** live, counted by
   date from headings), and **189** with today's four. ⚠ **THIS IS THE MIRROR OF YESTERDAY'S
   "39 SESSIONS" CATCH, AND THE PAIR IS THE FINDING: on 10-22 a narrative figure in prose
   drifted beside a sound counter, and the lesson drawn was *"quote the counter item, never a
   number from inside a sentence"* — AND THE COUNTER ITEM IT POINTED AT WAS ITSELF 19
   BEHIND.** ⚠ **A tracked counter is not self-maintaining; it is only as current as the last
   seat that re-derived it. The SESSION half of the same item reconciles exactly and was
   re-derived here too (a `bars --days 90` pull returns exactly **34** rows strictly after the
   09-03 fill).**
2. **The 44bp → 7bp benchmark move and its decomposition** (cash cushion **+11.96bp** vs
   entry price on the one fill **−18.84bp**, net **−6.88bp**). ⚠ **Do not score it as
   progress — it is the cash drag running backwards and it reverses when the index turns up.**
3. **The §3 foreign-listing pattern**, which added two more instances today (Welspun,
   Seatrium, Electro Cable Egypt, Saab, Roche).
4. **The missing-close-run detector that still does not exist** (open human item (11)) — two
   of 33 close runs have vanished, and `alerts.md` reading "zero open incidents" still cannot
   tell a healthy week from a seat that died before `commit.py`.
5. **Monthly rollover is due next Friday, not today** — `research_log.md` is at **102** live
   October headings and the file is **~350KB**; the September section is already archived.
