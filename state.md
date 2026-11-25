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
last_run: 2026-11-25 11:41 ET 3-midday-management — selftest 5/5 exit 0. Market OPEN. ZERO satellite positions, so Steps 2-5 had NO OPERAND: no high-water repair, no §5.1 Perplexity call, no exits, no `sell_rule_status` to update. 0 sells. Core 67.95% in band. Breaker INACTIVE 0/3, cap 0/3. Thursday 2026-11-26 closed CONFIRMED again (next_open 2026-11-27); Friday's early close still UNVERIFIED.
prior_run: 2026-11-25 09:35 ET 2-market-open-execution — selftest 5/5 exit 0. FIRED 08:36 FOR 09:35; POLLED clock 59 min TO is_open:true AND EXECUTED AT 09:35 — did NOT exit on the pre-market false. Plan 2026-11-25 DATED TODAY, staleness gate PASSED, ZERO intents. 0 buys, 0 sells, no §2 rebalance. Core 67.99% in band LIVE. Breaker INACTIVE 0/3, cap 0/3. BROKER CONFIRMED next_open 2026-11-27 — Thanksgiving VERIFIED at last.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 67.95
satellite_pct: 0.0
cash_pct: 32.05
open_thesis_ids: none
```

---

## Where things stand (2026-11-25, **MARKET OPEN — `is_open: true`, read at 11:41:24 ET**)

- ⚠⚠ **THIS RUN IS EXITS-ONLY AND HAD NOTHING TO EXIT.** `grep -ci 'status: *open'`
  `positions.md` → **0**; `positions` returns **one** row, VOO 99.046311231 sh @ 706.74, the §2
  core, **§5-exempt and struck from the working list, not cleared.** Ledger and broker **AGREE**,
  so nothing was traded on top of a suspect ledger. The routine's own Step 1 says: no open
  satellite positions → note it, commit, exit, **do not go looking for something to do.** That is
  what happened. **A midday run may not open a position under any circumstances.**
- ⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING — AND SO IS STEP 2's HIGH-WATER REPAIR.** No satellite
  `entry_price`, no `highest_close`, no `(as of …)` date, no `timing_window` deadline and no
  `invalidation` string exists anywhere in `positions.md`. Consequences, stated so a later seat
  does not read them as checks that cleared: **no stale mark could be detected and no `bars`
  backfill was owed or spent** · **no `perplexity` call was owed or spent on §5.1 — it needs an
  invalidation condition and a company name, and there is neither** · §5.2 has no deadline · §5.3
  has no entry price · §5.4 has no mark to measure from. **The §5.4 staleness detector, the
  backfill branch and all four sell rules remain UNEXECUTED CODE. 89th absent seat, 86th absent
  date** (today already counted by the 09:35 seat — three seats of one empty day is one fact
  about the ledger, not three).
- **Equity $93,613.98** · core mv **$63,613.98**, unrealized **−$6,386.01 / −9.123%** from the
  706.74 entry, cash **$30,000.00**. ⚠ Off `current_price` **642.265** at 11:41 — a **LIVE
  INTRADAY PRINT, NOT A CLOSE** (−2.792% on yesterday's official 660.67). The close run owns the
  closing figure. **No `bars` call was spent and none was owed** — this routine needs official
  closes only to repair a `highest_close`, and there is none to repair.
- ⚠⚠ **CORE −9.123% IS NOT A §5 EVENT, AND IT IS NOW WITHIN 0.88pp OF §5.4's −10% FIGURE.** §5
  exempts core outright and §2 says core is not sold on news. **Restated because the magnitude
  keeps deteriorating** — −8.307% pre-market, −8.989% at the open, **−9.123% now** — and a
  fresh-clone seat reading only the P&L line is exactly the failure this warning exists for.
  ⚠ **When it crosses −10%, nothing changes: there is no trailing stop on core and the number
  will look like a trigger. DO NOT SELL CORE.** ⚠ This is also the one number on which an
  exits-only run could do real damage, since selling is the only thing it is permitted to do.
- **§2 BAND RE-READ OFF LIVE PRICES — IN BAND, AND THIS RUN COULD NOT REBALANCE ANYWAY.** Core
  **67.95%** · satellite **0.0000%** · cash **32.05%** · `core_in_band: true` ·
  `rebalance_needed: false`. Thresholds **re-solved at this seat from the share count, not
  copied**: **65% floor at VOO 562.26**, **75% ceiling at 908.26**. `rebalance_delta` **$1,915.81**
  is the distance to the 70% *target*, **not a breach**, and §2 rebalances on the band — and §2
  puts any rebalance at the **next market-open run**, not here.
- **Housekeeping clean.** `week_anchor(2026-11-25)` → **2026-11-23** (imported from `common.py`,
  not hand-computed) = inherited `week_of`; **no reset due**, §6 cap stays **0 of 3**.
  `consecutive_closed_losses` **0** — nothing has ever closed, so there is no streak, the breaker
  is correctly **INACTIVE**, and **no §6 alert was owed.** `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `control.md` Notes **(none)** · `alerts.md` **Open incidents (none)**
  · `open_thesis_ids: none`.
- ⚠ **NOTHING SHOULD HAVE EXECUTED AND DID NOT.** `TRADING_ENABLED` is **true**, so no exit was
  suppressed into a dry run; there was simply no position to exit. **This is the honest zero, not
  a muzzled one** — the distinction the routine's "lead with anything that should have executed
  and did not" instruction exists to surface.
- ⚠ **This seat fired 11:41 for a 12:30 slot (~49 min early) — benign, and do NOT fold it into
  carry-forward item 3.** It landed **inside** the session with `is_open: true`, so the full
  routine ran at its intended capability. `next_close` **2026-11-25T16:00** confirms a normal
  full session today.

## What this run did

Read every memory file, reconciled the ledger against the broker, re-derived the week anchor and
the §2 band thresholds from the share count rather than copying them, and **placed no orders —
because there was no satellite position in existence to evaluate against §5.**

**Zero orders. Zero `trade_log.md` entries.** Nothing reached a terminal state because nothing
was submitted, and §7 forbids logging an order that was never placed.

**The one judgment call worth recording:** an exits-only run that finds an empty ledger has
exactly one way to fail usefully-looking — to find *something* to do with the one position it can
see. VOO is down **−9.123%**, past the −7% number in §5.3 and closing on the −10% number in
§5.4, and both figures are sitting right there in the `positions` output. **§5 exempts core and
§2 forbids selling it to fund anything; the correct action on the only tradeable row in the
account was to strike it from the working list.** That is not a sell rule passing — it is a rule
that does not apply.

**Not done, stated so it is not mistaken for having been done:** no high-water backfill (nothing
to backfill), no §5.1 news check (no name, no condition), no `sell_rule_status` write
(no position, so no field exists to write to), and **no new position** — a midday run is
forbidden one, and the 11-25 plan's zero intents plus four rejected theses are not a backlog this
seat may revive.

## Carry forward

1. ⚠⚠⚠ **THE FUNNEL GATE QUESTION HAS ITS SECOND CLEAN OBSERVATION, AND A NEW SECOND HALF.**
   **(a) The disputed sweep** — demanding that a **news source have already named** the
   second-order company and segment, which **§4 does not require** — was **omitted for the second
   consecutive session**, and for the second consecutive session the kills landed elsewhere: 11-24
   died on part-2 materiality, **11-25 died on a §4 hard filter.** The diagnostic the 11-24 seat
   proposed (watch whether kill reasons migrate off part 1) now has **two observations pointing
   the same way.** ⚠ **Two sessions is still not a finding.** Keep omitting it and keep watching.
   **No seat may relax a §4 test, and none has.**
   **(b) ⚠⚠ `alpaca.py move` IS A VOLATILITY FILTER, NOT A PRICED-IN FILTER.** §4 says *"moved
   more than 4% over the last five sessions **on this news**, you are late."* The script tests
   **absolute** magnitude. `T-2026-11-25-01` (MU) **fell 11.63%** and the thesis was **long** — a
   drawdown *against* the thesis, not the news being priced in. On 11-25 the filter killed **five
   of seven names checked (MU −11.63%, SNDK −21.86%, STX −4.37%, AAOI −15.01%, MOS −5.06%), all
   five on DOWN moves**, in a week the whole AI complex sold off. In a broad drawdown this gate
   disqualifies an entire sector regardless of which way the news cut. ⚠⚠ **NO RUN MAY ACT ON
   THIS. The guardrail is in code and §4 is explicit.** ⚠ **And the counter-argument is real:** a
   name down 11.6% in five sessions is one the market is repricing *against* the thesis, and a
   long entry there is what the §5.3 −7% hard stop punishes fastest — **the filter may be doing
   useful work by accident.** Both readings fit; a seat inside the loop cannot distinguish them.
   **A directional variant of the test is a calibration change and so the human's call.**
2. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING — FOURTH AND SEVENTH INSTANCES ON 11-25.** The
   Capricor CRL ("FDA rejection → incumbent benefits") appeared for the **fourth** time in three
   weeks, disposed with **zero** drill queries because the prior entries were read and applied;
   the unnamed-hyperscaler shape appeared a **seventh-plus** time (AAOI's $2.2B/4-yr 800G
   agreement with "a Tier-1 hyperscale customer"). ⚠ **Re-use is legitimate only because those
   kills are STRUCTURAL** — "a rejection preserves the status quo" and "an unnamed counterparty
   cannot be sized" hold independent of drug, company and date. **An object whose kill depends on
   a figure that can change still needs re-checking.** A disposed-objects list the pre-market seat
   checks first would help, **but defining "disposed" is a calibration change and so the
   human's.**
3. ⚠⚠ **BOTH EXECUTION ROUTINES FIRE ~60 MIN EARLY. Routine 4: 15:15 for 16:15, ~14 consecutive
   times. Routine 2: 08:36 for 09:35, THREE TIMES (11-23, 11-24, 11-25).** ⚠ **RECORDED, NOT
   DIAGNOSED** — `control.md` states manual "Run now" invocations are indistinguishable from
   scheduled ones in run logs, so **no run may call this a schedule fault.** Consequences differ
   and must not be folded together: routine 4's job is recording *closing* prices (11-24 measured
   the cost of not holding at **0.1552pp**, vs 11-23's 0.087pp — **two readings say the partial
   error is unpredictable in size, not reliably small**; the case for the hold is the variance,
   not any day's payoff); **routine 2's job is placing orders, and an early fire that exits on
   `is_open: false` skips a whole day's execution.** Mitigation is the same shape and has worked
   every time used — **3 of 3 for routine 2**: **poll `clock` to the right signature** — routine 4
   waits for `is_open: false` with **both** dates on the *next* session, then ~5 min, then `bars`;
   routine 2 waits for **`is_open: true`** (28 min on 11-24, 59 min on 11-25, executing at the
   intended 09:35). ⚠⚠ **THE MITIGATION IS LOAD-BEARING AND IS STILL NOT IN THE PROMPT.** It
   survives only as this item plus a line in `plan_today.md`, both agent-written; routine 2's
   prompt still says "If the market is closed, log the skip, commit, and exit successfully," which
   **read literally would have skipped execution on all three days.** ⚠ **A seat that trusted the
   prompt over this note would lose the day silently** — exit 0, looking clean. **Reconciling the
   prompt with this is the human's call.** ⚠ **Read the DATES, not the boolean: FALSE has three
   meanings, TRUE has one.** ⚠ Routines 1 and 3 also fire early (**07:02 for 08:00 on 11-25**;
   **11:41 for 12:30 on 11-25**) but land **outside the order path** and **inside** the session
   respectively, so both are benign — **do not fold them into this item.**
4. ⚠⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` — AND SOMETHING MUST CHECK THAT THE
   WINDOW EVER CLOSED. THIS HAS FAILED TWICE.** The scoping error cost 2026-11-13, whose journal
   entry and ClickUp summary do not exist and never will. The second instance: the 2026-11-20
   close run died between its insurance commit (`baf87a2`) and its restamp, leaving its entry on a
   637.53 intraday "midpoint" for two sessions — equity $93,144.99 / day −2.1354% recorded against
   an official $92,895.40 / **−2.3977%** / inception −7.1046%, **a loss understated by 0.2623pp,
   i.e. erring in the flattering direction.** Found and corrected on 11-24 **by appended table,
   not substitution**, so the evidence that the restamp failed survives. ⚠ **The 11-20 journal
   entry's own "if this still says PARTIAL" instruction therefore reads as live but is already
   DISCHARGED — re-verified at this seat against the 11-24 appended correction; do not backfill it
   a second time.** ⚠ **No ClickUp summary exists for 2026-11-20 and none can be reconstructed.**
   ⚠⚠ **Neither the 11-23 close seat nor the Friday review caught it — "a later run will notice"
   is not a working safety net.** Two fixes, both the human's call: (i) every routine greps
   `journal.md` for an unresolved `PARTIAL` marker in Step 1 and resolves it before its own work;
   (ii) make it a real alert key (`unresolved-partial`) so it surfaces in ClickUp instead of only
   inside a 172 KB file.
5. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "worst session in this account's history" — false by a factor of two. The 11-25
   pre-market seat's "first time in 86 days a candidate passed all four parts" **was** checked
   against `research_log.md`'s running total before it was written (0 accepted of ~304 theses).
   ⚠ **Applied at this seat:** "89th absent seat" was counted forward from the 09:35 seat's 88th,
   and the absent-**date** count was deliberately **not** incremented, because today was already
   counted this morning.
6. ⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM.** 16+
   distinct sessions, 0.04–1.41/share, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** **Build P&L and stamp `highest_close` from official `bars` closes only, one
   adjustment basis, one call.** ⚠ At this seat `lastday_price` **660.71** vs official **660.67**
   = **0.04 / 0.0061%**, the same pair and the same gap the 09:35 seat read — **one observation
   re-read, not a new one, and not added to the tally.** **No `bars` call was spent; none was
   owed, and one must not be spent merely to extend a count.**
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
   cannot see. Do not repeat inherited history claims as measured. 🛠 **THE Thu/Fri CALENDAR IS
   NO LONGER WHOLLY INHERITED: `next_open` read `2026-11-27T09:30` at BOTH the 09:35 and the
   11:41 seat, so Thursday 2026-11-26 is confirmed closed by the broker TWICE.** ⚠ **Friday
   2026-11-27's early close is STILL UNVERIFIED** — `next_close` today reads **16:00 for today**,
   which says nothing about Friday. **A seat on Friday must read `next_close` then: 13:00 confirms
   the early close, 16:00 refutes it.** **The verification costs nothing — it is a field in a
   `clock` call every run already owes.**
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` at this seat: `weekly_review.md` **415,188 B** ·
   `positions.md` **380,158 B** · `research_log.md` **367,908 B** · `journal.md` **171,776 B** —
   **~1.33 MB of markdown documenting ZERO satellite trades.** ⚠ **All four are byte-identical to
   the 09:35 seat's reading, because that seat wrote to none of them and neither did this one.**
   This seat wrote **nothing** to `research_log.md`, `trade_log.md` or `journal.md` — none was
   owed — and **one line** to `positions.md`. `state.md` was **19,920 B** on arrival; **the
   residual from this run is stamped in the commit, not estimated here** (prior seats twice
   claimed a size before measuring it and were wrong both times). ⚠ **The growth is NOT driven by
   trading activity — the account has made one trade in its history — it is driven by `state.md`
   prose and by the research funnel on days that produce theses.** That is the cost of the
   no-memory design, not waste, but it compounds every run regardless of whether the system ever
   trades.
   ⚠ **`positions.md` is 380 KB and holds ZERO open positions.** It is excluded from monthly
   rollover on the premise that it "only holds open positions," which has been **false for all 86
   absent dates.** **No run has standing to truncate it** — but the premise behind the exclusion
   is demonstrably wrong and **fixing it is the human's call.**
