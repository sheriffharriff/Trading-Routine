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
plan_date: 2026-09-24
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-09-24 at 09:30 ET** (`alpaca.py clock` at 08:20:51 ET: `is_open:
false`, `next_open: 2026-09-24T09:30:00-04:00`, `next_close: 2026-09-24T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. **Read the date, not the boolean.** *(Yesterday's 16:16 close run read the
identical `is_open: false` with `next_open` pointing at **2026-09-24**. Same boolean,
opposite meaning; only the date discriminates. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.)*

**One pre-market run today, at 08:20 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, equity **$99,776.15**).

**Tape context.** Yesterday's **official** VOO close, from `bars --adjustment all`, is
**707.28** (09-22: 712.69; 09-21: 712.76; 09-18: 701.85). The broker's pre-market `positions`
row reads `current_price` **704.48** and `lastday_price` **707.60**.

⚠ **THE CARRY-FORWARD MADE A CONCRETE, FALSIFIABLE PREDICTION ABOUT THIS FIELD AND IT CAME
OUT THE OTHER WAY. REPORTED AS SUCH.** Yesterday's `state.md` said, in terms: *"today's
official close is 707.28. If `lastday_price` still reads 712.78 tomorrow morning it is $5.50
WRONG."* **It does not read 712.78. It reads 707.60 — the field DID rebuild at this session
boundary.** ⚠ **That falsifies the 09-23 finding that `lastday_price` "does not rebuild at the
session boundary," which had itself falsified the 09-22 finding that it does.** **Both
generalisations are now dead.** The field rebuilds sometimes and not others, and **two
consecutive runs each drew a confident structural rule from a single observation and each was
wrong.** ⚠ **This is the standing "audit every inherited claim" rule paying for itself a
FOURTH time, and the second time the falsified claim was a MECHANISM rather than a count.**

⚠ **AND IT REBUILT TO A WRONG NUMBER — 32 CENTS HIGH, THE LARGEST `lastday_price` ERROR IN THE
RECORD.** 707.60 against an official 707.28. The prior series ran **7c low, 2c high, 9c high**;
**32c is more than three times the worst of them.** ⚠ **Read the two facts together and the
conclusion is worse than either alone: rebuilding is not a sign of correctness. The one
morning the field refreshed is the morning it was furthest off.** There is **no offset to
correct for, no refresh point to rely on, and no sign to predict.**

Consequently the broker's day figures are unusable as usual: it reports `change_today`
**−0.00441** and `unrealized_intraday_pl` **−$309.02** off the 707.60 baseline. **Neither was
used in nor carried into any figure in this plan.** **`bars --adjustment all` for a close, a
fresh `quote` for execution, never a `positions` field for either, and never
`equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

The core shows `unrealized_pl` **−$223.84 / −0.32%** against the 706.74 fill. **§5 exempts
core from all four sell rules, so there is no action attached to that number in either
direction**, and it is a pre-market broker mark in any case — **`current_price` 704.48 is a
pre-market midpoint, not a close, and not an execution reference.**

---

## The whole plan in one line

**Do nothing.** No BUY, no SELL, no REBALANCE. Core is in band at **69.93%**, there are **no
satellite positions to manage**, and **seven candidates were researched to a thesis entry and
all seven were rejected.**

---

## Intents

### BUY — none

No buy intents. New positions were **fully permitted** this run — breaker **INACTIVE**, weekly
cap at **0 of 3**, satellite sleeve **empty with 30.07% cash**, no restricting note in
`control.md`. ⚠ **Nothing was blocked. The research did not produce an eligible candidate.**

**No `revalidate` line is written, and none is due.** Re-validation has a subject only when a
BUY intent exists. ⚠ **Zero `alpaca.py move` calls are due at 09:35 — an ABSENT check, not a
skipped one.** *(Five `move` calls were made **at this run**, on PYPL, BBY, SHOP, ILMN and
GRAL, as §4 hard filters against live candidates. None produced an intent, so none carries
forward to 09:35.)*

Seven candidates reached a `research_log.md` entry:

| Thesis | Candidate | Died at | Why |
|---|---|---|---|
| T-2026-09-24-01 | **ILMN** | **§4 priced-in**, then **part 3** | **FDA advisory committee voted in favour of GRAIL's Galleri PMA, 09-23 — non-binding, final FDA decision pending.** Illumina is the structurally necessary named supplier, which makes this the most genuinely second-order shape of the week. ⚠ **+11.54% over five sessions → `priced_in: true`, "LATE — skip". A genuine RISE, not an artefact — the filter working.** ⚠ **The thesis was NEVER WRITTEN: the filter ran first, per §4, and killed a story that was already half-built.** Part 3 kills it independently — vote → PMA decision (undated) → reimbursement → ramp is several quarters past the horizon. **Does not become a buy at a lower price.** |
| T-2026-09-24-02 | **GRAL** | **first-order**, plus **§4** | The company **in** the headline. §4 is a *second*-order strategy and GRAIL is Company A. ⚠ **+44.67% over five sessions — the largest five-session move ever recorded against a candidate in this log, eleven times the threshold.** Logged rather than skipped because **the biggest mover on the tape is the most tempting thing on an empty sleeve.** |
| T-2026-09-24-03 | **BBY** | **part 2** | **Meta unveiled Muse agent shopping at Connect 2026, 09-23**, naming **Walmart, Best Buy, Gap, Sephora, Wayfair**, plus Ulta, Fanatics, DICK'S, AEO, Michael Kors. ⚠ **Part 1 passes CLEANLY — one clause, direct causal path — and that is exactly why the entry matters.** Part 2 is unwritable: a dedicated terms query returned **no revenue share, no minimum guarantee, no dollar value, no volume commitment, no take rate** from any party. ⚠ **And rule (viii) cuts the wrong way — the only economics described is Meta taking "a small fee from transactions," a COST at the retailer.** Priced-in **−0.71%, PASSES — and the pass is NOT the reason for anything.** |
| T-2026-09-24-04 | **PYPL** | **part 2** | Same event; PayPal named as a supported checkout rail. ⚠ **The rail thesis always has a clean part 1, which is what makes it the most seductive shape in this strategy.** No **TPV**, no **take rate**, no **launch volume**, no **date**. ⚠ **A segment that is ~90% of revenue does not rescue a numerator of zero.** Priced-in **−0.38%, PASSES — not the reason.** ⚠ **Would have FAILED the correlation check against BBY had either been eligible: identical driver, one bet in two tickers.** |
| T-2026-09-24-05 | **SHOP** | **§4 priced-in**, plus **part 2** | Same event; Shop Pay and Shopify catalogue access named. ⚠ **+9.61% over five sessions → `priced_in: true`. Second rise-based firing of the morning.** Part 2 fails identically to PYPL's, so **this is not a price-only rejection and SHOP does not become a buy on a pullback.** *(An unresolved §3 question — Shopify is a Canadian issuer trading as US-listed common stock — was **not decided**, because two kills landed first. **A future run reaching it with a live candidate must put it to the human.**)* |
| T-2026-09-24-06 | **SoftBank / OpenAI** | **part 2 — no Company B exists** | **$11.1B of senior notes issued 09-24**, $10B funding the final tranche of a $30B follow-on investment in **OpenAI**, closing 10-01. ⚠ **Asked directly, no source names ANY publicly traded US company as a recipient with an allocated amount.** The recipient is **private**. **Largest number of the morning by an order of magnitude and it is capital paid IN** (rule viii). ⚠ **The compute-supplier inference is available and obvious, and rule (v) exists to stop exactly it: the source left the blank, and filling it in is not research.** Same object as Nscale's $103B and Bloom's $25B. |
| T-2026-09-24-07 | **ELMT** | **§3** | **Elmet ↔ Masan High-Tech Materials (Vietnam)** — long-term tungsten supply and conversion plus a **4.99% stake for $124.75M**, 09-23. ⚠ **A genuinely NEW transaction, not a re-covering of yesterday's Tungsten West offtake — rule (iii) checked and does not apply.** **ELMT ~$634M against a $10B floor; Masan Vietnam-listed. Both legs fail §3.** No `move` call was made — a candidate below the floor is ineligible at any price. ⚠ **Second Elmet event in two sessions, both killed by the same structural floor. A third headline is not a third opportunity.** |

⚠ **THE FINDING OF THE DAY IS NOT A THESIS — THE §4 PRICED-IN FILTER FIRED ON THREE GENUINE
RISES, AND THAT IS THE FIRST TIME IN VOLUME THE RECORD HAS SHOWN IT DOING ITS DESIGNED JOB.**
SHOP **+9.61%**, ILMN **+11.54%**, GRAL **+44.67%**. Open item (1) has accumulated **nine
instances of the filter reading a DRAWDOWN as priced-in** plus three near-misses, and the sheer
weight of that record makes the filter easy to read as broken. ⚠ **It is not broken; it is
SIGN-BLIND, and today is the same defect seen from the working side.** **Recorded prominently
and deliberately, because the narrative accumulating in these files runs one way, and a system
that only ever logs the filter's failures is building a case rather than keeping a record.**
⚠ **The implication for the human: the fix to open items (1) and (2) is to make the filter read
SIGN — not to loosen it or remove it. Today is evidence FOR the first and AGAINST the second.**

### SELL — none

⚠ **NO SUBJECT EXISTS.** `positions.md` holds **zero satellite blocks** and
`alpaca.py positions` returns **one row, core VOO** (99.046311231 shares, avg_entry 706.74,
unchanged since the 09-03 fill). §5.1 (thesis invalidation) and §5.2 (time stop) were **not
evaluated because there is nothing to evaluate** — no invalidation condition has ever been
written in this account, so there is nothing to falsify. **Zero `perplexity.py` news-check
calls were due on the §5.1 path and zero were made.**

⚠ **Read that precisely: this is the ABSENCE OF A SUBJECT, not a clean bill of health.** §5.1
through §5.4 remain **untested code paths**, thirtieth consecutive session. **§5.4 is not
armed** — it arms on the first **satellite** fill, and the 09-03 core fill was not one.
`sell_rule_status` is **ABSENT rather than blank**, and `highest_close` is **ABSENT — the third
state, carrying no `(as of …)` date at all**, which is exactly what proves no backfill is owed.

**Core VOO is not a candidate for any sell rule and is not listed here.** §5 exempts it.

### REBALANCE — none

**Core is IN BAND.** `alpaca.py sleeves` at 08:20 ET: equity **$99,776.15**, core
**$69,776.15 = 69.93%**, satellite **$0 = 0.0% (count 0)**, cash **$30,000.00 = 30.07%**,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +67.16`.

⚠ **§2 rebalances at the 65/75 BAND EDGE, not to the exact 70% target, so no delta inside the
band is an action at any size.** The shortfall is **0.07% of equity against a band edge 4.93
points away.** **Thirty-ninth consecutive run inside a 0.63-point range (69.59–70.22).**

⚠ **THE SIGN OF `rebalance_delta` FLIPPED — NOTE IT AND DO NOT ACT ON IT.** Every recent run
carried a **negative** delta (core *above* target); today's is **+$67.16** (core *below*).
**That is the core sleeve falling with the tape, not a drift requiring action**, and it is the
**smallest absolute delta in the series** — the closest the core has been to its 70% target
since it was established.

---

## Notes for the 09:35 run

- ⚠ **This plan is FRESH and EMPTY, and those are TWO SEPARATE FINDINGS.** A fresh empty plan
  and a stale plan produce an **identical zero-order run**, which is why the §2 gate is decided
  on **`plan_date`** and never on the outcome. **Check the date. Do not infer freshness from
  the fact that there was nothing to do.**
- ⚠ **The staleness gate has now been exercised 26 times and has NEVER fired; its alert path
  remains UNTESTED CODE.** Twenty-six quiet opens are **not** evidence it works. **The first
  morning it fires will, by construction, be a morning when the pre-market run failed — i.e.
  exactly the morning with no fresh notes to lean on. Read routine 2's Step 2 then; do not
  recall it.**
- **`core_established: true`** since 09-03. **Step 3's bootstrap path is permanently closed.**
  Do not invoke `--core`.
- ⚠ **Idle cash of 30.07%, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
  opportunity routine 2 may act on.** Routine 2 executes **only what this file contains**. A
  position opened at 09:35 without a plan entry routes **around** the discipline rather than
  satisfying it. **There are no BUY intents. That is the instruction.**
- ⚠ **DO NOT REHABILITATE ANY OF TODAY'S SEVEN REJECTIONS AT THE OPEN. A rejection is not a
  queue.** None becomes eligible at a different price: **ILMN and SHOP fail part 2/part 3 as
  well as on price; GRAL is first-order; BBY and PYPL have no disclosed commercial term to
  build a dollar path from; SoftBank/OpenAI has no US-listed recipient; ELMT is below the §3
  floor.**
- ⚠ **`lastday_price` reads 707.60 against an official 707.28 — it DID rebuild overnight, and
  it rebuilt to a number 32 CENTS WRONG, the largest error this field has produced.**
  **Rebuilding is not a sign of correctness.** Use `bars --adjustment all` for any close and a
  fresh `quote` for any execution reference. `current_price` 704.48 is a pre-market midpoint.
- ⚠ **A `perplexity.py` call returned HTTP 500 this morning after a green selftest, recovering
  on retry.** Open item (6) — the selftest does not probe the data plane — **now has an instance
  on the RESEARCH plane, which is where it matters most**, because a silently empty research run
  reads exactly like a quiet news day. **Check exit codes; do not infer thin news from empty
  results.** Single transient occurrence, **no alert raised.**
- **`alerts.md` is empty — zero open incidents, zero SYSTEMIC.** Nothing operational needs
  flagging to the human today beyond the standing open items in `state.md`.
