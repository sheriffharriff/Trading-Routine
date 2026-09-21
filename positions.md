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

**Reconciliation 2026-09-21 09:36 ET (2-market-open-execution) — LEDGER AGREES WITH THE BROKER; ZERO
SATELLITE POSITIONS ON BOTH SIDES; ZERO ORDERS PLACED AND THE PLAN WAS VERIFIED FRESH BEFORE THAT WAS
DECIDED.**
*(This block **replaces** the 09-21 08:20 pre-market reconciliation, read in full by this run — **one
block per date, not one per run.** **Collapse, do not append — thirty-seventh consecutive run.**)*
Selftest passed all five checks at **09:35 ET** (`trading_enabled: true`, LIVE paper account, equity
**$99,971.27** at pre-flight).

**`clock` READ `is_open: TRUE` AT 09:36:09**, `next_close` **2026-09-21T16:00**, `next_open`
**2026-09-22T09:30**. **The session is open and this is the first shape this week that the boolean
settles on its own** — the three runs before it each had to discriminate holiday from pre-market from
post-bell on the `next_open` **date**. Worth recording precisely because it is the easy case.

**⚠ THE STALE-PLAN GATE WAS EXERCISED AND PASSED: `plan_date` 2026-09-21 vs today in ET 2026-09-21.**
The plan is **FRESH**, and **its emptiness is the plan rather than a gap in it.** ⚠ **An empty-but-
current plan and a stale plan produce IDENTICAL zero-order runs**, so nothing in the order count could
ever distinguish them — **only the date does.** **Twenty-second exercise, twenty-second non-firing; the
alert path remains UNTESTED CODE**, and twenty-two quiet opens are not evidence it works.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker; the core is deliberately untracked here per
§5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares, unchanged; no order has
touched it since the 09-03 fill**, eighteen sessions ago. avg_entry **706.74**, cost_basis
**$69,999.99**, market_value **$69,972.26**, unrealized_pl **−$27.73 / −0.04%** on the broker mark —
**still the 09-03 entry gap, never tracking error.** Measure it from the **706.74 fill**, never from a
prior VOO close.

**SLEEVES IN BAND; STEP 7 EVALUATED AND CORRECTLY DECLINED.** `alpaca.py sleeves`: equity
**$99,972.26**, cash **$30,000.00**, core **$69,972.26 = 69.99%**, satellite **0.0% (count 0)**, cash
**30.01%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: 8.32` — **0.008% of
equity.** §2 rebalances at the **65/75 band edge, not to the exact 70% target**, so no delta inside the
band is an action at any size. **Thirtieth consecutive run inside a 0.41-point range (69.59–70.00).**

**⚠ NINTH TWO-PRICE INSTANCE PERSISTED INTO THE SESSION — AND WAS PRICED IN DOLLARS AT AN OPEN FOR THE
FIRST TIME.** `lastday_price` **still reads 701.78** against Friday's official close of **701.85** —
**seven cents LOW**, the same instance carried across the bell rather than a tenth. Because
`change_today` (**+0.667%**) and `unrealized_intraday_pl` (**+463.54**) are **both computed off that
stale baseline**, the broker's implied day-P&L is overstated by **99.046311231 × $0.07 = $6.93** —
*before* the separate objection that **`current_price` 706.46 is a live in-session midpoint, not a
close.** **09-18's version of the identical arithmetic was wrong by $106.** ⚠ **The mechanism is the
same and only the gap differs; the gap is not something a run controls, so the small number today is
not reassurance.** **Neither figure was quoted as a day's P&L. `bars --adjustment all` for a close, a
fresh `quote` for execution, never a `positions` field for either, and never `last_equity`.**

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTY-SECOND SESSION.** No thesis to invalidate
(§5.1), no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no
`highest_close` to measure −10% against (§5.4). **`sell_rule_status` is ABSENT rather than blank.** The
count advances on **sessions, not runs** — the 08:20 run was the first read of 09-21 and this is the
second, so the session counter moves **once**, from twenty-one to twenty-two, on the date and not on
this run. **All four remain untested code paths. §5.4 is NOT ARMED; it arms on the first *satellite*
fill.** Core VOO taken out of the working list per §5's exemption.

**ZERO `alpaca.py move` CALLS AND THAT IS AN ABSENT CHECK, NOT A SKIPPED ONE.** Step 5 re-validation
has a subject only when a BUY intent exists; the plan carried **none**, so there was no candidate to
re-price and no priced-in reading to take. **A run that placed no orders because it had nothing to
place is not the same as a run that skipped its checks, and the distinction is only legible if the
absence is stated.**

**⚠ NO HIGH-WATER BACKFILL WAS DUE, AND THIS RUN CONFIRMED IT BY READING RATHER THAN ASSUMING.** The
backfill trigger compares an `(as of …)` stamp against the last trading day. **There is no stamp to
compare**, because there is no `highest_close` to carry one. The marks are **ABSENT — a third state,
distinct from "stale" and from "current and unchanged"** — and **an absent field carries no date, which
is exactly what proves no backfill is due.** **Nothing was skipped.** Zero `bars` calls were issued for
a high-water purpose and none was due.

**CORE VOO DELIBERATELY NOT STAMPED.** §5 exempts core from all four sell rules, so it has no row here
and no `highest_close`. **Stamping it would fabricate a §5.4 trailing stop on the one position the
strategy exempts.** Refused, for the thirty-seventh run.

**NO TRADES, NOTHING IN LIMBO.** No order has been placed since the 09-03 core VOO buy
(`d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled, terminal). **This run placed none**, so `trade_log.md`
is correctly left unappended — **a run with no fill writes no trade entry** (§7). **There is no order in
a non-terminal state anywhere in this account's history**, and that is the single most important thing
an execution run can report. **Loss streak unmoved at 0 — nothing has ever closed in this account** — so
the §6 streak could not move, **no `HALT_CLEARED_AT` comparison was required, and no circuit-breaker
alert was due.**

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** today is **Monday 2026-09-21**, the ISO
Monday of its own week, and `week_of` **already reads 2026-09-21** because **Friday's review advanced it
ahead of the boundary**. **The anchors match, so no reset was due and none was performed** —
`new_positions_this_week` stays **0 of 3**. **That is the mechanism working as designed, not a skipped
check**, and it is worth stating because a run that finds nothing to do here is indistinguishable from
one that never looked. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`,
`consecutive_closed_losses: 0` — **new positions were fully permitted this run and none was proposed.**
**Sleeve drift:** core **69.99%**, inside the band, **no rebalance executed and none due.**

**⚠ GNRC NOT LOOKED AT FOR THE NINTH CONSECUTIVE RUN — AND THE PREDICTED NINTH COSTUME DID NOT ARRIVE,
FOR A REASON THAT WEAKENS THE RECORD RATHER THAN STRENGTHENING IT.** The 09-21 pre-market run closed
with *"expect a ninth at the bell."* **No ninth framing presented itself, and the honest explanation is
not restraint: there was nowhere for it to hide.** The plan carried **zero BUY intents and therefore
zero re-validations**, so **this run had no pricing step at all** — a GNRC pull would have had to be
**invented from nothing** rather than attached to a `move`/`quote` call that was already happening.
⚠ **That makes today a WEAKER test of the refusal than the eight runs before it, not a stronger one, and
the prediction is neither confirmed nor refuted.** **Watch for the ninth on the next run that has a
genuine pricing step.** The two standing facts are unchanged: **open item (7) says no run may
reinterpret the priced-in filter — that is a human editing §4 or `alpaca.py move`**, so no number this
seat could collect would close it; and **GNRC is the named counterparty in the Amazon announcement,
first-order and outside §4 at any price.** **Zero `move`/`quote`/`bars`/`asset` calls, nine runs
running.** Costumes so far: diligence, curiosity, tidiness, completeness, zero-marginal-cost,
self-audit, proxy-procurement, issue-closure.

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
