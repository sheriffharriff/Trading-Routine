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

⚠⚠ **AND THE MARK CARRIES A BASIS, NOT JUST A NUMBER — DISCOVERED 2026-09-28 ON THE FIRST
CORPORATE ACTION IN THIS ACCOUNT'S HISTORY.** `bars --adjustment all` **back-adjusts every
prior close on an ex-dividend date.** VOO went ex-dividend on 2026-09-28 and the *same
sessions* that read 710.705 / 707.28 / 712.76 on Friday now read **708.88 / 705.47 / 710.93**
on an `--adjustment all` pull — every historical close multiplied by **0.997432**. The raw
prints did not change; the **basis** did.
⚠ **CONSEQUENCE FOR §5.4, AND IT FAILS IN THE DIRECTION OF SELLING:** a `highest_close`
stamped before an ex-date and compared against a post-ex `--adjustment all` close manufactures
a **phantom drawdown equal to the dividend**. On a 10% trailing stop, a 2%-yielding name
gives away **a fifth of the stop's width per year** to an arithmetic artifact, and §5.4 fires
on a position that never fell.
⚠ **RULE: `highest_close` and the close it is compared against must come from the SAME
adjustment basis, pulled in the SAME call.** The safe procedure is to re-pull the whole
window each run and take the max from that one pull, rather than comparing today's price to a
number stamped on an older basis. **Record the basis with the mark.** The failure is silent —
nothing in the bar, the field or the date tells you the basis moved under you.

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
position's own holding window.

⚠⚠ **THE SECOND HALF OF THAT SENTENCE USED TO READ "and it stays correct for positions closed
months later." THAT CLAIM IS FALSE AND WAS FALSIFIED ON 2026-09-28.** It is only true between
ex-dividend dates. A baseline captured on an `--adjustment all` pull sits on the basis in force
*that day*; every later ex-date rescales the series **underneath the stored number**, leaving
the recorded baseline too HIGH relative to current prices. The computed VOO return is then
**understated by the accumulated dividend factor — roughly 0.26% per quarter, ~1.0% a year —**
⚠ **and it understates the BENCHMARK, which flatters the book.** Over a multi-month hold that is
a material share of the excess the strategy is trying to produce, running in the one direction a
run is least likely to question.
⚠ **THE FIX IS NOT TO STOP STORING IT.** Store it, and **re-derive the benchmark leg from a
fresh `--adjustment all` pull of the entry date at review time**; use the stored value only to
check that the pull returned the right session. A stored baseline is a *label*, not a *price*.

---

## Open positions

*(none — no **satellite** positions have been opened yet. Core VOO exists and is deliberately not tracked here, per the top-of-file rules and the fill note further down.)*

**Reconciliation 2026-10-02 — 12:42 ET, 3-midday-management. THE LEDGER AGREES WITH THE BROKER;
ZERO SATELLITE POSITIONS ON BOTH SIDES; ZERO EXITS; NO MARK WRITTEN, NONE DUE, AND NO BACKFILL POSSIBLE.**

Selftest passed all five checks; `trading_enabled: true`, LIVE paper. `clock` **12:41:56** reads
**`is_open: true`** — the one boolean value with a single meaning, and the shape this seat expects.
`positions` returns **one row, core VOO**, 99.046311231 shares at avg_entry **706.74** (a **RAW** print),
cost_basis **$69,999.99** — unchanged since the 09-03 fill — against **zero satellite blocks in this file.
THEY AGREE.** ⚠ **Core VOO was removed from the working list BEFORE any §5 rule was read**, per §5's core
exemption. Sleeves: core **70.0%**, satellite **0.0%** (count 0), cash **30.0%**, `core_in_band: true`.

⚠⚠ **STEP 2 — THE HIGH-WATER DETECTOR RAN AND HAD NO INPUT, WHICH IS NOT THE SAME AS RUNNING CLEAN.**
This is the seat whose named job is to **detect** a `highest_close` that a missed close run left stale, and
the carry-forward warns that a stale mark **silently disables §5.4** while every other check still passes.
⚠ **Its entire input is an `(as of …)` date compared against the last trading day. THERE IS NO POSITION, SO
THERE IS NO FIELD, SO THERE IS NO DATE — NO STALENESS COULD BE DETECTED AND NONE WAS RULED OUT.** The only
`highest_close` string in this file is the **template placeholder at line 53**, verified from source with
`grep`; every other occurrence is prose. ⚠ **`highest_close` is ABSENT — the third state, carrying no
`(as of …)` date at all.** **A detector handed no input returns the same silence as a detector finding
everything healthy, and this is the sixth consecutive run in that state.**
⚠ **NO BACKFILL WAS PERFORMED AND NONE WAS POSSIBLE — there was nothing to write a mark onto.**
⚠ **ZERO `bars` CALLS WERE MADE, DELIBERATELY: at 12:42 a bar dated today is PARTIAL, and its `c` field is
the last trade so far wearing a close's clothes.** **The backfill path remains UNEXERCISED CODE.**
⚠ **SIXTY-SEVENTH CONSECUTIVE REFUSAL TO STAMP A `highest_close` ON CORE — graded FREE, because this seat
writes no marks and had no operand to write one onto. FREE IS NOT THE SAME AS RESTRAINT.**

⚠⚠ **STEP 4 HAD NO OPERAND: ZERO SELL ORDERS, AND THAT FOLLOWS FROM AN EMPTY SLEEVE RATHER THAN FROM ANY
RULE BEING EVALUATED AND PASSED.** Zero Perplexity news-on-holdings queries were due and **zero were run** —
§5.1 reads an `invalidation` string verbatim off a held position, and no such string exists. Zero `quote`
calls were made for the same reason: the routine's quote step names "every open satellite ticker" and that
list is **empty**.

### `sell_rule_status` — ALL FOUR RULES ABSENT, NOT PASSING (2026-10-02 12:42 ET)

⚠⚠ **THERE IS NO POSITION TO WRITE A `sell_rule_status` LINE ON. The distance to each rule is therefore not
"large" — it is UNDEFINED, and those are different facts.** ⚠ **"Nothing close to triggering" would be a
fabrication: nothing can be close to a threshold it has no operand for.**

| Rule | Status this run | Distance | Why it is not "passing" |
|---|---|---|---|
| **§5.1** thesis invalidation | **NO OPERAND** | n/a | No thesis is held, so no `invalidation` string exists to read verbatim. Zero news queries due, zero run. |
| **§5.2** time stop | **NO OPERAND** | n/a | No `timing_window` and no deadline field exists anywhere in this file. |
| **§5.3** hard stop −7% from entry | **DISTANCE UNDEFINED** | **UNDEFINED, not large** | There is no satellite `entry_price` to measure a drawdown from. The 706.74 core fill is **exempt under §5** and is not an operand. |
| **§5.4** trailing stop −10% from `highest_close` | **NOT ARMED** | **UNDEFINED, not large** | No `highest_close` field — the **third state**, carrying no `(as of …)` date at all. It arms on the first **satellite** fill; the 09-03 core fill was not one. |

**§5.1–§5.4 have never had an operand in this account's history: 22 completed sessions since 2026-09-01,
19 after the 09-03 core fill, zero satellite positions ever.** ⚠ **The session counter was NOT advanced —
today is a session IN PROGRESS, not a completed one, and this seat reads `is_open: true`.**

**Reconciliation 2026-10-02 — 09:38 ET, 2-market-open-execution. THE LEDGER AGREES WITH THE BROKER;
ZERO SATELLITE POSITIONS ON BOTH SIDES; ZERO ORDERS PLACED; NO MARK WRITTEN AND NONE DUE.**

`clock` **09:36:33** reads **`is_open: true`** — the one value with a single meaning. `positions` returns
**one row, core VOO**, 99.046311231 shares, cost_basis **$69,999.99** — unchanged since the 09-03 fill —
against **zero satellite blocks in this file. THEY AGREE.** Core was removed satellite-to-satellite before
any §5 rule was read. Sleeves: core **70.05%**, satellite **0.0%**, cash **29.95%**, `core_in_band: true`.
⚠ **No `bars` call was made and no `highest_close` was written: a bar dated today is PARTIAL while the
market is open, and there was no position to stamp one onto in any case.** **Sixty-sixth consecutive
refusal to stamp a mark on core — graded FREE, this seat writes no marks.**

**Reconciliation 2026-10-02 — 08:23 ET, 1-premarket-research. THE LEDGER AGREES WITH THE BROKER;
ZERO SATELLITE POSITIONS ON BOTH SIDES; NO §5 RULE HAS A SUBJECT; NO MARK WRITTEN AND NONE DUE.**

Selftest passed all five checks; `trading_enabled: true`, LIVE paper; pre-flight broker equity
**$99,865.29** at 08:23. `clock` at **08:23:38** reads **`is_open: false`** with `next_open`
**2026-10-02T09:30** — the **PRE-MARKET** shape, read off the DATE (it points at TODAY), not off the
boolean. ⚠ **FALSE has three meanings; TRUE has one.** ⚠ **Corroborated from the data plane rather than
inferred: `bars` returns a complete 2026-10-01 bar and NO bar dated 2026-10-02.** **Not a holiday.**

**RECONCILIATION, SATELLITE-TO-SATELLITE.** `alpaca.py positions` returns **one row, core VOO**,
99.046311231 shares at avg_entry **706.74** (a **RAW** print), cost_basis **$69,999.99** — unchanged
since the 09-03 fill — against **zero satellite blocks in this file. THEY AGREE.** ⚠ **Core VOO was
removed from the working list BEFORE any §5 rule was read**, per §5's core exemption; **a run that
compares the raw ledger to the raw broker reads a correct ledger as broken.**

### `sell_rule_status` — ALL FOUR RULES ABSENT, NOT PASSING (2026-10-02 08:23 ET)

⚠⚠ **THERE IS NO POSITION TO WRITE A `sell_rule_status` LINE ON. The distance to each rule is therefore
not "large" — it is UNDEFINED, and those are different facts.**

| Rule | Status this run | Distance | Why it is not "passing" |
|---|---|---|---|
| **§5.1** thesis invalidation | **NO OPERAND** | n/a | No thesis is held, so no `invalidation` string exists to read verbatim. **Zero Perplexity news-on-holdings queries were due and zero were run.** |
| **§5.2** time stop | **NO OPERAND** | n/a | No `timing_window` and no deadline field exists anywhere in this file. |
| **§5.3** hard stop −7% from entry | **DISTANCE UNDEFINED** | **UNDEFINED, not large** | There is no `entry_price` to measure a drawdown from. ⚠ **"Comfortably far" would be a fabrication.** |
| **§5.4** trailing stop −10% from `highest_close` | **NOT ARMED** | **UNDEFINED, not large** | No `highest_close` field — the **third state**, carrying no `(as of …)` date at all. It arms on the first **satellite** fill; the 09-03 core fill was not one. |

**Zero orders submitted by this run** (a pre-market seat places none by design), **zero fills, nothing
opened, nothing closed, no realised P&L.** `consecutive_closed_losses` stays **0** — nothing has closed.
Breaker **INACTIVE** (`halt_triggered_at: none`, so no `HALT_CLEARED_AT` comparison was required; the
`none` in `control.md` is therefore **untested against a live halt**, not cleared).

**§5.1–§5.4 HAVE NEVER HAD AN OPERAND IN THIS ACCOUNT'S ENTIRE HISTORY** — **22 completed trading
sessions since 2026-09-01, 19 AFTER the 09-03 core fill**, **zero satellite positions ever opened.**
⚠⚠ **THE COUNTER IS NOT ADVANCED BY THIS RUN AND THE REFUSAL IS THE STRONG FORM OF CATCH (11): at 08:23
the market has not opened, so TODAY IS NOT A COMPLETED SESSION and a pre-market seat has none of today's
to add.** ⚠ **Catch (11) names routines 1 and 2 as the two exposed seats. This is one of them, the
increment was available, and it was declined from the CLOCK rather than from a claim about which routine
this is.**

⚠ **CORE VOO IS AGAIN NOT STAMPED WITH A `highest_close` — SIXTY-FIFTH CONSECUTIVE RUN.** §5 exempts core
from all four sell rules; a mark on VOO would fabricate a §5.4 trailing stop on the one position the
strategy exempts, a stop that could eventually sell core on a drawdown, which §7 forbids outright.
⚠ **Graded honestly: this seat does NOT write marks, so today's refusal is FREE. The close run's is the
load-bearing instance; a pre-market refusal is weaker evidence of restraint and is logged as such.**

⚠ **ONE FRESH TAPE FACT FOR THE FILE: the 2026-10-01 bar's `n`/`v` HAVE MOVED SINCE YESTERDAY'S CLOSE RUN
READ THEM** — **1633/51892 then, 1634/51893 now** — **while its close held at 702.255 to the cent.**
⚠ **Second clean instance of "a completed daily bar is not immutable in `n` and `v`." Late-reported prints
keep arriving after the bell. The CLOSE is the stable field; the CLOCK is the reliable discriminator; and
the n/v FLOOR test is a corroborant built on a ruler that moves.**

---

**Reconciliation 2026-10-01 — ONE BLOCK FOR THE DATE, COVERING ALL FOUR RUNS, LED BY THE 16:16 CLOSE.
⚠ COLLAPSED DELIBERATELY: the 09:37 and 12:41 blocks this replaces recorded the same null reconciliation
and their load-bearing findings are preserved below. THE LEDGER AGREES WITH THE BROKER; ZERO SATELLITE
POSITIONS ON BOTH SIDES; NO ORDER PLACED ALL DAY; NO HIGH-WATER MARK WRITTEN AND NONE DUE; NO §5 RULE HAD
A SUBJECT.**

**— 16:16 ET, 4-market-close-journal.** Selftest passed all five checks; `trading_enabled: true`, LIVE
paper; pre-flight broker equity **$99,611.63** at 16:16. `clock` at **16:16:49** reads **`is_open: false`**
with `next_open` **2026-10-02T09:30** and `next_close` **2026-10-02T16:00** — the **POST-BELL** shape.
⚠ **Read off the DATES, not the boolean: `next_open` points at TOMORROW, which is what separates post-bell
from pre-market and from a holiday. FALSE has three meanings.**
⚠ **The stronger discriminator was run rather than inferred: a VOO daily bar for 2026-10-01 EXISTS AND IS
COMPLETE** — o 702.95, h 703.43, l 697.50, **c 702.255**, n 1633, v 51892 — **and the 15:59:59 ET
`latestTrade` prints 702.255 to the cent, so the bar's close field is the last trade of the session.**
**A session happened. This is not a holiday skip and the summary is owed.**

### THE n/v FLOOR TEST GOT ITS FIRST POST-BELL APPLICATION. IT PASSED, AND THE MARGIN IS THE FINDING.

Today's midday run replaced the old "`n`/`v` are visibly tiny" smell test with a sharper discriminator:
**is `n` below the trailing completed-session minimum?** This is the first seat to run it on a bar it
believes is **complete**, which is the other half of the test and the half that can only fail quietly.

- **It passed.** Re-pulled fresh: across the **24 completed sessions** in the trailing 25-day window the
  minimum `n` is **1,450** and the minimum `v` is **43,730** (both 09-02, which has not yet rolled out of
  the window). Today's completed bar reads **n 1,633 / v 51,892** — **above both floors.**
- ⚠⚠ **AND THE MARGIN IS THIN ON THE SIDE THAT MATTERS. Today's `n` sits only 12.6% above the floor
  (`v` 18.7%), while this morning's PARTIAL bar at 12:41 sat 32.3% BELOW it (`n` 982).** The two
  populations did not overlap today, but **the complete-side clearance is less than half the partial-side
  clearance** — so a quiet, low-participation full session could land under the floor without being
  partial at all.
- ⚠ **GRADED HONESTLY: this is a corroborating instance, NOT a validation.** One ticker, one day, on the
  easy side of the test. **The CLOCK plus a matching 15:59:59 `latestTrade` remains the primary; the floor
  test stays a corroborant and must never be promoted.** Its stated falsifier is unchanged and untested:
  **it must fail on a half-day session** (day after Thanksgiving, Christmas Eve), where a complete bar
  legitimately carries about half the usual `n`/`v`. **The next early close is still the test.**

**PRESERVED FROM THE 12:41 MIDDAY RUN — THE PRICE HALF OF THE PARTIAL-BAR WARNING, CONFIRMED WITH ITS
MECHANISM, AND IT IS THE DANGEROUS HALF.** Read ~3h12m into the session, the partial bar's **`c` 700.35**
sat **26 cents** from 09-30's official 700.605, mid-range against a trailing 691.44–710.93 band — a wholly
plausible close carrying no warning of any kind. ⚠⚠ **AND `c` 700.35 EQUALED `latestTrade.p` 700.35 TO THE
CENT: the partial bar's close field is simply the last trade so far wearing a close's clothes.** A §5.4
mark stamped from it records an intraday print as a high-water close and silently moves the stop.
⚠ **NO `bars` CLOSE MAY BE STAMPED AS A MARK BEFORE THE BELL, ON ANY BASIS.**

**STEP 2 — THE HIGH-WATER WRITE HAD NO OPERAND, FOR A FIFTH CONSECUTIVE CLOSE RUN, AND THAT IS NOT THE
SAME AS IT WORKING.** There are **zero open satellite positions**, so there was no `highest_close` to
raise and **no `(as of …)` date to advance.** Zero `bars` calls were due on any satellite symbol and
**zero were made**; the VOO pulls were for the day's close, the sleeve arithmetic and the floor test.
⚠⚠ **THIS IS THE WRITING SEAT, HOLDING A COMPLETE OFFICIAL 702.255 CLOSE AT THE MOMENT IT HAD NOTHING TO
STAMP IT ONTO — the sharpest form of the item, and the sentence this run first reached for was "high-water
marks updated," which would have been FALSE.** ⚠ **The honest form is: THE JOB HAD NO OPERAND.**
⚠⚠ **THE ROUTINE'S OWN INSTRUCTION IS TO UPDATE THE `(as of …)` DATE EVERY DAY WHETHER OR NOT THE VALUE
MOVES, PRECISELY SO A CURRENT MARK IS DISTINGUISHABLE FROM A SKIPPED ONE. THERE IS NO FIELD, SO THERE IS NO
DATE, SO THAT DISCIPLINE PRODUCED NO ARTIFACT TODAY EITHER.** `highest_close` is **ABSENT — the third
state.** ⚠ **TOMORROW'S RUNS MUST NOT READ THE MISSING STAMP AS A FAILED CLOSE RUN. Nothing was skipped;
there was no operand. DO NOT BACKFILL ANYTHING.** **The backfill path in this file's header — re-pull the
whole window on a STATED adjustment basis and take the max from that ONE pull — remains UNEXERCISED CODE,
as does routine 3's detector for it. The cost has been zero because the sleeve is empty. That is luck, not
a control, and the first satellite fill arms both halves at once.**

⚠ **SIXTY-FOURTH CONSECUTIVE REFUSAL TO WRITE A `highest_close` ON CORE.** Today's official 702.255 is
deliberately **NOT written anywhere in this file**: §5 exempts core from all four rules, and a mark on it
would fabricate a §5.4 trailing stop on the one position the strategy exempts — a stop that could
eventually sell core on a drawdown, which §7 forbids outright. ⚠ **This seat WRITES marks, so the refusal
is load-bearing here rather than free — but it is still the sixty-fourth, and automatic is not sound.**

### `sell_rule_status` — ALL FOUR RULES ABSENT, NOT PASSING (16:16 ET)

⚠⚠ **THERE IS NO POSITION TO WRITE A `sell_rule_status` LINE ON. The distance to each rule is therefore
not "large" — it is UNDEFINED, and those are different facts.**

| Rule | Status this run | Why it is not "passing" |
|---|---|---|
| **§5.1** thesis invalidation | **NO OPERAND** | No thesis is held, so no `invalidation` string exists to read verbatim. **Zero Perplexity news-on-holdings queries were due and zero were run.** |
| **§5.2** time stop | **NO OPERAND** | No `timing_window` and no deadline field exists anywhere in this file. |
| **§5.3** hard stop −7% | **DISTANCE UNDEFINED** | No `entry_price` to measure a drawdown from. ⚠ **Not "comfortably far" — undefined.** |
| **§5.4** trailing stop −10% | **NOT ARMED** | No `highest_close` field — the **third state**, carrying no `(as of …)` date at all. It arms on the first **satellite** fill; the 09-03 core fill was not one. |

**RECONCILIATION, SATELLITE-TO-SATELLITE.** `alpaca.py positions` returns **one row, core VOO**,
99.046311231 shares at avg_entry **706.74** (a **RAW** print), cost_basis **$69,999.99** — unchanged since
the 09-03 fill — against **zero satellite blocks in this file. THEY AGREE.** ⚠ **Core VOO was removed from
the working list BEFORE any §5 rule was read**, per §5's core exemption; **a run that compares the raw
ledger to the raw broker reads a correct ledger as broken.**
**`orders --status all` returns ONE ROW for the account's entire history** (the 09-03 core VOO buy,
`status: filled`, `filled_at` 2026-09-03T13:36:21Z, terminal) — **so no order from today exists to be left
in limbo, and §7 has nothing unverified anywhere.** **Zero fills today, zero orders submitted by any of the
four runs, nothing opened, nothing closed, no realised P&L.** `consecutive_closed_losses` stays
**0 — CONFIRMED against what actually closed today (nothing), not recomputed**; breaker **INACTIVE**
(`halt_triggered_at: none`, so no `HALT_CLEARED_AT` comparison was required).

**§5.1–§5.4 HAVE NEVER HAD AN OPERAND IN THIS ACCOUNT'S ENTIRE HISTORY** — **22 completed trading sessions
since 2026-09-01, 19 AFTER the 09-03 core fill**, **zero satellite positions ever opened.**
⚠⚠ **THE COUNTER ADVANCES 21/18 → 22/19 AND THIS SEAT IS ENTITLED TO ADVANCE IT — BUT THE ROUTE IS WHAT
MAKES THAT TRUE, NOT THE SEAT.** What makes the increment safe is that **today is a COMPLETED session**,
established from a 2026-10-01 bar that exists plus a 15:59:59 ET `latestTrade` matching its close — not
from "routine 4 is the close run." ⚠ **That is catch (6): a correct number reached by an unchecked route is
not a checked fact.** ⚠ **Both earlier seats today declined the same increment correctly — 08:24 because
the market had not opened, 09:37 because the session was in progress.**

⚠⚠ **NEW TODAY, AND IT IS A REPRODUCIBILITY FACT RATHER THAN A DEFECT: A HISTORICAL *BOOK* DAY-RETURN
CANNOT BE REPRODUCED EXACTLY FROM A LATER `--adjustment all` PULL ONCE AN EX-DATE INTERVENES, FOR TWO
SEPARATE REASONS. CHECKED BY DECOMPOSITION, NOT ASSERTED.** Worked on 09-22 → 09-23:
**raw −0.532701%**, **exact-rescale −0.532293%**, **published `--adjustment all` −0.531690%.**
- **VOO's own day return is basis-INVARIANT under an exact rescale** (−0.759096% both ways): a constant
  multiple cancels in a ratio.
- **The BOOK's is NOT** (+0.000408pp). **The cash leg does not rescale**, so rescaling the core leg moves
  the core WEIGHT, and the book return is weight × VOO return.
- **Published closes add a second, larger effect** (+0.000859pp on VOO): the rescaled closes are
  **rounded** — exact 710.859812 → published 710.86; exact 705.463705 → published **705.47**, 0.6c up.
⚠ **MAGNITUDE IS ~0.001pp AND NOTHING TURNS ON IT.** Recorded because the Friday review recomputes every
post-fill session from one fresh pull and will get figures that differ in the fourth decimal from the
dailies. ⚠ **NEITHER IS WRONG. A day-return must be quoted with its BASIS *and* its VINTAGE.**
⚠ **§5.4 IS UNAFFECTED — it compares two numbers from the SAME pull, which is exactly why the header's
same-basis-same-call rule is written that way.** ⚠ **Today's own figures are unaffected too: 09-30 → 10-01
are both post-ex, so no rescaling sits inside the window.**

**TAPE, WITH THE BASIS NAMED ON EVERY FIGURE.** **Official/price basis (`bars --adjustment all`, the
complete 2026-10-01 session, c 702.255): equity $99,555.77, core $69,555.77 = 69.8661%, cash $30,000.00 =
30.1339%, satellite 0.0%.** **BROKER MARK at 16:16 (NOT a close): equity $99,603.80, core $69,603.80 =
69.88%, `current_price` 702.74, `rebalance_delta` +$118.86** — a **tenth** consecutive positive reading and
**NOT the sign defect resolving** (the same quantity disagreed in sign on 09-24).
⚠ **Post-bell `current_price` minus official close = +$0.485, the TENTH observation.** Range is now
−$0.97 to +$1.145 and **+$0.485 is unremarkable inside it — the largest is still 09-30's +$1.145.**
⚠⚠ **A NINTH EQUITY-DRIFT INSTANCE, AND THE NEW PART IS THE HOUR: `selftest` read $99,611.63 and
`account`/`sleeves` both read $99,603.80, a $7.83 spread, ALL THREE AFTER THE BELL.** ⚠ **The drift is not
confined to market hours — consistent with `current_price` being a live midpoint that keeps updating in
after-hours, which is the already-solved two-price finding and NOT a new defect.** ⚠ **Inside the
established $1.97–$216.91 range, so no evidence of narrowing.** ⚠ **An equity figure is only meaningful
with its CALL and its TIMESTAMP attached, and two figures from different calls must never be differenced.**
**NO REBALANCE WAS DUE AND NONE IS DUE TOMORROW** — §2 acts at the **65/75 band edge**, and core sits
**4.866 points** inside the 65 edge on the official close (**4.88** on the broker mark).
⚠ **Fifty-sixth consecutive run inside 69.59–70.22.**
⚠⚠ **`cash` READ EXACTLY $30,000.00 FOR A THIRTEENTH TIME, DAY 4 OF 8 — the VOO dividend is still unpaid.
NO READING'S HOUR MAKES IT STRONGER: settlement does not run on the bell.**

*(Earlier stamps, **TODAY, 2026-10-01**, all four runs: 12:41 ET 3-midday-management $99,370.06,
`is_open: true`, exits-only seat with no operand, zero orders; 09:37 ET 2-market-open-execution selftest
$99,625.59 / `account` $99,641.94, `is_open: true`, zero orders on a FRESH EMPTY plan, staleness gate
exercised for the 31st time without firing; 08:24 ET 1-premarket-research $99,693.94, `is_open: false` in
the PRE-MARKET shape, six theses written and all six rejected, zero intents.)*
⚠ **PRESERVED FROM THE 09:37 BLOCK, BECAUSE IT NAMES WHICH BROKER FIELD IS A PRICE: `last_equity`
99,417.59768935866 equals qty × `lastday_price` 700.86 + cash TO ELEVEN DECIMAL PLACES (residual 0E−11),
and its gap to the official-close equity (qty × 700.605 + cash = 99,392.340879994755) is
$25.256809363905 = qty × $0.255 exactly.** ⚠ **So `equity − last_equity` and `change_today` are artifacts
of ONE substitution — a broker field standing in for an official close — and neither is a day return. This
does NOT re-open WHY `lastday_price` reads what it reads; four mechanisms are already falsified, and an
identity and a mechanism are different claims.** *(`lastday_price` reads 700.86 again today, unchanged
from the 09:37 pull.)*

*(**2026-09-30**'s stamps, retained under their OWN date: 12:41 ET 3-midday-management $99,908.87; 09:35 ET
2-market-open-execution $99,792.98; 08:23 ET 1-premarket-research $99,598.85. ⚠ **They are kept separately
because a superseded 10-01 block once listed them under a "same day" heading — correct stamps under a wrong
date label, caught and fixed. ACTED ON; the narrative is dropped and the dated facts are kept.**)*

---

**Reconciliation 2026-09-28 — ONE BLOCK FOR THE DATE, AND IT COVERS ONE RUN, NOT FOUR. ⚠⚠ ROUTINES 1,
2 AND 3 LEFT NO COMMITTED OUTPUT TODAY — SEE THE HOUSEKEEPING NOTE BELOW. THE LEDGER AGREES WITH THE
BROKER; ZERO SATELLITE POSITIONS ON BOTH SIDES; NO ORDER PLACED; NO HIGH-WATER MARK WRITTEN AND NONE DUE;
NO §5 RULE HAD A SUBJECT.**

**— 16:16 ET, 4-market-close-journal.** Selftest passed all five checks; pre-flight equity **$99,664.22**
(broker mark), `trading_enabled: true`, LIVE paper. `clock` at **16:16:24** reads `is_open: FALSE` with
`next_open` **2026-09-29T09:30** and `next_close` **2026-09-29T16:00** — the **POST-BELL** shape.
⚠ **The stronger discriminator was run rather than inferred: a VOO daily bar for 2026-09-28 EXISTS AND IS
COMPLETE** (o 706.23, h 707.22, l 702.03, **c 703.60**, v 62,354, n 3,061; re-pulled once and **identical**,
and the 15:59:59 ET `latestTrade` prints **703.60** — the bar's close is the last trade of the session).
**A session happened; this is not a holiday skip and the summary is owed.**
⚠ **THE VOLUME IS 38% OF FRIDAY'S AND IT IS NOT EVIDENCE OF ANYTHING.** `feed=iex` returns **IEX-only**
volume, a single venue's slice of consolidated tape, and the pulled window already spans 47,589 to 164,725
on sessions all known to be complete. **This is the standing `n`/`v` smell-test rule doing its job: the
CLOCK settled it, the volume was not allowed to.**

**⚠⚠ STEP 2 HAD NO OPERAND — AND FOR THE FIRST TIME THAT IS NOT THE WHOLE STORY.** There are **zero open
satellite positions**, so there was **no `highest_close` to raise and no `(as of …)` date to advance**;
`highest_close` is **ABSENT — the third state, carrying no `(as of …)` date at all.** Zero `bars` calls
were due on any satellite symbol and **zero were made**; the VOO pulls were for the day's close and the
sleeve arithmetic. ⚠ **TOMORROW'S RUNS MUST NOT READ THE MISSING STAMP AS A FAILED CLOSE RUN. Nothing was
skipped; there was no operand. DO NOT BACKFILL ANYTHING.**
⚠⚠ **BUT THE EMPTY SLEEVE IS THE ONLY REASON TODAY WAS HARMLESS, BECAUSE TODAY IS THE DAY THE §5.4
MECHANISM WOULD HAVE BROKEN.** VOO went **ex-dividend** this session and `--adjustment all` silently
rescaled every prior close by **0.997432** (see the finding below). **A `highest_close` stamped on Friday
and compared against today's `--adjustment all` close would have shown a 0.257% drawdown that did not
happen.** The defect is written up in the file header, where it will be read before the next mark is
stamped. ⚠ **This is the first time the "free today, load-bearing the moment a fill lands" warning has
had a concrete, dated mechanism attached to it rather than a general caution.**

**RECONCILIATION CLEAN.** `alpaca.py positions` returns **one row, core VOO** — 99.046311231 shares
unchanged since the 09-03 fill, avg_entry 706.74, cost_basis $69,999.99, market_value $69,664.22 (broker
mark), `unrealized_pl` **−$335.77 / −0.48%** on that mark. **Zero satellite blocks against zero satellite
Alpaca rows — they agree** (satellite-to-satellite, never raw ledger to raw broker). Core VOO was excluded
from the working list before any §5 rule was read. **§5.1–§5.4 have never had an operand in this account's
entire history; §5.4 is STILL NOT ARMED; §5.3's distance is UNDEFINED, not large.**
⚠ **COUNTED AGAINST THE CALENDAR, NOT INHERITED — catch (9) says the "Nth consecutive SESSION" series in
these journals is a RUN counter wearing a session label, so it is not continued here. The verified figures
are: 19 trading sessions since 2026-09-01, 16 sessions since the 09-03 core fill, and ZERO satellite
positions in the account's entire history.** ⚠ **`TRADING_ENABLED` WAS TRUE, so a triggered stop WOULD
have been submitted — the null is an EMPTY SLEEVE, not a disabled stop.**

**⚠⚠ THE FINDING OF THIS RUN, AND IT IS THE FIRST CORPORATE ACTION IN THIS ACCOUNT'S HISTORY: VOO WENT
EX-DIVIDEND TODAY, AND `bars --adjustment all` REWROTE THE PAST WITHOUT SAYING SO.**
Friday's close journal recorded VOO's official closes as **710.705 (09-25), 707.28 (09-24), 707.28
(09-23), 712.69 (09-22), 712.76 (09-21), 701.85 (09-18)** — every one pulled from `bars --adjustment all`.
**The same command, on the same sessions, today returns 708.88 / 705.47 / 705.47 / 710.86 / 710.93 /
700.05.** ⚠ **Every historical close is multiplied by a single constant, 0.997432, and today's close is
untouched.**
**Diagnosed, not assumed.** `--adjustment raw` and `--adjustment split` **both return the ORIGINAL series
to the cent** (701.85 / 712.76 / 712.69 / 707.28 / 707.28 / 710.705). ⚠ **`split` ≡ `raw` rules out a split;
`raw` unchanged rules out a data revision; a single multiplicative factor from one date forward is a
DIVIDEND.** Implied dividend, bounded across six date-pairs against 2dp rounding: **$1.820–$1.824 per
share**, i.e. **$180.26–$180.64** on 99.046311231 shares. ⚠ **Alpaca does not expose the figure — this is
an INFERENCE from the adjustment factor and is labelled as one.**
⚠⚠ **AND `quote` AND `bars` NOW DISAGREE ABOUT THE SAME SESSION, RIGHT NOW.** `quote`'s `prevDailyBar`
reports Friday's close as **710.705**; `bars --adjustment all` reports the same session as **708.88**.
**Two endpoints of the same API, one session, $1.825 apart, both correct on their own basis.** ⚠ **The
standing "both legs from the same source" rule does NOT catch this — `quote` and `bars` were never
distinguished as different bases, only broker fields and bar fields were.**
⚠⚠ **THE LOAD-BEARING CONSEQUENCE IS THAT THE ACCOUNT AND THE BENCHMARK RECOGNISE THE DIVIDEND ON
DIFFERENT DATES.** VOO's adjusted series credits it **on the ex-date, today**. The account's `cash` reads
**exactly $30,000.00, unchanged** — the cash has **not** been paid. So for the next few sessions any
close-to-close comparison of the book against an `--adjustment all` benchmark is **wrong by the dividend
in one direction or the other** unless the receivable is carried explicitly. **Both bases are stated on
every figure below for exactly this reason.**

**THE DAY'S NUMBERS — BOTH BASES, BECAUSE TODAY THEY DIFFER MATERIALLY.**
**Price-only (official closes, `--adjustment raw`):** VOO **703.60** vs Friday's **710.705** = **−$7.105 /
−0.9997%**; core **$69,688.98**, cash **$30,000.00**, equity **$99,688.98**; **day P&L −$703.72 /
−0.7010%**; **since inception −$311.02 / −0.3110%.**
**Total-return (carrying the ~$180.45 dividend receivable):** economic equity **~$99,869.4**; **day P&L
−$523.3 / −0.5212%**; **since inception −$130.6 / −0.1306%.** VOO's own total return today is **−0.745%**
against its **−1.000%** price return.
**Broker basis at 16:16:** equity **$99,664.22**, core **69.90%**, cash **30.10%**, `core_in_band: true`,
`rebalance_needed: false`, delta **+$100.73**. **Official-close basis:** core **69.9064%**, cash
**30.0936%**, delta **+$93.30**.
⚠ **`rebalance_delta` is POSITIVE on both bases — a SIGN FLIP from the four consecutive negative runs, and
the bases AGREE. Neither is an action:** §2 acts at the **65/75 band edge** and core sits **~4.91 points**
inside it. **NO REBALANCE IS DUE TOMORROW on either basis.** Forty-seventh consecutive run inside
69.59–70.22.
⚠ **BROKER DAY-P&L FIELDS PULLED, RECORDED, NOT USED:** `equity − last_equity` = 99,664.22 − 100,401.13 =
**−$736.91**; `unrealized_intraday_pl` **−$736.90**; `change_today` −0.01047. **Against the real price-basis
move of −$703.72 the artifact is −$33.19**, and against the total-return move of −$523.3 it is **−$213.6**.
⚠ **`last_equity` reads 100,401.13 — a FOURTH distinct number, matching neither the official prior equity
(100,392.71) nor Friday's 16:20 broker equity (100,387.36). The field remains UNUSABLE, not imprecise.**

**⚠ THE SUPERLATIVE WAS PULLED BEFORE IT WAS WRITTEN, AND IT SPLIT ON THE BASIS.** A 30-session `bars`
pull gives the full post-fill equity series. **On the price-only basis, −0.7010% IS the largest single-day
loss in the account's history** (previous worst 09-23, −0.5327%). ⚠ **On the total-return basis it is
−0.5212%, which is SECOND — 09-23's −0.5327% still holds the record, and 09-23 had no dividend in its
window so the comparison is like-for-like.** ⚠⚠ **A record loss that exists on one basis and not the
other, where the difference is a dividend the account is OWED. The price basis manufactures a record that
did not happen. Quote the basis or do not quote the number.**
⚠ **Since inception, −0.3110% is NOT a low** — 09-16 reached **−1.3396%**, 09-15 −1.0350%, 09-10 −0.9954%.
Grounded from the pulled series, not asserted.

**⚠ PRICE-FIELD OBSERVATIONS.** `current_price` **703.35** is **25c BELOW** the official 703.60 — **series
now SEVEN post-bell observations: +$1.13 (09-18), −$0.22 (09-21), +$0.169 (09-22), +$0.02 (09-23), −$0.97
(09-24), −$0.054 (09-25), −$0.25 (09-28)**; both signs, range 2c to $1.13, no predictable sign and no
correctable offset. `lastday_price` reads **710.79** against Friday's actual **710.705** — **8.5c high, and
it matches NEITHER basis** (not the raw 710.705, not the adjusted 708.88). ⚠ **The field was already
CLOSED as a question; today it is wrong in a way that is not even a basis error. Do not re-open it.**

**CORE VOO DELIBERATELY NOT STAMPED — FIFTY-SIXTH RUN, AND IT GRADES HIGH.** §5 exempts core from all four
sell rules; a `highest_close` on VOO would **fabricate a §5.4 trailing stop on the one position the
strategy exempts**, a stop that could eventually sell core on a drawdown, which §7 forbids outright.
⚠ **Sharper than usual today: routine 4's Step 2 is THE dedicated write step, the run arrived holding a
fresh official close, the field was empty, AND the run had just finished building the ex-dividend
machinery that a mark would have been written with. Having the tooling in hand is its own pull.** Refused.
**GNRC NOT LOOKED AT — TWENTY-EIGHTH REFUSAL, AND A WEAK ONE:** zero `move`, zero `quote` on GNRC, no
research step by construction, **nowhere to put a number.** ⚠ **The bare count overstates the evidence.**

**⚠ §1 — A VOO-DOWN DAY, A POSITIVE EXCESS, AND THE SEPARATION IS NOW 16 OF 16.** On the total-return
basis: **VOO −0.7448%, book −0.5212%, excess +0.2240pp — against +0.2227pp predicted by holding 70.12%
core and the rest in idle cash.** Agreement to **0.0013pp**. Satellite contributed **exactly 0.0000%**, as
it has for the account's entire history. ⚠ **Friday's weekly review recorded perfect separation over 15
post-fill sessions — 9 VOO-down days all positive excess, 5 VOO-up all negative, 1 flat exactly zero.
Today is a tenth VOO-down day with a positive excess: 16 of 16, still not one exception.** ⚠ **This is not
performance. It is the signature of a book that is 70% one long position and 30% nothing, and today it
reads as a "good" day precisely because the market fell.**

**HOUSEKEEPING — ALL FOUR CHECKS RUN, NONE FIRED, AND ONE THING IS WRONG THAT IS NOT A CHECK.**
**Week rollover:** today is Monday **2026-09-28** (confirmed via `TZ=America/New_York`, not assumed); ISO
Monday **2026-09-28**; `week_of` already reads 2026-09-28 — **advanced by Friday's weekly review, which is
where the reset belongs.** ⚠ **The anchors matched on the ONE day of the week when a rollover was genuinely
due — the reset had already been done, it was not skipped.** `new_positions_this_week` stays **0 of 3**;
next boundary **Monday 2026-10-05**. **Loss streak:** nothing closed today and **nothing has ever closed**,
so `consecutive_closed_losses` stays **0 — it has never had an input**; breaker **INACTIVE**,
`halt_triggered_at: none`, **no `HALT_CLEARED_AT` comparison required, NO `circuit-breaker` alert due.**
**Unresolved orders:** `orders --status all` returns **one row for the account's entire history** — the
09-03 core VOO buy, `status: filled`, terminal. **Nothing is in limbo overnight.** `trade_log.md` correctly
unappended (no fill); `research_log.md` correctly unappended (routine 4 does not research — and see below);
`alerts.md` **empty, zero open, zero SYSTEMIC**; `control.md` notes **(none)**.

**⚠⚠ THE THING THAT IS WRONG: ROUTINES 1, 2 AND 3 PRODUCED NO COMMITTED OUTPUT TODAY.** Observable facts,
not inference from timestamps: **`git log` shows no commit dated 2026-09-28** — the newest is Friday's
20:59 UTC weekly-review merge; **`git ls-remote` shows only `main`**, no working branch from today;
**`plan_today.md` still carries `plan_date: 2026-09-25`**; **`state.md`'s `last_run` still reads
2026-09-25 16:45 ET.** ⚠ **The repo's own definition of a run having happened is a commit — "push, or it
never happened" — and by that definition three of today's four runs did not happen.**
⚠ **`control.md` warns not to diagnose schedule faults from run TIMESTAMPS, and this is not that: it is
the ABSENCE of committed output on a confirmed full session. The cause is not visible from inside this
run and is NOT asserted here. It is a question for the human.**
⚠⚠ **TODAY'S COST WAS ZERO AND THAT IS LUCK, NOT DESIGN** — an empty sleeve meant routine 3 had nothing to
manage, and an empty plan meant routine 2 had nothing to execute. ⚠ **On a day with an open satellite
position, a missing routine 3 is an unmanaged §5 book for a full session.**
⚠⚠ **AND ONE PIECE OF EVIDENCE WAS DESTROYED BY THE GAP: today was the FIRST morning in this account's
history with a GENUINELY STALE `plan_today.md`.** The staleness gate has been exercised 28 times and has
never fired; its alert path is **untested code**; the carry-forward predicted in writing that *"the first
morning it fires will by construction be a morning when the pre-market run failed."* ⚠ **That morning
arrived, and the gate was not reached, because the run that contains it did not execute. The prediction
was exactly right about the setup and the test still did not happen. The gate remains untested code and
the 28 is now 28, not 29.**
⚠ **`plan_today.md` IS LEFT UNTOUCHED, DELIBERATELY.** Routine 4 does not write it, and overwriting a
stale plan_date would erase the only in-repo evidence that the pre-market run did not produce one.

---

**⚠ THE 2026-09-25 PER-RUN BLOCK (FOUR RUNS) HAS BEEN COLLAPSED BY THIS RUN, UNDER THE FILE'S OWN STANDING
INSTRUCTION.** All four recorded the same null — zero satellite blocks against zero satellite Alpaca rows,
agreeing; no §5 rule evaluated; no high-water mark stamped; no backfill due; no order placed. **Nothing
live was discarded.** The load-bearing facts it carried:

- **09-25 official close 710.705 on the basis in force THAT DAY**, a complete session (n 4,250, v 164,725);
  equity **$100,392.71**, day **+$339.23 / +0.3391%**, since inception **+0.3927%**; core 70.117% official /
  70.12% broker, `rebalance_delta` −$117.81 / −$116.21. ⚠ **THOSE CLOSES ARE NOW STALE ON AN
  `--adjustment all` PULL — see today's block. They remain correct on `--adjustment raw`.**
- **The midday volume calibration was WRONG and the close run corrected it:** a partial bar's `v` measured
  against a PRIOR-DAY mean looks like a measurement of the current day and is not one. **`n` and `v` are a
  smell test; the CLOCK is the discriminator.** ⚠ **Today's 62,354-share session re-exercised that rule and
  it held.**
- **A bar dated TODAY is PARTIAL while the market is open**, and the midday shape (n 1,731, v 69,713,
  c 710.555, plausible OHLC) **does not look like a stub**. Routines 2 and 3 both read `is_open: true`.
- **JBL was the most decision-relevant rejection on the board** — $1.7B named and allocated in an 8-K, and
  **capital paid in, held in consignment as bailee, repurchased at cost.** Zero margin. **Do not reach for
  it at a lower price; the price was never the problem.**
- **Excess −0.1452pp against −0.1453pp predicted by the cash weight alone** — the cleanest arithmetic
  demonstration that the book is 70% VOO and nothing else.


**Reconciliation 2026-09-24 — ONE BLOCK FOR THE DATE, ALL FOUR RUNS (1-premarket 08:20, 2-market-open
09:36, 3-midday 12:40, 4-market-close 16:15), UPDATED IN PLACE AND COLLAPSED BY THE CLOSE RUN. THE
LEDGER AGREES WITH THE BROKER AT ALL FOUR; ZERO SATELLITE POSITIONS ON BOTH SIDES AT ALL FOUR; NO ORDER
PLACED AT ANY; NO HIGH-WATER MARK WAS WRITTEN AND NONE WAS DUE AT ANY; NO §5 RULE HAD A SUBJECT.**

**— 16:15 ET, 4-market-close-journal.** Selftest passed all five checks; pre-flight equity **$99,957.40**
(broker mark), `trading_enabled: true`, LIVE paper. `clock` at **16:15:53** reads `is_open: FALSE` with
`next_open` **2026-09-25T09:30** and `next_close` **2026-09-25T16:00** — the **POST-BELL** shape.
⚠ **The stronger discriminator was run rather than inferred: a VOO daily bar for 2026-09-24 EXISTS**
(o 704.10, h 708.505, l 703.355, **c 707.28**, v 141,074, n 3,718). **A session happened; this is not a
holiday skip and the summary is owed.**

**⚠ STEP 2 — THE RUN'S INVISIBLE JOB — HAD NO SUBJECT, AND THAT IS THE CORRECT OUTCOME.** There are
**zero open satellite positions**, so there is **no `highest_close` to raise and, more importantly, no
`(as of …)` date to advance.** `highest_close` is **ABSENT — the third state, carrying no `(as of …)`
date at all** — which is precisely what distinguishes *nothing to backfill* from *a mark silently not
written.* **Zero `bars` calls were due on any satellite symbol and zero were made.** ⚠ **Tomorrow's
midday run must not read the missing stamp as a failed close run. Nothing was skipped; there was no
operand.** ⚠ **This distinction is FREE only while the sleeve is empty and becomes load-bearing the
moment a satellite fill lands. Compare the date; never infer from the field's emptiness.**

**RECONCILIATION CLEAN.** `alpaca.py positions` returns **one row, core VOO** — 99.046311231 shares
unchanged since the 09-03 fill, avg_entry 706.74, cost_basis $69,999.99, market_value $69,957.40.
**Zero satellite blocks against zero satellite Alpaca rows — they agree** (satellite-to-satellite, never
raw ledger to raw broker). **§5.1–§5.4 never started for the thirty-third consecutive session; §5.4 is
STILL NOT ARMED.** The tally of "no exits" records the **absence of a subject**, not thirty-three clean
bills of health.

**⚠⚠ THE DAY'S REAL MOVE WAS EXACTLY ZERO, AND THE BROKER REPORTED −$127.77. THE ENTIRE HEADLINE WAS
ARTIFACT — 100% OF IT.** VOO's **official** close is **707.28**, **identical to the 09-23 close of
707.28**, so the true close-to-close is **$0.00 / +0.000000%**. ⚠ **The identical close was treated as
suspect and verified before use: an independent second `bars` pull on a different window returned the
same 707.28 with DISTINCT OHLV** (09-23 o 712.13 / h 712.38 / l 706.395 / v 147,584; 09-24 o 704.10 /
h 708.505 / l 703.355 / v 141,074). **Two genuinely different sessions that happened to close to the
same cent — a coincidence, not a duplicated bar.**
**On official closes: core $70,053.48 + cash $30,000.00 = equity $100,053.48; day P&L $0.00 (0.000%);
since inception +$53.48 (+0.053475%).** The broker's competing figures — `equity − last_equity`
**−$127.77**, `unrealized_intraday_pl` **−$127.77**, `change_today` **−0.00182** — were **NOT used in
and NOT carried into any figure.** ⚠ **The carry-forward predicted in terms that this rule's value is
INVERSELY PROPORTIONAL TO THE SIZE OF THE REAL MOVE. Today the real move is exactly zero, so the ratio
of artifact to signal is unbounded. That is the prediction confirmed at its limit — and it is a
CONFIRMATION, not a save: the rule was followed because it is standing, not because anything was
spotted.**

**⚠ NEW, AND THE FIRST TIME THE TWO-PRICE DEFECT HAS REACHED A §2 QUANTITY: IT FLIPPED THE SIGN OF
`rebalance_delta`.** `alpaca.py sleeves` at 16:15 (broker marks): equity **$99,957.40**, core
**$69,957.40 = 69.99%**, satellite **0.0% (count 0)**, cash **$30,000.00 = 30.01%**, `core_in_band:
true`, `rebalance_needed: false`, `rebalance_delta` **+$12.78**. **Recomputed on the official close:**
equity **$100,053.48**, core **$70,053.48 = 70.016%**, cash **29.984%**, delta **−$16.04**.
⚠ **Same instant, same position, opposite sign — core reads BELOW target on broker marks and ABOVE
target on official ones.** **It changes nothing today**: §2 rebalances at the **65/75 band edge**, not
to the exact target, and the core sits **4.98 points** from the nearest edge, so **no delta inside the
band is an action at any size on either basis.** **NO REBALANCE IS DUE TOMORROW.** ⚠ **But it is the
same sign-error shape as 09-22, now on the §2 plane rather than the P&L plane, and it would be
load-bearing under any rule that rebalanced TO TARGET rather than AT THE EDGE.** **Forty-second
consecutive run inside the range 69.59–70.22.**

**⚠ FIFTH `lastday_price` OBSERVATION OF THE DAY: 707.60 AT 16:15, IDENTICAL TO 08:20, 09:36 AND
12:40.** The field did not move once across the pre-market, the opening bell, the midday session **or
the close**; the **32-cent error against the official 707.28 survived the entire day.**
⚠ **AND THE 09-24 PRE-MARKET'S FALSIFIABLE PREDICTION HAS GONE PARTLY DEGENERATE — SEE THE JOURNAL.**
Today's official close (707.28) **equals** the number the field was supposed to read today and did not,
so a **707.28** reading tomorrow can no longer distinguish *"correctly rebuilt to 09-24's close"* from
*"belatedly corrected to 09-23's close."* **Only the 707.60 branch stays informative.** **Do not record
a 707.28 reading as a clean rebuild.**

**⚠ `current_price` 706.31 IS 97 CENTS BELOW THE OFFICIAL 707.28 — AND IT IS NOT THE LARGEST IN THE
RECORD, THOUGH THE INHERITED SERIES SAYS IT WOULD BE.** The carry-forward's post-bell series ran
**22c LOW (09-21), 16.9c HIGH (09-22), 2c HIGH (09-23)** — three entries. ⚠ **`journal.md`'s own 09-18
close entry records `current_price` 702.98 against an official 701.85 — $1.13 HIGH, and it was called
"the widest gap yet" at the time. The inherited series had silently dropped its own largest member.**
**Corrected series, five post-bell observations: +$1.13 (09-18), −$0.22 (09-21), +$0.169 (09-22),
+$0.02 (09-23), −$0.97 (09-24).** **97c is the SECOND largest.** **Both signs, range 2c to $1.13, no
predictable sign and no correctable offset.**

**CORE VOO DELIBERATELY NOT STAMPED — FIFTY-FIRST RUN, AND THIS IS A STRONG INSTANCE.** §5 exempts core
from all four sell rules; a `highest_close` on VOO would **fabricate a §5.4 trailing stop on the one
position the strategy exempts**, a stop that could eventually sell core on a drawdown, which §7 forbids
outright. ⚠ **Graded by the standing rule: this run PULLED A FRESH OFFICIAL CLOSE (707.28), HELD IT,
and had an entirely EMPTY Step 2 to put it in — the sharpest form of the temptation, and the exact
profile the ledger flags as a strong instance.** Refused. ⚠ **"Nothing to write" is the correct output
of an empty Step 2, not an invitation to find a row to write it to.**
**GNRC NOT LOOKED AT — TWENTY-THIRD REFUSAL, AND A FREE ONE.** The only `bars` call this run was on
**VOO**, for the day's close; routine 4 has no research step and no candidate was under evaluation, so
there was nowhere to put a GNRC number. **Free is not the same as permitted, and the count accumulates
fastest on exactly the runs where it means least.**

**HOUSEKEEPING — ALL FOUR CHECKS RUN, NONE FIRED.** **Week rollover:** today is Thursday **2026-09-24**
(confirmed via `TZ=America/New_York`, not assumed); its ISO Monday is **2026-09-21** and `week_of`
already reads 2026-09-21 — **sixteenth consecutive run to find the reset already done**,
`new_positions_this_week` stays **0 of 3**, next boundary **Monday 2026-09-28**. **Loss streak:**
**nothing closed today and nothing has ever closed**, so `consecutive_closed_losses` stays **0 — it has
never had an input**; breaker **INACTIVE**, `halt_triggered_at: none`, so **no `HALT_CLEARED_AT`
comparison was required and NO `circuit-breaker` alert was due.** **Unresolved orders:** `orders
--status all` returns **one row for the account's entire history** — the 09-03 core VOO buy,
`status: filled`, terminal. **Nothing is in limbo overnight; no order has EVER reached a non-terminal
state in this account.** `trade_log.md` correctly left unappended — **a day with no fill writes no trade
entry.** `alerts.md` **empty — zero open incidents, zero SYSTEMIC.**

**— EARLIER TODAY, COLLAPSED (08:20 pre-market, 09:36 open, 12:40 midday).** All three recorded the same
null and are compressed here rather than restated; the narrative lives in `journal.md`.
**08:20 pre-market** — `is_open: FALSE` with `next_open` pointing at **TODAY**, the pre-market shape;
equity $99,776.15; core 69.93%, delta **+$67.16**; **research ran in FULL and produced NO TRADE** —
five Perplexity scans (one after an **HTTP 500** that recovered on a reworded retry), **seven candidates
reached a `research_log.md` entry and all seven were rejected** (T-2026-09-24-01 ILMN, -02 GRAL, -03
BBY, -04 PYPL, -05 SHOP, -06 SoftBank/OpenAI, -07 ELMT); **five `alpaca.py move` calls** as §4 hard
filters (PYPL, BBY, SHOP, ILMN, GRAL). ⚠ **The §4 priced-in filter fired on THREE GENUINE RISES — SHOP
+9.61%, ILMN +11.54%, GRAL +44.67% — the first time in volume the record shows it doing its designed
job. It is not broken; it is SIGN-BLIND.** ⚠ **The 09-23 prediction about `lastday_price` was falsified
here: it read 707.60, not 712.78 — the field DID rebuild, and to a number 32c wrong.**
**09:36 open** — `is_open: TRUE`, the **in-session** shape, the one reading where the boolean alone
settles it. **Staleness gate: `plan_date` 2026-09-24 against ET date 2026-09-24 — FRESH, gate did not
fire, twenty-seventh exercise and still never fired; its alert path remains UNTESTED CODE.** ⚠ **The
plan was FRESH *and* EMPTY, and the zero-order run it produced is byte-for-byte what a STALE plan would
have produced. Only `plan_date` distinguished them.** Bootstrap permanently closed (`core_established:
true`); zero BUY intents so **zero `move` re-validation calls were due — an ABSENT check, not a skipped
one**; equity $99,808.83, core 69.94%, delta **+$57.35**.
**12:40 midday** — `is_open: TRUE`; equity $100,113.47, core 70.03%, delta **−$34.04**; **§5 had no
operand**; ⚠ **`TRADING_ENABLED` was TRUE, so a triggered stop WOULD have been submitted — the null is
an EMPTY SLEEVE, not a disabled stop, and those two produce the identical zero-exit line.**
⚠ **ACROSS ALL FOUR RUNS, EVERY GATE THAT COULD HAVE STOPPED A BUY WAS OPEN — breaker INACTIVE, weekly
cap 0 of 3, sleeve empty, ~30% idle cash, no restricting note in `control.md`. NOTHING WAS BLOCKED. The
research simply produced no eligible candidate, and the seven rejections were NOT rehabilitated at any
later run — no `move`, `quote`, `bars` or `asset` call was made on any of them after the pre-market.
A rejection is not a queue.**
*(**One block per date, not one per run.** **Collapse, do not append — forty-ninth consecutive run.**
The close run merged this date's four per-run blocks into the single block above. **Nothing live was
discarded**; the load-bearing facts are carried here and in `state.md`.)*

---

**⚠ THE 2026-09-22 AND 2026-09-23 PER-RUN BLOCKS (EIGHT RUNS, ~350 LINES) HAVE BEEN COLLAPSED BY THIS
RUN, DELIBERATELY AND UNDER THE FILE'S OWN STANDING INSTRUCTION.** Every one of the eight recorded the
same null result — zero satellite blocks checked against zero satellite Alpaca positions, agreeing; no
§5 rule evaluated; no high-water mark to stamp; no backfill due; no order placed. `state.md` flags this
accumulation as **actively harmful rather than untidy**, because this repo's only continuity mechanism
is the next run *reading* these files in full. **Nothing live was discarded.** The load-bearing facts
those blocks carried:

- **09-22 close was the SIGN-ERROR instance** — `lastday_price` **712.78** (2c high) and
  `current_price` **712.859** (16.9c high) **at once, in opposite directions**, so the broker computed
  `equity − last_equity` = **+$7.82 UP** on a day whose true close-to-close was **−$6.93 DOWN**.
  ⚠ **On a flat day the standing rule is a DIRECTION rule, not a precision rule.** And had a satellite
  position existed, stamping `current_price` as `highest_close` would have written 712.859 instead of
  712.69, **silently moving a §5.4 stop 17 cents** — the ledger header's warning, with real numbers.
- **09-23 close: the largest single-day decline since the core was established** — VOO 712.69 → 707.28,
  **−0.759%**, **−$535.84** on the core, **−0.533%** on equity, leaving the account **+0.053% since
  inception**. Grounded from a pulled 25-session series, not asserted.
- **Post-bell `current_price` error runs 22c LOW (09-21), 16.9c HIGH (09-22), 2c HIGH (09-23)** — same
  routine, same minute, **no predictable sign and no correctable offset.**
- **Both halves of the `lastday_price` mechanism were falsified in turn** (09-22: rebuilds; 09-23: does
  not; **09-24: does, and to a 32c-wrong value**). See this run's block above — **the field has no
  reliable structure at all.**
- **Nine theses were written across those two days and all nine were rejected**; none was rehabilitated
  at a later run. **A rejection is not a queue.**
- **The §2 staleness gate was exercised at every open and has never fired; its alert path is untested
  code.** A fresh empty plan and a stale plan produce an identical zero-order run — **read `plan_date`,
  never the outcome.**

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
