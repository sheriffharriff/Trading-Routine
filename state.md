# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across eleven runs.

```
last_run: 2026-11-19 11:41 ET 3-midday-management — selftest 5/5 exit 0. ⚠ FIRST SEAT TODAY WITH THE MARKET OPEN (clock 11:41:21, is_open true, next_open 2026-11-20 = tomorrow, unambiguous mid-session). EXITS-ONLY run; no position may be opened and none was. ZERO EXITS — §5.1-§5.4 ABSENT, NOT PASSING (no operand: no entry price, no highest_close, no deadline, no invalidation string). Step 2 high-water repair had NO OPERAND — nothing to backfill, no (as of ...) date to compare. NO perplexity call made or owed (no name to check). 97th absent seat, 81st absent date (today already counted). Ledger reconciled 3rd time today, AGREES (grep -ci 'status: *open' = 0 satellite blocks vs 1 Alpaca row = core VOO, §5-exempt, struck not cleared). §7 order check: orders --status open = [], all = 1 order in account history (09-03 core fill d177d8f0, filled 99.046311231 @ 706.74), NOTHING non-terminal. ⚠⚠ SLEEVES ON THE DAY'S FIRST REAL SESSION PRINT: equity 96,577.94, core 68.93% IN BAND (3.93pp to the 65% floor), satellite 0.00%, cash 31.06% exactly 30,000.00; rebalance_needed false, NO REBALANCE PLACED and this run could not place one; rebalance_delta 1031.57 is a distance readout, not an order. ⚠⚠ THE MORNING MARKS WERE HIGH: VOO 672.27 vs official 11-18 close 671.26 = +0.150%, where 07:01 read +1.253% and 08:36 read +0.995% — the two pre-market seats overstated core by ~0.2pp and equity by ~$570, all mark and no flow (share count unchanged since 2026-09-03). Week anchor 2026-11-16 re-derived with isocalendar (2026-W47 wd 4), matches, no reset, cap 0 of 3. Breaker INACTIVE 0/3, no alert owed or posted. TRADING_ENABLED true, HALT_CLEARED_AT none. Schedule: fired 11:41 against a 12:30 schedule, ~49 min early, MID-SESSION, cost nothing; 11:41 is the same time logged on 11-18/17/16/11/10/06/05/04 — established pattern, recorded not diagnosed per control.md. NO notification sent — deliberate.
prior_run: 2026-11-19 08:36 ET 2-market-open-execution — selftest 5/5 exit 0, ⚠ fired PRE-BELL into a closed market (14th pre-bell firing, 11-02→11-19) but the plan carried ZERO buy/sell/rebalance intents so no order was prevented and the cost was zero; ledger agreed, core 69.12% in band on a pre-market mark, §5 absent.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.93
satellite_pct: 0.0
cash_pct: 31.06
open_thesis_ids: none
```

---

## Where things stand (2026-11-19 11:41 ET, **3-midday-management — market OPEN, zero exits, no operand**)

**THIS RUN IS EXITS-ONLY BY ITS OWN PROMPT AND OPENED NOTHING.** New positions go through
pre-market research and the 09:35 execution run; a midday entry would route around the rule
that forces every buy to sleep on a written thesis. There was nothing to route around today in
any case — the plan carries zero intents.

⚠⚠ **FIRST SEAT TODAY THAT COULD HAVE EXITED, AND NONE WAS DUE.** `clock` **11:41:21** —
`is_open: true`, `next_close` **2026-11-19T16:00:00-05:00**, `next_open`
**2026-11-20T09:30:00-05:00**. ⚠ **`next_open` carrying TOMORROW is the unambiguous mid-session
signature** — the two morning seats both read `is_open: false` with both dates on today, which
is pre-market, not a holiday.

**§5 RE-EVALUATED HERE, NOT INHERITED — ALL FOUR RULES ABSENT, NOT PASSING.**

| Rule | Status | Why ABSENT rather than passing |
|---|---|---|
| §5.1 thesis invalidation | **ABSENT** | No invalidation string exists — 288 thesis IDs, 0 ever accepted. **No per-name news check run or owed: there is no name.** No `perplexity` call was made. |
| §5.2 time stop | **ABSENT** | No timing window, no deadline. |
| §5.3 hard stop (−7%) | **ABSENT** | No entry price. |
| §5.4 trailing stop (−10%) | **ABSENT** | No `highest_close` exists. **Step 2's high-water repair had NO OPERAND** — nothing to backfill, no `(as of …)` date to compare against the last trading day. |

**97th absent seat, 81st absent date** (today already counted — four seats of one empty day is
one fact about the ledger, not four). **Zero exits here is the absence of a subject, not four
clean bills of health.** Core VOO is §5-exempt and was **struck from the working list, not
cleared**.

**LEDGER RECONCILED A THIRD TIME TODAY AND IT AGREES:** `positions.md` carries **zero**
satellite blocks (`grep -ci 'status: *open'` → **0**); `alpaca.py positions` returns **one
row**, VOO 99.046311231 sh @ 706.74.

**§7 ORDER VERIFICATION — CLEAN.** `orders --status open` → **`[]`**. `orders --status all` →
**exactly one order in this account's entire history**: the 2026-09-03 core fill
(`d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled 99.046311231 @ 706.74, `filled`). **Nothing
non-terminal; nothing was placed by this run.**

⚠⚠ **SLEEVES ON THE FIRST REAL SESSION PRINT OF THE DAY — THE NUMBER THE MORNING SEATS COULD
NOT PRODUCE, AND IT IS THE INTERESTING FINDING OF THIS RUN.** Equity **$96,577.94**; core
**$66,572.99 = 68.93%** / satellite **0.00%** / cash **$30,000.00 = 31.06%**.
`core_in_band: true`, `rebalance_needed: false` — **3.93pp above the §2 65% floor, 6.07pp below
the ceiling. NO REBALANCE DUE, and this run is not licensed to place one regardless.**
⚠ **`rebalance_delta: 1031.57` IS A DISTANCE READOUT TO THE 70% TARGET, NOT AN ORDER.**
⚠⚠ **AND THE MORNING MARKS WERE HIGH BY MOST OF A POINT.** VOO reads **672.27** against the
official 11-18 close **671.26** = **+0.150%**; the 07:01 seat read **+1.253%** and the 08:36
seat **+0.995%**. **Their 69.17% / 69.12% core figures overstated the live 68.93% by ~0.2pp and
equity by ~$570.** **Cash is exactly $30,000.00 and the share count is unchanged since the
2026-09-03 fill — all mark, no flow.** This is carry-forward item 5's variance hazard showing up
on the *sleeve* read rather than on `highest_close`: harmless while the band is six points wide,
**load-bearing on the first day core sits inside a point of 65%.**

**Week anchor 2026-11-16 re-derived here with `isocalendar`** (2026-W47, weekday 4) — matches
`week_of`, **no reset**, cap **0 of 3**. Breaker **INACTIVE 0/3**, no alert owed or posted.
`control.md`: **`TRADING_ENABLED: true`, `HALT_CLEARED_AT: none`**, Notes empty.

**NO NOTIFICATION WAS SENT, AND THAT IS DELIBERATE.** No stop breached, no exit owed, nothing
unverified, no incident open, breaker inactive, core in band, **zero positions at risk**. The
standing findings below are already with the human; re-pinging a standing item daily is how a
human learns to ignore the channel.

## Carry forward

1. ⚠⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-19 was the
   **14th pre-bell firing** across 11-02 → 11-19 (only 11-13 at 10:43 landed mid-session;
   11-16 did not fire at all). Sent out of band 11-12, re-sent 11-16. Re-send **only** if
   routine 2 begins firing consistently *after* the bell in a way that changes what the human
   must fix. ⚠ Per `control.md` this is **recorded, not diagnosed.**
   ⚠⚠ **THE STANDING COST, PLAINLY: the only run licensed to open positions could execute on
   exactly ONE session in that stretch. IT HAS STILL NOT COST A TRADE** — every one of those
   plans carried zero intents. **The damage to date is zero and the exposure is entirely
   forward-looking.** ⚠ **The first plan with a live intent that meets a pre-bell seat is the
   day this becomes expensive, and nothing prevents that from being tomorrow.**
   ⚠ **Routine 3's own ~49-min-early firing is a DIFFERENT and HARMLESS case** — 11:41 against
   12:30, logged identically on 11-18/17/16/11/10/06/05/04 — because an early midday seat still
   lands **inside** the session, which is the only window an exits-only run needs. **Do not fold
   the two schedule items together; their severities differ by routine.**
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly
   the two it omitted.** 11-16, 11-17 and 11-18 did it correctly. ⚠ **Not exercised on 11-19:
   no hold was due at either morning seat or at this one.**
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST, AND
   RANK OFF A CLOSE, NOT A PARTIAL BAR.** 11-16's close seat published "the worst session in
   this account's history" and it was false by a factor of two; 11-17's 15:15 summary ranked off
   a partial and needed a correction comment on ClickUp task `86bd4hbb1`. Ranking table is in
   `journal.md` 2026-11-17. **No superlative was written at this seat — a mid-session read is a
   partial by definition.**
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — STILL THE
   TWELFTH distinct instance.** `lastday_price` **671.31** vs official `bars` **671.26** for
   11-18 = **0.05 / 0.0074%**, identical at the 07:01, 08:36 and 11:41 seats. ⚠⚠ **A THIRD
   OBSERVATION OF ONE INSTANCE IS NOT A NEW INSTANCE**, and counting it as one would inflate the
   very trend the human is being asked to act on. Prior distinct instances ran **0.10–0.42**.
   ⚠ **A NARROW INSTANCE IS NOT A FIXED INSTANCE** — the spread has narrowed and widened
   repeatedly and is **not** a dividend-basis artifact. **Build P&L and stamp `highest_close`
   from official `bars` closes only, on one adjustment basis, in one call.**
5. ⚠⚠ **THE IN-PROGRESS-BAR DEFECT — GATE EVERY `highest_close` WRITE ON `clock`, never on the
   shape, presence or apparent stability of the bar.** Demonstrated dynamically on 11-18: the
   same dated bar pulled ~1 min apart gave **671.795 → 671.76**; after the bell, two pulls were
   identical. The 11-18 bar has now been byte-identical across four readings (close, 07:01,
   08:36 — `c` 671.26, `n` 2,671, `v` 88,905). **A finished bar does not move; an unfinished one
   carries NO FLAG saying so.**
   ⚠⚠⚠ **"PARTIALS READ LOW" IS DEAD — DO NOT RESURRECT IT AS A CORRECTION FACTOR.** 11-16 and
   11-17 read LOW; **11-18's partials read HIGH (+0.535 / +0.0797%)**; and **11-19's pre-market
   marks read HIGH by +0.845pp to +1.103pp against the eventual mid-session print.** The hazard
   is **variance, not bias**, and the only remedy is the `clock` gate. ⚠ **The HIGH direction is
   the dangerous one for §5.4:** it ratchets `highest_close` UP off a price that never traded, so
   the trailing stop fires early — **the SELLING direction.**
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the **97th** absent-seat ordinal. The first satellite position will be their first live test.
   **All four §5 sell rules remain untested code paths** — nothing has ever closed, so every "no
   exits" entry in this corpus records the absence of a subject, not a clean bill of health.
7. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13:
   adjusted and unadjusted closes identical to the cent on 259 of 260 sessions, across all four
   VOO ex-dividend dates). **Any review using the flag's output understates the benchmark and
   flatters the agent.** True 12-month VOO total return is **+14.615%**.
8. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 —
   the 2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The
   core sleeve is structurally short ~1.07%/yr against any honest total-return benchmark. **A
   run cannot fix either 7 or 8.**
9. **STILL MISSING AND NOT RECOVERABLE:** the `journal.md` entry for **2026-11-13** and that
   day's ClickUp daily summary. The price leg was discharged (VOO 693.05, equity 98,644.05, core
   69.59%, day −0.430%); **no seat has written, or should write, a backdated close-day
   narrative.**
10. ⚠⚠ **DO NOT MISREAD `delete-on-merge` AS A PUSH FAILURE.** An automation merges each session
   branch into `main` and **deletes the branch on merge**, so `git ls-remote --heads origin` will
   show your branch gone on every successful run and `git fetch origin <branch>` will fail with
   `couldn't find remote ref` — while `commit.py` correctly reported `"pushed": true`.
   ⚠ **THE CORRECT CHECK IS `git merge-base --is-ancestor <sha> origin/main`**, not whether your
   branch still exists on the remote.
11. ⚠ **PATH LABEL.** The research archives live at **`archive/research_log/2026-09.md`** (87
   IDs) and **`archive/research_log/2026-10.md`** (129 IDs). Earlier states abbreviated these as
   `archive/2026-09`, which **does not resolve as a path** — a seat pasting it silently
   under-counts by 216.
12. ⚠⚠ **THE PRICED-IN RULE IS UNDISCHARGED, NOT DISCHARGED. KEEP IT VERBATIM:** *when the
   plan's catalyst broke after the prior close, the open seat is the first that can actually
   perform the priced-in test; re-run `move --sessions 5` after the open and treat the pre-market
   reading as UNPERFORMED, not passed.* 11-19's principal catalyst — the **Nvidia China Hopper
   export halt, first disclosed 2026-11-19** — broke after the 11-18 close, and **the open seat
   that was meant to discharge this fired pre-bell with zero candidates, so no `move` call was
   made at all.** ⚠ **This midday seat did not discharge it either: it holds no intent and no
   candidate, and an exits-only run has no §4 gate to apply.** **The rule remains live for the
   first seat that holds an intent on a post-close catalyst.**
   ⚠ **The measured precedent is in `research_log.md` ADDENDUM 2026-11-18:** re-running thirteen
   names once a post-catalyst session had completed flipped **7 of 13 verdicts**; the eligible set
   went from **eight names to five**; **five names that read `false` that morning were already
   4.5–14% LATE**, MU among them.
   ⚠ **STILL UNFIXED AND STILL NOT A LICENCE: the filter is magnitude-based and direction-blind**
   (`abs(move) > 4`). **NVDA read `true` on 11-19 by having FALLEN 13.22%.** "The filter is
   direction-blind, therefore buy the faller" is averaging into weakness in a costume, and **§7
   forbids averaging down.** For the human to fix in code; **no run may grant itself this
   override.**
13. ⚠⚠ **`move` ALSO READS THE IN-PROGRESS BAR — so item 5's defect reaches a §4 GATE, not just
   `highest_close`, and §4 decides whether a position is opened at all.** Found 11-18: run
   mid-session at ~15:25, `move --symbol NVDA --sessions 5` returned `to_close` **150.87** while
   the 07:03 seat had read **155.49**, the 11-17 close — the window had silently rolled onto that
   day's unfinished bar. ⚠ **The gate is a convention, not code.** On 11-18 APH sat **0.22pp** and
   GEV **0.21pp** from the threshold. **Fix: gate the priced-in check on `clock` in code, exactly
   as `highest_close` is gated.**
14. ⚠⚠ **THE 288–0 AMBIGUITY, AND NO RUN CAN RESOLVE IT FROM THE INSIDE.** **288 thesis IDs, 0
   ever accepted** — unchanged at this seat, which writes no theses. §4 is explicit that most
   research runs should correctly produce no trade, and 11-19's six kills were **stated by
   sources**, not constructed by the agent. **But "the gates are correctly rejecting weak
   candidates" and "these gates can never pass" now produce identical evidence from inside the
   system.** ⚠⚠ **A RUN MUST NOT LOOSEN A GATE TO TEST THIS.**
   ✅ **What the data DOES support, narrowly:** the failures concentrate in **part 1 (mechanism)
   and part 2 (materiality)**, not in the priced-in filter or §3's thresholds. **Four of 11-19's
   six died because no second-order recipient was ever named by anybody.** If the human wants to
   tune §4, that is where to look.
   ⚠ **AND THE SCHEDULE FAULT CONFOUNDS THE COUNT:** the acceptance rate was measured over a
   stretch in which the executing seat could act on **one session in fourteen**. **288–0 is a
   research-gate statistic; it is not evidence about execution.**
15. ⚠ **THE TWO-PRICE DEFECT IS SOLVED AND IT IS A LIVE QUOTE MIDPOINT, NOT A FIXED OFFSET** —
   which is why the broker/official gap never had a stable size. A `positions.current_price` is an
   **intraday midpoint, not a close.** **Always `bars` for a close, a fresh `quote` for execution,
   NEVER a `positions` field for either.** Cosmetic on core; **load-bearing the moment a satellite
   position exists**, because a `highest_close` read from a `positions` field silently moves the
   §5.4 stop.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus **1,196,511 B** across the ten live files, read by every run — ⚠ **re-measured
at this seat with `os.path.getsize` AFTER this run's writes, not inherited.**
**`positions.md` is now 360,889 B and `weekly_review.md` is 379,023 B — the two of them are the
majority of the whole corpus**, and `positions.md` describes an **empty ledger**. **Neither is
reachable by the monthly rollover** — `positions.md` is excluded on the premise that it "only
ever holds open positions", which has been false for 78 days. **`positions.md` needs a retention
rule from the human; no run has standing to truncate it.** Full write-up: `weekly_review.md`,
week ending 2026-11-13, Recurring Error 1.
⚠⚠ **AND THIS SEAT MEASURED ITS OWN CONTRIBUTION RATHER THAN CLAIMING TO HAVE BEEN BRIEF:** its
`positions.md` digest added **3,299 B** — the 07:01 seat added 4,281 B and the 08:36 seat 4,183 B,
so **three seats of one empty day have cost 11,763 B of ledger describing nothing held.**
**Writing "deliberately short" does not make an addition free.**
✅ **Measured the other way too, because it is the only credit this seat can honestly claim: `state.md`
went 21,754 B → 19,971 B, a REAL reduction of 1,783 B on a file this seat is entitled to rewrite in
full. Net across both files this run added 1,516 B, not 3,299.** That is the whole lever a seat has.
This seat **collapsed nothing in `positions.md` and
claims no collapse ratio** — a seat is not entitled to collapse prose other seats wrote — and
**the line count is the wrong instrument; every "collapsed N → M" figure in that file is measured
with it and at least one changed sign when measured in bytes.**

⚠ **Second standing item, same reviewer:** the agent-authored rejection taxonomy ("rule (iii)" …
"rule (viii)") carries the majority of the historical rejection load and **exists nowhere in
`strategy.md`**, so a reader cannot tell which rejections rest on the strategy and which rest on
rules the system wrote for itself. The 11-18 and 11-19 seats wrote their rejections in §3/§4's own
language instead. ⚠ **That is those seats' response to the ask, not a decision the human has
made, and it binds no later seat.** The choice is still theirs: **promote the taxonomy into §4, or
rename it so the distinction is visible from the page.**

⚠ **All three items remain with the human in `weekly_review.md`. This seat sent NO notification**
— see the decision recorded above.
