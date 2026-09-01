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

### 2026-09-01 — event survey (funnel, pre-thesis)

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
