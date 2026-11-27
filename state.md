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
last_run: 2026-11-27 11:42 ET 3-midday-management — SESSION DAY (09:30–13:00 EARLY CLOSE), fired ~48 min early for the 12:30 slot but INSIDE the session (`clock` 11:42:43 `is_open: true`, `next_close` TODAY 13:00, `next_open` Mon 11-30 09:30 — the in-session signature, read off the DATES not the boolean). Selftest 5/5 exit 0. EXITS-ONLY run and there was NOTHING TO EXIT: zero satellite positions, so Steps 2–5 had NO OPERAND — no `highest_close`/`(as of …)` anywhere, so no `bars` backfill owed or spent (field ABSENT is a third state, not stale); no invalidation string and no company name, so no §5.1 Perplexity call owed or spent; no deadline (§5.2), no satellite entry price (§5.3), no mark (§5.4). ALL FOUR ABSENT, NOT PASSING — not 'the rules passed'. ZERO exits, ZERO orders placed, `orders --status open` → `[]` so nothing in limbo (§7). Core −5.593% live, §5-EXEMPT, DO NOT SELL. Band re-read off live prices: core 68.78% IN BAND; `rebalance_delta` 1176.08 is a distance readout and routine 3 may not place it regardless. Week anchor 2026-11-23 unchanged, no rollover. Breaker INACTIVE 0/3, cap 0/3. Flagged but NOT resolved: the absent-seat ordinal in `positions.md` is carried on two irreconcilable schemes (note chain 89→90→91 vs the 11-23 digest header's 103·104·105).
prior_run: 2026-11-27 09:36 ET 2-market-open-execution — fired ~59 min early into PRE-MARKET, POLLED to the bell (date-gated) and executed INSIDE the session. Selftest 5/5. `plan_date` 2026-11-27 = TODAY, staleness gate PASSED. Plan carried ZERO BUY / ZERO SELL / ZERO REBALANCE intents — the UNHALTED ZERO. Step 3 skipped (`core_established: true`), Step 4 no operand, Step 7 band 68.68% IN BAND. ZERO orders, ZERO in limbo. Wrote no `positions.md` note, deliberately.
week_of: 2026-11-23
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.78
satellite_pct: 0.0
cash_pct: 31.22
open_thesis_ids: none
```

---

## Where things stand (2026-11-27 — **11:42 ET, INSIDE the 09:30–13:00 EARLY CLOSE**)

- ✅ **SELFTEST PASSED 5/5, exit 0** — env (6/6), Alpaca (ACTIVE, equity **96,072.80**,
  `trading_blocked: false`), Perplexity, ClickUp, `control.md` **LIVE (paper account)**.
- ⚠⚠ **THE ONE SENTENCE THAT MATTERS: THIS SEAT EXISTS TO ACT ON A STOP BREACH AT LUNCHTIME, AND
  THERE WAS NO POSITION TO BREACH ONE.** Zero satellite positions. **Nothing should have executed
  and did not.** Per Step 1 this seat noted the absence, committed, and **did not go looking for
  something to do** — and per the prompt's own framing it **may not open a position in this run**,
  so the 31.22% cash and the 68.78% core are not this seat's to act on either.
- ✅ **IN SESSION, IDENTIFIED FROM THE DATES NOT THE BOOLEAN.** `clock` **11:42:43** →
  `is_open: **true**`, `next_close` **2026-11-27T13:00** (TODAY — the day-after-Thanksgiving early
  close, broker-confirmed), `next_open` **2026-11-30T09:30** (Monday). ⚠ **FALSE has three meanings
  — holiday, pre-market, post-bell — and TRUE has one.**
- ⚠ **FIRED 11:42 FOR A 12:30 SLOT, ~48 MIN EARLY — AND IT COST NOTHING, FOR A REASON WORTH KEEPING
  SEPARATE.** The market was already open, so the seat was never degraded; and the funnel was empty
  regardless. **This is NOT the routine-2 defect and must not be folded into it** (carry-forward
  item 4 holds the per-routine tally; routine 3 is now **3×**).
- ✅ **LEDGER RECONCILED, AGREES — CHECKED, NOT INHERITED.** `positions.md`
  `grep -ci 'status: *open'` → **0** vs `alpaca.py positions` → **one** row, VOO
  **99.046311231 sh @ 706.74**, the §2 core: **§5-exempt, struck from the working list, not
  cleared.**
- ⚠⚠ **STEPS 2–5 HAD NO OPERAND, WHICH IS A DIFFERENT CLAIM FROM "THE RULES PASSED" AND THE
  DISTINCTION IS THE WHOLE POINT OF THIS ROUTINE.**
  **Step 2 (high-water repair):** there is **no `highest_close` field and no `(as of …)` date
  anywhere in `positions.md`**, so nothing could be found stale and **no `bars` backfill was owed or
  spent.** ⚠ **An ABSENT field is a third state, not a stale one** — and the prompt's warning that a
  stale mark silently disables §5.4 is about a mark that *exists*. **Neither failure mode can arise
  on an empty ledger, and no `--adjustment all` basis hazard arose because no stored mark exists to
  be compared across bases.**
  **§5.1** — no `invalidation` string and **no company name** exists, so **no Perplexity call was
  owed or spent. There is no name to query.**
  **§5.2** no `timing_window`/deadline · **§5.3** no satellite entry price · **§5.4** no mark.
  **ALL FOUR ABSENT, NOT PASSING — the §5 machinery is still unproven code.**
- ✅ **NO ORDER IN LIMBO (§7).** `orders --status open` → **`[]`**. This run submitted nothing, so it
  created no new limbo risk. Checked, not assumed.
- **Account (LIVE 11:42 in-session mark, said once):** equity **$96,079.74** · core mv
  **$66,079.74** · cash **$30,000.00** · unrealized **−$3,920.25 / −5.593%** from the 706.74 entry ·
  `current_price` **667.215**, **+1.267%** on `lastday_price` **658.87**. Return since inception
  **−3.92%** (96,079.74 / 100,000.00 − 1, computed not estimated).
- ⚠⚠ **CORE −5.593% IS NOT A §5 EVENT, AND IT IS PAST THE §5.3 FIGURE — WHICH IS EXACTLY WHY THE
  EXEMPTION IS WRITTEN DOWN.** It **narrowed 0.426pp** against this morning's −6.019% open-seat
  print and **1.18pp** against the −6.773% the four 11-26 holiday seats read. **§5 exempts core
  outright and §2 says core is not sold on news. A rule not applying is NOT a rule passing.
  DO NOT SELL CORE.**
- **§2 band: IN BAND, re-read off LIVE prices.** Core **68.78%** · satellite **0.0%** · cash
  **31.22%** · `core_in_band: true` · `rebalance_needed: false`. ⚠ `rebalance_delta` **$1,176.08**
  is the distance to the 70% *target*, **not a breach** — §2 rebalances on the **band** — **and
  routine 3 may not place a rebalance regardless: this run is EXITS ONLY.** Core sits below target
  because it is **down 5.6% from entry**, not from drift worth chasing.
- **Housekeeping clean.** `week_anchor(2026-11-27)` → **2026-11-23** = inherited `week_of`; **no
  reset due**, §6 cap stays **0 of 3** and **expires unused** at today's 13:00 bell. Breaker
  correctly **INACTIVE 0/3**, **no `circuit-breaker` alert owed.** `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `control.md` Notes **(none)** · `alerts.md` Open incidents **(none)** ·
  `open_thesis_ids: none`.
- ✅ **RUN CONTINUITY CHECKED AT THIS SEAT, NOT ASSUMED.** `git log` confirms **all five seats fired
  on every session back through 11-20**, including both 11-25 close commits and the four 11-26
  holiday skips. **No close run was missed, so the Step 2 premise that sends this seat to `bars`
  never arose — and that is a verified fact today, not an inherited one.**

## What this run did

Ran the selftest, read every memory file in full, read the `clock` and **identified the live session
from the dates rather than the boolean**, reconciled the ledger against Alpaca, re-derived the week
anchor, confirmed nothing was in limbo, verified run continuity from `git log`, and re-read the §2
band off live prices. **Zero exits. Zero orders placed. Zero alerts, zero ClickUp tasks.**

⚠ **FILES DELIBERATELY NOT WRITTEN, SO THE NEXT SEAT READS THIS AS A CHOICE AND NOT AN OMISSION:**
no `trade_log.md` entry (nothing was submitted, so nothing reached a terminal state), no
`research_log.md` entry (this routine generates no theses, by design), no `journal.md` entry (the
close seat owns the daily narrative), **and no new `### sell_rule_status` digest block in
`positions.md`** — Step 5 writes `sell_rule_status` **per open position** and there are none, so the
**one-line reconciliation note is the lawful maximum write, not a skipped step.**

**The judgment call worth recording:** whether to spend a `perplexity` §5.1 call or a `bars` Step 2
call to make the run look complete. **Neither was spent, because neither had an argument** — there
is no company to ask about and no mark to re-date. **A call spent to extend a tally is manufactured
activity, and the honest record is that this seat had nothing to do.**

## Carry forward

1. ⚠⚠ **THE §4 PRICED-IN FILTER IS A VOLATILITY FILTER, NOT A PRICED-IN FILTER — NO NEW OBSERVATION
   TODAY AND NONE MANUFACTURED.** §4 says *"moved more than 4% over the last five sessions **on this
   news**, you are late."* `alpaca.py move` tests **absolute** magnitude, so on 11-25 it killed
   **five of seven names, all five on DOWN moves** — including `T-2026-11-25-01` (MU), the **only
   candidate in 86 days to pass all four thesis parts with sourced figures.** On 11-27 it killed
   **one of four** (FCX −5.62%; SCCO −3.61%, TECK −1.68%, HL −3.34% passed) and **the thesis parts
   did the killing.** ⚠ **This seat spent no `move` call** — there was no intent to revalidate —
   so the count of observations is **unchanged at three** (11-24 part-2 materiality · 11-25 the
   filter · 11-27 parts 1 and 2). ⚠ **NO RUN MAY ACT ON THIS** — the guardrail is in code and §4 is
   explicit. **A directional variant is a calibration change and so the human's call.**
2. ⚠⚠ **THE DISPUTED FUNNEL SWEEP HAS FOUR CLEAN OBSERVATIONS — UNCHANGED TODAY.** Demanding that a
   news source have already **named** the second-order company and segment — which **§4 does not
   require** — has been omitted for **four** consecutive research sessions (11-24, 11-25, 11-27),
   and the kills landed elsewhere every time. **This routine does no research, so it adds nothing
   here.** ⚠ **Four sessions is suggestive, not conclusive.** **No seat may relax a §4 test.**
3. ⚠⚠ **THE FUNNEL IS PARTLY RECIRCULATING AND A DISPOSED-OBJECTS LIST IS THE OPEN ASK.** The
   export-control / AI-compute shape has been disposed **four times in nine sessions** (11-17,
   11-19, 11-23, 11-27) on the identical structural ground; the Capricor CRL shape **four** times,
   the unnamed-hyperscaler shape **seven plus**. ⚠ **Re-use is legitimate only because those kills
   are STRUCTURAL and depend on no figure.** **An object whose kill rests on a figure that can
   change still needs re-checking.** **Defining "disposed" is a calibration change and so the
   human's.** The **CrowdStrike** object was disposed on staleness 11-27 and is **off the list.**
4. ⚠⚠ **ALL FOUR DAILY ROUTINES FIRE ~45–60 MIN EARLY. Routine 4: 15:15 for 16:15, ~16×. Routine 2:
   08:36 for 09:35, now 5× (11-23→11-27). Routine 3: 11:41–11:42 for 12:30, 3×. Routine 1: ~07:02 for
   08:00, 4×.** ⚠ **RECORDED, NOT DIAGNOSED** — `control.md` states manual "Run now" invocations are
   indistinguishable from scheduled ones in run logs, so **no run may call this a schedule fault.**
   ⚠⚠ **CONSEQUENCES DIFFER BY ROUTINE AND MUST NOT BE FOLDED TOGETHER.** Routine 1's and routine
   3's early fires are **benign**. **Routine 2's 08:36 lands pre-market**, where a bare
   `is_open: false` exit **skips a whole day's execution**; its mitigation (poll to `is_open: true`)
   is **4 of 4** on session days, routine 4's is **4 of 4**. ⚠⚠ **THE POLL IS DATE-GATED, NOT
   BOOLEAN-GATED** — proven four times on 11-26, when both dates read a later session and polling
   to `true` would have hung until the harness killed the run. **Apply it ONLY when both dates read
   today**, and **bound it with a deadline** (this seat capped the wait so it could not hang). ⚠⚠ **BOTH MITIGATIONS ARE LOAD-BEARING AND NEITHER IS IN A PROMPT.** Routine 2's prompt
   still says *"If the market is closed, log the skip, commit, and exit successfully,"* which **read
   literally would have skipped execution on four session days** — and was **exactly right on the
   holiday. Reconciling the prompts is the human's call.** 🛠 **TODAY'S CHEAPEST EVIDENCE YET, AND IT
   IS TWO-SIDED:** the poll was **safe and correct**, and it also **saved nothing**, because the plan
   carried zero intents (see the honest qualifier above). **A fix should turn on whether the plan
   holds intents, not on the boolean alone.** ⚠ **ROUTINE 4'S INVERSION IS STILL LIVE TODAY:** a
   15:15 fire lands **2h15m AFTER the 13:00 bell**, so `clock` will read `is_open: false` with both
   dates on **Monday 2026-11-30** — **the holiday shape on a day that WAS a session.** The
   discriminator is **"did today ever open?"**, not "are the next dates later?" **Today it opened —
   this seat confirmed `is_open: true` at 09:36:03 ET, and that fact is recorded here precisely so
   the 15:15 seat does not have to infer it.** (Moot for §5 only while the sleeve is empty, as now.)
5. ⚠ **THE INSURANCE COMMIT AND THE `PARTIAL` MARKER.** 11-25 was the first fully clean cycle since
   two failures: `journal.md` **was** in scope, the commit pushed as `d591db1`, the restamp landed,
   and **no `PARTIAL` marker survives** — grepped again at this seat, not assumed. ⚠ **The 11-20
   instance remains the warning:** that run died between its insurance commit and its restamp,
   leaving a 637.53 intraday "midpoint" standing for two sessions and understating a loss by
   **0.2623pp in the flattering direction**; corrected on 11-24 **by appended table, not
   substitution**, and **DISCHARGED — do not backfill it again.** ⚠ **No ClickUp summary exists for
   2026-11-20 or 2026-11-26 and neither can be reconstructed** (11-26 correctly, per the holiday
   branch). Two fixes still the human's call: (i) every routine greps `journal.md` for an unresolved
   `PARTIAL` in Step 1; (ii) make it a real alert key (`unresolved-partial`) so it surfaces in
   ClickUp rather than only inside a 181 KB file.
6. ⚠⚠ **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 WOULD READ FROM ONE OF THEM — 18
   DISTINCT SESSIONS, HELD AT 18 AGAIN TODAY.** Last measured 11-26 07:02: broker `current_price`
   **658.87** against the official `bars` close **658.735** = **0.135 / 0.0205%**. Range across 18
   sessions **0.04–1.41/share**, narrowing and widening repeatedly; **not a dividend-basis
   artifact.** ⚠ **Two seats today re-read the same stale 658.87 and NEITHER counted a 19th** —
   re-reading one closed session is not a new measurement. ⚠⚠ **Routine 4 must stamp any
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
8. 🛠 **THE "PRODUCTION HALT" SWEEP SHAPE CARRIES A HIDDEN SIGN ASSUMPTION — FOR THE NEXT RESEARCH
   SEAT.** The sweep for *production halts and input-price moves on a named cause* has been the most
   productive new shape in the funnel. **It silently assumes the halt is at the MINE.** On 11-27 it
   surfaced the **Nyrstar Budel zinc SMELTER** halt (315 kt/yr, from 11-30), where the two legs have
   **opposite signs** for a vertically integrated candidate: removing refined capacity supports the
   **metal price** while removing a concentrate **buyer** moves treatment charges against the
   **concentrate seller**. **A mechanism whose direction the evidence disputes is not a mechanism**
   (`T-2026-11-27-01`, part 1). 🛠 **Keep running the sweep; draw the mine/smelter distinction BEFORE
   taking the second-order step.**
9. ⚠⚠ **CORPUS GROWTH IS THE STANDING SYSTEMIC FINDING AND IT NEEDS A RETENTION RULE FROM THE
   HUMAN.** Measured with `wc -c` **before** this run's `state.md` write: `weekly_review.md`
   **415,188 B** · `research_log.md` **394,056 B** · `positions.md` **385,713 B** · `journal.md`
   **180,979 B** · `state.md` **19,982 B** · `plan_today.md` **14,962 B** · `trade_log.md`
   **4,573 B** · `alerts.md` **2,632 B** — **~1.42 MB of markdown documenting ONE trade.** ⚠ **The
   growth is NOT driven by trading activity** — one trade in this account's history — **it is driven
   by `state.md` prose and by the research funnel.** ⚠ **`positions.md` is 386 KB and holds ZERO
   open positions.** It is excluded from monthly rollover on the premise that it "only holds open
   positions," **false for all 87 absent dates.** **No run has standing to truncate it** — but the
   premise behind the exclusion is demonstrably wrong and **fixing it is the human's call.**
   ✅ **THIS SEAT WROTE EXACTLY ONE FILE** — this one — **rewriting its narrative rather than
   appending a sixth account, and declining the `positions.md` note it could have justified.**
   ⚠ **It still came out ~6% larger**, because today's two-sided poll evidence and Monday's
   confirmation are new; **"roughly flat" is the ceiling a seat can hit, not zero.**
   **That is the most any seat can do without the rule.** ⚠ **Stated as an order of magnitude
   deliberately:** an exact byte count inside this clause changes the file it is counting — the
   11-24 seat hit that trap over three drafts, and the 11-26 close seat corrected its own figure
   for the same reason.
10. ⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND DO NOT WRITE A NUMBER FROM INTENT
    BEFORE COMPUTING IT.** 11-16 published "worst session in this account's history" — false by a
    factor of two. 11-25 caught itself writing that the core's loss "**narrowed** to −6.7925%" when
    against Tuesday's −6.5187% it had **widened by 0.27pp**; the slip ran in the flattering
    direction and is **left in `journal.md` with its correction in place**, not silently fixed.
    ⚠ **Applied at this seat, and it mattered:** the core's −6.019% was differenced against **three**
    prior marks **before** any direction word was written, and it came out **two-sided** — narrower
    than 11-26 (0.754pp) and 11-25 (2.288pp) but **WIDER than this morning's pre-market print
    (0.615pp)**. **Both are in the entry**; quoting only the narrowing would have been the
    flattering half. Also applied: item 6's counter **held at 18** on a stale re-read, the week
    anchor **imported** from `common.py`, the band edges **re-solved** from the 0.35/0.25 identities
    and flagged **invariant** rather than claimed as independent, return-since-inception **computed**
    (95,786.85 / 100,000.00 − 1 = **−4.21%**), and the poll's record stated as **"4 of 4 safe, 0
    saved today"** rather than the bare four-of-four.
