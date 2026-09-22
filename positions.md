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

**Reconciliation 2026-09-22 (1-premarket-research 08:15 ET, 2-market-open-execution 09:36 ET,
3-midday-management 12:40 ET) — LEDGER AGREES WITH THE BROKER; ZERO SATELLITE POSITIONS ON BOTH SIDES;
NO ORDER PLACED AT ANY OF THE THREE RUNS; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE.**
*(**One block per date, not one per run** — the midday run **updated this block in place** rather than
adding a fourth. **Collapse, do not append — forty-second consecutive run.**)*
All three selftests passed all five checks (`trading_enabled: true`, LIVE paper account); equity read
**$100,649.73** at 08:15, **$100,742.84** at 09:35, **$100,558.61** at 12:40 pre-flight.

**`clock` READ `is_open: TRUE` AT 09:36:04 AND AGAIN AT 12:40:50**, `next_close`
**2026-09-22T16:00**, `next_open` **2026-09-23T09:30**. ⚠ **This is the INTRADAY shape — the one case of
the three where the boolean alone is sufficient.** The pre-market run read `is_open: FALSE` with
`next_open` pointing at **today**; yesterday's close run read the *same* FALSE with `next_open` pointing
at **tomorrow**; a holiday reads FALSE with `next_open` past the holiday and **no bar for today**.
**Only in the TRUE case does the boolean settle it. In the FALSE case, read the date.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree, at all three
runs.** Compare **satellite to satellite**, never raw ledger to raw broker; the core is deliberately
untracked here per §5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares,
unchanged; no order has touched it since the 09-03 fill**, twenty sessions ago, avg_entry **706.74**,
cost_basis **$69,999.99**, market_value **$70,739.87** at 09:36 and **$70,556.63** at 12:40.

**MIDDAY (routine 3) — NO SATELLITE POSITIONS, THEREFORE NOTHING TO MANAGE, AND THE RUN STOPPED THERE.**
Steps 2 through 5 each had **no operand**: no `highest_close` to test for staleness or backfill, no
`invalidation` to check against the news, no `timing_window` to expire, no `entry_price` to measure −7%
against, no high-water mark to measure −10% against, and no surviving position whose `sell_rule_status`
needed refreshing. **Zero `perplexity.py` calls were issued** — §5.1 has a subject only when an
invalidation condition exists to falsify, and **searching for news with no thesis to test it against is
not diligence, it is the run manufacturing work for itself.** The routine's own instruction — *"Do not
go looking for something to do"* — was honoured. **Zero `quote`, `bars`, `move` or `asset` calls on any
symbol.**

**⚠ THIS RUN MAY NOT OPEN A POSITION, AND 29.83% IDLE CASH IS NOT AN ARGUMENT THAT IT SHOULD.** Routine 3
is **exits only**. Every permission was open — breaker INACTIVE, weekly cap **0 of 3**, satellite sleeve
**0% deployed** — and the binding constraint was **the absence of an eligible candidate**, which this
routine is not allowed to relieve. **A midday entry would route around the pre-market research and the
09:35 execution gate, which is the whole point of that gap.** The one live research item — **General
Mills Q1 FY2027, printing tomorrow 2026-09-23** — is **tomorrow's pre-market run's**, not this one's.

**THE PLAN WAS FRESH AND IT WAS EMPTY, AND THOSE ARE TWO SEPARATE FINDINGS.** `plan_date` read
**2026-09-22** against an ET date of **2026-09-22** — **match**. The plan carried **no BUY, no SELL and
no REBALANCE intent**, so the open run submitted **zero orders**. ⚠ **A fresh empty plan and a stale plan
produce an identical zero-order run**, which is why the gate is decided on the **date** and never on the
outcome. **The §2 staleness gate has now been exercised twenty-four times and has never fired — its
alert path remains UNTESTED CODE.**

**STEP 3 BOOTSTRAP IS PERMANENTLY CLOSED.** `core_established: true` since the 09-03 fill. The
`--core` path was not invoked at any point today.

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTY-FIFTH SESSION.** **`sell_rule_status` is ABSENT
rather than blank.** **All four remain untested code paths.** **§5.4 is still NOT ARMED; it arms on the
first *satellite* fill**, and the 09-03 core fill was not it. Core VOO taken out of the working list per
§5's exemption, at the midday run as at every other.

**⚠ NO HIGH-WATER BACKFILL IS DUE, AND THE MISSING STAMP IS NOT EVIDENCE OF A FAILED CLOSE RUN.** The
marks are **ABSENT — a third state, distinct from "stale" and from "current-and-unchanged"** — and **an
absent field carries no `(as of …)` date to compare against.** That is precisely what proves no backfill
is owed. **Nothing was skipped.** ⚠ **This is routine 3's Step 2, the step written to catch a silently
disabled trailing stop; it found the disabled-looking state and correctly read it as NOT-YET-ARMED.**

**CORE VOO DELIBERATELY NOT STAMPED — FORTY-SECOND RUN.** §5 exempts core from all four sell rules. A
`highest_close` on VOO would **fabricate a §5.4 trailing stop on the one position the strategy exempts.**
Refused. **Measure the core from the 706.74 fill and from an official close, never from a `positions`
field.**

**⚠ THE BROKER'S `current_price` IS A LIVE MIDPOINT AND IS NOT A CLOSE — 714.21 at 09:36, 712.36 at
12:40.** `lastday_price` still read **712.78** at both, against yesterday's official close of **712.76**
— **two cents HIGH, the same flipped-sign instance the pre-market run logged, persisting through the
session exactly as expected**, since `lastday_price` only rebuilds at a session boundary. ⚠ **Re-reading
it at midday is NOT a second confirmation.** ⚠ **No run today took a price from a `positions` field and
none needed to:** with no order to place there was **no execution reference to pull** and **no close to
record**. Standing rule unchanged — **`bars --adjustment all` for a close, a fresh `quote` for execution,
never a `positions` field for either, and never `equity − last_equity` or `unrealized_intraday_pl` for a
day's P&L.** ⚠ **The broker's `unrealized_intraday_pl` of −$41.60 at 12:40 is exactly that forbidden
figure and was not used as the day's P&L.**

**SLEEVES IN BAND; CORE ABOVE TARGET FOR THE FIFTH RUN RUNNING; NO REBALANCE WAS DUE OR TAKEN.**
`alpaca.py sleeves` at 12:40: equity **$100,556.63**, cash **$30,000.00**, core **$70,556.63 = 70.17%**,
satellite **0.0% (count 0)**, cash **29.83%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: −166.99`. §2 rebalances at the **65/75 band edge, not to the exact 70% target**, so
**no delta inside the band is an action at any size, in either direction** — the −$166.99 is **0.17% of
equity**, against a band edge **4.83 points** away. **Thirty-third consecutive run inside a 0.63-point
range (69.59–70.22).** ⚠ **Routine 3 has no rebalance step at all — this was read for the state file,
not acted on.**

**NO TRADES, NOTHING IN LIMBO.** No order has been placed since the 09-03 core VOO buy
(`d177d8f0-cd0c-41bf-95c1-4772318265fd`, `status: filled`, terminal) — **one row for the account's
entire history.** Today placed none, so `trade_log.md` is correctly left unappended — **a run with no
fill writes no trade entry** (§7). **There is no order in a non-terminal state anywhere in this
account's history.** **Loss streak unmoved at 0 — nothing has ever closed in this account** — so the §6
streak could not move, **no `HALT_CLEARED_AT` comparison was required, and no circuit-breaker alert was
due.** Breaker **INACTIVE**, `halt_triggered_at: none`.

**HOUSEKEEPING — WEEK ROLLOVER CHECKED AT EVERY RUN, ANCHORS MATCHED, NO RESET DUE.** Today is **Tuesday
2026-09-22**; its ISO Monday is **2026-09-21**, and `week_of` already reads **2026-09-21**. **Seventh
consecutive run to find the reset already done** — `new_positions_this_week` stays **0 of 3**. Next
boundary **Monday 2026-09-28**. **That is the mechanism working as designed, not a skipped check.**

**⚠ GNRC NOT LOOKED AT FOR THE FOURTEENTH CONSECUTIVE RUN.** Like the 09:36 open run, the midday run
issued **no `move`, `quote`, `bars` or `asset` call on any symbol at all**, so **today's second refusal
is as cheap as the first and is therefore equally weak evidence** — there was no open data plane for a
costume to ride, twice over. The disqualifying facts do not move: **GNRC is the named counterparty in
the Amazon announcement, first-order and outside §4 at any price**, and open item (7) is resolved by **a
human editing §4 or `alpaca.py move`**, not by a number this seat collects. Costumes so far: diligence,
curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure,
call-already-open, screen-already-running. **Expect an eleventh on a run that has a reason to touch the
data plane — tomorrow's GIS pre-market screen is exactly such a run.**

**RESEARCH — NONE WAS DUE AT EITHER THE OPEN OR THE MIDDAY RUN, AND NONE WAS DONE.** Neither routine
generates ideas; the gap between 08:15 and 09:35 is deliberate, and routine 3 is downstream of both. The
pre-market run's five rejections (T-2026-09-22-01 through -05: Paramount/WBD, **ACN**, Nscale, **Vicor**,
GPC/ORLY/LKQ off the AutoZone print) stand as written in `research_log.md` and **no skip needed logging
against any of them** — a §4 priced-in skip is logged only against a thesis that reached a BUY intent,
and **none did.**
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
