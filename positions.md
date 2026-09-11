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

**Reconciliation 2026-09-11 16:16 ET (4-market-close-journal) — NO MARKS WRITTEN, NO SUBJECT TO
WRITE THEM FOR, AND THE ALPACA OUTAGE IS OVER.**
*(This block replaces the 12:34 midday reconciliation, read in full by this run and carrying nothing
this one does not. Collapse, do not append — fifteenth consecutive run.)* Selftest passed all five
checks at **16:16 ET** (`trading_enabled: true`, LIVE paper account, equity $99,591.92).

**✅ THE DATA-PLANE OUTAGE IS RESOLVED. PROBED BY HAND, NOT INFERRED FROM THE SELFTEST.**

| Endpoint | Midday 12:34–12:36 ET | **This run, 16:16 ET** |
|---|---|---|
| `clock` | **500 × 4 attempts** | **200** — `is_open: false`, `next_open` Mon 09-14 09:30 ET |
| `quote --symbols VOO` | **504 × 2** | **200** — live NBBO 702.59 / 702.65 |
| `bars --days 3 --adjustment all` | **504** | **200** — 09-11 close **702.52** |
| `account` / `positions` / `sleeves` | 200 | 200 |

**The market was read from `clock`, not inferred.** `is_open: false` at 16:16 with `next_open`
**Monday 2026-09-14 09:30 ET** — a normal Friday close, **not a holiday**: the session happened
(`change_today` +0.857%, equity moved $591.31 off `last_equity`). Yesterday's inference concession
is **closed and did not become a precedent.**

**⚠ OPEN ITEM (6) SURVIVES THE OUTAGE IT WAS FOUND IN.** The selftest still probes only env /
account / Perplexity / ClickUp / `control.md` — **it does not probe `clock` and it does not probe
market data.** The endpoints recovered on their own; **the blind spot did not.** A green pre-flight
still certifies nothing about the data plane. **Probe by hand. Whether `selftest.py` should change
is a human's call, not a run's.**

**⚠ STEP 2 — THE HIGH-WATER UPDATE — HAD NO SUBJECT. ZERO MARKS WERE WRITTEN, AND THAT IS THE
CORRECT OUTCOME RATHER THAN A SKIPPED STEP.** There is **no satellite block in this file**, so there
is **no `highest_close` and no `(as of ...)` date** to advance. The marks are **ABSENT: a third
state, distinct from both "current and unchanged" and "stale."** **Core VOO was deliberately NOT
stamped** — stamping it would fabricate a §5.4 trailing stop on the one position §5 exempts from
every sell rule, and the pressure to do it precisely *because* this routine's prompt calls Step 2
its load-bearing job is recorded in today's journal. **§5.4 remains NOT ARMED**; it arms on the
first *satellite* fill. **Unlike at midday, the stamp WOULD have been possible today** — `bars`
answered. The data path was tested; the rule was not.

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.**
Compare **satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns
**one row, VOO core** (99.046311231 shares, avg_entry 706.74, market_value $69,591.92, broker
`current_price` **702.62**, `lastday_price` 696.65, unrealized_pl **−$408.07, −0.583%**,
unrealized_intraday_pl **+$591.31, +0.857%**). `alpaca.py sleeves`: equity **$99,591.92**, cash
$30,000.00, core **69.88%**, satellite **0.0% (count 0)**, cash 30.12%, `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: +122.42` — **0.12% of equity. NO REBALANCE IS DUE
TOMORROW**, and §2 rebalances at the **band edge (65/75)**, not to the exact target.

**§5.1–§5.4 HAD NO SUBJECT — twelfth consecutive day, and it is not a clean bill of health.**
No thesis to test for invalidation (§5.1); no `timing_window` to expire (§5.2); no `entry_price` to
measure −7% against (§5.3); no high-water mark to measure −10% against (§5.4). **Nothing was near
triggering because nothing exists to trigger.** `sell_rule_status` is **absent rather than blank**.
**All four remain untested code paths; nothing has ever closed in this account**, which is why
`consecutive_closed_losses` cannot have moved and **no circuit-breaker alert was due.**

**NO ORDER WAS PLACED AND NONE COULD BE — this routine does not trade.** `orders --status all`
returns **one row**, the 09-03 core fill, `status: filled`, terminal. **Nothing was left in limbo
overnight**, so §7's warning had no occasion to fire and `trade_log.md` was correctly left
unappended.

**⚠ THE TWO-PRICE TRAP IS SOLVED, AND IT IS NOT AN OFFSET — IT IS A QUOTE MIDPOINT.** Six days of
notes called the broker/official gap an *unstable offset* (6.5c on 09-09, **59.85c** on 09-10, 4c on
09-11 morning) without explaining it. **Today it resolves exactly: broker `current_price` = 702.62,
latest quote = 702.59 / 702.65, midpoint = 702.62 TO THE CENT.** The official close is **702.52**
(last trade 15:59:57 ET; `bars` close agrees). **The broker mark is not a stale close — it is not a
close at all.** It is a live bid/ask midpoint that keeps moving after the bell, which is why the gap
never had a stable size and never will. **Consequence, unchanged but now sharp-edged: the moment a
satellite position exists, a `highest_close` taken from a `positions` field records an after-hours
quote midpoint and silently moves the §5.4 stop.** Always `bars --adjustment all` for a close, a
fresh `quote` for execution, **never a `positions` field for either.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-11 09:36) HAVE BEEN COLLAPSED,
DELIBERATELY.** Twenty-five blocks spanning 09-01 to this morning's open run each recorded the same
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
