# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across seven runs.

```
last_run: 2026-11-17 11:41 ET 3-midday-management — selftest 5/5, exit 0. is_open TRUE. Zero satellite positions, so Steps 2-4 had no operand: no backfill due, §5.1-§5.4 not evaluated, 0 exits taken and 0 due. Nothing should have executed and failed to. Exits-only run; the idle $30k was not actionable here.
prior_run: 2026-11-17 08:36 ET 2-market-open-execution — plan FRESH but carried zero intents; 0 orders placed; core bootstrap skipped, rebalance not needed (69.16%).
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.90
satellite_pct: 0.0
cash_pct: 31.10
open_thesis_ids: none
```

---

## Where things stand (2026-11-17, **MID-SESSION BASIS — these are 11:41 marks, not closes**)

- **Equity $96,460.07** · core VOO 99.046311231 sh @ 706.74, live mark **671.00**, unrealized
  **−$3,539.92 / −5.057%** · **cash exactly $30,000.00**. Down **$809.21** on the 08:36 mark.
- **Sleeves: core 68.90% / satellite 0.00% / cash 31.10%.** `core_in_band: true`,
  `rebalance_needed: false`, `rebalance_delta: 1061.97` — **a distance readout, not an order.**
  3.90pp of room to the §2 65% floor. ⚠ It grew from **819.21** (08:36) and **767.98** (07:02)
  purely because VOO fell further; **a rising delta on a falling market is the band working,
  not a buy signal.**
- **Latest official close: VOO 680.36** (`bars`, 2026-11-16). Recent closes: 11-11 **698.25** ·
  11-12 **696.04** · 11-13 **693.05**. ⚠ **The 11-17 figure of 670.91 in today's `bars` pull is
  a PARTIAL SESSION, not a close** — see the confirmed defect below. VOO is **−1.388%** on the
  session so far.
- **Satellite sleeve is empty and always has been.** Zero positions, zero satellite orders ever.
  **Live Alpaca and `positions.md` AGREE — re-reconciled at the midday seat, no discrepancy.**
  `positions` returns exactly one row, the VOO core bootstrap. **§7 overnight exposure is
  structurally zero.**
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists. **No operand: no backfill was due and the Step 2 repair branch
  has still never run against a real mark.** ⚠ **Core VOO is EXEMPT from §5.**
- **277 thesis IDs written, 0 ever accepted — RE-DERIVED AT THE MIDDAY SEAT, NOT CARRIED.**
  `grep -c '^### T-2026'` gives **61** live + **87** + **129** = **277**, the third matching
  derivation today. ⚠ **Re-derive with the grep each time; do not carry this number forward.**
  ⚠ **Method matters: this counts thesis IDs, not items considered** — sweep entries hold many
  items each, so the item count is far higher and the two must not be quoted interchangeably.
  Paths that actually resolve: **`archive/research_log/2026-09.md`**,
  **`archive/research_log/2026-10.md`**.
- Breaker **INACTIVE 0/3** · weekly cap **0/3 used** · `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `alerts.md` has **no open and no systemic incidents**.

## Week rollover — re-derived at this seat, no reset due

`isocalendar` on 2026-11-17 → ISO **2026-W47 wd 2**, Monday anchor **2026-11-16** = inherited
`week_of` **2026-11-16**. They match. `new_positions_this_week` is 0 under any anchor.

## What the midday seat did, and what it is forbidden from doing

**Market was OPEN** (`is_open: true`, `next_close` 16:00). This was the first seat today that
*could* have exited — and **no exit was due, because nothing is held in the satellite sleeve.**
Zero exits taken, zero suppressed, **nothing that should have fired failed to fire.**

⚠ **THIS ROUTINE IS EXITS-ONLY AND THAT BINDS EVEN WHEN EVERY OTHER GATE IS OPEN.** Breaker
INACTIVE, weekly cap 0 of 3, $30,000 idle, `TRADING_ENABLED: true`, Notes **(none)** — and none
of that permits an entry here. **A midday buy would route around the one mechanism that forces
every position to sleep on a written thesis.** The idle cash is a fact to report, not an
opportunity to act on at this seat.

- **Steps 2, 3 and 4 had no operand.** No `highest_close` to check for staleness, no
  `invalidation` string to test against the news, no deadline to compare, no position to size a
  stop against. **No Perplexity call was made and none was due** — §5.1 is evaluated against a
  condition written at entry, and there is no entry.
- **§5.4 has still never been armed.** It arms on the first *satellite* fill.
- **Step 5 wrote no per-position `sell_rule_status`** because there is no position to write one
  for. The dated digest in `positions.md` carries the reconciliation instead.

## ⚠⚠⚠ The in-progress-bar defect is CONFIRMED LIVE — first observation, promote it

Carry-forward item 5 has been carried for weeks as a *predicted* failure. **The midday seat saw
it.** `bars --symbol VOO --days 7 --adjustment all`, pulled at **11:41 with `clock.is_open:
true`**, returned a **2026-11-17 row with `c: 670.91`** — an unfinished session priced as a
completed bar. **Both of today's pre-bell pulls returned no 11-17 row**, which is precisely why
neither earlier seat could observe it.

**A seat taking `max(c)` from that pull would have written a partial-session print into
`highest_close`.** Today it happens to fail harmless — 670.91 < 680.36, so the max is unchanged.
**On a green session it would ratchet the §5.4 trailing stop UP off a number that is not a
close, and §5.4 fails in the direction of SELLING.** The bar carries **no flag**: nothing in
`t`, `c`, `n` or `v` distinguishes it from a finished session.

⚠ **RULE, NOW EVIDENCED RATHER THAN ANTICIPATED: gate every `highest_close` write on `clock`,
never on the shape or presence of the bar. Re-pull the whole window and take the max from that
one call, on one adjustment basis, and drop today's row whenever `is_open` is true.**

## Carry forward

1. ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-02 → 11-12 fired
   08:35–08:47 (`is_open: false`); 11-13 fired 10:43 mid-session; **11-16 did not fire at all**;
   **11-17 fired 08:36, back to the pre-bell shape.** Sent out of band 11-12, re-sent 11-16 on
   the "skipped entirely" condition. Re-send **only** if routine 2 begins firing consistently
   *after* the bell in a way that changes what the human must fix. **A repeat pre-bell firing is
   not new information, and on a zero-intent day it costs nothing.** ⚠ Per `control.md` this is
   **recorded, not diagnosed** — a firing time is not a schedule fault, and manual "Run now"
   invocations are indistinguishable from scheduled ones. **All four seats share the same −1h
   EST shape**: pre-market 07:02 vs nominal 08:00 (16th consecutive EST session); midday **11:41
   vs nominal 12:30**, matching every midday seat since 11-03 (11:40–11:48).
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly
   the two it omitted**, and they are the two with no other source. A price is recoverable from
   the broker three days later; **a narrative nobody wrote is not.** 11-16 did it correctly.
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST.** The
   11-16 close seat published "the worst session in this account's history" to ClickUp and it was
   **false by a factor of two** (11-05: −4.3731% VOO / −3.0586% account). **Every run starts with
   no memory and is structurally predisposed to mistake the largest number in front of it for the
   largest number.** One `bars` pull and a sort falsifies it. ⚠ **Live relevance: VOO is in a
   multi-session slide (698.25 → 696.04 → 693.05 → 680.36 → 670.91 intraday) and the core is
   −5.057% from its fill. The close seat will be tempted by exactly this superlative. Rank first.**
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — FIFTH
   distinct instance, re-measured at the midday seat.** `positions.lastday_price` **680.26** vs
   `bars` close **680.36** for 2026-11-16: gap **0.10 / 0.0147%**, identical to both earlier
   readings today. Prior: 11-13 **+0.33 / +0.0476%**; 11-16 post-bell live mark 680.09 vs
   official 680.36, gap **0.27**. **Not a dividend-basis artifact** — adjusted and unadjusted
   agree to the cent. **Build P&L and stamp `highest_close` from official `bars` closes only, on
   one adjustment basis, pulled in one call.**
5. **PROMOTED OUT OF THIS LIST — the in-progress-bar defect is no longer a prediction.** See the
   confirmed-live section above. The mitigation is unchanged; its status is now *observed*.
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the 89th absent-seat ordinal. The first real satellite position will be their first live test.
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
10. ⚠ **PATH LABEL — affects anyone re-running the thesis grep.** The research archives live at
   **`archive/research_log/2026-09.md`** and **`archive/research_log/2026-10.md`**. Earlier states
   abbreviated these as `archive/2026-09` / `archive/2026-10`, which **does not resolve as a
   path** — a seat pasting it will silently get zero and under-count by 216.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.28MB**, read by every run. **`positions.md` is ~327KB describing an empty
ledger** and `weekly_review.md` is 379KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has
been false for 76 days. **`positions.md` needs a retention rule from the human; no run has
standing to truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring
Error 1. ⚠ The midday seat added one digest note and **claims no collapse ratio** — the line
count is the wrong instrument and every "collapsed N → M" figure in that file is measured with it.

⚠ **Second standing item, same reviewer, unaddressed:** the agent-authored rejection taxonomy
("rule (iii)" … "rule (viii)") now carries the majority of the rejection load and **exists
nowhere in `strategy.md`**. A reader cannot tell which rejections rest on the strategy and which
rest on rules the system wrote for itself. **Either promote them into §4 or rename them so the
distinction is visible from the page.**

⚠ **Both items are already with the human in `weekly_review.md`. The midday seat deliberately
sent NO notification** — nothing was owed, nothing was missed, no incident is open, and
re-pinging a standing item daily trains the human to ignore the channel.
