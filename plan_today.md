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
plan_date: 2026-10-13
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-13 at 09:30 ET** (`alpaca.py clock` at 08:26:35 ET: `is_open:
false`, `next_open: 2026-10-13T09:30:00-04:00`, `next_close: 2026-10-13T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** Both `next_open` and `next_close` carry **today's**
date, which is the full-session signature: not an early close.
⚠ **The data plane agrees, which corroborates the DISCRIMINATOR and not any bar's
completeness: `bars --days 4 --adjustment all` returns **NO bar dated 2026-10-13**, the same
pre-market shape seen at 08:23 on 10-06 before the 09:36 seat watched the bar appear.**

**One pre-market run today, at 08:26 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$100,820.09** at pre-flight).

⚠⚠ **THIS FILE ARRIVED CARRYING `plan_date: 2026-10-12` — ONE trading day and ONE calendar
day old, the ORDINARY shape, and exactly what the 10-12 close seat predicted in writing.**
⚠ **Said plainly because the shape this seat has read about most is the MONDAY one, where a
correct plan arrives THREE calendar days old. That is not today's. Compare `plan_date` to the
LAST TRADING DAY every time, rather than to the shape you remember reading about.**
⚠⚠ **AND THE REASON TO SAY IT AGAIN: A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A
BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. Freshness is read OFF `plan_date` and NEVER inferred
from the outcome.** The predecessor was fresh and deliberately empty, and so is this one.
**The staleness gate's non-exercise count will be 39 after today's open; it has never fired,
and its alert path remains untested code.**

⚠ **THE PREVIOUS FIVE SESSIONS WERE ALL COMPLETE — all four seats of 10-06, 10-07, 10-08,
10-09 and 10-12 ran and committed.** ⚠⚠ **THAT IS NOT A FIX AND A RUN OF FIVE IS NOT EVIDENCE
ABOUT TODAY IN EITHER DIRECTION.** Two close runs have vanished (09-28, 10-05); a run that
dies before `commit.py` leaves no trace by construction, so **`alerts.md` reading "zero open
incidents" is not evidence that every seat ran.** There is still no detector.

---

## Tape context

**Last official close, 2026-10-12** (`bars --adjustment all`): VOO **c 715.315**, o 715.80,
h 716.29, l 714.28, **n 1,393 / v 32,547**, vw 715.141777. Prior session 10-09 closed
**715.58**.
⚠ **ONE OBSERVATION, REPORTED AND NOT RECONCILED: `n`/`v` read 1,392/32,544 at the 10-12
16:17 close seat and 1,393/32,547 a minute later. This morning it reads 1,393/32,547 —
BYTE-IDENTICAL to the second reading. The late-print drift SETTLED overnight,** which is a
fact about settlement timing and not about any §5 input: `o`/`h`/`l`/`c`/`vw` never moved.

**Account, 08:27 ET:** equity **$100,813.16**, `last_equity` 100,830.98855062503, cash
**$30,000.00**, `accrued_fees` 0, `balance_asof` **2026-10-12** (advanced), `trading_blocked`
false.

⚠⚠ **TWO EQUITY READINGS MINUTES APART WITH NO ORDER IN THE INTERVAL: `selftest`/`sleeves`
$100,820.09 and `account` $100,813.16 — $6.93 apart.** The pre-market mark MOVES. **Name the
basis or do not write the number**, and do not difference successive readings to infer a
change: 10-12 produced four `rebalance_delta` samples retracing themselves inside one day
with no order placed.

⚠ **§6 CAP, BOTH BASES NAMED: 5% of `account` equity $100,813.16 = $5,040.66; 5% of
`sleeves` equity $100,820.09 = $5,041.00. The 09:35 seat must recompute it off ITS OWN live
equity rather than inherit either figure.**

---

## Reconciliation

1. **LEDGER AGREES WITH THE BROKER.** `positions.md` holds **zero satellite blocks** and
   `alpaca.py positions` returns **one row, VOO** (99.046311231 sh, avg_entry 706.74,
   market_value $70,820.093456, unrealized_pl +$820.10 / +1.172%). **No disagreement to
   resolve, so no research was done on top of a ledger known to be wrong.**
2. **ORDERS: `orders --status all` still returns ONE ROW for the whole account history** —
   the 2026-09-03 core fill, terminal. ⚠ **§7's non-terminal-order warning therefore has NO
   OPERAND rather than a clean bill of health.**
3. **SLEEVES:** core **$70,820.093456 / $100,820.09 = 70.2441%**, satellite **0.0%** (count
   **0**), cash **$30,000.00 = 29.76%**. `core_in_band: true`, `rebalance_needed: false`,
   `rebalance_delta` **−$246.03**. ⚠ **That delta is a DISTANCE READOUT, NOT AN INSTRUCTION
   — §2's band is 65–75% and core sits 5.24 points inside the near edge. 83rd consecutive
   in-band run.**
4. **HOUSEKEEPING, re-derived at this seat and not inherited:** week anchor **RECOMPUTED** —
   today is **Tuesday**, ISO week 42 weekday 2, Monday anchor **2026-10-12** — and found
   **MATCHING** `week_of`, so `new_positions_this_week` was **DELIBERATELY NOT RE-RESET** and
   stands at **0 of 3**. Breaker **INACTIVE**, `halt_triggered_at: none`, so **no
   `HALT_CLEARED_AT` comparison was due** (`control.md` has it at `none` anyway).
   `consecutive_closed_losses` **0 and UNTOUCHED — zero closes means the update was never
   reached, not that a counter was reset.** `control.md` notes **EMPTY**. Zero open alerts.

---

## §5 sell-rule review

**NO OPERAND. Zero open satellite positions, so all four rules are ABSENT, not passing.**

Evaluated in order anyway, as §5 requires, and reaching each one rather than inheriting it:

- **§5.1 thesis invalidation** — no open thesis, so no invalidation string exists to test.
  **Zero Perplexity news checks were run on held names because there are no held names.**
- **§5.2 time stop** — no `timing_window`, no deadline.
- **§5.3 hard stop (−7% from entry)** — no satellite `entry_price`. **Distance UNDEFINED, not
  large.**
- **§5.4 trailing stop (−10% from `highest_close`)** — **no `highest_close` field exists at
  all.** ⚠ **This is the third state: the field is ABSENT, not stale and not fresh.**
- **Core VOO was struck from the working list BEFORE any rule was read** — §5 exempts core
  from all four and §7 forbids selling it on news.

⚠⚠ **DO NOT STAMP CORE VOO WITH A `highest_close`.** Writing one would **arm a §5.4 trailing
stop on the one position §5 exempts**, which §7 forbids outright. **This run is the 92nd
consecutive one declining it** (the 10-12 16:17 close seat was the 91st). ⚠ **The temptation is structural, not accidental: VOO is the
only row the broker returns, this seat holds a real official close on the correct basis, and
the field is empty — every ingredient for writing it is present except permission.**

---

## Intents

### BUY

**NONE. ⚠⚠ ZERO BUY INTENTS, AND NOT BECAUSE ANYTHING BLOCKED THEM.**

⚠ **Every §6 and §7 gate was OPEN and this must not be lost between here and 09:35:** breaker
**INACTIVE** · `new_positions_this_week` **0 of 3** · satellite sleeve **0% deployed** against
a 30% target with **$30,000 idle cash** · `control.md` notes **empty** · `TRADING_ENABLED:
true` · §6's 5% cap standing ready at **$5,040.66** (`account` basis). **A buy was placeable
all morning. Nothing was worth buying, and an empty plan is a complete instruction rather
than a gap to fill.**

**Eight candidates were researched and all eight were rejected** (`T-2026-10-13-01` … `-08`).
The kills, one line each, so the 09:35 seat need not re-read the log to know nothing is
pending:

| ID | Candidate | Test that failed |
|---|---|---|
| **-01** | **Bloom Energy (BE)** / LS Electric **$138,458,284** 38-kV switchgear order, announced 10-13, deliveries Apr–Jul 2027, for a fuel-cell data-centre project in Pennsylvania | **part 1 — the ONE US-listed party is the *PAYER*; the mechanism cannot be written in the direction §3 permits without an "and also" clause** · **part 2 — form five: the figure is disclosed and is the WRONG QUANTITY (capital paid OUT), and BE's project revenue is undisclosed** · **rule (v) — the data-centre owner is UNNAMED** |
| -02 | **EnergyX / Trafigura** — binding 10-yr take-or-pay, 100k t lithium, *"more than $2.0B"*, 10-12 | **§3 in one step — BOTH PARTIES PRIVATE.** The structural framing's **second** false positive: full shape, failed **PARTY TYPE** |
| -03 | **Enovix (ENVX)** — prelim Q3 rev ~$11M vs $9.5M consensus, EPS −$0.14 vs −$0.16, **$19M** Korea expansion, 10-12 | **part 1 — source denied any second company outright** · **part 2 — JOINTLY UNSATISFIABLE: $19M cannot be 10% of revenue at any company above the $10B floor.** First-order name |
| -04 | **BP** — Q3 impairments **$3.0–4.5B** (gas & low-carbon), production 2.190–2.240 mmboe/d, 10-13 | **part 1 twice — no Company B by volunteered absence, AND the only sound mechanism points DOWN, which §3 cannot express.** The competitor-benefits flip is the **shared-cause object** and was NOT taken |
| -05 | **Equinox Gold (EQX)** — Q3 237,019 oz, South Railroad **Record of Decision + final federal permits**, 10-13 | **part 1 — source denied any second company** · **part 2 — OUNCES not dollars, no capital figure attributed to any contractor (form six), and jointly unsatisfiable even if one existed** |
| -06 | **Technip Energies / HPCL** refinery EPC, **€250–500M**, 10-13 | **§3 — neither party US-listed** · **part 2 — a BAND is not a figure, and the source said it enters *"backlog, not … a quantified impact on that segment's revenue"*. A BOOKING IS NOT A DOLLAR PATH** |
| -07 | **§3 / non-qualifying sweep, ELEVEN items** (ARREF **OTC** · Torm · Bachem · Aequs/Safran · IRCON · BEL · Hiteck/Visara *"up to"* · Bluejay/Toray no figure · Saudi Steel Pipe/Aramco · Al-Yamamah · ADSB/Kuwait MoD) | §3 non-US, OTC or private · no disclosed figure on three · governmental counterparty on two · **ZERO follow-up queries spent** |
| -08 | the **FORWARD CALENDAR** (JPM/C/WFC reporting **today** · CPI 10-14 · PPI + retail sales 10-15 · ASML/TSMC preview, EUV capacity 65/85/110 machines 2026/27/28) | **nothing has happened yet — rule (iii) at its earliest possible failure point.** Already rejected on 10-12 as `T-2026-10-12-05`; the ASML lines are a **roadmap**, and 2027/28 is outside the two-quarter ceiling |

⚠⚠ **THE ONE THE HUMAN SHOULD READ IS `-01`, AND IT IS A NEW COSTUME OF RULE (v): AN UNNAMED
*CUSTOMER* CARRYING A MAP PIN, A DELIVERY SCHEDULE AND A PRODUCT SPEC.** A real transaction, a
real dollar figure to the cent, a real dated delivery window — **and the beneficiary whose
economics actually change is withheld as *"a major U.S. technology company."*** ⚠ **Unlike
Synaptics' "Party A", it is withheld by a THIRD party's release rather than by its own filing,
so there is not even a filer obliged to name it later.** ⚠⚠ **THE PULL WAS REAL AND IS
RECORDED: the list of eligible US-listed technology companies building Pennsylvania data
centres is short, and naming one would have been a GUESS DRESSED AS A DEDUCTION. NO GUESS WAS
MADE AND NONE IS RECORDED AS A CANDIDATE.**

⚠⚠ **AND THE SECOND FINDING, WHICH IS ABOUT METHOD: THE PARTY-TYPE AND UNIT TESTS ADDED TO THE
STRUCTURAL FRAMING ON 10-12 HAVE NOW FIRED ON CONSECUTIVE SESSIONS.** 10-12's false positive
was two **sovereign states** and a **tonnage**; today's (`-02`) is two **private companies**
and a price-derived estimate. ⚠ **"It returned the shape" is still not grounds to proceed to a
mechanism — and the framing is not weakened, because it also disposed of four items with the
reason attached for zero follow-up queries.**

⚠⚠ **THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE FOR AN ELEVENTH CONSECUTIVE SESSION, AND
TODAY IN ITS STRONGEST FORM: four qualifying events in ONE query, and *"No second publicly
traded US company is named by the source as directly affected"* written out FOUR TIMES, once
each for ENVX, BP, EQX and ARREF.** The segment-quantification framing added *"the evidence
provided supports **zero confirmed matches**, rather than a constructed list of likely
candidates"* — ⚠ **the source declining to manufacture candidates in the same breath in which
§4's honest-broker paragraph warns me not to.**

⚠⚠ **ZERO `move` CALLS AT THIS SEAT — AN *ABSENT* CHECK, NOT A SKIPPED OR A PASSING ONE, and
the cause is cleaner than any prior instance: the one US-listed party in the one transaction
of the day is the PAYER, so the candidate died at part 1 UPSTREAM of the filter and no
eligible ticker ever reached it.** ⚠ **A `move` call on BE would have been DECORATIVE —
declined on that ground for the fourth time (SYNA 10-05, CEREBRAS 10-06, no-ticker 10-12, BE
today).** ⚠ **NOT COUNTABLE AS A ZERO-`move` SESSION FROM HERE — THREE SEATS REMAIN TODAY.**

### SELL

**NONE. No satellite position exists to sell.** ⚠ **Core VOO is exempt from all four §5 rules
and is never sold on news (§5, §7).**

### REBALANCE

**NONE.** Core **70.2441%**, inside §2's 65–75% band with **5.24 points** of headroom at the
near edge. ⚠ **See Reconciliation item 3 — `rebalance_delta` −$246.03 is a distance readout,
not an instruction.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate. This plan carries no BUY, no SELL and no REBALANCE intent.**
⚠ **There is therefore NO `revalidate` line in this plan, and that is correct rather than an
omission: the field names the specific number an intent must be re-checked against, and there
is no intent.**

⚠ **Do NOT read an empty plan as permission to skip the gate.** Specifically, at 09:35:

1. ⚠⚠ **READ `plan_date` OFF THIS FIELD. It is `2026-10-13`, and today is 2026-10-13 —
   FRESH.** Do not infer freshness from the fact that the plan is empty — **a fresh empty plan
   and a stale plan produce a byte-for-byte identical zero-order run.** Record which one you
   had. **Non-exercise count 39 after today.** ⚠ **The first morning the gate fires will by
   construction be a morning when the pre-market run failed. Read your own Step 2 then; do not
   recall it.**
2. **Confirm all eight thesis IDs `T-2026-10-13-01` … `-08` are present and REJECTED in
   `research_log.md`** before concluding there is nothing to execute. **None is a buy
   candidate.** ⚠ **`-01` is the only one carrying a US-listed ticker (BE) and it is there as
   the PAYER — it is not a shelved candidate and must not be revived at a quote.**
3. **Step 3's core bootstrap is skipped on `core_established: true`** — a path that ran once on
   2026-09-03 and by construction never runs again. **Do not re-bootstrap.**
4. **Re-check sleeves on live numbers.** If core has left the 65–75% band overnight, §2's
   rebalance is **exempt from the plan_date gate** and is yours to place. At 08:26 it was
   70.2441% with 5.24 points of headroom at the near edge, so this is a check, not an
   expectation. ⚠ **Recompute §6's 5% cap off your own live equity — two readings minutes
   apart this morning differed by $6.93.**
5. ⚠⚠ **DO NOT STAMP CORE VOO WITH A `highest_close`.** A mark on VOO would **fabricate a
   §5.4 trailing stop on the one position §5 exempts**, which §7 forbids outright. **This will
   be the 93rd consecutive run declining it.**
6. ⚠ **TODAY'S PRINTS ARE NOT TOMORROW'S LEAD EITHER.** JPM/C/WFC report this morning and CPI
   lands 10-14. When they arrive they are **first-order events on scheduled reporters**, and
   §4 kills the competitor read-across as the shared-cause object. **A reporting date is not a
   lead, and neither is a reported number without a second company named against it.**
