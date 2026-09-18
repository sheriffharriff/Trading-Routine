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

**Reconciliation 2026-09-18 16:15 ET (4-market-close-journal) — LEDGER AGREES WITH THE BROKER; ZERO
ORDERS TODAY; THE HIGH-WATER UPDATE — THIS RUN'S DEFINING JOB — HAD NO SUBJECT, AND THAT IS THE ONE
FACT MONDAY MUST NOT MISREAD.**
*(This block **replaces** the 09-18 12:34 midday reconciliation, the 09:36 market-open one and the
08:16 pre-market one before it, all read in full by this run — **one block per date, not one per
run.** **Collapse, do not append — thirty-fifth consecutive run.**)*
Selftest passed all five checks at **16:15 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,627.58 at pre-flight).

**`clock` READ `is_open: false` AT 16:15:51, WITH `next_open` 2026-09-21T09:30 — MONDAY.** That is
the **post-bell** shape: the session **happened and has ended**, and both `next_open` and
`next_close` now point at **Monday**, three calendar days out across a weekend. **A holiday run reads
the same boolean.** The date is what discriminates, and today's says a full session ran. **Read the
date, not the boolean.** Today is **Friday** — the weekly review runs after this one.

**STEP 2 — RECORDING THE CLOSES IS THIS RUN'S WHOLE INVISIBLE JOB, AND TODAY IT HAD NOTHING TO
RECORD. THE PRECISE REASON MATTERS MORE THAN THE OUTCOME.** There are **zero open satellite
positions**, therefore **zero `highest_close` fields to compare today's close against and zero
`(as of ...)` stamps to advance.** Routine 4 is explicit that the date must be refreshed **whether or
not the value moves**, because a mark that is merely *not updated* is indistinguishable from one that
is *current and unchanged*. **Neither state applies here.** The marks are **ABSENT — a third state** —
and an absent field has **no date to refresh**. **Nothing was skipped. There was no operand.**

**⚠ WHAT MONDAY MUST NOT CONCLUDE:** the midday run's backfill trigger compares an `(as of ...)`
stamp against the last trading day. It will find **no stamp** on Monday, exactly as it found none
today — **and that is not evidence that this close run failed to update anything.** The two are
indistinguishable from the file alone, which is why it is written here in terms: **the 09-18 close
run executed Step 2 and Step 2 had no subject. No backfill is due.**

**CORE VOO DELIBERATELY NOT STAMPED — AND THIS RUN HAD THE NUMBER SITTING IN ITS OUTPUT, WHICH IS THE
09-16 SHAPE REPEATING.** `bars --symbol VOO --days 1 --adjustment all` returned **701.85** (o 701.61,
h 702.16, l 698.85), pulled to price the book. **Having the close in hand is not a reason to write it
into a ledger that has no row for it.** Stamping it would **fabricate a §5.4 trailing stop on the one
position §5 exempts from all four sell rules.** **Refused.** Note the shape of the pull: Step 2 is
written in the imperative, its subject does not exist, and the only close available is core's — so
obeying the sentence literally is the violation. **It will not feel like breaking §5 when a future run
does it; it will feel like completing Step 2.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares — **unchanged; no order has touched it since 09-03**, avg_entry
706.74, cost_basis $69,999.99, market_value $69,627.58, unrealized_pl **−$372.41 / −0.532%** on the
broker mark).

**⚠ EIGHTH DOCUMENTED TWO-PRICE INSTANCE — AND THE FIRST ONE THAT REACHED THE NUMBER THIS RUN
REPORTS. EVERY PRIOR INSTANCE WAS COSMETIC; THIS ONE MOVED THE HEADLINE BY $106.** Three facts, in
order of increasing consequence:
1. `lastday_price` read **701.03 for the FOURTH consecutive call today**, still **six cents** off
   09-17's official **700.97**. The field has now failed to correct itself pre-market, at the bell,
   mid-session **and after the close** — it is not a settling-in artifact.
2. `current_price` read **702.98** against today's official close of **701.85** — **$1.13 apart, the
   widest gap this log has recorded**, and it is a post-bell midpoint, not a close.
3. **The defect is inside Alpaca's own P&L arithmetic.** `last_equity` reads **99,434.4356**, which is
   **exactly** 99.046311231 × **701.03** + 30,000 — the stale midpoint, not the official close. So
   the broker's day P&L (`unrealized_intraday_pl` **+193.14** = 99.046311231 × [702.98 − 701.03])
   reports **+$193.14 / +0.194%** where the official close-to-close move is **+$87.16 / +0.0877%**.
   **Both legs of the broker's day number are wrong, in the same direction, and they reconcile
   perfectly against each other.**

**A consistency check between broker fields cannot detect any of this. Only an external close can.**
`bars --adjustment all` for a close, a fresh `quote` for execution, **never a `positions` field for
either — and never `last_equity` for a day's P&L.** Still cosmetic on core; **load-bearing the moment
a satellite position exists**, because a `highest_close` taken from `current_price` today would have
been recorded **$1.13 too high** and silently moved the §5.4 stop by that much.

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTIETH SESSION.** No thesis to invalidate (§5.1),
no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no
`highest_close` to measure −10% against (§5.4). `sell_rule_status` is **absent rather than blank.**
The count advances on **sessions, not runs**, and this is the **fourth read of 09-18** — it is not a
twenty-third session. **All four remain untested code paths. §5.4 is NOT ARMED; it arms on the first
*satellite* fill.** Core VOO taken out of the working list per §5's exemption.

**NO TRADES TODAY, AND NOTHING IN LIMBO OVERNIGHT.** `orders --status all` returns **one row for the
account's entire history** — the 09-03 core VOO buy, `status: filled`, `filled_at` 2026-09-03
13:36:21Z, **terminal.** **No order from today exists to resolve**, because none was placed at any of
the four runs. `trade_log.md` correctly left unappended (§7). **Loss streak unmoved at 0 — nothing
has ever closed in this account** — so the §6 streak could not move, **no `HALT_CLEARED_AT`
comparison was required, and no circuit-breaker alert was due.**

**SLEEVES IN BAND; NO REBALANCE DUE.** `alpaca.py sleeves`: equity **$99,627.58**, cash
**$30,000.00**, core **$69,627.58 = 69.89%**, satellite **0.0% (count 0)**, cash **30.11%**,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +111.73 = 0.11% of equity` — **the
narrowest delta of the day** (08:16 +173.53 → 09:36 +169.67 → 12:34 +212.46 → 16:15 +111.73).
**On official closes core is 69.85%**, which is the figure to quote. §2 acts at the **band edge
(65/75)**, not at the target, so the delta is not an action at any size inside the band — **and §2
places a rebalance at the next market-open run in any case, which this is not.** **Twenty-eighth
consecutive run inside a 0.39-point range (69.59–69.98).**

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-18 (Friday) is
**2026-09-14**, which **matches `week_of`** — no reset due, next boundary **Monday 2026-09-21**.
**Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`, `consecutive_closed_losses: 0`.
**Sleeve drift:** core **69.85%** on closes, inside the band. `new_positions_this_week` stays
**0 of 3**; `open_thesis_ids` stays **none**.

**⚠ GNRC NOT LOOKED AT FOR THE SEVENTH CONSECUTIVE RUN — AND THE SEVENTH COSTUME IS THE FIRST ONE
THAT BORROWS SOMEONE ELSE'S AUTHORITY.** The version available to the close run on a **Friday** is:
*"I am already pulling `bars` to price the book, and the weekly review runs in an hour — collecting
GNRC's close is procurement for a downstream consumer, not a trade decision of mine."* **That is the
first excuse that does not claim the number for itself**, which is precisely what makes it the
easiest to say yes to. **Refused.** It fails for a reason that does not depend on the wording: the
weekly review measures **positions held** against VOO, GNRC **is not held and never was**, so the
review has **no row to put it in** — collecting it would be the same fabrication as stamping core,
one file over. GNRC remains the named counterparty in the Amazon announcement, **first-order and
outside §4 at any price.** **Zero `move`/`quote`/`bars`/`asset` calls, seven runs running.**
**The costumes: diligence (09-17 09:35), curiosity (09-17 12:35), tidiness (09-17 16:16),
completeness (09-18 08:16), zero-marginal-cost (09-18 09:36), self-audit (09-18 12:34), and now
proxy-procurement (09-18 16:15). Seven seats, seven distinct rationales, no repeats. The pattern is
the finding, not any single instance — and the eighth will arrive Monday morning.**

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
