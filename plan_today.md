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
plan_date: 2026-10-20
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-20 at 09:30 ET** (`alpaca.py clock` at 08:03:00 ET: `is_open:
false`, `next_open: 2026-10-20T09:30:00-04:00`, `next_close: 2026-10-20T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is **pre-market**, and **both**
`next_open` and `next_close` carry **today's** date, which is the full-session signature
rather than an early close or a holiday. ⚠ **Read off the DATES, not the boolean.**

The plan this run replaced was dated **2026-10-19** — **one calendar day and one trading
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
| Account equity | **$99,604.80** | `sleeves` 08:03, live broker mark |
| Cash | **$30,000.00** exactly | `sleeves` — ~**37th** consecutive unchanged reading |
| Core VOO | **$69,604.795218** · **99.046311231 sh** @ **706.74** avg entry | `positions` 08:03 |
| Core % | **69.88%** | `sleeves`, live-mark basis |
| Satellite | **$0.00 · 0.0% · count 0** | `sleeves` |
| Cash % | **30.12%** | `sleeves` |
| Unrealized P&L on core | **−$395.194781 / −0.565%** | `positions`, against the 706.74 fill |
| VOO live pre-bell | **702.75** | `positions` `current_price`, 08:03 — a **pre-market indicative mark, NOT a close** |
| VOO official 10-19 close | **704.47** | carried from the 10-19 close seat's own `bars` pull; **not re-pulled this run** |
| VOO `lastday_price` | **704.60** | ⚠ **NOT the official close. See the warning below.** |
| §6 5% cap | **$4,980.24** | 99,604.80 × 5%, **with no operand** |

⚠⚠ **DO NOT USE `equity − last_equity`, `change_today` (−0.00263), OR
`unrealized_intraday_pl` (−$183.235675) AS A P&L FIGURE.** All three are built on
`lastday_price`, which reads **704.60** against the official 10-19 close of **704.47**.
⚠⚠ **TENTH CONSECUTIVE SEAT ON THE STALE `lastday_price`, AND THE GAP FLIPPED SIGN AGAIN:
it was −$0.135 yesterday and is **+$0.13** this morning.** ⚠ **The defect is NOT a fixed
offset that could be corrected for — it has now flipped sign on consecutive seats. Never
difference the two.**

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
   `America/New_York` → **2026-10-20, Tuesday, ISO week 43, weekday 2, Monday anchor
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
   **before** any §5 rule was read, per §5's core exemption. ⚠ **ELEVENTH consecutive seat with
   §5 absent rather than passing. The repair machinery has still never been exercised once.**

---

## Sleeve check (§2)

**Core 69.88%, IN BAND** (65–75%), **4.88pp above the lower edge and 5.12pp below the upper.**
`core_in_band: true`, `rebalance_needed: false`.
⚠ **`rebalance_delta: +118.56` is a THIRTEENTH reading and a DISTANCE READOUT, NOT AN
INSTRUCTION.** It is the dollar distance to a perfect 70.00%, driven by VOO's own mark moving
under a fixed share count. **$119 on a $69,605 position is 0.17%.** ⚠ *It is the largest such
reading recorded (prior range $5–$58) and still an order of magnitude inside the band — the
drift is VOO falling 1.72 from its 10-19 close against unchanged cash, nothing else.* **No
rebalance is due and none is queued.**

---

## Intents

### BUY — none

**ZERO BUY INTENTS. This is the output §4 says most research runs should produce, and it is
not a failed run.**

New positions were **permitted** this morning on every gate — breaker inactive,
`new_positions_this_week` **0 of 3**, satellite sleeve **entirely undeployed** ($30,000 and
30.12% of the account in cash), `control.md` notes empty. ⚠ **So the absence of a buy is a
RESEARCH result, not a permission result. Nothing was blocked; nothing qualified.**

**Six theses written, all six rejected** — `T-2026-10-20-01` through `-06`. Where they died:

| ID | Object | Killed by |
|---|---|---|
| `-01` | **3M (MMM) / Amazon** — $6B data-centre optical warrant arrangement | **part 2** (no segment, no figure, no guidance change) · **rule (viii) NEW COSTUME** · rule (iii) split verdict |
| `-02` | **GSEO (Taiwan 3406) / 3M** — the genuine second-order Company B | **§3** — not US-listed. Part 2 would have killed it too |
| `-03` | **Northrop Grumman (NOC)** Q3 | **part 1** — own results; **the figure that moved (EPS) has no supplier chain; sales guidance MAINTAINED** |
| `-04` | **RTX** Q3 | **rule (iii)** — guidance vs CONSENSUS not its own prior · **rule (iv) 6th appearance** · part 1 |
| `-05` | **MKSI / TTMI** — Ophir Optics $650M | **part 1** — merger/divestiture arbitrage is not in §4 · rule (viii) both signs |
| `-06` | Sweep of **twelve** (BAE, GD, GEV, Elbit, Aquirian, Wärtsilä, TSEM/SMTC, Nscale, Samsung Bioepis, AVGO/Docomo, Krakatau, JPM) | disposed as one, **zero drill queries** |

⚠⚠⚠ **THE ONE THING THE OPEN SEAT MUST CARRY FROM THIS RESEARCH, AND IT IS A DEFECT IN THE
OPEN SEAT'S OWN MACHINERY — NOT A LEAD.** `T-2026-10-20-01` is **the first candidate in seven
sessions to reach the §4 priced-in filter**, and it exposed a **sixth defect shape**:
`move --symbol MMM --sessions 5` returned **160.895 → 162.01, +0.69%, `priced_in: false`,
"passes"** — ⚠ **and every close in that window PREDATES the event, because the 3M 8-K landed
after the 10-19 bell. The verdict is arithmetically correct and carries zero information about
the news.** ⚠⚠ **AND THE `revalidate` MECHANISM CANNOT CATCH IT: a `move` call at 09:35 reads
CLOSES, and today's close does not exist at 09:35, so the re-check would return the SAME
+0.69% pass bit for bit. Catching an overnight gap needs a quote-against-prior-close
comparison, which is a different call.** ⚠ **It cost nothing today because the thesis died at
part 2. It becomes a wrong trade the first time a post-bell event produces a writeable part 2.
Only a human may change §4 or `alpaca.py move` — this is open items (1), (2) and (7).**

⚠ **NO `revalidate` LINES EXIST BECAUSE THERE IS NOTHING TO REVALIDATE.** The template asks
for the specific number the open run should re-check against an overnight gap. **With zero BUY
intents there is no candidate, no priced-in figure, and no number.** ⚠ **A `revalidate` line
invented for an empty plan would be the open seat's most dangerous possible inheritance.**

### SELL — none

**§5 has no operand** — zero satellite positions, so rules 5.1–5.4 are **ABSENT, not passing**.
Core VOO is **exempt** by §5 and was struck from the working list before the rules were read.

### REBALANCE — none

Core **69.88%**, in band. See **Sleeve check** above. `rebalance_needed: false`.
⚠ **`rebalance_delta: 118.56` must be RE-COMPUTED at the open seat, not inherited** — it is a
distance to 70.00% on a mark that moves every minute.

---

## Carried from the research — for the open seat

- ⚠ **DO NOT re-litigate any of `T-2026-10-20-01`…`-06`.** All six are disposed with named
  reasons in `research_log.md`.
- ⚠⚠ **MMM IS NOT A DEFERRED LEAD. IT IS A REJECTION.** It died at **part 2** — 3M disclosed
  no segment, no revenue figure and no guidance change, and the "$6 billion" is **a warrant
  vesting threshold, not a purchase commitment**. ⚠ **If the funnel re-serves it today dressed
  as the session's best candidate, that is rule (iv) and the 10-12 RTX warning: a disposed
  reject can arrive as a run's best idea. The answer is already written.**
- ⚠⚠ **A MARGIN OR EPS RAISE IS NOT A SECOND-ORDER CATALYST — NOBODY SUPPLIES MARGIN.**
  `T-2026-10-20-03` (NOC: EPS and segment-margin guidance raised, **sales guidance maintained**)
  is `T-2026-10-15-01` (TSMC: revenue outlook raised, **capex reaffirmed**) repeating in an
  unrelated industry five sessions later. **Apply rule (iii) to the figure the mechanism runs
  on, not to the release.** Expect this shape through the rest of earnings season.
- ⚠ **RTX WILL BE BACK — rule (iv), now at SIX appearances in NINE sessions across FIVE
  distinct disclosures, dead at part 1 every time.** 10-20's arrival is an **earnings print**
  rather than a programme award — **a new disclosure TYPE is still not fresh evidence when the
  kill is structural.**
- ⚠ **GE VERNOVA IS AT THREE APPEARANCES IN SIX SESSIONS** (10-15, 10-19, 10-20) and has died
  on part 2 or part 3 each time. Long-dated energy and merchant-power contracting is a
  **standing feature of this funnel, not a visitor.**
- ⚠⚠ **SECOND CONSECUTIVE SESSION IN WHICH A GENUINE NAMED COMPANY B EXISTED AND WAS NOT
  BUYABLE** (10-19: three §3-dead transactions; 10-20: GSEO, Taiwan-listed, named in 3M's own
  disclosure with a 4.7% equity stake pinning it down). ⚠ **Observation 2 of the 3 the 10-19
  entry asked for. Two sessions is not a finding. It changes nothing today and must not be
  written up as a conclusion.**
- ⚠ **ONE `move` CALL AND ONE MARKET CAP SOURCED, breaking a six-session run of zero — and
  the cap (~$87B for MMM, Perplexity, order-of-magnitude) was NEVER LOAD-BEARING, because the
  thesis died at part 2 above it.** The `move` call was legitimate rather than decorative, and
  what it bought was the defect-shape finding, not a trade.
