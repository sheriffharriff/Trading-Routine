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

**Reconciliation 2026-10-05 — FOUR SEATS, ALL FOUR RUN: 08:28 `1-premarket-research`, 09:36
`2-market-open-execution`, 12:41 `3-midday-management`, 16:17 `4-market-close-journal`. THE LEDGER AGREES
WITH THE BROKER ON ALL FOUR READINGS; ZERO SATELLITE POSITIONS ON EVERY SIDE; NO §5 RULE HAD A SUBJECT; NO
HIGH-WATER MARK WRITTEN AND NONE DUE; ZERO ORDERS FROM ANY SEAT.**
⚠ **THE THREE EARLIER SEATS' BLOCKS ARE COLLAPSED HERE RATHER THAN APPENDED TO, under this file's standing
instruction and `state.md`'s open item (9). All four recorded the same null. Nothing live was discarded.**

**Session counters, advanced by the CLOSE seat and only by it: 23/20 → 24/21.** **24 completed sessions
since 2026-09-01, 21 after the 09-03 core fill, zero satellite positions ever opened.** ⚠⚠ **TODAY IS A
COMPLETED SESSION AND THAT IS WHY THE ADVANCE IS SOUND, NOT BECAUSE ROUTINE 4 IS EXEMPT FROM CATCH (11).**
Confirmed three ways, not assumed: `clock` 16:17:29 `is_open: false` with `next_open` **2026-10-06T09:30**
(the post-bell shape, read off the DATE — FALSE has three meanings, TRUE has one); a VOO daily bar dated
**2026-10-05** exists and is **complete** (o 707.52 h 713.82 l 707.52 **c 712.41** n 1,800 v 60,535); and
the **15:59:59 ET `latestTrade` prints 712.41**, matching that bar's close to the cent.
⚠ **The three earlier seats correctly added none — 08:28 and 09:36 stand in a session IN PROGRESS and 12:41
is a THIRD SEAT in the same day. 09:36 wrote "twenty-fifth" and corrected it in file (catch 15); 12:41 met
the same trap and did not fall into it.**

**RECONCILIATION, SATELLITE-TO-SATELLITE.** `alpaca.py positions` at 16:17 returns **one row, core VOO** —
99.046311231 shares, avg_entry **706.74** (a **RAW** print), cost_basis **$69,999.99**, unchanged since the
09-03 fill — against **zero satellite blocks in this file. THEY AGREE.** ⚠ **Core VOO was removed from the
working list BEFORE any §5 rule was read**, per §5's core exemption; **a run that compares the raw ledger to
the raw broker reads a correct ledger as broken.** **No discrepancy was found, so none is flagged.**
⚠ **The 24th session with nothing to reconcile — and an AGREEING ledger and an EMPTY ledger are the same
artifact here. That is the absence of a test, not a clean bill of health.**

**⚠⚠ STEP 2 — RECORDING THE CLOSES — HAD NO OPERAND, AND THAT IS THE INVISIBLE JOB THIS SEAT OWNS.**
Zero open satellite positions means **no `highest_close` to raise and no `(as of …)` date to advance.**
"High-water marks updated" would have been **FALSE**; the honest form is that the job had **no operand.**
⚠⚠ **SEVENTH CONSECUTIVE CLOSE RUN BY THE COUNT THIS RECORD KEEPS — AND THE CONDITION HAS IN FACT HELD ON
EVERY CLOSE RUN IN THE ACCOUNT'S HISTORY, since no satellite position has ever existed. THE COUNT MEASURES
HOW LONG THE FINDING HAS BEEN *NAMED*, NOT HOW LONG IT HAS BEEN *TRUE* — a mild instance of the counter
family, recorded rather than promoted.** ⚠ **The backfill path and its DETECTOR both remain unexercised
code; the first satellite fill arms both at once.**

**⚠ CORE VOO IS AGAIN NOT STAMPED WITH A `highest_close` — SEVENTY-SECOND CONSECUTIVE RUN — AND THIS SEAT
HELD THE RAW MATERIAL IN HAND.** Step 3's day P&L requires an official close, so a `bars --symbol VOO` pull
**was made** and returned a complete **712.41**. A trailing maximum is **one arithmetic step** from that
pull, and writing it would have **fabricated a §5.4 trailing stop on the one position §5 exempts** — a stop
that could eventually sell core on a drawdown, which **§7 forbids outright.** **The step was not taken and
no mark was written.** ⚠ **GRADED, NOT COUNTED: this is the SAME load-bearing form every close run has,
because every close run pulls VOO bars for the P&L. It is not a new or stronger instance and is not claimed
as one.** ⚠ **The only `highest_close` string in this file remains the TEMPLATE PLACEHOLDER — the field is
ABSENT, the third state, carrying no `(as of …)` date at all.**

**⚠⚠ CATCH (17) — THE RECORD HAS HAD 09-28 EXACTLY BACKWARDS FOR THREE RUNS, AND THE CORRECTION POINTS THE
OTHER WAY.** The standing claim (`state.md` carry-forward, and the 09-29 midday and close runs before it)
is *"09-28 … lost its close run, so with one position open 09-29's midday would have had to backfill ACROSS
AN EX-DIVIDEND DATE."* ⚠⚠ **09-28 DID NOT LOSE ITS CLOSE RUN. THE CLOSE RUN IS THE ONLY ROUTINE THAT RAN
THAT DAY.** `git log` for 2026-09-28 returns exactly two commits — the close run and its merge; the 09-28
close commit says so itself (*"routines 1-3 left NO committed output today"*), 09-29's pre-market run
verified it independently from inside that run, and the archived journal carries a full 09-28 close entry
with a 16:16:24 `clock` read. ⚠ **So the hypothetical is impossible as written: a close run that ran would
have written the mark, leaving 09-29's midday nothing to backfill.**
⚠⚠ **THE CORRECTED LESSON IS THE MORE USEFUL ONE: 09-28 LOST ROUTINES 1, 2 AND 3 — AND ROUTINE 3 IS THE
DETECTOR. A MISSING WRITER LEAVES EVIDENCE (a stale `(as of …)` date for the next detector to find). A
MISSING DETECTOR LEAVES NOTHING AT ALL — it is silent by construction, and its absence is indistinguishable
from its finding everything healthy. 09-28 is a worked instance of the HARDER failure, not the easier one.**
⚠ **Consequence for this file's standing line: it is right about the SHAPE (both halves share a blind spot)
and wrong about the HISTORY — the WRITING seat has never been missed; the DETECTING seat has, once.**

**⚠⚠ `cash` READ EXACTLY $30,000.00 FOR A TWENTY-SECOND TIME, AT 16:17 POST-BELL — THE VOO DIVIDEND IS
STILL UNPAID**, on the fourth trading day after the 09-28 ex-date. ⚠ **Twenty-two readings are ONE
unresolved observation.** **The falsifiable test stands verbatim: `cash` should rise to about $30,180.76
($1.825/share × 99.046311231, an INFERENCE — Alpaca does not publish it). If it has not by 2026-10-07, the
paper account does not model dividends at all.** ⚠ **$1.825/share is independently corroborated by the
ex-date adjustment factor (710.705 raw × 0.002568 = 1.8251), so the 09-28 close run's "~$180.45" was a slip
and $180.76 is the figure.**
⚠⚠ **EIGHT SEATS REMAIN AFTER THIS RUN — 10-06 r1–r4 and 10-07 r1–r4; routine 5 is Friday-only and 10-09 is
past the deadline. RE-ENUMERATED FROM THIS SEAT, NOT INHERITED, AND THE INHERITED NUMBER WAS WRONG WHEN IT
WAS WRITTEN — CATCH (18).** The 12:41 seat's *"nine seats stand between that claim and it (10-05 close;
10-06 r1–r4; 10-07 r1–r4)"* **omits the 10-05 midday seat it was itself sitting in** — the right answer from
09:36 was **ten** — and its *"eight remain after this run"* is one low for the same reason: after midday,
**nine** remained. ⚠⚠ **Both halves off by exactly one, same direction, same cause: a seat excluding itself
from a period it was standing in. That is catch (11)/(15)'s mechanism arriving INSIDE catch (16)'s own
correction, and the fourth consecutive proof of catch (9): NAMING A FAILURE DOES NOT RETIRE IT.**
⚠ **THE GENERALISABLE HALF: A COUNTDOWN INHERITED VERBATIM IS A DIFFERENT AND MORE DANGEROUS OBJECT THAN A
COUNT-UP.** A count-up is right or wrong independent of its reader; a countdown is true only at the instant
it was written. **"Eight" was wrong when written and is right now, so inheriting it unchanged would have
produced the correct number BY ACCIDENT with no signal that anything had been checked.** **Write a countdown
with the seat it was written from, or write the deadline and make the next reader count.**

### `sell_rule_status` — ALL FOUR RULES ABSENT, NOT PASSING (2026-10-05, FINAL READ AT 16:17 ET BY THE CLOSE SEAT; UNCHANGED FROM ALL THREE EARLIER SEATS)

⚠⚠ **THERE IS NO POSITION TO WRITE A `sell_rule_status` LINE ON. The distance to each rule is therefore
not "large" — it is UNDEFINED, and those are different facts.** ⚠ **"Nothing close to triggering" would be
a fabrication: nothing can be close to a threshold it has no operand for.**

| Rule | Status this run | Distance | Why it is not "passing" |
|---|---|---|---|
| **§5.1** thesis invalidation | **NO OPERAND** | n/a | No thesis is held, so no `invalidation` string exists to read verbatim. **Zero Perplexity news-on-holdings queries were due and zero were run.** |
| **§5.2** time stop | **NO OPERAND** | n/a | No `timing_window` and no deadline field exists anywhere in this file. |
| **§5.3** hard stop −7% from entry | **DISTANCE UNDEFINED** | **UNDEFINED, not large** | There is no satellite `entry_price` to measure a drawdown from. The 706.74 core fill is **exempt under §5** and is not an operand. |
| **§5.4** trailing stop −10% from `highest_close` | **NOT ARMED** | **UNDEFINED, not large** | No `highest_close` field — the **third state**, carrying no `(as of …)` date at all. It arms on the first **satellite** fill; the 09-03 core fill was not one. |

**Zero orders submitted by ANY of the four seats today** — the pre-market seat places none by design, the
09:36 open seat placed none **because the plan it consumes carried no intent**, the 12:41 midday seat placed
none because it is **exits-only and there was nothing to exit**, and this close seat **records and journals
and does not trade.** **Zero fills, nothing opened, nothing closed, no realised P&L.**
**`orders --status all` returns ONE ROW for the account's entire history** — the 09-03 core buy, `status:
filled`, terminal — so **nothing is in limbo overnight and §7 has nothing unverified.**
`consecutive_closed_losses` stays **0, confirmed against what actually closed today, which was nothing.**
The §6 three-loss breaker has therefore **never been approached, not merely never breached**, and
`clickup.py alert --key circuit-breaker` remains **UNTESTED CODE.** Breaker **INACTIVE**
(`halt_triggered_at: none`, so no `HALT_CLEARED_AT` comparison was required; the `none` in `control.md` is
**untested against a live halt**, not cleared).

**§5.1–§5.4 HAVE NEVER HAD AN OPERAND IN THIS ACCOUNT'S ENTIRE HISTORY** — **24 completed trading sessions
since 2026-09-01, 21 AFTER the 09-03 core fill**, **zero satellite positions ever opened.**

**⚠ TODAY'S OFFICIAL CLOSE AND WHAT IT IS AND IS NOT.** VOO **712.41** on **both** `--adjustment all` and
`raw` (no ex-date since 09-28, so this week's comparisons are basis-clean — **a property of this week, not
a repeal; the next ex-date restores the trap**). Official-close equity **$100,561.58** = 99.046311231 ×
712.41 + $30,000.00, core **70.1675%**, cash **29.8325%**. Day **+$501.17 / +0.5009%** from 10-02's
$100,060.41, both legs official and same-basis.
⚠ **Broker mark at 16:17 for contrast and NOT for differencing: equity $100,535.83, `current_price` 712.15,
which sits −$0.26 against the official close — a THIRD post-bell reading of a MOVING LIVE MIDPOINT (10-02
16:16 +$0.470, 16:46 −$0.0254), not an offset.** ⚠ **One observation, not a mechanism: 712.15 also equals
the 16:01 `latestQuote` midpoint (bp 712.12 / ap 712.19 → 712.155) to the cent. NOT asserted as a
mechanism — the record's standing instruction is to STOP PREDICTING these fields.**
⚠⚠ **`equity − last_equity` WOULD HAVE PRINTED +0.4562% AGAINST THE TRUE +0.5009% — AN UNDERSTATEMENT OF
0.0446pp, WHERE ON 10-02 THE SAME FIELD FLATTERED BY 0.0372pp. THE ARTIFACT'S DIRECTION IS NOT STABLE.**
Fully attributed as before: `last_equity` 100079.22704838174 = 99.046311231 × `lastday_price` 707.54 +
$30,000.00, exactly. ⚠ **NEVER use it, and do not re-open WHY `lastday_price` differs from the close.**

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
