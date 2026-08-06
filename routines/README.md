# Routines

Five scheduled cloud runs. Each is a fresh clone of this repo, runs with no conversation
history, and is destroyed afterward. The prompt file *is* the entire input.

## Schedule

All times **US/Eastern**. Cron in UTC shifts with DST — if your scheduler does not support a
timezone, remember these move by an hour in March and November.

| # | Prompt | Time | Days | Trades? |
|---|---|---|---|---|
| 1 | `1-premarket-research.md` | 08:00 | Mon–Fri | No |
| 2 | `2-market-open-execution.md` | **09:35** | Mon–Fri | **Yes** |
| 3 | `3-midday-management.md` | 12:30 | Mon–Fri | Exits only |
| 4 | `4-market-close-journal.md` | 16:15 | Mon–Fri | No |
| 5 | `5-friday-weekly-review.md` | 16:45 | **Fri** | No |

09:35, not 09:30 — the opening auction produces spreads that make market orders expensive.

16:15, not 16:00 — closing marks need to settle. On early-close days routines 4 and 5 still
run at their normal times.

Every routine calls `/v2/clock` first. On a holiday it logs the skip, commits, and exits 0.
A closed market is not an error.

## Why the work is split this way

**Research and execution are separate runs on purpose.** Routine 1 writes theses and a plan;
routine 2 executes it the next morning. Nothing gets bought that was not written down before
the bell. That gap is the main structural defence against talking yourself into a position
at the moment you are able to act on it.

**Routine 2 refuses a plan not dated today.** If routine 1 failed or never fired, yesterday's
intents are stale research being executed as though fresh — the candidate has had another
session to move, and the priced-in check that cleared it ran against prices that no longer
exist. Core bootstrap and rebalance still proceed; neither depends on the day's research.

**Routine 3 is exits only.** A midday entry would route around the cooling-off period. Exits
have no such problem: a stop that should fire at 11am should not wait until 16:15.

**Routine 4 does the invisible work.** It writes each position's closing price into the
high-water marks that the trailing stop depends on. Miss it and §5.4 silently stops
working — every field still populated, every check still passing, the stop simply never
firing. Routine 3 backfills from daily bars when it detects a stale mark.

## Any run can be skipped without corrupting state

The system is built so a failed or missed run degrades rather than breaks:

- **Weekly position counter** resets off the ISO-week anchor, checked by every routine — not
  off the Friday review having run.
- **Trailing-stop high-water marks** backfill from daily bars when stale.
- **Circuit breaker** persists in `state.md` and clears only on a `HALT_CLEARED_AT` in
  `control.md` dated later than the trigger, so a stale clearance date cannot pre-clear a
  future halt.
- **Every run commits**, including holidays, no-trade days and aborted selftests, so a gap in
  the git history means a run genuinely never fired.

## Running one by hand

```
/replay 2
```

Runs the full logic with no orders and no commit. Check `TRADING_ENABLED` in `control.md`
first — with it set to `true`, a replay of routine 2 will place real paper orders.
