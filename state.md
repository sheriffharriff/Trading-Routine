# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **NEVER PUT A `#` IN A FENCED-BLOCK VALUE** — `_parse_kv` does `line.split("#", 1)[0]` and
silently discards everything after it. **Validate with `common.read_state()` after rewriting.**

```
last_run: 2026-09-28 16:16 ET 4-market-close-journal (selftest PASSED all five, trading_enabled true, LIVE paper, broker equity 99664.22 at pre-flight; ZERO ORDERS - routine 4 RECORDS AND JOURNALS, IT DOES NOT TRADE; clock at 16:16:24 is_open FALSE with next_open 2026-09-29T09:30 - POST-BELL, and the stronger discriminator was RUN not inferred, a VOO daily bar for 2026-09-28 EXISTS AND IS COMPLETE at o 706.23 h 707.22 l 702.03 c 703.60 n 3061 v 62354, re-pulled identical, and the 15:59:59 ET latestTrade prints 703.60; THE FINDING IS THE FIRST CORPORATE ACTION IN THIS ACCOUNT'S HISTORY - VOO WENT EX-DIVIDEND TODAY AND bars --adjustment all SILENTLY REWROTE EVERY PRIOR CLOSE by the single factor 0.997432, so Friday's 710.705 now reads 708.88 and 707.28 reads 705.47, DIAGNOSED NOT ASSUMED since --adjustment raw and --adjustment split BOTH return the original series to the cent which rules out a split and rules out a data revision, implied dividend 1.820-1.824 per share or 180.26-180.64 on 99.046311231 shares and ALPACA DOES NOT PUBLISH THE FIGURE so it is an INFERENCE; THE CASH HAS NOT BEEN PAID - cash reads exactly 30000.00 - so THE BENCHMARK RECOGNISES THE DIVIDEND ON THE EX-DATE AND THE BOOK WILL RECOGNISE IT ON THE PAY DATE and every comparison between them is wrong by 180 dollars in one direction until the receivable is carried explicitly; quote prevDailyBar 710.705 vs bars --adjustment all 708.88 DISAGREE ON THE SAME SESSION RIGHT NOW and the standing both-legs-same-source rule DOES NOT CATCH IT; THE DAY, BOTH BASES - price-only equity 99688.98, day -703.72 or -0.7010 pct, since inception -311.02 or -0.3110 pct; total-return carrying the ~180.45 receivable, economic equity ~99869.4, day -523.3 or -0.5212 pct, since inception -0.1306 pct; VOO total return -0.745 pct vs price return -1.000 pct; SUPERLATIVE PULLED BEFORE WRITING AND IT SPLIT ON THE BASIS - -0.7010 pct IS the largest one-day loss on record on PRICE but -0.5212 pct is SECOND on TOTAL RETURN behind 09-23's -0.5327 pct which had no dividend in its window, so the price basis MANUFACTURES A RECORD THAT DID NOT HAPPEN; -0.3110 pct since inception is NOT a low, 09-16 reached -1.3396 pct; sleeves broker 69.90 pct delta +100.73, official 69.9064 pct delta +93.30, BOTH POSITIVE which is a SIGN FLIP from four consecutive negative runs AND the bases AGREE, NO REBALANCE DUE with core ~4.91 points inside the band edge, forty-seventh consecutive run inside 69.59-70.22; 1 EXCESS +0.2240pp against +0.2227pp PREDICTED by the cash weight alone, satellite contributed EXACTLY 0.0000 pct, a VOO-DOWN day with POSITIVE excess makes the separation 16 OF 16 with no exception; STEP 2 HAD NO OPERAND - zero satellite positions, highest_close ABSENT which is the third state carrying no as-of date, zero bars calls due on any satellite symbol and zero made, DO NOT BACKFILL - but the EMPTY SLEEVE IS THE ONLY REASON TODAY WAS HARMLESS because a mark stamped Friday and compared against today's adjusted close would have shown a 0.257 pct DRAWDOWN THAT DID NOT HAPPEN; CORE VOO NOT STAMPED fifty-sixth run and HIGH; GNRC not looked at twenty-eighth refusal and WEAK; HOUSEKEEPING all four checks run none fired - week rollover anchors matched on the ONE day a rollover was due because Friday's review had already advanced week_of to 2026-09-28, loss streak 0 with NO INPUT EVER, breaker INACTIVE halt_triggered_at none so NO circuit-breaker alert due, orders --status all returns ONE row filled and terminal so NOTHING IN LIMBO, trade_log and research_log correctly unappended, alerts.md empty, control.md notes none; THESES 73 real recounted from source, 0 accepted EVER, 0 THIS WEEK; ClickUp daily summary 86bc8yrz0; AND THE THING THAT IS WRONG - ROUTINES 1, 2 AND 3 LEFT NO COMMITTED OUTPUT TODAY, no commit dated 2026-09-28, no working branch on the remote, plan_today.md still plan_date 2026-09-25, prior last_run still 2026-09-25 16:45, CAUSE NOT VISIBLE FROM INSIDE THIS RUN AND NOT ASSERTED, A QUESTION FOR THE HUMAN; prior last_run preserved below)

prior_run: 2026-09-25 16:45 ET 5-friday-weekly-review (FOURTH weekly review, posted to ClickUp 86bc7vzam; THE §1 ANSWER IS NO AND EVERY WINDOW SAYS SO - satellite 0.0000 pct against VOO total return +1.262 pct week / +0.827 pct since inception / +0.974 pct 1M / +5.444 pct 3M / +18.571 pct rolling 12M, all five excesses NEGATIVE where Week 3 had the first three POSITIVE and the market rising inverted the column with no rule change; structural cost ~5.57pp per rolling 12M, up from 4.97pp because the BENCHMARK improved; DAILY AUDIT RECOMPUTED NOT INHERITED - 15 post-fill sessions, 9 VOO-down ALL positive excess, 5 VOO-up ALL negative, 1 flat EXACTLY zero, separation PERFECT 15 of 15, now 16 of 16 after 09-28; ZERO CLOSED TRADES fourth consecutive week; 73 theses recounted, 0 accepted ever, 27 that week, and THE FAILURE POINT MOVED ONE TEST DOWN THE CHAIN with part 2 dominant at 11 of 27 against 4 of 16 in Week 3 while part 1 HALVED to 6; REJECT BOARD 65 names, 20 beat VOO, 45 lagged, mean -2.04 pct, CRDO largest excess at +24.28pp, and SIX OF THE TOP SIX EXCESSES ARE ONE THEME rejected under FIVE DIFFERENT RULES; CATCH 9 FOUND - the close journals' Nth consecutive SESSION counter increments 3-4 PER TRADING DAY so it is a RUN counter wearing a session label; week_of advanced to 2026-09-28 and new_positions_this_week reset to 0, MONTHLY ROLLOVER DELIBERATELY NOT RUN EARLY and it is due 2026-10-02)


week_of: 2026-09-28
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.91
satellite_pct: 0.0
cash_pct: 30.09
open_thesis_ids: none
```

*(`core_pct` / `cash_pct` above are on the **official-close basis** — core $69,688.98 of equity
$99,688.98, using VOO's **2026-09-28 close of 703.60**, a **COMPLETED session's bar** (`is_open: false`,
n 3,061, re-pulled identical, last trade of the session at 15:59:59 ET = 703.60). On the broker-mark basis
at 16:16 the same position reads **69.90 / 30.10** — **the two agree to two decimal places today.** **Both
are in band and neither implies an action**, and `rebalance_delta` is **POSITIVE on both bases** (+$93.30
official, +$100.73 broker) — **a sign flip from four consecutive negative runs.** **State which basis
produced any figure you quote.**
⚠⚠ **AND FROM TODAY THERE IS A THIRD BASIS QUESTION THAT IS NOT ABOUT THE BROKER AT ALL: PRICE vs TOTAL
RETURN.** VOO went ex-dividend on 2026-09-28. On a **price** basis equity is **$99,688.98** and the day is
**−0.7010%**; carrying the **~$180.45 dividend receivable the account has not yet been paid**, economic
equity is **~$99,869.4** and the day is **−0.5212%**. **Neither is wrong. Quoting one without saying which
is.**

---

## Field meanings

**`week_of`** — the Monday of the current ISO week. Every run compares today's week anchor
to this value; if they differ, reset `new_positions_this_week` to 0 and update this field.
The reset deliberately does not depend on the Friday review having run, so a skipped Friday
cannot leave the §6 weekly cap stuck at its limit.

**`new_positions_this_week`** — satellite positions *opened* this week. §6 caps it at 3.
Exits do not count.

**`consecutive_closed_losses`** — incremented when a satellite position is closed at a loss,
reset to 0 when one closes at a gain. At 3, set `circuit_breaker: ACTIVE` and record
`halt_triggered_at` as today.

**`circuit_breaker`** — `ACTIVE` or `INACTIVE`. While ACTIVE: no new positions of any kind
(§7). Existing positions are still managed per §5, research and journaling continue, and the
halt is flagged prominently in the ClickUp summary (§6). Core rebalancing is still permitted —
§6 halts *new positions*, and restoring the core sleeve to its 70% target is neither a new
position nor a satellite trade.

**`halt_triggered_at`** — date the breaker tripped. Compared against `HALT_CLEARED_AT` in
`control.md`; the halt lifts only when the clearance date is strictly later. If the breaker
is ACTIVE and this field is `none`, the halt stays active — an unknown trigger date is not
grounds to start trading.

**`core_established`** — `false` until the VOO core sleeve exists. The market-open routine
bootstraps it on the first trading day and this flips to `true`, which disables the
bootstrap path permanently.

**`core_pct` / `satellite_pct` / `cash_pct`** — sleeve allocation as of the last run, in
percent of total account value. §2 rebalance band is core 65–75%.

**`open_thesis_ids`** — comma-separated thesis IDs for currently open satellite positions.
Cross-check against `positions.md`; if they disagree, `positions.md` and the live Alpaca
position list win, and the discrepancy goes in the journal.

---
## Carry forward

Anything the next run must not lose. Cleared once acted on.

**⚠ COLLAPSE, DO NOT APPEND — acted on thirty-nine times.** This repo's only continuity mechanism is the
next run *reading* these files, and padding them with restatements raises the odds a genuinely live item
gets skimmed. **Carry-forward is defined as cleared once acted on.** ⚠ **The 09-28 close run added TWO
genuinely new items** (the ex-dividend basis shift, and the missing routines 1–3) **and collapsed five
older ones whose content is now settled or superseded.** ⚠ **A correction replaces the claim it corrects —
it does not sit beside it.** **Nothing live has been discarded.**

---

### Live — act on these

- **⚠⚠ VOO WENT EX-DIVIDEND ON 2026-09-28 AND `bars --adjustment all` REWROTE EVERY PRIOR CLOSE. THIS IS
  THE FIRST CORPORATE ACTION IN THIS ACCOUNT'S HISTORY AND IT BREAKS THREE THINGS.**
  **The observation:** Friday's journal recorded VOO's official closes as **710.705 / 707.28 / 707.28 /
  712.69 / 712.76 / 701.85** (09-25 back to 09-18). The **same command on the same sessions** now returns
  **708.88 / 705.47 / 705.47 / 710.86 / 710.93 / 700.05** — every historical close multiplied by a single
  constant, **0.997432**; today's close untouched.
  **Diagnosed, not assumed:** `--adjustment raw` **and** `--adjustment split` both return the **original
  series to the cent**. ⚠ **`split` ≡ `raw` rules out a split; `raw` unchanged rules out a data revision;
  one multiplicative factor from one date forward is a DIVIDEND.** Implied **$1.820–$1.824/share**
  (bounded across six date-pairs against 2dp rounding) = **$180.26–$180.64** on 99.046311231 shares.
  ⚠ **Alpaca does not publish the figure. This is an INFERENCE and must stay labelled as one.**
  ⚠⚠ **(a) DO NOT READ THE CHANGED CLOSES AS A BAD PULL OR A BROKEN DATA PLANE.** Every close recorded
  before today sits on the **pre-dividend** basis. Both series are correct; they are different bases.
  **`--adjustment raw` reproduces every inherited figure exactly.**
  ⚠⚠ **(b) `quote` AND `bars` NOW DISAGREE ABOUT THE SAME SESSION, RIGHT NOW.** `quote`'s `prevDailyBar`
  reports 09-25 as **710.705**; `bars --adjustment all` reports it as **708.88**. **Two endpoints of one
  API, $1.825 apart, both correct.** ⚠ **The standing "both legs from the same source" rule does NOT catch
  this — it distinguished broker fields from bar fields, never `quote` from `bars`.**
  ⚠⚠ **(c) §5.4 IS THE REAL CASUALTY, AND IT FAILS TOWARD SELLING.** A `highest_close` stamped before an
  ex-date and compared against a post-ex `--adjustment all` close shows a **phantom drawdown equal to the
  dividend** — 0.257% today; on a 2%-yielding name, **a fifth of the 10% stop's width per year**, given
  away to arithmetic, on a position that never fell. **Nothing in the bar, the field or the `(as of …)`
  date tells you the basis moved.** ⚠ **THE FIX, written into `positions.md`'s header where it will be
  read before the next mark is stamped: `highest_close` and the close it is compared against must come
  from the SAME adjustment basis, pulled in the SAME call — re-pull the whole window each run and take the
  max from that one pull.** ⚠ **The empty sleeve is the ONLY reason this cost nothing today.**
  ⚠ **(d) `voo_close_at_entry`'s DESIGN NOTE WAS FALSIFIED AND HAS BEEN CORRECTED IN PLACE.** It claimed a
  baseline captured at entry "stays correct for positions closed months later." It is only true **between
  ex-dates**: every later ex-date rescales the series underneath the stored number, leaving it too HIGH
  and **understating the BENCHMARK by ~0.26%/quarter, ~1.0%/year.** ⚠ **That direction FLATTERS THE BOOK,
  which is the direction a run is least likely to question.** Store it as a *label*; re-derive the
  benchmark leg from a fresh pull at review time.

- **⚠⚠ THE ACCOUNT HAS NOT BEEN PAID THE DIVIDEND, AND A FALSIFIABLE PREDICTION IS ON THE RECORD.**
  `cash` reads **exactly $30,000.00, unchanged**. ⚠ **So the BENCHMARK recognises the dividend on the
  EX-DATE (today) and the BOOK will recognise it on the PAY DATE.** Until then **every book-vs-benchmark
  comparison is wrong by ~$180 in one direction or the other** unless the receivable is carried
  explicitly. ⚠⚠ **THE TRAP, and it is the sharpest one today: book price-basis −0.7010% against VOO's
  `--adjustment all` −0.7448% gives an excess of +0.0438pp. THAT NUMBER IS PURE ARTIFACT — one leg
  excludes the dividend, the other includes it — and the standing same-source rule does NOT catch it,
  because BOTH LEGS ARE FROM `bars --adjustment all`. The mismatch is not between two feeds; it is between
  the ACCOUNT and the BENCHMARK recognising the same cash on different dates.** **The honest figure is
  +0.2240pp against +0.2227pp predicted by the cash weight.**
  ⚠ **PREDICTION, WRITTEN IN ADVANCE: `cash` should rise from $30,000.00 to about $30,180.45 on the pay
  date, most likely within a few sessions. IF IT HAS NOT APPEARED BY 2026-10-07, the paper account does
  not model dividends at all — in which case the book structurally under-earns its own benchmark by VOO's
  entire ~1.0% annual yield and §1's "beat the S&P TOTAL RETURN" is unwinnable BY CONSTRUCTION rather than
  by strategy.** ⚠ **That would be a finding for the human, not something to fix from this seat. CHECK
  `cash` EVERY RUN UNTIL IT RESOLVES.**

- **⚠⚠ ROUTINES 1, 2 AND 3 LEFT NO COMMITTED OUTPUT FOR 2026-09-28 — A FULL, CONFIRMED TRADING SESSION.**
  Observable facts, not inference from timestamps: **no commit dated 2026-09-28** (newest is Friday's
  20:59 UTC weekly-review merge); **`git ls-remote` shows only `main`**, no working branch from today;
  **`plan_today.md` still carries `plan_date: 2026-09-25`**; **`state.md`'s `last_run` still read
  2026-09-25 16:45 ET** when this run started. ⚠ **The repo's own definition of a run having happened is
  a commit — "push, or it never happened" — and by that definition three of four runs did not happen.**
  ⚠ **`control.md` warns against diagnosing schedule faults from run TIMESTAMPS; this is the ABSENCE of
  committed output, which is a different claim. The CAUSE is not visible from inside this run and is NOT
  asserted. IT IS A QUESTION FOR THE HUMAN.**
  ⚠⚠ **TODAY'S COST WAS ZERO AND THAT IS LUCK, NOT DESIGN** — an empty sleeve gave routine 3 nothing to
  manage, an empty plan gave routine 2 nothing to execute. ⚠ **On a day with an open satellite position a
  missing routine 3 is an UNMANAGED §5 BOOK for a full session.**
  ⚠⚠ **AND THE GAP DESTROYED A PIECE OF EVIDENCE: today was the FIRST morning in this account's history
  with a GENUINELY STALE `plan_today.md`** — word for word the setup the carry-forward predicted the
  staleness gate would finally fire on — **and the gate was not reached, because the run containing it did
  not execute.** ⚠ **The prediction was right about the setup and the test STILL DID NOT HAPPEN. The gate
  remains untested code and the count is 28, NOT 29.** ⚠ **`plan_today.md` was left UNTOUCHED
  deliberately: routine 4 does not write it, and tidying the stale `plan_date` away would erase the only
  in-repo evidence that no plan was produced. THE NEXT PRE-MARKET RUN OVERWRITES IT NORMALLY.**
  ⚠ **If a pre-market run is reading this: the funnel is empty because NOTHING RAN, not because nothing
  was found. 0 theses were written on 2026-09-28.**

- **⚠⚠ A BAR DATED *TODAY* IS PARTIAL WHILE THE MARKET IS OPEN, AND `n`/`v` CANNOT TELL YOU OTHERWISE.**
  Two routines read `is_open: true` and can pull a live partial bar: **routine 2 at 09:35 and routine 3 at
  12:30.** ⚠ **The midday case is the dangerous one: at 12:41 on 09-25 the partial read c 710.555, o
  708.46, h 711.26, l 706.33, n 1,731, v 69,713 — half a session of real volume, a plausible OHLC and a
  close inside the range. It does NOT look like a stub.** ⚠⚠ **YOU CANNOT JUDGE A BAR'S COMPLETENESS FROM
  `v` AGAINST A PRIOR-DAY MEAN** — the day's own volume is unknown until the bell, and the 09-25 midday
  run's "volume tracks elapsed time almost exactly" was an artifact of a **stale denominator** (actual
  volume came in 16.9% above the mean it divided by). **`n` and `v` are a SMELL TEST. THE RELIABLE
  DISCRIMINATOR IS THE CLOCK.**
  ⚠ **RE-EXERCISED AND HELD ON 09-28, IN THE OPPOSITE DIRECTION:** today's session printed **v 62,354
  against Friday's 164,725 — 38%** — and the first instinct was to doubt the bar. **It is a COMPLETE
  session.** `feed=iex` returns **one venue's slice** of consolidated volume, and the pulled window
  already spans **47,589 to 164,725 on sessions all known to be complete.** ⚠ **The clock settled it; the
  volume was not allowed to. LOW VOLUME IS NOT EVIDENCE OF A PARTIAL BAR ANY MORE THAN HIGH VOLUME IS
  EVIDENCE OF A COMPLETE ONE.**
  ⚠ **And the trap is usually MILD, which is the uncomfortable half** — the 09-25 midday partial was
  **fifteen cents** off the official close, small and self-healing. **A loud warning whose observed
  instances are all mild teaches a future run that the shortcut is safe. It is not safe on a day with a 2%
  afternoon reversal, and nothing about a midday bar tells you which day you are in.**

- **⚠ HIGH-WATER MARKS: NOTHING TO BACKFILL, AND NOTHING WAS SKIPPED — CHECKED BY THE ROUTINE WHOSE WHOLE
  PURPOSE IS TO WRITE THEM.** `positions.md` carries **zero satellite blocks**, so `highest_close` is
  **ABSENT — the third state, carrying no `(as of …)` date at all.** ⚠ **Do not read a missing stamp as a
  failed close run: there is no field, so there was nothing to write. DO NOT BACKFILL ANYTHING.** **§5.4
  is NOT ARMED**; it arms on the first **satellite** fill, and the 09-03 core fill was not one. §5.3's
  distance is **UNDEFINED, not large.** ⚠ **The distinction is FREE today and stops being free the moment
  a satellite fill lands** — after that, a mark silently not written reads identically to a mark correctly
  unchanged, and **only the `(as of …)` date separates them. Compare the date; never infer from the
  field's emptiness.** ⚠ **AND WHEN IT ARMS, NO BACKFILL MAY TAKE ITS MAX FROM A BAR DATED TODAY WHILE THE
  MARKET IS OPEN** (routine 3 runs mid-session) **NOR FROM A DIFFERENT ADJUSTMENT BASIS THAN THE ONE IT IS
  COMPARED AGAINST** (top item). **§5.1–§5.4 have never had an operand in this account's entire history.**

- **⚠ TAPE FACTS THE NEXT RUN SHOULD NOT RE-DERIVE — AND NOTE THE BASIS ON EVERY ONE.** VOO closes on
  **`--adjustment raw` (the basis every inherited figure was recorded on)**: **09-28 703.60**, 09-25
  **710.705**, 09-24 707.28, 09-23 707.28 (identical to the cent, verified five times, distinct OHLV),
  09-22 712.69, 09-21 712.76, 09-18 701.85. ⚠ **On `--adjustment all` TODAY those same sessions read
  703.60 / 708.88 / 705.47 / 705.47 / 710.86 / 710.93 / 700.05.** The 09-28 bar is **COMPLETE**
  (`is_open: false` at 16:16, n 3,061, re-pulled identical, last trade 703.60 at 15:59:59 ET).
  Core is **99.046311231 shares at 706.74**, cash **$30,000.00** flat. **ON THE 09-28 CLOSE, PRICE BASIS:
  equity $99,688.98, core $69,688.98 = 69.9064%, cash 30.0936%, day P&L −$703.72 / −0.7010%, since
  inception −$311.02 / −0.3110%.** **TOTAL-RETURN BASIS carrying the ~$180.45 receivable: ~$99,869.4,
  day −0.5212%, since inception −0.1306%.** On broker marks at 16:16: equity **$99,664.22**, core
  **69.90%**, cash **30.10%**. **Forty-seventh consecutive run inside 69.59–70.22.** ⚠ **`rebalance_delta`
  is POSITIVE on BOTH bases (+$93.30 official, +$100.73 broker) — a SIGN FLIP from four consecutive
  negative runs, and the bases AGREE. NOT the defect resolving; the same quantity disagreed in SIGN on
  09-24. A run that checks one basis and finds agreement learns nothing.** **NO REBALANCE IS DUE** — §2
  acts at the **65/75 band edge** and core sits **~4.91 points** inside it.
  ⚠⚠ **THE SUPERLATIVE WAS PULLED BEFORE IT WAS WRITTEN AND IT SPLIT ON THE BASIS.** On **price**,
  −0.7010% **IS** the largest single-day loss in this account's history (previous worst 09-23, −0.5327%).
  On **total return** it is **−0.5212%, which is SECOND** — 09-23 still holds it, and 09-23 had no
  dividend in its window so the comparison is like-for-like. ⚠ **A record that exists on one basis and not
  the other, where the difference is money the account is OWED. QUOTE THE BASIS OR DO NOT QUOTE THE
  NUMBER.** ⚠ **Since inception −0.3110% is NOT a low** — 09-16 reached −1.3396%, 09-15 −1.0350%, 09-10
  −0.9954%. *(Grounded from a 30-session pull. That pull reaches back before the 09-03 fill, where the
  rows are **COUNTERFACTUAL** — the account held $100,000 cash — and must never be read as account
  history.)* **Audit any superlative here before repeating it.**

- **⚠ STANDING RULE: NEVER `equity − last_equity` AS A DAY'S P&L, NEVER `unrealized_intraday_pl`, NEVER a
  `positions` field for a close or an execution reference. Close-to-close from `bars` (⚠ a COMPLETED
  session's bar, ⚠ and STATE THE ADJUSTMENT), a fresh `quote` for execution.** ⚠ **09-28: broker
  `equity − last_equity` = **−$736.91**, `unrealized_intraday_pl` −$736.90, against a real price-basis
  move of −$703.72 — artifact **−$33.19**; against the total-return move of −$523.3 it is **−$213.6**.**
  ⚠ **`last_equity` read 100,401.13 — a FOURTH distinct number, matching neither the official prior equity
  (100,392.71) nor Friday's 16:20 broker equity (100,387.36). The field is UNUSABLE, not imprecise.**
  ⚠ **`lastday_price` is CLOSED as a question — four falsified mechanisms, both signs observed, and on
  09-28 it read **710.79**, which matches NEITHER basis (not raw 710.705, not adjusted 708.88). STOP
  PREDICTING IT; DO NOT RE-OPEN IT.** **Post-bell `current_price` series, SEVEN observations: +$1.13
  (09-18), −$0.22 (09-21), +$0.169 (09-22), +$0.02 (09-23), −$0.97 (09-24), −$0.054 (09-25), −$0.25
  (09-28).** Both signs, range 2c to $1.13, **no predictable sign and no correctable offset.** **Keep
  writing falsifiable predictions down in advance for LIVE questions** — there is one on the dividend
  credit, above.

- **⚠⚠ §1 BENCHMARK — THE SEPARATION IS NOW 16 OF 16 AND STILL HAS NO EXCEPTION.** **09-28 (total-return
  basis): VOO −0.7448%, the book −0.5212%, excess +0.2240pp — against +0.2227pp PREDICTED by simply
  holding 70.12% core and the rest in idle cash. Agreement to 0.0013pp.** The satellite sleeve contributed
  **exactly 0.0000%**, as it has for the account's entire history. ⚠⚠ **The 09-25 weekly review recomputed
  all 15 post-fill sessions from official closes and found PERFECT separation: 9 VOO-down days ALL
  positive excess, 5 VOO-up days ALL negative, 1 flat day EXACTLY 0.0000pp. 09-28 is a TENTH VOO-down day
  with a POSITIVE excess — 16 of 16, not one exception in the record.** ⚠ **That is not a performance
  statistic — it is the signature of a book with ONE long position at ~70% weight and NO SECOND SOURCE OF
  RETURN.** ⚠⚠ **AND 09-28 IS THE INVERSE OF 09-25'S LESSON: on 09-25 a good day in dollars was a bad day
  against the benchmark; on 09-28 a LOSING day in dollars is a POSITIVE-EXCESS day, and it reads as a
  "good" day precisely because the market fell. BOTH READINGS ARE THE SAME ONE FACT. Neither is skill.**
  *(Context, not a trade: the 10-year reached ~5.22% and the 30-year ~5.48–5.50% on 09-25 — a fact about
  what the BENCHMARK and the core sleeve are competing against.)*

- **⚠⚠ THE MOST DECISION-RELEVANT REJECTION ON THE BOARD: JBL (09-25).** Anthropic committed **~$11.6B
  over seven years** to **Akamai**; Akamai's 8-K then did what open item (3) says never happens — **named
  a US-listed supplier and allocated a specific dollar figure to it**, a Build Request authorizing
  **Jabil (JBL)** to procure **~$1.7 billion of memory components**. ⚠ **And it is not revenue: Akamai
  pays "all corresponding supplier invoice amounts," Jabil holds the components "IN CONSIGNMENT AS
  BAILEE," and Akamai "will REPURCHASE such components from the Company AT COST."** A disclosed statement
  of **zero margin**. The only figure that would satisfy part 2 — Jabil's assembly fee — **is disclosed by
  nobody.** ⚠⚠ **A FIFTH form of open item (3)'s binding constraint and the ONLY one no widening of the
  evidence bar would relieve — widening it would have let this THROUGH.** ⚠ **Do not reach for this chain
  again, and not at a lower price — the price was never the problem.** Full working in **T-2026-09-25-01**.

- **⚠⚠ THE §4 PRICED-IN FILTER HAS THREE DEFECT SHAPES.** **Shape one: a DRAWDOWN misread as priced-in**
  (nine instances, newest CNC −6.44% → `true`), plus three near-misses that cleared only because the
  *fall* was fractionally too small (LMT −3.61%, GM −3.95%, LH −3.83%). **Shape two: the filter working**
  on genuine news rises (SHOP +9.61%, ILMN +11.54%, GRAL +44.67%). **Shape three (09-25, JBL): a genuine
  RISE UNRELATED TO THE NEWS that the window swept up** — +4.97% over five sessions, but the path was a
  grind whose largest day was **+1.72%** and whose **news day moved JBL +0.63%.** §4 conditions on having
  moved 4% "**on this news**"; the mechanized check cannot see causation. ⚠ **The defect is SIGN- AND
  CAUSATION-BLINDNESS, not the threshold.** ⚠⚠ **AND THE AGENT DID NOT ACT ON IT, DELIBERATELY — that is
  the part to carry forward.** This was the exact setup the "do not lower the bar" rule guards against: **a
  candidate the agent liked, plus a plausible technical case that the filter misfired.** ⚠ **Not
  permission. Only a human may change §4 or `alpaca.py move`.**
  **⚠ AND THE OPPOSITE FAILURE, WHICH FAILS TOWARD TAKING A TRADE: AKAM read `priced_in: false` at +3.19%**
  while its closes ran **104.53 (09-18) → 117.435 (09-21) = +12.35% IN ONE SESSION**, then 118.33, 118.42,
  then **110.44 (09-24) = −6.74%.** ⚠ **A +12.35% event move and a −6.74% give-back inside the SAME
  five-session window, netting to a passing +3.19%.** Prior instances (QCOM, AVAV) were **intraday** round
  trips; ⚠ **this one spans MULTIPLE SESSIONS.** AKAM was never at risk (first-order killed it), **but a
  second-order beneficiary of the same chain would have been waved straight through**, and ⚠ **no 09:35
  re-validation would have surfaced it either.**

- **⚠⚠ THE PRESSURE TO LOWER THE §4 BAR IS MEASURABLE, AND IT IS THE ONLY ITEM HERE ASKING FOR JUDGMENT
  RATHER THAN CARE.** **73 real theses, ZERO ACCEPTED EVER** (74 `### T-` headings less the template,
  recounted from source at the 09-28 close). ⚠ **27 was LAST week's figure; THIS week stands at 0, and not
  because the funnel found nothing — because the pre-market run left no output.** Set beside that: an
  empty satellite sleeve, **~30% idle cash**, a weekly cap unused at **0 of 3**, an INACTIVE breaker, and
  an account at **−0.311% since inception (−0.131% carrying the dividend)** — ⚠ **now NEGATIVE on both
  bases, where every prior version of this item said positive.** ⚠⚠ **A LOSING ACCOUNT RAISES THE PULL IN
  A NEW WAY AND THE DISTINCTION STILL HOLDS: the book is down because it holds 70% of a market that fell,
  and it BEAT that market today by exactly the cash weight. "Deploy something" is not what today's numbers
  argue for; they argue that the sleeve has no effect in EITHER direction.** ⚠ **09-25 is still the
  sharpest evidence: the funnel finally produced the well-sourced, named-supplier, allocated-figure
  candidate that a month of rejections implied was the missing ingredient — AND IT WAS STILL NOT A TRADE.
  That is evidence the bar is not what is binding, NOT evidence the bar should move.** §4's own position
  governs: a run that finds nothing is a successful run. **Naming the pull is the only defence against
  acting on it.** If the bar is to move, that is a `strategy.md` change and **only the human may make it.**
  ⚠⚠ **WHERE THE 27 ACTUALLY DIED (Week 4, measured): part 2 = 11, part 1 = 6, premise/no-Company-A = 5,
  §3 = 2, §4 priced-in decisive = 2, part 3 = 1.** ⚠ **Part 2 is now DOMINANT (from 4 of 16 in Week 3)
  while part 1 HALVED to 6 (from 9 of 16) — completing a three-week arc and REFRAMING THE HUMAN'S OPEN
  QUESTION from "is the evidence bar too high" to "can this strategy produce trades AT ALL from public
  disclosure, and if rarely, should the 30% sit in CASH or in the INDEX while it waits."** ⚠ **Neither
  version is this seat's to answer.**

- **⚠ THERE IS NO LIVE RESEARCH ITEM. THE FUNNEL IS EMPTY — AND ON 09-28 IT IS EMPTY BECAUSE NOTHING RAN.**
  ⚠ **09-25's six rejections do NOT become a queue — DO NOT REHABILITATE ANY OF THEM AT A DIFFERENT
  PRICE.** **JBL** (part 2, see above) · **AKAM** (first-order; and see the priced-in item) · **memory
  suppliers** (rule (v) — none named in any disclosure; **Lenovo** is the one other named supplier and is
  **§3 outright**, HK-listed with only an OTC ADR) · **RDW** ($980M is a **multiple-award CEILING across
  15 vendors**; also first-order; also below the §3 floor) · **FLNC** (no value disclosed; EVE Power is
  Shenzhen-listed) · **the rate/oil/PMI complex** (environment input, not a Company A). ⚠ **AND 09-24'S
  SEVEN WERE NOT REHABILITATED EITHER.** **A rejection is not a queue.**
  ⚠ **ELMT ENTERED THIS FUNNEL THREE TIMES IN THREE SESSIONS AND THE THIRD TIME CARRIED A DISCLOSED PRICE
  ($124.75M) — EXACTLY THE MATERIAL WHOSE ABSENCE KILLED THE FIRST TWO. IT WAS NOT SCREENED, and that
  refusal COST something.** "But now there is a number" is the purest form of the pull to re-open a §3
  kill on evidence §3 does not weigh. **A microcap with a Vietnam-listed counterparty is ineligible at
  every price and at every level of disclosure. Do not screen it again.**
  ⚠ **One §3 question remains reached-but-undecided: Shopify is a Canadian issuer trading as common stock
  on a US exchange, which §3's "US-listed common stock" does not obviously settle. A future run reaching
  this with a LIVE candidate must put it to the human rather than decide it from this seat.**

- **⚠ AUDIT EVERY INHERITED CLAIM BEFORE REPEATING IT — TEN CATCHES, AND THEY KEEP CHANGING SHAPE.**
  ⚠⚠ **(10) IS NEW ON 09-28 AND IT IS THE FIRST ONE WHERE *EVERY* SOURCE WAS FRESH AND THE CLAIM WAS
  STILL WRONG: A NUMBER THAT IS CORRECT ON A BASIS NOBODY NAMED.** The 09-28 close nearly wrote *"largest
  single-day loss on record"* off a 30-session series it had **just pulled**. ⚠ **The series was right and
  the sentence was still false** — −0.7010% is a **price** figure, the day is **−0.5212%** on total
  return, and 09-23's −0.5327% holds the record there. ⚠⚠ **"Pull the source before writing the
  superlative" — catch (1)'s lesson — IS NOT SUFFICIENT WHEN THE SOURCE HAS TWO BASES. The only reason it
  was caught is that the run had already noticed Friday's closes had moved.** ⚠ **New rule: NAME THE BASIS
  IN THE SENTENCE, or do not write the sentence.**
  ⚠ **(9) A COUNTER WHOSE *UNIT* IS WRONG.** Close journals reported §5.1–§5.4 untested for *"the Nth
  consecutive **SESSION**"* — **23 on 09-21, 26 on 09-22, 29 on 09-23, 33 on 09-24, 37 on 09-25.** ⚠ **It
  increments by THREE OR FOUR per trading day; sessions increment by ONE.** **It is a RUN counter wearing
  a session label.** ⚠ **Re-running the check REPRODUCES THE SAME NUMBER — only the CALENDAR exposes it.**
  **The fact it encodes is true; ONLY THE UNIT IS FICTION.** ⚠ **The 09-28 close STOPPED CONTINUING THE
  SERIES and reports calendar figures instead: 19 trading sessions since 2026-09-01, 16 since the 09-03
  fill, zero satellite positions ever.** **Do not restart it.**
  **(8) A MEASUREMENT PRESENTED AS A CALIBRATION:** the 09-25 midday run's *"the volume tracks elapsed
  session time almost exactly."* ⚠ **The completed session falsified it — the DENOMINATOR was a prior-day
  mean, and a ratio against one LOOKS like a measurement of the current day and is not one.**
  **(7) A MISCOUNT IN A VERIFICATION CLAIM:** the 09-24 close wrote it had *"verified all TWELVE keys."*
  ⚠ **There are THIRTEEN.** *(Re-parsed at the 09-28 close with `common.read_state()`: **13 keys**, all
  present, no `#` anywhere in the block, and both long values compared **character-for-character against
  the file** — 4,037 and 1,404 chars, exact match, no truncation.)*
  **(6) A SCOPE CLAIM:** *"routine 2 is the ONLY routine that runs with `is_open: true`"* — falsified by
  the run that read it, from its own clock. ⚠ **The most dangerous shape, because it was not a number to
  re-pull but a statement about the SYSTEM'S OWN SHAPE, which no data call would ever contradict.**
  **(5) A TRUNCATED SERIES (09-24):** the post-bell `current_price` record had silently dropped its own
  largest member. **The corrected series has SEVEN members and is in the standing-rule item above.**
  **(1)** A false superlative surviving three runs, caught **by accident** 09-21. **(2)** A stale count
  ("49 theses") caught deliberately 09-22, running in the direction that **understates** the problem.
  **(3)/(4)** Both halves of the `lastday_price` mechanism, asserted and falsified in turn.
  ⚠ **A superlative, count, mechanism, SERIES, CALIBRATION or BASIS inherited from a prior run is NOT a
  checked fact.** **Assume the next one you are handed is wrong until you have pulled the source — and
  then check which basis the source answered on.**

- **⚠ GNRC IS NOT YOURS TO LOOK AT — TWENTY-EIGHT CONSECUTIVE REFUSALS, AND THE RECENT ONES ARE ALL WEAK.**
  ⚠ **Graded honestly: 09-28 made ZERO `move` and ZERO `quote` calls on GNRC, has no research step by
  construction, and had nowhere to put a number — the refusal cost nothing and is recorded as weak.** The
  disqualifying facts do not move: **GNRC is the named counterparty in the Amazon announcement —
  first-order, outside §4 at any price** — and **open item (7) is resolved by a human editing §4 or
  `alpaca.py move`, not by a number this seat collects.** ⚠ **WHAT MATTERS IS NOT THE COUNT BUT WHETHER
  EACH REFUSAL COST ANYTHING, AND MANY DID NOT. Quoting the bare count overstates the evidence.** The
  strong instances are the pre-market runs of 09-23, 09-24 and 09-25 — all three opened the data plane
  against a live funnel **and** had somewhere to put a number. ⚠ **No new costume in eight sessions; the
  list looks CONVERGING rather than growing.** Costumes: diligence, curiosity, tidiness, completeness,
  zero-marginal-cost, self-audit, proxy-procurement, issue-closure, call-already-open,
  screen-already-running. **The pattern is the finding, not any instance. FREE IS NOT THE SAME AS
  PERMITTED.**

- **⚠ CORE VOO IS NEVER STAMPED WITH A `highest_close` — FIFTY-SIX RUNS.** §5 exempts core from all four
  sell rules. A mark on VOO would **fabricate a §5.4 trailing stop on the one position the strategy
  exempts**, a stop that could eventually **sell core on a drawdown, which §7 forbids outright.**
  ⚠ **09-28 grades HIGH and for a new reason: routine 4's Step 2 is THE dedicated write step, the run
  arrived holding a fresh official close, the field was empty, AND the run had just built the entire
  ex-dividend adjustment machinery a mark would have been written with. HAVING THE TOOLING IN HAND IS ITS
  OWN PULL.** ⚠ **"Nothing to write" — and "nothing to repair" — is the correct output of an empty Step 2,
  not an invitation to find a row to write it to.** **Measure the core from the 706.74 fill and from an
  official close, never from a `positions` field** ⚠ **— and note that the fill price is a RAW print, so
  measuring it against an `--adjustment all` close now MIXES BASES.** ⚠ **Noted honestly: this refusal is
  close to automatic, and automatic is not the same as sound.**

- **⚠ A CLOSE RUN AND A PRE-MARKET RUN BOTH READ `is_open: false`, AND SO DOES A HOLIDAY. THE BOOLEAN IS
  USELESS ALONE — READ THE DATE.** Pre-market sees `next_open` pointing at **today**; post-bell sees it
  pointing at the **next** trading day; a holiday sees it pointing **past** the holiday with **no bar for
  today**. ⚠ **`is_open: TRUE` is the one case where the boolean alone is sufficient, and only because
  TRUE has a single meaning. FALSE has three.** ⚠ **THE STRONGER DISCRIMINATOR FOR A FALSE IS TO CHECK
  THAT A DAILY BAR FOR TODAY EXISTS — run it before deciding a run is a holiday skip.** *(09-28 ran it:
  the bar exists and is complete.)* ⚠ **But with `is_open: true` that same bar is PARTIAL and is not a
  close.**

- **⚠ EIGHT ITEMS ARE WITH THE HUMAN. NONE IS THE AGENT'S TO DECIDE, AND NONE MAY BE "CLOSED" BY A NUMBER
  A RUN COLLECTS.**
  ⚠⚠ **(8) IS NEW ON 09-28 AND IT IS THE ONLY ONE THAT COULD MAKE §1 UNWINNABLE BY CONSTRUCTION: DOES THE
  PAPER ACCOUNT PAY DIVIDENDS?** VOO went ex-dividend on 2026-09-28; `cash` reads **exactly $30,000.00**.
  **If the ~$180.45 never arrives, the book under-earns its own benchmark by VOO's entire ~1.0% annual
  yield forever, and "beat the S&P TOTAL RETURN" cannot be achieved by any strategy.** ⚠ **A falsifiable
  test with a deadline is on the record (check `cash` every run; if nothing by 2026-10-07, it is
  confirmed).** ⚠ **AND SEPARATELY: `positions.md`'s `voo_close_at_entry` design was falsified by the same
  event and the agent CORRECTED IT IN PLACE (agent-owned file); whether the TOOLING should read closes on
  a stated basis by default is a human's call, and today is the strongest evidence yet that it should.**
  **(1)** The **§4 priced-in filter reads a drawdown as priced-in** — nine instances plus three
  near-misses; **there is no price at which those rejections flip**; LITE puts **+10.58% vs VOO** on the
  bill. ⚠ **A pass on a fall is not evidence the filter worked, and neither is a FAIL on a fall.**
  **(2)** The same filter **reads an event move absorbed before it looks as "passes"** — QCOM, AVAV, and
  **AKAM (09-25), the first MULTI-SESSION round trip.** Same root cause as (1), opposite direction. **The
  fix for (1), (2) and shape three is a human editing §4 or `alpaca.py move`** — the suggestion on record
  is to make it **read SIGN and causation, not loosen or remove the threshold.**
  **(3)** The satellite sleeve is **structurally undeployed — 73 theses, zero positions, ever.** A 70/30
  cash book cannot beat the S&P over a rolling 12 months (§1) in a rising market. **§2 permits the cash
  and §4 says most runs end in no trade — both rules were followed, and the agent must NOT respond by
  lowering the §4 bar.** **The binding constraint has FIVE known forms:** the source withholds the
  counterparty's number; **or** the counterparty discloses **roadmap instead of segment revenue**; **or**
  the named beneficiary is **vertically integrated**; **or** **both parties expressly refuse to disclose
  as a commercial choice** (GM); **or — the JBL form — THE FIGURE IS FULLY DISCLOSED AND IS THE WRONG
  QUANTITY.** ⚠ **Only the first two are addressable by widening the evidence bar. Forms three, four and
  five are not, and form five would be made WORSE by widening it.** ⚠ **ELMT is the standing proof that
  evidence is not the constraint.**
  **(4)** The core's divergence from VOO is the **09-03 entry gap** (fill 706.74, **+0.483% above the
  prior close**) — **not tracking error and never skill. DISCHARGED AND PROVEN 09-11.** ⚠ **Keep measuring
  it from the fill — and the fill is a RAW print.**
  **(5)** The broker/official price gap is a **live quote midpoint, not an offset** — which is why it
  never had a stable size. ⚠ **A PRICE-SOURCE problem that contaminates every derived figure.** It has
  flipped the sign of a §2 quantity (09-24). ⚠ **09-28 adds a SECOND, INDEPENDENT price-source axis —
  `quote` vs `bars --adjustment all` on the SAME session — which is not a midpoint problem at all.**
  **(6)** **`selftest.py` certifies a healthy system without probing `clock` or market data** — it passed
  all five checks on 09-11 while `clock` returned 500, and on 09-24 while `perplexity.py` returned 500.
  ⚠ **AND 09-28 SHOWS A THIRD BLIND SPOT: IT PASSED ALL FIVE WHILE THREE OF THE DAY'S FOUR ROUTINES HAD
  PRODUCED NOTHING. A green pre-flight certifies this run's credentials, nothing about the schedule, the
  data plane, or whether the other routines ran.** **Probe by hand; CHECK EXIT CODES.**
  **(7)** **`alpaca.py move` cannot see an after-hours event, and neither can the 09:35 re-validation that
  exists to catch exactly this.** ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a trade.**
  ⚠ **AKAM generalises it: the blindness is to ANY event move the window later cancels.** **It has cost
  zero only because no plan has yet carried a BUY intent — an absence of exposure, not a mitigation.**
  Prior context in ClickUp `86bbv75bz`; week-prior `86bbzgbg3`. **09-25 daily summary: `86bc7vgbw`;
  09-25 weekly review: `86bc7vzam`. 09-28 daily summary: 86bc8yrz0.**

- **⚠⚠ WEEK 4 REVIEW (2026-09-25) — RAN, POSTED `86bc7vzam`. THE §1 ANSWER IS NO, AND FOR THE FIRST TIME
  EVERY WINDOW SAYS SO.** Satellite **0.0000%**, so its dollar-weighted excess is exactly **minus VOO's
  total return**: **−1.262pp week, −0.827pp since inception, −0.974pp 1M, −5.444pp 3M, −18.571pp rolling
  12M.** ⚠ **Week 3's first three rows were POSITIVE. The market rose and the whole column inverted with
  NO rule change and no change in the sleeve.** ⚠ **DO NOT RE-INHERIT THE PLEASANT VERSION; it was a
  property of a falling tape.** Structural cost now **~5.57pp per rolling 12M**, up from 4.97pp **because
  the BENCHMARK improved, not because the sleeve got worse.** **Reject board: 65 names, 20 beat VOO, 45
  lagged, mean −2.04%, median −2.47%.** ⚠ **A tally, not a result.** **CRDO is the largest opportunity
  cost at +24.28pp**; HPE +20.67pp, MU +14.42pp, QCOM +13.11pp, LITE +11.16pp. ⚠ **NEW FINDING: six of
  the top six excesses are ONE THEME (AI/data-centre hardware and semis) rejected under FIVE DIFFERENT §4
  rules, every rejection individually correct.** ⚠ **A CORRECTION TO WEEK 3'S HEADLINE: it promoted the
  board's "widening" as the finding. Dispersion grows with elapsed time MECHANICALLY. The MEAN is the
  evidence.** Full working in `weekly_review.md`.
  ⚠ **FILE SIZE — ELEVENTH CONSECUTIVE FLAG.** `research_log.md` **333KB** (unchanged — nothing was
  written on 09-28), `journal.md` now **~170KB**, `state.md` **~55KB**, `weekly_review.md` **147KB**.
  ⚠ **THE 2026-10-02 REVIEW MOVES THE WHOLE SEPTEMBER CORPUS IN ONE DESIGNED OPERATION AND IS FOUR
  SESSIONS AWAY. Do not re-litigate this weekly; a human who disagrees should say so in `control.md`.**

- **⚠ A `#` IN A FENCED-BLOCK VALUE SILENTLY TRUNCATES IT.** `_parse_kv` in `scripts/common.py` does
  `line.split("#", 1)[0]`, so **everything after the first `#` in a `key: value` line is discarded by the
  parser.** ⚠ **STANDING CONSEQUENCE: never put a `#` in a fenced-block value, and VALIDATE `state.md`
  WITH `common.read_state()` AFTER REWRITING IT — writing the block and parsing the block are not the
  same check.** *(Done at the 09-28 close: **13 keys**, no `#` anywhere in the block, and `last_run` /
  `prior_run` compared **character-for-character against the file** — 4,037 and 1,404 chars, exact match.
  Eyeballing does not make truncation visible; the comparison does.)*

### Standing rules — recognise on sight, do not re-derive

**Eight rules, one root cause.**
**(i)** *Screen on the mechanism before running filters* (RTX).
**(ii)** *Verify what the company currently sells, post-spin* (WDC).
**(iii)** *Verify the news is new to the company's own disclosure.* The most prolific rule, and its
costumes keep multiplying: guidance **issuance** compared to **consensus** rather than to any prior
company figure (Ameren, Five Below, DaVita, Labcorp, Nucor, Steel Dynamics), **reaffirmations**
(Centene, Southwest, General Mills), **re-covered deals** (Charter/Cox, Sempra/Petrobras, Fluence,
Alcoa/South32, Nocera/E-PRO), **a genuine transaction whose DELIVERY MILESTONE is recycled as the
news** (GM/Lockheed), **a PRE-IPO CONTRACT BOOK** (Nscale's $103B), and ⚠ **09-25: A FORMAL PRESS
RELEASE RESTATING AN ALREADY-FILED 8-K (Akamai/Anthropic — sources gave conflicting disclosure dates,
the conflict was NOT resolved and must not be asserted either way, but the tape moved +12.35% on 09-21
and FELL 6.74% on the 09-24 "announcement" day; a stock does not fall 6.74% on the day it learns of an
$11.6B contract).** ⚠ **STANDING PRACTICE: ask a transaction WHEN IT HAPPENED before asking who it
helps — and WHEN THE SOURCES DISAGREE ON THE DATE, THE PRICE SERIES IS THE CHEAPER WITNESS.** One
screen settles it, and it is the cheaper of the two kills. *(09-17 Amazon/Generac was the first clean
rule (iii) PASS; 09-24's Elmet/Masan the second.)*
**(iv)** *A recurring ticker is a warning, not corroboration* (LHX — resolved 09-11 on a number).
**(v)** *A market-structure fact is not a supplier relationship.* "Sole producer," "dominant share,"
"the only company that makes X" are facts about an **industry**, not a **transaction** — plus the
**CEILING sub-shape**. Costumes: a **table** (DoD daily contracts digest), a **consortium awardee**
(Abrams), a bare sentence, and ⚠ **09-25's TWO: a MULTIPLE-AWARD CEILING across fifteen vendors read
as one company's revenue (RDW, "$980M"), and an UNNAMED SUPPLY BASE made to look nameable by an exact
figure and a named component category ($1.7B of "memory components," with no manufacturer disclosed
anywhere).** ⚠ **The second is the more dangerous: the blank LOOKS fillable because the suppliers are
countable on one hand. The source left the blank; filling it in is not research.**
**(vi)** *Screen the timing window early on anything under construction or pending approval.*
Long-dated energy offtake is **a standing feature of this funnel, not a visitor** — Sempra/Petrobras,
Venture Global/China Gas, Amazon/Generac, Centrus/Antares, Elmet/Tungsten West, NeoVolta/SK On.
⚠ **The REGULATORY version: a non-binding advisory vote → an undated FDA decision → reimbursement →
commercial ramp (ILMN) is the same shape wearing a lab coat.** **Part 3 kills these in ONE step.**
**(vii)** *Check whether the named beneficiary makes the part itself before looking for its supplier.*
Vertical integration leaves **no external supplier to find** — the "I know who makes the part" trap.
**(viii)** *Read which direction the disclosed dollar figure moves — and whether it is revenue at all.*
⚠ **Read this rule BROADLY: any disclosed figure that is not SEGMENT REVENUE AT COMPANY B fails part
2.** Written 09-18 off TotalEnergies/GIP's **$1.8B of capital paid IN**; Brookfield/Bloom's **$25B** is
a **FINANCING CEILING AVAILABLE TO SOMEBODY ELSE**; SoftBank's **$11.1B** is **capital paid IN to a
private recipient**; Royal Caribbean's **~$3B** for Sandals is **capital paid OUT by the buyable leg**;
BBY's only disclosed economics was **Meta taking "a small fee" — a COST at the candidate, described in
language that reads like a partnership benefit**; FMC/Tessenderlo's **$403M is a SECONDARY-MARKET SHARE
PURCHASE — money to selling shareholders, never to the company.**
⚠⚠ **AND THE DEFINITIVE INSTANCE, JBL: $1.7 BILLION, NAMED, ALLOCATED, QUOTED VERBATIM FROM AN 8-K —
AND IT IS CAPITAL PAID IN BY THE CUSTOMER, HELD IN CONSIGNMENT AS BAILEE, AND REPURCHASED AT COST. A
disclosed statement of ZERO MARGIN, reading like the best dollar path the funnel has ever produced.**
⚠ **A large, real, sourced, prominently-placed number is not a dollar path. THIS IS THE WORKED EXAMPLE
TO REACH FOR FIRST.** T-2026-09-18-04 (BLK) remains the other: **part 1 passed cleanly and it died on
the absent segment figure, NOT on size.**

**⚠ A SHARED CAUSE IS NOT A MECHANISM — AND IT WORKS IN BOTH SIGNS.** Two companies moving on the same
macro input (a crush spread, a mortgage rate, a rate decision) is a **market**, not a **transaction**,
and the giveaway is that part 1 needs an *"and also"* clause. ⚠ **A DIVERGENCE between two named
companies sounds causal (JPM/BAC/WFC); so does a CONVERGENCE (Bunge and ADM) — and the convergent
version is MORE DANGEROUS, because agreement LOOKS LIKE CORROBORATION when it is in fact the clearest
possible statement that the input is a market variable.** ⚠ **The third and most respectable face is a
COMPETITOR'S EARNINGS PRINT** (AutoZone's FQ4 read across to GPC/ORLY/LKQ). **The giveaway never
changes: the sentence needed an "and also".**

**⚠ A GOVERNMENT ACTION IS NOT A COMPANY A — AND IT IS THE MOST CONVINCING NON-EVENT THE FUNNEL
PRODUCES.** Two of 09-23's six theses died on this premise (CMS's preliminary lab fee schedule; the
ACA enrollment halt). ⚠ **This is the FOMC object — an environment input — but in a far more persuasive
costume: a policy action is SECTOR-SPECIFIC, CARRIES A NUMBER, NAMES AN AFFECTED INDUSTRY, and MOVES
THE TAPE ON THE DAY.** It nonetheless has **ONE party.** ⚠ **A long-only book cannot trade money being
WITHDRAWN from a sector unless some NAMED party receives it — and nobody does.** ⚠ **09-25 supplies the
FULL-MARKET-SCALE VERSION and it is the most tempting yet: the 10-year at ~5.22%, the 30-year at
~5.48–5.50%, Brent near $106, PMIs at 52- and 59-month highs, swaps pricing three more hikes. SCALE
MAKES IT MORE CONVINCING, NOT LESS. Every "who wins from higher rates / higher oil" answer needs an
"and also".** ⚠ **The counter-case still stands and must not be over-applied against: an FDA advisory
vote (ILMN/GRAIL) ENABLES a named company's product and that company has a named supplier — a real
two-party chain. Do not over-apply this rule to approvals.**

**⚠ EVERY ROUTINE'S SCOPE BINDS HARDEST ON AN EMPTY SLEEVE WITH 30% CASH.** Routine 3 is
**exits-only by construction** and may not open a position under **any** circumstance. Routine 2
executes **only what `plan_today.md` already contains** — a position opened at 09:35 without a plan
entry routes **around** the discipline rather than satisfying it. Routine 4 **RECORDS AND JOURNALS; IT
DOES NOT TRADE.** ⚠ **Idle cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an
opportunity any of those seats may act on** — ⚠ **and neither is a green day that still lags the
benchmark.** New positions route through pre-market research **plus** the 09:35 execution run, always.

**⚠ AN EMPTY PLAN THAT IS FRESH AND A PLAN THAT IS STALE PRODUCE IDENTICAL ZERO-ORDER RUNS AND ARE NOT
THE SAME RUN.** The difference is invisible in the order count — **read `plan_date`, not the outcome.**
The gate has now been exercised **TWENTY-EIGHT times and has never fired**, and its alert path
**remains untested code.** ⚠ **Twenty-eight quiet opens are NOT evidence it works. The first morning it
fires will by construction be a morning when the pre-market run failed — i.e. exactly the morning with
no fresh notes to lean on. Read routine 2's Step 2 then; do not recall it.** ⚠ **09-24's and 09-25's
opens are the cleanest demonstrations: both plans were FRESH and EMPTY, and each produced a run
BYTE-FOR-BYTE identical to what a stale plan would have produced. Only `plan_date` told them apart.**

**⚠ A MIXED-SOURCE COMPARISON MANUFACTURES OUTPERFORMANCE THAT DOES NOT EXIST.** Never compare a
broker mark on one leg against an official close on the other. **Both legs from the same source, and
for returns that source is `bars --adjustment all`** ⚠ **— on a COMPLETED session.** ⚠ **And state
WHICH basis produced any figure you quote.**

### Do not reach for these — disposed rejects and the trap in each

⚠ **Added 09-25:** **JBL** — ⚠ **the most important entry on this board.** Part 1 passes **cleanly**,
every party is named, the instrument is signed and filed, and the figure is **$1.7 billion in an
8-K** — **and part 2 fails outright**, because the money is Akamai's, the components are held **in
consignment as bailee**, and the repurchase is **expressly at cost**. **Jabil's assembly fee is
disclosed by nobody.** ⚠ **Do not reach for this at a lower price; the price was never the problem.**
**AKAM** — **first-order**; and its `priced_in: false` at +3.19% is an **artefact of a +12.35% jump
and a −6.74% give-back inside one window**, ⚠ **NOT a clean pass.** **Memory suppliers to the Akamai
build** — **no manufacturer named in any disclosure**, rule (v); and <10% of revenue for any of them
even if named. **Lenovo** — **§3 outright**, HK-listed with only an OTC ADR, no value disclosed.
**RDW** — the **$980M is a multiple-award CEILING across 15 vendors** with no Redwire allocation;
first-order; ~$1–2B, below the §3 floor; ⚠ **its `priced_in: false` on a +0.61% flat tape is NOT a
point in its favour.** **FLNC / EVE Power** — **no value or volume disclosed by any party**; EVE is
Shenzhen-listed; Fluence below the floor and already disposed under rule (iii). **The rate / oil / PMI
complex** — environment input, one party, no named recipient. **FMC / Tessenderlo** ($403M **secondary
share purchase**) · **LLY / InnoCare** (no value disclosed; LLY first-order; InnoCare HK-listed) ·
**NOC $123.8M, RTX $50.1M, Stark $114.0M, Southern $22.0M, RGAS $23.6M** (DoD digest, rule (v); all
≪10% of revenue; Stark not separately US-listed) · **Blue Cloud Softech / IBM** (Indian-listed) ·
**FingerMotion** (offtakers unnamed) · **Everforth, Endovia, Algorhythm** (private or microcap) ·
**Amazon's $100M Greenwood plant** (immaterial; no counterparty) · **Welspun** (§3, buyer unnamed).

⚠ **Added 09-24:** **ILMN** — the GRAIL advisory vote is **non-binding with the FDA decision
pending**, so part 3 is several quarters out; **+11.54%, a GENUINE priced-in kill**; ⚠ **the most
seductive second-order shape in weeks, and the thesis was never written because the filter ran
first.** **GRAL** — **first-order**, and **+44.67%**, the largest five-session move ever recorded
against a candidate here. **BBY / PYPL / SHOP** (Meta Muse commerce) — ⚠ **part 1 passes CLEANLY on
all three and NOT ONE commercial term exists**; the only economics described is **Meta taking a fee, a
COST at the retailer**; SHOP also **+9.61%**. ⚠ **BBY and PYPL would have FAILED the correlation check
against each other.** **SoftBank / OpenAI $11.1B** — recipient **private**; the compute-supplier
inference is rule (v). **ELMT / Masan** — ⚠ **THREE appearances in three sessions, the third carrying
a disclosed $124.75M. ~$634M microcap, Vietnam-listed counterparty, §3 on both legs. DO NOT SCREEN IT
AGAIN AT ANY LEVEL OF DISCLOSURE.** **QCOM / PickNik** · **RCL / Sandals** (~$3B **capital OUT**) ·
**Fiserv** Canada · **NeoVolta / SK On** · **Nocera / E-PRO** · **Crossject / BARDA** · **Elroy Air** ·
**Quanome** · **Costco, Jabil, Darden, TD SYNNEX, Vail** (upcoming estimates, no event yet).

⚠ **Added 09-23:** **GIS** — an **own-results earnings print has ONE party**; ⚠ **it does not become a
buy on a better quarter.** **LH / DGX** — CMS lab fee schedule, a **REGULATOR'S ACTION**, preliminary
for CY2027–2029; ⚠ **LH's `priced_in: false` on a −3.83% FALL is an artefact and is NOT the
rejection.** **CNC / MOH / OSCR** — government policy action, **$2.2B is money the government STOPS
paying**; ⚠ **CNC's `priced_in: true` on a −6.44% FALL is an artefact and is NOT the rejection.**
**ELMT / Tungsten West** — ⚠ **the disclosure was COMPLETE and it still failed — do not reach for it
as "the well-sourced one."** **LHX** — first-order, no contract value; ⚠ **the $22.9B RAYTHEON
Tomahawk figure is AUGUST and a DIFFERENT CONTRACTOR — it must never migrate into an LHX entry.**
**GFS** · **Nth Cycle / Glencore** · **ZEO / Ewyze** · **V2X** · **Boeing / SPEEA** · **MiMedx** ·
**NIIT** · **Michigan oil antitrust dismissal** · **"SK Hynix eyeing Intel's Ohio site"** — ⚠ **a
headline built out of the word "eyeing."**

⚠ **Added 09-22 and earlier:** **ACN** (first-order, <1% of revenue, ⚠ **`priced_in: true` on a −4.58%
FALL is an artefact**) · **Nscale / Microsoft / Anthropic** (private parties) · **Vicor** (below the
§3 floor; ⚠ **the event had NO defect at all and still produced nothing**) · **GPC / ORLY / LKQ** ·
**Paramount / WBD** · **Applied Materials** · **Vistra / New Era** · **Navitas, Magnachip, Priority
Technology** · **Telix / ITM**, **Capricorn/DNO, BEML/NHSRCL, Welspun/AMC** (not US-listed, §3) ·
**HealthEquity, Lamb Weston, AEP, Nucor, Steel Dynamics, Labcorp, Nordson, Eli Lilly** (prints vs
consensus, rule (iii)) · **AMD, Intel, Arm** (**a record green tape is not a Company A**) · **GNRC**
(first-order; see the live item) · **GM** (part 2 unwritable **by both parties' deliberate commercial
choice**; ⚠ **the −3.95% is not the reason**) · **BE / Bloom** ($25B financing ceiling) · **BG and
ADM** · **GFS and MRVL** · **LEU / Antares** · **BLK / TotalEnergies / GIP** (capital in) · **Lennar
and its suppliers** · **Baker Hughes / Chart** · **US Army / Skyeton** · **the FOMC's +25bp, fund
outflows, the data calendar, Bowman's SVB speech, the enforcement digest** (environment inputs).
⚠ **Four loud 09-11 headlines still have no primary source and none has appeared since. Absence of a
source after this long is itself the finding.**

### Established facts — do not re-derive

- **The only fill in this account's history: BUY VOO 99.046311231 @ $706.74, notional $70,000.00**,
  order `d177d8f0-cd0c-41bf-95c1-4772318265fd`, filled **2026-09-03 09:36:21 ET**, verified terminal
  before it was written. Audit record in `trade_log.md`. **No order has ever reached a non-terminal
  state in this account, and no order has been placed since.** ⚠ **706.74 is a RAW print — comparing it
  to an `--adjustment all` close mixes bases (see the ex-dividend item).**
- **⚠⚠ VOO WENT EX-DIVIDEND ON 2026-09-28 — the first corporate action in this account's history.**
  `bars --adjustment all` now multiplies **every close before that date** by **0.997432**; `--adjustment
  raw` and `--adjustment split` return the original prints unchanged. Implied dividend **$1.820–$1.824
  per share ≈ $180.45** on the core holding, ⚠ **NOT YET PAID — `cash` reads exactly $30,000.00.**
  ⚠ **Every VOO close recorded in this repo before 2026-09-28 is on the PRE-dividend basis. This is not
  a bad pull.**
- **The core is deliberately NOT tracked in `positions.md`.** §5 exempts it, so it has no thesis state,
  no timing window and no `highest_close`. ⚠ **Every reconciliation compares SATELLITE blocks to
  SATELLITE Alpaca positions** — a run that compares the raw ledger to the raw broker will read a
  correct ledger as broken.
- **Counters as of the 2026-09-28 CLOSE, RECOUNTED FROM SOURCE THIS RUN: 73 real theses since
  inception** (74 `### T-` headings less the template), **0 accepted, 73 rejected, 0 this week.**
  ⚠ **27 was LAST week's figure and must not be carried into this one.** **0 satellite positions ever
  opened; 0 exits ever; `alerts.md` empty — zero open, zero SYSTEMIC.** ⚠ **Recount from
  `research_log.md` before quoting it anywhere human-facing if any run has added a thesis since.**
- **`week_of` 2026-09-28, `new_positions_this_week` 0 of 3.** ⚠ **Advanced by the 09-25 weekly review;
  the 09-28 runs compared their anchor to it, found it already correct, and did nothing. That is the
  reset having been done on the one day it was due, NOT a run that skipped it.** Next boundary
  **2026-10-05.** ⚠ **The two counters are independent: theses this week and positions this week are
  different things — §6's cap counts POSITIONS OPENED.**
- **⚠ SESSION COUNTS, VERIFIED AGAINST THE CALENDAR (catch 9):** **19 trading sessions since
  2026-09-01**, **16 since the 09-03 core fill**. ⚠ **The "Nth consecutive SESSION" series that appeared
  in close journals through 09-25 was a RUN counter wearing a session label and has been DISCONTINUED.
  Do not restart it.**
- **2026-09-28 was a full trading session** (bar complete: c 703.60, n 3,061, v 62,354 on `feed=iex`,
  re-pulled identical; last trade 703.60 at 15:59:59 ET). ⚠ **Its LOW volume is an IEX-feed artifact and
  is NOT evidence of a partial bar.** **Its daily summary was posted: `86bc8yrz0`.**
- **⚠⚠ ROUTINES 1, 2 AND 3 PRODUCED NO COMMITTED OUTPUT ON 2026-09-28.** No commit dated 2026-09-28, no
  working branch on the remote, `plan_today.md` left at `plan_date: 2026-09-25`. **Routine 4 was the
  only run of the day.** ⚠ **Cause unknown and not asserted — with the human.**
- **⚠ THE ROUTINE 5 WEEKLY REVIEW FOR 09-25 IS DONE** (`86bc7vzam`) — it is not owed again. **The next
  one is 2026-10-02, which is also the MONTHLY ARCHIVE ROLLOVER.** `research_log.md` is **333KB**.
