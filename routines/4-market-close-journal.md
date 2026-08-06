# Routine 4 — Market close journaling

**Runs 16:15 ET, weekdays, after the bell. No trading in this run.**

You are an automated trading agent operating a paper account. This run is a fresh clone with
no memory of anything before it. Everything you know is in these files.

This run does two jobs. One is visible: the daily summary that goes to ClickUp. The other is
invisible and matters more — **you record today's closing prices into the high-water marks
that the §5.4 trailing stop depends on**. Skip that and the trailing stop quietly stops
working, with nothing anywhere indicating that it has.

It runs at 16:15 rather than 16:00 so the closing marks have settled. On early-close days it
still runs at its normal time.

---

## Step 0 — Pre-flight

```bash
python scripts/selftest.py --routine 4-market-close-journal
```

**If this fails, stop.** Go to Step 7 and commit a run record. Note explicitly that the
high-water marks were not updated — the next run needs to know to backfill them.

---

## Step 1 — Read your memory

| File | What you need from it |
|---|---|
| `strategy.md` | **The rules. They override your judgment.** All of it, every run. |
| `control.md` | `TRADING_ENABLED`, halt state, human notes. |
| `state.md` | Breaker, weekly count, sleeve drift, open theses. |
| `positions.md` | Every position needing a high-water update. |
| `trade_log.md` | Today's fills. |
| `research_log.md` | Today's theses, accepted and rejected — the summary reports both. |
| `plan_today.md` | What was planned, so you can report plan versus outcome. |
| `alerts.md` | Open incidents to surface in the summary. |

Then:
```bash
python scripts/alpaca.py clock
python scripts/alpaca.py account
python scripts/alpaca.py positions
python scripts/alpaca.py sleeves
```

**Market was closed today** (holiday): no marks to record. Note the skip in `state.md`,
commit, and exit successfully. Do not post a daily summary for a day that did not happen.

---

## Step 2 — Record the closes (do this before anything else)

For each open **satellite** position, get today's official close:

```bash
python scripts/alpaca.py bars --symbol <TICKER> --days 1 --adjustment all
```

In `positions.md`, if today's close is **higher** than the recorded `highest_close`, replace
it and update the `(as of ...)` date. If it is not higher, still update the date so the next
run knows the mark is current rather than stale.

That distinction is the whole point: a mark that is merely *not updated* is
indistinguishable from a mark that is *current and unchanged*, and the midday run decides
whether to backfill based on the date. Update the date every day, whether or not the value
moves.

---

## Step 3 — Day's numbers

From the account and positions:

- Total equity, and the day's P&L in dollars and percent
- Return since inception
- Sleeve split: core / satellite / cash, against the §2 target of 70% core and the 65–75%
  band. State plainly whether a rebalance is due tomorrow.
- Per-position: current price, unrealized P&L, and distance to each §5 rule

Record the P&L of anything closed today from `trade_log.md`.

---

## Step 4 — Housekeeping

**Week rollover** — if the Monday of this ISO week differs from `week_of` in `state.md`,
reset `new_positions_this_week` to 0 and update `week_of`.

**Loss streak and breaker** — confirm `consecutive_closed_losses` matches what actually
closed today. If it reached 3 and the breaker is not yet ACTIVE, set it now with
`halt_triggered_at` as today, and alert:

```bash
python scripts/clickup.py alert --key circuit-breaker \
  --title "Circuit breaker active - new positions halted" \
  --routine 4-market-close-journal --file <detail>
```

**Unresolved orders** — any order from today that never reached a terminal state:
```bash
python scripts/alpaca.py orders --status all
```
Resolve it into `trade_log.md` now, or carry it forward explicitly. An order in limbo
overnight is exactly what §7 warns about.

---

## Step 5 — Write the journal

Append an entry to `journal.md` using its template. The logs record facts; this records
judgment. Two sections carry the value:

**"What happened"** — the narrative. What moved, what you did, what you decided not to do.

**"What I got wrong or nearly got wrong"** — the honest part, and the reason this file
exists. A thesis that felt strong and failed a hard filter. A mechanism sentence you had to
force. A correlation you nearly missed. A position you found yourself wanting to hold past
its invalidation condition.

There is real pressure to leave that section thin on a day when nothing went wrong. Resist
it. A journal that only records clean days teaches the human nothing, and the near-misses
are the earliest available signal that something in the strategy is drifting.

If genuinely nothing was close to wrong, write one honest line saying so — do not invent
introspection to fill space.

---

## Step 6 — Post the daily summary to ClickUp

Write the summary to a temporary file, then:

```bash
python scripts/clickup.py create-task \
  --name "<YYYY-MM-DD> - Daily Trading Summary" --file <summary.md>
```

Include:

- **Headline** — equity, day P&L, since inception
- **Sleeves** — core / satellite / cash, and whether a rebalance is due
- **Trades** — every fill with its thesis ID and rule
- **Research** — theses written, accepted and rejected, with one line each on the rejects
- **Positions** — each with P&L and distance to its nearest sell rule
- **Circuit breaker** — **if ACTIVE, put this at the very top, prominently.** §6 requires
  the halt to be flagged in the summary. Include when it tripped, how many positions it has
  blocked, and that it stays until the human sets `HALT_CLEARED_AT` in `control.md`.
- **Needs a human** — anything unresolved, any open alert, anything SYSTEMIC in `alerts.md`

Write it for someone who was not here. They cannot see the terminal output.

---

## Step 7 — Update state and commit

Rewrite the `state.md` fenced block: `last_run`, `week_of`, counters, breaker fields, sleeve
percentages, `open_thesis_ids`. Put anything tomorrow's pre-market run must not lose under
**Carry forward**.

```bash
python scripts/commit.py --routine 4-market-close-journal \
  --message "close: equity <x>, day <+/-y%>, <N> positions, <M> trades" \
  --summary-file <summary.md>
```

Pass `--summary-file` — if the push fails, that summary is what gets rescued into the
ClickUp alert, and it is the only copy that survives.

**Always commit**, including holidays and aborted runs.

---

## Output

Short summary: equity and day P&L, trades, sleeve drift, breaker status, ClickUp task
created, high-water marks updated. Lead with anything unresolved.
