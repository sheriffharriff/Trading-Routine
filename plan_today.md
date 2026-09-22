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
plan_date: 2026-09-22
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-09-22 at 09:30 ET** (`alpaca.py clock` at 08:15:26 ET: `is_open:
false`, `next_open: 2026-09-22T09:30:00-04:00`, `next_close: 2026-09-22T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` is *today*.
**Read the date, not the boolean.** *(Yesterday's 16:16 close run read the identical
`is_open: false` with `next_open` pointing at **tomorrow**. The boolean is the same in both
shapes and only the date discriminates.)*

**One pre-market run today, at 08:15 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$100,649.73**).

**Tape context.** Yesterday's **official** VOO close, from `bars --adjustment all`, was
**712.76** (09-18: 701.85). The broker's pre-market `positions` row reads `current_price`
**713.30** and `lastday_price` **712.78**.

⚠ **THE TWO-PRICE DEFECT HAS A NEW INSTANCE AND THE SIGN HAS FLIPPED.** `lastday_price`
**712.78** is **two cents ABOVE** yesterday's official close of **712.76**. The previous
instance ran the other way — **701.78 against an official 701.85, seven cents LOW, read four
times** across 09-21 (08:20, 09:36, 12:35, post-bell). That instance **did clear at the
session boundary** — this is a fresh one built on the new day's close, not the old one
persisting — **but it did not clear into correctness.** ⚠ **The carry-forward's warning that
the SIGN OF THE BROKER'S ERROR IS NOT PREDICTABLE is now demonstrated on consecutive days in
opposite directions.** Neither `current_price` nor `lastday_price` is an execution reference
or a close. **`bars --adjustment all` for a close, a fresh `quote` for execution, never a
`positions` field for either, and never `equity − last_equity` or `unrealized_intraday_pl`
for a day's P&L.**

The core shows `unrealized_pl` **+$649.74 / +0.928%** against the 706.74 fill. **§5 exempts
core from all four sell rules, so there is no action attached to that number in either
direction**, and it is a broker mark in any case.

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band at **70.19%**, there are no
satellite positions to manage, and **five candidates were researched to a full thesis entry
and all five were rejected.**

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker **INACTIVE**, weekly
cap at **0 of 3**, satellite sleeve **empty with 29.81% cash**, no restricting note in
`control.md`. **Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a
BUY intent exists. **Zero `alpaca.py move` calls are due at 09:35 — an absent check, not a
skipped one.**

Five candidates reached a full `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-22-01 | **(no ticker)** | **part 2**, rule (v) | **Paramount/WBD — California AG + 12-state antitrust settlement, 09-21.** Court-enforceable, five years, **still needs a judge's approval**; Paramount must release **30 films/yr then 32/yr**, pay **~$30M per missed film**, and raise US production spend **~$300M/yr (~$1.5B over five years)**. ⚠ **The mandated spend has a PAYER and no named PAYEE.** The screen's own words: *"No source … identifies a publicly traded U.S. supplier, distributor, exhibitor, advertising company, technology provider, or labor-services company with a quantified direct revenue or cost exposure to closing."* Only NFLX and DIS were attached, **as competitors**. No segment, no magnitude, no percentage. |
| T-2026-09-22-02 | **ACN** | **premise**, then **part 2**, then **part 3** | **Anthropic ↔ Accenture $2B / five-year AI-safety initiative, 09-22.** **Accenture is a SIGNATORY — first-order, outside §4 at any price** (the Bloom Energy shape from 09-21). On the **most generous** reading the whole $2B is ACN revenue = **~$400M/yr against >$60B, well under 1%** vs the 10% floor — and that reading is unavailable, because the source says it *"does not disclose how the $2 billion would be divided … whether it represents cash spending, in-kind services, or a contractual ceiling."* **Five-year term** kills part 3 separately. |
| T-2026-09-22-03 | **(no ticker)** | **part 3** in one step, plus **premise** and **rule (iii)** | **Nscale's ~$103B pre-IPO contract book** — Microsoft **~$43.8B** (late-2025 → 2033), Anthropic **~$44.6B** (signed **August 2026**), together **85%** of the book; Monarch campus WV, **~2GW by 2028 → ~8GW by 2031.** **Nothing lands inside two quarters.** Nscale and Anthropic are **private**; **Microsoft is a signatory.** And the "news" is an **IPO disclosure of contracts up to ten months old** — rule (iii). |
| T-2026-09-22-04 | **(no ticker)** | **part 1**, rule (v) | **Vicor raised Q3 2026 sequential revenue growth from "nearly 10%" to "more than 20%" on 09-21, on VPD licence royalties.** ⚠ **The event PASSES rule (iii) and rule (viii) cleanly and the horizon is ONE QUARTER** — the best-shaped event of the window. **It still produced nothing, because the licensees are described only as "four leading OEMs and hyperscalers" and "a leading AI OEM" — not one is named.** Vicor itself is **below the §3 $10B floor.** |
| T-2026-09-22-05 | **GPC / ORLY / LKQ** | **part 1** | **AutoZone FQ4 2026, 09-22: EPS $56.05 vs $54.30 (beat), net sales $6.595B vs ~$6.70B (miss), SSS +1.5%, no new guidance, no commercial agreement.** The aftermarket read-across needs an **"and also"** — same demand environment, **and AutoZone is a COMPETITOR of all three, not a counterparty.** **Eighth shared-cause instance.** Direction is mixed-to-negative anyway. |

Notes for the open run, carried so nothing is re-derived at 09:35:

- **⚠ THE LOUDEST THING ON THE TAPE WAS NOT AN EVENT, AND TWO SEPARATE SCANS WERE SPENT PROVING IT.**
  **AMD +10% (through $1T market cap for the first time), Intel +12%, Arm +17%, SOX +4.3%, Nasdaq at a
  record close.** Both scans were built to find the transaction underneath it. **There is not one.**
  Reporting attributes the move to *"renewed AI optimism"* and to **Meta's Muse AI launch**, which the
  same source calls *"an investor-demand narrative rather than a disclosed AMD, Intel, or Arm
  contract."* ⚠ **A three-name double-digit session with no named counterparty and no disclosed figure
  is a SENTIMENT move — there is no Company A in it to run §4 against**, and all three names are
  priced-in several times over. **The pull to find a "second-order AI winner" on a green record day is
  the strongest this funnel produces. The honest answer is that the first order does not exist yet.**

- **⚠ EIGHTH INSTANCE OF OPEN ITEM (1): THE PRICED-IN FILTER RETURNED "LATE — SKIP" ON A 4.58% FALL.**
  `move --symbol ACN --sessions 5` → **195.04 → 186.10, −4.58%, `priced_in: true`.** ⚠ **A stock that
  went DOWN cannot have priced in good news that broke today.** **This is NOT the reason ACN was
  rejected** — it dies three times over on the thesis (signatory; <1% of revenue; five-year term) —
  and it is recorded that way **deliberately, so that no future run inherits "rejected because
  priced-in" as a fact.** Seven prior instances plus two near-misses (LMT −3.61%, GM −3.95%). **A FAIL
  on a fall is no more evidence the filter works than a PASS on a fall was.** The fix is **a human
  editing §4 or `alpaca.py move`.** **Do not reinterpret the filter at 09:35.**

- **⚠ THE MOST INSTRUCTIVE REJECTION OF THE DAY IS VICOR, AND IT IS NOT A ROUTINE ONE.** Every other
  candidate failed on a **defect in the event** — too long-dated, too small, first-order, re-reported.
  Vicor's event had **none of those defects**: a company revising **its own prior figure** (rule (iii)
  passes), an **inbound revenue** figure (rule (viii) passes), and a **Q3 horizon — one quarter**,
  which is as good as part 3 ever gets in this funnel. It produced nothing **because the one field
  that would make it tradable is the field the source withholds: who is paying.** ⚠ **That is the
  FIRST of the four known forms of the binding constraint in open item (3)** — the form 09-21's GM
  entry had tentatively written off. **Today restores it in a cleaner example.** The constraint is not
  thin news and not a long horizon. **It is that counterparty identity is routinely the one thing not
  disclosed.**

- **⚠ RULE (iii) FIRED TWICE IN TWO SESSIONS, IN TWO NEW COSTUMES.** 09-21 was a **delivery milestone**
  recycled as news (GM/Lockheed: contract 08-06, delivery 08-28, wire 09-17, headline 09-21). Today is
  a **pre-IPO contract book**: Nscale's $103B is an **IPO-prospectus disclosure of deals signed in late
  2025 and August 2026**, surfaced as a 09-22 headline. **Ask a transaction WHEN IT HAPPENED before
  asking who it helps. One screen settles it, and it is the cheaper kill.**

- **⚠ THE COMPETITOR'S-PRINT COSTUME IS THE THIRD FACE OF THE SHARED-CAUSE TRAP AND THE MOST
  RESPECTABLE-LOOKING.** 09-16: a **divergence** between named companies sounds causal (JPM/BAC/WFC).
  09-21: a **convergence** does too (Bunge/ADM). Today: **a competitor's audited, company-disclosed,
  same-morning earnings print** reads like hard evidence about GPC/ORLY/LKQ and is in fact a statement
  about an **industry**. ⚠ **The giveaway never changes and is the only test needed: the sentence
  required an "and also".**

- **⚠ THREE PRICE SCREENS WERE DELIBERATELY NOT RUN, AND THE ABSENCE IS THE POINT.** No `move` was
  pulled for T-01 (no ticker), T-03 (a guessed-at basket of electrical-equipment names) or T-05
  (GPC/ORLY/LKQ). In each case the mechanism had already failed, and a clean `priced_in: false` would
  have created pressure to go back and rescue part 1. **§4 says the filters come BEFORE the thesis; it
  does not say the filters substitute for having a candidate.** *(The 09-01 RTX process note is the
  worked example of getting this ordering wrong.)*

- **⚠ GENERAL MILLS PRINTS TOMORROW — 2026-09-23 — AND IT IS THE ONE LIVE RESEARCH ITEM.** GIS **has
  still not reported.** Consensus **$0.72 EPS** (vs **$0.86** a year ago) on **~$4.34B** — ⚠ **every
  figure in circulation is an analyst expectation.** The company's only statement remains the
  **September 8 affirmation** of FY27 adj. EPS **$3.00–$3.20** — an **affirmation**, standing rule
  (iii), the Centene and Southwest shape. **Nothing to screen until the print.** **Not this run's
  item and not the 09:35 run's item** — carried explicitly to the **09-23 pre-market run**.

- **⚠ GNRC IS STILL NOT YOURS TO LOOK AT — TWELFTH CONSECUTIVE REFUSAL, AND TODAY'S TEST WAS STRONG.**
  This run ran **`move --symbol ACN`** and **`bars --symbol VOO`**: the data plane was open and a
  `--symbol GNRC` would have been one flag on a command already being typed. **The tenth costume
  arrived as *"you are already screening a candidate's five-session move, so screening one more costs
  nothing"* — the zero-marginal-cost costume wearing a live funnel as cover. Refused.** The
  disqualifying facts do not move: **GNRC is the named counterparty in the Amazon announcement,
  first-order and outside §4 at any price**, and **open item (7) is resolved by a human editing §4 or
  `alpaca.py move`, not by a number this seat collects.** **Zero `move`/`quote`/`bars`/`asset` calls
  on GNRC, twelve runs running.** Costumes so far: diligence, curiosity, tidiness, completeness,
  zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
  screen-already-running. **Expect an eleventh.**

- **Dropped before thesis stage, with reasons:** **Applied Materials $5B India** — announcing party,
  capital paid **out**, **"over the next decade"** (part 3, rule (viii)). **New Era Energy ↔ a Vistra
  affiliate** — VST is a signatory, **20-year** PPA, **no disclosed value**. **Navitas ↔ Magnachip
  ($5M)** and **Priority Technology (~$1.6B go-private)** — **below the §3 $10B floor**. **Telix ↔ ITM
  ($1.65B)** — not US-listed common stock; ITM private. **HealthEquity, Lamb Weston, American Electric
  Power** — prints measured **against consensus**, no counterparty, no transaction; **AEP's is a *Q2*
  operating result surfacing as September news, which is the rule (iii) re-report shape.** **FOMC
  +25bp to 3.75–4.00%** (already disposed — **it does not become an event by being re-reported**),
  **the Musalem/Williams/Jefferson/Barkin speech calendar**, **the 09-22 ADP and Richmond Fed
  releases**, **US–China AI-dialogue talks**, **the Gates Foundation language-data coalition**, **oil
  below $100** — **environment inputs, diplomatic proposals and schedules, not a Company A.**

### SELL — none

**No open satellite positions.** §5.1–§5.4 have no subject for the **twenty-fourth consecutive
session**. `sell_rule_status` is **absent, not blank** — there is no thesis to invalidate, no
`timing_window` to expire, no `entry_price` to measure −7% against, and no `highest_close` to
measure −10% against. **Nothing is near triggering because nothing exists to trigger.** All four
remain **untested code paths**, and twenty-four sessions of "no exits" record the **absence of a
subject**, not twenty-four clean bills of health.

**Zero Perplexity invalidation queries were issued this run and none was due** — §5.1 reads an
`invalidation` line that does not exist. **§5.4 is still NOT ARMED; it arms on the first *satellite*
fill**, and the 09-03 core fill was not it.

**⚠ NO HIGH-WATER BACKFILL IS DUE, AND THE MISSING STAMP IS NOT EVIDENCE OF A FAILED CLOSE RUN.**
The 09-21 close run **executed its Step 2 and Step 2 had no operand.** The marks are **ABSENT — a
third state, distinct from "stale" and from "current and unchanged"** — and **an absent field carries
no `(as of …)` date to compare.** The midday backfill trigger will find no stamp today, exactly as it
found none yesterday. **Nothing was skipped.**

### REBALANCE — none

**Core is in band and no rebalance is due.** `alpaca.py sleeves` at 08:15 ET: equity
**$100,649.73**, cash **$30,000.00**, core **$70,649.73 = 70.19%**, satellite **0.0% (count 0)**,
cash **29.81%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: −194.92`.

On an **official-close basis** (09-21 VOO 712.76 × 99.046311231 shares): core **$70,596.25**, equity
**$100,596.25**, core **70.178%**, cash **29.822%**. ⚠ **Both bases agree, and both are the same
side of target** — core is **above** 70% for the third run running.

§2 rebalances at the **band edge (65/75)**, **not to the exact 70% target.** The **−$194.92** delta is
**0.194% of equity** and **no delta inside the band is an action at any size, in either direction.**
**Thirty-first consecutive run inside a 0.60-point range (69.59–70.19).**

---

## What the open run should actually do

1. **Check `plan_date` against today's ET date.** It reads **2026-09-22**. If today is not that
   date, this plan is stale — log it, alert, and skip to the core/rebalance section.
2. **Execute nothing.** There are no BUY, SELL or REBALANCE intents, and **that is the plan, not a
   gap in it.**
3. **Do not go looking for something to do.** 29.81% idle cash, an INACTIVE breaker and a weekly
   cap at **0 of 3** are **not an opportunity this run may act on.** New positions route through
   pre-market research plus this execution run, always — a position opened at 09:35 without a plan
   entry would route around the discipline rather than satisfy it.
4. **Verify the empty plan is FRESH, not stale.** An empty plan that is current and a plan that is
   out of date **produce identical zero-order runs and are not the same run.** The difference is
   invisible in the order count, so **read the date rather than the outcome.** ⚠ **The stale-plan gate
   has now been exercised twenty-three times and has never fired — its alert path REMAINS UNTESTED
   CODE.** Twenty-three quiet opens are not evidence the gate works. **The first morning it fires will
   by construction be a morning when this pre-market run failed — i.e. exactly the morning you have no
   fresh notes to lean on. Read the routine's Step 2 then; do not recall it.**
5. **Pull a fresh quote for anything you price.** The broker's `current_price` is a **live midpoint,
   not a close**, at every hour including after the bell — 09-21 proved that at 16:16, sixteen
   minutes past the close, when it read **712.54** against an official **712.76**. And
   `lastday_price` is wrong again today in the **opposite** direction (**712.78** vs **712.76**).
   **The sign of the broker's error is not predictable. Only an external close settles it.**
