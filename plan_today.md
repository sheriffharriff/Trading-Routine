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
plan_date: 2026-09-25
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-09-25 at 09:30 ET** (`alpaca.py clock` at 08:24:08 ET: `is_open:
false`, `next_open: 2026-09-25T09:30:00-04:00`, `next_close: 2026-09-25T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. **Read the date, not the boolean.** FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.

**One pre-market run today, at 08:24 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$100,299.16**).

**Today is also a weekly-review day (routine 5)**, and the last review before the
**2026-10-02 monthly archive rollover**. `research_log.md` grew to **~333KB** this run.

---

## Tape context

Yesterday's **official** VOO close, from `bars --adjustment all`, is **707.28** (09-23:
707.28 — identical to the cent, verified last run as a real coincidence with distinct OHLV;
09-22: 712.69; 09-21: 712.76; 09-18: 701.85).

⚠ **THE `lastday_price` PREDICTION RESOLVED ON ITS INFORMATIVE BRANCH — AND THE FIELD IS
WRONG IN A FOURTH WAY.** The carry-forward set out three readings in advance: **707.60 ⇒ it
never rebuilt (informative); 707.28 ⇒ AMBIGUOUS and not to be logged as a clean rebuild;
anything else ⇒ wrong in a fourth way.** ⚠ **It reads 706.99.** That is the third branch.
**The field DID rebuild — it moved off the 707.60 it had held through four consecutive reads
on 09-24 — and it rebuilt to 706.99, which is 29 cents BELOW the official 707.28 and matches
no recent official close** (09-22 712.69, 09-21 712.76, 09-18 701.85, 09-17 700.97 — none is
706.99).
⚠ **Writing the prediction down in advance is what made this readable at a glance, and it is
the first time the pre-registered branches have paid off on the branch that was hardest to
argue after the fact.** ⚠ **The error has now been observed in BOTH SIGNS: +32c on 09-24,
−29c today. There is no offset to correct for, no refresh point to rely on, and no sign to
predict. The field is unusable, and "it rebuilt" is not evidence it is right — on both
mornings it rebuilt, it was wrong.**

The broker's pre-market `positions` row reads `current_price` **709.7605** — **a pre-market
midpoint, not a close and not an execution reference** — with `change_today` **+0.00392** and
`unrealized_intraday_pl` **+$274.41** computed off the wrong 706.99 baseline. **None of those
were used in or carried into any figure in this plan.** **`bars --adjustment all` for a
close, a fresh `quote` for execution, never a `positions` field for either, and never
`equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

The core shows `unrealized_pl` **+$299.17 / +0.427%** against the 706.74 fill, on a pre-market
mark. **§5 exempts core from all four sell rules, so no action attaches to that number in
either direction.**

---

## Sleeves and the rebalance question

**State which basis produced any figure you quote** — last run established that the two can
disagree in *sign* on `rebalance_delta`.

| Basis | Equity | Core | Core % | Cash % | `rebalance_delta` |
|---|---|---|---|---|---|
| **Broker marks** (`sleeves`, 08:24) | $100,299.16 | $70,299.16 | **70.09%** | 29.91% | **−$89.75** |
| **Official 09-24 close** (707.28 × 99.046311231) | $100,053.48 | $70,053.48 | **70.016%** | 29.984% | **−$16.04** |

⚠ **NO REBALANCE IS DUE, ON EITHER BASIS.** §2 rebalances at the **65/75 band edge**, not to
the exact target. The core sits **4.91 points** from the nearest edge on broker marks and
**4.98** on official closes. `core_in_band: true`, `rebalance_needed: false`.
⚠ **Note the two bases AGREE IN SIGN today** (both negative, core above target) — unlike
09-24, where they disagreed. **That is not a sign the defect has gone away; it is a sign it
is intermittent, which is worse.** **Forty-third consecutive run inside the range
69.59–70.22.**

Cash is **$30,000.00 flat** — unchanged since the 09-03 core fill.

---

## Position review — §5

**There are zero open satellite positions.** `alpaca.py positions` returns **one row, core
VOO**, 99.046311231 shares at avg_entry 706.74, cost_basis $69,999.99 — unchanged since the
09-03 fill.

**RECONCILIATION CLEAN.** Zero satellite blocks in `positions.md` against zero satellite
Alpaca rows — they agree. *(Satellite-to-satellite, never raw ledger to raw broker: the core
is deliberately untracked in `positions.md` because §5 exempts it.)*

**§5.1–§5.4 have no operand — the THIRTY-FOURTH consecutive session.** No thesis to
invalidate, no timing window to expire, no entry price to measure a −7% hard stop from, no
`highest_close` to measure a −10% trailing stop from. ⚠ **§5.4 is STILL NOT ARMED**; it arms
on the first **satellite** fill, and the 09-03 core fill was not one. **The running tally of
"no exits" records the ABSENCE OF A SUBJECT, not thirty-four clean bills of health. All four
remain UNTESTED CODE PATHS.**

**High-water marks: nothing to backfill, and nothing was skipped.** `highest_close` is
**ABSENT — the third state, carrying no `(as of …)` date at all.** ⚠ **Yesterday's close run
had no `highest_close` to stamp because there is no field, not because it failed. Do not read
the missing stamp as a failed close run.** **Zero `bars` calls were due on any satellite
symbol and zero were made.**

---

## Intents

### BUY

**NONE.**

⚠ **Every gate that could have blocked a buy was OPEN, and nothing was blocked.** Circuit
breaker **INACTIVE**; `new_positions_this_week` **0 of 3**; satellite sleeve **empty** with
**~30% idle cash**; `control.md` notes **(none)**; `TRADING_ENABLED: true`. **Research ran in
full and produced no eligible candidate.** Per §4, that is a successful run, not a failed one.

**Six candidates reached a `research_log.md` entry and all six were rejected:**

| ID | Candidate | Killed by |
|---|---|---|
| T-2026-09-25-01 | **JBL** (Jabil) | **Part 2** — the $1.7B is capital paid IN, held on consignment, repurchased **at cost**. Not segment revenue at Company B. |
| T-2026-09-25-02 | **AKAM** (Akamai) | **First-order** — the company in the headline. |
| T-2026-09-25-03 | memory suppliers (no ticker) | **Rule (v)** — no supplier named in any disclosure; and <10% of revenue for any of them even if named. |
| T-2026-09-25-04 | **RDW** (Redwire) | **Ceiling** — $980M is a multiple-award ceiling across **15 vendors**, no Redwire allocation; also first-order; also below the §3 floor. |
| T-2026-09-25-05 | **FLNC** (Fluence) | **No value or volume disclosed**; supplier is Shenzhen-listed. |
| T-2026-09-25-06 | rate/oil/PMI complex (no ticker) | **Environment input, not a Company A.** |

⚠⚠ **READ T-2026-09-25-01 BEFORE ANY FUTURE RUN REACHES FOR THIS CHAIN.** The Akamai/Anthropic
deal produced exactly what open item (3) has said for a month never arrives — **a named
US-listed supplier with a specifically allocated dollar figure, quoted verbatim from an
8-K.** And it still produced nothing, because **the figure was the wrong quantity**: Akamai
paying Jabil's supplier invoices for components **Jabil holds in consignment as bailee and
repurchases at cost.** ⚠ **That is a FIFTH form of open item (3)'s binding constraint, and
the only one that no widening of the evidence bar would relieve — widening it would have let
this through.**

⚠ **AND THE PRICED-IN FILTER IS NOT THE REASON FOR THE JBL REJECTION.** It fired first
(`priced_in: true`, +4.97%), as §4 requires, but on a **five-session grind whose largest
single day was +1.72% and whose news day moved JBL +0.63%** — a rise unrelated to the news.
**That is a THIRD defect shape for open items (1) and (2)** and it is the human's to resolve.
⚠ **The agent did not act on it: a correct reading of §4's "on this news" wording is still a
`strategy.md` change, and this was precisely the setup that rule guards against — a candidate
the agent had begun to like plus a technical argument that the filter misfired. The bar does
not move from this seat.**

### SELL

**NONE.** No satellite positions exist. §5 has no operand.

### REBALANCE

**NONE.** Core is in band on both bases (70.09% broker / 70.016% official; band 65–75%).
⚠ **Do not act on `rebalance_delta` — §2 rebalances at the band edge, and the core is ~4.9
points inside it.**

---

## For the market-open run

**Zero BUY intents, so ZERO `move` re-validation calls are due. That is an ABSENT check, not
a skipped one** — record it that way.

⚠ **The staleness gate: this plan is dated 2026-09-25 and today's ET date is 2026-09-25, so
it is FRESH.** ⚠ **But note what that does and does not tell you: a FRESH EMPTY plan and a
STALE plan produce a byte-for-byte identical zero-order run. Read `plan_date`, never the
outcome.** The gate has been exercised **twenty-seven times and has never fired**; its alert
path **remains untested code**, and the first morning it fires will by construction be a
morning when this run failed — i.e. the morning with no fresh notes to lean on. **Read
routine 2's Step 2 then; do not recall it.**

**Bootstrap is permanently closed** (`core_established: true`). **Do not re-run it.**

⚠ **Open item (7) is live but unexposed, as always: `alpaca.py move` cannot see an after-hours
event, and neither can the 09:35 re-validation that exists to catch exactly that. It has cost
zero only because no plan has yet carried a BUY intent — an absence of exposure, not a
mitigation.** ⚠ **This run supplied new and sharper evidence for it: AKAM moved +12.35% in a
single session on 09-21 and gave back 6.74% on 09-24, netting to a +3.19% `priced_in: false`
"pass." A five-session window can hide an entire event move behind a later give-back, and no
re-validation at 09:35 would have surfaced it.**
