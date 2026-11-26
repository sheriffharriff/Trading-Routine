# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠⚠ **KEEP `last_run` TO ONE LINE.** This file was compacted from 324 KB on 2026-11-13, regrew
×7.8, was compacted again on 11-20 and 11-26. **A value that needs a paragraph belongs in
`journal.md`.** See `weekly_review.md` 2026-11-20, Recurring Error 8.

```
last_run: 2026-11-26 08:36 ET 2-market-open-execution — MARKET HOLIDAY (Thanksgiving), SKIPPED per Step 1. Selftest 5/5 exit 0. `clock` 08:36:39 `is_open: false` with next_open AND next_close both 2026-11-27 = holiday, so NO poll-to-open was owed. ZERO orders. Ledger reconciled AGREES (0 satellite both sides). Core 68.51% in band, no rebalance. Breaker INACTIVE 0/3, cap 0/3. No stale-plan alert owed — Step 1 precedes the Step 2 gate. Next session Friday 2026-11-27 09:30–13:00 early close.
prior_run: 2026-11-26 07:02 ET 1-premarket-research — MARKET HOLIDAY, SKIPPED per Step 2. Selftest 5/5. No research, no theses, no plan written (`plan_date` correctly still 2026-11-25). Ledger AGREES. Core 68.51%. Breaker INACTIVE 0/3, cap 0/3.
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

## Where things stand (2026-11-26 — **MARKET HOLIDAY, EXECUTION RUN SKIPPED AT STEP 1**)

- ✅ **ZERO ORDERS PLACED. This is the only routine that opens positions, and it opened nothing,
  because §7 forbids trading when the market is closed.** Nothing was pending, nothing was
  submitted, nothing reached a non-terminal state. There is no unresolved order anywhere.
- ⚠⚠ **THE EARLY-FIRE MITIGATION WAS CORRECTLY *NOT* APPLIED, AND THAT IS THE NEW OBSERVATION.**
  Carry-forward item 4 says Routine 2 fires ~60 min early and its mitigation is to **poll `clock`
  until `is_open: true`** rather than exit on a bare `false`. **Today that mitigation would have
  polled forever.** What separates the two cases is the **DATES, not the boolean**: on an early
  pre-market fire both `next_open` and `next_close` read **today** (poll); today both read
  **2026-11-27** (skip). **A seat that applies item 4 mechanically without reading the dates hangs
  on a holiday.** That refinement belongs in the item.
- ✅ **SELFTEST PASSED 5/5, exit 0** — env (6/6), Alpaca (ACTIVE, equity 95,258.64,
  `trading_blocked: false`), Perplexity (`sonar-pro`), ClickUp, `control.md` LIVE.
- ✅ **LEDGER RECONCILED, AGREES.** `positions.md` **Open positions: (none)** vs **one** Alpaca row,
  VOO **99.046311231 sh @ 706.74** — the §2 core, **§5-exempt, struck from the working list, not
  cleared.** §5.1–§5.4 remain **ABSENT, NOT PASSING**: no satellite entry price, no `highest_close`,
  no deadline, no invalidation string exists. Step 4 (exits) had **no operand**; Steps 5–6 had no
  intents to validate. **Nothing was written to `positions.md` — the lawful minimum on a non-session
  is zero lines, as on the 07:02 run.**
- ⚠⚠ **NO `stale-plan` ALERT WAS POSTED AND THAT IS DELIBERATE — DO NOT READ THE ABSENCE AS A MISS.**
  `plan_today.md` reads `plan_date: 2026-11-25`, which **is** stale against today. But **Step 1's
  closed-market exit precedes the Step 2 gate**, and the gate exists to catch a pre-market run that
  *failed*. Today's 07:02 run did not fail — it correctly declined to plan a session that does not
  exist. **Alerting here would file an incident against a run that behaved correctly**, in the one
  channel whose value depends on every entry being real. The stale date is logged here instead.
- **Account (closed-market read):** equity **$95,258.64** · core mv **$65,258.64** · cash
  **$30,000.00** · unrealized **−$4,741.35 / −6.773%** from the 706.74 entry. **Byte-identical to
  the 07:02 read** — `change_today: 0`, `lastday_price == current_price == 658.87`. **Same stale
  closed-market mark, same session: this is NOT a second independent measurement** and item 6's
  session counter was deliberately **NOT** incremented (item 10's rule).
- ⚠⚠ **CORE −6.77% IS NOT A §5 EVENT. §5 exempts core outright and §2 says core is not sold on
  news. When it crosses −10%, nothing changes — there is no trailing stop on core. DO NOT SELL
  CORE.** This remains the one number on which an empty-ledger run could do real damage.
- **§2 band: IN BAND, re-read not copied.** Core **68.51%** · satellite **0.0%** · cash **31.49%** ·
  `core_in_band: true` · `rebalance_needed: false`. `rebalance_delta` **$1,422.40** is the distance
  to the 70% *target*, **not a breach** — **Step 7 had nothing to do even though it is exempt from
  the staleness gate**, and a rebalance could not have been placed into a closed market regardless.
- **Housekeeping clean.** `week_anchor(2026-11-26)` → **2026-11-23** (imported from `common.py`, not
  hand-computed) = inherited `week_of`; **no reset due**, §6 cap stays **0 of 3**.
  `consecutive_closed_losses` **0** — nothing has ever closed, so there is no streak and the breaker
  is correctly **INACTIVE**; no §6 alert owed. `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` ·
  `control.md` Notes **(none)** · `alerts.md` Open incidents **(none)** · `open_thesis_ids: none` ·
  `journal.md` carries **no unresolved `PARTIAL`** (the 11 hits are historical prose; the 11-20
  instance is DISCHARGED per item 5 — **do not backfill it again**).

## What this run did

Ran the selftest, read every memory file, read the clock, **identified a market holiday from the
dates and stopped at Step 1 as instructed.** Reconciled the ledger against the broker, re-derived
the week anchor from `common.py`, re-read the §2 band, confirmed no exits and no rebalance were owed,
and rewrote this file. **Zero orders, zero `trade_log.md` entries, zero `research_log.md` entries,
zero `positions.md` lines, zero alerts.**

**The judgment call worth recording:** this routine's own prompt calls itself "the only run that
opens new positions," and it fired with a plan on disk, a passing selftest, a live broker and 31%
idle cash. **The temptation on a holiday is not to over-trade, it is to treat the closed market as a
technicality and act on the one intent-shaped file in the repo** — `plan_today.md` still holds
2026-11-25's intents, and nothing in the file announces itself as spent. **Two independent rules say
no** (§7: never trade when the market is closed; Step 2: never execute a plan whose date is not
today), **and either alone is sufficient.** A holiday is not spare execution capacity.

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
   ⚠ **MU's −11.63% is now three sessions stale; Friday's seat must re-run `move`, not inherit it.**
2. ⚠⚠ **THE DISPUTED FUNNEL SWEEP HAS THREE CLEAN OBSERVATIONS.** Demanding that a news source have
   already **named** the second-order company and segment — which **§4 does not require** — was
   omitted for three consecutive sessions, and the kills landed elsewhere each time: 11-24 on part-2
   materiality, **11-25 on a §4 hard filter and on part-1 causal denial (`-03`: the drill query
   established the source explicitly denies the path).** ⚠ **Three sessions is still not a finding,
   and the two holiday skips add nothing to it — a non-session is not an observation.** Keep
   omitting it and keep watching. **No seat may relax a §4 test, and none has.**
3. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING.** The Capricor CRL shape ("FDA rejection → incumbent
   benefits") has appeared **four** times in three weeks and the unnamed-hyperscaler shape **seven
   plus**, each disposed with **zero** drill queries because the prior entries were read and applied.
   ⚠ **Re-use is legitimate only because those kills are STRUCTURAL** — "a rejection preserves the
   status quo" and "an unnamed counterparty cannot be sized" hold independent of drug, company and
   date. **An object whose kill depends on a figure that can change still needs re-checking.** A
   disposed-objects list the pre-market seat checks first would help, **but defining "disposed" is a
   calibration change and so the human's.**
4. ⚠⚠ **BOTH EXECUTION ROUTINES FIRE ~60 MIN EARLY. Routine 4: 15:15 for 16:15, ~15 consecutive
   times. Routine 2: 08:36 for 09:35, FOUR times (11-23, 11-24, 11-25, 11-26).** ⚠ **RECORDED, NOT
   DIAGNOSED** — `control.md` states manual "Run now" invocations are indistinguishable from
   scheduled ones in run logs, so **no run may call this a schedule fault.** Consequences differ and
   must not be folded together. **Routine 4's mitigation is 4 of 4**: poll `clock` for
   `is_open: false` with **both** dates on the *next* session, then ~5 min, then one `bars` call.
   ⚠ Cost of NOT holding, three measurements: **0.0704pp (11-25) · 0.087pp (11-23) · 0.1552pp
   (11-24)** — **the spread is the argument for the hold; the partial error is unpredictable in
   size, not reliably small.** **Routine 2's job is placing orders**, and an early fire that exits on
   `is_open: false` skips a whole day's execution; its mitigation (poll to `is_open: true`) is **3 of
   3 on session days.** 🛠 **NEW TODAY — THE MITIGATION IS DATE-GATED, NOT BOOLEAN-GATED.** Today's
   early fire was **harmless** (no session to lose) and **polling would have hung**: `next_open` and
   `next_close` both read **2026-11-27**. **Apply item 4's poll ONLY when both dates read today;
   when both read a later date, skip.** ⚠⚠ **BOTH MITIGATIONS ARE LOAD-BEARING AND NEITHER IS IN A
   PROMPT.** Routine 2's prompt still says *"If the market is closed, log the skip, commit, and exit
   successfully,"* which **read literally would have skipped execution on three session days** — and
   which is **exactly right today.** **Reconciling the prompts with this is the human's call.**
   ⚠ **Read the DATES, not the boolean: FALSE has three meanings — holiday, pre-market, post-bell —
   and TRUE has one.** ⚠⚠ **FRIDAY IS THIS ITEM'S WORST CASE FOR ROUTINE 2:** an 08:36 fire plus a
   **13:00** close leaves a **3.5-hour** session; both dates will read **2026-11-27 = today**, so
   **the poll applies and a bare `is_open: false` exit would lose a short day it cannot make up.**
   🛠 For Routine 4 Friday is moot: a 15:15 fire lands **two hours after** a 13:00 bell.
5. ✅ **THE INSURANCE COMMIT WORKED AS INTENDED ON 11-25 — first fully clean cycle since the two
   failures.** `journal.md` **was** in scope (the 2026-11-13 scoping error that destroyed that day's
   entry was not repeated), the commit pushed as `d591db1`, and **the restamp landed**, so no
   `PARTIAL` marker survives — verified by grep again at this seat, not assumed. ⚠ **The 11-20
   instance remains the warning:** that run died between its insurance commit and its restamp,
   leaving a 637.53 intraday "midpoint" standing for two sessions and understating a loss by
   **0.2623pp in the flattering direction**; it was corrected on 11-24 **by appended table, not
   substitution**, and **that correction is DISCHARGED — do not backfill it again.** ⚠ **No ClickUp
   summary exists for 2026-11-20 and none can be reconstructed.** Two fixes still the human's call:
   (i) every routine greps `journal.md` for an unresolved `PARTIAL` marker in Step 1 and resolves it
   before its own work; (ii) make it a real alert key (`unresolved-partial`) so it surfaces in
   ClickUp instead of only inside a 181 KB file.
6. ⚠⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM — 18
   DISTINCT SESSIONS.** Last measured 11-26 07:02: broker `current_price` **658.87** against the
   official `bars` close **658.735** = **0.135 / 0.0205%**. Range across 18 sessions
   **0.04–1.41/share**, narrowing and widening repeatedly; **not a dividend-basis artifact.**
   ⚠ **This seat re-read the same stale mark (658.87 == `lastday_price`) and did NOT count it as a
   19th session** — a second read of one closed session is not a new measurement. **Build P&L and
   stamp any `highest_close` from official `bars` closes only, one adjustment basis, one call.**
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** (i) **`--adjustment all` is not
   a total-return series on this feed** — byte-identical to the unadjusted series on 259 of 260
   sessions across all four ex-dates. Reconstruct by reinvesting at the ex-date close: 2025-12-22
   $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28 $1.8226 (TTM $7.43; **none since
   09-28**). Taken literally, §1's benchmark is understated by **1.25pp**. (ii) **The paper broker
   never credits distributions** — `cash` is exactly `30000`, `accrued_fees` 0. The core sleeve is
   structurally short ~1.07%/yr against any honest total-return benchmark, widening every quarter.
   ⚠⚠ **The two defects roughly cancel, which is why ten reviews caught neither.**
8. 🛠 **CALENDAR DISCHARGED — STOP RE-ASKING IT.** **2026-11-26 (Thanksgiving) closed — observed
   twice today, at 07:01:50 and 08:36:39, not predicted.** `clock` reads `next_open`
   **2026-11-27T09:30** and `next_close` **2026-11-27T13:00**: **FRIDAY 2026-11-27's 13:00 EARLY
   CLOSE IS NOW BROKER-VERIFIED THREE TIMES** (11-25 post-bell, 11-26 ×2). **Next session: Friday
   2026-11-27, 09:30–13:00.** ⚠ **THIS CLONE IS SHALLOW** — any run citing git history beyond ~2
   weeks is citing something it cannot see. Do not repeat inherited history claims as measured.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` at this seat **before** this run's writes: `weekly_review.md`
   **415,188 B** · `positions.md` **383,983 B** · `research_log.md` **367,908 B** · `journal.md`
   **180,979 B** · `state.md` **17,562 B** · `plan_today.md` **12,017 B** — **~1.38 MB of markdown
   documenting ONE trade.** ⚠ **The growth is NOT driven by trading activity** — one trade in this
   account's history — **it is driven by `state.md` prose and by the research funnel on days that
   produce theses.** That is the cost of the no-memory design, not waste, but it compounds every run
   regardless of whether the system ever trades. ⚠ **`positions.md` is 384 KB and holds ZERO open
   positions.** It is excluded from monthly rollover on the premise that it "only holds open
   positions," **false for all 87 absent dates.** **No run has standing to truncate it** — but the
   premise behind the exclusion is demonstrably wrong and **fixing it is the human's call.**
   ✅ **Both of today's seats wrote ZERO bytes to all four append-only files** (`research_log`,
   `trade_log`, `positions`, `journal`), and each rewrote `state.md` without growing it — checked
   against `wc -c` and `git status`, not asserted from intent.
10. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND DO NOT WRITE A NUMBER FROM INTENT
    BEFORE COMPUTING IT.** 11-16 published "worst session in this account's history" — false by a
    factor of two. 11-25 caught itself writing that the core's loss "**narrowed** to −6.7925%" when
    against Tuesday's −6.5187% it had **widened by 0.27pp** — the slip ran in the flattering
    direction and is **left in `journal.md` with its correction in place**, not silently fixed.
    ⚠ **Applied at this seat:** item 6's session counter was held at 18 rather than incremented on a
    re-read of the same stale mark; the week anchor was imported from `common.py`; the equity figures
    were compared byte-for-byte against the 07:02 read before being called identical; and the
    absent-seat/absent-date counters were again **deliberately NOT incremented** — **today is not an
    absent trading seat, it is a non-session**, and folding a holiday into the §5-absence tally would
    overstate how many chances the §5 machinery has had to run.
