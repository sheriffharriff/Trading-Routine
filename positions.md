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

**Reconciliation 2026-09-17 16:16 ET (4-market-close-journal) — LEDGER AGREES WITH THE BROKER;
NO HIGH-WATER MARK RECORDED BECAUSE THERE IS NO POSITION TO RECORD ONE FOR.**
*(This block **replaces** the 09-17 12:35 midday reconciliation, read in full by this run —
**one block per date, not one per run.** **Collapse, do not append — thirty-first consecutive
run**, and this is the strongest test the rule has faced: **FOUR runs, ONE date.**)*
Selftest passed all five checks at **16:16 ET** (`trading_enabled: true`, LIVE paper account, equity
$99,404.72 at pre-flight).

**⚠ STEP 2 IS THE REASON THIS ROUTINE EXISTS, AND TODAY IT HAD NO SUBJECT — WHICH IS NOT THE SAME AS
BEING SKIPPED.** The step says to write every open **satellite** position's official close into
`highest_close`, raising the value if higher and **re-stamping the date either way**. There are
**zero satellite positions**, so there is **no `highest_close` field in this file at all.** **ABSENT
is a third state, distinct from "current and unchanged" and from "stale," and it is the only one
carrying no date** — and that missing date is exactly what tells tomorrow's midday run no backfill is
due. **§5.4 remains NOT ARMED; it arms on the first *satellite* fill.**

**CORE VOO WAS DELIBERATELY NOT STAMPED, AND THE ACCOMPLICE THE 09-16 CLOSE RUN PREDICTED SHOWED UP
AGAIN.** This run pulled `bars --symbol VOO --days 3 --adjustment all` **to price the book**, so
today's official close **700.97 was sitting in the terminal output with nothing to do.** Writing it
here would fabricate a §5.4 trailing stop on the one position §5 exempts from all four sell rules.
**Refused. It does not feel like a violation; it feels like tidiness** — and the prediction landing
verbatim one day later means this is a standing feature of the routine, not a mood.

**`clock` READ `is_open: false` AT 16:16:29** with `next_open` **2026-09-18T09:30 — TOMORROW**, and
`next_close` 2026-09-18T16:00. **Post-bell, CONFIRMED not predicted. Today was a trading day, NOT a
holiday.** A close run and a pre-market run both read `is_open: false`; only the `next_open` **DATE**
discriminates. **Read the date, not the boolean.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker. `alpaca.py positions` returns **one row,
VOO core** (99.046311231 shares — **unchanged, no order has touched it since 09-03**, avg_entry
706.74, cost_basis $69,999.99, broker `current_price` **700.58**, `lastday_price` **693.24**,
market_value $69,389.86, unrealized_pl **−$610.13 / −0.872%**, `change_today` **+1.059%**).
**`current_price` 700.58 is an AFTER-HOURS QUOTE MIDPOINT, not a close** — the official close is
**700.97**, 39 cents away, and the two must never be mixed. **On official closes: core
$69,428.49, unrealized −$571.50 / −0.816%, which is EXACTLY VOO 706.74 → 700.97 over the same
window. Tracking error 0.0000%, fourth check.**

**SLEEVES — IN BAND, NO REBALANCE DUE AT TOMORROW'S OPEN.** `alpaca.py sleeves` (broker marks):
equity **$99,389.86**, cash **$30,000.00**, core **$69,389.86 = 69.82%**, satellite **0.0% (count
0)**, cash **30.18%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +183.04`.
**On official closes: equity $99,428.49, core $69,428.49 = 69.83%, cash 30.17%, delta +$171.45 =
0.17% of equity — the smallest recorded in this range.** §2 acts at the **band edge (65/75)**, not at
the target. **Twenty-fourth consecutive run inside a 0.39-point range (69.59–69.98).**

**§5.1–§5.4 HAD NO SUBJECT AND THE ORDERED EVALUATION NEVER STARTED.** No thesis to invalidate
(§5.1), no `timing_window` to expire (§5.2), no `entry_price` to measure −7% against (§5.3), no
`highest_close` to measure −10% against (§5.4). **Nothing is near triggering because nothing exists
to trigger.** `sell_rule_status` is **absent rather than blank.** Still the **nineteenth** session
with an empty sleeve — the count advances on **sessions, not runs**, and this run shares 09-17 with
the three runs that preceded it today. **All four remain untested code paths.**

**ORDERS — NOTHING IN LIMBO OVERNIGHT (§7).** `alpaca.py orders --status all` returns **one row for
the account's entire history**: the 09-03 core VOO buy `d177d8f0-cd0c-41bf-95c1-4772318265fd`,
`status: filled`, terminal. **No order from today exists to resolve or carry forward, because no
order was placed today.** `trade_log.md` correctly left unappended — a run with no fill writes no
trade entry.

**HOUSEKEEPING — ALL THREE CHECKS RAN.** **Week rollover:** the ISO Monday of 2026-09-17
(Thursday) is **2026-09-14**, which **matches `week_of`** — no reset due, next boundary Monday
2026-09-21. **Circuit breaker:** **INACTIVE**, `halt_triggered_at: none`; `consecutive_closed_losses`
stays at **0** because nothing has ever closed in this account, so the §6 streak cannot move, no
`HALT_CLEARED_AT` comparison was required and **no circuit-breaker alert was due.** **Sleeve drift:**
core **69.83%**, inside the band. `open_thesis_ids` stays **none** — all three of today's theses were
rejected before the bell and nothing was opened.

**⚠ THIS RUN FOUND A DELETED JOURNAL HEADER AND RESTORED IT — SEE THE 09-17 JOURNAL ENTRY.** Commit
**`5fe9e4c`** (the 09-16 close run) deleted `### 2026-09-15 (Tuesday)` from `journal.md` while
inserting its own entry above it; that was its **only** deletion. The 09-15 body survived but was
left headerless and glued to 09-16's entry — **a full trading day invisible to any header scan.**
**The top-of-`## Entries` insert is the dangerous edit in this repo**, and it is the edit every close
run makes. Restored, and the check that catches it is one command: **list the `###` headers after
writing and confirm one per trading day.**

**⚠ OPEN ITEM (7) IS UNCHANGED AND THIS RUN DID NOT MEASURE IT.** `alpaca.py move` is structurally
blind to an after-hours event — the five-session window ends at the last official close. **It is a
BUY-path defect and this routine has no buy path.** **GNRC was not looked at for the third
consecutive run today: zero `move`, `quote`, `bars` or `asset` calls.** Tonight's close is the first
that could admit the gap into `bars`, which makes "just check what it did" the most plausible costume
yet — and the one with the least justification from a seat that trades nothing at all. **No run may
reinterpret the filter; that is a human editing §4 or the script.**

---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-17 12:35) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-three blocks spanning 09-01 to today's midday run each recorded the same
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
