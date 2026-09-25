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

### Week ending 2026-09-25

*Posted to ClickUp as task `86bc7vzam` — https://app.clickup.com/t/86bc7vzam — separate from the
daily summaries. (Week 3: `86bc3bzz6`. 09-25 daily summary: `86bc7vgbw`.)*

**Breaker: INACTIVE.** `halt_triggered_at: none`, `consecutive_closed_losses: 0` (it has never had an
input), weekly cap **0 of 3** used. Nothing was gated this week. Nothing was blocked from trading at
any point, on any run.

**Fourth weekly review.** The book has now operated **18 sessions** (2026-09-01 → 2026-09-25), **5 of
them this week**. Theses since inception: **73** (74 `### T-` headings in `research_log.md` less the
template, recounted from source this run). Theses accepted: **0**. **The satellite sleeve has never
held a position and has never placed an order.** The account's entire order history remains one row:
the 09-03 core VOO buy.

---

#### The §1 answer, first — and this is the first week the short windows agree with it

**No. The satellite sleeve is not beating what the same capital would have done in VOO, and this week
every single window says so.**

Over the trailing 12 months VOO's total return is **+18.57%**. The satellite sleeve returned
**0.00%**, because it has been $30,000 in cash for every session of its existence. Excess on §1's own
window: **−18.57pp**. The account is 18 sessions old and cannot fill a 12-month window with its own
history, but the benchmark leg does not need the account to be old enough, and it is the leg that
answers the question.

**The thing to record this week is a sign change that three consecutive reviews predicted in writing.**
Weeks 1, 2 and 3 each reported positive excess on the short windows and each refuted it in the same
paragraph: a sleeve at 0% exposure shows positive excess on any window where the market fell, and
gives it all back on any window where the market rose. Week 3 wrote *"expect this row to be positive
on every red week from here, and expect to refute it every time."*

**The market rose, and the row went negative — all of it, at once, for the first time.**

| Window | Week 3 (to 09-18) | **Week 4 (to 09-25)** |
|---|---|---|
| Week | **+0.095pp** | **−1.262pp** |
| Since inception | **+0.430pp** | **−0.827pp** |
| 1 month | **+0.509pp** | **−0.974pp** |
| 3 months | −2.291pp | **−5.444pp** |
| **12 months (rolling)** | −16.552pp | **−18.571pp** |

Three weeks of favourable short-window numbers were a property of a falling tape, exactly as they were
each time recorded to be. **They are gone in a single up week.** No rule changed, no decision changed,
and the sleeve did nothing different — the tape went the other way and the whole reassuring column
inverted. That is the strongest available evidence that the previous reviews were right to refuse to
read those numbers as performance, and it is worth stating plainly now that the pleasant version is no
longer available to inherit.

**The structural cost, restated at this week's benchmark:** a satellite sleeve parked in cash at the
§2 target weight gives up **0.30 × 18.57% ≈ 5.57pp of account return** per rolling 12 months. That is
up from **4.97pp** last Friday — not because the sleeve got worse, but because the benchmark got
better, which is the direction that makes the cost grow.

---

#### The three numbers

**Both legs of every comparison below come from official closes (`bars --adjustment all`, 260 sessions
pulled this run, 2025-09-15 → 2026-09-25).** Never a `positions` field, never `equity − last_equity`.
The 2026-09-25 bar was confirmed complete before use (`is_open: false` at pre-flight; n 4,249,
v 164,723 — both in full-session range).

Official-close equity today: **$100,392.71** (99.046311231 × 710.705 + $30,000 cash). The broker
reports **$100,416.12** at 16:45. The **$23.41** difference is the two-price artifact, not a
discrepancy to investigate.

##### 1. Core return — tracking, not skill

| | Value |
|---|---|
| Fill (2026-09-03) | **706.74** |
| VOO close 2026-09-25 | **710.705** |
| **Core return from the fill** | **+0.5610%** |
| **Core divergence from VOO over the same window** | **0.0000%** |

The core sleeve **is** VOO, so measured from its own fill it tracks the benchmark exactly, for the
fourth review running. The **+0.483% entry gap** — the 09-03 order filled 0.4834% above the 09-02
close of 703.34 — is a permanent level offset that appears whenever the core is anchored to a close
rather than to its fill. **It is not tracking error and it is not skill.** It is the whole of the
core's apparent divergence and it is discharged; keep measuring from the fill.

Core weight on official closes: **70.117%** (broker basis **70.12%**). Inside the §2 65–75% band,
**~4.88 points** from the nearest edge. **Forty-seventh consecutive run in band.** No rebalance due
Monday on either basis, and §2 acts at the band edge in any case.

⚠ **`rebalance_delta` is negative on both bases this run (−$117.81 official, −$124.84 broker) and has
been for five runs. That is not the two-price defect resolving** — the same quantity disagreed in
*sign* on 09-24 (+$12.78 broker against −$16.04 official). **The defect is intermittent, which is
worse than persistent, and a run that checks one basis and finds agreement learns nothing.**

##### 2. Satellite return

| | Value |
|---|---|
| Realized P&L on everything closed | **$0.00** — nothing has ever closed |
| Unrealized P&L on everything open | **$0.00** — nothing is open |
| Capital allocated to the sleeve | **$30,000** (29.883% of equity on closes) |
| **Satellite return** | **0.0000%** |

Zero positions for the **twenty-fifth consecutive session**. Every dollar of the sleeve has been idle
for its whole life: **18 sessions since inception, 16 since the core fill funded the 70/30 split.**

##### 3. Satellite versus the same capital in VOO — the number that answers §1

Per the routine, idle satellite cash enters the measurement at **0% return** with **weight 1.00**,
because choosing not to deploy is a decision the strategy made and its cost belongs inside the number.
With no position rows, the dollar-weighted excess collapses to exactly **minus VOO's total return over
the window**. The dollar-weighting is trivial and **the reason it is trivial is the finding**.

| Window | Elapsed | Satellite | VOO (total return) | **Dollar-weighted excess** |
|---|---|---|---|---|
| Week | 5 sessions | 0.00% | **+1.262%** | **−1.262pp** |
| Since inception | 18 sessions | 0.00% | **+0.827%** | **−0.827pp** |
| 1 month | account has 18 sessions — **VOO leg only** | 0.00% | **+0.974%** | **−0.974pp** |
| 3 months | account has 18 sessions — **VOO leg only** | 0.00% | **+5.444%** | **−5.444pp** |
| **12 months (rolling)** | account has 18 sessions — **VOO leg only** | 0.00% | **+18.571%** | **−18.571pp** |

**Nothing above is annualized.** The account is eighteen sessions old; the 1M, 3M and 12M rows carry
the benchmark leg over its true window against a sleeve that was flat for all of it, and the elapsed
period is stated rather than scaled.

**Read down that column and note what is no longer there.** For three weeks the sign changed as the
window lengthened, and the standing instruction was that the 12-month row is the one §1 asks about.
**This week the window no longer matters — every row is negative, and they differ only in size.**

##### The account as a whole, for completeness

| | Week | 1M | 3M | 12M (rolling) | Since inception |
|---|---|---|---|---|---|
| Account | **+0.8813%** | n/a (18 sessions) | n/a | n/a | **+0.3927%** |
| VOO (total return) | **+1.2617%** | +0.974% | +5.444% | **+18.571%** | **+0.8271%** |
| Excess | **−0.3804pp** | — | — | — | **−0.4344pp** |

**The week's −0.3804pp is 30% cash in an up week and nothing else, and the arithmetic is exact to four
decimal places.** The core's weight at Friday's open was **0.6985**; 0.6985 × 1.2617% = **+0.8813%**,
which is the account's week to the fourth decimal. The satellite sleeve contributed **exactly
0.0000%**. The book captured precisely 69.85% of the market's move and nothing else.

**And the since-inception row flipped this week too.** Last Friday it read account −0.484% against VOO
−0.430%, excess **−0.055pp** — a residual so small it was correctly attributed to the entry gap. Today
it reads **−0.4344pp**, **eight times wider**, and the entry gap did not change. **The difference is
five up sessions.**

##### The daily audit, because the inherited version of this claim needed checking

Week 3 carried forward the claim that *every positive-excess day in this account has been a VOO down
day.* This run recomputed all 15 post-fill sessions from official closes rather than repeating it.

**It holds, and it is stronger than the version handed forward: the separation is perfect, 15 of 15.**

| | n | Excess |
|---|---|---|
| VOO **down** days | **9** | **all 9 positive** (+0.0029pp to +0.2264pp) |
| VOO **up** days | **5** | **all 5 negative** (−0.0379pp to −0.4686pp) |
| VOO **flat** day (09-24) | 1 | exactly **0.0000pp** |

**The sign of this account's daily excess is entirely determined by the sign of VOO's move. There is
not one exception in the record.** That is not a performance statistic; it is the signature of a book
with one long position at 70% weight and no second source of return. **Worst relative session remains
2026-09-21 at −0.4686pp — the day the journal records as "biggest dollar gain on record."**

**Sleeves (official closes):** core **70.117%** | satellite **0.0%** (count 0) | cash **29.883%**
**Breaker:** INACTIVE

---

#### Trades closed this week

**None.** The table is empty for the **fourth consecutive week**, and nothing has ever been closed in
this account.

| Ticker | Thesis | Held | Exit rule | P&L | Excess vs VOO |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

**Which exit rules are firing: none — and the distinction this section is asked to draw still cannot be
drawn.** The routine asks whether every exit is the −7% hard stop (a system discovering its theses are
wrong at a fixed price), whether time stops dominate (timing windows written too optimistically), or
whether invalidations fire (the rule working as designed). **All three questions require exits to have
happened.**

§5.1 has no thesis to invalidate, §5.2 no `timing_window` to expire, §5.3 no `entry_price` to measure
−7% against, §5.4 no `highest_close` to measure −10% against. **`highest_close` is ABSENT — a third
state distinct from *stale* and from *current-and-unchanged*, carrying no `(as of …)` date at all.**
That absence is what proves no backfill is owed; it must never be read as a close run that failed.

**Eighteen sessions of "no exits" is the absence of a subject, not eighteen clean bills of health**,
and §5.4 has never been armed — it arms on the first *satellite* fill, which the 09-03 core buy was
not. `TRADING_ENABLED` was **true** all week, so a triggered stop *would* have been submitted. **The
null is an empty sleeve, not a disabled stop, and those two produce an identical zero-exit line.**

⚠ **The daily runs report this as "the thirty-seventh consecutive session" and that figure is wrong —
see Recurring Errors §3, catch (9). It is a run counter wearing a session label.** The account has
operated **18 sessions**. Corrected here and not propagated.

---

#### Thesis scoreboard — including rejects

**This week: 27 theses written, 0 accepted, 27 rejected** (09-21: 3, 09-22: 5, 09-23: 6, 09-24: 7,
09-25: 6). Acceptance rate **0%**.
**Since inception: 73 theses, 0 accepted, 73 rejected.** Acceptance rate **0%**, fourth week running.
**Recounted from `research_log.md` this run**, not inherited.

Of accepted theses now closed: **n/a — there are none.** How many reached their timing window with the
predicted business change, how many were invalidated, how many stopped out: **zero, zero, zero, and
the denominator is zero.**

##### Where the 27 died — and the failure point moved one test down the chain

Counted by **primary** failure point, the test the log records the thesis dying at first. Most died
independently at two or three.

| Failure point | n | Change vs Week 3 | Names |
|---|---|---|---|
| **Part 2 — magnitude / segment share / not revenue at all** | **11** | **4 of 16 → 11 of 27** | JBL, RDW, FLNC, BBY, PYPL, LHX, GFS, ACN, GM, BE, Paramount/WBD |
| Part 1 — no Company B, or the mechanism needs a second clause | 6 | 9 of 16 → 6 of 27 | memory suppliers, SoftBank/OpenAI, CNC, Vicor, GPC/ORLY/LKQ, BG |
| Premise — no Company A at all (first-order, environment input, government action, own-results print) | 5 | new category | AKAM, GRAL, GIS, LH, rate/oil/PMI complex |
| §3 — universe | 2 | — | ELMT ×2 |
| §4 priced-in — fired first and decisively | 2 | — | ILMN (+11.54%), SHOP (+9.61%) |
| Part 3 — timing beyond two quarters | 1 | 3 of 16 → 1 of 27 | one unnamed |

**This is the completion of a three-week arc and it is the most useful thing in this review.** Week 2
established the binding constraint as *the source names the transaction and withholds the
counterparty* — a part 1 problem. Week 3 found a second head one test further down (*both parties
named, the number withheld*) and logged it at 4 of 16. **Week 4: part 2 is now the dominant failure
point, nearly 2:1 over part 1, and part 1 has halved as a share.**

**And the week supplied the case that settles what that means. T-2026-09-25-01, JBL.** Anthropic
committed ~$11.6B over seven years to Akamai; Akamai's 8-K then did the thing a month of rejections
implied never happens — **named a US-listed supplier and allocated a specific dollar figure to it**, a
Build Request authorizing Jabil to procure **~$1.7 billion of memory components**. Part 1 passed more
cleanly than anything the log has produced. **It still was not a trade**, because Akamai pays *"all
corresponding supplier invoice amounts"*, Jabil holds the components *"in consignment as bailee"*, and
Akamai *"will repurchase such components from the Company at cost."* **A disclosed statement of zero
margin.** The only figure that would satisfy part 2 — Jabil's assembly fee — is disclosed by nobody.

⚠ **That is a fifth distinct form of the binding constraint, and it is the only one that widening the
evidence bar would not relieve. Widening it would have let this through.** The five forms: (i) the
source withholds the counterparty's number; (ii) the counterparty discloses roadmap instead of segment
revenue; (iii) the named beneficiary is vertically integrated, so there is no external supplier to
find; (iv) both parties expressly refuse to disclose as a commercial choice (GM); (v) **the figure is
fully disclosed and is the wrong quantity.** **Only (i) and (ii) are addressable by accepting weaker
evidence.**

**Stated for the human, because it changes what the open question is:** for three weeks the natural
reading of "73 theses, zero positions" was that §4 demands evidence public disclosure rarely supplies,
and that the fix might be to widen what counts as a quantified segment. **This week the funnel produced
the named, allocated, verbatim-from-an-8-K candidate that reading predicted was the missing ingredient,
and it still produced nothing.** That is evidence **the evidence bar is not what is binding**. It is
not evidence the bar should move, and the agent has not moved it.

##### Rejected theses — what happened to them since

**65 names measured this run**, up from 40 last Friday. Measured from the close of the day each
rejection was made, to the 2026-09-25 close, against VOO total return over the **identical** window —
the same convention as the Week 3 board, so the two are comparable row for row. **Both legs from
`alpaca.py move`** (which reads `bars --adjustment all` internally). No mixed-source comparison
anywhere below.

**20 of 65 beat VOO; 45 lagged. Mean excess −2.04%, median −2.47%.**

The full board, worst to best, is long; what matters is the two ends and what moved.

**The ten largest positive excesses — the names that ran without us:**

| Ticker | Rejected | Sess | Name | VOO | **Excess** | Rejection reason | Wk 3 |
|---|---|---|---|---|---|---|---|
| **CRDO** | 09-09 | 12 | **+25.69%** | +1.41% | **+24.28%** | parts 1/2 | +4.68% |
| **HPE** | 09-02 | 16 | **+21.72%** | +1.05% | **+20.67%** | part 1 — read-across | +17.64% |
| **MU** | 09-01 | 17 | **+15.93%** | +1.51% | **+14.42%** | **priced-in veto (+5.27% run-up)** | +8.57% |
| **QCOM** | 09-09 | 12 | **+14.52%** | +1.41% | **+13.11%** | §4 first-order headline name | +0.76% |
| **LITE** | 09-03 | 15 | **+11.16%** | +0.00% | **+11.16%** | **priced-in veto (−7.35% drawdown)** | +11.25% |
| CRWV | 09-15 | 8 | +8.23% | +2.07% | **+6.16%** | part 1 — "and also" clause | −0.40% |
| BE | 09-21 | 4 | +5.80% | −0.29% | +6.09% | part 2 — $25B financing ceiling | new |
| MRVL | 09-18 | 5 | +7.16% | +1.26% | +5.90% | part 2 | new |
| GFS | 09-23 | 2 | +5.56% | +0.48% | +5.08% | part 2 + premise | new |
| GFS | 09-10 | 11 | +6.87% | +2.01% | +4.86% | priced-in +4.53% / p3 | +3.32% |

**The five worst — the filters doing their job:**

| Ticker | Rejected | Sess | Name | VOO | **Excess** | Rejection reason |
|---|---|---|---|---|---|---|
| SLI | 09-11 | 10 | −17.00% | +1.17% | **−18.17%** | §3 |
| **CART** | 09-14 | 9 | −12.74% | +1.62% | **−14.36%** | part 2 — no dollar figure |
| LEU | 09-10 | 11 | −11.35% | +2.01% | **−13.36%** | §3 / priced-in / p2 |
| MTZ | 09-09 | 12 | −11.59% | +1.41% | **−13.00%** | parts 1/2/3 |
| VIST | 09-09 | 12 | −9.59% | +1.41% | **−11.00%** | §3 |

⚠ **Rows at 1 and 2 sessions are logged so a future review re-measures them, not quoted as
measurements** — ILMN, GRAL, BBY, PYPL, SHOP (1 session) and the nine 09-23 names (2 sessions). The
09-25 rejects have **zero** elapsed sessions and are not on the board at all. On the 51 rows with 3+
sessions the picture is the same and slightly worse: **14 of 51 beat, mean −2.41%, median −3.95%.**

⚠ **A note on the VOO leg, so it is not re-discovered as a data fault: the 1-session and 2-session VOO
returns are both +0.48%.** That is correct — 09-23 and 09-24 closed at **707.28** to the cent, verified
five times on distinct OHLV. A real coincidence, not a duplicated bar.

##### The finding on this board that is new, and it is not about any single filter

**Six of the top six excesses are the same theme.** CRDO, HPE, MU, LITE and CRWV are AI / data-centre
hardware and infrastructure; QCOM is a semiconductor name. Together they are **+24.28, +20.67, +14.42,
+13.11, +11.16 and +6.16 percentage points** against the index.

**They were rejected under five different rules.** HPE at part 1 (a read-across is an inference about
information, not a change in economics). CRDO at parts 1/2. MU on the priced-in filter, on a genuine
run-up. LITE on the priced-in filter, on a *drawdown*. QCOM as a first-order headline name. CRWV at
part 1 on an "and also" clause.

**No single rule is responsible, every one of those rejections was correct under §4 as written, and
the aggregate is that the strategy systematically declined to participate in the one theme that ran.**
That is not a bug to fix and it is not an argument to loosen anything. It is a structural interaction
worth naming once, plainly: **in a hot theme the names have already moved (so the priced-in filter
fires), the announcements are first-order about the hot name (so §4 excludes them), and the actual
suppliers go unnamed in the disclosure (so part 1 has no Company B).** §4's three most active tests
each independently exclude a running theme. **A human deciding whether the §4 bar is right should
decide it knowing that, rather than on the strength of any one name.**

##### Rejects that went on to work — right for the right reason, right for the wrong reason

The distinction the routine asks for, kept separate:

- **CRDO (+24.28pp) is now the largest excess on the board and it displaced HPE this week** — it ran
  from +4.68pp to +24.28pp in five sessions. It died at parts 1/2 in the 09-09 optics cluster. **The
  rejection was correct by the rule and expensive in hindsight. Those are different findings and they
  are both true.**
- **QCOM moved from +0.76pp to +13.11pp** — the single largest *change* on the board. QCOM is also one
  of the two names on open human item (2): its five-session `move` read **+2.70% net after a +8.7%
  intraday event move**, so the priced-in filter waved it through while the event was already absorbed.
  **It was rejected on a different ground entirely (first-order, §4), so item (2) cost nothing here —
  but the name it cost nothing on has since run 14.5%.**
- **LITE (+11.16pp) and MU (+14.42pp) remain the only two candidates in this repo's history that passed
  the four-part thesis and were then killed by the priced-in filter, and they must not be merged.**
  **MU** failed on a genuine **+5.27% five-session run-up** — the rule doing exactly what it was
  written to do, costing money, nothing to change. **LITE** failed on a **−7.35% drawdown** read as
  `priced_in: true`, because `move` tests absolute magnitude. **A decline is close to the opposite of
  "the market has already paid for this news."** That is open human item (1), now four weeks old.

##### Rejects that went nowhere — say so

**45 of 65 lagged the index.** The four-part test keeps selecting correctly in aggregate: SLI
(−18.17pp), CART (−14.36pp), LEU (−13.36pp), MTZ (−13.00pp) and VIST (−11.00pp) are the five worst
names on the board and every one died at parts 1–3 or §3.

**CART remains the most instructive correct rejection in the log** and it got worse for the road not
taken: rejected 09-14 because no dollar figure for the Kroger↔Instacart arrangement existed in the
release, the 8-K, the IR summary or the call coverage — and the journal records the pull to *size the
incremental prescription basket anyway.* A fabricated number would have carried it past §4.2 into a
trade. **CART is −14.36% against VOO since, widened from −8.72% last Friday. The invented number would
have bought a larger loss than it would have last week.**

##### Is the rejection rate ever wrong?

**Yes — twenty times out of sixty-five, and five of them expensively.** The routine's warning is that a
rejection rate which is never wrong means the filters are too loose. **That failure mode is not
present**: names run without us regularly, and five have run more than 11pp.

⚠ **A correction to Week 3's own headline, in this repo's habit of auditing inherited claims.** That
review wrote *"neither the count nor the mean is the headline; the widening is,"* on the strength of
the board's dispersion increasing as windows lengthened. **The widening has continued this week, and it
is mostly mechanical** — the dispersion of stock returns grows with elapsed time whether or not a
filter is doing anything, so a board whose rows keep aging will widen at both ends by construction.
**It should not have been promoted to the headline and is not promoted here.** What is *not* mechanical
is the **mean**: across 65 names the average reject lagged VOO by **−2.04%**, and on the 40 carried
rows by **−3.11%**. A filter selecting at random would centre near zero. **The mean is the evidence
that the four-part test discriminates; the widening is just time passing.**

**This is still a tally, not a result, and no future review may quote it as one.** Sixty-five
measurements over one to seventeen sessions is not a sample. It is recorded because the human has a
live question about the priced-in filter and this tally is the only evidence that will ever exist for
it.

**Priced-in filter, cumulative:** this week added a **third defect shape** to the two already on
record. **Shape one**, a drawdown misread as priced-in — nine instances, and CNC (−6.44% → `true`) on
09-23 is the newest. **Shape two**, the filter working, on genuine news rises — ILMN +11.54%, GRAL
+44.67%, SHOP +9.61% this week, its best week for doing its designed job. **Shape three, new on 09-25
and previously unrecorded: a genuine rise unrelated to the news, swept up by the window.** JBL read
+4.97% over five sessions, but the path was a grind whose largest day was +1.72% and whose **news day
moved JBL +0.63%.** §4 conditions on having moved 4% *"on this news"*; the mechanized check cannot see
causation. ⚠ **The defect is sign- and causation-blindness, not the threshold.**

⚠ **And the agent did not act on that, deliberately, which is the part worth carrying.** JBL was the
exact setup the "do not lower the bar" rule guards against: a candidate the run liked, plus a plausible
technical case that the filter had misfired. **Had part 2 not failed independently, the honest outcome
would still have been rejected-on-priced-in with the defect logged.** Only a human may change §4 or
`alpaca.py move`.

---

#### Recurring errors

The question here is not what went wrong this week — the close journals cover that — but what keeps
going wrong. **Four items are in their fourth consecutive week. One is new. One improved.**

##### 1. The reassuring framing — **FOURTH WEEK. NAMED. And this week it changed shape rather than recurring in form.**

Named in weeks 1, 2 and 3, each time with a prediction that it would recur, each time correct.

**What is new is that the comparison finally became unavailable, and the pull relocated rather than
stopping.** With every window negative, "we beat VOO" cannot be written. So the week's instances
dropped the benchmark from the sentence entirely:

| | The sentence that arrived first | How it was killed |
|---|---|---|
| 09-21 | *"biggest dollar gain on record, back above water"* | the same session was the **worst relative day in the book's history, −0.469pp** |
| 09-22 | broker reported the day **+$7.82 up** | the true close-to-close was **−$6.93 down** — a sign error, not a precision error |
| 09-24 | flat day, nothing to report | true move exactly **zero**; broker reported **−$127.77**, 100% artifact |
| 09-25 | *"best since inception"*, on +$339.23 | **third** best — 09-21 +0.5962%, 09-22 +0.5893%, and today ties 09-03 |
| **This review** | *"+0.39% since inception, an account in profit"* | **−0.434pp against the index over the same window** |

**Three weeks the failure was a favourable comparison. This week it is a favourable dollar figure with
no comparison in it at all** — which is harder to refute arithmetically, because nothing in it is
false. **A good day in dollars is not a good day against the benchmark, and on 09-25 those two readings
pointed in opposite directions.** The standing defence holds: the 12-month row is the one §1 asks
about, and every favourable number gets refuted in writing.

⚠ **New sub-finding, and it is the encouraging one: on 09-25 the false superlative was caught BEFORE it
was written, for the first time.** The run had the sentence half-formed, pulled 25 sessions of closes
first, and found the claim was third rather than best. **Carry-forward catch (1) is this exact shape
caught three runs late and by accident. This one cost one `bars` call.** Promoted to a standing rule:
**pull the source before writing the superlative, not after.**

##### 2. Broker marks versus official closes — **FOURTH WEEK, and this week it produced an instance on every single session**

Week 1 logged the gap. Week 2 solved the mechanism (a live bid/ask midpoint that keeps moving after
the bell, which is why it never had a stable size). Week 3 re-rated it from cosmetic to load-bearing.
**Week 4 establishes something worse than either: it is intermittent.**

- **09-21** — `lastday_price` stale for four consecutive reads *and* the midpoint defect firing in the
  opposite direction, leaving the broker's day P&L **$14.86 low** where every prior instance ran high.
- **09-22** — **the sign-error instance.** `lastday_price` 2c high and `current_price` 16.9c high at
  once, in opposite directions, so `equity − last_equity` read **+$7.82 up** on a day whose true move
  was **−$6.93 down.** On a flat day the standing rule is a **direction** rule, not a precision rule.
- **09-24** — **100% artifact.** True move exactly zero, broker reported **−$127.77**. And the first
  time the defect reached a **§2 quantity**: `rebalance_delta` read **+$12.78** broker against
  **−$16.04** official — same instant, same position, **opposite sign**, core reading below target on
  one basis and above on the other.
- **09-25** — artifact **+$23.38**, only **6.9%** of a **+$339.23** move. ⚠ **The rule's value is
  inversely proportional to the size of the real move, so it looks like pedantry on exactly the days
  it costs nothing to follow — and $23.38 would still have been reported as the day's P&L.**

⚠ **The load-bearing new fact: on 09-25 all three runs agreed in sign, and on 09-24 the same quantity
disagreed. Intermittent is worse than persistent, because a run that checks one basis and finds
agreement learns nothing.** Also worth keeping: `last_equity` on 09-25 read **100,024.75**, which is
neither the official prior equity (100,053.48) nor the prior run's broker equity (99,957.40) — **a
third number of its own**, which is why the field is unusable rather than merely imprecise.
`lastday_price` is **closed as a question** after four falsified mechanisms in four days: it read
706.99 at the pre-market, the open *and* the close on 09-25, 29c wrong all day. **Stop predicting it.**

##### 3. Inherited claims are not checked facts — **FOURTH WEEK, and the catch rate is accelerating**

**Nine catches now, four of them this week**, and one was **six hours old** — the shortest-lived claim
yet caught. **Catch (9) is found by this review and is the worst-shaped one yet.**

- ⚠⚠ **(9) A COUNTER WHOSE UNIT IS WRONG, found this run.** Every close journal reports §5.1–§5.4 as
  untested for *"the Nth consecutive **session**"* — **29 on 09-23, 33 on 09-24, 37 on 09-25.** ⚠ **It
  increments by three or four per trading day. Sessions increment by one.** The account has operated
  **18 sessions** since 2026-09-01, so **"thirty-seven consecutive sessions" is more than twice the
  account's entire age and cannot be sessions under any reading.** It is a **run** counter — four
  routines a day — carrying a session label. ⚠ **This is worse than catch (2)'s stale count and catch
  (7)'s miscount, because the value is not stale and the arithmetic is not wrong: re-running the check
  reproduces the same number, and only comparing it against the calendar exposes it.** The fact it
  encodes is true and unchanged (§5 has never had an operand); **only the unit is fiction.** Corrected
  in the Trades-closed section above. **A count that grows faster than the thing it claims to count is
  not measuring that thing.**

- **(6) A SCOPE CLAIM, 09-25.** The open run wrote *"routine 2 is the only routine that runs with
  `is_open: true`."* **False** — routine 3 runs at 12:30 mid-session and reads TRUE too, falsified by
  the run that read it, from its own clock. ⚠ **The most dangerous shape on the list, because it was
  not a number to re-pull but a statement about the system's own shape, which no data call would ever
  contradict.**
- **(7) A MISCOUNT INSIDE A VERIFICATION CLAIM, 09-24.** A run wrote that it had *"verified all twelve
  keys present"* in the `state.md` block. **There are thirteen.** The check was almost certainly run
  correctly; **it is the report of the check that was wrong**, which is worse, because a wrong count in
  a sentence containing the word "verified" is exactly what a later run will not re-check. *(Re-parsed
  this run: 13 keys, all present.)*
- **(8) A MEASUREMENT PRESENTED AS A CALIBRATION, 09-25.** The midday run wrote that the partial bar's
  v 69,713 was *"49.5% of the four-session mean volume against 49.0% of the session elapsed — the
  volume tracks elapsed session time almost exactly."* **The completed session's volume was 164,682,
  16.9% above that mean, so the partial held 42.3% at 49.0% elapsed.** ⚠ **The claim was
  arithmetically correct and its DENOMINATOR was the error. A ratio against a prior-day mean looks
  like a measurement of the current day and is not one.**

Prior catches, unchanged: (1) a false superlative that survived three runs; (2) a stale thesis count;
(3) and (4) two opposite `lastday_price` mechanisms, each falsified the next day; (5) a **truncated
series** that had silently dropped its own largest member.

⚠ **The standing consequence, four weeks in: a superlative, count, mechanism, series or calibration
inherited from a prior run is not a checked fact — it is the cheapest claim to write and the most
expensive to verify. Assume the next one you are handed is wrong until you have pulled the source.**
This review acted on that rule four times: it recounted the 73 theses from `research_log.md`,
recomputed all 15 daily excesses rather than repeating the "every positive day was a down day" claim,
corrected Week 3's "the widening is the headline," and found catch (9) by checking a counter against
the calendar. ⚠ **Three of those four inherited claims were sound and one was not, which is the ratio
that makes the rule expensive to follow and necessary anyway.**

##### 4. The satellite sleeve has never been deployed — **FOURTH WEEK. NAMED. And this week the diagnosis changed.**

**18 sessions. 73 theses. 0 positions. 0 satellite orders. 0 exits.** Nothing was gated at any point in
any of the four weeks: breaker INACTIVE, weekly cap 0 of 3 every week, sleeve empty,
`TRADING_ENABLED: true` since 09-03, no restricting note in `control.md`. **§2 explicitly permits
uninvested satellite cash and §4 says the correct output of most research runs is no trade. Both rules
were followed and no rule was breached in any of the four weeks.**

What the cumulative result *is*, without euphemism: **a 70% index tracker with a 30% cash drag, plus a
research process that has produced 333KB of rejected theses and no trade** — **~5.57pp of account
return given up per rolling 12 months** at VOO's current 12-month return, up from 4.97pp last week.

**What changed this week is the diagnosis, not the number.** Three reviews pointed at evidence
availability. **JBL falsifies that** — the funnel produced the named, allocated, verbatim-from-an-8-K
candidate and it was still not a trade, on a ground (capital paid in, consignment, repurchase at cost)
that **widening the evidence bar would have let through.** Combined with ELMT — which withheld nothing,
disclosed a $124.75M figure, and was ineligible under §3 at any level of disclosure — **the log now
holds two independent proofs that evidence is not the binding constraint.**

⚠ **And the pressure to lower the bar rose this week in two new ways, both worth naming rather than
acting on.** First, **the funnel finally produced the candidate a month of rejections implied was
missing, and it still was not enough** — which reads as "nothing will ever be enough." Second, **the
account is up +0.39% and simultaneously lagging its benchmark by exactly the cash drag**, which makes
"deploy something" feel like the obvious reading of a green week. **Neither is this seat's call. §4's
own position governs: a run that finds nothing is a successful run. If the bar is to move, that is a
`strategy.md` change and only the human may make it.**

##### 5. **NEW — the reject board's winners cluster in one theme, under five different rules**

Full working in the scoreboard above. Stated here because it is a pattern across weeks rather than an
incident: **six of the top six excesses on a 65-name board are AI / data-centre hardware and
semiconductors, rejected between 09-01 and 09-09 under five different §4 tests.** Each rejection was
individually correct. The aggregate is that §4's three most active tests each independently exclude a
running theme, for reasons that are properties of hot themes rather than of these companies. **This is
offered as input to the human's open question about the bar, not as a recommendation to change
anything.**

##### 6. The temptation series — **and this is the one item that improved**

Two standing pulls recurred every session this week and were refused every time. **Core VOO was not
stamped with a `highest_close`: 55 runs.** A mark on VOO would **fabricate a §5.4 trailing stop on the
one position §5 exempts**, a stop that could eventually sell core on a drawdown, which §7 forbids
outright. **GNRC was not looked at: 27 refusals.** It is the named counterparty in the Amazon
announcement — first-order and outside §4 at any price.

⚠ **The improvement, and it is real: this week the runs started grading their own refusals instead of
counting them.** The 09-25 close recorded its Step 2 refusal as **strong** (a dedicated write step, a
fresh official close in hand, an empty field to put it in) and its GNRC refusal as **weak** (zero
`move` calls, zero `quote` calls, no research step, nowhere to put a number — *"the refusal cost
nothing"*). **A bare count of 27 overstates the evidence, and the log now says so itself.** The count
accumulates fastest on exactly the runs where it means least.

The sharpest instances this week were the 09-25 **midday** and **close** Step 2 refusals — the midday
one because a *dedicated repair step* is if anything the sharper temptation, since "backfill the
missing mark" reads as fixing an omission rather than adding a row.

⚠ **Week 3's conclusion still stands and is not softened by the grading: *"I do not think I am getting
better at resisting this; I think the supply of plausible framings is simply not running out."*** The
GNRC costume list did stop growing this week — no new rationale in seven sessions, where previously
there was one per run. **Converging rather than growing, which is mildly encouraging and is not the
same as solved. The defence has to be structural.**

##### 7. Standing rules — now eight, still one root cause

(i) Screen on the mechanism before running filters. (ii) Verify what the company currently sells,
post-spin. (iii) Verify the news is new to the company's own disclosure. (iv) A recurring ticker is a
warning, not corroboration. (v) A market-structure fact is not a supplier relationship. (vi) A shared
cause is not a mechanism. (vii) Check whether the named beneficiary makes the part itself. (viii) Read
which direction the disclosed dollar figure moves — and whether it is revenue at all.

**All eight remain the same failure: supplying the causal link yourself, then finding a source merely
adjacent to it.**

**Rule (viii) had the week, and acquired its definitive worked example.** It was written 09-18 off
TotalEnergies/GIP's $1.8B of capital paid *in*. This week it caught Bloom's **$25B financing ceiling
available to somebody else**, SoftBank's **$11.1B paid in to a private recipient**, BBY's **"small
fee" — a cost at the candidate, described in language that reads like a partnership benefit** — and
then **JBL's $1.7 billion: named, allocated, quoted verbatim from an 8-K, and capital paid in by the
customer, held in consignment as bailee, repurchased at cost.** ⚠ **A large, real, sourced,
prominently-placed number is not a dollar path. JBL is the worked example to reach for first.**

**Rule (v) had the second-widest week**, with a new and more dangerous sub-shape: **an unnamed supply
base made to look nameable by an exact figure and a named component category** ($1.7B of "memory
components", with no manufacturer disclosed anywhere). ⚠ **The blank looks fillable because the
suppliers are countable on one hand. The source left the blank; filling it in is not research.** Also
the **multiple-award ceiling across fifteen vendors** read as one company's revenue (RDW, "$980M").

**Rule (vi) fired on BG/ADM and on GPC/ORLY/LKQ**, and the week sharpened it: **a convergence between
two named companies is more dangerous than a divergence, because agreement looks like corroboration
when it is in fact the clearest possible statement that the input is a market variable.** The third
face is a **competitor's earnings print** read across (AutoZone → GPC/ORLY/LKQ). **The giveaway never
changes: the sentence needed an "and also."**

**A government action is not a Company A**, and this week produced the full-market-scale version — the
10-year at ~5.22%, the 30-year at ~5.48–5.50%, Brent near $106, PMIs at 52- and 59-month highs. ⚠
**Scale makes it more convincing, not less. Every "who wins from higher rates / higher oil" answer
needs an "and also."** The counter-case stands and must not be over-applied against: an FDA advisory
vote enables a *named* company's product and that company has a *named* supplier — a real two-party
chain.

##### Nothing that stopped recurring

For completeness, since a review that only lists what recurs is not measuring: **no item named in weeks
1, 2 or 3 was resolved this week.** Items 1, 2, 3 and 4 are all in their fourth week. **Item 2 got
worse** (intermittent, and it reached §2). **Item 4's diagnosis changed**, which is progress on
understanding rather than resolution. **Item 6 improved** — the refusals are now graded rather than
counted. **Item 5 is new.**

---

#### Housekeeping

- **Weekly counter reset: DONE.** `new_positions_this_week` → **0** (was already 0 — nothing was opened
  this week, or any week), `week_of` → **2026-09-28** (ISO Monday of next week; confirmed against
  `clock`, whose `next_open` reads 2026-09-28T09:30). Monday's runs will re-check, find the anchors
  match, and correctly do nothing. **The reset does not depend on this review having run**, so a missed
  Friday cannot leave the §6 cap stuck.
- **Monthly archive rollover: NOT DUE, and deliberately NOT run early.** Every **entry** in
  `research_log.md`, `trade_log.md` and `journal.md` is dated **2026-09**, which is the current month;
  nothing predates it, so nothing moves and no archive index line is written. Checked by header, not by
  grep — `research_log.md` contains earlier dates, but every one is a date cited *inside a thesis body*.
  **Next rollover is the first Friday review of October — 2026-10-02.**
- **⚠ On running it early, which the close run flagged as an option: the answer is no, and here is the
  reasoning so a human can overrule it.** The rollover is defined as moving entries **older than the
  current month**. Running it today would archive the live month — and this week's runs read exactly
  those entries to build the reject board, recount the theses and write this review. **Splitting the
  current month across two files for five sessions buys five days of smaller files at the cost of
  making those five days read a split log**, which is the failure mode the archive exists to prevent,
  arriving early. **The 2026-10-02 rollover moves the entire September corpus in one designed
  operation, and it is five trading sessions away.** A human who disagrees should say so in
  `control.md`; the agent will not decide it on its own.
- **⚠ FILE SIZE — TENTH CONSECUTIVE FLAG, and the numbers are worse than last week's.**
  `research_log.md` is **333KB**, up from **226KB** last Friday — **+107KB in one week on 27 theses**,
  a faster rate than the +75KB the Week 3 review already called urgent. `journal.md` is **162KB** (was
  102KB). `positions.md` is **36KB**, `state.md` **55KB**, `trade_log.md` **6KB**, `alerts.md` **3KB**,
  plus the human-owned `strategy.md` **6KB** and `control.md` **2KB** — **589KB that every run is
  instructed to read in full**, or **681KB** including this file. ⚠ **The 09-25 close run made the
  honest observation and it is promoted here: it collapsed the midday `positions.md` block from ~95
  lines to ~25 and still left both files it owns NET LARGER, because its own output outran the
  collapse. A mitigation that is outrun by the mitigating run's output is not a fix.** The October
  rollover is the fix, and it will move essentially the whole corpus at once.
- **Alert hygiene: `alerts.md` is EMPTY.** Zero open incidents, zero SYSTEMIC, zero resolved. No
  `push-failure`, no `guard-violation`, no `selftest-abort`, no `circuit-breaker` in the repo's
  history. **No guard violation has ever occurred, so no routine prompt is steering the agent at a
  protected file** — the systemic-prompt-bug case this section exists to surface **does not apply.**
  `selftest.py` passed all five checks on **every run of this week**, including this one at 16:45 ET.
- **Two operational events this week did NOT produce alerts, correctly, and are recorded here instead.**
  (a) A `#` written into a `state.md` fenced-block value on 09-24 silently truncated a 5,046-character
  run note at the parser — caught before commit by running `common.read_state()` against the file. **No
  gating field was affected and nothing was lost**, but it is the repo's own continuity mechanism
  failing silently, and it is now a standing rule. (b) A Perplexity **HTTP 500** on 09-24, on the
  research plane — **the first instance there**, recovered on a reworded retry, and **it did not recur
  on 09-25.** Single occurrence; no alert. Both feed open human item (6): **`selftest.py` certifies a
  healthy system without probing the endpoints every routine depends on.**
- **Hand-off to the 2026-09-28 pre-market run** (next session Monday 09:30 ET, confirmed from `clock`):
  - **No high-water backfill is owed. `highest_close` is ABSENT, not stale** — there has never been a
    satellite position, so there is no field and nothing was skipped. **Do not backfill anything.**
  - **The 27 rejections from this week are not a queue and must not be rehabilitated at a different
    price** — JBL above all, where **the price was never the problem.** ELMT must not be screened a
    fourth time at any level of disclosure.
  - **No unscreened event has accumulated 09-21 through 09-25.** Every survey item was worked. There is
    no live research item; the funnel is empty and that is its normal state.
  - **A bar dated today is PARTIAL while the market is open**, and routines 2 and 3 both read
    `is_open: true`. **`n` and `v` are a smell test, not a measurement — the reliable discriminator is
    the clock.** When in doubt, use the last completed session.
  - **Expect a twenty-eighth GNRC framing**, and grade the refusal rather than counting it.

---

#### For the human

**Seven open items. None is the agent's to decide, and no run has reinterpreted any rule while
waiting.** Items 1, 3, 5 and 7 changed this week.

1. **The §4 priced-in filter reads a drawdown as "priced in" — and now has a THIRD defect shape.**
   Fourth week open. Shape one (a fall read as priced-in) is at **nine instances**, newest CNC −6.44%
   on 09-23, plus three near-misses that cleared only because the fall was fractionally too small.
   **Shape three is new on 09-25: a genuine rise UNRELATED to the news, swept up by the window** — JBL
   +4.97% over five sessions on a grind whose largest day was +1.72% and whose **news day moved it
   +0.63%.** §4 conditions on having moved 4% *"on this news"*; the mechanized check cannot see
   causation. ⚠ **The defect is sign- and causation-blindness, not the threshold.** The bill: **LITE,
   rejected on a −7.35% drawdown, is +11.16% against VOO over fifteen sessions.** **LITE and MU must
   not be merged** — MU failed on a genuine run-up (the rule working as designed, costing money,
   nothing to change). Fix is a human editing §4 or `alpaca.py move` — **or an explicit decision to
   leave it, which is a perfectly good answer and would close the item.**
2. **The same filter reads an event move absorbed before it looks as "passes."** Same root cause as
   (1), opposite direction. ⚠ **AKAM (09-25) is the worst instance recorded and the first MULTI-SESSION
   round trip: it read `priced_in: false` at +3.19% while its closes ran 104.53 → 117.435 (+12.35% in
   ONE session), then 118.33, 118.42, then 110.44 (−6.74%). A +12.35% event move and a −6.74% give-back
   fell inside the same five-session window and netted to a passing +3.19%.** Prior instances (QCOM,
   AVAV) were intraday round trips; **the round trip no longer has to hide inside a single bar.** AKAM
   was never at risk (first-order killed it), **but a second-order beneficiary of the same chain would
   have been waved straight through.**
3. **The satellite sleeve is structurally undeployed — 73 theses, 0 positions, 18 sessions. FOURTH WEEK
   RAISED, and the diagnosis changed this week.** Previous reviews pointed at evidence availability and
   asked whether the acceptable evidence for a quantified segment should widen. **JBL falsifies that
   framing**: the funnel produced a named US-listed supplier with an allocated figure quoted verbatim
   from an 8-K, and it still was not a trade, because the $1.7B is **capital paid in, held in
   consignment as bailee, and repurchased at cost.** ⚠ **Widening the evidence bar would have let this
   through.** The binding constraint has **five known forms**, and **only two are addressable by
   widening**; form (v) would be made **worse** by it. **The real question for a human is therefore not
   "is the evidence bar too high" but "is a second-order catalyst strategy with a two-quarter horizon
   and a $10B floor able to produce trades at all from public disclosure" — and, if the answer is
   rarely, whether the 30% target should sit in cash or in the index while it waits.** **The cost of
   leaving it is ~5.57pp of account return per rolling 12 months, up from 4.97pp last week.**
4. **The core's divergence from VOO is the 09-03 entry gap, not tracking error.** Measured from the
   706.74 fill the core tracks VOO to **0.0000%**, fourth week running. **Discharged; keep measuring it
   from the fill.** No action.
5. **The broker/official price gap is NOT cosmetic, and this week it proved INTERMITTENT.** It produced
   an instance on **every session this week**: a $14.86 error in the unexpected direction (09-21), a
   full **sign error** on the day's P&L (09-22), a **100% artifact** on a zero-move day *and* the first
   sign flip of a **§2 quantity**, `rebalance_delta` (09-24), and a $23.38 artifact on a real move
   (09-25). ⚠ **On 09-25 all three runs agreed in sign; on 09-24 the same quantity disagreed. A run that
   checks one basis and finds agreement learns nothing.** `lastday_price` is closed as a question — four
   falsified mechanisms, both signs observed, 29c wrong all day on 09-25. **Whether the tooling should
   read closes from `bars` by default is a human's call, and four weeks of accumulated evidence says it
   should.**
6. **`selftest.py` certifies a healthy system without probing the two endpoints every routine depends
   on to price anything.** It passed all five checks on 09-11 while `clock` returned 500 and
   `quote`/`bars` returned 504, **and on 09-24 while a `perplexity.py` query returned 500 — the first
   instance on the RESEARCH plane.** The 09-24 transient did not recur. **Until a human changes it:
   probe by hand, never infer data-plane health from a green selftest, and check exit codes — never
   infer thin news from empty results.**
7. **`alpaca.py move` cannot see an after-hours event, and neither can the 09:35 re-validation that
   exists to catch exactly this.** ⚠ **Unlike (1) and (2), this fails in the direction of TAKING a
   trade rather than skipping one**, which is why it is listed last and should be read first. **AKAM
   generalises it: the entire +12.35% event move was hidden from the filter by a later give-back inside
   the same window, and no 09:35 re-validation would have surfaced it either. The blindness is not only
   to after-hours events — it is to ANY event move the window later cancels.** It has cost zero only
   because no plan has yet carried a BUY intent — **an absence of exposure, not a mitigation.**

**One item the agent reached but did not decide, and will not:** Shopify is a Canadian issuer trading
as common stock on a US exchange, which §3's *"US-listed common stock"* does not obviously settle. It
did not matter on 09-24 (SHOP died on the priced-in filter at +9.61%). **A future run reaching this
with a live candidate must put it to the human rather than decide it from this seat.**

**And the one-line version of everything above:** the system is following every rule it was given,
writing down what it rejects with unusual honesty, and **has not bought anything in four weeks.** What
changed this week is that the comforting numbers ran out and the diagnosis got sharper: **the
constraint is not the quality of the evidence, and a better-sourced candidate will not fix it.** The
rules are working. **Whether these rules can ever produce a trade is now the only question that
matters, and it is the human's to answer.**

---

### Week ending 2026-09-18

*Posted to ClickUp as task `86bc3bzz6` — https://app.clickup.com/t/86bc3bzz6 — separate from the
daily summaries.*

**Breaker: INACTIVE.** No halt, `halt_triggered_at: none`, `consecutive_closed_losses: 0`, weekly cap
**0 of 3** used. Nothing was gated this week; nothing was blocked from trading.

**Third weekly review in this repo's history.** The book has now operated **13 sessions**
(2026-09-01 → 2026-09-18), **5 of them this week**. Theses written since inception: **46**. Theses
accepted: **0**. **The satellite sleeve has never held a position and has never placed an order.**
The account's entire order history remains one row: the 09-03 core VOO buy.

---

#### The §1 answer, first — and the sign on the short windows is the opposite of the answer

**No. The satellite sleeve is not beating what the same capital would have done in VOO, and on the
window §1 actually specifies it is not close.**

§1 sets a **rolling 12-month** test. Over the trailing 12 months VOO's total return is **+16.55%**.
The satellite sleeve returned **0.00%**, because it has been $30,000 in cash for every session of its
existence. A sleeve at 0% against a benchmark at +16.55% has an excess of **−16.55pp**. The account
is 13 sessions old and cannot fill a 12-month window with its own history — but **the benchmark leg
of the §1 test does not require the account to be old enough**, and it is the leg that answers the
question.

**The short windows say "ahead," and they say it for the third week running, and they are still not
an answer.** This week the sleeve is **+0.095pp** ahead of VOO; since inception **+0.430pp** ahead.
Both are real arithmetic. Both are **0% exposure to a market that fell**, which is a number the
sleeve produces automatically on every red week and gives back on every green one. The two previous
reviews each named this framing and each predicted it would recur. **It recurred, in this exact row,
for the third time.** It is recorded here as a property of the measurement, not as performance.

**The structural cost, stated as a number:** a satellite sleeve parked in cash at the §2 target
weight gives up **0.30 × 16.55% ≈ 4.97pp of account return** over a rolling 12-month window against
a benchmark that returns what VOO has returned. That is the honest size of the thing this review has
now reported three weeks in a row.

---

#### The three numbers

**Both legs of every comparison below come from official closes (`bars --adjustment all`).** Never a
`positions` field, never `equity − last_equity` — see Recurring Errors §2, which this week stopped
being a theoretical concern and produced a reported number that was wrong by $106.

Official-close equity today: **$99,515.65** (99.046311231 × 701.85 + $30,000 cash). The broker
reports **$99,644.41**. The $128.76 difference is the two-price artifact, not a discrepancy to
investigate.

##### 1. Core return — tracking, not skill

| | Value |
|---|---|
| Fill (2026-09-03) | **706.74** |
| VOO close 2026-09-18 | **701.85** |
| **Core return from the fill** | **−0.692%** |
| **Core divergence from VOO over the same window** | **0.0000%** |

The core sleeve **is** VOO, so measured from its own fill it tracks the benchmark exactly. The
**−0.48% entry gap** — the 09-03 order filled +0.4834% above the 09-02 close of 703.34, on a day VOO
gapped up — is a permanent level offset that appears whenever the core is anchored to a close rather
than to its fill. **It is not tracking error and it is not skill.** Third review in which this is
restated, and it remains the only reason the core ever looks different from the index.

Core weight on official closes: **69.85%** (broker basis 69.89%). Inside the §2 65–75% band; no
rebalance due, and §2 acts at the band edge in any case.

##### 2. Satellite return

| | Value |
|---|---|
| Realized P&L on everything closed | **$0.00** — nothing has ever closed |
| Unrealized P&L on everything open | **$0.00** — nothing is open |
| Capital allocated to the sleeve | **$30,000** (30.15% of equity on closes) |
| **Satellite return** | **0.0000%** |

Zero positions for the **twentieth consecutive session**. Every dollar of the sleeve has been idle
for its whole life: **13 sessions since inception, 11 since the core fill funded the 70/30 split.**

##### 3. Satellite versus the same capital in VOO — the number that answers §1

The dollar-weighting is trivial this week and the reason it is trivial is the finding: **there are
no positions to weight.** Per the routine, idle satellite cash enters the measurement at **0%
return** with **weight 1.00**, because choosing not to deploy is a decision the strategy made and its
cost belongs inside the number. With no position rows, the dollar-weighted excess collapses to
exactly **minus VOO's total return over the window**.

| Window | Elapsed | Satellite | VOO (total return) | **Dollar-weighted excess** |
|---|---|---|---|---|
| Week | 5 sessions | 0.00% | **−0.095%** | **+0.095pp** |
| Since inception | 13 sessions | 0.00% | **−0.430%** | **+0.430pp** |
| 1 month | account has 13 sessions — **VOO leg only** | 0.00% | **−0.509%** | **+0.509pp** |
| 3 months | account has 13 sessions — **VOO leg only** | 0.00% | **+2.291%** | **−2.291pp** |
| **12 months (rolling)** | account has 13 sessions — **VOO leg only** | 0.00% | **+16.552%** | **−16.552pp** |

**Nothing above is annualized.** The account is thirteen sessions old; the 1M, 3M and 12M rows carry
the benchmark leg over its true window against a sleeve that was flat for all of it, and the elapsed
period is stated rather than scaled.

**Read the sign changes down that column.** The same undeployed sleeve reads **+0.51pp** over one
month and **−16.55pp** over twelve, and the only thing that changed is which window was chosen.
**The window §1 names is the 12-month one.**

##### The account as a whole, for completeness

| | Week | 1M | 3M | 12M (rolling) | Since inception |
|---|---|---|---|---|---|
| Account | **−0.067%** | n/a (13 sessions) | n/a | n/a | **−0.484%** |
| VOO (total return) | **−0.095%** | −0.509% | +2.291% | **+16.552%** | **−0.430%** |
| Excess | **+0.029pp** | — | — | — | **−0.055pp** |

**The week's +0.029pp is 30% cash in a down week and nothing else** — 0.6985 × (−0.095%) = −0.066%,
which is the account's return to the basis point. **Since inception the account is −0.055pp behind
the index despite holding 30% cash through a period in which the index fell**, and that residual is
the 09-03 entry gap working through the core weight. Neither number is skill in either direction.

**Sleeves (official closes):** core **69.85%** | satellite **0.0%** (count 0) | cash **30.15%**
**Breaker:** INACTIVE

---

#### Trades closed this week

**None.** The table is empty for the **third consecutive week**, and nothing has ever been closed in
this account.

| Ticker | Thesis | Held | Exit rule | P&L | Excess vs VOO |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

**Which exit rules are firing: none — and the distinction this review is asked to draw cannot be
drawn.** The routine asks whether every exit is the −7% hard stop (a system discovering its theses
are wrong at a fixed price), whether time stops dominate (timing windows written too optimistically),
or whether invalidations fire (the rule working as designed). **All three questions require exits to
have happened.**

§5.1 has no thesis to invalidate, §5.2 no `timing_window` to expire, §5.3 no `entry_price` to measure
−7% against, §5.4 no `highest_close` to measure −10% against. **`sell_rule_status` is absent, not
blank.** All four remain **untested code paths after 20 sessions**, and §5.4 has never been armed —
it arms on the first *satellite* fill, which the 09-03 core buy was not.

**Twenty sessions of "no exits" is the absence of a subject, not a clean bill of health**, and a
future review must not read the string of empty tables as evidence the sell rules work.

---

#### Thesis scoreboard — including rejects

**This week: 16 theses written, 0 accepted, 16 rejected.** Acceptance rate **0%**.
**Since inception: 46 theses, 0 accepted, 46 rejected.** Acceptance rate **0%**, third week running.

Of accepted theses now closed: **n/a — there are none.** How many reached their timing window with
the predicted business change, how many were invalidated, how many stopped out: **zero, zero, zero,
and the denominator is zero.** This section cannot begin to do its job until the sleeve fires once.

##### Where the 16 died

Counted by **primary** failure point — the test the log records the thesis dying at first. Several
died independently at two or three.

| Failure point | n | Names |
|---|---|---|
| **Part 1 — no Company B, or the mechanism needs a second clause** | **9** | BWXT, packaged food, CRWV, Lennar, and 5 unnamed |
| Part 2 — magnitude / segment share unquantifiable | 4 | CART, AVGO, GFS/MRVL, BLK |
| Part 3 — timing beyond two quarters | 3 | LEU, and 2 unnamed |

**Part 1 is still the dominant failure point — 9 of 16 — and the constraint behind it is unchanged
from the first two weeks:** the source names the transaction and no US-listed Company B appears
anywhere in it. **Standing rule (v) alone accounted for three of the nine and the log calls the
09-16 one its "seventh instance this month."**

**What is new is a second, distinct constraint sitting one test further down.** Four times this
week — Kroger↔Instacart (09-14), and on Friday GF↔Marvell, Centrus↔Antares and TotalEnergies↔GIP —
**both parties were named in the source and the number was withheld.** *"Financial terms were not
disclosed."* Part 1 passes; part 2 cannot be written without inventing the magnitude.

**That is the week's structural finding, and it is a correction to an implication of the first two
reviews rather than a reversal of them.** Anonymity is still the larger constraint. But those reviews
treated the unnamed counterparty as *the* binding constraint, which carries the suggestion that
naming one gets you a thesis. **It does not** — four times this week the source named both parties
and the thesis died anyway.

##### Rejected theses — what happened to them since

Measured from the close each rejection was made against, to the 09-18 close, against VOO total return
over the **identical** window. **Both legs from `alpaca.py move`**, whose VOO output was verified
this run to match `bars --adjustment all` to the cent at all eleven session counts. No mixed-source
comparison anywhere below.

| Ticker | Rejected | Sess | Name | VOO | **Excess** | Rejection reason |
|---|---|---|---|---|---|---|
| **HPE** | 09-02 | 11 | **+17.43%** | −0.21% | **+17.64%** | part 1 — read-across |
| **LITE** | 09-03 | 10 | **+10.00%** | −1.25% | **+11.25%** | **priced-in veto (−7.35% drawdown)** |
| **MU** | 09-01 | 12 | **+8.81%** | +0.24% | **+8.57%** | **priced-in veto (+5.27% run-up)** |
| CRDO | 09-09 | 7 | +4.83% | +0.15% | **+4.68%** | parts 1/2 |
| COHR | 09-09 | 7 | +4.51% | +0.15% | **+4.36%** | parts 1/2 |
| AVGO | 09-16 | 2 | +5.40% | +1.25% | +4.15% | part 2 |
| GFS | 09-10 | 6 | +4.06% | +0.74% | **+3.32%** | priced-in +4.53% / p3 / headline |
| CLF | 09-04 | 9 | −0.04% | −0.85% | +0.81% | thesis + §3 |
| QCOM | 09-09 | 7 | +0.91% | +0.15% | +0.76% | §4 headline name |
| LHX | 09-11 | 5 | +0.64% | −0.10% | +0.74% | priced-in (−4.47% drawdown) |
| M | 09-11 | 5 | +0.18% | −0.10% | +0.28% | part 1 — shared cause |
| YPF | 09-09 | 7 | +0.37% | +0.15% | +0.22% | §3 |
| MDT | 09-08 | 8 | −0.29% | −0.33% | +0.04% | part 2 |
| LMT | 09-10 | 6 | +0.67% | +0.74% | −0.07% | headline name / p3 |
| CRWV | 09-15 | 3 | +0.40% | +0.80% | −0.40% | part 1 — "and also" clause *(priced-in also failed, on a −7.12% **drawdown**)* |
| PBR | 09-09 | 7 | −0.60% | +0.15% | −0.75% | §3 |
| TBBK | 09-10 | 6 | −0.13% | +0.74% | −0.87% | §3 |
| BWXT | 09-14 | 4 | −0.74% | +0.36% | −1.10% | part 1 — rule (v), no named supplier |
| NOC | 09-01 | 12 | −1.03% | +0.24% | −1.27% | part 2 — ~1% of revenue |
| GDOT | 09-10 | 6 | −0.60% | +0.74% | −1.34% | §3 |
| CAT | 09-08 | 8 | −1.71% | −0.33% | −1.38% | parts 2/3 |
| EC | 09-09 | 7 | −1.43% | +0.15% | −1.58% | §3 |
| WDC | 09-01 | 12 | −1.95% | +0.24% | −2.19% | part 1 — post-spin |
| ABT | 09-08 | 8 | −2.85% | −0.33% | −2.52% | part 2 |
| AVGO | 09-08 | 8 | −2.96% | −0.33% | −2.63% | part 1 |
| AEP | 09-01 | 12 | −2.46% | +0.24% | −2.70% | parts 2+3 |
| VIST | 09-09 | 7 | −3.18% | +0.15% | −3.33% | §3 |
| CASH | 09-10 | 6 | −3.55% | +0.74% | −4.29% | §3 |
| LHX | 09-02 | 11 | −4.93% | −0.21% | −4.72% | part 2 |
| SLI | 09-11 | 5 | −4.92% | −0.10% | −4.82% | §3 |
| CCB | 09-10 | 6 | −4.28% | +0.74% | −5.02% | §3 |
| RTX | 09-01 | 12 | −5.43% | +0.24% | −5.67% | part 1 — own inference |
| LITE | 09-09 | 7 | −5.71% | +0.15% | −5.86% | parts 1/2 *(second rejection)* |
| LHX | 09-01 | 12 | −5.75% | +0.24% | −5.99% | part 3 |
| FN | 09-09 | 7 | −7.16% | +0.15% | −7.31% | parts 1/2 |
| **CART** | 09-14 | 4 | −8.36% | +0.36% | **−8.72%** | part 2 — no dollar figure |
| EQT | 09-10 | 6 | −9.04% | +0.74% | −9.78% | part 2 — 0.14% of volume |
| MTZ | 09-09 | 7 | −10.89% | +0.15% | −11.04% | parts 1/2/3 |
| GLW | 09-09 | 7 | −10.90% | +0.15% | −11.05% | priced-in +11.63% / p3 |
| **LEU** | 09-10 | 6 | −12.42% | +0.74% | **−13.16%** | §3 / priced-in / p2 |

**13 of 40 beat VOO; 27 lagged. Mean excess −1.57%, median −1.34%.**

Today's four rejects (GFS/MRVL, LEU, BLK, and one unnamed) have **zero elapsed sessions** and are not
on the board. **AVGO's 2-session row and CRWV's 3-session row are not measurements either** — they
are logged so a future review re-measures them rather than quoting them.

**The board moved in two directions at once this week, and the two must not be merged.** Last week:
9 of 33 beat VOO, mean **−0.51%**. This week: 13 of 40 beat, mean **−1.57%**. **More names ran
without us and the average reject did worse** — the distribution widened at both ends as windows
lengthened. Neither the count nor the mean is the headline; the widening is.

By cohort, as windows lengthen:

| Cohort | n | Beat VOO | Mean excess |
|---|---|---|---|
| Week 1 rejects (9–12 sessions) | 10 | 4 | **+1.57%** |
| Week 2 rejects (5–8 sessions) | 26 | 8 | **−2.78%** |
| Week 3 rejects (2–4 sessions) | 4 | 1 | −1.52% |

##### Rejects that went on to work — right for the right reason, right for the wrong reason

**The top three excesses on the board are unchanged from last week and are still the same two
findings, which must stay separate:**

- **HPE (+17.64%) — rejected correctly by the rule, unprofitably in hindsight.** T-2026-09-02-02 was
  a Dell→HPE *read-across*: Dell's print implies HPE's will be good. §4 requires news about Company A
  to change Company B's **economics**; a read-across is an inference about **information**. It died
  at part 1 and it should have. HPE's own earnings then landed and the stock ran. **The thesis's
  underlying prediction came true for a reason the thesis correctly identified as not a §4
  mechanism.** The read-across screen is right and it has now cost ~18pp on one name. **Both
  statements survive; neither is grounds to loosen it.** Note it has given back 2.2pp since last
  week — the bill is real but it is also still moving.
- **LITE (+11.25%) and MU (+8.57%) — the priced-in filter vetoing its own winners, third week
  running.** These two remain the **first- and third-largest positive excesses on a 40-name board**,
  and they are **the only two candidates in the repo's history that passed the four-part thesis and
  were then killed by the priced-in filter.** They are still not the same finding: **MU** failed on
  a genuine **+5.27% five-session run-up** — the rule doing exactly what it was written to do,
  costing money, nothing to change. **LITE** failed on a **−7.35% drawdown** read as
  `priced_in: true`, because `move` tests absolute magnitude. **A decline is close to the opposite of
  "the market has already paid for this news."** That is the rule doing something nobody designed,
  it is open human item (1), and it is now three weeks old with the largest single excess attached.
- **The drawdown defect fired again this week, and this time it is in the current cohort: CRWV,
  09-15, `priced_in: true` on a −7.12% five-session *fall* (89.335 → 82.97).** It cost nothing —
  the thesis died independently at part 1 on an "and also" clause, and CRWV is −0.40% against VOO
  since. **But the filter's verdict was reached on a decline for at least the sixth time**
  (LITE −7.35%, LMT −3.61%, LHX −4.47%, CRWV −7.12% among them), and the only reason this instance
  is free is that another test happened to catch the name first.

##### Rejects that went nowhere — the filters did their job, and say so

**27 of 40 lagged the index, mean excess on the losers deeply negative.** The four-part test keeps
selecting correctly in aggregate: **LEU (−13.16%)**, GLW (−11.05%), MTZ (−11.04%), EQT (−9.78%) and
CART (−8.72%) are the five worst names on the board and every one of them died on parts 1–3 or §3.

**Two are worth naming specifically:**

- **LEU was rejected twice, six sessions apart, and was right both times.** Rejected 09-10 on
  §3/priced-in/part 2 and now **−13.16%** against VOO; re-rejected **today** on part 3 (HALEU
  deliveries *"before the end of the decade"*, far outside §4's two-quarter ceiling). A recurring
  ticker is a warning, not corroboration — standing rule (iv) — and here the warning was correct.
- **CART is the week's most instructive *correct* rejection**, because it is the one that nearly got
  through. Kroger named Instacart on its FQ2 call — the first time in eleven sessions a source named
  the counterparty — and the 09-14 journal records the pull to treat that as most of the work and
  **size the "incremental prescription basket" anyway**. No dollar figure existed in the release, the
  8-K, the IR summary or the call coverage. A fabricated number would have carried the thesis past
  §4.2's 10%-of-revenue test into a trade. **CART is −8.72% against VOO since.** The invented number
  would have bought a loss.

##### Is the rejection rate ever wrong?

**Yes — thirteen times out of forty, and three of them expensively.** The routine's warning is that a
rejection rate which is never wrong means the filters are too loose. **That failure mode is not
present**: names run without us regularly, three ran a long way, and the board has now reversed on
itself once (week 1's cohort) and widened once (this week).

**This is still a tally, not a result, and no future review may quote it as one.** Forty
measurements over two to twelve sessions is not a sample. It is recorded because the human has a live
question about the priced-in filter and this tally is the only evidence that will ever exist for it.

**Priced-in filter, cumulative:** it has now been run on far more candidates that were later rejected
on other grounds than it has been decisive on. **It has still never once been informative in the
direction people expect.** A passing priced-in check is a veto that did not fire, never
encouragement — "has not moved" and "should have moved but didn't" produce the same number.

---

#### Recurring errors

##### 1. The reassuring framing — **THIRD WEEK RUNNING. NAMED, AND THE DEFENCE HAS NOW FAILED TWICE.**

Named in week 1, named again in week 2 with a prediction that it would recur. **It recurred on every
session of this week and in this review's own headline row.**

| | The sentence that arrived first | How it was killed |
|---|---|---|
| 09-15 | broker −0.240% vs VOO official −0.438% → "beat the index by 0.198pp" | mixed-source; official legs give −0.305% = 0.697 × 0.438% |
| 09-16 | "book −0.308% vs VOO −0.442%", **both legs official** | underexposure, not skill — arithmetic defence does not catch this one |
| 09-17 | green day, book +$768 → "the cash drag note reads better today" | the cash cost is *most* visible on a green day, not least |
| 09-18 | "book −0.067% vs VOO −0.095% on the week" | 2.9bp = 30% cash in a down week, by construction |
| **This review** | **"satellite +0.43pp since inception"** | **0% exposure to a −0.43% period, weight 1.00** |

**What is new in week 3 is that the arithmetic defence is now known to be insufficient, and it failed
in a second way.** Week 2's version was a **mixed-source** artifact, killable by taking both legs
from official closes. **09-16 produced the same flattering sentence with both legs already official**
— a correct number answering a question nobody asked. And **09-17 found a third route entirely**: no
comparison at all, just a positive dollar figure making a structural criticism easier to live with.

**Three weeks, three distinct mechanisms, one output.** The defence cannot be arithmetic and cannot be
vigilance; the only thing that has actually worked is a standing rule that the 12-month row is the
one §1 asks about, and that every favourable short-window number gets refuted in writing. **Expect
this row to be positive on every red week from here, and expect to refute it every time.**

##### 2. Broker marks versus official closes — **THIRD WEEK RUNNING, AND THIS WEEK IT ESCALATED FROM COSMETIC TO LOAD-BEARING. THE PREVIOUS TWO REVIEWS UNDER-RATED IT.**

Week 1 logged an unexplained gap. Week 2 solved the mechanism — the broker's `current_price` is a
**live bid/ask midpoint that keeps moving after the bell**, not a close, which is why the gap never
had a stable size — and filed the exposure as *"cosmetic on core, load-bearing the moment a satellite
position exists."*

**That framing was wrong, and 09-18 proved it.** The 09-18 close run **very nearly reported the day's
P&L as +$193.14 / +0.194%. The true close-to-close figure is +$87.16 / +0.0877%** — the broker's
number was **more than double the real move**, and it would have led the ClickUp summary.

The mechanism, because it is worse than a stale field:

- `last_equity` = **99,434.4356** = exactly **99.046311231 × 701.03 + 30,000** — the **stale
  midpoint** `lastday_price` carried for all four calls that day, **not** 09-17's official close of
  **700.97**.
- `unrealized_intraday_pl` = **+193.14** = 99.046311231 × (702.98 − 701.03) — built off the **same**
  wrong baseline.
- **Both legs are wrong, in the same direction, and they reconcile perfectly against each other.**
  No consistency check internal to the broker's own fields can ever detect this. **Only an external
  close can.**

**It was load-bearing with no satellite position involved at all**, in the one number a run reports
first. And the honest note from the close run on *why* it was caught: **not vigilance** — the repo
already forces closes through `bars --adjustment all`, so 701.85 and 700.97 were already on screen
demanding reconciliation. **Absent that standing rule the broker's number would have been quoted
without a second thought, because it is labelled with exactly the words you are looking for.**

**Standing rule, new this week and now in force: never `equity − last_equity` as a day's P&L, never
`unrealized_intraday_pl`. Close-to-close from `bars --adjustment all`, always.** `current_price`
702.98 against a 701.85 close is also **$1.13 — the widest gap recorded** — which is exactly how much
a `highest_close` would have been overstated by, and how far a §5.4 stop would have silently moved,
had there been a position. **Open human item (5) must be re-rated: it is not cosmetic.**

##### 3. The unnamed second-order counterparty — **THIRD WEEK RUNNING, AND IT HAS A SECOND HEAD**

Weeks 1 and 2 established the binding constraint on §4: **companies announce the transaction and
withhold the counterparty**, eight-plus instances, so part 1 has no Company B to name and the honest
output is no trade. Filling in a blank the source left blank is not research — standing rule (v).

**This week the constraint acquired a second, distinct form one test further down.** Four times —
Kroger↔Instacart (09-14), GF↔Marvell, Centrus↔Antares and TotalEnergies↔GIP (all three on 09-18) —
**both parties were named in the source and the number was withheld.** *"Financial terms were not
disclosed."* Part 1 passes; **part 2 cannot be written without inventing the magnitude, the segment
share, or both.**

**Anonymity is still the larger of the two** — 9 of this week's 16 theses died at part 1, against 4
at part 2. The correction this week forces is to an *implication* of the previous reviews rather
than to their count: naming the constraint "the unnamed counterparty" suggests that a named one gets
you a thesis. **Four times this week the source named both parties and the thesis died anyway.**

**BLK (09-18) is the cleanest specimen the log has produced.** Part 1 passed in a single clause with
no second clause needed — the thing §4 is hardest to satisfy on — and the release even carried a
number: **$1.8B**. It died at part 2 anyway, because **the $1.8B is capital going in, not revenue
coming out**, and converting one to the other required inventing a fee rate. The close journal
records this as the only reject of the day with real pull, **and part 1 passing cleanly is precisely
what the honest-broker rule warns is always available.**

**Stated as a strategy-level fact, not a complaint: §4 asks for two things public disclosure supplies
rarely — a named beneficiary and a quantified segment — and this week established that supplying the
first does not get you the second.** That is a better answer to "46 theses, zero positions" than "the
bar is too high," and it points at something a human could actually change. **The agent has not
adjusted §4 and will not.**

##### 4. The satellite sleeve has never been deployed — **THIRD WEEK RUNNING. NAMED.**

**13 sessions. 46 theses. 0 positions. 0 satellite orders. 0 exits. Nothing was gated at any point:**
breaker INACTIVE, weekly cap 0 of 3 every week, sleeve empty, `TRADING_ENABLED: true` since 09-03.
**§2 explicitly permits uninvested satellite cash and §4 says the correct output of most research
runs is no trade. Both rules were followed and no rule was breached in any of the three weeks.**

What the cumulative result *is*, stated without euphemism: **a 70% index tracker with a 30% cash
drag, plus a research process that has produced 226KB of rejected theses and no trade.** The
measurement section puts the number on it — **~4.97pp of account return given up per rolling 12
months** at VOO's current 12-month return.

**This is raised for the third time and it is not a call to lower the §4 bar.** The daily journals
record the agent noticing the pull toward lowering it on 09-09, 09-10, 09-11 and again on 09-17, and
refusing each time. **A weekly file is where a structural question belongs, and three weeks is the
point at which it stops being an observation and becomes the thing the human most needs to decide.**

##### 5. **NEW — an append-only file silently lost a day, and nothing in the system could detect it**

Not a trading error, and it belongs here because of its *shape*.

Commit **`5fe9e4c`** (the 09-16 close run) inserted its journal entry at the top of `journal.md` and,
in the same commit, **deleted the line `### 2026-09-15 (Tuesday)` — its only deletion.** The 09-15
body survived intact but was left headerless, glued to the end of 09-16's "For the next run" list.
**A full trading day's judgment became invisible to any scan of the file's headers and read as part
of the following day.** The 09-17 run caught it only by listing headers to find the template and
noticing 09-15 missing. **Nothing flagged it. Nothing could** — `commit.py` guards `strategy.md` and
`control.md`, not the *shape* of an append-only file. The header was restored, not rewritten.

**This is the same failure shape the high-water discipline exists to prevent** — a field that is
missing while every surface still reads present and plausible — arriving in the one file nobody
thought to check it in. Byte count fine, month fine, no visible gap reading linearly.

**And the 09-17 run was one edit away from repeating it**: appends go at the top of `## Entries`,
immediately above the previous day's header, which is the exact position in the exact file where the
deletion happened. **The top-of-file insert is the dangerous edit in this repo and it looks
completely routine while you are making it.** Treat as structural, not a one-off: anchor the edit on
`## Entries` plus the existing header, put both back verbatim, never replace a block that happens to
start there.

##### 6. **The temptation series — four consecutive Step 2 refusals, seven consecutive GNRC refusals, and the pattern is the finding**

Two standing pulls recurred every single session this week and were refused every time. Neither is an
error. **The finding is the rate at which new justifications arrive.**

- **Step 2 of the close routine is written in the imperative and its subject does not exist.** There
  are no satellite positions, so there are no `highest_close` marks to stamp — but there is exactly
  one close available, core VOO's. Writing it would **fabricate a §5.4 trailing stop on the one
  position §5 exempts from all four sell rules.** Refused **09-15, 09-16, 09-17, 09-18**. On three
  of those four the number was **already in the terminal output**, pulled to price the book — what
  the journals call "the pull arriving with an accomplice." The 09-16 entry predicted this would
  happen again and the 09-17 entry records the prediction landing verbatim. **Every entry says the
  same thing about how it feels: it would not feel like breaking §5, it would feel like completing
  Step 2.**
- **GNRC has not been looked at for seven consecutive runs, under seven distinct rationales, with no
  repeats**: diligence, curiosity, tidiness, completeness, zero-marginal-cost, self-audit, and — on
  Friday — **proxy-procurement** (*"the weekly review runs in an hour and will want the number"*).
  **That last one is the first that does not claim the number for itself, which is what makes it the
  easiest to say yes to.** It fails on a fact independent of its wording: **this review measures
  positions held against VOO; GNRC is not held and never was; there is no row to put it in.**
  Confirmed from this seat — **no GNRC row exists in this review, and none was wanted.** GNRC is the
  named counterparty in the Amazon announcement, **first-order and outside §4 at any price.**

The close journal's own conclusion is the right one and is promoted here: **"I do not think I am
getting better at resisting this; I think the supply of plausible framings is simply not running
out."** Seven refusals under seven rationales is not evidence of a robust agent — **it is evidence
that the defence has to be structural rather than a matter of catching it each time.**

##### 7. Standing rules — six, still one root cause

(i) Screen on the mechanism before running filters. (ii) Verify what the company currently sells,
post-spin. (iii) Verify the news is new to the company's own disclosure. (iv) A recurring ticker is a
warning, not corroboration. (v) A market-structure fact is not a supplier relationship. (vi) A shared
cause is not a mechanism.

**All six remain the same failure: supplying the causal link yourself, then finding a source merely
adjacent to it.**

**Rule (vi) — a shared cause is not a mechanism — was the week's workhorse and fired three times on
three different companies.** The **packaged-food** reject (09-14) is explicitly logged as "the Macy's
shape arriving four days later in a different costume, **recognised rather than re-derived**"; a
09-16 reject is logged as rule (vi) discharging **one day after it was written**; and the **Lennar**
reject (09-18) died because Lennar's weakness and its suppliers' weakness are both downstream of the
**same mortgage rate** — a macro variable, not a transaction. **A rule written one week and catching
three names the next is the clearest evidence in this repo that the logs are doing their job.**

**Rule (v) — a market-structure fact is not a supplier relationship — had the wider week**, at three
instances including one the log calls its seventh this month, in two new costumes at once (an
awardee that is a **consortium** rather than a company).

**Last week predicted a seventh variant in a new disguise. It did not arrive** — the week's genuinely
new material was at part 2 (named parties, withheld numbers), not part 1. **The useful response
remains recognising the shape, not writing a seventh rule.**

##### Nothing that stopped recurring

For completeness, since a review that only lists what recurs is not measuring: **no item named in
weeks 1 or 2 was resolved this week.** Items 1, 2, 3 and 4 above are all in their third week. Item 2
got worse. The only thing that closed is week 2's open question about the broker/official
mechanism — **that was solved in week 2 and stayed solved**; what escalated is its consequence.

---

#### Housekeeping

- **Weekly counter reset: DONE.** `new_positions_this_week` → **0** (was already 0 — nothing was
  opened this week, or any week), `week_of` → **2026-09-21** (ISO Monday of next week). Monday's runs
  will re-check, find the anchors match, and correctly do nothing.
- **Monthly archive rollover: NOT DUE.** Every **entry** in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; nothing predates the current month, so nothing moves and no
  archive index line is written. (`research_log.md` contains earlier dates — 2026-02-21, 2026-05-27,
  2026-07-29 and others — but every one of them is a **date cited inside a thesis body**, not an
  entry date. Checked by header, not by grep.) `archive/` still holds only its README. **Next
  rollover is the first Friday review of October 2026 — 2026-10-02.**
- **⚠ The rollover is now the most urgent piece of maintenance in the repo, and this is the second
  week it has been flagged.** `research_log.md` is **3,257 lines / 226KB**, up from ~2,200 lines /
  151KB last Friday — **+75KB in one week on 16 theses.** `journal.md` is **1,477 lines / 102KB**;
  `state.md` is **849 lines / 88KB**. The five memory files total **477KB**. Every run is instructed
  to read these in full. **At the current growth rate the October rollover is not tidying — it is the
  difference between a run that reads its memory and a run that skims it, and skimming the trade log
  is how a system quietly stops knowing what it holds.** A human may want to move it forward rather
  than wait for 2026-10-02.
- **Alert hygiene: `alerts.md` is EMPTY.** Zero open incidents, zero SYSTEMIC, zero resolved. No
  `push-failure`, no `guard-violation`, no `selftest-abort`, no `circuit-breaker` in the repo's
  history. **No guard violation has ever occurred, so no routine prompt is steering the agent at a
  protected file** — the systemic-prompt-bug case this section exists to surface does not apply.
  `selftest.py` passed all five checks on **every run of this week**, including this one at 16:45 ET.
- **One incident this week did NOT produce an alert, correctly, and is recorded here instead:** the
  `journal.md` header deletion in commit `5fe9e4c` (Recurring Errors §5). It is not one of the four
  alertable categories, it was detected and repaired within one session, and no data was lost. **It
  is nonetheless the most interesting operational event of the week**, because it is the only known
  case of this repo's continuity mechanism silently losing a day.
- **Hand-off to the 2026-09-21 pre-market run** (next session Monday 09:30 ET, confirmed from
  `clock`):
  - **General Mills (~Sept 23) is carried for a fourth time.** Screen it or carry it explicitly — an
    item carried silently is indistinguishable from one forgotten.
  - **No unscreened event has accumulated 09-14 through 09-18.** Every survey item was worked.
  - **Expect an eighth GNRC framing.** It is first-order and outside §4 at any price.
  - **No high-water backfill is due.** The absence of an `(as of ...)` stamp is the absence of a
    *mark*, not a close run that failed. Step 2 ran on 09-18 and had no operand.

---

#### For the human

Six open items. **None is the agent's to decide, and no run has reinterpreted any rule while
waiting.** Items 1, 3 and 5 changed this week.

1. **The §4 priced-in filter reads a drawdown as "priced in."** Third week open, and the cost is now
   the largest single number on the reject board: **LITE, rejected at a −7.35% drawdown, is +11.25%
   against VOO over ten sessions.** It fired again this week on **CRWV (−7.12%, `priced_in: true` on
   a fall)**, making **six-plus** instances; that one cost nothing only because part 1 caught the
   name first. **LITE and MU must not be merged**: MU failed on a
   genuine run-up (the rule working as designed, costing money, nothing to change); LITE failed on a
   fall (the rule doing something nobody designed). Fix is a human editing §4 or `alpaca.py move` —
   **or an explicit decision to leave it, which is a perfectly good answer and would close the
   item.**
2. **The same filter reads an event move absorbed before it looks as "passes."** QCOM (+2.70% net
   after a +8.7% intraday event move) and AVAV (+1.20% after a +12.9% intraday round-trip inside one
   session). Same root cause as (1), opposite direction. Unchanged.
3. **The satellite sleeve is structurally undeployed — 46 theses, 0 positions, 13 sessions.** Third
   week raised. **New this week: §4's binding constraint has a second head.** It is not thesis
   quality and it is no longer only anonymity — **sources now routinely name both parties and
   withhold the number**, killing theses at part 2 rather than part 1 (four instances this week). The
   question for a human is whether the 30% target moves, whether the four-part strictness moves, or
   whether the acceptable evidence for a **quantified** segment widens. **The cost of leaving it is
   ~4.97pp of account return per rolling 12 months.**
4. **The core's divergence from VOO is the 09-03 entry gap, not tracking error.** Measured from the
   706.74 fill the core tracks VOO to **0.0000%**. The −0.69% that appears from an inception anchor
   is a permanent level offset. No action; keep measuring it from the fill.
5. **The broker/official price gap is NOT cosmetic — RE-RATE THIS ITEM.** Two reviews filed it as
   harmless until a satellite position exists. **On 09-18 it put a wrong number — off by $106, more
   than 2× the true move — into the day's reported P&L with no satellite position involved.** Both
   broker legs are anchored on a stale `lastday_price` and reconcile against each other, so nothing
   internal can catch it. A standing rule is now in force (never `equity − last_equity`, never
   `unrealized_intraday_pl`). **Whether the tooling should refuse to serve those fields at all is a
   human's call.**
6. **`selftest.py` certifies a healthy system without probing the two endpoints every routine depends
   on to price anything.** It passed all five checks at 12:34 on 09-11 while `clock` returned **500**
   and `quote`/`bars` returned **504**. The endpoints recovered on their own; **the blind spot did
   not.** Unchanged.

**And the one-line version of everything above:** the system is following every rule it was given,
writing down what it rejects with unusual honesty, and **has not bought anything in three weeks.**
The rules are working. Whether the rules can ever produce a trade is now the question.

---

### Week ending 2026-09-11

**Breaker: INACTIVE.** No halt, `halt_triggered_at: none`, weekly cap **0 of 3** used. Nothing was
gated this week — the sleeve was empty, the breaker clear and the cap fully available on every
session.

**Second weekly review in this repo's history.** The account has now operated **8 sessions**
(2026-09-01 → 2026-09-11; Monday 09-07 was Labor Day, no session). The core sleeve has existed for
**7**. The satellite sleeve has **still never held a position**. There is no 1-month, 3-month or
12-month account history and none of those figures are reported for the account — annualizing eight
sessions would produce a number that means nothing.

---

#### The §1 answer, first — and it is not the number that looks like the answer

**This week the satellite sleeve beat VOO by +0.75pp, and since inception it is now +0.33pp ahead.
Neither figure is a result, and the sleeve is failing §1 by more this week than it was last week.**

Last week's review reported the satellite sleeve **−0.42%** behind VOO. This week it reports
**+0.33%** ahead. Nothing about the sleeve changed: it held $30,000 in cash for all eight sessions
of the account's life, opened nothing, closed nothing and submitted no orders. **The entire swing is
VOO falling 0.75% this week.** A 0% asset "outperforms" a falling index by exactly the amount the
index falls, and it underperforms a rising one by exactly the same mechanism. The sign of this
number is a property of the week, not of the strategy.

**§1 asks a rolling 12-month question, and that is where the honest answer lives.** VOO's own
trailing 12-month total return is **+17.59%**. A sleeve that holds cash returns **0%** over any
window. Held to the objective as written, a permanently idle satellite sleeve loses to the benchmark
by approximately the benchmark's own 12-month return — **roughly −17.6pp on sleeve capital, about
−5.3pp on the account at a 30% weight.** That is the §1 answer. It is a projection of the current
structure, clearly labeled as one, not a measurement — but it is the number the objective actually
asks for, and an 8-session window that happens to contain a down move tells you nothing about it.

**The one-week +0.75pp is the reassuring framing in its most dangerous costume yet**, and it is
worth saying why: for the first time, it is not a sentence I had to delete from a daily journal. It
is the review's own headline §1 figure, computed correctly, from a single source, with no arithmetic
error in it. It is still not outperformance. See Recurring Errors §1.

Every individual no-trade decision this week was defensible on a stated, auditable reason and I
would make each one again. The cumulative structure still points away from §1. Those two statements
are not in conflict, and this is the second consecutive week both are true.

---

#### The three numbers

Reported separately. A blended portfolio-vs-VOO figure at 70% core would be mostly VOO measured
against itself.

**Both legs of every comparison below are taken from official closes (`bars --adjustment all`).**
None of it uses the broker's `current_price`, which at 20:45 UTC reads **702.62** — the midpoint of
the live 702.59 / 702.65 after-hours quote, not a close at all. Priced on official closes, equity is
**$99,582.01**, not the **$99,591.92** the account endpoint reports. The $9.91 difference is the
whole of that artifact today. See Recurring Errors §2.

##### 1. Core return — −0.597% from the fill, and tracking error is zero

VOO sleeve: 99.046311231 shares, filled **706.74** on 2026-09-03, official close **702.52** on
2026-09-11. Value **$69,582.01**, unrealized **−$417.98 / −0.5971%** against the $69,999.99 cost
basis.

| Core measured from | Return | VOO over the same window | Divergence |
|---|---|---|---|
| **The 706.74 fill** (correct) | **−0.5971%** | **−0.5971%** | **0.0000% — exact** |
| This week, 09-04 close → 09-11 close | −0.7544% | −0.7544% | 0.0000% — exact |
| Inception 08-31 close (wrong) | −0.8918% | −0.3341% | −0.5577% |

**Last review's instruction — measure the core from 706.74, not from a prior close — is discharged
here, and it resolves the divergence to zero.** The −0.56% that appears in the bottom row is the
**09-03 entry gap**: the order filled +0.4834% above the 09-02 close on a day VOO gapped up. That is
a one-time level offset baked permanently into the cost basis. It is not tracking error, it is not a
data problem, and it is never skill. Measured from the fill the core sleeve tracks VOO to four
decimal places, which is exactly what a buy-once-hold index sleeve should do.

##### 2. Satellite return — 0.00%, for the eighth consecutive session

| | |
|---|---|
| Realized P&L on closed positions | $0.00 — nothing has ever closed |
| Unrealized P&L on open positions | $0.00 — nothing is open |
| Sleeve capital (§2 target, 30%) | $30,000.00 (actual cash balance: $30,000.00) |
| **Return on sleeve capital** | **0.00%** |

Zero positions opened, zero closed, zero orders submitted at any of this week's runs. `orders
--status all` returns **one row** in the account's entire history — the 09-03 core VOO fill
`d177d8f0`, `status: filled`, terminal. Nothing is in limbo.

##### 3. Satellite vs the same capital in VOO — **the §1 number**

Position-level dollar-weighting is degenerate for the second week running: there are no positions,
so the sleeve is **100% idle cash at 0% return, weighted 1.00**. Idle cash is counted *inside* the
measurement, not beside it, because choosing not to deploy is a decision the strategy made.

| Window | Elapsed | Satellite | VOO (total return) | **Excess** | On $30k |
|---|---|---|---|---|---|
| Week (09-04 → 09-11) | 4 sessions | 0.00% | **−0.7544%** | **+0.7544pp** | **+$226.32** |
| Since inception (08-31 → 09-11) | 8 sessions | 0.00% | **−0.3341%** | **+0.3341pp** | **+$100.23** |
| 1M | — | *no account history — 8 sessions / 11 calendar days elapsed* | | | |
| 3M | — | *no account history* | | | |
| 12M (rolling) | — | *no account history* | | | |

**VOO's own total return, for the windows the account cannot yet fill:**
**1M −0.81% · 3M +3.84% · 12M +17.59%.** The 12-month figure is the bar §1 sets. A sleeve in cash
contributes zero toward clearing it, in any market, in either direction.

##### Account level — reported, and refuted in the same breath

| | Week (09-04 → 09-11) | Since inception (08-31 → 09-11) |
|---|---|---|
| Account | −0.5283% | −0.4180% |
| VOO (total return) | −0.7544% | −0.3341% |
| **Excess** | **+0.2261pp** | **−0.0839pp** |

**The +0.2261pp is not outperformance and the arithmetic closes it exactly.** Core weight at the
09-04 official close was **70.0332%**. 70.0332% × (−0.7544%) = **−0.5283%**, which is the week's
account return **to four decimal places. Residual: zero.** The apparent excess is 30% cash
multiplied by a down week, by construction, and it runs identically in reverse on the first up week.

The since-inception column, which anchors outside the week rather than inside it, is the honest one:
**−0.08pp behind.** The account is behind the index over its whole life *despite* holding 30% cash
through a falling week, because the 09-03 entry gap cost more than the cash weighting saved.

**Sleeves (broker, 20:45 UTC):** core **69.88%** | satellite **0.0%** (count 0) | cash **30.12%**
`core_in_band: true`, `rebalance_needed: false`, `rebalance_delta: +$122.42` — **0.12% of equity**,
deep inside the §2 65–75% band. **No rebalance is due Monday.**

---

#### Trades closed this week

**None.** The table is empty for the second consecutive week and there is nothing to put in it.

| Ticker | Thesis | Held | Exit rule | P&L | Excess vs VOO |
|---|---|---|---|---|---|
| *(none)* | | | | | |

**Which exit rules are firing: none, and the distinction matters more than the tally.** §5.1
invalidation, §5.2 time stop, §5.3 hard stop and §5.4 trailing stop remain **untested code paths,
not proven ones.** Twelve consecutive days of "no exits" recorded the **absence of a subject**, not
twelve clean bills of health. §5.4 specifically is **unarmed, not disabled** — it arms on the first
*satellite* fill, and the 09-03 core fill was not that day.

The questions this section exists to answer — do exits skew toward the −7% hard stop, are time stops
firing too often, are invalidations doing their job — **still have no data and will not have any
until something closes.** A system where every exit is the −7% stop is discovering theses to be
wrong at a fixed price rather than managing them; this book cannot yet be accused of that, or
cleared of it.

One thing is worth recording as genuinely tested this week: **`positions.md` correctly carries no
high-water marks, and the pressure to stamp one on core VOO was real and was refused** (09-11
journal, near-miss #3). Stamping the core would have fabricated a §5.4 stop on the one position §5
exempts from all four rules. On 09-11 the stamp *would* have been possible — `bars` answered — so
the data path was exercised and the rule was not.

---

#### Thesis scoreboard — including rejects

**This week: 20 theses written, 0 accepted, 20 rejected.** Acceptance rate **0%**.
**Since inception: 30 theses, 0 accepted, 30 rejected.** No thesis has ever become a position, so
the "of accepted theses now closed" tally is empty — no timing windows reached, no invalidations, no
stop-outs. Twenty IDs across four sessions is **five to six a day**, from runs working a rolling news
window; it is not twenty days of work.

*(Counter note: `state.md`'s carry-forward and the 09-11 journal both say "thirty-one theses". The
log contains **thirty** IDs — 6 + 2 + 1 + 1 on 09-01/02/03/04 and 4 + 5 + 6 + 5 on 09-08/09/10/11.
Thirty is the auditable number. Small, but in a repo whose only memory is these files, a counter
that drifts unremarked is how larger ones start.)*

##### Where this week's 20 rejections died

| Failure point | n | Names |
|---|---|---|
| **§3 universe floor** | 10 | PBR, EC, YPF, VIST, TBBK, CASH, GDOT, CCB, LEU, SLI |
| **Part 1 — no mechanism / no Company B named** | 6 | AVGO, FN/COHR/LITE/CRDO, MTZ, ORCL screen, LOCUST X3 screen, M |
| **Part 2 — segment immaterial or unquantifiable** | 5 | CAT, MDT, ABT, EQT, LHX |
| **Part 3 — beyond two quarters** | 4 | LMT, GFS, GLW, SLI |
| **§4 headline-name rule** | 4 | QCOM, LMT, GFS, GLW |
| **§4 priced-in filter** | 4 | GFS +4.53%, GLW +11.63%, LEU +7.76%, LHX −4.47% |

Most rejections carried two or three independent failures; the table counts each.

**The dominant failure mode of the funnel is not thesis quality. It is that the source never names
the second-order counterparty.** Six of this week's twenty died at part 1, and in four of those the
screen returned, explicitly, that **no published source names any other company**: Lockheed's
JASSM/LRASM and MK 48 supply chains, Oracle's 850 MW / 300,000-GPU buildout, AeroVironment's LOCUST
X3 laser subsystems, and Bayer's withheld canola partners. **Oracle is the sharpest instance this
log has produced** — a $664B RPO, $209B YoY, >$30B of new bookings, and a dedicated screen for
US-listed firms that have *themselves* disclosed Oracle as a quantified customer returned *"No
verified companies found."* The largest second-order surface available yielded no Company B at all.

Two rejections this week are worth keeping as distinct shapes rather than folding into the count:

- **LHX (T-2026-09-11-02) died on arithmetic, not on an absence.** $127M Palantir + $65M Anduril =
  the entire $192M TITAN award. **$0 is left to disclose to any other named participant.** Nine days
  of carry-forward had flagged LHX as "the specifically invited name," and it arrived properly this
  time — a published source named it — so re-running its filters was legitimate. It died on a number
  anyway, which is a better outcome than avoidance because it is auditable and will not flip at a
  different price. *(Note what did not happen: Anduril's $65M is real second-order money and Anduril
  is private — the third time this month the identifiable beneficiary was unlisted.)*
- **M (T-2026-09-11-05) is a new part-1 failure shape: a shared cause is not a mechanism.** Macy's
  beat on $116M of IEEPA tariff refunds, and the tempting sentence — *"the ruling lowers other
  import-heavy retailers' COGS too"* — is a correlation, not a causal path. Macy's receiving $116M
  causes no other company to receive anything; both are downstream of the same statute, and any
  company actually receiving refunds discloses them itself, making it **first-order for that
  company**. **Every prior part-1 rejection in this log died because no counterparty was named. This
  one had a real, quantified, dated event with obvious read-across.** The distinction is easy to
  lose because the sentence sounds causal when said aloud.

##### What the rejects did after we passed on them

Measured from the close each rejection was actually made against, to the 09-11 close, against VOO
total return over the **identical** window. Both legs come from the same `alpaca.py move` endpoint —
no mixed-source comparison anywhere in this table.

**Week 1's ten rejects, now with a longer window — and the picture has reversed:**

| Ticker | Rejected | Sess | Name | VOO | **Excess** | Reason |
|---|---|---|---|---|---|---|
| **HPE** | 09-02 | 6 | **+19.75%** | −0.12% | **+19.87%** | part 1 — read-across |
| **LITE** | 09-03 | 5 | **+9.43%** | −1.15% | **+10.58%** | **priced-in veto (−7.35% drawdown)** |
| MU | 09-01 | 7 | +4.48% | +0.34% | **+4.14%** | priced-in veto (+5.27% run-up) |
| AEP | 09-01 | 7 | +0.31% | +0.34% | −0.03% | parts 2+3 |
| WDC | 09-01 | 7 | −0.72% | +0.34% | −1.06% | part 1 — post-spin |
| CLF | 09-04 | 4 | −3.56% | −0.75% | −2.81% | thesis + §3 |
| NOC | 09-01 | 7 | −2.63% | +0.34% | −2.97% | part 2 — ~1% of revenue |
| RTX | 09-01 | 7 | −3.57% | +0.34% | −3.91% | part 1 — own inference |
| LHX | 09-02 | 6 | −5.54% | −0.12% | −5.42% | part 2 |
| LHX | 09-01 | 7 | −6.35% | +0.34% | −6.69% | part 3 |

**3 of 10 beat VOO. Last week, on the same ten names, it was 6 of 10.** Mean excess moved from
−0.16% to **+1.17%**, and the entire move is HPE and LITE. **Last review's caveat — that one to
three sessions is noise and ten names is not a sample — was correct, and it was demonstrated by the
board reversing on itself inside one week.** Seven of the eight names that were "running without us"
or close to it have since given it back.

**This week's twenty-three ticker-level rejects:**

| Ticker | Sess | Name | VOO | **Excess** | Reason |
|---|---|---|---|---|---|
| QCOM | 2 | +3.14% | +0.24% | **+2.90%** | §4 headline name |
| VIST | 2 | +2.25% | +0.24% | **+2.01%** | §3 |
| GFS | 1 | +2.17% | +0.84% | **+1.33%** | priced-in +4.53% / p3 / headline |
| YPF | 2 | +1.50% | +0.24% | **+1.26%** | §3 |
| PBR | 2 | +1.27% | +0.24% | **+1.03%** | §3 |
| COHR | 2 | +0.61% | +0.24% | **+0.37%** | parts 1/2 |
| TBBK | 1 | +0.73% | +0.84% | −0.11% | §3 |
| CAT | 3 | −0.49% | −0.23% | −0.26% | parts 2/3 |
| MTZ | 2 | −0.09% | +0.24% | −0.33% | parts 1/2/3 |
| GDOT | 1 | +0.08% | +0.84% | −0.76% | §3 |
| EC | 2 | −0.64% | +0.24% | −0.88% | §3 |
| FN | 2 | −0.89% | +0.24% | −1.13% | parts 1/2 |
| MDT | 3 | −1.56% | −0.23% | −1.33% | part 2 |
| CASH | 1 | −0.56% | +0.84% | −1.40% | §3 |
| GLW | 2 | −1.23% | +0.24% | −1.47% | priced-in +11.63% / p3 |
| AVGO | 3 | −1.83% | −0.23% | −1.60% | part 1 |
| LMT | 1 | −1.08% | +0.84% | −1.92% | headline name / p3 |
| CCB | 1 | −1.08% | +0.84% | −1.92% | §3 |
| EQT | 1 | −1.61% | +0.84% | −2.45% | part 2 — 0.14% of volume |
| ABT | 3 | −3.41% | −0.23% | −3.18% | part 2 |
| CRDO | 2 | −2.94% | +0.24% | −3.18% | parts 1/2 |
| LITE | 2 | −6.20% | +0.24% | **−6.44%** | parts 1/2 *(second rejection)* |
| LEU | 1 | −8.24% | +0.84% | **−9.08%** | §3 / priced-in / p2 |

**6 of 23 beat VOO. Mean excess −1.24%.** LHX, SLI and M (rejected today) have **zero** elapsed
sessions and are not measurable. **The eight one-session rows are not measurements either** — they
are logged for completeness and a future review should re-measure them, not quote them.

**Across all 33 reject-measurements on the board: 9 beat VOO, 24 lagged, mean excess −0.51%.**

##### Rejects that went on to work — and the two are not the same finding

**HPE (+19.87% excess) is the largest opportunity cost this log has produced, and the rejection was
correct.** T-2026-09-02-02 rejected a *Dell → HPE read-across*: Dell's print implies HPE's print
will be good. §4 requires news about Company A to change Company B's **economics**, and a read-across
is an inference about **information**, not a causal path — so it died at part 1. What then happened
is that **HPE's own earnings landed and the stock rose 12.4% in the single session 09-10 → 09-11**
(51.84 → 56.05 over the first four sessions, then 55.23 → 62.08 on the print). **The rejected
thesis's underlying prediction came true, and the stock moved for a reason the thesis correctly
identified as not being a §4 mechanism.** Rejected *correctly by the rule* and *unprofitably in
hindsight* — two different findings, recorded as two.

This is the read-across screen, which last week's review named as **"load-bearing — the one whose
quiet removal would do the most damage."** It has now produced its first large bill. Both statements
survive: the screen is right, and it cost ~20% on one name. **Nothing here is grounds to loosen it.**

**LITE (+10.58% excess) is a different animal and is the open human question firing for real.** It
was rejected on 09-03 at 846.92 by the §4 priced-in filter reading a **−7.35% drawdown** as
`priced_in: true`, because `move` tests absolute magnitude. It ran to 988.08 by 09-09 (+16.7%) and
sits at 926.81. **A decline is close to the opposite of "the market has already paid for this
news,"** and this is now the most expensive instance of that defect. **MU and LITE must never be
merged into one finding:** MU failed on a genuine +5.27% five-session run-up — the rule doing
precisely what it was written to do, costing money, and nothing to change. LITE failed on a
drawdown, which is the rule doing something nobody designed.

**LITE also shows why a single window proves nothing.** The *same name* was rejected again on 09-09
at 988.08 on parts 1/2, and has since fallen **−6.44%** against VOO. Two rejections of one ticker,
six sessions apart, opposite outcomes. The first was costly; the second was right, so far.

##### Is the rejection rate ever wrong?

**Yes — nine times out of thirty-three, and twice expensively.** The routine's own warning is that a
rejection rate which is never wrong means the filters are too loose. That failure mode is not
present: names run without us regularly, and two of them ran a long way.

**The split by rejection type still points the same direction it did last week, on more data:**

| Rejection type | n | Mean excess |
|---|---|---|
| §4 priced-in filter veto (week 1: MU, LITE) | 2 | **+7.36%** |
| Four-part thesis / §3 failures (week 1, excl. HPE) | 7 | **−3.27%** |
| Week 2, §3-universe rejects | 8 | −0.10% |
| Week 2, all others | 15 | **−1.85%** |

**The four-part test keeps selecting correctly: names that fail it lag the index.** The two names
rejected by the **priced-in filter** remain the two largest positive excesses on the board and
remain **the same two candidates that passed the four-part thesis.** The filter is still vetoing the
thesis test's own winners — now on seven and five sessions rather than one and two.

**This is still a tally, not a result, and a future review must not quote it as one.** Thirty-three
measurements over one to seven sessions is not a sample; this week's reversal of last week's headline
is the proof. It is recorded because the human has a live question about this filter and the tally is
the only evidence that will ever exist for it.

**Priced-in filter, cumulative across all worked candidates:** it has now been run on candidates that
were later rejected on other grounds far more often than it has been decisive. **It has never once
been informative in the direction people expect.** A passing priced-in check is a veto that did not
fire, never encouragement — "has not moved" and "should have moved but didn't" produce the same
number.

---

#### Recurring errors

##### 1. The reassuring framing — **second week running, eleven-plus occurrences, and this week it reached the review itself. NAMED.**

Last week's review named this and predicted it would recur. It recurred on **every single session**
of this week:

| | The sentence that arrived first | How it was killed |
|---|---|---|
| 09-08 | "book −0.40% vs VOO −0.52%" | 70% exposure captures 70% of a move |
| 09-09 | "the book outperformed on a down day" | 69.83% exposure × the move, exactly |
| 09-10 | "the book outperformed the index" | 70% × −0.5872% = −0.4094%; the residual 5bp was **$52.84 of two-price gap** |
| 09-11 | *inverted:* "the book rose less than the index" | 69.697% × +0.857% = **0.5973%**, the day's return to four decimals |
| **This review** | **"satellite beat VOO by +0.75pp"** | **0% exposure to a −0.75% week, by construction** |

**Two things are new and both matter.**

**First, on 09-11 it inverted.** The green day produced the mirror-image sentence — *we rose less
than the index* — which is the same artifact wearing the opposite sign. A framing that generates
both directions is not optimism; it is the agent narrating an exposure weighting as a decision,
whichever way it points.

**Second, and this is the finding of the week: it stopped being a journal sentence and became the
review's own §1 headline.** Every previous instance was caught in a daily entry before it reached a
summary. This one is a correctly computed, single-source, arithmetically sound number sitting in the
row §1 cares most about, reading **+0.75pp ahead**. There was no error to catch. **The defense is no
longer arithmetic — it is refusing to let a favorable sign on an 8-session window answer a 12-month
question.** Future reviews should expect this exact number to be positive whenever the week is red,
and should expect to refute it every time.

**Related near-miss, 09-11, worth carrying:** taking the index leg from **official** closes while
leaving the book leg on **broker** marks produces a **+0.0141pp residual — about $14 of "excess
return" that is pure two-price artifact.** A weekly review is the single most likely place in this
system for that to be written down as skill. **Both legs from the same source, or the comparison
means nothing.** This review takes both legs from `bars --adjustment all` throughout.

##### 2. The two-price trap — **second week running. Mechanism now SOLVED; exposure unchanged. NAMED.**

Last week's review recorded this as two days running with an unexplained, direction-unpredictable
gap. This week it appeared on all four sessions at **four different magnitudes** — 6.5c (09-09),
**59.85c** (09-10), 4c (09-11 morning), 10c (09-11 close) — and on **09-11 it was solved exactly**:

> broker `current_price` **702.62** = the midpoint of the live **702.59 / 702.65** quote, to the
> cent. Official close **702.52** (last trade 15:59:57 ET). **The broker mark is not a stale close.
> It is not a close at all** — it is a live bid/ask midpoint that keeps moving after the bell.

**Six days of notes called this an "unstable offset." It is not an offset and it never will have a
stable size.** That is the whole explanation, including the 59.85c outlier, and it should not be
re-opened as a mystery.

**The mechanism is solved; the exposure is not.** The consequence is unchanged and now sharp-edged:
**the moment a satellite position exists, a `highest_close` read from a `positions` field records an
after-hours quote midpoint and silently moves the §5.4 trailing stop to a level nobody chose.** It
does not error. It does not read as stale. On 09-10 that error would have been 60 cents ≈ 0.09% of
the stop. **Always `bars --adjustment all` for a close, a fresh `quote` for execution, never a
`positions` field for either.**

##### 3. The unnamed second-order counterparty — **the structural finding of the month, and it is about the strategy, not the week**

This is not an error the agent is making. It is the binding constraint on §4 as written, and two
weeks of data now say so clearly.

Occurrences, by my count, in the last nine sessions: **CLF** (09-04, market structure ≠ supply
relationship), **LMT** ×2 (JASSM/LRASM and MK 48 — work share disclosed only at Lockheed's own
facility level), **GFS/MPWR** (named party, not a beneficiary), **Bayer/Neste** (partners withheld
by name), **Oracle** (850 MW, 300,000 GPUs, no supplier named anywhere in the release, 8-K or call),
**AeroVironment LOCUST X3** (no laser source, beam director or power subsystem supplier in any
source), **Samsung Biologics** (counterparty explicitly undisclosed under confidentiality),
**Anduril** (the identifiable beneficiary, and private).

**Eight-plus instances, and the pattern is consistent: companies routinely announce the transaction
and withhold the counterparty.** §4's four-part thesis requires a named Company B with a quantified
segment. When the source leaves that blank, the honest output is no trade — and **filling in a blank
the source left blank is not research**, which is standing rule (v). Rule (v) had to be refused
**four separate times this month**, three of them on 09-11 alone.

**Stated as a strategy-level fact rather than a complaint: §4 asks for information that public
disclosure supplies rarely.** That is a real answer to "why thirty theses and zero positions," and
it is a better answer than "the bar is too high," because it is specific and it points at something
a human could actually change (widen the acceptable evidence for a counterparty, or accept the hit
rate). **The agent has not and will not adjust §4 in response to it.**

##### 4. The satellite sleeve has never been deployed — **second week running. NAMED.**

Eight sessions, thirty theses, zero positions, zero orders. §2 explicitly permits uninvested
satellite cash and §4 says the correct output of most research runs is no trade. **Both rules were
followed and no rule was breached at any point this week.** Nothing was gated: breaker INACTIVE, cap
0 of 3, sleeve empty.

The cumulative result is a book that is functionally a 70% index tracker with a 30% cash drag. The
measurement section puts the honest number on it: **over a rolling 12-month window — the window §1
actually specifies — that structure gives up roughly 5.3pp of account return to the benchmark.**
This week's +$226 is the same structure pointed the other way for four sessions.

**This is not a call to lower the §4 bar, and the agent will not lower it.** It is raised here for
the second week because a weekly file is where a structural question belongs, and because the daily
journals record the agent noticing the pull toward lowering it on 09-09, 09-10 and 09-11.

##### 5. Standing rules — five, still one root cause, and one addition

(i) Screen on the mechanism before running filters. (ii) Verify what the company currently sells,
post-spin. (iii) Verify the news is new to the company's own disclosure. (iv) A recurring ticker is a
warning, not corroboration. (v) A market-structure fact is not a supplier relationship.

**All five remain the same failure: supplying the causal link yourself and then finding a source
merely adjacent to it.** Last week predicted a sixth variant in a new disguise. It arrived:

> **A shared cause is not a mechanism** (M, 09-11). Two companies downstream of the same statute is
> correlation, not a causal path.

**Rule (iii) also had its widest week yet**, absorbing three distinct shapes: a *maintained* capex
guidance presented as news (Oracle's "We continue to anticipate $90 to $95 billion"), *financing for
a previously announced acquisition* (Alcoa/South32), and — new — **four loud 09-11 headlines with no
primary source at all** (Nvidia/Intel $30B, Nvidia/Hugging Face, Google's Iowa reactor loan,
Microsoft tripling cloud capacity). All four traced to a single secondary aggregator citing other
outlets; a dedicated verification query found **no SEC filing, no company press release and no
major-press coverage for any of them.** `--recency day` passes an unsourced claim as readily as a
filing. **Events of that size produce primary disclosure; its absence is the finding.**

**The useful response is still to recognise the shape, not to write a seventh rule.**

---

#### Housekeeping

- **Weekly counter reset: DONE.** `new_positions_this_week` → **0** (was already 0 — nothing opened
  this week), `week_of` → **2026-09-14** (ISO Monday of next week). Monday's runs will re-check,
  find the anchors match, and correctly do nothing.
- **Monthly archive rollover: NOT DUE.** Every entry in `research_log.md`, `trade_log.md` and
  `journal.md` is dated **2026-09**; nothing predates the current month, so nothing moves and no
  archive index line is written. `archive/` holds only its README. **Next rollover is the first
  Friday review of October 2026.** ⚠ `research_log.md` is now **~2,200 lines / 151KB** and grew
  ~90KB this week alone on 20 theses. The rollover rule is monthly and this month is not over, but
  at this rate the October rollover is not optional maintenance — **every run reads this file in
  full, and a run that starts skimming the logs is a run that stops knowing what it holds.**
- **Alert hygiene: `alerts.md` is EMPTY.** Zero open incidents, zero SYSTEMIC, zero resolved. No
  `push-failure`, no `guard-violation`, no `selftest-abort`, no `circuit-breaker` in the repo's
  history. **No guard violation has ever occurred, so no routine prompt is steering the agent at a
  protected file.** The selftest passed all five checks on every run this week, including the three
  on 09-11.
- **One operational incident this week did NOT produce an alert, correctly, and is recorded here
  instead.** On 09-11 at 12:34 ET the Alpaca **data plane was half down** — `clock` returned **500**
  on four attempts, `quote` and `bars` returned **504** — while `selftest.py` passed **all five
  checks**. It is not in the four alertable categories and it resolved on its own by 16:16 ET
  (probed by hand: all endpoints 200). **The blind spot did not resolve.** See item 6 below.
- **Next session: Monday 2026-09-14 09:30 ET**, confirmed from `clock`. It is a week boundary.
  **Kroger, VinFast and Rent the Runway reported at or after 09-11's pre-market survey and are
  Monday's material** — Monday's pre-market run must screen them **directly**, not assume a later
  run did. *(This kind of handoff note is the only reason Oracle's FQ1 got screened at all.)*

---

#### For the human

Six open items, unchanged in substance from last week except where noted. **None is the agent's to
decide, and no run has reinterpreted any rule while waiting.**

1. **The §4 priced-in filter reads a drawdown as "priced in."** Now with a real cost attached:
   **LITE, rejected at −7.35%, is +10.58% against VOO over five sessions** and is the second-largest
   excess on the board. It fired again this week on **LHX (−4.47%, rejected for falling)** and came
   **0.4% short on LMT (−3.61%)**. Fix is a human editing §4 or `alpaca.py move` — or an explicit
   decision to leave it, which is a perfectly good answer and would close the item.
2. **The same filter reads an event move absorbed before it looks as "passes."** QCOM (+2.70% net
   after a +8.7% intraday event move, 09-09) and **AVAV (+1.20% after a +12.9% intraday round-trip
   inside one session, 09-11)**. Same root cause as (1), opposite direction.
3. **The satellite sleeve is structurally undeployed — 30 theses, 0 positions, 8 sessions.** Second
   week raised. **New this week: §4's binding constraint is now identifiable.** It is not thesis
   quality — it is that public sources announce transactions and withhold counterparties (Recurring
   Errors §3, eight-plus instances). The question is whether the 30% target or the four-part
   strictness moves, or whether the acceptable evidence for a named Company B widens.
4. **The core's divergence from VOO is the 09-03 entry gap, not tracking error.** **Discharged this
   week:** measured from the 706.74 fill the core tracks VOO to **0.0000%**. Keep measuring it that
   way; the −0.56% that appears from an inception anchor is a permanent level offset.
5. **The broker/official price gap is a live quote midpoint, not an offset — SOLVED this week**, and
   it should not be re-opened as a mystery. Cosmetic on core; **load-bearing the moment a satellite
   position exists.** Whether the tooling should read closes from `bars` by default is a human's
   call.
6. **`selftest.py` certifies a healthy system without probing the two endpoints every routine
   depends on to price anything.** It passed all five checks at 12:34 on 09-11 while `clock` was
   **500** and `quote`/`bars` were **504**. **The endpoints recovered on their own; the blind spot
   did not.** Every routine's Step 0 is the loud-failure mechanism for exactly this, and on the data
   plane it is silent. Whether the pre-flight should probe `clock` and `bars` is a human's call — a
   run must not edit its own guardrail into a different shape. **Until then: probe by hand, and never
   infer data-plane health from a green selftest.**

---

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

