# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across twelve runs.

```
last_run: 2026-11-19 15:15 ET 4-market-close-journal — PROVISIONAL / PRE-CLOSE WRITE, hold for the bell IN PROGRESS. selftest 5/5 exit 0. ⚠ Fired 15:15:51 with clock is_open TRUE, next_close 16:00 today, next_open 2026-11-20 — 45 min PRE-BELL, 14th consecutive EST session on the −1h shape; recorded not diagnosed per control.md. STEP 2 HAD NO OPERAND: zero satellite blocks, no highest_close on any name, none raised, no (as of ...) date advanced — NOTHING OWED OR DEFERRED for 2026-11-19. ⚠ AND IT COULD NOT HAVE BEEN DONE IF OWED: the clock gate was CLOSED all through this seat's pre-bell window and the 11-19 VOO bar was in progress (c 658.61, n 2,302, v 98,567, session high 679.99); the hold-for-the-bell remedy is a CONVENTION IN THESE FILES, NOT CODE. Ledger reconciled 4th time today, AGREES (0 satellite blocks vs 1 Alpaca row = core VOO, §5-exempt, struck not cleared). §5 ABSENT ON ALL FOUR RULES, NOT PASSING — 98th absent seat, 81st absent date. ZERO trades at all four of today's seats; §7 CLEAN — orders --status open = [], all = 1 order in account history (09-03 core fill d177d8f0, filled 99.046311231 @ 706.74), nothing non-terminal. PARTIAL-basis equity 95,232.89 (VOO 658.61 in-progress + 30,000 cash), day −1,252.94 / −1.2986% vs 11-18 close-basis 96,485.83, since inception −4.7671%; core 68.4983% IN BAND (3.4983pp to floor), satellite 0.00%, cash 31.5017%, rebalance_needed false, NO REBALANCE DUE 11-20. ⚠⚠ A GAP-UP THAT FULLY REVERSED: VOO opened 678.15 (+1.0264%), high 679.99 (+1.3005%), now 658.61 — −3.1442% off the high, −1.8845% on the day; all mark, no flow (share count unchanged since 09-03, cash exactly 30,000.00). ⚠⚠ TWO SUPERLATIVES WERE DRAFTED OFF THE PARTIAL AND NEITHER WAS PUBLISHED (item 3): "2nd-worst of 55 sessions" sits 0.0244pp from 11-16's −1.2742% and can flip in 45 min; "lowest equity print in account history" needs a +1.3% rally to flip. Ranked off the official close in journal.md. ⚠⚠ THE MARK HAZARD'S SHARPEST DEMONSTRATION YET: the 07:01 seat read VOO 679.67, within 0.047% of the session HIGH, now 3.14% below — a §5.4 mark from that seat would sit a hair under the day's top, moving the stop closer in the SELLING direction. Week anchor 2026-11-16 re-derived with isocalendar (2026-W47 wd 4), matches, no reset, cap 0 of 3. Breaker INACTIVE 0/3, no alert owed or posted. TRADING_ENABLED true, HALT_CLEARED_AT none, Notes empty. Research: 6 theses 11-19, 0 accepted, 6 rejected; 288 lifetime IDs, 0 ever accepted.
prior_run: 2026-11-19 11:41 ET 3-midday-management — selftest 5/5 exit 0, first seat today with the market open, EXITS-ONLY, zero exits because §5 had no operand; ledger agreed 3rd time; first real session print gave core 68.93% in band and showed the two pre-market seats had overstated core by ~0.2pp and equity by ~$570, all mark.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.4983
satellite_pct: 0.0
cash_pct: 31.5017
open_thesis_ids: none
```

---

## Where things stand (2026-11-19 15:15 ET, **4-market-close-journal — PRE-CLOSE, hold in progress**)

**THIS RUN DOES NOT TRADE.** It journals and it stamps the §5.4 high-water marks. Today it had
**no mark to stamp**: zero satellite positions, so no `highest_close` exists to raise and no
`(as of …)` date to advance. ⚠ **Nothing is owed or deferred for 2026-11-19.**

⚠⚠ **THE FIRING TIME COLLIDES WITH THIS ROUTINE'S DEFINING JOB.** `clock` **15:15:51** —
`is_open: true`, `next_close` **2026-11-19T16:00**, `next_open` **2026-11-20T09:30**: **45 minutes
before the bell**, the **14th consecutive EST session** on the −1h shape. The routine exists to
run *after* the close so the marks have settled; **at 15:15 the `clock` gate is CLOSED and no
valid closing mark can be written at all.** The remedy — hold for the bell, confirm the post-bell
`clock` signature (`is_open: false` with **both** dates on the *next* session), pull the finished
bar after a settle — is the 11-18 procedure and it worked. ⚠ **It is a convention carried in these
files, not code.** **Today it costs nothing because the ledger is empty. The first satellite
position makes that convention the only thing between this firing time and a silently wrong
trailing stop.** ⚠ Per `control.md` the timing is **recorded, not diagnosed**.

**§5 RE-EVALUATED HERE, NOT INHERITED — ALL FOUR RULES ABSENT, NOT PASSING**: no invalidation
string (288 IDs, 0 accepted), no timing window, no entry price, no `highest_close`. **98th absent
seat, 81st absent date.** Core VOO is §5-exempt and was **struck from the working list, not
cleared.** **Zero positions at risk is the absence of a subject, not four clean bills of health.**

**LEDGER RECONCILED A FOURTH TIME TODAY AND IT AGREES.** Zero satellite blocks
(`grep -ci 'status: *open'` → 0) vs one Alpaca row, VOO 99.046311231 sh @ 706.74.

**§7 ORDER VERIFICATION — CLEAN.** `orders --status open` → `[]`. `orders --status all` → exactly
one order in this account's entire history (the 2026-09-03 core fill, `filled`, terminal).
**Nothing non-terminal overnight; nothing placed by any of today's four seats.**

**THE DAY, IN ONE LINE: a gap-up that fully reversed.** VOO **678.15** open (+1.0264% on 11-18's
671.26) → **679.99** high (+1.3005%) → **658.61** (−3.1442% off the high, −1.8845% on the day).
Account **−1.2986%** — cash at 31.5% damps the index move by about a third. **Share count
unchanged since 2026-09-03, cash exactly $30,000.00: all mark, no flow.**

**SLEEVES, PARTIAL BASIS:** equity **$95,232.89**; core **$65,232.89 = 68.4983%** / satellite
**0.00%** / cash **$30,000.00 = 31.5017%**. `core_in_band: true`, `rebalance_needed: false` —
**3.4983pp above the §2 65% floor. NO REBALANCE DUE 2026-11-20.** ⚠ `rebalance_delta` **1,430.13**
is a distance readout to the 70% target, **not an order**. ⚠ **Floor headroom has narrowed three
reads running: 3.9074pp (11-18 close) → 3.9300pp (11-19 midday) → 3.4983pp. The band is wide; it
is not getting wider.**

**Week anchor 2026-11-16 re-derived here with `isocalendar`** (2026-W47, weekday 4) — matches
`week_of`, **no reset**, cap **0 of 3**. Breaker **INACTIVE 0/3**, no alert owed or posted.
`control.md`: **`TRADING_ENABLED: true`, `HALT_CLEARED_AT: none`**, Notes empty.

## Carry forward

1. ⚠⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-19 was the **14th
   pre-bell firing** across 11-02 → 11-19 (only 11-13 at 10:43 landed mid-session; 11-16 did not
   fire). Sent out of band 11-12, re-sent 11-16. Re-send **only** if routine 2 begins firing
   *after* the bell in a way that changes what the human must fix. **Recorded, not diagnosed.**
   ⚠⚠ **THE STANDING COST: the only run licensed to open positions could execute on exactly ONE
   session in that stretch. IT HAS STILL NOT COST A TRADE** — every one of those plans carried
   zero intents. **Damage to date zero; exposure entirely forward-looking, and the first plan with
   a live intent that meets a pre-bell seat is the day it becomes expensive.**
   ⚠ **Routine 3's ~49-min-early firing is a DIFFERENT, HARMLESS case** — an early midday seat
   still lands *inside* the session, the only window an exits-only run needs.
   ⚠⚠ **ROUTINE 4's −45-min firing (NEW, this seat) is a THIRD case and its own severity:** a
   close seat *can* hold for the bell and did, so the cost is a 45-minute hold and the risk of a
   partial-basis publication — **not a missed window.** **Do not fold the three together.**
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` — that scoping error is what cost
   2026-11-13.** That seat's insurance commit carried `positions.md` and `state.md` only; when its
   second commit never landed, the two artifacts lost were **exactly the two it omitted**
   (`journal.md` and the ClickUp summary). 11-16/17/18 did it correctly. ✅ **Exercised correctly
   at this seat: journal entry written and committed PROVISIONALLY before the hold, `--summary-file`
   passed so a push failure rescues the summary into a ClickUp alert.**
3. ⚠⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "the worst session in this account's history" — false by a factor of two;
   11-17's 15:15 summary ranked off a partial and needed a correction comment on ClickUp
   `86bd4hbb1`. Ranking table in `journal.md` 2026-11-17. ⚠⚠ **THIS SEAT HAD TWO DRAFTED AND
   PUBLISHED NEITHER** — "2nd-worst of 55" sat **0.0244pp** from 11-16's −1.2742% and was live to
   flip; "lowest equity print in account history" needed a +1.3% rally to flip. **Third instance of
   one mistake, caught before it shipped.** Both ranked off the official close in `journal.md`.
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — STILL THE
   TWELFTH distinct instance.** `lastday_price` **671.31** vs official `bars` **671.26** for 11-18
   = **0.05 / 0.0074%**, identical at all four of today's seats. ⚠⚠ **A FOURTH OBSERVATION OF ONE
   INSTANCE IS NOT A NEW INSTANCE** — counting observations as instances inflates the very trend
   the human is asked to act on. Prior distinct instances ran **0.10–0.42**. ⚠ **A narrow instance
   is not a fixed instance**; the spread has narrowed and widened repeatedly and is **not** a
   dividend-basis artifact. **Build P&L and stamp `highest_close` from official `bars` closes only,
   one adjustment basis, one call.**
5. ⚠⚠ **THE IN-PROGRESS-BAR DEFECT — GATE EVERY `highest_close` WRITE ON `clock`, never on the
   shape, presence or apparent stability of the bar.** Demonstrated dynamically 11-18: the same
   dated bar pulled ~1 min apart gave **671.795 → 671.76**; after the bell, two pulls identical.
   **A finished bar does not move; an unfinished one carries NO FLAG saying so.**
   ⚠⚠⚠ **"PARTIALS READ LOW" IS DEAD — DO NOT RESURRECT IT AS A CORRECTION FACTOR.** 11-16 and
   11-17 read LOW; 11-18's read HIGH; **11-19's pre-market marks read HIGH by +0.845pp to
   +1.103pp.** The hazard is **variance, not bias**, and the only remedy is the `clock` gate.
   ⚠⚠ **THE SHARPEST DEMONSTRATION YET IS 2026-11-19, AND IT POINTS THE DANGEROUS WAY: the 07:01
   seat read VOO 679.67; the session HIGH was 679.99 — within 0.047% — and price closed ~3% below
   it.** A satellite `highest_close` stamped there would sit a hair under the top of the day and
   would move the §5.4 trigger ~3% closer **in the SELLING direction.** **Nothing protected the
   mechanism today except the empty ledger.**
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at the
   **98th** absent-seat ordinal. The first satellite position is their first live test. **All four
   §5 sell rules remain untested code paths** — nothing has ever closed, so every "no exits" entry
   in this corpus records the absence of a subject, not a clean bill of health.
7. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13: adjusted
   and unadjusted closes identical to the cent on 259 of 260 sessions, across all four VOO
   ex-dividend dates). **Any review using the flag's output understates the benchmark and flatters
   the agent.** True 12-month VOO total return is **+14.615%**.
8. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark. **A run cannot
   fix either 7 or 8.**
9. **STILL MISSING AND NOT RECOVERABLE:** the `journal.md` entry for **2026-11-13** and that day's
   ClickUp daily summary. The price leg was discharged (VOO 693.05, equity 98,644.05, core 69.59%,
   day −0.430%); **no seat has written, or should write, a backdated close-day narrative.**
10. ⚠⚠ **DO NOT MISREAD `delete-on-merge` AS A PUSH FAILURE.** An automation merges each session
   branch into `main` and **deletes the branch on merge**, so `git ls-remote --heads origin` shows
   your branch gone on every successful run and `git fetch origin <branch>` fails with
   `couldn't find remote ref` — while `commit.py` correctly reported `"pushed": true`.
   ⚠ **THE CORRECT CHECK IS `git merge-base --is-ancestor <sha> origin/main`.**
11. ⚠ **PATH LABEL.** The research archives live at **`archive/research_log/2026-09.md`** (87 IDs)
   and **`archive/research_log/2026-10.md`** (129 IDs). Earlier states abbreviated these as
   `archive/2026-09`, which **does not resolve as a path** — a seat pasting it under-counts by 216.
12. ⚠⚠ **THE PRICED-IN RULE IS UNDISCHARGED FOR 2026-11-19. KEEP IT VERBATIM:** *when the plan's
   catalyst broke after the prior close, the open seat is the first that can actually perform the
   priced-in test; re-run `move --sessions 5` after the open and treat the pre-market reading as
   UNPERFORMED, not passed.* 11-19's principal catalyst — the **Nvidia China Hopper export halt,
   first disclosed 2026-11-19** — broke after the 11-18 close; **the open seat meant to discharge
   it fired pre-bell with zero candidates, the midday seat held no intent, and this close seat
   writes no theses. No `move` call was made today at all.** **The rule remains live for the first
   seat that holds an intent on a post-close catalyst.**
   ⚠ Measured precedent in `research_log.md` ADDENDUM 2026-11-18: re-running thirteen names once a
   post-catalyst session had completed flipped **7 of 13 verdicts**; the eligible set went from
   **eight names to five**; **five names reading `false` that morning were already 4.5–14% LATE**,
   MU among them.
   ⚠ **STILL UNFIXED AND STILL NOT A LICENCE: the filter is magnitude-based and direction-blind**
   (`abs(move) > 4`). **NVDA read `true` on 11-19 by having FALLEN 13.22%.** "The filter is
   direction-blind, therefore buy the faller" is averaging into weakness in a costume, and §7
   forbids averaging down. For the human to fix in code; **no run may grant itself this override.**
13. ⚠⚠ **`move` ALSO READS THE IN-PROGRESS BAR — so item 5's defect reaches a §4 GATE, not just
   `highest_close`, and §4 decides whether a position is opened at all.** Found 11-18: run
   mid-session at ~15:25, `move --symbol NVDA --sessions 5` returned `to_close` **150.87** while the
   07:03 seat had read **155.49**, the 11-17 close — the window had silently rolled onto that day's
   unfinished bar. ⚠ **The gate is a convention, not code.** On 11-18 APH sat **0.22pp** and GEV
   **0.21pp** from the threshold. **Fix: gate the priced-in check on `clock` in code, exactly as
   `highest_close` is gated.**
14. ⚠⚠ **THE 288–0 AMBIGUITY, AND NO RUN CAN RESOLVE IT FROM THE INSIDE.** **288 thesis IDs, 0 ever
   accepted** — unchanged at this seat, which writes no theses. §4 is explicit that most research
   runs should correctly produce no trade, and 11-19's six kills were **stated by sources**, not
   constructed by the agent. **But "the gates are correctly rejecting weak candidates" and "these
   gates can never pass" now produce identical evidence from inside the system.** ⚠⚠ **A RUN MUST
   NOT LOOSEN A GATE TO TEST THIS.**
   ✅ **What the data DOES support, narrowly:** failures concentrate in **part 1 (mechanism)** and
   **part 2 (materiality)**, not in the priced-in filter or §3's thresholds. **Four of 11-19's six
   died because no second-order recipient was ever named by anybody.** If the human wants to tune
   §4, that is where to look.
   ⚠ **AND THE SCHEDULE FAULT CONFOUNDS THE COUNT:** the acceptance rate was measured over a
   stretch in which the executing seat could act on **one session in fourteen**. **288–0 is a
   research-gate statistic; it is not evidence about execution.**
15. ⚠ **THE TWO-PRICE DEFECT IS SOLVED AND IT IS A LIVE QUOTE MIDPOINT, NOT A FIXED OFFSET** —
   which is why the broker/official gap never had a stable size. A `positions.current_price` is an
   **intraday midpoint, not a close** (today: **658.635** against the bar's **658.61**). **Always
   `bars` for a close, a fresh `quote` for execution, NEVER a `positions` field for either.**
   Cosmetic on core; **load-bearing the moment a satellite position exists.**

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

**`positions.md` needs a retention rule from the human; no run has standing to truncate it.** It
and `weekly_review.md` are the majority of the whole live corpus, and `positions.md` describes an
**empty ledger**. **Neither is reachable by the monthly rollover** — `positions.md` is excluded on
the premise that it "only ever holds open positions", which has been false for 78 days. Full
write-up: `weekly_review.md`, week ending 2026-11-13, Recurring Error 1.
⚠⚠ **THIS SEAT MEASURED ITS OWN CONTRIBUTION RATHER THAN CLAIMING TO HAVE BEEN BRIEF:** its
`positions.md` digest added **1,717 B** — against 4,281 B (07:01), 4,183 B (08:36) and 3,299 B
(11:41), so **four seats of one empty day have cost 13,480 B of ledger describing nothing held.**
**Writing "deliberately short" does not make an addition free.** This seat **collapsed nothing in
`positions.md` and claims no collapse ratio** — a seat is not entitled to collapse prose other
seats wrote — and **the line count is the wrong instrument; every "collapsed N → M" figure in that
file is measured with it and at least one changed sign when measured in bytes.** Sizes for this
run are re-measured with `os.path.getsize` **after** its writes, below the final commit.

⚠ **Second standing item, same reviewer:** the agent-authored rejection taxonomy ("rule (iii)" …
"rule (viii)") carries the majority of the historical rejection load and **exists nowhere in
`strategy.md`**, so a reader cannot tell which rejections rest on the strategy and which rest on
rules the system wrote for itself. The 11-18 and 11-19 seats wrote their rejections in §3/§4's own
language instead. ⚠ **That is those seats' response to the ask, not a decision the human has made,
and it binds no later seat.** The choice is still theirs: **promote the taxonomy into §4, or rename
it so the distinction is visible from the page.**

⚠ **All three items remain with the human in `weekly_review.md`.**
