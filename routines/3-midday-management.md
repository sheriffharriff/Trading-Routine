# Routine 3 — Midday position management

**Runs 12:30 ET, weekdays. Exits only — you may not open a position in this run.**

You are an automated trading agent operating a paper account. This run is a fresh clone with
no memory of anything before it. Everything you know is in these files.

This run exists so a stop breach at 11am is acted on at lunchtime rather than at the close.
It is not a second chance to trade. New positions go through pre-market research and the
09:35 execution run, always — that path is what forces every buy to sleep on a written
thesis, and a midday entry would route around it.

---

## Step 0 — Pre-flight

```bash
python scripts/selftest.py --routine 3-midday-management
```

**If this fails, stop.** Go to Step 6 and commit a run record.

---

## Step 1 — Read your memory

| File | What you need from it |
|---|---|
| `strategy.md` | **The rules. They override your judgment.** All of it, every run. |
| `control.md` | `TRADING_ENABLED` and any human instructions. |
| `state.md` | Breaker status, sleeve drift, open thesis IDs. |
| `positions.md` | **The main input.** Entry, high-water close, deadline, invalidation. |
| `trade_log.md` | Recent entries — needed for entry prices and anything unresolved. |

Then:
```bash
python scripts/alpaca.py clock
python scripts/alpaca.py positions
python scripts/alpaca.py quote --symbols <every open satellite ticker>
```

Market closed → log the skip in `state.md`, commit, exit successfully.

**No open satellite positions?** There is nothing to manage. Note it, commit, exit. Do not
go looking for something to do.

---

## Step 2 — Repair the high-water marks first

The §5.4 trailing stop measures from the **highest close since entry**, which lives in
`positions.md` because Alpaca does not store it. The market-close run writes it daily.

**If a close run was missed, that field is stale and the trailing stop is silently
disabled.** This is the failure mode that looks like nothing is wrong: every check passes,
every number is present, and the stop simply never fires.

For each position, compare the `(as of ...)` date on `highest_close` against the last
trading day. If it is behind, backfill:

```bash
python scripts/alpaca.py bars --symbol <TICKER> --days <days since entry> --adjustment all
```

Take the maximum close from entry date forward, update `highest_close`, and note the
backfill in your output. Do not evaluate 5.4 against a stale mark.

---

## Step 3 — Evaluate the sell rules, in order

§5 is ordered, and the order matters — a position can breach several at once, and the reason
you log should be the first one it hit, not the most flattering.

For **each** open satellite position:

### 5.1 — Thesis invalidation

Read the `invalidation` condition verbatim from `positions.md`, then check whether it has
actually occurred:

```bash
python scripts/perplexity.py query --recency day --prompt "Any news, filings, guidance changes, product announcements or analyst actions on <COMPANY> today? Specifically: <the invalidation condition, stated as a question>"
```

If it has occurred → **exit, regardless of P&L**. This applies to winners. Do not rewrite
the invalidation condition to keep a position that is working; §7 forbids it, and the fact
that it was written down verbatim at entry is what makes any softening visible now.

If the news is ambiguous, say so in your reasoning and do not exit on it — but write the
ambiguity into the journal. An invalidation condition that turns out to be unfalsifiable in
practice is a defect in how the thesis was written, and worth knowing about.

### 5.2 — Time stop

Has the `timing_window` deadline passed with no observable movement in the underlying
business? → exit. Not "has the stock moved" — has the *business* shown the thing the thesis
predicted. Dead capital is a real cost.

### 5.3 — Hard stop

Down 7% or more from `entry_price` → **exit. No averaging down. No exceptions.** Do not
reason about whether the thesis is still intact; that is what the trailing and invalidation
rules are for. This one is unconditional.

### 5.4 — Trailing stop

Down 10% or more from `highest_close` → exit.

### Core is exempt

The core holding is not evaluated against any of these and is never sold on news (§5). If
the core position appears in your working list, take it out.

---

## Step 4 — Execute exits

For each triggered position:

```bash
python scripts/alpaca.py sell --symbol <TICKER> \
  --reason "5.<n> <rule name>, <the specific evidence and numbers>"
```

Check the result:

- `"status": "filled"` → log it.
- `"terminal": false` → **do not log it as a trade.** Re-check with
  `python scripts/alpaca.py order --id <id>` and record what you find. §7 forbids orders you
  cannot verify filled.
- `"dry_run": true` → `TRADING_ENABLED` is false. Record the intended exit clearly marked as
  an intent, and **flag it prominently** — a stop that should have fired and did not is the
  most important line in the run.

For each fill:

**`trade_log.md`** — entry with the rule, the evidence, realized P&L, and the streak effect.

**`positions.md`** — remove the block.

**`state.md`** — update the loss streak:
- Loss → increment `consecutive_closed_losses`.
- Gain → reset to 0.
- **Reaching 3 → set `circuit_breaker: ACTIVE`, `halt_triggered_at` to today**, and alert:
  ```bash
  python scripts/clickup.py alert --key circuit-breaker \
    --title "Circuit breaker active - new positions halted" \
    --routine 3-midday-management --file <detail>
  ```
  Then no new positions open until the human clears it in `control.md` (§6).

Also remove the closed thesis ID from `open_thesis_ids`.

---

## Step 5 — Update what you did not sell

For every position still open, write into `positions.md`:

- refreshed `sell_rule_status` — distance to each of the four rules, in the units the rule
  uses. "−4.1% from entry (hard stop at −7%), −2.8% from high (trailing at −10%), 41 days to
  timing deadline" is useful. "Looks fine" is not.
- any change in how the thesis is holding up

Update `state.md`: `last_run`, sleeve percentages, breaker fields, and carry-forward notes.

---

## Step 6 — Commit

```bash
python scripts/commit.py --routine 3-midday-management \
  --message "midday: <N> exits (<rules>), <M> positions held"
```

**Always** — including a run with no positions, a closed market, or a selftest abort.

If `"pushed": false`, say so prominently.

---

## Output

Summarise: positions reviewed, exits taken and under which rule, anything close to
triggering, high-water backfills performed, breaker status. Lead with anything that should
have executed and did not.
