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

**Reconciliation 2026-09-15 12:35 ET (3-midday-management) — LEDGER AGREES WITH THE BROKER;
STILL NO SATELLITE SUBJECT, SEVENTEENTH CONSECUTIVE SESSION.**
*(This block **replaces** the 09-15 09:36 open reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — twenty-second consecutive
run.**)*
Selftest passed all five checks at **12:34 ET** (`trading_enabled: true`, LIVE paper account, equity
$98,980.31). `clock` **`is_open: true`** at 12:34:55, `next_close` 2026-09-15T16:00:00-04:00 —
**the market is open; no closed-market skip.**

**THE RUN ENDED AT STEP 1 BECAUSE ITS SUBJECT DOES NOT EXIST, WHICH IS THE PROMPT'S OWN
INSTRUCTION AND NOT A SHORTCUT.** Routine 3 says in terms: *no open satellite positions → note it,
commit, exit; do not go looking for something to do.* Steps 2–5 were reached and had nothing to
act on. **This run is EXITS-ONLY and may not open a position under any reading** — the 30.31% idle
cash, the breaker reading INACTIVE and the weekly cap at 0 of 3 are **not an opportunity this
routine may take**. New positions route through pre-market research plus the 09:35 execution run,
always.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares, avg_entry 706.74, market_value $68,980.80, broker `current_price`
**696.45**, `lastday_price` 699.30, unrealized_pl **−$1,019.19, −1.456%**, unrealized_intraday_pl
**−$282.28, −0.408%**). `alpaca.py sleeves`: equity **$98,982.78**, cash $30,000.00, core **69.69%**,
satellite **0.0% (count 0)**, cash 30.31%, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: +305.16` — **0.31% of equity. Routine 3 places no rebalance in any case**, and §2
rebalances at the **band edge (65/75)**, not to the exact target. **Fifteenth consecutive run inside
a 0.29-point range (69.69–69.98).**

**⚠ THE CORE MARK CARRIES NO ACTION IN EITHER DIRECTION AND IS NOT A SELL SIGNAL.** §5 exempts core
from all four sell rules and §5 says core is never sold on news. **Measured from the 706.74 fill,
not from an inception anchor** — the 09-03 fill landed +0.483% above the prior close and that
permanent entry gap, not tracking error and never skill, is the whole of the core's reported
divergence from VOO. Today's −1.456% unrealized is a price, not a signal, and the sleeve percentage
§2 actually triggers on is 69.69% and inside the band.

**STEP 2 HIGH-WATER REPAIR: NO BACKFILL WAS DUE, AND THE REASON IS STRUCTURAL RATHER THAN
INCIDENTAL.** There is no satellite block, so there is no `highest_close` to compare against the
last trading day and no `(as of ...)` date to find stale. **The marks are ABSENT — a third state,
and the only one that carries no date**, and that absence of a date is exactly what tells this run
no `bars` call is due for a high-water purpose. **Zero `bars` calls were issued and none was due.**
**Core VOO is deliberately never stamped** — stamping it would fabricate a §5.4 trailing stop on the
one position §5 exempts from every sell rule. **§5.4 remains NOT ARMED; it arms on the first
*satellite* fill.** **This is the second midday run to exercise the REPAIR step against an empty
sleeve and find nothing to repair — the "no subject" branch, and nothing else, has ever run.**

**§5.1–§5.4 HAD NO SUBJECT — seventeenth consecutive session, and it is not a clean bill of
health.** No thesis to test for invalidation (§5.1); no `timing_window` to expire (§5.2); no
`entry_price` to measure −7% against (§5.3); no high-water mark to measure −10% against (§5.4).
**Nothing was near triggering because nothing exists to trigger.** `sell_rule_status` is **absent
rather than blank**. **ZERO Perplexity invalidation queries were issued and none was due** — §5.1
reads the `invalidation` line of an open position, and there is none; **an absent check, not a
skipped one.** **All four remain untested code paths; nothing has ever closed in this account**,
which is why `consecutive_closed_losses` cannot have moved and **no circuit-breaker alert was due.**

**NOTHING SHOULD HAVE EXECUTED AND FAILED TO.** Step 4 had no triggered position, so **zero sell
orders were placed**; no `"terminal": false` case could arise, and **no dry-run intent was
suppressed** — `TRADING_ENABLED` is **true**, so had a stop fired it would have been submitted for
real. **`trade_log.md` correctly left unappended — a run with no fill writes no trade entry.** The
account's entire order history remains **one row**, the 09-03 core fill, `status: filled`, terminal,
re-verified by hand this run.

**Two facts carried forward, settled and not to be re-derived:** (1) **the Alpaca data-plane outage
is resolved** — `clock`, `positions` and `sleeves` all answered cleanly this run, probed by hand;
but **open item (6) survives it**, because `selftest.py` still does not probe `clock` or market data
and a green pre-flight therefore certifies nothing about the data plane. (2) **The two-price defect
is SOLVED and it is a live quote midpoint, not an offset** — which is why the gap never had a stable
size. **This run's broker `current_price` 696.45 is an intraday midpoint, not a close**, and it was
used for nothing but reporting. Always `bars --adjustment all` for a close, a fresh `quote` for
execution, **never a `positions` field for either.** Cosmetic on core; **load-bearing the moment a
satellite position exists**, because a `highest_close` stamped from a `positions` field would record
a midpoint and silently move the §5.4 stop.

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-15 09:36) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty blocks spanning 09-01 to this morning's open run each recorded the same
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
- **The two-price defect is SOLVED and it is a live quote midpoint, not an offset** — which is why
  the broker/official gap (6.5c, 59.85c, 4c on successive days) never had a stable size and never
  will. A `current_price` of 700.57 against a `lastday_price` of 702.56 is an **intraday midpoint,
  not a close.** Always `bars --adjustment all` for a close, a fresh `quote` for execution, **never
  a `positions` field for either.** Cosmetic on core; **load-bearing the moment a satellite
  position exists**, because a `highest_close` read from a `positions` field records an after-hours
  midpoint and silently moves the §5.4 stop.
- **The 09-11 Alpaca data-plane outage is resolved** (every endpoint 200 at the 09-11 close, probed
  by hand), **but `selftest.py` still does not probe `clock` or market data** — a green pre-flight
  certifies nothing about the data plane. Probe by hand before relying on a price.
