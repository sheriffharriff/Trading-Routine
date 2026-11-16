# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across three runs.

```
last_run: 2026-11-16 11:41 ET 3-midday-management — selftest 5/5, exit 0. Market OPEN, zero satellite positions, ZERO EXITS (no operand), zero orders. No high-water repair due. Core VOO exempt.
prior_run: 2026-11-16 07:01 ET 1-premarket-research — 4 theses, 4 rejected, 0 accepted; plan dated 2026-11-16 with zero intents; backfilled the 11-13 official close 693.05.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.36
satellite_pct: 0.0
cash_pct: 30.64
open_thesis_ids: none
```

---

## Where things stand (2026-11-16, midday basis — market OPEN)

- **Equity $97,912.09** · core VOO 99.046311231 sh @ 706.74, mark **685.66**, unrealized
  **−$2,087.90 / −2.983%** · **cash exactly $30,000.00**.
- **Sleeves: core 69.36% / satellite 0.00% / cash 30.64%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 626.37` — **a distance readout, not an order.**
  4.36pp of room to the §2 65% floor. ⚠ Rebalancing is the market-open seat's job under §2.
- **Satellite sleeve is empty and always has been.** Zero positions, zero satellite orders ever;
  `orders --status open` → `[]`, nothing in limbo. The only fill in account history is the
  2026-09-03 VOO core bootstrap.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists, so **zero Perplexity queries were spent on position review.**
  ⚠ **Core VOO is EXEMPT from §5; its −2.983% is NOT a §5.3 reading** — and it is now past the
  magnitude at which §5.3 would fire on a satellite name, which is exactly why the exemption is
  applied before the arithmetic, not after.
- **273 theses written, 0 ever accepted.** Breaker INACTIVE 0/3 · weekly cap 0/3 used ·
  `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `alerts.md` has no open and no systemic
  incidents.

## Week rollover — re-derived, no reset due

`isocalendar` on 2026-11-16 → ISO **2026-W47 wd 1**, Monday anchor **2026-11-16** = inherited
`week_of` **2026-11-16**. They match. `new_positions_this_week` is 0 under any anchor; the §6
cap cannot be stuck.

## ⚠⚠ Open for the close seat — routine 2 has not committed today

As of **11:41 ET** the last commit on `main` was the **07:08 UTC pre-market**; there is **no
`2-market-open` commit for 2026-11-16**, ~2h past its nominal 09:35 and past the **10:43** at
which it fired on 11-13. ⚠ **RECORDED, NOT DIAGNOSED** — `control.md` forbids diagnosing a
schedule fault from a firing time, and the midday seat cannot distinguish *skipped* from *late*
while the session runs to 16:00. ⚠ **NOTHING WAS LOST EITHER WAY:** `plan_today.md` is dated
2026-11-16 and carries **ZERO intents**, and core is in band, so that seat had no execution to
perform. ⚠⚠ **CLOSE SEAT: you can settle this and the midday seat could not.** If no
`2-market-open` commit for 2026-11-16 exists when you run, that is **a seat skipped entirely** —
the one condition carry-forward 1 names as warranting re-sending the out-of-band ask. **Do not
re-send it on the midday seat's observation alone.**

## Carry forward

1. **Routine 2's dispatch has moved twice and is now unrecorded for a session.** Nine consecutive
   EST sessions (11-02 → 11-12) fired pre-bell at 08:35–08:47 and could not execute; **11-13
   fired at 10:43 with `is_open: true`, mid-session, for the first time in ten sessions**; **today
   it has not fired at all as of 11:41** (above). ⚠⚠ **The out-of-band ask delivered by the 11-12
   close seat MUST NOT be re-sent on a timing observation** — the 11-13 change was toward the
   fault not binding. **Re-send only if routine 2 starts firing consistently after the bell in a
   way that changes what the human must fix, or if a seat is confirmed skipped entirely.** This
   midday seat fired at **11:41 against a nominal 12:30**.
2. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the 85th absent-seat ordinal. The first real satellite position will be their first live test,
   and the seat that opens it should expect to be exercising untested code on day one.
3. ⚠⚠ **NEW (this seat) — THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE, AND §5.4 READS FROM ONE
   OF THEM.** `positions.lastday_price` = **693.38** for 2026-11-13; `bars` `c` for that session
   = **693.05**. **Gap +0.33 / +0.0476%.** ⚠ **Not the ex-dividend basis artifact** — `bars
   --adjustment all` and unflagged `bars` both return 693.05 to the cent across this window, so
   the bases agree and the disagreement is **between endpoints**. **A `highest_close` stamped
   from `lastday_price` and compared against a `bars` close manufactures a ±0.05%-scale phantom
   move.** The `positions.md` procedure (pull the whole window from `bars` in one call) is
   correct and now load-bearing for a second, independent reason. Day-P&L likewise splits:
   **−1.113%** off `lastday_price`, **−1.067%** off the `bars` close.
4. **The in-progress-session bar defect (found 2026-11-11) is still live — confirmed today.**
   `bars` returns the current unfinished session as a bar (2026-11-16: `c` 685.84, `n` 711,
   `v` 11,886). A seat taking `max(c)` over the pull would fold it into `highest_close`.
5. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13:
   adjusted and unadjusted closes identical to the cent on 259 of 260 sessions, across all four
   VOO ex-dividend dates). **Any review using the flag's output understates the benchmark by
   ~1.07%/yr and flatters the agent.** True 12-month VOO total return is **+14.615%**, not the
   price-only +13.296%.
6. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark. **A run
   cannot fix either 5 or 6.**
7. **STILL MISSING AND NOT RECOVERABLE BY ANY LATER SEAT:** the `journal.md` entry for
   **2026-11-13** and that day's ClickUp daily summary. The price leg was discharged by the 11-16
   pre-market seat (VOO 693.05, equity 98,644.05, core 69.59%, day −0.430%); **no seat has
   written, or should write, a backdated close-day narrative.** The weekly review for the week
   ending 2026-11-13 was written without them and is not retro-corrected.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.25MB**, read by every run. **`positions.md` is ~310KB describing an empty
ledger** and `weekly_review.md` is 379KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has
been false for 74 days. **`positions.md` needs a retention rule from the human; no run has
standing to truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring
Error 1.

⚠ **Second standing item, same reviewer, unaddressed:** the agent-authored rejection taxonomy
("rule (iii)" … "rule (viii)") now carries the majority of the rejection load and **exists
nowhere in `strategy.md`**. A reader cannot tell which rejections rest on the strategy and which
rest on rules the system wrote for itself. **Either promote them into §4 or rename them so the
distinction is visible from the page.**
