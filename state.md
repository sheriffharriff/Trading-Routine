# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-03 12:35 ET 3-midday-management
week_of: 2026-08-31
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 70.1
satellite_pct: 0.0
cash_pct: 29.9
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


- **✅ THE §2 CORE SLEEVE IS ESTABLISHED — the first real fill in this repo's history landed at
  09:36:21 ET on 2026-09-03.** `core_established` is now `true` and the flag path in Step 3 will
  not run again. Fill: BUY VOO **99.046311231 @ $706.74**, notional $70,000.00, order
  `d177d8f0-cd0c-41bf-95c1-4772318265fd`, verified `"status": "filled", "terminal": true` before
  it was written to `trade_log.md`. **Do not re-run the bootstrap tomorrow, or the day after, or
  ever** — Step 3's whole point is that this path never fires again once the flag flips. Step 7's
  rebalance only fires again if drift takes core outside 65–75%. At 12:35 ET core is **70.1%**
  (`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: −99.53`) — nowhere near the
  band edges, and the sign flip from +5.06 to −99.53 is just VOO up 0.95% on the session, not
  drift worth acting on.

- **⚠ `positions.md` legitimately disagrees with the broker. The 12:35 run confirmed it and it is
  now a normal steady state, not a pending surprise.** The ledger reads *(none)* while
  `alpaca.py positions` returns one VOO row (99.046311231 @ avg_entry 706.74). **This is not a
  discrepancy** — §5 exempts core from all four sell rules, so it deliberately has no thesis, no
  timing window, no `highest_close`. Every reconciliation must check **satellite blocks** against
  **satellite** Alpaca positions, never the raw ledger against the raw broker. A run that does the
  raw comparison will read a correct ledger as broken. **Keep carrying this line until the first
  satellite position exists**, at which point the two lists start matching again on their own.

- **The §5.4 trailing stop is still not armed, and the core fill did not arm it.** Core is exempt
  from §5.4 by design. It arms the day the first *satellite* position opens. This is the
  thirteenth consecutive run to record the distinction rather than assume it carried — the state
  ("not silently disabled, not yet armed") is unchanged by a core fill, and unchanged at midday.

- **Week rollover checked again this run: none due.** ISO Monday of 2026-09-03 (Thursday) is
  **2026-08-31**, which matches `week_of`. `new_positions_this_week` stays 0 — the §6 weekly cap
  is fully available at 0 of 3, and the core bootstrap does **not** count against it (§6 caps
  *satellite* positions; core is not a satellite position). Breaker INACTIVE,
  `consecutive_closed_losses: 0`, `halt_triggered_at: none`; only a **closed** position can move
  the streak and nothing has ever closed. **The next week boundary is 2026-09-07.**

- **Midday 2026-09-03 was a genuine no-op, and the run stopped rather than looking for work.**
  Zero satellite positions means §5.1–5.4 had empty input; no Perplexity query was run, because
  with no `invalidation` line to defend a news query is manufacturing activity (§4 honest-broker,
  and Routine 3 Step 1 says so outright). **Nothing should have executed and did not** — and note
  that `TRADING_ENABLED` is now `true`, so the dry-run suppression that shaped 09-01 and 09-02 is
  no longer the reason nothing traded. The reason is that there is nothing to sell.

- **⚠ LITE / the priced-in filter — the hypothetical from 2026-09-02 became real yesterday's
  pre-market run, and it is a decision waiting on the human.** T-2026-09-03-01 (Lumentum) produced
  **the best-sourced part 1 in the log**: Morgan Stanley names LITE as a key **pump-laser**
  supplier to a Ciena that is explicitly "supply-constrained… particularly pump lasers," against a
  Ciena Q3 that grew revenue 37% y/y and raised FY guidance. It was rejected because
  `move --sessions 5` returned **−7.35%**, `priced_in: true`. **That is a drawdown, not a run-up**
  — CIEN itself is −12.25% over the same window on a beat-and-raise. **The premarket run did not
  reinterpret the filter and no future run should** — §4 is a veto, a veto that over-fires is the
  safe direction, and the fix is a human editing §4 or `alpaca.py move`, not a run deciding to
  ignore it. **LITE is not "wait for a better entry": it failed for having already fallen, so a
  further decline makes the reading worse.** There is no price at which the rejection flips.

- **⚠ Do not reach for COHR, CIEN, AVGO, CSCO, AAOI, GLW, APH, NOK, ERIC or ANET on the strength
  of the Ciena story.** The sourced screen named **only Lumentum** as a Ciena supplier. Every
  other name is an ecosystem read-through with no sourced supplier relationship — buying one would
  be the RTX failure exactly. If AI-optics ever becomes a live driver, **LITE, COHR and CIEN would
  share it** and §4's correlation rule permits at most one.

- **The scoreboard: the priced-in filter has still never been informative.** Across nine worked
  candidates, **seven passed the filter and failed the thesis** (NOC, LHX×2, WDC, AEP, RTX, and
  HPE which died at part 1) and **two passed the thesis and failed the filter (MU, LITE)**. Treat
  a passing priced-in check as a veto that did not fire, never as encouragement — "has not moved"
  and "should have moved but didn't" are the same number.

- **⚠ STANDING RULES — four, sharing one root cause.**
  (i) *Screen on the mechanism before running filters* (from RTX — a filter is not a substitute
  for a sourced candidate). (ii) *Verify what the company currently sells, post-spin* (from WDC).
  (iii) *Verify the news is new to the company's own disclosure* (from AEP — if management has
  already guided the pipeline the contract falls inside, the deal illustrates guidance rather than
  changing it). (iv) *A recurring ticker is a warning, not corroboration* (from LHX).

- **MU and LHX: not re-checked, and the reason is absence of evidence, not resolve.** Neither
  appeared in the 2026-09-03 08:27 ET funnel; the reason not to re-check them is that today's
  evidence does not produce them. If a future funnel surfaces one from a source, re-run the filter
  and re-test the timing window from that day's date — legitimate, and different from an
  inheritance-of-conclusion re-check.

- **The "Company A's print implies Company B's print" failure did not recur on 09-03, and it was
  actively screened for.** Broadcom's weak guidance was the obvious vehicle ("AVGO guides soft, so
  a competitor is taking share") and the dedicated screen came back explicitly empty. Two prior
  instances stand on record: SAIC → LDOS/CACI/BAH (09-01) and Dell → HPE (09-02). Expect the shape
  again; it is the most fluent sentence available on any given day.

- **Live events examined and deliberately not traded — do not re-derive these.**
  (a) **Ciena FQ3 beat-and-raise** (2026-09-02): LITE is the only sourced second-order name,
  rejected on the priced-in filter, above. (b) **Google adtech no-divestiture ruling** (Judge
  Brinkema, 2026-09-02): only Alphabet named by any source; a status-quo ruling changes no third
  party's revenue line, and the mechanism for a rival runs *against* it — nothing long. (c)
  **Broadcom FQ3 beat, weak guidance**: no Company B, and wrong direction for a long-only book.
  (d) **FuelCell Energy 75 MW Texas capacity reservation + 380 MW Fit Energy agreement**: FCEL is
  Company A and sub-$10B; counterparties are private or unnamed. (e) **KBR / NOAA National
  Mesonet**: Company A, no sourced subcontractor, five-year ceiling outside §4.3. (f) **Studsvik /
  GE Vernova Hitachi / Samsung C&T, 1.2 GW Swedish nuclear**: "commit to advancing" is not an
  order, non-US, years out. (g) **Uber's 3,300 layoffs**: internal cost action; no third company's
  revenue line moves. Earlier events (PAC-3 MSE / THAAD ramp, memory-cost cycle, Beacon Point,
  GE's F414 award, unsigned NVDA / Hugging Face talks) remain rejected on their original grounds.

- **Nine thesis IDs now carry a 2026-09-0x date across three days**; six of those are from
  2026-09-01, produced by three runs against one rolling news window. A reader scanning
  `research_log.md` should not read nine IDs as nine days of work.

- **`alerts.md` remains empty — zero incidents, nothing SYSTEMIC, nothing unresolved.** Selftest
  passed all five checks this run. No alert was raised and none was warranted. The
  `TRADING_ENABLED: false` incident previously reported via ClickUp task `86bbrna9n` remains
  resolved. **No circuit-breaker alert was sent, and none was due** — nothing has ever closed, so
  the streak cannot have moved.

- **Cleared from carry-forward this run:** the fill-sizing detail from the 09:36 bootstrap block
  (resolved — condensed; the audit record lives in `trade_log.md` and `positions.md`), and the
  09:36 post-fill sleeve snapshot (superseded by the 12:35 read above). All research
  carry-forward is retained because the funnel is rolling and the same names will recur.
  **Next run is the 16:00-ET close (4-market-close-journal); its high-water pass still has no
  subject, and it should say so rather than assume it carried.**
