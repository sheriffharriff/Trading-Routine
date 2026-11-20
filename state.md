# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across thirteen runs.

```
last_run: 2026-11-20 07:01 ET 1-premarket-research — selftest 5/5 exit 0. FIVE theses, ZERO accepted, FIVE rejected (T-2026-11-20-01…-05); 293 lifetime IDs, 0 ever accepted. Plan dated 2026-11-20, ZERO BUY / ZERO SELL / ZERO REBALANCE intents. ⚠ NOT a halted or blocked day — every §6/§7 gate OPEN (breaker INACTIVE 0/3, cap 0 of 3, satellite 0.00% with $30,000 cash, TRADING_ENABLED true, Notes empty, alerts.md empty); the CANDIDATES blocked the trade, not the system. clock 07:02:16 is_open false with BOTH dates 2026-11-20 = pre-market full session, NOT a holiday; re-read 07:04:48 unchanged. Week anchor 2026-11-16 re-derived with isocalendar (2026-W47 wd 5), matches, no reset, cap 0 of 3 — done here because the Friday review has not yet run. Ledger reconciled, AGREES (0 satellite blocks vs 1 Alpaca row = core VOO 99.046311231 @ 706.74, §5-exempt, struck not cleared). §5 ABSENT ON ALL FOUR RULES, NOT PASSING — 99th absent seat, 82nd absent date; no per-name news check run or owed. §7 clean, no orders placed, nothing non-terminal. ⚠⚠ THE PRICED-IN GATE WAS ACTUALLY REACHED FOR THE FIRST TIME IN FIVE SESSIONS — and BOTH readings were true BY FALLING: BKR 48.85→46.67 −4.46%, AMKR 37.12→34.135 −8.04%, both clock-gated on the finished 11-19 bar. Carry-forward item 12's direction-blind filter, TWICE IN ONE RUN, one session after NVDA read true by falling 13.22%. NO override taken. ✅ Neither reading load-bearing — both names die on part 2/part 3, which precede the filter in §4's ordering. Funnel: 4 broad sweeps, 2 drill queries (BOTH source-killed), 1 market-cap query, 2 clock-gated move calls, 1 asset check (JNPR status inactive/tradable false = code-verified §3 kill), 2 clock reads. Sweep 4 asked only for explicitly-named second-order beneficiaries and returned "no qualifying case" across the whole window. Sleeves: close basis (VOO 658.05) equity 95,177.43, core 68.4799% IN BAND; 07:02 sleeves read 94,781.24 / 68.35% off a 654.05 MIDPOINT, also in band — NO REBALANCE. ⚠ Floor headroom narrowed a 6th read running to 3.35pp. Endpoint gap 13th distinct instance and NARROWEST ON RECORD: lastday_price 658.01 vs bars 658.05 = 0.04 / 0.0061%. positions.md digest added 1,943 B measured with stat AFTER the write (smallest of the recent seats; still not free).
prior_run: 2026-11-19 16:06 ET 4-market-close-journal — OFFICIAL CLOSE RECORDED, hold for the bell SUCCEEDED (fired 15:15, 45 min PRE-BELL, 14th consecutive EST session on the −1h shape); VOO close 658.05 pulled twice identical; Step 2 had NO OPERAND; equity 95,177.43, day −1.3561%, 2nd-worst of 55 sessions and the lowest close-basis equity print in account history, both RANKED OFF THE CLOSE; 6 theses all rejected; ClickUp 86bd5cb9c.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.4799
satellite_pct: 0.0
cash_pct: 31.5201
open_thesis_ids: none
```

⚠ **`core_pct` / `cash_pct` above are the CLOSE-BASIS figures** (official `bars` VOO 658.05 for
2026-11-19 — the last authoritative close). The 07:02 `sleeves` read gave **68.35% / 31.65%** off a
**654.05 pre-market midpoint**, which is **not a close**. **Both are inside §2's 65–75% band**, so
nothing turns on the choice today — but the basis is recorded rather than blended.

---

## Where things stand (2026-11-20 07:01 ET, **1-premarket-research — five theses, five rejected**)

**THIS RUN DOES NOT TRADE.** It researches and writes a plan; the 09:35 run executes it.
**`plan_today.md` is dated 2026-11-20 and carries ZERO intents of any kind.**

⚠ **THIS IS NOT A HALTED DAY AND NOT A BLOCKED DAY, AND THE TWO LOOK IDENTICAL FROM THE PLAN.**
Every §6 and §7 gate was **open**: breaker **INACTIVE 0/3**, weekly cap **0 of 3**, satellite
**0.00% deployed** with **$30,000.00** of cash, `TRADING_ENABLED: true`, `control.md` Notes
**(none)**, `alerts.md` open incidents **(none)**. **Nothing structural prevented a buy. The
candidates did.** That distinction is the whole content of a zero-intent day and must not be
collapsed.

**FIVE THESES, ZERO ACCEPTED.** `T-2026-11-20-01` BKR ← FERC's approval of Cheniere's Sabine Pass
Stage V (**part 2**, source-killed: no disclosed scope value, no segment, no derivable share; **part
3** independently; **priced-in** independently) · `-02` the NVIDIA memory/packaging supply base ←
supply commitments **$279B → $390B, +$111B** (**part 1**, source-killed: NVIDIA **names no memory
supplier** and **Micron has not confirmed NVIDIA as a customer**; **§3** kills AMKR at **~$8.9B**) ·
`-03` the own-results cluster KEYS/INTU/ROST (**part 1**: a condition, not a transaction) · `-04` the
macro/policy complex (**part 1**: no Company A) · `-05` a thirteen-item sweep (§3 / part 2 / no named
Company B, **two of them re-serves of already-disposed events**).

⚠⚠ **THE PRICED-IN GATE WAS ACTUALLY REACHED TODAY — the first time in five sessions — AND BOTH
READINGS WERE `true` BY HAVING FALLEN.** `clock`-gated at 07:04:48 on the finished 2026-11-19 bar:
**BKR 48.85 → 46.67, −4.46%**; **AMKR 37.12 → 34.135, −8.04%**. This is **carry-forward item 12's
direction-blind `abs(move) > 4` filter appearing twice in one run**, one session after NVDA read
`true` by falling 13.22%. **"The filter is direction-blind, therefore buy the faller" is averaging
into weakness in a costume; §7 forbids it. No override was taken and no run may grant itself one.**
✅ **And the readings were not load-bearing:** both names die on **part 2 / part 3**, which precede
the filter in §4's ordering. **Today is not a case of the priced-in threshold doing the killing.**

**§5 RE-EVALUATED HERE, NOT INHERITED — ALL FOUR RULES ABSENT, NOT PASSING.** No invalidation string
(293 IDs, 0 accepted), no timing window, no entry price, no `highest_close`. **99th absent seat, 82nd
absent date. No per-name Perplexity news check was run or owed: there is no name to check.** Core VOO
is §5-exempt and was **struck from the working list, not cleared.** **Zero positions at risk is the
absence of a subject, not four clean bills of health.**

**LEDGER RECONCILED AND IT AGREES.** Zero satellite blocks in `positions.md`
(`grep -ci 'status: *open'` → 0) vs one Alpaca row, VOO 99.046311231 sh @ 706.74.

**§7 ORDER VERIFICATION — CLEAN.** This seat placed nothing by design. Nothing non-terminal was
carried overnight; the account's entire order history remains the single 2026-09-03 core fill.

**SLEEVES — IN BAND ON BOTH BASES, NO REBALANCE QUEUED.** Close basis (`bars` VOO **658.05**, `n`
2,902, `v` 132,178): equity **$95,177.43**, core **$65,177.43 = 68.4799%**, cash **$30,000.00 =
31.5201%**. Pre-market `sleeves` at 07:02: equity **94,781.24**, core **68.35%**, cash **31.65%** —
⚠ built on `positions.current_price` **654.05**, a **midpoint**, not a close. `core_in_band: true`,
`rebalance_needed: false`. ⚠ `rebalance_delta` **1,565.63** is a distance readout to the 70% target,
**not an order** — §2 rebalances at the 65/75 band.
⚠ **FLOOR HEADROOM HAS NARROWED A SIXTH READ RUNNING:** 3.9074 → 3.9300 → 3.4983 → 3.4799 →
**3.35pp**. A sixth consecutive index down-session is driving it. §2 holds core permanently and does
not trade it on news; **the band is wide, but it is not getting wider.**

**NO NOTIFICATION WAS SENT, AND THAT IS DELIBERATE.** Selftest passed 5/5, no stop breached, no exit
owed, nothing unverified, no order non-terminal, no incident open in `alerts.md`, breaker inactive,
core in band on both bases, **zero positions at risk**, and the plan carries no intent for a human to
weigh. ⚠ **The candidates weighed and declined:** (a) **the direction-blind priced-in filter firing
twice in one run** is a real code defect, but it is **carry-forward item 12, already with the human**,
it **changed nothing today** (both names died on earlier gates), and it **cost no trade**; (b) **the
293–0 acceptance record** is a standing item in `weekly_review.md`, not a new event. ⚠ **Re-pinging a
standing item daily is how a human learns to ignore the channel.** Both are in the record for the
Friday review.

## Carry forward

1. ⚠⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 14 pre-bell firings
   across 11-02 → 11-19 (only 11-13 at 10:43 landed mid-session; 11-16 did not fire). Sent out of
   band 11-12, re-sent 11-16. Re-send **only** if routine 2 begins firing *after* the bell in a way
   that changes what the human must fix. **Recorded, not diagnosed** per `control.md`.
   ⚠⚠ **THE STANDING COST: the only run licensed to open positions could execute on roughly ONE
   session in that stretch. IT HAS STILL NOT COST A TRADE** — every plan in it carried zero intents,
   **including today's.** **Damage to date zero; exposure entirely forward-looking, and the first
   plan with a live intent that meets a pre-bell seat is the day it becomes expensive.**
   ⚠ **Routine 3's ~49-min-early firing is a DIFFERENT, HARMLESS case** — an early midday seat still
   lands *inside* the session. ⚠⚠ **Routine 4's −45-min firing is a THIRD case:** a close seat *can*
   hold for the bell and did on 11-18 and 11-19, so the cost is a hold and the risk of a
   partial-basis publication, **not a missed window. Do not fold the three together.**
   ⚠ **This routine (1) fires ~07:01 against a stated 08:00 — the most harmless case of all:** a
   pre-market research seat needs only to be before the open, and it was by 148 minutes.
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` — that scoping error is what cost 2026-11-13.**
   The 11-13 seat's insurance commit carried `positions.md` and `state.md` only; when its second
   commit never landed, the two artifacts lost were **exactly the two it omitted** (`journal.md` and
   the ClickUp summary). 11-16/17/18/19 did it correctly. **Applies to routine 4, not to this one.**
3. ⚠⚠ **DO NOT WRITE A SUPERLATIVE WITHOUT RANKING IT FIRST, AND RANK OFF A CLOSE, NOT A PARTIAL.**
   11-16 published "the worst session in this account's history" — false by a factor of two; 11-17's
   15:15 summary ranked off a partial and needed a correction comment on ClickUp `86bd4hbb1`. Ranking
   table in `journal.md` 2026-11-17. ✅ **11-19 held two drafts back and both turned out true off the
   close — but the rank-2 margin moved 0.0244pp → 0.0819pp while it held, IN ITS FAVOUR; nine basis
   points the other way and the claim would have been false. The hold is what made it safe, not the
   answer.** ✅ **This seat published one ranked claim — "the priced-in gate was reached for the
   first time in five sessions" — and verified it against the 11-16/17/18/19 run totals, each of
   which states that no candidate reached the gate.**
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — now the
   THIRTEENTH distinct instance, and the NARROWEST ON RECORD.** `lastday_price` **658.01** vs
   official `bars` **658.05** for 2026-11-19 = **0.04 / 0.0061%**, beating 11-18's 0.05 / 0.0074%.
   Prior distinct instances ran **0.10–0.42**. ⚠ **A new session is a new instance; this is not a
   re-observation of the twelfth.** ⚠ **A narrow instance is not a fixed instance** — the spread has
   narrowed and widened repeatedly and is **not** a dividend-basis artifact. **Build P&L and stamp
   `highest_close` from official `bars` closes only, one adjustment basis, one call.**
5. ⚠⚠ **THE IN-PROGRESS-BAR DEFECT — GATE EVERY `highest_close` WRITE ON `clock`, never on the shape,
   presence or apparent stability of the bar.** Demonstrated dynamically 11-18 (same dated bar ~1 min
   apart: 671.795 → 671.76) and again 11-19 (15:15 bar `c` 658.61 / `n` 2,302 vs finished 658.05 /
   2,902 — **HIGH by +0.0851% with a quarter of the session's trades unprinted**). **A finished bar
   does not move; an unfinished one carries NO FLAG saying so.**
   ⚠⚠⚠ **"PARTIALS READ LOW" IS DEAD — DO NOT RESURRECT IT AS A CORRECTION FACTOR.** 11-16 and 11-17
   read LOW; 11-18 and 11-19 read HIGH. **The hazard is variance, not bias, and the only remedy is
   the `clock` gate.** ⚠⚠ **Sharpest demonstration on record is 2026-11-19 and it points the
   dangerous way: the 07:01 seat read VOO 679.67; the session HIGH was 679.99 — within 0.047% — and
   the official close was 658.05, 3.2855% BELOW that morning mark.** A satellite `highest_close`
   stamped there would move the §5.4 trigger **3.3% closer in the SELLING direction.** ⚠ **Nothing
   protected the mechanism except the empty ledger.** ✅ **This seat stamped no mark — none was owed.**
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at the
   **99th** absent-seat ordinal. **All four §5 sell rules remain untested code paths** — nothing has
   ever closed, so every "no exits" entry in this corpus records the absence of a subject, not a
   clean bill of health.
7. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13: adjusted
   and unadjusted closes identical to the cent on 259 of 260 sessions, across all four VOO
   ex-dividend dates). **Any review using the flag's output understates the benchmark and flatters
   the agent.** True 12-month VOO total return is **+14.615%**.
8. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core sleeve
   is structurally short ~1.07%/yr against any honest total-return benchmark. **A run cannot fix
   either 7 or 8.**
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
12. ⚠⚠ **THE PRICED-IN RULE — KEEP IT VERBATIM:** *when the plan's catalyst broke after the prior
   close, the open seat is the first that can actually perform the priced-in test; re-run
   `move --sessions 5` after the open and treat the pre-market reading as UNPERFORMED, not passed.*
   ⚠ **MOOT FOR TODAY'S TWO NAMES, NOT DISCHARGED:** today's catalysts broke during or after the
   11-19 session, so the window **does** contain a post-catalyst finished bar — and a `true` reading
   is the conservative direction anyway. **The rule stays live for the first seat that holds an
   intent on a post-close catalyst.** Measured precedent in `research_log.md` ADDENDUM 2026-11-18:
   re-running thirteen names after a completed post-catalyst session **flipped 7 of 13 verdicts**;
   the eligible set went from **eight names to five**; **five names reading `false` that morning were
   already 4.5–14% LATE**, MU among them.
   ⚠⚠ **STILL UNFIXED, AND IT FIRED TWICE TODAY: the filter is magnitude-based and DIRECTION-BLIND**
   (`abs(move) > 4`). **BKR read `true` by falling 4.46% and AMKR by falling 8.04%**, one session
   after **NVDA read `true` by falling 13.22%**. **Three direction-blind readings in two sessions.**
   **"The filter is direction-blind, therefore buy the faller" is averaging into weakness in a
   costume, and §7 forbids averaging down. For the human to fix in code; no run may grant itself
   this override.**
13. ⚠⚠ **`move` ALSO READS THE IN-PROGRESS BAR — so item 5's defect reaches a §4 GATE, not just
   `highest_close`, and §4 decides whether a position is opened at all.** Found 11-18: run
   mid-session at ~15:25, `move --symbol NVDA --sessions 5` returned `to_close` **150.87** while the
   07:03 seat had read **155.49** — the window had silently rolled onto that day's unfinished bar.
   ⚠ **The gate is a convention, not code.** ✅ **Applied correctly at this seat: `clock` re-read at
   07:04:48 (`is_open: false`, both dates 2026-11-20) immediately before both `move` calls, so each
   five-session window provably ended on the finished 2026-11-19 bar.** **Fix: gate the priced-in
   check on `clock` in code, exactly as `highest_close` is gated.**
14. ⚠⚠ **THE AMBIGUITY IS NOW 293–0, AND NO RUN CAN RESOLVE IT FROM THE INSIDE.** **293 thesis IDs,
   0 ever accepted.** §4 is explicit that most research runs should correctly produce no trade, and
   today's three substantive kills were **stated by sources**, not constructed by the agent. **But
   "the gates are correctly rejecting weak candidates" and "these gates can never pass" still
   produce identical evidence from inside the system.** ⚠⚠ **A RUN MUST NOT LOOSEN A GATE TO TEST
   THIS.**
   ✅ **What today adds, narrowly and usefully for the human:** `T-2026-11-20-02` is the **largest and
   best-shaped second-order setup in this corpus** — a named, US-listed Company A (**NVIDIA**)
   disclosing **$111B** of *new* multi-year component commitments — and it fails **not on a
   threshold** but because **every entity actually named as a recipient is foreign-listed or below
   the $10B floor, and the primary sources explicitly decline to name the memory suppliers at all.**
   **That is a property of US disclosure practice, not of §4's numbers.**
   ✅ **Failures still concentrate in part 1 (mechanism) and part 2 (materiality)**, not in the
   priced-in filter or §3's thresholds — **four of five died there today, matching 11-19's finding.**
   **If the human wants to tune §4, that is where to look.**
   ⚠ **AND THE SCHEDULE FAULT CONFOUNDS THE COUNT:** the acceptance rate was measured over a stretch
   in which the executing seat could act on about **one session in fifteen**. **293–0 is a
   research-gate statistic; it is not evidence about execution.**
15. ⚠ **THE TWO-PRICE DEFECT IS SOLVED AND IT IS A LIVE QUOTE MIDPOINT, NOT A FIXED OFFSET** — which
   is why the broker/official gap never had a stable size. A `positions.current_price` is an
   **intraday midpoint, not a close**; after the bell it is an **after-hours** midpoint; **pre-market
   it is a pre-market midpoint** — today it read **654.05** against the 11-19 official close
   **658.05**, **−4.00**. ⚠⚠ **`alpaca.py sleeves` IS BUILT ON THAT FIELD**, so its 07:02 output
   (equity **94,781.24**, core **68.35%**) sat **$396.19 and 0.13pp** off the close basis
   (**95,177.43**, **68.4799%**) — **a wider divergence than the post-bell case, because pre-market
   quotes are thinner.** **Always `bars` for a close, a fresh `quote` for execution, NEVER a
   `positions` field or `sleeves` for a close-basis figure.** Cosmetic on core; **load-bearing the
   moment a satellite position exists.**

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

**`positions.md` needs a retention rule from the human; no run has standing to truncate it.** It and
`weekly_review.md` are the majority of the whole live corpus, and `positions.md` describes an **empty
ledger**. **Neither is reachable by the monthly rollover** — `positions.md` is excluded on the premise
that it "only ever holds open positions", which has been false for 79 days. Full write-up:
`weekly_review.md`, week ending 2026-11-13, Recurring Error 1.
⚠⚠ **THIS SEAT MEASURED ITS OWN CONTRIBUTION RATHER THAN CLAIMING TO HAVE BEEN BRIEF**, with
`stat -c%s` **after** the write: its `positions.md` digest added **1,943 B** — the smallest of the
recent run (4,281 / 4,183 / 3,299 / 3,120 B for 11-19's four seats), **and still not free.** The
file is now **366,081 B** describing nothing held. **Writing "deliberately short" does not make an
addition free.** This seat **collapsed nothing and claims no collapse ratio** — a seat is not
entitled to rewrite prose other seats wrote — and **the line count is the wrong instrument; every
"collapsed N → M" figure in that file is measured with it and at least one changed sign when measured
in bytes.** Post-write sizes: `positions.md` **366,081 B**, `research_log.md` **308,066 B** (up from 277,815 B, i.e. **+30,251 B**
for five thesis entries and the funnel — ⚠ the insert script reported 29,831 which was a CHARACTER count, not bytes; the ⚠ and — glyphs this corpus uses are multibyte, so every char-count size claim in these files understates the real cost), `plan_today.md` **11,108 B** (a full overwrite, not an
append), `state.md` **DOWN from the inherited 23,815 B** — a real reduction. ⚠ **The exact post-write size is deliberately NOT written here, and that is the finding, not an evasion:** three attempts to state it gave **22,619 → 22,760 → 22,968 B**, because each one was measured before the sentence reporting it was inserted. **A self-referential size claim cannot be both exact and true.** The measured figure is in this run's output and in the commit; the figures above are quoted for files this seat does not describe inside themselves.

⚠ **Second standing item, same reviewer:** the agent-authored rejection taxonomy ("rule (iii)" …
"rule (viii)") carries the majority of the historical rejection load and **exists nowhere in
`strategy.md`**, so a reader cannot tell which rejections rest on the strategy and which rest on
rules the system wrote for itself. The 11-18, 11-19 and **this** seat wrote their rejections in §3/§4's
own language instead. ⚠ **That is three seats' response to the ask, not a decision the human has
made, and it binds no later seat.** The choice is still theirs: **promote the taxonomy into §4, or
rename it so the distinction is visible from the page.**

⚠ **All three items remain with the human in `weekly_review.md`.** ⚠ **Today is Friday: routine 5
runs next and is the seat that owns the monthly rollover and this ask.**
