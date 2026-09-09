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

**Reconciliation 2026-09-09 16:16 ET (4-market-close-journal) — RECONCILED AT THE CLOSE. NO
SATELLITE POSITION EXISTS, SO NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS OWED.** *(This block
replaces the 09-09 12:35 midday reconciliation, which was read and acted on by this run and carries
nothing this one does not. Collapse, do not append.)* Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity $99,433.45). **`clock` at 16:16:14 ET returns
`is_open: false`, `next_open: 2026-09-10T09:30 ET` — a normal session that has ended, not a
holiday.**

`alpaca.py positions` returns **one row, VOO core** (99.046311231 shares, avg_entry 706.74,
market_value $69,433.45, broker `current_price` **701.02**, `lastday_price` 704.07, `change_today`
**−0.433%**, unrealized_pl **−$566.54, −0.809%**). `alpaca.py sleeves`: equity **$99,433.45**,
cash $30,000.00, core **69.83%**, satellite **0.0% (count 0)**, cash 30.17%,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +169.97`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.**
Compare **satellite to satellite**, never raw ledger to raw broker.

**⚠ STEP 2 — THE HIGH-WATER UPDATE — HAD NO SUBJECT. THIS IS NOT A SKIPPED MAINTENANCE STEP AND NO
BACKFILL IS OWED.** There is no `highest_close` and no `(as of ...)` date anywhere in this file,
because there is no satellite position block to carry one. The marks are **ABSENT — a third state,
distinct from both "current and unchanged" and "stale."** The midday backfill trigger keys on a
**stale date**, and an absent field cannot be stale: **no `bars` call was due for a high-water
purpose and none was made for one.** Core VOO was again deliberately not given a mark — stamping
one would fabricate a §5.4 trailing stop on the one position §5 exempts from all four rules.
**§5.4 remains NOT ARMED, not disabled, not skipped.** A future run must not read "no mark was
updated today" as evidence that this run failed its headline job.

**Step 3 (§5.1–§5.4) had no subject either.** No thesis to test for invalidation (§5.1); no timing
window to expire (§5.2); no entry price to measure −7% against (§5.3); no high-water mark to
measure −10% against (§5.4). `sell_rule_status` is absent rather than blank.

**Today's official close, recorded for the record and NOT as a high-water mark:** VOO
**700.805** (`bars --adjustment all`, 2026-09-09), against **704.16** on 09-08 — **−0.48% on the
session.**

**⚠ The two-price trap, live again and in its plainest form yet: three numbers for one day.**
Official close **700.805**, broker `current_price` **701.02**, `lastday_price` **704.07** (against
yesterday's official **704.16**). Always pull `bars --adjustment all` for a close and a fresh
`quote` for execution — **never a `positions` field for either.** The day a satellite position
exists, that shortcut writes a wrong high-water mark that does not error, does not look stale, and
silently moves the §5.4 stop to a level nobody chose.

**§2 rebalance:** **not due tomorrow.** 69.83% sits well inside the 65–75% band and the +$169.97
delta is **0.17% of equity** — VOO's mark moving, not drift. §2 rebalances at the **band edge**, not
to the exact target.

**⚠ The core's mark closed negative again and it still means nothing procedurally — and the close
run is where that pull is strongest.** −$566.54 (−0.809%) against the 706.74 fill. **§5 exempts core
from all four sell rules.** A day with no satellite position and a visibly red core is exactly the
setup in which core gets sold "as a stop," or in which the §4 bar gets lowered tomorrow to put
*something* on. **It is not a stop, and a quiet day is not a reason to lower the bar. There is no
action.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-09 12:35) HAVE BEEN COLLAPSED,
DELIBERATELY.** Twenty blocks spanning 09-01 to the 09-09 midday run each recorded the same
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
