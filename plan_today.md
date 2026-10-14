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
plan_date: 2026-10-14
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-14 at 09:30 ET** (`alpaca.py clock` at 08:21:37 ET: `is_open:
false`, `next_open: 2026-10-14T09:30:00-04:00`, `next_close: 2026-10-14T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both** `next_open`
and `next_close` carry **today's** date, which is the full-session signature rather than an
early close. ⚠ **Read the DATES, not the boolean: FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** The 10-13 close seat predicted this exact signature in
writing, and it is what arrived.

**One pre-market run today, at 08:21 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$101,007.25** at pre-flight).

⚠ **THIS FILE ARRIVED CARRYING `plan_date: 2026-10-13` — ONE trading day and ONE calendar day
old, the ORDINARY shape, exactly as predicted.** Compare `plan_date` to the **last trading
day**, never to the calendar — the Monday shape, where a correct plan arrives three calendar
days old, is not today's. ⚠ **Its predecessor was fresh and deliberately empty, and so is this
one: a fresh empty plan and a stale plan produce a byte-for-byte identical zero-order run, so
freshness is read OFF `plan_date` and never inferred from the outcome.** **The staleness gate's
non-exercise count will be 40 after today's open; it has never fired and its alert path remains
untested code.**

---

## Tape context

⚠ **EVERY FIGURE BELOW CARRIES ITS CALL AND ITS BASIS. Never difference across calls.**

- `sleeves` **equity $101,007.25** · `selftest` **$101,007.25** minutes earlier — the twelfth
  two-readings instance and the **SECOND to agree to the cent.** ⚠ **AGREEMENT IS NOT A
  CALIBRATION: two samples of a moving mark that coincided. Never difference the two.**
- Since inception **+1.0072%** on a $100,000.00 opening (live-mark basis, pre-bell — **not** an
  official-close figure, and **not** comparable to the close seat's series).
- Broker `positions` row: `current_price` **716.9096**, `lastday_price` **715.20**.
  ⚠⚠ **THE TWO-FEED FINDING THE 10-13 CLOSE SEAT RAISED IS LIVE AGAIN THIS MORNING AND IN THE
  SAME DIRECTION: the official 10-13 bar closed **715.08**, and the broker's `lastday_price`
  reads **715.20** — a **+12¢** gap on the identical session.** ⚠ **A MARK READ OFF `positions`
  IS NOT A CLOSE. Harmless while the sleeve is empty; the moment §5.4 arms, a trailing stop that
  mixes a broker mark into a bar series fires on the wrong number and looks entirely correct
  doing it.**
- ⚠ **ZERO `bars` CALLS AT THIS SEAT, DELIBERATELY.** No mark is owed (no satellite position
  exists), and a decorative pull would read in the artifact as a mark having been checked.
- ⚠⚠ **DO NOT STAMP CORE VOO WITH A `highest_close` — DECLINED A 96th CONSECUTIVE RUN.** §7
  forbids arming §5.4 on the one position §5 exempts.

---

## Reconciliation

**1. Ledger — BOTH SIDES AGREE, checked before any research was done.** `positions` returns **ONE
row**: VOO **99.046311231 sh** @ **706.74**, `market_value` **71,007.251366**, `cost_basis`
**69,999.989999**, `unrealized_pl` **+1,007.261367 / +1.439%**. `positions.md` holds **ZERO
satellite blocks**. ⚠ **GREP TRAP: `entry_price` / `highest_close` / `invalidation` return three
hits, all inside `## Template` — the expected reading of an EMPTY ledger, not a position.**

**2. Week rollover — RECOMPUTED FROM SOURCE AND FOUND MATCHING, SO NOT RE-RESET.**
`America/New_York` → **2026-10-14, Wednesday, ISO week 42, weekday 3 → Monday anchor
2026-10-12**, which equals `week_of` in `state.md`. ⚠ **`new_positions_this_week` DELIBERATELY
LEFT AT 0 of 3 — an untouched counter, not a reset one.**

**3. Circuit breaker — INACTIVE**, `halt_triggered_at: none`, `consecutive_closed_losses: 0`.
⚠ **No `HALT_CLEARED_AT` comparison was due, so that comparison remains UNTESTED CODE.** Nothing
has ever closed in this account, so §6's three-loss breaker has never been approached and both
its increment and its `clickup.py alert --key circuit-breaker` path are also untested.

**4. Sleeve drift — IN BAND, NO REBALANCE QUEUED.** Core **70.2992%**
(71,007.251366 / 101,007.25), **5.30 points** of headroom at the near edge and **4.70** at the
far — the **87th consecutive in-band run**. Satellite **0.0%**, count **0**. Cash **29.7008%**
($30,000.00 exactly, `accrued_fees: 0`). ⚠ **`rebalance_needed: false`; `rebalance_delta`
−$302.18 is a DISTANCE READOUT, NOT AN INSTRUCTION.**

**5. Controls.** `TRADING_ENABLED: true` · `control.md` notes **EMPTY** · `alerts.md` **zero
open incidents**. ⚠ **Zero open alerts is NOT evidence that every seat ran — a run that dies
before `commit.py` leaves no trace by construction. See the vanished-runs item in `state.md`.**

---

## §5 sell-rule review

**NO OPERAND, 84th CONSECUTIVE SESSION.** Core VOO was struck from the working list **before any
rule was read** — §5 exempts it and §7 forbids selling it on news. With core removed, the list
is empty, so §5.1, §5.2, §5.3 and §5.4 were re-evaluated **in order** and each reached nothing.

⚠⚠ **THE DISTANCE TO EVERY RULE IS *UNDEFINED*, NOT *LARGE*.** There is no `entry_price` to
measure −7% from and no `highest_close` to measure −10% from. **"All four rules passing" would be
a false statement; "all four rules absent" is the true one.**

- **§5.1 invalidation** — no thesis is held, so **no Perplexity news check was issued on any
  holding**, and that is an absence rather than a skipped step.
- **§5.2 time stop** — no `timing_window` deadline exists to have passed.
- **§5.3 hard stop / §5.4 trailing stop** — no operand; `sell_rule_status` in `positions.md` is
  updated to say so in those terms rather than to report a distance it cannot compute.

⚠ **`orders --status all` history remains ONE row for the whole account (the 2026-09-03 core
fill, `filled`, terminal), so §7's non-terminal-order warning has NO OPERAND rather than a clean
bill of health.**

---

## Intents

### BUY

**NONE. ⚠⚠ ZERO BUY INTENTS, AND NOTHING BLOCKED THEM.**

⚠ **Every §6 and §7 gate was OPEN and this must not be lost between here and 09:35:** breaker
**INACTIVE** · `new_positions_this_week` **0 of 3** · satellite sleeve **0% deployed** against a
30% target with **$30,000 idle cash** · `control.md` notes **empty** · `TRADING_ENABLED: true` ·
§6's 5% cap standing ready at **$5,050.36** (`sleeves` basis, pre-bell — re-compute it against
live equity at 09:35 rather than carrying this number). **A buy was placeable all morning.
Nothing was worth buying, and an empty plan is a complete instruction rather than a gap to fill.**

**Five candidates were researched and all five were rejected** (`T-2026-10-14-01` … `-05`). The
kills, one line each, so the 09:35 seat need not re-read the log to know nothing is pending:

| ID | Candidate | Test that failed |
|---|---|---|
| **-01** | **Lockheed Martin / Avio S.p.A.** — strategic cooperation giving LMT access to Avio's **merchant solid-rocket-motor** capacity for **ER GMLRS / PrSM**; Avio discloses **">$500M"** of new **US** capacity investment, announced **10-13** | **§3 — `asset --symbol AVIO` returns 404: Avio is NOT in the US equity universe.** ESTABLISHED FROM SOURCE, not inherited from its 10-07 disposal · **part 1 — LMT is the headline name and the BUYER of capacity** · **part 2 — >$500M is Avio's own CAPEX, capital paid OUT (rule viii); the source states it "does not disclose … expected revenue … or a specific cost impact for Lockheed Martin"** |
| **-02** | **AMD** / Fermi (FRMI) **credit support agreement** backstopping the **222 MW** phase-one Project Matador lease, framework to **650 MW**, announced **10-13** | **part 1 — AMD is a NAMED PARTY to the announcement, so §4's premise does not apply; the second-order sentence needs an "and also"** · **part 2 — source: *"a figure for AMD is not disclosed"*, no AMD segment identified** · **part 3 — the only dollar figure (~$6.5B) is FERMI's revenue over a FIFTEEN-YEAR term** |
| **-03** | **Hormel Foods (HRL)** acquires **Brakebush Brothers** (private, family-held) for **~$1.055B**, closing Q1 FY2027, announced **10-14** | **part 1 — HRL is the headline name AND the payer; no Company B exists (the seller is private and unbuyable, no supplier named)** · **part 2 — form five: consideration paid OUT by the only listed leg, the GEHC/Sofie shape** · **merger activity is not in §4 at all** |
| **-04** | **RTX** — **"up to $8B"** from the **US Air Force Nuclear Weapons Center**, strategic communications modernisation, **10-13** | **rule (iv) — FIFTH RTX appearance in EIGHT sessions, FOURTH distinct award, same death every time** · first-order · **government counterparty is not a Company A** · **"up to" is a CEILING (rule v)** · no supplier below RTX named. **ZERO queries spent** |
| **-05** | **§3 / non-qualifying sweep, NINE items** (Galderma/ZO **SIX-listed** · Chemring/Roke **LSE** + unnamed prime · Alpha Compute **$81.7M**, unnamed customer, signed 10-09 · FFR/FFAI microcaps signed 10-12 · Aegis/Tristar **Indian** · Moreld/**Norwegian MoD** · BigBear.ai below floor, *"options and ceilings rather than earned revenue"* · **LS Electric/Bloom $138,458,284 — an EXACT one-session-old RE-SERVE of `T-2026-10-13-01`** · the **macro complex incl. CPI printing today**) | §3 on six · rule (v) unnamed counterparty on two · rule (iii) on two · jointly unsatisfiable on three · **ZERO follow-up queries spent on any of them** |

⚠⚠ **THE ONE THE HUMAN SHOULD READ IS `-01`, BECAUSE IT IS A NEW DOOR ONTO AN OLD CORRIDOR.**
It is the **thirteenth** US-defence-award instance and the **first** where the mechanism is
sound, the second-order beneficiary **is** named, and the dollar figure **is** real and dated —
**and the beneficiary is simply not listed here.** The previous twelve died because the tier
below the prime is commercially confidential. ⚠ **This one died because the tier below the prime
was named and is ITALIAN. The rule's conclusion is unchanged; its MECHANISM now has two forms,
and only the first is fixable by better questions.**

⚠⚠ **AND THE PRIOR IT SUMMONED POINTS THE WRONG WAY, WHICH IS NEW.** The reflex on any missile
award is **the solid-rocket-motor tier** (NOC/Orbital ATK, L3Harris/Aerojet). ⚠ **But Lockheed is
buying *merchant Italian* capacity precisely because the US incumbents' capacity is constrained,
so the honest read-across is NEGATIVE for them — §3 permits only the long side, and the
"competitor loses relative standing" flip is the shared-cause object. NOT TAKEN: the prior was
wrong in SIGN as well as unnamed.**

⚠⚠ **`-02` ADDS A NEW COSTUME TO RULE (viii) AND IT IS WORTH THE HUMAN'S TIME: A CREDIT BACKSTOP
IS A CONTINGENT LIABILITY ASSUMED BY THE BUYABLE LEG — THE OPPOSITE SIGN FROM REVENUE — AND IT
READS AS A STRONG COMMERCIAL SIGNAL BECAUSE THE MARKET PRICED *FERMI* UP ON IT.** The catalogue
held capital in, capital out, financing ceilings, synergy estimates and consensus misses. **This
is the first *guarantee*, and if it is ever quantified it appears as a RISK, not a sale.**

⚠⚠ **TWELFTH CONSECUTIVE SESSION OF VOLUNTEERED ABSENCE (09-29 → 10-14 UNBROKEN), IN A NEW FORM:
THE STRUCTURAL FRAMING RETURNED SIX ITEMS AND SELF-EXCLUDED ALL SIX IN A TABLE WITH A NAMED
FAILURE AGAINST EACH** — *"no announcement can be confirmed as meeting all criteria
simultaneously."* ⚠ **Both framings were asked, the structural one FIRST, and the announcement
date was demanded inside every prompt — which is how Alpha Compute's 10-09 and FFAI's 10-12
signing dates arrived volunteered rather than hunted.**

⚠⚠ **ZERO `move` CALLS AT THIS SEAT — AN *ABSENT* CHECK, NOT A SKIPPED OR A PASSING ONE — AND
THE CAUSE IS THE 10-13 CAUSE ONE RUNG HIGHER: TWO GENUINELY ELIGIBLE US-LISTED TICKERS REACHED
THE RUN (`HRL`, `AMD`) AND BOTH DIED AT PART 1, WHICH IS UPSTREAM OF THE PRICED-IN FILTER.**
⚠ **A `move` on either would have been DECORATIVE and was declined on that ground — the fifth and
sixth such refusals (SYNA 10-05, CEREBRAS 10-06, no-eligible-ticker 10-12, BE 10-13).**
⚠ **NOT COUNTABLE AS A ZERO-`move` SESSION FROM HERE — THREE SEATS REMAIN TODAY.**

### SELL

**NONE. No satellite position exists to sell.** ⚠ **Core VOO is exempt from all four §5 rules
and is never sold on news (§5, §7).**

### REBALANCE

**NONE.** Core **70.2992%**, inside §2's 65–75% band with **5.30 points** of headroom at the
near edge. ⚠ **See Reconciliation item 4 — `rebalance_delta` −$302.18 is a distance readout, not
an instruction.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate. This plan carries no BUY, no SELL and no REBALANCE intent.**
⚠ **There is therefore NO `revalidate` line in this plan, and that is correct rather than an
omission: the field names the specific number an intent must be re-checked against, and there is
no intent.**

⚠ **Do NOT read an empty plan as permission to skip the gate.** At 09:35:

1. ⚠⚠ **READ `plan_date` OFF THE FIELD. It is `2026-10-14`, and today is 2026-10-14 — FRESH.**
   Do not infer freshness from the fact that the plan is empty. Record which state you had.
   **Non-exercise count 40 after today.** ⚠ **The first morning the gate fires will by
   construction be a morning when the pre-market run failed. Read your own Step 2 then; do not
   recall it.**
2. **Re-read `control.md` from disk.** It was `TRADING_ENABLED: true` with empty notes at 08:21;
   a human may have changed it in the intervening 74 minutes.
3. **Re-check the sleeve band against live equity.** Core was 70.2992% pre-bell; the band test is
   robust to all three price bases, but the reading is not. **If core has left 65–75%, a
   REBALANCE is due even though this plan queues none** — §2 does not depend on the day's
   research and is exempt from the staleness gate.
4. ⚠⚠ **DO NOT OPEN A POSITION THAT IS NOT WRITTEN HERE.** All five of today's candidates are
   REJECTED, not deferred. **A rejection is not a queue, and the funnel is empty.** ⚠ **If the
   09:35 tape makes one of them look attractive, that is a higher price, not new evidence — and
   `-01` through `-04` did not die on price at all, so no price makes them live.**
5. ⚠ **A bar dated TODAY is PARTIAL while the market is open — its `c` is the last trade so far
   wearing a close's clothes.** No operand today (no position will be opened), but **open item 12
   stands: the sound substitute is the PRIOR completed session's close, named on its basis.**

---

## Carried from the research, for the seats that follow

- ⚠⚠ **SEPTEMBER CPI PRINTS TODAY AT 08:30 ET**, PPI and retail sales **10-15**, ASML and TSMC
  later this week. ⚠ **IT IS NOT A LEAD AND NO NEW THESIS ID WAS MINTED FOR IT — it is the same
  disposed object as `T-2026-10-12-05` and `T-2026-10-13-08`.** Its **status** changed (from "the
  forward calendar, nothing has happened yet" to a print landing inside this session); its
  **ELIGIBILITY** did not. **A macro print has ONE party and no transaction — the
  government-action object in a calendar's clothing.** ⚠ **Expect the funnel to re-serve it, and
  expect the bank prints and ASML/TSMC read-across to arrive with it; §4 kills the
  competitor-earnings read-across as the shared-cause object every time.**
- ⚠ **Counters live in `state.md`, not here: thesis 151 → 156, session HELD at 30 / 27.**
