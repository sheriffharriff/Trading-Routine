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

**Reconciliation 2026-09-17 12:35 ET (3-midday-management) — LEDGER AGREES WITH THE BROKER;
NOTHING TO MANAGE. NO EXIT EVALUATED, NO HIGH-WATER MARK BACKFILLED, AND NEITHER WAS DUE.**
*(This block **replaces** the 09-17 09:35 market-open reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — thirtieth consecutive
run.**)*
Selftest passed all five checks at **12:34 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,383.43 at pre-flight).

**⚠ THIS ROUTINE IS EXITS-ONLY AND IT HAD NO SUBJECT.** §5.1–§5.4 are evaluated per **open satellite
position**, and there are **zero**. The run is not permitted to open anything, so an empty sleeve
leaves it with **literally nothing to do** — which is the correct outcome, not a degraded one. **No
search for something to manage was performed and none was warranted.**

**`clock` READ `is_open: true` AT 12:35:02** with `next_close` **2026-09-17T16:00 TODAY** and
`next_open` **2026-09-18T09:30 TOMORROW** — the IN-SESSION shape, the only one of the three daily
shapes where the boolean alone is informative. **Read the DATE, not the boolean.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares — **unchanged, no order has touched it since 09-03**, avg_entry
706.74, market_value $69,387.88, cost_basis $69,999.99, broker `current_price` **700.56**,
`lastday_price` **693.24**, unrealized_pl **−$612.11 / −0.874%**, `change_today` **+1.056%**).
**`current_price` 700.56 is a LIVE IN-SESSION MARK, not a close** — do not mix it with a `bars`
close. `alpaca.py sleeves`: equity **$99,387.88**, cash **$30,000.00**, core **$69,387.88 = 69.82%**,
satellite **0.0% (count 0)**, cash **30.18%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: +183.63` = **0.18% of equity.** **NO REBALANCE WAS DUE, AND THIS ROUTINE COULD NOT
HAVE PLACED ONE ANYWAY** — §2 rebalances at the **next market-open run**, at the **band edge
(65/75)**, not to the exact target. **Twenty-third consecutive run inside a 0.39-point range
(69.59–69.98)**: a drifting core mark on an unchanged share count.

**STEP 2 — THE HIGH-WATER BACKFILL CHECK RAN AND DISCHARGED ON AN ABSENT FIELD, NOT A CURRENT ONE.**
The check compares each position's `highest_close (as of ...)` date against the last trading day.
**There is no `highest_close` field in this file at all**, because there is no satellite block to
carry one. **ABSENT is a third state, distinct from "current and unchanged" and from "stale" — and it
is the only one carrying no date.** The missing date is exactly what discharges the check. **Zero
`alpaca.py bars` calls were issued this run for any purpose**, and **core VOO was again deliberately
NOT stamped**: writing a close into this file for the one position §5 exempts from all four sell
rules would fabricate a §5.4 stop. **It would not feel like a violation, it would feel like
tidiness.** Refused again.

**STEP 3 — §5.1–§5.4 HAD NO SUBJECT, AND THE ORDERED EVALUATION NEVER STARTED.** No thesis to test
for invalidation (§5.1) and **zero `perplexity.py` invalidation queries were issued — an ABSENT
check, not a skipped one**; no `timing_window` to expire (§5.2); no `entry_price` to measure −7%
against (§5.3); no `highest_close` to measure −10% against (§5.4). **Nothing was near triggering
because nothing exists to trigger.** `sell_rule_status` is **absent rather than blank.** Still the
**nineteenth** session with an empty sleeve — the count advances on **sessions, not runs**, and this
run shares 09-17 with the two runs that preceded it today. **All four remain untested code paths and
§5.4 has never been armed** — it arms on the first *satellite* fill.

**STEP 4 — ZERO SELL ORDERS. Not one `alpaca.py sell` call was made, so no order-verification path
was exercised and no `terminal: false` or `dry_run: true` case arose.** **Nothing should have
executed and failed to** — the most important line this run could have carried is the one it does not
need. **The loss streak could not move: no position closed, so §6's counter has no event to count.**

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-17
(Thursday) is **2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday
2026-09-21. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`; `consecutive_closed_losses`
stays at **0** because nothing has ever closed in this account, so the §6 streak cannot move, no
`HALT_CLEARED_AT` comparison was required and **no circuit-breaker alert was due.** **Sleeve drift:**
core **69.82%**, inside the 65–75% band. `open_thesis_ids` stays **none** — nothing to add or remove;
all three of today's theses were rejected before the bell and this run opened nothing.

**⚠ OPEN ITEM (7) REMAINS OPEN AND THIS RUN DID NOT TOUCH IT — `alpaca.py move` IS BLIND TO AN
AFTER-HOURS EVENT.** The pre-market run found `move --symbol GNRC --sessions 5` returning **186.55 →
175.19, −6.09%, `priced_in: true`** the morning after GNRC reportedly surged after the bell on the
Amazon supply agreement, because **the five-session window ends at the last official close.** **It is
a BUY-path defect and this routine has no buy path**, so it had no bearing here and **no measurement
was taken to "document" it.** Tonight's close is what finally admits the gap into `bars`. **No run
may reinterpret the filter; that is a human editing §4 or the script.**

**⚠ GNRC WAS NOT LOOKED AT AGAIN, AND THE SECOND REFUSAL IS THE ENTRY WORTH KEEPING.** **Zero `move`,
`quote`, `bars` or `asset` calls were made on it this run.** The pull is now recurring: at 09:35 it
was "just to document the defect"; at 12:35 it would have been "just to see how it settled." **Both
are the same reflex — looking at the loud ticker — and the empty sleeve means there was no §5 subject
that could have justified a single price call on ANY ticker.** GNRC is the **named counterparty** in
the Amazon announcement — **first-order, outside §4 at any price** — and this run **cannot open a
position under any circumstance**, so no reading of it could have produced an action. **A midday run
with nothing to manage is meant to be short. Filling it with lookups is how an exits-only seat
quietly turns into a scouting seat.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-17 09:35) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-two blocks spanning 09-01 to this morning's open run each recorded the same
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
