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
last_run: 2026-11-25 09:35 ET 2-market-open-execution — selftest 5/5 exit 0. FIRED 08:36 FOR 09:35; POLLED clock 59 min TO is_open:true AND EXECUTED AT 09:35 — did NOT exit on the pre-market false. Plan 2026-11-25 DATED TODAY, staleness gate PASSED, ZERO intents. 0 buys, 0 sells, no §2 rebalance. Core 67.99% in band LIVE. Breaker INACTIVE 0/3, cap 0/3. BROKER CONFIRMED next_open 2026-11-27 — Thanksgiving VERIFIED at last.
prior_run: 2026-11-25 07:02 ET 1-premarket-research — selftest 5/5 exit 0. Pre-market, full session. Ledger AGREES (0 satellite). Core 68.15% in band. Breaker INACTIVE 0/3, cap 0/3. 5 theses, 0 accepted; plan 2026-11-25 has ZERO intents. T-2026-11-25-01 (MU) passed ALL FOUR §4 parts and died on the priced-in filter at −11.63% — FIRST TIME IN 86 DAYS. Calibration question escalated, nothing changed.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 67.99
satellite_pct: 0.0
cash_pct: 32.02
open_thesis_ids: none
```

---

## Where things stand (2026-11-25, **MARKET OPEN — `is_open: true`, read at 09:35:52 ET**)

- **Equity $93,707.58** · core mv **$63,707.58**, unrealized **−$6,292.41 / −8.989%** from the
  706.74 entry, cash **$30,000.00**. ⚠ Read off `current_price` **643.21** at 09:35:52 — a **LIVE
  INTRADAY PRINT, not a close** (−2.649% on yesterday's official 660.67). It will move all
  session; the close run owns the closing figure. **No `bars` call was spent; none was owed** —
  this routine needs `voo_close_at_entry` only when it opens a position, and it opened none.
- ⚠⚠ **CORE −8.989% IS NOT A §5 EVENT, AND IT IS NOW WITHIN 1.01pp OF §5.4's −10% FIGURE.** §5
  exempts core outright and §2 says core is not sold on news. **Restated because the magnitude is
  deteriorating** — −8.307% pre-market, **−8.989% at the open** — and a fresh-clone seat reading
  only the P&L line is exactly the failure this warning exists for. ⚠ **When it crosses −10%,
  nothing changes: there is no §5.4 trailing stop on core, and the number will look like a
  trigger.** **Do not sell core.**
- **§2 BAND RE-READ OFF LIVE PRICES, AS THE PLAN REQUIRED — IN BAND, NO REBALANCE PLACED.** Core
  **67.99%** · satellite **0.0000%** · cash **32.02%** · `core_in_band: true` ·
  `rebalance_needed: false`. Thresholds **re-solved at this seat from the share count, not
  copied**: **65% floor at VOO 562.51** (a further **−12.55%** from 643.21), **75% ceiling at
  908.67**. `rebalance_delta` **$1,882.53** is the distance to the 70% *target*, **not a breach**,
  and §2 rebalances on the band. ⚠ **Step 7 was executed and returned "no action" — that is a
  verdict, not a skip.** ⚠ Core drifted 68.15% → 67.99% between 07:02 and 09:35 purely because VOO
  fell; buying to target here would be **adding to the core on weakness**, which §2 does not ask
  for.
- **LEDGER RECONCILED AGAINST THE BROKER, AGREES.** `grep -ci 'status: *open'` → **0**;
  `positions` returns one row, VOO 99.046311231 sh @ 706.74, the §2 core, §5-exempt and
  deliberately untracked in `positions.md`. **No disagreement, so no reconciliation was owed and
  nothing was traded on top of a suspect ledger.**
- ⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING.** Step 4 had **NO OPERAND** — no entry price, no
  `highest_close`, no deadline, no invalidation string exists anywhere in `positions.md`, so no
  SELL intent could be re-confirmed and none was. **This is not "the sell rules were checked and
  cleared."** §5.1–§5.4 remain **unexecuted code**; the first satellite position will be their
  first live test. **88th absent seat, 86th absent date.**
- **Housekeeping clean.** `week_anchor(2026-11-25)` → **2026-11-23** (imported from `common.py`,
  not hand-computed) = inherited `week_of`; **no reset due**, §6 cap stays **0 of 3**.
  `consecutive_closed_losses` **0** — nothing has ever closed, so there is no streak, the breaker
  is correctly **INACTIVE**, and **no §6 alert was owed.** `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `control.md` Notes **(none)** · `alerts.md` **no open and no SYSTEMIC
  incidents** · `open_thesis_ids: none`.
- **STALENESS GATE PASSED, AND FOUND AN EMPTY INSTRUCTION SET.** `plan_date: 2026-11-25` =
  today's ET date, so **no stale-plan alert was owed and none was posted.** The plan carried
  **0 BUY, 0 SELL, 0 REBALANCE** intents. **NEW POSITIONS WERE PERMITTED THROUGHOUT** — breaker
  inactive, cap 0/3, satellite 0% deployed, $30,000 cash, no `control.md` note. **Nothing
  structural blocked a buy today. This is the unhalted zero.**
- ⚠⚠ **ZERO `move` CALLS WERE SPENT, AND THAT IS CORRECT, NOT AN OMISSION.** Step 5's
  re-validation runs **per BUY intent**. With zero intents there was nothing to re-validate.
  ⚠ **§4 re-validation only ever REMOVES intents — it does not authorise adding one**, so no
  amount of fresh price data could have produced a trade here.
- ⚠⚠⚠ **THE INHERITED HOLIDAY CALENDAR IS NOW HALF VERIFIED — FIRST BROKER CONFIRMATION.** With
  `is_open: true`, `next_open` points at the **next session**, and it reads
  **`2026-11-27T09:30:00-05:00`**. **Thursday 2026-11-26 is therefore confirmed closed by the
  broker, not merely inherited.** ⚠ **Friday 2026-11-27's early close is STILL UNVERIFIED** —
  `next_close` today reads 16:00 for *today*, which says nothing about Friday. A seat on Friday
  should read `next_close` then; **13:00 confirms the early close, 16:00 refutes it.**
- ⚠ **This seat fired ~08:36 for a 09:35 slot (~59 min early) — THE THIRD TIME for routine 2.**
  See carry-forward item 3. **The mitigation was applied and worked:** polled `clock` for 59
  minutes to `is_open: true`, then executed at **09:35**, the intended slot. **Nothing was
  skipped and no order was placed into the opening auction.**

## What this run did

Read every memory file, reconciled the ledger against the broker, re-derived the week anchor and
the §2 band thresholds from the share count rather than copying them, **polled through to the
open rather than exiting on a pre-market `is_open: false`**, re-read the §2 band off live prices,
and placed **no orders** — because the plan correctly dated today carried no intents and Step 3's
bootstrap had already run on 2026-09-03.

**Zero orders. Zero `trade_log.md` entries.** Nothing reached a terminal state because nothing
was submitted, and §7 forbids logging an order that was never placed.

**The one judgment call worth recording:** at 08:36 this seat held a passing selftest, a valid
plan, an open §2 band question and a market that was **closed**. The cheap reading of
`is_open: false` is "market closed → log the skip, commit, exit successfully" — Step 1 of the
routine authorises exactly that, and it would have been a clean-looking run. **It would also have
thrown away the day's execution window on a boolean that was false for the most boring of its
three possible reasons.** The plan's own instruction 3 and carry-forward item 3 both said to poll;
both were written by seats that had already made this mistake once. **The 59-minute wait produced
no trade, and that is not evidence it was wasted** — the band could have broken, the ledger could
have diverged, and neither was knowable at 08:36.

**What this seat did NOT do, stated so it is not mistaken for having been done:** it did not
revive `T-2026-11-25-01` through `-04`. `-01` (MU) passed all four §4 thesis parts yesterday and
died on the priced-in filter at **−11.63%** — **7.6pp past the threshold, a gap no overnight move
could close** — and the plan is explicit that those four are **rejected, not deferred.** An empty
plan is not licence to improvise, and a buy reasoned into existence at 09:35 is the precise thing
the 08:00/09:35 handoff exists to prevent. **No new idea was generated at this seat.**

## Carry forward


1. ⚠⚠⚠ **THE FUNNEL GATE QUESTION HAS ITS SECOND CLEAN OBSERVATION, AND A NEW SECOND HALF.**
   **(a) The disputed sweep** — demanding that a **news source have already named** the
   second-order company and segment, which **§4 does not require** — was **omitted for the second
   consecutive session**, and for the second consecutive session the kills landed elsewhere: 11-24
   died on part-2 materiality, **11-25 died on a §4 hard filter.** The diagnostic the 11-24 seat
   proposed (watch whether kill reasons migrate off part 1) now has **two observations pointing
   the same way.** ⚠ **Two sessions is still not a finding.** Keep omitting it and keep watching.
   **No seat may relax a §4 test, and none has.**
   **(b) ⚠⚠ NEW, AND THE SHARPER HALF: `alpaca.py move` IS A VOLATILITY FILTER, NOT A PRICED-IN
   FILTER.** §4 says *"moved more than 4% over the last five sessions **on this news**, you are
   late."* The script tests **absolute** magnitude. `T-2026-11-25-01` (MU) **fell 11.63%** and the
   thesis was **long** — a drawdown *against* the thesis, not the news being priced in. Today the
   filter killed **five of seven names checked (MU −11.63%, SNDK −21.86%, STX −4.37%, AAOI
   −15.01%, MOS −5.06%), all five on DOWN moves**, in a week the whole AI complex sold off. In a
   broad drawdown this gate disqualifies an entire sector regardless of which way the news cut.
   ⚠⚠ **NO RUN MAY ACT ON THIS. The guardrail is in code and §4 is explicit.** ⚠ **And the
   counter-argument is real and is recorded against this seat's own finding:** a name down 11.6%
   in five sessions is one the market is repricing *against* the thesis, and a long entry there is
   what the §5.3 −7% hard stop punishes fastest — **the filter may be doing useful work by
   accident.** Both readings fit the evidence; a seat inside the loop cannot distinguish them.
   **A directional variant of the test is a calibration change and so the human's call.**
2. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING — NOW WITH A FOURTH AND A SEVENTH INSTANCE.** The
   Capricor CRL ("FDA rejection → incumbent benefits") appeared for the **fourth** time in three
   weeks and was disposed with **zero** drill queries because the prior entries were read and
   applied; the unnamed-hyperscaler shape appeared a **seventh-plus** time (AAOI's $2.2B/4-yr
   800G agreement with "a Tier-1 hyperscale customer"). ⚠ **Re-use is legitimate only because
   those kills are STRUCTURAL** — "a rejection preserves the status quo" and "an unnamed
   counterparty cannot be sized" hold independent of drug, company and date. **An object whose
   kill depends on a figure that can change still needs re-checking**, and `-01`/`-03` were
   re-checked from scratch today for exactly that reason. A disposed-objects list the pre-market
   seat checks first would help, **but defining "disposed" is a calibration change and so is the
   human's.**
3. ⚠⚠ **BOTH EXECUTION ROUTINES FIRE ~60 MIN EARLY. Routine 4: 15:15 for 16:15, ~14 consecutive
   times. Routine 2: 08:36 for 09:35, THREE TIMES (11-23, 11-24, 11-25).** ⚠ **RECORDED, NOT DIAGNOSED** —
   `control.md` states manual "Run now" invocations are indistinguishable from scheduled ones in
   run logs, so **no run may call this a schedule fault.** Consequences differ and must not be
   folded together: routine 4's job is recording *closing* prices (11-24 measured the cost of not
   holding at **0.1552pp**, vs 11-23's 0.087pp — **two readings say the partial error is
   unpredictable in size, not reliably small**; the case for the hold is the variance, not any
   day's payoff); **routine 2's job is placing orders, and an early fire that exits on
   `is_open: false` skips a whole day's execution.** Mitigation is the same shape and has worked
   every time used — **3 of 3 for routine 2**: **poll `clock` to the right signature** — routine 4
   waits for `is_open: false` with **both** dates on the *next* session, then ~5 min, then `bars`;
   routine 2 waits for **`is_open: true`** (28 min on 11-24, **59 min on 11-25, executing at the
   intended 09:35**). ⚠⚠ **THE MITIGATION IS NOW LOAD-BEARING AND IS STILL NOT IN THE PROMPT.**
   It survives only as this item plus a line in `plan_today.md`, both agent-written; routine 2's
   prompt still says "If the market is closed, log the skip, commit, and exit successfully," which
   **read literally would have skipped execution on all three days.** ⚠ **A seat that trusted the
   prompt over this note would lose the day silently** — the run would exit 0 and look clean.
   **Reconciling the prompt with this is the human's call.** ⚠ **Read the DATES, not the boolean: FALSE has three
   meanings, TRUE has one.** ⚠ Routines 1 and 3 also fire early (**07:02 for 08:00 today**; 11:41
   for 12:30) but land **outside the order path** and **inside** the session respectively, so both
   are benign — **do not fold them into this item.**
4. ⚠⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` — AND SOMETHING MUST CHECK THAT THE
   WINDOW EVER CLOSED. THIS HAS FAILED TWICE.** The scoping error cost 2026-11-13, whose journal
   entry and ClickUp summary do not exist and never will. The second instance: the 2026-11-20
   close run died between its insurance commit (`baf87a2`) and its restamp, leaving its entry on a
   637.53 intraday "midpoint" for two sessions — equity $93,144.99 / day −2.1354% recorded against
   an official $92,895.40 / **−2.3977%** / inception −7.1046%, **a loss understated by 0.2623pp,
   i.e. erring in the flattering direction.** Found and corrected on 11-24 **by appended table,
   not substitution**, so the evidence that the restamp failed survives. ⚠ **No ClickUp summary
   exists for 2026-11-20 and none can be reconstructed.** ⚠⚠ **Neither the 11-23 close seat nor
   the Friday review caught it — "a later run will notice" is not a working safety net.** Two
   fixes, both the human's call: (i) every routine greps `journal.md` for an unresolved `PARTIAL`
   marker in Step 1 and resolves it before its own work; (ii) make it a real alert key
   (`unresolved-partial`) so it surfaces in ClickUp instead of only inside a 172 KB file.
   ⚠ **This seat did NOT grep for `PARTIAL`** — fix (i) is not in routine 1's prompt and this seat
   does not get to add steps to itself. **Recorded as not done, not as unnecessary.**
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two.
   ⚠ **Applied today:** this seat wrote "first time in 86 days a candidate passed all four parts."
   That is checkable — **0 accepted of ~304 theses across the account's whole history** — and it
   was checked against `research_log.md`'s own running total before it was written, **not after.**
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 16+
   distinct sessions, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.** ⚠ Today: `lastday_price` **660.71** vs official **660.67** =
   **0.04 / 0.0061%**, tying the narrowest recorded value — but this is a **different endpoint
   pair** from the post-bell readings, so it is **recorded as an observation, not added to the
   tally.** **No `bars` call was spent; none was owed, and one must not be spent merely to extend
   a count.**
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** (i) **`--adjustment all` is
   not a total-return series on this feed** — byte-identical to the unadjusted series on 259 of
   260 sessions across all four ex-dates. Reconstruct by reinvesting at the ex-date close:
   2025-12-22 $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28 $1.8226 (TTM $7.43;
   **none since 09-28**). Taken literally, §1's benchmark is understated by **1.25pp**.
   (ii) **The paper broker never credits distributions** — `cash` is exactly `30000`, not
   $30,180.52; `accrued_fees` 0. The core sleeve is structurally short ~1.07%/yr against any
   honest total-return benchmark, widening every quarter. ⚠⚠ **The two defects roughly cancel,
   which is why ten reviews caught neither.**
8. ⚠ **THIS CLONE IS SHALLOW.** Any run citing git history beyond ~2 weeks is citing something it
   cannot see. Do not repeat inherited history claims as measured. ⚠ **Applied today:** the
   endpoint-disagreement instance count remains **inherited and flagged as such.** 🛠 **THE Thu/Fri
   CALENDAR IS NO LONGER WHOLLY INHERITED:** with `is_open: true` at 09:35, `next_open` read
   **2026-11-27T09:30**, which **confirms Thursday 2026-11-26 closed against the broker** for the
   first time. ⚠ **Friday's early close is still unverified** — read `next_close` on Friday itself;
   **13:00 confirms it, 16:00 refutes it.** **The verification cost nothing: it was a field in a
   `clock` call the run already owed.**
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` at this seat: `weekly_review.md` **415,188 B** ·
   `positions.md` **380,158 B** · `research_log.md` **367,908 B** · `journal.md` **171,776 B** —
   **~1.36 MB of markdown documenting ZERO satellite trades**, up from ~1.31 MB one session ago.
   ⚠⚠ **THIS SEAT IS THE CHEAP CASE AND IT PROVES THE POINT THE EXPENSIVE SEATS CANNOT.** It wrote
   **nothing** to `research_log.md`, `positions.md`, `trade_log.md` or `journal.md` — **no thesis
   was written, so none was owed; no position exists, so no block was owed; no order was placed,
   so no entry was owed.** `state.md` went **17,653 B → ~20,000 B (+~13%)**, and **that is the
   entire footprint of this run.** ⚠ **The growth is therefore NOT driven by trading activity — the
   account has made one trade in its history — it is driven by `state.md` prose and by the research
   funnel on days that produce theses.** A run with literally nothing to execute still costs ~2.3 KB
   of permanent state, **because the carry-forward is the only channel through which a fresh clone
   learns anything.** That is the cost of the no-memory design, not waste, but it compounds at
   ~1 KB/run regardless of whether the system ever trades.
   ⚠ **`positions.md` is 380 KB and holds ZERO open positions.** It is excluded from monthly
   rollover on the premise that it "only holds open positions," which has been **false for all 86
   absent dates.** **No run has standing to truncate it** — but the premise behind the exclusion is
   now demonstrably wrong and **fixing it is the human's call.**
   ⚠ **Measured AFTER the write, not estimated from intent** — prior seats twice stated a size
   claim before measuring it and were wrong both times. Only the residual from writing this
   sentence is inexact by construction.
