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

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-26, **`1-premarket` 08:05 — FIRST SEAT OF THE DATE; later seats append to this block and the close seat closes it.** ⚠ **RE-EVALUATED AT THIS SEAT, NOT INHERITED: a table left alone and a table re-evaluated to the same answer are indistinguishable to the next reader.** This is the **27th** consecutive absent seat, counted forward from Friday's close at the 26th — ⚠ **and the ordinal is stated only because it was counted from the preceding block in the same breath, per the rule against ordinals computed from a truncation.**)

**Ledger reconciled FIRST, before any research — three sides, all agreeing.**
`positions.md` satellite block-header pattern `grep -cE '^### [A-Z]{1,5} '` = **0** · Alpaca
`positions` = **ONE row, core VOO only** (99.046311231 sh @ **706.74**, `cost_basis`
**$69,999.989999**, `market_value` **$69,460.187603**, unrealized **−$539.802396 / −0.771%**,
`current_price` **701.29** — ⚠ **a pre-bell indicative midpoint, NOT a close** — share count
unchanged since 2026-09-03) · `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`.
**NO DISCREPANCY**, so nothing was reconciled — the check was performed and came back clean.
⚠ **GREP TRAP, documented and NOT re-raised: the one `entry_price` hit in this file is line 45,
inside `## Template`.**

⚠ **Zero SELL intents in today's plan and zero satellite rows to test them against, so Step 4
had NO OPERAND. `consecutive_closed_losses` stays 0 — UNTOUCHED, not checked-and-clean.**

| Rule | State | Distance to the rule |
|---|---|---|
| **§5.1** thesis invalidation | **ABSENT — no operand** | No `invalidation` field on any satellite row. **ZERO Perplexity news queries run for §5.1, ZERO DUE** — there is no invalidation string to test news against. ⚠ The four Perplexity calls this run were §4 research, not §5 checks; **do not read the call count as a §5 exercise.** |
| **§5.2** time stop | **ABSENT — no operand** | No `timing_window`, no deadline on any satellite row. |
| **§5.3** hard stop (−7% from entry) | **ABSENT — NOT COMPUTABLE** | No satellite `entry_price` exists. ⚠ **NOT COMPUTABLE is a different state from "far away", and the two must not be written the same way.** The 706.74 core fill is **§5-exempt** and is not an operand. |
| **§5.4** trailing stop (−10% from `highest_close`) | **ABSENT — no operand** | No satellite `highest_close` has ever been written in this repo. ⚠ **Core VOO AGAIN NOT STAMPED.** ⚠⚠ **THE REFUSAL COUNT IS WITHHELD RATHER THAN QUOTED — see the 10-23 weekly review: a monotone counter was found to have moved BACKWARDS (95 → 103 → 107 → 102) and is not re-derivable from source, because no file records the individual refusal events. THE REFUSAL ITSELF IS UNBROKEN; ONLY THE NUMBER IS UNTRUSTWORTHY. Do not "fix" it to an inferred figure either.** |

⚠⚠ **STEP 2 HAD NO OPERAND AGAIN AND THE NEXT SEAT MUST READ THAT AS *NOTHING-TO-STAMP*, NOT AS
*STEP-SKIPPED*.** There is no `highest_close` to raise and no `(as of …)` date to advance, so the
midday backfill detector gets **NO INPUT** today: **no staleness detected and NONE RULED OUT.**
⚠ **A detector handed no input returns the same silence as one finding everything healthy.**

⚠ **THE §5.4 TEMPTATION, REFUSED AGAIN AND WITH ITS LIVE NUMBERS WRITTEN OUT SO THE REFUSAL IS
AUDITABLE RATHER THAN ASSERTED:** VOO's max close **over the seven sessions this
seat actually pulled (2026-10-15 → 10-23)** is **710.70 (2026-10-21)**; Friday's official close
is **698.33**, which is **−1.741%** from it. ⚠⚠ **THAT IS A WINDOW MAXIMUM, NOT A TRAILING MAX,
AND THE DIFFERENCE IS NOT COSMETIC: the 10-23 block one section down records **716.29
(2026-10-06)** from a longer pull, against which Friday's close is **−2.507%**. A seven-session
pull cannot produce a since-entry high-water mark, and writing one as though it could is exactly
the §5.4 failure the header rule guards against.** Both readings sit comfortably inside a −10%
trailing band **if core were subject to one.** ⚠⚠ **IT IS NOT. §5's final line
exempts core from all four rules, so this figure is NOT a sell-rule reading and must never be
written into a `highest_close` field, quoted as a §5.4 distance, or carried forward as one.**
⚠ **It is recorded here only to show the number was seen and the stamp was still refused.**

⚠ **AND THE BASIS RULE THAT GUARDS IT, RESTATED BECAUSE THE NEXT EX-DATE RESTORES THE TRAP: a
`highest_close` and the close it is compared against must come from the SAME adjustment basis
and ideally the SAME pull. VOO went ex-dividend 2026-09-28 and `--adjustment all` rescaled every
prior close by 0.99743914. §5.4 fails TOWARD SELLING when the bases are mixed.**

⚠ **A `bars` close dated TODAY may never be stamped as a mark before the bell on any basis — a
partial bar's `c` is the last trade so far wearing a close's clothes. This seat stands at 08:05
and pulled no bar dated today.**

**Friday's completed bar, re-pulled at this seat and carried as context only:** VOO **c 698.33**
(o 698.47, h 701.52, l 697.56), `v` **34,733**, `n` **1,082** — ⚠ **against 34,730 / 1,080 read
by Friday's own 16:16 close seat. +3 shares, +2 trades on a bar that cannot have changed, with
o/h/l/c unchanged. A FRESH INSTANCE OF THE RETIRED n/v DRIFT ITEM, NOT A NEW FINDING — late-print
settlement, and the reason `n`/`v` are unusable as evidence in either direction.**

---

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-23, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` **08:03** · `2-market-open` **09:36** · `3-midday` **12:41** · `4-market-close` **16:16**. ⚠ **CLOSED BY THE CLOSE SEAT, THE ONLY SEAT ENTITLED TO TOUCH WHAT THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written; the close note is the last item below and it CORRECTS two claims the earlier seats left here. ⚠ **RE-EVALUATED AT EACH SEAT, NOT INHERITED: a table left alone and a table re-evaluated to the same answer are indistinguishable to the next reader.** The table below was written at **09:36** and is the **24th** consecutive absent seat; 12:41 is the 25th and the close is the **26th**.)

**Ledger reconciled BEFORE the order path was entered — three sides, all agreeing.**
`positions.md` satellite block-header pattern `grep -cE '^### [A-Z]{1,5} '` = **0** · Alpaca
`positions` = **ONE row, core VOO only** (99.046311231 sh @ **706.74**, `cost_basis`
**$69,999.989999**, `market_value` **$69,165.029596**, unrealized **−$834.960403 / −1.193%**,
`current_price` **698.31**, unchanged in share count since 2026-09-03) · `sleeves`
`satellite.count: 0`, `value: 0`, `pct: 0.0`. **NO DISCREPANCY**, so nothing was reconciled —
the check was performed and came back clean. ⚠ **GREP TRAP, documented and NOT re-raised: the one
`entry_price` hit in this file is line 45, inside `## Template`.**

⚠ **Zero SELL intents in today's plan and zero satellite rows to test them against, so Step 4 had
NO OPERAND. `consecutive_closed_losses` stays 0 — UNTOUCHED, not checked-and-clean.**

| Rule | State | Distance to the rule |
|---|---|---|
| **§5.1** thesis invalidation | **ABSENT — no operand** | No `invalidation` field on any satellite row. **ZERO Perplexity news queries run, ZERO DUE** — there is no invalidation string to test news against. |
| **§5.2** time stop | **ABSENT — no operand** | No `timing_window`, no deadline on any satellite row. |
| **§5.3** hard stop (−7% from entry) | **ABSENT — NOT COMPUTABLE** | No satellite `entry_price` exists. ⚠ **NOT COMPUTABLE is a different state from "far away", and the two must not be written the same way.** The 706.74 core fill is **§5-exempt** and is not an operand. |
| **§5.4** trailing stop (−10% from `highest_close`) | **ABSENT — no operand** | No satellite `highest_close` has ever been written in this repo. ⚠ **Core VOO AGAIN NOT STAMPED — 100th consecutive refusal.** |

⚠⚠ **THE §5.4 TEMPTATION CARRIED A LIVE NUMBER THIS TIME AND WAS REFUSED AGAIN — AND THE 100TH
REFUSAL IS NOT A MILESTONE.** VOO's trailing max close is **716.29 (2026-10-06)**; the live
`current_price` **698.31** at 09:36 is **−2.51%** from it, so a §5.4 stop would be nowhere near
triggering. ⚠ **THAT IS PRECISELY WHAT MAKES STAMPING IT FEEL HARMLESS — it is harmless TODAY.**
Arming a trailing stop against the one sleeve §5 **exempts** and §2 holds **permanently** is not a
thing to do on a quiet day. ⚠ **And 698.31 is a LIVE INTRADAY MIDPOINT, not a close — it is not
comparable to the 716.29 close except as a rough distance, which is a second reason the figure does
not belong on a row.** The 702.02 official 10-22 close is carried as a tape fact and written to no
row.

⚠ **STEP 5's SCOPE IS "EVERY POSITION STILL OPEN" AND THERE ARE NONE, so nothing below the
table was written either.** The absent `highest_close` field is in its **THIRD STATE** —
carrying no date at all, which is neither current-and-unchanged nor stale — so the midday
backfill detector gets **no input** for a 21st consecutive seat: **no staleness detected and
none ruled out.** ⚠ **The repair path has never executed once in this repo's history; the
first satellite fill is its first real test. Its trigger condition is real — the 2026-09-28
and 2026-10-05 close runs genuinely vanished — and it costs nothing only because the sleeve is
empty: LUCK, NOT DESIGN.**


---

**⚠ SEAT 3 OF 4 — `3-midday-position-management` 12:41 ET. RE-EVALUATED, NOT INHERITED, AND THE
TABLE ABOVE STANDS UNCHANGED: all four rules still ABSENT, 25th consecutive seat.** Ledger
reconciled three sides again at this seat and agreeing: Alpaca `positions` **ONE row, core VOO
only** (99.046311231 sh @ 706.74, `market_value` 69,410.664448, `current_price` **700.79**,
unrealized **−589.325551 / −0.842%**) · satellite block-header count in this file **0** · `sleeves`
`satellite.count 0 / value 0 / pct 0.0`. **ZERO exits taken, ZERO were due, and NOTHING SHOULD HAVE
FIRED AND DID NOT.** Zero Perplexity invalidation queries run and **zero due**. Core VOO **not
stamped** — one clause, the count is in `state.md`.

⚠⚠⚠ **AND THIS SEAT ADVANCED THE ITEM DIRECTLY ABOVE, WHICH THIS FILE HAS CARRIED FOR 21 SEATS AS
"NEVER EXECUTED, FIRST FILL IS ITS FIRST TEST": THE BACKFILL COMMAND WAS RUN FOR THE FIRST TIME,
AGAINST VOO AS A TOOL CHECK WITH NOTHING STAMPED ANYWHERE — AND STEP 2'S PRESCRIPTION, AS WRITTEN,
WOULD MANUFACTURE A PHANTOM HIGH-WATER MARK.** `bars --symbol VOO --days 5 --adjustment all` at
12:41 returned **five** bars, and the last one is **TODAY'S, STILL IN PROGRESS**: dated 2026-10-23
with `c` **700.69**, `n` **572** trades and `v` **16,676** against yesterday's `n` 2,597 / `v`
62,938 — and its `c` tracks the live `current_price` 700.79, because **on an unfinished session `c`
is the last trade, not a close.**
⚠ **Step 2 says "take the maximum close from entry date forward," and that maximum is taken over a
set that INCLUDES the partial bar.** So on any day where the intraday print exceeds every real
close since entry — **which is exactly what a winner making new highs looks like** — the midday
seat stamps `highest_close` with a price that was never a close, and **§5.4's trailing stop is
tightened against a position that never closed there.**
⚠ **THE FAILURE DIRECTION IS TOWARD SELLING — THE SAME DIRECTION AS THE EX-DIVIDEND BASIS ARTIFACT
AT THE TOP OF THIS FILE, AND IT COMPOUNDS WITH IT.** A mark that is too high and a comparison close
that is too low both eat the stop's width from the same end.
⚠ **IT COST NOTHING TODAY AND THAT WAS LUCK, NOT SAFETY:** today's partial `c` 700.69 and today's
high 701.52 both sit **below** all four real closes in the window (704.47 · 706.33 · **710.70** ·
702.02), so the max would have come from a finished bar anyway. Had the tape been up, it would not.
⚠ **THE FIX IS IN THE PROMPT, NOT THE SCRIPT, AND IT IS ONE CLAUSE: when backfilling at any
PRE-CLOSE seat, take the max over bars STRICTLY BEFORE today's ET date.** ⚠ **The close seat at
16:16 is unaffected — by then the bar is finished — so this is specific to routine 3, the one
routine whose whole purpose is to repair this field.** ⚠ **NOT THE SAME DEFECT AS HUMAN ITEM 12:
that one is routine 2 Step 6 writing `voo_close_at_entry` from a partial bar (a BENCHMARK LABEL);
this one is routine 3 Step 2 writing `highest_close` (A STOP OPERAND). Same root cause, different
field, different routine, and this one can sell a position.**

---

**⚠ SEAT 4 OF 4 — `4-market-close-journal` 16:16 ET, THE CLOSE SEAT. RE-EVALUATED, NOT
INHERITED: all four rules still ABSENT, 26th consecutive seat** (24th at 09:36 · 25th at 12:41 ·
26th here). Ledger reconciled three sides after the bell and agreeing: Alpaca `positions` **ONE
row, core VOO only** (99.046311231 sh @ 706.74, `cost_basis` 69,999.989999, `market_value`
69,243.276182, `current_price` **699.10**, unrealized **−756.713817 / −1.081%**) · satellite
block-header count in this file **0** · `sleeves` `satellite.count 0 / value 0 / pct 0.0`.

⚠⚠ **STEP 2 — THE HIGH-WATER WRITE, THE ONLY REASON THIS ROUTINE RUNS AT 16:15 RATHER THAN
16:00 — HAD NO OPERAND, AND THE NEXT RUN MUST READ THAT AS "NOTHING TO STAMP", NOT AS "NOT
RUN".** Zero open satellite positions, so there was no `highest_close` to raise and no
`(as of …)` date to advance. **The field is ABSENT — the third state, carrying no date at
all — which is neither current-and-unchanged nor stale.** ⚠ **Monday's midday backfill
detector will again get NO INPUT: no staleness detected and NONE RULED OUT.** The step was
performed and had nothing to write; **"high-water marks updated" would have been a false
sentence and is not claimed.** Core VOO **not stamped** — 102nd consecutive refusal (99th at
08:03 · 100th at 09:36 · 101st at 12:41 · 102nd here); the count is tracked in `state.md`.

⚠⚠⚠ **AND THIS SEAT CLOSES THE 12:41 FINDING DIRECTLY ABOVE BY MEASURING IT AGAINST THE
FINISHED BAR — THE PREDICTION HELD AND NOW CARRIES A PRICE.** The same
`bars --symbol VOO --days 1 --adjustment all` pull at 16:16, with the session over, returns the
**COMPLETE** 2026-10-23 bar: `o` 698.47 · `h` **701.52** · `l` 697.56 · `c` **698.33** · `n`
**1,080** · `v` **34,730**. Against the 12:41 partial (`c` 700.69 · `n` 572 · `v` 16,676):
⚠ **the partial `c` sat $2.36 ABOVE the real close**, and `v` doubled while `h` did not move,
so the day's high was already set by midday and the afternoon only sold off. **Had the midday
seat stamped a mark from that bar it would have written 700.69 for a session that closed
698.33 — a $2.36 phantom, 0.34% of the stop's 10% width, taken out of the selling side on a
day the tape went DOWN.** ⚠ **The defect is confirmed as real and is not a worst case: it is
bounded below by nothing, and on an up day the partial `c` is the day's high rather than
$2.36 under it.** The one-clause fix stands — **at any pre-close seat, max over bars STRICTLY
BEFORE today's ET date** — and this seat needed no such guard, which is the asymmetry that
makes it routine 3's defect alone.

⚠⚠ **CORRECTION TO THE PARAGRAPH ABOVE, AND IT REPLACES THE CLAIM RATHER THAN SITTING BESIDE
IT: ONE CLOSE RUN HAS VANISHED IN THIS REPO'S HISTORY, NOT TWO.** The Step 5 paragraph above
(and the tracked item in `state.md`) say *"the 2026-09-28 and 2026-10-05 close runs genuinely
vanished"* and that **both** journal entries are gone and unrecoverable. ⚠ **The 2026-09-28
entry is in the repo and always was** — `archive/journal/2026-09.md` holds it in full, a
contemporaneous close-seat entry carrying its own 16:16:24 `clock` read, the complete 09-28
VOO bar and the ex-dividend discovery that the whole dividend thread descends from. That
archive was written by the **2026-10-02** monthly rollover, which moved **all 22** September
entries verbatim, so the entry was committed before 10-02 and cannot have been reconstructed
later. ⚠ **2026-10-05 is the ONLY gap**, verified below. **The detection gap is unchanged and
the item stays open — one vanished run is still a vanished run — but its headline figure was
wrong, and it is a TRACKED item, which is the shape this repo keeps being told to trust over
prose.**

⚠⚠ **AND THE DETECTOR THAT "STILL DOES NOT EXIST" (open human item 11) IS A SUPERSET TEST OVER
DATA ALREADY COMMITTED, RUN FOR THE FIRST TIME AT THIS SEAT.** `journal.md` is written by this
routine and only this routine, one entry per trading day, so **the set of session dates from a
`bars --adjustment all` pull must be a SUBSET of the `### YYYY-MM-DD` headings in `journal.md`
plus `archive/journal/`.** Run over the 90-session window: **exactly one session has no journal
entry — 2026-10-05** (the pre-09-01 sessions predate journaling and are excluded by date).
⚠ **It must be a SUBSET test, not equality: 2026-09-07 is a journal heading with no session row,
because Labor Day correctly produced a holiday-skip entry.** ⚠ **It needs no new script, no new
`state.md` field, and — the part that matters — IT WORKS ON AN EMPTY LEDGER, which is exactly
where the date-based staleness route in this file gets no input.** **FLAGGED, NOT BUILT: the
routine prompts are not this seat's to edit. It is now the seventh item for tonight's review.**

| §5 rule | State at the close | Distance |
|---|---|---|
| **§5.1** invalidation | **ABSENT — no operand** | No `invalidation` string on any satellite row. **ZERO Perplexity news queries run, ZERO DUE.** |
| **§5.2** time stop | **ABSENT — no operand** | No `timing_window`, no deadline anywhere. |
| **§5.3** hard stop (−7%) | **ABSENT — NOT COMPUTABLE** | No satellite `entry_price`. ⚠ **NOT COMPUTABLE, which is a different state from "far away."** |
| **§5.4** trailing stop (−10%) | **ABSENT — no operand** | No satellite `highest_close` has ever been written. Core **not stamped, 102nd refusal.** |

⚠ **The core §5.4 arithmetic, computed CLOSE-TO-CLOSE FROM ONE PULL as the top-of-file rule
requires, and written to NO row:** VOO's trailing max close is **716.29 (2026-10-06)** and
today's official **698.33** is **−2.5074%** from it (10-22 read −1.99% on the same basis).
⚠ **Both figures come from the SAME `--adjustment all` call, so the ex-dividend artifact at the
top of this file cannot be in this comparison.** Still nowhere near −10%, **and that is still
exactly what makes stamping it feel harmless.**

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-22, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` **08:07** · `2-market-open` **09:36** · `3-midday` **12:41** · `4-market-close` **16:16**. ⚠ **CLOSED BY THE CLOSE SEAT, THE ONLY SEAT ENTITLED TO TOUCH WHAT THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. The 09:36 and 12:41 seats wrote nothing here; the close note is the last item below. ⚠ **RE-EVALUATED AT THIS SEAT, NOT INHERITED: a table left alone and a table re-evaluated to the same answer are indistinguishable to the next reader.**)

**Ledger reconciled FIRST, before any research — three sides, all agreeing.**
`positions.md` satellite block-header pattern `grep -cE '^### [A-Z]{1,5} '` = **0** · Alpaca
`positions` = **ONE row, core VOO only** (99.046311231 sh @ **706.74**, `cost_basis`
**$69,999.989999**, unchanged since 2026-09-03) · `sleeves` `satellite.count: 0`, `value: 0`,
`pct: 0.0`. **NO DISCREPANCY.** ⚠ **GREP TRAP, documented and NOT re-raised: the one `entry_price`
hit in this file is line 45, inside `## Template`.**

| Rule | State | Distance to the rule |
|---|---|---|
| **§5.1** thesis invalidation | **ABSENT — no operand** | No `invalidation` field on any satellite row. **ZERO Perplexity news queries run, ZERO DUE** — Step 4.1 has nothing to check news against. |
| **§5.2** time stop | **ABSENT — no operand** | No `timing_window`, no deadline on any satellite row. |
| **§5.3** hard stop (−7% from entry) | **ABSENT — NOT COMPUTABLE** | No satellite `entry_price`. ⚠ **"Not computable" ≠ "far away".** The 706.74 core fill is **§5-EXEMPT**, not an operand. |
| **§5.4** trailing stop (−10% from `highest_close`) | **ABSENT — no operand** | No satellite `highest_close` anywhere in this file. |

⚠ **NINETEENTH consecutive seat recording §5 as ABSENT rather than PASSING.** The distinction is
load-bearing and is the reason this table is re-typed rather than dated forward.

⚠ **CORE VOO NOT STAMPED WITH A `highest_close` — 96th CONSECUTIVE REFUSAL, and the GRADE is the
point rather than the count: stamping the one position §5 explicitly EXEMPTS would ARM a §5.4
trailing stop against the sleeve §2 says to hold permanently.** Today's official 10-21 close
(**710.70**) is carried in `state.md` as a tape fact and is written to no position row here.

⚠⚠ **STEP 2 / HIGH-WATER WRITE — STILL NO OPERAND, AND THE CONSEQUENCE IS UNCHANGED AND MUST NOT BE
READ AS A CLEAN BILL.** Zero satellite positions → no `highest_close` to raise and no `(as of …)`
date to advance. The field is **ABSENT — the THIRD STATE, carrying no date at all** — which is
neither "current and unchanged" nor "stale". ⚠ **The midday seat's staleness detector therefore has
**NO INPUT** again today: no staleness was detected and **NONE WAS RULED OUT**. NINETEEN consecutive
seats; the repair path has still never executed once in this repo's history, and a gap that cannot
occur on an empty ledger is not evidence the repair works. The first satellite fill is its first
real test.**

⚠⚠ **TODAY'S ONE-LINE NOTE THAT IS NOT A NULL: the §5 table had its closest brush yet with having an
operand, and it is worth one line because it is the reason the next seat should not read this block as
routine.** `T-2026-10-22-01` (**AMKR** / NVIDIA **$1.3B**, Amkor's own IR release, 2026-10-21) is the
best-documented candidate this repo has produced — and it was rejected on **three independent §4
parts** (part 1, it **is** the headline name · part 2, the figure is **`prepayments`**, rule (viii)'s
JBL capital-paid-in shape, with no segment and no revenue share · part 3, the only date in the
document is **end-2028**, ~9 quarters against §4's two). ⚠ **Had it been bought, this file would
today hold its first `entry_price`, `invalidation`, `timing_window` and `highest_close`, and every
"no operand" line above would have become a live computation. IT WAS NOT BOUGHT, AND THE REASONS ARE
NOT PRICE-DEPENDENT — see `plan_today.md` and `research_log.md`.**

⚠⚠ **CLOSE SEAT, 16:16 ET — THE STEP 2 HIGH-WATER WRITE RAN AND HAD NO OPERAND. THIS IS THE SEAT THAT
OWNS THE WRITE, SO ITS NULL IS THE ONE THAT MATTERS.** Re-reconciled at the bell, three sides still
agreeing (Alpaca `positions` **one row**, core VOO only · this file's satellite block-header `grep -cE`
= **0** · `sleeves` `satellite.count: 0`). **No `highest_close` was raised and no `(as of …)` date was
advanced, because there is no row carrying either.** ⚠ **The field remains ABSENT — the THIRD STATE,
no date at all — so tomorrow's midday backfill detector gets NO INPUT for a TWENTIETH consecutive
seat: no staleness detected and NONE RULED OUT.** The repair path has still never executed once in this
repo's history; the first satellite fill is its first real test.
⚠ **CORE VOO AGAIN NOT STAMPED — 98th CONSECUTIVE REFUSAL.** Today's official close (**702.02**,
`bars --adjustment all`, session proved complete off the clock's post-bell date signature) is carried
in `state.md` as a tape fact and is written to no position row here. ⚠ **The temptation had a number
behind it today: VOO's trailing max close is 716.29 (2026-10-06) and 702.02 is −1.99% from it, so a
§5.4 stop would have been nowhere near triggering. That is what makes stamping it feel harmless — it is
harmless TODAY, and arming a trailing stop against the sleeve §2 says to hold permanently is not a
thing to do on a quiet day.**

---

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-21, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` 08:03 · `2-market-open` 09:36 · `3-midday` 12:41 · `4-market-close` 16:16. ⚠ **COLLAPSED *AND REPAIRED* BY THE CLOSE SEAT, THE FIRST SEAT ENTITLED TO TOUCH WHAT THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. ⚠ **RE-EVALUATED AT THIS SEAT, NOT LEFT: a table untouched and a table re-evaluated to the same answer are indistinguishable to the next reader.**)

⚠⚠⚠ **THE REPAIR THIS SEAT MADE IS THE DAY'S REAL FINDING IN THIS FILE, AND IT IS A DEFECT THIS FILE
ALREADY NAMED NINE DAYS AGO: THE 12:41 MIDDAY SEAT'S 2026-10-21 DIGEST WAS PHYSICALLY INSIDE THE
**2026-10-06** RECONCILIATION BLOCK — 438 lines below the 10-21 block it was written for, under a heading
dated FIFTEEN DAYS EARLIER.** ⚠ **AND `state.md`'s own `last_run` field asserts the opposite in writing:
*"positions.md 10-21 midday digest APPENDED to the session block the 08:03 seat opened (NOT a new
block)"*. The append happened; the destination did not. **A seat that verifies its line COUNT (`+47`,
taken from the tool) can still be wrong about its line POSITION, and nothing in a diffstat distinguishes
the two.** ⚠⚠ **THE 10-12 CLOSE SEAT WROTE THE RULE THAT CATCHES THIS, IN THIS FILE, AT THE TOP OF THE
10-12 DIGEST: *"dated material living under another date's heading is the same defect as a fresh date
over a stale body."* It was written on 10-12 and broken on 10-21 by a seat that read the file. ⚠ **THE
CHECK IS ONE LINE AND IT IS CHEAP: after appending a dated block, `grep -n` the date headers and confirm
your insertion point is inside the one you named. Verifying the SIZE of a write is not verifying its
PLACE.** **Both halves of the 10-21 material are now joined here, in one dated digest, and nothing live
was discarded — the three seats' findings are below, one line each.**

**LEDGER RECONCILED FIRST AT ALL FOUR SEATS, BEFORE ANY §5 RULE WAS READ. THREE SIDES AGREED EVERY
TIME.** `alpaca.py positions` returns **one row, core VOO**, qty **99.046311231** (unchanged since the
2026-09-03 fill), avg_entry **706.74**, `cost_basis` **$69,999.989999** · **ZERO satellite blocks in this
file** · `sleeves` reports `satellite.count: 0` — at 08:03, 09:36, 12:41 and 16:16 alike. **No
discrepancy at any seat. Nothing was researched, and nothing was placed, on top of a ledger in doubt.**
⚠ **Verified STRUCTURALLY at the 09:36, 12:41 and 16:16 seats, not by eye: `grep -cE` for this file's own
position-block header pattern returns **0**, and the only `entry_price` hit is line 45 inside
`## Template` — the documented grep trap, RE-CONFIRMED rather than re-raised as a finding.**
⚠ **Core VOO was struck from the working list BEFORE any §5 rule was read at every seat, per §5's core
exemption. It is not a satellite operand and is never a §5 subject.**

| §5 rule | Status | Operand |
|---|---|---|
| §5.1 thesis invalidation | **ABSENT** | No thesis is held. **Zero Perplexity invalidation checks were run at any seat, and zero were due** — there is no `invalidation` field to test. |
| §5.2 time stop | **ABSENT** | No `deadline` field exists. |
| §5.3 hard stop (−7% from entry) | **ABSENT** | No `entry_price` field on any satellite row. ⚠ **Distance to the rule is NOT COMPUTABLE, which is different from "far away".** |
| §5.4 trailing stop (−10% from `highest_close`) | **ABSENT** | ⚠ **`highest_close` has never been written in this repo's history — an EIGHTEENTH consecutive seat with no operand. The gap that would silently disable §5.4 cannot occur on an empty ledger, which is NOT evidence that the backfill repair works.** |

⚠⚠⚠ **STEP 2 — THE HIGH-WATER WRITE, WHICH IS THIS ROUTINE'S OWN REASON FOR EXISTING — HAD NO OPERAND,
AND "HIGH-WATER MARKS UPDATED" WOULD HAVE BEEN A FALSE SENTENCE.** There are **zero open satellite
positions**, so there was **no `highest_close` to raise and no `(as of …)` date to advance.** ⚠ **The
field is ABSENT — the THIRD STATE, carrying no `(as of …)` date at all — which is NOT the same as
`current and unchanged` and NOT the same as `stale`.** ⚠⚠ **THAT MATTERS FOR TOMORROW'S MIDDAY SEAT
SPECIFICALLY: routine 3's Step 2 backfill decides from the `(as of …)` DATE, and with no date anywhere in
this file its detector has NO INPUT. So no staleness was detected and **none was ruled out** — a detector
handed no input returns the same silence as a detector finding nothing wrong.** ⚠ **The repair path has
still never executed once in this repo's history, across 18 consecutive seats. The first satellite fill
is its first real test.**

**TODAY'S OFFICIAL CLOSE IS RECORDED HERE FOR THE RECORD AND STAMPED NOWHERE.** `bars --symbol VOO
--days 4 --adjustment all` at 16:16, on a session the clock proved COMPLETE (`is_open: false` with
**both** `next_open` and `next_close` dated **2026-10-22** — the post-bell signature): **2026-10-21 `c`
710.70** (`n` 1,228 / `v` 24,709), against **10-20 706.33** · **10-19 704.47** · **10-16 701.745**.
⚠⚠ **CORE VOO WAS AGAIN NOT STAMPED WITH A `highest_close` — A 95th CONSECUTIVE RUN DECLINING IT, AND
THE REASON IS NOT TIDINESS: stamping the one position §5 EXEMPTS would ARM a §5.4 trailing stop against
it, manufacturing a sell rule on a holding the strategy says is never sold on news.**
⚠ **The 09:36 seat met the partial-bar trap today in its exact documented form and refused it on sight —
the same `bars` call six minutes after the bell returned a 2026-10-21 row at `c` **708.04**, `n` **64**,
`v` **1,966**: a RUNNING bar wearing a close's clothes, recorded nowhere as a close. The standing item
worked as written. The completed bar closed 2.66 higher than that running print.**

**§2 IN BAND ALL DAY, AND NO REBALANCE IS DUE TOMORROW.** Core **70.05% (08:03) → 70.04% (09:36) →
70.11% (12:41) → 70.12% (16:16)**, `core_in_band: true` and `rebalance_needed: false` at every seat ·
satellite **$0.00 / 0.0% / count 0** · cash **$30,000.00 exactly** (~44th consecutive unchanged reading)
· equity **$100,167.38 → $100,123.81 → $100,376.32 → $100,394.19** on live marks.
⚠ **`rebalance_delta` ran **−50.21 → −37.14 → −112.89 → −118.26** across the four seats: SAME SIGN, SAME
SESSION, re-computed at each seat and never inherited. It is a DISTANCE READOUT to a perfect 70.00%, not
an instruction — $118 on a $70,394 position is 0.17%, and the whole range is VOO's mark moving under a
FIXED share count, not drift developing.** ⚠ **§2 assigns any rebalance to the market-open run; the
09:36 seat had none to place and Step 7 correctly placed nothing.**

**THE DAY'S HONEST P&L, CLOSE-TO-CLOSE ON ONE STATED BASIS.** Official closes, `--adjustment all`:
**99.046311231 × 706.33 + 30,000 = $99,959.38** → **99.046311231 × 710.70 + 30,000 = $100,392.21**, i.e.
**+$432.83 (+0.433%)** on VOO's **+$4.37 (+0.619%)**. Core unrealized against the 706.74 fill:
**+$392.22 (+0.560%)** — **a mark moving, not a result.**
⚠⚠ **NEVER differenced from `equity − last_equity`, `change_today` (+0.00555) or
`unrealized_intraday_pl` (+$388.26). All three are built on `lastday_price`, which read **706.80** at
ALL FOUR SEATS today against the official 10-20 close of **706.33** (+$0.47) — a SEVENTEENTH consecutive
seat, FROZEN WITHIN the session and moving ACROSS sessions, which is exactly why it is not a correctable
offset. Recognised on sight per the standing list; not re-derived.**

⚠ **POST-BELL BROKER/OFFICIAL SAMPLE — TENTH ON THAT SERIES, AND THE SMALLEST IN MAGNITUDE YET.**
`positions.current_price` **710.72** against the official `c` **710.70** = **+$0.02**. ⚠ **ORDINAL
COUNTED FROM THE LIST IN `state.md` IN THE SAME BREATH, per the truncated-series rule — that list holds
nine samples (10-02 16:16 +0.470 · 10-02 16:46 −0.0254 · 10-06 +0.1207 · 10-08 +0.57 · 10-09 +0.1500 ·
10-12 −0.19 · 10-14 −0.67 · 10-15 −0.04 · 10-16 −0.6098, four positive and five negative), so this is the
TENTH and the split becomes FIVE–FIVE.** ⚠ **+$0.02 is smaller in magnitude than the previous smallest
(−$0.0254, 10-02 16:46). A sample this small is NOT convergence and NOT a fixed offset: the series has
both signs and a ~26-fold spread, and two numbers nearly agreeing is a coincidence of a moving mark, not
a calibration.** ⚠ **It attributes exactly: equity $100,394.19 − close-basis $100,392.21 = **+$1.98** =
99.046311231 × $0.02, re-confirming `equity = qty × current_price + cash` to the cent.**

**NOTHING WAS TRADED, AND NOTHING WAS DUE.** Zero orders at all four seats · zero exits · **zero
positions near a sell rule, and the honest form is NO OPERAND rather than "nothing close."**
⚠ **ORDER LIMBO CHECKED AND EMPTY at the 12:41 and 16:16 seats: `orders --status all` returns **one row
for the entire account history** — the 2026-09-03 core fill, `status: filled`, terminal. **No order is in
limbo overnight, so §7's unverifiable-order clause has NO OPERAND — which is not the same as a clean
bill.** ⚠ **Nothing should have executed and failed to. `TRADING_ENABLED: true`, so no dry-run intent was
generated or possible.** ⚠⚠ **Every §6 gate PERMITTED a buy all day — breaker INACTIVE, 0 of 3 this week,
sleeve entirely undeployed ($30,000 / 29.88% in cash), `control.md` Notes empty — so the absence of a buy
is a RESEARCH result, not a permission result. Nothing was blocked; nothing qualified.** The four
2026-10-21 theses (`T-2026-10-21-01`…`-04`, all rejected pre-market) were **not re-litigated at the
09:36, 12:41 or 16:16 seats**: a post-bell or midday entry would route around the path that forces every
buy to sleep on a written thesis, and §4 ideas are not those routines' to generate.

⚠ **THE BUY-SIDE FINDING OF THE DAY IS NOT THIS FILE'S AND IS NOT RE-NARRATED HERE — ONE LINE AND A
POINTER.** Seven `move` calls, the largest sample the §4 priced-in filter has ever had, returned
`priced_in: true` on **all seven with ALL SEVEN DOWN** (`COHR` −20.07% · `AMKR` −12.45% · `GLW` −10.94% ·
`GM` −8.24% · `AVGO` −6.41% · `MU` −5.92% · `TSM` −4.43%) against **`VOO` −1.22% / `priced_in: false`**
over the identical window. ⚠ **That is SHAPE ONE at its largest recorded sample, i.e. `state.md`'s OPEN
HUMAN ITEM (1) — NOT a new shape and NOT a new item. A 10-21 seat wrote it up as "shape seven" in four
files before correcting it.** Full statement: `T-2026-10-21-01`. **Only a human may change §4 or
`alpaca.py move`.**
---

**Reconciliation 2026-10-12 — ONE DIGEST FOR THE DATE, ALL FOUR SEATS** (`1-premarket` 08:36,
`2-market-open` 09:37, `3-midday` 12:42, `4-market-close` 16:17). *(⚠ **RESTRUCTURED BY THE 16:17 CLOSE SEAT,
WHICH IS THE FIRST SEAT ENTITLED TO TOUCH IT** — the block had grown to **161 lines, the largest in this
file**, because three successive seats folded themselves into it, and a seat cannot fairly collapse a
paragraph it has just written. ⚠⚠ **AND THE MEASUREMENT IS REPORTED AS IT CAME OUT, NOT AS IT WAS
INTENDED: THIS IS NOT A COLLAPSE. The 10-12 block went 160 lines → 196 and `positions.md` went
85,955B → 87,597B (+1,642)**, because folding a FOURTH seat in, separating the 10-09 material into its
own dated digest and re-writing the whole `sell_rule_status` body all push the other way. **Per-seat density improved; absolute size did not. Item (9)'s mechanism
again, and the honest word for the result is RESTRUCTURED.** ⚠ WHAT WAS REMOVED IS NAMED: four per-seat
narrations of the SAME null, three retellings of the plan handoff, and the duplicated clock/sleeve
readings. **The 10-09 material that had been folded in under a 10-12 heading is now its own dated digest
below — dated material living under another date's heading is the same defect as a fresh date over a
stale body.**)*

**THE LEDGER AGREED WITH THE BROKER AT ALL FOUR SEATS, AND IT WAS EACH RUN'S FIRST JOB.** `alpaca.py
positions` returns **one row, core VOO**, qty **99.046311231** (unchanged since the 2026-09-03 fill),
avg_entry **706.74**, cost_basis **$69,999.99** — against **ZERO satellite blocks in this file** and
`sleeves` reporting `satellite.count: 0`, at 08:36, 09:37, 12:42 and 16:17 alike. **No discrepancy at
any seat. Nothing was researched, and nothing was placed, on top of a ledger in doubt.** ⚠ **Core VOO
was struck from the working list BEFORE any §5 rule was read at every seat, per §5's core exemption. It
is not a satellite operand.**

**CLOCK, READ OFF THE DATE AND NOT THE BOOLEAN, THROUGH A FULL DAY.** 08:36:59 `is_open: false` with
`next_open` **2026-10-12T09:30** and `next_close` **2026-10-12T16:00**, both carrying TODAY's date — the
pre-market full-session signature, **not a holiday and not an early close**. 09:37:19 and 12:42:05
`is_open: **true**` with `next_open` rolled to **2026-10-13** while `next_close` **stayed at today
16:00** — the mid-session signature. 16:17:05 `is_open: **false**` with **both** `next_open` and
`next_close` dated **2026-10-13** — the **post-bell** signature. ⚠ **FALSE has three meanings and TRUE
has one; the pair of dates separates them. The closed-skip path was not taken at any seat, and the
close seat confirmed the session was real before journaling it.**
⚠ **The 08:36 data plane agreed — `bars --days 4 --adjustment all` returned NO bar dated 2026-10-12 —
which corroborates the DISCRIMINATOR, not any bar's completeness; by 16:17 that bar existed and was
complete.**

**THE TWO OFFICIAL CLOSES THIS DATE DEPENDS ON, BOTH NAMED ON THEIR BASIS.** 2026-10-09 (the comparison
day, pulled 08:36): VOO o 713.52 h 716.37 l 712.75 **c 715.58**, n 1,645 v 70,028, vw 715.336895.
2026-10-12 (pulled 16:17, post-bell, complete): o 715.80 h 716.29 l 714.28 **c 715.315**, n 1,392
v 32,544, vw 715.141777 — **and `--adjustment raw` returns the SAME 715.315**, so the basis is
non-decisive on a post-ex date, as expected from 09-28 onward. ⚠ **THE 09:37 AND 12:42 SEATS' PRICES
ARE NOT CLOSES:** 716.1532 and 715.42 are **LIVE BROKER MIDPOINTS** and are not interchangeable with a
close on any basis.

**WEEK ROLLOVER: ANCHOR RECOMPUTED AT EVERY SEAT, FOUND MATCHING, DELIBERATELY NOT RE-RESET.** Today is
**Monday** (ISO week 42, weekday 1), so the ISO anchor **IS** 2026-10-12 and `state.md` already carried
`week_of: 2026-10-12`, set by the 10-09 review. `new_positions_this_week` stays **0 of 3**.
⚠ **Recomputed rather than trusted, per the rule that the §6 cap must not stay stuck at its limit if a
Friday run fails. It simply matched.**

**PLAN HANDOFF, BOTH DIRECTIONS IN ONE DAY.** The 08:36 seat RECEIVED `plan_date: 2026-10-09` — **three
calendar days old and CORRECT**, because the comparison is against the last **TRADING** day — and then
WROTE `plan_date: 2026-10-12`. The 09:37 seat READ that field against the clock's ET date and found it
**FRESH**, so **the staleness gate did not fire; non-exercise count 38, still never fired, alert path
still untested code.**
⚠⚠ **AND THE PLAN IT PASSED WAS FRESH *AND* EMPTY — zero BUY, zero SELL, zero REBALANCE — WHICH IS THE
EXACT CASE WHERE FRESHNESS CANNOT BE INFERRED FROM THE OUTCOME. Recorded here as FRESH.**

**SLEEVES, FOUR MARKS ACROSS ONE DAY, NOT DIFFERENCED INTO A TREND:** 08:36 equity **$100,874.57**,
core **70.26%**, `rebalance_delta` **−$262.37** · 09:37 **$100,932.33** / **70.28%** / **−$279.70** ·
12:42 **$100,859.71** / **70.26%** / **−$257.91** · **16:17 $100,830.49 / 70.2471% / −$249.15**, cash
**$30,000.00 = 29.75%**, satellite **$0 / 0.0% / count 0**, `core_in_band: true`,
`rebalance_needed: false`. **Core sits inside §2's 65–75% band with 5.25 points at the lower edge and
4.75 at the upper — the 82nd consecutive run inside it (unit: a RUN; inherited-and-incremented, not
re-derived). NO REBALANCE DUE AT TOMORROW'S OPEN.**
⚠ **`rebalance_delta` is a DISTANCE READOUT, not an instruction: §2 acts at the band EDGE, not at the
70% target, and core sits fractionally ABOVE target rather than outside the band. The delta widened
−$262.37 → −$279.70 across the bell and then narrowed back to −$249.15 by the close, with **NO ORDER in
the entire interval** — purely VOO moving. **FOUR SAMPLES IN ONE DAY RETRACING THEMSELVES IS THE
STRONGEST ARGUMENT YET AGAINST DIFFERENCING SUCCESSIVE READINGS INTO ANYTHING.**
⚠ **A SEVENTH SAMPLE OF THE MOVING LIVE MARK, AND IT IS THE FIRST ZERO: at 09:37 `selftest.py` read
equity $100,939.44 against `sleeves` $100,932.33 seconds later (a $7.11 spread); at 16:17 both read
**$100,830.49 exactly**. ⚠ **The spread vanished because the mark is STATIC after the bell, not because
the readings became reliable — the series measures the clock, not the data.**

**§5 — ALL FOUR RULES RE-EVALUATED IN ORDER AT EVERY SEAT AND ALL FOUR HAVE NO OPERAND.** 5.1 no
invalidation string to test, 5.2 no `timing_window`, and 5.3 / 5.4 are **UNDEFINED, NOT DISTANT**.
⚠ **"Nothing is near a stop" is a statement about an EMPTY SET.** ⚠ **`consecutive_closed_losses` stays
0 and CANNOT MOVE on an empty sleeve — the increment path and the circuit-breaker alert path both remain
UNTESTED CODE.** ⚠⚠ **NEITHER THE 09:37 NOR THE 16:17 SEAT REACHED THE LOSS-STREAK UPDATE AT ALL: zero
SELL intents and zero closes, so 0 is an UNTOUCHED counter rather than a reset one.**

**THE BROKER/OFFICIAL PRICE SERIES, EXTENDED AT THIS SEAT AND STILL NOT A CALIBRATION.**
`current_price` ran **716.1532 (09:37) → 715.42 (12:42) → 715.125 (16:17)**, and the post-bell reading
sits **−$0.19 BELOW** the official close 715.315 — a **sixth** post-bell sample, and the signs across
the series are both positive and negative (+$0.470, −$0.0254, +$0.1207, +$0.57, +$0.15, **−$0.19**),
a spread of more than twenty-fold. ⚠ **IT IS A MOVING LIVE MIDPOINT, NOT AN OFFSET, AND MAY NEVER BE
DIFFERENCED AGAINST AN OFFICIAL CLOSE.**
⚠⚠ **`lastday_price` READ 715.59 AT ALL FOUR SEATS, BYTE-IDENTICAL END TO END — the third complete
session confirming it behaves as a FIXED prior-day field while `current_price` moved — AND IT IS **NOT**
10-09's OFFICIAL CLOSE 715.58.** **A 1¢ disagreement between the broker's prior-day field and the
completed bar, on the SAME session, reported rather than reconciled away:** this field was treated as a
fixed prior-day close all day, and a cent of drift against the bar is exactly the basis difference the
top-of-file §5.4 rule was written about.
⚠ **NEW 16:17 — `balance_asof` READS 2026-10-09 AFTER TODAY'S BELL.** The broker's balance date has not
rolled to today. **Reported, not reconciled away.** It is the same field whose advance past the pay date
settled the dividend test on 10-08, so this log has leaned on it once already.
⚠ **NEW 16:17 — THE CHEAPEST `n`/`v` DRIFT INSTANCE ON RECORD: the same complete 2026-10-12 bar read
`n` 1,392 / `v` 32,544 and then `n` 1,393 / `v` 32,547 roughly a minute later, post-bell, market shut,
with `c`/`o`/`h`/`l`/`vw` identical to the cent.** ⚠ **It CONFIRMS the retired floor test's retirement
and adds nothing: a field that moves on a bar that cannot have changed is unusable as evidence in either
direction. THE CLOCK REMAINS THE ONLY WORKING MARKET-STATE DISCRIMINATOR.**

⚠⚠ **STEP 2 — THE HIGH-WATER MARKS, THE ONE JOB THE CLOSE RUN OWNS ALONE — HAD NO OPERAND FOR A FIFTH
CONSECUTIVE CLOSE SEAT, AND THE MIDDAY DETECTOR HAD NONE FOR A FOURTH.** There are **zero open
satellite positions**, so there was **no `highest_close` to raise and no `(as of …)` date to advance**.
`highest_close` is **ABSENT — the third state, carrying no date at all** — so the every-day date rule
had nothing to write onto and the midday staleness comparison had **no left-hand side**. ⚠ **"HIGH-WATER
MARKS UPDATED" WOULD BE FALSE TODAY, AND SO WOULD "VERIFIED". The honest form is: the job had no
subject.** ⚠⚠ **THE NEXT RUN NEEDS NO BACKFILL, AND THE REASON IS THAT THERE IS NO FIELD, NOT THAT THE
FIELD IS FRESH.** §5.4 arms on the first **SATELLITE** fill; the 09-03 core fill was not one, and the
backfill path remains **UNEXERCISED CODE**. ⚠ **On the day it arms, open item (12) fires the same
morning — routine 2's Step 6 would stamp a partial bar's `c` into `voo_close_at_entry`.**
⚠ **The 12:42 seat's ONE `bars` call (`--days 4`) established 10-09's close as the comparison's RIGHT
hand side and found no LEFT one — a REFERENCE, not a repair. The 16:17 seat's two calls were for the
day's P&L basis, not for a mark.**

⚠⚠ **CORE VOO WAS NOT STAMPED WITH A `highest_close` — A 91st CONSECUTIVE RUN DECLINING IT, AND THE
16:17 SEAT'S INSTANCE IS THE STRONGEST GRADE ANY SEAT CAN GIVE:** it held a **real, complete, official
close on the correct basis (715.315)**, it **owns the Step 2 write path**, the field is **empty**, and
VOO is the **only row the broker returns**. ⚠ **Declined on its merits, re-made rather than inherited:
writing it would ARM A §5.4 TRAILING STOP ON THE ONE POSITION §5 EXEMPTS — a stop that could eventually
sell core, which §7 forbids outright.** ⚠ **The 08:36, 09:37 and 12:42 seats declined it on weaker
grades: routine 2 and routine 3 hold no stamp write path at all.**

**HOUSEKEEPING:** **Breaker INACTIVE**, `halt_triggered_at: none`, so **no `HALT_CLEARED_AT` comparison
was due** at any seat. **`control.md` notes EMPTY. Zero open alerts** — ⚠ **which is not evidence every
seat ran; a run dying before `commit.py` leaves no trace by construction.** **STEP 3 CORE BOOTSTRAP
SKIPPED** on `core_established: true` — that path ran once, on 2026-09-03, and by construction never
runs again. **Do not re-bootstrap.** **`orders --status all` returns ONE ROW for the whole account
history** (the 09-03 core fill, terminal) at every seat, **so §7's overnight-limbo warning has NO
OPERAND rather than a clean bill.**

⚠⚠ **THE LINE THE LEDGER EXISTS FOR, FROM THE 09:37 SEAT — THE ONLY ONE OF THE FOUR THAT MAY OPEN:
EVERY GATE WAS OPEN AND NOTHING WAS BOUGHT.** Breaker **INACTIVE** · `new_positions_this_week`
**0 of 3** · satellite **0% deployed** against a 30% target · **$30,000 idle cash** · `control.md` notes
**EMPTY** · `TRADING_ENABLED: true` · §6's 5% cap standing at **$5,046.62**. **A buy was placeable all
morning. Nothing was worth buying, and §4 says that is the correct output of most runs.** ⚠ **The 12:42
seat's refusal is worth less (exits-only, no buy path) and the 08:36 seat's is worth nothing at all.**

**THE DAY'S RESEARCH, FOR THE LEDGER'S SAKE: five theses written at the 08:36 seat, ALL FIVE REJECTED
(`T-2026-10-12-01` … `-05`), four of them carrying no ticker at all; zero orders, zero buy intents, and
not because anything blocked them. Thesis count 143** (87 archived + 56 live headings; ⚠ the live
`grep -c '^### T-'` returns **57** because the file's own TEMPLATE heading matches — **DO NOT "FIX" 143
TO 144**).
⚠⚠ **THE ONE WORTH A LEDGER NOTE IS `T-2026-10-12-01`, AND IT IS A FINDING ABOUT THIS REPO'S OWN METHOD
RATHER THAN ABOUT A CANDIDATE: THE STRUCTURAL QUERY FRAMING HAS A FALSE-POSITIVE FORM.** The 10-09
US/Russia diesel arrangement returned **two named parties, a precise announcement date, a dated delivery
schedule, a named regulatory instrument with an expiry (OFAC licence to 2027-04-07) and a four-rung
quantity ladder** — the entire shape the framing exists to find — **and it is untradeable, because the
two named parties are SOVEREIGN STATES and the disclosed quantity is NOT MONEY.** ⚠ **THE FIX IS
ADDITIVE AND CHEAP: the structure must ALSO satisfy PARTY TYPE (both parties companies) and UNIT
(dollars, at Company B). "IT RETURNED THE SHAPE" IS NO LONGER SUFFICIENT GROUNDS TO PROCEED TO A
MECHANISM.** ⚠ **The framing is not weakened — on the same run it disposed eight items with reasons
attached for zero follow-up queries.**
⚠ **`T-2026-10-12-02` IS A DISPOSED REJECT RE-SERVED TWICE IN ONE RUN** (RTX SM-3 *"up to $6.3B"*), and
one of the two queries called it **"the closest apparent match"** of the whole session. **Reading the
log first cost one grep and saved the drill.**

⚠⚠ **CATCH (25) IS RECORDED AND FIXED IN THIS FILE — A FRESH DATE OVER A STALE BODY.** The 09:37 seat
re-dated the `sell_rule_status` heading to 2026-10-12 and left 10-09's numbers under it (thesis count
**138**, "today's **eight**", "DO NOT FIX 138 TO 146"). Found and corrected by the 12:42 seat.
⚠ **THE GENERAL FORM: WHEN YOU RE-DATE A SECTION, YOU HAVE ADOPTED EVERY NUMBER IN IT. Re-date the body
or do not re-date the heading.**

---

**Reconciliation 2026-10-09 — ONE DIGEST, ALL FOUR SEATS.** *(Separated out of the 10-12 block by the
10-12 16:17 seat, where it had been folded on 10-12 08:36: dated material living under another date's
heading is the same defect as a fresh date over a stale body. Nothing live discarded.)*
**Ledger agreed with the broker at all four seats** (one VOO row, 99.046311231 at 706.74); **week
rollover NOT due** (computed ISO Monday of Friday 10-09 is 2026-10-05, matching `week_of`); **breaker
INACTIVE**; **core in band all day**; **eight theses written at 08:27, ALL EIGHT REJECTED**; **zero
orders at any seat**; **Step 2 null at both the detector seat and the stamp seat**; **`highest_close`
NOT stamped on core, 87th run, declined on the STRONG grade by the 16:17 seat.**
⚠⚠ **`T-2026-10-09-01`, GFS/TSMC — the *SECOND* candidate in the live log to clear §3's instrument tests
AND the priced-in filter (+1.48% over five sessions, +2.72% on the news day) and then die on the THESIS
PARTS**: part 3 (H1 2028 ramp, six quarters against a two-quarter ceiling) and part 2 (~$400M/yr on
$6.791B revenue = 5.89%, under the 10% floor), both computable from GF's own release in one step each.
**AMD (`T-2026-10-01-02`) did it FIRST, on 10-01, with a stronger §3 pass and the same primary kill.**
⚠ **The non-superlative observation is the useful one: PART 3 KILLED BOTH, and part 2 was failing in
both.**
⚠⚠ **CATCH (24), THE LESSON THAT OUTLIVES THE ITEM: a correction was published as "corrected in ALL
THREE FILES" and there were FOUR — this file carried the same superlative, was not in the enumeration,
and kept it for three seats. The defect is AN ENUMERATION THAT SOUNDED EXHAUSTIVE AND WAS NOT, and the
harm is that it is SELF-CERTIFYING: it reads as closure and suppresses the next re-check. NEVER WRITE A
CORRECTION'S SCOPE AS A COUNT — `grep` the phrase repo-wide, then name the files the grep returned.**
⚠⚠ **AND THE OTHER CORRECTION TO THIS REPO'S OWN ARGUMENT: THE PHANTOM DRAWDOWN IS NOT A ONE-WAY
RATCHET.** `state.md` had written that the cost of a fabricated core mark "GROWS ON ITS OWN". **It
SHRANK** — against a mark stamped at 10-06's 716.29, 10-09's close 715.58 sits **−0.0991%** below,
against **−0.7064%** at the 10-08 close, a **0.607pp recovery in one session**. ⚠ **The refusal to stamp
core is unchanged and is NOT strengthened by the number moving either way; what is corrected is the
ARGUMENT.** ⚠⚠ **THE DURABLE LESSON: AN INHERITED CLAIM THAT ARGUES FOR WHAT YOU ALREADY INTEND TO DO
IS THE ONE YOU ARE LEAST LIKELY TO AUDIT.**

---


**Reconciliation 2026-10-08 — ONE BLOCK FOR THE DATE, COVERING ALL FOUR SEATS:
`1-premarket-research` 08:25 ET, `2-market-open-execution` 09:37 ET, `3-midday-management` 12:41 ET and
`4-market-close-journal` 16:16 ET. ⚠⚠ ALL FOUR RAN AND COMMITTED — 2026-10-08 IS A COMPLETE SESSION,
THE THIRD CONSECUTIVE ONE. ⚠ THREE IN A ROW IS NOT A FIX AND IS NOT EVIDENCE ABOUT THE NEXT SESSION IN
EITHER DIRECTION: the failure mode is a seat that never STARTS. Two of ~28 close runs have vanished
(09-28, 10-05) and THE DETECTION GAP IS UNCHANGED.**
*(Collapsed from four per-seat sections by the 2026-10-09 08:27 seat, 113KB→ smaller, continuing the
rollover item (9) work. ⚠ WHAT WAS REMOVED IS NAMED SO A NEAR-MISS CANNOT VANISH QUIETLY: the four
seats' repeated statements of the same null, the four per-seat sleeve readings, and the four per-seat
restatements of the broker/official gap. EVERY DURABLE FINDING BELOW OR ALREADY IN `state.md`.)*

**THE LEDGER AGREED AT ALL FOUR SEATS AND NOTHING MOVED ALL DAY.** `positions` returned **one row,
core VOO**, 99.046311231 shares at avg_entry 706.74, against **zero satellite blocks** — four
reconciliations, one session, so the session counter advanced only once. **ZERO ORDERS at every seat,
and `orders --status all` returned ONE ROW for the whole account history** (the 09-03 core fill,
filled, terminal) — **nothing in limbo overnight.** **Ten theses, all rejected. Zero sell/quote/move
calls at any seat.**

**THE DAY'S NUMBERS, BOTH BASES, NEVER CONCATENATED.** **OFFICIAL CLOSE 2026-10-08** (`bars --days 3
--adjustment all`, pulled by the 16:16 seat): o 712.26 h 714.11 l 708.45 **c 711.23**, n 1,594 v 41,588,
vw 711.620829 → equity **$100,444.7079**, core **70.1328%**, cash 29.8672%, day **−$339.7288 =
−0.3371%**, since inception **+0.4447%**. VOO itself −0.4799%, so the book **beat it by +0.1429pp ON THE
CASH FLOAT, NOT ON SKILL** (0.702335 × −0.4799485% = −0.337085%, the book's return to six decimals;
satellite contributed **exactly 0.000000%**). **LIVE BROKER MARK 16:16:** equity $100,501.16, core
70.1496%, `current_price` 711.80, `lastday_price` 714.34, `change_today` −0.356%. ⚠ **TWO DAY-RETURNS
FOR ONE DATE, BOTH CORRECT ON THEIR OWN BASIS.**

**THE TWO DURABLE FINDINGS OF THAT SESSION:**
⚠⚠ **(a) `lastday_price` READ 714.34 BYTE-IDENTICAL AT ALL FOUR SEATS — end to end across a complete
session — while `current_price` moved 716.29 → 712.28 over the same span. SO IT IS A FIXED PRIOR-DAY
FIELD, AND THE MOVING-MIDPOINT PROPERTY BELONGS TO THE LIVE MARK ONLY.** ⚠ **This narrows WHICH series
moves; it does not license differencing either against an official close.**
⚠⚠ **(b) A "COMPLETE" BAR IS NOT A "FINAL" BAR: the 2026-10-07 bar read n 1,323 / v 23,415 at 10-07's
16:17 seat and n 1,325 / v 23,423 at 10-08's 08:25 seat — +2 trades, +8 shares, same date, same basis,
16 hours apart, with o/h/l/c and vw UNCHANGED.** ⚠ **A field that sometimes moves on a bar that cannot
have changed is unusable as evidence in either direction. The retired n/v floor test stays retired, and
THE CLOCK REMAINS THE ONLY WORKING MARKET-STATE DISCRIMINATOR.**

⚠ **STEP 2 HAD NO SUBJECT AT ALL FOUR SEATS — the third consecutive close-seat null for the stamp path
and another null for the midday detector. `highest_close` is ABSENT, not stale: no field and no
`(as of …)` date, so staleness could be neither ruled in nor out and the BACKFILL PATH REMAINS
UNEXERCISED CODE. SIX NULLS ACROSS THREE SESSIONS STILL DO NOT TEST EITHER PATH.**

---

**Reconciliation 2026-10-07 — ONE BLOCK FOR THE DATE, COVERING ALL FOUR SEATS:
`1-premarket-research` 08:24 ET, `2-market-open-execution` 09:37 ET, `3-midday-management` 12:41 ET and
`4-market-close-journal` 16:17 ET. ⚠⚠ ROUTINE 4 RAN — 2026-10-07 IS A COMPLETE SESSION, THE SECOND
CONSECUTIVE ONE, WHICH 10-05 AND 09-28 CANNOT SAY. ⚠ TWO COMPLETE SESSIONS IN A ROW IS NOT A FIX AND MUST
NOT BE READ AS ONE: the failure mode is a seat that never STARTS, and a session that completed is not
evidence about the next one in either direction. THE LEDGER AGREES WITH THE BROKER AT ALL FOUR SEATS;
ZERO SATELLITE POSITIONS ON BOTH SIDES; NO §5 RULE HAS A SUBJECT; NO MARK WRITTEN AND NONE DUE; ZERO
ORDERS AT ANY SEAT.**

Selftest passed all five checks; `trading_enabled: true`, LIVE paper; pre-flight broker equity
**$100,643.92** at 08:24. `clock` at **08:24:50** reads **`is_open: false`** with `next_open`
**2026-10-07T09:30** — the **PRE-MARKET** shape, read off the DATE (it points at **TODAY**), not off
the boolean. ⚠ **FALSE has three meanings; TRUE has one.** ⚠ **Corroborated from the data plane
rather than inferred: `bars --days 4 --adjustment all` returns a complete **2026-10-06** bar
(c 716.29) and **NO bar dated 2026-10-07**.** **Not a holiday.**

**RECONCILIATION, SATELLITE-TO-SATELLITE.** `alpaca.py positions` returns **one row, core VOO**,
99.046311231 shares at avg_entry **706.74** (a **RAW** print), cost_basis **$69,999.99** — unchanged
since the 09-03 fill — against **zero satellite blocks in this file. THEY AGREE.** ⚠ **Core VOO was
removed from the working list BEFORE any §5 rule was read**, per §5's core exemption; **a run that
compares the raw ledger to the raw broker reads a correct ledger as broken.** Sleeves at 08:24:
equity **$100,643.92**, core **$70,643.919783 = 70.19%**, satellite **0.0%** (count 0), cash
**29.81%**, `core_in_band: true`, `rebalance_needed: false`, `rebalance_delta` **−$193.18** (a
distance readout, not an instruction). ⚠ **NO DISCREPANCY WAS FOUND, SO NONE IS FLAGGED — and an
AGREEING ledger and an EMPTY ledger are the same artifact. That is not a clean bill of health on the
reconciliation logic; it is the absence of a test.** **TWENTY-SIXTH session with nothing to
reconcile.**

⚠ **CORE VOO IS AGAIN NOT STAMPED WITH A `highest_close` — SEVENTY-SIXTH CONSECUTIVE RUN.**
⚠⚠ **GRADED, NOT COUNTED, AND THIS IS THE *MIDDLE* GRADE: this seat holds **NO WRITE PATH** into the
field (routine 1 writes `sell_rule_status`, not the stamp — the close run and routine 3's Step 2
backfill own that), but it **DID** pull `bars --symbol VOO --days 4 --adjustment all` for the tape
context and that pull returned **716.29**, a real, completed, same-basis maximum on the only row the
broker returns. THE NUMBER WAS IN HAND AND WAS NOT WRITTEN.** ⚠ **It is a step weaker than 10-06
16:17, which held both the number and the path, and a step stronger than a seat that made no `bars`
call at all — those two look identical in a run summary and only the second is evidence of
anything.** ⚠ **The reason is unchanged and is not a judgment call: a mark on VOO would **fabricate a
§5.4 trailing stop on the one position §5 exempts**, which §7 forbids outright.**

**⚠ 2026-10-07's FOUR PER-SEAT SECTIONS WERE COLLAPSED TO THIS DIGEST BY THE 2026-10-08 16:16 CLOSE
SEAT (which owns this file's `highest_close` write path). Nothing live was discarded.** The four
sections recorded the SAME NULL four times — zero satellite positions, §5.1–§5.4 all ABSENT rather
than passing, zero `quote`/`perplexity`/`move`/`bars`-backfill calls, zero orders, an agreeing
one-row ledger, core in band at every seat — and the durable findings are carried in `state.md`.
⚠ **The bulk of what was removed was the four `THE DIVIDEND TEST, SEAT N OF 4` paragraphs
(readings 26–29 of `cash` at $30,000.00). THAT TEST IS NOW RESOLVED AND CLOSED — branch (a), the
platform does not model dividends, settled at the 2026-10-08 08:25 seat on `balance_asof` having
advanced to 2026-10-07 with `cash` still exactly $30,000.00. The readings they tracked are spent and
the counter is retired.**

**What survives from 2026-10-07, in one line each:**
- **ALL FOUR SEATS RAN AND COMMITTED** (08:24, 09:37, 12:41, 16:17) — the second consecutive complete
  session. ⚠ **Not a fix; the failure mode is a seat that never STARTS.**
- **STEP 2, BOTH SIDES OF THE PAIR, NULL:** the 12:41 midday seat owns the staleness DETECTOR and the
  16:17 close seat owns the STAMP, and each found **no `highest_close` field and no `(as of …)` date
  to compare** — **ABSENT, NOT STALE.** ⚠ **The backfill path stayed untested code.**
- **CORE VOO NOT STAMPED — runs 76 through 79.** The 16:17 seat is the record's strongest instance:
  it held **714.66** (a completed official same-basis close from its own `bars` pull) **AND** the
  write path, and wrote nothing. ⚠ **A mark would have armed §5.4 on the position §5 exempts.**
- **OFFICIAL CLOSE 2026-10-07** (`--adjustment all`): o 713.02 h 715.00 l 711.22 **c 714.66**,
  n 1,323 v 23,415 **as read at 16:17** → equity **$100,784.4368**, core **70.2335%**, cash
  **29.7665%**, day **−$161.4455 = −0.1599%**, since inception **+0.7844%**. VOO **−0.2276%**, book
  excess **+0.0676pp** — on the cash float, not on skill.
- **LIVE 16:17 MARK (a different series):** equity $100,763.64, core 70.23%, `rebalance_delta`
  −$229.09, `last_equity` $100,936.9681 → −0.1717%. ⚠ **Two correct day-returns for one date.**
- **THAT BAR'S n/v IS BELOW EVERY RECENT FLOOR AND THE BAR IS COMPLETE** — the demonstrated false
  positive that **RETIRED the n/v completeness floor test.** ⚠ **The clock is the only working
  market-state discriminator.**
- **THE `latestTrade`-MATCHING CORROBORANT ALSO FAILED THAT SESSION, BENIGNLY:** 714.53 at 16:00:52
  against the daily bar's c 714.66. ⚠ **A corroborant that disagrees with a correct close is worse
  than none.**
- **SEVEN THESES, ALL REJECTED** (`T-2026-10-07-01` … `-07`); **four volunteered absences** from the
  funnel; **PAC-3 MSE** is the instance where the named recipient was a buyable sub-prime and the
  defence-disclosure pattern held anyway.
- **NO ROLLOVER, BREAKER INACTIVE, STREAK 0 AND UNABLE TO MOVE, NO UNRESOLVED ORDERS.**

**Reconciliation 2026-10-06 — ONE DIGEST FOR THE DATE, ALL FOUR SEATS** (`1-premarket` 08:22,
`2-market-open` 09:36, `3-midday` 12:42, `4-close` 16:17 ET).
*(⚠ **COLLAPSED FROM FOUR PER-SEAT SECTIONS (~275 LINES) BY THE 2026-10-12 12:42 MIDDAY SEAT, UNDER THIS
FILE'S OWN STANDING INSTRUCTION — 10-07 and 10-08 were already digests and 10-06 was the last date still
carrying its raw per-seat narrative.** ⚠ **IT WAS COLLAPSED BY THE SEAT THAT HAD JUST ADDED ~3.2KB TO
THIS FILE, so the reduction is an OFFSET THAT WAS OWED, not a virtue. Nothing live was discarded; what
each seat UNIQUELY established is below, and the rest was four tellings of one null.)*

**THE SESSION WAS COMPLETE — ROUTINE 4 RAN, which it had not on 10-05 or 09-28.** At all four seats
`positions` returned **one row, core VOO**, 99.046311231 at avg_entry **706.74** (RAW), cost_basis
**$69,999.99**, against **zero satellite blocks here. THEY AGREED.** **No §5 rule had a subject, no mark
was written and none was due, ZERO orders at any seat.** Core struck from the working list before any rule
was read, per §5's exemption. **25th session with nothing to reconcile — NOT advanced for the 2nd, 3rd or
4th seat of one session (catch 15); session counters 24/21 likewise held, because 10-06 was the day those
runs stood inside.** Band: core 70.25% → **70.31%** intraday, in band, **65th consecutive run**.

**What 10-06 uniquely established, one line each:**

- ⚠⚠ **THE 10-05 CLOSE RUN (ROUTINE 4) PRODUCED NO COMMIT — the SECOND lost close run on record (09-28
  was the first), found by this date's pre-market seat from `git log`.** The 10-05 journal entry is gone
  and unrecoverable; **no alert fired and none could have — a run that dies before `commit.py` leaves no
  trace by construction.** ⚠ **It cost nothing in this file ONLY because the sleeve was empty: with one
  position open, the missed `highest_close` stamp would have forced routine 3 to backfill across it.
  LUCK, NOT DESIGN.** *(Open item (11) with the human.)*
- ⚠⚠ **OPEN ITEM (12), A LATENT DEFECT IN ROUTINE 2's STEP 6 AND IT LIVES IN THIS FILE'S FIELDS:** Step 6
  sources `voo_close_at_entry` from `bars --days 1 --adjustment all`, and at 09:36 **that call returns a
  PARTIAL bar dated TODAY** — `c` 715.32, **`n` 156 / `v` 2,029** against the completed 10-05 session's
  **1,802 / 60,541**. **Six minutes of a session wearing a complete bar's shape.** ⚠ **Followed literally
  on the first morning a fill occurs, it writes a six-minute partial's `c` into the §1 baseline the
  position is measured against for its whole holding window.** **Sound substitutes: the PRIOR completed
  session's close (`prevDailyBar`, or the dated-yesterday row of `bars --days 2`), named on its basis.**
  ⚠ **STILL NOT FIXED, and it cost nothing again only because nothing has opened.**
- **THE PARTIAL BAR WAS OBSERVED END TO END INSIDE ONE SESSION — the clean completion half of that
  finding:** the SAME call read **n 156 / v 2,029** at 09:36 and **n 3,734 / v 86,983** at 16:17.
- ⚠⚠ **CATCHES (17)+(18): A RANGE OVER A LIVE MOVING MARK GOES STALE BY CONSTRUCTION, SO THE STATISTIC
  ITSELF IS THE DEFECT.** The band range was repaired 69.59–70.22% → 69.59–70.25% at 08:22 and was false
  again by 12:42 (70.31%) — **catch (17) recurring inside the same session that fixed it, within four
  hours.** ⚠ **THE LESSON IS NOT "CHECK HARDER".** ⚠ **The band TEST, which is what §2 actually requires,
  never depended on the range.**
- ⚠⚠ **THE `highest_close` REFUSAL GRADED ACROSS THREE INSTANCES IN ONE DAY, WHICH IS WHERE THE GRADING
  RULE COMES FROM:** 12:42 made **zero** `bars` calls and never held the number (**weakest, despite
  owning the write path**); 08:22 pulled a 7-day window but **had no write path**; **16:17 held BOTH the
  number — today's completed official close 716.29, correct basis — AND the path, and declined.**
  ⚠ **Declining to write a number you are holding, from the seat whose job is to write it, is the only
  form of this refusal that is evidence of anything.** **Writing it would ARM §5.4 ON THE ONE POSITION §5
  EXEMPTS — a trailing stop that could eventually sell core, which §7 forbids outright.**
- ⚠⚠ **THREE PRICE SERIES EXIST AND NONE MAY BE CONCATENATED, and 10-06 destroyed any notion of an
  offset on two of them.** PRE-MARKET: `current_price` 715.25 at 08:23 vs the official 10-05 close 712.41
  = **+$2.84**, against the only prior pre-market sample (10-05) of **−$0.22** — **opposite sign, ~13×
  the magnitude.** POST-BELL GAP, three samples: **+$0.470 · −$0.0254 · +$0.1207 — two signs, an order of
  magnitude apart. NO OFFSET EXISTS ON EITHER SERIES.** ⚠ **NEVER difference a broker mark against an
  official close.**
- ⚠ **FOUR NUMBERS FROM ONE MINUTE, NONE DIFFERENCEABLE:** `positions.market_value` implied a mark of
  **717.1614** while `account.long_market_value`, read seconds later, implied **717.1400** (~2.1¢ lower
  from a different endpoint); `sleeves` and `account` agreed to the cent on equity while `selftest.py`
  had read **$101,041.96** a minute earlier. ⚠⚠ **TWO CALLS AGREEING IS NOT A CALIBRATION.** The band
  decision was robust on both bases — **one decision, which is the only reason the spread changed
  nothing.**
- ⚠ **`last_equity` IS FULLY ATTRIBUTED AND IS NOT YESTERDAY'S EQUITY:** 99.046311231 × `lastday_price`
  712.32 + 30,000 = $100,552.66841607 against a reported $100,552.66841606592, while the official 10-05
  close was 712.41. **NEVER `equity − last_equity` as a day's P&L. DO NOT RE-OPEN WHY.**
- **STEP 1's "quote every open satellite ticker" RESOLVED TO AN EMPTY SYMBOL LIST, so the call was NOT
  MADE rather than made on VOO** — ⚠ **a decorative quote on the exempt position would convert an honest
  absence into a fake exercise.** *(Applied again unchanged at the 10-12 midday seat.)*
- **THE DIVIDEND TEST, now CLOSED and recorded only as its mechanism:** `cash` read exactly $30,000.00 at
  the 22nd–25th consecutive reading across this date, from two independent calls each time, on the last
  trading seat before the 10-07 deadline the carry-forward named. ⚠ **The seat-countdown wording
  ("six became five") is kept for one reason: a SEAT WAS CONSUMED, not a day passed — and that counter is
  RETIRED, not merely satisfied.**
- **`orders --status all` returned ONE ROW FOR THE WHOLE ACCOUNT HISTORY** (the 09-03 core fill, terminal
  since 2026-09-03T13:36:21Z). ⚠ **§7's limbo-order warning therefore had NO OPERAND rather than a clean
  bill of health.** *(Still one row at the 10-12 midday seat.)*
- **THE 08:22, 12:42 AND 16:17 REFUSALS TO TRADE WERE ALL GRADED WORTH NOTHING AND SAID SO:** routines 1,
  3 and 4 cannot open a position, so the restraint was **structurally unavailable to violate** — even
  with every gate open (breaker INACTIVE, 0 of 3 weekly, sleeve 0.0%, ~29.7% idle cash, §6 cap ~$5,050).
  ⚠ **The only seat where not-buying is evidence is routine 2 at 09:35.** ⚠ **New positions go through
  pre-market research and the 09:35 run, ALWAYS; the idle cash, the unused cap and the inactive breaker
  are not an opportunity a midday seat may act on.**

**⚠ THE 2026-10-05 THREE-SEAT BLOCK (~105 LINES) HAS BEEN COLLAPSED BY THIS RUN, UNDER THE FILE'S OWN
STANDING INSTRUCTION — the same treatment this seat gave the 10-01/10-02 blocks.** All three seats
recorded the same null: zero satellite blocks against zero satellite broker rows, agreeing; no §5 rule
evaluated; no high-water mark stamped; no backfill due; no order placed. **Nothing live was discarded.**
The load-bearing facts those three blocks carried, kept because they are not reproducible from the
tape:

- ⚠⚠ **THE 09:36 OPEN SEAT IS THE FIRST LOAD-BEARING REFUSAL IN THIS FILE'S HISTORY.** `clock`
  **`is_open: true`** at 09:36:48 — the one state the boolean alone settles. **Routine 2 is the ONLY
  seat that may open**, `plan_today.md` was **FRESH** (`plan_date: 2026-10-05`) and carried **NO BUY
  INTENT**, and every gate was open (§6's 5% cap $5,007.87, no operand). **NOTHING STOPPED A BUY THAT
  MORNING EXCEPT THE ABSENCE OF AN INTENT** — which is exactly what the 08:00/09:35 handoff exists to
  enforce. ⚠ **The 12:41 midday seat faced the IDENTICAL gates with a larger cap ($5,024.34) and its
  restraint is worth NOTHING, because routine 3 is exits-only. Two seats, one session, one set of
  conditions, and only one of the two refusals is evidence of anything.**
- ⚠⚠ **THE 12:41 MIDDAY SEAT RAN STEP 2'S STALENESS DETECTOR WITH NO INPUT.** The detector's entire
  input is the `(as of …)` date, which is **ABSENT**. ⚠ **So the check did not pass; IT DID NOT RUN,
  and "high-water marks verified" would have been FALSE — from the very seat that is supposed to catch
  the close seat's silence.** **The backfill path remains UNEXERCISED CODE; both seats arm on the
  first satellite fill.**
- ⚠⚠ **CATCH (15), CAUGHT AND CORRECTED IN FILE: the 09:36 seat wrote "twenty-fifth session" and
  corrected it to twenty-fourth — A SECOND SEAT IN ONE DAY ADDS NO SESSION.** It is catch (11)
  verbatim, committed one session after catch (14) did the same for a weekend, **by a run that had
  just read (14) three screens above. THIRD CONSECUTIVE PROOF THAT NAMING A FAILURE DOES NOT RETIRE
  IT.**
- ⚠⚠ **CATCH (16): "TWO SESSIONS LEFT" / "THREE SEATS REMAIN" ON THE DIVIDEND TEST STOPPED AT THE NEXT
  MORNING INSTEAD OF AT THE 10-07 DEADLINE THE SAME SENTENCE NAMED** — nine seats stood between the
  claim and it. ⚠ **The first counting catch here whose UNIT was right and whose BOUND was wrong, and
  it failed toward URGENCY rather than comfort.**
- **A THIRD PRICE SERIES WAS OPENED AT 09:36: an INTRADAY LIVE MARK, `current_price` 708.33.** It is
  neither the post-bell gap series nor the pre-market one.
- **A COMPLETED BAR'S `n`/`v` DRIFT SOMETIMES AND NOT ALWAYS — the counter-instance that completes the
  rule.** The 10-02 bar read **n 2,524 / v 134,995** before and after a full weekend, identical, where
  10-01's had drifted 1633/51892 → 1634/51893 within a day. ⚠ **A field that sometimes moves on a
  complete bar is unusable as evidence in EITHER direction. The CLOSE is the stable field; the CLOCK is
  the discriminator.**
- **A Monday pre-market seat reads the same closing tape its predecessor read**, and **a correct
  `plan_today.md` arrives three calendar days old on a Monday** — compare `plan_date` to the last
  TRADING day, not to the calendar.

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-20, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` 08:03 · `2-market-open` 09:37 · `3-midday` 12:41 · `4-market-close` 16:16. ⚠ **COLLAPSED BY THE CLOSE SEAT, THE FIRST SEAT ENTITLED TO TOUCH WHAT THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. ⚠ **RE-EVALUATED AT THIS SEAT, NOT LEFT: a table untouched and a table re-evaluated to the same answer are indistinguishable to the next reader.** ⚠ **MEASURED COLLAPSE, COUNTED AFTER THE FACT AND REPORTED AS IT CAME OUT: 171 lines → 98, a REAL SAVING OF 73 LINES. ⚠ THE FIRST DRAFT OF THIS SENTENCE CLAIMED "171 → 48", WRITTEN FROM INTENT BEFORE THE COUNT; THAT FIGURE WAS FALSE AND IS REPLACED HERE RATHER THAN LEFT BESIDE ITS CORRECTION. It is the same defect three earlier seats recorded (`119 → 58`, `73 → 34`, `15 → 20`) arriving a FOURTH time, in the one line that reports on itself — which is now the strongest available evidence that the lesson does not survive contact with a seat writing its own collapse figure.** **WHAT WAS REMOVED IS NAMED:** the four per-seat narrations of the same null, the four re-derivations of the same week anchor and the four restatements of the ledger reconciliation are folded to one each. **WHAT WAS KEPT:** the three distinct findings in full, plus a fourth this seat measured.)

**LEDGER RECONCILED AT ALL FOUR SEATS, BEFORE ANY RULE WAS READ, THREE SIDES AGREEING EACH TIME.**
`positions` returns **one row, core VOO**, qty **99.046311231** (unchanged since the 2026-09-03 fill),
avg_entry **706.74**, cost_basis **$69,999.989999**; **ZERO satellite blocks in this file**; `sleeves`
reports `satellite.count: 0`. **No discrepancy at any seat.** ⚠ **Core VOO was struck from the working
list BEFORE any §5 rule was read, per §5's core exemption — it is not a satellite operand, is never
sold on news, and is never stamped with a `highest_close`.**

| §5 rule | Status | Distance to the rule |
|---|---|---|
| **5.1 thesis invalidation** | **ABSENT — no operand** | No thesis exists to invalidate. **Zero Perplexity invalidation calls at any seat** — a news check with no position to invalidate is theatre. |
| **5.2 time stop** | **ABSENT — no operand** | No `deadline` field on any row, because no row exists. |
| **5.3 hard stop (−7% from entry)** | **ABSENT — no operand** | No `entry_price` on any satellite row. **Not "no position is near the stop" — there is no position.** |
| **5.4 trailing stop (−10% from `highest_close`)** | **ABSENT — no operand** | `highest_close` **does not exist as a field.** ⚠ **Nothing was stale to detect and NO BACKFILL WAS POSSIBLE — there is no `(as of …)` date anywhere for a later seat to find.** |

⚠⚠ **FOURTEEN CONSECUTIVE SEATS WITH §5 ABSENT RATHER THAN PASSING. THE BACKFILL MACHINERY HAS STILL
NEVER BEEN EXERCISED ONCE IN 36 SESSIONS.** The silent-trailing-stop failure mode cannot occur on an
empty ledger, which is **NOT evidence that the step works.** First real test arrives with the first
satellite fill.

⚠⚠ **STEP 2 AT THE 16:16 CLOSE SEAT — THE ONE JOB THIS ROUTINE OWNS ALONE — HAD NO SUBJECT.** Zero
open satellite positions, so there was **no `highest_close` to raise and no `(as of …)` date to
advance.** `highest_close` is **ABSENT — the third state, carrying no date at all.** ⚠ **"High-water
marks updated" would be FALSE today and so would "verified"; the honest form is that the job had no
operand. The next run needs NO BACKFILL, and the reason is that there is no field, not that the field
is fresh.** **CORE VOO WAS NOT STAMPED — a 92nd consecutive run declining it, re-decided on its merits
at the one seat that owns the stamp write path and held a real, complete, official close (706.33):
writing it would ARM A §5.4 TRAILING STOP ON THE POSITION §5 EXEMPTS, a stop that could eventually
sell core, which §7 forbids outright.**

**CLOCK, READ OFF THE DATES AND NOT THE BOOLEAN — A FULL REGULAR SESSION, DEMONSTRABLY OVER.**
08:03:00 `is_open: false` with **both** `next_open` 2026-10-20T09:30 and `next_close` 2026-10-20T16:00
carrying **today's** date (pre-market full-session signature) → 09:37:38 and 12:41:48 `is_open: true`
with `next_close` **today 16:00** (mid-session) → **16:16:23 `is_open: false` with BOTH dates rolled to
2026-10-21** (post-bell). **Not a holiday, not an early close. The closed-market skip path was taken at
no seat.** ⚠ **The staleness gate at 09:37 was a REAL test and PASSED** (`plan_date: 2026-10-20` =
today), so the stale branch and its alert were **correctly not taken**.

**ZERO ORDERS AT ANY SEAT, AND NONE WERE DUE.** The 08:03 plan carried **zero BUY, zero SELL and zero
REBALANCE intents**, so 09:37's Steps 4–6 had no operand; 12:41 took the Step 1 early-exit path
deliberately (a midday entry would route around the thesis-sleeps-overnight path); Step 3's core
bootstrap was skipped **correctly** on `core_established: true`. ⚠ **New positions were PERMITTED on
every gate — breaker inactive, 0 of 3 this week, sleeve entirely undeployed. The absence of a buy is a
RESEARCH result, not a permission result.** `orders --status all` still returns **ONE row for the whole
account history** (the 09-03 core fill, `filled`, terminal), so **§7's order-limbo warning has no
operand — which is not a clean bill.**

**§2 IN BAND AT EVERY SEAT, NO REBALANCE DUE TOMORROW.** Close-basis (VOO `c` **706.33**): equity
**$99,959.381012**, core **$69,959.381012 = 69.9878%**, cash **$30,000.00 exactly** (~40th consecutive
unchanged reading), satellite **$0.00 / 0.0% / count 0**; **4.99pp above the lower edge, 5.01pp below
the upper**. Live 16:16 broker mark read **70.02% / $100,082.20** on `current_price` 707.57 — a
**separate series, quoted beside and never differenced against** the close basis. ⚠ **`rebalance_delta`
moved $118.56 (08:03) → $82.01 (09:37) → **−$17.83** (12:41, first negative on record) → **$12.19**
(close basis) — four readings of a DISTANCE, each RE-COMPUTED and none inherited; every earlier one is
dead the moment the mark moves.** **§6's 5% satellite cap is $4,997.97 on the close basis / $5,004.11
live and must be RE-COMPUTED wherever used.**

**WEEK ROLLOVER RE-DERIVED AT EVERY SEAT, NEVER READ OFF THE FIELD.** `America/New_York` **2026-10-20,
Tuesday, ISO week 43, weekday 2, Monday anchor 2026-10-19** — **MATCHES** `week_of`, so
`new_positions_this_week` was **NOT re-reset** and stands at **0 of 3** because nothing was opened.
Anchor holds through **Friday 2026-10-23**. **Breaker INACTIVE**, `consecutive_closed_losses: 0`,
`halt_triggered_at: none` — so `control.md`'s `HALT_CLEARED_AT: none` **has no operand and is correct.**
The streak **cannot move on a day nothing closed.** `control.md` notes **EMPTY**; **zero open alerts**
— ⚠ **which is not evidence every seat ran: a run dying before `commit.py` leaves no trace.**

⚠⚠ **FINDING 1 (08:03, UNRESOLVED) — THE PRICED-IN FILTER'S SIXTH DEFECT SHAPE, AND IT IS IN THE OPEN
SEAT'S MACHINERY.** `move --symbol MMM --sessions 5` returned **+0.69%, `priced_in: false`, "passes"**
while **every close in the window PREDATED the event** (the 3M 8-K landed after the 10-19 bell). ⚠ **A
09:35 `move` re-check CANNOT catch it — `move` reads closes and today's close does not exist at 09:35,
so the re-check returns the same pass bit for bit.** It cost nothing because `T-2026-10-20-01` died at
part 2 above it. **It becomes a wrong trade the first time a post-bell event produces a writeable part
2, and it fails TOWARD taking the trade.** Open human items **(1)(2)(7)**; only a human may change §4
or `alpaca.py move`.

⚠ **FINDING 2 (09:37, STANDS UNFALSIFIED — NOT CONFIRMED).** The seat that was supposed to test
Finding 1 made **zero `move` calls**, because there was nothing to revalidate. **A clean run did not
test it. It gets tested the first time a BUY intent survives to 09:35.**

⚠⚠ **FINDING 3 (12:41 PREDICTED → 16:16 MEASURED, AND THIS IS THE CLOSE SEAT'S ONE REAL ADDITION).**
The midday seat's `bars --days 4` call returned a **2026-10-20 bar at `c: 707.32`** and correctly
refused to treat it as a close. **Today's OFFICIAL close is 706.33.** ⚠ **So a midday backfill from
that running bar would have stamped `highest_close` $0.99 ABOVE the true close — a LOOSER §5.4 stop, on
the exact field §5.4 measures from. The trap is no longer predicted; it is MEASURED, with a signed
magnitude, for the first time.** Same shape and same direction at this seat from a different field:
`current_price` **707.57** post-bell is **$1.24 above** the official close, so stamping the `positions`
mark instead of the `bars` close would err the same loose way. ⚠ **RULE CONFIRMED BY MEASUREMENT:
`highest_close` may only ever be written from `bars --adjustment all`, by the close seat, after the
bell.**

⚠ **FINDING 4 — STALE `lastday_price` INTO A THIRTEENTH SEAT, RE-MEASURED NOT ASSUMED:** `positions`
reports **704.60** against the official 10-19 close **704.47** (`bars --days 4 --adjustment all`),
**+$0.13** — same sign and magnitude as 08:03, 09:37 and 12:41, but it flipped sign from 10-19's
−$0.135, so **it is NOT a fixed offset that could be corrected for.** ⚠⚠ **NEVER difference
`equity − last_equity`, `change_today` (0.00422) or `unrealized_intraday_pl` ($294.167545) into a P&L
figure.** The day's P&L in the journal is built from **official closes only**: 99.046311231 sh ×
(706.33 − 704.47) = **+$184.23** on a **$99,775.154873** prior-close equity = **+0.1846%**.

---

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-19, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` 08:13 · `2-market-open` 09:36 · `3-midday` 12:41 · `4-market-close` 16:16. ⚠ **COLLAPSED BY THE CLOSE SEAT, THE FIRST SEAT ENTITLED TO TOUCH A BLOCK THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. ⚠ **RE-DATED AND RE-EVALUATED, NOT LEFT: a table untouched and a table re-evaluated to the same answer are indistinguishable to the next reader.**)

**THE LEDGER AGREED WITH THE BROKER AT ALL FOUR SEATS, AND IT WAS EACH RUN'S FIRST JOB — BEFORE ANY
RESEARCH AND BEFORE ANY SELL RULE WAS READ.** `alpaca.py positions` returns **one row, core VOO**, qty
**99.046311231** (unchanged since the 2026-09-03 fill), avg_entry **706.74**, cost_basis
**$69,999.989999** — against **ZERO satellite blocks in this file** and `sleeves` reporting
`satellite.count: 0`, at 08:13, 09:36, 12:41 and 16:16 alike. **No discrepancy at any seat. Nothing was
researched, and nothing was placed, on top of a ledger in doubt.** ⚠ **Core VOO was struck from the
working list BEFORE any §5 rule was read at every seat, per §5's core exemption — it is not a satellite
operand.** ⚠ **GREP TRAP, do not re-raise: `entry_price` / `highest_close` / `invalidation` hits in this
file are ALL inside `## Template` or inside prose digests.**

| Rule | Status | Distance |
|---|---|---|
| §5.1 thesis invalidation | **ABSENT** | no thesis to invalidate — `open_thesis_ids: none`; **zero Perplexity checks, because §5.1's subject does not exist** |
| §5.2 time stop | **ABSENT** | no `timing_window`, so no deadline exists to pass |
| §5.3 hard stop (−7% from entry) | **ABSENT** | no `entry_price` on any satellite row |
| §5.4 trailing stop (−10% from `highest_close`) | **ABSENT** | ⚠ **`highest_close` does not exist as a field — a TENTH consecutive seat with no operand. The close seat wrote ZERO high-water marks and ZERO were POSSIBLE; there is no stale `(as of …)` date for the midday backfill to detect. The gap that would silently disable §5.4 cannot occur on an empty ledger, which is NOT evidence that the repair step works.** |

⚠ **"ABSENT" IS THE HONEST WORD AND "PASSING" WOULD BE A LIE.** A rule with no operand has not been
satisfied; it has not been evaluated, because there is nothing to evaluate.

**CLOCK, READ OFF THE PAIR OF DATES AND NOT THE BOOLEAN, THROUGH A FULL DAY.** 08:13 `is_open: false`
with **both** dates on **today** (pre-market, full session) → 12:41:17 `is_open: true`, `next_open`
rolled to **10-20** while `next_close` **stayed** 2026-10-19T16:00 (mid-session) → **16:16:56
`is_open: false` with BOTH dates rolled to 2026-10-20** (post-bell). **A full regular session, not a
holiday and not an early close, confirmed at both ends rather than assumed.**

**ZERO ORDERS AT ANY SEAT.** The staleness gate **PASSED** at 09:36 (`plan_date: 2026-10-19` = today),
so the plan was **executable** — the open seat bought and sold nothing because the plan carried **ZERO
BUY / ZERO SELL / ZERO REBALANCE intents, NOT because a gate blocked it.** Every §6 gate was open all
day (breaker INACTIVE, 0 of 3 positions used, $30,000 idle). Nothing closed, so
`consecutive_closed_losses` is **untouched at 0**. `orders --status all` still returns **one row for the
whole account history** — the 09-03 core fill, terminal. ⚠ **§7's order-limbo warning has no operand,
which is not a clean bill.**

**§2 RE-DERIVED AT EVERY SEAT, IN BAND AT EVERY SEAT.** Core **69.96% → 69.96% → 69.98% → 69.93%**
(08:13 / 09:36 / 12:41 / 16:16, the last on **official closes**), cash **$30,000.00 exactly** (~39th
consecutive unchanged reading). `rebalance_delta` **44.28 → 39.52 → 21.99 → 57.95** — a **DISTANCE
READOUT, NOT AN INSTRUCTION**, four readings of the same non-event ($58 on $69,807 = 0.08%), moving only
because VOO's mark moves under a fixed share count. **`rebalance_needed: false`. No rebalance due
2026-10-20.** §6's 5% cap is **$4,988.76** on the close basis and must be **RE-COMPUTED wherever used.**

**THE CLOSE SEAT'S BASIS WORK, AND IT CUTS BOTH WAYS.** VOO official 10-19 close **704.47** on
`bars --adjustment all`; a **`raw` pull returned the IDENTICAL 10-15 / 10-16 / 10-19 rows**, so the
ex-dividend basis trap at the top of this file was **NON-DECISIVE today — which means "no corporate
action since 09-28," NOT "the rule is satisfied."** It has still never been exercised against a real
`highest_close`, because one has never existed. ⚠⚠ **THE STALE `lastday_price` DEFECT PERSISTS INTO A
NINTH SEAT, GAP UNCHANGED AT −$0.135** (701.61 vs the official 10-16 close 701.745). ⚠⚠ **NEVER
difference `equity − last_equity`, `change_today` (0.00453) or `unrealized_intraday_pl`
(+$314.967269) into a P&L figure: today the forbidden figure was +$314.9676, reconciled to the cent
with `unrealized_intraday_pl`, and WRONG BY +$45.07 against the honest +$269.9012 — a 4.53bp error on a
27.12bp move, with BOTH components (+$13.37 stale `lastday_price`, +$31.69 live mark over the official
close) inflating the day.**

---

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-16, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` 08:13 · `2-market-open` 09:37 · `3-midday` 12:42 · `4-market-close` 16:18. ⚠ **COLLAPSED BY THE CLOSE SEAT, THE FIRST SEAT ENTITLED TO TOUCH A BLOCK THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. ⚠ **RE-DATED AND RE-EVALUATED, NOT LEFT: a table untouched and a table re-evaluated to the same answer are indistinguishable to the next reader.** ⚠⚠ **AND SEE THE CORRECTION AT THE FOOT OF THIS BLOCK — TWO CLAIMS THE 12:42 SEAT WROTE INTO THIS FILE ARE FALSE AND ARE REPLACED, NOT LEFT BESIDE THEIR REFUTATION.**)

**§5.1 → 5.2 → 5.3 → 5.4 REACHED IN ORDER AT EVERY SEAT AND FOUND EMPTY.** Core VOO was struck from the
working list **before any rule was read**, per §5's core exemption; with it gone the list is empty.

| Rule | Status | Distance |
|---|---|---|
| **§5.1 thesis invalidation** | **NO OPERAND** — no thesis to invalidate | **undefined** |
| **§5.2 time stop** | **NO OPERAND** — no timing window to expire | **undefined** |
| **§5.3 hard stop (−7% from entry)** | **NO OPERAND** — no entry price | ⚠ **UNDEFINED, NOT LARGE** |
| **§5.4 trailing stop (−10% from `highest_close`)** | **NO OPERAND** — `highest_close` **ABSENT**, not stale | ⚠ **UNDEFINED, NOT LARGE** |

⚠⚠ **"ALL FOUR RULES PASSING" WOULD BE FALSE. A rule reached and found to have no subject has produced
no evidence that it works.** **30 post-fill sessions of nulls are not 30 passes.**

**LEDGER RECONCILED AT EVERY SEAT AS ITS FIRST JOB, THREE SIDES AGREEING EACH TIME:** **zero satellite
blocks in this file** · `positions` **one row, core VOO**, qty **99.046311231** unchanged since the
2026-09-03 fill, avg_entry **706.74**, `cost_basis` **$69,999.989999** · `sleeves` `satellite.count: 0`.
**No discrepancy at any seat. Nothing was researched or managed on top of a ledger in doubt.**

**CLOCK, READ OFF THE DATES AND NOT THE BOOLEAN — ALL FOUR SIGNATURES IN ONE SESSION.** 08:13:02
`is_open: false` with **both** `next_open` and `next_close` dated **2026-10-16** — the **pre-market
full-session** signature, not a holiday and not an early close · 09:37:13 and 12:41:48 `is_open: **true**`,
`next_close` **today 16:00** and `next_open` **Monday 2026-10-19T09:30** — the **mid-session** signature,
and the only §7 clearance to trade that exists, which only the 09:37 seat may act on · **16:18:50
`is_open: false` with BOTH dates rolled to 2026-10-19 — the POST-BELL signature, which is what entitles
this seat to count the session it stands in.**

**THE SEAT-BY-SEAT RECORD, IN ONE LINE EACH, BECAUSE THE NULL WAS IDENTICAL AT ALL FOUR:**
- **08:13 pre-market** — five theses written (`T-2026-10-16-01` … `-05`), **all five REJECTED**; plan
  written with **no BUY, no SELL and no REBALANCE intent.** Zero `bars` calls.
- **09:37 market-open, THE ONLY SEAT THAT CAN OPEN A POSITION, AND IT OPENED NOTHING.** Staleness gate
  **PASSED, NOT FIRED** — `plan_date` 2026-10-16 **read off the field** against the clock's ET date, not
  inferred from the plan being empty (a fresh empty plan and a stale plan produce **identical zero-order
  runs**). ⚠⚠ **ITS REFUSAL IS THE ONLY ONE OF THE FOUR THAT COUNTS, AND IT WAS NOT STRUCTURAL:** every
  §6 gate **open** (breaker INACTIVE · 0 of 3 · satellite 0.0% with **$30,000 idle** · cap ~$5,016 ·
  notes empty), so **the only thing between this account and a trade at 09:37 was the absence of an
  intent.** The five bank prints (TRV·TFC·MTB·RF·CFG) landed **between 08:13 and this seat** and were
  **not** picked up; `T-2026-10-16-02` (JBHT → rail) did not return, and the answer was already written.
- **12:42 midday, EXITS-ONLY — it may not open a position and had nothing to close.** Step 1's own exit
  condition fired. **§5.1's Perplexity check cost zero queries and that is STRUCTURAL** (one query **per
  position**). Its two substantive claims are **corrected at the foot of this block.**
- **16:18 close** — Step 2 **no operand** for a sixth consecutive close seat; journal entry written;
  session count advanced; **nothing written to `trade_log.md` at any seat.**

**STEP 2 — THE HIGH-WATER MARKS, THE ONE JOB THE CLOSE RUN OWNS ALONE — HAD NO OPERAND FOR A SIXTH
CONSECUTIVE CLOSE SEAT, AND THE MIDDAY DETECTOR HAD NONE FOR A FIFTH.** Zero open satellite positions, so
no symbol to pull a bar for, **no `highest_close` to raise and no `(as of …)` date to advance**; the field
is **ABSENT — a third state carrying no date at all.** ⚠ **"HIGH-WATER MARKS UPDATED" WOULD BE FALSE
TODAY, AND SO WOULD "VERIFIED." The honest form is: the job had no subject.** ⚠⚠ **NO STALENESS WAS
DETECTED *OR* RULED OUT at 12:42 — the `(as of …)` date is the detector's entire input and it does not
exist, so the check did not pass, IT DID NOT RUN.** ⚠ **MONDAY NEEDS NO BACKFILL, AND THE REASON IS THAT
THERE IS NO FIELD, NOT THAT THE FIELD IS FRESH.** Both paths arm on the first **satellite** fill; the
09-03 core fill was not one.

**OFFICIAL CLOSE BASIS, THE SESSION THAT JUST ENDED — 2026-10-16** (`bars --days 4 --adjustment all`;
⚠ **a second `--adjustment raw` pull returned the IDENTICAL row for 10-15 and 10-16, so the basis was
NON-DECISIVE — recorded anyway, because the next ex-date restores the trap**): o **710.78** h **710.78**
l **699.53** **c 701.745**, n **1,019** v **26,591**, vw **704.617943** — **down $7.625 / −1.0749%** on
10-15's **709.37**.
⚠⚠ **THE OPEN *WAS* THE HIGH, AND THE SESSION IS THE EXACT MIRROR OF 10-15's:** VOO opened **$1.41 above**
the prior close, never traded higher, and fell to **699.53** before closing at 701.745 — where 10-15
opened **$3.10 below** its prior close, bottomed at 702.965 and **recovered to close +0.2728%.** **Two
consecutive sessions, opposite intrasession shapes, and neither close reveals its path.**
⚠⚠ **CHECKED AGAINST THE WHOLE POST-FILL SERIES RATHER THAN THE LAST FEW DAYS, AND THE TWO ORDERINGS
DISAGREE: −1.0749% IS THE LARGEST SINGLE-SESSION *PERCENTAGE* FALL ON RECORD** (ahead of 10-14's
−1.0684%), **WHILE 10-14 REMAINS THE LARGEST IN *DOLLARS*** (−$7.64 against −$7.625). **Both are stated so
neither can be quoted alone.** *(Raw basis; the ranking is unchanged on `--adjustment all`, since the
uniform pre-ex rescaling does not touch day-over-day ratios inside the post-ex window.)*
⚠ **`n` 1,019 is BELOW 10-13's COMPLETED 1,262 on a session the clock proves complete — a fresh
confirmation that the retired `n`/`v` floor test deserved retirement. THE CLOCK IS THE DISCRIMINATOR.**

**BOOK ON THAT BASIS:** equity **$99,505.253675**, core **$69,505.253675 = 69.8508%**, cash **30.1492%**;
day **−$755.228123 / −0.75327%**; core unrealized **−$494.736324 / −0.7068%** against the 706.74 fill
print; since inception **−0.4947%** (2026-09-01 convention). **Excess +0.32163pp**, ⚠ **which is the
algebraic identity `(w − 1) × VOO_return` at `w` = 0.700779 and measures NOTHING — VOO fell, so the sign
is positive by construction.**

**LIVE BROKER MARK, 16:18 (A DIFFERENT SERIES, NEVER CONCATENATED WITH THE ABOVE):** `sleeves` equity
**$99,444.86**, core **$69,444.855234 = 69.83%**, cash **30.17%**, `core_in_band: true`,
`rebalance_needed: false`, `core_target_value` **$69,611.40**. `positions`: `current_price` **701.1352**,
`lastday_price` **709.43**, `unrealized_pl` **−$555.134765 / −0.793%**.
⚠⚠ **POST-BELL PRICE-GAP SAMPLE: `current_price` 701.1352 against the official close 701.745 = −$0.6098
— THE SECOND-LARGEST IN MAGNITUDE OF THE NINE SAMPLES ON RECORD, NOT THE LARGEST.** See the correction
at the foot of this block; the full nine-sample list lives in `state.md`'s price-gap item.
⚠ **`lastday_price` 709.43 is STILL not the official 10-15 close 709.37 — the FOURTH consecutive seat on
that same +$0.06 stale value — so `change_today` −0.01169 and `unrealized_intraday_pl` −$821.569343 are
BROKER-MIDPOINT figures, NOT official-basis day figures.**
⚠⚠ **THE FORBIDDEN FIGURE ARRIVED PRE-CORROBORATED AGAIN AND THE ATTRIBUTION HOLDS FOR A THIRD SESSION:**
`equity − last_equity` = **−$821.5693**, agreeing **to the cent** with `unrealized_intraday_pl`, and
`last_equity` **recomputes exactly** as 99.046311231 × 709.43 + 30,000 = **$100,266.42457660833**. ⚠ **It
is −0.8194% against the honest −0.7533% — a 6.61bp error on the headline. NEVER USE IT. The wrong figure
comes assembled and corroborated; the right one has to be built from two official closes.**
⚠ **`balance_asof` reads 2026-10-15 after today's bell — the broker's balance date has not rolled.
Reported, not reconciled away; it is the same field that settled the dividend test on 10-08.**

**§2 — NO REBALANCE DUE AT ANY SEAT, AND THE CALL BELONGS TO THE MARKET-OPEN SEAT.** Core ran **70.12%
(08:13) → 70.10% (09:37) → 69.94% (12:42) → 69.85% (16:18 official / 69.83% live)** and **never came near
an edge**; at the close it stands **4.85 points above the lower edge and 5.15 below the upper.**
⚠⚠ **`rebalance_delta` +$166.55 IS A SEVENTH CONSECUTIVE READING AND A FOURTH SIGN FLIP:** +$73.15 →
−$21.89 → −$76.96 → −$119.15 → −$96.57 → +$63.92 → **+$166.55**. **A run reading it as a trigger has now
been told buy, sell, sell more, sell more still, sell, buy, AND BUY MORE — on one position unchanged
since 3 September.** **§2 triggers on the BAND and nothing else.**
⚠ **§6's 5% cap is $4,975.26 on the official close ($4,972.24 on the live mark) and MUST BE RE-COMPUTED
at the seat that uses it. It has no operand only because no plan has ever carried a buy intent.**

**§6 / §7 GATES, ALL OPEN AND ALL RE-READ AT EVERY SEAT:** breaker **INACTIVE**
(`consecutive_closed_losses: 0`, `halt_triggered_at: none`, so the `HALT_CLEARED_AT` comparison was **not
due** and no alert was owed) · week anchor **recomputed from source** (America/New_York → 2026-10-16 Fri,
ISO week 42 weekday 5, Monday anchor **2026-10-12**) and **MATCHED** `week_of`, so
`new_positions_this_week` was **not re-reset** and stands at **0 of 3 because nothing was opened** ·
nothing closed, so `consecutive_closed_losses` is **0 UNTOUCHED rather than reset** — and on an empty
sleeve it **cannot move**, so the increment path and the circuit-breaker alert path both remain
**UNTESTED CODE** · `orders --status all` → **one row, the 09-03 fill, `filled`**, so §7's order-limbo
warning has **no operand rather than a clean bill** · zero open alerts · `control.md` Notes **empty**.

**CORE VOO NOT STAMPED — 107th CONSECUTIVE REFUSAL, AND THE CLOSE SEAT'S GRADE IS THE STRONGEST THE
SERIES ADMITS:** it held a **real, completed, official close on the correct basis (701.745)** from its own
`bars` pull **AND** it owns the Step 2 write path, **and it wrote nothing.** §5 exempts core from all four
rules, and a `highest_close` on VOO would **fabricate a §5.4 trailing stop on the one position the
strategy exempts** — §7 forbids that outright. ⚠ **THE PHANTOM FIGURE WAS NOT DERIVED: no window was
pulled to find the highest close since the fill, because COMPUTING THE MARK IS THE FIRST HALF OF THE ACT
BEING REFUSED.** *(08:13 and 09:37 were the EASY grade — zero `bars` calls, no close in hand to decline.)*

**⚠⚠ CORRECTION — TWO CLAIMS THE 12:42 SEAT WROTE INTO THIS FILE ARE FALSE. THEY ARE REPLACED HERE, NOT
LEFT BESIDE THEIR REFUTATION.**
The 12:42 block said core being underwater put equity **"below the $100,000 bootstrap for the first time
in 34 sessions"** and that **"for 33 sessions the §5 exemption only ever protected a winner … today is
the first time it bound against a real drawdown."** ⚠ **BOTH ARE WRONG, and its stated evidence names the
defect: *"all prior readings gains: 10-15 16:16 · 10-16 08:13 · 09:37."* That is true of the three
readings the carry-forward happens to carry and FALSE OF THE SERIES.**
**ONE `bars --days 45 --adjustment raw` PULL SETTLES IT. THE BOOK HAS CLOSED BELOW $100,000 ON THIRTEEN
PRIOR POST-FILL SESSIONS** — 09-08 $99,744.45 · 09-09 $99,412.15 · 09-10 $99,004.57 · 09-11 $99,582.01 ·
09-14 $99,268.04 · 09-15 $98,964.96 · **09-16 $98,660.39 (−1.3396%, THE DEEPEST)** · 09-17 $99,428.49 ·
09-18 $99,515.65 · 09-28 $99,688.98 · 09-29 $99,557.25 · 09-30 $99,392.34 · 10-01 $99,555.77.
**Today's $99,505.25 / −0.4947% IS THE FOURTEENTH SUCH CLOSE AND ONLY THE SEVENTH DEEPEST.** The core
exemption has therefore bound against a real drawdown on **FOURTEEN** sessions, most severely at
**−1.9137%** on 09-16 against today's **−0.7068%.**
⚠ **NO DECISION CHANGES IN EITHER DIRECTION — core is exempt by §5 whether it is down 0.7% or 1.9%, and
it was struck before any rule was read on every one of those fourteen sessions. WHAT WAS AT STAKE WAS THE
RECORD, WHICH IS THE WHOLE OF WHAT THIS FILE IS FOR.**
⚠⚠ **THE MECHANISM IS CATCH (13)/(23) IN ITS PUREST FORM AND IT GENERALISES PAST THIS INSTANCE: A
SUPERLATIVE IS A CLAIM ABOUT A WHOLE SERIES, AND THE CARRY-FORWARD IS NOT THE SERIES — IT IS A
THREE-READING WINDOW THAT SCROLLS. Every seat that reads a "first" off it will reach the same wrong
answer, and the refutation cost ONE API CALL.**
**AND THE SAME SHAPE, CAUGHT A SECOND TIME IN THE SAME RUN, ON THE PRICE-GAP SERIES:** read against
`state.md`'s four-sample list (largest magnitude $0.57), today's **−$0.6098** would be "the largest on
record." ⚠⚠ **IT IS NOT — 10-14's −$0.67 IS LARGER AND IS RECORDED IN BOTH THIS FILE AND `journal.md`.**
Counted from source the samples are **NINE**, and ⚠⚠ **TWO CONSECUTIVE CLOSE SEATS EACH NUMBERED THEIR
OWN SAMPLE "THE FIFTH"** — 10-14 off a list that had dropped 10-09's and 10-12's, 10-15 off a list that
had additionally dropped 10-14's own, taken the previous day. ⚠ **THE CAUSE IS NOT CARELESSNESS:
`state.md`'s COLLAPSE of that item folded the per-sample narrations away AND TOOK TWO DATA POINTS WITH
THEM, and each later seat computed an ordinal against the truncation. THE COLLAPSE DISCIPLINE ITEM (9)
ASKS FOR PRODUCED CATCH (5)'s TRUNCATED SERIES.** ⚠⚠ **THE RULE THAT FOLLOWS IS NEW AND CHEAP:
COLLAPSING A NARRATIVE AND COLLAPSING A SERIES ARE DIFFERENT ACTS — FOLD THE PROSE, KEEP EVERY DATA
POINT, AND NEVER STATE AN ORDINAL THAT WAS NOT COUNTED FROM THE LIST IN THE SAME BREATH.**

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-15, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` 08:19 · `2-market-open` 09:37 · `3-midday` 12:42 · `4-market-close` 16:16. ⚠ **COLLAPSED BY THE CLOSE SEAT, WHICH IS THE FIRST SEAT ENTITLED TO TOUCH A BLOCK THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. ⚠ **RE-DATED AND RE-EVALUATED, NOT LEFT: a table untouched and a table re-evaluated to the same answer are indistinguishable to the next reader.**)

**§5.1–5.4 REACHED IN ORDER AT ALL FOUR SEATS AND FOUND EMPTY — RE-EVALUATED EACH TIME, NEVER
INHERITED.** Core VOO is struck from the working list **before any rule is read**, per §5's exemption;
with it gone the list is empty. **Zero `sell`, zero `quote`, zero `move`, zero Perplexity-on-a-holding
at any seat** — §5.1 costs one news query **per position** and there were none, so that absence is
**structural, not a skipped step**. Step 1's `quote --symbols <every open satellite ticker>` had an
**EMPTY SYMBOL LIST** — an *absent* call, not a skipped one.
⚠⚠ **DISTANCE IS UNDEFINED, NOT LARGE. "Nothing close to triggering" would be a fabrication, because
nothing can be close to a threshold it has no operand for.**

| Rule | Status | Distance | Why not "passing" |
|---|---|---|---|
| **§5.1** invalidation | **NO OPERAND** | n/a | No thesis held; no `invalidation` string to read. `open_thesis_ids: none`. |
| **§5.2** time stop | **NO OPERAND** | n/a | No `timing_window` or deadline field exists in this file. |
| **§5.3** hard stop −7% | **UNDEFINED** | **undefined** | No satellite `entry_price`. The 706.74 core fill is §5-exempt, not an operand. |
| **§5.4** trailing −10% | **NOT ARMED** | **undefined** | No `highest_close`. Arms on the first **satellite** fill; 09-03's core fill was not one. |

**LEDGER RECONCILED AS EACH RUN'S FIRST JOB, FOUR TIMES, THREE SIDES AGREEING EVERY TIME** (§7 forbids
acting on top of a ledger known wrong): this file **zero satellite blocks** · `positions` **one row,
VOO** 99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999** — **unchanged since 2026-09-03, now
32 sessions** · `sleeves` `satellite.count: 0`. **No discrepancy at any seat.**
**Zero non-terminal orders all day: `orders --status open` → `[]`, `--status all` → STILL ONE ROW for
the entire account history (the 09-03 core fill, `filled`), so §7's order-limbo requirement has NO
OPERAND rather than a clean bill.**

**CLOCK THROUGH A FULL DAY, READ OFF THE *DATES* AND NOT THE BOOLEAN.** 08:19:46 `is_open: false` with
**both** `next_open` and `next_close` dated **2026-10-15** — the pre-market full-session signature,
**not a holiday and not an early close**. 09:37:00 and 12:41:35 `is_open: **true**` with `next_open`
**rolled to 2026-10-16T09:30** while `next_close` **stood at 2026-10-15T16:00** — the mid-session
signature. **16:16:34 `is_open: false` with BOTH dates rolled to 2026-10-16 — the POST-BELL signature,
and the close seat's own confirmation that the session it is journaling actually happened.**
⚠ **FALSE has three meanings and TRUE has one; only the pair of dates separates them.**

**STALENESS GATE — EXERCISED AND *PASSED*, WHICH IS THE OPPOSITE OUTCOME FROM *FIRED*.** `plan_date`
**2026-10-15** read off the field against the clock's ET date **2026-10-15** → **FRESH**. ⚠ **Freshness
was NOT inferred from the plan being empty: a fresh empty plan and a stale plan produce IDENTICAL
zero-order runs, and only the field distinguishes them.** The gate's failing branch stays unexercised.

**NUMBERS WITH THEIR CALL AND BASIS — ⚠ FOUR LIVE MARKS AND ONE OFFICIAL CLOSE, AND NO TWO OF THEM WERE
EVER DIFFERENCED AGAINST EACH OTHER.**
**Live broker marks (`sleeves`):** 08:19 equity **$99,853.59**, core **69.96%** · 09:37 **$99,768.22**,
core **$69,764.606441 / 69.93%**, `rebalance_delta` **+$73.15** · 12:41 **$100,086.16**, core
**$70,082.198438 / 70.02%**, `rebalance_delta` **−$21.89** · **16:16 equity $100,256.52, core
$70,256.519945 / 70.08%, cash $30,000.00 exactly / 29.92%, satellite 0.0% `count 0`, `core_in_band:
true`, `rebalance_needed: false`, `core_target_value` $70,179.56, `rebalance_delta` −$76.96.**
`positions` 16:16: `current_price` **709.33**, `market_value` **$70,256.519945**, `unrealized_pl`
**+$256.529946 / +0.366%** against the 706.74 fill.
**OFFICIAL CLOSE BASIS, THE SESSION THAT JUST ENDED — 2026-10-15** (`bars --days 4 --adjustment all`,
pulled by this seat; **`raw` returned the identical row, so the basis was non-decisive and is stated
anyway**): o **704.34** h **710.32** l **702.965** **c 709.37**, n **1,796** v **41,161**, vw
**706.291079** — **up $1.93 / +0.2728%** on 10-14's **707.44**.
⚠⚠ **THE BROKER/OFFICIAL GAP TOOK A FIFTH POST-BELL SAMPLE: `current_price` 709.33 against the
official 709.37 = **−$0.04**, where the four prior samples ran +$0.470, −$0.0254, +$0.1207 and +$0.57.
BOTH SIGNS, A TWENTY-TWO-FOLD SPREAD (0.0254 → 0.57), STILL NO OFFSET.** ⚠ **It is the SECOND-smallest
of the five, not the smallest — 10-02's 16:46 reading of −$0.0254 is smaller, and this run wrote
"smallest yet" before checking the four numbers sitting in its own sentence. Corrected before
publication; see the journal.** ⚠⚠ **FOUR CENTS IS THE DANGEROUS SAMPLE, NOT THE REASSURING ONE: at
this distance the broker mark and the official close LOOK INTERCHANGEABLE, which is precisely when a
run reaches for whichever is at hand. The rule does not relax as the gap narrows.** ⚠ **And `lastday_price`
707.43 is STILL not the official 10-14 close 707.44 — a third consecutive seat reading the same $0.01
disagreement — so `change_today` +0.00269 and `unrealized_intraday_pl` +$188.187991 are broker-midpoint
figures and NOT official-basis day figures.**

⚠⚠ **`rebalance_delta` TOOK A THIRD READING TODAY AND THE 12:41 COUNTER-EXAMPLE GOT STRONGER, NOT
WEAKER: +$73.15 (09:37) → −$21.89 (12:41) → −$76.96 (16:16), while core ran 69.96% → 69.93% → 70.02% →
70.08% AND NEVER LEFT THE BAND.** A run reading only the delta would have been told "buy VOO" at the
open, "sell VOO" at lunch and "sell more VOO" at the close, **on one unchanged position in one
session.** ⚠ **§2 triggers on the 65–75% BAND and nothing else. The delta's SIGN is as uninformative
as its magnitude, and §2's call belongs to the market-open seat in any case.**

**§2 — NO REBALANCE DUE TOMORROW, STATED PLAINLY AS THE CLOSE SEAT IS ASKED TO.** On the official
close, core is **70.0779%** of a **$100,260.4818** book — **4.92 points of headroom at the 65% edge and
4.92 at the 75% edge.** The live 16:16 mark says the same thing at **70.08%**. ⚠ **Both band edges are
TWO FIXED VOO PRICES while cash sits at exactly $30,000 and the satellite sleeve is empty; both go VOID
the moment either changes.**

**STEP 2 — THE HIGH-WATER STAMP IS *THIS SEAT'S OWN STEP*, AND IT HAD NO SUBJECT.** There are **zero
open satellite positions**, so there was no symbol to pull a bar for, **no `highest_close` to raise and
no `(as of …)` date to advance.** ⚠⚠ **"HIGH-WATER MARKS UPDATED" WOULD HAVE BEEN FALSE, AND SO WOULD
"VERIFIED". The honest form is: THE JOB HAD NO OPERAND.** ⚠ **Nothing was backfilled and nothing could
be. The `(as of …)` date is the ONLY thing that will ever separate a mark correctly unchanged from a
mark silently not written — and it does not exist yet, so the midday detector that reads it has no
input either.** ⚠⚠ **The stamp path and the backfill path are BOTH still unexercised code after 32
sessions, and 32 sessions of "no subject" is not evidence that either works.**

⚠⚠ **CORE VOO NOT STAMPED — 103rd CONSECUTIVE REFUSAL, AND THIS ONE IS THE *HARD/STRONG* GRADE, WHICH
IS WHY IT IS WORTH MORE THAN THE THREE EASY ONES EARLIER TODAY.** This seat held **a real, completed,
correctly-basised official close — 709.37, from its own `bars` pull** — **AND** the write path, at the
one routine whose own instruction reads *"record the closes"*, on the only row the broker returns.
**NOTHING WAS WRITTEN.** §5 exempts core from all four sell rules, and a `highest_close` on VOO would
fabricate a §5.4 trailing stop on the one position the strategy exempts — which §7 forbids outright.
⚠ **A refusal repeated 103 times is a refusal nobody is deciding any more; it was re-made on its merits
here rather than inherited.**

---

### `sell_rule_status` — ALL FOUR RULES **ABSENT, NOT PASSING** (2026-10-14, **ONE DIGEST FOR THE DATE, ALL FOUR SEATS:** `1-premarket` 08:21 · `2-market-open` 09:37 · `3-midday` 12:41 · `4-market-close` 16:16. ⚠ **COLLAPSED BY THE CLOSE SEAT, WHICH IS THE FIRST SEAT ENTITLED TO TOUCH A BLOCK THREE EARLIER SEATS WROTE** — a seat cannot fairly collapse a paragraph it has just written. ⚠ **RE-DATED AND RE-EVALUATED, NOT LEFT: a table untouched and a table re-evaluated to the same answer are indistinguishable to the next reader.**)

**§5.1–5.4 RE-EVALUATED IN ORDER AT EVERY SEAT, REACHED AND NOT INHERITED — THE SAME NULL FOUR TIMES.**
Core VOO is struck from the working list **before any rule is read**, per §5's exemption; with it gone
the list is empty. Zero `sell`, zero `quote`, zero `move`, zero Perplexity at every seat — §5.1 takes one
news query **per position** and there were none, so that absence is **structural, not a skipped step.**
⚠⚠ **DISTANCE IS UNDEFINED, NOT LARGE. "Nothing close to triggering" would be a fabrication, because
nothing can be close to a threshold it has no operand for.**

| Rule | Status | Distance | Why not "passing" |
|---|---|---|---|
| **§5.1** invalidation | **NO OPERAND** | n/a | No thesis held; no `invalidation` string to read. `open_thesis_ids: none`. **No news check was issued on any holding — an absence, not a skipped step.** |
| **§5.2** time stop | **NO OPERAND** | n/a | No `timing_window` or deadline field exists in this file. |
| **§5.3** hard stop −7% | **UNDEFINED** | **undefined** | No satellite `entry_price`. The 706.74 core fill is §5-exempt, not an operand. |
| **§5.4** trailing −10% | **NOT ARMED** | **undefined** | No `highest_close`. Arms on the first **satellite** fill; 09-03's core fill was not one. |

**LEDGER RECONCILED FIRST AT ALL FOUR SEATS, BEFORE RESEARCH AND BEFORE ANY RULE WAS READ. THREE SIDES
AGREE AT EVERY SEAT:** this file holds **zero satellite blocks**; `positions` returns **one row — VOO**
99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999** (unchanged since 2026-09-03); `sleeves`
reports `satellite.count: 0`. ⚠ **GREP TRAP: `entry_price` / `highest_close` / `invalidation` return
three hits, ALL INSIDE `## Template` — the expected reading of an EMPTY ledger, not a position.**
⚠⚠ **SO THE EXITS-ONLY AND HIGH-WATER SCOPES HAVE NO SUBJECT, AND THAT IS AN ABSENCE RATHER THAN A
QUIET DAY.** **Nothing was researched and nothing was placed on top of a ledger in doubt.**

**STEP 2 (the high-water stamp and its detector) RAN AND HAD NO OPERAND AT BOTH SEATS THAT OWN IT.**
No `highest_close` exists outside the template placeholder: the field is **ABSENT — a third state
carrying no `(as of …)` date at all** — so there was no date to advance, no date to compare against the
last trading day, and ⚠ **NO STALENESS WAS DETECTED *AND* NONE WAS RULED OUT.** The backfill path stays
**UNEXERCISED CODE.** ⚠⚠ **DO NOT BACKFILL ANYTHING — THERE IS NOTHING TO WRITE.** "High-water marks
updated" and "verified" would both have been FALSE; the honest form is **the job had no subject.**

⚠⚠ **CORE VOO NOT STAMPED — DECLINED A 99th CONSECUTIVE RUN, AND AT THE CLOSE SEAT IT IS THE *HARD*
GRADE FOR THE FIRST TIME TODAY.** The 08:21, 09:37 and 12:41 refusals were the EASY grade and said so:
**zero `bars` calls at any of them, so there was no ingredient to be tempted by.** ⚠ **This seat called
`bars` — it needs the official close for the day's P&L — so VOO's complete, official **707.44** was
sitting in front of it, correctly basised and correctly dated, at the one moment a `highest_close` write
would have looked entirely routine.** §7 forbids arming §5.4 on the one position §5 exempts: a mark on
core would **fabricate a trailing stop on the only holding that is exempt from it.**

**CLOCK AT ALL FOUR SEATS, READ OFF THE DATES AND NOT THE BOOLEAN.** 08:21:37 **FALSE**, `next_open`
*and* `next_close` both **2026-10-14** — the **pre-market full-session** signature, not a holiday and
not an early close. 09:36:57 **TRUE** (TRUE has one meaning). 12:41:22 **TRUE**, `next_close`
**2026-10-14T16:00** with `next_open` **rolled to 2026-10-15T09:30** — mid-session.
**16:16:36 FALSE, `next_open` 2026-10-15T09:30 AND `next_close` 2026-10-15T16:00 — BOTH DATED
2026-10-15: the post-bell signature.**
⚠⚠ **CATCH (24) IS NOW FULLY RESOLVED, BOTH HALVES, AND BOTH IN THE CORRECTION'S FAVOUR.** The 08:21
seat predicted *"12:30 … read FALSE again"* and the 09:37 seat corrected it to TRUE **by checking the
10-12 record rather than reasoning about the boolean** — 12:41 read TRUE. Its second half, *"16:17 FALSE
with both dates on 2026-10-15"*, **is what arrived.** ⚠ **The transferable part is the method, not the
verdict: a clock prediction is checkable against the record, so check it there.**

**SLEEVES, EACH ON ITS OWN CALL AND BASIS — NEVER DIFFERENCED, NEVER CONCATENATED.** Pre-bell core
**70.2992%** of **$101,007.25** · post-open **70.16%** of **$100,544.75** · midday **70.04%** of
**$100,146.58** · **post-bell 70.0% of $100,002.96** (`sleeves` 16:17), satellite **0.0%** / count
**0**, cash **30.0%** — **$30,000.00 exactly at every seat.** On the official-close basis the close
seat reads core **70.0208%** / cash **29.9792%** of **$100,069.3224**. ⚠ **IN BAND AT ALL FOUR.
§2 puts the rebalance decision at the 09:37 seat and nowhere else, where it was TAKEN rather than
deferred: no rebalance was due and none was placed.** `rebalance_delta` ran **−$163.43 → −$43.97 →
−$0.89** across the day and is a **DISTANCE READOUT, NOT AN INSTRUCTION** at any seat but that one.

⚠⚠ **FINDING RE-DERIVED INDEPENDENTLY AND CONFIRMED TO THE CENT — THE §2 BAND IS TWO FIXED VOO PRICES,
AND IN-BAND RUNS KEEP REPORTING IT AS A MOVING PERCENTAGE INSTEAD.** The midday seat solved the edges
and the close seat **re-solved them from source rather than inheriting them, and got the same two
numbers:** while cash is **exactly $30,000** and the satellite sleeve is **EMPTY**,
`core/(core + 30,000)` = 0.65 and 0.75 give core **$55,714.29** and **$90,000**, which over the fixed
**99.046311231** shares is VOO at **$562.51** and **$908.67**. ⚠⚠ **THOSE TWO PRICES DID NOT MOVE ONCE
TODAY while the percentage was written down four different ways (70.2992 → 70.16 → 70.04 → 70.0208) on
VOO 716.9096 → 712.2401 → 708.22 → 707.44.** ⚠ **Today is the cleanest available demonstration: VOO fell
**−1.0684%** on the session and core% fell **0.28pp**, leaving the band **a fifth of VOO away** in
either direction.** ⚠⚠ **THE PRECONDITION IS THE ENTIRE VALUE OF THOSE TWO NUMBERS AND MUST BE
RE-CHECKED, NEVER INHERITED: both edges are VOID the moment cash leaves $30,000 or any satellite
position exists.**

⚠⚠ **TWO-FEED FINDING LIVE AT A FIFTH CONSECUTIVE SEAT, GAP UNCHANGED AT +12¢ ALL DAY:**
`lastday_price` **715.20** at 08:21, 09:37, 12:41 **and 16:16**, against the official 10-13 close
**715.08**. ⚠ **Byte-identical across a complete session — `lastday_price` is a FIXED prior-day field
WITHIN a session, which is the one exception to the moving-midpoint claim — and it still disagrees with
the official close by an unpredictable amount and must NEVER be differenced against one.**
⚠⚠ **AND A FIFTH POST-BELL BROKER/OFFICIAL SAMPLE, THE LARGEST IN MAGNITUDE ON RECORD AND NEGATIVE:
`current_price` **706.77** at 16:16 against today's official close **707.44** = **−$0.67.** The five
post-bell samples now read +$0.470, −$0.0254, +$0.1207, +$0.57, **−$0.67** — ⚠ **BOTH SIGNS, A
TWENTY-SIX-FOLD SPREAD. "It is roughly X" remains unavailable, and the largest sample is not a trend.
DO NOT PREDICT THE GAP AND DO NOT DIFFERENCE THE SERIES.** ⚠ **A mark read off `positions` is NOT a
close: harmless on an empty sleeve, wrong-numbered the moment §5.4 arms.**

**THE STALENESS GATE WAS EXERCISED AT 09:37 AND DID NOT FIRE — READ OFF THE FIELD, NOT THE OUTCOME:**
`plan_date: 2026-10-14` against an ET date of **2026-10-14**. **FRESH.** Non-exercise count **40**; the
gate has **never** fired and its `clickup.py alert --key stale-plan` path remains **untested code.**
⚠ **The plan was fresh AND deliberately empty — zero BUY, zero SELL, zero REBALANCE — and a fresh empty
plan and a stale plan produce a BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. THIS DAY HAD THE FORMER, and
recording which is the only thing that separates them afterwards.** ⚠ **No intent was opened that the
plan did not carry: all five of 10-14's candidates are REJECTED, not deferred, and four did not die on
price, so no later tape could revive them. A rejection is not a queue.**

**HOUSEKEEPING, RE-RUN FROM SOURCE AT EVERY SEAT** (full readings in `state.md`): week anchor
**recomputed** — `America/New_York` 2026-10-14, Wednesday, **ISO week 42 weekday 3, Monday anchor
2026-10-12** — **MATCHED** `week_of`, so `new_positions_this_week` was **not re-reset: 0 of 3** ·
breaker **INACTIVE**, `halt_triggered_at: none`, so **no `HALT_CLEARED_AT` comparison was due** ·
`consecutive_closed_losses` **0, untouched and not reset — nothing closed today, so there was no streak
to confirm against** · `control.md` re-read from disk at 09:37 and again at 16:16: `TRADING_ENABLED:
true`, **notes empty** · **zero open alerts, so no incident was due and none was raised** ·
`orders --status all` returns **one row for the entire account history** (2026-09-03 core fill,
`status: filled`, terminal), so **zero orders from today and zero non-terminal orders — §7's limbo
warning has NO OPERAND rather than a clean bill.** ⚠ **The satellite `buy` branch and the ENTIRE `sell`
path stay UNEXERCISED: the only order ever placed on this account is a `--core` one.**

**RESEARCH — SEAT 1 ONLY, AND THE OTHER THREE WERE NOT ENTITLED TO ANY.** **Five** candidates, **zero
accepted, five REJECTED** (`T-2026-10-14-01`…`-05`); thesis count **151 → 156**. `-01` (LMT/Avio) gave
the US-defence-award rule its **second mechanism** — the tier below the prime **named and FOREIGN**,
unreachable by any better question — and `-02` (AMD/Fermi) gave rule (viii) its **first guarantee**, a
credit backstop being a contingent liability of the opposite sign from revenue. ⚠ **§4 routes every buy
through the pre-market and 09:35 seats precisely so that no buy is reasoned into existence intraday or
after the bell.**

⚠⚠ **FINDING (25) STANDS AND THIS BLOCK IS NOW ITS REPAIR RATHER THAN ITS EVIDENCE — THE "Nth
CONSECUTIVE SESSION" COUNTER ON §5 WAS NOT COUNTING SESSIONS.** The 10-13 digest below carries **two
counters for the SAME null, same date, same file, 52 apart** ("83rd session" for §5, "31st session" for
Step 2), and the §5 one **advanced twice inside 10-14 alone** (84 at 08:21, 85 at 09:37) while all four
of 10-13's seats shared one value — so the unit was **neither a session nor a seat. IT WAS UNDEFINED.**
⚠⚠ **NO 86th WAS MINTED BY THE MIDDAY SEAT AND NONE IS MINTED HERE. The two DEFINED facts carry the
arithmetic: ZERO satellite positions ever, and — advanced by this seat, which is the only one entitled
to count the day it stands in — **31 completed sessions / 28 post-fill.**** ⚠ **Same defect as a
self-describing count and a false superlative: a number that sounds like evidence and measures nothing.**

**10-14 IS NOW COMPLETE AND IS COUNTABLE AS A ZERO-`move` SESSION — ALL FOUR SEATS, ZERO `move` CALLS.**
⚠ **The cause sits ABOVE the priced-in filter, which is the point: two genuinely eligible US-listed
tickers reached the run (`HRL`, `AMD`) and **both died at part 1**, upstream of price. A `move` on
either would have been **DECORATIVE** and was declined on that ground — the fifth and sixth such
refusals (SYNA 10-05, CEREBRAS 10-06, no-eligible-ticker 10-12, BE 10-13). ⚠ **An ABSENT check and a
PASSING one read identically in a summary, so this one names which it is.**

**MEASUREMENT, AND FOR THE FIRST TIME IN THIS FILE THE HONEST WORD IS *SHRANK*.** This digest **replaces**
the 176-line three-seat 10-14 block rather than appending a fourth seat to it, and it is shorter than
what it replaced **while carrying one more seat's readings** — the 10-13 digest below is untouched, and
nothing live was discarded: four per-seat narrations of the same null are folded to one statement each,
the repeated ledger and clock readings are stated once across all four seats, and every finding is kept.
⚠ **No self-describing count appears above, per the finding this file already paid three drafts for: a
number describing this block cannot live inside this block.** The exact deltas are `git diff --stat` on
this commit, which is the only place they are stable, and `wc` before and after is this seat's own check.
⚠⚠ **TEN SEATS HAD EACH JUDGED THEIR OWN BLOCK THE NECESSARY ONE; THIS ONE JUDGED THE OPPOSITE AND PAID
FOR IT OUT OF ITS OWN BLOCK.** ⚠ **It is a demonstration, not a fix: one seat collapsing once a day
cannot outrun four seats appending, and THE CAP ON WHAT A SEAT MAY APPEND WHEN THE NULL IS UNCHANGED IS
A RULE ONLY `control.md` OR THE ROUTINE PROMPTS CAN CARRY. STILL THE HUMAN'S TO WRITE.**


**Reconciliation 2026-10-13 — ONE DIGEST FOR THE DATE, ALL FOUR SEATS** (`1-premarket` 08:26,
`2-market-open` 09:37, `3-midday` 12:41, `4-market-close` 16:17). *(Collapsed 2026-10-14 08:21 from the
90-line `sell_rule_status` digest the close seat left. Its live findings were promoted into the 10-14
block above and into `state.md`'s standing items; what was removed is four per-seat narrations of the
same null, the §5 table restated for a date with no operand, and the counter-derivation arithmetic that
`state.md` already carries. Nothing live discarded.)*
**A COMPLETE SESSION THAT CLOSED FLAT.** Equity **$100,826.0362** on official closes (**$100,829.01**
live), day **−$23.2759 / −0.0231%**. VOO closed **715.08** (`--adjustment all` and `raw` agree, so the
basis was non-decisive). Core **70.2458%**, **IN BAND**; satellite **0.0%** / count **0**; cash
**29.7542%**; `rebalance_delta` −$248.70. **§5.1–5.4 reached NO OPERAND for an 83rd session; zero fills at
all four seats; nothing closed.** **Step 2 had no subject for a 31st session** — no `highest_close` to
raise, the field **ABSENT** rather than stale, so **no backfill was due and none was performed.**
**Core VOO not stamped, 95th consecutive refusal**, and that seat's is the load-bearing one: it held a
real, complete, correctly based official close at the one moment it had nothing to write it onto.
**08:26** rejected all eight candidates (`T-2026-10-13-01`…`-08`) and wrote a fresh, deliberately empty
plan · **09:37** read `plan_date` **off the field — FRESH** (gate non-exercise **39**) and opened nothing
with every gate open: **DISCIPLINE** · **12:41** is exits-only by construction: **STRUCTURE** · **16:17**
stamped no mark because there is none, and advanced the session count 29/26 → **30/27** as the only seat
entitled to. ⚠ **Its two findings both survive above: the two-feed price disagreement (3¢ that day), and
the corpus, where its own first draft GREW this file 708B before measurement caught it.**

---

**⚠ THE 2026-10-01 AND 2026-10-02 PER-RUN BLOCKS (EIGHT RUNS, ~350 LINES) HAVE BEEN COLLAPSED BY THIS
RUN, UNDER THE FILE'S OWN STANDING INSTRUCTION.** All eight recorded the same null — zero satellite
blocks against zero satellite Alpaca rows, agreeing; no §5 rule evaluated; no high-water mark stamped;
no backfill due; no order placed. ⚠⚠ **AND THIS RUN HAD A SPECIFIC REASON TO ACT RATHER THAN APPEND:
`state.md` flags as an item for the human that `positions.md` had grown to 67KB while holding ZERO
positions, and that NO SEAT OWNED COLLAPSING IT. This seat writes `sell_rule_status`, so it owns this
file; the collapse is performed here and the item is discharged.** **Nothing live was discarded.** The
load-bearing facts those eight blocks carried:

- **A PARTIAL BAR'S `c` FIELD IS THE LAST TRADE SO FAR WEARING A CLOSE'S CLOTHES — confirmed to the
  cent.** At 12:41 on 10-01 the partial bar's `c` **700.35** equalled `latestTrade.p` **700.35**: a
  plausible price carrying no warning of any kind. ⚠ **NO `bars` CLOSE MAY BE STAMPED AS A MARK BEFORE
  THE BELL, ON ANY BASIS.** Two routines can pull one — routine 2 at 09:35 and routine 3 at 12:30.
- **The `n`/`v` FLOOR TEST, and its margin is the finding.** The old "n/v are visibly tiny" smell test
  was replaced by "is `n` below the trailing completed-session MINIMUM". The 12:41 partial's n/v were
  **47.8% / 43.0%** of the prior completed bar — **not visibly tiny**. On 10-01 the completed bar
  cleared the floor by only **12.6%**; on 10-02 by **+61.8% / +199.8%**, the widest margin recorded.
  ⚠ **The floors themselves drift (1,450/43,730 → 1,560/45,031), so it is a corroborant built on a
  moving ruler and is NEVER the primary. STATED LIMIT, STILL UNTESTED: it MUST FAIL on a half-day
  session.**
- **A COMPLETED DAILY BAR IS NOT IMMUTABLE IN `n`/`v`** (09-30 read 2050/61014 then 2053/61032; 10-01
  1633/51892 then 1634/51893 — **the CLOSE held to the cent both times**). ⚠ **See this run's block
  above for the counter-instance that completes the rule: 10-02 did NOT drift over a weekend.**
- **A HISTORICAL *BOOK* DAY-RETURN IS NOT EXACTLY REPRODUCIBLE FROM A LATER PULL once an ex-date
  intervenes** — the cash leg does not rescale. ⚠ **Quote a day-return with its BASIS *and* its
  VINTAGE.** This is a reproducibility fact, not a defect.
- **Official closes:** 10-02 **707.35** (o 708.30 h 710.09 l 705.545; **identical on `all`, `raw` and
  `split`**, verified by three separate pulls) · 10-01 **702.255** · 09-30 **700.605**. Equity on the
  10-02 close **$100,060.4082**, core **70.0181%**, cash **29.9819%**; on the 10-01 close
  **$99,555.77**, core **69.8661%**.
- **THE EQUITY-DRIFT INSTANCES AND THE HOUR THAT MATTERED:** on 10-01 `selftest` read $99,611.63 and a
  later call in the same minute differed — a ninth instance. ⚠ **An equity figure is meaningless
  without its CALL and its TIMESTAMP, and two figures from different calls must NEVER be differenced.**
- **STEP 2 HAD NO OPERAND IN EVERY ONE OF THOSE RUNS, AND THE WRITING SEAT'S INSTANCE IS THE STRONG
  ONE:** on both 10-01 and 10-02 the close run held a complete, verified official close at the moment
  it had nothing to write it onto. ⚠ **The routine's instruction to advance the `(as of …)` date EVERY
  DAY whether or not the value moves had nothing to advance, so a run that wrote no mark and a run
  that correctly left one unchanged are indistinguishable in every artifact.** **Both the writing seat
  and routine 3's detecting seat have a blind spot of the same shape; the first satellite fill arms
  both at once; the backfill path remains UNEXERCISED CODE.**
- **`cash` read exactly $30,000.00 throughout** (a thirteenth reading on 10-01) — the dividend series,
  carried live in this run's block above.
- **Nine theses were written across those two days and all nine were rejected**; none was rehabilitated
  at a later run. **A rejection is not a queue.**
- **The §2 staleness gate was exercised at every open and never fired; its alert path is untested
  code.** ⚠ **Read `plan_date`, never the outcome.**

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
