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
plan_date: 2026-09-03
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today 2026-09-03 at 09:30 ET (`alpaca.py clock`: `is_open: false`,
`next_open: 2026-09-03T09:30:00-04:00`, timestamp `08:27:45 ET`). **Not a holiday** — the market
is closed because it is pre-market, and `next_open` is today.

**One pre-market run today, at 08:27 ET.** This plan supersedes nothing; there is no earlier run
today to reconcile against.

**Tape context:** VOO's last actual trade is the **2026-09-02 close at 703.34**, up from 700.14
on 09-01 (+0.457%) and against 704.875 on 08-31. As on previous pre-market runs, do not use the
`latestQuote` spread before the bell as a reference price — pull a fresh quote at 09:35.

---

## ⚠ READ FIRST — trading is live as of today

**`TRADING_ENABLED: true` in `control.md`.** The human set it at 21:08 PT on 2026-09-02
(commit `1005b1e`, "Enable trading") — 00:08 ET today. The selftest at 08:27 ET confirms it:
`"control": "control.md ok - LIVE (paper account)"`, `"trading_enabled": true`.

**Every run in this repo's history before today was a dry run. This one is not.** The
REBALANCE intent below will place a **real $70,000 order** against the paper account, not
print an intent and return `"dry_run": true`. Three previous open runs submitted this same
bootstrap and got nothing back; **do not pattern-match on that.** The correct expectation at
09:35 is a filled order, a `trade_log.md` → *Entries* row, and `core_established: true`.

**Anything in `state.md`'s carry-forward or in `trade_log.md` → *Dry-run intents* that says
`TRADING_ENABLED: false` is stale as of today** and describes 2026-09-01 and 09-02 only. The
carry-forward has been rewritten this run; the trade-log dry-run section is history and is
deliberately left standing as history.

---

## Intents

### REBALANCE — core (the bootstrap, and it is the whole plan)

- current_core_pct:  0.0%   (target 70%, §2 band 65–75% — outside the band)
- action:            BUY VOO to establish the core sleeve at 70% of account value
- notional:          $70,000.00
- account_equity:    $100,000.00 (100% cash, no positions — `alpaca.py sleeves`, 08:27 ET:
                     `core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0`)
- command:           `python scripts/alpaca.py buy --symbol VOO --notional 70000 --core`
- reference_price:   VOO last trade **703.34** (2026-09-02 close). Asset check at 08:27 ET:
                     `tradable: true`, `fractionable: true`, ARCA, us_equity, status active —
                     §3 clear. No priced-in check applies: §4's hard filters govern satellite
                     catalyst trades, not the permanent core sleeve (§2).
- revalidate:        Re-read `alpaca.py sleeves` at the open. If `core_established` is still
                     `false` and `core.pct` is still 0.0, proceed. **Size to 70% of live equity
                     at the open**, not to the $70,000 written here — if equity has moved, the
                     target moves with it. Confirm VOO is still `tradable: true` before
                     submitting.
- verify:            **This is the part that is new today.** `buy` polls to a terminal state.
                     If `"terminal": false`, do **not** write a fill — re-check with
                     `alpaca.py order --id <id>` and log what is actually there (§7). Only
                     write `trade_log.md` → *Entries* and flip `core_established: true` once a
                     fill is confirmed.

**⚠ Step 3's bootstrap and Step 7's rebalance are the SAME $70,000 VOO buy on this account, not
two actions. Do not submit both.** `core_established: false` and core 0.0% against a 70% target
describe one condition with one remedy. Three previous open runs each correctly submitted this
once; today it costs real money to get wrong.

**This intent is exempt from the `plan_date` staleness gate** and does not depend on the day's
research, but it is dated today regardless.

### BUY — none

No buy intents. One candidate was worked through §4 today and was rejected.

| Thesis | Ticker | Died at | Why |
|---|---|---|---|
| T-2026-09-03-01 | LITE | §4 priced-in filter | Morgan Stanley names Lumentum as a key **pump-laser** supplier to a Ciena that is explicitly "supply-constrained… particularly pump lasers," off a Q3 that grew 37% and raised guidance. Best-sourced part 1 in this log. But `move --sessions 5` returns **−7.35%**, `priced_in: true`. §4 is a veto and it fired. |

Eleven further events were dropped before thesis stage — Broadcom's weak guidance (**dedicated
screen empty; no Company B, and wrong direction for a long-only book**), the Google adtech
no-divestiture ruling (**only Alphabet named; a status-quo ruling changes no one's revenue
line**), FuelCell Energy's 75 MW Texas reservation and 380 MW Fit Energy agreement (**FCEL is
Company A and sub-$10B; counterparties private or unnamed**), Uber's 3,300 layoffs, KBR/NOAA,
Studsvik/GE Vernova Hitachi's Swedish nuclear commitment, BioLargo (**OTCQX, §3-ineligible**),
PharmaEssentia, and the ADP / ISM / construction-spending macro misses. The funnel is written
out in full in `research_log.md`.

Notes for the open run, carried so nothing is re-derived at 09:35:

- **Nothing here is queued or deferred, and LITE specifically is not a "wait for a better
  entry."** It failed because it had **already fallen** 7.35%; a further decline makes the
  filter reading worse, not better. There is no price at which today's rejection flips.
- **⚠ Do not reach for LITE, COHR, CIEN or any AI-optics name at the bell.** The screen named
  **only** Lumentum as a sourced Ciena supplier. Coherent, Cisco, Broadcom, AAOI, Corning,
  Amphenol, Nokia, Ericsson and Arista appear in the retrieved material purely as ecosystem
  read-throughs, with **no sourced supplier relationship to Ciena** — buying one of those
  would be the RTX failure exactly.
- **Do not reach for MU.** It did not enter today's funnel, no source named it, and its filter
  was not re-run. This is the second consecutive day recording that the reason is *absence of
  evidence today*, not resolve.
- **A live account is not a reason to open something.** Today is the first day an order can
  reach the broker. §4's honest-broker rule is unchanged by that fact, and the correct output
  of most research runs is still no trade.

### SELL — none

No open satellite positions. `positions.md` and `alpaca.py positions` agree — both empty (`[]`,
checked 08:27 ET). §5.1–5.4 have nothing to evaluate against: no invalidation condition exists to
test, no timing window to expire, and no entry or high-water mark to measure a stop against.

---

## Standing flags for the open run

- **The §5.4 trailing stop is not yet armed** — not disabled, not skipped. It arms the day the
  first satellite position opens. Today's core buy does **not** arm it: the core sleeve is
  exempt from §5 entirely and is deliberately not tracked in `positions.md`.
- **The §6 weekly cap is fully available at 0 of 3.** Week rollover was checked this run: ISO
  Monday of 2026-09-03 (Thursday) is **2026-08-31**, which matches `week_of` — no reset was due.
  The next boundary is **2026-09-07**, not today.
- **Circuit breaker INACTIVE**, `consecutive_closed_losses: 0`, `halt_triggered_at: none`,
  `HALT_CLEARED_AT: none`. Nothing has ever closed, so the streak cannot have moved.
- **`alerts.md` is empty — zero incidents, nothing SYSTEMIC.** Selftest passed all five checks
  at 08:27 ET.

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
