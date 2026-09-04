# Weekly Review

**AGENT-OWNED. Newest first. Written by the Friday routine.**

The objective in §1 is to beat the S&P 500 total return over a rolling 12-month window.
This file is the only place that question actually gets answered.

**One benchmark, used everywhere: VOO total return.** §1 names S&P 500 total return and the
core sleeve holds VOO, so the review measures against the same instrument the account
actually owns — using SPY here would make the headline number quietly disagree with the
core sleeve's own performance for no reason. Bars are pulled with `adjustment=all` so
dividends are included; a price-only series understates the benchmark by roughly its yield,
which would flatter the agent a little more every single week.

---

## Template

```
### Week ending YYYY-MM-DD

**Performance**
| | Week | 1M | 3M | 12M (rolling) | Since inception |
|---|---|---|---|---|---|
| Account | | | | | |
| VOO (total return) | | | | | |
| Excess | | | | | |

12-month figures use the full window once available; before then, state the actual elapsed
period rather than annualizing a short run into a number that means nothing.

**Sleeves:** core 0.0% | satellite 0.0% | cash 0.0%
**Breaker:** INACTIVE | ACTIVE since YYYY-MM-DD

**Trades closed this week**
| Ticker | Thesis | Held | Exit rule | P&L |
|---|---|---|---|---|

**Thesis scoreboard — including rejects**
- Theses written: N (N accepted, N rejected)
- Of accepted theses now closed: N reached their timing window, N invalidated, N stopped out
- **Of rejected theses: what happened to them since?** Track the ones that ran without you.
  A rejection rate that is never wrong means the filters are too loose, not that the
  judgment is perfect.

**Recurring errors**
<what shows up across multiple weeks — the point of this section is patterns, not incidents.
If the same failure appears three weeks running, say so plainly and name it.>

**Housekeeping**
- Monthly archive rollover: <done / not due>
- Weekly counter reset: new_positions_this_week → 0, week_of → <next Monday>
```

---

## Reviews

### Week ending 2026-09-04

**Breaker: INACTIVE.** No halt. Weekly cap 0 of 3 used.

**This is the first weekly review in this repo's history.** The book has been operating for
**four sessions** (2026-09-01 → 2026-09-04). The core sleeve has existed for **two** (filled
2026-09-03). The satellite sleeve has **never held a position**. There is no 1-month, 3-month or
12-month history and none of those figures are reported — annualizing four sessions would produce
a number that means nothing.

---

#### The §1 answer, first

**The satellite sleeve is behind what the same capital would have done in VOO, by −0.42% since
inception (−$127 on $30,000 of sleeve capital).**

It is behind for exactly one reason: it held cash every session. There were no losing trades,
because there were no trades. Idle satellite cash is counted at 0% return inside the measurement
— not excluded from it — because choosing not to deploy is a decision the strategy made, and its
cost belongs in the number rather than beside it.

Every individual no-trade decision this week was defensible and I would make each one again. The
cumulative result is still a shortfall against §1, and those two statements are not in conflict.

---

#### The three numbers

Reported separately. A blended portfolio-vs-VOO figure at 70% core would be mostly VOO measured
against itself, and would report a satellite sleeve doing real damage as a rounding error.

##### 1. Core return — +0.158%

VOO sleeve, filled 706.74 on 2026-09-03, official close 707.86 on 2026-09-04.
Unrealized **+$110.93** on 99.046311231 shares.

VOO total return over the same two-session window (09-02 close 703.34 → 707.86) was **+0.643%**.
The core is **−0.485%** against its own benchmark.

**This is not skill and it is not tracking error — it is the entry gap, and it is permanent.**
The fill at 706.74 was **+0.483%** above the prior close: the order went in at the 09-03 open on a
day VOO gapped up. That 0.48% is a one-time level offset baked into the sleeve's cost basis
forever; it will show up as this same divergence in every future review unless it is measured
from the fill instead of from inception. **Future reviews should measure the core from 706.74, not
from the 09-02 close.** Measured that way the core tracks VOO exactly, which is what a
buy-once-hold index sleeve should do. Nothing here is a data problem.

##### 2. Satellite return — 0.00%

| | |
|---|---|
| Realized P&L on closed positions | $0.00 (nothing has ever closed) |
| Unrealized P&L on open positions | $0.00 (nothing is open) |
| Sleeve capital (§2 target, 30% of equity) | $30,000.00 |
| **Return on sleeve capital** | **0.00%** |

Zero positions opened, zero closed, zero orders submitted. The sleeve has been 100% cash for all
four sessions of the account's operating life.

##### 3. Satellite vs the same capital in VOO — **the §1 number**

Position-level dollar-weighting is degenerate this week: there are no positions, so the entire
sleeve is idle cash at 0% return, weighted 100%.

| Window | Elapsed | Satellite | VOO (total return) | **Excess** | On $30k |
|---|---|---|---|---|---|
| Week (from 08-28 close 707.18) | 4 sessions | 0.00% | +0.096% | **−0.10%** | −$28.85 |
| Since inception (from 08-31 close 704.875) | 4 sessions | 0.00% | +0.423% | **−0.42%** | −$127.04 |
| 1M / 3M / 12M | — | *no history — account has operated 4 sessions* | | | |

For context on what §1 actually asks for: **VOO's own trailing total return is +20.04% over 12
months**, −0.14% over 1 month and +1.98% over 3 months. The 12-month figure is the bar. A sleeve
sitting in cash contributes nothing toward clearing it.

##### Account level — reported, and immediately qualified

| | Week (from 08-28) | Since inception (from 08-31) |
|---|---|---|
| Account | +0.111% | +0.111% |
| VOO (total return) | +0.096% | +0.423% |
| **Excess** | **+0.015%** | **−0.313%** |

The account number is identical in both columns because the book sat flat at $100,000 until the
09-03 core fill; only the VOO anchor moves.

**The +0.015% "outperformance" on the week is not outperformance and must not be recorded as
any.** It exists because the book was 100% cash through VOO's −0.67% down day on 09-01 and only
bought in afterward. That is an exposure gap that happened to be pointed the right way for one
session, and it runs identically in reverse on every up day. The since-inception column, which
anchors before the down day rather than inside it, is the honest one: **−0.31%**.

This is the third instance of the same framing pull in four days. See below.

**Sleeves (official close):** core 70.03% | satellite 0.0% | cash 29.97%
`core_in_band: true`, `rebalance_delta: −16.04` — 0.02% of equity, deep inside the §2 65–75% band.
No rebalance due.

---

#### Trades closed this week

**None.** The table is empty and there is nothing to put in it.

| Ticker | Thesis | Held | Exit rule | P&L | Excess vs VOO |
|---|---|---|---|---|---|
| *(none)* | | | | | |

`orders --status all` returns exactly one order in the account's entire history: the 09-03 core
VOO buy `d177d8f0`, `status: filled`, terminal. Nothing is in limbo.

**Which exit rules are firing:** none, and this is worth stating rather than skipping. §5 has never
been evaluated against a real subject. §5.1 invalidation, §5.2 time stop, §5.3 hard stop and §5.4
trailing stop are all **untested code paths, not proven ones.** §5.4 specifically is **unarmed, not
disabled** — it arms the day the first satellite position opens. Four days of midday runs reporting
"no exits" reported the absence of a subject, not four clean bills of health, and the daily logs
were careful about that distinction every time.

There is no read yet on whether exits skew toward the −7% hard stop, whether time stops fire too
often, or whether invalidations do their job. Those questions need closed trades and there are none.

---

#### Thesis scoreboard — including rejects

**Written this week: 10 (0 accepted, 10 rejected).** Acceptance rate 0%. No thesis became a
position, so there is nothing in the "of accepted theses now closed" tally — no timing windows
reached, no invalidations, no stop-outs.

Ten IDs carry a 2026-09-0x date across four days, six of them from 09-01 alone (three runs against
one rolling news window). **Ten IDs is not ten days of work.**

##### What the rejects did after we passed on them

Measured from the close each rejection was actually made against, versus VOO total return over the
identical window. Windows are 1–3 sessions. **This is a scoreboard being opened, not evidence.**

| Ticker | Thesis | Rejected on | Name | VOO | **Excess** | Rejection reason |
|---|---|---|---|---|---|---|
| MU | T-2026-09-01-04 | priced-in filter (+5.27%/5d) | +5.92% | +0.42% | **+5.49%** | filter veto |
| WDC | T-2026-09-01-05 | part 1 — not exposed post-spin | +3.76% | +0.42% | **+3.34%** | thesis |
| CLF | T-2026-09-04-01 | parts 1/2/3 + §3 cap $7.01B | +1.79% | −0.40% | **+2.19%** | thesis + universe |
| HPE | T-2026-09-02-02 | part 1 — read-across, no mechanism | +2.36% | +1.10% | **+1.26%** | thesis |
| AEP | T-2026-09-01-06 | parts 2+3 — segment / timing | +1.66% | +0.42% | **+1.23%** | thesis |
| LITE | T-2026-09-03-01 | priced-in filter (−7.35%/5d) | +1.27% | +0.64% | **+0.62%** | filter veto |
| LHX | T-2026-09-02-01 | part 2 — ≤0.58% of revenue | −2.22% | +1.10% | **−3.33%** | thesis |
| LHX | T-2026-09-01-02 | part 3 — timing unsourced | −3.22% | +0.42% | **−3.64%** | thesis |
| RTX | T-2026-09-01-03 | part 1 — mechanism was own inference | −3.37% | +0.42% | **−3.79%** | thesis |
| NOC | T-2026-09-01-01 | part 2 — ~1% of revenue | −4.56% | +0.42% | **−4.98%** | thesis |

**Six of ten rejects beat VOO; four lagged. Equal-weight mean excess −0.16%.**

**The filters are not never-wrong, and that is the healthy reading.** The routine's own warning is
that a rejection rate which is never wrong means the filters are too loose. Six names running
without us in four sessions says we are rejecting enough. CLF is on the list for completeness only
— zero full sessions have elapsed since its rejection today and its +2.19% is not a measurement.

**The split that matters, and it is not the one the headline shows:**

| Rejection type | n | Mean excess |
|---|---|---|
| Priced-in filter veto (MU, LITE) | 2 | **+3.06%** |
| Thesis / universe failure (the other 8) | 8 | **−0.97%** |

The eight names rejected on the four-part thesis or §3 have, on average, lagged the index. **The
four-part test is selecting correctly.** The two names rejected by the §4 priced-in filter are the
two largest positive excesses on the board — and **they are the same two candidates that passed the
four-part thesis.** The filter is currently vetoing the thesis test's own winners.

Both were **rejected correctly by the rule and unprofitably in hindsight**, and those are two
different findings that must not be recorded as one:

- **MU** (+5.49% excess) failed on a genuine run-up, +5.27% over five sessions. The rule did
  precisely what it was written to do. We were late; the filter said so; the name went on to +5.92%
  anyway. This is the priced-in filter working as designed and costing money — an acceptable,
  expected outcome for a veto, and nothing to change.
- **LITE** (+0.62% excess) is a different animal and is **not** the filter working as designed. It
  failed on **−7.35%** over five sessions — a *drawdown*, read as `priced_in: true` because
  `move` tests absolute magnitude. A decline is close to the opposite of "the market has already
  paid for this news." This is the open question already flagged to the human on 09-03 and 09-04
  and it is unchanged. **No run has reinterpreted the filter and none should** — the fix is a human
  editing §4 or `alpaca.py move`, not a run deciding a rule is out of scope for a name it likes.

**Caveat, stated plainly so a future review cannot quote this section as a result:** one to three
sessions of price action is noise. Ten names is not a sample. Nothing above is evidence about
filter calibration. It is the first row of a tally that needs months before it says anything, and I
am opening it now precisely because the human already has a live question about this filter.

**Priced-in filter, cumulative record across all 10 worked candidates:** 7 passed the filter and
failed the thesis; 2 passed the thesis and failed the filter (MU, LITE); 1 (CLF) had the filter
deliberately not run because the mechanism failed first and §4 orders the filters before the
thesis. **The filter has never once been informative in the direction people expect it to be.** A
passing priced-in check is a veto that did not fire, never encouragement — "has not moved" and
"should have moved but didn't" are the same number.

---

#### Recurring errors

##### 1. The reassuring framing — **three of four days. Named.**

This is the recurring error of the week and it is a finding about the agent, not about the week.

- **09-01:** the core bootstrap failed to fill and the index fell 0.67%. Filed as "no harm done."
- **09-02:** the up day arrived; the symmetric temptation was to present the $271 as *the cost of
  the dry run* — a concrete number arguing a preferred conclusion.
- **09-04:** the book fell −0.31% against VOO's −0.40% and the first sentence that arrived was
  that it held up better. It did not. It is 70% invested and captured 70% of a down move.

Each time it was caught and corrected in the journal before it reached a summary. But it arrived
**first** each time, in three different book structures — 100% cash, dry-run counterfactual, 70/30
invested. **A framing that survives that much structural variation is not a slip; it is what this
agent produces by default whenever partial exposure and a down day coincide.**

**It recurred in this review.** The week-anchored account column above shows +0.015% excess, and
that number is available to be written as beating the index. It is not. It is one down day the book
sat out. Every future review should expect to generate this sentence and should expect to delete it.

##### 2. The satellite sleeve has never been deployed, and the structure points away from §1

Four days, ten theses, zero positions. §2 explicitly permits uninvested satellite cash and §4 says
the correct output of most research runs is no trade. **Both rules were followed and no rule was
breached.** The cumulative result is a book that is functionally a 70% index tracker with a 30%
cash drag, and **a 70/30 cash book cannot beat the S&P over a rolling 12 months in a rising market
— only in a falling one.** The measurement above now puts a number on it: **−$127 of sleeve
capital in four sessions.**

**This is not a call to lower the §4 bar, and the agent will not lower it.** It is a strategy-level
question — is the 30% satellite target reachable at the four-part thesis's current strictness, or
does one of the two need to move? — and it belongs with the human. Raised in the 09-04 daily
summary and restated here because a weekly file is where a structural question should live.

##### 3. The two-price trap — two days running, and it went live this week

`alpaca.py positions` returns `current_price`; `bars --adjustment all` returns the official close.
At 16:16 ET the first looks exactly like the second. On 09-03 the agent nearly reported the day's
numbers off the wrong one. On 09-04 the gap was real and measured: broker mark **707.59** against
official close **707.86**, **$26.75** on the core position — and the official close sat *above* the
broker mark, the reverse of the intraday fades seen all week, so the direction is not predictable.

It has cost nothing because core carries no `highest_close`. **The day a satellite position exists,
that shortcut writes a wrong high-water mark — which does not error, does not look stale, and
silently moves the §5.4 trailing stop to a level nobody chose.** Two occurrences is not yet three,
but this one does not need a third to be worth acting on, because its first real cost lands on the
first day the sleeve is ever deployed. **Always pull `bars` for the close. Never mix the two inside
one §5.4 comparison.**

*(This review used the official close 707.86 throughout, not the 707.28 broker mark that
`positions` returned at 20:45 UTC. At the official close, equity is $100,110.92, not the
$100,053.48 the account endpoint reports.)*

##### 4. The read-across shape — appears daily, caught every time

"Company A's print implies Company B's print": SAIC → LDOS/CACI/BAH (09-01), Dell → HPE (09-02,
recorded as recurring within 24 hours), Broadcom → competitors (09-03), screened for and absent
(09-04). **The recurrence here is in the funnel, not in the decisions** — the news flow generates
this shape every single day and the screen has caught it every single time, including once as a
formal thesis (HPE, T-2026-09-02-02, rejected at part 1).

Recorded as a finding about workload rather than error: **the read-across screen is load-bearing
and is the most frequently exercised filter in the system.** It is the one whose quiet removal
would do the most damage.

##### 5. Five standing rules, one root cause

(i) Screen on the mechanism before running filters (RTX). (ii) Verify what the company currently
sells, post-spin (WDC). (iii) Verify the news is new to the company's own disclosure (AEP).
(iv) A recurring ticker is a warning, not corroboration (LHX). (v) A market-structure fact is not a
supplier relationship (CLF).

All five are the same failure: **supplying the causal link yourself and then finding a source that
is merely adjacent to it.** Five separate names in four days produced five separately-worded
lessons for one mechanism. A sixth variant should be expected next week wearing another disguise;
the useful response is to recognise the shape, not to write a sixth rule.

---

#### Housekeeping

- **Weekly counter reset: DONE.** `new_positions_this_week` → 0 (was already 0),
  `week_of` → **2026-09-07** (ISO Monday of the next week). This discharges the rollover the
  09-04 carry-forward flagged as owed to Tuesday's run. Tuesday will re-check, find the anchors
  match, and correctly do nothing. **Note 2026-09-07 is Labor Day — the anchor is the ISO Monday,
  not the first session, so the reset is correct even though that Monday has no session.**
- **Monthly archive rollover: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated 2026-09. Nothing predates the current month, so nothing moves and no
  archive index line is written. `archive/` holds only its README. First time this check has run.
- **Alert hygiene: `alerts.md` is EMPTY.** Zero open incidents, zero SYSTEMIC, zero resolved. No
  `push-failure`, no `guard-violation`, no `selftest-abort`, no `circuit-breaker` in the repo's
  history. The selftest passed all five checks on all five of today's runs.
- **Next session: Tuesday 2026-09-08 09:30 ET.** Monday 2026-09-07 is Labor Day; a run firing
  Monday should log a holiday skip and exit successfully. That is not a fault.

---

#### For the human

Three things, in order of how much they need a decision:

1. **The §4 priced-in filter reads a drawdown as "priced in"** (LITE, −7.35% over five sessions →
   `priced_in: true`). Third consecutive day flagged, now with a scoreboard entry attached. The
   agent will not reinterpret this rule on its own. It needs either an edit to §4 or a change to
   `alpaca.py move` — or an explicit decision to leave it as is, which is a perfectly good answer
   and would close the item.
2. **The satellite sleeve is structurally undeployed.** Ten theses, zero positions, −$127 vs
   benchmark in four sessions. Either the 30% target or the four-part strictness may need to move,
   and that is not the agent's call to make.
3. **The core sleeve's −0.485% divergence is the 09-03 entry gap**, not tracking error. Future
   reviews should measure the core from the 706.74 fill. Flagged so it is not mistaken for drift.

