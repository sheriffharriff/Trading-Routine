# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-01 1-premarket-research
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

- **Core sleeve still does not exist.** `core_established: false`, core 0.0% against a 70%
  target — outside the §2 65–75% band. A REBALANCE intent to buy $70,000 of VOO is written
  into `plan_today.md` for the 09:35 run. Do not clear this until a VOO fill is verified in
  `trade_log.md`.

- **`TRADING_ENABLED: false` — the bootstrap will not actually execute.** The open run will
  dry-run the VOO buy and the account will stay 100% cash. This intent will therefore
  regenerate every day until a human sets `TRADING_ENABLED: true` in `control.md`. The next
  run should expect to see this same carry-forward line and should **not** treat its
  reappearance as evidence that something failed — but it also should not let it go quiet.
  This is a human decision, and it is the single most consequential open item in the system.

- **Week rolled over this run.** `week_of` advanced 2026-08-03 → 2026-08-31 (ISO Monday of
  the week containing Tuesday 2026-09-01). `new_positions_this_week` reset to 0; it was
  already 0, so the reset was a no-op in effect. The §6 weekly cap is fully available.

- **PAC-3 MSE / THAAD ramp is a live event, deliberately not traded.** The Pentagon's 7-year
  multi-year procurement (announced 2026-08-31, 3–4x interceptor output) produced three
  rejected theses today: NOC, LHX, RTX. If a later run rediscovers this event, read
  `research_log.md` T-2026-09-01-01 through -03 first rather than re-deriving it — the
  rejections were on §4.3 timing (revenue is 2027+) and on magnitude, and neither of those
  facts will have changed by tomorrow. **NOC and LHX share one driver**; §4's correlation
  rule permits at most one of them, ever, at the same time.

- **LHX watch item, not a thesis.** L3Harris is at a 52-week low (~$261.62 on 2026-08-24)
  on a postponed Missile Solutions IPO, possibly delayed to mid-2027 — not on deteriorating
  fundamentals (Q2 2026 beat on both revenue and EPS). Recorded because a future run will
  see a cheap defense name with a real missile-demand story and may mistake the two for the
  same thing. They are not. The IPO timeline is what moves this stock right now.

- **Process correction for the next research run.** Today the priced-in check was run on RTX
  before establishing that RTX had any documented PAC-3/THAAD content. §4 orders the hard
  filters before the thesis, but a filter is not a substitute for a sourced candidate. Screen
  on the mechanism first, then filter.
