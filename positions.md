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

**Reconciliation 2026-09-11 08:20 ET (1-premarket-research) — PRE-MARKET RECONCILIATION ON A REGULAR
TRADING DAY. NO SATELLITE POSITION EXISTS. NO HIGH-WATER MARK WAS DUE OR WRITTEN.** *(This block
replaces the 09-10 16:15 close reconciliation, which was read in full by this run and carries
nothing this one does not. Collapse, do not append — twelfth consecutive run.)* Selftest passed all
five checks (`trading_enabled: true`, LIVE paper account, equity $99,456.23). **`clock` at 08:19:54
ET returns `is_open: false` with `next_open: 2026-09-11T09:30 ET` — the market is closed because it
is PRE-MARKET, NOT because today is a holiday. `next_open` is *today*, which is how the two are
told apart.**

`alpaca.py positions` returns **one row, VOO core** (99.046311231 shares, avg_entry 706.74,
market_value $69,456.23, broker `current_price` **701.25**, `lastday_price` 696.65, `change_today`
**+0.66%**, unrealized_pl **−$543.76, −0.777%**). `alpaca.py sleeves`: equity **$99,456.23**, cash
$30,000.00, core **69.84%**, satellite **0.0% (count 0)**, cash 30.16%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: +163.14`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.**
Compare **satellite to satellite**, never raw ledger to raw broker.

**⚠ THE HIGH-WATER FIELD IS ABSENT, NOT STALE — checked against the actual trigger, not assumed.**
The backfill rule at the top of this file fires when a `highest_close` is **behind the last trading
day**. There is **no satellite position block in this file**, so there is **no `highest_close` and
no `(as of ...)` date** to be behind anything. The marks are **ABSENT: a third state, distinct from
both "current and unchanged" and "stale."** An absent field carries no date, so the backfill trigger
cannot fire. **No `bars` call was due for a high-water purpose and none was made for one.** (A
`bars --adjustment all` call *was* made this run — for **AVAV**, to check whether a +1.20% five-
session reading was describing a quiet tape or a round-tripped +12.9% intraday spike. It was the
latter. That is research, not high-water maintenance.) **Core VOO was again deliberately not given a
mark**, because stamping one would fabricate a §5.4 trailing stop on the one position §5 exempts
from all four rules. **§5.4 remains NOT ARMED, not disabled, not skipped.** It arms on the first
*satellite* fill.

**§5.1–§5.4 have no subject this morning.** No thesis to test for invalidation (§5.1); no timing
window to expire (§5.2); no entry price to measure −7% against (§5.3); no high-water mark to measure
−10% against (§5.4). `sell_rule_status` is **absent rather than blank** — there is no position block
to carry the field. **No §5.1 Perplexity invalidation query was issued and none was due.** **All
four remain untested code paths; nothing has ever closed in this account.**

**⚠ THE TWO-PRICE GAP COLLAPSED THIS MORNING, AND THAT IS THE POINT.** Yesterday's official close
was **696.69** (`bars --adjustment all`); this morning's `lastday_price` is **696.65** — a **4-cent**
gap, against the **59.85-cent** gap between the official close and the broker mark at last night's
16:15 run. **The gap is not a stable offset that could be corrected for; it was ~6.5 cents on 09-09,
~60 cents at the 09-10 close, and ~4 cents now.** On core this is cosmetic. **On a satellite position
the same shortcut writes a `highest_close` wrong by an amount that changes day to day, which does not
error, does not read as stale, and silently moves the §5.4 stop to a level nobody chose.** Always
`bars --adjustment all` for a close and a fresh `quote` for execution — **never a `positions` field
for either.**

**§2 rebalance: NOT DUE TODAY.** 69.84% sits well inside the 65–75% band; `core_in_band: true`,
`rebalance_needed: false`, and the +$163.14 delta is **0.16% of equity** — VOO's mark moving, not
drift. §2 rebalances at the **band edge** (65/75), not to the exact target.

**⚠ The core's mark is still negative but is up $455.61 on this morning's indication, after nine
consecutive negative closes. It means nothing procedurally in either direction.** −$543.76 (−0.777%)
against the 706.74 fill. **§5 exempts core from all four sell rules.** A round number is not a
threshold, there is no §5.3 or §5.4 on this position to cross, and **a green mark is not a result any
more than the nine red ones were.** **A book whose only holding is core, sitting on 30% cash with a
clear breaker and an empty weekly cap, is precisely the setup in which the §4 bar gets quietly
lowered to put *something* on.** It was not lowered. **Five theses were written today and all five
were rejected on their own filters — including the largest second-order surface this log has ever
screened, Oracle's $664B RPO print, which produced no Company B at all.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-10 09:36) HAVE BEEN COLLAPSED,
DELIBERATELY.** Twenty-three blocks spanning 09-01 to the 09-10 open run each recorded the same
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
