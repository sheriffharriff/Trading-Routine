# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** This file was compacted from 324 KB on 2026-11-13, regrew
×7.8 and was compacted again on 11-20; it had regrown to 18,170 B by 11-26. **A value that needs
a paragraph belongs in `journal.md`.** See `weekly_review.md` 2026-11-20, Recurring Error 8.

```
last_run: 2026-11-26 07:02 ET 1-premarket-research — MARKET HOLIDAY (Thanksgiving), SKIPPED per Step 2. Selftest 5/5 exit 0. `clock` 07:01:50 `is_open: false` with next_open AND next_close both 2026-11-27 = holiday, not pre-market. No research, no theses, no plan written. Ledger reconciled AGREES (0 satellite both sides). Core 68.51% in band. Breaker INACTIVE 0/3, cap 0/3. Next session Friday 2026-11-27 09:30–13:00 early close.
prior_run: 2026-11-25 16:06 ET 4-market-close-journal — restamped on the official close (VOO 658.735), insurance commit d591db1 discharged. Equity 95,245.27, day −0.2008%, inception −4.7547%. Zero satellite positions; Step 2 had no operand (no `highest_close` field exists at all — ABSENT ≠ STALE). Core 68.5024% in band. Breaker INACTIVE 0/3, cap 0/3.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.51
satellite_pct: 0.0
cash_pct: 31.49
open_thesis_ids: none
```

---

## Where things stand (2026-11-26 — **MARKET HOLIDAY, RUN SKIPPED AT STEP 2**)

- 🛠 **THIS IS A HOLIDAY SKIP, NOT A QUIET DAY, AND THE DIFFERENCE MATTERS TO `research_log.md`.**
  Today's prompt warns that a day with no theses is indistinguishable in the log from a day where
  nothing met the bar. **There are no theses today because no research was run** — Step 2 ends the
  run before Step 5 — **not because candidates were considered and rejected.** `research_log.md` is
  deliberately untouched: a holiday entry there would be noise in the one file whose value depends
  on every entry being a real judgment.
- ✅ **THE HOLIDAY SIGNATURE WAS READ FROM THE DATES, NOT THE BOOLEAN.** `clock` at **07:01:50**
  returned `is_open: false` with `next_open` **2026-11-27T09:30** and `next_close`
  **2026-11-27T13:00**. On a normal 07:00 pre-market run both dates read **today**; both reading
  **tomorrow** is what separates a holiday from a pre-market hour. Carry-forward item 8 had already
  broker-verified this on 11-25 and it is now confirmed twice.
- ✅ **SELFTEST PASSED 5/5, exit 0** — env (6/6), Alpaca (ACTIVE, equity 95,258.64,
  `trading_blocked: false`), Perplexity (`sonar-pro`), ClickUp, `control.md` LIVE. ⚠ **Stated
  explicitly because of the asymmetry the prompt names: Perplexity was REACHABLE and was simply
  never queried.** A later seat must not read today's zero theses as a silent API failure.
- ✅ **LEDGER RECONCILED, AGREES.** `positions.md` **Open positions: (none)** vs **one** Alpaca row,
  VOO **99.046311231 sh @ 706.74** — the §2 core, **§5-exempt, struck from the working list, not
  cleared.** §5.1–§5.4 remain **ABSENT, NOT PASSING**: no satellite entry price, no `highest_close`,
  no deadline, no invalidation string exists. No §5.1 Perplexity call was owed (no name, no
  condition); no `bars` backfill was owed (no mark to backfill).
- 🛠 **NOTHING WAS WRITTEN TO `positions.md` TODAY, DELIBERATELY — DO NOT READ THE GAP AS A MISSED
  RECONCILIATION.** The reconciliation happened and is recorded here instead. `state.md` is
  rewritten each run so a note here costs nothing twice; an append to a **383,983 B** ledger
  describing an empty position list compounds forever. On a holiday the lawful minimum write to that
  file is **zero lines**, and this is the first seat to take it.
- **Account (closed-market read):** equity **$95,258.64** · core mv **$65,258.64** · cash
  **$30,000.00** · unrealized **−$4,741.35 / −6.773%** from the 706.74 entry. `change_today: 0` and
  `lastday_price == current_price == 658.87` — the closed-market signature, **not a flat session.**
- ⚠⚠ **CORE −6.77% IS NOT A §5 EVENT. §5 exempts core outright and §2 says core is not sold on
  news. When it crosses −10%, nothing changes — there is no trailing stop on core. DO NOT SELL
  CORE.** This remains the one number on which an empty-ledger run could do real damage.
- **§2 band: IN BAND, re-read not copied.** Core **68.51%** · satellite **0.0%** · cash **31.49%** ·
  `core_in_band: true` · `rebalance_needed: false`. `rebalance_delta` **$1,422.40** is the distance
  to the 70% *target*, **not a breach**. **NO REBALANCE QUEUED** — and §2 puts any rebalance at the
  next market-open run, which is Friday.
- **Housekeeping clean.** `week_anchor(2026-11-26)` → **2026-11-23** (imported from `common.py`, not
  hand-computed) = inherited `week_of`; **no reset due**, §6 cap stays **0 of 3**.
  `consecutive_closed_losses` **0** — nothing has ever closed, so there is no streak and the breaker
  is correctly **INACTIVE**; no §6 alert owed. `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` ·
  `control.md` Notes **(none)** · `alerts.md` Open incidents **(none)** · `open_thesis_ids: none`.
- ⚠ **`plan_today.md` STILL READS `plan_date: 2026-11-25` AND THAT IS CORRECT.** No plan was written
  for a day with no session. **If Friday's pre-market run fails, the stale date will correctly
  refuse execution** — the gate working as designed, not a fault to repair.

## What this run did

Ran the selftest, read every memory file, read the clock, **identified a market holiday and stopped
at Step 2 as instructed.** Reconciled the ledger against the broker, re-derived the week anchor from
`common.py`, re-read the §2 band, and rewrote this file. **Zero orders, zero theses, zero
`trade_log.md` entries, zero `research_log.md` entries, zero `positions.md` lines, no plan.**

**The judgment call worth recording:** the prompt's Step 5 pressure ("a run that finds nothing is a
successful run") is aimed at a *research* run. On a holiday the temptation is the inverse and
quieter — to run the Perplexity sweep anyway because the API is up and the run otherwise feels
empty, producing theses for a session that cannot act on them and that Friday's seat would then
inherit as pre-chewed candidates it did not screen itself. **Step 2 says stop, so this seat
stopped.** A holiday is not a failure and it is also not spare capacity.

## Carry forward

1. ⚠⚠⚠ **THE §4 PRICED-IN FILTER IS A VOLATILITY FILTER, NOT A PRICED-IN FILTER.** §4 says *"moved
   more than 4% over the last five sessions **on this news**, you are late."* `alpaca.py move` tests
   **absolute** magnitude. ⚠⚠ **`T-2026-11-25-01` (MU) PASSED ALL FOUR THESIS PARTS WITH SOURCED
   FIGURES — the first time in 86 days** (HP's own FQ4 disclosure: memory+storage ~15–18% → **~40%
   of PC parts cost**; DRAM **$39.8B of $54.2B = 73%** of Micron FQ4 revenue vs a 10% floor; FQ1
   2027 within weeks; a falsifiable invalidation condition) **and died on this filter at −11.63%, on
   a DOWN move, with a LONG thesis.** On 11-25 the gate killed **five of seven names (MU −11.63%,
   SNDK −21.86%, STX −4.37%, AAOI −15.01%, MOS −5.06%), all five on DOWN moves.** ⚠⚠ **NO RUN MAY
   ACT ON THIS — the guardrail is in code and §4 is explicit.** ⚠ **The counter-argument is real:** a
   name repricing 11.6% *against* the thesis is what §5.3's −7% stop punishes fastest, so the filter
   may be doing useful work by accident. **Both readings fit; a seat inside the loop cannot
   distinguish them. A directional variant is a calibration change and so the human's call.**
   ⚠ **The temptation to name: reading a four-part pass killed by a drawdown, the tempting move is to
   argue the filter "obviously" does not apply to a down move — that is a calibration change dressed
   as a reading of the text.** ⚠ **MU's −11.63% is now two sessions stale; Friday's seat must re-run
   `move` rather than inherit it.**
2. ⚠⚠ **THE DISPUTED FUNNEL SWEEP HAS THREE CLEAN OBSERVATIONS.** Demanding that a news source have
   already **named** the second-order company and segment — which **§4 does not require** — was
   omitted for three consecutive sessions, and the kills landed elsewhere each time: 11-24 on part-2
   materiality, **11-25 on a §4 hard filter and on part-1 causal denial (`-03`: the drill query
   established the source explicitly denies the path).** ⚠ **Three sessions is still not a finding.**
   Keep omitting it and keep watching. **No seat may relax a §4 test, and none has.**
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
   must not be folded together. **Routine 4's mitigation is 4 of 4**: poll `clock` for
   `is_open: false` with **both** dates on the *next* session, then ~5 min, then one `bars` call.
   ⚠ Cost of NOT holding, three measurements: **0.0704pp (11-25) · 0.087pp (11-23) · 0.1552pp
   (11-24)** — **the spread is the argument for the hold; the partial error is unpredictable in
   size, not reliably small.** **Routine 2's job is placing orders**, and an early fire that exits on
   `is_open: false` skips a whole day's execution; its mitigation (poll to `is_open: true`) is **3 of
   3**. ⚠⚠ **BOTH MITIGATIONS ARE LOAD-BEARING AND NEITHER IS IN A PROMPT.** Routine 2's prompt still
   says *"If the market is closed, log the skip, commit, and exit successfully,"* which **read
   literally would have skipped execution on all three days.** **Reconciling the prompts with this is
   the human's call.** ⚠ **Read the DATES, not the boolean: FALSE has three meanings — holiday,
   pre-market, post-bell — and TRUE has one.** **Today's holiday read is the third meaning in
   practice and it worked.** ⚠ Routines 1 and 3 also fire early (07:02 for 08:00; 11:41 for 12:30)
   but land **outside the order path** and **inside** the session respectively — both benign, **do
   not fold them into this item.** 🛠 **ON FRIDAY THIS ITEM IS MOOT FOR ROUTINE 4:** the 13:00 early
   close means a 15:15 fire lands **over two hours AFTER the bell**, so the close is already final.
   ⚠⚠ **BUT FRIDAY IS THE ITEM'S WORST CASE FOR ROUTINE 2:** a 08:36 fire plus a **13:00** close
   leaves a **3.5-hour** session, and an early seat that exits on `is_open: false` loses a short day
   it cannot make up.
5. ✅ **THE INSURANCE COMMIT WORKED AS INTENDED ON 11-25 — first fully clean cycle since the two
   failures.** `journal.md` **was** in scope (the 2026-11-13 scoping error that destroyed that day's
   entry was not repeated), the commit pushed as `d591db1`, and **the restamp landed**, so no
   `PARTIAL` marker survives — verified by grep after the write, not assumed. ⚠ **The 11-20 instance
   remains the warning:** that run died between its insurance commit and its restamp, leaving a
   637.53 intraday "midpoint" standing for two sessions and understating a loss by **0.2623pp in the
   flattering direction**; it was corrected on 11-24 **by appended table, not substitution**, and
   **that correction is DISCHARGED — do not backfill it again.** ⚠ **No ClickUp summary exists for
   2026-11-20 and none can be reconstructed.** Two fixes still the human's call: (i) every routine
   greps `journal.md` for an unresolved `PARTIAL` marker in Step 1 and resolves it before its own
   work; (ii) make it a real alert key (`unresolved-partial`) so it surfaces in ClickUp instead of
   only inside a 181 KB file.
6. ⚠⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM — 18th
   DISTINCT SESSION.** Today, with the market closed, broker `current_price` **658.87** against
   yesterday's official `bars` close **658.735** = **0.135 / 0.0205%**. Range across 18 sessions
   **0.04–1.41/share**, narrowing and widening repeatedly; **not a dividend-basis artifact.** ⚠ Note
   the shape today: `current_price` **equals** `lastday_price`, so the broker is carrying a stale
   mark that still does not match the official close. **Build P&L and stamp any `highest_close` from
   official `bars` closes only, one adjustment basis, one call.**
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** (i) **`--adjustment all` is not
   a total-return series on this feed** — byte-identical to the unadjusted series on 259 of 260
   sessions across all four ex-dates. Reconstruct by reinvesting at the ex-date close: 2025-12-22
   $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28 $1.8226 (TTM $7.43; **none since
   09-28**). Taken literally, §1's benchmark is understated by **1.25pp**. (ii) **The paper broker
   never credits distributions** — `cash` is exactly `30000`, `accrued_fees` 0. The core sleeve is
   structurally short ~1.07%/yr against any honest total-return benchmark, widening every quarter.
   ⚠⚠ **The two defects roughly cancel, which is why ten reviews caught neither.**
8. 🛠 **CALENDAR DISCHARGED — STOP RE-ASKING IT.** **2026-11-26 (Thanksgiving) is confirmed closed —
   observed, not predicted, by this run.** `clock` reads `next_open` **2026-11-27T09:30** and
   `next_close` **2026-11-27T13:00**: **FRIDAY 2026-11-27's 13:00 EARLY CLOSE IS BROKER-VERIFIED
   TWICE** (11-25 post-bell and again today). **Next session: Friday 2026-11-27, 09:30–13:00.**
   ⚠ **THIS CLONE IS SHALLOW** — any run citing git history beyond ~2 weeks is citing something it
   cannot see. Do not repeat inherited history claims as measured.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` at this seat **before** this run's writes: `weekly_review.md`
   **415,188 B** · `positions.md` **383,983 B** · `research_log.md` **367,908 B** · `journal.md`
   **180,979 B** · `state.md` **18,170 B** · `plan_today.md` **12,017 B** — **~1.38 MB of markdown
   documenting ONE trade.** ⚠ **The growth is NOT driven by trading activity** — one trade in this
   account's history — **it is driven by `state.md` prose and by the research funnel on days that
   produce theses.** That is the cost of the no-memory design, not waste, but it compounds every run
   regardless of whether the system ever trades. ⚠ **`positions.md` is 384 KB and holds ZERO open
   positions.** It is excluded from monthly rollover on the premise that it "only holds open
   positions," **false for all 87 absent dates.** **No run has standing to truncate it** — but the
   premise behind the exclusion is demonstrably wrong and **fixing it is the human's call.**
   ✅ **This seat is the first to write ZERO bytes to all four append-only files** (`research_log`,
   `trade_log`, `positions`, `journal` — a holiday run owes `journal.md` nothing, that is the close
   routine's file) **and it compacted `state.md` instead of growing it.** A holiday is the cheapest
   possible run and this one was taken that way on purpose.
10. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND DO NOT WRITE A NUMBER FROM INTENT
    BEFORE COMPUTING IT.** 11-16 published "worst session in this account's history" — false by a
    factor of two. 11-25 caught itself writing that the core's loss "**narrowed** to −6.7925%" when
    against Tuesday's −6.5187% it had **widened by 0.27pp** — the slip ran in the flattering
    direction and is **left in `journal.md` with its correction in place**, not silently fixed.
    ⚠ **Applied at this seat:** the "first seat to write zero bytes to all four append-only files"
    claim in item 9 was checked against this run's own `git status` before being written, not
    asserted from intent; the week anchor was imported from `common.py` rather than computed by
    hand; and the absent-seat/absent-date counters were **deliberately NOT incremented** — 87 absent
    dates, but **today is not an absent trading seat, it is a non-session**, and folding a holiday
    into the §5-absence tally would overstate how many chances the §5 machinery has had to run.
