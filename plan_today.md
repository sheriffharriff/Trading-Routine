# Today's Plan

**AGENT-OWNED. Written by the pre-market routine, consumed by the market-open routine,
overwritten daily.**

This file is the handoff between the two runs. The pre-market run does the thinking and
writes intents here; the market-open run executes them. Nothing gets bought that was not
written here first, which is what forces every buy to sleep on a written thesis instead of
being reasoned into existence at the moment of execution.

The market-open run **re-validates every intent against fresh quotes before acting**. An
intent written at 08:00 can be dead by 09:35 — an overnight gap can push a candidate past
the §4 4%-in-five-sessions priced-in threshold, in which case the trade is skipped and the
skip is logged. A stale intent is a proposal, not an instruction.

---

## Status

`plan_date` is load-bearing, not a comment. The market-open routine compares it to today's
ET date and **refuses to execute any intent from a plan not dated today** — it logs the
stale plan, posts an alert, and proceeds to the core/rebalance section only.

If the pre-market run failed, was skipped, or crashed before writing, this file still holds
yesterday's intents. Executing them would be running stale research as though it were
fresh — the candidate has had another full session to move, and the §4 priced-in check that
cleared it was performed against prices that no longer exist. Doing nothing is strictly
better. Core and rebalance actions are exempt from the gate because neither depends on the
day's research.

```
plan_date: 2026-09-02
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-02 at 09:30 ET (`alpaca.py clock`: `is_open: false`,
`next_open: 2026-09-02T09:30:00-04:00`, timestamp `08:30:11 ET`). **Not a holiday** — the market
is closed because it is pre-market, and `next_open` is today.

**One pre-market run today, at 08:30 ET**, against three yesterday. This plan supersedes nothing;
there is no earlier run today to reconcile against.

**Tape context:** at 08:30 ET no pre-market quote had printed for VOO — `latestQuote` still
carried yesterday's 16:00 ET close stamp with a wide 679.52 / 721.61 book, which is a stale
after-hours spread and **must not be used as a reference price**. VOO's last actual trade is the
2026-09-01 close at **700.14**, down from 704.875 on 08-31 (−0.67%) and from 707.18 on 08-28.

---

## Intents

### REBALANCE — core (this is the first-run bootstrap, and it is the whole plan)

- current_core_pct:  0.0%   (target 70%, §2 band 65–75% — outside the band)
- action:            BUY VOO to establish the core sleeve at 70% of account value
- notional:          $70,000.00
- account_equity:    $100,000.00 (100% cash, no positions — `alpaca.py sleeves`, 08:30 ET:
                     `core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0`)
- command:           `python scripts/alpaca.py buy --symbol VOO --notional 70000 --core`
- reference_price:   VOO last trade **700.14** (2026-09-01 close). Asset check at 08:30 ET:
                     `tradable: true`, `fractionable: true`, ARCA, us_equity, status active —
                     §3 clear. No priced-in check applies: §4's hard filters govern satellite
                     catalyst trades, not the permanent core sleeve (§2).
- revalidate:        Re-read `alpaca.py sleeves` at the open. If `core_established` is still
                     `false` and `core.pct` is still 0.0, proceed. Size to **70% of live equity
                     at the open**, not to the $70,000 written here — if equity has moved, the
                     target moves with it. Confirm VOO is still `tradable: true` before
                     submitting. **Do not use the pre-market `latestQuote` spread recorded
                     above as a price reference** — pull a fresh quote at 09:35.

**⚠ Step 3's bootstrap and Step 7's rebalance are the SAME $70,000 VOO buy on this account, not
two actions. Do not submit both.** `core_established: false` and core 0.0% describe one condition
with one remedy.

**This intent is exempt from the `plan_date` staleness gate** and does not depend on the day's
research, but it is dated today regardless.

### BUY — none

No buy intents. Two candidates were worked through §4 today and both were rejected. Details in
`research_log.md`; the short version:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-02-01 | LHX | part 2 | Only publicly traded US name on the Army TITAN team, sourced. But the whole production award is **$127M across a five-partner team** against $21.865B FY2025 revenue — **≤0.58%**, and L3Harris's own share is unstated. Worse than NOC's ~1.0%. |
| T-2026-09-02-02 | HPE | part 1 | Rose ~5% because Dell's AI-server guidance raise "improved sentiment." That is a read-across, not a mechanism — Dell shipping more servers does not raise HPE's revenue. The SAIC failure from 2026-09-01, recurring within 24 hours. |

Nine further events were dropped before thesis stage — GE's $2.87B F414 award (**sole-source, no
Company B, confirmed by a dedicated screen**), the unsigned Nvidia/Hugging Face rumour, NASA/Blue
Origin, ISM PMI, construction spending, JOLTS, Zepp Health, Enovix, Doosan Fuel Cell and Honda.
The funnel is written out in `research_log.md`.

Notes for the open run, carried so nothing is re-derived at 09:35:

- **Nothing here is queued or deferred.** Both of today's candidates are rejected outright. LHX
  fails on magnitude and HPE on the absence of a mechanism; neither is a number that a better
  entry price repairs.
- **LHX has now surfaced on two consecutive days through two different drivers** (PAC-3 MSE /
  THAAD yesterday, Army TITAN today) and failed on two different parts. Treat a recurrence as a
  warning, not corroboration — a large diversified prime appears in every defense news cycle,
  and appearing is not being materially affected. The stock is still trading on the postponed
  Missile Solutions IPO, which is neither of those mechanisms.
- **MU did not enter today's funnel and its filter was not re-run.** No source in six queries
  named it. Do not reach for it at the open on the strength of Dell's AI-server numbers — the
  component-supplier screen came back explicitly empty, and naming a memory vendor would be
  inference.
- **NOC and LHX share the PAC-3 driver; MU, STX and SNDK share the memory-cycle driver.** §4's
  correlation rule permits at most one of each group at a time, if either ever becomes live.

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — both empty (`[]`,
checked 08:30 ET). §5.1–5.4 have nothing to evaluate against: no invalidation condition exists to
test, no timing window to expire, and no entry or high-water mark to measure a stop against.

---

## Standing flag for the open run

`TRADING_ENABLED: false` in `control.md`. Every order below will be a **dry run** —
`alpaca.py buy` will print the intended order, return `"dry_run": true`, and submit nothing.

**This includes the core bootstrap.** The account will remain 100% cash after the open run,
`core_established` stays `false`, and this same REBALANCE intent will be regenerated
tomorrow. That is the configured behavior, not a fault — but it means the §1 objective
(beat the S&P over a rolling 12 months) is currently being pursued from an all-cash book
that cannot track the index in either direction. Only the human can change it, in
`control.md`. Log the intent as an intent, never as a fill.

**Day two of this condition.** The 2026-09-01 open run executed the identical intent and got back
`{"ok": true, "dry_run": true, "reason": "TRADING_ENABLED is not true in control.md"}`, exit 0, no
order submitted — recorded under `trade_log.md` → *Dry-run intents*. Yesterday VOO fell 0.67% and
the un-deployed core sleeve happened to sit out a down day. **That was luck and is not a reason to
be relaxed:** the same mechanism sits out up days at exactly the same rate. `control.md` itself
describes the dry run as a way to "watch the system think for a week before it touches the
account," so this is a deliberate human setting on its second day, not an incident — do not raise
an alert for it.

---

## Template

```
### BUY — <TICKER>
- thesis_id:      T-YYYY-MM-DD-NN   (must already exist in research_log.md)
- asset_type:     stock | etf
- market_cap:     $00.0B  (stocks only; §3 floor is $10B)
- market_cap_src: <source>
- notional:       $0.00   (≤5% of account value, §6)
- driver:         <catalyst, checked against every open position's driver>
- revalidate:     <what would make this dead by the open — the specific number to re-check>

### SELL — <TICKER>
- thesis_id:      T-YYYY-MM-DD-NN
- rule:           §5.1 invalidation | §5.2 time stop | §5.3 hard stop | §5.4 trailing stop
- evidence:       <the observable fact that triggered it>

### REBALANCE — core
- current_core_pct: 0.0%
- action:           buy | sell to return core to 70% (§2)
- notional:         $0.00
```

---

## No-trade days

An empty intent list is the expected output most days. §4: *"The correct output of most
research runs is no trade. A run that finds nothing worth buying is a successful run."*
When there is nothing to do, write that plainly here with the reasoning — do not pad the
list to look productive. The rejected candidates still go in `research_log.md`, which is
where the value of a quiet day actually lives.
