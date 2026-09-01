# Research Log

**AGENT-OWNED. Newest first.**

Every thesis goes here, **accepted or rejected** (§8). Rejected theses are not clutter —
they are the most useful data this system produces, because they are how the human finds
out what the agent keeps almost getting wrong. A log containing only the trades that
happened hides exactly the pattern worth seeing.

A thesis ID must exist in this file before `alpaca.py buy` will submit an order. That is
enforced in code, not trusted to prose.

**ID format:** `T-YYYY-MM-DD-NN`, NN counting from 01 within the day.

**Monthly rollover:** the Friday review moves entries older than the current month into
`archive/research_log/YYYY-MM.md` and leaves an index line behind. Without it this file
eventually grows past what every run can afford to read.

---

## Template

```
### T-YYYY-MM-DD-NN — <TICKER> — ACCEPTED | REJECTED
**Company A / the news:** <what actually happened, with source>
**Company B / the candidate:** <who benefits second-order>

**1. Mechanism (one sentence):**
> <Event> causes <Company B>'s <specific revenue or cost line> to <improve> because <causal path>.

**2. Dollar path:** <segment affected, magnitude estimate, segment as % of total revenue>
**3. Timing window:** <when this shows in reported results> → deadline YYYY-MM-DD
**4. Invalidation:** <specific observable event that proves this wrong>

**Hard filters:**
- Priced-in (§4): moved __% over last 5 sessions → pass | FAIL
- Correlation (§4): drivers of open positions checked → pass | FAIL
- Universe (§3): asset_type, market cap $__B (source: __), ADV __ → pass | FAIL

**Outcome:** <accepted → plan_today.md, or rejected and precisely why>
```

If any of the four parts cannot be written honestly, there is no trade (§4). Write the
entry anyway, marked REJECTED, and say which part failed. "I could not write part 2 without
guessing at the segment size" is a real and useful result.

Note the mechanism test: if the sentence needs a second clause to make sense, the link is
too weak and the answer is no. A mechanism sentence held together by "and also" is the
single most common way a plausible-sounding connection gets mistaken for an opportunity.

---

## Entries

### 2026-09-01 (second run, 01:15 ET) — event survey (funnel, pre-thesis)

**Read this header before reading the entries.** This is the **second** `1-premarket-research`
run for 2026-09-01. The first committed at 00:48 ET (`577ff28`); this one fired at 01:15 ET,
27 minutes later. Both fired roughly seven hours before the routine's intended 08:00 ET slot.
That is a scheduling fault, not a research finding — see `state.md` → Carry forward.

The consequence for this log: two funnel blocks and five thesis IDs carry today's date, from
two runs against a near-identical news window. A later reader should not read `T-…-04` and
`-05` as a second day's work. They are not.

Re-ran the overnight scan (Perplexity, recency=day). It returned substantially the same event
set as the 00:48 run — unsurprising at a 27-minute interval. Per the carry-forward instruction,
the PAC-3 MSE / THAAD event was **not re-litigated**: T-2026-09-01-01 through -03 already
settled it on §4.3 timing and §4.2 magnitude, and neither fact changes in 27 minutes.

Events already funnelled by the 00:48 run and deliberately not reworked here: SEC
shareholder-proposal rulemaking, Chicago PMI 47.1, Treasury/IRS CFC regulations, US–Iran /
oil, NVDA–MediaTek $3.5B, FTC v. Amazon, California wildfire bill (PG&E, EIX).

Three items surfaced that the 00:48 funnel did not carry. Two were dropped pre-thesis:

- **SLB to acquire Kelvion for $3.4B cash** (data-centre cooling; swissinfo markets wrap,
  2026-08-31 21:03 UTC). Dropped at part 1. An acquisition changes the *acquirer's* segment
  mix; it does not change any third company's revenue or cost line, which is what §4 asks for.
  The only reading with a real mechanism — a better-capitalised entrant in data-centre cooling
  — points *against* the incumbent suppliers, and §3 leaves this strategy long-only. No
  Company B exists here.
- **ICE and Cboe fall on Hyperliquid/Payward perpetual-futures talks** (same wrap). A negative
  catalyst on the named parties, with the beneficiary being a private company (Payward) and the
  product being crypto derivatives — outside §3 twice over. Nothing long and eligible.

The third — **Nvidia's gross-margin guidance** — had genuine second-order structure and is
worked as T-2026-09-01-04 and -05 below.

**The event:** Nvidia reported record revenue of **$96.2B** for the quarter ended 2026-07-31,
and guided gross margin **down from 75% to 71–72% by fiscal Q4 2027**, attributing the
compression explicitly to **rising memory-chip costs** (Gallagher weekly markets update,
2026-08-31). This is the cleanest §4 shape available today: Company A has publicly named a
**cost line** that is, by construction, somebody else's **revenue line**. The second-order
question writes itself — who is collecting the money Nvidia says it is now paying?

The answer is the DRAM/HBM/NAND suppliers. Screened on the mechanism first this time, per the
process correction the 00:48 run left in carry forward, and only then filtered:

| Ticker | 5-session move | §4 priced-in |
|---|---|---|
| MU | **+5.27%** (910.34 → 958.31) | FAIL |
| SNDK | **+5.11%** (1491.835 → 1568.135) | FAIL |
| STX | **+4.20%** (794.74 → 828.145) | FAIL |
| WDC | +3.49% (435.30 → 450.495) | pass |

Samsung and SK Hynix are Korea-listed and fail §3 without further work.

**Three of the four are past the threshold, and the fourth cleared it by 0.51pp.** That
pattern is the finding, and it is worth more than any of the individual entries: this is not
a market that has failed to notice: NVDA itself is **+5.94%** over the same five sessions, and
MU is **+15.6% over twenty**. By the time Company A is discussing the cost line on an earnings
call, the trade in Company B is not early — it is consensus with a lag measured in weeks.

---

### T-2026-09-01-04 — MU — REJECTED
**Company A / the news:** Nvidia's Q2 FY2027 report (quarter ended 2026-07-31): record revenue
$96.2B, gross margin guided down from 75% to 71–72% by fiscal Q4 2027, attributed to rising
memory-chip costs. (Gallagher weekly financial markets update, 2026-08-31.)
**Company B / the candidate:** Micron Technology — the only US-listed pure-play DRAM/HBM/NAND
supplier of scale.

**1. Mechanism (one sentence):**
> Nvidia's HBM and DRAM procurement at rising prices causes Micron's DRAM revenue to rise
> because Micron supplies that memory and holds 63.2% of the global HBM market.

One clause, no "and also." Part 1 passes cleanly — this is the strongest mechanism sentence
written in either of today's runs.

**2. Dollar path:** PASSES, comfortably. Micron FY2025 revenue ~**$37.4B**, of which **DRAM
$31.3B (76%)** and NAND $9.9B (24%); disclosed **34.8% global DRAM revenue share and 63.2% HBM
revenue share** for 2025 (Perplexity, citing an FY2025 results summary — secondary source, and
I would want the 10-K before sizing a position on it). Far above the §4.2 10% floor. The
affected segment is essentially the whole company.

**3. Timing window:** PASSES. Memory is priced on short contract cycles and Micron reports
quarterly; NVDA's own guidance places the cost pressure inside fiscal Q4 2027 (ending
2027-01-31). Within the §4.3 two-quarter horizon.

**4. Invalidation:** (not reached — the hard filter fires first, and §4 orders it that way)

**Hard filters:**
- Priced-in (§4): moved **+5.27%** over last 5 sessions (910.34 → 958.31) → **FAIL**. Also
  **+15.6% over 20 sessions** (829.01 → 958.31). Not marginal, and not recent.
- Correlation (§4): no open positions → pass, vacuously
- Universe (§3): stock, well above the $10B floor → pass (figure not sourced; the trade is
  already dead on the priced-in check and I am not going to source a number I cannot use)

**Outcome:** REJECTED on the §4 priced-in filter. Skipped, per the rule.

**This is the uncomfortable one, and I want it on the record properly.** All three thesis
parts I reached are the strongest of any candidate in either run today — a one-clause
mechanism with no strain in it, a segment that *is* the company rather than 1% of it, and a
timing window inside the horizon. T-2026-09-01-01 (NOC) failed because $3B over seven years is
a rounding error against a $42B base; nothing like that is wrong here. This one failed purely
because I am late.

The temptation §4 exists to catch is precisely this: three green parts create real pressure to
find the filter negotiable — to argue 5.27% is "barely over," or that a 20-session window is
not what the rule means, or that HBM has further to run. The rule says more than 4% over five
sessions means you are late, and it does not have an exception for theses that are otherwise
good. **A correct thesis discovered late is not an opportunity; it is a description of a move
that already happened.** No trade.

Worth carrying forward: the mechanism is sound and it is not a one-week story. If MU's
five-session move mean-reverts below 4% while the memory cost cycle is still live, this
becomes a legitimate candidate again — but at that point the timing window needs re-testing
from scratch, because two more quarters will have moved and the horizon is measured from the
day of entry, not from today.

---

### T-2026-09-01-05 — WDC — REJECTED
**Company A / the news:** Same Nvidia margin guidance and memory-cost attribution, 2026-08-31.
**Company B / the candidate:** Western Digital — the one name in the memory complex that
cleared the §4 priced-in filter (+3.49% over five sessions).

**1. Mechanism (one sentence):** COULD NOT BE WRITTEN HONESTLY. **Western Digital does not
sell the product.** WDC's FY2026 10-K states that the Separation completed **2026-02-21**,
with WD continuing the **HDD business** and Sandisk taking the **Flash business**. Post-spin
WDC is hard-disk-drive only; its reportable segments are **Cloud (89% of revenue), Client (8%)
and Consumer (3%)**. Nvidia's guidance is about DRAM and HBM. There is no revenue line inside
WDC that rises because memory-chip prices rise, so the sentence cannot be written at all.

**2–4:** Not attempted. Part 1 failed.

**Hard filters:**
- Priced-in (§4): moved **+3.49%** over last 5 sessions (435.30 → 450.495) → pass
- Correlation (§4): no open positions → pass, vacuously
- Universe (§3): stock, above the $10B floor → pass

**Outcome:** REJECTED at part 1. WDC is not exposed to the driver.

**Why this entry matters more than the rejection does.** I went looking for WDC *because* it
was the only survivor of the priced-in screen — I had a filter result before I had a business,
and a name that "passes while its peers are late" is an inviting shape. It reads like the
market overlooking one member of a complex.

It was nothing of the kind. **WDC lagged the memory complex because it is not in the memory
complex.** It sold that business eighteen months ago. The filter did not find me an
overlooked name; it found me a name whose price is set by nearline HDD demand, and I nearly
built a memory thesis on top of it.

That is a **different failure from T-2026-09-01-02 (LHX)**, and the pair is worth reading
together. On LHX the mechanism was real but the price was trading on something else (a delayed
Missile Solutions IPO). Here the mechanism does not exist at all. What the two share is the
thing to watch for: **a passing priced-in check is not evidence of an opportunity.** It says
only that the stock has not moved, and "has not moved" and "should have moved but didn't" are
the same number. Establishing that the candidate is actually exposed to the driver is a
separate question the filter never asks, and both of today's near-misses ran through exactly
that gap.

Practical form of the rule, for the next run: **verify the business before running the
screen.** A one-line check of what the company currently sells — post-spin, post-divestiture —
would have killed this candidate before it reached the funnel.

---

### 2026-09-01 (first run, 00:48 ET) — event survey (funnel, pre-thesis)

Overnight scan (Perplexity, recency=day) surfaced eight events. Five were dropped before
thesis stage and are recorded here so the funnel is visible, not just its output:

- **SEC step toward eliminating shareholder-proposal requirements** — procedural, no dollar
  path to any single name. No part-2 possible.
- **Chicago PMI 47.1 vs 58 consensus** — macro, and a *negative*. This strategy is long-only
  (§3 forbids inverse/leverage), so a demand-contraction print has no long second-order
  candidate.
- **Treasury/IRS proposed CFC pro-rata regulations (OBBBA)** — affects effective tax rates at
  every US multinational. Too diffuse to name a Company B; no segment, no magnitude.
- **US–Iran clashes push oil higher** — first-order energy, geopolitical and mean-reverting.
  No segment dollar path, and §1 is a fundamentals horizon, not a headline-risk trade.
- **NVDA invests $3.5B in MediaTek** — MediaTek is Taiwan-listed and fails §3 outright. US
  second-order names would have been pure inference; no source named any.
- **FTC + 22 states sue Amazon over advertiser overcharging** — the mechanism runs through
  litigation. Any revenue reallocation to competing ad platforms is years out, well past the
  §4.3 two-quarter horizon.
- **California wildfire liability bill routs PG&E and EIX** — a negative catalyst with no
  clean long beneficiary. Dropped for the same reason as the PMI print.

The one event with real second-order structure was the **Pentagon's 7-year multi-year
procurement to expand PAC-3 MSE and THAAD interceptor production 3–4x**, announced 2026-08-31
with framework agreements to Lockheed Martin and General Dynamics. The three entries below
work that event.

---

### T-2026-09-01-01 — NOC — REJECTED
**Company A / the news:** Pentagon signed 7-year multi-year procurement framework agreements
with Lockheed Martin and General Dynamics on 2026-08-31 to triple PAC-3 MSE and quadruple
THAAD interceptor production, with guaranteed minimum annual quantities so suppliers can
build capacity ahead of demand. (Defense News 2026-08-31; Bloomberg Law; Inside Defense.)
**Company B / the candidate:** Northrop Grumman — newly qualified second-source supplier of
PAC-3 MSE solid rocket motors.

**1. Mechanism (one sentence):**
> The PAC-3 MSE/THAAD production ramp causes Northrop Grumman's tactical solid rocket motor
> revenue to rise because Northrop completed qualification in Q2 2026 as the second-source
> SRM supplier and signed $3B of framework agreements to supply those motors.

Holds together in one clause. Part 1 passes.

**2. Dollar path:** FAILED. Northrop's own release (news.northropgrumman.com) puts the
frameworks at "more than $3 billion" — ~$2B for PAC-3 MSE solid rocket motors and ignition
safety devices, ~$1B for THAAD components — spread across a 7-year term. That is roughly
**$430M/yr against FY2025 total revenue of $41.95B, or ~1.0%**. Northrop's CEO said on the
Q2 call that the company's initial share is "relatively small" and expected to grow over
time. Separately, **I could not source which reportable segment houses tactical SRM
production** — Perplexity explicitly declined to assign it, and I am not willing to assume
Defense Systems ($2.09B in Q2 2026) just because it would clear the 10% bar. Part 2 requires
a segment I can name and a magnitude that is material; I have neither.

**3. Timing window:** FAILED. Seven-year MYP, "contract definitization expected at a later
date," ABL capacity tripling "by 2027." Nothing here shows in reported results inside two
quarters. §4.3 puts this outside the strategy's horizon.

**4. Invalidation:** (not reached — parts 2 and 3 already failed)

**Hard filters:**
- Priced-in (§4): moved **−1.33%** over last 5 sessions (546.85 → 539.58) → pass
- Correlation (§4): no open positions → pass, vacuously
- Universe (§3): stock, market cap ~$77–83B (source: Perplexity aggregating Macroaxis,
  MarketBeat, MarketScreener, Supercycle, late-Aug 2026) → pass

**Outcome:** REJECTED on part 2 (magnitude ~1% of total revenue, and the affected segment
could not be identified from any source) and part 3 (revenue arrives over 7 years, not 2
quarters).

**Worth recording:** this one was tempting and I had largely talked myself into it before
running the numbers. A $3B contract announcement paired with a stock that is *down* 1.33%
over five sessions reads like the market not paying attention, which is exactly the shape
§4 is looking for. The filters that killed it were the boring ones — divide $3B by seven
years and by a $42B revenue base and the "landmark agreement" is a rounding error. The
priced-in check passing is not evidence of opportunity; it is just evidence of no move.

Also noted: Northrop issued its *own* press release about its *own* $3B agreements. That
makes NOC a named party to the deal, not a second-order beneficiary of someone else's news.
§4 asks for Company B, and on a strict reading this is another Company A that got less
coverage. Even had parts 2 and 3 passed, that is a mark against it.

---

### T-2026-09-01-02 — LHX — REJECTED
**Company A / the news:** Same Pentagon PAC-3 MSE / THAAD multi-year procurement, 2026-08-31.
**Company B / the candidate:** L3Harris Technologies, via Aerojet Rocketdyne, which supplies
the PAC-3 MSE two-pulse motor, attitude-control motors and Lethality Enhancer and is
"preparing to nearly triple production."

**1. Mechanism (one sentence):**
> The PAC-3 MSE production ramp causes L3Harris's Aerojet Rocketdyne propulsion revenue to
> rise because Aerojet supplies the interceptor's two-pulse and attitude-control motors and
> is tripling that production line.

One clause, no "and also." Part 1 passes.

**2. Dollar path:** PASSES, weakly. Aerojet Rocketdyne reported **$629M in Q1 2025** revenue
(+8%, 12.1% operating margin), plus ~$300M of Fuzing and Ordnance Systems revenue realigned
into AR — annualizing to roughly **$2.5–2.9B against LHX FY2025 revenue of $21.865B, or
~11–13%**, above the §4.2 10% floor. Management has disclosed the THAAD/PAC-3 framework at
**~$12B of future production revenue and ~$2B of future profit**. But PAC-3 propulsion is a
subset of AR, and **no source gives AR's full-year revenue or the PAC-3 share within it** —
the $629M is a single quarter that predates the FOS realignment. The segment clears the bar;
the specific line item is unsourced.

**3. Timing window:** FAILED. No source — including the Q2 2026 call coverage — states that
the PAC-3 propulsion ramp contributes revenue in Q3 or Q4 2026. The $12B is explicitly
"future production revenue" across the 7-year framework, and the capacity tripling is a
build-ahead. This lands in 2027+, outside §4.3.

**4. Invalidation:** (not reached — part 3 failed)

**Hard filters:**
- Priced-in (§4): moved **+1.30%** over last 5 sessions (262.81 → 266.22) → pass
- Correlation (§4): no open positions → pass. **But note:** LHX and NOC (T-2026-09-01-01)
  move on the identical driver. Had both survived, §4 permits at most one — two tickers on
  one PAC-3 ramp is a single bet wearing a diversification costume.
- Universe (§3): stock, market cap ~$49–54B (source: Perplexity aggregating MarketBeat,
  Stockpolly, Barron's, InvestSmart, late-Aug 2026) → pass

**Outcome:** REJECTED on part 3. The revenue is real and the framework value is large, but
it is a 2027–2029 story and this strategy's horizon stops at two quarters.

**The more important reason, recorded because it nearly escaped notice:** LHX set a 52-week
low of ~$261.62 on 2026-08-24 — below its 50-day ($289.65) and 200-day ($320.54) averages —
*despite* a Q2 beat ($5.88B revenue, $3.13 EPS, both above consensus). The selloff is
attributed to L3Harris **postponing the IPO/spinoff of its Missile Solutions segment**, now
possibly not until mid-2027 or later. So the thing actually moving this stock is a corporate
structure timeline, not interceptor demand. My mechanism sentence describes a real causal
path that is **not the path the price is trading on**. Buying LHX here would be a bet on the
IPO overhang clearing, dressed up as a second-order missile thesis. That is precisely the
substitution §4's honest-broker rule warns about, and the priced-in check cannot catch it —
a stock can pass "hasn't moved on this news" while being dominated by different news
entirely. A cheap stock with a good story attached to the wrong catalyst is still the wrong
trade.

---

### T-2026-09-01-03 — RTX — REJECTED
**Company A / the news:** Same Pentagon PAC-3 MSE / THAAD procurement, 2026-08-31.
**Company B / the candidate:** RTX (Raytheon), on the assumption that Patriot-system radar,
seekers and guidance electronics scale with interceptor output.

**1. Mechanism (one sentence):** COULD NOT BE WRITTEN HONESTLY. I know from general
familiarity that Raytheon builds Patriot radar and the GEM-T interceptor, and it would have
been easy to write a fluent sentence connecting a Patriot ramp to RTX. But **no retrieved
source ties RTX to PAC-3 MSE or THAAD component content in the context of these framework
agreements.** The only RTX item in the coverage was an unrelated $22.9B Tomahawk award.
Interceptor production volume and radar/launcher procurement are separately funded lines;
assuming they scale together is exactly the plausible-sounding link §4 says is a limitation
of how I reason rather than evidence of anything.

**2–4:** Not attempted. Part 1 failed.

**Hard filters:**
- Priced-in (§4): moved **−0.73%** over last 5 sessions (209.26 → 207.73) → pass (ran the
  check before establishing the mechanism, which was the wrong order — noted below)
- Correlation (§4): same PAC-3 driver as the two entries above → would have FAILED anyway
- Universe (§3): stock, market cap ~$275B → pass

**Outcome:** REJECTED at part 1 — the mechanism rests on my own inference, not on anything
reported. Logged rather than dropped silently because "I could not source the link" is a
real result and this is the candidate I was most likely to have waved through on familiarity.

**Process note against myself:** I ran the priced-in check on RTX in the same batch as NOC
and LHX, before confirming RTX had any documented PAC-3/THAAD content. §4 says apply the
hard filters before writing a thesis, but the filters are not a substitute for having a
candidate — I screened a name into the funnel on a hunch. It failed anyway, so nothing turned
on it, but the ordering was wrong and the next run should not repeat it.
