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

**Reconciliation 2026-09-22 08:15 ET (1-premarket-research) — LEDGER AGREES WITH THE BROKER; ZERO
SATELLITE POSITIONS ON BOTH SIDES; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE.**
*(This block **replaces** the 09-21 16:16 close reconciliation, read in full by this run — **one block
per date, not one per run.** **Collapse, do not append — fortieth consecutive run.**)*
Selftest passed all five checks at **08:15 ET** (`trading_enabled: true`, LIVE paper account, equity
**$100,649.73** at pre-flight).

**`clock` READ `is_open: FALSE` AT 08:15:26**, `next_open` **2026-09-22T09:30**, `next_close`
**2026-09-22T16:00**. ⚠ **This is the PRE-MARKET shape, NOT a holiday, and the boolean cannot tell you
which** — `next_open` points at **today**. Yesterday's close run read the *identical* boolean with
`next_open` pointing at **tomorrow**. **Read the date, not the boolean.** Today is a normal trading
session; the market opens in seventy-five minutes.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker; the core is deliberately untracked here per
§5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares, unchanged; no order
has touched it since the 09-03 fill**, nineteen sessions ago, avg_entry **706.74**, cost_basis
**$69,999.99**, market_value **$70,649.73**.

**§5.1–§5.4 NEVER STARTED — NO SUBJECT, FOR THE TWENTY-FOURTH SESSION.** No thesis to invalidate
(§5.1), no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no
`highest_close` to measure −10% against (§5.4). **`sell_rule_status` is ABSENT rather than blank.**
**All four remain untested code paths.** Core VOO taken out of the working list per §5's exemption.
**Zero Perplexity invalidation queries were issued and none was due** — §5.1 reads an `invalidation`
line that does not exist. **§5.4 is still NOT ARMED; it arms on the first *satellite* fill.**

**⚠ NO HIGH-WATER BACKFILL IS DUE, AND THE MISSING STAMP IS NOT EVIDENCE OF A FAILED CLOSE RUN.** The
09-21 close run **executed its Step 2 and Step 2 had no operand**, exactly as it recorded. The marks
are **ABSENT — a third state, distinct from "stale" and from "current-and-unchanged"** — and **an
absent field carries no `(as of …)` date to compare against.** That is precisely what proves no
backfill is owed. **Nothing was skipped.**

**CORE VOO DELIBERATELY NOT STAMPED — FORTIETH RUN.** §5 exempts core from all four sell rules. This
run pulled `bars --symbol VOO --days 5 --adjustment all` for the official-close arithmetic, so it held
a clean close (**712.76**) in hand and writing it into a `highest_close` would have cost one line and
looked like tidiness. **Refused.** A `highest_close` on VOO would **fabricate a §5.4 trailing stop on
the one position the strategy exempts**, seeded at the highest mark the account has ever recorded.

**⚠ THE TWO-PRICE DEFECT HAS A NEW INSTANCE AND THE SIGN HAS FLIPPED — SECOND CONSECUTIVE DAY, OPPOSITE
DIRECTION.** `lastday_price` reads **712.78** against yesterday's official close of **712.76** — **two
cents HIGH**. The previous instance ran **seven cents LOW** (701.78 vs 701.85) and was read **four
times** across 09-21 (08:20, 09:36, 12:35, 16:16). ⚠ **That instance DID clear at the session
boundary** — this is a fresh one built on the new day's close, not the old one persisting — ⚠ **but it
did not clear into correctness.** Combined with the 09-21 post-bell finding that `current_price` read
**712.54** against an official **712.76** *sixteen minutes after the close*, the record now shows the
broker's error running **low four times, then high**, on consecutive days. **The direction of the
broker's error is not predictable and must never be assumed.** Only an external close settles it.
**`bars --adjustment all` for a close, a fresh `quote` for execution, never a `positions` field for
either, and never `equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

**SLEEVES IN BAND ON BOTH BASES; CORE IS ABOVE TARGET FOR THE THIRD RUN RUNNING; NO REBALANCE IS DUE.**
Broker-mark basis at 08:15: equity **$100,649.73**, cash **$30,000.00**, core **$70,649.73 = 70.19%**,
satellite **0.0% (count 0)**, cash **29.81%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: −194.92`. Official-close basis (712.76 × 99.046311231): core **$70,596.25**, equity
**$100,596.25**, core **70.178%**, cash **29.822%**. **Both bases agree and both put core on the same
side of target.** §2 rebalances at the **65/75 band edge, not to the exact 70% target**, so **no delta
inside the band is an action at any size**, in either direction. Rebalance is a market-open step in any
case and not this run's to take.

**NO TRADES, NOTHING IN LIMBO.** No order has been placed since the 09-03 core VOO buy
(`d177d8f0-cd0c-41bf-95c1-4772318265fd`, `status: filled`, terminal) — **one row for the account's
entire history.** This run placed none, so `trade_log.md` is correctly left unappended — **a run with
no fill writes no trade entry** (§7). **There is no order in a non-terminal state anywhere in this
account's history.** **Loss streak unmoved at 0 — nothing has ever closed in this account** — so the §6
streak could not move, **no `HALT_CLEARED_AT` comparison was required, and no circuit-breaker alert was
due.** Breaker **INACTIVE**, `halt_triggered_at: none`.

**HOUSEKEEPING — WEEK ROLLOVER CHECKED, ANCHORS MATCHED, NO RESET DUE.** Today is **Tuesday
2026-09-22**; its ISO Monday is **2026-09-21**, and `week_of` already reads **2026-09-21**. **Fifth
consecutive run to find the reset already done** — `new_positions_this_week` stays **0 of 3**. Next
boundary **Monday 2026-09-28**. **That is the mechanism working as designed, not a skipped check.**

**⚠ GNRC NOT LOOKED AT FOR THE TWELFTH CONSECUTIVE RUN — AND TODAY WAS A STRONG TEST.** This run issued
**`move --symbol ACN`** and **`bars --symbol VOO`**: the data plane was open and a `--symbol GNRC` was
one flag on a command already being typed. **The tenth costume arrived as *"you are already screening a
candidate's five-session move, so screening one more costs nothing"* — the zero-marginal-cost costume
wearing a LIVE FUNNEL as its cover, which is the most plausible version yet. Refused.** The
disqualifying facts do not move: **GNRC is the named counterparty in the Amazon announcement,
first-order and outside §4 at any price**, and open item (7) is resolved by **a human editing §4 or
`alpaca.py move`**, not by a number this seat collects. **Zero `move`/`quote`/`bars`/`asset` calls on
GNRC, twelve runs running.** Costumes so far: diligence, curiosity, tidiness, completeness,
zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
screen-already-running.

**RESEARCH — 5 THESES, 0 ACCEPTED, 5 REJECTED.** T-2026-09-22-01 (Paramount/WBD settlement) died at
**part 2** — the mandated ~$300M/yr of production spend has a payer and **no named payee**, rule (v).
T-2026-09-22-02 (**ACN**) died at the **premise** (signatory, first-order), again at **part 2** (<1% of
revenue on the most generous reading) and again at **part 3** (five years). T-2026-09-22-03 (Nscale's
$103B book) died at **part 3** in one step (2GW by 2028, 8GW by 2031) and at the premise, and is a
**rule (iii) re-report** besides. T-2026-09-22-04 (**Vicor's** licensees) died at **part 1** — *"four
leading OEMs and hyperscalers"*, **not one named**. T-2026-09-22-05 (GPC/ORLY/LKQ off the **AutoZone**
print) died at **part 1** — a competitor's print is a shared cause, the sentence needs an *"and also"*.
⚠ **Eighth instance of open item (1): `move --symbol ACN` returned `priced_in: true` on a −4.58%
FALL.** That is **not** why ACN was rejected, and is recorded that way deliberately.
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
