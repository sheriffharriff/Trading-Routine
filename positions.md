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

**Reconciliation 2026-09-21 12:35 ET (3-midday-management) — LEDGER AGREES WITH THE BROKER; ZERO
SATELLITE POSITIONS ON BOTH SIDES; NO EXIT TAKEN, NO EXIT WITHHELD, AND NO EXIT DUE.**
*(This block **replaces** the 09-21 09:36 market-open reconciliation, read in full by this run — **one
block per date, not one per run.** **Collapse, do not append — thirty-eighth consecutive run.**)*
Selftest passed all five checks at **12:34 ET** (`trading_enabled: true`, LIVE paper account, equity
**$100,500.09** at pre-flight).

**`clock` READ `is_open: TRUE` AT 12:35:12**, `next_close` **2026-09-21T16:00**, `next_open`
**2026-09-22T09:30** — a genuine midday session read, not a holiday and not a post-bell shape.

**THIS RUN HAD NO SUBJECT AND STOPPED, WHICH IS THE INSTRUCTION AND NOT A SHORTFALL.** Routine 3 is
**exits-only by construction** — it may not open a position under any circumstance — and with an empty
satellite sleeve there was nothing to exit. The routine's own words: *note it, commit, exit; do not go
looking for something to do.* **29.85% idle cash and an unused 0-of-3 weekly cap are not an
opportunity this seat may act on.** A midday entry would route *around* the pre-market research and
09:35 execution path, which is the whole point of that path.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker; the core is deliberately untracked here per
§5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares, unchanged; no order has
touched it since the 09-03 fill**, eighteen sessions ago, avg_entry **706.74**, cost_basis
**$69,999.99**.

**⚠ STEP 2 (HIGH-WATER REPAIR) RAN AND FOUND NO OPERAND — AND THIS IS THE RUN THE 09-18 CLOSE NOTE WAS
ADDRESSED TO.** That note predicted the midday backfill trigger *"will find no stamp on Monday."*
**It was correct.** The trigger compares an `(as of …)` stamp against the last trading day; **there is
no stamp to compare**, because there is no `highest_close` to carry one. The marks are **ABSENT — a
third state, distinct from "stale" and from "current and unchanged"** — and **an absent field carries
no date, which is exactly what proves no backfill is due.** **Zero `bars` calls were issued for a
high-water purpose and none was due. Nothing was skipped.**

**ZERO `quote` CALLS IN TOTAL, AND THAT IS AN ABSENT CHECK RATHER THAN A SKIPPED ONE.** Step 1 says to
quote *every open satellite ticker*; there are none, so there was no symbol to pass. A run that issued
no price call because it had no position to price is not the same as a run that skipped its checks, and
the distinction is only legible if the absence is stated.

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTY-THIRD SESSION.** No thesis to invalidate
(§5.1), no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no
`highest_close` to measure −10% against (§5.4). **`sell_rule_status` is ABSENT rather than blank.**
**All four remain untested code paths. §5.4 is NOT ARMED; it arms on the first *satellite* fill.**
Core VOO taken out of the working list per §5's exemption.

**CORE VOO DELIBERATELY NOT STAMPED.** §5 exempts core from all four sell rules, so it has no row here
and no `highest_close`. **Stamping it would fabricate a §5.4 trailing stop on the one position the
strategy exempts.** Refused, for the thirty-eighth run.

**⚠ THE ONE FINDING OF THIS RUN IS A DATA-QUALITY FLAG, AND IT IS NEW: TODAY'S ENTIRE BROKER INTRADAY
BLOCK IS ONE ROUND NUMBER PROPAGATED THREE WAYS.** `current_price` **711.78** minus `lastday_price`
**701.78** is **exactly $10.000**; `unrealized_intraday_pl` **990.463112** is **exactly
99.046311231 × 10.00** to the cent; `change_today` **0.01425** is exactly **10 ÷ 701.78**. ⚠ **Real
quotes do not land on whole dollars.** **Treat 711.78 as a synthetic or coarsely-quantised paper mark
until an official close confirms it, and do not carry it into any return figure.** **The 16:00 close
run is the first run that can settle this** — if Monday's official VOO close is not 711.78, that is
the answer.
**Consequence: the core's broker mark is POSITIVE FOR THE FIRST TIME IN THIS ACCOUNT'S HISTORY** —
`unrealized_pl` **+$499.19 / +0.713%**, against a run of small negatives — **and it is positive only on
that suspect midpoint.** 711.78 is above the **706.74** fill, so **the sign is probably real; the
magnitude is not yet a fact.** ⚠ **Measure the core from the 706.74 fill and from an official close,
never from a `positions` field.**

**⚠ NINTH TWO-PRICE INSTANCE IS NOW THREE READS DEEP ON A SINGLE INSTANCE.** `lastday_price` **still
reads 701.78** against Friday's official close of **701.85** — **seven cents low at 08:20, at 09:36 and
again at 12:35.** This is the **first direct evidence that the defect persists through a whole session
rather than clearing at the bell**, and it is the same instance carried across, not a tenth. The
broker's implied day-P&L is overstated by **99.046311231 × $0.07 = $6.93** at every one of the three
reads — *before* the separate and today much larger objection above. **No run today has quoted either
figure as a day's P&L.** `bars --adjustment all` for a close, a fresh `quote` for execution, never a
`positions` field for either, and never `equity − last_equity`.

**SLEEVES IN BAND, BUT THE BAND MOVED AND THE DELTA CHANGED SIGN.** `alpaca.py sleeves`: equity
**$100,499.18**, cash **$30,000.00**, core **$70,499.18 = 70.15%**, satellite **0.0% (count 0)**, cash
**29.85%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: −149.76` — **−0.149% of
equity.** **70.15% is the first reading above 70.00 in thirty-one runs**, against a prior band of
**69.59–70.00**, and **the delta is negative for the first time — core is now ABOVE target rather than
below.** §2 rebalances at the **65/75 band edge, not to the exact 70% target**, so **no delta inside
the band is an action at any size**, in either direction. Rebalance is a market-open step in any case
and not this run's to take.

**NO TRADES, NOTHING IN LIMBO.** No order has been placed since the 09-03 core VOO buy
(`d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled, terminal). **This run placed none**, so `trade_log.md`
is correctly left unappended — **a run with no fill writes no trade entry** (§7). **There is no order in
a non-terminal state anywhere in this account's history. Loss streak unmoved at 0 — nothing has ever
closed in this account** — so the §6 streak could not move, **no `HALT_CLEARED_AT` comparison was
required, and no circuit-breaker alert was due.** Breaker **INACTIVE**, `halt_triggered_at: none`.

**HOUSEKEEPING — WEEK ROLLOVER CHECKED, ANCHORS MATCHED, NO RESET DUE.** Today is **Monday
2026-09-21**, the ISO Monday of its own week, and `week_of` **already reads 2026-09-21** because
**Friday's review advanced it ahead of the boundary**. **Third consecutive run to find the reset
already done** — `new_positions_this_week` stays **0 of 3**. **That is the mechanism working as
designed, not a skipped check.**

**⚠ GNRC NOT LOOKED AT FOR THE TENTH CONSECUTIVE RUN — AND IT IS THE SECOND WEAK TEST IN A ROW, FOR THE
SAME STRUCTURAL REASON.** This run issued **zero price calls of any kind**, so a GNRC pull would have
had to be **invented from nothing** rather than attached to a call that was already happening. ⚠ **Two
weak tests in a row do not add up to one strong one**; the ninth costume predicted on 09-21 pre-market
is **still neither confirmed nor refuted.** **Watch the 09-23 pre-market run** — it will price GIS and
therefore carries a genuine `move`/`quote` step for a pull to attach itself to. The disqualifying facts
do not depend on the wording: **routine 3 may not open a position under ANY circumstance**, so no
reading could produce an action; and **GNRC is the named counterparty in the Amazon announcement,
first-order and outside §4 at any price.** **Zero `move`/`quote`/`bars`/`asset` calls, ten runs
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
