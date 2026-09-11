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

**Reconciliation 2026-09-11 09:36 ET (2-market-open-execution) — RECONCILED AT THE BELL ON AN OPEN
MARKET. NO SATELLITE POSITION EXISTS. NO ORDER WAS PLACED. NO HIGH-WATER MARK WAS DUE OR WRITTEN.**
*(This block replaces this morning's 08:20 pre-market reconciliation, read in full by this run and
carrying nothing this one does not. Collapse, do not append — thirteenth consecutive run.)* Selftest
passed all five checks at 09:36 ET (`trading_enabled: true`, LIVE paper account, equity $99,728.60).
**`clock` at 09:36:29 ET returns `is_open: true` with `next_close: 2026-09-11T16:00 ET` — the market
is OPEN and this is a regular session. Contrast this morning's pre-market read, where `is_open:
false` meant pre-market rather than holiday.**

`alpaca.py positions` returns **one row, VOO core** (99.046311231 shares, avg_entry 706.74,
market_value $69,726.61, broker `current_price` **703.9799**, `lastday_price` 696.65,
`change_today` **+1.052%**, unrealized_pl **−$273.38, −0.391%**, unrealized_intraday_pl
**+$725.99**). `alpaca.py sleeves`: equity **$99,722.65**, cash $30,000.00, core **69.92%**,
satellite **0.0% (count 0)**, cash 30.08%, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: +82.20`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.**
Compare **satellite to satellite**, never raw ledger to raw broker.

**⚠ THE STALENESS GATE PASSED, AND IT MATTERS THAT IT PASSED RATHER THAN FIRED.** `plan_today.md`
carries **`plan_date: 2026-09-11`**, which equals today's ET date, so **every intent in the plan was
executable and none was skipped for age.** No stale-plan alert was due and none was posted. **The
plan simply contains no intent of any kind** — the 08:20 run wrote five theses and rejected all five.
**A zero-order open run on a passed gate and a zero-order open run on a failed gate look identical
from the outside and are opposite events.** This was the first.

**Nothing was blocked at the bell.** Breaker INACTIVE, `consecutive_closed_losses: 0`, weekly cap
**0 of 3**, satellite sleeve **empty with 30.08% cash**, `control.md` notes empty, `alerts.md`
empty. **§6's three constraints were all fully available and none of them was reached.** Step 3 was
skipped on `core_established: true` — the bootstrap path is closed permanently. **Steps 5–6 made no
`alpaca.py move` call and none was due: re-validation has a subject only when there is a BUY intent
to re-validate, and there was none.** The open run **does not generate ideas**; a candidate that was
not researched before the bell does not get reasoned into existence after it.

**⚠ THE HIGH-WATER FIELD IS ABSENT, NOT STALE — checked against the actual trigger, not assumed.**
The backfill rule at the top of this file fires when a `highest_close` is **behind the last trading
day**. There is **no satellite position block in this file**, so there is **no `highest_close` and
no `(as of ...)` date** to be behind anything. The marks are **ABSENT: a third state, distinct from
both "current and unchanged" and "stale."** An absent field carries no date, so the backfill trigger
cannot fire. **No `bars` call was due for a high-water purpose and none was made — this run made no
`bars` call at all**, since `voo_close_at_entry` is captured only when a satellite position opens.
**Core VOO was again deliberately not given a mark**, because stamping one would fabricate a §5.4
trailing stop on the one position §5 exempts from all four rules. **§5.4 remains NOT ARMED, not
disabled, not skipped.** It arms on the first *satellite* fill.

**§5.1–§5.4 have no subject at this open.** No thesis to test for invalidation (§5.1); no timing
window to expire (§5.2); no entry price to measure −7% against (§5.3); no high-water mark to measure
−10% against (§5.4). `sell_rule_status` is **absent rather than blank** — there is no position block
to carry the field. **All four remain untested code paths; nothing has ever closed in this account**,
which is also why `consecutive_closed_losses` cannot have moved and no circuit-breaker alert was due.

**⚠ THE TWO-PRICE TRAP IS UNCHANGED AND STILL UNTESTED IN ANGER.** The broker's `lastday_price`
reads **696.65** against yesterday's official close of **696.69** (`bars --adjustment all`) — a
4-cent gap this morning, against ~60 cents at last night's close and ~6.5 cents on 09-09. **The gap
is not a stable offset that could be corrected for.** On core it is cosmetic. **On a satellite
position the same shortcut writes a `highest_close` wrong by an amount that changes day to day,
which does not error, does not read as stale, and silently moves the §5.4 stop to a level nobody
chose.** Always `bars --adjustment all` for a close and a fresh `quote` for execution — **never a
`positions` field for either.**

**§2 rebalance: NOT DUE.** 69.92% sits well inside the 65–75% band; `core_in_band: true`,
`rebalance_needed: false`, and the +$82.20 delta is **0.08% of equity** — the smallest drift yet
recorded, and it is VOO's mark moving rather than drift at all. §2 rebalances at the **band edge**
(65/75), not to the exact target. **Step 7 was evaluated and correctly produced no order.**

**⚠ THE CORE OPENED GREEN, AND THAT IS NOT A RESULT EITHER.** The mark is **+1.05% / +$725.99 on
the session**, narrowing the loss against the 706.74 fill to **−$273.38 (−0.391%)** from −$543.76 at
08:20 — after nine consecutive negative closes. **It means nothing procedurally in either
direction:** §5 exempts core from all four sell rules, there is no §5.3 or §5.4 on this position to
cross, and **a green mark is no more a result than the nine red ones were.** The specific trap today
is the **inverted** reassuring sentence — "the book rose less than the index," "we lagged" — which is
wrong for the same two reasons its falling twin was: ~0.70 exposure returns ~70% of an index move by
construction, and both ends of the broker's day P&L are broker marks. **A book whose only holding is
core, sitting on 30% cash with a clear breaker and an empty weekly cap, on a green open, is precisely
the setup in which the §4 bar gets quietly lowered to put *something* on.** It was not lowered. **No
order was placed in either sleeve.**
---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-10 09:36) HAVE BEEN COLLAPSED,
DELIBERATELY.** Twenty-three blocks spanning 09-01 to the 09-10 open run each recorded the same
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
