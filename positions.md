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

**Reconciliation 2026-09-21 08:20 ET (1-premarket-research) — LEDGER AGREES WITH THE BROKER; ZERO
SATELLITE POSITIONS ON BOTH SIDES; WEEK ROLLED OVER CLEANLY AND THE ANCHORS MATCHED.**
*(This block **replaces** the 09-18 16:15 close reconciliation, read in full by this run — **one block
per date, not one per run.** **Collapse, do not append — thirty-sixth consecutive run.**)*
Selftest passed all five checks at **08:20 ET** (`trading_enabled: true`, LIVE paper account, equity
**$99,988.10** at pre-flight).

**`clock` READ `is_open: false` AT 08:20:11, WITH `next_open` 2026-09-21T09:30 — TODAY.** That is the
**pre-market** shape: the session **has not started yet**. **A holiday run reads the same boolean, and
so does a post-bell run.** The `next_open` **date** is what discriminates, and today's says a session
begins in 70 minutes. **Not a holiday. Read the date, not the boolean.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker; the core is deliberately untracked here per
§5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares, unchanged; no order has
touched it since the 09-03 fill**, avg_entry 706.74, cost_basis $69,999.99, market_value $69,988.10,
unrealized_pl **−$11.89 / −0.017%** on the broker mark. **That is the narrowest the core's reported
divergence has ever read, and it is still the 09-03 entry gap rather than tracking error** — measure it
from the **706.74 fill**, never from a prior VOO close.

**⚠ NINTH DOCUMENTED TWO-PRICE INSTANCE, AND THE GAP CHANGED SIGN OVER THE WEEKEND.** `lastday_price`
reads **701.78** against Friday's official close of **701.85** — **seven cents LOW**, where every
instance from 09-17 and 09-18 read **701.03 against 700.97, six cents HIGH**. **The field is named for
the prior day and is still not that day's close**; it is a carried live midpoint, and the sign of its
error is not stable either. `current_price` **706.62** is a **pre-market midpoint**, not a price anything
may be booked at. ⚠ **`unrealized_intraday_pl` reads +479.38 and must not be quoted as a day's P&L** —
it is computed off the stale `lastday_price` baseline, which is precisely the arithmetic that nearly put
**+$193.14** into Friday's headline in place of the true **+$87.16**. **`bars --adjustment all` for a
close, a fresh `quote` for execution, never a `positions` field for either, and never `last_equity` for
a day's P&L.**

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTY-FIRST SESSION.** No thesis to invalidate (§5.1),
no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no `highest_close`
to measure −10% against (§5.4). **`sell_rule_status` is ABSENT rather than blank**, and there is no
distance to record because there is no rule with an operand. The count advances on **sessions, not
runs**, and this is the **first read of 09-21** — later runs today must **not** advance it again.
**All four remain untested code paths. §5.4 is NOT ARMED; it arms on the first *satellite* fill.**
Core VOO taken out of the working list per §5's exemption.

**⚠ NO HIGH-WATER BACKFILL IS DUE, AND THIS RUN CONFIRMS IT BY READING RATHER THAN ASSUMING.** The
backfill trigger compares an `(as of …)` stamp against the last trading day. **There is no stamp to
compare**, because there is no `highest_close` to carry one. The marks are **ABSENT — a third state,
distinct from "stale" and from "current and unchanged"** — and **an absent field carries no date, which
is exactly what proves no backfill is due.** The 09-18 close run wrote this in terms precisely so today
would not misread it: **that run executed its Step 2 and Step 2 had no operand. Nothing was skipped.**
**Zero `alpaca.py bars` calls were issued for a high-water purpose and none was due.**

**CORE VOO DELIBERATELY NOT STAMPED.** §5 exempts core from all four sell rules, so it has no row here
and no `highest_close`. **Stamping it would fabricate a §5.4 trailing stop on the one position the
strategy exempts.** Refused, for the thirty-sixth run. *(Today the pull was weaker than usual only
because this run had no reason to pull VOO `bars` at all — a research run prices nothing. Note that the
refusal was therefore cheap today, which says nothing about the close run's version of it at 16:00.)*

**NO TRADES, NOTHING IN LIMBO.** No order has been placed since the 09-03 core VOO buy
(`d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled, terminal). **Routine 1 places no orders by design**, so
this run placed none and `trade_log.md` is correctly left unappended — **a run with no fill writes no
trade entry** (§7). **Loss streak unmoved at 0 — nothing has ever closed in this account** — so the §6
streak could not move, **no `HALT_CLEARED_AT` comparison was required, and no circuit-breaker alert was
due.**

**SLEEVES IN BAND; NO REBALANCE DUE.** `alpaca.py sleeves`: equity **$99,988.10**, cash **$30,000.00**,
core **$69,988.10 = 70.0%**, satellite **0.0% (count 0)**, cash **30.0%**, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: +3.57 = 0.004% of equity` — **the narrowest delta in the
account's history**, against a prior range of $111.73–$212.46. §2 acts at the **band edge (65/75)**, not
at the target, so the delta is not an action at any size inside the band — **and §2 places a rebalance at
the next market-open run in any case, which this is not.** **Twenty-ninth consecutive run inside a
0.41-point range (69.59–70.00).**

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** today is **Monday 2026-09-21**, the ISO
Monday of its own week, and `week_of` **already reads 2026-09-21** because **Friday's review advanced it
ahead of the boundary**. **The anchors match, so no reset was due and none was performed** —
`new_positions_this_week` stays **0 of 3**. **That is the mechanism working as designed, not a skipped
check**, and it is worth stating because a run that finds nothing to do here is indistinguishable from
one that never looked. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`,
`consecutive_closed_losses: 0` — **new positions were fully permitted this run and none was proposed.**
**Sleeve drift:** core **70.0%**, inside the band, no REBALANCE intent queued.

**⚠ GNRC NOT LOOKED AT FOR THE EIGHTH CONSECUTIVE RUN, AND THE PREDICTED EIGHTH COSTUME ARRIVED ON
SCHEDULE.** The version available to a Monday research run is: *"the 09-16 after-hours gap is now three
sessions deep in `bars`, so a clean `move` reading finally exists — pulling it would let open item (7)
be CLOSED with a number rather than left open for the human."* **It is the first of the eight that
proposes to do the HUMAN'S work rather than the agent's**, which is what makes it the most
useful-sounding. **Refused, on two facts independent of the wording:** open item (7) states that **no
run may reinterpret the filter — that is a human editing §4 or `alpaca.py move`** — so **no number this
seat could collect would close it**; and **GNRC is the named counterparty in the Amazon announcement,
first-order and outside §4 at any price.** **Zero `move`/`quote`/`bars`/`asset` calls, eight runs
running.** **The costumes: diligence, curiosity, tidiness, completeness, zero-marginal-cost, self-audit,
proxy-procurement, issue-closure — eight seats, eight distinct rationales, no repeats.** **Expect a
ninth at the bell.**

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
