# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. **The compaction has now held across three runs.**

```
last_run: 2026-11-16 08:36 ET 2-market-open-execution — selftest 5/5, exit 0. Market CLOSED, 54 min pre-bell; plan carried zero intents, so nothing was due and nothing was placed. No orders, no alerts.
prior_run: 2026-11-16 07:01 ET 1-premarket-research — 4 theses, 4 rejected, 0 accepted; plan dated 2026-11-16 with zero intents. Backfilled the 11-13 price leg; its journal leg stays missing.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.46
satellite_pct: 0.0
cash_pct: 30.54
open_thesis_ids: none
```

---

## Where things stand (2026-11-16, market-open seat, live basis)

- **Equity $98,217.06** · core VOO 99.046311231 sh @ 706.74, mark **688.739**, unrealized
  **−$1,782.93 / −2.547%**, **−0.669%** on the day · **cash exactly $30,000.00**.
- **Sleeves: core 69.46% / satellite 0.00% / cash 30.54%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 534.88` — **a distance readout, not an order.**
  **4.46pp of room to the §2 65% floor.** Core untouched since the 2026-09-03 bootstrap.
- **Satellite sleeve is empty and always has been.** Zero positions, zero orders ever.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no
  distance-to-stop exists. ⚠ **Core VOO is EXEMPT from §5; its −2.547% is NOT a §5.3 reading.**
- **273 theses written, 0 ever accepted.** Breaker **INACTIVE 0/3** · weekly cap **0 of 3** ·
  `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `alerts.md` no open, no systemic incidents.

## What this seat did, and what it could not

**Fired 08:36 ET against a nominal 09:35 — `is_open: false`, 54 minutes before the bell.**
Two independent facts, and the record needs both:

1. **§7 forbids trading while the market is closed**, so no order *could* have been placed.
2. **The plan carried zero intents**, so no order was *owed*.

⚠ **Today the binding constraint was (2), not (1).** Nothing was lost to the clock. A seat that
could not trade and a seat with nothing to trade look identical in a log, and only the first is
a fault — **this was the second.**

**Staleness gate PASSED, not skipped:** `plan_date` **2026-11-16** = today. **No stale-plan
alert was posted and none was due.** Steps 3–7 each ran with no operand: bootstrap retired
(`core_established: true`), zero positions to exit, zero intents to re-validate — **the §4
priced-in re-check is ABSENT today, not passed** — and core inside the band, so no rebalance.

**Week anchor re-derived with `isocalendar`, not inherited:** ISO **2026-W47 wd 1**, Monday
anchor **2026-11-16** = inherited `week_of`. **No reset due**; the §6 cap cannot be stuck.

**Ledger reconciled three sides:** `positions.md` satellite 0 (its one `### <TICKER>` heading is
the template at line 42) · `sleeves` count 0 · `positions` one row, core VOO only. **No
disagreement between Alpaca and the ledger.**

## Carry forward

1. **Routine 2's dispatch landed pre-bell again — 08:36, the tenth such session in eleven EST
   sessions** (11-02 → 11-12 fired 08:35–08:47; 11-13 fired 10:43 mid-session). ⚠ **Recorded,
   NOT diagnosed** — `control.md` forbids diagnosing a schedule fault from a firing time.
   ⚠⚠ **THE OUT-OF-BAND ASK WAS DELIVERED BY THE 11-12 CLOSE SEAT AND WAS DELIBERATELY NOT
   RE-SENT TODAY.** The standing condition to re-send is routine 2 firing *consistently after*
   the bell in a way that changes what the human must fix, or **a seat skipped entirely**.
   Neither happened: this seat ran in full, and **the fault did not bind, because the plan was
   empty.** ⚠ **Re-sending on a day that cost nothing would spend the human's attention on a
   non-event and blunt the alert for the day it does bind.**
2. **NEW — "the official 2026-11-13 close" of 693.05 looks like an IEX print, not the
   consolidated close.** `v` **42,853** shares for a full VOO session is ~1% of true
   consolidated volume. **The `positions` endpoint disagrees: `lastday_price` 693.38, +0.33
   above.** ⚠ **An observation, not a correction** — which print is authoritative was not
   established here. **It compounds item 5:** both say the benchmark series is less
   authoritative than the prose around it claims.
3. **NEW — the 11-13 "15:17 partial bar close" of 692.64 equals that session's `vw` field,
   692.64139, to five significant figures.** The **+0.41 / +0.0592%** gap recorded by the last
   two seats as a sixth data point may be **a close compared against a VWAP.** ⚠ **The series is
   NOT struck** — this seat cannot confirm what the 11-13 close seat read. Flagged for a seat
   that can; an undetected unit mismatch would corrupt every later point.
4. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the **85th** absent-seat ordinal. The first real satellite position is their first live test.
5. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13).
   **Any review using it understates the benchmark by ~1.07%/yr and flatters the agent.** True
   12-month VOO total return **+14.615%**, not the price-only +13.296%.
6. **The paper broker does not pay dividends.** Cash is exactly $30,000.00 — the 2026-09-28 VOO
   distribution (**$180.52**) was never credited. **A run cannot fix 5 or 6.**
7. **STILL MISSING, NOT RECOVERABLE:** the `journal.md` entry for **2026-11-13** and that day's
   ClickUp summary. **No seat has written a backdated narrative, and none should** — the
   recovered figures in `plan_today.md` under BACKFILL are where a reader should look instead.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.25MB**, read by every run. **`positions.md` is ~307KB describing an
empty ledger** and `weekly_review.md` is ~379KB. **Neither is reachable by the monthly
rollover** — `positions.md` is excluded on the premise that it "only ever holds open
positions", false for 74 days. **`positions.md` needs a retention rule from the human; no run
has standing to truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13,
Recurring Error 1.

⚠ **Second standing item, unaddressed:** the agent-authored rejection taxonomy ("rule (iii)" …
"rule (viii)") carries the majority of the rejection load and **exists nowhere in
`strategy.md`**. A reader cannot tell which rejections rest on the strategy and which rest on
rules the system wrote for itself. **Either promote them into §4 or rename them.**
