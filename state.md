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
last_run: 2026-11-25 07:02 ET 1-premarket-research — selftest 5/5 exit 0. Pre-market, full session. Ledger AGREES (0 satellite). Core 68.15% in band. Breaker INACTIVE 0/3, cap 0/3. 5 theses, 0 accepted; plan 2026-11-25 has ZERO intents. T-2026-11-25-01 (MU) passed ALL FOUR §4 parts and died on the priced-in filter at −11.63% — FIRST TIME IN 86 DAYS. Calibration question escalated, nothing changed.
prior_run: 2026-11-24 16:10 ET 4-market-close-journal — selftest 5/5 exit 0. RESTAMPED ON THE OFFICIAL CLOSE (VOO 660.67). Equity 95436.93, day -0.3454%, inception -4.5631%. 0 trades. Step 2 high-water marks NOT updated — NO OPERAND. Core 68.5656% in band. FOUND + CORRECTED the 2026-11-20 entry, whose restamp never landed.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.15
satellite_pct: 0.0
cash_pct: 31.85
open_thesis_ids: none
```

---
## Where things stand (2026-11-25, **PRE-MARKET — `is_open: false`, both `clock` dates 2026-11-25**)

- **Equity $94,185.06** · core mv **$64,185.06**, unrealized **−$5,814.93 / −8.307%** from the
  706.74 entry, cash **$30,000.00**. ⚠ **Read off `current_price` 648.0308 at 07:02 — a
  PRE-MARKET PRINT, not a close** (−1.913% on yesterday's official `bars` close of 660.67). It
  will move before the bell. **No `bars` call was spent today; none was owed.**
- ⚠⚠ **CORE −8.307% IS NOT A §5 EVENT.** §5 exempts core outright, §2 says core is not sold on
  news. **Repeated prominently because the magnitude now sits past the §5.3 −7% *figure* and is
  within reach of §5.4's −10%**, and a fresh-clone seat reading only the P&L line is exactly the
  failure mode this warning exists for. **Do not sell core.**
- **§2 band: in band, no rebalance due.** Core **68.148%** pre-market (**68.566%** on yesterday's
  official close) · satellite **0.0000%** · cash **31.852%** · `core_in_band: true` ·
  `rebalance_needed: false`. Thresholds **re-solved at this seat, not copied**: **65% floor at VOO
  562.51** (−13.20% from the pre-market mark), **75% ceiling at 908.67**. `rebalance_delta`
  **$1,744.48** is the distance to the 70% *target*, **not a breach of the band**, and §2
  rebalances on the band. **§2 rebalancing is routine 2's job, not this seat's.**
- **LEDGER RECONCILED, AGREES.** `grep -ci 'status: *open'` → **0**; `positions` returns one row,
  VOO 99.046311231 sh @ 706.74, the §2 core, §5-exempt. **No disagreement to resolve, so no
  reconciliation work was owed.**
- ⚠⚠ **§5.1–§5.4 ARE ABSENT, NOT PASSING, AND `sell_rule_status` HAD NO OPERAND.** No entry
  price, no `highest_close`, no deadline, no invalidation string exists. **Step 4's instruction to
  record the distance to the hard and trailing stops had no field to write to** — that is not the
  same as the rules having been checked and cleared. **No `perplexity` call was spent on §5.1**;
  it needs an invalidation condition to test and none exists. **87th absent seat, 86th absent date.**
- **Housekeeping clean.** `week_anchor(2026-11-25)` → **2026-11-23** (imported from `common.py`)
  = inherited `week_of`; **no reset due**, §6 cap stays **0 of 3**. `consecutive_closed_losses`
  **0** — nothing has ever closed, so there is no streak, the breaker is correctly **INACTIVE**
  and **no §6 alert was owed.** `TRADING_ENABLED: true` · `HALT_CLEARED_AT: none` · `control.md`
  Notes **(none)** · `alerts.md` **no open and no SYSTEMIC incidents** · `open_thesis_ids: none`.
- **Five theses pre-market, five rejected** (`T-2026-11-25-01` … `-05`). **Plan dated 2026-11-25
  with ZERO intents: 0 BUY, 0 SELL, 0 REBALANCE.** **NEW POSITIONS WERE PERMITTED THROUGHOUT** —
  breaker inactive, cap 0/3, satellite 0% deployed, $30,000 cash, no `control.md` note. **Nothing
  structural blocked a buy. The candidates did. This is the unhalted zero.**
- ⚠⚠⚠ **THE ONE NEW THING TODAY — SEE CARRY-FORWARD ITEM 1.** `T-2026-11-25-01` (**MU**) passed
  **all four §4 thesis parts with sourced figures** and was killed by the **priced-in hard filter
  at −11.63%**. That is the **first time in 86 days and ~304 theses** a candidate has cleared all
  four parts. The kill migrated off part 1 and off the disputed sourcing gate onto one of §4's own
  filters.
- ⚠ **This seat fired ~07:02 for an 08:00 slot (~58 min early).** Per `control.md` manual "Run
  now" invocations are indistinguishable from scheduled ones in run logs, so this is **recorded,
  not diagnosed as a schedule fault.** **Benign for routine 1** — no orders are placed and the
  only cost is that the research window starts an hour earlier. **Do not fold it into
  carry-forward item 3**, whose subject is the two *execution* routines.
- ⚠ **ENDPOINT DISAGREEMENT, SAID ONCE:** `positions.lastday_price` **660.71** vs the official
  `bars` close **660.67** for 2026-11-24 = **0.04 / 0.0061%**, which **ties the narrowest value in
  the recorded 0.04–1.41 spread.** ⚠ **Different endpoint pair from 11-24's post-bell reading**
  (which compared same-session `bars` to `current_price`), so this is **recorded as an
  observation, not claimed as the Nth distinct instance** — this seat cannot verify the tally from
  a shallow clone.
- ⚠⚠ **THURSDAY 2026-11-26 IS THANKSGIVING; FRIDAY 2026-11-27 IS AN EARLY CLOSE.** **Still
  INHERITED and still NOT verified against the broker by any seat.** Check `clock` on the day, and
  **do not read Thursday's `is_open: false` as the pre-market signature. Read the DATES, not the
  boolean: FALSE has three meanings, TRUE has one.**

## What this run did

Read the memory files, reconciled the ledger against the broker, re-derived the week anchor and
the §2 band thresholds rather than copying them, and ran the funnel: **three broad sweeps, one
drill query, one figures query, seven `move` calls, three `asset` calls, zero `bars` calls.**
Wrote five theses, rejected five, wrote a plan with no intents.

**The one thing not on the checklist:** the drill query was spent to *test* the day's most
attractive bridge rather than to support it. HP's wording was "memory **and storage**" costs, and
**WDC was the only name in the complex that passed the priced-in filter** — so the tempting move
was to bridge the wording to a storage company and call it a thesis. **The query was asked in the
form that could break the link, and it broke it**: the source states HDDs are not a driver. The
right names were disqualified by a filter; the available name was disqualified by the facts.

The temptation this seat had to resist was **not** trading `-01` after writing four clean thesis
parts for it. Having done the work and found the thesis sound, the pull toward reading −11.63% as
"not really priced in, just a selloff" was strong and is **exactly** what §4's honest-broker rule
and the code guardrail exist to stop. **The filter was honored, the trade was skipped, and the
observation was escalated instead of acted on.**

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
   times. Routine 2: 08:36 for 09:35, twice (11-23, 11-24).** ⚠ **RECORDED, NOT DIAGNOSED** —
   `control.md` states manual "Run now" invocations are indistinguishable from scheduled ones in
   run logs, so **no run may call this a schedule fault.** Consequences differ and must not be
   folded together: routine 4's job is recording *closing* prices (11-24 measured the cost of not
   holding at **0.1552pp**, vs 11-23's 0.087pp — **two readings say the partial error is
   unpredictable in size, not reliably small**; the case for the hold is the variance, not any
   day's payoff); **routine 2's job is placing orders, and an early fire that exits on
   `is_open: false` skips a whole day's execution.** Mitigation is the same shape and has worked
   every time used: **poll `clock` to the right signature** — routine 4 waits for `is_open: false`
   with **both** dates on the *next* session, then ~5 min, then `bars`; routine 2 waits for
   **`is_open: true`** (28 min on 11-24). ⚠ **Read the DATES, not the boolean: FALSE has three
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
   endpoint-disagreement instance count and the Thu/Fri holiday calendar are both **inherited and
   flagged as such**, not restated as verified.
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` before this seat's writes: `weekly_review.md` **415,188 B** ·
   `positions.md` **378,179 B** · `research_log.md` **345,256 B** · `journal.md` **171,776 B** —
   **~1.31 MB of markdown documenting ZERO satellite trades.** ⚠ **This seat added ~22.7 KB to
   `research_log.md` and ~2.0 KB to `positions.md`, and that growth is defended, not apologised
   for:** `-01` and `-03` are the two most useful entries this funnel has produced — one records a
   thesis that passed every honest test and was stopped by a mechanised filter, the other records
   a bridge this seat wanted to build and spent a query to break. **A log that omitted either
   would hide the pattern the log exists to expose.** `positions.md` is excluded from monthly
   rollover on the premise that it "only holds open positions," which has been false for all 86
   absent dates, **so no run has standing to truncate it.**
   ⚠ **`state.md`: 15,088 B before this write, 17,653 B measured with `wc -c` AFTER it — +2,565 B,
   +17.0%.** 🛠 **SELF-CAUGHT AND CORRECTED IN PLACE:** this seat's first draft of this line said
   the rewrite was "roughly the same order as what it replaced" and that the figure "cannot be
   measured after, because it cannot be" — **both false, and both written from intent before
   measurement, which is the exact defect this item records and which prior seats committed twice.**
   It *can* be measured after; only the figure *stated inside the file* is inexact, because writing
   it adds to it. **So: the +17.0% is real and this seat makes no flatness claim.** The growth is
   carry-forward item 1(b), which is genuinely new. ⚠ Adding this correction grows the file again by
   a few hundred bytes, so the byte count a later seat reads will exceed 17,653 — **that residual,
   and only that, is the part inexact by construction.**
