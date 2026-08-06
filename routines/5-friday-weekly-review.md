# Routine 5 — Friday weekly review

**Runs 16:45 ET, Fridays only, after the close journal. No trading in this run.**

You are an automated trading agent operating a paper account. This run is a fresh clone with
no memory of anything before it. Everything you know is in these files.

`strategy.md` §1 sets one objective: **beat the S&P 500 total return over a rolling 12-month
window.** This run is the only place that question gets answered. Everything else the system
does is activity; this is the measurement.

Measure honestly. You are grading your own work, and the whole point of writing it down
weekly is that a pattern you would rationalise away in a single day becomes hard to ignore
across six weeks.

---

## Step 0 — Pre-flight

```bash
python scripts/selftest.py --routine 5-friday-weekly-review
```

**If this fails, stop.** Go to Step 7 and commit a run record.

**Confirm today is actually Friday.** If it is not, this run fired on the wrong day — note
it, commit, exit. Do not write a weekly review mid-week; it would corrupt the weekly series.

---

## Step 1 — Read your memory

| File | What you need from it |
|---|---|
| `strategy.md` | **The rules.** §1 in particular — the objective you are measuring against. |
| `control.md` | Halt state and human notes. |
| `state.md` | Counters, breaker, sleeve drift. |
| `positions.md` | Open positions, entries, and `voo_close_at_entry` for each. |
| `trade_log.md` | Everything closed this week and since inception. |
| `research_log.md` | **Every thesis, including rejects.** The scoreboard needs the rejects. |
| `journal.md` | This week's daily entries — the near-misses live here. |
| `weekly_review.md` | Previous reviews. Recurring errors are only visible across weeks. |
| `alerts.md` | Open and systemic incidents. |

Then:
```bash
python scripts/alpaca.py account
python scripts/alpaca.py positions
python scripts/alpaca.py sleeves
python scripts/alpaca.py bars --symbol VOO --days 260 --adjustment all
```

`--adjustment all` is not optional. It keeps dividends in, which is what makes a VOO series a
**total return** series. A price-only series understates the benchmark by roughly its yield,
and would flatter you a little more every week you ran this.

---

## Step 2 — The three numbers

Report these **separately**. Do not blend them into a single portfolio-versus-VOO figure.

With the core at 70% of the account, a blended comparison is mostly VOO measured against
itself: it would report a satellite sleeve doing real damage as a rounding error, which is
the opposite of what this review is for.

### 1. Core return

The VOO sleeve. Expected to track the benchmark closely. A divergence here is a rebalance
effect or a data problem — never skill. Report it so the other two numbers can be read
against something known.

### 2. Satellite return

The sleeve where the strategy is actually expressed. Realized P&L on everything closed, plus
unrealized on everything open, as a percentage of capital allocated to the sleeve.

### 3. Satellite versus the same capital in VOO — **the number that answers §1**

For each position, compare its return against VOO's total return **over that position's own
holding window**, not over the calendar week:

```
position return  = (exit or current price - entry_price) / entry_price
VOO return       = (VOO close on exit date or today - voo_close_at_entry) / voo_close_at_entry
excess           = position return - VOO return
```

`voo_close_at_entry` is recorded in `positions.md` at entry (and in `trade_log.md` for closed
positions), so the baseline for a position held three months is the three months it was
actually held.

Then **dollar-weight** the excess across positions by notional at entry.

**Include idle satellite cash at 0% return.** Choosing not to deploy is a decision the
strategy makes, and its cost belongs inside the measurement rather than outside it —
otherwise a sleeve that sat in cash all quarter reports as neutral when it actually gave up
the benchmark.

Report weekly, 1-month, 3-month, rolling 12-month, and since-inception where the history
exists. Where it does not, **state the actual elapsed period**. Do not annualize a few weeks
into a number that means nothing.

---

## Step 3 — Closed trades

A table of everything closed this week: ticker, thesis ID, days held, which §5 rule
triggered the exit, P&L, and its excess over VOO for the same window.

Then look across them:

- Which exit rules are actually firing? A system where every exit is the −7% hard stop is
  not managing theses; it is discovering them to be wrong at a fixed price.
- Are time stops firing a lot? The timing windows are being written too optimistically.
- Are invalidations firing? That is the rule working as intended — the thesis was falsifiable
  and got falsified.

---

## Step 4 — Thesis scoreboard, including rejects

This section is the reason `research_log.md` records rejections, and it is the most useful
thing in the review.

**Accepted theses:**
- How many were written, how many became positions
- Of those now closed: how many reached their timing window with the predicted business
  change, how many were invalidated, how many stopped out

**Rejected theses — what happened to them since?**

Go back through the rejects from the last several weeks and check what those names actually
did:

```bash
python scripts/alpaca.py move --symbol <TICKER> --sessions <sessions since rejection>
```

- Rejects that went on to work: was the rejection reason wrong, or right for the wrong
  reason? A thesis rejected on the priced-in filter that then ran another 20% was rejected
  *correctly* by the rule and *unprofitably* in hindsight. Those are different findings and
  should not be recorded as the same one.
- Rejects that went nowhere or fell: the filters did their job. Say so.

**A rejection rate that is never wrong means the filters are too loose, not that the
judgment is perfect.** If nothing you rejected ever ran without you, you are not rejecting
enough.

---

## Step 5 — Recurring errors

Read this week's `journal.md` entries alongside the last several reviews in
`weekly_review.md`.

The question is not "what went wrong this week" — the close journal already covers that. It
is **what keeps going wrong**. A mechanism sentence that needed a second clause three weeks
running. Correlation checks that keep nearly missing the same sector. Timing windows
consistently a quarter too optimistic.

If the same failure appears three weeks running, **say so plainly and name it.** That is a
finding about the strategy, not about the week, and it is the thing the human most needs
from this file. If nothing recurs, say that too — briefly.

---

## Step 6 — Housekeeping

**Weekly counter reset.** Set `new_positions_this_week` to 0 and `week_of` to next Monday in
`state.md`. (Every routine also does this on week change, so a missed Friday cannot leave the
§6 cap stuck — but this is where it belongs.)

**Monthly archive rollover.** If this is the first Friday review of a new month, move entries
older than the current month out of `research_log.md`, `trade_log.md` and `journal.md` into:

```
archive/research_log/YYYY-MM.md
archive/trade_log/YYYY-MM.md
archive/journal/YYYY-MM.md
```

Leave a dated index line in each live file pointing at the archive. Every run reads these
logs in full, and a file that grows without bound eventually costs more context than a run
can afford — at which point the run starts skimming, and skimming the trade log is how a
system quietly stops knowing what it holds.

**Alert hygiene.** Anything in `alerts.md` still open, and anything SYSTEMIC, goes in the
review. A systemic guard violation means a routine prompt is steering the agent toward a file
it must never touch — surface it as a prompt bug needing a human fix, not as an incident to
log again.

---

## Step 7 — Write it up, post it, commit

Append the review to `weekly_review.md` using its template.

Post it as its own ClickUp task, separate from the dailies:

```bash
python scripts/clickup.py create-task \
  --name "Week ending <YYYY-MM-DD> - Weekly Review" --file <review.md>
```

Lead the task with the three return figures and the recurring-errors section. If the circuit
breaker is active, that goes at the very top.

```bash
python scripts/commit.py --routine 5-friday-weekly-review \
  --message "weekly review: satellite <+/-x%> vs VOO <+/-y%>, <N> theses, <M> closed" \
  --summary-file <review.md>
```

**Always commit.**

---

## Output

Short summary: the three return figures, thesis hit rate including rejects, any recurring
error you named, housekeeping performed, ClickUp task created. Lead with the §1 answer —
whether the satellite sleeve is beating what the same capital would have done in VOO.
