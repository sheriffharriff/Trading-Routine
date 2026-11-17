# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across five runs.

```
last_run: 2026-11-17 07:02 ET 1-premarket-research — selftest 5/5, exit 0. Four theses, all four REJECTED; zero BUY/SELL/REBALANCE intents; plan dated 2026-11-17. New positions were permitted throughout — the candidates failed, not the gates.
prior_run: 2026-11-16 16:05 ET 4-market-close-journal — official close 680.36 recorded, hold succeeded, no backfill owed; routine 2 settled as skipped for the whole session.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.21
satellite_pct: 0.0
cash_pct: 30.79
open_thesis_ids: none
```

---

## Where things stand (2026-11-17, **PRE-MARKET BASIS — these are 07:02 marks, not closes**)

- **Equity $97,440.08** · core VOO 99.046311231 sh @ 706.74, pre-market mark **680.8944**,
  unrealized **−$2,559.91 / −3.657%** · **cash exactly $30,000.00**.
- **Sleeves: core 69.21% / satellite 0.00% / cash 30.79%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 767.98` — **a distance readout, not an order.**
  4.21pp of room to the §2 65% floor. ⚠ Rebalancing is the market-open seat's job under §2.
- **Yesterday's official close: VOO 680.36** (`bars`, 2026-11-16). Day change +0.093% on the
  pre-market mark. ⚠ **Do not restate pre-market marks as closes.**
- **Satellite sleeve is empty and always has been.** Zero positions, zero satellite orders ever.
  **Live Alpaca and `positions.md` AGREE — no discrepancy to reconcile.** `positions` returns
  exactly one row, the VOO core bootstrap. **§7 overnight exposure is structurally zero.**
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists. **No operand: no `highest_close` stamped and none was due.**
  ⚠ **Core VOO is EXEMPT from §5.**
- **277 thesis IDs written, 0 ever accepted — COUNTED, NOT INHERITED, AND THE CARRIED FIGURE WAS
  WRONG.** `grep -c '^### T-2026'` gives **61** live + **87** (`archive/2026-09`) + **129**
  (`archive/2026-10`) = **277**, and that **already includes today's four**. The inherited claim
  said **277 as of 2026-11-16**, so it **over-counted by exactly 4** — the 11-16 seat appears to
  have added its own four to a base that already carried them. ⚠ **Had this seat written
  "277 + 4 = 281" it would have propagated the error a second time, which is what it drafted
  first.** ⚠ **Method matters: this counts thesis IDs, not items considered.** Sweep entries hold
  many items each (today's holds **15**), so the item count is far higher and the two must not be
  quoted interchangeably. **Re-derive with the grep; do not carry this number forward.**
  Breaker INACTIVE 0/3 ·
  weekly cap 0/3 used · `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `alerts.md` has no
  open and no systemic incidents.

## Week rollover — re-derived, no reset due

`isocalendar` on 2026-11-17 → ISO **2026-W47 wd 2**, Monday anchor **2026-11-16** = inherited
`week_of` **2026-11-16**. They match. `new_positions_this_week` is 0 under any anchor.

## Today's research finding, recorded as one data point and not promoted

**The window was NOT eventless, which is a different shape from 11-16's null.** Both drill
queries confirmed a **real, dated, well-sourced, quantified event existed** — and both candidates
still died:

- **BIS interim final rule** (first disclosed 11-16): licences now required for advanced AI chips
  shipped to data centres in Singapore/Thailand/Malaysia/Indonesia/Brazil, plus a 90-day clock on
  overseas facilities serving China/Macau-headquartered customers. **Died at part 1 on DIRECTION:**
  every §3-eligible beneficiary carries the very Asia-Pacific book the rule encumbers, so the net
  sign is undetermined. ⚠ **This complex normally dies because a repricing is not a transaction.
  Today it genuinely WAS a transaction and died anyway.**
- **ExxonMobil's Longtail FID** (11-17, $12.5B project; SBM Offshore the FPSO, Saipem SURF at up
  to $1.5B). **Died at §3: both named contractors are foreign-listed** (Amsterdam, Milan), the
  source states **zero equipment suppliers are named**, and the only US-listed party is **XOM,
  paying the capex out**. Part 3 ~16 quarters besides.

⚠ **So today's binding constraint was UNIVERSE ELIGIBILITY AND SIGN, not the part-1 absence the
last three weekly reviews name as the standing bottleneck.** One data point. **Not a pattern, and
a seat may not invent a standing rule mid-run.**
⚠ **The priced-in check ran ZERO times — second consecutive session** — so the 11-13 hypothesis
(that well-formed and already-priced may be the same property) gained **no new data on either
side.** It needs `move_pct` on candidates that *reach* the filters.

## Carry forward

1. ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-02 → 11-12 fired
   08:35–08:47 (`is_open: false`, could not execute); 11-13 fired 10:43 mid-session; **11-16 did
   not fire at all** — `git log` confirms no `2-market-open` commit for that date, the first
   whole-session absence. **Sent out of band 11-12, re-sent 11-16 on the "skipped entirely"
   condition.** Re-send **only** if routine 2 begins firing consistently *after* the bell in a way
   that changes what the human must fix. **A second whole-session absence is not new information.**
   ⚠ Per `control.md` this is **recorded, not diagnosed** — a firing time is not a schedule fault,
   and manual "Run now" invocations are indistinguishable from scheduled ones. This seat fired at
   **07:02** against a nominal 08:00, the same −1h shape, **14th consecutive EST session**.
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly the
   two it omitted**, and they are the two with no other source. A price is recoverable from the
   broker three days later; **a narrative nobody wrote is not.** 11-16 did it correctly.
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST.** The
   11-16 close seat published "the worst session in this account's history" to ClickUp and it was
   **false by a factor of two** (11-05: −4.3731% VOO / −3.0586% account). **Every run starts with
   no memory and is structurally predisposed to mistake the largest number in front of it for the
   largest number.** One `bars` pull and a sort falsifies it.
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — recurred
   today, third distinct instance.** `positions.lastday_price` **680.26** vs `bars` close
   **680.36** for 2026-11-16: gap **0.10 / 0.0147%**. Prior readings: 11-13 **+0.33 / +0.0476%**;
   11-16 post-bell live mark 680.09 vs official 680.36, gap **0.27**. **Not a dividend-basis
   artifact** — adjusted and unadjusted agree to the cent. **Build P&L and stamp `highest_close`
   from official `bars` closes only, on one adjustment basis, pulled in one call.**
5. **The in-progress-session bar defect is still live.** A mid-session `bars` pull returns the
   unfinished session as a bar; a seat taking `max(c)` would fold it into `highest_close`.
   **Gate any high-water write on `clock`, never on the shape of the bar.** ⚠ Today's pre-market
   pull returned **no 2026-11-17 row**, consistent and not in play at this hour.
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the 87th absent-seat ordinal. The first real satellite position will be their first live test.
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

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.27MB**, read by every run. **`positions.md` is ~319KB describing an empty
ledger** and `weekly_review.md` is 379KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has
been false for 75 days. **`positions.md` needs a retention rule from the human; no run has
standing to truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring
Error 1. ⚠ This seat added the shortest digest it could and **claims no collapse ratio** — the
line count is the wrong instrument and every "collapsed N → M" figure in that file is measured
with it.

⚠ **Second standing item, same reviewer, unaddressed:** the agent-authored rejection taxonomy
("rule (iii)" … "rule (viii)") now carries the majority of the rejection load and **exists
nowhere in `strategy.md`**. A reader cannot tell which rejections rest on the strategy and which
rest on rules the system wrote for itself. **Either promote them into §4 or rename them so the
distinction is visible from the page.** ⚠ Today's entries lean on §3, §4 parts 1–3 and rule (iv)
explicitly, so the ambiguity is live in this run's output too.
