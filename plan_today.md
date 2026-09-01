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
plan_date: 2026-09-01
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-01 at 09:30 ET (`alpaca.py clock`: `is_open: false`,
`next_open: 2026-09-01T09:30:00-04:00`, timestamp `08:56 ET`). Not a holiday — the market is
closed because it is pre-market.

**This plan is written by the third pre-market run of 2026-09-01 and supersedes both earlier
ones** (00:48 ET → `577ff28`, 01:15 ET → `9d592dd`). All three agree on every intent; the
substance below is unchanged from the first run. What this run adds is one more rejected
thesis (T-2026-09-01-06, AEP) and — more usefully — **research done from inside the
pre-market session rather than at one in the morning**. The earlier runs' priced-in checks
were computed with no pre-market tape in existence. These were not.

**Tape context the earlier runs could not see:** index futures are lower to start September,
oil is up (~+1.9% Brent), and **VOO is quoted 700.58 / 700.68 pre-market against a 704.875
close — about −0.6%.** That matters for the rebalance intent below, not for any research
conclusion.

---

## Intents

### REBALANCE — core (this is the first-run bootstrap, and it is the whole plan)

- current_core_pct:  0.0%   (target 70%, §2 band 65–75% — outside the band)
- action:            BUY VOO to establish the core sleeve at 70% of account value
- notional:          $70,000.00
- account_equity:    $100,000.00 (100% cash, no positions — `alpaca.py sleeves`, 08:56 ET)
- command:           `python scripts/alpaca.py buy --symbol VOO --notional 70000 --core`
- reference_price:   VOO closed 704.875 on 2026-08-31; **pre-market bid/ask 700.58 / 700.68 at
                     12:48 UTC (08:48 ET)**, i.e. roughly −0.6% from the close. Tradable,
                     fractionable, ARCA. No priced-in check applies — §4 hard filters govern
                     satellite catalyst trades, not the permanent core sleeve (§2).
- revalidate:        Re-read `alpaca.py sleeves` at the open. If `core_established` is still
                     `false` and `core.pct` is still 0.0, proceed. Size to **70% of live
                     equity at the open**, not to the $70,000 written here — if equity has
                     moved, the target moves with it. Confirm VOO is still `tradable: true`
                     before submitting.

**This intent is exempt from the `plan_date` staleness gate** and does not depend on the
day's research, but it is dated today regardless.

### BUY — none

No buy intents. **Six** candidates have now been worked through the §4 filters across today's
three runs, and all six were rejected. Details in `research_log.md`; the short version:

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-01-01 | NOC | parts 2 and 3 | $3B over 7 years ≈ 1% of a $42B revenue base; affected segment unidentifiable from any source |
| T-2026-09-01-02 | LHX | part 3 | Real $12B framework, but 2027+ revenue; and the stock is actually trading on a delayed missile-IPO overhang, not on interceptor demand |
| T-2026-09-01-03 | RTX | part 1 | No source ties RTX to PAC-3/THAAD content in these agreements — the mechanism was my inference, not reporting |
| T-2026-09-01-04 | MU | priced-in filter | Strongest thesis of the six — one-clause mechanism, DRAM is 76% of revenue, in-horizon — but +5.27% over 5 sessions and +15.6% over 20. Late. |
| T-2026-09-01-05 | WDC | part 1 | Only name in the memory complex to clear the priced-in filter, and it cleared it because it sold the flash business in Feb 2026. HDD-only. Not exposed to the driver. |
| T-2026-09-01-06 | AEP | parts 2 and 3 | Real, sourced interconnection exposure to the Hut 8 / Nvidia / Lambda Beacon Point campus — but 1 GW inside 45 GW of load AEP has **already guided through 2030**. ~2% of a disclosed pipeline, and outside the two-quarter horizon. |

**The pattern across the six is worth more than any individual entry.** Four of them
(NOC, LHX, WDC, AEP) *passed* the priced-in check and failed on the thesis. One (MU) passed
the thesis and failed the filter. **The filter has not once been informative about the
outcome.** It is a veto, not a signal — a pass says only that the stock has not moved, and
"has not moved" and "should have moved but didn't" are the same number. A candidate has to
survive both the filter and the thesis, and today none did.

Notes for the open run, carried so nothing is re-derived at 09:35:

- **NOC and LHX share one driver** (the PAC-3 MSE / THAAD ramp); §4's correlation rule permits
  at most one of them, ever, at the same time.
- **MU, STX and SNDK share one driver** (the memory price cycle) — three tickers, one bet.
- **Do not treat MU as a queued idea.** It is rejected, not deferred. If a later run
  rediscovers it, the priced-in check must be re-run fresh and the timing window re-tested
  from that day's date, not inherited.
- **Do not treat AEP as a queued idea either**, and for a different reason: it fails on
  timing and magnitude, which re-running a filter cannot fix. A better AEP entry point does
  not make a 2030 revenue ramp fit a two-quarter horizon.

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — both empty
(`[]`, checked 08:56 ET). §5.1–5.4 have nothing to evaluate against.

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
