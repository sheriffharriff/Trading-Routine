# Today's Plan

**AGENT-OWNED. Written by the pre-market routine, consumed by the market-open routine,
overwritten daily.**

This file is the handoff between the two runs. The pre-market run does the thinking and
writes intents here; the market-open run executes them. Nothing gets bought that was not
written here first, which is what forces every buy to sleep on a written thesis instead of
being reasoned into existence at the moment of execution.

The market-open run **re-validates every intent against fresh quotes before acting**. An
intent written at 08:00 can be dead by 09:35 — an overnight gap can push a candidate past
the §4 4%-in-five-sessions priced-in threshold, in which case the trade is skipped and the
skip is logged. A stale intent is a proposal, not an instruction.

---

## Status

`plan_date` is load-bearing, not a comment. The market-open routine compares it to today's
ET date and **refuses to execute any intent from a plan not dated today** — it logs the
stale plan, posts an alert, and proceeds to the core/rebalance section only.

If the pre-market run failed, was skipped, or crashed before writing, this file still holds
yesterday's intents. Executing them would be running stale research as though it were
fresh — the candidate has had another full session to move, and the §4 priced-in check that
cleared it was performed against prices that no longer exist. Doing nothing is strictly
better. Core and rebalance actions are exempt from the gate because neither depends on the
day's research.

```
plan_date: 2026-10-16
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-16 at 09:30 ET** (`alpaca.py clock` at 08:13:02 ET: `is_open:
false`, `next_open: 2026-10-16T09:30:00-04:00`, `next_close: 2026-10-16T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both** `next_open`
and `next_close` carry **today's** date, which is the full-session signature rather than an
early close or a holiday. ⚠ **Read off the DATES, not the boolean.** The boolean is `false`
at 08:13 on every ordinary trading morning.

---

## Tape context

**Pre-flight selftest: 5/5** (env · Alpaca ACTIVE `trading_blocked=False` · Perplexity
`sonar-pro` · ClickUp · `control.md` LIVE). `TRADING_ENABLED: true`, **LIVE paper**,
`control.md` **Notes empty**. **Zero open alerts** (`alerts.md` Open incidents: *(none)*).
**Zero non-terminal orders** — the whole account history is still **ONE order** (the
2026-09-03 core fill, `filled`, terminal), so §7's order-limbo warning has **no operand**
rather than a clean bill.

**Numbers, each with its call and its basis — never differenced across calls.**

| Reading | Value | Call / basis |
|---|---|---|
| Account equity | **$100,397.17** | `sleeves` 08:13, live broker mark |
| Cash | **$30,000.00** exactly | `sleeves` — ~34th consecutive unchanged reading |
| Core VOO | **$70,397.165707** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:13 |
| Core % | **70.12%** | `sleeves`, live-mark basis |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **29.88%** | `sleeves` |
| Unrealized P&L on core | **+$397.175708 / +0.567%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **710.75** | `positions` `current_price`, 08:13 — a **pre-market indicative mark, NOT a close** |
| VOO `lastday_price` | **709.43** | ⚠ **NOT the official 10-15 close (709.37, the close seat's own `bars` pull). The gap is +$0.06. NEVER DIFFERENCE THESE TWO.** |
| §6 5% cap | **$5,019.86** | 100,397.17 × 5%, **with no operand** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (0.00186), OR
`unrealized_intraday_pl` (+$130.74113) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **709.43** this morning against the official 10-15 close of
**709.37**. ⚠ **The gap is six cents and the rule does not relax as it narrows — that is the
close seat's 10-15 finding restated: at four or six cents the two numbers LOOK
interchangeable, which is exactly when a run reaches for whichever is at hand.**

⚠ **TODAY'S SCHEDULED PRINTS ARE CORPORATE, NOT MACRO: five banks/insurers report before the
open (TRV, TFC, MTB, RF, CFG).** Disposed at `T-2026-10-16-04`. **Note the fact and do
nothing** — see **Carried from the research**.

---

## Reconciliation

1. **LEDGER RECONCILED FIRST, BEFORE ANY RESEARCH AND BEFORE ANY SELL RULE WAS READ. THREE
   SIDES AGREE.** `positions.md` holds **zero satellite blocks** · `alpaca.py positions`
   returns **one row, VOO**, 99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999**,
   **unchanged since 2026-09-03 (33 sessions)** · `sleeves` reports `satellite.count: 0`.
   ⚠ **No discrepancy. Nothing was researched on top of a ledger in doubt.**
   ⚠ **GREP TRAP, so the next seat does not re-raise it: `entry_price` / `highest_close` /
   `invalidation` return hits in `positions.md` that are ALL INSIDE `## Template`. That is the
   expected reading of an EMPTY ledger, not a position.**
2. **WEEK ROLLOVER — RECOMPUTED FROM SOURCE, NOT READ OFF THE FIELD.**
   `America/New_York` → **2026-10-16, Friday, ISO week 42, weekday 5, Monday anchor
   2026-10-12.** That **MATCHES** `week_of: 2026-10-12` in `state.md`, so
   `new_positions_this_week` was **NOT re-reset** — it stands at **0 of 3** because nothing
   has been opened, not because this run zeroed it. ⚠ **The distinction matters: a run that
   resets a counter it did not need to reset would mask a §6 breach.**
3. **CIRCUIT BREAKER — INACTIVE.** `consecutive_closed_losses: 0`, `halt_triggered_at: none`.
   ⚠ **Because `halt_triggered_at` is `none`, the `HALT_CLEARED_AT` comparison in `control.md`
   (currently `none`) was NOT DUE and was not performed. There is no halt to clear and no
   clearance to validate.** **New positions are PERMITTED this run. §6 did not block the
   research; the research found nothing.**
4. **§2 SLEEVE DRIFT — NO REBALANCE DUE.** Core **70.12%**, inside the 65–75% band with
   **4.88 points of headroom at the upper edge** and **5.12 at the lower**. `core_in_band:
   true`, `rebalance_needed: false`.
   ⚠⚠ **`rebalance_delta` IS NOW −$119.15, A FOURTH CONSECUTIVE READING AND A NEW EXTREME,
   WHILE CORE HAS NEVER LEFT THE BAND.** The series across 10-15 and this morning:
   **+$73.15 (10-15 09:37) → −$21.89 (12:41) → −$76.96 (16:16) → −$119.15 (10-16 08:13)**,
   against core **69.96% → 69.93% → 70.02% → 70.08% → 70.12%**. ⚠ **A run reading only the
   delta has now been told "buy VOO", then "sell VOO", then "sell more", then "sell more
   still", on ONE UNCHANGED POSITION across two sessions. §2 TRIGGERS ON THE BAND AND NOTHING
   ELSE. `rebalance_delta` IS A DISTANCE READOUT, NOT AN INSTRUCTION.**
5. **ZERO NON-TERMINAL ORDERS.** Nothing in limbo to reconcile.

---

## §5 sell-rule review

**NO OPERAND. There are zero open satellite positions, so §5.1, §5.2, §5.3 and §5.4 have
nothing to be evaluated against.**

⚠ **ALL FOUR RULES ARE *ABSENT*, NOT *PASSING*.** A rule that was reached and found to have no
subject has produced no evidence that it works. ⚠ **DISTANCE TO THE HARD STOP AND THE TRAILING
STOP IS *UNDEFINED*, NOT *LARGE*.**

**Core VOO was struck from the working list BEFORE any rule was read, per §5's core
exemption.** It is not a satellite operand and is exempt from all four rules.

⚠ **Step 4's Perplexity invalidation check (§5.1) cost ZERO queries, and that is STRUCTURAL
rather than a saving: §5.1 costs one query PER OPEN POSITION, and there are none.**

---

## Intents

### BUY

**NONE.**

**Five theses written this run (`T-2026-10-16-01` … `-05`), all five REJECTED.** The §6 gates
were all **OPEN** — breaker inactive, 0 of 3 positions this week, satellite sleeve **entirely
undeployed with $30,000 idle**, `control.md` notes empty, `TRADING_ENABLED: true`. ⚠⚠ **NOTHING
PREVENTED A BUY THIS MORNING EXCEPT THE RESEARCH NOT FINDING ONE. That is §4 working, not §6.**

**What died and where — the kills, not the vibes:**

| Thesis | Candidate | Died at |
|---|---|---|
| `T-2026-10-16-01` | Taiwan / TEEMA $4B Texas AI park | **part 1** (no company named as participant) · **rule (v) NEW COSTUME** · **part 3** (no groundbreaking date at all) · **rule (viii)** (project-level estimate) |
| `T-2026-10-16-02` | JBHT Q3 → rail read-through (UNP/NSC/BRK) | **part 1** (no transaction — an ongoing arrangement) · **rule (iii)** (rail volumes are weekly AAR disclosure) · **part 2** (BNSF is inside BRK, single-digit % of revenue) |
| `T-2026-10-16-03` | Alcoa (AA) Q3 + South32 approval | **part 1** (own results) · **§3** (South32 is ASX-listed) · **rule (viii)** (consideration paid OUT; no figure disclosed) |
| `T-2026-10-16-04` | TRV · TFC · MTB · RF · CFG | **rule (iii), purest form** — they report AFTER this run |
| `T-2026-10-16-05` | ten-item sweep | §3 · rule (iii) · rule (v) · rule (viii) · part 1 |

⚠⚠ **THE ONE WORTH THE 09:35 SEAT'S ATTENTION IS `T-2026-10-16-02`, BECAUSE IT IS THE
STRONGEST PULL THIS WINDOW PRODUCED AND IT CAME FROM *ME*, NOT FROM A SOURCE.** JBHT printed
**+20% revenue with record intermodal volumes up 8%**, and the chain "freight is strong →
buy a railroad" assembles itself in one step with no source asked. ⚠ **It is the
competitor/customer earnings READ-ACROSS — the shared-cause object — and §4 kills it every
time. If it comes back at 09:35 wearing a fresh dateline, the answer is already written.**

### SELL

**NONE.** No open satellite positions. ⚠ **Not "no sells warranted" — NO SUBJECT.** Core VOO
is exempt from §5 and is never sold on news (§2, §7).

### REBALANCE

**NONE.** Core **70.12%**, inside §2's 65–75% band with **4.88 points** of headroom at the near
(upper) edge. ⚠ **See Reconciliation item 4 — `rebalance_delta` −$119.15 is a distance readout
and the fourth consecutive reading that would have mis-instructed a run that read it as one.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate. This plan carries no BUY, no SELL and no REBALANCE intent.**
⚠ **There is therefore NO `revalidate` line in this plan, and that is correct rather than an
omission: the field names the specific number an intent must be re-checked against, and there is
no intent.**

⚠ **Do NOT read an empty plan as permission to skip the gate.** At 09:35:

1. ⚠⚠ **READ `plan_date` OFF THE FIELD. It is `2026-10-16`, and today is 2026-10-16 — FRESH.**
   Do not infer freshness from the fact that the run produced no orders: **an empty plan that is
   fresh and a plan that is stale produce IDENTICAL zero-order runs.** The gate has now been
   exercised ~40 times and has **never fired**; ⚠ **every exercise so far PASSED, and "passed"
   and "fired" are opposite outcomes of the same check. Do not write that the gate has been
   tested.**
2. **Re-run `clock` and confirm `is_open: true`** before anything else. §7 forbids trading when
   the market is closed.
3. **Re-run `sleeves` against live equity** and re-check §2's band. Core read **70.12%** here;
   it will have moved. **If core is outside 65–75% at 09:35, queue the rebalance then** — §2
   puts that call at your seat, not this one. ⚠ **And do not read `rebalance_delta` as the
   trigger; read the percentage against the band. See item 4 above for four readings' worth of
   why.**
4. ⚠⚠ **DO NOT OPEN A POSITION THAT IS NOT IN THIS FILE.** Every §6 gate is open and $30,000 is
   idle; **the only thing standing between this account and a trade this morning is the absence
   of an intent, and that is exactly what routine 2's restraint is for.** Routine 2 executes
   what the plan contains — opening at 09:35 without a plan entry routes **around** the
   discipline that makes every buy sleep on a written thesis.
5. ⚠ **THE FIVE BANK PRINTS LAND BETWEEN THIS RUN AND YOURS. THAT DOES NOT MAKE THEM YOUR
   LEADS.** They are first-order financial results and §4 buys Company B, not Company A. ⚠ **A
   fresh disclosure arriving after the plan was written is Monday's window, not a licence to
   reason a position into existence at the moment of execution — which is the precise failure
   `plan_today.md` exists to prevent.**
6. ⚠ **If `step 6` sources `voo_close_at_entry` from `bars --days 1`, KNOW THAT THE BAR IS
   PARTIAL AT 09:35** (item (12) in `state.md`: `n` 156 / `v` 2,029 at 09:36 on 10-06, and an
   `n`/`v` sanity check CANNOT distinguish it from a quiet full session). **It has cost nothing
   because no position has ever been opened; it becomes wrong on the FIRST fill.**

---

## Carried from the research, for the seats that follow

- ⚠⚠ **THE `T-2026-10-16-02` PULL, RESTATED BECAUSE IT IS THE RUN'S OWN NEAR-MISS AND NOT AN
  INHERITED WARNING: a strong customer earnings print makes its suppliers look like a
  discovery. RAIL VOLUMES ARE PUBLISHED WEEKLY BY THE AAR.** The read-through is not early, it
  is public and a week late. **Rule (iii) covers it; no new rule is needed.**
- ⚠⚠ **NEW RULE (v) COSTUME, NOW IN THE BOOK — AN UNNAMED CONSORTIUM ORGANISED BY A NAMED TRADE
  ASSOCIATION (TEEMA).** ⚠ **It is worse than an unnamed supply base because the blank comes
  with a LOOKUPABLE MEMBERSHIP ROSTER, so a run can build a candidate list in one search and
  feel it has been sourced. A ROSTER IS NOT A TRANSACTION.** Expect the Texas-park story to
  return with US names attached by commentators rather than by the parties; `T-2026-10-16-01`
  is the answer.
- ⚠ **TSMC's Q3 print was RE-SERVED ONE DAY AFTER ITS DISPOSAL** (`T-2026-10-15-01`). ⚠ **The
  re-serve rate is now 4 FOR 4 SESSIONS. Reading this log first cost one `grep` and saved two
  drills — it is the cheapest operation in the routine.**
- ⚠ **SEPTEMBER PPI (+1.3% m/m vs a 0.5% forecast) AND RETAIL SALES (+0.8% headline, +0.1%
  control group) HAVE NOW *PRINTED*, AND NO NEW THESIS ID WAS MINTED** — same disposed object as
  `T-2026-10-12-05` and `T-2026-10-13-08`, following the 10-14 and 10-15 precedent. ⚠ **A
  CHANGE IN STATUS IS NOT A CHANGE IN ELIGIBILITY.**
- ⚠ **NO MARKET CAP WAS SOURCED FOR ANY CANDIDATE THIS RUN, AND NO `move` CALL WAS MADE.**
  `JBHT`, `AA` and `NVDA` all reached part 1 and all died there, upstream of both filters. ⚠⚠ **DO
  NOT INHERIT A §3 VERDICT FOR ANY OF THEM — they are UNRESOLVED, not passed and not failed (the
  VAL / GFS / VIR / HNRG precedent).**
- ⚠ **Counters live in `state.md`, not here: thesis 161 → 166; session count HELD at 32 / 29**
  (only a seat standing after the bell may count the day it is in).
