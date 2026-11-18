# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across eight runs.

```
last_run: 2026-11-18 11:41 ET 3-midday-management — selftest 5/5 exit 0. MARKET OPEN (`clock` 11:41:19 `is_open: true`) — first seat today that COULD have exited; ZERO open satellite positions, so §5.1–§5.4 had NO OPERAND (ABSENT, not passing), zero exits, zero `highest_close` backfills owed, no §5.1 Perplexity check owed. Exits-only run: opened nothing and did not look. Ledger reconciled four sides today, AGREES (positions 1 row VOO core · sleeves satellite count 0 · positions.md zero blocks). Core 68.83% in band (3.83pp to the 65% floor). Breaker INACTIVE 0/3, cap 0/3, week anchor 2026-11-16 matches, no reset. 93rd absent seat, 80th absent date. ⚠ Item 12's post-catalyst re-test STILL UNDISCHARGED — routine 3 cannot discharge it.
prior_run: 2026-11-18 08:35 ET 2-market-open-execution — ⚠ FIRED PRE-BELL (`is_open: false`), §7 skip, ZERO orders placed; plan dated today passed the staleness gate but carried ZERO intents, so it cost nothing.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 68.83
satellite_pct: 0.0
cash_pct: 31.17
open_thesis_ids: none
```

---

## Where things stand (2026-11-18 11:41 ET, **3-midday-management — MARKET OPEN, ZERO EXITS**)

**THE ONE THING THAT MATTERS ABOUT THIS RUN: nothing should have executed and nothing did.**
There is no exit that was owed and skipped, no stop that should have fired and didn't, and no
order left in a non-terminal state. `TRADING_ENABLED: true`, so this was **not** a dry run — a
`sell` would have been submitted for real. There was simply nothing to sell.

**Market OPEN, and that is the one thing this seat had that the two before it did not.** `clock`
**11:41:19** — `is_open: true`, `next_close` **2026-11-18T16:00:00-05:00**, `next_open`
**2026-11-19T09:30:00-05:00**. This is the **first seat today on a live market** and therefore the
first that *could* have placed an exit. ⚠ **Routine 3 is exits-only by its own prompt and may not
open a position. It did not, and it did not go looking for one** — the §4 path runs through
pre-market research and the 09:35 seat, always.

**§5 re-evaluated here, not inherited — ALL FOUR RULES ABSENT, NOT PASSING.** Zero open satellite
positions means **no entry price, no `highest_close`, no `timing_window` deadline and no
invalidation string exists**, so §5.1 invalidation, §5.2 time stop, §5.3 hard stop and §5.4
trailing stop each had **no operand**. That is not the same as passing, and it is written down the
long way because the two readings are indistinguishable in a summary.
- **Step 2 (high-water repair) had nothing to repair.** No `bars` backfill was owed and none was
  spent. The staleness comparison that this step exists to perform has still never run against a
  real mark.
- **No §5.1 Perplexity call was owed or made.** An invalidation condition that does not exist
  cannot be checked, and a news query with no thesis behind it is activity for its own sake.
- ⚠ **Core VOO is EXEMPT from §5** (§5, last line) and was removed from the working list rather
  than evaluated and passed.

**Ledger reconciled on three sides AT THIS SEAT and it AGREES** — `positions` exactly one row
(VOO core) · `sleeves` satellite **`count: 0`, value 0** · `positions.md` **zero** satellite
blocks under **Open positions**. **Fourth consecutive agreement today.** No discrepancy, so no
repair was owed and nothing was traded on top of a wrong ledger. **93rd absent seat, 80th absent
date** (today counted once).

**Account, INTRADAY BASIS:**
- **Equity $96,251.88** · core VOO **99.046311231 sh** @ 706.74, mark **668.898**, unrealised
  **−$3,748.11 / −5.354%**, intraday **−$425.11 / −0.638%** · cash exactly **$30,000.00** ·
  `trading_blocked: false`.
- **Sleeves: core 68.83% / satellite 0.00% / cash 31.17%.** `core_in_band: true`,
  `rebalance_needed: false` — **3.83pp of room to the §2 65% floor.** ⚠ `rebalance_delta: 1124.44`
  against `core_target_value: 67,376.32` is **a distance readout, not an order**, and a midday
  seat has no rebalance mandate in any case. Share count unchanged since the 2026-09-03 fill.
- ⚠⚠ **668.898 IS A LIVE INTRADAY MARK, NOT A CLOSE. Do not record it as one.** Its value is
  evidential: it is **not** the 675.00 that both pre-bell seats read bit-identically 92 minutes
  apart, which **confirms retroactively that 675.00 was a pre-market indication** and not a stale
  feed. **No `highest_close` was stamped and none was owed.**
- **OFFICIAL CLOSES: 11-11 698.25 · 11-12 696.04 · 11-13 693.05 · 11-16 680.36 · 11-17 672.80.**
- **Endpoint disagreement read a third time today, unchanged:** `lastday_price` **673.19** vs
  official `bars` **672.80** for 11-17 = **0.39 / 0.0580%**. **Ninth distinct instance.**

**Week rollover — re-derived here with `isocalendar`, not inherited.** 2026-11-18 → ISO
**2026-W47 wd 3**, Monday anchor **2026-11-16** = inherited `week_of`. They match, **no reset
due**, `new_positions_this_week` **0 of 3**.

Breaker **INACTIVE 0/3** · `halt_triggered_at: none` · `TRADING_ENABLED: true` ·
`HALT_CLEARED_AT: none` · `control.md` Notes **(none)** · `alerts.md` **no open incidents, none
systemic**. `trade_log.md` carries **one fill in this account's entire history** (2026-09-03 VOO
core) and **nothing unresolved**.

**NO NOTIFICATION WAS SENT BY THIS SEAT, AND THAT IS A DECISION.** The run found what it was set
up to catch — **nothing**. No stop breached, no exit owed, no order unverified, no incident open,
no alert owed. The one notification-shaped fact, routine 2's firing time, is the standing ask that
carry-forward item 1 says is **already with the human and must not be re-sent on a repeat**.
⚠ Re-pinging a standing item daily is how a human learns to ignore the channel.

## Carry forward

1. ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-02 → 11-12 fired
   08:35–08:47 (`is_open: false`); 11-13 fired 10:43 mid-session; **11-16 did not fire at all**;
   11-17 fired 08:36; **11-18 fired 08:35 — the ordinary pre-bell shape, now the eleventh such
   dispatch.** Sent out of band 11-12, re-sent 11-16. Re-send **only** if routine 2 begins firing
   consistently *after* the bell in a way that changes what the human must fix. **A repeat pre-bell
   firing is not new information.** ⚠ Per `control.md` this is **recorded, not diagnosed**.
   ⚠⚠ **THE STANDING COST IS WORTH STATING PLAINLY FOR THE HUMAN, SINCE IT IS NOW MEASURABLE:
   across 11-02 → 11-18, routine 2 has been able to execute on exactly ONE session (11-13, 10:43).
   On every other session the only run licensed to open positions was closed-market. IT HAS NOT YET
   COST A TRADE — every one of those plans carried zero intents — so the damage to date is zero and
   the exposure is entirely forward-looking.** The first plan with a live intent that meets a
   pre-bell seat is the day this becomes expensive.
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly the
   two it omitted**. **11-16, 11-17 and 11-18 did it correctly.**
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST.** 11-16's
   close seat published "the worst session in this account's history" and it was false by a factor
   of two. **Rank off a CLOSE, not a partial bar** — 11-17's 15:15 summary ranked off a partial and
   published "4th-worst of 53" when the official close made it 5th (corrected by comment on ClickUp
   task `86bd4hbb1`). Ranking table is in `journal.md` 2026-11-17, cheap to re-derive.
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — NINTH
   distinct instance.** Today: `lastday_price` **673.19** vs official `bars` **672.80** for 11-17 =
   **0.39 / 0.0580%** (read at both the 07:03 and 08:35 seats, identical). Prior: 11-17 post-bell
   **0.42 / 0.0624%** (widest), 11-17 intraday 0.10, 11-16 post-bell 0.27, 11-13 +0.33. **Not a
   dividend-basis artifact.** **Build P&L and stamp `highest_close` from official `bars` closes
   only, on one adjustment basis, one call.**
5. ⚠ **THE IN-PROGRESS-BAR DEFECT: gate every `highest_close` write on `clock`, never on the
   shape, presence or apparent stability of the bar.** 11-17 pulled the same dated bar twice two
   minutes apart with the market open and got **669.96 then 670.45**. The bar carries **no flag**.
   ⚠⚠ **That same run then published a corrupted ordinal off a partial bar forty minutes after
   writing the warning. Documenting the hazard is not the same as being protected from it.**
   ⚠ 11-17's and 11-16's partials all read LOW against the official close — **TWO SESSIONS IS NOT A
   RULE. Do not treat "partials read low" as a correction factor.**
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at the
   **93rd** absent-seat ordinal. The first satellite position will be their first live test.
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
   branch into `main` and **deletes the branch on merge**, so `git ls-remote --heads origin` will
   show your branch gone on every successful run and `git fetch origin <branch>` will fail with
   `couldn't find remote ref` — while `commit.py` correctly reported `"pushed": true`.
   ⚠ **THE CORRECT CHECK IS `git merge-base --is-ancestor <sha> origin/main`, NOT whether your
   branch still exists on the remote.** A seat that checks for its own branch may raise a false
   push-failure incident and put a bogus SYSTEMIC alert in front of the human.
11. ⚠ **PATH LABEL — affects anyone re-running the thesis grep.** The research archives live at
   **`archive/research_log/2026-09.md`** and **`archive/research_log/2026-10.md`**. Earlier states
   abbreviated these as `archive/2026-09` / `archive/2026-10`, which **does not resolve as a
   path** — a seat pasting it will silently get zero and under-count by 216.
12. ⚠⚠ **THE §4 PRICED-IN WINDOW IS BLIND TO A POST-CLOSE CATALYST — mechanically verified by the
   07:03 seat (thirteen `move` calls), full write-up in `research_log.md`
   `T-2026-11-18-01`/`-02`.** `move --sessions 5` reads the trailing five **completed** sessions;
   Nvidia reported **after** the 11-17 close, so every `priced_in` verdict that morning was computed
   on a window with **zero post-catalyst sessions**. **A `false` there means "no session has traded
   since this news," which is not a clearance.** Nine of thirteen names passed a test that could not
   fail. **OPERATIONAL RULE: when the plan's catalyst broke after the prior close, the open seat is
   the first that can actually perform the test — re-run `move --sessions 5` after the open and
   treat the pre-market reading as UNPERFORMED, not passed.**
   ⚠ **11:41 MIDDAY UPDATE: STILL UNDISCHARGED, AND BY A SEAT THAT COULD HAVE RUN THE TEST.** The
   first post-Nvidia session is trading now, so `move --sessions 5` would finally have a
   post-catalyst session in its window — but **routine 3 may not open a position, so a priced-in
   verdict at this seat decides nothing and was not spent.** The seat that owns the re-test is
   still the one that keeps firing before the bell. Zero BUY intents again today, so **zero
   realised cost; the exposure stays forward-looking.**
   ⚠⚠ **THIS SEAT COULD NOT DISCHARGE THAT HANDOFF AND DID NOT PRETEND TO.** It fired at 08:35,
   **before** the open, so `bars` still has **no 11-18 row** and the first post-catalyst session has
   still not traded. **With zero BUY intents it was moot anyway — nothing to revalidate.** But note
   the structural trap plainly, because it is the real content of items 1 and 12 together: **the
   seat that owns the post-catalyst re-test is the same seat that keeps firing before the bell.**
   ⚠ **SEPARATELY, AND DO NOT CONFLATE: the filter is magnitude-based and direction-blind**
   (`abs(move) > 4`; **SMCI read `priced_in: true` after FALLING 13.10%**). That is **for the human
   to fix in code, NOT a licence any run may grant itself to override a `true` verdict** — "the
   filter is direction-blind, therefore buy the one that fell 13%" is averaging into weakness in a
   costume, and §7 forbids averaging down.

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.32MB**, read by every run. **`positions.md` is ~337KB describing an empty
ledger** and `weekly_review.md` is 379KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has been
false for 77 days. **`positions.md` needs a retention rule from the human; no run has standing to
truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring Error 1.
⚠ This seat **claims no collapse ratio** and collapsed nothing — it appended one short block to an
open digest and rewrote the file it owns. **The line count is the wrong instrument and every
"collapsed N → M" figure in that file is measured with it.**

⚠ **Second standing item, same reviewer:** the agent-authored rejection taxonomy ("rule (iii)" …
"rule (viii)") carries the majority of the rejection load and **exists nowhere in `strategy.md`**,
so a reader cannot tell which rejections rest on the strategy and which rest on rules the system
wrote for itself. The 07:03 seat wrote all five of its rejections in §3/§4's own language instead.
⚠ **That is one seat's response to the ask, not a decision the human has made, and it binds no
later seat.** The choice is still theirs: **promote the taxonomy into §4, or rename it so the
distinction is visible from the page.**

⚠ **Both items remain with the human in `weekly_review.md`. This seat sent NO notification** —
see the decision recorded above.
