# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **THIS FILE WAS REWRITTEN COMPACTLY BY THE 2026-11-13 FRIDAY REVIEW: 324KB / 2,988 lines
→ this.** The 13 keys below are unchanged in name, order and format. What was removed was
prose, overwhelmingly a `last_run:` *value* that had grown into a multi-thousand-byte
paragraph. **Nothing factual was lost** — the prior version is at `HEAD:state.md` in git, and
the findings it carried are written up in the `weekly_review.md` entry for 2026-11-13 under
Recurring Error 1. **Keep `last_run` to ONE LINE. A value that needs a paragraph belongs in
`journal.md`.**

```
last_run: 2026-11-13 15:45 ET 5-friday-weekly-review — selftest 5/5, exit 0. Fired PRE-CLOSE (clock is_open true, next_close 16:00) so all figures are partial-bar/live-mark basis, not official close.
prior_run: 2026-11-13 15:15 ET 4-market-close-journal — insurance commit only; its second (post-bell) commit and the 2026-11-13 journal entry DO NOT EXIST. See backfill note below.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.56
satellite_pct: 0.0
cash_pct: 30.44
open_thesis_ids: none
```

---

## Where things stand (2026-11-13, pre-close basis)

- **Equity $98,552.43** · core VOO 99.046311231 sh @ 706.74, mark 692.125, unrealized
  **−$1,447.56 / −2.068%** · **cash exactly $30,000.00**.
- **Sleeves: core 69.56% / satellite 0.00% / cash 30.44%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 434.27` — **a distance readout, not an order.**
- **Satellite sleeve is empty and always has been.** Zero positions, zero orders ever. The
  only fill in account history is the 2026-09-03 VOO core bootstrap.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no
  distance-to-stop exists. ⚠ **Core VOO is EXEMPT from §5; its −2.068% is NOT a §5.3 reading.**
- **269 theses written, 0 ever accepted** (87 + 129 archived, 53 live in `research_log.md`).
- Breaker INACTIVE 0/3 · weekly cap 0/3 used · `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none`
  · `alerts.md` has no open and no systemic incidents.

## Note on `week_of`

Set to **2026-11-16** (next Monday) per the routine 5 Step 6 instruction. ⚠ `week_anchor()`
returns **2026-11-09** for today, so a run firing later today or over the weekend will see a
mismatch and reset `week_of` back to 2026-11-09. **That is harmless** —
`new_positions_this_week` is 0 under either anchor and the §6 cap cannot be stuck — but do not
read it as a corrupted counter.

## ⚠ Backfill owed to Monday's first run

The 2026-11-13 close seat committed before the bell and its post-bell commit never landed.
**Missing and not recoverable from this file:** the official 2026-11-13 VOO close
(`bars --adjustment all`), close-basis equity / day-P&L / sleeve figures, the `journal.md`
entry for 2026-11-13, and that day's ClickUp daily summary. **The weekly review for the week
ending 2026-11-13 was written WITHOUT them.**

## ⚠⚠ Two measurement defects a run cannot fix — for the human

1. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED.** Verified 2026-11-13:
   adjusted and unadjusted closes are **identical to the cent on 259 of 260 sessions**, a
   window spanning all four VOO ex-dividend dates. The routine 5 prompt asserts the opposite.
   **Any review using the flag's output understates the benchmark by ~1.07%/yr and flatters the
   agent.** The 2026-11-13 review reconstructs total return by reinvesting distributions
   (12-month: price-only +13.296% vs **true +14.615%**).
2. **The paper broker does not pay dividends.** `cash` is exactly `30000`, not $30,180.52 —
   the 2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The
   core sleeve is therefore structurally short ~1.07%/yr against any honest total-return
   benchmark, and the gap widens each quarter.

## ⚠⚠⚠ Corpus size — the standing systemic finding

Live memory corpus **1.29MB**, read in full by every run. `positions.md` is **296KB / 3,080
lines describing an empty ledger**; `weekly_review.md` is 348KB. **Neither is reachable by the
monthly rollover** — `positions.md` is excluded on the premise that it "only ever holds open
positions", which has been false for 71 days. **`positions.md` needs a retention rule from the
human; no run has standing to truncate it.** Full write-up: `weekly_review.md`, week ending
2026-11-13, Recurring Error 1. **This file is the one part a run could fix, and did.**
