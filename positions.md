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

**Reconciliation 2026-09-18 09:36 ET (2-market-open-execution) — LEDGER AGREES WITH THE BROKER;
ZERO ORDERS PLACED OF ANY KIND; NO HIGH-WATER MARK RECORDED BECAUSE THERE IS NO POSITION TO
RECORD ONE FOR.**
*(This block **replaces** the 09-18 08:16 pre-market reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — thirty-third consecutive run.**)*
Selftest passed all five checks at **09:36 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,435.43 at pre-flight).

**`clock` READ `is_open: TRUE` AT 09:36:21**, with `next_close` **2026-09-18T16:00 — TODAY** and
`next_open` **2026-09-21T09:30 — MONDAY**. **This is the intraday shape, and it is the only one of
the four that needs no date to disambiguate:** `is_open: true` is unambiguous, where `is_open: false`
is shared by a pre-market run and a post-bell run and is resolved only by the `next_open` DATE.
Today is **Friday** — the weekly review runs after the close.

**⚠ THE STALENESS GATE WAS CHECKED AND DID NOT FIRE.** `plan_date` reads **2026-09-18** and today's
ET date **is 2026-09-18**. The plan is **FRESH**, so **its emptiness is the plan and not a gap in
it** — and that distinction is the whole reason the date is read rather than the outcome, because
**a fresh empty plan and a stale plan produce identical zero-order runs.** **Twenty-first
consecutive non-firing; the alert path REMAINS UNTESTED CODE.** Twenty-one quiet opens are not
evidence the gate works. **The first morning it fires will be a morning the pre-market run failed —
exactly the morning with no fresh notes to lean on. Read Step 2 then; do not recall it.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares — **unchanged, no order has touched it since 09-03**, avg_entry
706.74, cost_basis $69,999.99, market_value $69,434.44, unrealized_pl **−$565.55 / −0.808%**).

**⚠ SIXTH DOCUMENTED TWO-PRICE INSTANCE, AND IT CARRIES A NEW SUB-SHAPE WORTH MORE THAN THE COUNT.**
`lastday_price` read **701.03 again** — **the same six cents off 09-17's official close of 700.97**
that the 08:16 run recorded, so the field corrected itself **neither overnight nor at the bell.**
And this time **`current_price` read 701.03 as well, with `change_today` EXACTLY 0, six minutes into
a LIVE session.** **That flat is an artifact of both fields carrying the same stale midpoint, not a
measurement that VOO is unchanged.** A run that read `change_today` as the day's move here would
have read **zero on a moving tape** — a number that looks *deliberate* rather than merely imprecise,
which is what makes it worse than the close-vs-midpoint error. **`bars --adjustment all` for a
close, a fresh `quote` for execution, never a `positions` field for either.** Cosmetic on core;
**load-bearing the moment a satellite position exists.**

**STEP 3 — CORE BOOTSTRAP SKIPPED PERMANENTLY.** `core_established: true`. The path is disabled for
the life of the account and was not evaluated further.

**STEP 4 — EXITS HAD NO SUBJECT, AND THAT IS NOT THE SAME AS BEING SKIPPED.** Zero SELL intents in
the plan and zero satellite positions in the account, so the §5.1–§5.4 ordered evaluation **never
started**: no thesis to invalidate (§5.1), no `timing_window` to expire (§5.2), no `entry_price` to
measure −7% against (§5.3), no `highest_close` to measure −10% against (§5.4). `sell_rule_status` is
**absent rather than blank.** **Still the TWENTIETH session with an empty sleeve** — the count
advances on **sessions, not runs**, and this is the **second read of 09-18**, not a twenty-first.
**All four remain untested code paths. §5.4 is NOT ARMED; it arms on the first *satellite* fill.**
**Zero Perplexity invalidation queries were issued and none was due.** **Loss streak unmoved at 0**
because nothing has ever closed in this account, so the §6 streak could not move, **no
`HALT_CLEARED_AT` comparison was required** and **no circuit-breaker alert was due.**

**STEP 5 — RE-VALIDATION HAD NO SUBJECT.** Zero BUY intents, therefore **zero `alpaca.py move` calls
and none due** — an **absent** check, not a skipped one. **Open item (7) cost nothing again, and for
precisely the reason it cost nothing yesterday: it has no subject.** That is an **absence of
exposure, not a mitigation** — the 09:35 re-validation inherits `move`'s blindness to an after-hours
event in full the moment one BUY intent exists. **No run may reinterpret the filter; that is a human
editing §4 or the script.**

**STEP 6 — NOTHING EXECUTED, AND NOTHING WAS BLOCKED.** Breaker **INACTIVE**, weekly cap **0 of 3**,
sleeve **empty**, **30.17% idle cash**, no restricting note in `control.md`. **Nothing prevented a
trade; there was simply nothing the plan authorised.** Idle cash and a permissive cap are **not an
opportunity this run may act on** — a position opened at 09:36 without a plan entry would route
around the discipline rather than satisfy it.

**STEP 7 — SLEEVES IN BAND, NO REBALANCE DUE.** `alpaca.py sleeves`: equity **$99,434.44**, cash
**$30,000.00**, core **$69,434.44 = 69.83%**, satellite **0.0% (count 0)**, cash **30.17%**,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +169.67 = 0.17% of equity` —
smaller than the 08:16 read of +173.53. §2 acts at the **band edge (65/75)**, not at the target, so
the delta is not an action at any size inside the band. **Twenty-sixth consecutive run inside a
0.39-point range (69.59–69.98).**

**ORDER STATE — NOTHING IN LIMBO.** `orders --status all` still returns **one row for the account's
entire history** (09-03 core VOO buy, filled, terminal). **No order from this run exists to resolve
because none was placed**, so `trade_log.md` was correctly left unappended. §7 forbids orders that
cannot be verified filled; there are none to verify.

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-18 (Friday) is
**2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday 2026-09-21.
**Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`, `consecutive_closed_losses: 0`.
**Sleeve drift:** core **69.83%**, inside the band. `new_positions_this_week` stays **0 of 3** and
`open_thesis_ids` stays **none**.

**CORE VOO DELIBERATELY NOT STAMPED, AND THIS RUN AGAIN DID NOT HAVE THE NUMBER.** Zero
`alpaca.py bars` calls were issued for any purpose. Writing a close here would fabricate a §5.4
trailing stop on the one position §5 exempts from all four sell rules. **Refused.**

**⚠ GNRC NOT LOOKED AT FOR THE FIFTH CONSECUTIVE RUN — AND THE PREDICTED FIFTH COSTUME ARRIVED.**
The plan warned to expect a new one; the version actually available to an execution run was *"I am
at the open with the data plane already in hand, one more symbol costs nothing"* — **the cheapest
yet, and the first that would have been FREE rather than merely justifiable.** Zero `move`, `quote`,
`bars` or `asset` calls, **five runs running.** **The excuses are getting better, not worse; that is
the finding.** GNRC is the named counterparty in the Amazon announcement — **first-order, outside §4
at any price** — and it was not in the plan, which is the only fact that has ever mattered here.

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
