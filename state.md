# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-03 08:27 ET 1-premarket-research
week_of: 2026-08-31
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: false
core_ticker: VOO
core_pct: 0.0
satellite_pct: 0.0
cash_pct: 100.0
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


- **⚠ TRADING IS LIVE AS OF TODAY — this is the single most important line in this file, and it
  overrides every "dry run" statement in the run history below it.** The human set
  `TRADING_ENABLED: true` in `control.md` at 21:08 PT on 2026-09-02 (commit `1005b1e`, "Enable
  trading"), i.e. 00:08 ET on 2026-09-03. Today's selftest confirms it:
  `"control": "control.md ok - LIVE (paper account)"`, `"trading_enabled": true`, all five checks
  passed. **Every run in this repo's history before today was a dry run; runs from here are not.**
  `alpaca.py buy` and `sell` now submit real orders against the paper account instead of printing
  an intent and returning `"dry_run": true`. **The three-day-old carry-forward complaint about an
  all-cash book is resolved and has been deleted, not carried** — the human acted on it. Do not
  re-raise it, and do not let a run pattern-match on the three previous open runs that got
  `"dry_run": true` back from the identical bootstrap command.

- **The §2 core bootstrap is today's whole plan, it is a REAL ~$70,000 order, and the bootstrap
  and the rebalance are ONE action.** `core_established: false`, core 0.0% against a 70% target,
  outside the §2 65–75% band (`core_in_band: false`, `rebalance_needed: true`,
  `rebalance_delta: 70000.0` — unchanged across every run since 2026-09-01 00:48 ET). Step 3's
  bootstrap and Step 7's rebalance are **the same VOO buy**; three previous open runs each
  correctly submitted it once, and today submitting twice would cost real money. **Size to 70% of
  live equity at the open, not to the $70,000 written in the plan** — if equity has moved, the
  target moves. **New today: verification actually matters.** `buy` polls to a terminal state; if
  `"terminal": false`, do not write a fill — re-check with `alpaca.py order --id <id>` and log
  what is there (§7). Do not clear this line until a VOO fill is verified in `trade_log.md` →
  *Entries*. Reference: VOO closed **703.34** on 2026-09-02, +0.457% from 700.14.

- **⚠ After today's fill, `positions.md` will legitimately disagree with the broker — this is not
  a discrepancy.** The core holding is deliberately **not** tracked in `positions.md` (§5 exempts
  it from all four sell rules, so it has no thesis, deadline or high-water mark). Expect
  `alpaca.py positions` to return one VOO row while that ledger still reads *(none)*. Every
  reconciliation note written so far asserted that an empty ledger matching an empty broker was
  the check passing; the first run to see one position against an empty ledger must not read that
  as a broken ledger. The check that matters from tomorrow is **satellite** positions against
  satellite blocks.

- **The §5.4 trailing stop is still not armed, and today's core buy does not arm it.** Zero
  satellite position blocks means zero `highest_close` fields and zero `(as of ...)` dates — there
  was nothing to write and nothing to stamp, and a `bars` backfill has no input. **Not silently
  disabled; not yet armed.** It arms the day the first *satellite* position opens, which is not
  today. Eleven runs across three trading days have each recorded this distinction rather than
  assume it carried. The near-miss noted in the 2026-09-02 journal still stands: the pass now
  feels ceremonial, and the first day it matters is the day after the first satellite fill.

- **Week rollover checked this run: none due.** ISO Monday of 2026-09-03 (Thursday) is
  **2026-08-31**, which matches `week_of`. `new_positions_this_week` stays 0 — the §6 weekly cap
  is fully available at 0 of 3. Breaker INACTIVE, `consecutive_closed_losses: 0`,
  `halt_triggered_at: none`; only a **closed** position can move the streak and nothing has ever
  opened. `HALT_CLEARED_AT: none` in `control.md`, correct and irrelevant while no halt exists.
  **The next week boundary is 2026-09-07** — re-check against ISO Monday every run rather than
  inheriting this line.

- **⚠ LITE / the priced-in filter — the hypothetical from 2026-09-02 became real today, and it is
  a decision waiting on the human.** T-2026-09-03-01 (Lumentum) produced **the best-sourced part 1
  in this log**: Morgan Stanley names LITE as a key **pump-laser** supplier to a Ciena that is
  explicitly "supply-constrained… particularly pump lasers," against a Ciena Q3 that grew revenue
  37% y/y and raised FY guidance. It was rejected because `move --sessions 5` returned **−7.35%**,
  `priced_in: true`. **That is a drawdown, not a run-up** — CIEN itself is −12.25% over the same
  window on a beat-and-raise, so the five-session decline brackets Broadcom's weak guidance and a
  broad AI-optics selloff rather than the market pricing in Ciena's quarter. Yesterday's log
  predicted exactly this ("a legitimate candidate that fell 5% on unrelated news would be
  blocked"); today it cost a candidate. **I did not reinterpret the filter and no future run
  should** — §4 is a veto, a veto that over-fires is the safe direction, and the fix is a human
  editing §4 or `alpaca.py move`, not a run deciding at 08:00 that the rule does not mean what it
  says. **LITE is not "wait for a better entry": it failed for having already fallen, so a further
  decline makes the reading worse.** There is no price at which the rejection flips.

- **⚠ Do not reach for COHR, CIEN, AVGO, CSCO, AAOI, GLW, APH, NOK, ERIC or ANET on the strength
  of the Ciena story.** The sourced screen named **only Lumentum** as a Ciena supplier. Every
  other name appears in the retrieved material as an ecosystem read-through with no sourced
  supplier relationship — buying one would be the RTX failure exactly. If AI-optics ever becomes a
  live driver, note that **LITE, COHR and CIEN would share it** and §4's correlation rule permits
  at most one.

- **The scoreboard, updated — the priced-in filter has still never been informative.** Across nine
  worked candidates, **seven passed the filter and failed the thesis** (NOC, LHX×2, WDC, AEP, RTX,
  and HPE which died at part 1) and **two passed the thesis and failed the filter (MU, LITE)**.
  Treat a passing priced-in check as a veto that did not fire, never as encouragement — "has not
  moved" and "should have moved but didn't" are the same number.

- **⚠ STANDING RULES — four, sharing one root cause.**
  (i) *Screen on the mechanism before running filters* (from RTX — a filter is not a substitute
  for a sourced candidate). (ii) *Verify what the company currently sells, post-spin* (from WDC).
  (iii) *Verify the news is new to the company's own disclosure* (from AEP — if management has
  already guided the pipeline the contract falls inside, the deal illustrates guidance rather than
  changing it). (iv) *A recurring ticker is a warning, not corroboration* (from LHX).

- **LHX: no longer today's most dangerous name, but the rule it produced still stands.** It did
  not appear in today's funnel at all, through any driver. It surfaced on 2026-09-01 and 09-02
  through two separately sourced drivers and died on §4.3 timing then §4.2 magnitude (0.58% of
  revenue). Its absence today is the standing rule working as intended, not a reason to relax it.

- **MU: not re-checked, second consecutive day, and the reason is again absence of evidence rather
  than resolve.** No source across today's four queries named Micron or any memory supplier in
  connection with any of today's events. **The correct reason not to re-check a rejected candidate
  is that today's evidence does not produce it.** If a future funnel surfaces it from a source,
  re-running the filter and re-testing the timing window from that day's date is legitimate.

- **The "Company A's print implies Company B's print" failure did not recur today, and it was
  actively screened for.** Broadcom's weak guidance was the obvious vehicle ("AVGO guides soft, so
  a competitor is taking share") and the dedicated screen came back explicitly empty — no source
  names any company whose revenue or costs change. Two prior instances stand on the record: SAIC →
  LDOS/CACI/BAH (2026-09-01) and Dell → HPE (2026-09-02). Expect the shape again; it is the most
  fluent sentence available on any given day.

- **Live events examined and deliberately not traded — do not re-derive these.**
  (a) **Ciena FQ3 beat-and-raise** (2026-09-02): LITE is the only sourced second-order name,
  rejected on the priced-in filter, above. (b) **Google adtech no-divestiture ruling** (Judge
  Brinkema, 2026-09-02): only Alphabet named by any source; a status-quo ruling changes no third
  party's revenue line, and the mechanism for a rival runs *against* it — nothing long. (c)
  **Broadcom FQ3 beat, weak guidance**: no Company B, and wrong direction for a long-only book.
  (d) **FuelCell Energy 75 MW Texas capacity reservation + 380 MW Fit Energy agreement**: FCEL is
  Company A and sub-$10B; the counterparties are private (Fit Energy) or unnamed ("a major
  colocation data centre operator"). (e) **KBR / NOAA National Mesonet, $1.1B ceiling over five
  years**: Company A, no sourced subcontractor, and a five-year ceiling is outside §4.3. (f)
  **Studsvik / GE Vernova Hitachi / Samsung C&T, 1.2 GW Swedish nuclear**: "commit to advancing"
  is not an order, non-US, and years from reported results. (g) **Uber's 3,300 layoffs**: an
  internal cost action; a staffing cut does not become another firm's revenue. Earlier events —
  the PAC-3 MSE / THAAD ramp, the memory-cost cycle, the Beacon Point datacentre deal, GE's F414
  award and the unsigned Nvidia / Hugging Face talks — remain rejected on their original grounds
  and none of them reappeared in today's window.

- **Nine thesis IDs now carry a 2026-09-0x date across three days**; six of those are from
  2026-09-01, produced by three runs against one rolling news window. **A reader scanning
  `research_log.md` should not read nine IDs as nine days of work.**

- **`alerts.md` remains empty — zero incidents, nothing SYSTEMIC, nothing unresolved.** Selftest
  passed all five checks. No alert was raised this run and none was warranted. **The standing
  `TRADING_ENABLED: false` condition previously reported via ClickUp task `86bbrna9n` is now
  resolved by the human** and should not be re-alerted or re-reported as open.

- **Cleared from carry-forward this run:** the entire dry-run block and its foregone-return
  arithmetic (resolved — the human enabled trading), and the 2026-09-02 close-run report
  (`positions: []` for the tenth run, ClickUp task `86bbtvf94`, no orders in limbo), which was a
  report about a completed day and tells today nothing it did not re-derive from a live broker
  read. The schedule item is also cleared: this routine has now fired **once per day at ~08:27 ET
  on two consecutive days**, which is the behaviour that was being watched for. The research items
  are carried and updated rather than retired, because today's run produced evidence bearing on
  them.
