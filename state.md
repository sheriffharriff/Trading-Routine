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
last_run: 2026-11-27 07:02 ET 1-premarket-research — SESSION DAY, ran in full. Selftest 5/5 exit 0, equity 96,217.41. `clock` 07:01:51 `is_open: false` with BOTH dates 2026-11-27 = pre-market, NOT a holiday; `next_close` 13:00 BROKER-CONFIRMS the early close for the first time. Ledger RECONCILED, AGREES (0 satellite both sides); §5 had NO OPERAND. FIVE theses written, FIVE rejected (T-2026-11-27-01..05) on §4 parts 1/2 and §3 — every §6/§7 gate was OPEN, so this is the UNHALTED ZERO. `plan_today.md` dated 2026-11-27 with ZERO BUY/SELL/REBALANCE intents. Core 68.82% in band, −5.404% (narrowed 1.369pp). Breaker INACTIVE 0/3, cap 0/3 and it now expires unused.
prior_run: 2026-11-26 15:15 ET 4-market-close-journal — MARKET HOLIDAY (Thanksgiving), SKIPPED per Step 1, as were that day's other three seats (07:01 · 08:36 · 11:41). No high-water marks owed or updated, zero journal/trade/research/positions writes, no ClickUp summary. Core 68.51% in band. Breaker INACTIVE 0/3.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.82
satellite_pct: 0.0
cash_pct: 31.18
open_thesis_ids: none
```

---

## Where things stand (2026-11-27 — **SESSION DAY, 09:30–13:00 EARLY CLOSE, RAN IN FULL**)

- ✅ **SELFTEST PASSED 5/5, exit 0** — env (6/6), Alpaca (ACTIVE, equity **96,217.41**,
  `trading_blocked: false`), Perplexity (`sonar-pro`), ClickUp, `control.md` LIVE. **Step 0's abort
  branch was NOT taken, and that matters most in this routine:** a Perplexity outage would have
  produced a theses-free day indistinguishable in `research_log.md` from a legitimate quiet one.
  **All three sweeps returned substantive cited answers, so the thin funnel is the window, not the
  tooling.**
- ⚠⚠ **TODAY IS A REAL SESSION AND THE DATE TEST IS WHAT PROVES IT.** `clock` 07:01:51 —
  `is_open: false`, `next_open` **2026-11-27T09:30**, `next_close` **2026-11-27T13:00**. **BOTH
  dates read TODAY = the pre-market signature.** Contrast 11-26, where both read a *later* session
  = holiday. **The distinction is the DATES, never the boolean.**
- ✅ **CARRY-FORWARD ITEM 8 DISCHARGED ON ITS OWN TERMS: THE 13:00 EARLY CLOSE IS NOW
  BROKER-CONFIRMED FROM A SEAT INSIDE THE SESSION DAY**, read straight off `next_close`. Five
  prior seats could only inherit it. **Next session: Monday 2026-11-30, 09:30–16:00** (per
  `next_open` once today's bell rings — **not yet verified, do not treat as measured**).
- ✅ **LEDGER RECONCILED, AGREES.** `positions.md` **Open positions: (none)** (`grep -ci 'status:
  *open'` → **0**) vs **one** Alpaca row, VOO **99.046311231 sh @ 706.74** — the §2 core,
  **§5-exempt, struck from the working list, not cleared.** §5.1–§5.4 **ABSENT, NOT PASSING** —
  no entry price, no `highest_close`, no deadline, no invalidation string. **Step 4 had NO OPERAND**,
  and **no `bars` backfill was owed**: the backfill branch keys on a stale `(as of …)` date and the
  field does not exist, which is a third state, not staleness.
- ✅ **NO ORDER IN LIMBO (§7).** `orders --status all` → **exactly one order in the account's entire
  history**, the 2026-09-03 VOO core buy, `filled`, already in `trade_log.md`. Checked, not assumed.
- **Account (pre-market mark, said once):** equity **$96,217.41** · core mv **$66,217.41** · cash
  **$30,000.00** · unrealized **−$3,782.58 / −5.404%** from the 706.74 entry · `current_price`
  **668.55**, **+1.469%** on `lastday_price` 658.87. Return since inception **−3.78%**
  (96,217.41 / 100,000.00 − 1, computed not estimated).
- ⚠⚠ **CORE −5.404% IS NOT A §5 EVENT, AND IT NARROWED.** Against **−6.773%** at all four 11-26
  seats, narrowed **1.369pp**; against −8.307% on 11-25, **2.903pp**. **Direction computed before
  being written** (item 10's rule — the 11-25 seat caught itself asserting "narrowed" on a figure
  that had widened). **§5 exempts core outright and §2 says core is not sold on news. No hard stop,
  no trailing stop on core. DO NOT SELL CORE.**
- **§2 band: IN BAND, re-read not copied.** Core **68.82%** · satellite **0.0%** · cash **31.18%** ·
  `core_in_band: true` · `rebalance_needed: false`. `rebalance_delta` **$1,134.78** is the distance
  to the 70% *target*, **not a breach** — §2 rebalances on the band. **NO REBALANCE INTENT.** Band
  edges re-solved: 65% breaks at VOO **562.51**, 75% at **908.67** (invariant while cash is exactly
  $30,000 and the share count is unchanged — that reproduction is arithmetic, not a copied value).
- **Housekeeping clean.** `week_anchor(2026-11-27)` → **2026-11-23** (imported from `common.py`) =
  inherited `week_of`; **no reset due**, §6 cap stays **0 of 3** and **now expires unused.**
  `consecutive_closed_losses` **0** — nothing has ever closed, so there is no streak, the breaker is
  correctly **INACTIVE** and **no §6 `circuit-breaker` alert is owed.** `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` (none needed) · `control.md` Notes **(none)** · `alerts.md` Open incidents
  **(none)** · `open_thesis_ids: none` · `journal.md` carries **no unresolved `PARTIAL`** (grepped
  at this seat; the 11-20 instance is DISCHARGED per item 5 — **do not backfill it again**).
- ⚠ **ENDPOINT DISAGREEMENT — NO NEW INSTANCE, AND NONE CLAIMED.** `lastday_price` **658.87** is the
  **same stale mark the four 11-26 seats read**, because 11-26 was not a session. **Item 6's counter
  holds at 18 distinct sessions.** No `bars` call was spent; none was owed, and one must not be spent
  merely to extend a tally.

## What this run did

Ran the selftest, read every memory file, read the clock and **confirmed a session day from the
dates**, reconciled the ledger, re-derived the week anchor, re-read the §2 band, and **did the
research the routine exists for**: three broad sweeps, three drill/figures queries, four `move`
calls, three `asset` calls, **zero `bars` calls**. **Five theses written and five rejected.** Wrote
`research_log.md` (~26 KB, five entries), `plan_today.md` (overwritten, dated **2026-11-27**, zero
intents), a one-line `positions.md` reconciliation, and this file. **Zero trades, zero alerts, zero
ClickUp tasks.**

**The judgment call worth recording:** `T-2026-11-27-01` had **TECK passing every mechanised gate** —
§3 cap ~$27.8B, `us_equity`/NYSE/tradable/active, priced-in **−1.68% `false`**, correlation clear by
vacancy — and it died because **two queries could not return an eligible filing figure for zinc's
share of its revenue.** This seat could have written "~20–25%" from general knowledge and the order
would have cleared `alpaca.py buy` in full, because the script **cannot tell a sourced figure from an
invented one.** **The figure was not supplied.** The guardrail that held was §4 part 2 read honestly,
not code — and that is the single most useful line in today's log, because it is the one there was
most pressure to leave out.

## Carry forward

1. ⚠⚠ **THE §4 PRICED-IN FILTER IS A VOLATILITY FILTER, NOT A PRICED-IN FILTER — BUT THIS WEEK'S
   EVIDENCE NOW CUTS AGAINST IT BEING THE BINDING CONSTRAINT.** §4 says *"moved more than 4% over
   the last five sessions **on this news**, you are late."* `alpaca.py move` tests **absolute**
   magnitude, so on 11-25 it killed **five of seven names (MU −11.63%, SNDK −21.86%, STX −4.37%,
   AAOI −15.01%, MOS −5.06%), all five on DOWN moves** — including `T-2026-11-25-01` (MU), the
   **only candidate in 86 days to pass all four thesis parts with sourced figures.** ⚠⚠ **TODAY IT
   KILLED ONE OF FOUR: SCCO −3.61%, TECK −1.68%, HL −3.34% all PASSED; only FCX −5.62% failed. The
   THESIS PARTS did the killing.** That is **three consecutive observations** (11-24 part-2
   materiality · 11-25 the filter · 11-27 parts 1 and 2) and only one of the three implicates the
   filter. ⚠ **NO RUN MAY ACT ON THIS — the guardrail is in code and §4 is explicit.** **A
   directional variant is a calibration change and so the human's call.**
2. ⚠⚠ **THE DISPUTED FUNNEL SWEEP NOW HAS FOUR CLEAN OBSERVATIONS AND THE PATTERN IS HOLDING.**
   Demanding that a news source have already **named** the second-order company and segment — which
   **§4 does not require** — has now been omitted for **four** consecutive sessions (11-24, 11-25,
   11-27, the 11-26 holiday adding nothing), and the kills landed elsewhere every time: part-2
   materiality, a §4 hard filter, part-1 causal denial, and today **part-1 sign ambiguity plus
   part-2 unsourceability.** ⚠ **Four sessions is suggestive, not conclusive.** Keep omitting it and
   keep watching. **No seat may relax a §4 test, and none has.**
3. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING AND TODAY IS THE STRONGEST CASE YET FOR A
   DISPOSED-OBJECTS LIST.** The export-control / AI-compute shape has now been disposed **four times
   in nine sessions** (11-17, 11-19, 11-23, 11-27) on the identical structural ground — *an export
   restriction removes a market from a US seller and names no US-listed recipient of the diverted
   demand* — with **zero drill queries** spent today. The Capricor CRL shape has appeared **four**
   times and the unnamed-hyperscaler shape **seven plus**. ⚠ **Re-use is legitimate only because
   those kills are STRUCTURAL and depend on no figure.** **An object whose kill rests on a figure
   that can change still needs re-checking** — which is why CF/MOS and Wanhua were re-verified
   rather than waved through. **Defining "disposed" is a calibration change and so the human's.**
   ✅ **ONE OBJECT DISCHARGED TODAY:** the **CrowdStrike results**, carried as UNESTABLISHED by the
   11-24 and 11-25 sweeps, is **disposed on staleness** — three sessions old, outside any sweep's
   window. **Off the list. This seat does NOT claim nothing material was in it.**
4. ⚠⚠ **ALL FOUR DAILY ROUTINES FIRE ~45–60 MIN EARLY. Routine 4: 15:15 for 16:15, ~16×. Routine 2:
   08:36 for 09:35, 4× (11-23→11-26). Routine 3: 11:41 for 12:30, 2×. Routine 1: ~07:02 for 08:00,
   4× including today.** ⚠ **RECORDED, NOT DIAGNOSED** — `control.md` states manual "Run now"
   invocations are indistinguishable from scheduled ones in run logs, so **no run may call this a
   schedule fault.** ⚠⚠ **CONSEQUENCES DIFFER BY ROUTINE AND MUST NOT BE FOLDED TOGETHER.** Routine
   1's and routine 3's early fires are **benign**. **Routine 2's 08:36 lands pre-market**, where a
   bare `is_open: false` exit **skips a whole day's execution**; its mitigation (poll to
   `is_open: true`) is **3 of 3** on session days, routine 4's (poll for `false` with both dates on
   the NEXT session, then ~5 min, then one `bars` call) is **4 of 4**. ⚠⚠ **THE POLL IS DATE-GATED,
   NOT BOOLEAN-GATED** — proven four times on 11-26, when both dates read a later session and
   polling to `true` would have hung until the harness killed the run. **Apply it ONLY when both
   dates read today.** ⚠ **FALSE has three meanings — holiday, pre-market, post-bell — and TRUE has
   one.** ⚠⚠ **BOTH MITIGATIONS ARE LOAD-BEARING AND NEITHER IS IN A PROMPT.** Routine 2's prompt
   still says *"If the market is closed, log the skip, commit, and exit successfully,"* which **read
   literally would have skipped execution on three session days** — and was **exactly right on the
   holiday. Reconciling the prompts is the human's call.** 🛠 **TODAY'S TWO EDGE CASES, BOTH LIVE:**
   routine 2 faces an 08:36 fire into a **13:00** close — a 3.5-hour session it cannot make up —
   and **both dates read today, so the poll applies** (flagged prominently at the top of
   `plan_today.md`). **Routine 4 INVERTS: a 15:15 fire lands 2h15m AFTER the 13:00 bell**, so
   `is_open` reads false with both dates on **Monday** — **the holiday shape on a day that WAS a
   session.** ⚠⚠ **A seat keying only on "both dates later = skip" would skip today's Step 2
   wrongly.** The discriminator is **"did today ever open?"**, not "are the next dates later?"
   (Moot only while the sleeve is empty, as now — there is no `highest_close` to stamp.)
5. ⚠ **THE INSURANCE COMMIT AND THE `PARTIAL` MARKER.** 11-25 was the first fully clean cycle since
   two failures: `journal.md` **was** in scope (the 2026-11-13 scoping error was not repeated), the
   commit pushed as `d591db1`, the restamp landed, and **no `PARTIAL` marker survives** — grepped
   again at this seat, not assumed. ⚠ **The 11-20 instance remains the warning:** that run died
   between its insurance commit and its restamp, leaving a 637.53 intraday "midpoint" standing for
   two sessions and understating a loss by **0.2623pp in the flattering direction**; it was corrected
   on 11-24 **by appended table, not substitution**, and **that correction is DISCHARGED — do not
   backfill it again.** ⚠ **No ClickUp summary exists for 2026-11-20 or 2026-11-26 and neither can be
   reconstructed** (11-26 correctly, per the holiday branch). Two fixes still the human's call:
   (i) every routine greps `journal.md` for an unresolved `PARTIAL` in Step 1 and resolves it before
   its own work; (ii) make it a real alert key (`unresolved-partial`) so it surfaces in ClickUp
   rather than only inside a 181 KB file.
6. ⚠⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM — 18
   DISTINCT SESSIONS.** Last measured 11-26 07:02: broker `current_price` **658.87** against the
   official `bars` close **658.735** = **0.135 / 0.0205%**. Range across 18 sessions
   **0.04–1.41/share**, narrowing and widening repeatedly; **not a dividend-basis artifact.**
   ⚠ **This seat re-read the same stale mark and did NOT count a 19th** — re-reading one closed
   session is not a new measurement. ⚠⚠ **This is Step 2's hazard specifically: stamp any
   `highest_close` from official `bars` closes only, one adjustment basis, one call** — never from
   the broker's `current_price`, or §5.4 trails a number from the wrong endpoint.
7. ⚠⚠ **TWO MEASUREMENT DEFECTS A RUN CANNOT FIX — FOR THE HUMAN.** (i) **`--adjustment all` is not
   a total-return series on this feed** — byte-identical to the unadjusted series on 259 of 260
   sessions across all four ex-dates. Reconstruct by reinvesting at the ex-date close: 2025-12-22
   $1.7710 · 2026-03-27 $1.8724 · 2026-06-26 $1.9622 · 2026-09-28 $1.8226 (TTM $7.43; **none since
   09-28**). Taken literally, §1's benchmark is understated by **1.25pp**. (ii) **The paper broker
   never credits distributions** — `cash` is exactly `30000`, `accrued_fees` 0. The core sleeve is
   structurally short ~1.07%/yr against any honest total-return benchmark, widening every quarter.
   ⚠⚠ **The two defects roughly cancel, which is why ten reviews caught neither.**
8. 🛠 **NEW — THE "PRODUCTION HALT" SWEEP SHAPE CARRIES A HIDDEN SIGN ASSUMPTION. FOR THE HUMAN, AND
   USABLE BY THE NEXT SEAT TODAY.** The 11-24 seat added a sweep for *production halts and input-price
   moves on a named cause*, and it has been the most productive new shape in the funnel. **It
   silently assumes the halt is at the MINE.** Today it surfaced the **Nyrstar Budel zinc SMELTER**
   halt (315 kt/yr, from 11-30), where the two legs have **opposite signs** for a vertically
   integrated candidate: removing refined capacity supports the **metal price** while removing a
   concentrate **buyer** moves treatment charges against the **concentrate seller**. ⚠ **This seat
   reasoned the TC sign wrong in the harder direction first and spent a drill query rather than
   writing it down — and the sourcing came back INTERNALLY CONTRADICTORY**, the summary asserting
   TCs fall while both cited sources describe relief *for smelters*, i.e. TCs rising against the
   miner. **A mechanism whose direction the evidence disputes is not a mechanism** (`T-2026-11-27-01`,
   part 1). 🛠 **Keep running the sweep; draw the mine/smelter distinction BEFORE taking the
   second-order step.**
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` **before** this run's `state.md` write: `weekly_review.md`
   **415,188 B** · `positions.md` **383,983 B** (→ **385,713 B** after this seat's ~1.7 KB one-line
   note) · `research_log.md` **367,908 B** (→ **~394 KB** after today's five entries, **~+26 KB, the
   largest single-day research write this month**) · `journal.md` **180,979 B** · `state.md`
   **19,423 B** · `plan_today.md` **12,017 B** (→ **14,962 B**) · `trade_log.md` **4,573 B** ·
   `alerts.md` **2,632 B** — **~1.39 MB of markdown documenting ONE trade.** ⚠ **The growth is NOT
   driven by trading activity** — one trade in this account's history — **it is driven by `state.md`
   prose and by the research funnel on days that produce theses, and today is the clearest
   demonstration yet: a day with ZERO trades wrote ~31 KB.** ⚠ **`positions.md` is 386 KB and holds
   ZERO open positions.** It is excluded from monthly rollover on the premise that it "only holds
   open positions," **false for all 87 absent dates.** **No run has standing to truncate it** — but
   the premise behind the exclusion is demonstrably wrong and **fixing it is the human's call.**
   ⚠ **THIS SEAT REWROTE ITS OWN NARRATIVE RATHER THAN APPENDING A FIFTH ACCOUNT AND HELD THIS FILE
   TO ROUGHLY ITS INHERITED SIZE**, which is the most any seat can do without the rule. ⚠ **Stated
   as an order of magnitude deliberately:** an exact byte count inside this clause changes the file
   it is counting — the 11-24 seat hit that trap over three drafts. **A per-run finding and a flat
   file remain in direct tension.**
10. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND DO NOT WRITE A NUMBER FROM INTENT
    BEFORE COMPUTING IT.** 11-16 published "worst session in this account's history" — false by a
    factor of two. 11-25 caught itself writing that the core's loss "**narrowed** to −6.7925%" when
    against Tuesday's −6.5187% it had **widened by 0.27pp**; the slip ran in the flattering direction
    and is **left in `journal.md` with its correction in place**, not silently fixed.
    ⚠ **Applied at this seat:** the core's −5.404% was differenced against 11-26's −6.773% **before**
    the word "narrowed" was written (it had genuinely narrowed, 1.369pp); item 6's session counter was
    **held at 18** rather than advanced on a re-read of a stale mark; the week anchor was imported
    from `common.py`; the band edges were re-solved from the 0.35/0.25 identities and flagged as
    **invariant** rather than claimed as independently derived; return-since-inception was computed
    (96,217.41 / 100,000.00 − 1 = **−3.78%**); **"the largest single-day research write this month"
    was ranked against the month's entries before being written**; and the absent-seat counters
    **were** incremented (91 seats / 87 dates) **because today IS a session** — unlike 11-26, where
    four seats correctly declined to increment them for a non-session.
