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
plan_date: 2026-11-03
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-11-03 at 09:30 ET** (`alpaca.py clock` at 07:02:16 ET: `is_open:
false`, `next_open: 2026-11-03T09:30:00-05:00`, `next_close: 2026-11-03T16:00:00-05:00`).
**NOT a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean — FALSE has
three meanings and TRUE has one.**

The plan this run replaced was dated **2026-11-02** — the previous trading day, the ordinary
shape. It was fresh when consumed and carried **zero intents**.

---

## ⚠⚠⚠ READ THIS FIRST — THE SEAT CONSUMING THIS PLAN PROBABLY CANNOT EXECUTE

**Routine 2's stored schedule was read on 2026-11-02 and is `13:35:00 UTC` = `08:35 ET`,
against a nominal `09:35 ET`. The 09:30 open is 55 minutes LATER. On 2026-11-02 that seat
dispatched at 08:46:55 ET, read `is_open: false`, and could place nothing.**

⚠ **IF YOU ARE THE OPEN SEAT AND `clock` SAYS `is_open: false`: THAT IS THE EXPECTED,
CONFIRMED CONDITION, NOT A NEW FAULT AND NOT A HOLIDAY.** §7 forbids trading a closed
market. **Placing nothing is CORRECT. The fault is the schedule; the handling is not yours
to fix and the schedule is not yours to change.** Record the firing time and `is_open` as
the first line of your run, log the skip, commit.

⚠⚠ **THIS PLAN CARRIES ZERO BUY INTENTS, SO THE FAULT COSTS NOTHING TODAY — AND THAT IS
EXACTLY WHAT MAKES IT DANGEROUS. A pre-open seat over an empty plan and a correctly-timed
seat over an empty plan are byte-identical in output. The day this plan carries a BUY, the
trade will simply not happen, and nothing in the order count will say why.**

⚠ **The human has been notified four times (11-02 ×3, 11-03 ×1). Nothing has been fixed:
this pre-market seat fired at 07:02 ET again today. DO NOT re-notify on an unchanged item.**

---

## Tape context

**Pre-market readings, and every one of them is a LIVE MIDPOINT, not an official close — do
not stamp any of them into `positions.md` or compare them against a close-basis number.**

- `sleeves` at 07:02: equity **$98,318.18** · core VOO **$68,318.183635 / 69.49%** ·
  satellite **$0 / 0.0%**, count **0** · cash **$30,000.00 / 30.51%** ·
  `core_in_band: true` · `rebalance_needed: false` · `rebalance_delta: 504.54`.
- Core VOO: 99.046311231 sh @ `avg_entry_price` **706.74**, `cost_basis` **$69,999.989999**
  (unchanged since 2026-09-03 — only the mark moves), `current_price` **689.76**,
  unrealised **−$1,681.81 / −2.403%**.
- ✅ **2026-11-02's OFFICIAL CLOSE IS BACKFILLED AND THE CARRY-FORWARD ITEM IS DISCHARGED:
  VOO closed at `c` 691.185** (`bars --days 3 --adjustment all`, `t` 2026-11-02, `v` 58,546,
  `n` 2,239). The 11-02 intraday figures in `state.md` and `journal.md` are **not**
  close-basis and must not be quoted as such.
- ⚠⚠ **AND THE PARTIAL-BAR ERROR IS NOW MEASURED, NOT JUST MECHANISED.** The 11-02 15:15 ET
  close seat's bar read `c` **693.91**; the true close is **691.185** — **an error of $2.725,
  or 0.394%.** **A `highest_close` stamped from that bar would have displaced every later
  §5.4 trailing-stop trigger by 39 basis points for the life of the position.** That seat
  refused to stamp it. **The refusal was right and is now quantified.**
- ✅ **The broker-pair cross-check is RESTORED** (it was unavailable on 11-02 for want of a
  close basis): `lastday_price` **691.32** vs bar `c` **691.185** = **0.135 / 0.0195%**
  disagreement on the same session. Normal venue/consolidation noise, no action.

---

## Intents

### BUY — none

**Zero BUY intents. Three Perplexity queries, five candidates, zero survivors.**

⚠ **This is the §4 honest-broker outcome, not a failed run.** All five are written up in
`research_log.md` as `T-2026-11-03-01` … `-05`. Named here so the open seat does not have to
open that file to know nothing is pending:

| ID | Candidate | Died at |
|---|---|---|
| `T-2026-11-03-01` | memory tier (MU · SNDK · STX · WDC) | **part 1** — Apple remarking on DRAM pricing is *evidence of* a market condition, not a *cause*; the mechanism needs an "and also". **Identical to 11-02's Intel disposition.** |
| `T-2026-11-03-02` | unnamed Apple supply base ($33B) | **rule (v) + part 2** — right sign, real figure, **no named recipient and no component breakdown.** |
| `T-2026-11-03-03` | optical tier (COHR · FN) | **merger arbitrage, not in §4** — a change in who *owns* Lumentum changes nobody's revenue line. |
| `T-2026-11-03-04` | refiners / airlines (Brent −8%) | **part 1** — a commodity price is a market variable; there is no Company A. |
| `T-2026-11-03-05` | sweep, seven items | §3 (×3), government counterparty, three macro objects, one first-order headline name. |

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

**Core 69.49%, inside §2's 65–75% band. `rebalance_needed: false`.**

**Both bounds re-derived from the live share count, not inherited** (99.046311231 sh,
$30,000 cash fixed):
- **65% floor** → VOO at **$562.51**, i.e. **−18.45%** from 689.76.
- **75% ceiling** → VOO at **$908.67**, i.e. **+31.74%** from 689.76.

The target is $68,822.73 and the $504.54 delta is **0.51% of equity** — residual drift
against a moving mark, nowhere near a band edge. **Do not rebalance on the delta; rebalance
on the band.**

---

## Notes for the open seat

1. **Record your firing time and `clock` `is_open` as the first line of your run.** This is
   the only reason any of the schedule faults were ever seen. Keep doing it.
2. **Nothing to execute.** Confirm the plan date, confirm zero intents, confirm the sleeve
   band, log, commit. **A no-trade day is a successful day (§4).**
3. **Do not stamp any pre-market or intraday price into `positions.md`.** There is nothing to
   stamp today — zero satellite positions — but the rule holds the moment that changes.
4. ⚠ **`alpaca.py move` is DIRECTION-BLIND and this is newly characterised today.** It
   thresholds **absolute** 5-session magnitude, so it returned `priced_in: true` / *"LATE —
   skip"* on four names that **FELL** 5–14% (MU −7.77%, SNDK −14.40%, STX −7.87%, WDC
   −4.96%). §4's words are *"moved more than 4% **on this news**"*. **It over-blocks and can
   never wrongly PERMIT, so it is safe to keep obeying — but a `priced_in: true` reading must
   NOT be quoted as "the market has already captured this upside."** Prompt/script-level
   finding; **not a seat's to change.**
