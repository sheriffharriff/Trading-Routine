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
plan_date: 2026-11-04
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-11-04 at 09:30 ET** (`alpaca.py clock` at 07:02:42 ET: `is_open:
false`, `next_open: 2026-11-04T09:30:00-05:00`, `next_close: 2026-11-04T16:00:00-05:00`).
**NOT a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

The plan this run replaced was dated **2026-11-03** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

---

## ⚠⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Routine 2's stored schedule was read on 2026-11-02 and is `13:35:00 UTC` = `08:35 ET`,
against a nominal `09:35 ET`. The 09:30 open is 55 minutes LATER. On 2026-11-02 that seat
dispatched at 08:46:55 ET and on 2026-11-03 at 08:36 ET; both read `is_open: false` and
could place nothing.**

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED,
CONFIRMED CONDITION, NOT A NEW FAULT AND NOT A HOLIDAY.** §7 forbids trading a closed
market. **Placing nothing is CORRECT. The fault is the schedule; the handling is not yours
to fix and the schedule is not yours to change.** Record the firing time and `is_open` as
the first line of your run, log the skip, commit.

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS
EXACTLY WHAT MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed
seat over an empty plan are byte-identical in output. The day this plan carries a BUY, the
trade will simply not happen, and nothing in the order count will say why.** **This is now
the THIRD consecutive EST session in that condition.**

⚠ **The human has been notified six times (11-02 ×3, 11-03 ×1 on this item plus 1 on the
`move` defect naming this as context, and four prior). Nothing has been fixed: this
pre-market seat fired at 07:02 ET again today. DO NOT re-notify on an unchanged item — and
DO NOT read the silence as the fault having been fixed.**

---

## Tape context

**Pre-market readings, and every one of them is a LIVE PRINT, not an official close — do not
stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 07:02: equity **$99,431.46** · core VOO **$69,431.464173 / 69.83%** ·
  satellite **$0 / 0.0%**, count **0** · cash **$30,000.00 / 30.17%** ·
  `core_in_band: true` · `rebalance_needed: false` · `rebalance_delta: 170.56`.
- Core VOO: 99.046311231 sh @ `avg_entry_price` **706.74**, `cost_basis` **$69,999.989999**
  (unchanged since 2026-09-03 — only the mark moves), `current_price` **701.00**,
  unrealised **−$568.53 / −0.8122%**.
- ⚠ **`current_price` 701.00 is a PRE-MARKET PRINT at +1.0713% over the official 11-03 close
  and the day is 2½ hours from opening. It is quoted here as context and nowhere as a close.**
- ✅ **2026-11-03's OFFICIAL CLOSE IS BACKFILLED AND THE CARRY-FORWARD ITEM IS DISCHARGED:
  VOO closed at `c` 693.57** (`bars --days 4 --adjustment all`, `t` 2026-11-03, `v` 34,539,
  `n` 1,628). **Close-basis 11-03: equity $98,695.55 · day +$236.23 / +0.2399% · since
  inception −1.3044%.** The 11-03 intraday figures in `state.md` and `journal.md`
  ($98,641.08 / +0.1710%) are **not** close-basis and must not be quoted as such.
- ⚠⚠⚠ **AND THE PARTIAL-BAR ERROR INVERTED SIGN, WHICH REPLACES THE INHERITED READING.**
  11-02: partial **693.91** vs true **691.185** = **+$2.725 / +0.3943% TOO HIGH.**
  11-03: partial **692.93** vs true **693.57** = **−$0.64 / −0.0923% TOO LOW.** **It is not a
  bias and cannot be corrected for.** The 11-03 close seat found the partial-bar *volume*
  signature inverted across the same two sessions; **the error itself inverts too — two
  inversions in one pair of sessions, on both quantities a seat might use to rescue a stamp.**
  ⚠ **The only reliable completeness detector is the CLOCK.**
- ✅ **Broker-pair cross-check run:** `lastday_price` **693.54** vs bar `c` **693.57** =
  **$0.03 / 0.004%** — the tightest pair on record, normal venue noise. Neither stamped.

---

## Intents

### BUY — none

**Zero BUY intents. Three Perplexity queries (one of them a drill), five theses, zero
survivors.**

⚠ **This is the §4 honest-broker outcome, not a failed run.** All five are written up in
`research_log.md` as `T-2026-11-04-01` … `-05`. Named here so the open seat does not have to
open that file to know nothing is pending:

| ID | Candidate | Died at |
|---|---|---|
| `T-2026-11-04-01` | alternative auto power/analog tier (TXN · ADI · MCHP · NXPI) ← onsemi diverting capacity from automotive to AI | **rule (v) + part 2** — a DIVERSION names only the party GIVING UP the revenue. onsemi never quantified the deferred automotive volume (its auto line fell **1%** sequentially, the whole measured hole), and no peer has named onsemi. **The source volunteered the kill.** |
| `T-2026-11-04-02` | **PNW** ← TSMC's 25-year, 1.88 GW Arizona power contract | **part 3 / rule (vi)** — *"at full build-out"*, 25-year term, **subject to regulatory approval**: ~40+ quarters vs §4's two. **Part 2 fails independently — the commitment is in GIGAWATTS, no dollar figure exists.** ⚠ **PART 1 PASSED CLEANLY — first clean part-1 pass since 10-30.** |
| `T-2026-11-04-03` | ON / Ferric, $600M + $175M contingent | **rule (viii)** — consideration paid OUT by the buyable leg to a private seller. The GEHC/Sofie shape unchanged. |
| `T-2026-11-04-04` | own-prior-figure sweep (Spartan Delta · SM Energy · Mowi · Ferroglobe) | **§3 (×2, TSX and Oslo) · rule (v) · rule (vi) · rule (iii)** — ⚠ **three clean rule (iii) passes in one call and every one died elsewhere.** |
| `T-2026-11-04-05` | sweep, eleven items (Talen · Metallus · Atlas · Cabot · CVR/Marathon · Energy Transfer · Solvay · ASTA · JOLTS · Fed/GDP · the midterms) | own-results prints (×6), one acquisition, unnamed counterparties, macro/political objects. **Zero drill queries spent.** |

**`revalidate` — nothing to re-check.** ⚠ **There are no BUY intents, so there is no number
for the open seat to re-validate. This line is present and empty ON PURPOSE: an absent
`revalidate` line and an empty one are different things, and the open seat should be able to
tell "nothing pending" from "a field was forgotten."**

### SELL — none

**Zero satellite positions exist, so all four §5 rules are ABSENT, NOT PASSING — there is no
operand to test.** Reconciled three ways at 07:02 and re-derived, not inherited: Alpaca
`positions` = one row (core VOO only) · `positions.md` satellite block count **0** ·
`sleeves` `satellite.count: 0`. **No discrepancy.**

⚠ **No Perplexity news query was spent checking a position's invalidation condition, because
there is no position and no invalidation condition to check.**

### REBALANCE — none

**Core 69.83%, inside §2's 65–75% band. `rebalance_needed: false`.**

**Both bounds re-derived from the live share count, not inherited** (99.046311231 sh,
$30,000 cash fixed):
- **65% floor** → VOO at **$562.51**, i.e. **−19.76%** from 701.00 (**−18.90%** from the
  693.57 close).
- **75% ceiling** → VOO at **$908.67**, i.e. **+29.62%** from 701.00.

Core is **$4,801.02 above the floor** and **$5,142.13 below the ceiling** — ⚠ **the nearer
edge is still the FLOOR, eighth consecutive seat, though the gap narrowed on today's
pre-market strength.** The target is $69,602.02 and the **$170.56 delta is 0.1715% of
equity** — residual drift against a moving mark, nowhere near a band edge. ⚠ **Do not
rebalance on the delta; rebalance on the band. The delta is a DISTANCE READOUT, NOT AN
INSTRUCTION.**

---

## Notes for the open seat

1. **Record your firing time and `clock` `is_open` as the first line of your run.** This is
   the only reason any of the schedule faults were ever seen. Keep doing it.
2. **Nothing to execute.** Confirm the plan date, confirm zero intents, confirm the sleeve
   band, log, commit. **A no-trade day is a successful day (§4).**
3. **Do not stamp any pre-market or intraday price into `positions.md`.** There is nothing to
   stamp today — zero satellite positions — but the rule holds the moment that changes, and
   today's **+1.07% pre-market print** is exactly the kind of number that invites it.
4. ⚠ **`alpaca.py move` is DIRECTION-BLIND, and it fired for a THIRD consecutive session
   today: ON at **−7.69%** returned `priced_in: true` / *"LATE — skip"*.** Running tally:
   **INTC −24.36% · MU −7.77% · SNDK −14.40% · STX −7.87% · WDC −4.96% · ON −7.69%** —
   **six "LATE" verdicts on six DECLINES.** §4's words are *"moved more than 4% **on this
   news**"*. **It over-blocks and can never wrongly PERMIT, so keep obeying it — but a
   `priced_in: true` reading must NOT be quoted as "the market has already captured this
   upside."** Script-level; **not a seat's to change.** Reported to the human 11-03.
5. ⚠⚠ **TODAY SEPARATED THE TWO HALVES OF THAT POINT IN ONE RUN, AND IT IS WORTH CARRYING:
   PNW PASSED the priced-in filter (+2.25%) and died anyway at part 3; ON FAILED it and was
   already dead at rule (v) before the filter ran.** **A hard-filter pass is not progress
   toward a trade, and the filter was not what disqualified anything today.**
