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
plan_date: 2026-10-21
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-21 at 09:30 ET** (`alpaca.py clock` at 08:03:24 ET: `is_open:
false`, `next_open: 2026-10-21T09:30:00-04:00`, `next_close: 2026-10-21T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean.**

The plan this run replaced was dated **2026-10-20** — **one calendar day and one trading
day old.** Correct and current; nothing to note.

---

## Tape context

**Pre-flight selftest: 5/5** (env · Alpaca ACTIVE `trading_blocked=False` · Perplexity
`sonar-pro` · ClickUp · `control.md` LIVE). `TRADING_ENABLED: true`, **LIVE paper**,
`control.md` **Notes empty**. **Zero open alerts** (`alerts.md` Open incidents: *(none)*).
**Zero non-terminal orders** — the whole account history is still **ONE order** (the
2026-09-03 core fill, `filled`, terminal), so §7's order-limbo warning has **no operand**
rather than a clean bill.

**Numbers, each with its call and its basis — never differenced across calls.**

| Reading | Value | Call / basis |
|---|---|---|
| Account equity | **$100,167.38** | `sleeves` 08:03, live broker mark |
| Cash | **$30,000.00** exactly | `sleeves` — ~**41st** consecutive unchanged reading |
| Core VOO | **$70,167.378265** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:03 |
| Core % | **70.05%** | `sleeves`, live-mark basis |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **29.95%** | `sleeves` |
| Unrealized P&L on core | **+$167.388266 / +0.239%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **708.43** | `positions` `current_price`, 08:03 — a **pre-market indicative mark, NOT a close** |
| VOO official 10-20 close | **706.33** | `bars --days 4 --adjustment all`, **re-pulled this run** |
| VOO `lastday_price` | **706.80** | ⚠ **NOT the official close. See the warning below.** |
| §6 5% cap | **$5,008.37** | 100,167.38 × 5%, **with no operand** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (+0.00231), OR
`unrealized_intraday_pl` (+$161.445487) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **706.80** against the official 10-20 close of **706.33**.
⚠⚠ **FOURTEENTH CONSECUTIVE SEAT ON THE STALE `lastday_price`, GAP NOW +$0.47 — THE LARGEST
RECORDED AND POSITIVE FOR A SECOND CONSECUTIVE SEAT.** ⚠ **The defect is NOT a fixed offset
that could be corrected for — it has flipped sign across seats before (−$0.135 on 10-19,
+$0.13 on 10-20, +$0.47 today). Never difference the two.**

⚠ **The core is ABOVE its entry for the first time in several sessions (+$167.39 against the
706.74 fill). That is a mark moving, not a result, and it changes nothing: §5 exempts core and
§2's band is the only test that applies to it.**

---

## Reconciliation

1. **LEDGER RECONCILED FIRST, BEFORE ANY RESEARCH AND BEFORE ANY SELL RULE WAS READ. THREE
   SIDES AGREE.** `positions.md` holds **zero satellite blocks** · `alpaca.py positions`
   returns **one row, VOO**, 99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999**,
   **unchanged since 2026-09-03** · `sleeves` reports `satellite.count: 0`.
   ⚠ **No discrepancy. Nothing was researched on top of a ledger in doubt.**
   ⚠ **GREP TRAP, so the next seat does not re-raise it: `entry_price` / `highest_close` /
   `invalidation` return hits in `positions.md` that are ALL INSIDE `## Template`. That is the
   expected reading of an EMPTY ledger, not a position.**
2. **WEEK ROLLOVER — RECOMPUTED FROM SOURCE, NOT READ OFF THE FIELD.**
   `America/New_York` → **2026-10-21, Wednesday, ISO week 43, weekday 3, Monday anchor
   2026-10-19.** That **MATCHES** `week_of: 2026-10-19`. So `new_positions_this_week` was
   **NOT re-reset** — it stands at **0 of 3** because nothing has been opened, not because
   this run zeroed it. ⚠ **The distinction matters: a run that resets a counter it did not
   need to reset would mask a §6 breach.** The anchor holds through **Friday 2026-10-23**.
3. **CIRCUIT BREAKER — INACTIVE.** `consecutive_closed_losses: 0`, `halt_triggered_at: none`.
   ⚠ **Because `halt_triggered_at` is `none`, the `HALT_CLEARED_AT` comparison in `control.md`
   has no operand — there is nothing to clear, and `HALT_CLEARED_AT: none` is therefore
   CORRECT and not an oversight. New positions are NOT barred by §6's halt.**
4. **§5 HAS NO OPERAND.** Zero satellite positions → rules 5.1–5.4 are **ABSENT, not passing**,
   and `highest_close` does not exist as a field. **No Perplexity invalidation checks were run
   on holdings, because there are no holdings.** Core VOO was struck from the working list
   **before** any §5 rule was read, per §5's core exemption. ⚠ **FIFTEENTH consecutive seat with
   §5 absent rather than passing. The repair machinery has still never been exercised once.**

---

## Sleeve check (§2)

**Core 70.05%, IN BAND** (65–75%), **5.05pp above the lower edge and 4.95pp below the upper.**
`core_in_band: true`, `rebalance_needed: false`.
⚠ **`rebalance_delta: −50.21` is a DISTANCE READOUT, NOT AN INSTRUCTION.** It is the dollar
distance to a perfect 70.00%, driven by VOO's own mark moving under a fixed share count.
**$50 on a $70,167 position is 0.07%.** ⚠ *It has flipped SIGN from yesterday's +$118.56 —
core is now marginally ABOVE 70% rather than below it, because VOO's pre-bell mark rose against
unchanged cash. The sign flip is the mark moving, not drift developing.* **No rebalance is due
and none is queued.**

---

## Intents

### BUY — none

**ZERO BUY INTENTS. This is the output §4 says most research runs should produce, and it is
not a failed run.**

New positions were **permitted** this morning on every gate — breaker inactive,
`new_positions_this_week` **0 of 3**, satellite sleeve **entirely undeployed** ($30,000 and
29.95% of the account in cash), `control.md` notes empty. ⚠ **So the absence of a buy is a
RESEARCH result, not a permission result. Nothing was blocked; nothing qualified.**

**Four theses written, all four rejected** — `T-2026-10-21-01` through `-04`. Where they died:

| ID | Object | Killed by |
|---|---|---|
| `-01` | **Apple (AAPL) American Manufacturing Program → AVGO · GLW · COHR · TSM · AMKR** | **part 2 at all five legs** (no figure, no segment, no revenue share — source volunteered the absence) · **rule (iii) at all five** (existing partners, "progress reported" = the GM/Lockheed delivery-milestone costume) · **§3** on both NEW relationships (Perryman, Qnity — private) |
| `-02` | **Micron (MU) / Indium Corporation** | **part 1** — the only counterparty is PRIVATE · **rule (viii)** money paid OUT by the only buyable leg · **part 2** no figure, no segment · **NEW rule (iii) split, mirror of TSMC's** |
| `-03` | **General Motors (GM) Q3 → the auto-supplier read-across** | **part 1** — own results, no second party · **rule (iii) costume #1** — outlook vs MARKET expectations, not its own prior range · read-across is the **shared-cause** object and points DOWN |
| `-04` | Sweep of **fifteen** (Perryman · Qnity · Indium · MS International · Theon · Circle8/CAK · Polaris/Trina · Hotel101 · OESX · Archer · FTI/BP MoU · XCF · **MMM re-serve** · **RTX re-serve** · macro+calendar block) | disposed as one, **zero drill queries** |

⚠⚠⚠ **THE ONE THING THE OPEN SEAT MUST CARRY FROM THIS RESEARCH IS A DEFECT IN ITS OWN
MACHINERY — AND THE CLAIM IS CORRECTED FROM THE DRAFT: THIS IS **SHAPE ONE AT THE LARGEST SAMPLE EVER
RECORDED (7 OF 7)**, NOT A NEW "SHAPE SEVEN". `state.md` already carries *shape one — a DRAWDOWN misread
as priced-in* (nine instances) and *shape three — sign- and causation-blindness*; this seat re-derived
both from scratch and briefly promoted them to a discovery. ⚠ **`grep` THE EXISTING LIST BEFORE CLAIMING
AN ADDITION TO IT.** ⚠ **WHAT IS GENUINELY NEW IS THE EVIDENCE:** seven `move` calls
were spent today, the largest sample this filter has ever had, and **all seven returned
`priced_in: true` with ALL SEVEN DOWN**: `COHR` −20.07% · `AMKR` −12.45% · `GLW` −10.94% ·
`GM` −8.24% · `AVGO` −6.41% · `MU` −5.92% · `TSM` −4.43%. ⚠⚠ **`scripts/alpaca.py:177` is
`abs(move) > PRICED_IN_MOVE_PCT` — THE FILTER IS DIRECTION-BLIND and reads a 20% COLLAPSE as
"you are late, the news is priced in." For a §3 long-only strategy that is backwards.**
⚠⚠ **SECOND GAP, IN §4's WORDING NOT THE SCRIPT'S: the rule says "moved more than 4% … *on
this news*", and the filter cannot tell whether the move was on the news at all. Today it
demonstrably was not — `VOO` over the identical window is **−1.22%, `priced_in: false`**, so
the index is flat while the semi/AI complex is down 4–20%, and the scan named the cause
(*"an AI-stock pullback"*).** ⚠⚠⚠ **IT IS NOT GROUNDS TO OVERRIDE ANYTHING: the filter said
skip, the skip stands, and every one of the five Apple suppliers dies independently on part 2
and rule (iii), so the defect rescues NO candidate. Shape six failed TOWARD a trade; this one
fails toward refusing one — it costs opportunity, not capital.** ⚠ **Only a human may change
§4 or `alpaca.py move`. Open human item.**

⚠ **NO `revalidate` LINES EXIST BECAUSE THERE IS NOTHING TO REVALIDATE.** The template asks
for the specific number the open run should re-check against an overnight gap. **With zero BUY
intents there is no candidate, no priced-in figure, and no number.** ⚠ **A `revalidate` line
invented for an empty plan would be the open seat's most dangerous possible inheritance.**

### SELL — none

**§5 has no operand** — zero satellite positions, so rules 5.1–5.4 are **ABSENT, not passing**.
Core VOO is **exempt** by §5 and was struck from the working list before the rules were read.

### REBALANCE — none

Core **70.05%**, in band. See **Sleeve check** above. `rebalance_needed: false`.
⚠ **`rebalance_delta: −50.21` must be RE-COMPUTED at the open seat, not inherited** — it is a
distance to 70.00% on a mark that moves every minute, and it has already flipped sign once
since yesterday.

---

## Carried from the research — for the open seat

- ⚠ **DO NOT re-litigate any of `T-2026-10-21-01`…`-04`.** All four are disposed with named
  reasons in `research_log.md`.
- ⚠⚠⚠ **THE APPLE ITEM IS A REJECTION, AND IT IS THE MOST IMPORTANT ONE THIS LOG HAS PRODUCED
  SINCE GFS — READ IT BEFORE ANY RESEARCH TODAY.** For seven weeks this log's complaint has been
  that the funnel never names Company B. **Today Company A named FIVE, US-listed, with the
  facility and the component specified, and the mechanism sentence wrote itself in one clause.**
  ⚠ **AND THE KILL JUST MOVED ONE RUNG LATER — to the NUMBER instead of the NAME. The missing
  object was never Company B's identity; it is the SEGMENT-ATTRIBUTED DOLLAR FIGURE, reported
  absent seventeen consecutive sessions.** ⚠ **If the funnel re-serves any of AVGO/GLW/COHR/
  TSM/AMKR today, the answer is written: no figure, no segment, existing partner.**
- ⚠⚠ **A NAMED COMPANY B IS NOT ENOUGH, AND THE DRILL THAT FOUND IT IS WORTH KEEPING.** The
  structural scan surfaced only the **private** Perryman leg; the five listed suppliers appeared
  **only** under a one-line drill asking *"name EVERY company the announcement named."* **That
  clause converted a dead item into the log's first five-leg part-1 pass. Use it whenever
  Company A announces a programme rather than a transaction.**
- ⚠⚠ **THE BIG NUMBER AND THE NEW EVENT ARE DIFFERENT OBJECTS — NOW THE DOMINANT SHAPE, THREE
  SESSIONS RUNNING.** 10-20: 3M's "$6B" was a warrant vesting threshold, not revenue. 10-21:
  Micron's "up to $3B" is a **July** programme ceiling while the **genuinely new** Indium
  funding **has no amount at all**, and Broadcom's "$1.5B" is **Broadcom's own July capex**, not
  Apple's payment. ⚠ **A reader who asks "is there a dollar figure?" and "is this new?" as two
  separate yes/no questions gets two yeses and proceeds on a combination that does not exist.**
  ⚠ **THE FIX IS ONE CLAUSE IN THE DRILL: ask for the figure disclosed *FOR THIS TRANSACTION*,
  not for the figure in the announcement. It worked today and is the only reason the $3B did not
  become a part-2 input.**
- ⚠⚠ **DISPOSED-REJECT RE-SERVE IS AT THREE CONSECUTIVE SESSIONS AND TODAY WAS THE WORST FORM:
  the funnel named `T-2026-10-20-01` (MMM/Amazon) as the day's "clearest cross-company event"
  less than 24 hours after it was killed.** ⚠ **`RTX` was re-served too — SEVENTH appearance in
  eleven sessions — with the source itself dating the cited awards to 2026-09-28. READ THE LOG
  BEFORE THE TAPE; it cost one `grep` and saved two drills.**
- ⚠ **EARNINGS-SEASON PREDICTION NOW CONFIRMED, NOT OUTSTANDING.** The 10-20 seat wrote "expect
  it all earnings season" about guidance quoted against consensus rather than a company's own
  prior range. **GM did exactly that on 10-21, with the source stating outright that it "does
  not establish whether GM lowered guidance against its own previously stated range."**
  **Apply rule (iii) to the figure the mechanism runs on, not to the release.**
- ⚠ **THE FORWARD CALENDAR IS NOT A MONDAY-ONLY SHAPE.** The carry-forward predicted it for the
  Monday pre-market seat; it arrived on a **Wednesday** (Tesla/Meta/Netflix scheduled for 10-21).
  ⚠ **The prediction was too narrow: it is a shape of any THIN window, and a mid-week session
  with one trading day of inventory inside an AI pullback is thin. NOTE THE DATES AND DO NOTHING.**
- ⚠ **SEVEN `move` CALLS AND ZERO MARKET CAPS SOURCED.** The `move` calls were legitimate rather
  than decorative and bought the shape-seven finding. ⚠ **No §3 cap was sourced for any of
  AVGO/GLW/COHR/TSM/AMKR, so §3 is UNRESOLVED for all five, not passed — DO NOT INHERIT A §3
  VERDICT FROM `T-2026-10-21-01` (the VAL precedent). `AMKR` is plausibly near the $10B floor.**
