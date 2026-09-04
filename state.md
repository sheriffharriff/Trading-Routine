# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-04 16:16 ET 4-market-close-journal
week_of: 2026-08-31
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.03
satellite_pct: 0.0
cash_pct: 29.97
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

- **⚠ THE NEXT TRADING SESSION IS TUESDAY 2026-09-08. MONDAY 2026-09-07 IS LABOR DAY.** `clock`
  at 16:16 ET today returns `is_open: false` with `next_open: 2026-09-08T09:30:00-04:00`. Today
  itself was a **normal full session, 09:30–16:00 ET** — the closed flag at 16:16 means the bell
  has rung, not that the day was a holiday. **A run firing Monday should log a holiday skip and
  exit successfully; that is not a fault and is not a missed close run.**

- **⚠ TUESDAY'S RUN OWES A WEEK ROLLOVER, AND IT IS THE FIRST ONE THIS REPO HAS EVER DONE.** ISO
  Monday of 2026-09-08 is **2026-09-07**, which differs from `week_of: 2026-08-31`. Reset
  `new_positions_this_week` to **0** and set `week_of: 2026-09-07`. **The reset is due even
  though the boundary Monday is a holiday** — the anchor is the ISO Monday, not the first
  session — and it deliberately does not depend on the Friday review having run. Whichever
  routine fires first on Tuesday does it.

- **Close-run high-water pass: EXECUTED IN FULL, working list EMPTY. Nothing was recorded and
  that is correct.** Zero satellite positions, so `positions.md` has no `highest_close` field to
  stamp and no `(as of ...)` date to advance. **This is a third state, distinct from both
  "current" and "stale": ABSENT.** The midday backfill trigger keys on a stale date and an
  absent field cannot be stale — **so do NOT backfill from `bars`. There is nothing to
  backfill.** Eighteenth consecutive run recording this.

- **§5.4 trailing stop still NOT ARMED — not silently disabled.** §5 exempts core from all four
  sell rules, so VOO is deliberately absent from `positions.md`: no thesis, no timing window, no
  `highest_close`. **§5.4 arms the day the first *satellite* position opens.** VOO's official
  close today was **707.86** and was **deliberately not written as a high-water mark anywhere** —
  doing so would fabricate a trailing stop on a position §5 exempts. **Do not record it.**

- **⚠ THE TWO-PRICE TRAP WENT LIVE TODAY, AND THE ORDERING WAS THE REVERSE OF THE INTRADAY
  PATTERN.** `alpaca.py positions` runs first and hands back `current_price` **707.59**, which at
  16:16 looks exactly like a closing price. The official close from `bars --adjustment all` is
  **707.86** — the official close sat **ABOVE** the broker mark, unlike the intraday fades seen
  all week. On 99.046311231 shares the gap is **$26.75** of unrealized P&L. It cost nothing today
  because core has no `highest_close`. **The day a satellite position exists, that shortcut
  writes a wrong high-water mark — which does not error, does not look stale, and silently moves
  the §5.4 stop to a level nobody chose. Always pull `bars` for the close. Never mix the two
  inside one §5.4 comparison.**

- **Close sleeve read 16:16 ET: equity $100,084.18, cash $30,000.00, core VOO 70.03%, satellite
  0.0% (count 0), cash 29.97%.** `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: −25.25` — 0.03% of equity, deep inside the §2 65–75% band. **No rebalance is
  due Tuesday.** Day P&L **−$310.01 (−0.31%)** against `last_equity` 100,394.19; since inception
  **+$84.18 (+0.08%)**. VOO unrealized **+$84.19 (+0.12%)** on 99.046311231 shares at avg entry
  706.74.

- **⚠ The book fell −0.31% against VOO's −0.40% and THIS IS NOT OUTPERFORMANCE.** It is 70%
  exposure capturing 70% of a down move, and it runs identically in reverse on every up day. The
  09-01 journal caught the same reassuring framing when the book was 100% cash; **it recurred
  today in a different structure, which means it is not a one-off slip but a framing that will be
  produced every time the market falls.** Do not let a future summary write it as skill.

- **⚠ FLAGGED TO THE HUMAN, NEW TODAY AND UNRESOLVED: the structure points away from §1.** Four
  days of individually-correct no-trade decisions leave the satellite sleeve undeployed, making
  the book functionally a 70% index tracker with a 30% cash drag. §2 permits the cash and §4 says
  most runs should end in no trade — **both rules were followed** — but a 70/30 cash book cannot
  beat the S&P over a rolling 12 months (§1) in a rising market, only in a falling one. **The
  agent must NOT respond by lowering the §4 bar.** This is a strategy-level question for the
  human and went out in today's ClickUp summary.

- **NO TRADES, NO FILLS, NOTHING CLOSED, NOTHING IN LIMBO.** `orders --status all` returns
  exactly one order in the account's entire history — the 09-03 core VOO buy `d177d8f0`,
  `status: filled`, terminal. **Nothing from today needs resolving into `trade_log.md`**, which
  matters more than usual because the next session is four days away. `trade_log.md` was
  correctly not appended to. Loss streak stays 0 — **nothing has ever closed**, so the §6 streak
  cannot have moved and no circuit-breaker alert was due.

- **⚠ `positions.md` legitimately disagrees with the raw broker, and this is the normal steady
  state.** Ledger reads *(none)*; `alpaca.py positions` returns one VOO row. **Not a
  discrepancy** — compare **satellite blocks to satellite Alpaca positions**, never raw ledger to
  raw broker, or a correct ledger reads as broken. Reconciled again at 16:16: zero against zero,
  they agree. Keep carrying this until the first satellite position exists.

- **⚠ THE DAY'S REAL RESEARCH FINDING: three separate second-order screens came back EXPLICITLY
  EMPTY.** Not "the candidate failed a filter" — *no source named a publicly traded US Company B
  at all*, on any of: **Lululemon's −18% guidance cut** (the two named share-takers, **Alo Yoga
  and Vuori, are private**), **Snowflake's beat-and-raise** (+16.55%, no named supplier or
  partner), and **the grid/transformer capacity cluster** (Eaton $242M, Siemens >$200M, Southwire
  $256M, HSP US >$60M, Niagara $71M — no named US-listed supplier to any of the five). When the
  sourced answer is repeatedly "none identified," the honest read is that the day's news had no
  second-order structure.

- **⚠ STANDING RULE (v): A MARKET-STRUCTURE FACT IS NOT A SUPPLIER RELATIONSHIP.**
  T-2026-09-04-01 (CLF) reached candidate status on one sourced phrase — *"the only domestic
  producer of grain-oriented electrical steel."* That phrase does most of the work of a mechanism
  sentence without being one: it implies inevitability while saying **nothing about whether these
  buyers buy from this seller**. GOES is imported at scale, which is exactly why the
  sole-domestic-producer line gets written. "Sole producer," "dominant share," "the only company
  that makes X" are facts about an **industry**, not about a **transaction**. This is the RTX
  failure wearing a disguise designed to feel like it removes the need to check. **Recognise the
  phrase; do not re-derive the lesson.**

- **CLF is dead four ways and there is no price at which it revives.** T-2026-09-04-01 failed
  part 1 (no sourced supplier link to any of the five projects), part 2 (**Cliffs discloses no
  GOES or electrical-steel revenue breakdown anywhere** in the 10-K/10-Q), part 3 (the projects
  are capital builds completing **2028**, not two-quarter revenue), and **§3 — market cap $7.01B
  as of 2026-09-04**, **below the $10B floor**, so `alpaca.py buy` would have refused it. The
  priced-in check was **deliberately not run** — the mechanism failed first and §4 orders the
  filters before the thesis, per the RTX process note.

- **⚠ Do not reach for NKE, DECK, ONON, UAA or Gap/Athleta on the Lululemon story; do not reach
  for a hyperscaler on Snowflake; do not reach for ETN, PWR, GEV, HUBB, NVT or AMRC on the
  capacity cluster.** Every one of those is an ecosystem read-through with **no sourced
  relationship**, and Eaton is Company A announcing its own capex. The apparel version is the
  most fluent sentence available on today's tape and is the RTX failure exactly.

- **The "Company A's print implies Company B's print" failure did not recur, and it was actively
  screened for — fourth consecutive day.** Prior instances on record: SAIC → LDOS/CACI/BAH
  (09-01), Dell → HPE (09-02), Broadcom → competitors (09-03). **Expect the shape again.**

- **The §3 universe filter is now doing more work in this log than the priced-in filter ever
  has.** Four of the last dozen rejections were US-listing or market-cap failures on names that
  reached the funnel through a mechanism screen (CLF, Recordati, Smackover/SLI, plus the
  private-company drops). The priced-in filter's scoreboard is unchanged: across nine worked
  candidates, **seven passed it and failed the thesis**, **two passed the thesis and failed it
  (MU, LITE)**. **A passing priced-in check is a veto that did not fire, never encouragement** —
  "has not moved" and "should have moved but didn't" are the same number.

- **⚠ LITE / the priced-in filter — still waiting on the human, unchanged and not re-litigated.**
  T-2026-09-03-01 (Lumentum) produced the best-sourced part 1 in the log and was rejected because
  `move --sessions 5` returned **−7.35%**, `priced_in: true` — **a drawdown, not a run-up**. **No
  run has reinterpreted the filter and none should**; the fix is a human editing §4 or
  `alpaca.py move`, not a run deciding the rule does not mean what it says. **There is no price
  at which the rejection flips** — it failed for having already fallen. Re-flagged in today's
  ClickUp summary for the second consecutive day.

- **⚠ Do not reach for COHR, CIEN, AVGO, CSCO, AAOI, GLW, APH, NOK, ERIC or ANET on the Ciena
  story.** The sourced screen named **only Lumentum**. If AI-optics ever becomes a live driver,
  **LITE, COHR and CIEN would share it** and §4's correlation rule permits at most one.

- **LITE, MU and LHX: not re-checked, and the reason is absence of evidence, not resolve.** None
  appeared in today's funnel; their filters were **not** re-run. Fourth consecutive day recording
  this. If a future funnel surfaces one **from a source**, re-run the filter and re-test the
  timing window **from that day's date** — legitimate, and different from inheriting a
  conclusion.

- **⚠ FIVE STANDING RULES, sharing one root cause.** (i) *Screen on the mechanism before running
  filters* (RTX — a filter is not a substitute for a sourced candidate). (ii) *Verify what the
  company currently sells, post-spin* (WDC). (iii) *Verify the news is new to the company's own
  disclosure* (AEP). (iv) *A recurring ticker is a warning, not corroboration* (LHX). (v) *A
  market-structure fact is not a supplier relationship* (CLF).

- **Live events examined and deliberately not traded — do not re-derive these.** From 09-04:
  (a) **Lululemon guidance cut**, (b) **Snowflake beat/raise**, (c) **the grid capacity cluster**
  — all three above; (d) **Ionis ZANVASTRO FDA approval** — only partner is **Italy-listed
  Recordati** (§3), William Blair models **$295M peak *global*** sales against ~€2.3B revenue
  (§4.2), ex-US filings **expected 2027** (§4.3); (e) **Nscale–Figure $3.5B compute** — both
  private; (f) **Cipla/Qilu Keytruda biosimilar** — non-US parties, and the mechanism runs
  **against** Merck in a long-only book; (g) **LG Energy Solution / Smackover Lithium 10-year** —
  Korea-listed buyer, US parent Standard Lithium far below the floor; (h) **AEVEX, Curia,
  Calumet, UpSolv/NexKemia, Unusual Machines/Altana, Modular Medical** — all private or sub-floor
  with no named counterparty; (i) **Caltrain five-year consultant agreement** — **the
  consultant's name is blank in the source document**; (j) **the TTM Technologies Syracuse UHDI
  plant** — **June 2026, three months stale**; (k) **macro: ISM services 55.4 with input prices
  highest since Oct 2022, claims 206k, August payrolls, Waller's dovish remarks** — no segment,
  no dollar path.

- **"Nvidia acquires Hugging Face for $13B" resurfaced in the `--recency day` window and was NOT
  reconsidered.** Already rejected on prior runs as unsigned talks; it is now reported as a deal
  but thinly sourced (a news-brief summary, not a filing) and **closes in 2027**, outside §4.3 by
  itself. Listed only because it reappeared.

- **Ten thesis IDs now carry a 2026-09-0x date across four days**; six of them are from
  2026-09-01, produced by three runs against one rolling news window. **A reader scanning
  `research_log.md` should not read ten IDs as ten days of work.**

- **`alerts.md` remains empty — zero incidents, nothing SYSTEMIC, nothing unresolved.** The
  selftest passed all five checks on all four of today's runs.

- **⚠ `plan_today.md` is consumed and spent.** Its `plan_date` stays **2026-09-04** until the next
  pre-market run overwrites it. **No later run may re-execute it** — it was executed at 09:36 with
  an empty intent list. Plan versus outcome: the plan said *do nothing*, and nothing is what
  happened, on all three of BUY, SELL and REBALANCE.

- **Cleared from carry-forward this run:** the 12:35 midday sleeve snapshot and the midday
  "no exits, no subject" note — both superseded by the 16:16 close read above, which carries the
  same distinction. All research carry-forward is retained because the funnel is rolling and the
  same names recur.

- **Today's ClickUp daily summary: task `86bbv6npm`** — https://app.clickup.com/t/86bbv6npm

- **The week closed with zero satellite activity: four runs today (08:27, 09:36, 12:35, 16:16),
  each of which correctly did nothing.** `5-weekly-review` (Friday) is the only run left today
  and starts from core **70.03% in band**, **zero satellite positions**, weekly cap **0 of 3**,
  trailing stop **unarmed**, `alerts.md` empty, and **zero trades to review**. **Do not read the
  accumulation of quiet runs as pressure to find something.**
