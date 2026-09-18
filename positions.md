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

**Reconciliation 2026-09-18 12:34 ET (3-midday-management) — LEDGER AGREES WITH THE BROKER; ZERO
ORDERS PLACED; NO POSITION TO MANAGE, NO HIGH-WATER MARK TO REPAIR, NO SELL RULE WITH A SUBJECT.**
*(This block **replaces** the 09-18 09:36 market-open reconciliation and the 08:16 pre-market one
before it, both read in full by this run — **one block per date, not one per run.** **Collapse, do
not append — thirty-fourth consecutive run.**)*
Selftest passed all five checks at **12:34 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,294.36 at pre-flight).

**`clock` READ `is_open: TRUE` AT 12:34:56**, with `next_close` **2026-09-18T16:00 — TODAY** and
`next_open` **2026-09-21T09:30 — MONDAY**. The **intraday shape**, and the only one of the four that
needs no date to disambiguate: `is_open: true` is unambiguous, where `is_open: false` is shared by a
pre-market run and a post-bell run and is resolved only by the `next_open` DATE. Today is **Friday** —
the weekly review runs after the close.

**STEP 1 — THE ROUTINE'S OWN EXIT CONDITION FIRED, AND IT IS A LEGITIMATE END TO THE RUN, NOT A
SHORTFALL.** Routine 3's Step 1 says in terms: *no open satellite positions → there is nothing to
manage; note it, commit, exit; do not go looking for something to do.* That is the branch this run
took, on the third consecutive read of an empty sleeve today.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares — **unchanged, no order has touched it since 09-03**, avg_entry
706.74, cost_basis $69,999.99, market_value $69,291.81, unrealized_pl **−$708.18 / −1.012%**).

**⚠ SEVENTH DOCUMENTED TWO-PRICE INSTANCE, AND THE SUB-SHAPE FROM 09:36 DID NOT SURVIVE TO MIDDAY —
WHICH IS THE POINT.** `lastday_price` read **701.03 for the THIRD consecutive call today**, still
**six cents off 09-17's official close of 700.97**, so the field has now failed to correct itself
pre-market, at the bell, and three hours into the session. But `current_price` has **unstuck** —
699.59 against 09:36's 701.03 — and `change_today` now reads **−0.00205**, which is exactly
701.03 → 699.59. **So the fields are now internally consistent with each other and still wrong about
the prior close**, because `change_today` is computed off `lastday_price` rather than off the
official close. **The 09:36 flat was a stale midpoint; this is a live midpoint measured against a
stale baseline. Same defect, two different appearances in one session, and neither one announces
itself.** `bars --adjustment all` for a close, a fresh `quote` for execution, **never a `positions`
field for either.** Cosmetic on core; **load-bearing the moment a satellite position exists.**

**STEP 2 — HIGH-WATER REPAIR HAD NO SUBJECT, AND THE ABSENCE OF A DATE IS WHAT PROVED IT.** The
backfill trigger compares the `(as of ...)` stamp on a `highest_close` against the last trading day.
**There is no `highest_close` in this file to carry a stamp** — the marks are **ABSENT, a third state
distinct from "current" and from "stale"** — so the comparison has no operands and **no `bars` call
was due for a high-water purpose. Zero were issued.** This is the one step of routine 3 whose whole
purpose is to catch a silent failure, and it is worth being precise about why it stayed silent here:
**not because the marks checked out, but because there are none.**

**STEP 3 — THE §5.1–§5.4 ORDERED EVALUATION NEVER STARTED.** No thesis to invalidate (§5.1), no
`timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no `highest_close`
to measure −10% against (§5.4). `sell_rule_status` is **absent rather than blank**. **Zero Perplexity
invalidation queries were issued and none was due** — §5.1 reads an `invalidation` line that does not
exist, so it is an **absent check, not a skipped one**, and a run that manufactured the call would be
inventing a subject. **Still the TWENTIETH session with an empty sleeve** — the count advances on
**sessions, not runs**, and this is the **third read of 09-18**, not a twenty-second. **All four
remain untested code paths. §5.4 is NOT ARMED; it arms on the first *satellite* fill.** Core VOO was
taken out of the working list per §5's exemption, as the routine directs.

**STEP 4 — NO EXITS, THEREFORE NO STREAK MOVEMENT AND NO ALERT.** Zero `sell` calls. **Loss streak
unmoved at 0** because nothing has ever closed in this account, so the §6 streak could not move, **no
`HALT_CLEARED_AT` comparison was required**, and **no circuit-breaker alert was due**. `trade_log.md`
correctly left unappended — §7 forbids entries for orders that do not exist to verify.

**⚠ STEP 4's DRY-RUN BRANCH WAS NOT EXERCISED, AND THAT IS NOT REASSURANCE.** `TRADING_ENABLED` is
**true**, so a triggered exit would have been submitted for real. The routine's most important line —
*a stop that should have fired and did not* — **had nothing to report because nothing could have
fired.** A future run must not read a string of these as evidence the exit path works.

**STEP 5 — NOTHING TO UPDATE.** No position survived to carry a refreshed `sell_rule_status`, because
none existed to begin with.

**SLEEVES IN BAND, AND THIS RUN DID NOT ACT ON THEM BECAUSE IT MAY NOT.** `alpaca.py sleeves`: equity
**$99,291.81**, cash **$30,000.00**, core **$69,291.81 = 69.79%**, satellite **0.0% (count 0)**, cash
**30.21%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +212.46 = 0.21% of
equity` — wider than 09:36's +169.67 as core drifted down on the session. §2 acts at the **band edge
(65/75)**, not at the target, so the delta is not an action at any size inside the band — **and §2
places a rebalance at the next MARKET-OPEN run in any case, which this is not.** **Twenty-seventh
consecutive run inside a 0.39-point range (69.59–69.98).**

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-18 (Friday) is
**2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday 2026-09-21.
**Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`, `consecutive_closed_losses: 0`.
**Sleeve drift:** core **69.79%**, inside the band. `new_positions_this_week` stays **0 of 3** and
`open_thesis_ids` stays **none**.

**CORE VOO DELIBERATELY NOT STAMPED — AND THE MIDDAY RUN IS THE SEAT WHERE THAT PULL IS STRONGEST,
BECAUSE STEP 2 IS WRITTEN IN THE IMPERATIVE AND ITS SUBJECT DOES NOT EXIST.** "Repair the high-water
marks first" reads as an instruction to produce a mark, and the only close available to produce one
from is core's. **Writing it would fabricate a §5.4 trailing stop on the one position §5 exempts from
all four sell rules. Refused — and note it would have felt like completing Step 2, not like breaking
§5.** Zero `bars` calls were issued for any purpose, so unlike the 09-16 close run this one did not
even have the number sitting in its output.

**⚠ GNRC NOT LOOKED AT FOR THE SIXTH CONSECUTIVE RUN — AND THE SIXTH COSTUME WAS PREDICTED AND
ARRIVED.** The version available to an exits-only run is the narrowest yet: *"I am the run that
manages positions; checking whether the thing I refused to buy has moved is just measuring the cost
of the refusal."* **That one is not even a trade rationale — it is a self-audit, which is why it is
the most plausible of the six.** Zero `move`, `quote`, `bars` or `asset` calls, **six runs running.**
GNRC is the named counterparty in the Amazon announcement — **first-order, outside §4 at any price**,
and **routine 3 may not open a position under any circumstance**, so there is no version of looking
at it that could produce an action. **The excuses continue to improve; that remains the finding.**

**⚠ NO POSITION WAS OPENED AND NONE COULD HAVE BEEN. Routine 3 is exits-only.** The run read an
**INACTIVE breaker, a weekly cap at 0 of 3, an empty sleeve and 30.21% idle cash** — full authority on
every gate the scripts check — **from the one seat in the system that is forbidden to use it.** Carry-
forward item (3)'s structurally undeployed sleeve is **not licence for a midday entry**; new positions
route through pre-market research plus the 09:35 execution run, **always**, because that path is what
forces every buy to sleep on a written thesis. A midday entry would **route around the discipline
rather than satisfy it.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-18 08:16) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-five blocks spanning 09-01 to this morning's pre-market run each recorded the same
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
