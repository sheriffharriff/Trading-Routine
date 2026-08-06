---
description: Resume trading — re-enable TRADING_ENABLED and/or clear a §6 circuit-breaker halt.
---

Resume trading. There are two separate things this can mean, and they are not the same
switch. Work out which the user wants before changing anything.

1. Read `control.md` and `state.md`, then report the current position:
   - `TRADING_ENABLED` — the manual on/off switch.
   - `circuit_breaker` in `state.md` and its `halt_triggered_at` — the §6 automatic halt
     after three consecutive closed losses.

   Either one alone is enough to stop new positions. Clearing one while the other is still
   set will look like nothing happened.

2. **If `TRADING_ENABLED` is false**, set it to `true`.

3. **If the circuit breaker is ACTIVE**, clearing it requires `HALT_CLEARED_AT` in
   `control.md` to be a date **strictly later** than `halt_triggered_at` in `state.md`.
   Setting today's date does that in every normal case. Do not edit `state.md` to clear a
   halt — that is the agent's own record of what happened, and overwriting it destroys the
   evidence of why the breaker tripped.

   Before doing this, push back once. §6 exists because three consecutive losses is
   evidence the strategy is misfiring, and the halt is meant to force a look at *why*
   before more capital goes in. Ask whether the last three closed positions have actually
   been reviewed — they are in `trade_log.md` and `weekly_review.md`. If the user says
   proceed, proceed; it is their call and their account.

4. Add a dated note under `## Notes` recording what was resumed and why.

5. Confirm what changed and what will happen on the next run: new positions become possible
   again, subject to the §6 weekly cap of 3 (report how many have been opened this week).

6. Do not commit unless asked. If asked, commit `control.md` directly with git — **not**
   `scripts/commit.py`, which reverts changes to that file by design.
