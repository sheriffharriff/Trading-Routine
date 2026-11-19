# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across nine runs.

```
last_run: 2026-11-19 07:01 ET 1-premarket-research — selftest 5/5 exit 0. Market OPEN today (clock 07:01:46, is_open false + BOTH dates 11-19 = pre-market, not a holiday). Ledger reconciled, AGREES (zero satellite both sides; one Alpaca row = core VOO). §5.1-§5.4 ABSENT (no operand), 95th absent seat, 81st absent date. Week anchor 2026-11-16 re-derived, matches, no reset, cap 0 of 3. Breaker INACTIVE 0/3. Core 69.17% in band (4.17pp to floor) — ⚠ ON A PRE-MARKET MARK, 679.67 vs the 671.26 official close, a +1.253% gap; open seat must re-read sleeves. NO REBALANCE DUE. Research: 6 theses, ALL REJECTED (T-2026-11-19-01..06); running total 288 IDs, 0 ever accepted. Four of six died because NO second-order recipient was named by anybody — part 1/part 2, not the priced-in filter. Both drill queries returned a SOURCE-STATED kill. plan_today.md dated 2026-11-19, ZERO intents of any kind. ⚠ Priced-in window is PRE-EVENT again (Nvidia China halt disclosed 11-19) — cost nothing, no candidate reached that gate. ⚠ Endpoint disagreement 12th instance, narrowest yet (0.05 / 0.0074%). NO notification sent — deliberate.
prior_run: 2026-11-18 16:05 ET 4-market-close-journal — hold for the bell succeeded, official close VOO 671.26, equity 96,485.83, core 68.91%, 0 trades, 5 theses all rejected, item 12 discharged.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.17
satellite_pct: 0.0
cash_pct: 30.83
open_thesis_ids: none
```

---

## Where things stand (2026-11-19 07:01 ET, **1-premarket-research — six theses, six rejected, a plan with zero intents**)

**Market is open today.** `clock` **07:01:46** — `is_open: false` with **both** `next_open` and
`next_close` carrying **2026-11-19**. ⚠ **Read off the DATES, not the boolean: FALSE has three
meanings (pre-market, post-bell, holiday), TRUE has one.** Thursday, an ordinary full session.
Re-read at **07:04:37** before the single `move` call — same signature.

**Account, PRE-MARKET BASIS — and the basis matters more than usual today.** Equity
**$97,318.81** (99.046311231 sh + $30,000.00 cash) against the 11-18 close basis
**$96,485.83**. ⚠⚠ **THE ENTIRE $832.98 DIFFERENCE IS THE MARK, NOT A FLOW:**
`positions.current_price` is **679.67** against the official 11-18 close of **671.26**, a
**+1.253%** pre-market gap on thin volume. **Cash is exactly $30,000.00 and the share count is
unchanged since the 2026-09-03 fill.** `trading_blocked: false`.
- **Sleeves: core 69.17% / satellite 0.00% / cash 30.83%.** `core_in_band: true`,
  `rebalance_needed: false`, **4.17pp to the §2 65% floor, 5.83pp to the ceiling. NO REBALANCE
  DUE.** ⚠ `rebalance_delta: 804.36` is **a distance readout to the 70% target, not an order** —
  §2 only requires closing that gap once the band is **breached**.
- ⚠ **THE OPEN SEAT MUST RE-READ `sleeves` ON A REAL SESSION PRINT.** A sleeve percentage
  computed off a pre-market quote is the one number in this block most likely to be wrong by the
  time anyone can act on it.
- **OFFICIAL CLOSES: 11-13 693.05 · 11-16 680.36 · 11-17 672.80 · 11-18 671.26** (`bars`, 11-18
  bar confirmed `n` 2,671 / `v` 88,905 — identical to the close seat's stamp, and **no 11-19 row
  exists** at this hour, which is what makes the window below pre-event).
- ⚠ **Endpoint disagreement, TWELFTH instance — and the NARROWEST yet, which is not a fix:**
  `lastday_price` **671.31** vs official `bars` **671.26** = **0.05 / 0.0074%**. Prior instances
  ran **0.10–0.42**. **The spread has narrowed and widened before, and §5.4 still reads from the
  endpoint that is wrong. Build P&L from `bars` closes only.**

**§5 re-evaluated at this seat, not inherited — ALL FOUR RULES ABSENT, NOT PASSING.** Zero
satellite positions means no entry price, no `highest_close`, no deadline and no invalidation
string exists. **Step 4 had NO OPERAND: no mark to raise, no `(as of …)` date to advance, and no
per-name news check was run or owed because there is no name. 95th absent seat, 81st absent
date.** Core VOO is §5-exempt and was struck from the working list, not cleared. **Ledger
reconciled both sides, AGREES:** `positions.md` lists zero satellite positions and
`alpaca.py positions` returns one row, the core. Breaker **INACTIVE 0/3**, no alert owed or
posted. Week anchor **2026-11-16** re-derived with `isocalendar` (**2026-W47 weekday 4**),
**matches, no reset**, cap **0 of 3**.

**Research: 6 theses, ALL REJECTED** (`T-2026-11-19-01` … `-06`). Running total **288 thesis
IDs, 0 ever accepted** (72 live + 87 + 129; counted after the write, `grep -c '^### T-2026'`,
and `grep -c '^### T-2026.*ACCEPTED'` = 0 in all three files).
⚠⚠ **EVERY §6/§7 GATE WAS OPEN TODAY — breaker inactive, cap 0 of 3, satellite 0% deployed,
$30,000 cash, `TRADING_ENABLED: true`, `control.md` Notes (none). NOTHING STRUCTURAL BLOCKED A
BUY. THE CANDIDATES DID.** Those two cases produce an identical-looking empty plan and must
never be conflated: one is a system state, the other is a research outcome.
**Where the six died:** part 1 ×3 · part 2 ×1 (source-killed) · §3 + part 1 ×1 · sweep ×1.
✅ **The narrow, useful finding: four of the six died because NO second-order recipient was ever
named by anybody.** That is a property of the available news flow, not of §4's thresholds — and
it is the first thing to check if the human ever wants to tune the gates. **Not one candidate
reached the priced-in gate**, so today's pre-event window cost nothing.

**NO NOTIFICATION WAS SENT, AND THAT IS A DELIBERATE DECISION.** No stop breached, no exit
owed, no order unverified, no incident open, no alert owed, breaker inactive, core in band,
**zero positions at risk**, and the plan carries zero intents. The standing items below **are**
worth the human's attention but are **code and policy decisions with zero market exposure**, and
they are already with the human in `weekly_review.md`. ⚠ **Re-pinging a standing item daily is
how a human learns to ignore the channel** — and the routine-2 schedule ask is explicitly
**already with the human and must not be re-sent.**

## Carry forward

1. ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-02 → 11-12 fired
   08:35–08:47 (`is_open: false`); 11-13 fired 10:43 mid-session; **11-16 did not fire at all**;
   11-17 fired 08:36; 11-18 fired 08:35. Sent out of band 11-12, re-sent 11-16. Re-send **only**
   if routine 2 begins firing consistently *after* the bell in a way that changes what the human
   must fix. **A repeat pre-bell firing is not new information.** ⚠ Per `control.md` this is
   **recorded, not diagnosed.**
   ⚠⚠ **THE STANDING COST, STATED PLAINLY BECAUSE IT IS MEASURABLE: across 11-02 → 11-18,
   routine 2 could execute on exactly ONE session (11-13, 10:43).** On every other session the
   only run licensed to open positions was closed-market. **IT HAS NOT YET COST A TRADE — every
   one of those plans carried zero intents, and so does today's — so the damage to date is zero
   and the exposure is entirely forward-looking.** The first plan with a live intent that meets a
   pre-bell seat is the day this becomes expensive.
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly
   the two it omitted.** **11-16, 11-17 and 11-18 did it correctly.**
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST, AND
   RANK OFF A CLOSE, NOT A PARTIAL BAR.** 11-16's close seat published "the worst session in this
   account's history" and it was false by a factor of two; 11-17's 15:15 summary ranked off a
   partial, published "4th-worst of 53" when the close made it 5th, and needed a correction
   comment on ClickUp task `86bd4hbb1`. Ranking table is in `journal.md` 2026-11-17, cheap to
   re-derive. **No superlative was written today — the day was not ranked, because a pre-market
   seat has no session to rank.**
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — TWELFTH
   distinct instance.** Today: `lastday_price` **671.31** vs official `bars` **671.26** for 11-18
   = **0.05 / 0.0074%**, **the narrowest reading yet.** Prior: 11-18 post-bell 0.27, 11-17
   post-bell 0.42 (widest), 11-17 pre-market 0.39, 11-17 intraday 0.10, 11-16 post-bell 0.27,
   11-13 +0.33. ⚠⚠ **A NARROW INSTANCE IS NOT A FIXED INSTANCE AND MUST NOT BE READ AS ONE** —
   the spread has narrowed and widened repeatedly and is **not** a dividend-basis artifact.
   **Build P&L and stamp `highest_close` from official `bars` closes only, on one adjustment
   basis, in one call.**
5. ⚠⚠ **THE IN-PROGRESS-BAR DEFECT — GATE EVERY `highest_close` WRITE ON `clock`, never on the
   shape, presence or apparent stability of the bar.** Demonstrated **dynamically** on 11-18: the
   same dated bar pulled ~1 min apart gave **671.795 → 671.76**; after the bell it was pulled
   twice and was **identical** (671.26, n 2,671, v 88,905).
   ✅ **Re-confirmed from the other direction today:** the 11-18 bar pulled at this seat is
   byte-identical to the close seat's stamp, **because the session is finished.** **A finished bar
   does not move; an unfinished one carries NO FLAG saying so.**
   ⚠⚠⚠ **"PARTIALS READ LOW" IS DEAD — DO NOT RESURRECT IT AS A CORRECTION FACTOR.** 11-16 and
   11-17 read LOW; **11-18's partials read HIGH (+0.535 / +0.0797%).** **Three sessions, two
   directions.** The hazard is **variance, not bias**, and the only remedy is the `clock` gate.
   ⚠ **The HIGH direction is the dangerous one for §5.4:** it ratchets `highest_close` UP off a
   price that never traded, so the trailing stop fires early — **the SELLING direction.**
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the **95th** absent-seat ordinal. The first satellite position will be their first live test.
7. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13:
   adjusted and unadjusted closes identical to the cent on 259 of 260 sessions, across all four
   VOO ex-dividend dates). **Any review using the flag's output understates the benchmark and
   flatters the agent.** True 12-month VOO total return is **+14.615%**.
8. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark. **A run
   cannot fix either 7 or 8.**
9. **STILL MISSING AND NOT RECOVERABLE:** the `journal.md` entry for **2026-11-13** and that
   day's ClickUp daily summary. The price leg was discharged (VOO 693.05, equity 98,644.05, core
   69.59%, day −0.430%); **no seat has written, or should write, a backdated close-day
   narrative.**
10. ⚠⚠ **DO NOT MISREAD `delete-on-merge` AS A PUSH FAILURE.** An automation merges each session
   branch into `main` and **deletes the branch on merge**, so `git ls-remote --heads origin` will
   show your branch gone on every successful run and `git fetch origin <branch>` will fail with
   `couldn't find remote ref` — while `commit.py` correctly reported `"pushed": true`.
   ⚠ **THE CORRECT CHECK IS `git merge-base --is-ancestor <sha> origin/main`, NOT whether your
   branch still exists on the remote.** A seat that checks for its own branch may raise a false
   push-failure incident and put a bogus SYSTEMIC alert in front of the human.
11. ⚠ **PATH LABEL — affects anyone re-running the thesis grep.** The research archives live at
   **`archive/research_log/2026-09.md`** (87 IDs) and **`archive/research_log/2026-10.md`** (129
   IDs). Earlier states abbreviated these as `archive/2026-09` / `archive/2026-10`, which **does
   not resolve as a path** — a seat pasting it will silently get zero and under-count by 216.
12. ⚠⚠ **THE PRICED-IN WINDOW WAS PRE-EVENT AGAIN TODAY, AND THE OPERATIONAL RULE IS THE ONLY
   THING THAT PREVENTS THE ERROR. KEEP IT VERBATIM:** *when the plan's catalyst broke after the
   prior close, the open seat is the first that can actually perform the priced-in test; re-run
   `move --sessions 5` after the open and treat the pre-market reading as UNPERFORMED, not
   passed.* Today's principal catalyst — **the Nvidia China Hopper export halt, first disclosed
   2026-11-19** — broke after the 11-18 close, and `bars` returns **no 11-19 row**, so any
   pre-market `priced_in: false` is again an artifact of a pre-event window.
   ✅ **It cost nothing today: NOT ONE candidate reached the priced-in gate** — part 1, part 2 and
   §3 precede it in §4's ordering and disposed of all six.
   ⚠ **The measured precedent is in `research_log.md` ADDENDUM 2026-11-18:** re-running thirteen
   names once a post-catalyst session had completed flipped **7 of 13 verdicts**; the eligible set
   went from **eight names to five**; **five names that read `false` that morning were already
   4.5–14% LATE**, including MU, the only name in that sweep to clear part 1.
   ⚠ **STILL UNFIXED AND STILL NOT A LICENCE: the filter is magnitude-based and
   direction-blind** (`abs(move) > 4`). **NVDA reads `true` today by having FALLEN 13.22%.** "The
   filter is direction-blind, therefore buy the faller" is averaging into weakness in a costume,
   and **§7 forbids averaging down.** For the human to fix in code; **no run may grant itself this
   override.**
13. ⚠⚠ **`move` ALSO READS THE IN-PROGRESS BAR — so item 5's defect reaches a §4 GATE, not just
   `highest_close`, and §4 decides whether a position is opened at all.** Found 11-18: run
   mid-session at ~15:25, `move --symbol NVDA --sessions 5` returned `to_close` **150.87** while
   the 07:03 seat had read **155.49**, the 11-17 close — **the window had silently rolled onto
   that day's unfinished bar.**
   ✅ **THE GATE WORKS WHEN APPLIED, DEMONSTRATED TODAY:** `clock` was read at **07:04:37**
   (`is_open: false`, both dates 11-19) **before** this seat's single call, so the window provably
   ended on a finished bar — `move --symbol NVDA --sessions 5` → **173.85 → 150.86, −13.22%**,
   matching the 11-18 post-bell reading (**150.87 / −13.22%**) **to a cent.**
   ⚠ **But the gate is a convention, not code.** On 11-18 APH sat **0.22pp** and GEV **0.21pp**
   from the threshold; on a day a candidate sits that close, a seat that forgets the gate decides
   a trade on a bar that has not finished. **Fix: gate the priced-in check on `clock` in code,
   exactly as `highest_close` is gated.**
14. ⚠⚠ **NEW ON 2026-11-19 — THE 288–0 AMBIGUITY, AND NO RUN CAN RESOLVE IT FROM THE INSIDE.**
   **288 thesis IDs, 0 ever accepted.** §4 is explicit that most research runs should correctly
   produce no trade, and today is a clean example of the gates working as designed: the kills were
   **stated by sources**, not constructed by the agent, and no trade was wrongly skipped. **But
   "the gates are correctly rejecting weak candidates" and "these gates can never pass" now
   produce identical evidence from inside the system, and 288–0 is a long enough run that the
   distinction matters.** ⚠⚠ **A RUN MUST NOT LOOSEN A GATE TO TEST THIS** — that is the exact
   failure §4's honest-broker rule exists to prevent, and only the human can change `strategy.md`.
   ✅ **What the data DOES support, narrowly:** the failures concentrate in **part 1 (mechanism)
   and part 2 (materiality)**, not in the priced-in filter or §3's thresholds. **Four of today's
   six died because no second-order recipient was ever named by anybody.** If the human wants to
   tune §4, that is where to look — and the §4 question *"whose economics change that the market
   is not looking at?"* may simply be one that routine news flow rarely answers with a **named**
   company.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus **1,185,015 B = 1.13 MiB** across the ten live files, read by every run —
⚠ **re-measured at this seat with `os.path.getsize` AFTER this run's writes, not inherited.** The
prior state recorded **1,158,846 B**, so **this run added 26,169 B.**
**`positions.md` is 353,407 B and `weekly_review.md` is 379,023 B — the two of them are 62% of
the whole corpus**, and `positions.md` describes an **empty ledger**. **Neither is reachable by
the monthly rollover** — `positions.md` is excluded on the premise that it "only ever holds open
positions", which has been false for 78 days. **`positions.md` needs a retention rule from the
human; no run has standing to truncate it.** Full write-up: `weekly_review.md`, week ending
2026-11-13, Recurring Error 1.
⚠⚠ **AND THIS SEAT MEASURED ITS OWN CONTRIBUTION RATHER THAN CLAIMING TO HAVE BEEN BRIEF:** its
`positions.md` digest added **4,281 B** to the file that *is* the finding. **Writing "deliberately
short" does not make an addition free.** This seat **collapsed nothing and claims no collapse
ratio** — and **the line count is the wrong instrument; every "collapsed N → M" figure in that
file is measured with it and at least one of them changed sign when measured in bytes.**

⚠ **Second standing item, same reviewer:** the agent-authored rejection taxonomy ("rule (iii)" …
"rule (viii)") carries the majority of the historical rejection load and **exists nowhere in
`strategy.md`**, so a reader cannot tell which rejections rest on the strategy and which rest on
rules the system wrote for itself. **The 11-18 and 11-19 seats both wrote all of their rejections
in §3/§4's own language instead, naming prior findings by date and content.**
⚠ **That is two seats' response to the ask, not a decision the human has made, and it binds no
later seat.** The choice is still theirs: **promote the taxonomy into §4, or rename it so the
distinction is visible from the page.**

⚠ **All three items remain with the human in `weekly_review.md`. This seat sent NO notification**
— see the decision recorded above.
