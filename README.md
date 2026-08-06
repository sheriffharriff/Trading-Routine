# Trading Routine

An automated swing-trading agent running as five scheduled Claude Code cloud routines against
an Alpaca **paper** account.

The strategy is second-order catalyst trading: news breaks about Company A, and the agent
looks for Company B whose economics improve because of it. A 70% core index sleeve, a 30%
satellite sleeve of news-driven single names, and a set of hard rules the agent is not
permitted to talk itself out of.

`strategy.md` is the rulebook. It overrides everything, including the agent's own reasoning.

---

## The constraint everything is built around

Each routine run is a **fresh clone of this repo**, runs in the cloud with no conversation
history, and is destroyed when it finishes.

That means:

- The agent starts every run knowing nothing except what is in these files.
- Every run must commit and push, or the next run starts blind.
- Anything that must survive has to be committed markdown. There is nowhere else.

Three of the strategy's rules need state that Alpaca does not store, so they live in files
and would silently stop working if those files went stale:

| Rule | What has to be remembered |
|---|---|
| §5.4 trailing stop, −10% from highest close | The high-water mark. Alpaca has no such field. |
| §6 max 3 new positions per week | A week boundary that survives a missed Friday run. |
| §6 circuit breaker after 3 losses | The loss streak, and whether a human has cleared it. |

---

## Layout

```
strategy.md         HUMAN-OWNED. The rulebook. The agent reads it every run, never writes it.
control.md          HUMAN-OWNED. Live steering: TRADING_ENABLED, halt clearance, notes.

state.md            The run-to-run state machine. Rewritten every run.
positions.md        Satellite ledger: thesis, high-water close, deadline, invalidation, driver.
plan_today.md       Pre-market -> market-open handoff. plan_date is enforced.
research_log.md     Every thesis, accepted and rejected.
trade_log.md        Every order, after it reached a terminal state.
journal.md          Daily narrative from the close run.
weekly_review.md    Friday performance review.
alerts.md           Operational incident ledger.
archive/            Monthly rollover of the growing logs.

routines/           The five prompt files, one per scheduled run. Start here.
scripts/            Stdlib-only Python helpers. All guardrails live here.
.claude/            trading-ops skill + /status /halt /resume /replay commands.
```

---

## Guardrails are code, not prose

A prompt is an instruction a model can reason its way around on a bad day. An exit code is
not. `scripts/alpaca.py buy` refuses to submit an order if:

- the thesis ID is missing or absent from `research_log.md` (§7)
- `--asset-type` is missing — §3 has two eligibility tests and neither can be inferred
- a stock's market cap is missing, unparseable, or below $10B (§3)
- the symbol is leveraged, inverse, crypto-tracking, or not US equity (§3)
- the notional exceeds 5% of account equity, or three positions are already open this
  week (§6)
- the circuit breaker is active (§7)
- `--core` is used on anything but the designated core ticker
- `ALPACA_BASE_URL` is not a paper endpoint

**One honest limitation:** the market-cap figure comes from the agent's own research, so the
floor is an enforced *attestation*. The script catches a missing or below-floor number, never
a wrong one. `market_cap_source` in `trade_log.md` is what makes it auditable afterwards.

---

## Credentials

Six environment variables, supplied by the cloud environment. Never a `.env`, never
hardcoded, never committed.

```
ALPACA_API_KEY_ID
ALPACA_API_SECRET_KEY
ALPACA_BASE_URL          # paper endpoint; a non-paper host is refused
PERPLEXITY_API_KEY
CLICKUP_API_TOKEN
CLICKUP_LIST_ID
```

`scripts/selftest.py` verifies all six and pings all three APIs. Every routine runs it first
and aborts on failure — a run on a partial credential set produces research with no theses,
which reads exactly like a legitimate quiet day.

---

## Human controls

| | |
|---|---|
| `/status` | Positions, sleeve drift, breaker, distance to every sell rule. Read-only. |
| `/halt` | Stop trading. Does **not** close positions or enable stops to fire. |
| `/resume` | Re-enable trading and/or clear a §6 circuit-breaker halt. |
| `/replay 2` | Dry-run a routine: full logic, no orders, no commit. |

You steer the agent by editing `control.md`. The agent is forbidden from writing that file
and `strategy.md`; `scripts/commit.py` reverts any change to them, commits the rest of the
run's work, and reports the violation to ClickUp. A repeat violation on the same file is
escalated as a systemic prompt bug rather than logged again.

**Dry-run first.** Set `TRADING_ENABLED: false` in `control.md` and let it run for a week.
Everything happens except order submission, so you can read a week of theses and intended
trades before it touches the account.

---

## Reporting

One ClickUp task per trading day, plus a separate task for the Friday review, in
`CLICKUP_LIST_ID`. Operational problems post `[ALERT]`-prefixed tasks, deduplicated to one
task per incident: `push-failure`, `guard-violation`, `selftest-abort`, `circuit-breaker`.

Push failures alert to ClickUp specifically because it is the only channel that survives a
failed push — the run's own files are in the repo that could not be written.

---

## What this is not

Paper trading only. No backtesting. No options, futures, margin, leverage, or crypto — §3
bans them permanently and the buy script enforces it.
