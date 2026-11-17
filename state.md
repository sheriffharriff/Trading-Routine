# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across six runs.

```
last_run: 2026-11-17 08:36 ET 2-market-open-execution — selftest 5/5, exit 0. is_open FALSE, 54 min pre-bell. Plan FRESH (plan_date = today) but carried zero intents: 0 orders placed, 0 skipped-for-cause. Core bootstrap skipped (established), rebalance not needed (69.16%, in band). Nothing executed and nothing owed.
prior_run: 2026-11-17 07:02 ET 1-premarket-research — four theses, all four REJECTED; zero BUY/SELL/REBALANCE intents; plan dated 2026-11-17.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.16
satellite_pct: 0.0
cash_pct: 30.84
open_thesis_ids: none
```

---

## Where things stand (2026-11-17, **PRE-MARKET BASIS — these are 08:36 marks, not closes**)

- **Equity $97,269.28** · core VOO 99.046311231 sh @ 706.74, pre-bell mark **679.17**,
  unrealized **−$2,730.71 / −3.901%** · **cash exactly $30,000.00**.
- **Sleeves: core 69.16% / satellite 0.00% / cash 30.84%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 819.21` — **a distance readout, not an order.**
  4.16pp of room to the §2 65% floor. ⚠ It grew from **767.98** at 07:02 purely because VOO fell
  further; **a rising delta on a falling market is the band working, not a buy signal.**
- **Latest official close: VOO 680.36** (`bars`, 2026-11-16). ⚠ **Do not restate pre-market marks
  as closes.** Recent official closes: 11-11 **698.25** · 11-12 **696.04** · 11-13 **693.05**.
- **Satellite sleeve is empty and always has been.** Zero positions, zero satellite orders ever.
  **Live Alpaca and `positions.md` AGREE — re-reconciled at the market-open seat, no discrepancy.**
  `positions` returns exactly one row, the VOO core bootstrap. **§7 overnight exposure is
  structurally zero.**
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists. **No operand: no `highest_close` stamped and none was due.**
  ⚠ **Core VOO is EXEMPT from §5.**
- **277 thesis IDs written, 0 ever accepted — RE-DERIVED AT THE MARKET-OPEN SEAT, NOT CARRIED.**
  `grep -c '^### T-2026'` gives **61** live + **87** + **129** = **277**, matching the 07:02
  figure exactly. **The 11-16 over-count by four is not propagating.** ⚠ **Re-derive with the
  grep each time; do not carry this number forward.** ⚠ **Method matters: this counts thesis IDs,
  not items considered** — sweep entries hold many items each, so the item count is far higher
  and the two must not be quoted interchangeably.
- Breaker **INACTIVE 0/3** · weekly cap **0/3 used** · `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `alerts.md` has **no open and no systemic incidents**.

## Week rollover — re-derived at this seat, no reset due

`isocalendar` on 2026-11-17 → ISO **2026-W47 wd 2**, Monday anchor **2026-11-16** = inherited
`week_of` **2026-11-16**. They match. `new_positions_this_week` is 0 under any anchor.

## What the market-open seat did, and the one distinction that matters

**It placed nothing, and the reason is NOT that the market was closed.**

The §2/§4/§6 gates were all open: breaker INACTIVE, weekly cap 0 of 3, satellite sleeve 0.0%
deployed with $30,000 idle, `TRADING_ENABLED: true`, Notes **(none)**. The staleness gate
**PASSED** — `plan_date` **2026-11-17 = today**, so the plan was fresh and its intents would have
been *consumable*. **There simply were none: zero BUY, zero SELL, zero REBALANCE.**

⚠⚠ **SO THE CLOSED MARKET BLOCKED NOTHING, AND THIS RUN MUST NOT BE FILED AS A §7
CLOSED-MARKET SKIP.** With no orders to place, `is_open: false` cost exactly zero. The
hold-for-the-bell procedure in `plan_today.md` is conditioned on the plan carrying an intent;
it carried none, **so no hold was due and none was performed.** A future seat reading "fired
pre-bell, placed nothing" must not infer that something was lost.

- **§2 core bootstrap: SKIPPED**, `core_established: true`. That path never runs again.
- **§7 rebalance: NOT NEEDED**, core 69.16% inside the 65–75% band.
- **No stale-plan alert was due and none was posted.**
- ⚠ **The priced-in check ran ZERO times at this seat — third consecutive session** — because no
  BUY intent existed to re-check. The 11-13 hypothesis (that well-formed and already-priced may
  be the same property) gains **no data in either direction.** It needs `move_pct` on candidates
  that actually *reach* the filters.

## Carry forward

1. ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-02 → 11-12 fired
   08:35–08:47 (`is_open: false`); 11-13 fired 10:43 mid-session; **11-16 did not fire at all**;
   **11-17 fired 08:36, back to the pre-bell shape.** Sent out of band 11-12, re-sent 11-16 on
   the "skipped entirely" condition. Re-send **only** if routine 2 begins firing consistently
   *after* the bell in a way that changes what the human must fix. **A repeat pre-bell firing is
   not new information, and on a zero-intent day it costs nothing.** ⚠ Per `control.md` this is
   **recorded, not diagnosed** — a firing time is not a schedule fault, and manual "Run now"
   invocations are indistinguishable from scheduled ones. The 07:02 pre-market seat fired against
   a nominal 08:00, the same −1h shape, **15th consecutive EST session**.
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly
   the two it omitted**, and they are the two with no other source. A price is recoverable from
   the broker three days later; **a narrative nobody wrote is not.** 11-16 did it correctly.
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST.** The
   11-16 close seat published "the worst session in this account's history" to ClickUp and it was
   **false by a factor of two** (11-05: −4.3731% VOO / −3.0586% account). **Every run starts with
   no memory and is structurally predisposed to mistake the largest number in front of it for the
   largest number.** One `bars` pull and a sort falsifies it.
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — re-measured
   at the market-open seat, FOURTH distinct instance.** `positions.lastday_price` **680.26** vs
   `bars` close **680.36** for 2026-11-16: gap **0.10 / 0.0147%**, identical to the 07:02 reading.
   Prior: 11-13 **+0.33 / +0.0476%**; 11-16 post-bell live mark 680.09 vs official 680.36, gap
   **0.27**. **Not a dividend-basis artifact** — adjusted and unadjusted agree to the cent.
   **Build P&L and stamp `highest_close` from official `bars` closes only, on one adjustment
   basis, pulled in one call.**
5. **The in-progress-session bar defect is still live.** A mid-session `bars` pull returns the
   unfinished session as a bar; a seat taking `max(c)` would fold it into `highest_close`.
   **Gate any high-water write on `clock`, never on the shape of the bar.** ⚠ Both of today's
   pre-bell pulls returned **no 2026-11-17 row**, consistent and not in play at that hour.
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the 88th absent-seat ordinal. The first real satellite position will be their first live test.
7. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13:
   adjusted and unadjusted closes identical to the cent on 259 of 260 sessions, across all four
   VOO ex-dividend dates). **Any review using the flag's output understates the benchmark and
   flatters the agent.** True 12-month VOO total return is **+14.615%**.
8. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark. **A run
   cannot fix either 7 or 8.**
9. **STILL MISSING AND NOT RECOVERABLE:** the `journal.md` entry for **2026-11-13** and that
   day's ClickUp daily summary. The price leg was discharged (VOO 693.05, equity 98,644.05, core
   69.59%, day −0.430%); **no seat has written, or should write, a backdated close-day narrative.**
10. ⚠ **PATH LABEL CORRECTION — affects anyone re-running the thesis grep.** The research
   archives live at **`archive/research_log/2026-09.md`** and **`archive/research_log/2026-10.md`**.
   Earlier states abbreviated these as `archive/2026-09` / `archive/2026-10`, which **does not
   resolve as a path** — a seat pasting it will silently get zero and under-count by 216.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.27MB**, read by every run. **`positions.md` is ~325KB describing an empty
ledger** and `weekly_review.md` is 379KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has
been false for 75 days. **`positions.md` needs a retention rule from the human; no run has
standing to truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring
Error 1. ⚠ The market-open seat added the shortest digest it could and **claims no collapse
ratio** — the line count is the wrong instrument and every "collapsed N → M" figure in that file
is measured with it.

⚠ **Second standing item, same reviewer, unaddressed:** the agent-authored rejection taxonomy
("rule (iii)" … "rule (viii)") now carries the majority of the rejection load and **exists
nowhere in `strategy.md`**. A reader cannot tell which rejections rest on the strategy and which
rest on rules the system wrote for itself. **Either promote them into §4 or rename them so the
distinction is visible from the page.**
