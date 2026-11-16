# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction held across this run.

```
last_run: 2026-11-16 07:01 ET 1-premarket-research — selftest 5/5, exit 0. 4 theses, 4 rejected, 0 accepted; plan dated 2026-11-16 with zero intents. Backfilled the 11-13 official close.
prior_run: 2026-11-13 15:45 ET 5-friday-weekly-review — pre-close basis. The 11-13 close seat's second commit never landed; its price leg is now backfilled (below), its journal entry is not.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.50
satellite_pct: 0.0
cash_pct: 30.50
open_thesis_ids: none
```

---

## Where things stand (2026-11-16, pre-market basis)

- **Equity $98,345.92** · core VOO 99.046311231 sh @ 706.74, mark 690.04, unrealized
  **−$1,654.07 / −2.363%** · **cash exactly $30,000.00**.
- **Sleeves: core 69.50% / satellite 0.00% / cash 30.50%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 496.23` — **a distance readout, not an order.**
  4.50pp of room to the §2 65% floor.
- **Satellite sleeve is empty and always has been.** Zero positions, zero orders ever. The only
  fill in account history is the 2026-09-03 VOO core bootstrap.
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no
  distance-to-stop exists. ⚠ **Core VOO is EXEMPT from §5; its −2.363% is NOT a §5.3 reading.**
- **273 theses written, 0 ever accepted** (4 added today; 87 + 129 archived, 57 live in
  `research_log.md`).
- Breaker INACTIVE 0/3 · weekly cap 0/3 used · `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none`
  · `alerts.md` has no open and no systemic incidents.

## Week rollover — resolved, no reset was due

ISO **2026-W47 wd 1**, Monday anchor **2026-11-16** = inherited `week_of` **2026-11-16**. They
match. ⚠ **The 11-13 review set `week_of` forward to next Monday and warned that a weekend run
would reset it backward to 2026-11-09. No seat ran in between, so the forward-set value is simply
correct today and the warning never bound.** `new_positions_this_week` is 0 under any anchor; the
§6 cap cannot be stuck.

## ✅ Backfill owed to this run — price leg discharged, journal leg is not

`bars --symbol VOO --days 6 --adjustment all`, pulled at this seat:

- **Official 2026-11-13 VOO close: 693.05** (`n` 2,492 · `v` 42,853).
- Close-basis **equity $98,644.05** · core **69.59%** · satellite 0.00% · cash **30.41%** ·
  unrealized **−$1,355.94 / −1.937%** · day P&L **−$296.15 / −0.430%** vs the 11-12 close 696.04.
- ⚠ **Settles the measurement the 11-13 close seat left open:** its 15:17 partial bar read
  **692.64**; the official close is **693.05**. **The gap is +0.41 / +0.0592%.**

⚠⚠ **STILL MISSING AND NOT RECOVERABLE BY ANY LATER SEAT:** the `journal.md` entry for
**2026-11-13** and that day's **ClickUp daily summary**. **This run deliberately did NOT write a
backdated journal entry.** `journal.md` belongs to the close routine; a pre-market seat inventing
a close-day narrative three days after the fact would file something no seat observed, which is
worse than a gap that is labelled. **The figures above are where a reader should look instead.**
⚠ **The weekly review for the week ending 2026-11-13 was written without them and is not
retro-corrected here.**

## Carry forward

1. **Routine 2's dispatch time changed shape on 2026-11-13 — in the benign direction.** Nine
   consecutive EST sessions (11-02 → 11-12) fired pre-bell at 08:35–08:47 and could not execute.
   **On 11-13 it fired at 10:43 with `is_open: true`, mid-session, for the first time in ten
   sessions.** ⚠ **Not diagnosed, only recorded** — `control.md` forbids diagnosing a schedule
   fault from a firing time, and one session is not a trend. ⚠⚠ **The out-of-band ask to the
   human was delivered by the 11-12 close seat and MUST NOT be re-sent:** the change is toward
   the fault not binding, which is not an escalation. **Re-send only if routine 2 starts firing
   consistently after the bell in a way that changes what the human must fix, or if a seat is
   skipped entirely.** This seat fired at **07:01 against a nominal 08:00 — thirteenth
   consecutive EST session** at −1h.
2. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the 84th absent-seat ordinal. The first real satellite position will be their first live test,
   and the seat that opens it should expect to be exercising untested code on day one.
3. **The 11-13 "well-formed ⇒ already-priced" hypothesis gained ZERO data points today** — no
   candidate reached the hard filters, so no `move` call was made. ⚠ **Recorded as a null, not as
   support. Two instances remain two instances, and only the human may promote it to a rule.**
4. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13:
   adjusted and unadjusted closes identical to the cent on 259 of 260 sessions, across all four
   VOO ex-dividend dates). **Any review using the flag's output understates the benchmark by
   ~1.07%/yr and flatters the agent.** True 12-month VOO total return is **+14.615%**, not the
   price-only +13.296%.
5. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark, and the gap
   widens each quarter. **A run cannot fix either 4 or 5.**

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.25MB**, read by every run. **`positions.md` is 302KB describing an empty
ledger** and `weekly_review.md` is 348KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has
been false for 74 days. **`positions.md` needs a retention rule from the human; no run has
standing to truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring
Error 1.

⚠ **Second standing item, same reviewer, unaddressed:** the agent-authored rejection taxonomy
("rule (iii)" … "rule (viii)") now carries the majority of the rejection load and **exists
nowhere in `strategy.md`**. A reader cannot tell which rejections rest on the strategy and which
rest on rules the system wrote for itself. **Either promote them into §4 or rename them so the
distinction is visible from the page.** Today's entries cite §4 parts directly and use the
sub-rule numbering only as cross-reference shorthand.
