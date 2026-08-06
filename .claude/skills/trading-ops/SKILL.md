---
name: trading-ops
description: Operating procedure for the automated trading routines — run order, script reference, guardrails, and the commit protocol. Load this at the start of any trading routine run, and whenever working on the routine prompts, the memory files, or the scripts in this repo.
---

# Trading operations

Shared procedure for all five routines. The routine prompt says *what* to do; this says
*how* the system works. If the two disagree, the routine prompt wins — and tell the human,
because that disagreement is a bug in one of them.

`strategy.md` overrides both. It always wins.

---

## The one thing that matters most

**Every run starts blind and ends destroyed.** A fresh clone, no conversation history, no
memory of previous runs. The only continuity is committed markdown.

This has two consequences that shape everything else:

1. **Read the memory files first.** Not skimmed — read. You do not know what you hold,
   what you decided yesterday, or whether trading is halted until you have read them.
2. **Push, or it never happened.** A run that does excellent work and fails to push has
   produced nothing. The next run will not know it happened.

---

## Run order

Every routine follows this sequence. Do not reorder it.

```
0. python scripts/selftest.py --routine <name>     # abort the run on failure
1. Read: strategy.md, control.md, state.md, positions.md, alerts.md
        + the logs relevant to this routine
2. python scripts/alpaca.py clock                  # closed -> log the skip, commit, exit
3. Reconcile: week rollover, state vs live positions
4. Do the routine's actual job
5. Write back to the memory files
6. python scripts/commit.py --routine <name> --message "..."
```

**Step 0 is not optional.** A missing credential produces a run that looks like it worked:
research with no theses reads exactly like a legitimate quiet day. The selftest makes that
failure loud at the start, because nothing downstream will make it visible at the end.

**Step 3, week rollover.** Compare `week_anchor(today)` to `week_of` in `state.md`. If they
differ, reset `new_positions_this_week` to 0 and update `week_of`. Any routine does this —
it must not depend on the Friday run having happened.

---

## Files: who owns what

| File | Owner | Rule |
|---|---|---|
| `strategy.md` | **Human** | Read every run. Never write. Overrides your judgment. |
| `control.md` | **Human** | Read every run. Never write. Live steering + halt clearance. |
| `state.md` | Agent | Rewrite every run. Fenced block is machine-parsed. |
| `positions.md` | Agent | Satellite ledger. High-water marks, deadlines, invalidations. |
| `plan_today.md` | Agent | Pre-market writes, market-open consumes. `plan_date` is enforced. |
| `research_log.md` | Agent | Append. Every thesis, **accepted and rejected**. |
| `trade_log.md` | Agent | Append. Only after an order reaches a terminal state. |
| `journal.md` | Agent | Append. Daily narrative from the close routine. |
| `weekly_review.md` | Agent | Append. Friday only. |
| `alerts.md` | Agent | Written by the scripts. Do not hand-edit during a run. |

Writing to `strategy.md` or `control.md` is caught by `commit.py`, reverted, and reported as
an incident. A second attempt on the same file is escalated as a systemic prompt bug. If you
find yourself wanting to edit one of them, the answer is to say so in the run output and let
the human decide.

---

## Scripts

Stdlib-only Python. No installs. Run from the repo root.

```bash
# Market state and account
python scripts/alpaca.py clock
python scripts/alpaca.py account
python scripts/alpaca.py positions
python scripts/alpaca.py sleeves          # core/satellite/cash split + rebalance delta

# Prices
python scripts/alpaca.py quote --symbols NVDA,VRT
python scripts/alpaca.py bars --symbol VOO --days 30 --adjustment all
python scripts/alpaca.py move --symbol VRT --sessions 5     # the priced-in check, mechanised
python scripts/alpaca.py asset --symbol VRT

# Orders
python scripts/alpaca.py buy --symbol VRT --notional 4000 \
    --thesis-id T-2026-08-05-01 --asset-type stock \
    --market-cap 47.2B --market-cap-source "Perplexity: company Q2 filing"
python scripts/alpaca.py buy --symbol VOO --notional 70000 --core
python scripts/alpaca.py sell --symbol VRT --reason "5.3 hard stop, -7.4% from entry"
python scripts/alpaca.py order --id <id>

# Research
python scripts/perplexity.py query --prompt "..." --recency day

# ClickUp
python scripts/clickup.py create-task --name "2026-08-05 - Daily Trading Summary" --file s.md
python scripts/clickup.py alert --key circuit-breaker --title "Circuit breaker active" \
    --file detail.md --routine 4-market-close-journal

# Finish
python scripts/commit.py --routine <name> --message "..." [--summary-file s.md]
```

All of them print JSON and exit non-zero on failure. **Check the exit code.** A `buy` that
fails prints an error and returns 1; treating that as a fill and writing it to `trade_log.md`
puts a position in the ledger that does not exist.

---

## What the scripts enforce, so you do not have to

Guardrails live in code because a prompt is something a model can reason its way around on
a bad day, and an exit code is not. `alpaca.py buy` refuses to submit if:

- the thesis ID is missing, or absent from `research_log.md` (§7)
- `--asset-type` is missing — §3 has two different eligibility tests and neither can be
  inferred: market cap ≥$10B for stocks, ADV >500k for ETFs
- a stock's `--market-cap` is missing, unparseable, or below the floor (§3)
- the symbol is leveraged, inverse, crypto-tracking, or not US equity (§3)
- the notional exceeds 5% of account equity (§6)
- three positions have already been opened this week (§6)
- the circuit breaker is active (§7)
- `--core` is used on anything other than the designated core ticker

**These are a floor, not a ceiling.** The script cannot check whether your thesis is any
good, whether the mechanism sentence needs a second clause, or whether the correlation check
was done honestly. It also cannot tell whether a market cap figure is *correct* — only that
it is present and above the floor. Passing the script's checks is not the same as the trade
being right.

---

## Order verification

§7 forbids placing orders you cannot verify filled. `buy` and `sell` poll to a terminal
state before returning, so the JSON tells you what actually happened.

If `"terminal": false`, the order did not resolve inside the poll window. **Do not write it
to `trade_log.md`.** Re-check with `alpaca.py order --id <id>` and log what you find. An
entry written at submission time records an intention, not a trade.

---

## Dry-run mode

`TRADING_ENABLED: false` in `control.md` makes `buy` and `sell` print the intended order and
submit nothing, returning `"dry_run": true`.

Everything else still runs: research happens, files are written, the commit goes through.
Log the intended trades as intents, clearly marked, and never as fills.

---

## Committing

```bash
python scripts/commit.py --routine <name> --message "<what happened>"
```

Always. Including when nothing happened — a holiday skip, a no-trade day, an aborted
selftest. A silent gap in the git history is indistinguishable from a run that never fired,
and the next run cannot tell the difference either.

`commit.py` stages everything, reverts any change to the human-owned files, commits,
rebases on `origin/main`, and pushes with one retry. Push failure posts a ClickUp alert
carrying the run summary — the only channel that survives a failed push. Pass
`--summary-file` when the run produced something worth rescuing.

---

## Alerts

Four incidents get a ClickUp alert, deduplicated to one task each:
`push-failure`, `guard-violation:<file>`, `selftest-abort`, `circuit-breaker`.

Titles must be **stable** across runs — no dates or counts inside `--title`, since that
string is the dedupe key. A persisting condition comments on the existing task instead of
creating a new one.

---

## Tone in the logs

The logs are how a human finds out what the system keeps getting wrong. That only works if
they are honest.

Write down the theses you rejected and why. Write down the ones that felt strong and were
not. When a hard filter catches something you had already talked yourself into, say so —
that is the single most useful line in the whole log, and it is the one there is the most
pressure to leave out.

§4 is explicit that most research runs should end in no trade. A day with nothing to do is
a successful day. Do not manufacture activity, and do not write the log as though activity
were the goal.
