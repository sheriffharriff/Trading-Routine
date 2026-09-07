# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-07 16:16 ET 4-market-close-journal (HOLIDAY SKIP — market closed all day, Labor Day; no session close existed, no high-water marks recorded, no ClickUp summary posted)
week_of: 2026-09-07
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.04
satellite_pct: 0.0
cash_pct: 29.96
open_thesis_ids: none
```

---

## Field meanings

**`week_of`** — the Monday of the current ISO week. Every run compares today's week anchor
to this value; if they differ, reset `new_positions_this_week` to 0 and update this field.
The reset deliberately does not depend on the Friday review having run, so a skipped Friday
cannot leave the §6 weekly cap stuck at its limit.

**`new_positions_this_week`** — satellite positions *opened* this week. §6 caps it at 3.
Exits do not count.

**`consecutive_closed_losses`** — incremented when a satellite position is closed at a loss,
reset to 0 when one closes at a gain. At 3, set `circuit_breaker: ACTIVE` and record
`halt_triggered_at` as today.

**`circuit_breaker`** — `ACTIVE` or `INACTIVE`. While ACTIVE: no new positions of any kind
(§7). Existing positions are still managed per §5, research and journaling continue, and the
halt is flagged prominently in the ClickUp summary (§6). Core rebalancing is still permitted —
§6 halts *new positions*, and restoring the core sleeve to its 70% target is neither a new
position nor a satellite trade.

**`halt_triggered_at`** — date the breaker tripped. Compared against `HALT_CLEARED_AT` in
`control.md`; the halt lifts only when the clearance date is strictly later. If the breaker
is ACTIVE and this field is `none`, the halt stays active — an unknown trigger date is not
grounds to start trading.

**`core_established`** — `false` until the VOO core sleeve exists. The market-open routine
bootstraps it on the first trading day and this flips to `true`, which disables the
bootstrap path permanently.

**`core_pct` / `satellite_pct` / `cash_pct`** — sleeve allocation as of the last run, in
percent of total account value. §2 rebalance band is core 65–75%.

**`open_thesis_ids`** — comma-separated thesis IDs for currently open satellite positions.
Cross-check against `positions.md`; if they disagree, `positions.md` and the live Alpaca
position list win, and the discrepancy goes in the journal.

---

## Carry forward

Anything the next run must not lose. Cleared once acted on.
- **✅ MONDAY 2026-09-07 WAS THE LABOR DAY HOLIDAY SKIP AND ALL FOUR RUNS EXECUTED IT CORRECTLY.**
  08:29 pre-market, 09:36 market-open, 12:35 midday and 16:16 close each passed the selftest on all
  five checks (`trading_enabled: true`, LIVE paper account) and each stopped at its own market-closed
  branch. **Across the four runs: zero orders submitted, zero theses written, `plan_today.md` not
  overwritten, no §5 rule evaluated, no high-water mark recorded, and no ClickUp daily summary posted.**
  The close run withheld the summary deliberately — the routine forbids one for a day that did not
  happen, and a summary reading "day P&L 0.00%" would report a flat session rather than an absent one.
  **The holiday was confirmed, not assumed:** `clock` gave `is_open: false` with `next_open:
  2026-09-08T09:30:00-04:00` — **tomorrow, which is what separates a holiday from the ordinary
  post-16:00 closed state**, since at 16:15 on a normal weekday `is_open` is false too — and `bars
  --days 6` returned its newest bar dated **2026-09-04**, i.e. no 09-07 session bar exists. Account
  agrees: `balance_asof: 2026-09-04`, `change_today: 0`, equity = `last_equity`.
  *(This one item replaces the four separate per-run narrations of the same skip, and the 08:29 /
  09:36 / 12:35 / 09-04-close sleeve snapshots, all of which were acted on and are now cleared.)*

- **⚠ NEW, AND FLAGGED TO THE HUMAN: THE MEMORY FILES ARE BEING APPENDED TO WHERE THEY SHOULD BE
  CLEARED, AND IT NOW WORKS AGAINST THE CONTINUITY IT EXISTS TO SERVE.** `state.md` reached **405
  lines** and `positions.md` **42KB**, the majority of both being restatements of one null fact —
  no satellite positions, nothing to backfill. This block carried an item reading *"Nineteenth
  consecutive run recording this."* Carry-forward is defined four lines above as **cleared once
  acted on**; holiday-skip narration is acted on the moment the next run reads it. **The pull is
  structural, not a slip: a run is rewarded for showing it checked something, and a deleted note
  looks like a check that never happened.** It is harmful rather than untidy because this repo's
  only continuity mechanism is the next run *reading* these files — padding them with restatements
  of a null result raises the odds a genuinely live item (LITE, the standing rules, the undeployed
  sleeve) gets skimmed. **This run trimmed acted-on items and kept every live research item intact.
  A future run will feel the same pull; the correct response is to collapse, not to append.**

- **⚠ THE HIGH-WATER MARKS ARE NOT STALE — THEY ARE ABSENT, A THIRD STATE.** No satellite position
  exists, so `positions.md` has **no `highest_close` field and no `(as of ...)` date anywhere** in
  its `## Open positions` section. The midday backfill trigger keys on a **stale date**, and an
  absent field cannot be stale — **so do NOT backfill from `bars`. There is nothing to backfill.**
  **Do not manufacture a mark on core VOO to give the step a subject:** §5 exempts core from all
  four sell rules, and stamping one would fabricate a §5.4 trailing stop on a position that must
  never carry one. **§5.4 is NOT ARMED, not disabled — it arms the day the first satellite
  position opens.**

- **⚠ THE TWO-PRICE TRAP — ALWAYS PULL `bars` FOR A CLOSE, NEVER A `positions` FIELD.** The gap has
  now appeared in three different shapes: intraday fades all week, `current_price` **707.59** vs
  official close **707.86** at the 09-04 close (official *above* the broker mark, $26.75 on 99.05
  shares), and on a holiday a **third number** entirely — the broker carries `current_price` =
  `lastday_price` = **708.01** against Friday's official **707.86**, $14.86 apart. **The day a
  satellite position exists, that shortcut writes a wrong high-water mark that does not error, does
  not look stale, and silently moves the §5.4 stop to a level nobody chose. Never mix the two
  inside one §5.4 comparison.**

- **⚠ `positions.md` LEGITIMATELY DISAGREES WITH THE RAW BROKER — THIS IS THE NORMAL STEADY STATE.**
  Ledger reads *(none)*; `alpaca.py positions` returns one VOO row. **Compare satellite blocks to
  satellite Alpaca positions, never raw ledger to raw broker**, or a correct ledger reads as broken.
  Reconciled again at 16:16: zero satellite against zero satellite, they agree. Carry this until the
  first satellite position exists.

- **WEEK ROLLOVER DONE AND RE-CHECKED AT THE CLOSE: anchors matched, nothing reset — the check
  working, not a skipped step.** `week_of` **2026-09-07** is today's own ISO Monday;
  `new_positions_this_week` **0 of 3**. The anchor is the ISO Monday, **not the first session**,
  which is why it is correct even though 09-07 is a holiday. Tuesday should also find them matching.

- **NO TRADES, NO FILLS, NOTHING CLOSED, NOTHING IN LIMBO.** `orders --status all` returns exactly
  one order in the account's entire history — the 09-03 core VOO buy `d177d8f0`, `status: filled`,
  terminal. **Nothing needed resolving into `trade_log.md`**, which matters more than usual with a
  session gap. Loss streak stays **0 — nothing has ever closed**, so the §6 streak cannot have moved
  and no circuit-breaker alert was due. `alerts.md` **empty**.

- **⚠ `plan_today.md` STILL READS `plan_date: 2026-09-04` AND THAT IS INERT, NOT A FAULT.** The
  holiday run does not write a plan; **Tuesday's 08:00 pre-market run overwrites it**, and Tuesday's
  open run would refuse a plan not dated 2026-09-08 anyway. **Do not execute it.** No `stale-plan`
  alert was posted and none was due — the market-closed check precedes the staleness gate.

- **⚠ THREE ITEMS ARE WITH THE HUMAN, IN THE WEEKLY REVIEW AND IN ClickUp `86bbv75bz`. NONE IS THE
  AGENT'S TO DECIDE.** (1) The §4 priced-in filter reads a **drawdown** as priced-in — T-2026-09-03-01
  (LITE) produced the best-sourced part 1 in the log and was rejected because `move --sessions 5`
  returned **−7.35%**, `priced_in: true`. **No run has reinterpreted the filter and none should**; the
  fix is a human editing §4 or `alpaca.py move`. **There is no price at which that rejection flips** —
  it failed for having already fallen. (2) The satellite sleeve is **structurally undeployed** — ten
  theses, zero positions; a 70/30 cash book cannot beat the S&P over a rolling 12 months (§1) in a
  rising market. §2 permits the cash and §4 says most runs end in no trade — **both rules were
  followed. The agent must NOT respond by lowering the §4 bar.** (3) The core's **−0.485% divergence
  from VOO is the 09-03 entry gap** (fill 706.74, +0.483% above the prior close), **not tracking error
  and never skill** — measure the core from the **706.74 fill**, or a one-time level offset gets
  re-reported as drift every week.

- **⚠ REJECT SCOREBOARD (opened 09-04, a tally not evidence — 1–3 sessions is noise and 10 names is
  not a sample; a future review must not quote it as a result).** 6 of 10 rejects beat VOO, mean
  excess −0.16%. **The split is the finding:** the 8 rejected on the four-part thesis or §3 average
  **−0.97%** (the thesis test selecting correctly); the 2 rejected by the §4 priced-in filter —
  **MU +5.49%, LITE +0.62%** — average **+3.06%** and are **the same two that passed the thesis.**
  **MU and LITE must never be merged into one finding:** MU failed on a real +5.27% run-up (the rule
  working as designed and costing money — change nothing), LITE on a drawdown (the open question).
  **Six of ten rejects running without us is the HEALTHY reading** — a rejection rate that is never
  wrong would mean the filters are too loose. **Do not tighten §4 in response, and do not loosen it.**

- **⚠ THE REASSURING FRAMING — EXPECT TO GENERATE IT AND EXPECT TO DELETE IT.** "The book fell −0.31%
  against VOO's −0.40%" is **70% exposure capturing 70% of a down move**, and it runs identically in
  reverse on every up day. It has now appeared on 09-01, 09-02, 09-04 and inside the weekly review
  itself, across three different book structures (100% cash, dry-run counterfactual, 70/30 invested)
  — **not a slip but the sentence this agent produces by default whenever partial exposure and a down
  day coincide.** Caught every time before reaching a summary; keep that record intact. Related:
  anchoring the week to the 08-28 close reads **+0.015% excess and that is not outperformance** — it
  puts VOO's 09-01 −0.67% day inside a window the book was 100% cash for. **Anchor to 08-31, the
  first operating day: the honest number is −0.313%.**

- **⚠ FIVE STANDING RULES, ONE ROOT CAUSE.** (i) *Screen on the mechanism before running filters*
  (RTX — a filter is not a substitute for a sourced candidate). (ii) *Verify what the company
  currently sells, post-spin* (WDC). (iii) *Verify the news is new to the company's own disclosure*
  (AEP). (iv) *A recurring ticker is a warning, not corroboration* (LHX). (v) *A market-structure
  fact is not a supplier relationship* (CLF — "the only domestic producer of grain-oriented
  electrical steel" does the work of a mechanism sentence while saying **nothing about whether these
  buyers buy from this seller**; "sole producer," "dominant share," "the only company that makes X"
  are facts about an **industry**, not a **transaction**. This is the RTX failure in a disguise
  designed to feel like it removes the need to check. **Recognise the phrase; do not re-derive it.**)

- **The "Company A's print implies Company B's print" failure did not recur and was actively screened
  for — four consecutive days.** Instances on record: SAIC → LDOS/CACI/BAH (09-01), Dell → HPE
  (09-02), Broadcom → competitors (09-03). **Expect the shape again.**

- **⚠ DO NOT REACH FOR THESE — every one is an ecosystem read-through with NO sourced relationship.**
  On the Lululemon story: NKE, DECK, ONON, UAA, Gap/Athleta (the apparel version is the most fluent
  sentence available on that tape and is the RTX failure exactly). On Snowflake: any hyperscaler. On
  the grid/transformer cluster: ETN, PWR, GEV, HUBB, NVT, AMRC — **Eaton is Company A announcing its
  own capex.** On the Ciena story: COHR, CIEN, AVGO, CSCO, AAOI, GLW, APH, NOK, ERIC, ANET — the
  sourced screen named **only Lumentum**; if AI-optics becomes a live driver, **LITE, COHR and CIEN
  share it** and §4's correlation rule permits at most one.

- **Live events examined 09-04 and deliberately not traded — do not re-derive these.**
  (a) **Lululemon −18% guidance cut** — the two named share-takers, **Alo Yoga and Vuori, are
  private**; (b) **Snowflake beat/raise** (+16.55%) — no named supplier or partner; (c) **the grid
  capacity cluster** (Eaton $242M, Siemens >$200M, Southwire $256M, HSP US >$60M, Niagara $71M) — no
  named US-listed supplier to any of the five; (d) **Ionis ZANVASTRO FDA approval** — only partner is
  **Italy-listed Recordati** (§3), ~$295M peak **global** sales vs ~€2.3B revenue (§4.2), ex-US
  filings **2027** (§4.3); (e) **Nscale–Figure $3.5B compute** — both private; (f) **Cipla/Qilu
  Keytruda biosimilar** — non-US parties, and the mechanism runs **against** Merck in a long-only
  book; (g) **LG Energy Solution / Smackover Lithium** — Korea-listed buyer, US parent far below the
  floor; (h) **AEVEX, Curia, Calumet, UpSolv/NexKemia, Unusual Machines/Altana, Modular Medical** —
  private or sub-floor, no named counterparty; (i) **Caltrain consultant agreement** — **the
  consultant's name is blank in the source document**; (j) **TTM Technologies Syracuse UHDI plant** —
  **June 2026, three months stale**; (k) **macro: ISM services 55.4, claims 206k, August payrolls,
  Waller's dovish remarks** — no segment, no dollar path. **"Nvidia acquires Hugging Face for $13B"
  resurfaced in the `--recency day` window and was NOT reconsidered** — thinly sourced and **closes
  in 2027**, outside §4.3 by itself. **CLF (T-2026-09-04-01) is dead four ways** — no sourced supplier
  link, no disclosed GOES revenue breakdown anywhere in the 10-K/10-Q, projects completing **2028**,
  and **§3 market cap $7.01B, below the $10B floor** — `alpaca.py buy` would have refused it.

- **⚠ THE FRIDAY FUNNEL HAS NOT AGED OUT, BUT IT HAS NOT BEEN RE-SCREENED EITHER.** The last live
  news read was **Friday 09-04**, so every standing rule and every "do not reach for X" above is
  exactly as fresh on Tuesday as it was Friday — **a holiday skip does not age out the funnel.** The
  one thing Tuesday must NOT do is treat these rejects as already-screened for Tuesday's tape: the
  `--recency day` window will have moved on. **If a name resurfaces from a source, re-run its filters
  and re-test the timing window from Tuesday's date** — that is legitimate, and different from
  inheriting a conclusion. **LITE, MU and LHX were not re-checked, and the reason is absence of
  evidence, not resolve** — none appeared in the funnel; their filters were not re-run.

- **⚠ ALL FOUR §5 SELL RULES ARE UNTESTED CODE PATHS, NOT PROVEN ONES.** Zero positions have ever
  closed, so §5.1 invalidation, §5.2 time stop, §5.3 hard stop and §5.4 trailing stop have never been
  evaluated against a real subject. **Five days of "no exits" recorded the absence of a subject, not
  five clean bills of health.**

- **THE WEEK BEGINNING 2026-09-07 OPENED WITH A HOLIDAY. THE FIRST LIVE SESSION IS TUESDAY
  2026-09-08** (`next_open` 09:30 ET) — it gets a full pre-market run, a real plan, and the first
  genuine close-run high-water pass of the week if a position is opened. State carried into it: core
  **70.04% in band** (`rebalance_delta` −$37.73, 0.04% of equity — **no rebalance due Tuesday**),
  satellite **0.0% / zero positions**, cash 29.96%, weekly cap **0 of 3**, trailing stop **unarmed**,
  breaker **INACTIVE**, `alerts.md` **empty**. **Do not read the accumulation of quiet runs as
  pressure to find something on Tuesday.**

- **MONTHLY ARCHIVE ROLLOVER: CHECKED 09-04, NOT DUE.** Every entry in `research_log.md`,
  `trade_log.md` and `journal.md` is dated **2026-09**; `archive/` holds only its README. Next
  rollover is the first Friday review of **October 2026**.

- **Friday's ClickUp tasks, for reference:** daily summary `86bbv6npm`
  (https://app.clickup.com/t/86bbv6npm), weekly review `86bbv75bz`
  (https://app.clickup.com/t/86bbv75bz). **No ClickUp task was created by any of today's four
  holiday runs** — correctly, since no session occurred.
