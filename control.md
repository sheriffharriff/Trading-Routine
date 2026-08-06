# Control

**HUMAN-OWNED FILE. The agent reads this every run and must never write to it.**
`scripts/commit.py` enforces that in code — a run that modifies this file has the
change reverted before it can be committed.

This is the live steering wheel. `strategy.md` is the permanent rulebook; this file
is where you change things day to day without touching it.

---

## Settings

The block below is parsed by `scripts/common.py`. Keep the `KEY: value` format exactly.

```
TRADING_ENABLED: false
HALT_CLEARED_AT: none
```

**`TRADING_ENABLED`**
- `true` — orders are submitted for real against the paper account.
- `false` — full dry run. Every routine runs its complete logic and writes every file,
  but `alpaca.py buy` / `sell` print the intended order and submit nothing. Use this to
  watch the system think for a week before it touches the account.

If this file is missing or unreadable, the scripts treat trading as **disabled**. A
missing control file means something is wrong, and the safe direction is not to trade.

**`HALT_CLEARED_AT`**
`none`, or a date in `YYYY-MM-DD` form.

`strategy.md` §6 halts new positions after three consecutive closed losses, and says the
halt lifts only when the human clears it. This is where you clear it.

The date must be **later than** the `halt_triggered_at` date recorded in `state.md`. A
clearance date that predates the halt does nothing. That is deliberate: without the
comparison, a date left in this file from months ago would silently auto-clear the *next*
halt the moment it triggered, which would void §6 without anyone noticing.

To clear a halt: set this to today's date. To re-arm, set it back to `none`.

---

## Notes

Free-text instructions for the agent. It reads these every run and must honor them.
They sit below `strategy.md` in priority — these can restrict what the agent does, never
permit something the strategy forbids.

- (none)
