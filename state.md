# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** The 2026-11-13 review compacted this file from 324KB /
2,988 lines after its `last_run` value had grown into a multi-thousand-byte paragraph; it
regrew ×7.8 and was compacted again on 11-20. **A value that needs a paragraph belongs in
`journal.md`.** See `weekly_review.md` 2026-11-20, Recurring Error 8.

```
last_run: 2026-11-25 16:06 ET 4-market-close-journal — RESTAMPED ON THE OFFICIAL CLOSE, insurance commit d591db1 discharged. Selftest 5/5 exit 0. Fired 15:15 for 16:15 (~15th) and HELD: post-bell signature 16:00:45, both dates 2026-11-27, 5-min settle, one `bars` call. Official close VOO 658.735. Equity 95,245.27, day −0.2008%, inception −4.7547%. ZERO satellite positions — Step 2 had NO OPERAND: `positions.md` has NO `highest_close` FIELD AT ALL, so no mark was updated and none was owed. ABSENT ≠ STALE. Core 68.5024% in band. Breaker INACTIVE 0/3, cap 0/3. Friday 2026-11-27 13:00 early close BROKER-VERIFIED.
prior_run: 2026-11-25 11:41 ET 3-midday-management — selftest 5/5 exit 0. Market OPEN. ZERO satellite positions, Steps 2-5 NO OPERAND. 0 sells. Core 67.95% in band. Breaker INACTIVE 0/3, cap 0/3.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.50
satellite_pct: 0.0
cash_pct: 31.50
open_thesis_ids: none
```

---

## Where things stand (2026-11-25, **POST-BELL — official close recorded**)

- ⚠⚠ **STEP 2 — THE ONE JOB THIS ROUTINE EXISTS FOR — HAD NO OPERAND, AND THE SHAPE OF THAT
  MATTERS TO THE NEXT RUN.** `positions.md` contains **no `highest_close` field and no `(as of …)`
  date at all** — not a stale mark, not a missed update, but **no field**, because no satellite
  position has ever been opened. The routine's rule (*update the date every day so a current mark is
  distinguishable from a stale one*) **presumes a field that does not exist here.** 🛑 **THE MIDDAY
  RUN DECIDES WHETHER TO BACKFILL OFF THAT DATE: it will find nothing, and nothing is the correct
  answer. ABSENT ≠ STALE ≠ CURRENT-AND-UNCHANGED. Do not spend a `bars` backfill chasing a mark that
  was never created.** No adjustment-basis hazard arose either, because no stored mark exists to be
  compared across bases.
- ⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING.** No satellite `entry_price`, `highest_close`, deadline or
  `invalidation` string exists. Stated so a later seat does not read them as checks that cleared:
  §5.1 had no name and no condition, so **no `perplexity` call was owed or spent**; §5.2 has no
  deadline; §5.3 no entry price; §5.4 no mark. **All four remain UNEXECUTED CODE at 90 absent seats
  / 86 absent dates** (today already counted by the 09:35 seat — four seats of one empty day is one
  fact about the ledger, not four).
- ✅ **OFFICIAL CLOSE RECORDED, AND THE HOLD IS WHY.** `clock` polled from 15:18 to the post-bell
  signature at **16:00:45** — `is_open: false` with **both** `next_open` and `next_close` on
  **2026-11-27**, the only reading that separates post-bell from pre-market — then a 5-minute
  settle, then **one** `bars` call on one adjustment basis. **VOO 658.735 on 237,062 shares**
  against yesterday's official **660.67** = **−0.2929%**.
- **Equity $95,245.27** (close basis) · core mv **$65,245.27**, unrealized **−$4,754.72 /
  −6.7925%** from the 706.74 entry · cash **$30,000.00** · day **−$191.65 / −0.2008%** · inception
  **−4.7547%**. ⚠ Broker `equity` read 95,328.97 off `current_price` 659.58 — **not the close**; see
  carry-forward 6.
- ⚠⚠ **CORE −6.79% IS NOT A §5 EVENT, AND THE INTRADAY SWING IS THE WARNING.** The midday seat read
  **642.265 / −9.123%** and left a note that it was 0.88pp from §5.4's −10% figure; it **closed at
  −6.79%**, a **2.33pp recovery in three hours**. §5 exempts core outright and §2 says core is not
  sold on news. ⚠ **When it crosses −10%, nothing changes — there is no trailing stop on core.
  DO NOT SELL CORE.** This is the one number on which an empty-ledger run could do real damage.
- **§2 BAND RE-SOLVED FROM THE SHARE COUNT, NOT COPIED — IN BAND.** Core **68.5024%** · satellite
  **0.0000%** · cash **31.4976%** · `core_in_band: true` · `rebalance_needed: false`. **65% floor at
  VOO 562.51**, **75% ceiling at 908.67** — the band is ~15% of today's price away on the downside.
  `rebalance_delta` **$1,426.42** is the distance to the 70% *target*, **not a breach**. **NO
  REBALANCE IS DUE** — and §2 puts any rebalance at the next market-open run, which is Friday.
- **Housekeeping clean.** `week_anchor(2026-11-25)` → **2026-11-23** (imported from `common.py`, not
  hand-computed) = inherited `week_of`; **no reset due**, §6 cap stays **0 of 3**.
  `consecutive_closed_losses` **0** — nothing has ever closed, so there is no streak, the breaker is
  correctly **INACTIVE**, and **no §6 alert was owed.** **No order is in limbo:** `orders --status
  all` returns exactly one order in the account's history, the 2026-09-03 VOO core buy, `filled`.
  `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md` Notes **(none)** · `alerts.md`
  Open incidents **(none)** · `open_thesis_ids: none`.
- ⚠ **NOTHING SHOULD HAVE EXECUTED AND DID NOT.** `TRADING_ENABLED` is **true**, so no exit was
  suppressed into a dry run; there was no position to exit and this routine places no orders anyway.
  **The honest zero, not a muzzled one.**

## What this run did

Read every memory file, reconciled the ledger against the broker (**AGREE** — zero satellite blocks
vs one Alpaca row, the §2 core, §5-exempt and struck from the working list), re-derived the week
anchor and the §2 band thresholds from the share count, **wrote an insurance commit including
`journal.md` at 15:18 (`d591db1`), held 42 minutes for the bell, and restamped every figure on the
official close.** Appended the daily entry to `journal.md`, posted the ClickUp summary, and wrote
one reconciliation line plus one header-only repair to `positions.md`.

**Zero orders. Zero `trade_log.md` entries.** Nothing reached a terminal state because nothing was
submitted.

**The judgment call worth recording:** an empty-ledger close run's way of failing while looking busy
is to find *something* to do with the one position it can see. VOO printed −9.123% at midday and
−6.79% at the close, straddling §5.3's −7% figure, with both numbers sitting in the `positions`
output all run. **§5 exempts core and §2 forbids selling it; the correct action on the only
tradeable row in the account was to strike it from the working list.** That is a rule **not
applying**, not a rule **passing**.

**Not done, stated so it is not mistaken for having been done:** no high-water write (**no field
exists to write to**), no `bars` backfill (nothing to backfill), no §5.1 news check (no name, no
condition), no `sell_rule_status` write (no position, so no field), no §6 alert (breaker correctly
inactive), **and no new position** — this routine opens none by design.

## Carry forward

1. ⚠⚠⚠ **THE §4 PRICED-IN FILTER IS A VOLATILITY FILTER, NOT A PRICED-IN FILTER — AND IT NOW HAS
   THE STRONGEST EVIDENCE IT WILL EVER GET.** §4 says *"moved more than 4% over the last five
   sessions **on this news**, you are late."* `alpaca.py move` tests **absolute** magnitude.
   ⚠⚠ **`T-2026-11-25-01` (MU) PASSED ALL FOUR THESIS PARTS WITH SOURCED FIGURES — THE FIRST TIME IN
   86 DAYS** (HP's own FQ4 disclosure: memory+storage ~15–18% → **~40% of PC parts cost** in one
   fiscal year; DRAM **$39.8B of $54.2B = 73%** of Micron FQ4 revenue vs a 10% floor; FQ1 2027 in
   **three weeks**; an invalidation condition capable of failing) **and died on this filter at
   −11.63%, on a DOWN move, with a LONG thesis.** On 11-25 the gate killed **five of seven names
   checked (MU −11.63%, SNDK −21.86%, STX −4.37%, AAOI −15.01%, MOS −5.06%), all five on DOWN
   moves**, in a week the whole AI complex sold off. ⚠⚠ **NO RUN MAY ACT ON THIS — the guardrail is
   in code and §4 is explicit.** ⚠ **AND THE COUNTER-ARGUMENT IS REAL:** a name repricing 11.6%
   *against* the thesis is what §5.3's −7% stop punishes fastest, so the filter may be doing useful
   work by accident. **Both readings fit; a seat inside the loop cannot distinguish them. A
   directional variant is a calibration change and so the human's call.** ⚠ **The temptation this
   seat felt and names: reading a four-part pass killed by a drawdown, the tempting move is to argue
   the filter "obviously" does not apply to a down move — that argument is a calibration change
   dressed as a reading of the text.**
2. ⚠⚠ **THE DISPUTED FUNNEL SWEEP HAS ITS THIRD CLEAN OBSERVATION.** Demanding that a news source
   have already **named** the second-order company and segment — which **§4 does not require** — was
   omitted for a **third** consecutive session, and the kills again landed elsewhere: 11-24 on part-2
   materiality, **11-25 on a §4 hard filter and on part-1 causal denial (`-03`: the drill query
   established the source explicitly denies the path).** Three observations now point the same way.
   ⚠ **Three sessions is still not a finding.** Keep omitting it and keep watching. **No seat may
   relax a §4 test, and none has.**
3. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING.** The Capricor CRL shape ("FDA rejection → incumbent
   benefits") has appeared **four** times in three weeks and the unnamed-hyperscaler shape **seven
   plus**, each disposed with **zero** drill queries because the prior entries were read and applied.
   ⚠ **Re-use is legitimate only because those kills are STRUCTURAL** — "a rejection preserves the
   status quo" and "an unnamed counterparty cannot be sized" hold independent of drug, company and
   date. **An object whose kill depends on a figure that can change still needs re-checking.** A
   disposed-objects list the pre-market seat checks first would help, **but defining "disposed" is a
   calibration change and so the human's.**
4. ⚠⚠ **BOTH EXECUTION ROUTINES FIRE ~60 MIN EARLY. Routine 4: 15:15 for 16:15, ~15 consecutive
   times. Routine 2: 08:36 for 09:35, three times (11-23, 11-24, 11-25).** ⚠ **RECORDED, NOT
   DIAGNOSED** — `control.md` states manual "Run now" invocations are indistinguishable from
   scheduled ones in run logs, so **no run may call this a schedule fault.** Consequences differ and
   must not be folded together. **Routine 4's mitigation worked again and is now 4 of 4**: poll
   `clock` for `is_open: false` with **both** dates on the *next* session, then ~5 min, then `bars`.
   ⚠ **Cost of NOT holding, third measurement: 0.0704pp today** (partial 15:17 close 658.27 →
   official 658.735), against **0.087pp on 11-23 and 0.1552pp on 11-24.** **The spread is the
   argument for the hold — the partial error is unpredictable in size, not reliably small.**
   **Routine 2's job is placing orders**, and an early fire that exits on `is_open: false` skips a
   whole day's execution; its mitigation (poll to `is_open: true`) is **3 of 3**. ⚠⚠ **BOTH
   MITIGATIONS ARE LOAD-BEARING AND NEITHER IS IN A PROMPT.** Routine 2's prompt still says *"If the
   market is closed, log the skip, commit, and exit successfully,"* which **read literally would
   have skipped execution on all three days.** A seat that trusted the prompt over these notes would
   lose the day silently — exit 0, looking clean. **Reconciling the prompts with this is the human's
   call.** ⚠ **Read the DATES, not the boolean: FALSE has three meanings, TRUE has one.** ⚠ Routines
   1 and 3 also fire early (07:02 for 08:00; 11:41 for 12:30) but land **outside the order path**
   and **inside** the session respectively — both benign, **do not fold them into this item.**
   🛠 **AND ON FRIDAY THIS ITEM IS MOOT FOR ROUTINE 4:** the 13:00 early close means a 15:15 fire
   lands **over two hours AFTER the bell**, so the official close is already final.
5. ✅ **THE INSURANCE COMMIT WORKED AS INTENDED TODAY — FIRST FULLY CLEAN CYCLE SINCE THE TWO
   FAILURES.** `journal.md` **was** in scope (the 2026-11-13 scoping error that destroyed that day's
   entry and summary was not repeated), the commit pushed at 15:18 as `d591db1`, and **the restamp
   landed**, so no `PARTIAL` marker survives in `journal.md` — verified by grep after the write, not
   assumed. ⚠ **The 11-20 instance remains the warning:** that run died between its insurance commit
   and its restamp, leaving a 637.53 intraday "midpoint" standing for two sessions and understating
   a loss by **0.2623pp in the flattering direction**; it was corrected on 11-24 **by appended
   table, not substitution**, and **that correction is DISCHARGED — do not backfill it again.**
   ⚠ **No ClickUp summary exists for 2026-11-20 and none can be reconstructed.** The two fixes are
   still the human's call: (i) every routine greps `journal.md` for an unresolved `PARTIAL` marker in
   Step 1 and resolves it before its own work; (ii) make it a real alert key (`unresolved-partial`)
   so it surfaces in ClickUp instead of only inside a 172 KB file.
6. ⚠⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM — 17th
   DISTINCT SESSION, AND THE WIDEST IN A WHILE.** Broker `current_price` **659.58** vs official
   `bars` close **658.735** = **0.845 / 0.1283%**, read 6 minutes apart post-bell. Range across 17
   sessions now 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp any `highest_close` from official `bars` closes only, one
   adjustment basis, one call.**
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** (i) **`--adjustment all` is not
   a total-return series on this feed** — byte-identical to the unadjusted series on 259 of 260
   sessions across all four ex-dates. Reconstruct by reinvesting at the ex-date close: 2025-12-22
   $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28 $1.8226 (TTM $7.43; **none since
   09-28**). Taken literally, §1's benchmark is understated by **1.25pp**. (ii) **The paper broker
   never credits distributions** — `cash` is exactly `30000`, `accrued_fees` 0. The core sleeve is
   structurally short ~1.07%/yr against any honest total-return benchmark, widening every quarter.
   ⚠⚠ **The two defects roughly cancel, which is why ten reviews caught neither.**
8. 🛠 **CALENDAR DISCHARGED — STOP RE-ASKING IT.** The post-bell `clock` at 16:00:45 read `next_open`
   **2026-11-27T09:30** and `next_close` **2026-11-27T13:00**. **Thursday 2026-11-26 is confirmed
   closed and FRIDAY 2026-11-27's 13:00 EARLY CLOSE IS NOW BROKER-VERIFIED**, which is what this
   item carried as UNVERIFIED for several sessions. **Next session: Friday 2026-11-27, 09:30–13:00.**
   ⚠ **THIS CLONE IS STILL SHALLOW** — any run citing git history beyond ~2 weeks is citing something
   it cannot see. Do not repeat inherited history claims as measured.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` at this seat **before** this run's writes: `weekly_review.md`
   **415,188 B** · `positions.md` **381,569 B** · `research_log.md` **367,908 B** · `journal.md`
   **171,776 B** — **~1.34 MB of markdown documenting ONE trade.** This seat wrote **nothing** to
   `research_log.md`, `trade_log.md` or `weekly_review.md` — none was owed — one reconciliation line
   plus one header-only repair to `positions.md` (**net +835 B, 4 lines changed**, measured with
   `git diff --stat` after the write, not estimated before it), and one entry to `journal.md`.
   ⚠ **The growth is NOT driven by trading activity** — the account has made one trade in its history
   — **it is driven by `state.md` prose and by the research funnel on days that produce theses.**
   That is the cost of the no-memory design, not waste, but it compounds every run regardless of
   whether the system ever trades.
   ⚠ **`positions.md` is 381 KB and holds ZERO open positions.** It is excluded from monthly rollover
   on the premise that it "only holds open positions," which has been **false for all 86 absent
   dates.** **No run has standing to truncate it** — but the premise behind the exclusion is
   demonstrably wrong and **fixing it is the human's call.**
10. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND DO NOT WRITE A NUMBER FROM INTENT
    BEFORE COMPUTING IT.** 11-16 published "worst session in this account's history" — false by a
    factor of two. ⚠ **Caught in this run's own draft:** this seat wrote *"the core's unrealized loss
    **narrowed** to −6.7925%"* when against Tuesday's −6.5187% it had **widened by 0.27pp**. The
    cause is named in `journal.md` and is worth carrying: having just written the 2.33pp **intraday
    recovery**, the seat carried "recovery" into the **day-over-day** comparison, which runs off a
    different baseline — **and the slip ran in the flattering direction.** It is **left in the
    journal with its correction in place**, not silently fixed. ⚠ **Applied at this seat:** "90th
    absent seat" was counted forward from the midday seat's 89th, the absent-**date** count was
    deliberately **not** incremented, and the "first time in 86 days" claim about `T-2026-11-25-01`
    was checked against `research_log.md`'s running total before being repeated (0 accepted of ~304
    theses).
