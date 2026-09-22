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
