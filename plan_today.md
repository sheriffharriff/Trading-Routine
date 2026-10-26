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

```
plan_date: 2026-10-26
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-26 at 09:30 ET** (`alpaca.py clock` at 08:05:20 ET: `is_open:
false`, `next_open: 2026-10-26T09:30:00-04:00`, `next_close: 2026-10-26T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean.**

⚠⚠ **THE PLAN THIS RUN REPLACED WAS DATED 2026-10-23 — THREE CALENDAR DAYS OLD AND ONE
TRADING DAY OLD, WHICH IS THE MONDAY SHAPE THE CARRY-FORWARD NAMES: A *CORRECT* PLAN ARRIVES
THREE CALENDAR DAYS OLD ON A MONDAY.** ⚠ **Compared to the last TRADING day (Friday
2026-10-23), not to the calendar — so it was **fresh, not stale**, and no stale-plan
condition existed.** ⚠ **It is also irrelevant to execution either way: the 09:35 seat reads
the `plan_date` written above, which is today's.**

---

## Tape context

**Pre-flight selftest: 5/5** (env · Alpaca ACTIVE `trading_blocked=False` · Perplexity
`sonar-pro` · ClickUp · `control.md` LIVE). `TRADING_ENABLED: true`, **LIVE paper**,
`control.md` **Notes empty**. **Zero open alerts** (`alerts.md` Open incidents: *(none)*).

**Numbers, each with its call and its basis — never differenced across calls.**

| Reading | Value | Call / basis |
|---|---|---|
| Account equity | **$99,460.19** | `sleeves` 08:05, live broker mark |
| Cash | **$30,000.00** exactly | `account` + `sleeves`, `accrued_fees: 0` |
| Core VOO | **$69,460.187603** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:05 |
| Core % | **69.84%** | `sleeves`, live-mark basis — **IN BAND** |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **30.16%** | `sleeves` |
| Unrealized P&L on core | **−$539.802396 / −0.771%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **701.29** | `positions` `current_price`, 08:05 — a **pre-market indicative mark, NOT a close** |
| VOO official 10-23 close | **698.33** | `bars --days 7 --adjustment all`, re-pulled at this seat — **not inherited** |
| VOO `lastday_price` | **698.58** | ⚠ **NOT the official close. See below.** |
| §6 5% cap | **$4,973.01** | 99,460.19 × 5%, **with no operand today** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (+0.00388), OR
`unrealized_intraday_pl` (+$268.415503) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **698.58** against the official 10-23 close of **698.33**.
⚠ **TWENTY-THIRD CONSECUTIVE SEAT ON THIS STANDING ITEM; the gap is +$0.25.** Attributed to
the cent at this seat rather than asserted: `last_equity` **99,191.77209975198** = 99.046311231
× **698.58** + 30,000 **exactly**, so **both ends of the broker's own day-P&L pair are live
midpoints.** ⚠ **It is a MOVING LIVE MIDPOINT, NOT AN OFFSET — +$0.28 on Friday, +$0.25 today —
so neither a small nor a large reading means anything. STANDING ITEM, NOT RE-RAISED AS NEW.**

⚠ **`equity` moved across three calls in three minutes — $99,434.44 (selftest 08:04) ·
$99,460.19 (`sleeves` 08:05) · $99,471.08 (`account` 08:06). Each figure above is tagged with
its call for that reason, and two calls agreeing would not have been a calibration either.**

⚠ **The pre-market mark 701.29 is **+2.96 (+0.4239%)** against the official 10-23 close of
698.33. That is an indicative pre-bell quote on thin volume and **is not a close**; it is
recorded as context and used for nothing. The 09:35 seat must re-pull its own numbers.**

**Friday's tape, carried as context and used for nothing:** VOO closed **698.33** vs **702.02**,
**−0.5256%**, on volume **34,733** / `n` **1,082**. ⚠ **A FRESH INSTANCE OF THE RETIRED n/v
DRIFT ITEM, NOT A NEW FINDING: the same completed bar read `v` 34,730 / `n` 1,080 at Friday's
16:16 close seat and reads 34,733 / 1,082 now — **+3 shares, +2 trades, same date, same basis**,
with `o`/`h`/`l`/`c` **unchanged**, so nothing any §5 rule reads has moved.** ⚠ **Late-print
settlement. `n`/`v` remain unusable as evidence in either direction.**

---

## §2 sleeve check — IN BAND, NO REBALANCE DUE

`sleeves` 08:05: core **69.84%**, `core_in_band: true`, `rebalance_needed: false`,
`rebalance_delta: 161.95`, `core_target_value: $69,622.13`.

⚠ **`rebalance_delta` is a DISTANCE READOUT, NOT AN INSTRUCTION — standing item.** $161.95 on
$69,460 is **0.23%**, all of it the mark moving under a **fixed share count — no shares have
moved since 2026-09-03.** §2's band is **65–75%**, which on this equity is **$64,649.12 to
$74,595.14**; core sits **$161.95 BELOW** the 70% target of **$69,622.13** and is **~$4,811
above the 65% floor**, i.e. roughly **4.8% of equity away from the edge, not 0.23%.**
⚠ **A drifting percentage with no transaction behind it is not drift that §2 asks anyone to
correct, and the band is not close.** **NO REBALANCE INTENT.**
⚠ **Re-compute at 09:35; do not inherit this figure.**

---

## §6 gate status — EVERY GATE OPEN, AND NOTHING IS BOUGHT ANYWAY

| Gate | State | Source |
|---|---|---|
| Circuit breaker (§6/§7) | **INACTIVE** | `state.md` `circuit_breaker: INACTIVE`, `halt_triggered_at: none`, `consecutive_closed_losses: 0`; `control.md` `HALT_CLEARED_AT: none` |
| New positions this week (§6, max 3) | **0 of 3** | `state.md` `new_positions_this_week: 0`, `week_of: 2026-10-26` |
| Satellite sleeve (§2) | **ENTIRELY UNDEPLOYED** — $0.00 / 0.0% / count 0, **$30,000.00 idle across 35 post-fill sessions** | `sleeves` |
| `control.md` Notes | **EMPTY** — no restriction | `control.md` |
| 5% position cap (§6) | **$4,973.01** | computed, **no operand** |

⚠⚠ **A BUY WAS PERMITTED ALL RUN AND NOTHING IS BOUGHT. THAT IS A RESEARCH RESULT, NOT A
PERMISSION RESULT.**

---

## Week rollover (§6)

Today is **Monday 2026-10-26**; ISO week **2026-W44**; Monday of this ISO week is
**2026-10-26**. `state.md` `week_of` reads **2026-10-26** — **MATCH, no rollover performed
here, counter stays at 0 of 3.** ⚠ **Computed from the date with `isocalendar()`, not
inherited from the field it was checked against.**

⚠⚠ **AND THE REASON IT MATCHED IS WORTH ONE LINE, BECAUSE A MATCH HERE COULD MEAN TWO DIFFERENT
THINGS: Friday's weekly review performed the roll FORWARD to 2026-10-26 on 10-23, deliberately
and as a non-correction. So this seat found the work already done rather than finding nothing to
do.** ⚠ **The routine prompt tells this seat to roll the week here rather than rely on Friday —
precisely so a failed Friday cannot leave the §6 cap stuck at its limit. That safety net was
exercised today and was not needed. It is still the right place for it.**

---

## Intents

### BUY — **NONE**

**Four theses written, ZERO accepted, FOUR rejected** — `T-2026-10-26-01` through `-04`,
disposing **twenty** distinct items in all. **Three broad scans, one drill query, ZERO quotes
and ZERO `move` calls pulled on any ticker.**

⚠⚠ **THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE AGAIN, IN BOTH SCANS THAT ASK IT
DIRECTLY AND IN THE DRILL, IN ITS OWN WORDS:** *"the evidence supports **zero confirmed
matches**, rather than a list of likely candidates"* · ***"no second publicly traded U.S.
company is named with a dollar figure attributed to it"*** · and the overnight scan's
volunteered limit, *"The available evidence is insufficient to claim that the list above is
exhaustive."*

**WHY THERE IS NO BUY INTENT, ONE LINE EACH:**

| Candidate | Killed at | The number or fact that killed it |
|---|---|---|
| **EQT / Range Resources** | part 1 · part 2 · part 3 | **Verbatim denial** on any named third party; every figure is an **enterprise value**, an **exchange ratio** or **consideration to shareholders**; close **Q1 2027** |
| **Audi / VW Georgia $4.2B** | part 3 · part 1 · §3 | **Production in the EARLY 2030s** — ~16–24 quarters against §4's two; **no counterparty named at all**; VW is **Frankfurt-listed** |
| **Samsung SDI / Alpha Omega** | §3 · part 2 · rule (iii) | **KRX-listed** Company A, **private** customer; the quantity is **1 GWh, not money**; headline 1.5 GWh is **part re-report** |
| **Sweep of seventeen** | §3 / rule (viii) / govt / repeats | Each a one-step kill — see `T-2026-10-26-04` |

⚠⚠⚠ **THE DAY'S HONEST SUMMARY, AND IT IS NOT A COMPLAINT ABOUT THE WINDOW: THE STRUCTURAL
FRAMING RETURNED FOUR ITEMS AND SELF-EXCLUDED NONE OF THEM — THE FIRST TIME THAT HAS HAPPENED —
AND ALL FOUR DIED ON THE *UNIT* TEST ANYWAY.** Four dollar figures (EV, gross proceeds,
consideration paid out, a credit ceiling) and **not one is segment revenue at a Company B.**
⚠ **Rule (viii) sweeping a scan's entire output in one pass is new, and it says the framing is
reaching real inventory while the §4 bar sits exactly where the disclosures are not.**

⚠⚠ **THE ONE CANDIDATE THE RUN HAD TO REFUSE RATHER THAN DISPOSE IS NAMED IN WRITING:
`T-2026-10-26-03`'s Stellantis (STLA) read-across through the StarPlus Energy joint venture.**
It is the only path in today's entire funnel output reaching a US-listed name above $10B.
⚠⚠ **IT WAS SUPPLIED BY ME, NOT BY THE SOURCE — the disclosure never mentions Stellantis, the
JV's ownership or any dollar figure. That is rule (v) and the honest-broker paragraph on the
same object, and it is recorded as a REFUSED PRIOR, not as a candidate.**

### SELL — **NONE**

⚠ **NO OPERAND, NOT "NOTHING DUE".** Zero open satellite positions, so §5.1–§5.4 have no
subject to evaluate. **Core VOO is §5-exempt (§5, final line) and was struck from the working
list rather than stamped — not stamping it is the correct action, not an omission.**
**Details in `positions.md` under today's `sell_rule_status`.**

### REBALANCE — **NONE**

Core **69.84%**, inside §2's 65–75% band. See the §2 section above.

---

## Revalidation instructions for the 09:35 seat

There are no BUY intents, so there is **nothing to revalidate** — the usual
`revalidate: re-run move --symbol X --sessions 5, skip if >4%` line has **no operand today.**

⚠⚠ **AND THE STANDING LIMIT OF THAT MECHANISM IS RESTATED HERE SO IT IS NOT LOST ON A QUIET
DAY: a `move` call at 09:35 READS CLOSES, and today's close does not exist at 09:35 — so a
re-check returns the SAME figure, bit for bit. THE REVALIDATE MECHANISM CANNOT SEE AN OVERNIGHT
GAP WITH THE TOOL IT IS POINTED AT.** Catching one needs a quote-against-prior-close comparison,
a different call. **This is priced-in defect shape six and it is open human item (13).**

**What the 09:35 seat should actually do today:**
1. Re-pull `clock`, `sleeves`, `positions` — **do not inherit any number from this file.**
2. Confirm `plan_date` above reads **2026-10-26** and matches today's ET date.
3. Reconcile the three-sided ledger (Alpaca `positions` satellite rows · `positions.md`
   satellite headers · `sleeves.satellite.count`) **before any order path.**
4. Re-check core against the 65–75% band on **its own** numbers. **69.84% is not close to an
   edge**, but recompute rather than inherit.
5. **Nothing else. There is no buy to make and no sell to make.**
   ⚠ **None of today's four rejections is price-dependent, so NO 09:35 quote can revive any of
   them.** EQT died on the absence of a named third party and a Q1 2027 close; Audi on a
   production date in the early 2030s and a non-US issuer; Samsung SDI on §3 and a unit that is
   not money. **"But it has not run yet" is "but it went up" wearing a coat.**

---

## Open items for the human — FOURTEEN, unchanged this run

⚠ **No item was added, closed or re-litigated today. Listed as pointers only; the substance is
in `state.md`'s carry-forward and in `weekly_review.md` (week ending 2026-10-23).**

1. The §4 priced-in filter tests `abs(move)`, so a **drawdown reads as priced-in** — sixteen
   instances, and LITE's rejection is now **in profit by nine points**, which does not close the
   item: a rule that is only wrong while it is losing is not a rule.
2. §1 is **unmeetable as written on this platform** — the paper account does not model
   dividends, so a 70% core under-earns ~0.93pp/yr against an S&P 500 **total**-return
   objective. Three options are written out in the 2026-10-08 plan.
3. ⚠ **And choosing option (i) without also moving the 2026-08-06 reference from the
   adjustment-all 704.83 to the raw 706.645 is a NO-OP THAT LOOKS LIKE A FIX.**
4. The **cash drag**: 30% idle is **4.35pp/yr** of the 5.25pp/yr total handicap.
5. The broker/official price gap is a **moving live midpoint**, not an offset — no API field
   may be differenced against an official close.
6. `strategy.md` §3's treatment of **Shopify-style Canadian issuers on US exchanges** is
   reached-but-undecided; a live candidate must go to the human.
7. Build the **missing-close-run detector** as a subset test (session dates ⊆ journal
   headings). Flagged, not built — a run does not edit routine prompts mid-run.
8. **2026-10-05's close run vanished** and no alert could have fired; a run that dies before
   `commit.py` leaves no trace by construction.
9. ⚠ **Never pair an adjusted return with a raw one** — this trap was met live on 10-23 and
   returned +26.73bp, a figure belonging to nothing.
10. **Collapse discipline** in `state.md` / `positions.md` — the files keep growing, and
    collapsing a *series* (rather than prose) has a measured cost.
11. Whether the §4 evidence bar should move. ⚠ **The evidence keeps cutting AGAINST moving it:
    the binding constraint is disclosure practice and the calendar, neither of which a wider bar
    would touch.**
12. Routine 2 Step 6 captures `voo_close_at_entry` from `bars --days 1` at 09:35, where it meets
    a **partial bar every time**.
13. The `revalidate` mechanism **cannot see an overnight gap** — priced-in shape six.
14. **The reject board is not reproducible** — it is rebuilt by an ad-hoc parse each Friday and
    nothing persists the rows; its count has read 64 / 64 / 63 / 60 over a frozen set. Fix is a
    committed `(ticker, rejection_date, thesis_id)` file so the review RE-PRICES rows rather than
    RE-DISCOVERS which rows exist.

---

## ⚠ Agenda for tonight's close run

- **Nothing special.** Zero trades expected, zero positions to mark, **Step 2 will again have
  NO OPERAND** — and the next run must read that as *nothing-to-stamp*, **not** as
  *step-skipped*. The `highest_close` field stays **ABSENT**, a third state carrying no date.
- **Advance the session counter at the close seat and nowhere else** — the unit is a *completed*
  session, the `bars` route is valid only from a seat standing after the bell, and today's bar
  must be excluded before counting at any earlier seat. **35 post-fill as of Friday's close;
  tonight should read 36.**
- **Take the day's P&L from `bars --adjustment all` close-to-close, never from the `account`
  call.** `lastday_price` is +$0.25 away from the official close this morning.
