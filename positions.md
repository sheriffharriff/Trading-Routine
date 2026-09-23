# Open Positions Ledger

**AGENT-OWNED.** One block per open **satellite** position. The core holding is not
tracked here — it is never sold on news (§5) and needs no thesis state.

Alpaca is authoritative for what is held and at what cost. This file exists for the
things Alpaca does not store and that §5 cannot be enforced without:

- the **highest close since entry**, without which the §5.4 trailing stop does not exist
- the **timing window deadline**, without which the §5.2 time stop never fires
- the **invalidation condition**, verbatim, because §7 forbids softening it later —
  keeping it written down is what makes softening visible

**High-water maintenance:** the market-close routine writes every open position's official
close into `highest_close` each day (only if it is higher). If a close run was skipped, the
next run must backfill from `python scripts/alpaca.py bars --symbol X --days N` before
evaluating §5.4. A gap in this field silently disables the trailing stop, which is the kind
of failure that looks like nothing is wrong.

---

## Template

```
### <TICKER> — <thesis-id>

- entry_date:            YYYY-MM-DD
- entry_price:           0.00
- qty:                   0.000
- notional_at_entry:     0.00
- pct_of_account_entry:  0.0%
- voo_close_at_entry:    0.00  (adjustment=all — the same-period baseline for this position)
- asset_type:            stock | etf
- market_cap_at_entry:   $00.0B
- market_cap_source:     <where the figure came from>
- highest_close:         0.00  (as of YYYY-MM-DD)
- timing_window:         <next earnings | Q_ YYYY>  → deadline YYYY-MM-DD
- invalidation:          <verbatim from the thesis, part 4 — never reworded>
- sell_rule_status:      <which of §5.1–5.4 are near triggering, and the distance to each>
- driver:                <the underlying catalyst, for the §4 correlation check>
```

The `driver` line is what makes the correlation check possible. Before opening anything new,
the pre-market routine reads every `driver` here and rejects a candidate exposed to the same
one — otherwise you are making a single bet spread across several tickers and mistaking it
for diversification.

`voo_close_at_entry` is recorded once, at entry, and never updated. The Friday review needs
each position measured against what the same capital would have done in VOO over that
position's own holding window; capturing the baseline at entry means the review never has to
re-derive it from price history, and it stays correct for positions closed months later.

---

## Open positions

*(none — no **satellite** positions have been opened yet. Core VOO exists and is deliberately not tracked here, per the top-of-file rules and the fill note further down.)*

**Reconciliation 2026-09-23 — ALL FOUR RUNS (1-premarket 08:20, 2-open 09:36, 3-midday 12:44,
4-close 16:16 ET). LEDGER AGREES WITH THE BROKER AT ALL FOUR; ZERO SATELLITE POSITIONS ON BOTH SIDES;
NO ORDER PLACED AT ANY; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE; NO §5 RULE HAD A SUBJECT.**
*(**One block per date, not one per run** — the open, midday and close runs each **updated this block
in place** rather than adding a second. **Collapse, do not append — forty-seventh consecutive run.**)*

---

**THE 16:16 CLOSE RUN — THE HIGH-WATER STEP THIS ROUTINE EXISTS FOR, AND IT HAD NO SUBJECT.**

Selftest passed all five checks (`trading_enabled: true`, LIVE paper); pre-flight equity **$100,055.46**.
`clock` at **16:16:15** reads **`is_open: false`** with `next_open` **2026-09-24T09:30** — the
**post-bell** shape. The boolean is identical on a holiday; only the date discriminates, and the third
discriminator was checked directly: **a VOO daily bar for 2026-09-23 exists** (c **707.28**, n 3,960),
so a real session happened.

**⚠ STEP 2 WAS A NO-OP FOR THE TWENTY-NINTH SESSION, AND THAT IS NOT THE SAME AS PASSING.** This file
carries **zero satellite blocks**; `alpaca.py positions` returns **one row, core VOO**, 99.046311231
shares, avg_entry 706.74, cost_basis 69,999.99, market_value 70,055.46 — unchanged since the 09-03 fill.
`highest_close` is **ABSENT — the third state, carrying no `(as of ...)` date at all** — which is exactly
what proves no mark was owed and none went stale. ⚠ **Zero `bars` calls were due FOR A HIGH-WATER MARK
and none was made for one.** The single `bars --adjustment all` call this run issued was for the **core
close**, to compute the day's P&L without touching a broker field — a different purpose, and core is
not a §5.4 subject. **§5.4 remains NOT ARMED**; it arms on the first **satellite** fill, and the 09-03
core fill was not one.

**⚠ THE SENTENCE THIS STEP MUST NOT WRITE — CAUGHT IN DRAFT.** "High-water marks updated, nothing
moved" is true of a book whose closes did not exceed their marks and **false here, where there are no
marks.** Those two states are the precise pair Step 2 exists to keep apart, and the wrong one is the
more natural sentence. The distinction is **free today and stops being free the moment a satellite fill
lands** — after that, a mark silently not written reads identically to a mark correctly unchanged, and
only the `(as of ...)` date separates them.

**NOTHING CLOSED, NOTHING IS IN LIMBO.** `orders --status all` returns **one row for the account's
entire history** — the 09-03 core VOO buy, `status: filled`, terminal. No order has ever reached a
non-terminal state here, so nothing carries overnight per §7 and `trade_log.md` was correctly left
unappended. `consecutive_closed_losses` stays **0** — it has never had an input.

**TWO-PRICE DEFECT — THIRD POST-BELL INSTANCE, AND IT RECONCILES EXACTLY.** `current_price` **707.30**
against the official **707.28** — **2 cents HIGH**. `lastday_price` **712.78** for the **fourth time
today** (08:20, 09:36, 12:44, 16:16), still **nine cents high** against 712.69, still never rebuilt. The
broker's `equity − last_equity` is **−$542.77** where the true close-to-close is **−$535.84**;
⚠ **the $6.93 gap decomposes perfectly — 99.046311231 × $0.09 (stale baseline) − 99.046311231 × $0.02
(high midpoint) = $8.91 − $1.98 = $6.93.** Both legs wrong at once in opposite directions, reconciling
against each other, which is why **no check internal to the broker's fields can surface either.**
**Neither field was used in any figure this run reported.** ⚠ **Post-bell record now runs 22c LOW
(09-21), 16.9c HIGH (09-22), 2c HIGH (09-23) — same routine, same minute of the day, no predictable
sign and no correctable offset.**

---

**THE 12:44 MIDDAY RUN — THE §5.4 BACKFILL STEP HAD NO SUBJECT, AND THAT IS NOT THE SAME AS PASSING.**

Selftest passed all five checks (`trading_enabled: true`, LIVE paper); pre-flight equity **$100,095.07**,
`sleeves` equity **$100,085.07** moments later. `clock` at **12:44:41** reads **`is_open: TRUE`**,
`next_close` **2026-09-23T16:00** — the unambiguous shape, mid-session.

**⚠ STEP 2 IS THE REASON THIS ROUTINE EXISTS, AND IT WAS A NO-OP FOR THE TWENTY-EIGHTH SESSION.** The
routine's own framing is that a missed close run leaves `highest_close` stale, silently disabling the
§5.4 trailing stop while every other check still passes. **There was nothing to check.** `positions.md`
carries **zero satellite blocks**, so `highest_close` is **ABSENT — the third state, carrying no
`(as of ...)` date at all** — which is precisely what proves no backfill was owed. **Zero `bars` calls
were due and zero were made.** ⚠ **A staleness check with no field to read is an ABSENT check, not a
clean one, and the ABSENT state is the only one that can be distinguished from a stale one without
reading a date.** The moment a satellite fill lands, this step acquires a subject and the distinction
stops being free.

**⚠ STEP 3 HAD NO OPERAND — ALL FOUR §5 RULES ITERATE OVER OPEN SATELLITE POSITIONS AND THERE ARE
ZERO.** §5.1 has no `invalidation` string to falsify because none has ever been written, so **zero
`perplexity.py` news calls were due on that path and zero were made** — this run issued **no research
call of any kind**, and routine 3 has no research step for one to land in. §5.2 has no `timing_window`,
§5.3 no `entry_price`, §5.4 no `highest_close`. **Twenty-eighth session with §5.1–§5.4 never started;
§5.4 remains NOT ARMED.** The string of "no exits" lines across this account's history records **the
absence of a subject, not four rules returning clean** — they remain untested code paths.

**STEP 4 — ZERO EXITS, ZERO ORDERS OF ANY KIND.** No `sell` was submitted, so there was no
`"terminal": false` to chase and no `"dry_run": true` to flag. ⚠ **The loudest line this routine can
produce — a stop that should have fired and did not — HAS NO INSTANCE HERE, and the reason is that
nothing could fire, not that everything was checked and held.** `consecutive_closed_losses` stays **0**,
nothing has ever closed, breaker **INACTIVE**, `halt_triggered_at` **none**, so **no `HALT_CLEARED_AT`
comparison was required and no circuit-breaker alert was due.** `open_thesis_ids` stays `none` — no
thesis ID to strike.

**STEP 5 HAD NOTHING TO REFRESH.** `sell_rule_status` is **ABSENT rather than blank** on a file with no
position blocks. Writing a distance-to-rule line here would require inventing an entry price.

**⚠ THE MIDDAY RUN MAY NOT OPEN A POSITION, AND THE CONDITIONS THAT MAKE THAT TEMPTING WERE ALL
PRESENT.** Satellite sleeve **0.0%**, cash **29.97%**, weekly cap **0 of 3 unused**, breaker INACTIVE,
no restricting note in `control.md`. **Idle capital is not an opportunity this seat may act on**: the
routine is exits-only by construction, and a midday entry would route around the pre-market thesis and
the 09:35 execution path, which is the discipline rather than an obstacle to it. **Nothing was bought.**

**TWO-PRICE DEFECT — `lastday_price` READS 712.78 FOR THE THIRD TIME TODAY.** The identical stale value
at 08:20, 09:36 and now 12:44, **nine cents high** against the official 712.69. `current_price` **707.655**
is a live midpoint, not a close. The broker reports `change_today` **−0.00719** and
`unrealized_intraday_pl` **−507.61**, both computed off the stale 712.78 baseline; **707.655 against the
official 712.69 is −0.706%**, so the broker **overstates today's decline by about 1.3 basis points**.
⚠ **Neither field was used nor carried into any figure in this run.** Cosmetic on core, which §5 exempts;
**load-bearing the day a satellite position exists.** Always `bars --adjustment all` for a close.

**GNRC NOT LOOKED AT — EIGHTEENTH REFUSAL, AND A FREE ONE.** This run made `clock`, `positions` and
`sleeves` calls only and issued **no `quote`, `bars`, `move` or `asset` call on any symbol**, so the
symbol data plane was **shut** and no costume had a vehicle. **Reported honestly: a refusal on a run
that could not have used the number is weaker evidence than one on a run that could.** The
disqualifying facts are unchanged — **GNRC is the named counterparty in the Amazon announcement,
first-order, outside §4 at any price.**

---

**THE 09:36 OPEN RUN — WHAT IT DID, AND WHAT IT WAS NOT PERMITTED TO DO.**

Selftest passed all five checks (`trading_enabled: true`, LIVE paper); pre-flight equity **$100,485.32**,
`sleeves` equity **$100,491.25** moments later. ⚠ **Two broker marks six dollars apart at two instants —
that is the tape moving, not a discrepancy, and neither is a close.**

`clock` at **09:36:18** reads **`is_open: TRUE`**, `next_close` **2026-09-23T16:00**, `next_open`
**2026-09-24T09:30**. ⚠ **This is the FOURTH and ONLY UNAMBIGUOUS SHAPE — the one case where the boolean
alone settles it, and it is safe to read it that way ONLY because TRUE has a single meaning while FALSE
has three** (pre-market, post-bell, holiday).

**⚠ THE §2 STALENESS GATE WAS EXERCISED AND DID NOT FIRE — TWENTY-FIFTH TIME, STILL NEVER FIRED.**
`plan_date` reads **2026-09-23**; the ET date is **2026-09-23**, taken from `TZ=America/New_York` rather
than assumed from the run's own clock. **MATCH — every intent in the file was executable, and the file
contained none.** ⚠ **This run is the sharpest demonstration yet of why the gate reads the DATE: it
submitted ZERO ORDERS, which is exactly what a FIRED gate produces too. A fresh empty plan and a stale
plan are indistinguishable in the order count, and the only thing separating them is a line that anyone
reasoning from the outcome would never have looked at.** The alert path **remains untested code.**

**STEP 3 — BOOTSTRAP PERMANENTLY CLOSED.** `core_established: true` since 09-03. **`--core` was not
invoked at any point in this run**, on either side.

**⚠ STEP 4 HAD NO OPERAND TWICE OVER.** The plan carried **zero SELL intents**, and there are **zero open
satellite positions** to apply §5 against. **No exit was re-confirmed because none was proposed and none
was possible.** Nothing closed, nothing has ever closed — `consecutive_closed_losses` stays **0**, no
`HALT_CLEARED_AT` comparison was required, and **no circuit-breaker alert was due.**

**⚠ STEPS 5 AND 6 HAD NO SUBJECT, AND THE ABSENCE IS THE RECORD.** Zero BUY intents means re-validation
has nothing to re-validate: **ZERO `alpaca.py move` calls were due at 09:35 and ZERO were made.** ⚠ **An
ABSENT check, not a skipped one — and the plan said so in advance**, which is what makes the distinction
checkable rather than asserted. **None of the six 09-23 rejections (GIS, LH, CNC, ELMT, LHX, GFS) was
re-screened or rehabilitated at the open. A rejection is not a queue.**

**⚠ IDLE CASH WAS NOT AN OPPORTUNITY THIS SEAT MAY ACT ON.** 29.85% cash, breaker **INACTIVE**, weekly
cap **0 of 3 unused**, no restricting note in `control.md` — **nothing was blocking a trade, and that is
precisely the condition under which the scope rule does its work.** Routine 2 executes **only what
`plan_today.md` already contains**; a position opened at 09:35 without a plan entry routes **around** the
discipline rather than satisfying it.

**STEP 7 — NO REBALANCE.** `sleeves` at 09:36: equity **$100,491.25**, core **$70,492.25 = 70.15%**,
satellite **0.0% (count 0)**, cash **$30,000.00 = 29.85%**, `core_in_band: true`, `rebalance_needed:
false`, `rebalance_delta: −148.38`. §2 rebalances at the **65/75 band edge, not to the exact target**, so
**no delta inside the band is an action at any size** — 0.15% of equity above target against a band edge
**4.85 points away**. **Thirty-sixth consecutive run inside a 0.63-point range (69.59–70.22).**

**NOTHING IS IN LIMBO — CHECKED DIRECTLY.** `orders --status all` returns **one row for the account's
entire history**: the 09-03 core VOO buy (`d177d8f0-cd0c-41bf-95c1-4772318265fd`, `status: filled`,
terminal). **No order has ever reached a non-terminal state in this account** (§7). `trade_log.md`
correctly left unappended — **a run with no fill writes no trade entry.**

**⚠ THE TWO-PRICE DEFECT, CONFIRMED INTRA-SESSION AND NOW WITH A COST ATTACHED.** `lastday_price` at
09:36 reads **712.78 again** — the **identical** nine-cents-high value the 08:20 run found, which itself
was the identical value the field carried all day on 09-22. ⚠ **It did not rebuild at the session
boundary and has not rebuilt since the open. Both halves of this field's behaviour are now settled, and
neither favours it.** ⚠ **The broker's day figures inherit that staleness:** it reports `change_today`
**−0.00149** and `unrealized_intraday_pl` **−$104.99**, computed from 712.78. Against the **official**
close of **712.69**, `current_price` **711.72** is **−$0.97/share = −0.136%** — so the broker
**OVERSTATES today's decline by nine cents a share, ≈$8.92 on the core.** ⚠ **Every prior instance had
the broker running HIGH on the day; this one runs LOW. The sign is still not predictable.** **Neither
field was used or reported by this run**, and `current_price` **711.72** is an intraday midpoint, not a
close, in either direction.

**CORE VOO DELIBERATELY NOT STAMPED — FORTY-FIFTH RUN.** ⚠ **Graded honestly, this one is cheap: the
open run pulled no `bars` call at all, so there was no close in hand to be tempted by.** A refusal only
costs something on a run that was holding the number.

**⚠ GNRC NOT LOOKED AT — SEVENTEENTH REFUSAL, AND IT IS A WEAK ONE.** This run issued `clock`, `sleeves`,
`positions` and `orders` and **no `move`, `quote`, `bars` or `asset` call on any symbol.** The symbol data
plane was **shut**, so the refusal was **FREE** — it belongs with 09-22's 09:36 and 12:40 runs, not with
this morning's pre-market refusal made against a live funnel. ⚠ **The count accumulates fastest on exactly
the runs where it means least, because routines 2, 3 and 4 have no research step. Seventeen is not
seventeen equal observations.** The disqualifying facts do not move: **GNRC is first-order in the Amazon
announcement, outside §4 at any price.**

**ZERO `perplexity.py` calls and none due — routine 2 generates no ideas, by construction.** The gap
between 08:20 and 09:35 is the point of the design, not a gap in coverage.

**WEEK ROLLOVER RE-CHECKED AT THE OPEN — ANCHOR MATCHED.** Wednesday **2026-09-23**, ISO Monday
**2026-09-21**, `week_of` already **2026-09-21**. **Tenth consecutive run to find the reset already
done**; `new_positions_this_week` stays **0 of 3**. Next boundary **Monday 2026-09-28**.
**`alerts.md` empty — zero open incidents, zero SYSTEMIC.**

---

**THE 08:20 PRE-MARKET RUN (preserved):**

Selftest passed all five checks (`trading_enabled: true`, LIVE paper account); pre-flight equity
**$100,504.14**. `clock` at **08:20:08** reads `is_open: FALSE` with `next_open`
**2026-09-23T09:30** and `next_close` **2026-09-23T16:00** — ⚠ **the PRE-MARKET shape: `next_open`
points at TODAY.** Yesterday's 16:15 close run read the **identical boolean** with `next_open` pointing
at **2026-09-23**. **Same boolean, opposite meaning; only the date discriminates.** **Not a holiday —
the market opens in 70 minutes and today's plan is owed.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree.** Compare
**satellite to satellite**, never raw ledger to raw broker; the core is deliberately untracked here per
§5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares, unchanged; no order
has touched it since the 09-03 fill**, twenty-one sessions ago, avg_entry **706.74**, cost_basis
**$69,999.99**, market_value **$70,504.14**.

**§5 EVALUATION HAD NO OPERAND, AND THAT IS THE ENTIRE RESULT.** Routine 1 owes §5.1 (thesis
invalidation) and §5.2 (time stop) properly, and owes the **distance** to §5.3/§5.4 recorded under
`sell_rule_status`. **All four iterate over open satellite positions; there are zero.** ⚠ **No
invalidation condition has ever been written in this account, so §5.1 has nothing to falsify — zero
`perplexity.py` news-check calls were due on that path and zero were made.** `sell_rule_status` is
**ABSENT rather than blank**, and `highest_close` is **ABSENT — the THIRD STATE, distinct from "stale"
and from "current-and-unchanged"**, carrying **no `(as of …)` date**, which is exactly what proves **no
backfill is owed.** **Twenty-seventh consecutive session with §5.1–§5.4 never started; §5.4 is NOT
ARMED** — it arms on the first **satellite** fill and the 09-03 core fill was not one.

**CORE VOO DELIBERATELY NOT STAMPED — FORTY-FOURTH RUN.** §5 exempts core from all four sell rules. A
`highest_close` on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
exempts** — a stop that could eventually sell core on a drawdown, which §7 forbids outright. ⚠ **This
run held a clean official close (712.69) in hand for sleeve arithmetic, which is the pre-market version
of the temptation.** Refused. ⚠ **Noted honestly, as it was yesterday: this refusal is now close to
automatic, and automatic is not the same as sound.**

**⚠ THE TWO-PRICE DEFECT PRODUCED A GENUINELY NEW SHAPE THIS MORNING: `lastday_price` DID NOT REBUILD
AT THE SESSION BOUNDARY.** Yesterday's **official** VOO close (`bars --adjustment all`) is **712.69**.
The broker's 08:20 `positions` row reads `lastday_price` **712.78** — ⚠ **NINE CENTS HIGH, and it is
the IDENTICAL value the field carried all day yesterday**, when it was two cents high against 09-21's
close of **712.76**. ⚠ **The field did not rebuild; it carried the same stale number across a session
boundary and became MORE wrong, because the underlying close moved and the field did not.**
⚠ **Yesterday's carry-forward recorded, as a settled fact, that the previous instance "DID clear at the
session boundary — this is a fresh one built on the new day's close." TODAY'S DID NOT CLEAR. The
session boundary is NOT a reliable refresh point**, which removes the last piece of structure anyone
might have used to reason about this field. `current_price` reads **711.83**, an intraday/pre-market
midpoint and not a close in either direction. **Standing rule unchanged: `bars --adjustment all` for a
close, a fresh `quote` for execution, never a `positions` field for either, and never
`equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

**SLEEVES IN BAND; NO REBALANCE QUEUED FOR THE OPEN.** `alpaca.py sleeves`: equity **$100,504.14**,
core **$70,504.14 = 70.15%**, satellite **0.0% (count 0)**, cash **$30,000.00 = 29.85%**,
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: −151.24`. §2 rebalances at the
**65/75 band edge, not to the exact 70% target**, so **no delta inside the band is an action at any
size** — the overshoot is **0.15% of equity against a band edge 4.85 points away**. **Thirty-fifth
consecutive run inside a 0.63-point range (69.59–70.22).**

**WEEK ROLLOVER CHECKED — ANCHOR MATCHED, NO RESET DUE.** Today is Wednesday **2026-09-23**; its ISO
Monday is **2026-09-21** and `week_of` already reads **2026-09-21**. **Ninth consecutive run to find
the reset already done** — `new_positions_this_week` stays **0 of 3**. Next boundary **Monday
2026-09-28**. **That is the mechanism working, not a skipped check.** Breaker **INACTIVE**,
`halt_triggered_at: none`, so **no `HALT_CLEARED_AT` comparison was required**; nothing has ever closed,
so `consecutive_closed_losses` stays **0**.

**RESEARCH RAN IN FULL AND PRODUCED NO TRADE.** New positions were **fully permitted** — breaker
INACTIVE, weekly cap 0 of 3, sleeve empty, no restricting note in `control.md`. **Six Perplexity scans;
six candidates reached a full thesis entry; all six rejected** (T-2026-09-23-01 GIS, -02 LH, -03
CNC/MOH/OSCR, -04 ELMT, -05 LHX, -06 GFS). ⚠ **The six-session GIS carry item is DISCHARGED — the print
arrived, was screened, and died at the PREMISE rather than at the rule (iii) fight the carry note
anticipated: an own-results print has one party and §4 needs two.**

**⚠ GNRC NOT LOOKED AT — SIXTEENTH CONSECUTIVE REFUSAL, AND THIS IS THE STRONG TEST THE CARRY-FORWARD
NAMED.** Yesterday's file predicted the eleventh costume would arrive **at this run specifically**,
because routine 1 **opens the data plane AND has somewhere to put a number** — unlike the close run,
where the costume had nowhere to go. ⚠ **The prediction was right about the setup: this run issued
`move --symbol LH` and `move --symbol CNC` on one command line, against a live funnel, making
`--symbol GNRC` one flag on a command already being typed.** It was not added. ⚠ **Reported precisely:
NO NEW ELEVENTH COSTUME APPEARED. The pull arrived in its already-catalogued form — "screen-already-
running" wearing "zero-marginal-cost" — which is a fact about the pattern, not a gap in the watch.**
The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon announcement,
first-order and outside §4 at any price**, and open item (7) is resolved by **a human editing §4 or
`alpaca.py move`**, not by a number this seat collects. Costumes so far: diligence, curiosity, tidiness,
completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
screen-already-running.

---

**Reconciliation 2026-09-22 — ALL FOUR RUNS (1-premarket 08:15, 2-open 09:36, 3-midday 12:40,
4-close 16:15 ET). LEDGER AGREES WITH THE BROKER; ZERO SATELLITE POSITIONS ON BOTH SIDES; NO ORDER
PLACED AT ANY RUN; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE.**
*(**One block per date, not one per run** — the close run **updated this block in place** rather than
adding a fifth. **Collapse, do not append — forty-third consecutive run.**)*
All four selftests passed all five checks (`trading_enabled: true`, LIVE paper account); pre-flight
equity read **$100,649.73** / **$100,742.84** / **$100,558.61** / **$100,606.05**. ⚠ **Those four
figures are broker marks at four different instants, not four closes — the spread between them is the
tape moving, plus the midpoint defect below. The day's P&L is derived from neither end of them.**

**`clock`: `is_open: TRUE` at 09:36:04 and 12:40:50; `is_open: FALSE` at 16:15:55 with `next_open`
2026-09-23T09:30 and `next_close` 2026-09-23T16:00.** ⚠ **The 16:15 read is the POST-BELL shape, not a
holiday, and the boolean alone cannot tell them apart.** Pre-market reads FALSE with `next_open`
**today**; post-bell reads FALSE with `next_open` **tomorrow**; a holiday reads FALSE with `next_open`
**past the holiday and no bar for today**. **Only in the TRUE case does the boolean settle it. In the
FALSE case, read the date — and the close run confirmed the third discriminator directly: a VOO daily
bar for 2026-09-22 EXISTS, so a session happened.** **Today was a full trading day. The daily summary
is owed.**

**Satellite blocks (zero) checked against satellite Alpaca positions (zero) — they agree, at all four
runs.** Compare **satellite to satellite**, never raw ledger to raw broker; the core is deliberately
untracked here per §5. `alpaca.py positions` returns **one row, VOO core** — **99.046311231 shares,
unchanged; no order has touched it since the 09-03 fill**, twenty sessions ago, avg_entry **706.74**,
cost_basis **$69,999.99**.

**⚠ THE CLOSE RUN'S STEP 2 — RECORD THE CLOSES — HAD NO OPERAND, AND THAT IS THE FINDING.** Step 2
iterates over **open satellite positions**; there are **zero**, so **zero `bars` calls were due on that
path and zero marks were written.** ⚠ **Read this precisely: the marks are ABSENT, which is a THIRD
STATE, distinct from "stale" and from "current-and-unchanged". An absent field carries no `(as of …)`
date, and that is exactly what proves no backfill is owed to tomorrow's midday run.** **Nothing was
skipped, and this is NOT the silent-trailing-stop failure the step exists to catch** — §5.4 **has never
been armed**, because it arms on the first **satellite** fill and the 09-03 core fill was not one.
**Twenty-sixth session with §5.1–§5.4 never started; `sell_rule_status` is ABSENT rather than blank;
all four remain untested code paths.**

**CORE VOO DELIBERATELY NOT STAMPED — FORTY-THIRD RUN.** §5 exempts core from all four sell rules. A
`highest_close` on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
exempts.** Refused again at the close, where the pull is strongest: **the close run is the one with a
fresh official close in hand and an empty Step 2, and "nothing to write" is the correct output, not an
invitation to find a row to write it to.**

**⚠ THE TWO-PRICE DEFECT PRODUCED A SIGN FLIP TODAY, AND THE CLOSE RUN IS WHERE IT WOULD HAVE DONE
REAL DAMAGE.** Today's **official** VOO close (`bars --adjustment all`) is **712.69**; yesterday's is
**712.76**. **VOO fell 7 cents, −0.0098%.** The broker's 16:15 `positions` row instead reads
`current_price` **712.859** — an **after-hours midpoint, 16.9 cents ABOVE the official close** — and
`lastday_price` **712.78**, still the **two-cents-high** instance that has persisted all session
(`lastday_price` only rebuilds at a session boundary, so re-reading it is never a second
confirmation). ⚠ **Both legs of the broker's day-P&L are therefore defective, and it reports
`equity − last_equity` = **+$7.82** — UP — on a day the tape was DOWN $6.93. Not a magnitude error: a
SIGN ERROR.** ⚠ **And had a satellite position existed, Step 2 taking `current_price` for its
`highest_close` would have stamped 712.859 instead of 712.69 and silently moved the §5.4 stop 17 cents
in the position's favour — the exact failure the ledger header warns about, demonstrated with real
numbers for the first time.** Standing rule unchanged and now evidenced: **`bars --adjustment all` for
a close, a fresh `quote` for execution, never a `positions` field for either, and never
`equity − last_equity` or `unrealized_intraday_pl` for a day's P&L.**

**PLAN VERSUS OUTCOME — THEY MATCH, AND THE PLAN WAS FRESH AND EMPTY (two separate findings).**
`plan_date` **2026-09-22** matched the ET date — the §2 staleness gate has now been exercised **twenty-
four times and has never fired; its alert path remains UNTESTED CODE**. The plan's one line was **"Do
nothing — no BUY, no SELL, no REBALANCE"**, and **nothing is what happened.** ⚠ **A fresh empty plan
and a stale plan produce an identical zero-order run**, which is why the gate is decided on the
**date** and never on the outcome. **Step 3 bootstrap is permanently closed** (`core_established: true`
since 09-03); the `--core` path was not invoked at any point today.

**SLEEVES IN BAND ON THE OFFICIAL CLOSE; NO REBALANCE DUE TOMORROW.** On the **official close**: equity
**$100,589.32**, core **$70,589.32 = 70.18%**, satellite **0.0% (count 0)**, cash **$30,000.00 =
29.82%**. `alpaca.py sleeves` on its broker mark agrees to two decimals — `core_in_band: true`,
`rebalance_needed: false`, `rebalance_delta: −181.82`. §2 rebalances at the **65/75 band edge, not to
the exact 70% target**, so **no delta inside the band is an action at any size** — the overshoot is
**0.18% of equity against a band edge 4.82 points away**. **Thirty-fourth consecutive run inside a
0.63-point range (69.59–70.22).**

**NO TRADES, NOTHING IN LIMBO — CHECKED AT THE CLOSE, WHICH IS THE RUN THAT OWES THE CHECK.**
`orders --status all` at 16:15 returns **one row for the account's entire history**: the 09-03 core VOO
buy (`d177d8f0-cd0c-41bf-95c1-4772318265fd`, `status: filled`, terminal). **No order from today, and
no order in a non-terminal state anywhere in this account's history — nothing carries overnight**
(§7). `trade_log.md` correctly left unappended — **a run with no fill writes no trade entry.**
**Nothing closed today, nothing has ever closed**, so the §6 loss streak stayed at **0**, no
`HALT_CLEARED_AT` comparison was required and **no circuit-breaker alert was due**. Breaker
**INACTIVE**, `halt_triggered_at: none`.

**WEEK ROLLOVER CHECKED AT ALL FOUR RUNS — ANCHORS MATCHED, NO RESET DUE.** Today is Tuesday
**2026-09-22**; its ISO Monday is **2026-09-21** and `week_of` already reads **2026-09-21**. **Eighth
consecutive run to find the reset already done** — `new_positions_this_week` stays **0 of 3**. Next
boundary **Monday 2026-09-28**. **That is the mechanism working, not a skipped check.**

**⚠ GNRC NOT LOOKED AT FOR THE FIFTEENTH CONSECUTIVE RUN — AND TODAY'S THIRD REFUSAL IS THE FIRST ONE
WORTH ANYTHING.** The 09:36 and 12:40 runs issued **no `move`, `quote`, `bars` or `asset` call on any
symbol at all**, so both refusals were free — no open data plane for a costume to ride. ⚠ **The close
run is different: it opened the data plane on purpose**, calling `bars --symbol VOO --days 3
--adjustment all` for the official close. **A `bars --symbol GNRC` alongside it would have cost one
call and ridden in on the "call-already-open" and "zero-marginal-cost" costumes, both of which are
already on the list.** It was not made. ⚠ **Reported honestly, the pull was mild rather than strenuous,
and the reason is not virtue: this routine has no research step for a number to land in, so the costume
had nowhere to go even if worn.** That makes it **real evidence, but weaker than a refusal on a run
that could have used the number** — tomorrow's GIS pre-market screen is exactly such a run, and it is
the one to watch. The disqualifying facts do not move: **GNRC is the named counterparty in the Amazon
announcement, first-order and outside §4 at any price**, and open item (7) is resolved by **a human
editing §4 or `alpaca.py move`**, not by a number this seat collects. Costumes so far: diligence,
curiosity, tidiness, completeness, zero-marginal-cost, self-audit, proxy-procurement, issue-closure,
call-already-open, screen-already-running.

**RESEARCH — NONE WAS DUE AT THE OPEN, MIDDAY OR CLOSE RUN, AND NONE WAS DONE.** None of the three
generates ideas; the gap between 08:15 and 09:35 is deliberate, and routine 4 is the furthest
downstream of all. **Zero `perplexity.py` calls were issued today after 08:15.** The pre-market run's
five rejections (T-2026-09-22-01 through -05: Paramount/WBD, **ACN**, Nscale, **Vicor**, GPC/ORLY/LKQ
off the AutoZone print) stand as written in `research_log.md`, and **no skip needed logging against any
of them** — a §4 priced-in skip is logged only against a thesis that reached a BUY intent, and **none
did.** ⚠ **The close run neither re-screened nor rehabilitated any of the five. A rejection is not a
queue.**
---

**⚠ EARLIER PER-RUN RECONCILIATIONS (2026-09-01 through 2026-09-18 08:16) HAVE BEEN COLLAPSED,
DELIBERATELY.** Thirty-five blocks spanning 09-01 to this morning's pre-market run each recorded the same
null result — zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no
§5 rule evaluated; no high-water mark to stamp; no backfill due. `state.md` flags this
accumulation as
actively harmful rather than untidy: this repo's only continuity mechanism is the next run
*reading* these files, and padding them with restatements of one null fact raises the odds that
a genuinely live item gets skimmed. Carry-forward is defined as **cleared once acted on**, and
each of those blocks was acted on by the run that read it. **The correct response to the pull to
append is to collapse, not to add another.** Nothing live was discarded — the load-bearing facts
those blocks carried are preserved here:

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional
  $70,000.00**, order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**,
  verified terminal before it was written. Audit record in `trade_log.md`.
- **Measure the core from the 706.74 fill, not from a prior VOO close.** The fill landed
  **+0.483% above the previous close**, and that one-time entry gap — not tracking error and
  never skill — is the whole of the core's reported divergence from VOO.
- **The core is not tracked in this ledger by design.** §5 exempts it from all four sell rules,
  so it has no thesis state, no timing window and no `highest_close`. **Every reconciliation
  compares satellite blocks to satellite Alpaca positions**; a run that compares the raw ledger
  to the raw broker will read a correct ledger as broken.
- **§5.4 has never been armed.** It arms on the first *satellite* fill. The 09-03 core fill was
  not that day, and no day since has been either.
- **All four §5 sell rules remain untested code paths.** Nothing has ever closed, so the string
  of "no exits" entries recorded the absence of a subject, not clean bills of health.
- **The two-price defect is SOLVED and it is a live quote midpoint, not an offset** — which is why
  the broker/official gap (6.5c, 59.85c, 4c on successive days) never had a stable size and never
  will. A `current_price` of 700.57 against a `lastday_price` of 702.56 is an **intraday midpoint,
  not a close.** Always `bars --adjustment all` for a close, a fresh `quote` for execution, **never
  a `positions` field for either.** Cosmetic on core; **load-bearing the moment a satellite
  position exists**, because a `highest_close` read from a `positions` field records an after-hours
  midpoint and silently moves the §5.4 stop.
- **The 09-11 Alpaca data-plane outage is resolved** (every endpoint 200 at the 09-11 close, probed
  by hand), **but `selftest.py` still does not probe `clock` or market data** — a green pre-flight
  certifies nothing about the data plane. Probe by hand before relying on a price.
