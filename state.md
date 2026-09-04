# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-04 08:27 ET 1-premarket-research
week_of: 2026-08-31
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.12
satellite_pct: 0.0
cash_pct: 29.88
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


- **This run produced NO plan intents at all — no BUY, no SELL, no REBALANCE — and that is the
  finished output, not an unfinished one.** `plan_today.md` is dated **2026-09-04** and says so
  explicitly. The 09:35 run should read it, confirm core is in band, and do nothing. **Core is
  established (`core_established: true`); the bootstrap path is closed permanently — do not
  re-run it.**

- **⚠ New positions were fully permitted this run and nothing was blocked.** Breaker INACTIVE,
  weekly cap **0 of 3**, satellite sleeve **empty with 29.88% cash ($30,000.00)**, no
  restricting note in `control.md`. **The research simply did not produce an eligible
  candidate.** This distinction matters for anyone reading `research_log.md` later: today's
  empty output is a §4 result, not a §6 constraint.

- **Sleeve read 08:27 ET: equity $100,415.98, cash $30,000.00, core VOO 70.12%, satellite 0.0%
  (count 0), cash 29.88%.** `core_in_band: true`, `rebalance_needed: false`,
  `rebalance_delta: −124.80`. **No rebalance is due** — the delta is 0.12% of equity and is
  VOO's overnight mark moving, not drift. §2 rebalances at the **band edge** (65–75%), never to
  the exact 70% target. VOO marks at **710.94** against `lastday_price` 710.72, unrealized
  **+$415.99 (+0.594%)** on 99.046311231 shares at avg_entry 706.74.

- **⚠ Two VOO prices exist and they are not interchangeable.** The broker mark (710.94 here)
  drives `equity` and P&L; `bars --adjustment all` returns the official close (**710.70** for
  09-03) and that is what would feed `highest_close`. **Never mix them inside one §5.4
  comparison.**

- **The §5.4 trailing stop is still NOT ARMED — fifteenth consecutive run recording it.** §5
  exempts core from all four sell rules, so VOO is deliberately absent from `positions.md`: no
  thesis, no timing window, no `highest_close`. **§5.4 arms the day the first *satellite*
  position opens.** Step 4's sell-rule pass ran in full this run and had **no subject** — that
  is now written out as a table in `positions.md` under the 08:27 reconciliation. **Do not
  backfill anything from `bars`. There is nothing to backfill.**

- **⚠ `positions.md` legitimately disagrees with the raw broker, and this is the normal steady
  state.** Ledger reads *(none)*; `alpaca.py positions` returns one VOO row. **Not a
  discrepancy** — compare **satellite blocks to satellite Alpaca positions**, never raw ledger
  to raw broker, or a correct ledger reads as broken. Keep carrying this until the first
  satellite position exists.

- **Week rollover checked: none due.** ISO Monday of 2026-09-04 (Friday) is **2026-08-31**,
  matching `week_of`. `new_positions_this_week` stays **0 of 3**. Breaker INACTIVE,
  `consecutive_closed_losses: 0`, `halt_triggered_at: none`, `HALT_CLEARED_AT: none`; only a
  **closed** position can move the streak and nothing has ever closed. **Next week boundary:
  Monday 2026-09-07 — the Friday review runs today, and the reset belongs to Monday's run, not
  to it.**

- **⚠ THE DAY'S REAL FINDING: three separate second-order screens came back EXPLICITLY EMPTY.**
  Not "the candidate failed a filter" — *no source named a publicly traded US Company B at
  all*, on any of: **Lululemon's −18% guidance cut** (the two named share-takers, **Alo Yoga
  and Vuori, are private**), **Snowflake's beat-and-raise** (+16.55%, no named supplier or
  partner), and **the grid/transformer capacity cluster** (Eaton $242M, Siemens >$200M,
  Southwire $256M, HSP US >$60M, Niagara $71M — no named US-listed supplier to any of the
  five). When the sourced answer is repeatedly "none identified," the honest read is that the
  day's news had no second-order structure.

- **⚠ NEW STANDING RULE, and it is the most valuable thing this run produced: a
  MARKET-STRUCTURE FACT IS NOT A SUPPLIER RELATIONSHIP.** T-2026-09-04-01 (CLF) reached
  candidate status on one sourced phrase — *"the only domestic producer of grain-oriented
  electrical steel."* That phrase does most of the work of a mechanism sentence without being
  one: it implies inevitability while saying **nothing about whether these buyers buy from this
  seller**. GOES is imported at scale, which is exactly why the sole-domestic-producer line
  gets written. "Sole producer," "dominant share," "the only company that makes X" are facts
  about an **industry**, not about a **transaction**. This is the RTX failure wearing a
  disguise designed to feel like it removes the need to check. **Recognise the phrase; do not
  re-derive the lesson.**

- **CLF is dead four ways and there is no price at which it revives.** T-2026-09-04-01 failed
  part 1 (no sourced supplier link to any of the five projects), part 2 (**Cliffs discloses no
  GOES or electrical-steel revenue breakdown anywhere** in the 10-K/10-Q), part 3 (the projects
  are capital builds completing **2028**, not two-quarter revenue), and **§3 — market cap
  $7.01B as of 2026-09-04** (StrongBuyAnalytics; corroborated by MarketBeat $6.99B on 09-02 and
  $7.05B in August), **below the $10B floor**, so `alpaca.py buy` would have refused it. The
  priced-in check was **deliberately not run** — the mechanism failed first and §4 orders the
  filters before the thesis, per the RTX process note.

- **⚠ Do not reach for NKE, DECK, ONON, UAA or Gap/Athleta on the Lululemon story; do not reach
  for a hyperscaler on Snowflake; do not reach for ETN, PWR, GEV, HUBB, NVT or AMRC on the
  capacity cluster.** Every one of those is an ecosystem read-through with **no sourced
  relationship**, and Eaton is Company A announcing its own capex. The apparel version is the
  most fluent sentence available on today's tape and is the RTX failure exactly.

- **The "Company A's print implies Company B's print" failure did not recur, and it was actively
  screened for — third consecutive day.** Lululemon was the obvious vehicle ("LULU guides down,
  so a peer is taking share") and the dedicated screen came back explicitly empty. Prior
  instances on record: SAIC → LDOS/CACI/BAH (09-01), Dell → HPE (09-02), Broadcom → competitors
  (09-03). **Expect the shape again.**

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
  at which the rejection flips** — it failed for having already fallen. Flagged to the human in
  the 09-03 ClickUp summary and re-flagged today.

- **⚠ Do not reach for COHR, CIEN, AVGO, CSCO, AAOI, GLW, APH, NOK, ERIC or ANET on the Ciena
  story.** The sourced screen named **only Lumentum**. If AI-optics ever becomes a live driver,
  **LITE, COHR and CIEN would share it** and §4's correlation rule permits at most one.

- **LITE, MU and LHX: not re-checked, and the reason is absence of evidence, not resolve.** None
  appeared in today's funnel; their filters were **not** re-run. Third consecutive day recording
  this. If a future funnel surfaces one **from a source**, re-run the filter and re-test the
  timing window **from that day's date** — legitimate, and different from inheriting a
  conclusion.

- **⚠ FOUR EARLIER STANDING RULES, sharing one root cause, now joined by the fifth above.**
  (i) *Screen on the mechanism before running filters* (RTX — a filter is not a substitute for a
  sourced candidate). (ii) *Verify what the company currently sells, post-spin* (WDC).
  (iii) *Verify the news is new to the company's own disclosure* (AEP). (iv) *A recurring ticker
  is a warning, not corroboration* (LHX). (v) *A market-structure fact is not a supplier
  relationship* (CLF, new today).

- **Live events examined and deliberately not traded — do not re-derive these.** From today:
  (a) **Lululemon guidance cut**, (b) **Snowflake beat/raise**, (c) **the grid capacity
  cluster** — all three above; (d) **Ionis ZANVASTRO FDA approval** — only partner is
  **Italy-listed Recordati** (§3), William Blair models **$295M peak *global*** sales against
  ~€2.3B revenue (§4.2), and ex-US filings are **expected 2027** (§4.3); (e) **Nscale–Figure
  $3.5B compute** — both private; (f) **Cipla/Qilu Keytruda biosimilar** — non-US parties, and
  the mechanism runs **against** Merck in a long-only book; (g) **LG Energy Solution / Smackover
  Lithium 10-year** — Korea-listed buyer, US parent Standard Lithium far below the floor;
  (h) **AEVEX, Curia, Calumet, UpSolv/NexKemia, Unusual Machines/Altana, Modular Medical** — all
  private or sub-floor with no named counterparty; (i) **Caltrain five-year consultant
  agreement** — **the consultant's name is blank in the source document**; (j) **the TTM
  Technologies Syracuse UHDI plant** — **June 2026, three months stale**, not a catalyst in this
  window; (k) **macro: ISM services 55.4 with input prices highest since Oct 2022, claims 206k,
  August payrolls due today (consensus +56k), Waller's dovish remarks** — no segment, no dollar
  path, and a rising-input-cost print has no long second-order candidate here.

- **"Nvidia acquires Hugging Face for $13B" resurfaced in the `--recency day` window and was NOT
  reconsidered.** Already rejected on prior runs as unsigned talks; it is now reported as a deal
  but thinly sourced (a news-brief summary, not a filing) and **closes in 2027**, outside §4.3
  by itself. Listed only because it reappeared.

- **Ten thesis IDs now carry a 2026-09-0x date across four days**; six of them are from
  2026-09-01, produced by three runs against one rolling news window. **A reader scanning
  `research_log.md` should not read ten IDs as ten days of work.**

- **`alerts.md` remains empty — zero incidents, nothing SYSTEMIC, nothing unresolved.** Selftest
  passed all five checks this run. No alert raised and none warranted. No circuit-breaker alert
  was due — nothing has ever closed, so the streak cannot have moved.

- **Cleared from carry-forward this run:** the 2026-09-03 core-fill establishment note (acted on
  and superseded — `core_established: true` is now simply state), the 09-03 close snapshot
  (superseded by today's 08:27 sleeve read), and the "no orders in limbo overnight" note
  (nothing has been submitted since). All research carry-forward is retained because the funnel
  is rolling and the same names recur.

- **Next run is today's 09:35 ET market-open (2-market-open-execution).** It starts with core at
  **70.12% in band**, **zero satellite positions**, the weekly cap at **0 of 3**, the trailing
  stop **still unarmed**, and a plan dated **2026-09-04** whose entire content is *do nothing*.
  **Today is Friday — the weekly review (5-weekly-review) also runs, and it will be reviewing a
  week with zero satellite trades.**
