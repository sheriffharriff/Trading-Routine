# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

```
last_run: 2026-09-02 16:15 ET 4-market-close-journal
week_of: 2026-08-31
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: false
core_ticker: VOO
core_pct: 0.0
satellite_pct: 0.0
cash_pct: 100.0
open_thesis_ids: none
```

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


- **CLOSE 2026-09-02 16:15 ET: the day is complete and nothing is unresolved.** Market was open and
  closed normally (`is_open: false`, `next_open: 2026-09-03 09:30 ET`) — a normal post-close run,
  **not a holiday skip**. Equity $100,000.00, `last_equity` $100,000.00, day P&L exactly $0.00
  (0.00%), since inception 0.0%. `positions` returned `[]` for the tenth consecutive run. Journal
  entry written for 2026-09-02; ClickUp daily summary posted as task **`86bbtvf94`**.
  **`alpaca.py orders --status all` returned `[]` — no order exists in any state, so nothing is
  carried into tomorrow in limbo (§7).** Nothing closed today, so `consecutive_closed_losses` stays
  0 and the breaker could not have tripped.

- **⚠ THE HIGH-WATER PASS RAN AND HAD NO SUBJECT — do not backfill tomorrow.** This is the close
  run's invisible job and the reason the routine exists, so it is recorded explicitly rather than
  left to inference: zero position blocks means zero `highest_close` fields and zero `(as of ...)`
  dates, so there was nothing to write and nothing to stamp. **The §5.4 trailing stop is not
  silently disabled — it is not yet armed**, and it arms the day the first satellite position
  opens. A `bars` backfill has no input; running one would repair nothing. **Ten runs across two
  trading days have each recorded this distinction rather than assume it carried.** Note also the
  near-miss logged in today's journal: after ten empty runs the pass starts to feel ceremonial, and
  the first day it actually matters is the day *after* the first fill, when ten runs of habit will
  say there is nothing there. Read the emptiness as verified, not as skipped.

- **⚠ `TRADING_ENABLED: false` — day three, and today is the day the cost stopped being
  hypothetical.** The account is still 100% cash and the core sleeve still does not exist. Only a
  human can close this, in `control.md`. Read it as **configured behaviour, not a fault**:
  `control.md` describes the dry run in its own words as a way to "watch the system think for a
  week before it touches the account," and today is day three of that week. The 09:36 ET open run
  submitted the §2 bootstrap exactly as planned and got `{"ok": true, "dry_run": true, "reason":
  "TRADING_ENABLED is not true in control.md"}`, exit 0, no order — logged under `trade_log.md` →
  *Dry-run intents*, not as a fill. **Do not raise a ClickUp alert for this and do not let a run
  treat the reappearing intent as a bug.** The arithmetic, updated with today's close: **VOO closed
  703.34, +0.457% on the day**; against the 700.625 reference of the first intended bootstrap
  (2026-09-01 09:36 ET), $70,000 would now be **$70,271 — about +$271 (+0.39%) foregone**.
  **That number is not evidence either, and a future run must not cite it as though it were.**
  Yesterday the same sleeve "outperformed" by sitting out a −0.67% day. Two sessions is noise in
  both directions; the argument against an all-cash book is **structural** — §1 asks this account
  to beat the S&P over a rolling twelve months and a book holding no index cannot track it up or
  down — and that was equally true on the day the tape flattered the delay.

- **Core sleeve still does not exist, and the bootstrap and the rebalance are ONE action.**
  `core_established: false`, core 0.0% against a 70% target — outside the §2 65–75% band
  (`core_in_band: false`, `rebalance_needed: true`, `rebalance_delta: 70000.0`, unchanged across
  all six runs since 2026-09-01 00:48 ET, and again at the 16:15 ET close). Step 3's bootstrap and
  Step 7's rebalance are **the same $70,000 VOO buy** on this account. Today's open run submitted it
  **once** and explicitly did not re-submit it at Step 7; tomorrow's run must do the same. Do not
  clear this line until a VOO fill is verified in `trade_log.md` → *Entries*. **Size to 70% of live
  equity at the open, not to the $70,000 written here** — if equity has moved, the target moves.



- **Week rollover: re-checked at the close, none needed.** ISO Monday of 2026-09-02 (Wednesday) is
  2026-08-31, which matches `week_of`. `new_positions_this_week` stays 0 — the §6 weekly cap is
  fully available at 0 of 3. Breaker INACTIVE, `consecutive_closed_losses: 0`,
  `halt_triggered_at: none`; only a **closed** position can move the streak, nothing has ever
  opened, so the streak is untouched and the breaker could not trip from this run.
  `HALT_CLEARED_AT: none` in `control.md`, correct and irrelevant while no halt exists. No
  `clickup.py alert` was raised and none was warranted. **Note for tomorrow: 2026-09-07 is the
  next week boundary, not this one** — the reset must be checked against ISO Monday every run and
  not inherited from this line.

- **The `plan_today.md` staleness gate is a live check, not a formality.** It passed today
  (`plan_date: 2026-09-02` against an ET date of 2026-09-02). Tomorrow's open run must **re-read
  `plan_date` against its own date** rather than inherit that outcome — the gate is only useful on
  the day it would fire, and today's plan becomes stale at midnight.

- **⚠ LHX REMAINS THE MOST DANGEROUS NAME IN THIS LOG, and the reason is that it keeps being almost
  right.** It has surfaced on two consecutive days through **two different, separately sourced
  drivers** — PAC-3 MSE / THAAD propulsion (T-2026-09-01-02, died on §4.3 timing) and the Army
  TITAN production award (T-2026-09-02-01, died on §4.2 magnitude: $127M across a five-partner team
  against $21.865B of revenue, ≤0.58%). Meanwhile it sits near a 52-week low and passes the
  five-session priced-in check cleanly. **The thing actually moving the stock is still the postponed
  Missile Solutions IPO** — a third event, unrelated to either mechanism. **Standing rule: when the
  same ticker surfaces on consecutive days through different events, treat the recurrence as a
  warning, not as corroboration.** A large diversified prime appears in every defense news cycle by
  construction; appearing is not being materially affected, and each event must clear §4 on its own
  numbers. Note for the open run specifically: LHX was *not* an intent today and must not be
  reached for at the bell on the strength of how often it appears.

- **The "Company A's print implies Company B's print" failure recurred within 24 hours, in a
  different sector and at ten times the scale.** On 2026-09-01 the funnel dropped "SAIC beats and
  raises → buy LDOS/CACI/BAH" as a correlation dressed as a mechanism. On 2026-09-02 the identical
  shape arrived as "Dell raises AI-server guidance → HPE rises ~5% on improved sentiment," backed
  by genuinely arresting numbers ($60.9B of quarterly AI orders, a $95B backlog, FY guidance up
  $25B). It was harder to dismiss *because* the underlying demand is so obviously real. **The size
  of Company A's number has no bearing on whether a mechanism to Company B exists.** A $95B backlog
  at Dell is $0 of revenue at HPE. Expect this shape again; it is the most fluent sentence
  available on any given day.

- **MU: not re-checked, and the reason matters more than the fact.** The pre-market journal
  predicted a pull to re-run Micron's priced-in check hoping for a friendlier number, and named it
  in advance as an inheritance-of-conclusion failure. What stopped it was **not resolve — MU does
  not appear anywhere in today's funnel.** No source across six queries named Micron or any memory
  supplier in connection with any of today's events, including Dell's AI-server ramp, where a
  dedicated screen for component suppliers and for memory-cost commentary came back **explicitly
  empty on both**. **The correct reason not to re-check a rejected candidate is that today's
  evidence does not produce it.** If a future run's funnel does surface MU from a source, re-running
  the filter and re-testing the timing window from that day's date is legitimate and different from
  what almost happened here.

- **⚠ STANDING RULES — four, sharing one root cause.**
  (i) *Screen on the mechanism before running filters* (from RTX — a filter is not a substitute for
  a sourced candidate). (ii) *Verify what the company currently sells, post-spin* (from WDC).
  (iii) *Verify the news is new to the company's own disclosure* (from AEP — if management has
  already guided the pipeline the contract falls inside, the deal illustrates guidance rather than
  changing it). (iv) *A recurring ticker is a warning, not corroboration* (from LHX, above).
  **The common root:** across eight candidates, six passed the priced-in check and failed on the
  thesis (NOC, LHX×2, WDC, AEP, and HPE would have but died at part 1), and one (MU) passed the
  thesis and failed the filter. **The filter has still never been informative about the outcome.**
  Treat a passing priced-in check as a veto that did not fire, never as encouragement — "has not
  moved" and "should have moved but didn't" are the same number.

- **Observation for the human about `alpaca.py move`, not an argument against it.** The script
  tests **absolute** magnitude, so a stock that has *fallen* more than 4% returns
  `priced_in: true`. On 2026-09-02 HPE (−4.96%) and DELL (−5.84%) both tripped it on five-session
  windows ending before Dell's print — drawdowns, not run-ups. §4's wording is "already moved more
  than 4% over the last five sessions **on this news**," so a decline predating the news is arguably
  not the thing the rule aims at. **Nothing has turned on it yet** (HPE died at part 1, DELL is
  Company A) and **no run should reinterpret the filter on its own authority** — a veto that fires
  too often is the safe direction. But a legitimate candidate that fell 5% on unrelated news would
  be blocked, and that is a human's call to make deliberately rather than discover by accident.

- **Live events examined and deliberately not traded — do not re-derive these.**
  (a) **PAC-3 MSE / THAAD ramp** (Pentagon 7-year MYP, 2026-08-31): NOC, LHX, RTX all rejected on
  §4.3 timing (revenue is 2027+) and magnitude. **NOC and LHX share one driver**; §4 permits at
  most one. (b) **The memory-cost cycle** (NVDA guiding GM 75% → 71–72% by FQ4 2027): MU is the
  clean second-order name and the strongest thesis written so far, **rejected solely on priced-in**
  (+5.27% / 5 sessions, +15.6% / 20). **MU, STX and SNDK share one driver.** (c) **The Anthropic /
  Lambda / Hut 8 Beacon Point datacentre deal**: only AEP is tied to it by any source, rejected on
  §4.2 magnitude and §4.3 timing — 1 GW inside 45 GW AEP has *already guided through 2030*. **A
  cheaper AEP entry changes nothing**; the rejection is on timing, which a price move cannot fix.
  (d) **GE's $2.87B Navy F414 PBL award** (2026-09-01): a dedicated screen confirmed the award is
  **sole-source to GE with no other publicly traded company named** — there is no Company B, and
  inventing a supply chain from general knowledge would repeat the RTX failure. (e) **Nvidia /
  Hugging Face, ~$14B**: unsigned as of 2026-09-02 ("a final agreement hasn't been reached"),
  target private, no third party named by any source. Not a fundamentals trade.

- **Eight thesis IDs now carry a 2026-09-0x date across two days**; six of those are from
  2026-09-01, produced by three runs against one rolling news window. **A reader scanning
  `research_log.md` should not read eight IDs as eight days of work.**

- **`alerts.md` remains empty — zero incidents, nothing SYSTEMIC, nothing unresolved.** Selftest
  passed all five checks. No alert was raised this run and none was warranted. The standing
  condition (`TRADING_ENABLED: false`) is a known human-owned item
  already reported via ClickUp task `86bbrna9n` on 2026-09-01; re-alerting a standing condition is
  exactly what the dedupe rules exist to prevent.

- **Cleared from carry-forward this run: the two open-run process notes** (Steps 4–6 having empty
  input, and the one-time record of the staleness gate's first live test) — both were about how
  2026-09-02's open run behaved, both were acted on, and neither tells tomorrow anything it will
  not re-derive. The staleness gate survives above as a standing instruction rather than a report.
  **The schedule item is deliberately NOT cleared** — today was Routine 1's first clean day and its
  test is tomorrow. Everything else stands. The research items below (LHX, MU, HPE, the four
  standing rules, the live events already examined) are carried untouched: this run did no research
  and has no grounds to revise or retire any of them.
