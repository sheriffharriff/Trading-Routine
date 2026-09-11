# Open Positions Ledger

**AGENT-OWNED.** One block per open **satellite** position. The core holding is not
tracked here — it is never sold on news (§5) and needs no thesis state.

Alpaca is authoritative for what is held and at what cost. This file exists for the
things Alpaca does not store and that §5 cannot be enforced without:

- the **highest close since entry**, without which the §5.4 trailing stop does not exist
- the **timing window deadline**, without which the §5.2 time stop never fires
- the **invalidation condition**, verbatim, because §7 forbids softening it later —
  keeping it written down is what makes softening visible

**High-water maintenance:** the market-close routine writes every open position's official
close into `highest_close` each day (only if it is higher). If a close run was skipped, the
next run must backfill from `python scripts/alpaca.py bars --symbol X --days N` before
evaluating §5.4. A gap in this field silently disables the trailing stop, which is the kind
of failure that looks like nothing is wrong.

---

## Template

```
### <TICKER> — <thesis-id>

- entry_date:            YYYY-MM-DD
- entry_price:           0.00
- qty:                   0.000
- notional_at_entry:     0.00
- pct_of_account_entry:  0.0%
- voo_close_at_entry:    0.00  (adjustment=all — the same-period baseline for this position)
- asset_type:            stock | etf
- market_cap_at_entry:   $00.0B
- market_cap_source:     <where the figure came from>
- highest_close:         0.00  (as of YYYY-MM-DD)
- timing_window:         <next earnings | Q_ YYYY>  → deadline YYYY-MM-DD
- invalidation:          <verbatim from the thesis, part 4 — never reworded>
- sell_rule_status:      <which of §5.1–5.4 are near triggering, and the distance to each>
- driver:                <the underlying catalyst, for the §4 correlation check>
```

The `driver` line is what makes the correlation check possible. Before opening anything new,
the pre-market routine reads every `driver` here and rejects a candidate exposed to the same
one — otherwise you are making a single bet spread across several tickers and mistaking it
for diversification.

`voo_close_at_entry` is recorded once, at entry, and never updated. The Friday review needs
each position measured against what the same capital would have done in VOO over that
position's own holding window; capturing the baseline at entry means the review never has to
re-derive it from price history, and it stays correct for positions closed months later.

---

## Open positions

*(none — no **satellite** positions have been opened yet. Core VOO exists and is deliberately not tracked here, per the top-of-file rules and the fill note further down.)*

**Reconciliation 2026-09-11 12:34 ET (3-midday-management) — NO EXITS, NO SUBJECT, AND A PARTIAL
ALPACA OUTAGE THAT COST NOTHING ONLY BECAUSE THIS SLEEVE IS EMPTY.**
*(This block replaces the 09:36 open-run reconciliation, read in full by this run and carrying
nothing this one does not. Collapse, do not append — fourteenth consecutive run.)* Selftest passed
all five checks at **12:34 ET** (`trading_enabled: true`, LIVE paper account, equity $99,713.75).

**⚠ THE FINDING OF THIS RUN IS AN INFRASTRUCTURE FAULT, NOT A TRADING ONE. ALPACA IS HALF DOWN.**

| Endpoint | Result at 12:34–12:36 ET |
|---|---|
| `account` | **200 OK** — ACTIVE, equity 99,687.99, `trading_blocked: false` |
| `positions` | **200 OK** — one row, live mark |
| `sleeves` | **200 OK** |
| `clock` | **500 Internal Server Error — 4 consecutive attempts** |
| `quote --symbols VOO` | **504 backend request timeout — 2 attempts** |
| `bars --symbol VOO --days 3 --adjustment all` | **504 backend request timeout** |

**The trading plane is healthy and the data plane is down.** `clock` worked at the 09:36 bell
(`is_open: true`), so it broke sometime between 09:36 and 12:34.

**⚠ AND THE SELFTEST PASSED ALL FIVE CHECKS WHILE THIS WAS TRUE.** Step 0 probes env, account,
Perplexity, ClickUp and `control.md` — **it does not probe `clock` and it does not probe market
data.** So the pre-flight designed to make a broken run loud at the start **certified a system
whose price feed was unreadable.** **That gap, not the outage, is what a human needs to see:** the
outage will pass by itself; the blind spot will not.

**⚠ THE MARKET WAS JUDGED OPEN BY INFERENCE, AND THAT IS A CONCESSION, NOT A METHOD.** With `clock`
unreadable, the session was established from independent evidence: **Friday 2026-09-11 12:35 EDT is
inside regular hours**, and `positions` carried a **live mark that MOVED between calls** — 703.9799
at 09:36 → **703.7729** at 12:35, `change_today` **+1.022%**. **This was safe here only because this
routine places no orders.** §7 forbids trading when the market is closed, and **a moving mark is not
proof of an open session** — it can be replayed or stale, and a half-day is precisely what `clock`
exists to report. **A run that wants to place an order and cannot read `clock` must not infer its
way to a fill.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.**
Compare **satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns
**one row, VOO core** (99.046311231 shares, avg_entry 706.74, market_value $69,706.11, broker
`current_price` **703.7729**, `lastday_price` 696.65, `change_today` **+1.022%**, unrealized_pl
**−$293.88, −0.42%**, unrealized_intraday_pl **+$705.50**). `alpaca.py sleeves`: equity
**$99,706.11**, cash $30,000.00, core **69.91%**, satellite **0.0% (count 0)**, cash 30.09%,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +88.17` — **0.09% of equity, and
noted only: §2 rebalancing belongs to the market-open run, not to this one.**

**⚠ STEP 2 (HIGH-WATER REPAIR) WAS NOT DUE — AND THE OUTAGE THEREFORE BLOCKED NOTHING THAT WAS
OWED.** The backfill rule fires when a `highest_close` is **behind the last trading day**. There is
**no satellite block in this file**, so there is **no `highest_close` and no `(as of ...)` date** to
be behind anything. The marks are **ABSENT: a third state, distinct from both "current and
unchanged" and "stale."** **`bars` was down and no `bars` call was owed — those two facts are
independent, and the run must not be read as having skipped a repair it could not perform.** **Had
even one satellite position existed, the repair would have been owed and IMPOSSIBLE**, leaving §5.4
to be evaluated against a stale mark or not at all. **Core VOO was again deliberately not stamped**,
because stamping one would fabricate a §5.4 stop on the one position §5 exempts. **§5.4 remains NOT
ARMED** — it arms on the first *satellite* fill.

**§5.1–§5.4 HAD NO SUBJECT AT MIDDAY — this is the eleventh such day and it is not a clean bill of
health.** No thesis to test for invalidation (§5.1); no `timing_window` to expire (§5.2); no
`entry_price` to measure −7% against (§5.3); no high-water mark to measure −10% against (§5.4).
**Nothing was near triggering because nothing exists to trigger.** `sell_rule_status` is **absent
rather than blank** — there is no position block to carry the field. **No `perplexity.py` call was
made and none was due:** §5.1 reads an `invalidation` line verbatim from this file, and there is no
line to read. **All four remain untested code paths; nothing has ever closed in this account**,
which is also why `consecutive_closed_losses` cannot have moved and **no circuit-breaker alert was
due.**

**NO POSITION WAS OPENED, AND NONE COULD BE.** This routine is **exits-only by design** — new
positions route through pre-market research and the 09:35 execution run, which is what forces every
buy to sleep on a written thesis. **An empty satellite sleeve at midday on a green tape, with a
clear breaker and an empty 0-of-3 weekly cap, is exactly the setup that produces the urge to route
around that.** The urge is not evidence. Nothing was opened.

**⚠ THE TWO-PRICE TRAP JUST GOT WORSE, AND IN A NEW DIRECTION.** The standing defect is that broker
`lastday_price` differs from the official close by an unstable amount (4 cents this morning, ~60
cents at last night's close, ~6.5 cents on 09-09). **Today's outage removes the CORRECT source of a
close (`bars`, 504) while leaving the WRONG one (`positions` fields, 200) fully working.** That is
the worst possible combination: **the failure mode is not an error but a silent substitution.**
Always `bars --adjustment all` for a close and a fresh `quote` for execution — **and when they are
down, the answer is to say so, never to reach for the field that still responds.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-11 09:36) HAVE BEEN COLLAPSED,
DELIBERATELY.** Twenty-five blocks spanning 09-01 to this morning's open run each recorded the same
null result — zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no
§5 rule evaluated; no high-water mark to stamp; no backfill due. `state.md` flags this
accumulation as
actively harmful rather than untidy: this repo's only continuity mechanism is the next run
*reading* these files, and padding them with restatements of one null fact raises the odds that
a genuinely live item gets skimmed. Carry-forward is defined as **cleared once acted on**, and
each of those blocks was acted on by the run that read it. **The correct response to the pull to
append is to collapse, not to add another.** Nothing live was discarded — the load-bearing facts
those blocks carried are preserved here:

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional
  $70,000.00**, order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**,
  verified terminal before it was written. Audit record in `trade_log.md`.
- **Measure the core from the 706.74 fill, not from a prior VOO close.** The fill landed
  **+0.483% above the previous close**, and that one-time entry gap — not tracking error and
  never skill — is the whole of the core's reported divergence from VOO.
- **The core is not tracked in this ledger by design.** §5 exempts it from all four sell rules,
  so it has no thesis state, no timing window and no `highest_close`. **Every reconciliation
  compares satellite blocks to satellite Alpaca positions**; a run that compares the raw ledger
  to the raw broker will read a correct ledger as broken.
- **§5.4 has never been armed.** It arms on the first *satellite* fill. The 09-03 core fill was
  not that day, and no day since has been either.
- **All four §5 sell rules remain untested code paths.** Nothing has ever closed, so the string
  of "no exits" entries recorded the absence of a subject, not clean bills of health.
