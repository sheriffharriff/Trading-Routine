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

**Reconciliation 2026-09-17 09:35 ET (2-market-open-execution) — LEDGER AGREES WITH THE BROKER;
ZERO ORDERS PLACED FROM THE ONE SEAT THAT COULD HAVE PLACED THEM. NO HIGH-WATER MARK WAS WRITTEN
AND NONE WAS DUE.**
*(This block **replaces** the 09-17 08:11 pre-market reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — twenty-ninth consecutive
run.**)*
Selftest passed all five checks at **09:35 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,319.54 at pre-flight).

**⚠ THIS IS THE ONLY ROUTINE PERMITTED TO OPEN A POSITION, AND IT OPENED NOTHING.** It read an
**INACTIVE breaker**, a weekly cap at **0 of 3**, an **empty satellite sleeve**, **30.21% idle cash**
and **no restricting note in `control.md`** — full authority — and placed **zero orders, because the
plan it consumes carries no BUY intent.** **Nothing was blocked by a guardrail.** The 08:00/09:35 gap
exists precisely so a candidate reasoned into existence at the bell cannot become a fill; a run that
"found something" at 09:35 would not be diligent, it would be the failure this architecture is built
to prevent.

**`clock` READ `is_open: true` AT 09:35:56 WITH `next_close` 2026-09-17T16:00 TODAY AND `next_open`
2026-09-18T09:30 TOMORROW — the IN-SESSION shape, and the ONLY one of the three daily shapes where
the boolean alone is informative.** The pre-market read sixteen hours after the prior bell and the
post-bell read tonight will both carry `is_open: false` and differ only in the `next_open` **date**.
**Read the DATE, not the boolean.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares — **unchanged, no order has touched it since 09-03**, avg_entry
706.74, market_value $69,308.65, cost_basis $69,999.99, broker `current_price` **699.76**,
`lastday_price` **693.24**, unrealized_pl **−$691.34 / −0.988%**, `change_today` **+0.941%**).
**`current_price` 699.76 is a LIVE IN-SESSION MARK, not a close** — yesterday's official close is
**693.215** and `lastday_price` reads **693.24**, a third number again. **Never mix the two sources
in one comparison.** `alpaca.py sleeves`: equity **$99,307.66**, cash **$30,000.00**, core
**$69,307.66 = 69.79%**, satellite **0.0% (count 0)**, cash **30.21%**, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: +207.71` = **0.21% of equity.** **NO REBALANCE WAS DUE
AND NONE WAS PLACED** — §2 rebalances at the **band edge (65/75)**, not to the exact target.
**Twenty-second consecutive run inside a 0.39-point range (69.59–69.98)**: a drifting core mark on an
unchanged share count, not a position being added to or reduced.

**⚠ A FOURTH NUMBER APPEARED THIS RUN AND IT IS THE SAME MECHANISM, NOT A NEW DEFECT.** `sleeves`
reported core **$69,307.656284** and `positions`, called about a second later, reported market_value
**$69,308.646747** — **99 cents apart on an identical share count.** Both are **live intraday marks
pulled at different instants**, which is exactly what the solved two-price finding predicts. **It is
not a reconciliation break and must not be logged as one.** It is, however, the clearest preview yet
of why a `highest_close` must never be read from a `positions` field: **two calls one second apart
disagree, so a §5.4 stop set from either is set from noise.**

**STEP 4 — §5.1–§5.4 HAD NO SUBJECT. The plan carried ZERO SELL intents and there was nothing to
re-confirm against current prices.** Still the **nineteenth** session with an empty sleeve — the
count advances on **sessions, not runs**, and this run shares 09-17 with the pre-market run that
already advanced it. No thesis to test for invalidation (§5.1); no `timing_window` to expire (§5.2);
no `entry_price` to measure −7% against (§5.3); no `highest_close` to measure −10% against (§5.4).
**Nothing was near triggering because nothing exists to trigger.** `sell_rule_status` is **absent
rather than blank.** **All four remain untested code paths and §5.4 has never been armed** — it arms
on the first *satellite* fill. **The loss streak could not move: no position closed, so §6's counter
has no event to count.**

**NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE — READ, NOT ASSUMED.** **There is no
`highest_close` field in this file at all**, because there is no satellite block to carry one.
**ABSENT is a third state, distinct from "current and unchanged" and from "stale" — and it is the
only one carrying no date.** The missing date is exactly what discharges the midday backfill check.
**Zero `alpaca.py bars` calls were issued this run for any purpose**, and **core VOO was again
deliberately NOT stamped.** Writing a close into this file for the one position §5 exempts from all
four sell rules would fabricate a §5.4 stop; **it would not feel like a violation, it would feel like
tidiness.** Refused again.

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-17
(Thursday) is **2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday
2026-09-21. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`; `consecutive_closed_losses`
stays at **0** because nothing has ever closed in this account, so the §6 streak cannot move, no
`HALT_CLEARED_AT` comparison was required and **no circuit-breaker alert was due.** **Sleeve drift:**
core **69.79%**, inside the 65–75% band. `open_thesis_ids` stays **none** — nothing to add or remove;
all three of today's theses were rejected before the bell.

**⚠ OPEN ITEM (7) — `alpaca.py move` CANNOT SEE AN AFTER-HOURS EVENT, AND THIS RUN IS THE ONE WHOSE
RE-VALIDATION STEP INHERITS THAT BLINDNESS. IT COST NOTHING TODAY FOR A REASON THAT WILL NOT ALWAYS
HOLD.** The pre-market run found `move --symbol GNRC --sessions 5` returning **186.55 → 175.19,
−6.09%, `priced_in: true`** the morning after GNRC reportedly surged after the bell on the Amazon
supply agreement. **The five-session window ends at the last official close, so a candidate whose
news breaks AFTER the close is measured against prices that predate the news — and the gap does not
enter `bars` until tonight's close prints, meaning a 09:35 re-validation would have passed such a
candidate for the same wrong reason.** **Today's cost is zero only because there were no BUY intents
to re-validate** — the defect was never given a subject, which is **not** the same as the defect
being contained. **Open item (1) causes MISSED trades; this one would cause a trade TAKEN at exactly
the price the filter exists to refuse.** **No run may reinterpret the filter; that is a human editing
§4 or the script.**

**⚠ GNRC WAS NOT LOOKED AT, AND THE REFUSAL IS THE ENTRY WORTH KEEPING.** The plan named it as the
one ticker likely to be loudest on the tape this morning and instructed this run not to look. **Zero
`move`, `quote`, `bars` or `asset` calls were made on it.** There was a live pull toward pulling its
open "just to document open item (7)'s magnitude for the human" — a diagnostic, not a trade
consideration, and genuinely zero-risk on its own terms. **It was refused anyway, because the
habit it would establish is *looking at the loud ticker at 09:35*, and that habit is the exact
failure this 08:00/09:35 architecture exists to prevent.** GNRC is the **named counterparty** in the
Amazon announcement — **first-order, outside §4 at any price** — so no reading of it could have
produced an action. **The pre-market run already documented the defect with the same data. A second
measurement adds nothing and normalises the wrong reflex.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-15 12:35) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-one blocks spanning 09-01 to today's midday run each recorded the same
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
