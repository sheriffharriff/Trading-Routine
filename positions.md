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

**Reconciliation 2026-09-24 — ONE BLOCK FOR THE DATE, ALL FOUR RUNS (1-premarket 08:20, 2-market-open
09:36, 3-midday 12:40, 4-market-close 16:15), UPDATED IN PLACE AND COLLAPSED BY THE CLOSE RUN. THE
LEDGER AGREES WITH THE BROKER AT ALL FOUR; ZERO SATELLITE POSITIONS ON BOTH SIDES AT ALL FOUR; NO ORDER
PLACED AT ANY; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE AT ANY; NO §5 RULE HAD A SUBJECT.**

**— 16:15 ET, 4-market-close-journal.** Selftest passed all five checks; pre-flight equity **$99,957.40**
(broker mark), `trading_enabled: true`, LIVE paper. `clock` at **16:15:53** reads `is_open: FALSE` with
`next_open` **2026-09-25T09:30** and `next_close` **2026-09-25T16:00** — the **POST-BELL** shape.
⚠ **The stronger discriminator was run rather than inferred: a VOO daily bar for 2026-09-24 EXISTS**
(o 704.10, h 708.505, l 703.355, **c 707.28**, v 141,074, n 3,718). **A session happened; this is not a
holiday skip and the summary is owed.**

**⚠ STEP 2 — THE RUN'S INVISIBLE JOB — HAD NO SUBJECT, AND THAT IS THE CORRECT OUTCOME.** There are
**zero open satellite positions**, so there is **no `highest_close` to raise and, more importantly, no
`(as of …)` date to advance.** `highest_close` is **ABSENT — the third state, carrying no `(as of …)`
date at all** — which is precisely what distinguishes *nothing to backfill* from *a mark silently not
written.* **Zero `bars` calls were due on any satellite symbol and zero were made.** ⚠ **Tomorrow's
midday run must not read the missing stamp as a failed close run. Nothing was skipped; there was no
operand.** ⚠ **This distinction is FREE only while the sleeve is empty and becomes load-bearing the
moment a satellite fill lands. Compare the date; never infer from the field's emptiness.**

**RECONCILIATION CLEAN.** `alpaca.py positions` returns **one row, core VOO** — 99.046311231 shares
unchanged since the 09-03 fill, avg_entry 706.74, cost_basis $69,999.99, market_value $69,957.40.
**Zero satellite blocks against zero satellite Alpaca rows — they agree** (satellite-to-satellite, never
raw ledger to raw broker). **§5.1–§5.4 never started for the thirty-third consecutive session; §5.4 is
STILL NOT ARMED.** The tally of "no exits" records the **absence of a subject**, not thirty-three clean
bills of health.

**⚠⚠ THE DAY'S REAL MOVE WAS EXACTLY ZERO, AND THE BROKER REPORTED −$127.77. THE ENTIRE HEADLINE WAS
ARTIFACT — 100% OF IT.** VOO's **official** close is **707.28**, **identical to the 09-23 close of
707.28**, so the true close-to-close is **$0.00 / +0.000000%**. ⚠ **The identical close was treated as
suspect and verified before use: an independent second `bars` pull on a different window returned the
same 707.28 with DISTINCT OHLV** (09-23 o 712.13 / h 712.38 / l 706.395 / v 147,584; 09-24 o 704.10 /
h 708.505 / l 703.355 / v 141,074). **Two genuinely different sessions that happened to close to the
same cent — a coincidence, not a duplicated bar.**
**On official closes: core $70,053.48 + cash $30,000.00 = equity $100,053.48; day P&L $0.00 (0.000%);
since inception +$53.48 (+0.053475%).** The broker's competing figures — `equity − last_equity`
**−$127.77**, `unrealized_intraday_pl` **−$127.77**, `change_today` **−0.00182** — were **NOT used in
and NOT carried into any figure.** ⚠ **The carry-forward predicted in terms that this rule's value is
INVERSELY PROPORTIONAL TO THE SIZE OF THE REAL MOVE. Today the real move is exactly zero, so the ratio
of artifact to signal is unbounded. That is the prediction confirmed at its limit — and it is a
CONFIRMATION, not a save: the rule was followed because it is standing, not because anything was
spotted.**

**⚠ NEW, AND THE FIRST TIME THE TWO-PRICE DEFECT HAS REACHED A §2 QUANTITY: IT FLIPPED THE SIGN OF
`rebalance_delta`.** `alpaca.py sleeves` at 16:15 (broker marks): equity **$99,957.40**, core
**$69,957.40 = 69.99%**, satellite **0.0% (count 0)**, cash **$30,000.00 = 30.01%**, `core_in_band:
true`, `rebalance_needed: false`, `rebalance_delta` **+$12.78**. **Recomputed on the official close:**
equity **$100,053.48**, core **$70,053.48 = 70.016%**, cash **29.984%**, delta **−$16.04**.
⚠ **Same instant, same position, opposite sign — core reads BELOW target on broker marks and ABOVE
target on official ones.** **It changes nothing today**: §2 rebalances at the **65/75 band edge**, not
to the exact target, and the core sits **4.98 points** from the nearest edge, so **no delta inside the
band is an action at any size on either basis.** **NO REBALANCE IS DUE TOMORROW.** ⚠ **But it is the
same sign-error shape as 09-22, now on the §2 plane rather than the P&L plane, and it would be
load-bearing under any rule that rebalanced TO TARGET rather than AT THE EDGE.** **Forty-second
consecutive run inside the range 69.59–70.22.**

**⚠ FIFTH `lastday_price` OBSERVATION OF THE DAY: 707.60 AT 16:15, IDENTICAL TO 08:20, 09:36 AND
12:40.** The field did not move once across the pre-market, the opening bell, the midday session **or
the close**; the **32-cent error against the official 707.28 survived the entire day.**
⚠ **AND THE 09-24 PRE-MARKET'S FALSIFIABLE PREDICTION HAS GONE PARTLY DEGENERATE — SEE THE JOURNAL.**
Today's official close (707.28) **equals** the number the field was supposed to read today and did not,
so a **707.28** reading tomorrow can no longer distinguish *"correctly rebuilt to 09-24's close"* from
*"belatedly corrected to 09-23's close."* **Only the 707.60 branch stays informative.** **Do not record
a 707.28 reading as a clean rebuild.**

**⚠ `current_price` 706.31 IS 97 CENTS BELOW THE OFFICIAL 707.28 — AND IT IS NOT THE LARGEST IN THE
RECORD, THOUGH THE INHERITED SERIES SAYS IT WOULD BE.** The carry-forward's post-bell series ran
**22c LOW (09-21), 16.9c HIGH (09-22), 2c HIGH (09-23)** — three entries. ⚠ **`journal.md`'s own 09-18
close entry records `current_price` 702.98 against an official 701.85 — $1.13 HIGH, and it was called
"the widest gap yet" at the time. The inherited series had silently dropped its own largest member.**
**Corrected series, five post-bell observations: +$1.13 (09-18), −$0.22 (09-21), +$0.169 (09-22),
+$0.02 (09-23), −$0.97 (09-24).** **97c is the SECOND largest.** **Both signs, range 2c to $1.13, no
predictable sign and no correctable offset.**

**CORE VOO DELIBERATELY NOT STAMPED — FIFTY-FIRST RUN, AND THIS IS A STRONG INSTANCE.** §5 exempts core
from all four sell rules; a `highest_close` on VOO would **fabricate a §5.4 trailing stop on the one
position the strategy exempts**, a stop that could eventually sell core on a drawdown, which §7 forbids
outright. ⚠ **Graded by the standing rule: this run PULLED A FRESH OFFICIAL CLOSE (707.28), HELD IT,
and had an entirely EMPTY Step 2 to put it in — the sharpest form of the temptation, and the exact
profile the ledger flags as a strong instance.** Refused. ⚠ **"Nothing to write" is the correct output
of an empty Step 2, not an invitation to find a row to write it to.**
**GNRC NOT LOOKED AT — TWENTY-THIRD REFUSAL, AND A FREE ONE.** The only `bars` call this run was on
**VOO**, for the day's close; routine 4 has no research step and no candidate was under evaluation, so
there was nowhere to put a GNRC number. **Free is not the same as permitted, and the count accumulates
fastest on exactly the runs where it means least.**

**HOUSEKEEPING — ALL FOUR CHECKS RUN, NONE FIRED.** **Week rollover:** today is Thursday **2026-09-24**
(confirmed via `TZ=America/New_York`, not assumed); its ISO Monday is **2026-09-21** and `week_of`
already reads 2026-09-21 — **sixteenth consecutive run to find the reset already done**,
`new_positions_this_week` stays **0 of 3**, next boundary **Monday 2026-09-28**. **Loss streak:**
**nothing closed today and nothing has ever closed**, so `consecutive_closed_losses` stays **0 — it has
never had an input**; breaker **INACTIVE**, `halt_triggered_at: none`, so **no `HALT_CLEARED_AT`
comparison was required and NO `circuit-breaker` alert was due.** **Unresolved orders:** `orders
--status all` returns **one row for the account's entire history** — the 09-03 core VOO buy,
`status: filled`, terminal. **Nothing is in limbo overnight; no order has EVER reached a non-terminal
state in this account.** `trade_log.md` correctly left unappended — **a day with no fill writes no trade
entry.** `alerts.md` **empty — zero open incidents, zero SYSTEMIC.**

**— EARLIER TODAY, COLLAPSED (08:20 pre-market, 09:36 open, 12:40 midday).** All three recorded the same
null and are compressed here rather than restated; the narrative lives in `journal.md`.
**08:20 pre-market** — `is_open: FALSE` with `next_open` pointing at **TODAY**, the pre-market shape;
equity $99,776.15; core 69.93%, delta **+$67.16**; **research ran in FULL and produced NO TRADE** —
five Perplexity scans (one after an **HTTP 500** that recovered on a reworded retry), **seven candidates
reached a `research_log.md` entry and all seven were rejected** (T-2026-09-24-01 ILMN, -02 GRAL, -03
BBY, -04 PYPL, -05 SHOP, -06 SoftBank/OpenAI, -07 ELMT); **five `alpaca.py move` calls** as §4 hard
filters (PYPL, BBY, SHOP, ILMN, GRAL). ⚠ **The §4 priced-in filter fired on THREE GENUINE RISES — SHOP
+9.61%, ILMN +11.54%, GRAL +44.67% — the first time in volume the record shows it doing its designed
job. It is not broken; it is SIGN-BLIND.** ⚠ **The 09-23 prediction about `lastday_price` was falsified
here: it read 707.60, not 712.78 — the field DID rebuild, and to a number 32c wrong.**
**09:36 open** — `is_open: TRUE`, the **in-session** shape, the one reading where the boolean alone
settles it. **Staleness gate: `plan_date` 2026-09-24 against ET date 2026-09-24 — FRESH, gate did not
fire, twenty-seventh exercise and still never fired; its alert path remains UNTESTED CODE.** ⚠ **The
plan was FRESH *and* EMPTY, and the zero-order run it produced is byte-for-byte what a STALE plan would
have produced. Only `plan_date` distinguished them.** Bootstrap permanently closed (`core_established:
true`); zero BUY intents so **zero `move` re-validation calls were due — an ABSENT check, not a skipped
one**; equity $99,808.83, core 69.94%, delta **+$57.35**.
**12:40 midday** — `is_open: TRUE`; equity $100,113.47, core 70.03%, delta **−$34.04**; **§5 had no
operand**; ⚠ **`TRADING_ENABLED` was TRUE, so a triggered stop WOULD have been submitted — the null is
an EMPTY SLEEVE, not a disabled stop, and those two produce the identical zero-exit line.**
⚠ **ACROSS ALL FOUR RUNS, EVERY GATE THAT COULD HAVE STOPPED A BUY WAS OPEN — breaker INACTIVE, weekly
cap 0 of 3, sleeve empty, ~30% idle cash, no restricting note in `control.md`. NOTHING WAS BLOCKED. The
research simply produced no eligible candidate, and the seven rejections were NOT rehabilitated at any
later run — no `move`, `quote`, `bars` or `asset` call was made on any of them after the pre-market.
A rejection is not a queue.**
*(**One block per date, not one per run.** **Collapse, do not append — forty-ninth consecutive run.**
The close run merged this date's four per-run blocks into the single block above. **Nothing live was
discarded**; the load-bearing facts are carried here and in `state.md`.)*

---

**⚠ THE 2026-09-22 AND 2026-09-23 PER-RUN BLOCKS (EIGHT RUNS, ~350 LINES) HAVE BEEN COLLAPSED BY THIS
RUN, DELIBERATELY AND UNDER THE FILE'S OWN STANDING INSTRUCTION.** Every one of the eight recorded the
same null result — zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no
§5 rule evaluated; no high-water mark to stamp; no backfill due; no order placed. `state.md` flags this
accumulation as **actively harmful rather than untidy**, because this repo's only continuity mechanism
is the next run *reading* these files in full. **Nothing live was discarded.** The load-bearing facts
those blocks carried:

- **09-22 close was the SIGN-ERROR instance** — `lastday_price` **712.78** (2c high) and
  `current_price` **712.859** (16.9c high) **at once, in opposite directions**, so the broker computed
  `equity − last_equity` = **+$7.82 UP** on a day whose true close-to-close was **−$6.93 DOWN**.
  ⚠ **On a flat day the standing rule is a DIRECTION rule, not a precision rule.** And had a satellite
  position existed, stamping `current_price` as `highest_close` would have written 712.859 instead of
  712.69, **silently moving a §5.4 stop 17 cents** — the ledger header's warning, with real numbers.
- **09-23 close: the largest single-day decline since the core was established** — VOO 712.69 → 707.28,
  **−0.759%**, **−$535.84** on the core, **−0.533%** on equity, leaving the account **+0.053% since
  inception**. Grounded from a pulled 25-session series, not asserted.
- **Post-bell `current_price` error runs 22c LOW (09-21), 16.9c HIGH (09-22), 2c HIGH (09-23)** — same
  routine, same minute, **no predictable sign and no correctable offset.**
- **Both halves of the `lastday_price` mechanism were falsified in turn** (09-22: rebuilds; 09-23: does
  not; **09-24: does, and to a 32c-wrong value**). See this run's block above — **the field has no
  reliable structure at all.**
- **Nine theses were written across those two days and all nine were rejected**; none was rehabilitated
  at a later run. **A rejection is not a queue.**
- **The §2 staleness gate was exercised at every open and has never fired; its alert path is untested
  code.** A fresh empty plan and a stale plan produce an identical zero-order run — **read `plan_date`,
  never the outcome.**

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
