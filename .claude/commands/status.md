---
description: Show account status — positions, sleeve drift, circuit breaker, open theses, and anything near a sell rule.
---

Give me a read on the trading system right now. Do not trade, do not commit, do not modify
any file — this is read-only.

1. Run `python scripts/selftest.py --routine manual-status --no-alert`. If it fails, report
   what is broken and stop; nothing below will be trustworthy.

2. Gather:
   - `python scripts/alpaca.py sleeves`
   - `python scripts/alpaca.py positions`
   - `python scripts/alpaca.py clock`

3. Read `state.md`, `positions.md`, `control.md`, and `alerts.md`.

4. Report, compactly:

   **Account** — equity, cash, day P&L if available.

   **Sleeves** — core / satellite / cash as percentages, against the §2 target of 70% core
   and the 65–75% rebalance band. Say plainly whether a rebalance is due.

   **Positions** — one line each: ticker, thesis ID, entry, current, P&L%, and **distance to
   each of the four §5 sell rules**. Flag anything within 2 percentage points of the hard
   stop or the trailing stop. The trailing stop is measured from `highest_close` in
   `positions.md`, not from the entry price.

   **Trading state** — `TRADING_ENABLED`, circuit breaker status (and, if active, whether
   `HALT_CLEARED_AT` would clear it), positions opened this week against the §6 cap of 3.

   **Open alerts** — anything in `alerts.md` not resolved, especially anything SYSTEMIC.

   **Staleness** — when did each routine last run, per `state.md` and the git log? If a
   routine has not run when it should have, say so. A missing close run means the
   trailing-stop high-water marks are stale, which silently disables §5.4.

5. If `positions.md` and the live Alpaca positions disagree, lead with that. Everything else
   in the report is unreliable until it is resolved.

Be direct. If something looks wrong, say it is wrong rather than presenting it neutrally
alongside everything else.
