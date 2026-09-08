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

**Reconciliation 2026-09-08 08:24 ET (1-premarket-research) — RECONCILED, NO §5 EVALUATION
DUE, NOTHING TO BACKFILL:** selftest passed all five checks (`trading_enabled: true`, LIVE paper
account). Market **opens today** — `clock` at 08:24:02 ET returns `is_open: false` with
`next_open: 2026-09-08 09:30 ET` and `next_close: 2026-09-08 16:00 ET`, i.e. **pre-market on a
normal session day, not a holiday**; Monday 09-07 was Labor Day and this is the week's first
live session. `alpaca.py positions` returns **one row, VOO core** (99.046311231 shares,
avg_entry 706.74, broker mark **706.04**, `lastday_price` 708.01, `change_today` **−0.278%**,
unrealized_pl **−$69.33, −0.099%**). `alpaca.py sleeves`: equity **$99,930.66**, cash
$30,000.00, core **69.98%**, satellite **0.0% (count 0)**, cash 30.02%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: +20.80`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** No
discrepancy, and no research was done on top of a doubtful ledger.

**Two things changed from the holiday reads and both are ordinary price movement, not faults.**
(1) The core's mark is **below** the 706.74 fill for the first time — `unrealized_pl` is
**−$69.33** where every prior run recorded a gain. That is a −0.099% move on a position §5
exempts from all four sell rules; **it is not a stop of any kind and there is no action.**
(2) `rebalance_delta` is **+$20.80**, sign-flipped from the −$37.73 carried out of Monday, and
at 0.02% of equity it is the closest to the 70% target the core has ever sat. §2 rebalances at
the **band edge**, not to the exact target — **no REBALANCE intent was queued.**

**No §5 rule was evaluated and none was due.** Zero satellite blocks means §5.1 has no
invalidation condition to test (**no Perplexity news query was issued against a holding, because
there is no holding**), §5.2 no deadline, and §5.3/§5.4 no entry price or high-water mark to
measure against. **No `sell_rule_status` field was updated because none exists.**

**No high-water backfill was run and none was due.** There is still **no `highest_close` field
and no `(as of ...)` date anywhere** in this section, so the staleness trigger has nothing to key
on. **Absent is not stale — do not backfill from `bars`.** Core VOO was again deliberately not
given a mark: stamping one would fabricate a §5.4 trailing stop on a position §5 exempts.
**§5.4 remains NOT ARMED, not disabled.**

---

**Reconciliation 2026-09-04 16:16 ET (4-market-close-journal) — HIGH-WATER PASS, NOTHING TO
RECORD:** selftest passed all five checks (`trading_enabled: true`, LIVE paper account).
`clock` at 16:16:10 ET returns `is_open: false` **because the bell has rung, not because the
day was a holiday** — the session ran 09:30–16:00 today and `next_open` is
**2026-09-08 09:30 ET**, i.e. Tuesday, because **Monday 2026-09-07 is Labor Day.**
`alpaca.py positions` returns **one row, VOO** (99.046311231 shares, avg_entry 706.74, broker
mark 707.59, market_value $70,084.18, unrealized_pl **+$84.19, +0.12%**, `lastday_price`
710.72, `change_today` **−0.44%**); `alpaca.py sleeves` reports equity **$100,084.18**, cash
$30,000.00, core **70.03%**, satellite **0.0% (count 0)**, cash 29.97%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: −25.25`.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree. No
discrepancy.** Compare **satellite to satellite**, never raw ledger to raw broker.

**Step 2 — record the closes: executed in full, and its working list was empty.** This is the
run whose whole job is to stamp today's official close into every open satellite position's
`highest_close` and to refresh the `(as of ...)` date **whether or not the value moved**. It
had **no position to stamp**: there is no `highest_close` field anywhere in this file's
`## Open positions` section and no `(as of ...)` date to advance. So the field the §5.4
trailing stop depends on was **not left stale — it does not exist yet.**

**⚠ Read this distinction precisely, because the whole design of Step 2 rests on it.** The
routine stamps the date every day so that a *current, unchanged* mark cannot be confused with
a *skipped* one. That machinery presupposes a mark. Today there is none, which is a **third**
state: not current, not stale, **absent**. The midday backfill trigger keys on a stale date,
and an absent field cannot be stale — so **the next run must not backfill from `bars`. There
is nothing to backfill.** This is the eighteenth consecutive run recording it.

**§5.4 is NOT ARMED, and is not silently disabled.** It arms the day the first *satellite*
position opens. §5 exempts core from all four sell rules, so VOO is deliberately absent from
this ledger — no thesis, no timing window, no `highest_close`. VOO's official close today was
**707.86** (`bars --adjustment all`, 09-04) against **710.70** on 09-03, **−0.40%**, and that
number was **deliberately not written anywhere as a high-water mark** — recording a core close
into this file would fabricate a trailing stop on a position §5 exempts.

**⚠ The two-price rule bit again today, in the direction worth noting.** The broker mark
(**707.59**) drives `equity` and the +$84.19 unrealized P&L above; the official close
(**707.86**) is what would feed `highest_close`. On 99.046311231 shares the gap is **$26.75**
of unrealized P&L — small, but it is the *first* time the two have been compared at the close
rather than intraday, and the ordering (official close **above** the broker mark) is the
reverse of what an intraday fade would suggest. **Never mix them inside one §5.4 comparison.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-04 12:35) HAVE BEEN COLLAPSED,
DELIBERATELY.** Fourteen blocks spanning 09-01 to 09-04 each recorded the same null result —
zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no §5 rule
evaluated; no high-water mark to stamp; no backfill due. `state.md` flags this accumulation as
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
