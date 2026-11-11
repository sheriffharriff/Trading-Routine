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

### 2026-11-11 (07:02 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$98,910.48** at pre-flight).
`clock` 07:02:17 — `is_open: false`, `next_open` **2026-11-11T09:30:00-05:00**, `next_close`
**2026-11-11T16:00:00-05:00**: **both fields carry today's date — the pre-market full-session
signature. NOT a holiday.** ⚠ **AND TODAY IS THE ONE DATE IN THE YEAR WHERE THAT MATTERS MOST:
2026-11-11 IS VETERANS DAY. THE BOND MARKET IS CLOSED AND THE EQUITY MARKET IS OPEN.** A seat that
reasons from "federal holiday" instead of from `next_open` would skip a full trading session.
Fired ~58 min early against a nominal 08:00, the **eighth** EST session running in that condition
(observation only — `control.md` forbids diagnosing a schedule from a firing time).

**WEEK ROLLOVER — NO ACTION DUE, re-derived with `isocalendar`, not inherited.** ISO **2026-W46,
weekday 3**; Monday anchor **2026-11-09** = `week_of` **2026-11-09**. `new_positions_this_week`
stays **0 of 3**.

**Ledger reconciliation CLEAN, re-derived three independent ways:** `positions.md` satellite block
count **0** (`grep -cE '^### [A-Z]+ — T-'`) · `sleeves` `satellite.count 0` / `value 0` / `pct 0.0`
· `positions` returns **one row, core VOO only** (99.046311231 sh @ `avg_entry_price` **706.74**,
`cost_basis` **$69,999.99** — unchanged since the 2026-09-03 fill; **only the mark moves**).
**No disagreement, so no reconciliation work.** Core **$68,901.57 / 69.67%**, `core_in_band: true`,
`rebalance_delta` **329.53**, **NOT DUE**. Cash **$30,000.00 / 30.33%**. Mark **695.65**
(pre-market, not a close); core unrealised **−$1,098.42 / −1.5690%**.

**✅ NO BACKFILL DUE — THIRD SESSION RUNNING.** The 11-10 close seat held past the bell and
committed the official **VOO close 689.415** (1,671 prints, `adjustment=all`).
⚠ **BROKER/BAR GAP — AND THIS READING IS FILED UNDER A LABEL, WHICH IS THE WHOLE POINT.** The
11-10 close seat **retired the five-point series as constructed**, because it had been assembled
out of two different comparison forms, and directed that it be re-opened as **two labelled
series**. This is the first entry in **SERIES A — `lastday_price` vs the PRIOR session's committed
bar close**: broker **689.50** vs committed **689.415** = **+$0.085**. ⚠ **ONE POINT IS NOT A
SERIES AND NO TREND IS CLAIMED. Series B — `current_price` vs the SAME session's bar — cannot be
read pre-market and is left empty.** ⚠ **The committed 689.415 is NOT corrected toward the broker
figure; the bar close is the official print.**

**FOUR BROAD SWEEPS AND ONE DRILL QUERY.** The transaction sweep — both parties named **and** a
dollar figure in one sentence — returned ***"no qualifying announcement was identified"***, having
itself disqualified four near-misses. The regulatory/operational sweep returned **four food recalls
and two job-cut announcements at private or §3-dead names, and an explicit nil** on FDA approvals
and rejections, FTC, DOJ, FCC, EPA, plant openings, strikes and capacity curtailments. The
overnight sweep returned **macro plus two pre-dated capacity items.** The guidance sweep was the
only productive one: **four own-prior-figure guidance changes, a clean rule (iii) pass on every
one — and not one of them names a counterparty.**

⚠ **ONE DRILL QUERY SPENT ALL RUN, on Curtiss-Wright, and it was spent to TEST a kill this seat
could already name rather than to assume it.** The predicted kills — long performance period,
immaterial annual magnitude, no named supplier — all held, and the query returned a **harder** part
3 than predicted (**through 2030**). ⚠ **It also produced a result worth keeping: the source could
NOT establish CW's TTM revenue, segment split or market cap, so §3 was never reached as a gate and
no §3 pass is claimed below.**

---

### T-2026-11-11-01 — CW (Curtiss-Wright) ← contracts >$140M from General Dynamics Electric Boat — REJECTED (part 3 verified at ~16 quarters; part 2 at ~1% of revenue; and it is the FIRST-ORDER leg)
**Company A / the news:** Curtiss-Wright announced **2026-11-10** contracts **valued in excess of
$140 million** from **General Dynamics Electric Boat** for propulsion equipment supporting the US
Navy's **Virginia-class and Columbia-class** submarine programmes (Businesswire, 2026-11-10).
**Company B / the candidate:** none reached. **CW itself is the recipient**, and the drill query
confirms **no supplier TO Curtiss-Wright is named anywhere in the release** — only CW's own
propulsion valves and pumps.

**1. Mechanism:** not written. ⚠ **This is the shape the funnel keeps mistaking for a §4
candidate: a genuinely two-party, both-named, dollar-figured COMMERCIAL transaction — the exact
object the transaction sweep asks for — in which the buyable leg is the one that issued the press
release about its own revenue.** §4's first line is that you are not chasing the headline name.
Same rung as `T-2026-11-09-01` (COHR).
**2. Dollar path: FAILS, and the magnitude was verified rather than estimated.** Performance runs
**through 2030**, so ~$140M over ~4 years ≈ **$35M/yr** against Q3-2026 net sales **alone** of
**$952.6M** (annualised ~$3.8B) = **~0.9% of revenue** — **more than ten times below §4's 10%
floor.** ⚠ **And it is not even allocable: the source states the figure is split between the
Naval & Power segment AND the Defense Electronics division and is NOT broken out between them, so
no segment share is computable in either direction.**
**3. Timing window: FAILS OUTRIGHT — and harder than predicted.** "Engineering, manufacturing and
testing had begun and would continue **through 2030**" ≈ **16 quarters against §4's ceiling of
two.** ⚠ **This is rule (vi) arriving in defence rather than energy clothing: the standing rule
names long-dated energy offtake, and a submarine hull programme is the same shape with a longer
tail.**
**4. Invalidation:** not written — there is no thesis to invalidate.

**Hard filters:**
- Priced-in (§4): **−3.93%** over 5 sessions (497.55 → 477.975) → script verdict `priced_in: false`,
  "passes". ⚠ **Recorded, NOT leaned on: the move is a DECLINE and the filter thresholds absolute
  magnitude, so "passes" here means "has not fallen 4% yet", not "the upside is still available".
  Instance 14 of the direction-blind defect — see the standing item.**
- Correlation (§4): **not reached** — zero open positions, so `driver` fields are empty.
- Universe (§3): **NOT REACHED AS A GATE.** The drill query could not establish CW's market cap or
  TTM revenue from the available sources. ⚠ **No §3 pass is claimed, and a later seat revisiting CW
  must pull the figure itself rather than inherit an absence.**

**Outcome:** **REJECTED** on **part 3** (through 2030) and **part 2** (~0.9% of revenue,
unallocated) independently, with **part 1** structurally dead because this is the first-order leg.
⚠ **The one genuinely new finding: this is the best-formed transaction the sweep has surfaced in
weeks, and the thing that killed it is the thing that made it findable — a company announcing its
own award is, by construction, Company A.**

---

### T-2026-11-11-02 — the AI-datacenter supply tier ← CoreWeave's raise of its OWN FY2026 revenue guidance — REJECTED (rule (iii) PASSES on the WRONG FIGURE; no counterparty named; rule (iv), fifth appearance of this complex in five sessions)
**Company A / the news:** **CoreWeave (CRWV)** reported **2026-11-10** and **raised its own
FY2026 guidance**: revenue **$12.4–13.2B → $13.0–13.3B**, adjusted operating income
**$960M–1.15B → $1.275–1.375B**, citing continued AI-infrastructure demand (CNBC, 2026-11-10).
**Company B / the candidate:** none reached — the GPU, power, cooling and networking tier. ⚠ **The
source states plainly that NO specific customer, supplier or counterparty is named.**

**1. Mechanism:** not written without an "and also". ⚠⚠ **THIS IS THE 10-15 TSMC DEFECT ARRIVING
IN A NEW SECTOR, AND IT IS WHY RULE (iii) PASSING IS NOT PROGRESS: the figure that MOVED is
REVENUE, and revenue has no supplier chain hanging off it. The figure a supplier thesis would run
on is CAPEX, and the source discloses no change to it — so the mechanism needs "and also CoreWeave
will have to spend more to deliver that revenue", which is the second clause §4 forbids.**
⚠ **Apply rule (iii) to the figure the mechanism runs on, not to the release.**
**2. Dollar path: FAILS.** The disclosed increment is **+$0.6B at the revenue-range midpoint** at
**Company A**, not segment revenue at any Company B. Allocating any part of it to a supplier
requires inventing a capex ratio, a vendor split and a delivery schedule — three assumptions, the
`T-2026-11-04-02` shape.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **−9.29%** over 5 sessions (53.73 → 48.74) → `priced_in: true`, "LATE — skip".
  ⚠ **Instance 15 of the direction-blind defect, and the clearest one yet: CRWV FELL 9.3% and the
  script calls it LATE. The verdict is OBEYED — it fails safe — but it must NEVER be quoted as "the
  market has captured this upside", because here it means precisely the reverse.**
- Correlation (§4): not reached — zero open positions.
- Universe (§3): not reached; the thesis dies at part 1.

**Outcome:** **REJECTED** at **part 1** — rule (v) (no named recipient anywhere in the second-order
leg) and the wrong-figure defect, both independently. ⚠ **Rule (iv): this complex has now arrived
in five consecutive sessions (11-05 the valuation unwind · 11-06 IREN and QCOM · 11-09 the
sovereign-AI tier · 11-10 AAON and AAOI · 11-11 CRWV) and died at part 1 or part 2 every time. The
disclosures keep changing shape — a repricing, a delayed delivery, a collaboration, a guidance
raise — and the kill does not move. That is a fact about how AI-infrastructure demand is
DISCLOSED, not about a candidate maturing.**

---

### T-2026-11-11-03 — VG (Venture Global) ← FY2026 adjusted EBITDA raised from its OWN $8.7–9.1B to $10.0–10.3B on Plaquemines Phase 1 commercial operations — REJECTED (FOURTH appearance; first-order leg, no named recipient; its two suppliers were disposed at T-2026-10-15-02)
**Company A / the news:** Venture Global reported **2026-11-10** and raised FY2026 adjusted EBITDA
guidance to **$10.0–10.3B from its own prior $8.7–9.1B**, alongside **commencement of commercial
operations at Phase 1 of Plaquemines**. **Company B / the candidate:** none reached.

**1. Mechanism:** not written. **The EBITDA raise is VG's own economics — first-order.** The only
second-order legs are the equipment suppliers, and **the announcement names no recipient of
anything.**
**2. Dollar path: FAILS.** ⚠ **The suppliers are already disposed and the answer was written four
weeks ago: `T-2026-10-15-02` killed the GE Vernova / Baker Hughes power-island frame agreements
because the ~$17.2B in circulation was conditional, aggregated across two agreements, UNALLOCATED
between the two buyable legs, and paid OUT by Venture Global. Nothing in an EBITDA raise allocates
a dollar to either of them.**
**3. Timing window:** not reached. ⚠ **Noted because it is the one genuinely NEW thing here: the
three prior appearances all died at part 3 / rule (vi) on long-dated contracting, and this event —
a plant actually entering commercial operation — is NOT long-dated. The kill has MOVED UP a rung,
to part 1. That is a real change and it still does not produce a candidate.**
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **−7.77%** over 5 sessions (13.00 → 11.99) → `priced_in: true`, "LATE — skip".
  **Instance 16 of the direction-blind defect.** ⚠ **Also §3-relevant: at **$11.99** VG is a
  candidate whose cap must be checked, not assumed, if it is ever reached — it was not reached.**
- Correlation (§4): not reached — zero open positions.
- Universe (§3): not reached.

**Outcome:** **REJECTED** at **part 1** (first-order leg, no named recipient) with **part 2**
pre-disposed. ⚠ **Rule (iv), FOURTH appearance, and the standing roll-call predicted this issuer's
return explicitly — "expect this issuer again; the answer is already written." It was. Zero drill
queries were spent on it, which is what the roll-call is FOR.**

---

### T-2026-11-11-04 — the macro / policy complex (October CPI · the December hike repricing · a 17bp two-year move · a $42B 10-year auction · the USTR Section 301 extension) — REJECTED (no Company A; the standing government-action object; the tariff leg is rule (v)'s most fillable blank)
**Company A / the news:** October **CPI +0.4% m/m headline and +0.3% core**, both **above the
+0.3% / +0.2% consensus** — ⚠ **the figures the 11-10 plan carried as ESTIMATES, now printed;
quoting them as outcomes is correct today and was not yesterday.** Futures priced a **December
25bp hike as near-certain with ~15% on 50bp**; Governor Waller said 50bp should be considered.
**2-year +17bp to 4.73%**, 5-year +14bp to 4.81%, **10-year +10bp to 4.98%**, 30-year +9bp to
5.35%; a **$42B 10-year auction** cleared at **5.02%**. USTR extended **178 Section 301 exclusions**
plus maritime-service fees and port-cargo-handling-equipment tariffs **through 2027-01-09**.
**Company B / the candidate:** none exists.

**1. Mechanism:** not written. **Every leg has ONE party.** ⚠ **The standing rule is explicit and
this is a textbook instance: a government action is sector-specific, carries a number, names an
industry and moves the tape — and a long-only book cannot trade money being withheld from, or
returned to, a sector unless some NAMED party receives it. Nobody does.**
⚠ **Rule (iii) independently on the CPI leg: the comparison in the source is to CONSENSUS, not to
the BLS's own prior figure — the single most prolific costume in the standing rules.**
⚠⚠ **THE USTR LEG IS THE ONE WORTH NAMING, BECAUSE IT WEARS RULE (v)'s BEST-FITTING COSTUME: it
pairs an EXACT COUNT (178 exclusions), a DATED deadline (2027-01-09) and a NAMED COMPONENT
CATEGORY ("port cargo-handling equipment") — and the source's own list of beneficiaries is
"importers, shipping companies, and port-equipment projects", i.e. three CATEGORIES and zero
names. A precise figure beside a named component category is the most fillable-looking blank this
funnel produces, and filling it in is not research.**
**2–4:** not reached.

**Hard filters:** not reached — no candidate.
**Outcome:** **REJECTED**, **zero drill queries spent.** ⚠ **Five consecutive sessions have now
logged a macro/policy complex in exactly this shape (11-05, 11-06, 11-09, 11-10, 11-11). THE
FINDING IS THE PATTERN, NOT THE INSTANCE — and the correct cost of recognising it is one paragraph
and no query.**

---

### T-2026-11-11-05 — sweep: two pre-dated capacity announcements, three own-results prints with no counterparty, a $26B private placement, a foreign aircraft order, two sub-scale defence POs, four recalls and three workforce actions — REJECTED (eighteen items, disposed as one, ZERO drill queries spent)

- **FCX (Freeport-McMoRan) — Bagdad $4.5B expansion, +225Mlb/yr copper. RULE (iii), and the
  source volunteered the kill: ANNOUNCED 2026-11-04**, surfaced by a `--recency day` sweep seven
  days later. ⚠ **A sweep window is not a disclosure date. This is the cheapest rule (iii) failure
  there is and it arrives every few sessions.** No customer contract or affected company is
  identified — rule (v) on top.
- **Lydian Energy / Faraday (Utah), 150MW / 600MWh to PacifiCorp. RULE (iii) AGAIN, VOLUNTEERED:
  the source states the facility actually began operating 2026-09-18**, so the 11-10 item is the
  commercial-operation ANNOUNCEMENT, not the event. **Lydian is private; PacifiCorp is a Berkshire
  subsidiary, not separately buyable.** ⚠ **A DELIVERY MILESTONE RECYCLED AS NEWS — the GM/Lockheed
  costume, in batteries.**
- **Anthropic private placement, ~$26B, Google / NVIDIA / Microsoft among seven committing. RULE
  (viii): capital paid IN**, and paid in BY the §3-eligible legs TO a private recipient that cannot
  be bought at any price. The AZN/SMMT and GEHC/Sofie shapes combined.
- **Cathay Pacific / Airbus, 11 × A330-900, $5.114B.** ⚠ **Two kills: the buyer is HONG
  KONG-LISTED and Airbus is PARIS-LISTED (§3 kills both legs), and the figure is an aggregate
  CATALOG price, which is not a transaction value in commercial aviation.** Rule (v)'s ceiling in
  a new costume — a LIST PRICE.
- **Summit Midstream (SMC)** EBITDA $235–255M → **$250–260M** · **Grove Collaborative (GROV)**
  revenue $142.5–152.5M → **$144–146M**, EBITDA breakeven-to-low-single-digits → **$1–2M** ·
  **StubHub (STUB)** GMS outlook raised, **no old or new range in the source.** ⚠ **All three are
  clean rule (iii) passes on their own prior figures and ALL THREE NAME NO COUNTERPARTY. The first
  two are also §3-dead on market cap by inspection. A clean pass on one filter is not progress
  toward a trade.**
- **Vestas (VWDRY)** FY revenue €20–22B → **€20.5–21.5B** — **§3: Copenhagen-listed, US exposure
  via an OTC ADR.** Dead before the mechanism.
- **Senseonics (SENS)** $62–66M → **$68–70M** · **Zeta Global (ZETA)** +$37M to a $1.855B midpoint
  · **MNTN** $347–357M → **$311–314M**: all three **reported 11-04 or 11-09 — behind seats that
  have already run.** Rule (iii) on the window.
- **VEEM / Huntington Ingalls Newport News, ~$800,000 PO.** ⚠ **Recorded only to name the floor:
  it is **four orders of magnitude** below §4's materiality, and VEEM is AUSTRALIAN-LISTED. Two
  independent §3/part-2 kills on one line.**
- **Stabilis Solutions — three-year LNG take-or-pay.** Customer **unnamed**, **no dollar value
  disclosed.** Rule (v) plus a missing part 2.
- **Four FDA recalls and three workforce actions:** Family Farmstead Dairy cheddar (*Listeria*,
  company notice dated **10-15**, FDA published 11-10 — rule (iii)) · Laub's Feeding & Cubing
  89 tons of hay cubes (*C. botulinum*) · **Nexteer Automotive** Saginaw reductions, **count
  undisclosed** · **Ferrara** Little Village closure, 154 jobs, ⚠ **production moves to Ferrara's
  OWN other facilities — rule (vii), vertical integration leaves no external beneficiary** ·
  **PepsiCo** ~1,000 North American job cuts plus two 2026 bottling-plant closures. ⚠ **A COST
  ACTION AT COMPANY A IS NOT A SECOND-ORDER CATALYST: nobody is disclosed as receiving the saved
  money, and the only read available is a reader-supplied share shift. Every recalling or closing
  entity here is private or §3-dead.**

**Outcome:** **REJECTED, all eighteen, zero drill queries spent.** ⚠ **Two of the three cheapest
kills today were VOLUNTEERED BY THE SOURCES THEMSELVES (Freeport's 11-04 date, Lydian's 09-18
start). Asking the sweep for the disclosure date rather than the publication date costs one clause
and killed two items before a mechanism was attempted.**

---

### 2026-11-10 (07:02 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$98,608.39** at pre-flight).
`clock` 07:01:59 — `is_open: false`, `next_open` **2026-11-10T09:30:00-05:00**, `next_close`
**2026-11-10T16:00:00-05:00**: **both fields carry today's date — the pre-market full-session
signature. NOT a holiday.** ⚠ **Read off the DATES, not the boolean: FALSE has three meanings,
TRUE has one.** Fired ~58 min early against a nominal 08:00, the **seventh** EST session running
in that condition (observation only — `control.md` forbids diagnosing a schedule from a firing
time).

**WEEK ROLLOVER — NO ACTION DUE, re-derived with `isocalendar` rather than inherited.** ISO
**2026-W46, weekday 2**; Monday anchor **2026-11-09** = `week_of` **2026-11-09**.
`new_positions_this_week` stays **0 of 3**. ⚠ Recorded as *re-derived*, not as *skipped* — §6's
cap must not depend on any earlier seat having run.

**✅ NO BACKFILL DUE — SECOND SESSION RUNNING, AND THE FIRST BACK-TO-BACK PAIR IN THIS FAULT'S
HISTORY.** The 11-09 close seat held past the bell and committed the official **VOO close
691.93** on 2,880 prints, `adjustment=all`. Broker `lastday_price` reads **691.87** — **6¢
below** the committed bar close, inside the known moving broker/bar midpoint and requiring
nothing. ⚠ **Do not "correct" the committed 691.93 toward the broker figure; the bar close is
the official print.**

**Ledger reconciliation CLEAN, re-derived three independent ways at this seat, not inherited:**
`positions.md` satellite block count **0** (`grep -cE '^### [A-Z]+ — T-'`) · `sleeves`
`satellite.count 0` / `value 0` / `pct 0.0` · `positions` returns **one row, core VOO only**
(99.046311231 sh @ `avg_entry_price` **706.74**, `cost_basis` **$69,999.99** — unchanged since
the 2026-09-03 fill; **only the mark moves**). **No disagreement, so no reconciliation work.**
Core **$68,589.57 / 69.57%**, `core_in_band: true`, `rebalance_delta` **423.13**, **NOT DUE**.
Cash **$30,000.00 / 30.43%**. Mark **692.50**; core unrealised **−$1,410.42 / −2.0149%**.

**FOUR BROAD SWEEPS AND ONE DRILL QUERY. THREE OF THE FOUR SWEEPS ANSWERED §4's QUESTION IN THE
NEGATIVE OUT LOUD.** The overnight-events sweep said the reporting *"does not support a reliable,
comprehensive list of major US corporate events for November 9–10, 2026"* and returned macro
plus an earnings calendar with no results attached. The transaction sweep — both parties named
**and** a dollar figure — returned ***"no qualifying announcement was identified"***, having
itself disqualified AEVEX's ~$400M and AeroVironment's $940M for unnamed customers. The
regulatory sweep returned **four pharma/device items and an explicit nil** on FTC/DOJ, FCC, EPA,
US plant closures, US recalls and US strikes. The structural sweep — which required **one source
sentence carrying both the dollar figure and the name of the company RECEIVING it** — answered
***"No qualifying disclosure was identified."***

⚠ **ONE DRILL QUERY SPENT ALL RUN, on the NASA CLPS 2 award, and it was spent deliberately to
TEST a kill this seat could already name rather than to assume it.** Standing rule (v)'s CEILING
sub-shape predicted an unallocated multiple-award vehicle; the query returned NASA's own
structure language and the prediction held exactly. ⚠ **That is the right reason to spend a
query: a named kill that has not been verified on this instance is still a guess.**

---

### T-2026-11-10-01 — LMT · NOC (and the Redwire / Honeybee / Yank supplier tier) ← NASA's $10B CLPS 2 lunar award — REJECTED (rule (v) CEILING, verified not assumed; part 2 by three orders of magnitude; rule (iii) re-covered; §3 kills six of eight legs)
**Company A / the news:** NASA selected **eight** companies for **CLPS 2** — Blue Origin, Firefly
Aerospace, Intuitive Machines, ispace-U.S., **Lockheed Martin Space**, **Northrop Grumman Space
Systems**, SpaceX, Voyager Technologies. NASA's own structure language, quoted from the drill
query: *"The CLPS 2 framework is a 10-year, multiple-award, indefinite-delivery/
indefinite-quantity master contract with a combined maximum value of $10 billion"* — rising to
$15B if a five-year option is exercised. Announced **2026-11-07**, NASA release **updated
11-10**.
**Company B / the candidate:** attempted two ways — (a) the two §3-eligible primes, **LMT** and
**NOC**; (b) the named Moon Base technology tier, **Redwire (RDW)**, Honeybee Robotics, Yank
Technologies, Quantum Space.

**1. Mechanism (one sentence):** *not writable without an "and also".* The honest attempt —
*"NASA's CLPS 2 award causes Lockheed Martin's Space segment revenue to improve because it can
now bid task orders"* — **states a right to compete, not a sale.**
**2. Dollar path: FAILS, AND BY THREE ORDERS OF MAGNITUDE.** ⚠⚠ **NO DOLLAR WAS ALLOCATED TO ANY
WINNER.** The drill query returned an awardee's own disclosure: *"a multiple-award, IDIQ contract
with a **combined ceiling** of $10 billion **across all awardees**"*, and ispace-U.S. stated the
selection ***"does not itself constitute a funded mission."*** Even the maximally generous
arithmetic — $10B ÷ 8 ÷ 10 years ≈ **$125M/yr against LMT's ~$74B revenue = ~0.17%** — is
**~60× below §4's 10% materiality floor**, and that figure is itself invented, because the
ceiling is not divisible.
**3. Timing window: FAILS INDEPENDENTLY.** A **10-year** vehicle with a five-year option, funded
only when NASA elects to issue task orders. Against §4's **two-quarter** ceiling.
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — the thesis was dead at parts 1, 2 and 3. No `move` call spent.
- Correlation (§4): **vacuous — zero open satellite positions**, so no `driver` field exists to
  collide with. ⚠ Recorded as *vacuous*, not as *passed*.
- Universe (§3): **KILLS SIX OF THE EIGHT LEGS BEFORE A MECHANISM IS NEEDED.** Blue Origin and
  SpaceX are **private**; Firefly, Intuitive Machines, ispace-U.S. and Voyager are all **well
  below the $10B floor**. Only **LMT** and **NOC** clear §3 — and they are the **first-order**
  recipients §4 exists to avoid. The supplier tier is worse: **Honeybee Robotics** (Blue
  Origin-owned), **Yank Technologies** and **Quantum Space** are all **private**, and **RDW** is
  a ~$1–2B cap, **§3-dead** — ⚠ **and RDW is already the named instance of rule (v)'s CEILING
  sub-shape in this log (its own "$980M" multiple-award ceiling). It arrived back inside the
  exact shape it was first used to illustrate.**

**Outcome: REJECTED — and this is the day's best candidate and the cleanest verified kill in
the log.** ⚠⚠ **IT IS WORTH KEEPING BECAUSE OF WHAT IT HAD: eight named companies, two of them
§3-eligible mega-caps, a $10 BILLION figure, a dated government award, and an exact structure
quote. That is more disclosed material than almost any candidate here has carried — and there is
still no second-order company in it, because NOBODY HAS BEEN PROMISED ANY MONEY.** ⚠ **RULE (iii)
RIDES ON TOP AND IS THE SUBTLER KILL: the announcement is dated 2026-11-07 and NASA merely
UPDATED its release on 11-10. A sweep run on 11-10 surfaces it as fresh. "Re-covered deal" is
costume #3 on rule (iii)'s list, and a government press-release refresh is a new costume for it.**
⚠⚠ **THE PROCEDURAL FINDING, WHICH IS THE PART WORTH CARRYING FORWARD: the drill query was spent
to VERIFY a kill rule (v) already predicted, and the verification mattered — had NASA allocated
per-winner task-order values, the predicted kill would have been WRONG. A named standing rule
tells you which question to ask; it does not answer it for a new instance.**

---

### T-2026-11-10-02 — the data-center cooling supply tier ← AAON's raise of its OWN FY sales-growth guidance from 55–60% to 72–75% — REJECTED (part 1: a company's own order book is a CONDITION, not an event; no named recipient anywhere in the second-order leg)
**Company A / the news:** **AAON** (NASDAQ: AAON), 2026-11-10, **raised its own full-year
sales-growth guidance to 72–75% from its own prior 55–60%.** ⚠⚠ **THIS IS THE CLEANEST RULE (iii)
PASS IN THIS LOG IN WEEKS — the prior COMPANY-ISSUED range is present in the source, the new range
is present, and the move is ENORMOUS (a ~15pp mid-point raise on an already-extraordinary growth
rate).**
**Company B / the candidate:** attempted two ways — (a) AAON's **component suppliers**
(compressors, coils, controls, motors); (b) the **read-across** to other data-center thermal names
(Vertiv, Trane, Johnson Controls, Lennox, Comfort Systems).

**1. Mechanism (one sentence): FAILS, AND IT IS THE STANDING "REMARKING ON A CONDITION" OBJECT IN
ITS MOST CREDIBLE COSTUME YET.** ⚠⚠ **NOTHING ABOUT ANY SUPPLIER'S OR COMPETITOR'S ECONOMICS
CHANGED ON 2026-11-10.** AAON's guidance raise is a **disclosure that its own order book is
larger than it previously said** — evidence of a data-center cooling demand condition that
**pre-dates the remark**. The attempted sentence needs the tell-tale second clause: *"AAON's raise
shows cooling demand is stronger than thought — **and also** Company B captures that demand."*
⚠ **The read-across leg (b) is the COMPETITOR'S EARNINGS PRINT face of the shared-cause object,
already killed on AutoZone→GPC/ORLY/LKQ, Carnival, Vail, CarMax and CALM.**
**2. Dollar path: FAILS — NO RECIPIENT IS NAMED.** The source states explicitly that **no named
customer, no named supplier and no capex figure** appears in the release. There is no sentence
anywhere containing both a figure and the name of a company receiving it. ⚠ **AAON's own revenue
line is the only quantified path, and that is the FIRST-ORDER leg.** The largest compressor
supplier to this market, **Copeland, is privately held** (Blackstone) — rule (viii)'s
private-recipient shape.
**3. Timing window:** *not reached.*
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — dead at part 1. No `move` call spent.
- Correlation (§4): **vacuous — zero open satellite positions.**
- Universe (§3): **not reached** for the second-order leg, because no second-order company was
  ever nameable. *(AAON itself is the headline name, not a candidate.)*

**Outcome: REJECTED at part 1.** ⚠⚠ **THIS IS THE ENTRY MOST WORTH READING TODAY, BECAUSE IT IS
THE ONE WITH A GENUINE PASS IN IT. A clean rule (iii) pass is a statement that the NEWS IS REAL —
it is not progress toward a trade, and this log already holds the proof (Antofagasta 10-15 passed
rule (iii) cleanly and died on §3 one line later; IOVA's pass was killed by rule (vii)).** ⚠ **The
pull here was strong and is recorded rather than omitted: a 15pp own-guidance raise on data-center
cooling is exactly the kind of number that invites a seat to go looking for someone to buy. There
was nobody to buy — every candidate on the second-order leg is private, unnamed, or a
shared-cause read-across.**

---

### T-2026-11-10-03 — the brain-metastases radiation-oncology complex ← the FDA's rejection of Novocure's Optune Mya — REJECTED (part 1: a REJECTION preserves the status quo and changes nobody's economics; §3 kills NVCR; the only other story is a reader-supplied share shift)
**Company A / the news:** **2026-11-09** — the FDA **declined to approve** Novocure's **Optune
Mya** for adults with brain metastases from NSCLC following stereotactic radiation, citing
uncertainty about the degree of clinical benefit and **raising no safety concerns.** **No
financial impact was quantified** in any cited source.
**Company B / the candidate:** attempted as the incumbent radiation-oncology and
radiosurgery-equipment complex.

**1. Mechanism (one sentence): FAILS, AND IT IS A SHAPE THIS LOG HAS NOT PREVIOUSLY WRITTEN
DOWN — THE NON-ARRIVAL OF A COMPETITOR.** A rejection means **the market Novocure wanted to enter
continues exactly as it was.** ⚠⚠ **An incumbent that was never displaced has not GAINED anything;
it has merely not LOST something it never lost. No segment revenue, no cost line and no order
book moves on 11-09 at any company.** The only available sentence is the reader-supplied share
shift this log kills every earnings season.
**2. Dollar path: FAILS — THERE IS NO FIGURE OF ANY KIND.** Not at Novocure (no quantified
impact disclosed) and not at any incumbent (no incumbent was named by any source).
**3. Timing window:** *not reached.*
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **NOT REACHED.** No `move` call spent.
- Correlation (§4): **vacuous — zero open satellite positions.**
- Universe (§3): **NVCR is a ~$2–3B cap — below the $10B floor**, so the headline leg is
  ineligible independently. No second-order leg was ever named, so §3 had nothing to test there.

**Outcome: REJECTED at part 1.** ⚠ **Kept because of the sign: this funnel meets FDA
APPROVALS often and has a worked range for them (EW's own-valve integration at the strong end,
BMY's paediatric label extension at the weak end). A REJECTION is a different object and weaker
than either — an approval at least creates a product and a supply chain that must be stood up,
while a rejection creates NOTHING, by construction.** ⚠ **Do not re-derive this; it is the
status-quo-preservation shape and it has no long side.**

---

### T-2026-11-10-04 — the oral-anticoagulant complex ← the FDA's approval of Bayer's Sunharbo (asundexian) — REJECTED (§3 kills the headline leg; rule (vii) Bayer makes its own; the only second-order read has the WRONG SIGN for a long)
**Company A / the news:** **2026-11-09** — the FDA approved Bayer's **Sunharbo (asundexian)**, a
**Factor XIa inhibitor**, to reduce stroke risk in adults with recent non-cardioembolic ischemic
stroke or high-risk TIA, in combination with antiplatelet therapy. **No financial impact was
quantified.**
**Company B / the candidate:** attempted three ways — (a) a contract manufacturer or API supplier
to Bayer; (b) the incumbent DOAC franchises (Eliquis — **BMY**/**PFE**); (c) US drug distribution
(**MCK**, **COR**, **CAH**).

**1. Mechanism (one sentence): FAILS ON EVERY LEG, AND LEG (b) FAILS WITH THE WRONG SIGN.**
⚠⚠ **A NEW FACTOR XIa COMPETITOR ENTERING THE ANTICOAGULANT MARKET IS BAD NEWS FOR THE INCUMBENT
FRANCHISES, NOT GOOD — THE ONLY DATEABLE ECONOMIC EFFECT POINTS DOWN, AND THIS IS A LONG-ONLY
BOOK (§3: no inverse, no derivatives).** Leg (a) dies on **rule (vii)**: Bayer manufactures its
own pharmaceuticals and **no external supplier is named by any source.**
**2. Dollar path: FAILS on leg (c) BY MAGNITUDE, independently of everything else.** A single
drug launch routed through distributors with **~$300B+ of annual revenue each** cannot move a
segment that is a double-digit share of their revenue; the contribution is immaterial by three
or more orders of magnitude. ⚠ **No figure was disclosed for the launch at all, so even this
arithmetic is bounded above by nothing.**
**3. Timing window:** *not reached.*
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **NOT REACHED.** No `move` call spent.
- Correlation (§4): **vacuous — zero open satellite positions.**
- Universe (§3): **BAYER IS GERMAN-LISTED (XETRA: BAYN) — §3-DEAD AS A CANDIDATE AT ANY PRICE.**
  ⚠ **This is the GEHC/IBA/Siemens Healthineers shape again under rule (vii): the integrated
  beneficiary names no external supplier, and the non-integrated alternatives are
  foreign-listed.** The ADR fails too — §3 bars ADRs of companies below the cap floor and does
  not create an eligibility route for a non-US primary listing.

**Outcome: REJECTED.** ⚠ **The useful half: this is the first time this log has met an approval
whose only second-order read is NEGATIVE. The funnel's FDA range now has three points — a first
approval (creates a chain), an expanded indication (creates nothing), and a COMPETITIVE ENTRANT
(destroys incumbent economics and is unplayable long).**

---

### T-2026-11-10-05 — the macro / policy complex (October payrolls +165k vs 59k consensus · October CPI landing today · Brent below $92 on Iran de-escalation · a $42B 10-year auction) — REJECTED (no Company A; the standing government-action object; the Brent leg is the 11-03 object at a new level)
**Company A / the news:** four items, one object. **(1)** October nonfarm payrolls **+165,000**
against a **59,000** consensus; unemployment **4.1%** from 4.2%; average hourly earnings **+0.4%
m/m, +3.1% y/y**. **(2)** October **CPI released today, after this seat** — consensus headline
**+0.3% m/m** (from 0.6%) and core **+0.2%** (from 0.3%); ⚠ **these are ESTIMATES and the source
said so explicitly, so NOTHING may be written as though the print were known.** **(3)** Brent
**below $92**, one source saying *"approaching $90"*, on reports that the Iran conflict is
*"effectively over."* **(4)** A **$42B** 10-year note auction; 2-year **4.552%**, 10-year
**4.869%**.
**Company B / the candidate:** none. There is no Company B because there is no Company A.

**1. Mechanism (one sentence): FAILS — NO TRANSACTION AND NO SECOND PARTY, FOUR TIMES OVER.**
**2. Dollar path:** the figures are real, large and belong to **nobody** — a payroll count, a
price index, a commodity quote and a Treasury auction size. ⚠ **§4 requires a disclosed figure
accruing to a NAMED company's segment revenue.**
**3 & 4.** *not reached.*

**Hard filters:** not reached on any leg.

**Outcome: REJECTED — and ZERO drill queries were spent, because the answer was already written.**
⚠⚠ **THE BRENT LEG IS THE ONE THAT NEEDED DISCIPLINE, AND IT IS A STRICTER TEST THAN ON 11-03:
that seat killed refiners/airlines on Brent at ~$104.33 after an 8.01% fall; Brent is now below
$92, so the move is roughly 12% LARGER and the direction unchanged.** ⚠ **A BIGGER MOVE IN THE
SAME OBJECT IS NOT A NEW EVENT. The standing finding is that SCALE MAKES THE
GOVERNMENT-ACTION/MACRO OBJECT MORE CONVINCING, NOT MORE REAL — and a commodity price falling
further is the purest instance of it.** ⚠ **The payrolls surprise is a ~2.8× beat against
consensus and is still CONSENSUS, not any company's own prior figure — rule (iii) fails on it
independently.**

---

### T-2026-11-10-06 — sweep: the defence IDIQ cluster, AAOI's unnamed hyperscaler, six own-results guidance prints, two private-counterparty deals, a filing, a lobbying story, and a Canadian curtailment — REJECTED (fourteen items, disposed as one, ZERO drill queries spent)
**Company A / the news:** everything else the four sweeps returned. Grouped because each dies on a
rule already named, and spending a query on any of them would be paying to re-derive a written
answer.

- **The defence/space IDIQ cluster — rule (v) CEILING, three instances in one morning.** **AEVEX
  (AVEX)** ~**$400M** ceiling, customer described only as *"a U.S. customer"* — the sweep itself
  disqualified it. **AeroVironment** **$940M** IDIQ, unnamed US customer, plus a **$315M** award.
  **Leidos** **$672M** TSA checkpoint-modernisation contract — ⚠ **the one with a NAMED
  counterparty, and it fails anyway: TSA is a GOVERNMENT payer, LDOS is the FIRST-ORDER recipient,
  and a multi-year contract value against ~$17B of annual revenue is not a segment dollar path.**
- **AAOI — rule (v), the unnamed hyperscaler.** Applied Optoelectronics disclosed (11-05) that a
  new hyperscale customer agreement *"could generate $1 billion–$1.5 billion of revenue for
  Applied Optoelectronics over three years."* ⚠ **The receiving company IS named — but it is
  AAOI's OWN revenue, i.e. first-order; the CUSTOMER is unnamed; "could generate" is a ceiling;
  and AAOI is a ~$2–4B cap, §3-dead.** Dated 11-05, so it also sits behind two seats that already
  swept that window.
- **Six own-results guidance prints, all RAISES, none with a named counterparty: Telos (TLS)**
  revenue $187–200M → **$198.2–200.7M**; **NGS** EBITDA $103–108M → **$105–108M**; **Elanco
  (ELAN)** revenue to **$5.155–5.18B**; **Solventum (SOLV)** EPS to **$7.20–7.30**; **P3 Health
  (PIII)** EBITDA midpoint to **$100M**; **PubMatic (PUBM)** — ⚠ **direction not establishable,
  no prior company range in the source, which is rule (iii)'s AAR shape (fail in BOTH
  directions, not a pass).** ⚠ **All first-order; the source states no named customer, supplier
  or capex figure appears in any of them.** *(AAON's raise is the strongest of the set and was
  given its own entry at `T-2026-11-10-02` rather than buried here.)*
- **Two deals whose recipient is PRIVATE — rule (viii).** **Stellantis / Roshel**, a Brampton
  plant agreement (Roshel is privately held, Canadian). **Neo Performance Materials** raised FY
  EBITDA to **$180–185M** — **TSX-listed / OTCQX**, §3-dead.
- **Compass Pathways (CMPS)** completed its **COMP360 NDA submission** — ⚠ **a FILING is not a
  DECISION; the source notes the FDA had not confirmed acceptance for review.** Rule (vi).
- **Hims & Hers (HIMS)** will offer compounded peptides after regulators eased enforcement — ⚠
  **enforcement discretion, not an approval; HIMS is the first-order beneficiary; the peptide API
  tier is unnamed (rule (v)); no figure disclosed.**
- **Microsoft lobbying the administration to scuttle an EXPECTED ban on Chinese data-center
  technology** — ⚠⚠ **the most tempting item in the sweep and it is a non-event twice over: the
  ban HAS NOT HAPPENED (rule (vi), pending), and lobbying AGAINST it is the opposite sign from
  the US-alternative-supplier story a reader wants to build. No named recipient, no figure.**
- **Goodyear** expects a **$15–20M** annual operating-income benefit — **from its OWN plant
  closures**; rule (viii), the company's own cost line, no second company named as receiving
  redirected volume. **Quesnel River Pulp / Millar Western** indefinite curtailment — not
  establishably US-listed, §3.
- **NVIDIA** reportedly investigating CEO Jensen Huang over an alleged relationship with an
  executive at a Singaporean company suspected of smuggling chips into China — ⚠ **a governance
  story: no regulatory finding, no penalty, no contract cancellation, no figure. And NVDA is at
  rule (iv) FOUR appearances in five sessions.**

**Hard filters:** not reached on any item — every one dies at part 1 or part 2, or on §3, before
a filter is due. **Zero `move` calls and zero drill queries were spent on this entire group.**

**Outcome: REJECTED.** ⚠ **The honest summary of the sweep: the morning's four largest dollar
figures were $10B (an unallocated ceiling), $1.5B (a "could generate" to an unnamed customer),
$940M (an IDIQ ceiling, unnamed customer) and $672M (a government payment to the first-order
recipient). NOT ONE OF THEM IS A SECOND-ORDER SEGMENT DOLLAR PATH, and the aggregate size of
that list is precisely why §4 puts the hard filters BEFORE the thesis.**

---

### 2026-11-09 (07:02 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$97,368.33** at pre-flight).
`clock` 07:02:15 — `is_open: false`, `next_open` **2026-11-09T09:30:00-05:00**, `next_close`
**2026-11-09T16:00:00-05:00**: both carry today's date, the pre-market full-session signature.
**NOT a holiday** — read off the DATES, not the boolean. Fired ~58 min early against a nominal
08:00, the **sixth** EST session running (observation only — `control.md` forbids diagnosing a
schedule from a firing time).

**✅ WEEK ROLLOVER EXECUTED.** `isocalendar` gives **2026-W46, weekday 1**; Monday anchor
**2026-11-09** ≠ `week_of` **2026-11-02**, so `week_of` advances and `new_positions_this_week`
resets to **0** (it was already 0 — the reset is recorded as *performed*, not as *unnecessary*,
because §6's cap must not depend on the Friday seat having run).

**✅ NO BACKFILL WAS DUE, FOR THE FIRST MONDAY IN THIS FAULT'S HISTORY.** The 11-06 close seat
held past the bell and committed the official **VOO close 676.02**, so this seat inherited a
complete Friday. Broker `lastday_price` reads **675.99** — 3¢ below the bar close, inside the
known moving broker/bar midpoint and requiring nothing.

**Ledger reconciliation CLEAN, re-derived three ways:** `positions.md` satellite block count **0** ·
`sleeves` `satellite.count 0` / `pct 0.0` · `positions` returns **core VOO only** (99.046311231 sh
@ 706.74, cost basis $69,999.99 — unchanged since the 2026-09-03 fill; only the mark moves).
**No disagreement, so no reconciliation work.** Core **$67,368.33 / 69.19%**, `core_in_band: true`,
`rebalance_delta` **789.50**, **NOT DUE**. Cash **$30,000.00 / 30.81%**.

**FOUR BROAD SWEEPS, AND THREE OF THEM ANSWERED §4's QUESTION IN THE NEGATIVE OUT LOUD.** The
weekend sweep returned four items (below). The transaction sweep stated there were **"no qualifying
named supply agreement, offtake contract, capacity expansion, or long-term purchase commitment"** by
a US-listed company 11-06→11-09. The regulatory/8-K sweep found **one** item (FTAI, a refinancing)
and an explicit nil return on FDA, FTC/DOJ/FCC/EPA, plant closures, strikes and recalls. The
structural sweep — which asked for §4's shape directly, requiring **one sentence containing both the
dollar figure and the name of the receiving company** — returned **"No qualifying disclosure was
identified."** ⚠ **A Monday after a thin weekend is the funnel's most common shape, and the explicit
nil returns are worth more than the four items they came with.**

⚠ **ONE DRILL QUERY SPENT ALL RUN, on COHR, and it was spent because that item was the only one in
four sweeps carrying a real dollar figure beside a named US-listed leg.** It came back with four
independent kills.

---

### T-2026-11-09-01 — COHR (Coherent) — PhotonLink ~$20B five-year agreement — REJECTED (part 3 ramps in CY2028; rule (v) customer unnamed; rule (vii) internal capacity; and it is the FIRST-ORDER leg)
**Company A / the news:** Coherent disclosed on **2026-11-04**, with its FQ1-2027 results, an
approximately **$20 billion, five-year PhotonLink agreement** with a second anchor AI-datacenter
customer. Management guided total PhotonLink revenue to **>$100M in the March 2027 quarter** and
**$250M per quarter before the end of CY2027**.
**Company B / the candidate:** attempted two ways — (a) COHR itself, (b) COHR's external
indium-phosphide / substrate / laser-component suppliers.

**1. Mechanism (one sentence):** *(b)* "Coherent's $20B PhotonLink award causes [supplier]'s
compound-semiconductor revenue to rise because Coherent must buy more indium phosphide to fill it."
⚠ **The source refuses the subject of that sentence: Coherent said it had EXPANDED ITS OWN INTERNAL
indium-phosphide capacity and secured substrates and critical materials, and NO external supplier,
foundry or component partner is named, with or without a figure.** Rule **(vii)** — vertical
integration leaves no external supplier to find — and rule **(v)**, an unnamed supply base.
**2. Dollar path:** *(b)* does not exist: no segment, no name, no figure. *(a)* is a real dollar
path and it is **COHR's own revenue line**, i.e. the first-order leg §4 exists to avoid.
**3. Timing window:** ⚠ **KILLS IT INDEPENDENTLY AND NEEDED NO SECOND THOUGHT. Revenue from this
agreement "is expected to begin ramping in EARLY CALENDAR 2028"** — ~5 quarters before the ramp
*starts*, against §4's **two-quarter** ceiling. The >$100M March-2027 and $250M/quarter CY2027
figures are **total PhotonLink run-rate, apparently including the previously announced NVIDIA
business**, not this agreement.
**4. Invalidation:** not written — three parts failed first.

**Hard filters:**
- **Priced-in (§4): `move --sessions 5` returns `move_pct` −8.32% (210.28 → 192.79), `priced_in:
  true`, "LATE — skip".** ⚠⚠ **THIRTEENTH INSTANCE OF THE DIRECTION-BLIND `move` DEFECT, and the
  first on a non-semiconductor name: COHR FELL 8.32% and one source headline reads "Coherent sinks
  16% despite $20B". The script thresholds ABSOLUTE five-session magnitude, so it calls a decline
  "LATE".** ⚠ **THIS VERDICT IS NOT LOAD-BEARING HERE AND IS NOT BEING LEANED ON — the thesis was
  already dead at part 3 and rule (v). Recorded because the defect's instance count is the evidence
  the human needs, and because a seat that had nothing else would have taken the free "skip" and
  never noticed the filter had answered the wrong question.**
- Rule (iii): **a genuine PASS on the agreement, a FAIL on the programme.** PhotonLink itself was
  announced **September 2026** and a PhotonLink long-term agreement with **NVIDIA** in **March
  2026**; this agreement is a *new, second* anchor customer as of 11-04 and is not a re-announcement.
  ⚠ **Applied to the figure the mechanism runs on, per the 10-15 rule, and the figure is new.**
- Correlation (§4): **no operand** — zero open satellite positions, so no `driver` to collide with.
- Universe (§3): COHR is US-listed, market cap well above $10B. **Not reached** — not the binding test.

**Outcome:** REJECTED. ⚠ **The best-evidenced candidate in four sweeps and it dies four times over.
The instructive part is the shape: a disclosure that is large, dated, genuinely new, carries an exact
dollar figure, and names a US-listed company — and the named company is the one RECEIVING, with the
payer withheld. There is no Company A to pivot from, only a Company B wearing the headline.**

---

### T-2026-11-09-02 — the sovereign-AI infrastructure tier ← NVIDIA / SK Telecom / Rebellions collaboration — REJECTED (part 2, the source states no value, volume or timing exists; §3 on both counterparties; rule (iv) on NVDA)
**Company A / the news:** NVIDIA announced on **2026-11-09** a sovereign-AI collaboration with
**SK Telecom** and **Rebellions**, supported by South Korea's Ministry of Science and ICT, to build
Korean-model AI infrastructure using **NVLink Fusion**.
**Company B / the candidate:** sought among US-listed suppliers of NVLink-Fusion-adjacent
interconnect, networking and rack infrastructure.

**1. Mechanism (one sentence):** would require naming a US-listed company that receives an order
because of this collaboration. **No such company is named anywhere in the announcement.**
**2. Dollar path:** ⚠ **THE SOURCE APPLIED THE KILL AND VOLUNTEERED IT: "does not state contract
value, unit volumes, delivery timing, or revenue guidance, so commercial impact cannot be quantified
from the available evidence."** No figure of any kind exists, so there is nothing to allocate even to
a guessed recipient.
**3. Timing window:** not reachable — sovereign-AI buildouts are rule **(vi)** shaped (multi-year,
government-supported, undated), but part 2 ended it first.
**4. Invalidation:** not written.

**Hard filters:** not run — §3 kills both counterparties before a filter is needed (**SK Telecom is
Korea-listed; Rebellions is a private Korean company**), and the only buyable leg, NVDA, is the
**first-order** announcer. ⚠ **Rule (iv): NVDA's THIRD arrival in this funnel in four sessions
(11-05 unwind · 11-06 IREN · today) and it has died at a different rung each time — part 1, then
part 2, now part 2 again. A ticker that keeps arriving and keeps dying is telling you about its
industry's disclosure practice: NVIDIA announces COLLABORATIONS, which are frameworks without
figures.** ⚠ **The tempting move was a drill query asking who supplies NVLink Fusion racks. That is
asking the funnel to fill in an unnamed tier — rule (v) — and it was declined. ZERO drill queries
spent.**

**Outcome:** REJECTED on part 2, by the source's own sentence.

---

### T-2026-11-09-03 — the children's-apparel and liquidation complex ← The Children's Place Chapter 11 and §363 sale — REJECTED (every named recipient is PRIVATE; the only other story is a reader-supplied share shift; §3 kills PLCE)
**Company A / the news:** The Children's Place filed **Chapter 11** in New Jersey on **2026-11-09**
and said it intends to sell substantially all assets under **§363**, bids due **December 9**,
court-supervised sale expected by end-December. It entered an inventory-sales consulting agreement
with **GA Group, Tiger Group and SB360 Capital Partners**.
**Company B / the candidate:** attempted three ways — the named consultants, competing
children's-apparel retailers, and the landlords.

**1. Mechanism (one sentence):** the consultants' version is the only one with a *named* recipient,
and it fails on §3 rather than on logic. The competitor version needs *"a liquidating competitor
frees shelf space — and also [retailer] captures it rather than the off-price channel or the
private-label aisle"*: an **"and also"**, so part 1 refuses it. The landlord version has the **wrong
sign** — a REIT losing a tenant is a cost, not a tailwind.
**2. Dollar path:** ⚠ **GA Group, Tiger Group and SB360 Capital Partners are ALL PRIVATE. The money
in this transaction moves to parties that cannot be bought at any price** — rule (viii)'s
GEHC/Sofie shape (consideration paid out to a private seller), arriving here as *three* named
private recipients at once. No competitor is named as receiving anything, and no figure is attached
to any of them.
**3. Timing window:** the sale completes end-December, inside two quarters — ⚠ **the one part this
candidate passes, which is exactly why it is worth an entry rather than a line in the sweep.**
**4. Invalidation:** not written — parts 1 and 2 failed.

**Hard filters:** §3 kills **PLCE** itself (microcap, far below the $10B floor) and kills all three
consultants (unlisted). **ZERO drill queries spent.**

**Outcome:** REJECTED. ⚠ **ASK WHO IS NAMED AS RECEIVING, NOT WHO MUST ARITHMETICALLY BE RECEIVING
(11-04). Here the question has an answer — three firms, named in the filing — and the answer is
unbuyable. An ANSWERED blank with no listed occupant is a cleaner kill than an unnamed tier, and it
is NOT a new shape: it is the private-recipient entry under rule (viii), with the novelty only that
a bankruptcy produces three of them in one disclosure.**

---

### T-2026-11-09-04 — the macro / policy complex (October payrolls · the December hike repricing · the midterm read-across) — REJECTED (no Company A; the standing government-action object; rule (iii) on the revisions)
**Company A / the news:** October payrolls **+165,000** against expectations of ~**65,000**;
unemployment **4.1%**; wages **+0.4% m/m, +3.1% y/y**; August–September revised up a combined
**+84,000**; CME pricing implying roughly a **75% probability of a December Fed rate hike**; October
CPI due **11-10** and PPI **11-13**. A commentary source added that Democratic control of Congress
raised expectations of regulatory scrutiny of AI and data-center development.
**Company B / the candidate:** none nameable.

**1. Mechanism:** refused. ⚠ **A GOVERNMENT ACTION IS NOT A COMPANY A, and a market-implied
probability that MOVED is its most seductive costume — it reads like an event with a date. One
party, no transaction, no named recipient.** The AI-scrutiny leg is weaker still: the source itself
marks it as **the article's interpretation, not a reported agency action** — a third party remarking
on a condition.
**2–4:** not written.
**Rule (iii):** the **+84,000 revision is to AUGUST AND SEPTEMBER data** — a restatement of months
already reported, not new economic news, which fails rule (iii) independently of everything above.
⚠ **The ~75% December-hike figure is recorded as a REPORTED MARKET PRICE and is NOT being treated as
established** — the 11-06 seat logged two contradictory answers from this same model on this same
question four days ago, so a single uncorroborated probability is quoted with its provenance or not
at all.

**Outcome:** REJECTED. **ZERO drill queries spent — the answer was already written in the standing
rules and re-deriving it would have been the expense, not the discipline.**

---

### T-2026-11-09-05 — sweep: six own-results guidance prints, one refinancing, one Canadian merger — REJECTED (eight items, disposed as one, ZERO drill queries spent)
**Guidance raises, all dated 2026-11-09, all FIRST-ORDER prints naming no second party — part 1 ends
every one of them before rule (iii) matters:** **PCTY** FY revenue to a $1.92B midpoint from its own
$1.89B · **CNH** FY2026 adj. EPS to $0.44–0.48 from its own $0.41–0.46 · **PFE** 2026 revenue +$1.5B
to $62–64B · **INSM** BRINSUPRI to $1.35–1.40B and ARIKAYCE to $460–470M · **CTEV** a preliminary
2027 revenue expectation of $1.1B · **CL** 2026 net-sales growth of 4–5%.
⚠⚠ **THE INSTRUCTIVE PAIR, AND IT IS THE 09-29 IOVA/AAR PAIR ARRIVING AGAIN FROM ONE QUERY: PCTY and
CNH are CLEAN rule (iii) PASSES — the source carries each company's OWN prior figure — and PFE, INSM,
CTEV and CL are rule (iii) FAILS, with the new range present and the prior one absent. All six die
anyway, at part 1, for want of a Company B. A clean pass on one filter is not progress toward a
trade, and the six-way split is the cheapest available demonstration of it.**
**FTAI Aviation** — $1.0B of 7.125% senior notes due 2034 issued 11-06 (8-K filed 11-09), proceeds
to repay the revolver and redeem $500.0M of 5.50% notes due 2028. ⚠ **Rule (viii): money paid IN as
financing and OUT as debt redemption, on the filer's own balance sheet. The opposite sign from
revenue, twice, and no second party.**
**Strathcona Resources / Greenfire Resources** — definitive agreement, Alberta plan of arrangement,
disclosed 11-08; Greenfire Q3 production 27,166 bbl/d, roughly double the prior quarter. ⚠ **§3:
both are Canadian-listed, so neither is buyable at any price. Merger arbitrage is not in §4
independently, and the production jump is attributed to the Connacher acquisition and an
operatorship assumption — i.e. to prior transactions, which is rule (iii).**

**Outcome:** all REJECTED. **ZERO drill queries spent beyond the four broad sweeps.**

---

### 2026-11-06 (07:03 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$96,930.54** at pre-flight).
`clock` 07:03:02 — `is_open: false`, `next_open` **2026-11-06T09:30:00-05:00**, `next_close`
**2026-11-06T16:00:00-05:00**: both carry today's date, the pre-market full-session signature.
**Not a holiday.** Fired ~57 min early against a nominal 08:00, the **fifth** EST session running
(observation only — `control.md` forbids diagnosing a schedule from a firing time).

**✅ THE 2026-11-05 OFFICIAL CLOSE IS BACKFILLED, AND THE PREDICTION WAS WRONG BY $2.14 IN THE
DIRECTION THAT MATTERS.** `bars --symbol VOO --days 4 --adjustment all` gives **VOO 2026-11-05
`c` 673.94** (o 703.73 · h 703.90 · l 673.58 · n 4,331 · v 170,486 — *2.5x the 70-session
participation norm*). The 15:16 close seat read **676.075** off a partial bar and flagged it as
partial and unstamped; the official print is **$2.135 LOWER**, so the true session was
**−4.3731%** (704.76 → 673.94), not the −4.04% that seat computed. ⚠ **The partial bar was not
merely imprecise — it understated the largest single-session decline in this repo's history by
8% of its own magnitude. That is the §5.4 exposure in item (12)/(15) priced in dollars, and it
only cost nothing because the satellite ledger is empty.** Nothing beyond the mark was lost.

**Ledger reconciliation CLEAN, re-derived three ways:** `positions.md` satellite block count **0** ·
`sleeves` `satellite.count 0` · `positions` returns **core VOO only** (99.046311231 sh @ 706.74,
cost basis $69,999.99, unchanged since the 2026-09-03 fill — only the mark moves). **No disagreement.**

**The day's tape is a VALUATION UNWIND, not a transaction.** S&P −4.4% / Nasdaq −5.5% / **SOX −12%,
its second-largest decline on record**; all 11 sectors lower; tech sector −7.3%. Named moves: NVDA
−9.3% (largest single S&P drag) · AMD −17.3% · MU >−17% · SNDK ~−22% · MRVL ~−17% · INTC −10% ·
CoreWeave −9.8% · GEV −7.5% · MSFT/META/AMZN/GOOGL each −2% to −4%. Reported drivers: the Democratic
midterm sweep read as a policy risk to the AI data-center buildout, plus a broad reassessment of AI
capex sustainability. ⚠ **No source establishes a single triggering announcement** — which is
precisely why this is not a §4 object. Three broad queries spent; a fourth asked for §4's *structure*
(named Company A, named US-listed Company B, disclosed dollar value) and returned **zero confirmed
matches**.

⚠ **ONE SOURCE CONFLICT, RECORDED UNRESOLVED RATHER THAN PICKED.** The first sweep reported traders
pricing **">80% probability of a December Fed rate INCREASE to 4.00–4.25%"** (Reuters Take Five).
The second query, asked directly, said the available reporting **does not support a December hike
expectation at all** and declined to state a figure. **Both answers are from the same model on the
same morning.** Nothing turns on it — macro has no Company A — but a seat that quoted the first
number as fact would have published an unverified claim about the direction of Fed policy.

---

### T-2026-11-06-01 — the AI-infrastructure / semiconductor complex (NVDA · AMD · MU · MRVL · INTC · SNDK) ← the 11-05 valuation unwind — REJECTED (part 1, no Company A; a repricing is not a transaction)
**Company A / the news:** None exists. The 11-05 selloff is a market-wide reassessment of AI capex
and of post-midterm data-center policy risk. No source identifies a triggering announcement.
**Company B / the candidate:** The whole crashed complex, considered as a "buy the dislocation" idea.

**1. Mechanism:** *Unwritable.* The closest honest sentence is "a broad repricing causes these names
to be cheaper", which names no revenue or cost line and no causal path to one. **Part 1 fails on the
first clause.**
**2. Dollar path:** No segment, because no event touched a segment. Not reached.
**3. Timing window:** Not reached.
**4. Invalidation:** Not reached.

**Hard filters:** not reached on the thesis parts — but run anyway, because the *reading* is the
finding: **NVDA −15.03% · MU −29.51% · AMD −28.79% · QCOM −15.38% over five sessions, and all four
return `priced_in: true` / "LATE — skip per strategy.md section 4".**

**Outcome:** REJECTED at part 1. §4's buy rule is *"news breaks about Company A; you look for Company
B whose economics improve because of it"* — a sleeve-wide drawdown has no Company A, and treating
"it fell a lot" as a catalyst is the honest-broker failure in its purest form. ⚠⚠ **AND THE FILTER
CONSEQUENCE IS NEW, FORWARD-LOOKING, AND BIGGER THAN THE PREVIOUS EIGHT INSTANCES COMBINED: the
direction-blind `move` defect now blocks the ENTIRE semiconductor complex for the next five sessions
BECAUSE IT CRASHED. Twelve "LATE" verdicts on twelve declines across five sessions. Until ~11-12,
any genuine §4 candidate anywhere in semis dies at the hard filter before its thesis is read —
regardless of merit.** ⚠ **Obeyed anyway: the filter fails safe, over-blocking and never wrongly
permitting, and a seat must not reason past `priced_in: true` on the grounds that the move was
negative. The fix is a signed threshold in `scripts/alpaca.py` and is NOT a seat's to install.**

---

### T-2026-11-06-02 — the AI build tier / NVDA ← IREN's delayed Microsoft deliveries, $15B further spend, $18.95B capital commitments — REJECTED (rule (v) on the tier; part 2 on NVDA; rule (iv), second consecutive session)
**Company A / the news:** IREN disclosed delayed infrastructure deliveries **for Microsoft**, an
additional **$15B** spending push, a slip of its >$4B annualised revenue run rate from year-end to
January/February, **$18.95B** of capital commitments at Sept 30 (from $13.81B), and **$5.82B** of
GPU hardware on balance sheet (nearly 3x the prior quarter). Counterparties: "Nvidia, Microsoft and
13 others."
**Company B / the candidate:** (a) whoever supplies the $15B of build; (b) NVDA as the one named
hardware counterparty; (c) Microsoft's alternative capacity providers, as the delay's beneficiaries.

**1. Mechanism:** Leg (a) is **rule (v)** — the $15B names no recipient; 13 of 15 counterparties are
explicitly unnamed. Leg (c) needs a second clause to stand up ("the delay frees Microsoft demand
*and* someone else can absorb it *and* that is disclosed somewhere"), which §4 says is the test it
fails. Leg (b) is writable: *IREN's purchase of $5.82B of GPUs causes NVDA's data-center revenue to
rise because IREN is a named direct customer.*
**2. Dollar path:** **Leg (b) fails here.** $5.82B is a *cumulative balance-sheet* figure, not a
period sale, against an NVDA data-center line running far above $100B/yr — **well under §4's 10%
materiality floor**, and the incremental quarter is smaller still. No source quantifies the delay,
so leg (c) has no dollar path at all.
**3. Timing window:** Not reached.
**4. Invalidation:** Not reached.

**Hard filters:** NVDA **−15.03% / `priced_in: true`** — independently LATE. Universe: IREN itself is
the headline leg and §3-dead on the cap floor as established 11-05.

**Outcome:** REJECTED. Three legs, three independent kills: unnamed recipient (v), sub-10% materiality
(part 2), and a mechanism needing an "and also" (part 1). ⚠ **Second consecutive session on this
ticker and the second consecutive rejection — rule (iv): a recurring non-event in a fresh costume is
not fresh evidence when the kill is structural. Yesterday it was $2.8B of AI-cloud contracts; today
it is $15B and a delay. The blank where the recipient's name goes is identical.**

---

### T-2026-11-06-03 — the smartphone-silicon tier ← QCOM −9.5% on weak handset chip sales — REJECTED (part 1, an own-results miss is not a transaction; §3 on the only named beneficiary)
**Company A / the news:** Qualcomm fell ~9.5% after quarterly results showed weaker-than-expected
smartphone-chip sales.
**Company B / the candidate:** share gainers in handset application processors / modems.

**1. Mechanism:** The only writable version is *QCOM's handset share loss causes <rival>'s SoC revenue
to rise because the sockets moved* — **but no source names a rival taking the share, or a socket that
moved.** The weakness is reported as end-demand, not displacement, so there is no transfer to trace.
**Part 1 fails for want of a Company B, not for want of a sentence.**
**2. Dollar path:** The structurally obvious candidates are **MediaTek (Taiwan-listed) and Apple's
in-house modem**. MediaTek is **§3-dead** (not US-listed). The Apple leg fails part 2 — a modem
BOM saving is immaterial against ~$400B of revenue — and part 3, since that transition has run for
years and is nowhere near a two-quarter window.
**3. Timing window:** Not reached.
**4. Invalidation:** Not reached.

**Hard filters:** QCOM **−15.38% / `priced_in: true`**; §3 kills the only named beneficiary.

**Outcome:** REJECTED at part 1. **Rule (iii)'s shape:** a company's own results print is not a
transaction with a counterparty, and a *miss* does not become a §4 event by being large. The share
that left QCOM has no disclosed destination, and inventing one is exactly what the honest-broker rule
is for.

---

### T-2026-11-06-04 — the US aerospace rare-earth buyer ← MP Materials' $31.6M SEG+ supply to an unnamed customer — REJECTED (rule (v), counterparty unnamed; part 2 independently)
**Company A / the news:** MP Materials began supplying **SEG+** to an **unnamed US aerospace
customer**, generating **$31.6M** of quarterly revenue; Q3 net loss $20.7M (from $41.8M), adjusted
profit beat.
**Company B / the candidate:** the aerospace buyer — a first domestic rare-earth supply relationship.

**1. Mechanism:** *Unwritable for want of a subject.* ⚠ **This is rule (v)'s most fillable blank of
the week and it was recognised as such before any drill query was spent: there are perhaps four
US-listed aerospace primes it could plausibly be, the temptation to name one is strong, and a
REDACTION IS NOT A LEAD. Zero drill queries spent.**
**2. Dollar path:** **Fails independently even if the name arrived.** $31.6M is MP's *revenue*; the
buyer's *cost* line is at most that, against primes with $40–80B of revenue — **four orders of
magnitude below §4's 10% floor.** A supply relationship can be strategically important and
financially immaterial, and §4 tests the second.
**3. Timing window:** Not reached.
**4. Invalidation:** Not reached.

**Hard filters:** not reached. MP itself is the headline leg, not a second-order candidate.

**Outcome:** REJECTED on rule (v) and part 2, either sufficient. **The part-2 kill is the useful one**
— it means this item would still be dead on the session the counterparty is named, so a future seat
meeting the named version should not re-open it.

---

### T-2026-11-06-05 — sweep: a guidance raise, two defence awards, an unnamed-utility offtake, two financings, three non-qualifying telecom items, and the macro complex — REJECTED (nine items, disposed as one, ZERO drill queries spent)
**Disposed together because each dies on a standing rule at sight:**

- **IonQ** — FY26 revenue guide raised to **$505–515M**, RPO >2x to **$1.2B**. **Rule (iii)**, an
  own-results print. Second-order suppliers are **unnamed** (v); and against a $0.5B revenue base no
  supplier's exposure can clear part 2.
- **Pegasystems** — **$419M ceiling**, 10-year US Army IDIQ. **US defence program award: fifteenth
  instance, and the standing finding is that this shape cannot produce a §4 candidate.** Independently:
  **an IDIQ ceiling is not revenue** (no obligated dollars), and PEGA is the headline leg, not a
  Company B.
- **Arcfield** — **$156.5M** Navy follow-on. Defence award **and privately held — §3-dead.**
- **Uranium Energy (UEC)** — long-term sales, **1.1M lb through 2032**, to **"two US nuclear
  utilities"**: **(v)** unnamed, **no dollar value**, **§3** on the cap floor, and **2032 is ~24
  quarters past §4's two** (rule (vi)). Four independent kills.
- **Sinochem** — **>$12.8B** of procurement agreements. **Non-US party, no named US-listed recipient,
  no allocation of the figure.** The largest number in the sweep and the emptiest.
- **Cameco** — **$1B** equity distribution arrangement. **Rule (viii)** shape: capital raised, not
  revenue committed.
- **Evertec** — **$300M** revolver. Financing, not a transaction with a counterparty's revenue line.
- **FirstLight / Comm1 / Ribbon** — a fiber deal for an unnamed hyperscaler; a technology selection
  with no value and no evidence the buyer is US-listed. **(v) + no dollar figure.**
- **The macro complex** — October payrolls (consensus +65k after +29k; UR 4.2%, wages 2.9% — *released
  today, not yet out at this seat*), Williams on inflation, and the disputed December Fed pricing.
  **No Company A. Rule (iii) on the Fed leg.** ⚠ **Today's payroll print lands at 08:30 ET, between
  this seat and the next: a genuine event this seat cannot see, and no reason to pre-position.**

**Outcome:** REJECTED, all nine. ⚠ **The honest summary of the whole morning: the one largest market
event in this repo's 71-session history produced NOT ONE §4-shaped object, and that is not a paradox
— a −4.4% tape is a repricing of expectations, and §4 only buys a change in somebody's disclosed
revenue or cost line. The absence is the measurement.**

---

### 2026-11-05 (07:02 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,923.72** at pre-flight).
`clock` at 07:02:39 reads `is_open: false`, `next_open` **2026-11-05T09:30:00-05:00**, `next_close`
**2026-11-05T16:00:00-05:00** — both carry today's date: the pre-market full-session signature.
**Not a holiday.** ⚠ **Fired ~58 min early against a nominal 08:00 ET, the FOURTH EST session running.
RECORDED AS AN OBSERVATION, NOT DIAGNOSED** — `control.md` forbids diagnosing a schedule fault from a
run timestamp. ⚠⚠ **AND THIS SEAT ADDS ONE GENUINELY NEW FACT TO THAT ITEM, WHICH IS A FAILED ATTEMPT
TO RE-VERIFY IT: `CronList` returns *"No scheduled jobs"*, so these routines are NOT CronCreate jobs
and the stored schedule is NOT readable from inside a session. The `13:35:00 UTC` figure for routine 2
is the 11-02 seat's reading and CANNOT be independently confirmed by any later seat. It is carried as
INHERITED, and no seat should write it again as though it had checked.**

⚠⚠⚠ **FIRST THING, AND IT DISCHARGES THE CARRY-FORWARD ITEM — BUT THE DISCHARGE IS THE FINDING, NOT
THE NUMBER: 2026-11-04's OFFICIAL CLOSE IS BACKFILLED AND IT WAS SUBSTANTIVELY EMPTY.** VOO `c`
**704.76** (`bars --days 4 --adjustment all`, `v` 67,294, `n` 2,245). The close seat fired at 15:16 ET,
44 min before the bell, and wrote nothing — **correctly.** **Close-basis 11-04: equity $99,803.88 · day
+$1,108.33 / +1.1230% on 11-03's official $98,695.55 · since inception −0.1961% · VOO −0.2802% against
its 706.74 cost basis.**
✅ **METHOD VALIDATED RATHER THAN ASSERTED, AND THIS IS THE REASON TO TRUST THE FIGURE ABOVE: the same
arithmetic (`99.046311231 × c + $30,000`) reproduces 11-03's inherited close-basis equity to the CENT
($98,695.55). A backfill method that reproduces the previous backfill is worth more than a backfill
that merely looks plausible.**
⚠⚠ **AND THE REASON THE BACKFILL COST NOTHING IS THE EMPTY SLEEVE, NOT THE METHOD: with ZERO satellite
positions there was no `highest_close` to stamp and §5.4 had NO OPERAND. Core VOO is §5-exempt.** ⚠
**TWO INDEPENDENT BLOCKERS WERE LIVE ON 11-04 AND ONLY ONE HAS EVER BEEN TESTED. The day the sleeve is
non-empty, a pre-close mark stamped as a close mis-sets that position's trailing stop FOR ITS WHOLE
LIFE, and fixing the timing alone fixes nothing while the sleeve is empty.**
✅ **Broker-pair cross-check run: `lastday_price` **704.78** vs bar `c` **704.76** = **$0.02 / 0.0028%**,
the tightest pair on record, displacing 11-03's $0.03. Normal venue noise. Neither stamped.**

**Window surveyed:** Wednesday 2026-11-04 after the close through this morning. **Six queries, five
theses, ZERO survivors.** ⚠ **FIVE of the six broad queries returned the KILL VOLUNTEERED BY THE
SOURCE**, in the source's own words — *"no qualifying announcements can be confirmed"* · *"no verified
report … established a major US regulatory approval, supply agreement, capacity announcement, or
guidance change involving two clearly identified corporate parties and a disclosed transaction value"* ·
*"no available result reports a capacity expansion or new plant with a disclosed dollar figure"* · *"the
available results do not support a complete ranking"* · *"no announcement … meets the requested
categories involving a named company and a separate publicly traded US supplier, partner, or
counterparty."* ⚠⚠ **ASKING FOR THE NAMED COUNTERPARTY AND THE DOLLAR FIGURE IN THE SAME SENTENCE IS
STILL WHAT PRODUCES THE VOLUNTEERED KILL, and it is now the cheapest line in this funnel.**

⚠⚠⚠ **THE DAY'S STRUCTURAL FINDING: THE TAPE MOVED A LOT AND CONTAINED NO EVENT.** MSFT **+6.68%**,
AMZN **+6.12%**, AAPL **+5.31%** (AAPL passing NVDA on market cap at **$5.08T**) — and **every source
attributed the session to a broad mega-cap rally on a divided-government election read, naming NO
company-specific catalyst for any of the three.** ⚠ **A ~6% day in three of the five largest companies
on earth is the largest tape this funnel has ever surveyed, and §4 got NOTHING from it, because §4 asks
for a TRANSACTION and a rally is a MARKET.** ⚠⚠ **SCALE MAKES IT MORE CONVINCING, NOT MORE REAL — the
standing macro/government object, arriving at the largest size it can arrive at.**

**Ledger reconciled, three sides, re-derived not inherited.** Alpaca `positions` = **one row, core VOO
only** (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, **unchanged since 2026-09-03 — only the
mark moving**; `current_price` **706.20** is a LIVE PRE-MARKET PRINT at **+0.2043% over the official
11-04 close**, stamped nowhere and quoted nowhere as a close) · `positions.md` satellite block count
**0** · `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **No discrepancy.**

**Every §6 gate open.** Breaker INACTIVE, `halt_triggered_at: none`; `new_positions_this_week` **0 of
3**; satellite **0.0%** deployed, **$30,000 idle**; `control.md` Notes empty; zero open alerts. 5% cap
**$4,996.19**. **Week anchor re-derived with `isocalendar`: 2026-11-05 is ISO 2026-W45, weekday 4,
Monday anchor 2026-11-02 — MATCHES `week_of`. No rollover; not rolled a second time.**
⚠ **NOTHING BLOCKED A BUY TODAY EXCEPT THE CANDIDATES. That distinction is the whole value of this
entry: a gated no-trade day and a researched no-trade day are indistinguishable in the sleeve
percentages, and only this line separates them.**

⚠⚠ **THE DIRECTION-BLIND `move` DEFECT FIRED AGAIN — FOURTH CONSECUTIVE SESSION, SEVENTH AND EIGHTH
NAMES. NOT A NEW FINDING, and this seat's first draft of the plan wrongly called it one; the claim is
REPLACED rather than left beside its correction.** **IREN −24.70%** and **NVDA −7.04%** both returned
`priced_in: true` / *"LATE — skip per strategy.md section 4"*. Tally: **INTC −24.36% (11-02) · MU
−7.77% · SNDK −14.40% · STX −7.87% · WDC −4.96% (11-03) · ON −7.69% (11-04) · IREN −24.70% · NVDA
−7.04% (11-05)** — **eight "LATE" verdicts on eight DECLINES across four sessions, and not one "LATE"
on a RISE in the whole series.** ⚠ **OBEYED ANYWAY: the filter FAILS SAFE — it over-blocks and can
never wrongly PERMIT — so a seat must not reason past a `priced_in: true` because the move was
negative.** ⚠ **Both names died independently on part 2 and on §3, so nothing turned on it.** ⚠ **The
fix is a signed threshold in `scripts/alpaca.py`: SCRIPT-LEVEL, NOT A SEAT'S TO INSTALL.** Reported
2026-11-03; **re-notified 11-05 because the tally has DOUBLED since, not because the status changed.**

---

### T-2026-11-05-01 — the unnamed AI-datacenter build tier ← IREN's $2.8B of multiyear AI-cloud contracts — REJECTED (rule (v) + part 2; §3 kills the headline leg independently; ONE drill query spent, source applied the kill)
**Company A / the news:** **IREN Limited (IREN)**, 2026-11-05, announced **$2.8 billion of new
multiyear AI-cloud-services contracts** and **raised its 2026 revenue target** for that business.
Shares rose **as much as 16%** on the day. ⚠ **THE ANNOUNCEMENT NAMES ITS COUNTERPARTIES, WHICH IS WHY
IT WAS WORTH A QUERY AT ALL:** Microsoft, Nvidia, Perplexity, Figure AI, Together AI, Fluidstack,
Fireworks AI, Fal AI and Hume AI, plus one unnamed AI developer.

**Why this looked like a §4 setup:** a dated disclosure, a hard dollar figure, named counterparties on
both sides, and a 16% move that says the market agrees something happened. **It is the best-formed
event the funnel has met in four sessions.**

**Door 1 — the named parties (the CUSTOMERS). DEAD, two ways at once.**
⚠ **THE SIGN IS WRONG: every named party is SPENDING, not earning.** This is rule (viii) in its
plainest form — money paid OUT by the buyable leg. ⚠ **AND PART 2 FAILS BY ORDERS OF MAGNITUDE EVEN IF
THE SIGN WERE RIGHT: $2.8B spread across TEN counterparties, over MULTIPLE years, against Microsoft's
and Nvidia's revenue, is a rounding error — nowhere near §4's 10%-of-revenue floor.** ⚠ **AAPL/MSFT/NVDA
are also priced-in on the day (see the mega-cap rally finding above).**

**Door 2 — the suppliers who must build the capacity. DEAD at rule (v): the source LEFT THE BLANK.**
One drill query asked explicitly whether the announcement or any accompanying filing names equipment
suppliers, GPU vendors, power providers, cooling or electrical contractors, or discloses a capex figure
attached to delivering these contracts, **and asked for the exact wording.** The answer: *"the available
results do not identify specific equipment suppliers … GPU vendors in the announcement or a filing …
power providers … cooling contractors … electrical contractors … or capital expenditure specifically
allocated to delivering the reported $2.8 billion contracts"*, and *"no primary announcement or filing
text is present … so an exact quotation about capacity construction and equipment cannot be responsibly
supplied."*
⚠⚠ **THE TWO NEAR-MISSES ARE INSTRUCTIVE AND BOTH FAIL: (a)** a **$363M equipment-financing facility**
described by a SECONDARY source as backed by *"fully paid, revenue-generating Nvidia GPU assets"* — **a
FINANCING facility secured on GPUs ALREADY BOUGHT AND PAID FOR, which is the opposite of a new order,
and it is a secondary description rather than filing text**; **(b)** a commentary reference to a
*"$3 billion capex bet"* that the source expressly **does not** tie to the $2.8B contracts.
⚠ **A FINANCING SECURED ON ASSETS ALREADY PURCHASED IS NOT A PURCHASE. New on this list, and it is a
close cousin of the JBL consignment entry: the dollar figure is real, named and allocated, and it
describes money that bought nothing new.**

**Part 1 attempt, written out so the "and also" is visible:** *"IREN's $2.8B of AI-cloud contracts
causes [supplier]'s revenue to rise because IREN must buy GPUs, power and cooling to serve them — **and
also** [supplier] is the one that gets the order, **and also** the order lands within two quarters."*
**Two "and also"s. REJECTED at part 1.**

**§3 kills the headline leg independently, and this is the cheapest kill available:** IREN's market cap
is reported at **$8.73B (Morningstar, 2026-11-03)**, with other sources on 11-03/11-04 at **$8.74B,
$8.91B, and ~$9.4–9.5B** — **ALL BELOW the $10B floor**, and the source warned the figures are
inconsistent and not live. ⚠ **A +16% day could carry it across the floor, and that is EXACTLY the
"but now there is a number / but it went up" pull the ELMT entry names. §3 does not weigh outcomes.**
**Priced-in, for the record:** `move --sessions 5` → **−24.7%**, `priced_in: true`, *"LATE"* — the
direction-blind defect, obeyed, and not what killed this.
- **verdict:** **REJECTED.** Part 1 needs two "and also"s; part 2 has no dollar path on either door;
  rule (v) blank left by the source; §3 floor on the headline leg.
- **cost:** one drill query. **The named-counterparty door needed none — the sign is readable off the
  announcement.**

---

### T-2026-11-05-02 — SMMT (Summit Therapeutics) ← AstraZeneca's completed $2.0B strategic equity investment — REJECTED (rule (viii), capital paid IN; ZERO queries spent, answer already written)
**The news:** Summit's 2026-11-04 Q3 report disclosed a **GAAP loss of $208.4M**, that **AstraZeneca
completed a $2.0 billion strategic equity investment in October**, and that shareholders approved
**doubling authorized shares to 2 billion**.
⚠⚠ **THIS IS THE STANDING RULE (viii) ENTRY ARRIVING AS A COMPLETED FACT RATHER THAN AN ANNOUNCEMENT —
AND THE ANSWER IS UNCHANGED.** The log already carries *"AstraZeneca's $2.0B convertible preferred,
which DILUTES rather than earns"*. **Capital paid IN is not segment revenue at any Company B**, and the
authorized-share doubling is **the dilution in writing.**
⚠ **COMPLETION IS NOT A NEW ECONOMIC EVENT. A transaction moving from announced to closed changes its
STATUS, not its SIGN** — and the §4 answer runs on the sign.
⚠ **Rule (iii) fails independently:** the investment was announced earlier and merely **re-reported** in
an own-results print. ⚠ **Part 3 fails independently too:** the ivonescimab **FDA action date is
2026-11-14 — a FUTURE date, not an approval**, and the source said so explicitly.
- **verdict:** **REJECTED.** Rule (viii) + rule (iii) + part 3, any one sufficient.
- **cost:** **zero queries.** ⚠ **This is the right outcome for a settled shape, and the entry exists
  only so the next seat recognises the COMPLETED-TRANSACTION costume without spending a query on it.**

---

### T-2026-11-05-03 — the mega-cap tech rally (MSFT · AMZN · AAPL) ← a divided-government election read — REJECTED (part 1, no Company A; a market is not a transaction; ZERO drill queries spent)
**The "news":** MSFT **+6.68%** to $555.80 · AMZN **+6.12%** to $266.03 · AAPL **+5.31%** to $349.51,
AAPL overtaking NVDA at a **$5.08T** market cap. **Sources attribute the session to a broad mega-cap
rally on a divided-government read of the 2026 midterms, and explicitly identify NO company-specific
disclosure for any of the three.**
⚠⚠ **SHARED CAUSE, NOT A MECHANISM — AND IN ITS CONVERGENT FORM, WHICH THE STANDING RULE NAMES AS THE
MORE DANGEROUS ONE: three of the five largest companies on earth moving ~6% TOGETHER on the same input
looks like corroboration and is the clearest possible statement that the input is a MARKET VARIABLE.**
⚠ **The political leg is the government-action object: ONE party, no named recipient, no transaction —
and the dollar index falling to monthly lows near 101.00 is a price, not an event.**
⚠ **There is no Company A here, so there is no Company B to look for. Part 1 cannot be written at all.**
**Priced-in independently:** all three moved >4% in a single session.
- **verdict:** **REJECTED** at part 1. ⚠ **Logged rather than skipped BECAUSE of its size: the
  temptation scales with the move, and "the biggest tape of the quarter produced no trade" is the line
  a future seat will need.**
- **cost:** **zero drill queries.**

---

### T-2026-11-05-04 — the macro complex (midterm result · ADP · ISM services · trade deficit · PCE nowcast · the October FOMC hold) — REJECTED (no Company A; rule (iii) on the FOMC leg; ZERO queries spent)
**Items, with figures, so the next seat need not re-fetch them:** **ADP** private payrolls **+86,000**
in October vs a **69,000–75,000** consensus, with September **revised DOWN to 86,000 from 90,000** ·
**ISM services PMI 54.5**, down from **54.9**, vs **54.8** consensus · **September trade deficit $105B**,
**−0.7%** from August · **Cleveland Fed PCE nowcast** headline **3.77%** (Oct) / **4.03%** (Nov) vs
**3.6%** September, core **3.2%** / **3.31%** vs **3.1%** · **FOMC held at 3.75–4.00% on a 10–2 vote**,
Cook and Hammack dissenting **for a quarter-point INCREASE**.
⚠ **EVERY ITEM IS THE STANDING GOVERNMENT/MACRO OBJECT: sector-agnostic, carries a number, moves the
tape, ONE party, no named recipient.** A long-only book cannot trade an aggregate.
⚠⚠ **THE FOMC LEG FAILS RULE (iii) ON TOP AND IT IS THE SAME TRAP AS 10-02: the hold was decided on
2026-10-28 and is merely RE-REPORTED in this window. An eight-day-old decision re-covered inside a
24-hour recency filter reads as fresh news to the filter and is not new to the issuer.**
⚠ **The dissents are the most interesting detail and change nothing: a 10–2 vote with two dissents FOR
A HIKE is a fact about the committee, not about any company's revenue line.**
- **verdict:** **REJECTED.** No Company A exists.
- **cost:** **zero queries.** ⚠ **Fifth consecutive session logging a macro complex in exactly this
  shape. THE FINDING IS THE PATTERN, NOT THE INSTANCE — and the pattern is that an election week
  produces the largest, most quotable, least actionable tape of the year.**

---

### T-2026-11-05-05 — sweep: own-results prints, §3-dead counterparties, a merger, a share sale, a commissioning milestone — REJECTED (eighteen items, ZERO queries spent beyond the broad sweeps)
Disposed as a block. **Each line names the rung it dies on, so none of these needs re-screening.**

**Own-results prints — FIRST-ORDER, the candidate IS Company A, part 1 cannot be written (and most are
§3-dead on cap):** **L.B. Foster (FSTR)** Q3 EPS $0.64 vs $0.60, revenue $168.0M vs $152.2M, FY sales
guide RAISED from its OWN **~$540–580M to $570–590M** (a clean rule (iii) PASS — ⚠ **and a rule (iii)
pass is NOT progress toward a trade, the standing Antofagasta/ELMT lesson, arriving again**), capex
guide LOWERED from ~2.7% to ~2.0–2.2% of sales, plus a **$52.2M** acquisition of a residential
wastewater precast business and the Aeris platform (~$18M annual revenue, $6.5–7.5M EBITDA after
synergies) ⚠ **whose seller the source could not even spell consistently — "Dulworth" in one place,
"Dalworth" in another — so the counterparty is not reliably identifiable** · **Maravai (MRVI)** revenue
guide raised from its OWN **$205–215M to $212–216M**, adj EBITDA **$33–35M → $40–42M** · **Paycom
(PAYC)** revenue **$2.213–2.218B** · **TaskUs (TASK)** **$1.249–1.251B** · **Vertex Inc (VERX)**
**$828.9–830.9M** and a ~30% 2027 adj EBITDA margin against a prior *"high 20s"* ⚠ **a QUALITATIVE
prior, so rule (iii) is not establishable in either direction — the standing AAR shape** · **Sight
Sciences (SGHT)** $92–93M, ⚠ **against a START-OF-YEAR range, not the immediately previous one, which
the source flagged itself** · **Schrödinger (SDGR)** ACV $222–232M, drug-discovery revenue $75–85M on a
**named** Structure Therapeutics milestone ⚠ **NAMED COUNTERPARTY AND STILL DEAD: SDGR is §3-dead on
cap, GPCR is smaller, and a milestone payment is a one-off receipt, not a segment.**

**§3-dead on market cap, at any price and any level of disclosure:** FSTR · MRVI · VERX · TASK · SGHT ·
SDGR · **Emergent BioSolutions (EBS)** — ⚠ **EBS is the cleanest named-counterparty kill of the day:
a $22.3M option-period modification to supply BioThrax to the US Department of War, first delivery
~$7.4M, remainder in 2027. The counterparty is NAMED and GOVERNMENTAL, the figure is DISCLOSED — and
$22.3M at a sub-$1B issuer is both §3-dead and immaterial, with the 2027 remainder outside §4's two
quarters.** ⚠ **Also an OPTION-PERIOD MODIFICATION under an EXISTING contract — rule (iii)'s
undefinitized/amendment costume.**

**No dollar figure disclosed, or no named counterparty, or both — rule (v), all §3-dead microcaps:**
**Sidney Resources / Ocean Partners** (25,000-tonne offtake, **PREVIOUSLY ANNOUNCED** — rule (iii) —
and no value or term) · **Galantas Gold / Ocean Partners** (doré purchase agreement, 3-year initial
term, **priced by reference to metal content and market prices, so NO total value exists**) · **Boron
One** (buyer not identified, no value) · **Alchemy** (partner not identified, no value).

**Not US-listed — §3, no mechanism needed:** **Viridis / Solvay** · **ArcelorMittal** (and it
**MAINTAINED** 2026 capex at **$4.5–5.0B** — ⚠ **reaffirmation, rule (iii) costume #1**) · **Leonardo**
(2026 order guidance raised **€28.2B → ~€29.5B** — ⚠ **ORDERS are not revenue, capex or margin:
rule (viii) read broadly**) · **SOCAR / Comstock** definitive purchase and sale agreement ⚠ **the
PENDING-DEFINITIVE deal from the 11-03 sweep now SIGNED — and signing changes its STATUS, not its
shape: a state-owned counterparty, and §4 asks whose economics change.**

**Wrong shape, settled rules:** **ANI Pharmaceuticals / Egetis Therapeutics** offer — ⚠ **merger
arbitrage, NOT IN §4; the target's price is contractually pinned and the acquirer is first-order** ·
**CVR Energy** **$500M** share sale — ⚠ **capital paid IN, rule (viii)** · **Revolution Wind fully
commissioned, supplying Rhode Island and Connecticut** — ⚠ **a DELIVERY MILESTONE recycled as news,
the standing GM/Lockheed costume, and Ørsted is Danish-listed** · **HSBC** tender offer — non-US,
a financing action · **"AI wobbles continue"** — ⚠ **a MARKET CONDITION remarked upon, which the
standing rule names as the most respectable disguise a non-event can wear.**

- **verdict:** **ALL REJECTED.**
- **cost:** **zero queries beyond the broad sweeps.** ⚠ **Eighteen items and not one of them needed a
  drill query, because every one of them matches a shape already written down. THAT is what the
  standing-rules section is for, and this is the clearest return it has produced.**

---

### 2026-11-04 (07:02 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,441.37** at pre-flight).
`clock` at 07:02:42 reads `is_open: false`, `next_open` **2026-11-04T09:30:00-05:00**, `next_close`
**2026-11-04T16:00:00-05:00** — both carry today's date: the pre-market full-session signature.
**Not a holiday.** ⚠ **Fired ~58 min early against a nominal 08:00 ET, the THIRD EST session running.
RECORDED AS AN OBSERVATION, NOT DIAGNOSED** — `control.md` forbids diagnosing a schedule fault from a
run timestamp, routine 1's stored schedule was read on 11-02, and this adds nothing to a confirmed
finding. Harmless at this seat: no orders are placed here.

⚠⚠⚠ **FIRST THING, AND IT DISCHARGES THE CARRY-FORWARD ITEM: 2026-11-03's OFFICIAL CLOSE IS
BACKFILLED. VOO `c` **693.57** (`bars --days 4 --adjustment all`, `v` 34,539, `n` 1,628).** The close
seat fired at 15:16 ET, 44 min before the bell, and wrote nothing — correctly. **Close-basis 11-03:
equity $98,695.55 · day +$236.23 / +0.2399% on 11-02's official $98,459.32 · since inception
−1.3044%.** ⚠ **The intraday $98,641.08 / +0.1710% carried in the 11-03 journal and state is NOT
close-basis and must not be quoted as one.**

⚠⚠⚠ **AND THE BACKFILL PRODUCED A FINDING THAT REPLACES THE INHERITED ONE RATHER THAN SITTING BESIDE
IT — THE PARTIAL-BAR ERROR INVERTED SIGN BETWEEN TWO CONSECUTIVE SESSIONS, SO IT IS NOT A BIAS AND
CANNOT BE CORRECTED FOR.** 11-02: partial **693.91** vs true **691.185** = **+$2.725 / +0.3943%, too
HIGH.** 11-03: partial **692.93** vs true **693.57** = **−$0.64 / −0.0923%, too LOW.** ⚠⚠ **The 11-03
close seat recorded that the partial-bar VOLUME signature inverted across the same two sessions; the
ERROR ITSELF inverts too. Two inversions in the same pair of sessions, on the two different quantities
a seat might have used to rescue the stamp.** ⚠ **DO NOT CARRY "a partial bar reads high" — it is the
companion of the volume error and fails the same way. The magnitude is bounded by this sample at ~0.4%,
which is enough to displace a §5.4 trigger, and the SIGN is unknowable in advance.** ⚠⚠⚠ **THE ONLY
RELIABLE DETECTOR REMAINS THE CLOCK. The refusal is still NEVER TESTED — zero satellite positions means
Step 2 had no operand on both sessions, and two vacuous passes are not a track record.**
✅ **Broker-pair cross-check run: `lastday_price` 693.54 vs bar `c` 693.57 = $0.03 / 0.004%, the
tightest pair on record and normal venue noise. Neither stamped.**

**Window surveyed:** Tuesday 2026-11-03 after the close through this morning. The 11-02 lesson was
applied again — the window was opened to catch the previous evening's after-close prints, and it
recovered the day's genuine events (onsemi and Pinnacle West both reported after the 11-03 close).
⚠ **2026-11-03 was US MIDTERM ELECTION DAY. It produced a tape and no Company A; disposed in the sweep
at `T-2026-11-04-05`, zero queries spent — scale is not a substitute for a named counterparty.**

**Ledger reconciled, three sides, re-derived not inherited.** Alpaca `positions` = **one row, core VOO
only** (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, **unchanged since 2026-09-03 — only the
mark moving**; `current_price` **701.00** is a LIVE PRE-MARKET PRINT at **+1.0713% over the official
11-03 close**, stamped nowhere and quoted nowhere as a close) · `positions.md` satellite block count
**0** · `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **No discrepancy.**

**Every §6 gate open.** Breaker INACTIVE, `halt_triggered_at: none`; `new_positions_this_week` **0 of
3**; satellite **0.0%** deployed, **$30,000 idle**; `control.md` Notes empty; zero open alerts. 5% cap
**$4,971.57**. **Week anchor re-derived with `isocalendar`: 2026-11-04 is ISO 2026-W45, weekday 3,
Monday anchor 2026-11-02 — MATCHES `week_of`. No rollover; not rolled a second time.**

**Three queries, five theses, zero survivors.** ⚠ **TWO of the three broad queries returned the KILL
VOLUNTEERED BY THE SOURCE** — *"no US-listed company meeting both conditions"* on the named-counterparty
sweep, and *"no publicly documented peer has named onsemi or quantified incremental revenue"* on the one
drill query spent. **That is the cheapest possible form of rule (v), and asking for the named
counterparty and the dollar figure IN THE SAME STATEMENT is what produced it. Keep framing it that way.**

⚠⚠⚠ **THE DAY'S FINDING, AND IT IS A CLEAN SEPARATION THE LOG HAS NOT HAD BEFORE: A CANDIDATE PASSED
THE PRICED-IN FILTER AND DIED ANYWAY, WHILE THE ONE THAT FAILED THE FILTER WAS ALREADY DEAD FOR A
STRUCTURAL REASON.** **PNW passed** — `move` **+2.25%** over five sessions, `priced_in: false`,
*"passes the priced-in check"* — and then **died at part 3**, because a **25-year** contract **subject to
regulatory approval** serving **1.88 GW at full build-out** is ~40+ quarters against §4's two.
**ON failed** — `move` **−7.69%**, `priced_in: true`, *"LATE"* — and was **independently dead at rule
(v)** before the filter was ever run. ⚠⚠ **SO TODAY DEMONSTRATES BOTH HALVES OF THE SAME POINT IN ONE
RUN: a hard-filter PASS is not progress toward a trade (the ELMT/Antofagasta lesson), and a hard-filter
FAIL was not what disqualified the only candidate it touched.**

⚠⚠ **AND THE DIRECTION-BLIND `move` DEFECT FIRED AGAIN, THIRD CONSECUTIVE SESSION, SIXTH NAME: ON at
**−7.69%** returned `priced_in: true` / *"LATE — skip per strategy.md section 4"*.** The tally is now
**INTC −24.36% (11-02) · MU −7.77% · SNDK −14.40% · STX −7.87% · WDC −4.96% (11-03) · ON −7.69%
(11-04)** — **six "LATE" verdicts on six DECLINES across three sessions.** ⚠ **STATUS UNCHANGED, AND
IT WAS OBEYED ANYWAY: the filter fails safe, it over-blocks and can never wrongly PERMIT, so a seat
must not reason past a `priced_in: true` on the grounds that the move was negative.** ⚠ **The fix is a
signed threshold in `scripts/alpaca.py`, which is SCRIPT-LEVEL AND NOT A SEAT'S TO INSTALL. Reported to
the human 2026-11-03; NOT re-notified today, because the item's status has not changed.**

---

### T-2026-11-04-01 — the alternative automotive power/analog supplier tier ← onsemi diverting constrained capacity from automotive to AI — REJECTED (rule (v) + part 2; ONE drill query spent, source applied the kill)
**Company A / the news:** **onsemi (ON)** Q3 2026 print, after the 2026-11-03 close: revenue
**$1.722B** (+11% y/y), adj EPS **$0.90** vs **$0.63**; AI data-center revenue **$180M**, **+39%
sequentially / +175% y/y**, with management guiding **~$620M for 2026** and projecting that figure to
**double in 2027**. ⚠ **The operative disclosure is an ALLOCATION decision, not a number:** onsemi said
it was **supporting automotive end-demand shipments but NOT automotive inventory-replenishment
backlog**, directing constrained capacity to **AI data-center and industrial** customers, with
additional capacity expected in **Q1 2027**.
**Company B / the candidate:** the US-listed suppliers of the same automotive power/analog content that
an automaker deprived of onsemi parts would have to buy from instead — **TXN**, **ADI**, **MCHP**,
**NXPI**.

**1. Mechanism (one sentence):** ❌ **CANNOT BE WRITTEN IN ONE CLAUSE.** The honest version is
*"onsemi withholding automotive replenishment parts causes TXN's automotive analog revenue to improve
because deprived automakers reroute those orders — **and also** the automakers choose to reroute rather
than wait one quarter for onsemi's Q1 2027 capacity, **and also** the rerouted volume lands at a
US-listed supplier rather than at Infineon or STMicro."* ⚠ **Two "and also"s. §4 says one clause or
reject, and this is the shape the strategy file names explicitly.**
**2. Dollar path:** ❌ **DOES NOT EXIST.** The drill query asked for the segment, the segment revenue
and the share of total revenue at each candidate, and returned a table whose every cell reads *"Not
available"* / *"None reported"*. ⚠⚠ **onsemi NEVER QUANTIFIED THE DEFERRED AUTOMOTIVE REVENUE** — its
automotive line was **$777M, DOWN 1% sequentially and DOWN 1% y/y**, which management attributed to the
reallocation. **A 1% decline is the entire measured size of the hole, on a $777M line, split across an
unnamed number of automakers and an unnamed number of alternative suppliers. There is no figure to
allocate and therefore no segment share to compute.**
**3. Timing window:** n/a — not reached.
**4. Invalidation:** n/a — not reached.

**Hard filters:**
- Priced-in (§4): **ON −7.69%** over 5 sessions → `priced_in: true`, *"LATE"*. ⚠ **A SIXTH direction-blind
  reading, and it is NOT what disqualifies this thesis — the candidates are TXN/ADI/MCHP/NXPI, not ON.**
- Correlation (§4): **no open satellite positions, so no driver to collide with.** Vacuous pass, 54th.
- Universe (§3): not reached — no candidate survived to be screened.

**Outcome:** **REJECTED at rule (v), before part 1 could be written.** ⚠⚠⚠ **THE SOURCE APPLIED THE KILL
ITSELF AND IT IS WORTH QUOTING, BECAUSE IT ALSO NAMES THE TEMPTATION:** *"The available evidence does
**not** identify any other US-listed company that has, in its own filing or release, named onsemi's
capacity constraints as a source of incremental revenue or share gains… The absence of such disclosure
is not evidence that no competitor benefited; it means only that no such benefit is reported in the
available evidence."* ⚠⚠ **THAT SECOND SENTENCE IS THE TRAP, STATED PLAINLY BY THE SOURCE: "somebody
must be getting those orders" is TRUE and UNACTIONABLE. §4 needs a NAMED recipient with a DISCLOSED
figure, and a reallocation of capacity names neither — it names only the party GIVING UP the revenue.**
⚠ **THIS IS A NEW AND SHARPER FACE OF RULE (v), LOGGED AS SUCH: a DIVERSION has a certain beneficiary
and no nameable one. It is strictly worse than the "unnamed supply base" costume, because there the
blank at least had a dollar figure beside it; here the beneficiary set is not even enumerable — it
includes foreign-listed suppliers (§3-dead) and inventory the automakers already hold.** ⚠ **ASK WHO
IS NAMED AS RECEIVING, NOT WHO MUST ARITHMETICALLY BE RECEIVING.**

---

### T-2026-11-04-02 — PNW (Pinnacle West Capital) ← TSMC's first direct-pricing power contract for the Arizona campus — REJECTED (part 3 / rule (vi); part 2 independently; ZERO drill queries spent)
**Company A / the news:** **TSMC**'s Arizona campus expansion. **Pinnacle West (PNW)**, reporting
2026-11-04, disclosed it had **executed its first direct pricing contract with TSMC in October** — a
**25-year agreement**, **subject to regulatory approval**, serving approximately **1.88 GW** of demand
**at full build-out** across the Arizona campus. Its **committed-demand forecast rose to 5.8 GW, about
1.3 GW above its prior level.** Alongside: 2026 EPS guidance **$5.05–$5.25**, full-year retail-sales
growth outlook **8–10%**, Q3 EPS **$3.49**.
**Company B / the candidate:** **PNW itself** — the regulated utility whose load grows because a
semiconductor fab complex expands.

⚠⚠ **THIS IS THE BEST-SHAPED CANDIDATE THE FUNNEL HAS MET IN SEVERAL SESSIONS AND IT IS WORTH SAYING SO
BEFORE THE KILL: Company A is NAMED (TSMC), Company B is NAMED AND BUYABLE (PNW), the commitment is
QUANTIFIED (1.88 GW; +1.3 GW to the committed-demand forecast), the counterparty appears IN THE SAME
SENTENCE AS THE FIGURE — which is exactly the test `T-2026-11-03-02` was minted to impose — and the
mechanism needs no "and also."** ⚠ **It fails on timing alone, and that is the honest reason.**

**1. Mechanism (one sentence):** ✅ *"TSMC's Arizona campus expansion causes Pinnacle West's regulated
retail electricity revenue to improve because TSMC has contracted directly for ~1.88 GW of load on
PNW's system."* **One clause, no "and also." PART 1 PASSES — the first clean part-1 pass since 10-30.**
**2. Dollar path:** ❌ **FAILS — NO DOLLAR FIGURE EXISTS.** The commitment is denominated in
**GIGAWATTS, not dollars**, and no contract value was disclosed by either party. ⚠ **The segment is
trivially material — regulated electric is substantially all of PNW's revenue, so the §4 10% test would
pass if there were a number — but "the segment is big enough" is not a dollar path. Converting 1.88 GW
to revenue would require inventing a tariff rate, a load factor and a ramp schedule; that is three
assumptions, not an estimate.** ⚠ **AND THE 1.3 GW INCREMENT IS A *FORECAST OF COMMITTED DEMAND*, NOT
BOOKED REVENUE — a figure about what PNW expects to be asked to serve.**
**3. Timing window:** ❌ **FAILS, AND THIS IS THE DECISIVE KILL. ~40+ QUARTERS AGAINST §4'S TWO.** The
1.88 GW is **"at full build-out"** of a campus whose construction runs into the 2030s; the contract term
is **25 years**; and it is **"subject to regulatory approval"** that has not been granted. ⚠⚠ **RULE
(vi) IN ITS TEXTBOOK FORM — long-dated infrastructure offtake PLUS a pending regulatory gate, the two
shapes the rule was written for, stacked. Part 3 kills it in ONE step and NO drill query was spent.**
**4. Invalidation:** n/a — not reached.

**Hard filters:**
- Priced-in (§4): **PNW +2.25%** over 5 sessions → `priced_in: false`, *"passes the priced-in check"*.
  ⚠⚠ **A CLEAN PASS, AND IT BOUGHT NOTHING. Recorded deliberately: this is the ELMT/Antofagasta lesson
  arriving on a GOOD candidate rather than an ineligible one, which makes it the stronger instance.**
- Correlation (§4): no open satellite positions → vacuous pass.
- Universe (§3): **not reached, and deliberately not researched.** Part 3 is decisive, and §4 says filters
  come before the thesis precisely so that no effort goes into a story a single test was always going to
  end. ⚠ **PNW's market cap was NOT pulled — recording that, because the §3-first discipline would have
  had it pulled first, and the honest reason it was not is that rule (vi) got there in one step.**

**Outcome:** **REJECTED on part 3 (rule (vi)), with part 2 failing independently for want of any dollar
figure.** ⚠⚠⚠ **AND A SEPARATE LEG DISPOSED IN THE SAME ENTRY, BECAUSE IT IS THE ONE A READER WOULD
REACH FOR NEXT: THE EPS GUIDANCE RAISE IS NOT A SECOND-ORDER CATALYST AND FAILS RULE (iii) AS WELL.**
The **$5.05–$5.25** range is PNW's **own first-order disclosure about its own current year**, and
⚠ **THE SOURCE DOES NOT CARRY PNW'S OWN PRIOR RANGE** — *"the prior range was not provided."* **That is
the AAR shape from 09-29 exactly: not establishable in either direction, so the rule (iii) test cannot
be passed OR failed, which means it has not been passed.** ⚠ **A third leg — PNW needing +1.3 GW of
committed capacity implies turbine/grid-equipment orders — dies at rule (v) (no vendor named, no figure)
and at rule (vi) (generation build is multi-year), and GEV is at THREE prior appearances dead on part 2
or 3 each time. NO QUERY SPENT ON IT.**

---

### T-2026-11-04-03 — ON (onsemi) / Ferric — $600M cash + up to $175M contingent — REJECTED (rule (viii), ZERO queries spent)
**Company A / the news:** onsemi agreed on **2026-11-02** to acquire **Ferric** for **$600M in cash**
plus up to **$175M** in contingent payments tied to future revenue milestones.
**Company B / the candidate:** none reached.

**1. Mechanism:** ❌ not written. **2–4:** not reached.

**Outcome:** **REJECTED at rule (viii) on sight.** ⚠ **ACQUISITION CONSIDERATION PAID OUT BY THE BUYABLE
LEG TO A PRIVATE SELLER — the money leaves the only listed party, and the receiving leg cannot be bought
at any price. This is the GEHC/Sofie ($945M, 10-06) shape arriving unchanged.** ⚠ **The contingent
$175M is a liability on onsemi's future, not revenue at any Company B.** **Also merger-shaped, and
merger arbitrage is not in §4. Disposed in one line because the answer is already written.**

---

### T-2026-11-04-04 — the own-prior-figure sweep (Spartan Delta · SM Energy · Mowi · Ferroglobe) — REJECTED (§3 + rule (iii) + rule (v); ZERO drill queries)
**The query:** which US-listed companies changed a **previously-issued figure of their own** — capex,
unit volume, production target, capacity plan, explicitly **not** EPS/revenue vs consensus — in the
window, and did any name a US-listed supplier, vendor or customer affected? ⚠ **Framed this way to
attack rule (iii) at its source rather than testing it after the fact. It worked: three qualifying
changes came back WITH both figures, and the question of a named counterparty was answered in the same
table.**

| Item | Own prior → new | Kill |
|---|---|---|
| **Spartan Delta (SDE)** 2026 capital program | **$525–575M → $575–625M** (11-03) | ⚠ **A CLEAN RULE (iii) PASS — own prior figure present, raised, dated.** Dies at **rule (v)**: *"no specific affected counterparty reported."* Dies again at **§3** — TSX-listed, ~C$0.7B, far under the $10B floor; **and the company said the higher capex would NOT change 2026 production guidance (54,000 BOE/d midpoint), so even the first-order economics are unchanged.** |
| **Spartan Delta (SDE)** Duvernay plateau | **50,000 → 75,000 BOE/d by 2030** (11-03) | **Rule (vi)** — *by 2030*, ~16+ quarters. **§3** independently. |
| **SM Energy (SM)** 2026 oil production | prior **not identifiable** → **220–222 kb/d**, ~1% LOWER | **Rule (iii) fails in the AAR shape** — not establishable in either direction. ⚠ **And the sign is wrong for a long: production guidance CUT.** No counterparty named. |
| **Mowi ASA** 2026 harvest volume | **600,000 → 620,000 GWT** | **§3** — not US-listed. Another clean rule (iii) pass on an ineligible issuer. |
| **Ferroglobe (GSM)** five plant closures, ~80% utilisation target | **no prior company figure** | **Rule (iii)** — no prior number to compare. ⚠ **Capacity being CLOSED is the wrong sign; also ~$0.6B cap, §3.** |

**Outcome:** **REJECTED, five items, zero survivors, zero drill queries spent.** ⚠⚠⚠ **THE FINDING IS
THE DISTRIBUTION, NOT ANY ITEM: THIS QUERY PRODUCED THREE CLEAN RULE (iii) PASSES IN ONE CALL — more
than the last four sessions combined — AND EVERY ONE OF THEM DIED SOMEWHERE ELSE.** Two on **§3**
(TSX, Oslo), one on **rule (v)** (no counterparty), one on **rule (vi)** (2030). ⚠⚠ **Rule (iii) is
recorded in this log as "the most prolific rule," and that is still true of what it KILLS — but it is
now measured that passing it predicts nothing, because the binding constraints are §3 ELIGIBILITY and
rule (v) NAMING. Asking the rule (iii) question FIRST finds eligible-looking news; it does not find
trades.** ⚠ **Companion to the 10-30 ASE finding (*"a capex raise is a NECESSARY condition that was
never close to sufficient"*) — three more instances, from a query designed to hunt for them.**

---

### T-2026-11-04-05 — sweep: own-results prints, one acquisition, unnamed counterparties, and the macro/political complex — REJECTED (eleven items, disposed as one, ZERO drill queries spent)

| Item | Shape | Kill |
|---|---|---|
| **Talen Energy (TLN)** Q3 adj FCF **$433M** vs **$216M** y/y, EBITDA $669M | own-results print; drivers given as *"higher power prices"* | **Part 1** — own print, first-order; **and higher power prices is the SHARED-CAUSE object**, a market variable, not a transaction. |
| **Metallus (MTUS)** adj EPS $0.35 vs $0.30 cons; revenue **$337.2M vs $345.25M cons**, Q4 profitability to decline | own-results print, **revenue MISS** | **Rule (iv)** — MTUS was disposed at `T-2026-10-01-05`; **second appearance.** ⚠ **And an earnings MISS is not a second-order catalyst (the 10-02 Nike sub-shape) — a company's disappointment improves nobody's economics in any dateable way, and the sign is wrong for a long.** Consensus comparison, not its own prior figure → **rule (iii)** too. |
| **Atlas Energy Solutions (AESI)** revenue **$267.8M** vs $265.3M cons, weaker EBITDA | own-results print vs consensus | **Rule (iii)** + part 1. §3 fails independently (~$2B). |
| **Cabot (CBT)** **$125M** battery-materials capacity plan + **$50M DOE grant** + a multiyear supply agreement | capacity plan with an **unnamed** agreement counterparty | **Rule (v)** — the supply-agreement counterparty is not named and the equipment tier is unnamed. ⚠ **The $50M DOE grant is a GOVERNMENT ACTION: one party, no named recipient of the second-order money.** **Rule (iii)** — source could not establish whether either figure was previously disclosed. §3 fails (~$4–5B). |
| **CVR Energy (CVI) / Marathon Petroleum (MPC)** — **$4.2B** for two refineries | **acquisition** | **Not in §4.** ⚠ **Both legs dead on rule (viii) in opposite directions: capital paid OUT by CVI, capital paid IN to MPC.** CVI ~$2.5B, §3. |
| **Energy Transfer (ET)** **$1.6B** South Mississippi Pipeline, *"supported by long-term transportation agreements"* | big figure, **unnamed** shippers | **Rule (v)** — *"did not name a specific counterparty."* ⚠ **Rule (vi)** — a sanctioned pipeline is multi-year construction. ET is the SPENDER: first-order, and the figure is capex paid out. |
| **Solvay** long-term rare-earth feedstock supply agreement with **Viridis**, from **2028** | named counterparty, **no figure** | **Part 2** — no dollar value. **§3** — Euronext-listed; Viridis not US-listed. **Rule (vi)** — *begins 2028*. |
| **ASTA Energy Solutions AG** / **Virginia Transformer Corporation** long-term agreement | named counterparty, **no figure** | **§3** — German-listed; VTC is private. **Part 2** — no figure. |
| **JOLTS, September:** openings **7.52M** from **7.19M**, ~370k above expectations; quits 3.36M; layoffs 1.64M; payrolls **+29k** | macro data | **No Company A.** The standing macro object — ⚠ **and a sizeable surprise, which per the standing rule makes it MORE convincing, not more real.** |
| **Fed held 3.75–4.00% (reported 10–2)**; Q3 GDP **3.4%** vs 3.1%; core PCE **3.1%** | macro | **No Company A.** ⚠ **AND THE SOURCE FLAGGED ITS OWN EVIDENCE AS INTERNALLY INCONSISTENT** on the meeting date and warned the material should not be treated as verified. **Recorded as unverified and NOT used.** |
| **US midterm elections, 2026-11-03** | political event | **No Company A, no named counterparty, no figure.** ⚠ **The largest-tape item in the window and the emptiest: it is the government-action object with no recipient at all. Zero queries spent.** |

**Outcome:** **REJECTED, eleven items, zero survivors, zero drill queries spent.** ⚠ **Six of the eleven
are own-results prints or consensus comparisons — the ordinary earnings-season background the log says to
expect and kill on part 1 each time. The sweep exists so they cost one table row each instead of a query.**

---

### 2026-11-03 (07:02 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$98,318.99** at pre-flight).
`clock` at 07:02:16 reads `is_open: false`, `next_open` **2026-11-03T09:30:00-05:00**, `next_close`
**2026-11-03T16:00:00-05:00** — both carry today's date, the pre-market full-session signature.
**Not a holiday.** ⚠ **Fired ~58 min early against a nominal 08:00 ET, the second EST session running.
RECORDED AS AN OBSERVATION, NOT DIAGNOSED** — `control.md` forbids diagnosing a schedule fault from a
run timestamp, and routine 1's stored schedule was already read on 11-02, so this adds nothing to a
confirmed finding. Harmless at this seat either way: no orders are placed here.

**Window surveyed:** Monday 2026-11-02 after the close through this morning. ⚠ **The 11-02 seat's
lesson was applied: the window was opened deliberately to catch the PREVIOUS EVENING's after-close
print, and it recovered the day's only real event (Apple, reported after the 11-02 close).**

**Ledger reconciled, three sides, re-derived not inherited.** Alpaca `positions` = **one row, core VOO
only** (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, **unchanged since 2026-09-03 — only the
mark moving**; `current_price` 689.76 is a LIVE PRE-MARKET MIDPOINT, stamped nowhere) · `positions.md`
satellite block count **0** · `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **No discrepancy.**

**Every §6 gate open.** Breaker INACTIVE, `halt_triggered_at: none`; `new_positions_this_week` **0 of
3**; satellite **0.0%** deployed, **$30,000 idle**; `control.md` Notes empty; zero open alerts. 5% cap
**$4,915.91**. **Week anchor re-derived with `isocalendar`: 2026-11-03 is ISO 2026-W45, weekday 2,
Monday anchor 2026-11-02 — MATCHES `week_of`. No rollover; not rolled a second time.**

**Three queries, five candidates, zero survivors.**

⚠⚠⚠ **THE DAY'S FINDING — THE SAME NON-EVENT ARRIVED FROM A SECOND REPORTER ON CONSECUTIVE SESSIONS,
AND THE ANSWER WAS ALREADY WRITTEN VERBATIM.** On 10-29 **Intel** remarked that memory shortages were
raising PC prices; `T-2026-11-02-03` killed it with *"a third party REMARKING on a condition is not an
event — it is a reading of the tape with a filing date attached."* On 11-02 **Apple** called memory
pricing **"unprecedented"** and guided gross margin down to **45–46%** from a reported **47.9%**.
⚠ **DIFFERENT COMPANY, DIFFERENT SECTOR, LARGER NAME, SAME OBJECT.** Nothing about any memory maker's
economics changed on 2026-11-02. ⚠⚠ **THIS IS RULE (iv) PROMOTED FROM THE TICKER TO THE *OBJECT*: a
recurring NON-EVENT wearing a new reporter's name. The warning the log has been writing about tickers
applies to shapes, and a bigger, more credible reporter is NOT fresh evidence when the kill is
structural.**

⚠⚠ **AND A NEW COSTUME, LOGGED AT `T-2026-11-03-02`, WHICH IS THE MOST FILLABLE-LOOKING BLANK THIS
FUNNEL HAS PRODUCED: TWO TRUE STATEMENTS IN ONE DISCLOSURE THAT THE READER JOINS INTO A THIRD THAT
NEITHER MAKES.** Apple disclosed (a) manufacturing purchase obligations **+$33B** June→September, *"as
we work to improve supply"*, and (b) separately, that memory costs are rising. **Neither statement
mentions the other.** ⚠ **Rule (v)'s worst prior shape was a precise figure plus a named component
category in ONE sentence; this is a precise figure in one paragraph and the component category in
ANOTHER, which reads as better-sourced because the reader supplies only the JOIN.** ⚠ **The source
volunteered the refusal: *"attributing the $33 billion — or any portion of it — to memory or to a
particular supplier would go beyond what Apple stated."***

⚠⚠ **AND A DEFECT IN THE §4 PRICED-IN FILTER ITSELF, SECOND CONSECUTIVE SESSION: `alpaca.py move` IS
DIRECTION-BLIND.** It thresholds **absolute** 5-session magnitude, so it returned `priced_in: true`,
*"LATE — skip"* on **MU −7.77%**, **SNDK −14.40%**, **STX −7.87%**, **WDC −4.96%** — four names that
**FELL**. §4's words are *"already moved more than 4% **on this news**, you are late"*; a 14% DECLINE
is the opposite of late for a long, and none of these moves is attributable to last night's news.
⚠ **Yesterday's INTC −24.36% was the same reading and that seat said so (*"the filter is not what
disqualifies it"*); today it fired four more times in one call, so this is a PROPERTY OF THE SCRIPT,
not an instance.** ⚠⚠ **IT FAILS SAFE — it over-blocks and can never wrongly PERMIT — but a
`priced_in: true` reading MUST NOT be quoted as "the market has already captured this upside," and on
a book that has made exactly ONE trade in ~44 sessions an over-blocking hard filter is a plausible
contributor worth the human's attention.** **Prompt/script-level; not a seat's to change.**

---

### T-2026-11-03-01 — the memory-cost tier (MU · SNDK · STX · WDC) ← Apple's "unprecedented" memory pricing — REJECTED (part 1, zero drill queries spent)
**Company A / the news:** Apple's FQ4 2026 print (after the 2026-11-02 close) guided FQ1 gross margin
to **45–46%** vs **47.9%** reported, said **memory costs were higher** than the June quarter and
expected to **keep rising**, and called memory pricing **"unprecedented."**
**Company B / the candidate:** the US-listed memory tier — **Micron (MU)**, **SanDisk (SNDK)**,
**Seagate (STX)**, **Western Digital (WDC)**.

**1. Mechanism (one sentence):**
> Apple's disclosure that memory pricing is unprecedented causes Micron's DRAM revenue line to rise
> because tight supply lifts ASPs — **and also** Micron captures that pricing rather than conceding it.

⚠ **THE "AND ALSO" IS BACK, IN THE SAME PLACE, ONE SESSION LATER. §4: reject it.**

**2–4.** Not reached.

**Hard filters:**
- Priced-in (§4): **MU −7.77%** · **SNDK −14.40%** · **STX −7.87%** · **WDC −4.96%** over 5 sessions —
  all four return `priced_in: true`. ⚠⚠ **NOT CLAIMED AS THE KILL AND NOT A CLEAN TEST: every move is
  NEGATIVE and the script is direction-blind (see the survey note). The mechanism was already dead.**
- Correlation (§4): no operand — zero open satellite positions.
- Universe (§3): all four US-listed, above the floor — **PASS, and irrelevant.** ⚠ **SK Hynix, Samsung
  and Kioxia are Korea- and Japan-listed: §3 kills the three largest actual beneficiaries outright.**
  ⚠ **Rule (ii) honoured: WDC post-spin is HDD; the NAND leg is SNDK. Both screened, both dead.**

**Outcome:** **REJECTED — part 1, the third-party-remarking non-event.** ⚠⚠ **A DRAM up-cycle is a
MARKET VARIABLE. Apple is EVIDENCE OF it, not a CAUSE of it — the identical disposition
`T-2026-11-02-03` gave Intel, and the identical disposition `T-2026-10-29-04` gave SK Hynix.** ⚠ **MU
is now at FOUR appearances in five sessions (10-02 declined · 10-29 SK Hynix · 11-02 Intel · 11-03
Apple) and has died at part 1 every time it was screened. Rule (iv): expect it again, the answer is
written.** ⚠ **Rule (iii) fails independently: "unprecedented" carries no figure and no prior figure
from any memory maker.** **Zero drill queries spent.**

---

### T-2026-11-03-02 — the unnamed Apple supply base ← $33B increase in manufacturing purchase obligations — REJECTED (rule (v) + part 2)
**Company A / the news:** on the FQ4 call Apple said *"as we work to improve supply, our manufacturing
purchase obligations have increased by **$33 billion** from June to the September quarter."*
**Company B / the candidate:** **none reached** — the recipients are not named.

**1. Mechanism (one sentence):** not writable without naming a recipient Apple did not name.
**2. Dollar path:** **$33B exists and has the RIGHT SIGN** — money Apple has contractually committed
to pay suppliers, i.e. flowing TOWARD the buyable leg, which is the rarest property on rule (viii)'s
list. ⚠ **AND IT IS STILL UNUSABLE: NOT ALLOCATED to any supplier, NOT broken down by component, NOT
stated to concern memory at all.** A segment share of total revenue cannot be computed for a company
that has not been identified. **FAIL.**
**3. Timing window:** not reached. **4. Invalidation:** not reached.

**Hard filters:** not reached — no candidate exists to filter. ⚠ **§3 would kill the largest probable
recipients anyway: Hon Hai/Foxconn and Pegatron are Taiwan-listed, Samsung and SK Hynix Korea-listed,
Kioxia Japan-listed.**

**Outcome:** **REJECTED — rule (v), the unnamed supply base, in its most persuasive costume yet.**
⚠⚠ **THE NEW COSTUME IS THE JOIN: a precise, dated, purposive figure in one paragraph and a named
component category ("memory") in ANOTHER paragraph of the SAME call. The reader supplies only the
connection between two true statements, which feels like sourcing rather than invention.** ⚠ **The
source refused the join explicitly, unprompted — quoted in the survey note above.** ⚠ **A PURCHASE
OBLIGATION IS NOT A NAMED ORDER: "to improve supply" is a purpose, not a counterparty.**

---

### T-2026-11-03-03 — the optical-component tier (COHR · FN) ← Marvell / Lumentum ~$115B all-stock merger — REJECTED (merger arbitrage, not in §4; zero drill queries spent)
**Company A / the news:** Marvell (MRVL) announced an all-stock acquisition of Lumentum (LITE),
**4.5 MRVL shares per LITE share**, reported at ~**$115B**; MRVL fell **~12–13%** on the announcement.
**Company B / the candidate:** optical competitors — **Coherent (COHR)**, **Fabrinet (FN)**.

**1. Mechanism (one sentence):** requires *"and also the merger disrupts the combined entity's
customers enough to shift share"* — **a story the reader supplies.** **FAIL.**
**2–4.** Not reached.

**Hard filters:** not reached.

**Outcome:** **REJECTED on the standing rule, no query spent — MERGER ARBITRAGE IS NOT IN §4.** Both
legs are first-order. ⚠ **The all-stock structure means LITE is NOT price-pinned the way onsemi/
Synaptics and Schneider/PTC were, so the usual phrasing ("a target whose price is contractually
pinned has no economics left to change") does not apply as written — IT DIES ONE RUNG EARLIER INSTEAD:
§4 asks for a second-order party whose ECONOMICS change, and a change in who OWNS Lumentum changes
nobody's revenue or cost line.** ⚠ **The competitor read-across it invites is the shared-cause object.**
⚠ **The ~$115B figure is quoted from a market recap and looks implausible against Lumentum's standing
size; NOT relied on, because the disposition does not turn on the number.**

---

### T-2026-11-03-04 — refiners / airlines ← Brent −8.01% to ~$104.33 on US–Iran de-escalation — REJECTED (part 1, no Company A; zero drill queries spent)
**Company A / the news:** oil fell **~7–8%** (Brent ~**$104.33**, WTI ~**$96.25**) on expectations that
the US–Iran conflict might ease. **There is no Company A.**
**Company B / the candidate:** the usual fuel-cost beneficiaries. **Not elaborated.**

**1. Mechanism (one sentence):** a commodity price is a market variable; the sentence has no
transaction and no second party. **FAIL.**

**Outcome:** **REJECTED — the shared-cause / geopolitical object, recognise-on-sight.** ⚠ **An
8% one-day move in a benchmark commodity on a war headline is the FOMC object with a bigger number:
sector-wide, dated, moves the tape, and **one party — none of them a company.** ⚠ **SCALE MAKES IT
MORE CONVINCING, NOT LESS** — the fifth consecutive macro/geopolitical complex logged in this shape.

---

### T-2026-11-03-05 — sweep: a re-serve, two non-US parties, a government counterparty, three macro objects — REJECTED (seven items, disposed as one, ZERO drill queries spent)
Disposed without elaboration because each matches a written answer:

1. **Orion Group Holdings (ORN)** ~**$250M** October awards incl. a **$115M** concrete project —
   ⚠ **ALREADY DISPOSED at `T-2026-10-30-04` on §3 (microcap).** Rule (iv), second appearance in three
   sessions, **same kill**. Customer not a listed company either.
2. **Advanced Acoustic Concepts / US Navy** $53.9M, ceiling ~$196.2M — **§3** (parent Thales is
   Paris-listed) **+** government counterparty **+** rule (v)'s CEILING sub-shape. **Three kills.**
3. **Bavarian Nordic** four-year UKHSA vaccine supply — **§3** (Copenhagen-listed) and **no dollar
   value disclosed**.
4. **October ISM manufacturing PMI 55.5 from 54.5** (production 59.0, new orders 55.5) — macro, one
   party, no named recipient.
5. **US Treasury Q4 borrowing estimate cut $10B to $618B** — government action, not a Company A.
6. **US midterm elections** — ⚠ **an UNRESOLVED future event with no outcome and no enacted policy;
   not even a non-event yet.**
7. **Apple (AAPL) itself** — revenue **$114.5B** +12%, EPS **$2.10** vs **$1.99** consensus, iPhone
   +17%, Mac +24% — **first-order, the headline name §4 explicitly declines to chase.** ⚠ **Rule (iii)
   also fails on the beat: the comparison is to CONSENSUS, not to Apple's own prior figure.**

---

### 2026-11-02 (07:01 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,142.25** at pre-flight).
`clock` at 07:01:56 reads `is_open: false` with `next_open` **2026-11-02T09:30:00-05:00** and
`next_close` **2026-11-02T16:00:00-05:00** — both carry today's date, the pre-market full-session
signature. **Not a holiday.** ⚠ **NOTE THE `-05:00` OFFSET: DST ended Sunday 2026-11-01, so this is
the first EST seat of the season — and this run fired ~59 MINUTES EARLY against its nominal 08:00 ET
schedule, which is the signature of a UTC-anchored trigger that did not follow the fall-back. Logged
in `plan_today.md` as a conditional instruction to the open seat, NOT diagnosed as a confirmed fault
from a timestamp this file is warned not to diagnose from.**

**Window surveyed:** Friday 2026-10-30 after the close through this morning, **plus the Thursday
2026-10-29 after-close disclosures that drove Friday's session**. ⚠⚠ **THAT EXTENSION IS DELIBERATE
AND IT RECOVERED THE WEEK'S LARGEST EVENT: Intel printed Q3 after the close on 2026-10-29 and the
10-30 08:17 pre-market seat did not log it** — that seat's four scans returned a capex table, a
licence, two §3 kills and an RTX re-serve, and **the largest single-name disclosure of the week was
not among them.** It is minted here as `T-2026-11-02-01`, two sessions late. ⚠ **This is not an
indictment of that seat's queries; it is evidence that a 24-hour recency window on a pre-market seat
can miss an after-close print from the PREVIOUS evening, because the print is ~11 hours old at the
seat and ~35 hours old by the time its consequences are legible.**

**Ledger reconciled, three sides, agreeing, re-derived not inherited.** Alpaca `positions` = one row,
core VOO only (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, **unchanged since 2026-09-03 —
only the mark moving**) · `positions.md` satellite block count (`grep -cE '^### [A-Z]'`) **0** ·
`sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **No discrepancy.**

**Every §6 gate open.** Breaker INACTIVE, `halt_triggered_at: none`; `new_positions_this_week` **0 of
3**; satellite 0.0% deployed, **$30,000 idle**; `control.md` Notes empty; zero open alerts. 5% cap
**$4,957.11**. **Week anchor re-derived with `isocalendar`: 2026-11-02 is ISO 2026-W45, weekday 1,
Monday anchor 2026-11-02 — MATCHES `week_of`. ALREADY ROLLED by the 10-30 16:46 routine-5 seat; read
as already-rolled, NOT as a skipped step, and NOT rolled a second time.**

**Six queries, five candidates, zero survivors.** The shape of the morning is worth stating before
the entries, because it is not the shape the last two weeks produced.

⚠⚠⚠ **THE DAY'S FINDING: THIS MORNING PRODUCED THE BEST-SHAPED CANDIDATE THIS LOG HAS SEEN —
A NAMED TWO-PARTY CHAIN WITH THE BUYABLE LEG ON THE RECEIVING END — AND IT DIED ON PART 2 WITH
NOTHING TO MEASURE.** `T-2026-11-02-04`, Charles River / Ipsen. Nearly every prior entry in this log
fails at **rule (v)** (no Company B exists at all) or at **rule (viii)** (the dollar figure belongs to
the wrong party or moves the wrong way). **CRL fails at neither.** Ipsen is Company A, Charles River
is a **named external supplier** — not an inferred one, not a "supply base", not a redaction — and the
money flows **toward** the leg that can be bought. **§3 passes cleanly at $17.31B.** ⚠ **It dies
because the announcement discloses NO dollar value, NO term and NO revenue-commencement date.
Part 2 has nothing to be estimated FROM.** ⚠⚠ **THE LESSON IS THE MIRROR OF 10-30's: that seat found
a capex figure that moved the right way and no name to hang it on; this seat found the name and no
figure. The two failures are complementary halves of the SAME requirement, and the funnel has now
produced each half separately on consecutive sessions without once producing both together.**

⚠⚠ **AND THE PRICED-IN FILTER FIRED — TWICE — WHICH IS NEW, AND IT IS REPORTED WITH ITS CAVEAT
ATTACHED RATHER THAN AS A VINDICATION.** Open item 1 and the 10-30 weekly review record that the §4
priced-in filter **fired zero times last week** — *"not passed, never reached"*. This morning it was
reached by two live candidates and killed on both: **INTC −24.36%** and **CRL +4.18%** against a
**4.00%** threshold. ⚠ **NEITHER IS A CLEAN TEST.** INTC is **first-order and the wrong sign** — a
−24% collapse is not a §4 second-order long, and the filter is not what disqualifies it. **CRL fails
part 2 independently.** ⚠⚠ **AND ON CRL THIS SEAT MAY NOT CLAIM THE FILTER WAS THE BINDING KILL: the
§3/part-2 query and the `move` call were issued IN THE SAME TOOL CALL.** §4's ordering ("apply these
before writing the thesis") was satisfied **against the thesis** but **not between the two checks**,
so which fired first is not establishable from this run's own record. ⚠ **CRL at +4.18% is
nonetheless the first MARGINAL reading the filter has ever produced — 18bp over — where every prior
firing in this log's history has been far from the line.**

---

### T-2026-11-02-01 — the Intel Q4 guide-down and the Fab 28 shutdown → the unnamed advanced-packaging substrate tier — REJECTED
**Company A / the news:** **Intel (INTC)** printed Q3 2026 after the close on **2026-10-29**: revenue
**$16.51B** (+21% y/y), EPS **$0.52**, Q3 non-GAAP gross margin **44.1%**, ~200bp **above Intel's own
prior guidance** (a clean rule (iii) PASS on that figure). It then guided **Q4 revenue to $15.0–16.0B**
against consensus near **$17.1B**, with non-GAAP gross margin **38.0%** at the $15.5B midpoint — **−6.1pp
sequentially**. Three causes were given: weak client demand, **supply constraints in advanced organic
packaging substrates** (Intel said it is constrained on **both wafer and substrate** and must ramp
substrate capacity), and **an extended shutdown of Fab 28, Kiryat Gat, Israel** following an accident
that killed two workers, halting production ~two weeks and affecting **10nm server processor**
shipments. Management put the Fab 28 impact at **~$300M of Q4 revenue and ~200bp of gross margin**,
with a similar figure possible in Q1 2027. **INTC fell ~29% on Friday 2026-10-30, its steepest
one-day decline since 1974.**
**Company B / the candidate:** the **substrate and semiconductor-equipment tier** Intel must buy from
to relieve the constraint.

**1. Mechanism (one sentence):**
> Intel's disclosed substrate capacity constraint causes <substrate supplier>'s packaging-substrate
> revenue line to rise because Intel must place incremental orders to ramp that capacity.

⚠ **The sentence is well-formed. THERE IS NO COMPANY B TO PUT IN THE BLANK.**

**2. Dollar path:** **NOT WRITABLE.** Intel disclosed no substrate procurement figure. The only dollar
figures in the story are **Intel's own losses** — ~$300M of Q4 revenue and ~$1.1–2.1B of guidance
shortfall — which is **rule (viii)** in its plainest form: money moving the wrong way at the wrong
party.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **INTC −24.36% over 5 sessions (86.96 → 65.78) → FAIL, "LATE - skip"**. Applies to
  the headline name only; no Company B reached the filter.
- Correlation (§4): **zero open satellite positions, so the check has NO OPERAND — absent, not passing.**
- Universe (§3): the substrate tier that actually exists is **Ibiden and Shinko (Japan-listed), AT&S
  (Austria), Unimicron and Nan Ya PCB (Taiwan)** → **FAIL, none US-listed.**

**Outcome:** **REJECTED — rule (v), with §3 closing the back door and rule (viii) closing a third.**
⚠⚠ **The source applied the kill itself, twice and unprompted:** *"No equipment or materials vendor
was named in the available Intel-related results… Intel was placing purchase orders with equipment
vendors, but the available report does not identify those vendors by name"* and *"Assertions that
particular companies — such as semiconductor-equipment or substrate vendors — are exposed to Intel
would be INFERENCES, not direct disclosures."* ⚠ **A supply problem that is specific, dated,
quantified in its VICTIM's accounts and attributed to a named COMPONENT CATEGORY is rule (v)'s most
fillable-looking blank — the 10-05 "$1.7B of memory components" shape, scaled up. THE SOURCE LEFT THE
BLANK; FILLING IT IN IS NOT RESEARCH.**
⚠⚠ **AND THE SECOND DOOR WAS REFUSED EXPLICITLY, BECAUSE IT IS THE ONE THAT READS BEST:** Fab 28
halted **10nm server processor** output and Intel guided client shipments sharply lower, which invites
*"therefore AMD gains share"*. **That is the competitor's-earnings-print shared-cause object on the
recognise-on-sight list, in its purest form — a competitor's disappointment improves nobody's
economics in any disclosed, dateable way, and the share-shift story is supplied entirely by the
reader.** AMD passes the priced-in filter at **−2.25%**, which is exactly why the kill has to be
structural rather than numerical. **No ID was minted for AMD; it is disposed here.**
⚠ **Rule (iii) is a genuine PASS on the gross-margin figure (44.1% vs Intel's own prior guide) and a
FAIL on the revenue figure (quoted only against consensus ~$17.1B, never against Intel's own prior
range). THE 10-15 LESSON APPLIES: apply rule (iii) to the figure the mechanism runs on. The mechanism
here runs on neither — it runs on SUBSTRATE CAPACITY, for which no prior figure and no current figure
was disclosed at all.**

---

### T-2026-11-02-02 — SYM (Symbotic) / WMT (Walmart) ~$6B automation commitment → the unnamed automation component tier — REJECTED
**Company A / the news:** **Walmart and Symbotic** announced an **expanded Enterprise Master
Automation Agreement** on **2026-10-30** (8-K filed): an **initial Walmart commitment of ~$6B** over
several years covering **25 US regional distribution centres** plus global opportunities, a **$125M
Walmart-funded development programme for next-generation racking technology**, and a stated
**potential future backlog increase of up to $6.92B** against Symbotic's **~$22.5B total backlog at
2026-06-27**.
**Company B / the candidate:** the component tier beneath Symbotic — motors, drives, controls,
sensors, vision, steel racking.

**1. Mechanism (one sentence):**
> Walmart's $6B automation commitment causes <component supplier>'s industrial-automation revenue line
> to rise because Symbotic must buy that content to build 25 distribution-centre systems.

**2. Dollar path:** **NOT WRITABLE.** No component supplier is named anywhere, so there is no segment
to size and no denominator to divide by.
**3. Timing window:** **independently fatal.** The commitment runs *"over several years"* with **no
first-revenue date disclosed**; 25 DCs is a multi-year build. **Beyond §4's two-quarter ceiling.**
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **SYM −3.34%** (39.25 → 37.94) and **WMT +3.04%** (119.87 → 123.51) over 5 sessions
  — **both PASS.** ⚠ **Recorded because it is counter-intuitive and therefore worth having on the
  board: SYM is DOWN over the window in which it announced a $6B commitment, which is the
  AI-complex drawdown swamping the single-name news. A filter pass is not a signal.**
- Correlation (§4): **no operand.**
- Universe (§3): both US-listed and above the floor — **PASS**, and irrelevant.

**Outcome:** **REJECTED — part 1, with rule (v) and part 3 each independently fatal.** ⚠⚠ **THE
PRIMARY KILL IS STRUCTURAL AND IT IS THE ONE §4 EXISTS TO MAKE: BOTH NAMED PARTIES ARE FIRST-ORDER.**
Walmart is Company A paying the money out (**rule (viii)** — capital paid OUT by the buyable leg) and
**Symbotic is the headline name** — §4 opens by saying *"You are not chasing the headline name."*
Buying SYM here is buying the press release. ⚠ **The only genuinely second-order seat is the
component tier, and the source applied the kill itself:** *"the available results do not name a
specific US-listed supplier of motors, drives, controls, sensors, or steel racking… Any assertion
that a particular public company supplies Symbotic would be an inference or unsupported speculation."*
⚠ **Rule (iii) is a SPLIT and the split is instructive: the $6B and $6.92B figures are genuinely NEW
and genuinely Symbotic's own, but the RELATIONSHIP is an amendment — reporting states "the prior
agreements remain effective except where the new agreement modifies them". That is the Boeing/PAC-3
costume (a new dollar figure pricing an existing framework) in commercial dress. It is NOT the kill
here and is recorded so the costume list gains an instance rather than so the thesis gains a reason.**
⚠ **And a fourth door, closed before it opened: Symbotic's $22.5B backlog means a $6.92B increment is
~31% of backlog, a real number — but BACKLOG IS NOT SEGMENT REVENUE AT COMPANY B, and Company B does
not exist.**

---

### T-2026-11-02-03 — MU (Micron) ← Intel's memory-shortage demand commentary — REJECTED (part 1, zero drill queries spent)
**Company A / the news:** on the same 2026-10-29 call, Intel attributed part of the client weakness to
**memory shortages and higher system prices weighing on PC demand**, alongside an inventory correction
extending through at least Q1.
**Company B / the candidate:** **Micron (MU)**, the US-listed DRAM maker.

**1. Mechanism (one sentence):**
> Intel's disclosure that memory shortages are raising PC system prices causes Micron's DRAM revenue
> line to rise because tight supply lifts DRAM ASPs — **and also** Micron captures that pricing rather
> than conceding it to customers.

⚠ **THE SENTENCE NEEDS THE "AND ALSO" AND THAT IS THE ANSWER. §4: "If the sentence needs a second
clause to make sense, the link is too weak. Reject it."**

**2. Dollar path:** not reached.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **MU +0.82%** over 5 sessions (877.385 → 884.57) — **PASS.** ⚠ **Recorded because a
  clean pass on a name in the middle of a historic memory up-cycle is precisely the datapoint that
  makes a dead mechanism look alive. A FILTER PASS IS NOT A THESIS.**
- Correlation (§4): no operand.
- Universe (§3): US-listed, far above the floor — **PASS**, and irrelevant.

**Outcome:** **REJECTED — part 1, the shared-cause object.** ⚠⚠ **DRAM tightness is a MARKET
VARIABLE, not a TRANSACTION. Intel and Micron are both exposed to it with opposite signs, which is
exactly the DIVERGENCE face of the shared-cause shape on the recognise-on-sight list — and §4 asks
whose economics change BECAUSE OF the event.** ⚠⚠⚠ **THE DECISIVE POINT, AND IT IS THE ONE THIS LOG
HAS NOT WRITTEN DOWN BEFORE IN THIS FORM: INTEL'S DISCLOSURE IS *EVIDENCE OF* A PRE-EXISTING
CONDITION, NOT A *CAUSE* OF ANYTHING. Nothing about Micron's economics changed on 2026-10-29. A
third party REMARKING on a condition is not an event — it is a reading of the tape with a filing date
attached, which is the most respectable disguise a non-event can wear.** ⚠ **Rule (iii) fails on top:
"memory shortage" carries no figure, no prior figure and no date from Intel or from Micron.**
**Zero drill queries were spent — the mechanism sentence killed it at the first rung.**

---

### T-2026-11-02-04 — CRL (Charles River Laboratories) ← Ipsen Virtual Control Group expansion — REJECTED (part 2: no dollar value exists)
**Company A / the news:** **Ipsen** (Euronext Paris) agreed, announced **~2026-10-30**, to deploy
**Charles River's Virtual Control Group database across its toxicology studies** — reported as an
**expansion of existing Virtual Control Group use**.
**Company B / the candidate:** **Charles River Laboratories (NYSE: CRL)**, the **named** external
supplier and the US-listed leg.

**1. Mechanism (one sentence):**
> Ipsen's adoption of Virtual Control Group across its toxicology programme causes Charles River's
> Discovery and Safety Assessment (DSA) revenue line to rise because Ipsen contracts those studies to
> Charles River.

⚠ **THE SENTENCE STANDS WITHOUT AN "AND ALSO". That is rare in this log and it is the reason this
entry is written out in full rather than swept.**

**2. Dollar path:** ⚠⚠ **CANNOT BE WRITTEN. THIS IS THE KILL.** The announcement discloses **no
contract value, no term and no revenue-commencement date.** CRL's DSA segment is comfortably above
§4's 10%-of-revenue floor, so the *denominator* is fine — **there is no NUMERATOR.** ⚠ **Note what
this is NOT: it is not the rule (viii) failure of a figure belonging to the wrong party, and not the
rule (v) failure of a missing party. The party is named and the direction is right. THE NUMBER SIMPLY
DOES NOT EXIST, and §4 says an unmeasurable tailwind is not a tailwind.** ⚠ **Estimating it from
Ipsen's R&D budget and a guessed outsourcing share would be the exact move §4's honest-broker
paragraph forbids — constructing the magnitude the source declined to provide.**
**3. Timing window:** **NOT ESTABLISHABLE** — no revenue-commencement date is reported. A toxicology
database deployment plausibly recognises over years, which would fail §4's two-quarter ceiling, but
that is an inference and is **not** claimed as the kill.
**4. Invalidation:** would have been *"CRL's Q4 2026 or Q1 2027 filing shows DSA segment revenue flat
or declining sequentially"* — **well-formed, and never reached, because part 2 is unwritable.**

**Hard filters:**
- Priced-in (§4): **CRL +4.18% over 5 sessions (345.09 → 359.505) → FAIL, "LATE - skip"**, 18bp over
  the 4.00% threshold. ⚠⚠ **ORDERING DISCLOSED: this `move` call and the §3/part-2 query were issued
  in the SAME tool call. §4's "apply before writing the thesis" was satisfied, but which of the two
  checks fired first is NOT establishable from this run's record, so the filter is NOT claimed as the
  binding kill.**
- Correlation (§4): **no operand** — zero open positions.
- Universe (§3): US-listed common stock, **market cap $17.31B** → **PASS**.
  **market_cap_src: Yahoo Finance comparison page as of 2026-11-02, via Perplexity; corroborated at
  ~$17.15–17.16B by two further sources dated 2026-10-30/31. Recorded because §3's floor is only
  auditable if the provenance is written down.**

**Outcome:** **REJECTED — part 2, with the priced-in filter independently failing.** ⚠⚠⚠ **THIS IS
THE ENTRY THE WEEK SHOULD BE JUDGED ON. It cleared the rung that kills almost everything else —
a named, US-listed, above-floor Company B receiving money from a named Company A — and died for want
of a single number the counterparties chose not to publish.** ⚠ **It belongs beside `T-2026-10-09-01`
(GFS/TSMC) as a candidate that cleared every filter and died on the thesis parts, and it is the
cleaner of the two, because GFS died on a mechanism this one does not need.**

---

### T-2026-11-02-05 — sweep: unnamed-counterparty 8-Ks, non-US regulators, own-results prints, the forward calendar — REJECTED (nine items, disposed as one, ZERO drill queries spent)
Disposed in one entry because each fails at the first rung on evidence already in hand. Minting nine
IDs would inflate the thesis count without recording anything. **Each item names the rung.**

| # | Item | Rung |
|---|---|---|
| 1 | **Meta Platforms** 8-K, Item 1.01 "Entry into a Material Definitive Agreement", filed 2026-10-29 | **Rule (v), purest form.** The filing discloses **no counterparty, no financial terms and no description**. A blank with a filing date is still a blank — compare "Party A" (10-05). |
| 2 | **Chevron** 8-K, Item 2.02, 2026-10-30 | **First-order** — Item 2.02 IS "results of operations and financial condition", i.e. the company's own results. No second party exists in the filing type. |
| 3 | **Loews (L)** Q3: net income $306M / $1.50 vs $504M / $2.43; $67M buyback | **First-order own-results print**, and dated **2026-11-02**, outside the surveyed window. A buyback is capital paid OUT (**rule (viii)**). |
| 4 | **Broadcom (AVGO)** — South Korea Supreme Court decision, 2026-11-02 | **Not a US regulator**, and AVGO is the first-order party. No named supplier. |
| 5 | **Hashdex** 8-K, "Authorized Participant Agreement", 2026-10-30 | **§3 — crypto-tracking product. Ineligible at any price and any level of disclosure.** |
| 6 | **Precision Optics (POCI)** — lease, $13,316.33/mo | **§3 — microcap**, and a lease is a cost, not revenue. |
| 7 | **Gigabyte** — $526M GDR to fund AI-server supply chain | **§3 — Taiwan-listed.** |
| 8 | **MNI Chicago-area business activity slowed, released 2026-10-30** | **Macro object — one party, no transaction, and the result carried no index value.** |
| 9 | **The "$5 trillion AI wipeout" and a sell-side call for a further 9% S&P decline** | **A market move is not a Company A.** No named recipient, no transaction. ⚠ **SCALE MAKES IT MORE CONVINCING, NOT LESS.** |

⚠⚠ **AND THE TENTH ITEM, WHICH GETS NO ROW BECAUSE IT IS ALREADY DISPOSED: THE FORWARD CALENDAR, FOR
THE EIGHTH MONDAY PRE-MARKET SEAT.** The weekend window contains no trading, so the funnel filled the
space with the week ahead — **Apple and Palantir reporting TODAY 11-02, AMD Tuesday, Qualcomm / Arm /
Arista later, the October employment report 11-06, ISM manufacturing and services this week.** ⚠ **The
source named the exclusion itself again this morning** (*"These are forward calendar items and are
excluded"*), as it did on 10-12. **Already disposed at `T-2026-10-12-05` and `T-2026-10-13-08`. NOTE
THE DATES AND DO NOTHING.** ⚠ **The 10-12 lesson is holding without re-derivation and the expectation
written there — "expect this shape on EVERY Monday pre-market seat" — has now been met on every Monday
seat since.**

⚠ **STANDING DISPOSALS NOT RE-LITIGATED, AT ZERO QUERY COST: RTX (eight appearances), GNRC (42
consecutive refusals), Venture Global (three), GE Vernova (three).** None appeared this morning. ⚠
**GE Vernova's Q3 release DID surface in a citation list on the supply-agreement scan and was NOT
opened — it is an own-results print by a ticker already disposed three times, and the recognise-on-
sight list exists precisely so that costs nothing.**

---

### 2026-10-30 (08:17 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,299.73** at pre-flight).
`clock` at 08:17:22 reads `is_open: false` with `next_open` **2026-10-30T09:30:00-04:00** and
`next_close` **2026-10-30T16:00:00-04:00** — both carry today's date, the pre-market full-session
signature. Not a holiday. Window surveyed: Thursday 2026-10-29 after the close through this morning.

**Ledger reconciled, three sides, agreeing, re-derived not inherited.** Alpaca `positions` = one row,
core VOO only (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, unchanged since 2026-09-03) ·
`positions.md` satellite header count (`grep -cE '^### [A-Z]{1,5} '`) **0** · `sleeves`
`satellite.count: 0`, `value: 0`, `pct: 0.0`. **No discrepancy.** §7 limbo check: `orders --status all`
returns **exactly one order in the account's entire history** (`d177d8f0`, 2026-09-03, filled,
terminal, already in `trade_log.md`). **Nothing held is unverified and no order is in limbo.**

**Every §6 gate open.** Breaker INACTIVE, `halt_triggered_at: none`; `new_positions_this_week` **0 of
3** (week anchor re-derived with `isocalendar`: 2026-10-30 is ISO 2026-W44, weekday 5, Monday anchor
**2026-10-26**, matches `week_of`, **no rollover**); satellite 0.0% deployed, **$30,000 idle**;
`control.md` Notes empty; zero open alerts. 5% cap **$4,964.29**.

**Four broad scans, one drill, zero survivors.** Scan 1 (two named companies + a disclosed dollar
amount, M&A/earnings/macro excluded in the prompt, announcement date demanded in the prompt) returned
**zero qualifying items** with **five self-exclusions and reasons attached**. Scan 2 (who WON it and
what did the winner say it was worth to its OWN segment) returned **zero**, with four self-exclusions —
⚠ **and it re-served this log's own disposed 10-13 RTX award, the THIRD consecutive session the funnel
has done this, volunteering the kill in its own sentence.** Scan 4 (regulatory enable/block with a
named US-listed supplier) returned **zero**: *"No qualifying two-party action is identified."*

**Scan 3 is the one that mattered, and the answer inverts the last two sessions' emphasis.** The scan
asked the only question §4 cares about on an earnings-season tape driven by AI capital spending: **did
any overnight capex figure move UP against the company's OWN prior figure?** For two sessions the
answer has been *no, every one moved the wrong way*, recorded as though direction were the thing
standing between this log and a trade.

| Company | New capex figure | Its own prior figure | Direction |
|---|---|---|---|
| **ASE Technology** FY2026 | **~$11.5B** | **~$10.5B** (stated **2026-07-30**, itself a raise from ~$8.5B) | ⚠⚠ **RAISED +$1.0B — a clean rule (iii) PASS** |
| Amazon CY2026 | ~$220B | ~$220B | **reaffirmed** — rule (iii) costume #1 |
| ATI FY2026 | $280–300M | none in source | unestablishable |
| RPC FY2026 | $155–175M | none in source; deliveries **shifted 2026 → 2027** | down / deferred |
| Shell FY2026 | $23–25B | none in source | unestablishable |
| Sterling Infrastructure | not stated | ~$140M referenced | unestablishable |

⚠⚠⚠ **THE DAY'S FINDING: ASE PASSED RULE (iii) ON EXACTLY THE RIGHT FIGURE AND THE THESIS STILL DIED
ONE RUNG LATER, AT RULE (v).** The 10-15 lesson says to apply rule (iii) to *the figure the mechanism
runs on* rather than to the release — and capex is precisely the figure with a supplier chain hanging
off it. **ASE satisfied that test completely: the prior figure is present in the source, dated, and the
move is up by $1.0B.** Then the drill asked who supplies the equipment, and the answer was that **ASE
names no vendor** (it discloses only *"60% to LEAP and 40% to mainstream operations"*) and **no
US-listed supplier above $10B names ASE or quantifies ASE revenue in any filing.** The source applied
the kill itself: *"That would be an inference, not a reported customer relationship, and the available
evidence is insufficient to make that attribution."*
⚠ **SO THE INHERITED FRAMING WAS WRONG IN AN INSTRUCTIVE WAY. A capex raise was never the binding
constraint — it is a necessary condition that was never close to sufficient. The binding constraint is
NAMING, and it does not loosen when the number gets bigger or moves the right way.** ⚠ **Recorded as a
correction to this log's own emphasis, not as a new rule: it is rule (v) behaving exactly as written.
What is new is the demonstration that clearing rule (iii) buys nothing on its own.**

⚠ **ONE FUNNEL SELF-EXCLUSION WAS WRONG AND IS CORRECTED HERE — SECOND INSTANCE OF THE 10-13 BLOOM
LESSON.** Scan 1 excluded the GC Biopharma / Hanmi / BioMarin licence on the grounds that *"the two
Korean companies are not shown as U.S.-listed"* — true, and beside the point, because **BioMarin
(BMRN) is the US-listed leg.** It is logged as `T-2026-10-30-03` and disposed on its own merits.
**A self-exclusion is a HINT, NOT A RULING.**

---

### T-2026-10-30-01 — ASX (ASE Technology Holding) FY2026 capex raised ~$10.5B → ~$11.5B → the unnamed semiconductor assembly / advanced-packaging / test equipment supply tier — REJECTED
**Company A / the news:** ASE Technology Holding's Q3 2026 earnings call, **2026-10-29**, raised FY2026
capex to **~$11.5B** from its own **~$10.5B** given **2026-07-30** (which was itself a raise from
~$8.5B). Q3 was a record on revenue and margin, driven by advanced packaging. Incremental equipment
spend is disclosed as **60% to LEAP, 40% to mainstream operations**.
**Company B / the candidate:** any US-listed assembly, advanced-packaging or test equipment maker above
$10B — the drill asked for one **by name, from a filing**.

**1. Mechanism (one sentence):** **COULD NOT BE WRITTEN.** The sentence *"ASE's $1.0B capex raise lifts
[X]'s equipment revenue"* has no value for X that any source supplies. ⚠ **The candidates that arrive
instantly — AMAT, Teradyne, KLA — arrive from my own familiarity with the industry, which is precisely
the §4 limitation and not evidence.** ⚠ **The drill asked the question directly and got a direct
negative: no US-listed company above $10B both supplies ASE and has disclosed ASE as a named customer
or quantified ASE revenue in a filing.** ASE's own disclosure names a **component category and a
percentage split** and no vendor — **rule (v)'s most fillable-looking blank, in its exact canonical
form: a precise figure plus named component categories.**

**2. Dollar path:** **NOT WRITABLE, and it fails twice over even if a name is supplied.** The $1.0B is
ASE's **outgoing capex**, split between **facilities and equipment** with no further allocation, spread
across an unknown vendor set. Against AMAT's or Teradyne's revenue base an unallocated share of <$1.0B
is immaterial, and §4's 10%-of-revenue floor is unreachable. ⚠ **The figure is also money paid OUT by
the only leg whose figure is disclosed — rule (viii).**
**3. Timing window:** not reached. Part 1 failed.
**4. Invalidation:** not reached. Part 1 failed.

**Hard filters:**
- Priced-in (§4): **NOT RUN, AND NOT DUE — no `move` call was made on any symbol at this seat.** ⚠ **No
  candidate reached the filter, so the filter did not pass. Absent, not passing.**
- Correlation (§4): **no operand** — zero open satellite positions, so no `driver` field exists to
  collide with.
- Universe (§3): **not reached at Company B** (there is no Company B). Company A, ASE, is Taiwan-listed
  with a US ADR (ASX) and is in any case the first-order name.

**Outcome:** **REJECTED at part 1 / rule (v).** ⚠⚠ **This is the day's one genuine rule (iii) pass and
it is the entry the human should read, because it corrects an emphasis this log has been building for
two sessions.** 10-29 recorded that no AI-capex figure moved up and wrote that up as the whole of the
day's disposal, which invites the reading that an upward move was the missing ingredient. **It was not.
ASE delivered the upward move on the right figure with the prior figure present and dated, and the
thesis died at the very next rung for a reason that had nothing to do with direction.** ⚠ **Cost: one
drill query, which also returned the disclosure-history answer for free.**

---

### T-2026-10-30-02 — AMZN (Amazon) FY2026 capex ~$220B → the unnamed AI-infrastructure supply base — REJECTED
**Company A / the news:** Amazon's Q3 2026 results, reported after the close **2026-10-29**,
**maintained** CY2026 cash capex at **~$220B**.
**Company B / the candidate:** the datacenter, power, networking and optical supply base.

**1. Mechanism (one sentence):** **FAILS ON RULE (iii) BEFORE IT IS WRITTEN.** The figure was
**reaffirmed, not raised** — costume #1 on the standing list, and the fourth large AI-capex disclosure
in two sessions (after Alphabet's reaffirmation, Microsoft's downward revision and Tesla's cut) that
did not move up against the company's own prior. **A reaffirmation changes nobody's economics.**
**2. Dollar path:** **the increment is $0.** There is no magnitude to allocate. Rule (v) kills it
independently: *"the AI-infrastructure supply base"* names nobody, and $220B is the largest number this
funnel has met this week, which makes the unnamed blank look more fillable rather than less.
**3. Timing window / 4. Invalidation:** not reached.

**Hard filters:** priced-in **not run and not due**; correlation **no operand**; universe not reached.

**Outcome:** **REJECTED — rule (iii) costume #1, with rule (v) and part 2 as independent kills.** ⚠ **Of
five AI-capex disclosures across two sessions, exactly one moved up (ASE) and that one died at rule (v)
— see `-01`. The complex is now disposed on BOTH axes and neither needs a further query.**

---

### T-2026-10-30-03 — BMRN (BioMarin) ← GC Biopharma / Hanmi licence "up to $475M" — REJECTED
**Company A / the news:** reported **2026-10-30**: a licensing arrangement among **GC Biopharma**,
**Hanmi Pharmaceutical** and **BioMarin Pharmaceutical (BMRN)** valued at up to **$475M** — **$70M
upfront** plus up to **$405M in milestones**, plus royalties.
**Company B / the candidate:** none exists. See below.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN, because BMRN is a NAMED PARTY.** §4 asks for a
Company B whose economics change because of news about Company A; a party to the transaction is
**first-order**. A genuine second-order drill would have to reach a **third** company, and none is
named at any leg.
**2. Dollar path:** **fails on scale before the direction of payment is even established.** The only
near-term figure is the **$70M upfront** — the $405M is milestone-contingent and undated, which is rule
(v)'s ceiling sub-shape. $70M against BioMarin's revenue base is ~2%, against §4's **10%** floor. ⚠ **And
the direction is not established in the source: if BMRN is the licensee, the $70M is money paid OUT —
rule (viii). I did NOT spend a query to settle that, because part 1 had already killed it and the answer
could not change the outcome in either direction. Recorded so the omission is visible rather than
implied.**
**3. Timing window / 4. Invalidation:** not reached.

**Hard filters:** priced-in **not run, not due**; correlation **no operand**; universe — BMRN is
US-listed and above the §3 floor, **the one filter this item would have passed**, which is not progress
toward a trade.

**Outcome:** **REJECTED at part 1 (named party, no Company B), with part 2 as an independent kill.**
⚠ **Logged chiefly because the funnel's own self-exclusion was wrong — it dismissed the item as "two
Korean companies, not US-listed" and missed that BioMarin is the US-listed leg. That is the second
instance of the 10-13 Bloom lesson: A SELF-EXCLUSION IS A HINT, NOT A RULING. The correction cost one
sentence and the item still died, which is the honest outcome both times.**

---

### T-2026-10-30-04 — Orion Group Holdings $250M October awards · AEVEX $41.6M Maritime Systems — REJECTED (§3, two numbers, zero queries spent)
**Company A / the news:** **Orion Group Holdings**, 2026-10-29, announced **$250M** of October contract
awards and change orders including a **$115M** mission-critical project in its **Concrete** segment.
**AEVEX Corp.**, 2026-10-30, announced its **Maritime Systems** division won **$41.6M** across two
contracts ($15.6M SightGlass, $26.0M Fisher).
**Company B / the candidate:** none sought.

**1. Mechanism:** **not attempted.** Both are **own-award announcements** — the company announcing is
the company winning, so there is no second party and no Company B (part 1, structural).
**2–4:** not attempted.

**Hard filters:** **Universe (§3) kills both on a single number each — both are far below the $10B
market-cap floor.** ⚠ **§3-FIRST, applied as the discipline requires: the cap was checked before any
mechanism was elaborated, so no effort went into a story a single number was always going to end.**

**Outcome:** **REJECTED — §3 cap floor, plus part 1 independently.** ⚠ **These were the only two items
scan 2 returned with a winner's own segment named and a figure attached — the exact part-2 evidence that
is usually missing — and both are ineligible. §3 does not weigh outcomes and does not care that the
disclosure quality was, for once, good.**

---

### T-2026-10-30-05 — RTX — the 2026-10-13 award RE-SERVED — REJECTED (rule (iv), EIGHTH APPEARANCE, ZERO QUERIES SPENT)
**Company A / the news:** none that is new. Scan 2 surfaced an RTX item and **volunteered the kill in
its own sentence**: *"The cited item refers to an RTX contract announced on October 13, not October 29
or 30, and its annual-revenue percentage is an outside calculation rather than RTX's own
quantification."*

**1–4:** **not attempted. Disposed on the log, not on the tape.**

**Outcome:** **REJECTED — rule (iv), and the disposal needed no query because reading the log first
answered it.** ⚠⚠ **THIRD CONSECUTIVE SESSION the funnel has re-served this log's own disposed rejects
(10-09 three, 10-12 three, today one). The standing lesson holds and paid again: reading the log costs
one grep and saves a drill.**
⚠⚠ **AUDIT CATCH — THE INHERITED APPEARANCE COUNT IS WRONG BY ONE, AND IT IS WRONG IN THE DIRECTION
THAT UNDERSTATES THE PROBLEM.** `state.md` carries *"RTX IS NOW AT SIX APPEARANCES IN NINE SESSIONS"*,
built from a list beginning **09-29 (AMRAAM)**. Re-derived at this seat from thesis headers across
`research_log.md` **and** `archive/research_log/2026-09.md`: **T-2026-09-01-03 (RTX, died at part 1 on
an unsourced PAC-3 inference) · T-2026-09-29-01 (AMRAAM, RTX in the body) · T-2026-10-02-01 ·
T-2026-10-09-02 · T-2026-10-12-02 · T-2026-10-14-04 · T-2026-10-20-04 = SEVEN prior appearances.
Today is the EIGHTH.** ⚠ **The omitted entry sits in the September archive, which is exactly where a
count built by reading the live file will lose it — the same archive-inclusive arithmetic defect the
10-28 and 10-29 seats flagged on the thesis total.** *(Thesis total re-derived at this seat and it
MATCHES: 126 unique IDs live + 87 archived, combined unique **210**, and 123 + 87 header-defined IDs
= 210 with no header overlap.)*

---

### T-2026-10-30-06 — sweep: non-US-listed parties, unnamed counterparties, no-figure agreements, own-results prints — REJECTED (thirteen items, disposed as one, ZERO drill queries spent)

Every item the four scans returned that is not disposed above. **Each dies on a single named test, and
none was elaborated into a mechanism.**

| Item | Test that killed it |
|---|---|
| **T1 Energy (TE)** — >1.58 GW of solar-module offtake, 2026-10-30 | **No dollar amount disclosed, and the counterparties are not named.** GW is **not money** — the 10-12 UNIT failure recurring. |
| **Samsung Electro-Mechanics** — ~**$659.3M** MLCC supply contract, 2026-10-30 | **§3** (KRX-listed) **and** the customer is *"a global company"*, unnamed. ⚠ **Third appearance of this issuer in this log and the third identical death.** |
| **Critical One Energy / Solar International Core Canada** — C$25M + up to C$400M | **§3** — Canadian-listed; a third party (Northlink) is not listed at all. |
| **Woodside Energy / QatarEnergy** — 20-year LNG SPA | **§3** and **part 3** — rule (vi)'s standing shape; **no figure disclosed.** |
| **ABP Food Group / Dovecote Park** — UK CMA phase-one inquiry, 2026-10-29 | **§3** (neither party US-listed) **and** merger arbitrage is not in §4. |
| **ATI** FY2026 capex $280–300M | **Rule (iii) unestablishable** — no prior company figure in the source, so the direction cannot be read in either direction. |
| **RPC** FY2026 capex $155–175M | **Rule (viii) sign** — deliveries **shifted out of 2026 into 2027**; spending deferred, not added. |
| **Shell** FY2026 capex $23–25B | **Rule (iii) unestablishable** (no prior figure in source) **and §3** (not US-listed). |
| **Sterling Infrastructure** | **Rule (iii) unestablishable** — a prior ~$140M reference with no new figure stated. |
| **Huntington Ingalls (HII)** — $32.4B Q3 awards, raised shipbuilding forecast | **Part 1 — own results**, no transaction, no named second party. |
| **General Dynamics (GD)** Q3 2026 | **Part 1 — own results.** |
| **Exelon (EXC)** Q3 2026 | **Part 1 — own results.** |
| **Regeneron (REGN)** Q3 2026 | **Part 1 — own results.** |

⚠ **Five of the thirteen are own-results prints and that is the shape of a late-October tape: the
earnings wall is the one disclosure class that structurally names a single party.** ⚠ **A competitor
read-across is the only Company B any of them offers, and that is the shared-cause object — a market,
not a transaction. Killed on part 1 each time, as the standing rule says to expect every earnings
season.**

---

### 2026-10-29 (08:14 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,992.07** at pre-flight).
`clock` at 08:14:15 reads `is_open: false` with `next_open` **2026-10-29T09:30:00-04:00** and
`next_close` **2026-10-29T16:00:00-04:00** — both carry today's date, the pre-market full-session
signature. Not a holiday. Window surveyed: Wednesday 2026-10-28 after the close through this morning.

**Ledger reconciled, three sides, agreeing.** Alpaca `positions` = one row, core VOO only
(99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, unchanged since 2026-09-03) · `positions.md`
satellite count **0** · `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **No discrepancy.**

**Every §6 gate open.** Breaker INACTIVE, `halt_triggered_at: none`; `new_positions_this_week` **0 of
3** (week anchor re-derived with `isocalendar`: 2026-10-29 is ISO 2026-W44, Monday anchor 2026-10-26,
matches `week_of`, no rollover); satellite 0.0% deployed, **$30,000 idle**; `control.md` Notes empty;
zero open alerts. 5% cap **$4,999.60**.

**Three broad scans, one drill, zero survivors.** The overnight window is dominated by an
earnings-print wall — Alphabet, Microsoft, Oracle, FedEx, Ford, Vertiv, Robinhood, SK Hynix — the one
disclosure type that structurally names a single party. Scan 2 (new named-counterparty agreements,
M&A and earnings and policy excluded in the prompt) returned **zero qualifying items** and said so:
*"no qualifying announcement by a US company can be verified."* Scan 3 (regulatory enable/block
actions with a named US-listed supplier) likewise: *"No qualifying regulatory, antitrust, court,
tariff, or export-control action is identified."*

**The day's one genuinely useful result, and it is a negative with a shape worth naming.** The tape
this morning is moving on AI capital spending, which is the one earnings-season disclosure class that
*does* have a supplier chain hanging off it. So the drill asked the only question §4 cares about:
**did the capex figure move against the company's own prior figure, and in which direction?** All
three large disclosures answer the wrong way:

| Company | Capex figure disclosed | Its own prior figure | Direction |
|---|---|---|---|
| Alphabet FY2026 | $195–205B | $195–205B | **unchanged** — reaffirmation, rule (iii) costume #1 |
| Alphabet FY2027 | *"increase significantly"* | none stated | **unquantifiable** |
| Microsoft CY2026 | ~$170B | ~$175B | **down** |
| Microsoft quarter | $45.2B actual | $50B own projection | **underspent**, plans *"unchanged"* |
| Tesla FY2026 | ~$20B | *">$25B"* | **down ~$5B** |

**Not one figure moved up.** The two that moved, moved down; the one that was raised was raised in
**July**, three months before this window. ⚠ **A long-only second-order book cannot trade spending
being withdrawn — there is no named party whose revenue improves.** That is rule (viii) applied to
three companies in one night, and it is the whole of today's disposal.

⚠ **FOMC held at 3.75–4.00% (10–2) at 14:00 yesterday. NO NEW ID MINTED.** `T-2026-10-27-04` disposed
it in both states, pending and decided; the standing instruction is that a change in status is not a
change in eligibility. Honoured, not re-litigated.

⚠ **VRT IS NOT RE-LITIGATED AND NO NEW ID IS MINTED FOR IT.** It died at part 1 yesterday
(`T-2026-10-28-01`) and the carry-forward forbids re-opening a disposal on the same event. Recorded
only because the number is new and makes the point twice over: `move --sessions 5` returns
**+14.48%**, so VRT is now **mechanically LATE** as well as structurally dead. The item I most wanted
to work yesterday became the item it would have been most expensive to work today.

---

### T-2026-10-29-01 — GOOGL (Alphabet) → the datacenter / power / optical supplier tier — REJECTED

**Company A / the news:** Alphabet Q3 2026, released after the bell 2026-10-28. Revenue missed;
free cash flow **−$9.1B**; Q3 property-and-equipment purchases **$51.4B**; shares −~10% after hours.
FY2026 capex guidance **$195–205B**; FY2027 described only as *"increase significantly."*
(Perplexity, recency=day: Alphabet Q3 2026 earnings call transcript, alphastreet; CNBC 2026-10-29;
ppc.land.)
**Company B / the candidate:** the unnamed suppliers of datacenter capacity, power equipment and
optical interconnect that $195–205B of capex is spent with.

**1. Mechanism (one sentence):** cannot be written without an "and also."
> *"Alphabet's capex guidance causes [supplier]'s segment revenue to improve because Alphabet buys
> from it"* — **and also** Alphabet must spend **more** than it had already said it would, **and
> also** the supplier must be named somewhere, **and also** its share of that spend must be known.
**Three added clauses. Part 1 fails.**

**2. Dollar path:** **not calculable in either direction.** The FY2026 figure is unchanged, so the
increment is **$0**. The FY2027 figure does not exist — *"increase significantly"* is not a number.
No supplier is named by Alphabet or by any source in the window, so there is no segment and no
revenue share to compute. **Part 2 fails.**

**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:** (applied first, per §4, and two of them are the kill)
- Priced-in (§4): GOOGL **−2.79%** over 5 sessions → the script returns *"passes the priced-in
  check."* ⚠⚠ **DO NOT READ THAT AS A PASS. This is open human item 1 arriving live: the move is a
  DRAWDOWN on a bad print, and the −10% after-hours drop is not in the closes yet, so this morning's
  gap down will make the filter read MORE room, not less.** The filter cannot distinguish *"has not
  moved on this news"* from *"moved hard the wrong way."* **Recorded as an instance, not used as a
  pass — the thesis was already dead at parts 1 and 2.**
- Correlation (§4): no open satellite positions, so no driver to collide with → no operand.
- Universe (§3): US-listed, mega-cap, passes — and **irrelevant**, because §3 passing is not progress.

**Outcome: REJECTED at part 1 and independently at part 2, and the deeper kill is rule (iii).**
Alphabet **reaffirmed** its FY2026 capex range. A reaffirmation is costume #1 on the rule (iii) list
and this is its purest form: the figure *was* raised — from $175–185B to $195–205B — **in July**, and
reaches this funnel only because an earnings release restated it. ⚠ **The raise is real and is three
months old. The release is new. Those are not the same thing, and the TSMC lesson of 10-15 applies
exactly: apply rule (iii) to the figure the mechanism actually runs on, not to the release.**
⚠ **And the figure with the supplier chain is the one that did not move, while the figure that moved
(FY2027) has no number — the 10-15 sign problem recurring with the clauses swapped.**

---

### T-2026-10-29-02 — MSFT (Microsoft) → third-party datacenter capacity providers — REJECTED

**Company A / the news:** Microsoft Q1 FY2027, 2026-10-28. Azure +48% y/y. Quarterly capex **$45.2B
against Microsoft's own $50B projection**, which Microsoft attributed to **delayed third-party
capacity deliveries** and stated did **not** represent a change to its underlying spending plans;
calendar-2026 spend now *"approximately $170 billion"* against a prior *"$175 billion."* CoreWeave
and Nebius fell on the capex signal. (Perplexity, recency=day: MSFT Q1 FY2027 call transcript,
alphastreet; CNBC 2026-10-29; Fidelity/Reuters 2026-10-28.)
**Company B / the candidate:** the third-party capacity providers whose deliveries slipped.

**1. Mechanism (one sentence):** **fails on the sign.**
> *"Microsoft's capex underspend causes [provider]'s revenue to improve…"* — it does the opposite.
> Revenue Microsoft did not spend is revenue no provider recognised. The only improving reading is
> *"capacity is scarce, so pricing power rises,"* which needs an "and also" and names nobody.

**2. Dollar path:** **wrong sign and wrong party.** The $4.8B gap between $50B projected and $45.2B
actual is **spending that did not happen**; the $5B calendar-year revision is **downward**. Rule
(viii): read which direction the disclosed figure moves. Both move away from any Company B.
⚠ **And Microsoft said the forward plan is unchanged, so on its own account no budget figure moved at
all — the only thing that moved was timing.** **Part 2 fails.**

**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): MSFT **−0.11%** over 5 sessions → passes, and irrelevant.
- Correlation (§4): no operand.
- Universe (§3): passes, and irrelevant.

**Outcome: REJECTED at part 1 on the sign, and at part 2 on rule (viii).** ⚠ **The named second
companies the market actually traded — CoreWeave and Nebius — went DOWN, which is the market agreeing
with this disposal rather than contradicting it.** ⚠ **Rule (v) rides on top: "delayed third-party
capacity deliveries" is an UNNAMED supply base made to look nameable by a precise figure ($45.2B vs
$50B) and a named category ("capacity"). The source left the blank; filling it in is not research.**
⚠ **A quieter reason not to build on these figures even if the sign were right: the sources do not
agree on them.** One reports calendar-2026 capex at **$118.1B** against a *"prior full-year forecast"*
of **$175B**; another reports **~$170B** vs **~$175B**. Those cannot all be the same quantity.
**Figures that contradict each other across sources are not a dollar path.**

---

### T-2026-10-29-03 — TSLA (Tesla) → the automotive / battery / factory-equipment supplier tier — REJECTED

**Company A / the news:** Tesla cut its 2026 capital-spending outlook to **approximately $20B from
more than $25B** — an explicit forward reduction of at least ~$5B against its own prior figure.
(Perplexity, recency=day: Fidelity/Reuters 2026-10-28.)
**Company B / the candidate:** none identified; no supplier is named in the disclosure.

**1. Mechanism (one sentence):** **fails on the sign, in the cleanest form this funnel has produced.**
> *"Tesla cutting $5B of capex causes [supplier]'s revenue to improve"* is not a sentence that can be
> written at all. The money is being **withdrawn**.

**2. Dollar path:** the only disclosed figure is **−$5B of spending**. Rule (viii). **Part 2 fails.**
**3 / 4:** not reached.

**Hard filters:** not run — §4 says filters come before the thesis, and this one died before a ticker
existed to filter. No `move` call was spent.

**Outcome: REJECTED at part 1.** ⚠ **Logged rather than dropped because it is the day's third
independent instance of the same shape and the three together are the finding: Alphabet's figure did
not move, Microsoft's moved down, Tesla's moved down. The AI-capex complex that is driving the tape
this morning contains NO disclosed figure that moved up against its own prior.** ⚠ **A long-only
second-order book has nothing to do with a capex cut. There is no short leg in this strategy and §3
forbids every instrument that would create one.**

---

### T-2026-10-29-04 — MU (Micron) ← SK Hynix record quarter — REJECTED

**Company A / the news:** SK Hynix reported a record quarter, described as a more-than-sevenfold y/y
profit increase; shares +13%. Micron rose ~5.9% on the read-through. (Perplexity, recency=day:
sedaily 2026-10-29; newstribune 2026-10-29.)
**Company B / the candidate:** Micron Technology (MU).

**1. Mechanism (one sentence):** **fails — this is the shared-cause object, and in its most
respectable costume: a competitor's earnings print read across.**
> *"SK Hynix's record quarter causes Micron's DRAM revenue to improve because…"* — **because the DRAM
> market is tight.** SK Hynix did not buy anything from Micron and did not sell anything to it.
> **They are competitors in the same market responding to the same input.** Two companies moving on
> one macro input is a **market**, not a **transaction**.

**2. Dollar path:** no figure attaches to Micron from SK Hynix's result. No transaction, no segment,
no share. **Part 2 fails independently.**
**3 / 4:** not reached.

**Hard filters:**
- Priced-in (§4): MU **+7.59%** over 5 sessions → **FAIL, LATE.** ⚠ **This one is a genuine
  mechanical kill and it would have fired even if part 1 had held — it is the filter working as
  designed, on a real advance, which is worth recording beside `T-2026-10-29-01` where the same
  filter returned a meaningless pass on a drawdown. Same script, same threshold, two completely
  different epistemic values. That is open human item 1 in one paragraph.**
- Correlation (§4): no operand.
- Universe (§3): US-listed, passes.

**Outcome: REJECTED at part 1 (shared cause), at part 2 (no figure), and at the priced-in filter
(+7.59%).** ⚠ **Related to but distinct from `T-2026-10-28-03`, which took the SAME SK Hynix event to
AMAT/LRCX/KLA via the equipment chain. That was a supplier story and died on parts 1, 2 and 3. This
is the competitor story and dies on part 1. One event, two candidate shapes, two different deaths —
and rule (iv) now applies to the EVENT: SK Hynix's quarter has produced a candidate on two
consecutive sessions and killed it both times.**

---

### T-2026-10-29-05 — ORCL (Oracle) — REJECTED

**Company A / the news:** Oracle issued a fiscal-2030 outlook of **more than $225B revenue**
(implying >35% average annual growth); shares +~10.6%. Separately disclosed a plan to raise **no more
than $20B** in additional AI financing through fiscal 2030, and said capital spending will peak in
the current and following fiscal years then decline. (Perplexity, recency=day: kansascity.com /
sedaily / theedgemalaysia 2026-10-28–29.)
**Company B / the candidate:** none reaches a thesis.

**1. Mechanism:** not written. **Part 3 kills this before part 1 is worth spending a clause on** —
per rule (vi), screen the timing window early. FY2030 is **~16 quarters** against §4's **two**.
**2. Dollar path:** the $225B is **Oracle's own revenue**, not a segment at any Company B. The $20B
is a **FINANCING CEILING** — rule (viii), the Brookfield/Bloom $25B and Tesla $30B shape, money
*available to be raised*, not revenue earned by anybody. ⚠ **"No more than" is also rule (v)'s
CEILING sub-shape: a maximum, not a commitment.**
**3. Timing window:** **FY2030 → ~16 quarters. FAIL.**
**4. Invalidation:** not reached.

**Hard filters:** not run; part 3 ended it at the first date read, which is the §3-first discipline
applied to the timing test. No `move` call spent.

**Outcome: REJECTED at part 3, independently at part 2 twice over.** ⚠ **And the capex sentence cuts
against the only mechanism anyone would reach for: Oracle said spending will PEAK and then DECLINE.
Even the generous reading has the wrong sign past the near term.**

---

### T-2026-10-29-06 — sweep: own-results prints, non-US-listed contracts, government counterparties, one macro object — REJECTED (fifteen items, disposed as one, ZERO drill queries spent)

Every item below was killed by a rule already written down, from the scan output alone. **No drill
query was spent on any of them**, which is the point of the recognise-on-sight list.

**Own results, one party (shared-cause / first-order kill):**
- **FedEx** raised FY profit and sales guidance — no figure disclosed in the window, no counterparty.
- **Ford** raised the low end of FY profit guidance — no revised range disclosed, no counterparty.
- **Robinhood** Q3 profit below expectations on softer crypto activity, −3.3% — ⚠ **an earnings MISS
  is not a second-order catalyst, and the share-shift story has the wrong sign for a long.**
- **Alphabet / Microsoft / Oracle / Vertiv / SK Hynix** — worked above or disposed yesterday.

**§3, non-US-listed or below the floor** (the recurring majority of this funnel):
- **EnSilica plc** (UK) — ~$2.4M development-and-supply agreement with an **unnamed** US healthcare
  technology company. §3 **and** rule (v): the only buyable leg is the unnamed one.
- **Gaon Cable** (KRX) — **$90M** cable supply to an **unnamed US cloud company**. ⚠ **A precise
  figure plus a named category and an unnamed counterparty is the most fillable-looking blank this
  funnel produces. The priors arrive instantly and none of them is a disclosure.** Rule (v) + §3, and
  rule (viii) on top: the money is paid **by** the US leg **to** the Korean one.
- **Taihan** (KRX) — ~$90M EHV grid supply to its **own US subsidiary**, end customer unidentified.
- **Woodside** (ASX) / QatarEnergy — 20-year LNG SPA, up to 3 Mtpa, **no dollar value**. ⚠ **Rule
  (vi), the standing LNG shape: 20 years against two quarters. Venture Global's own answer, reused.**
- **Critical One Energy** (Canada) — C$25M + up to C$400M construction financing, Canadian project.
- **Kongsberg** (Oslo) — $54M DoD contract extension. **Government counterparty, one party.**
- **SK pharmteco** (Korea) — >$200M five-year US capacity plan, no counterparty.
- **UMC** (Taiwan) — ~$3.2B additional capex approved. §3; and no US-listed supplier named.
- **Eldorado Gold** — raised Skouries project capital to ~$1.425B plus $390M accelerated operational
  capital. ⚠ **Capital paid OUT by the only listed party, rule (viii), and no supplier named.**
- **AdvanSix (ASIX)** — $98.1M ammonia capacity expansion with **$47.4M proposed USDA funding**.
  ⚠ **US-listed and a real transaction, and it dies twice: the counterparty is a GOVERNMENT AGENCY
  (one party, no named recipient of a sale), and §3 kills ASIX on the market-cap floor regardless.**
- **Alume Biosciences** — FDA **accepted an NDA for filing**, product still investigational, **not
  approved**. ⚠ **An acceptance-for-filing is weaker than the expanded-indication shape of 10-06: it
  creates no product, no supply chain and no date. And no supplier is named.**

**Macro / policy, one party:**
- **FOMC held 3.75–4.00%, 10–2**, with an indication of fewer meetings next year. ⚠ **NO NEW ID
  MINTED — `T-2026-10-27-04` disposed this in both the pending and the decided state. The standing
  instruction was honoured at this seat.** Counted here as a swept item, not as a thesis.
- **10-year / 30-year yields, the "AI sell-off" and the Treasury rally** — a government action and a
  market variable. No named recipient, no transaction.

**Outcome: REJECTED, all fifteen.** ⚠ **Nine of the fifteen are killed by §3 alone, which is the
single most common death in this log and is a fact about where news is generated, not about this
funnel's judgment.** ⚠ **And the §3-first discipline held: for Gaon Cable, Taihan, EnSilica and
Woodside the market cap or listing venue was read BEFORE any mechanism was elaborated, so no effort
went into a story a single field was always going to end.**

---

### 2026-10-28 (08:04 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$100,156.48** at pre-flight
08:03). `clock` at **08:04:26** reads `is_open: false` with `next_open` **2026-10-28T09:30:00-04:00**
and `next_close` **2026-10-28T16:00:00-04:00** — **both carry TODAY's date, the pre-market
full-session signature. Not a holiday, not an early close.** Window surveyed: Tuesday 2026-10-27
after the close through this morning — a normal overnight window.

**Ledger reconciled FIRST, three sides, all agreeing.** Alpaca `positions` = **ONE row, core VOO
only** (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, unchanged since 2026-09-03) ·
`positions.md` satellite header count **0** (`grep -cE '^### [A-Z]{1,5} '`) · `sleeves`
`satellite.count: 0`, `value: 0`, `pct: 0.0`. **NO DISCREPANCY.**

**Every §6 gate open and nothing was bought — a research result, not a permission result.** Breaker
**INACTIVE**, `halt_triggered_at: none`, `new_positions_this_week` **0 of 3** (week anchor
re-derived with `isocalendar`: Wed 2026-10-28 is ISO 2026-W44, Monday anchor **2026-10-26**, matches
`week_of`, **NO ROLLOVER**), satellite **0.0% deployed**, `control.md` Notes **EMPTY**, zero open
alerts. 5% cap **$5,008.32**. **$30,000.00 idle across 38 post-fill sessions.**

**TWO BROAD SCANS, TWO DRILLS, ANNOUNCEMENT DATE AND ISSUER DEMANDED INSIDE EVERY PROMPT.**
⚠⚠ **BOTH SCANS ANSWERED §4's QUESTION IN THE NEGATIVE OUT LOUD.** Scan 1 (overnight events)
returned **four earnings prints and two macro data releases and said so**: *"No source in the
available results verifies a new large U.S. contract award, regulatory approval, or supply
agreement issued between Tuesday's close and Wednesday morning."* Scan 2 (new two-party
transactions, M&A and earnings and policy excluded by the prompt) returned **exactly one** item
meeting its own screen — **ELVA/Janus**, which §3 kills — and stated *"No qualifying October 27
transaction is established by the available results."*

⚠⚠ **THE DAY'S SHAPE IS AN EARNINGS-SEASON WALL: FOUR OF SIX ITEMS IN SCAN 1 ARE A COMPANY
REPORTING ITS OWN RESULTS, WHICH IS THE ONE DISCLOSURE TYPE THAT STRUCTURALLY CANNOT CARRY A
SECOND-ORDER MECHANISM** — it names one party. The carry-forward warned to expect exactly this
every earnings season and the answer was already written for three of the four.

⚠ **THE FOMC DECISION LANDS TODAY AT 14:00 ET AND NO NEW ID IS MINTED FOR IT.** `T-2026-10-27-04`
disposed it yesterday **in both states**, pending and decided, and the carry-forward instruction is
explicit that a change in STATUS is not a change in ELIGIBILITY. Scan 1 volunteered it as
*"a scheduled event, not an announced regulatory decision."* **Honoured, not re-litigated.**

---

### T-2026-10-28-01 — VRT — REJECTED
**Company A / the news:** Vertiv Holdings Q3 2026 results, **issued by Vertiv, 2026-10-28**: net
sales **$4.313B** (+61%), organic orders **more than doubled** YoY, FY2026 sales guidance **raised
by $650M** (source: Vertiv release via Morningstar/PR Newswire, and Vertiv 8-K).
**Company B / the candidate:** Vertiv's own component suppliers — power, thermal and busway
vendors — unnamed.

**1. Mechanism (one sentence):**
> Vertiv's raised FY2026 sales outlook causes supplier X's revenue to improve because Vertiv will
> have to buy more components **and also** because Vertiv converts that outlook into purchase
> orders that nobody has disclosed.

⚠ **THE SENTENCE NEEDS THE "AND ALSO" AND THAT IS THE WHOLE KILL (§4 part 1).** This is the
**TSMC 10-15 shape exactly**, and the standing rule applies verbatim: *apply rule (iii) to the
figure the mechanism actually runs on.* The figure that **moved** is Vertiv's own **revenue**, which
has **no supplier chain hanging off it**; the figure a supplier mechanism would need is Vertiv's
**procurement**, which **was not disclosed at all.**

**2. Dollar path:** **ABSENT — and both halves fail.** No segment at any Company B, because there
is **no named Company B**: the targeted drill asked directly whether VRT disclosed a named
counterparty with an attributable dollar figure and the answer came back **"No … the available
disclosure does not identify a third-party counterparty with an associated dollar amount."**
**$650M is Vertiv's own top-line guidance increase, i.e. revenue at Company A.** Rule (viii),
read broadly: *any disclosed figure that is not segment revenue at Company B fails part 2.*
**3. Timing window:** not reached — part 1 and part 2 both dead first.
**4. Invalidation:** not written — there is no thesis to invalidate.

**Hard filters:**
- Priced-in (§4): **NOT RUN, AND DELIBERATELY SO.** Standing rule (i) — *screen on the mechanism
  before running filters.* The kill is structural; a `move` call on a candidate already dead at
  part 1 buys nothing. ⚠ **No "but it might have passed" is available here, because the candidate
  has no ticker — the supplier was never named.**
- Correlation (§4): **NO OPERAND** — zero open positions, zero `driver` fields. ⚠ **Not the same
  as passing.**
- Universe (§3): VRT itself is US-listed and well above $10B, **which is irrelevant** — VRT is
  Company A here, and §3 is asked of Company B.

**Outcome:** **REJECTED at part 1, then independently at part 2.** ⚠ **THE HONEST NOTE: THIS WAS
THE DAY'S MOST ATTRACTIVE-LOOKING ITEM AND I WANTED IT TO WORK** — a genuinely new,
genuinely company-issued, correctly dated release, with a real rule (iii) **pass** on its own prior
guidance, in the one sector where this funnel keeps finding big numbers, on a day with $30,000 idle
and every gate open. **The pull was toward buying VRT itself, which is first-order and not what §4
asks**, and then toward an unnamed supplier, which is rule (v). **Neither is a trade.**

---

### T-2026-10-28-02 — GEV — REJECTED
**Company A / the news:** GE Vernova Q3 2026 results, **issued by GE Vernova, 2026-10-28**: orders
**$29.3B** (+96% organic), backlog **~$197B**, and an agreement to acquire **Trench Group for
$9.0B** (source: gevernova.com Q3 release; ⚠ **provenance caveat below**).
**Company B / the candidate:** Trench Group, and/or GEV's grid-equipment supply base.

**1. Mechanism (one sentence):** not written. **Dead before part 1 on two standing rules at once.**

**2. Dollar path:** **FAILS, and the $9.0B fails in the WRONG-DIRECTION way.** It is
**consideration paid OUT by the buyable leg to a seller** — the exact shape of GEHC/Sofie ($945M,
10-06) on the standing rule (viii) list. **The money leaves the only listed party.**
**3. Timing window:** not reached.
**4. Invalidation:** not written.

**Hard filters:**
- **MERGER ARBITRAGE IS NOT IN §4** — standing rule, answer needs no query: a target whose price is
  contractually pinned has no economics left to change, and the acquirer is first-order. Fourth
  deal in this repo's history to arrive in this costume (onsemi/Synaptics, Schneider/PTC,
  CHRW/RXO).
- Universe (§3): **Trench Group is NOT ESTABLISHED AS PUBLICLY TRADED** by the §3 check query
  (*"not established by the retrieved sources as a publicly traded company"*). **An unbuyable leg
  is not a candidate at any price.** The grid-equipment-supplier alternative is rule (v) — a supply
  base, unnamed, with no figure.
- Priced-in: not run; structural kill.
- Correlation: no operand.

⚠⚠ **PROVENANCE CAVEAT, RECORDED BECAUSE IT CUTS AGAINST ME RATHER THAN FOR ME:** the $9.0B
Trench figure reached this log through the **targeted drill's** citation of GEV's own release, and
the **follow-up §3 query could not independently substantiate it** — *"The claimed US$9.0 billion
GE Vernova acquisition was not independently substantiated by the retrieved search results."*
**The rejection does not depend on the figure being right**, which is why one query was not spent
confirming it. **Had the item survived the standing rules, confirming it would have been mandatory
before a thesis was written.**

⚠⚠ **GE VERNOVA IS NOW AT FOUR APPEARANCES** (10-15, 10-19, 10-20, **10-28**) **and this is the
rule (iv) warning in its strongest form, the RTX 10-20 form: a NEW DISCLOSURE *TYPE*** — the first
of GEV's appearances to carry an **acquisition** — **and it still dies at the same rung.** ⚠ **A
NEW DISCLOSURE TYPE IS NOT FRESH EVIDENCE WHEN THE KILL IS STRUCTURAL.** Expect GEV again; the
answer is written three times over.

**Outcome:** **REJECTED.** Merger arbitrage (outside §4) · rule (viii) money paid out by the
buyable leg · §3 unbuyable counterparty · rule (v) for the supplier variant. **Four independent
kills, zero drill queries spent.**

---

### T-2026-10-28-03 — AMAT / LRCX / KLA — REJECTED
**Company A / the news:** SK hynix Q3 2026 results, **issued by SK hynix, 2026-10-28**: record
quarterly revenue above **KRW 100T**, operating margin **~80% of revenue**, and the company said
**memory demand is expected to exceed supply through 2030**.
**Company B / the candidate:** US-listed semiconductor capital-equipment makers — Applied
Materials, Lam Research, KLA.

**1. Mechanism (one sentence):**
> SK hynix's statement that memory demand will exceed supply through 2030 causes Applied Materials'
> systems revenue to improve because SK hynix must add wafer capacity to close the gap **and also**
> because it will place orders it has not announced, in quarters it has not named, with suppliers
> it has not identified.

⚠ **"And also" twice. Part 1 fails.**

**2. Dollar path:** **FAILS — no figure attributable to any Company B exists.** KRW 100T is **Company
A's revenue**; the 80% margin is **Company A's profitability**. **No capex figure, no equipment
order, no named supplier.** ⚠ **"Demand will exceed supply" is a statement about a MARKET, which is
standing rule (v): a market-structure fact is not a supplier relationship.**
**3. Timing window:** **FAILS INDEPENDENTLY AND IT IS THE CHEAPEST KILL ON THE PAGE —
"through 2030" is ~16 quarters against §4's ceiling of TWO.** Standing rule (vi), killed in one
step before a query.
**4. Invalidation:** not written.

**Hard filters:**
- Universe (§3): **SK hynix is KRX-listed** — ⚠ **which does not by itself kill the thesis**,
  because §3 is asked of Company B, not Company A. The US-listed B candidates (AMAT, LRCX, KLA) all
  clear §3 comfortably. **This one dies on the mechanism, not the universe** — ⚠ **and recording
  that distinction matters, because the Antofagasta 10-15 note shows how easily a §3 kill on the
  wrong leg gets mistaken for a finished analysis.**
- Priced-in: not run; structural kill.
- Correlation: no operand.

**Outcome:** **REJECTED at part 1, part 2 and part 3 independently.** ⚠ **THE PRIOR IS ALREADY ON
THE BOOKS AND IT CAME OUT THE SAME WAY: `T-2026-10-15-01` TSMC → AMAT/LRCX/KLA. Same chain, same
three candidate names, same death. Second appearance of the memory/foundry-capex read-across in
nine sessions — rule (iv) applies to a MECHANISM as well as to a ticker.**

---

### T-2026-10-28-04 — ENPH — REJECTED
**Company A / the news:** Enphase Energy, **issued by Enphase, 2026-10-28**: weaker-than-expected
US residential solar demand; US revenue **+~3% sequentially**, which the company said was **below
expectations**; guided sales **lower**.
**Company B / the candidate:** residential-solar installers, distributors, battery and component
suppliers — and the share-shift read-across to competitors.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN IN THE REQUIRED DIRECTION.** ⚠⚠ **THE SIGN IS
WRONG FOR A LONG-ONLY BOOK AT EVERY NODE.** Weaker end demand at Enphase makes its suppliers'
economics **worse**, not better; the only *improving* story available is **"Enphase's
disappointment helps a competitor,"** which is the standing-rule object: **a competitor's
disappointment improves nobody's economics in any disclosed, dateable way — it only invites a
share-shift story THE READER SUPPLIES.** Standing rule, 10-02 sub-shape (Nike FQ1), expected every
earnings season and killed on part 1 each time.

**2. Dollar path:** **ABSENT.** Scan 1 said so without being asked: *"The available source does not
quantify effects on specific counterparties."* **No named counterparty, no segment, no figure.**
**3. Timing window:** not reached.
**4. Invalidation:** not written.

**Hard filters:** priced-in **not run** (structural kill, and the direction is wrong anyway);
correlation **no operand**; universe not reached. ⚠ **Enphase's own market cap was not pulled,
because it is Company A and §3 does not apply to it.**

**Outcome:** **REJECTED at part 1 on the sign, then at part 2 for want of any figure.** ⚠ **THE
USEFUL LINE: THIS IS THE FIRST *NEGATIVE* EARNINGS PRINT THIS FUNNEL HAS SERVED SINCE NIKE, AND IT
IS WORTH NOTING THAT IT IS NOT HARDER TO REJECT THAN A POSITIVE ONE — it is EASIER, because the
sign gives it away before the mechanism is even attempted. The positive prints (VRT today) are the
dangerous ones.**

---

### T-2026-10-28-05 — ELVA — REJECTED
**Company A / the news:** Electrovaya Inc. (ELVA), **issued by Electrovaya, 2026-10-28**: a
**strategic supply agreement** with **Janus Electric Holdings Limited** for Electrovaya lithium-ion
battery systems, with **~$26M in initial purchase orders** for US and Canadian demand; separately a
term sheet for Electrovaya to invest **~$1.4M** in Janus.
**Company B / the candidate:** Electrovaya itself is the supplier leg — this is the one item in
today's funnel where the **second-order leg is the one that issued the release.**

⚠⚠ **THIS IS THE ONLY GENUINELY NEW, GENUINELY FIRST-DISCLOSED, TWO-PARTY COMMERCIAL TRANSACTION
WITH A DISCLOSED DOLLAR VALUE AND NAMED COUNTERPARTIES THAT THE FUNNEL PRODUCED IN EITHER SCAN.**
It is a **clean rule (iii) pass** (scan 2, asked directly: *"it appears to be the first disclosure"*,
no amendment, no restatement, no re-pricing of an older framework), a **real purchase order rather
than a frame agreement or a ceiling** — **$26M in orders, not "up to $26M"** — and the rare case
where the money flows **INTO** the buyable-looking leg. **Every shape that killed the last fifty
candidates, it gets right.**

**Hard filters — §3 FIRST, AND IT ENDS HERE:**
- **Universe (§3): FAIL, and not marginally.** Market cap **C$366.49M** as of **2026-10-28**
  (source: Perplexity §3 check query, citing Hargreaves Lansdown company data) ≈ **US$0.26B**
  against §3's **$10B** floor — **roughly 38× below it.** The counterparty **Janus Electric
  Holdings** could not be established as publicly listed at all. **Ineligible.**
- Priced-in: **NOT RUN.** §3-first discipline, and it is the right call for the fourth session
  running (RARE 09-30, MTUS 10-01, ELMT): **pull the market cap before elaborating the thesis, so
  no effort goes into a story a single number was always going to end.**
- Correlation: no operand.

**1–4. Four-part thesis: NOT WRITTEN, DELIBERATELY.** §4 says apply the hard filters **before**
writing the thesis. The parts were not attempted and must not be reconstructed later.

**Outcome:** **REJECTED on §3 alone, at the first number pulled.** ⚠⚠ **THE FINDING, AND IT IS THE
ONE WORTH THE HUMAN'S ATTENTION TODAY: THE FUNNEL'S BEST-FORMED TRANSACTION OF THE DAY IS A
MICROCAP, AND THAT IS NOT A COINCIDENCE.** A $26M order is **material enough to announce** at a
$265M company and **too small to announce** at a $10B+ one. ⚠ **§3's floor and §4's requirement of a
NAMED, DATED, DOLLAR-QUANTIFIED two-party transaction pull in OPPOSITE DIRECTIONS: the disclosure
quality this strategy demands is systematically most available exactly where the universe rule
forbids trading.** ⚠ **ELMT is the standing proof that this does not become a reason to bend §3 —
"but now there is a number" and "but it went up" are the same pull wearing two coats.** **This is
a structural observation for the human, NOT a request to widen the universe, and no seat may act
on it.**

---

### T-2026-10-28-06 — sweep — REJECTED (five items, two drill queries spent, zero survivors)
Everything else both scans served, disposed in full. **None of these is price-dependent; none is to
be re-litigated.**

1. **QBTS / LG CNS** — D-Wave Quantum 8-K, 2026-10-28, a **NON-BINDING memorandum of understanding**
   on quantum-computing adoption. **No dollar value disclosed** → part 2 fails outright. ⚠ **And
   §3 kills it independently: QBTS market cap ~US$4.27–4.60B** (2026-10-26 close basis, source:
   Perplexity §3 check query citing Barron's/company data) **against the $10B floor.** ⚠ **An MOU is
   one rung BELOW a frame agreement, which the 10-15 Venture Global entry already established is
   not an order.** Scan 2 excluded it from its own qualifying list unprompted.
2. **Samsung Biologics / AstraZeneca** — long-term supply and commercial manufacturing agreement,
   **~$330.8M, expandable to ~$545.6M**, 2026-10-28. ⚠ **A real figure and a real two-party
   transaction — and §3 closes both doors: Samsung Biologics is KRX-listed, and the money is paid
   OUT by AstraZeneca**, whose US presence is an ADR of a UK-listed issuer. ⚠ **Rule (viii)
   wrong-party on top of §3: the leg receiving the revenue cannot be bought, and the leg that can
   be approximated is the one writing the cheque.** Scan 2 declined to include it for the same
   reason.
3. **Conference Board consumer confidence** — **91.7** in October from **84.2** in September
   (released 2026-10-27, reported 10-28); present situation **120.4**, expectations **72.6**. ⚠ **A
   7.5-point jump is a large move and it is still ONE PARTY AND NO TRANSACTION.** Macro data, not a
   Company A. Scan 1 classified it that way itself.
4. **September durable-goods orders** — **+1.8% m/m** against a **+1.5%** forecast; transportation
   **+4.6%**, civilian aircraft **+28.4%**. ⚠⚠ **THE AIRCRAFT LINE IS THE MOST CANDIDATE-SHAPED
   NUMBER IN THE SWEEP AND IT IS A BLANK: the source "does not identify the companies behind the
   aircraft-order increase" and cannot distinguish confirmed orders from estimates.** ⚠ **A precise
   figure plus a named COMPONENT CATEGORY and no named party is rule (v)'s most fillable-looking
   blank — the priors arrive instantly (BA, GE, SPR, HWM) and THE SOURCE LEFT THE BLANK.** **Filling
   it in is not research.** Also a **government statistical release**, i.e. the one-party object.
5. **FOMC, 14:00 ET today, consensus unchanged** — ⚠ **NO ID MINTED. Disposed at
   `T-2026-10-27-04` yesterday, in BOTH the pending and the decided state, by explicit
   carry-forward instruction.** Government action, one party, no transaction, no named recipient.
   **Recorded here only so the next reader can see it was seen and refused rather than missed.**

**Outcome:** **ALL FIVE REJECTED.** Two §3 kills, one rule (viii) wrong-party, two one-party macro
objects, one standing refusal honoured without a new ID.

---

### 2026-10-27 (08:20 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,915.80** at pre-flight
08:18). `clock` at **08:20:09** reads `is_open: false` with `next_open` **2026-10-27T09:30** and
`next_close` **2026-10-27T16:00** — ⚠ **both carrying TODAY's date: the pre-market full-session
signature. Not a holiday, not an early close. Read off the DATES, not the boolean.** Window
surveyed: Monday 2026-10-26 after the close through this morning — a normal overnight window, not
the thin weekend one.

**Ledger reconciled FIRST, three sides, all agreeing.** Alpaca `positions` = **ONE row, core VOO
only** (99.046311231 sh @ 706.74, `cost_basis` $69,999.989999, unchanged since 2026-09-03) ·
`positions.md` satellite header count **0** · `sleeves` `satellite.count: 0`, `value: 0`,
`pct: 0.0`. **NO DISCREPANCY.**

**Every §6 gate open and nothing was bought — a research result, not a permission result.** Breaker
**INACTIVE**, `halt_triggered_at: none`, `new_positions_this_week` **0 of 3**, satellite **0.0%
deployed**, `control.md` Notes **EMPTY**, zero open alerts. 5% cap **$4,996.43**, **$30,000.00 idle
across 36 post-fill sessions.**

**THREE BROAD SCANS PLUS TWO DRILLS, STRUCTURAL FRAMING FIRST, THE ANNOUNCEMENT DATE DEMANDED
INSIDE EVERY PROMPT.** ⚠ **THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE OUT LOUD IN BOTH
SCANS THAT ASK IT DIRECTLY.** ⚠⚠ **AND THE STREAK COUNTER IS *NOT* ADVANCED — THE CORRECTION IS
WORTH MORE THAN THE ORDINAL WOULD HAVE BEEN. A first draft of this entry wrote *"fifteenth
consecutive session"*, which INHERITED-AND-INCREMENTED A COUNTER THAT IS STALE AT FOURTEEN /
10-16 and has not been advanced since.** ⚠ **It is not cheaply re-derivable, and 10-20 is a
CANDIDATE BREAK: `MMM` reached the priced-in filter that day, so the funnel DID produce a
candidate.** ⚠⚠ **A COUNTER REACHED BY AN UNCHECKED ROUTE IS NOT A CHECKED FACT — recurring
error 4, caught in this run's own draft, inside the very paragraph reporting on the funnel.
THE TRACKED FIGURE STAYS FOURTEEN THROUGH 10-16; TODAY IS AN INSTANCE, NOT AN ORDINAL.** Verbatim: *"No announcement in the
available results can be confirmed to meet all of the stated criteria"* (structural framing, which
then **self-excluded four items with a named reason against each**) · *"no company can be reported
as meeting all criteria based on the available evidence"* (segment-quantification framing, five
self-exclusions). ⚠ **The scan-1 "significance" framing editorialised toward macro exactly as the
carry-forward predicts — a pending FOMC decision, Treasury yields and four own-results earnings
prints — and the structural framing is the one that found the day's only real object.**

⚠⚠ **THE DAY'S ONE FINDING, AND IT IS A GENUINELY NEW SUB-SHAPE OF RULE (iii) — THE MOST PROLIFIC
RULE IN THIS LOG — BECAUSE IT DEFEATS THE PROVENANCE TEST RATHER THAN FAILING IT: A SEVEN-WEEK-OLD
AGREEMENT ARRIVED WRAPPED INSIDE A GENUINELY NEW, GENUINELY COMPANY-ISSUED PRIMARY DISCLOSURE.**
Verizon's **2026-10-26** Q3 earnings release is real, new and issued by the company — it passes
every provenance test this log has built. **Inside it, Verizon refers to its Corning fiber
agreement as announced *"last month"*, and the funnel surfaced that agreement among today's news.**
⚠⚠ **EVERY PRIOR RE-SERVE WAS THE FUNNEL RE-STAMPING ITS OWN DATELINE OVER AN OLD EVENT — catchable
by asking who issued it and when. THIS ONE CANNOT BE CAUGHT THAT WAY, BECAUSE THE ISSUER AND THE
DATE ARE BOTH CORRECT AND BOTH NEW.** ⚠⚠⚠ **THE RULE THAT GENERALISES: THE DATE ON A RELEASE IS NOT
THE DATE OF EVERY EVENT INSIDE IT. Rule (iii) must be asked of the EVENT, not of the DOCUMENT —
and an earnings release is the highest-risk document for this, because its job is to recap a
quarter.** ⚠ **Expect this every earnings season, in exactly the shape that passes the existing
checks.** Caught here only because the drill asked for the agreement's **first** announcement date
rather than for its source.

⚠ **PRICED-IN: THE FOURTH STATE AGAIN — NOTHING TO FIRE ON. ZERO `move` CALLS, and the honest reason
is that both candidates died UPSTREAM OF PRICE** (`VZ` at part 1 and part 2, `GLW` at rule (iii) and
part 2). ⚠ **A `move` on either would have been DECORATIVE and was declined — the TENTH such
refusal.** ⚠ **GLW is a shape-one veteran in the priced-in defect list (−10.94%, a drawdown read as
priced-in), which makes declining the call worth stating: a candidate already dead at rule (iii)
cannot be revived by a price, and pulling one would have converted an honest absence into a fake
exercise.** ⚠ **An ABSENT check and a SKIPPED one look identical in a summary. This is the absent
kind.**

⚠ **THE CORRELATION CHECK (§4) HAD NO OPERAND AND THAT IS NOT THE SAME AS PASSING: zero open
positions means zero `driver` fields to compare against, so no candidate could have failed it. It
was not run because there was nothing to run it against.**

---

### T-2026-10-27-01 — VZ (Verizon) / Amazon Web Services — $2.0B+ AI-infrastructure fiber agreement → the unnamed optical / fiber / equipment supply tier — REJECTED (part 1 — VZ *IS* a named party, so the second-order drill asked for a THIRD company and returned **no named third party with any quantified impact**, which is rule (v); part 2 — the company's own release calls the figure the **"value of the agreement"**, assigns it to **NO reporting segment** and states **NO contract term**, so no revenue share is calculable; part 3 — no revenue-recognition date exists at any leg)

**Company A / the news:** Verizon's own release, **2026-10-26**, *"Verizon delivers another
record-breaking quarter with 3Q 2026 results"*, discloses an expanded AWS partnership as a
**"$2B+ AI infrastructure deal"** — Verizon supplying high-capacity fiber connectivity to AWS data
centres, i.e. **AWS pays Verizon.** ⚠ **Provenance PASSES cleanly: a dated, company-issued primary
release. This is not a rule (iii) failure.**
**Company B / the candidate:** none reached. The second-order question — whose optical components,
fiber, or construction revenue changes because Verizon must build this capacity — returned, verbatim:
*"no source in the available material identifies a specific third publicly traded equipment,
optical-component, fiber, or construction supplier whose revenue changes because of the AWS
agreement, with a dollar amount attributed to that company."*

**1. Mechanism:** **CANNOT BE WRITTEN.** There is no Company B to put in the sentence. Any name
would be a prior I supplied, which is the honest-broker paragraph's exact object and the 10-26
Stellantis refusal one session earlier.
**2. Dollar path:** **FAILS INDEPENDENTLY, AT THE FIRST-ORDER LEG.** ⚠ **This is rule (viii)'s
value-of-the-agreement costume, and the kill is the company's own wording.** The release says
*"valued at $2.0+ billion"* and establishes a *"commercial framework"* — ⚠ **not recognised
revenue, not bookings, and explicitly NOT assigned to a reporting segment.** No term is stated, so
even the annualised figure does not exist. Against VZ's ~$135B annual revenue, $2.0B over an
unstated multi-year term is **far under part 2's 10% floor on any reading** — and the floor is not
even reachable, because the denominator's period is undisclosed.
**3. Timing window:** **NO DATE EXISTS.** No term, no start, no recognition schedule at either leg.
**4. Invalidation:** not written — there is no thesis to invalidate.

**Hard filters:**
- Priced-in (§4): **NOT RUN — the FOURTH STATE.** Died at part 1 and part 2, upstream of price. A
  `move` would have been decorative; declined.
- Correlation (§4): **NO OPERAND** — zero open positions, zero `driver` fields.
- Universe (§3): VZ is us_equity/NYSE and far above the $10B floor — ⚠ **but §3 was never the
  binding constraint and no cap figure was pulled, so §3 is UNRESOLVED-AND-IRRELEVANT here, not
  passed. DO NOT INHERIT A §3 VERDICT FROM THIS ENTRY** (the VAL/GFS precedent).

**Outcome:** **REJECTED.** ⚠ **Worth recording because it is the day's only object that reached a
US-listed name above $10B with an official dated release behind it — and it died on the oldest
failure in this log: the headline name is buyable and the second-order tier is UNNAMED.** ⚠ **A
$2B+ fiber build must be supplied by somebody. The source would not say who, and a redaction is not
a lead.**

---

### T-2026-10-27-02 — GLW (Corning) / Verizon — 80+ million miles of optical fiber, 2027–2032 → REJECTED (rule (iii) — the agreement was announced **2026-09-08**, SEVEN WEEKS OLD, and reached today's funnel only because Verizon's new 10-26 earnings release recapped it; part 2 — **NO dollar value disclosed by either party**, only *"multi-billion dollar"*)

**Company A / the news:** Verizon's 2026-10-26 Q3 release recaps a Verizon–Corning fiber supply
agreement, jointly announced **2026-09-08**: more than **80 million miles** of optical fiber,
deliveries **2027 through 2032**. ⚠ **Verizon's own earnings call called it *"last month."***
**Company B / the candidate:** **GLW (Corning)** — US-listed, NYSE, well above the §3 floor, and a
genuinely named third party. ⚠ **This is the first time in several sessions that the funnel produced
a named, eligible, above-$10B Company B at all.**

**1. Mechanism:** writeable in one clause without an "and also" — *Verizon's fiber build causes
Corning's Optical Communications segment revenue to rise because Corning is the contracted
supplier.* ⚠ **PART 1 PASSES. That is rare in this log and is why the entry is written out rather
than swept.**
**2. Dollar path:** ⚠⚠ **FAILS ON THE MAGNITUDE HALF WHILE *PASSING* THE SEGMENT HALF — a split
this log has not recorded before and worth naming.** The segment is unambiguous: **Optical
Communications**, Q3 2026 sales **$2.379B** against consolidated core sales **$5.08B** = **~46.8%**,
⚠ **four and a half times part 2's 10% floor.** ⚠⚠ **AND THERE IS STILL NO DOLLAR PATH, BECAUSE
NEITHER COMPANY DISCLOSED A VALUE: no total contract value, no price per mile, no minimum purchase
obligation, no guaranteed revenue. *"Multi-billion dollar"* is an adjective.** ⚠ **80 million MILES
IS NOT MONEY — the UNIT failure, one session after 1 GWh did the same thing on 10-26 and two weeks
after the sovereign diesel tonnage ladder. Three instances now; the UNIT test earns its place.**
⚠ **Part 2 has two halves and this log has been recording them as one. A candidate can clear the
segment-materiality half by a factor of four and still have no dollar path at all.**
**3. Timing window:** deliveries **2027–2032**; no exact recognition date exists. ⚠ **NOT the clean
kill here — first deliveries in early 2027 would be inside §4's two quarters — but the contract's
mass sits five years out, and no dated first-revenue figure exists to size the near part.**
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **NOT RUN — the FOURTH STATE, declined as decorative** (tenth refusal). ⚠ **Named
  explicitly because GLW is a shape-one veteran at −10.94%: the filter would likely have returned
  `true` on a DRAWDOWN, and "but the filter would have blocked it anyway" is not why this was
  rejected. It died at rule (iii).**
- Correlation (§4): **NO OPERAND** — zero open positions.
- Universe (§3): us_equity/NYSE, above the floor. ⚠ **Not pulled from source and not needed — the
  kill is upstream. §3 UNRESOLVED, not passed.**

**Outcome:** **REJECTED — and it is the day's finding.** ⚠⚠ **A seven-week-old event reached a
pre-market research seat carrying a new date, a new document and a correct issuer, because an
earnings release's job is to recap a quarter. Rule (iii) must be asked of the EVENT, not of the
DOCUMENT.** ⚠ **Do not rehabilitate at a different price: nothing about the September announcement
date or the absent dollar figure moves with the quote.** ⚠ **If Corning or Verizon ever discloses a
contract value with a dated recognition start, part 1 and the segment half of part 2 are already
written and PASSING — this is the closest thing to a live standing condition in the log, and it is
still NOT a queue.**

---

### T-2026-10-27-03 — UPS Q3 2026 revenue $22.9B + raised FY guidance · Centene (CNC) FY2026 EPS floor and HBR guidance revision → REJECTED (part 1 — these are the companies' OWN RESULTS, which is not a second-order catalyst; the only Company B either offers is a competitor read-across, which is the shared-cause object)

**Company A / the news:** **UPS, 2026-10-27** — Q3 revenue **$22.9B**, FY2026 guidance raised to
~**$92.6B** revenue / **$8.75B** adjusted operating profit / **$7.28** adjusted EPS / **$6.1B**
adjusted FCF. **Centene, 2026-10-27** — GAAP EPS floor to **>$3.46**, adjusted to **>$5.20**,
health-benefits ratio cut to **90.4–91.1%**, interest expense to **$600–620M**.
**Company B / the candidate:** none exists.

**1. Mechanism:** **CANNOT BE WRITTEN.** ⚠ **A company's own print changes its own reported
numbers, not another company's revenue or cost line.** The read-across each invites — parcel peers
off UPS, managed-care peers off Centene's HBR — is the **COMPETITOR'S-EARNINGS-PRINT shared-cause
object**, the third and most respectable face of "a shared cause is not a mechanism": nobody's
economics changed, only relative standing, and **no counterparty is named in either release.**
⚠ **Both would need an "and also" in part 1, which is the designed kill.**
**2–4:** not reached.

**Hard filters:** all three **NOT RUN** — died at part 1, upstream. **No `move`, no cap pull.**

**Outcome:** **REJECTED.** ⚠ **The scan-1 "significance" framing returned these as the day's top
items. The structural framing returned neither, because neither is a transaction between two named
parties. That is the eleventh session in which the two framings disagreed in exactly this
direction.** ⚠ **Expect this shape every earnings season and kill it on part 1 each time.**

---

### T-2026-10-27-04 — FOMC two-day meeting opening 2026-10-27, decision 2026-10-28 (consensus: hold at 3.75–4.00%, 93% expect a pause, 76% expect a December hike) · 10-year Treasury +84bp YTD, 30-year +~50bp · the "AI-financing and federal deficits" market theme → REJECTED (no Company A — a government action has ONE party and no transaction; and the decision has **not happened yet**, which is rule (iii)'s purest form)

**Company A / the news:** there is none. ⚠ **A central-bank decision is the standing
GOVERNMENT-ACTION object: sector-moving, carrying numbers, naming no counterparty, with ONE
party.** The survey probabilities (93% / 76%) are the **MARKET-IMPLIED-PROBABILITY costume** the
carry-forward names as the most seductive form — a number that moved, wearing the shape of an event
with a date.
**Company B / the candidate:** none. ⚠ **A long-only book cannot trade a policy hold, and no named
party receives anything.**

**1. Mechanism:** **CANNOT BE WRITTEN — no event, no parties, no transaction.**
⚠⚠ **AND IT FAILS RULE (iii) AT THE EARLIEST POSSIBLE POINT: THE 10-28 DECISION HAS NOT HAPPENED.
The earliest possible failure of "is this new to the company's own disclosure?" is an event nobody
has disclosed because it does not yet exist.** ⚠ **The 3.75–4.00% range itself was set in
SEPTEMBER and is merely being re-reported, so the only concrete number here fails rule (iii) a
second way.** The Treasury-yield and AI-financing items are **macro aggregates** — the same object
in its plainest coat, and the source said so itself: *"not a newly announced supply agreement,
capacity decision, or regulatory action."*
**2–4:** not reached.

**Hard filters:** **NO TICKER TO RUN THEM ON.**

**Outcome:** **REJECTED.** ⚠ **The correct response is to note the date and do nothing — the 10-28
decision is for the 10-28 seat to meet, and it will be the same object then, because A CHANGE IN
STATUS IS NOT A CHANGE IN ELIGIBILITY.** ⚠ **No second ID will be minted for it tomorrow; this
entry disposes it in both states.** *(Same object as `T-2026-10-12-05`, `T-2026-10-13-08` and the
09-25/09-29/09-30/10-02 macro complex.)*

---

### T-2026-10-27-05 — §3 / unnamed-counterparty / wrong-quantity / own-results sweep of ELEVEN items — REJECTED (disposed as one, ZERO drill queries spent)

Every item below died at the first test applied. ⚠ **Named individually because a sweep that lists
no reasons is indistinguishable from a sweep that did no work.**

**Unnamed counterparty — rule (v):** **Boost Run (BRUN)**, a five-year **$525.6M** AI-cloud-services
agreement with **the customer not named.** ⚠ **A disclosed figure and a disclosed term with no second
party is not a two-party transaction.** *(Also almost certainly under the §3 cap floor; not pulled,
because the counterparty test kills it one step earlier.)*

**Party type / not US-listed — §3:** **Anthropic / "SpaceXAI"** — a reported **$120.5B** computing
arrangement where **neither leg is established as a US-listed company** and the SpaceX unit is not
separately listed ⚠ *(the largest dollar figure the funnel has ever served into this log, and
§3 does not weigh scale — the ELMT lesson in its biggest coat yet)* · **Quant Group / Chewujie** —
HK-listed, and the RMB figures are **explicitly estimates, not disclosures** · **ST Engineering** —
Singapore-listed, no customer named, no recognition date · **ADES Holding / PT Pertamina Hulu
Mahakam** **$46.2M** — not established as US-listed, no segment share, no recognition date.

**Wrong quantity — rule (viii):** **SpaceX / Apollo Global Management**, ~**$40B** — ⚠ **financing
and equipment leasing, i.e. CAPITAL, not revenue or cost savings at either leg**, and SpaceX is not
listed.

**No figure at all:** **California Nanotechnologies** — a purchase order disclosed **with no stated
value**, plus no segment share and no recognition date. *(Microcap; §3 would kill it independently.)*

**Own results — part 1:** **FirstSun Capital Bancorp** (Q3, 10-26) · **Herc Holdings** (Q3, 10-27) ·
**Alexandria Real Estate Equities** (Q3, 10-26) · **Phillips Edison** (Q3 + guidance, 10-26). ⚠ **A
company's own print is not a second-order catalyst, and the source volunteered that the snippets
"do not provide enough detail to determine whether any of these constituted a material earnings
surprise, guidance change, capacity announcement, or cross-company supply-chain event."**

⚠ **Zero drill queries spent on any of the eleven. Every kill was reachable from the scan output
plus this log.**

---

### 2026-10-26 (08:05 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$99,434.44** at
pre-flight 08:04). `clock` at **08:05:20** reads `is_open: false` with `next_open`
**2026-10-26T09:30** and `next_close` **2026-10-26T16:00** — ⚠ **both carrying TODAY's date,
which is the pre-market full-session signature. Read off the DATES, not the boolean: not a
holiday, not an early close.** Window surveyed: Friday 2026-10-23 after the close through this
morning — **a weekend window, the thinnest this routine ever screens.**

**Ledger reconciled FIRST, before any research — three sides, all agreeing.** Alpaca `positions`
= **ONE row, core VOO only** (99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999**,
unchanged since 2026-09-03) · `positions.md` satellite header `grep -cE '^### [A-Z]{1,5} '` =
**0** · `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **NO DISCREPANCY.**

**Every §6 gate open and nothing was bought — a research result, not a permission result.**
Breaker **INACTIVE**, `halt_triggered_at: none`, `new_positions_this_week` **0 of 3**, satellite
sleeve **0.0% deployed**, `control.md` Notes **EMPTY**, zero open alerts. 5% cap **$4,973.01**
against the `sleeves` 08:05 equity, **$30,000.00 idle across 35 post-fill sessions.**

**THREE BROAD SCANS PLUS ONE DRILL, THE STRUCTURAL FRAMING FIRST, THE ANNOUNCEMENT DATE DEMANDED
INSIDE EVERY PROMPT — AND THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE AGAIN IN THE TWO
SCANS THAT ASK IT DIRECTLY, PLUS THE DRILL.** Verbatim: *"the evidence supports **zero confirmed
matches**, rather than a list of likely candidates"* (segment-quantification framing) ·
*"**no second publicly traded U.S. company is named with a dollar figure attributed to it**"*
(the EQT/Range drill) · and from the overnight-events scan, the honest limit volunteered rather
than hidden: *"The available evidence is insufficient to claim that the list above is exhaustive
for the full Friday-after-close through Monday-pre-market interval."*

⚠⚠ **TODAY IS THE FIRST SESSION IN THIS LOG WHERE THE STRUCTURAL FRAMING RETURNED FOUR ITEMS AND
*NOT ONE* OF THEM WAS SELF-EXCLUDED — AND ALL FOUR DIED ANYWAY, ON THE *UNIT* AND *PARTY-TYPE*
TESTS THE 10-12 FALSE POSITIVE ADDED TO THE RULE.** The framing screens for **structure**, and
all four had it: two named parties, a date, a dollar figure. **EQT/Range** $50B+ — an
**enterprise value** · **Corxel/Amanat** $377M — **gross proceeds** · **Ovintiv/Logan** $890M —
**consideration paid out** · **Getty Images/DIP lenders** $143M — a **credit ceiling**.
⚠ **FOUR ITEMS, FOUR DOLLAR FIGURES, AND NOT ONE IS SEGMENT REVENUE AT A COMPANY B. That is
rule (viii) returning a clean sweep of a scan's entire output, which this log has not recorded
before.** ⚠ **The framing is not weakened by this — it still reached the funnel's actual
inventory, and the source named its own three near-misses unasked (High Liner/Umios Canadian ·
Axon's $22M government party · Elbit's $200M with no second named company).**

⚠ **THE MONDAY FORWARD-CALENDAR SHAPE ARRIVED ON SCHEDULE AND NO ID WAS MINTED FOR IT** — a
"weekly market insights October 26–30" item surfaced in the third scan's citations. **Disposed
already at `T-2026-10-12-05` and `T-2026-10-13-08`; the 10-14 precedent declined to mint a third
entry for one rejection and this seat declines a fourth.** It is folded into `-04` below.
⚠ **The carry-forward predicted this shape on *every* Monday pre-market seat. It was right.**

⚠ **THE RE-SERVE RATE HELD AND IT IS ONE SESSION OLD AGAIN: WELSPUN CORP CAME BACK, DISPOSED ON
2026-10-23 AT ~$730M AND RETURNING TODAY AT $580M** of coated line pipe for a US natural-gas
transportation project. ⚠⚠ **A NEW SUB-SHAPE WORTH THE LINE: the re-serves logged so far
repeated a figure *to the cent* (LS Electric's $138,458,284, RTX's $6.3B). THIS ONE CAME BACK
WITH A DIFFERENT NUMBER, which reads as a new award rather than a repeat — and the kill is
identical either way (Indian-listed, customer unnamed), so the LOG answered it and no query was
spent.** ⚠ **A changed figure is the one disguise a re-serve has not worn before. Check the
ISSUER, not the number.**

---

### T-2026-10-26-01 — EQT Corporation (EQT) / Range Resources (RRC) — $50B+ all-stock Appalachian gas merger → the unnamed midstream / gathering / service tier — REJECTED (merger arbitrage is not in §4, and the second-order drill returned a VERBATIM DENIAL; part 2 — every dollar figure in the story is an enterprise value, an exchange ratio or consideration to shareholders; part 3 — close is Q1 2027 and no revenue date exists at any third party)

**Company A / the news:** **EQT Corporation** announced on **2026-10-26** a definitive agreement
to acquire **Range Resources** in an **all-stock** transaction at an exchange ratio of **0.987
EQT shares per Range share**, creating a company with **pro forma enterprise value exceeding $50
billion**. EQT and Range holders would own approximately **73% / 27%** of the combined company
(EQT IR release and 8-K, 2026-10-26). **Reuters put the implied equity consideration at ~$12.83
billion.** ⚠ **This is by a wide margin the largest US corporate event in the window.**
**Company B / the candidate:** the Appalachian **midstream, gathering, processing and
oilfield-service tier** that would see contracted volumes consolidate under one counterparty.

**1. Mechanism (one sentence):** **cannot be written without an "and also", and the Company B
slot is empty before the sentence even starts.**
> *"EQT's acquisition of Range causes [midstream operator]'s gathering revenue to improve because
> the combined producer concentrates volumes on its system — **and also** the combined company
> renegotiates or redirects contracts that transfer unchanged at closing, **and also** that shows
> up in reported segment revenue inside two quarters."*

⚠⚠ **TWO "AND ALSO"s, AND §4 REJECTS AT THE FIRST.** ⚠⚠⚠ **BUT THE DECISIVE FACT IS NOT THE
SENTENCE — IT IS THAT THE DRILL QUERY RETURNED A VERBATIM DENIAL AND THE SENTENCE ABOVE COULD
ONLY BE COMPLETED BY *ME* SUPPLYING THE NAME.** Asked directly whether EQT's or Range's
announcement, 8-K or investor materials name any specific other publicly traded US company —
midstream, gathering, service, processing or equipment — with a dollar amount attached, the
source answered: ***"No. … no second publicly traded U.S. company is named with a dollar figure
attributed to it in the materials reflected in the available results. The available evidence
does not support identifying any directly affected third-party company with quantified
exposure."*** ⚠⚠ **THE PRIORS ARRIVED INSTANTLY AND SPECIFICALLY — the Appalachian gatherers are
a short, well-known list — AND NOT ONE IS WRITTEN DOWN HERE AS A CANDIDATE. That is rule (v) and
the honest-broker paragraph meeting on the same object: a market-structure fact about who
gathers Marcellus gas is a fact about an INDUSTRY, not a transaction.**

**2. Dollar path:** ⚠⚠ **FAILS, AND IT IS RULE (viii) SWEEPING THE WHOLE DISCLOSURE.** Three
dollar figures exist and **not one of them is revenue at any Company B**: the **$50B+ pro forma
enterprise value** is a valuation of the **combined merged entity** (rule (viii)'s wrong-quantity
shape at its largest scale yet) · the **0.987 exchange ratio** is a **share-swap term**, not money
at all · the **~$12.83B implied equity consideration** is **paid to Range's SHAREHOLDERS**, which
is neither party's revenue and is a Reuters *calculation* rather than a disclosure. ⚠ **No
segment is named, no share of revenue is computable at any third party, and no third party has a
figure.** ⚠ **The 10-21 standing fix — *ask for the figure disclosed FOR THIS TRANSACTION* — was
applied inside the drill prompt and is what separated the $50B EV from anything a part 2 could
use. Fourth consecutive session it has paid.**

**3. Timing window:** ⚠⚠ **FAILS INDEPENDENTLY, AND ON THE DEAL'S OWN STATED TIMETABLE.** The
transaction is expected to close in **Q1 2027**, subject to regulatory clearances and shareholder
approvals. ⚠ **So the earliest date on which the combined company exists at all is roughly ONE
quarter out, and any second-order effect on a gatherer's reported segment revenue is at minimum
one to two quarters BEYOND that — past §4's two-quarter ceiling before the first dollar could
move.** ⚠ **This is the merger-contingent part-3 kill the carry-forward already records against
the 10-06 pair, recurring without modification.**

**4. Invalidation:** **not written.** ⚠ **Parts 1, 2 and 3 all failed, and §4 is explicit that
failing one part ends the trade. A fourth part here would be building the roof of a house with
no foundation.**

**Hard filters** *(run BEFORE the parts, per §4):*
- **Priced-in (§4): NOT RUN, AND THE STATE IS "NO OPERAND", NOT "PASSES".** ⚠ **Both legs died at
  part 1 as named parties to the headline transaction, upstream of price. A `move` call on EQT or
  RRC would be DECORATIVE — the ninth time this log has declined one for that reason.** ⚠ **An
  ABSENT check and a PASSING one look identical in a summary; this is the absent kind.**
- **Correlation (§4): PASSES TRIVIALLY, AND THE REASON MATTERS.** Zero open satellite positions,
  so there is no `driver` field anywhere to collide with. ⚠ **An empty ledger makes this filter
  unfireable, which is not the same as a candidate that is genuinely uncorrelated.**
- **Universe (§3): NOT RESOLVED AND NOT NEEDED.** ⚠ **DO NOT INHERIT A §3 VERDICT FROM THIS ENTRY
  (the VAL precedent).** Both are US-listed common stock on the NYSE and EQT is comfortably above
  the floor, but **no market-cap figure was pulled from source**, because the thesis parts killed
  it first and §3 is not the reason it is rejected.

**Outcome:** **REJECTED.** ⚠⚠ **AND IT IS THE CLEANEST MERGER-ARBITRAGE INSTANCE THIS LOG HAS
MET, WHICH IS WHY IT IS WRITTEN OUT RATHER THAN SWEPT: §4 asks whose ECONOMICS change, and in an
all-stock merger Range's price is pinned to EQT's by a fixed ratio — the target has no economics
left of its own to change — while the acquirer is the headline name.** ⚠ **The competitor
read-across this invites (other Appalachian producers re-rating on consolidation) is the
shared-cause object in its purest form: a sector re-rating is a MARKET, not a transaction.**
⚠ **DO NOT REHABILITATE IT AT A DIFFERENT PRICE. Neither the Q1 2027 close, nor the absence of a
named third party, nor the fact that an enterprise value is not segment revenue moves with the
quote.**

---

### T-2026-10-26-02 — Audi / Volkswagen $4.2B Georgia assembly plant → the unnamed construction, equipment and supplier tier — REJECTED (part 3 — PRODUCTION IN THE EARLY 2030s, which BEATS Bayer's 2031/2034 as the record holder for the too-far-out form; part 1 — NO counterparty of any kind is named; §3 — the only named company is non-US-listed; and the announcement was made by a POLITICIAN AT A RALLY, not by the company)

**Company A / the news:** **Audi** (a **Volkswagen** subsidiary) announced a planned assembly
plant in **Georgia** — reported investment **$4.2 billion**, approximately **4,500 jobs**,
construction scheduled to begin **2027**, production **in the early 2030s** (reported
**2026-10-25**). **Company B / the candidate:** the construction, engineering, automation and
tier-one supplier base that would build and equip it.

**1. Mechanism (one sentence):** **there is no Company B to put in the slot.** ⚠⚠ **This is form
six — THERE IS NO COUNTERPARTY AT ALL — in its textbook presentation: a dollar figure, a map pin,
a headcount and a construction year, and not one contractor, engineer, equipment vendor or
tier-one supplier named anywhere.** ⚠ **It is the BDX $3B shape (Nebraska, Columbus, prefillable
syringes, and no contractor whatsoever) and the Bayer Ohio shape arriving together.** ⚠⚠ **AND
THE CARRY-FORWARD'S SHARPEST LINE APPLIES VERBATIM: A MAP PIN IS NOT A LEAD. The priors for a
greenfield auto plant are instant and specific; none is recorded here as a candidate, because
there is no Company B until the source names one.**

**2. Dollar path:** ⚠ **FAILS. The $4.2B is AUDI'S OWN CAPEX** — rule (viii)'s "capital paid out
by the non-candidate leg", and in this case paid out by a leg that cannot be bought under §3
anyway. **No portion is attributed to any named recipient; no segment exists to measure it
against.** ⚠ **A HEADCOUNT IS NOT A DOLLAR PATH** — the standing Pfizer-Sicily line, recurring.

**3. Timing window:** ⚠⚠⚠ **FAILS BY THE WIDEST MARGIN THIS LOG HAS EVER RECORDED, AND IT IS A
NEW RECORD HOLDER STATED WITH ITS PREDECESSOR NAMED SO THE ORDINAL CAN BE CHECKED: construction
begins 2027, PRODUCTION IN THE EARLY 2030s — roughly 16 to 24 quarters against §4's ceiling of
TWO.** ⚠ **The prior record was Bayer's Ohio plant at 2031/2034 (`T-2026-10-05`), and this is
further out on the production date than Bayer's earlier figure.** ⚠ **Counted against that entry
in the same breath, per the rule against stating an ordinal that was not counted from the list.**
⚠ **Part 3 kills it in ONE step, before any funnel query is spent — rule (vi) working exactly as
designed.**

**4. Invalidation:** **not written** — parts 1, 2 and 3 all failed.

**Hard filters:**
- **Universe (§3): HARD KILL AT COMPANY A.** **Volkswagen AG is listed in Frankfurt**, not on a US
  exchange as common stock; **Audi is a subsidiary, not separately buyable.** ⚠ **The source said
  so itself: *"Audi is owned by Volkswagen, a publicly traded non-U.S. company; the available
  result does not identify a second publicly traded U.S. company as counterparty."* The source
  applied the kill before I did.**
- **Priced-in (§4): NO OPERAND.** No eligible ticker exists to call it on.
- **Correlation (§4):** no open positions; unfireable.

**Outcome:** **REJECTED.** ⚠⚠ **AND THE ONE GENUINELY NEW THING HERE IS THE PROVENANCE, WHICH IS
WORTH MORE THAN THE REJECTION: THE SOURCE REPORTS THE ANNOUNCEMENT AS HAVING BEEN MADE BY
PRESIDENT TRUMP AT A CAMPAIGN RALLY.** ⚠⚠⚠ **THAT IS A NINTH REJECT FORM AND IT IS NOT ON THE
EXISTING LIST: AN ANNOUNCEMENT ABOUT A COMPANY, CARRYING A COMPANY'S DOLLAR FIGURE, THAT THE
COMPANY DID NOT ISSUE.** The seven known forms are all about what the source WITHHELD or WHEN the
money lands; the eighth (SUPN) is about what §3 permits. **This one is about WHO SPOKE.** ⚠ **A
third-party announcement of a corporate commitment has no 8-K behind it, no investor-relations
release to check a figure against, and no company on the hook for the number — so rule (iii)'s
test (*"did the source carry the company's OWN prior figure?"*) cannot even be ASKED, because the
source is not the company.** ⚠ **It would have been rejected on part 3 regardless, so this costs
nothing today. RECORD IT NOW — the next instance may be the one where every other part passes.**

---

### T-2026-10-26-03 — Samsung SDI America / Alpha Omega Power — 1 GWh energy-storage supply agreement → StarPlus Energy and the Stellantis (STLA) read-across — REJECTED (§3 — Company A is KRX-listed and the customer is not public; the disclosed quantity is 1 GWh, which is NOT MONEY — the 10-12 UNIT failure recurring; rule (iii) — the source flags the headline total as PART RE-REPORT; and the Stellantis link is a PRIOR I supplied, not a disclosure)

**Company A / the news:** **Samsung SDI** said on **2026-10-26** that its **US unit** signed an
agreement to supply **1 GWh** of energy-storage battery solutions to **Alpha Omega Power**, a US
energy-storage developer, with delivery **by December**. Including an initial agreement signed
**the prior year**, the agreements total **1.5 GWh**. Production is planned at the **StarPlus
Energy** plant in Indiana. **Company B / the candidate considered and refused:** **Stellantis
(STLA)**, StarPlus Energy's joint-venture partner.

**1. Mechanism (one sentence):** **not written as a thesis, and the reason is the point of this
entry.** ⚠⚠⚠ **THE CANDIDATE HERE WAS SUPPLIED ENTIRELY BY ME. The source names Samsung SDI,
Alpha Omega Power and a plant. It does NOT name Stellantis, does not mention the joint venture's
ownership, and attributes no dollar figure to anyone.** ⚠⚠ **"StarPlus Energy is the Samsung
SDI / Stellantis JV" is a FACT ABOUT A CORPORATE STRUCTURE — rule (v) in its cleanest form, a
market-structure fact rather than a transaction — and reaching for it is verbatim the failure
§4's honest-broker paragraph describes. IT IS WRITTEN DOWN HERE AS A REFUSED PRIOR, NOT AS A
CANDIDATE.** ⚠ **The pull was real: it is the only path in today's entire funnel output that
reaches a US-listed name above $10B, and the sleeve has been empty since inception. The answer
is still no.**

**2. Dollar path:** ⚠⚠ **FAILS ON THE UNIT, AND THIS IS THE 10-12 FALSE POSITIVE'S EXACT SHAPE
RECURRING.** The only quantity disclosed is **1 GWh** (1.5 GWh cumulative). ⚠ **A GIGAWATT-HOUR
IS NOT A DOLLAR.** The US/Russia diesel item (`T-2026-10-12-01`) died on precisely this: *"the
disclosed quantity is NOT MONEY"*, with a four-rung tonnage ladder standing in for a figure.
⚠ **The structural framing's UNIT test, added to the rule after that run, caught this one at the
first reading rather than after a mechanism had been elaborated. The fix paid.** ⚠ **No segment
is named at any leg, and no revenue share is computable for Samsung SDI, for Alpha Omega Power,
or for the JV.**

**3. Timing window:** **delivery "by December"** — genuinely **inside two quarters**, and ⚠ **a
clean pass on the one part that kills most of this log is not progress toward a trade when parts
1 and 2 and §3 have already failed.** ⚠ **Recorded because a part-3 PASS is rare enough here to
be worth the line.**

**4. Invalidation:** **not written** — §3 and parts 1 and 2 failed first.

**Hard filters** *(run BEFORE the parts, per the §3-first discipline):*
- **Universe (§3): HARD KILL ON BOTH NAMED PARTIES.** **Samsung SDI is KRX-listed** (Korea), not
  US-listed. **Alpha Omega Power is not established as publicly traded** anywhere — the source
  says only *"a U.S. energy-storage developer"*. ⚠ **So the two parties to the transaction are a
  non-US issuer and a private company, and the only US-listed name in the vicinity is one the
  source never mentions.**
- **Rule (iii): the source flagged the re-report itself, unasked.** Verbatim: *"the combined total
  includes an **initial contract signed last year**; only the latest 1 GWh agreement is new."*
  ⚠ **The 1.5 GWh headline is the aggregate-spanning-a-previously-announced-deal shape — Venture
  Global's $17.2B and Amkor's $3B, now in gigawatt-hours. Asking for the figure disclosed FOR
  THIS TRANSACTION is what separated the new 1 GWh from the 1.5 GWh total.**
- **Priced-in (§4): NO OPERAND** — no eligible ticker reached the filter.
- **Correlation (§4):** no open positions; unfireable.

**Outcome:** **REJECTED.** ⚠ **Three independent kills (§3 at both parties, part 2 on the unit,
rule (iii) on the headline total), and a fourth standing behind them: the only route to a buyable
name runs through a JV ownership fact the disclosure never mentions.**

---

### T-2026-10-26-04 — §3 / wrong-quantity / wrong-transaction / government-counterparty / disposed-repeat / forward-calendar sweep of SEVENTEEN items — REJECTED (disposed as one, ZERO drill queries spent)

⚠ **Disposed from the scans' own output and from this log, without spending a query on any of
them.** The sweep is written as one entry rather than seventeen because each kill is a single
step and minting an ID apiece would inflate the thesis count without recording anything.

**Wrong transaction type / rule (viii) — a dollar figure that is not segment revenue at a
Company B:**
- **Corxel Pharmaceuticals / Amanat Acquisition Corp (AMAN)** — ~**$377M gross proceeds** from a
  SPAC business combination (~$75M trust + ~$300M PIPE). **Capital paid IN**, rule (viii)'s first
  listed shape; Corxel is not US-listed; **a SPAC is far below §3's $10B floor.**
- **Ovintiv (OVV) / Logan Energy (LGN)** — ~**US$890M** acquisition including assumed net debt.
  **Merger arbitrage, not in §4**; consideration **paid OUT** by the only US-listed leg; Logan is
  **TSX Venture**-listed. Three kills, no query.
- **Getty Images / its DIP lenders** — **up to $143M** Chapter 11 debtor-in-possession financing,
  $85M drawn 2026-10-23. **A FINANCING CEILING** (rule v's ceiling sub-shape crossed with rule
  viii), the lenders are **unnamed**, and Getty is far below the §3 floor. ⚠ *A DIP facility is
  the clearest "money moving in the wrong direction" object this funnel has produced.*
- **MKS/TTM-style consideration items aside, the pattern across all four of the structural scan's
  returns is one finding, recorded above in the survey header, not four.**

**§3 — not US-listed, or below the floor:**
- **High Liner Foods / Umios** — **Canadian**, consideration in **C$**. *The source excluded it
  before I did.*
- **Welspun Corp** — **$580M** coated line pipe for a US natural-gas transportation project.
  **Indian-listed (NSE/BSE)**, customer **unnamed**. ⚠ **A ONE-SESSION-OLD RE-SERVE WITH A
  CHANGED FIGURE** — see the survey header; the log answered it and no query was spent.
- **KEC International** — **₹2,872 crore** award from **Power Grid Corporation of India**, a
  **government-controlled** counterparty. Indian-listed. ⚠ *KEC's third appearance in this log
  (10-12, 10-14, today) — rule (iv): a recurring ticker is a warning, not corroboration.*
- **Vection Technologies** — **$1.4M**, **ASX**-listed, client **unnamed**. Jointly unsatisfiable.
- **Elbit Systems (ESLT)** — **$200M** Asia-Pacific airborne defence contracts. **Israeli issuer**;
  and *"does not identify a second named company"* — the source's own words.
- **Cemex** — Mexican issuer; a Q3-disclosed supply agreement with **no announcement date and no
  counterparty named**. Not confirmable as a first-time announcement in the window.
- **6K Additive / ADDMAN** — a **30-month nickel-powder supply agreement** and a Burgettstown
  expansion to 6,000 t by end-2027. **6K is private, ADDMAN is private**, Q3 revenue **$7.2M** —
  ⚠ **part 2's 10% test and §3's $10B floor are JOINTLY UNSATISFIABLE, the free one-step screen.**
  ⚠ *Its capex guidance cut ($11–12M → $10–11M) is a clean rule (iii) PASS against its own prior
  range — and a clean pass on one filter is not progress toward a trade.*
- **StandardAero / TAROM** — a PW127M engine-support agreement, **2026-10-26**, with **no
  transaction value and no revenue-recognition timing.** Part 2 unwriteable.

**Government action / no Company A:**
- **Axon Enterprise (AXON)** — **$22M** Reno surveillance approval. **Government counterparty**;
  and $22M against AXON's revenue base is jointly unsatisfiable on part 2.
- **West Virginia Public Service Commission** — proposed rules for power-plant capacity. ⚠ **A
  government action is not a Company A — ONE party, no transaction.** *The source excluded it
  itself on the company-announcement requirement.*

**Own results / aggregate backlog — no transaction, no named second party:**
- **Alphabet (GOOGL)** — Google Cloud's **$514B backlog**, slightly more than half expected to be
  recognised over 24 months. ⚠⚠ **AN AGGREGATE BACKLOG IS NOT A TRANSACTION AND NAMES NO CUSTOMER
  — and it is the largest number this funnel has ever returned, which makes it the most persuasive
  non-event of the day rather than the most promising one. SCALE MAKES IT MORE CONVINCING, NOT
  LESS.** *The source applied the kill: "this is an aggregate backlog, not the value of a specific
  newly announced transaction."*
- **ServiceNow (NOW)** — **123 deals above $1M net new ACV**. A count, not a named transaction;
  no customer, no per-deal value, no recognition timing.
- **Atlas Energy** — bridge facility closed **2026-10-22** and reimbursement agreements announced
  **2026-09-25**. ⚠ **BOTH OUTSIDE THE WINDOW — rule (iii), and the source supplied both dates
  unasked.**

**The forward calendar:**
- **"Weekly market insights, October 26–30, 2026."** ⚠ **The Monday shape, predicted by the
  carry-forward and arriving on schedule. NOTHING HAS HAPPENED YET — rule (iii) at its earliest
  possible failure point. Already disposed at `T-2026-10-12-05` and `T-2026-10-13-08`; NO NEW ID
  MINTED, per the 10-14 precedent. Note the dates and do nothing.**

**Outcome:** **ALL SEVENTEEN REJECTED.** ⚠ **Zero drill queries spent on any of them — every kill
came from the scans' own output or from a `grep` of this log.**

---

### 2026-10-23 (08:03 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$99,378.54** at
pre-flight). `clock` at **08:03:12** reads `is_open: false` with `next_open` **2026-10-23T09:30**
and `next_close` **2026-10-23T16:00** — **both carrying TODAY's date, which is the pre-market
full-session signature. Read off the DATES, not the boolean: not a holiday, not an early close.**
Window surveyed: the 2026-10-22 regular session and the overnight into 2026-10-23.

**Ledger reconciled FIRST, before any research — three sides, all agreeing.** Alpaca `positions`
= **ONE row, core VOO only** (99.046311231 sh @ **706.74**, `cost_basis` **$69,999.989999**,
unchanged since 2026-09-03) · `positions.md` satellite header `grep -cE '^### [A-Z]{1,5} '` = **0**
· `sleeves` `satellite.count: 0`, `value: 0`, `pct: 0.0`. **NO DISCREPANCY.**

**Every §6 gate open and nothing was bought — a research result, not a permission result.**
Breaker **INACTIVE**, `halt_triggered_at: none`, `new_positions_this_week` **0 of 3**, satellite
sleeve **0.0% deployed**, `control.md` Notes **EMPTY**, zero open alerts. 5% cap = **$4,968.85**,
**$30,000.00 idle across 34 post-fill sessions.**

**THREE BROAD SCANS, THE STRUCTURAL FRAMING FIRST, THE ANNOUNCEMENT DATE DEMANDED INSIDE EVERY
PROMPT — AND THE FUNNEL ANSWERED §4's QUESTION IN THE NEGATIVE AGAIN, OUT LOUD, IN ALL THREE.**
Verbatim: *"The available results do not establish any qualifying item involving two named
corporate entities where both parties are companies and a disclosed dollar amount is tied to the
agreement"* · *"No company can be confirmed to meet all of the stated criteria from the available
reporting"* · *"The available sources provide no qualifying example in which a second publicly
traded company was both explicitly identified as directly affected in its revenue or cost lines
and assigned a dollar amount."*

⚠ **THE STRUCTURAL FRAMING PAID AGAIN AND THIS TIME IT PAID IN A TABLE: EIGHT ITEMS RETURNED AND
EIGHT SELF-EXCLUDED, WITH A NAMED FAILURE AGAINST EACH** — six of the eight excluded for a
**government or municipal counterparty** (Albany International/US govt $21.2M · Long Wall/MDA
$75M · Smith-Midland/Stafford County $2.2M), a **wrong transaction type** (IPM/ATD acquisition;
Foremost/Denison property consideration), or **no dollar amount at all** (Seatrium/Karpowership;
Cheniere/QatarEnergy). **Work the run would otherwise have done itself, for zero follow-up
queries.** ⚠ **A self-exclusion is a HINT, NOT A RULING** — each was re-checked, and this time
every one held.

⚠ **AND THE SECOND FRAMING EARNED ITS PLACE FOR ITS USUAL REASON: it stated the part-2 gap
outright on the day's largest named order** — Welspun's ~$730M US line-pipe win came back with
*"the customer was not named in one report"* and no segment attribution, **the source applying
two kills before I did.**

**ONE DRILL QUERY SPENT, ON THE ONE ITEM THAT DESERVED IT** (`T-2026-10-23-01`). Four of the
day's items carry a **clean rule (iii) pass** — Lockheed's own revenue outlook moved from its own
**$79.75–81.75B to $80–82B** and EPS from its own **$29.95–30.65 to $30.35–30.75**; Bloom Energy's
adjusted EPS from its own **$2.55–2.85 to $3.10–3.40** — ⚠ **and a clean pass on rule (iii) is not
progress toward a trade when part 1 has no Company B to name.** P&G **maintained** FY27 targets,
which is reaffirmation, costume #1.

---

### T-2026-10-23-01 — Lockheed Martin (LMT) 850-aircraft F-35 framework + raised FY2026 guidance → the unnamed F-35 supplier base — REJECTED (part 1 — NO Company B is named and the source says so on request; part 3 — the framework is contingent on CONGRESSIONAL AUTHORIZATION AND APPROPRIATIONS with NO first-delivery or first-revenue date in existence; rule (viii) NEW COSTUME — the only dollar figure in the story is Lockheed's own commitment to **SELF-FUND** $7B; and the framework's total value is **NEVER DISCLOSED AT ALL**)

**Company A / the news:** Lockheed Martin and the US Department of War announced a **10-year
framework agreement covering at least 850 US F-35 aircraft**, initial spares, 10 years of
modification kits and sustainment, and international orders across **Lots 21–30**, at an announced
production rate of **156 aircraft per year** (LMT release and DoW release, both **2026-10-22**;
`f35.com`, `globalsecurity.org`). In the same Q3 release LMT **raised its own FY2026 revenue
outlook to $80–82B from its own prior $79.75–81.75B** and EPS to **$30.35–30.75 from $29.95–30.65**.

**Company B / the candidate:** none. **That is the finding, not a gap in the research.**

**1. Mechanism (one sentence):** ❌ **CANNOT BE WRITTEN.** The drill asked the primary sources
directly whether any publicly traded supplier is named with a dollar amount attributed to it, and
the answer was a **verbatim denial**: *"No publicly traded supplier company or named supplier
reporting segment is identified in the cited primary releases … it does not name a supplier company
or assign any dollar amount to one."* ⚠⚠ **THE PRIORS WERE INSTANTLY READY AND SPECIFIC — RTX
(Pratt & Whitney F135), Northrop Grumman (centre fuselage), L3Harris, Honeywell, BAE Systems —
AND NO GUESS WAS MADE AND NONE IS RECORDED AS A CANDIDATE.** This is **rule (v)** in its plainest
form: *"sole producer on the F-35 programme"* is a fact about an **industry**, not a **transaction
disclosed on 2026-10-22**. ⚠ **The source left the blank; filling it in is not research.**
⚠ **Rule (iv) rides on top for the one prior that arrives loudest: RTX would be its SEVENTH
appearance in this log, and it has died at part 1 all six previous times.**

**2. Dollar path:** ❌ **NOT CALCULABLE AT ANY COMPANY B, AND NOT CALCULABLE AT COMPANY A EITHER.**
⚠⚠ **THE SOURCES DISCLOSE NO TOTAL DOLLAR VALUE FOR THE 850-AIRCRAFT FRAMEWORK — none, at the
headline name, in a deal covering a decade of production.** The one big number in circulation,
**$7 billion**, is the DoW release's statement of *"Lockheed Martin's commitment to self-fund at
least $7 billion in unspecified F-35-support initiatives"*, and the source named the defect
itself: *"The $7 billion is therefore not a supplier allocation or disclosed segment revenue
figure."*
⚠⚠⚠ **NEW RULE (viii) COSTUME, AND IT IS THE FIRST *SELF-FUNDING COMMITMENT* ON THAT LIST: A
DOLLAR FIGURE THE BUYABLE LEG PROMISES TO SPEND ON ITSELF, WITH NO NAMED RECIPIENT ANYWHERE.** It
is rule (viii)'s wrong-direction shape crossed with rule (v)'s unnamed-supply-base: the money
leaves Lockheed, and the tier it lands in is exactly the tier the release declines to name.
⚠ **It is distinct from the nearest prior entries — GEHC's $945M went OUT to a named private
seller; AMD/Fermi's backstop was a contingent liability with no figure; Royal Caribbean's ~$3B was
capex. This one is an UNDERTAKING TO SPEND, unallocated, and it reads as a measure of programme
commitment, which is why it is the number that gets quoted.**

**3. Timing window:** ❌ **FAILS, AND IT FAILS HARDER THAN ANY PRIOR INSTANCE ON THIS LIST.**
The sources state the framework *"remained subject to congressional authorization and
appropriations, and the parties still had to finalize contract terms, pricing, and delivery
schedules"*, and — asked directly — that **no first-delivery date and no first-revenue date is
stated in the cited primary materials at all.**
⚠⚠ **THIS IS RULE (vi)'s PENDING-DEFINITIVE-AGREEMENT SHAPE WITH THE GATE MOVED FROM A
COUNTERPARTY TO A LEGISLATURE, WHICH IS STRICTLY WORSE: CRK/SOCAR at least had two parties able to
sign. Here the authorising body has not voted, the pricing does not exist, and the schedule does
not exist.** ⚠ **A 10-year framework running Lots 21–30 is ~40 quarters of horizon against §4's
TWO, and part 3 kills it in one step before any Company B question is reached.**

**4. Invalidation:** ❌ **not reachable** — there is no position to invalidate.

**Hard filters:**
- **Priced-in (§4): NOT RUN, AND DELIBERATELY SO. ZERO quotes pulled, on LMT or on any of the five
  supplier priors.** ⚠ **There is no ticker to price, because part 1 produced no Company B. Pulling
  a quote on RTX or NOC here would be inventing the candidate and then pricing it, in that order.
  DECLINING TO LOOK IS STRONGER THAN LOOKING AND RESISTING.**
- **Correlation (§4): no operand** — zero open satellite positions, so no `driver` field exists to
  collide with. ⚠ **Recorded as ABSENT, not as PASSING.**
- **Universe (§3): UNRESOLVED, NOT PASSED.** No market cap was pulled for LMT or for any prior,
  because §3 is never reached on a candidate that does not exist. ⚠ **DO NOT INHERIT A §3 VERDICT
  FROM THIS ENTRY (the VAL precedent).**

**Outcome:** **REJECTED — three independent kills, and the most useful one is the LAST one anybody
would reach for.** ⚠⚠ **THE LESSON IS THE 10-15 TSMC SPLIT ARRIVING IN A SHARPER FORM: APPLY RULE
(iii) TO THE FIGURE THE MECHANISM ACTUALLY RUNS ON. On 10-15 the figure that moved (TSMC revenue)
had no supplier chain and the figure with the supplier chain (capex) did not move. HERE THE FIGURE
WITH THE SUPPLIER CHAIN — the framework's total value — WAS NEVER DISCLOSED IN THE FIRST PLACE, so
there is nothing to test rule (iii) against. A reader who tests the release, finds a clean pass on
the guidance range, and stops, proceeds on a number no supplier touches.**
⚠ **And this is the second-strongest-looking object §4 has met after GFS/TSMC: a real agreement, a
named counterparty, a dated announcement, a famous programme, a quantity (850 aircraft, 156/yr),
a genuine rule (iii) pass on the guidance, and a $7B figure in the headline. IT HAS NO COMPANY B,
NO DEAL VALUE AND NO DATE. The rules stopped it; the judgment did not have to.**
⚠ **DO NOT REHABILITATE IT WHEN CONGRESS APPROPRIATES. Appropriation would fix part 3's GATE and
change NEITHER the missing Company B nor the missing deal value — and a Lots 21–30 delivery
schedule cannot come inside two quarters however it is funded.**

---

### T-2026-10-23-02 — Lam Research (LRCX) component shortage delaying $300–400M of deliveries → the unnamed component supply base / the AMAT-KLA read-across — REJECTED (part 1 — the suppliers are UNNAMED and the only reachable Company B is a competitor, which is the shared-cause object; rule (viii) — the disclosed figure moves in the WRONG DIRECTION and §3 permits only the long side)

**Company A / the news:** Lam Research's **2026-10-22** results carried a record quarter with a
weaker near-term shipment outlook, because **component shortages were expected to delay
approximately $300–400 million of deliveries into March** (`hdfcsky.com` earnings wrap,
`bigmoves` 10-22).

**Company B / the candidate:** attempted two ways, dead both ways.

**1. Mechanism (one sentence):** ❌ **CANNOT BE WRITTEN IN EITHER DIRECTION.**
**(a) Upstream — the component makers.** ⚠ **THE SOURCE NAMES NO COMPONENT, NO CATEGORY AND NO
SUPPLIER: it says "component shortages" and stops.** That is rule (v)'s unnamed-supply-base with
*less* to work with than the $1.7B-of-"memory components" instance, which at least named a
category. **There is no Company B until the source names one.**
**(b) Across — AMAT, KLA.** ⚠⚠ **THIS IS THE SHARED-CAUSE OBJECT AND IT IS THE SHARE-SHIFT
COSTUME: a competitor's delivery slip improves nobody's revenue or cost line in any disclosed,
dateable way — it changes only relative standing, and the WET-process tools LRCX ships are not
the deposition or metrology tools AMAT and KLA ship, so there is not even a substitution story
without an "and also".** ⚠ **This is the 10-02 Nike sub-shape (*an earnings miss is not a
second-order catalyst*) arriving as a DELIVERY miss rather than a demand miss. Kill it on part 1
each time.**
**(c) And the honest third reading points DOWN, which §3 forbids expressing.** The parties whose
economics genuinely change are LRCX's **customers**, who receive tools a quarter late — and that
is a cost and a delay, not an improvement, at names nobody disclosed. ⚠ **This is the 10-08 SUPN
shape: the mechanism is sound and points the wrong way, and §3 permits only the long side. THE
TEMPTING MOVE IS TO FLIP IT INTO A "COMPETITOR BENEFITS" LONG, WHICH IS (b). NOT TAKEN.**

**2. Dollar path:** ❌ **the $300–400M is LRCX's OWN deferred revenue, at Company A, and it is
deferred rather than lost** — the source says *"delayed … into March"*. ⚠ **A figure that moves
between two of Company A's own quarters is not a dollar path at any Company B.**

**3. Timing window:** not reached. (⚠ **Worth noting it is the one part that would have PASSED —
"into March" is inside two quarters. A single passing part is not a candidate, and this is the
cheapest possible illustration of why §4 requires all four.**)

**4. Invalidation:** ❌ not reachable.

**Hard filters:** ⚠ **NONE RUN — zero quotes pulled on LRCX, AMAT or KLA.** Part 1 produced no
Company B, and a priced-in check on a name reached only by a share-shift story is a filter applied
to a thesis that was never eligible for one. **§3 and correlation: no operand.**

**Outcome:** **REJECTED at part 1, twice over, and the second reading is the one worth keeping.**
⚠ **A DISCLOSED DOLLAR FIGURE ATTACHED TO A NAMED LARGE-CAP'S NAMED PROBLEM IS NOT A SECOND-ORDER
CATALYST WHEN THE FIGURE IS THE PROBLEM'S SIZE RATHER THAN SOMEBODY'S REVENUE.** It arrives
carrying precision, a date, a specific operational cause and a mechanism that genuinely holds —
and every one of those features is about Company A.

---

### T-2026-10-23-03 — BioNTech (BNTX) / Gilead Sciences (GILD) — pumitamig + Trodelvy into Phase 3 Rosetta Breast-01 — REJECTED (part 3 — a Phase 3 BREAST-CANCER TRIAL is ~8–20 quarters against §4's two, and rule (vi) names clinical collaborations explicitly; part 2 — NO dollar amount reported at either leg; and the arrangement is a COST to both parties, not revenue to either)

**Company A / the news:** BioNTech and Gilead announced on **2026-10-22** that they are advancing
**pumitamig** in combination with Gilead's **Trodelvy** into the **Phase 3 Rosetta Breast-01**
trial. **BioNTech sponsors and leads the study; Gilead supplies the antibody-drug conjugate**
(`eoption` 10-22 market review).

**Company B / the candidate:** Gilead Sciences (GILD) — **and it is worth saying plainly that this
is the ONLY item in the entire day's funnel inventory where two publicly traded companies are both
named and a supply relationship between them is disclosed.** The source confirmed it in those
terms: *"Yes. Gilead Sciences was explicitly named as the supplying company."* ⚠ **It is therefore
the day's only candidate that gets past the structural screen at all — and it dies on the parts.**

**1. Mechanism (one sentence):** *"BioNTech's Phase 3 Rosetta Breast-01 trial causes Gilead's
Trodelvy supply volumes to rise because Gilead supplies the ADC for the combination arm."*
⚠ **The sentence stands up without an "and also", which is more than most entries in this log
manage — AND IT IS A SENTENCE ABOUT CLINICAL-TRIAL SUPPLY, which is a cost recovery at best and is
not a product sale.** Trial-supply volumes for one Phase 3 arm are not a commercial revenue line.

**2. Dollar path:** ❌ **FAILS ABSOLUTELY. No dollar amount is reported, by either company, for
either leg** — the source stated it: *"the source did not state a direct revenue or cost-line
impact for either company"* and *"No dollar amount reported."* ⚠ **Trodelvy sits inside Gilead's
oncology franchise; even the most generous reading of one trial arm's drug supply is immaterial
against GILD's ~$28B of annual revenue, and §4's floor is 10% of TOTAL revenue. The part-2 test
is not close — it is not even calculable, because there is no numerator.**

**3. Timing window:** ❌ **FAILS, AND IT IS THE PRIMARY KILL.** A Phase 3 oncology trial that is
only now being *entered* reports in **years, not quarters** — enrolment, then treatment, then
progression-free-survival readout. ⚠⚠ **RULE (vi) NAMES THIS EXACT OBJECT: *"CLINICAL
COLLABORATIONS (SMMT/AZN)"* are the regulatory version of long-dated offtake in a lab coat. SMMT/AZN
is the standing precedent and the answer was already written before the query ran.** ⚠ **Nothing
about this appears in either company's reported results inside two quarters, and the thing that
*would* eventually move — Trodelvy's commercial label — depends on a readout that does not exist.**

**4. Invalidation:** ❌ not reached.

**Hard filters:** ⚠ **NOT RUN. §3 was NOT resolved and no market cap was pulled for either leg** —
part 3 killed it in one step, before §3 was needed, which is the §3-first discipline running in the
only direction it is allowed to run (a cheaper kill first is not a §3 pass). ⚠ **No quote pulled on
BNTX or GILD. DO NOT INHERIT A §3 VERDICT FROM THIS ENTRY.**
**Correlation: no operand** — zero open positions.

**Outcome:** **REJECTED — part 3 primary, part 2 independently.** ⚠⚠ **THE REASON THIS ENTRY IS
WORTH ITS LENGTH: it is the shape the whole funnel has been failing to produce for fifteen
consecutive sessions — TWO NAMED US-LISTED PUBLIC COMPANIES ABOVE $10B, A DISCLOSED SUPPLY
RELATIONSHIP BETWEEN THEM, A DATED ANNOUNCEMENT AND A MECHANISM SENTENCE THAT NEEDS NO SECOND
CLAUSE — and the calendar kills it anyway.** ⚠ **That matters for the standing argument about the
§4 bar: the binding constraint here was NOT disclosure practice and NOT the evidence bar. It was
part 3, a rule no amount of widening would touch. Widening the evidence bar would not have bought
this trade.**

---

### T-2026-10-23-04 — §3 / wrong-counterparty / wrong-transaction / disposed-repeat / own-results sweep of TWENTY-ONE items — REJECTED (disposed as one, ZERO drill queries spent)

**One entry for twenty-one items, each dead on a filter that needs no mechanism, no query and no
quote.** ⚠ **A separate ID for each would inflate the thesis count and record nothing; the §4 work
is in `T-2026-10-23-01` through `-03`.**

**(a) GOVERNMENT OR MUNICIPAL COUNTERPARTY — one party, no transaction between companies (6):**
**Albany International** / US govt, $21.2M IBAS contract plus >$36M of its own investment (10-22;
also ~$1B cap, below the §3 floor) · **Long Wall** / Missile Defense Agency, $75M award plus $75M
of its own private capital (10-22) · **Smith-Midland** / Stafford County, Virginia, $2.2M
SlenderWall (10-22; microcap) · **Raytheon (RTX)**, a contract modification *raising the ceiling by
$394M* (10-22) — ⚠ **RULE (iv), SEVENTH APPEARANCE IN THIS LOG, AND RULE (v)'s CEILING SUB-SHAPE
ON TOP OF A GOVERNMENT COUNTERPARTY. Dead at part 1 for the seventh time, same rung, same reason.
A fresh award is not fresh evidence when the kill is structural** · **Lockheed Martin**'s F-35
framework in its government-action aspect (drilled separately at `-01`) · **Saab**'s Ukraine
fighter-jet order (also Stockholm-listed).
**(b) §3 — NOT US-LISTED, OR BELOW THE $10B CAP FLOOR (7):** **Zymeworks / Roche** — ⚠ **the
day's most complete-looking disclosure, $55M upfront + $40M Phase 1b + up to $718M milestones +
tiered royalties on ZW209, announced 10-23, and BOTH LEGS FAIL §3: ZYME is ~$1.5B against a $10B
floor and Roche is SIX-listed. §3 does not weigh outcomes (the ELMT precedent), and this is the
cheapest possible instance — one number at each leg, before any mechanism** · **Welspun Corp**,
~$730M (₹5,500 crore) US line-pipe order, India-listed, **and the customer unnamed** ·
**KEC International**, ₹1,006 crore of new orders, India-listed — ⚠ **DISPOSED-REPEAT, AND THE
RE-SERVE RATE HOLDS: KEC was disposed on 10-12 at ₹1,030 crore and is back with a FRESH FIGURE and
a fresh 10-23 dateline, order values and customers undisclosed both times. Reading the log before
the tape cost one grep** · **Seatrium / Karpowership**, Singapore-listed, no dollar amount ·
**Electro Cable Egypt**, >$16M supply order · **Foremost Lithium / Denison Mines**, $650k · **MSA
Safety**, a five-year purchase agreement *up to $10.6M* with an **unnamed** "major Northeast US
utility" (10-22) — ⚠ **rule (v): the counterparty is described, dated and sized, and not named.**
**(c) WRONG TRANSACTION TYPE / WRONG DIRECTION (2):** **Intelligent Protection Management /
Advanced Technology Distributors**, *up to $2.7M* — a purchase price paid BY the listed leg ·
**GM**-led **$108M** round into **Peak Energy** (sodium-ion storage, 10-23) — ⚠ **rule (viii):
capital paid OUT by the only buyable leg, into a PRIVATE recipient. The Brookfield/Bloom and
Tesla/$30B shape.**
**(d) OWN RESULTS, NO TRANSACTION, NO NAMED SECOND PARTY (4):** **P&G** Q1 beat ($23.28B vs
$22.80B est.) — ⚠ **and it MAINTAINED FY27 targets (1–3% organic, ~$7 core EPS), which is rule
(iii) costume #1, REAFFIRMATION; the raw-material, energy and freight headwinds it cited name
nobody** · **Omnicom** Q3 beat ($2.73 vs $2.67; revenue $6.42B vs $6.21B, +59.1% y/y on the IPG
combination) — ⚠ **measured against CONSENSUS, not its own prior figure** · **Bloom Energy**,
adjusted EPS guidance raised to **$3.10–3.40 from its own $2.55–2.85** (10-23) — ⚠ **a CLEAN rule
(iii) PASS on its own prior range, and dead at part 1 anyway: own results, no transaction, no named
second party, and its suppliers are unnamed. Rule (iv) second appearance (10-13, LS Electric).
A CLEAN PASS ON ONE FILTER IS NOT PROGRESS TOWARD A TRADE** · **Lam Research** in its own-results
aspect (reached separately at `-02`).
**(e) REGULATORY DECISION, NO SECOND PARTY, NO SUPPLIER (3):** **Aardvark Therapeutics** — FDA
lifted the clinical hold on **ARD-101** (10-22) · **Arbutus Biopharma** — FDA removed the hold on
**AB-101** (10-22) · **Biohaven** — FDA accepted the resubmitted NDA for **Vyglxia** (10-22).
⚠ **All three are microcaps, all three name no second company and no external supplier, and the
rule (vii) answer is already written: a clinical-hold lift creates no new manufacturing and no new
supplier — the drug was already being made. These are the 10-08 SUPN item with the SIGN REVERSED
(a hold lifted rather than imposed), which makes them long-expressible and changes nothing else.**
**(f) LONG-DATED ENERGY OFFTAKE (1):** **Cheniere Energy / QatarEnergy** — LNG purchase agreements
for **4 million tons annually through 2054** (10-23). ⚠ **NO DOLLAR AMOUNT DISCLOSED; the
quantity is a VOLUME AND A TERM, not money — which is `T-2026-10-12-01`'s unit defect arriving
again. Part 3 kills it without a query: a contract running to 2054 is ~112 quarters against §4's
two. QatarEnergy is state-owned, so the party-type test fails too, and Cheniere is the headline
name.** ⚠ **Rule (vi) calls long-dated energy offtake a standing FEATURE of this funnel, not a
visitor — Venture Global three times, and this is the same object with a longer tail than any of
them.**

**Outcome:** **REJECTED, all twenty-one, zero drill queries spent and zero quotes pulled.**
⚠ **Where a §3 or part-3 kill landed first, NO OTHER FILTER WAS RESOLVED, and none of these may be
read later as having passed anything.**

---

### 2026-10-22 (08:07 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, all exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$99,723.50** at
pre-flight). `clock` at **08:07:02** reads `is_open: false`, `next_open` **2026-10-22T09:30**,
`next_close` **2026-10-22T16:00** — **both carrying TODAY's date: the pre-market full-session
signature, read off the DATES and not the boolean. Not a holiday, not an early close.** Window
screened: **the completed 2026-10-21 session and the overnight into Thursday — ONE TRADING DAY.**
**Four broad scans plus three drills, all exit 0. FOUR theses, ALL FOUR REJECTED.**

**⚠⚠⚠ THE FUNNEL FINALLY PRODUCED THE OBJECT IT HAS BEEN MISSING FOR FIVE WEEKS, AND THE RULES STILL
STOPPED IT. READ `T-2026-10-22-01` BEFORE ANYTHING ELSE IN THIS ENTRY.** Amkor's **own IR release**
(`ir.amkor.com`, dated **2026-10-21**) discloses a **$1.3 billion** NVIDIA agreement — **a primary
source, a named counterparty, a dated announcement, and a dollar figure attributed to the buyable leg
BY THE BUYABLE LEG.** ⚠ **That is the exact object the segment-quantification framing has reported
absent for SEVENTEEN consecutive sessions.** ⚠⚠ **IT DIED ON PART 2 ANYWAY, ON THE RELEASE'S OWN
WORD: the $1.3B is `prepayments`, which is rule (viii)'s JBL shape — CAPITAL PAID IN BY THE CUSTOMER,
not segment revenue at Company B.** ⚠ **AND IT WAS NEVER A §4 CANDIDATE TO BEGIN WITH: Amkor is the
NAMED COUNTERPARTY — the headline name §4's opening sentence says not to chase.**

**⚠⚠ THE STRUCTURAL FRAMING WON AGAIN — SEVEN CONSECUTIVE SESSIONS — BUT TODAY IT WAS THE *WEAKER* OF
THE TWO SCANS, WHICH IS NEW AND WORTH THE HUMAN'S ATTENTION.** Scan 1 (structural: two named parties +
a disclosed amount) returned **four items, three of them disposed rejects**, and **never mentioned
Amkor at all.** Scan 2 (the routine's own Step 5a "significance" voice) returned the usual earnings
prints and macro — **but it was scan 2 that surfaced the Meta capex figure**, and the Amkor disclosure
was reached only by **drilling the NVIDIA/Samsung Electro-Mechanics item that scan 1 had killed on a
missing dollar amount.** ⚠⚠ **THE LESSON IS NOT THAT THE STRUCTURAL FRAMING FAILED — IT IS THAT A
SCAN'S *SELF-EXCLUSION* IS A HINT AND NOT A RULING, WHICH THIS FILE ALREADY SAYS (Bloom Energy,
10-13), AND TODAY IS ITS STRONGEST INSTANCE: scan 1 excluded NVIDIA/SEMCO for having no disclosed
figure, and the drill behind that exclusion found a $1.3B primary-sourced figure at a DIFFERENT,
US-LISTED counterparty in the same initiative.** ⚠ **DRILL THE EXCLUSIONS, NOT JUST THE PASSES.**

**⚠⚠ DISPOSED-REJECT RE-SERVE AT FOUR CONSECUTIVE SESSIONS, AND READING THE LOG FIRST SAVED THREE
DRILLS TODAY.** Scan 1's four results included **Apple/Perryman** (disposed yesterday, `T-2026-10-21-04`,
private), **Micron/Indium** (disposed yesterday, `T-2026-10-21-02`, and the source itself dated it
**10-20**, outside the window) and **Northrop Q3** (disposed 10-20, `T-2026-10-20-03`). ⚠ **No new IDs
minted, per the 10-14 precedent. One `grep` of this file, three drills saved.**

**⚠⚠ THE SEGMENT-QUANTIFICATION FRAMING VOLUNTEERED THE ABSENCE FOR THE SEVENTEENTH CONSECUTIVE
SESSION — 09-29 → 10-22 UNBROKEN.** Verbatim: *"No winning company in the available October 21–22,
2026 results disclosed both (1) the award's value specifically within its own reported business
segment and (2) that segment's share of total revenue."* ⚠ **All five items it returned were US
defence program awards — the standing item's FIFTEENTH instance of that shape (Lockheed F-35 framework
with no value and pricing not formalised · Karman $218M · Cherokee Nation Government Solutions $99.3M ·
Leidos $160M · CACI's $4.8B AGGREGATE).** ⚠ **Amkor's release does not rescue this streak: it supplied
a FIGURE, and the streak is about SEGMENT ATTRIBUTION. Amkor named no segment and no revenue share.**

**⚠⚠⚠ §3 ON FOREIGN LISTING IS NOW THE BINDING CONSTRAINT FOR A THIRD SESSION IN FOUR — OBSERVATION 3
OF THE 3 THE 10-19 ENTRY ASKED FOR, AND IT IS A COMPOUND INSTANCE RATHER THAN A REPEAT.** NVIDIA's
AI component-capacity initiative names **SIX** participants and **FIVE ARE FOREIGN-LISTED** (Samsung
Electro-Mechanics/Korea · Ibiden/Japan · Unimicron/Taiwan · King Yuan Electronics/Taiwan ·
SPIL/Taiwan, via NYSE-ADR parent ASE). ⚠ **10-19 was §3-dead at the TRANSACTION leg; 10-20 (GSEO) was
§3-dead at the COMPANY B leg; today is BOTH AT ONCE plus the one US-listed participant failing on the
thesis parts.** ⚠⚠ **FOR THE HUMAN, ATTACHED TO OPEN ITEM (3): if the second-order companies §4's
logic correctly identifies in the AI hardware chain are systematically foreign-listed, then §3 and §4
together cannot produce a trade in the sector that dominates the current news flow. THAT IS A
STRUCTURAL STATEMENT ABOUT THE CONFIGURATION, NOT A REASON TO LOWER §3.** Three sessions in four is
now a pattern rather than an observation; the next two weekly reviews should test it.

**⚠⚠ ONE `move` CALL ON A LIVE CANDIDATE AND IT IS THE RECORDED AKAM SUB-SHAPE, *NOT* A NEW SHAPE
SEVEN — THE `grep` THE CARRY-FORWARD DEMANDS WAS RUN FIRST AND IT CHANGED THE ANSWER.** `AMKR`
returned **−2.37% / `priced_in: false` / "passes"** over five sessions, **and the pass is manufactured
by arithmetic cancellation**: closes ran **44.78 → 41.875 → 41.69 → 43.72**, i.e. a **−6.9% sector
drawdown** against a **+4.87% news-day pop** (10-20 41.69 → 10-21 43.72, on **183,526** shares against
~115–125k on the preceding days). ⚠⚠ **THE INDEX CONTROL SEPARATES THE TWO LEGS AND COST ONE CALL, AS
10-21 ESTABLISHED: `VOO` over the IDENTICAL WINDOW returned +0.46%, `priced_in: false` — so the
drawdown was AMKR's and the sector's, not the market's.** ⚠ **A 10-21 SEAT CALLED THIS "SHAPE SEVEN"
IN FOUR FILES AND HAD TO CORRECT IT; the shape names are the index, and this one is already written
down as shape three's opposite-failure sub-shape (`AKAM` at +3.19% netting a 104.53 → 117.435 → 110.44
round trip). THE REFINEMENT, WHICH IS GENUINELY NEW: IN `AKAM` BOTH LEGS WERE THE TICKER'S OWN NEWS;
HERE THE TWO LEGS HAVE **DIFFERENT CAUSES**, so shape three's causation-blindness and the AKAM netting
sub-shape COMPOUND — and compounding is what makes the net verdict look clean.** ⚠⚠ **§4's words are
"moved more than 4% over the last five sessions *ON THIS NEWS*". On this news AMKR moved **+4.87%**.
THE GFS PRECEDENT (shape five) IS THIS LOG'S CONTROLLING PRACTICE AND IT PASSED ON **BOTH** BASES;
AMKR PASSES ONE AND FAILS THE OTHER, SO IT IS LATE.**

---

### T-2026-10-22-01 — Amkor Technology (AMKR) / NVIDIA $1.3B South Korea advanced packaging — REJECTED (part 1 — AMKR *IS* THE HEADLINE NAME; part 2 — rule (viii), the figure is **PREPAYMENTS**, the JBL capital-paid-in shape, and no segment or revenue share exists; part 3 — the only dated milestone is **END OF 2028** and the release states NO revenue date at all; priced-in FAILS on the news-day basis; §3 cap **UNRESOLVED**)

**Company A / the news:** **NVIDIA** and **Amkor Technology** announced a strategic-partnership
expansion on **2026-10-21**. **Amkor's own IR release** (`ir.amkor.com/news-releases/...`,
`T-2026-10-22` retrieval) states the South Korea commitment is worth **$1.3 billion** and targets a
**greater-than-300% increase in interposer-wafer capacity by the END OF 2028**. The release adds that
the combined multi-year Arizona + South Korea agreements **total $3 billion**.
**Company B / the candidate:** **AMKR itself** — which is the first thing wrong with it.

**1. Mechanism (one sentence):**
> NVIDIA's $1.3B advanced-packaging commitment causes Amkor's advanced-packaging revenue to improve
> because Amkor is the named counterparty building the interposer capacity NVIDIA has contracted for.

⚠⚠ **THAT SENTENCE IS ONE CLAUSE AND IT IS STILL A PART-1 FAILURE, WHICH IS A DISTINCTION THIS LOG
HAS NOT HAD TO DRAW BEFORE.** The one-clause test is a test of whether a *second-order* link is tight
enough; it is not a licence to buy a *first-order* name whose link is tight because there is no link
to make. ⚠ **§4's opening sentence: *"news breaks about Company A; you look for Company B, whose
economics improve because of it. You are not chasing the headline name."* The headline here is
"NVIDIA and Amkor announce agreement." AMKR is the counterparty — Company A's other half.**
⚠ **THIS IS THE GFS KILL REPEATING VERBATIM** (`T-2026-10-09-01`: *"GFS IS THE HEADLINE NAME, and the
genuine second-order question returned a verbatim denial"*), **and it is the second time the funnel's
single best-documented object of the month has been the first-order leg.**

**2. Dollar path:** ⚠⚠⚠ **FAILS THREE WAYS, ALL THREE OUT OF THE PRIMARY SOURCE.**
**(a) THE FIGURE IS NOT REVENUE AND THE RELEASE SAYS SO IN ITS OWN WORD — `PREPAYMENTS`.** Verbatim:
*"The prepayments align Amkor's manufacturing capacity with NVIDIA's long-term growth plans and
support increasing demand for advanced packaging solutions."* ⚠ **A prepayment is CAPITAL PAID IN BY
THE CUSTOMER — a deferred-revenue liability until the work is performed, NOT segment revenue at
Company B. That is rule (viii)'s list, and specifically its DEFINITIVE WORKED EXAMPLE: JBL's $1.7
BILLION, named, allocated, quoted verbatim from an 8-K, and still capital paid in by the customer.**
⚠⚠ **THE RELEASE EXPRESSLY DECLINES TO CALL IT REVENUE OR GIVE A RECOGNITION SCHEDULE** (source,
verbatim: *"does not expressly label the $1.3 billion as revenue or provide a revenue-recognition
schedule"*). **(b) NO SEGMENT, NO SHARE.** Amkor named no reporting segment for the award and no
segment revenue share; the sources do not carry Amkor's segment table or FY revenue at all, and the
source **declined to supply either rather than estimate** — so the **10%-of-revenue test is NOT
COMPUTABLE, which differs from "fails it".** **(c) THE $3B IS A TRAP AND THE STANDING FIX CAUGHT IT.**
$3B is an **AGGREGATE SPANNING THIS DEAL PLUS THE PREVIOUSLY ANNOUNCED ARIZONA COLLABORATION** — rule
(viii)'s Venture Global $17.2B shape (*"broader than the announced deal"*). ⚠ **The 10-21 fix — *ask
for the figure disclosed FOR THIS TRANSACTION* — is the only reason the $3B did not become a part-2
input. One clause, second consecutive session it has paid.**

**3. Timing window:** ⚠⚠ **FAILS, AND IN THE WORSE OF THE TWO AVAILABLE WAYS.** The only dated
milestone anywhere is **">300% interposer-wafer capacity by the END OF 2028"** — **~9 quarters against
§4's ceiling of TWO.** ⚠⚠ **AND THE RELEASE STATES NO REVENUE-CONTRIBUTION DATE AT ALL** (source,
verbatim: *"does not state a date or quarter when the South Korean project will begin contributing to
reported revenue"*). **So part 3 is not merely too long — it is UNWRITEABLE from the disclosure.**
⚠ **This is the GFS part-3 kill at a longer horizon** (GFS: ramp *"during the first half of 2028"*,
six quarters minimum; here, end-2028, nine) **— the third consecutive month in which the best-sourced
candidate in the log dies on a 2028 ramp date.** → **no deadline; no position.**

**4. Invalidation:** not written. ⚠ **Parts 1, 2 and 3 all failed first, and §4 is explicit that
failing one part ends the trade. Writing a fourth part here would be constructing the rest of a thesis
whose foundation is already gone.**

**Hard filters** *(run BEFORE the parts, per §4, and the §3-first discipline — the cap was pulled
before any part was elaborated):*
- **Priced-in (§4): SPLIT, AND IT FAILS ON THE BASIS §4's WORDS DESCRIBE.** Five-session:
  **−2.37%**, `priced_in: false`, *"passes"* (`move --symbol AMKR --sessions 5`: 44.78 → 43.72).
  **News-day: +4.87%** (10-20 close **41.69** → 10-21 close **43.72**, `bars --days 8 --adjustment
  all`, volume **183,526** vs ~115–125k preceding). ⚠⚠ **§4 says "more than 4% … ON THIS NEWS" →
  **FAIL**. The five-session pass is the recorded AKAM netting sub-shape of shape three, compounded:
  a −6.9% drawdown and a +4.87% news pop with DIFFERENT CAUSES cancelling to a clean-looking net.
  Index control over the identical window: `VOO` **+0.46%**, `priced_in: false`.** ⚠ **NOT a new
  defect shape — the `grep` was run first, as the carry-forward demands.**
- **Correlation (§4): PASSES TRIVIALLY AND THE REASON MATTERS.** Zero open satellite positions, so
  there is **no `driver` field anywhere to collide with.** ⚠ **An empty ledger makes this filter
  unfireable, which is not the same as a candidate that is genuinely uncorrelated. Thirty-ninth
  consecutive session with no operand.**
- **Universe (§3): `asset` returns `us_equity` / **NASDAQ** / `active` / `tradable`, not leveraged,
  not inverse, not crypto — all pass. MARKET CAP: **UNRESOLVED, NOT PASSED.** Perplexity **declined
  to supply a figure**, correctly and verbatim: *"A market capitalization figure must be tied to both
  a share price date and a share-count date… so no precise current market-capitalization calculation
  can be reported without introducing unsupported figures."* ⚠⚠ **DO NOT INHERIT A §3 VERDICT FROM
  THIS ENTRY (the VAL precedent). At the 10-21 close of 43.72 a $10B cap implies ~229M shares, so
  AMKR sits NEAR THE FLOOR ON EITHER SIDE and the 10-21 carry-forward's "plausibly near the $10B
  floor" is confirmed as the right caution.** ⚠ **It never needed resolving: the thesis parts killed
  it first, and §3 is not the reason it is rejected.**

**Outcome:** **REJECTED.** ⚠⚠⚠ **AND THIS IS THE MOST INFORMATIVE REJECTION SINCE GFS, FOR THE
OPPOSITE REASON TO MOST ENTRIES IN THIS FILE: nothing was missing.** A primary-source company release ·
a named counterparty · a dated announcement · a $1.3B figure attributed to the buyable leg BY the
buyable leg · a one-clause mechanism · `us_equity`/NASDAQ/tradable · and a filter verdict reading
*"passes"*. ⚠⚠ **THE PULL TO BUY IT WAS REAL AND IS NAMED HERE RATHER THAN OMITTED: the sleeve has
been undeployed since inception, $30,000 has earned nothing for 39 sessions, every §6 gate is open,
and this is the best-documented object this funnel has ever produced. THAT IS PRECISELY THE
CONFIGURATION §4's HONEST-BROKER RULE DESCRIBES, AND THE ANSWER IS STILL NO.** ⚠ **The three kills
are independent and each is sufficient: it is the headline name (part 1), the figure is a prepayment
rather than segment revenue (part 2 / rule (viii)), and the only date in the document is end-2028
(part 3).** ⚠ **DO NOT REHABILITATE IT AT A DIFFERENT PRICE — it did not die on price. Neither the
end-2028 date, nor the word "prepayments", nor Amkor's position in the headline moves with the quote.
"But it has not run yet" is "but it went up" wearing a coat.**

---

### T-2026-10-22-02 — NVIDIA / Samsung Electro-Mechanics ABF substrate lines → the second-order substrate chain (SEMCO · Ibiden · Unimicron · KYEC · SPIL/ASE) — REJECTED (§3 at EVERY genuine Company B; part 2 — no figure at any leg; part 3 — mid-2027 to end-2028; rule (v) — participation in an INITIATIVE is not a transaction)

**Company A / the news:** **Samsung Electro-Mechanics** announced on **2026-10-21** a strategic
partnership with **NVIDIA** to **jointly invest in dedicated ABF / FC-BGA package-substrate production
lines** at **Sejong and Busan, South Korea**, serving NVIDIA AI compute chipsets and high-speed
networking switches under a multiyear supply agreement.
**Company B / the candidate:** the substrate and advanced-packaging supply base NVIDIA named —
**Ibiden · Unimicron · King Yuan Electronics (KYEC) · SPIL**, plus **ASE Technology Holding (ASX)** as
SPIL's NYSE-ADR parent.

**1. Mechanism (one sentence):** cannot be written for any US-listed leg without an "and also."
> *"NVIDIA's capacity co-investments cause ASE Technology Holding's packaging revenue to improve
> because SPIL is a named participant — **and also** SPIL's participation translates into an
> ASE-level figure, **and also** NVIDIA's arrangement with SPIL has disclosed terms."*

⚠ **Two "and also"s. §4 rejects at the first.** ⚠⚠ **THE UNDERLYING DEFECT IS RULE (v) IN ITS CLEANEST
FORM: NVIDIA named these companies as PARTICIPANTS IN AN INITIATIVE, which is a fact about an
industry's capacity, not a transaction with any one of them.** The source drew the line itself,
verbatim: *"identifying Amkor in the initiative supports an inference of potential exposure… but it
does not establish substrate-specific revenue, contract value, or segment revenue."*

**2. Dollar path:** **FAILS AT EVERY LEG, AND THE ONE CIRCULATING FIGURE IS A NEW RULE (viii)
COSTUME.** ⚠⚠ **THE "$2.8 BILLION" (KRW 3.7T) IS SOURCED TO A NEWSPAPER CITING UNNAMED INDUSTRY
SOURCES, EXPLICITLY NOT CONFIRMED BY EITHER PARTY** — Reuters citing *Maeil Business Newspaper*; a
trade publication stated outright that *"neither company had disclosed the investment amount or how
costs would be divided."* ⚠ **AND ITS COMPOSITION IS THE TELL: KRW 2.6T from NVIDIA and KRW 1.1T from
**TESLA** — Tesla appearing, unconfirmed, in a substrate deal it is not a party to. A figure whose own
breakdown names a party the announcement does not is not a dollar path; it is a rumour with a decimal
point.** ⚠ **SEMCO's own KRW 4.27T Sejong plan and KRW 23T-through-2040 site plan are its BROADER
CAPEX, not this deal — rule (viii)'s "broader than the announced deal" shape, third session running.**
⚠ **NVIDIA/SPIL: capacity target only, "15× by mid-2027", and the source confirms NO SPIL-specific
dollar amount, prepayment or reservation was disclosed.**

**3. Timing window:** **FAILS INDEPENDENTLY, NO QUERY NEEDED.** SPIL **15× by mid-2027** with a further
doubling **by end-2028**; SEMCO deliveries *"beginning in 2026"* but under a multiyear agreement with
no revenue date. ⚠ **~3 to ~9 quarters against §4's TWO. Rule (vi) screened early, as the standing
rule instructs.**

**4. Invalidation:** not written — parts 1, 2 and 3 failed.

**Hard filters:** **§3 KILLS EVERY GENUINE COMPANY B BEFORE A MECHANISM IS NEEDED.** Samsung
Electro-Mechanics **KRX** · Ibiden **TSE** · Unimicron **TWSE** · KYEC **TWSE** · SPIL **TWSE**.
⚠ **ASE Technology Holding (ASX) is an NYSE ADR and §3 bars only *"ADRs of companies below the cap
floor"*, so it is not barred by form — but its cap was NOT sourced and is therefore UNRESOLVED, and
it dies on parts 1/2/3 regardless.** ⚠ **No `move` call spent on any leg: a candidate dead at part 1
does not reach the priced-in filter, and calling it anyway is the decorative use this log has
recorded six times.**

**Outcome:** **REJECTED.** ⚠⚠ **THIS IS THE GSEO FINDING (10-20) IN A COMPOUND FORM AND IT IS THE
RUN'S SECOND MESSAGE FOR THE HUMAN: §4's logic worked — it reached a real second-order supply base
from a real event — and FIVE OF THE SIX NAMED PARTICIPANTS ARE FOREIGN-LISTED.** ⚠ **Company B
exists, is correctly identified, and is not buyable. Third session in four where §3 on foreign listing
is the binding constraint. Attached to open item (3); NOT a reason to lower §3.**

---

### T-2026-10-22-03 — Meta Platforms (META) FY2026 capex $135–145B → the unnamed AI-infrastructure supply base — REJECTED (rule (v) — an UNNAMED SUPPLY BASE made nameable by a very large figure; part 2 — the source volunteered that any attribution *"would be inference, not disclosure"*; rule (iii) NEW COSTUME — a **NARROWED** range, one endpoint moved and one did not)

**Company A / the news:** **Meta** reported Q3 2026 on **2026-10-21**: revenue **$64.6B** against a
reported **$63.4B** expectation; quarterly capex **$34.9B**, up from **$31B** in Q2 and **$19.4B** a
year earlier; and FY2026 capex guidance of **$135–145B**.
**Company B / the candidate:** the data-centre, networking, semiconductor and power supply base — **no
company was ever named, by Meta or by anyone else.**

**1. Mechanism (one sentence):** **unwriteable without naming a company, and no source names one.**
⚠⚠ **THE DRILL RETURNED A VERBATIM REFUSAL, WHICH IS THE CLEANEST PART-2 KILL AVAILABLE:** *"No
publicly traded US company was identified as having disclosed a Meta-specific dollar revenue figure
for a specifically reported business segment… Any attribution based only on Meta's general
AI-infrastructure spending would be inference, not disclosure."* ⚠ **Meta named no supplier, vendor
or counterparty in the announcement. That is rule (v)'s UNNAMED SUPPLY BASE, and §4's warning about
the pull is exact: a $135–145B figure plus named component CATEGORIES (data centre, networking, power)
is the most fillable-looking blank this funnel produces. THE SOURCE LEFT THE BLANK; FILLING IT IN IS
NOT RESEARCH.**

**2. Dollar path:** **FAILS — THE FIGURE IS COMPANY A'S SPENDING, UNALLOCATED ACROSS AN UNNAMED
BASE.** No segment at any Company B, no share of revenue, no counterparty. ⚠ **Scale is the whole of
its persuasive force, which the standing macro rule already names: SCALE MAKES IT MORE CONVINCING,
NOT LESS.**

**3. Timing window / 4. Invalidation:** not written — parts 1 and 2 failed.

**⚠⚠ RULE (iii) — A GENUINELY NEW COSTUME, AND IT IS WORTH THE LINE IT COSTS: A *NARROWED* RANGE IN
WHICH ONE ENDPOINT MOVED AND THE OTHER DID NOT.** Scan 2 reported Meta *"raised the low end of its
2026 capital-expenditure outlook, to $135–145B from $130–145B."* ⚠ **The drill's primary-sourced
wording is **"narrowed from"**, not "raised": the LOW end rose $5B, the HIGH end is UNCHANGED, and the
midpoint moved $137.5B → $140B, **+1.8%**.** ⚠⚠ **BOTH DESCRIPTIONS ARE ARITHMETICALLY TRUE AND THEY
CARRY OPPOSITE IMPRESSIONS. This is the 10-15 TSMC SPLIT VERDICT one level deeper: there, two
different figures in one release gave a pass and a fail; here it is **ONE figure whose two endpoints
disagree**.** ⚠ **THE RULE: when a range moves, state which endpoint moved. "Raised guidance" is not
establishable from a narrowing, and "reaffirmed" is not establishable either — it is neither costume,
and it needs its own name.** ⚠ **NOTE THE INVERSION FROM 10-15, which is the one genuinely encouraging
line in this entry: at TSMC the figure that moved (revenue) had no supplier chain and the figure with
the supplier chain (capex) did not move. **Here the figure that moved IS the capex — the one WITH a
supplier chain.** The shape finally pointed the right way, and it still produced nothing, because the
supplier chain is unnamed. THE BINDING CONSTRAINT WAS NEVER THE SIGN; IT IS THE NAMING.**

**Outcome:** **REJECTED.** No named Company B exists, and the source said so unprompted.

---

### T-2026-10-22-04 — §3 / non-qualifying / defence / disposed-repeat / macro sweep of TWENTY-ONE items — REJECTED (disposed as one, ZERO drill queries spent)

Disposed without spending a drill, each with the test that kills it.

**⚠⚠ DISPOSED REPEATS RE-SERVED BY THE FUNNEL (4) — NO NEW ID MINTED, per the 10-14 precedent:**
**Apple / Perryman Company** *"up to $100M"* — **re-served by scan 1 as the day's only qualifying
announcement**, less than 24 hours after being disposed at `T-2026-10-21-04`; **Perryman is
family-owned and private**, and remains the holder of the only genuinely new dollar figure in Apple's
programme. ⚠ **The source itself conceded it *"does not provide a direct Apple or Perryman
announcement"* and attributed the report to Reuters at second hand.** · **Micron / Indium
Corporation** — disposed at `T-2026-10-21-02`; **the source dated it 2026-10-20, outside today's
window**, and Indium is private. · **Qnity Electronics** — no identified listing; joined Apple's
programme **March 2026** (rule (iii)). · **Northrop Grumman Q3** — disposed 10-20 at
`T-2026-10-20-03`; re-served as an EPS beat **against consensus** ($7.89 vs $7.18, FY guidance
$29.35–29.75 vs consensus $28.97), which is rule (iii) costume #1 and **not** its own prior range.

**§3 — not US-listed, or not listed at all (8):** **Samsung Electro-Mechanics** (KRX) · **Ibiden**
(TSE) · **Unimicron** (TWSE) · **King Yuan Electronics** (TWSE — ⚠ **and the separately reported
$1.1B NVIDIA capacity-reservation advance was formalised 2026-10-13, EIGHT DAYS before the window, so
rule (iii) kills it independently**) · **SPIL** (TWSE) · **Cherokee Nation Government Solutions**
($99.3M US Navy award — a tribal government enterprise, not listed) · **Luda Technology Group**
(long-term coal supply, **supplier unnamed and the parties stated there is NO fixed unit price or
total contract value** — rule (v) plus no figure) · **e3 Lithium** (TSXV).

**§3 cap floor — US-listed but nowhere near $10B (3):** **3 E Network Technology Group** (Nasdaq;
~$5.0M hardware sales agreement, **client unnamed** — rule (v) on top) · **Peraso** (production order
*"exceeding $2 million"*, **customer unnamed**) · **Karman Space & Defense** ($218M THAAD component
deal from Lockheed — ⚠ **a real two-party award with a real figure, and the closest thing in the sweep
to part-2 evidence; no segment attribution, and the §3 cap is unresolved and plausibly below the
floor**).

**⚠ US DEFENCE PROGRAM AWARDS — FIFTEENTH INSTANCE OF A STANDING SHAPE, DISPOSED AS A BLOCK (4):**
**Lockheed Martin F-35 framework** (850 aircraft, 10 years' sustainment, 156/yr — ⚠ **NO award value,
and the source states pricing and schedules still require a formal contract award: rule (vi)'s
pending-definitive shape, and LMT is first-order**) · **Leidos** $160M US Cyber Command (own award,
first-order, segments named but the value **not attributed** to one) · **CACI** *"$4.8 billion of
first-quarter contract awards"* (⚠ **an AGGREGATE, not an award — rule (v)**) · and the Karman item
above, counted once. ⚠ **The standing item holds: a defence program award names a government, which
is ONE party and no transaction.**

**Part 1 / rule (iii) — own results, no transaction, or not new to the company's own disclosure (4):**
**United Rentals** — ⚠ **A CLEAN RULE (iii) PASS AND IT STILL DIES, WHICH IS WORTH RECORDING: FY2026
revenue guidance raised to **$18.0–18.2B from its OWN $17.5–17.8B**, adjusted EBITDA to $8.3–8.4B, the
prior range present in the source. The company's own prior figure moved. But URI is FIRST-ORDER, named
no supplier, and disclosed no fleet-purchase commitment to anyone — the equipment-maker read-across
(CAT/DE/TEX/OSK) needs an "and also URI will therefore buy more", which is rule (v) and the
shared-cause object.** ⚠ **A clean pass on one filter is not progress toward a trade.** ·
**Procter & Gamble** (FQ1 net sales $23.3B, +4%; FY2027 guidance 2–4% **explicitly reflecting the
Thorne acquisition effective 2026-10-01** — an acquisition changing the reporting base, not a
second-order catalyst) · **PG&E** (reaffirmed 2026 core EPS $1.64–1.66 and 2027 $1.78–1.82 —
**reaffirmation is rule (iii) costume #1**) · **SpaceX / Capital One / Winnebago** (reported above
expectations; the source said the snippets lacked figures and operational detail — **not establishable
in either direction**, the AAR shape).

**⚠ MACRO COMPLEX — ONE PARTY, NO TRANSACTION, ALREADY DISPOSED AT `T-2026-10-12-05` AND
`T-2026-10-13-08` (1, as a block):** hotter-than-expected recent US CPI and PPI with higher energy
costs · expectations for a Fed **hold** at the **10/27–28** FOMC · Goldman Sachs reported as expecting
a further **25bp in December** to a **4.00–4.25%** peak · gold at a two-week low on an oil rally.
⚠⚠ **THE SOURCE DREW THE LINE ITSELF — *"These are market or economist expectations, not a Federal
Reserve decision. The available material does not establish a new policy action during the 24-hour
period."*** ⚠ **A third ID for the macro complex would inflate the thesis count. NOTE AND DO NOTHING.**

**Outcome:** **ALL TWENTY-ONE REJECTED.** ⚠ **Zero drill queries spent on any of them. Four were
killed by reading this log first, eleven arrived pre-excluded with the funnel's own reason attached,
four are the standing defence shape and one is macro.**

---

### 2026-10-21 (08:03 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, all exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$100,167.38** at
pre-flight). `clock` at **08:03:24** reads `is_open: false`, `next_open` **2026-10-21T09:30**,
`next_close` **2026-10-21T16:00** — **both carrying TODAY's date: the pre-market full-session
signature, read off the DATES and not the boolean. Not a holiday, not an early close.** Window
screened: **the completed 2026-10-20 session and the overnight into Wednesday — ONE TRADING DAY.**
**Two structural scans, one significance scan and two drills, all exit 0. FOUR theses, ALL FOUR
REJECTED.**

**⚠⚠⚠ CORRECTED BEFORE PUBLICATION, AND THE CORRECTION IS THE MORE USEFUL FINDING: THIS RUN'S `move`
RESULT IS **SHAPE ONE AT THE LARGEST SAMPLE EVER RECORDED**, NOT A NEW SEVENTH SHAPE. THE FIRST DRAFT OF
THIS ENTRY CALLED IT "A SEVENTH DEFECT SHAPE … THE FIRST THAT FAILS IN THE SAFE DIRECTION" IN FOUR FILES.
THAT WAS FALSE AND IS REPLACED HERE RATHER THAN LEFT BESIDE A CORRECTION.** ⚠⚠ **`state.md` ALREADY
CARRIES BOTH HALVES: *shape one — a DRAWDOWN misread as priced-in*, nine instances, and *shape three —
SIGN- AND CAUSATION-BLINDNESS*. I re-derived a documented defect from scratch and promoted it to a
discovery.** ⚠⚠⚠ **THAT IS CATCH (24)'s SHAPE WEARING A NEW COAT: not an enumeration that sounded
exhaustive and was not, but a seat that DID NOT READ THE ENUMERATION IT ALREADY HAD before adding to it.
The standing rules were read this run; the shape list forty lines below them was not. ⚠ THE FIX IS THE
SAME ONE: `grep` THE EXISTING LIST BEFORE CLAIMING AN ADDITION TO IT. It cost one grep to find and would
have cost one grep to prevent.** ⚠ **WHAT IS GENUINELY NEW IS THE EVIDENCE, AND IT IS WORTH HAVING:**
seven `move`
calls were spent today — **the largest single-run sample this filter has ever had** — and **all seven
returned `priced_in: true`, and ALL SEVEN WERE DOWN**: `COHR` **−20.07%** · `AMKR` **−12.45%** · `GLW`
**−10.94%** · `GM` **−8.24%** · `AVGO` **−6.41%** · `MU` **−5.92%** · `TSM` **−4.43%**. ⚠⚠ **`scripts/alpaca.py:177`
is `abs(move) > PRICED_IN_MOVE_PCT`. THE FILTER IS DIRECTION-BLIND, so it reads a 20% COLLAPSE as
"you are late, the news is priced in."** ⚠ **For a §3 long-only strategy that is backwards: §4's check
exists to stop a buy AFTER the stock has run UP on the news, and a name that has fallen a fifth has
whatever is in its price, but it is not the good news being bought.** ⚠⚠ **SECOND GAP, AND IT IS §4's
WORDING NOT THE SCRIPT'S: the rule says "moved more than 4% … *on this news*", and the filter CANNOT
TELL WHETHER THE MOVE WAS ON THE NEWS AT ALL. Today it demonstrably was not — `VOO` over the identical
window is **−1.22%, `priced_in: false`**, so the index is flat while the semi/AI complex is down 4–20%,
and the broad scan named the cause itself (*"an AI-stock pullback"*, *"chip stocks fall"*). The filter
blocked seven candidates for a SECTOR DRAWDOWN THAT HAS NOTHING TO DO WITH ANY OF THEIR THESES.**
⚠⚠ **THE DIRECTION OF THE ERROR IS WHY THIS IS NOT A CRISIS: shape six fails TOWARD taking a trade;
shape one fails toward REFUSING one. IT COSTS OPPORTUNITY, NOT CAPITAL — and that asymmetry is also the
reason nine prior instances were tolerated rather than escalated, which is a decision for the human and
not a defence of the filter.** ⚠⚠⚠ **AND IT
IS EXPLICITLY NOT USED AS GROUNDS TO OVERRIDE ANYTHING TODAY — the filter said skip and the skip stands,
and every one of the five Apple-named suppliers DIES INDEPENDENTLY ON PART 2 AND RULE (iii) ANYWAY, so
the defect rescues NO candidate. Recording a filter defect on the same run it would have helped is the
moment the temptation exists; it is named here so the next seat can see it was refused.** ⚠ **ONLY A
HUMAN MAY CHANGE §4 OR `alpaca.py move`. Open human item.**

**⚠⚠ THE STRUCTURAL FRAMING EARNED ITS PLACE FOR A SEVENTH CONSECUTIVE SESSION, AND THE "SIGNIFICANCE"
FRAMING FAILED IN THE *PREDICTED* WAY — THE CARRY-FORWARD CALLED THE SHAPE BEFORE THE QUERY RAN.** Scan 1
(the routine's own Step 5a voice) returned **pending home sales −7.3% m/m to a series low, the NAHB index
at 29, a Fed-pause repricing to 84.5%, the 10-year at 5.12% and oil reversing** — **the macro complex,
the one object §4 can never use** — and its two corporate items were an own-earnings print and a
**reject this log disposed less than 24 hours ago.** Scan 2 (**two named companies and a disclosed dollar
amount**) returned **one qualifying item plus SIX self-excluded with reasons attached**, and scan 3 (the
segment-quantification framing) returned **nothing qualifying plus EIGHT self-excluded**. ⚠ **Fourteen
items disposed for free across the two structural scans, for ZERO follow-up queries.**

**⚠⚠⚠ THE DISPOSED-REJECT RE-SERVE IS NOW AT THREE CONSECUTIVE SESSIONS AND TODAY IS THE WORST FORM YET:
THE FUNNEL NAMED A REJECT DISPOSED *YESTERDAY* AS THE DAY'S CLEAREST CROSS-COMPANY EVENT.** Scan 1's own
bottom line: *"The clearest cross-company events were 3M's Amazon-linked data-center arrangement and
raised outlook."* **That is `T-2026-10-20-01` verbatim — minted, drilled and killed on part 2 at this
same seat 24 hours ago**, and the re-serve arrived carrying the warrant structure as a selling point.
⚠ **`RTX` was ALSO re-served, by scan 3, now at a SEVENTH appearance — and the source itself dated the
cited missile awards to 2026-09-28, i.e. it re-served a reject while disclosing that it was stale.**
⚠⚠ **NO NEW ID WAS MINTED FOR EITHER, per the 10-14 precedent: a second entry for one rejection inflates
the thesis count and records nothing. They are disposed inside `T-2026-10-21-04`.** ⚠ **READING THE LOG
FIRST COST ONE `grep` AND SAVED TWO FULL DRILLS — third session running that this has been the single
highest-return minute of the run.**

---

### T-2026-10-21-01 — Apple (AAPL) American Manufacturing Program → its five named US-listed suppliers (AVGO · GLW · COHR · TSM · AMKR) — REJECTED (part 2 at every leg; rule (iii) — the GM/Lockheed *delivery-milestone-recycled-as-news* costume at FIVE legs at once; §3 on both genuinely NEW relationships; and the priced-in filter on all five — SHAPE ONE at its largest recorded sample, NOT a new shape)

**Company A / the news:** **Apple Inc. (AAPL)**, announcement dated **2026-10-20**, expanding its
American Manufacturing Program for the **iPhone Duo** and **iPhone 18 Pro**. The announcement **names
seven suppliers**: two new-or-expanded (**Perryman Company**, **Qnity Electronics**) and five existing
(**Broadcom**, **Corning**, **Coherent**, **TSMC**, **Amkor Technology**), each tied to a **named US
facility and a named component** — Perryman/grade-5 titanium enclosures (PA), Qnity/variable-aperture
camera films (DE), Broadcom/RF components (Fort Collins CO), Corning/Ceramic Shield cover glass
(Harrodsburg KY), Coherent/VCSELs for Face ID (Sherman TX), TSMC/advanced chips (Arizona),
Amkor/packaging and test (Peoria AZ).

**Company B / the candidate:** **this is the best-structured object this funnel has produced in seven
sessions, and it must be said plainly before it is killed.** Company A **named** its Company Bs — five
of them, US-listed, with the facility and the part specified. **No link had to be supplied, no blank had
to be filled, and no prior had to be guessed.** That is the entire thing rule (v) exists to complain
about the absence of, and today it was present.

**1. Mechanism (one sentence):** **WRITEABLE, in one clause, for at least three legs.** *"Apple's
expansion of US iPhone component sourcing causes Corning's specialty-materials revenue to improve
because Apple buys Ceramic Shield cover glass from Corning's Harrodsburg plant."* ⚠ **No "and also"
needed. Part 1 PASSES, and it is the first multi-leg part-1 pass in this log.**

**2. Dollar path:** **FAILS, AT ALL FIVE LEGS, AND THE SOURCE SAYS SO ITSELF.** Verbatim: *"The sources
do not provide supplier-specific dollar figures for Qnity, Corning, Coherent, TSMC, or Amkor."* **No
segment is named at any Company B, no magnitude is disclosed, and no share of total revenue is
establishable for any of the five.** ⚠⚠ **THE ONE DOLLAR FIGURE IN THE WHOLE ANNOUNCEMENT ATTACHED TO A
LISTED SUPPLIER IS RULE (iii) AND RULE (viii) AT ONCE: Broadcom's "$1.5 billion" is an investment in its
OWN Fort Collins facility, ANNOUNCED IN JULY, and the source states explicitly that it "does not
explicitly state that the entire amount is Apple's payment to Broadcom." It is Broadcom's capex, four
months old, not Apple's revenue to Broadcom.** ⚠ **The only NEW figure in the announcement — Apple's
**up to $100M over three years** — belongs to **Perryman**, and §3 kills it (see below). It is also
~0.025% of Apple's annual revenue, so it would fail part 2 at Company A too.**

**3. Timing window:** **NOT REACHED.** Part 2 failed first and §4 forbids constructing the rest to see
whether it survives. *(For the record: iPhone Duo volume ramp is a plausible one-to-two-quarter object,
so part 3 is the one part that would likely have passed. That makes the part-2 kill the whole story.)*

**4. Invalidation:** **NOT REACHED**, same reason.

**Hard filters:**
- **Priced-in (§4): FAIL AT ALL FIVE, AND THE FAILURE IS THE RUN'S FINDING.** `AVGO` **−6.41%** ·
  `GLW` **−10.94%** · `COHR` **−20.07%** · `TSM` **−4.43%** · `AMKR` **−12.45%** over five sessions,
  every one `priced_in: true`, **every one DOWN**, against `VOO` **−1.22% / false** over the identical
  window. ⚠ **THE FILTER BLOCKED FIVE CANDIDATES FOR A SECTOR SELL-OFF, NOT FOR THIS NEWS — defect
  SHAPE ONE at its largest recorded sample plus SHAPE THREE's first index control — stated in full in the
  survey above, where this entry's own false "seventh shape" claim is corrected, and raised for the human.** ⚠⚠ **THE SKIP STANDS
  ANYWAY: part 2 and rule (iii) kill all five independently, so the filter defect changes NO outcome
  today and is NOT used to rehabilitate anything.**
- **Correlation (§4): pass, VACUOUSLY — zero open satellite positions, so there is no `driver` field in
  `positions.md` to collide with.** ⚠ **A vacuous pass is not a pass the mechanism has ever been
  tested by; it has now passed this way for 37 sessions.**
- **Universe (§3): UNRESOLVED, NOT PASSED — and deliberately left that way.** All five are US-listed
  (`AVGO` Nasdaq · `GLW` NYSE · `COHR` Nasdaq · `TSM` NYSE · `AMKR` Nasdaq), but **no market-cap figure
  was sourced for any of them because they died two rungs earlier.** ⚠ **DO NOT INHERIT A §3 VERDICT
  FROM THIS ENTRY (the VAL precedent). `AMKR` in particular is plausibly NEAR the $10B floor and was
  not checked.** The two genuinely NEW relationships are **§3-dead outright: Perryman Company is
  family-owned and Qnity Electronics has no identified listing** — both private, neither buyable at any
  price.

**Outcome:** **REJECTED.** Part 2 fails at all five listed legs — **no figure, no segment, no revenue
share, with the source volunteering the absence** — and **rule (iii) fails at all five: Apple described
them as "existing partners whose progress Apple reported", which is the GM/Lockheed delivery-milestone
costume arriving at five legs simultaneously.** The two relationships that ARE new to disclosure are
private. ⚠⚠ **THE LESSON, AND IT CUTS THE SAME WAY AS GFS (`T-2026-10-09-01`): A NAMED COMPANY B IS NOT
ENOUGH. Seven weeks of this log have complained that the funnel never names Company B; today Company A
named five, and the kill moved one rung later — to the NUMBER rather than the NAME. The missing object
was never the identity of Company B; it is the SEGMENT-ATTRIBUTED DOLLAR FIGURE, which the
segment-quantification framing has now reported absent SEVENTEEN consecutive sessions.** ⚠ **AND THE
STRUCTURAL FRAMING DID NOT FIND THIS — scan 2 surfaced only the Perryman leg and its PRIVATE
counterparty; the five listed suppliers appeared ONLY under the targeted drill. A one-line drill on "name
every company the announcement named" converted a dead private-counterparty item into the log's first
five-leg part-1 pass. KEEP THAT DRILL.**

---

### T-2026-10-21-02 — Micron Technology (MU) / Indium Corporation — REJECTED (part 1 — the only counterparty is PRIVATE; rule (viii) — money paid OUT by the only buyable leg; part 2 — no figure, no segment; and a NEW rule (iii) SPLIT RUNNING THE OPPOSITE WAY FROM TSMC's)

**Company A / the news:** **Micron Technology (MU)** press release dated **BOISE, Idaho, Oct. 20, 2026**:
Micron is **investing in Indium Corporation** to restart and expand **critical-minerals and high-purity
materials processing in Clinton, New York**, in support of *"advanced memory manufacturing"*. The parties
also **"planned a long-term supply agreement"** — planned, not signed.

**Company B / the candidate:** **NONE EXISTS.** The announcement names **Micron and Indium Corporation
and no one else** (source, asked directly: *"No other company is identified as an investment recipient or
project participant"*). **Indium Corporation is private** — the release and all coverage identify no
ticker and no exchange. ⚠ **So the only US-listed party is Company A, and it is the PAYER.**

**1. Mechanism (one sentence):** **UNWRITEABLE — there is no second party to write it about.** The
mechanism that *could* be written runs the wrong way: *"Micron's investment causes Micron's own
critical-materials cost line to improve"* — **that is a first-order statement about Company A, which §4
is not a strategy for.**

**2. Dollar path:** **FAILS TWICE OVER.** Micron **disclosed no dollar amount for the Indium investment
at all**, and **named no reporting segment, no revenue percentage and no cost-base percentage**. ⚠ **The
source applied the kill before I did, in its own words: *"Any conclusion that the project materially
affects a particular segment or share of revenue/costs would be an inference, not a disclosed fact."***

**3. Timing window:** **NOT REACHED.** *(And it would have failed: a minerals-processing restart plus a
supply agreement that has not been signed is rule (vi)'s under-construction shape.)*

**4. Invalidation:** **NOT REACHED.**

**Hard filters:**
- **Priced-in (§4): `MU` −5.92% over 5 sessions, `priced_in: true` — FAIL.** ⚠ **Direction-blind again:
  Micron is DOWN over five sessions while the stock *"ticked up"* on this news per the coverage. The
  filter and the event disagree about the sign — shape one and shape three in one reading.** **Immaterial
  — part 1 killed it.**
- **Correlation (§4): pass, vacuously (zero open positions).**
- **Universe (§3): `MU` is plainly eligible; **Indium Corporation is §3-DEAD (private, not buyable with
  settled cash)**. No market cap sourced for `MU` — not needed, it is Company A.**

**Outcome:** **REJECTED.** ⚠⚠⚠ **AND IT CARRIES A GENUINELY NEW RULE (iii) VARIANT — THE *MIRROR* OF THE
10-15 TSMC SPLIT, WHICH IS WHY IT IS WORTH THE ENTRY.** On 10-15 one release carried a rule (iii) PASS
on revenue and a FAIL on capex, and **the figure that MOVED had no supplier chain while the figure WITH
the supplier chain did not move.** Today the split is along the *other* axis: **THE NEW DISCLOSURE
CARRIES NO NUMBER, AND THE ONLY QUOTABLE NUMBER CARRIES NO NEW DISCLOSURE.** The Indium funding **is**
new to Micron's disclosure (a clean rule (iii) pass) and **has no amount attached**; the **"up to $3
billion"** that every headline carried is **Micron's broader US supply-chain programme ceiling announced
in JULY** — rule (iii) costume #1 *and* rule (v)'s ceiling sub-shape at once. ⚠⚠ **THE TELL IS THE SAME
ONE AS 3M's $6B YESTERDAY, AND IT IS BECOMING THE DOMINANT SHAPE: THE BIG NUMBER AND THE NEW EVENT ARE
DIFFERENT OBJECTS. A reader who tests "is there a dollar figure?" and "is this new?" as two separate
yes/no questions gets two yeses and proceeds on a combination that does not exist.** ⚠ **THE FIX IS ONE
WORD IN THE DRILL: ask for the figure disclosed *FOR THIS TRANSACTION*, not for the figure in the
announcement. Today's drill did exactly that — "not the broader programme ceiling" — and that clause is
the only reason the $3B did not become a part-2 input.** ⚠ **Rule (viii) also lands cleanly: the money
moves OUT of the only buyable leg, the GEHC/Sofie and 44.01/Frontier costume for a third time.**

---

### T-2026-10-21-03 — General Motors (GM) Q3 2026 → the auto-supplier read-across — REJECTED (part 1 — own results, no transaction, no named second party; rule (iii) costume #1 — outlook moved against MARKET expectations, not its own prior range; and the supplier read-through is the shared-cause object)

**Company A / the news:** **General Motors (GM)**, **2026-10-20**: Q3 profit **above expectations**
while the **full-year 2026 outlook disappointed**, with the forecast midpoint **below market
projections**.

**Company B / the candidate:** **NONE REACHED, AND THE ONE ON OFFER IS A SHAPE THIS LOG HAS ALREADY
NAMED.** The tempting move is the **auto-supplier read-across** (a weaker GM build outlook → lower
volumes at `APTV`, `BWA`, `LEA`, `ALSN`, `MGA`). ⚠⚠ **IT IS THE SHARED-CAUSE OBJECT AND IT ALSO POINTS
DOWNWARD, WHICH `T-2026-10-08-02` (SUPN) ESTABLISHED IS UNTRADEABLE HERE: §3 permits only the long side,
so a correct bearish read cannot be expressed, and flipping it into a "GM's competitors benefit" long is
the shared-cause trap — no competitor's revenue or cost line changed, only its relative standing, and
NO COMPETITOR OR SUPPLIER WAS NAMED IN ANY SOURCE.** ⚠ **The supplier names above are MY priors, not the
source's. They are recorded as priors and NONE is logged as a candidate — the rule (v) / "Party A"
discipline.**

**1. Mechanism (one sentence):** **UNWRITEABLE in the required direction.** The only one-clause
mechanism available is a cost or volume line getting **WORSE** at an unnamed supplier.

**2–4:** **NOT REACHED.**

**Hard filters:**
- **Priced-in (§4): `GM` −8.24% over 5 sessions, `priced_in: true` — FAIL.** ⚠ **Direction-blind again,
  and here the sign is *informative* in a way the filter discards: GM fell on a disappointing outlook,
  which is the market pricing the BAD news. Immaterial — part 1 killed it.**
- **Correlation (§4): pass, vacuously.**
- **Universe (§3): `GM` eligible; no Company B to check.**

**Outcome:** **REJECTED.** **Part 1 — an own-results print naming no second party is a first-order
disclosure, the rung `RTX` has now died at seven times and `NOC` died at yesterday.** ⚠ **RULE (iii)
FAILS INDEPENDENTLY AND THE SOURCE WAS EXPLICIT: the shortfall is stated *"relative to analyst or market
expectations"* and the reporting *"does not establish whether GM lowered guidance against its own
previously stated range."* Costume #1, the most prolific costume on the list, for the Nth time.**
⚠⚠ **AND THE EARNINGS-SEASON PATTERN THE 10-20 SEAT PREDICTED IS HOLDING EXACTLY: it wrote "expect it
all earnings season" about a figure quoted against consensus rather than against the company's own prior
range, and 10-21's first earnings print does it again. THE PREDICTION IS NOW CONFIRMED RATHER THAN
OUTSTANDING.**

---

### T-2026-10-21-04 — §3 / non-qualifying / disposed-repeat / macro sweep of FIFTEEN items — REJECTED (disposed as one, ZERO drill queries spent)

Disposed without spending a drill, each with the test that kills it. ⚠ **This is where the two
structural scans' self-exclusions and the re-served rejects land; the funnel supplied the reason in
most of these cases, which is the whole return on the structural framing.**

**§3 — not US-listed, or not listed at all (6):** **Perryman Company** (family-owned, private — and it
is the holder of the only genuinely new dollar figure in the Apple announcement) · **Qnity Electronics**
(no identified listing; also previously announced, joined Apple's programme **March 2026**) · **Indium
Corporation** (private; see `T-2026-10-21-02`) · **MS International plc** (UK-listed; 12 DS30M naval gun
systems) · **Theon International plc** (Euronext Amsterdam; €45M night-vision from two NATO states) ·
**Circle8 Group / CAK** (**$68M/yr** managed services — and **CAK is a Dutch government implementation
agency**, so it is the government-action object on top of the listing failure).

**Part 2 / rule (viii) — the figure is not segment revenue at a buyable Company B (4):** **Polaris
Renewable Energy / Trina Energy Storage** (`TSX:PIF`, so §3 too — and the **US$55–60M** is **gross capex
for the whole Punta Lima project including transformer, tariffs and balance of plant**, NOT the Trina
contract value; the source said so) · **Hotel101 Global / Egypt JV** (**US$102.09M** is **expected
project value**, counterparty identity and listing unestablished) · **Orion Energy Systems (`OESX`)**
(a real **$45M / 3yr, ~$15M/yr recurring** award naming its **maintenance and technical services**
segment — ⚠ **the CLOSEST THING ALL DAY TO PART-2 EVIDENCE, and it still did not state the award's share
of that segment; killed outright by §3's $10B floor, which `OESX` is nowhere near**) · **Archer**
(Q3 backlog slides; no award figure, no §3 cap established).

**Part 1 / rule (iii) — no transaction, or not new (2):** **TechnipFMC / BP** (a **memorandum of
understanding** establishing a cooperation framework for 20k subsea systems — **no dollar amount, and an
MoU is rule (vi)'s pending-definitive-agreement shape**; note `FTI`/Petrobras was already disposed at
`T-2026-10-09-07`) · **XCF Global / Paramount facility** (definitive acquisition agreement, **no dollar
amount reported**).

**⚠⚠ DISPOSED REPEATS RE-SERVED BY THE FUNNEL (2) — NO NEW ID MINTED, per the 10-14 precedent:**
**3M (MMM) / Amazon** — **re-served by scan 1 as the day's "clearest cross-company event" less than 24
hours after being minted, drilled and killed at `T-2026-10-20-01`.** ⚠ **The re-serve arrived with the
3.2M-share warrant and the $6B trigger presented as commercial strength, which is precisely the rule
(viii) dilution costume that entry exists to record. Also note scan 1 could not establish whether 3M's
raised outlook moved against its own prior range — so the rule (iii) split verdict from yesterday is
*still* unresolved in the sources, not resolved in 3M's favour.** · **RTX** — **re-served by scan 3,
SEVENTH appearance in eleven sessions, as "$81 billion of contracts during the third quarter"; the source
itself dated the cited missile awards to **2026-09-28** and conceded the $81B was not identified as an
award announced on 10-20 or 10-21. ⚠ A reject re-served WITH its own staleness disclosed in the same
breath.**

**⚠ MACRO COMPLEX AND FORWARD CALENDAR — ONE PARTY, NO TRANSACTION, ALREADY DISPOSED TWICE (1, as a
block):** pending home sales **−7.3% m/m / −11.3% y/y**, a series low since 2001, against a ~0.4–0.5%
expected decline · NAHB HMI **29**, lowest since June 2012 (⚠ **released 2026-10-19, so it is not even
in today's window — the source flagged its own date discipline**) · Fed-pause probability **84.5%** for
the 10-27/28 FOMC, up from 81.2% · 10-year at **5.12%** · oil reversing on US–Iran mediation reports ·
September CPI **+0.6% m/m / +3.7% y/y** and FY2026 net interest **$1.052T** — ⚠ **both of which the source
explicitly declined to date to 10-21, so they are not establishable as today's news** · and **Tesla, Meta
and Netflix SCHEDULED to report 10-21**. ⚠⚠ **The forward calendar arrived on a WEDNESDAY, which the
carry-forward said was a Monday-seat shape — the prediction was too narrow: it is a shape of any thin
window, and a mid-week AI-pullback session with one trading day of inventory is thin. NOTE THE DATES AND
DO NOTHING; a macro aggregate has ONE party and no transaction, already disposed at `T-2026-10-12-05`
and `T-2026-10-13-08`, and a third ID for it would inflate the thesis count.**

**Outcome:** **ALL FIFTEEN REJECTED.** ⚠ **Zero drill queries spent on any of them. Eleven arrived
pre-excluded with the funnel's own reason attached, two were killed by reading this log first, and two
are macro.**

---

### 2026-10-20 (08:06 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, all exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$99,604.80** at
pre-flight). `clock` at **08:03:00** reads `is_open: false`, `next_open` **2026-10-20T09:30**,
`next_close` **2026-10-20T16:00** — **both carrying TODAY's date: the pre-market full-session
signature, read off the DATES and not the boolean. Not a holiday, not an early close.** Window
screened: **the completed 2026-10-19 session and the overnight into Tuesday — ONE TRADING DAY.**
**Three broad scans plus two drills, all exit 0. SIX theses, ALL SIX REJECTED.**

**⚠⚠ THE STRUCTURAL FRAMING EARNED ITS PLACE AGAIN AND THE "SIGNIFICANCE" FRAMING FAILED AGAIN, ON
THE SAME WINDOW — THE 10-06 PAIRED TEST REPRODUCED.** Scan 1 (the routine's own Step 5a voice, *"most
significant … news events"*) returned **two own-earnings prints and a macro aggregate**, and
volunteered *"the available results do not establish a material supply agreement."* Scan 2 (**two
named companies and a disclosed dollar amount**) returned **the 3M/Amazon warrant arrangement and the
MKS/TTM divestiture — NEITHER of which scan 1 mentioned at all** — plus five self-excluded items with
reasons attached. ⚠ **Scan 1's framing would have produced a no-trade day whose only content was two
earnings prints. USE THE STRUCTURAL FRAMING FIRST; it is now 6 for 6 sessions.**

**⚠⚠ THE SEGMENT-QUANTIFICATION FRAMING VOLUNTEERED THE ABSENCE FOR THE SIXTEENTH CONSECUTIVE SESSION
— 09-29 → 10-20 UNBROKEN.** Verbatim: *"Among the available results, no winner clearly disclosed the
award's value specifically to its own reported business segment. The reported figures are total
contract or agreement values where available—not segment-attributed values."* ⚠ **Seven awards
returned, seven with no segment figure. That framing's whole job is to find part-2 evidence, and it
has now reported its absence sixteen times running.**

**⚠⚠⚠ THE BINDING CONSTRAINT MOVED TO §3 FOR A SECOND CONSECUTIVE SESSION — OBSERVATION 2 OF THE 3
THE 10-19 ENTRY ASKED FOR, AND IT IS A STRONGER INSTANCE THAN THE FIRST.** On 10-19 three genuine
two-party transactions died at §3 on foreign listing (44.01/Frontier, NOVONIX/PowerCo, Orion
Minerals/Glencore). **Today the single best event in the window produced a genuine, named,
publicly-traded SECOND-ORDER company B — the thing this funnel has been failing to reach for five
weeks — and it is TAIWAN-LISTED** (`T-2026-10-20-02`, GSEO / Taiwan 3406). ⚠ **The 10-19 instances
were §3-dead at the *transaction* leg; this one is §3-dead at the *Company B* leg, which is the exact
rung §4 exists to reach. Company B now EXISTS, is CORRECTLY IDENTIFIED, and is NOT BUYABLE.** ⚠ **Two
sessions is still not a finding. Recorded for the next two reviews to test, not acted on.**

**⚠⚠ ONE `move` CALL — THE FIRST IN SEVEN SESSIONS, LEGITIMATE RATHER THAN DECORATIVE, AND IT EXPOSED
A SIXTH DEFECT SHAPE IN THE §4 PRICED-IN FILTER.** `MMM` reached the filter carrying a part-1 pass and
a real dated transaction. **It returned `priced_in: false`, +0.69% over five sessions, "passes" — and
the verdict carries ZERO information about the event, because every close in the window predates it.**
Full statement at `T-2026-10-20-01`; it is the run's most useful output and it belongs to the human.

---

### T-2026-10-20-01 — 3M (MMM) / Amazon — REJECTED (part 2 — no segment, no figure; rule (viii) NEW COSTUME — a $6B figure whose only disclosed function is to vest DILUTION at Company B; rule (iii) split verdict; and the priced-in filter's SIXTH defect shape)

**Company A / the news:** **Amazon.com** and a wholly owned subsidiary entered an **expanded
commercial relationship** with 3M, disclosed in a **3M 8-K dated 2026-10-19** (coverage timestamped
~17:36 ET, i.e. **after the 10-19 bell**), covering 3M's supply of **"optical connectivity and other
Data Center products."** Terms as disclosed: 3M **issued a warrant** to an Amazon subsidiary for up to
**3,162,015 3M shares**, **seven-year** term, exercise price **$164.89**; **85% of the warrant shares
vest on Amazon's cumulative payments** for those products and become **fully vested at $6 billion**
cumulative; the remaining **15%** vests on **unspecified "event-based milestones."** Full exercise
would yield 3M ~**$521.4M** in proceeds.
**Company B / the candidate:** **3M Company (MMM)** — tested under the reading that makes the strongest
possible case for it (Company A = Amazon, the party making the commitment; Company B = 3M, the supplier
whose revenue line it lands on). ⚠ **Under the plainer reading 3M is simply the headline name — it
filed the 8-K and its stock moved on it — and §4 forbids chasing the headline name. The entry is
written against the stronger reading because dismissing it on the weaker one would be dodging.**

**1. Mechanism (one sentence):**
> Amazon's expanded data-centre purchase arrangement causes 3M's data-centre optical-connectivity
> revenue line to rise because Amazon is contracting to buy those products from 3M.

⚠ **THIS IS A CLEAN PART-1 PASS AND THEY ARE RARE IN THIS LOG — one clause, no "and also", a named
buyer, a named seller, a named product line and a dated filing.** Five of the last six sessions died
*at* part 1 for want of a Company B. **This one gets through it, which is exactly why the rest of the
entry matters: the filters that follow are not a formality here, they are the whole decision.**

**2. Dollar path:** ⚠⚠ **THIS IS WHERE IT DIES, AND IT DIES WITHOUT A JUDGEMENT CALL.** 3M disclosed
**no reporting segment** for the sales, **no revenue figure**, **no backlog**, **no annual or total
contract value**, **no margin**, **no change to 2026 guidance** and **no quantified contribution to
any segment** — the sources state each of those absences explicitly. §4 part 2 requires *the segment
affected, the magnitude, and that segment's share of total revenue*; **I cannot supply one of the
three without inventing it.** 3M's total revenue runs ~**$24–25B/yr**, so even taking the $6B at face
value and spreading it over the warrant's seven-year term gives **~$860M/yr ≈ 3.5% of revenue —
UNDER §4's 10% floor** — and that arithmetic is itself illegitimate, because **the $6B is not a
purchase commitment** (see below). **No honest part 2 exists. REJECT.**

**3. Timing window:** **Not establishable, and it fails in the direction of too long.** No delivery
schedule, no first-revenue date and no guidance change were disclosed; the only dated horizon in the
document is the **warrant's seven-year term** (~28 quarters against §4's **two**). ⚠ *Not the decisive
kill — part 2 is — but it does not rescue anything either.*

**4. Invalidation:** *(not reached — part 2 is unwritable, so there is no thesis to invalidate.)*

**Hard filters:**
- **Priced-in (§4): `move --symbol MMM --sessions 5` → 160.895 → 162.01, +0.69%, `priced_in: false`,
  "passes the priced-in check" — AND THE VERDICT IS INFORMATIONALLY EMPTY. SEE THE DEFECT-SHAPE NOTE
  BELOW; this is a NEW failure mode, not a pass.**
- Correlation (§4): drivers of open positions checked → **pass, with NO OPERAND — zero satellite
  positions exist, so nothing could correlate.** ⚠ *Recorded as the fourth state, not as a pass.*
- Universe (§3): `asset` → **`us_equity` / NYSE / `tradable: true` / fractionable**; market cap
  **~$87B** (source: Perplexity, against 162.01 × ~537M shares — **order-of-magnitude only, and NOT
  audit-grade; it is recorded because the rule says to record where it came from, and it was never
  load-bearing because the thesis died at part 2**) → **pass, by a factor of ~8.7.**

**⚠⚠⚠ RULE (viii) — A NEW COSTUME, AND IT IS THE MOST SEDUCTIVE ONE SINCE JBL's $1.7B CONSIGNMENT.
A DOLLAR FIGURE WHOSE ONLY DISCLOSED FUNCTION IS TO MEASURE HOW MUCH DILUTION VESTS AT COMPANY B.**
The "$6 billion" is **not revenue, not a purchase order, not a commitment, and not a ceiling on a
contract** — it is **the threshold at which 85% of a warrant 3M GAVE ITS CUSTOMER becomes fully
vested.** ⚠ **The sign is inverted twice over: the instrument is equity issued BY the candidate TO the
counterparty, and the $6B's role is to accelerate that issuance.** ⚠ **The nearest prior entry on this
list is AstraZeneca's $2.0B convertible preferred, *"which DILUTES rather than earns"* — but this is
worse-shaped, because AZN's figure was at least the size of the instrument, whereas here the large
number ($6B) and the instrument ($521.4M of proceeds against 3.16M shares of dilution) are DIFFERENT
OBJECTS, and only the large one gets quoted.** ⚠⚠ **IT READS AS A $6 BILLION COMMERCIAL WIN. The
disclosure says only that if Amazon chooses to buy $6B of product over seven years, Amazon will have
earned the right to buy 3.16M shares of 3M at $164.89. NOBODY HAS COMMITTED TO BUY ANYTHING.**
⚠ **Rule (v)'s CEILING sub-shape rides along on top: "up to", cumulative, seven years, contingent on
the counterparty's own future purchasing decisions.**

**⚠⚠ RULE (iii) — A SPLIT VERDICT IN ONE DISCLOSURE, AND IT IS THE 10-15 TSMC LESSON REPEATING: APPLY
THE RULE TO THE FIGURE THE MECHANISM RUNS ON, NOT TO THE RELEASE.** The **warrant** is genuinely new —
the sources confirm no prior announcement of the warrant, the 3,162,015-share count, the $164.89 strike
or the $6B threshold (**a clean rule (iii) PASS**). The **commercial relationship is NOT** — 3M's own
word is **"EXPANDED"**, which concedes a pre-existing one of unstated size (**costume #1,
reaffirmation-shaped**). ⚠⚠ **AND THE SIGNS ARE THE WRONG WAY ROUND FOR §4, EXACTLY AS THEY WERE FOR
TSMC: THE THING THAT IS NEW (the warrant) HAS THE WRONG SIGN, AND THE THING THE MECHANISM RUNS ON (the
product revenue) IS THE PART THAT IS NOT NEW AND HAS NEVER BEEN SIZED.** A reader who tests the
release, hits the warrant's clean pass, and stops has proceeded on the wrong figure.

**⚠⚠⚠ PRICED-IN FILTER — DEFECT SHAPE SIX, NEW TODAY, AND IT FAILS TOWARD TAKING THE TRADE.
THE WINDOW CONTAINED ZERO POST-NEWS CLOSES, SO THE FILTER CERTIFIED A PASS ON A PRE-NEWS PRICE
SERIES.** The five-session window ends at the **2026-10-19 close (162.01)**; the 8-K and its coverage
landed **after that bell**. **Every close the filter read predates the event.** ⚠ **The +0.69% is
arithmetically correct and informationally empty: it measured the five sessions BEFORE the news and
reported that the news is not in the price — which is true, and useless.** ⚠ **It is not shape three
either: shape three is a real move swept up by the window; here there is no post-news close in the
window AT ALL, and the window's +0.69% nets a run-up (160.895 → 165.22) against a pull-back
(165.22 → 162.01) that have nothing to do with the event — 3M in fact closed **DOWN 1.62%** on the
announcement date, at 162.01 against the 10-16 close of 164.675, because the news broke after it
closed.** ⚠⚠ **THE DEFECT IS THE WINDOW'S RIGHT EDGE, NOT THE THRESHOLD AND NOT THE SIGN — and it is
systematic, not incidental: ANY event disclosed after a bell meets this filter in exactly this state
at the next pre-market seat, which is the seat that does all the research.**
⚠⚠⚠ **AND THE MITIGATION THE SYSTEM ALREADY HAS DOES NOT COVER IT — THIS IS THE PART FOR THE HUMAN.**
`plan_today.md` requires every BUY intent to carry a `revalidate` line precisely so the 09:35 seat can
catch an overnight gap past the 4% threshold. ⚠ **A `move` call at 09:35 READS CLOSES, and 2026-10-20's
close does not exist at 09:35 — so the re-check would return THE SAME 160.895 → 162.01 / +0.69% /
`priced_in: false`, bit for bit.** ⚠⚠ **THE REVALIDATE MECHANISM CANNOT SEE AN OVERNIGHT GAP WITH THE
TOOL IT IS POINTED AT. Catching it needs a quote-against-prior-close comparison, which is a different
call.** ⚠ **This is open items (1), (2) and (7) arriving in a new and sharper form, and only a human
may change §4 or `alpaca.py move`. IT COST NOTHING TODAY BECAUSE THE THESIS DIED AT PART 2; IT BECOMES
A WRONG TRADE THE FIRST TIME A POST-BELL EVENT PRODUCES A WRITEABLE PART 2.**
⚠ **WHAT I DID NOT VERIFY, STATED PLAINLY: the sources say MMM rose ~3.6% in extended hours. THE
ALPACA FEED CANNOT CORROBORATE THAT — `quote --symbols MMM` returns a `latestTrade` stamped
**2026-10-19T20:03Z (16:03 ET)** at 163.66 and NO 10-20 pre-market print at all, so this feed carries
no extended-hours tape. The gap's SIZE is an unverified source claim and is not relied on anywhere
above. The finding does not need it: what makes the window pre-news is the DATE of the last close in
it, which the tape does establish.**

**Outcome:** **REJECTED at part 2** — no segment, no figure, no guidance change, and the only large
number in the disclosure is a **warrant-vesting threshold, not revenue**. ⚠ **This is the best-formed
candidate the funnel has produced since GFS on 10-09 and the first in seven sessions to reach the
priced-in filter, and it still produces no trade.** ⚠ **The pull here was real and is worth naming: a
Dow component, a named hyperscaler, "$6 billion", a clean one-clause mechanism and a filter saying
"passes" — five things that each look like a reason to proceed, against one missing segment figure
that §4 makes decisive. The honest-broker rule is doing exactly the work it was written for.**

---

### T-2026-10-20-02 — Genius Electronic Optical (GSEO, Taiwan 3406) / 3M — REJECTED (§3, hard — the genuine second-order Company B, correctly reached, NOT US-LISTED)

**Company A / the news:** the same 2026-10-19 3M/Amazon arrangement as `T-2026-10-20-01` — Amazon
committing to buy 3M **optical connectivity and data-centre products** at scale.
**Company B / the candidate:** **Genius Electronic Optical Co. (GSEO, Taiwan 3406)** — named in 3M's
own collaboration disclosure as the **external manufacturing partner** for 3M's **expanded-beam optical
ferrules, co-packaged-optics solutions and related optical-interconnect** products. 3M supplies the
EBO technology, optical design and customer relationships; **GSEO supplies the precision-optics
manufacturing, production capacity and precision assembly**, and **3M is acquiring ~4.7% of GSEO** as
part of it.

**Hard filters — §3 FIRST, BEFORE THE MECHANISM WAS ELABORATED, per the standing discipline:**
- **Universe (§3): FAIL. GSEO is TAIWAN-LISTED (ticker 3406). Not US-listed → ineligible at any price,
  at any market cap, and at any level of disclosure. The thesis was stopped here and no further query
  was spent on it.**
- Priced-in / correlation: **not reached.** ⚠ *A `move` call on a Taiwan ticker is not even available,
  and would have been decorative if it were.*

**Why this one matters more than a routine §3 kill, stated carefully:** ⚠⚠ **THIS IS THE RUNG §4
EXISTS TO REACH, AND THE FUNNEL REACHED IT.** Not the headline name, not a shared-cause read-across,
not an unnamed supply base — **a specifically named, publicly traded manufacturing partner, named in
the principal's own disclosure, with a disclosed equity stake pinning the relationship down.** ⚠ **It
is the cleanest Company B this log has produced, and §3 kills it in one line.**
⚠ **AND PART 2 WOULD HAVE KILLED IT ANYWAY, WHICH IS WORTH RECORDING SO THE §3 KILL IS NOT MISTAKEN
FOR THE ONLY THING STANDING IN THE WAY:** the sources state that **no figure or percentage is reported
for how much of GSEO's revenue comes from 3M**, and do not establish that 3M is currently a material
customer at all. **Two independent kills, and §3 is the cheaper one.**

**Outcome:** **REJECTED on §3.** ⚠ **Second consecutive session in which a genuine named Company B
existed and was not buyable — observation 2 of the 3 the 10-19 entry asked for. §3 does not weigh
outcomes (the standing ELMT proof), and "but this is the best one yet" is the same pull ELMT wore.**

---

### T-2026-10-20-03 — Northrop Grumman (NOC) Q3 2026 — REJECTED (part 1 — own results, no transaction; and THE FIGURE THAT MOVED HAS NO SUPPLIER CHAIN HANGING OFF IT)

**Company A / the news:** NOC's **2026-10-20** Q3 print: sales **+7% to $11.1B**, net income **+2% to
$1.124B**, diluted EPS **$7.89 vs $7.67**. Backlog a record **$109.6B**. **Guidance: MTM-adjusted EPS
RAISED to $29.35–29.75 from its OWN prior $28.60–29.10; segment operating income RAISED to
$4.94–5.04B from its OWN $4.85–5.00B; FY2026 SALES guidance MAINTAINED at $43.75–44.25B** and adjusted
FCF **maintained at $3.1–3.5B**.
**Company B / the candidate:** **none reached.**

**1. Mechanism:** **cannot be written.** A company reporting its own quarter is **first-order**, and
the release names **no counterparty and no transaction** — the backlog figure is contracted demand in
aggregate, not an agreement with an identifiable second party. ⚠ **REJECT at part 1.**

**⚠⚠ RULE (iii) IS A CLEAN PASS HERE AND IT BUYS NOTHING — AND THAT IS THE ENTRY'S WHOLE VALUE.** The
EPS and segment-operating-income raises are measured against **NOC's OWN prior ranges**, present in the
source, which is the test the most prolific rule on the standing list asks for. **Sixteen costumes on
that list and this one is not wearing any of them.** ⚠⚠ **AND IT STILL DIES, BECAUSE OF *WHICH* FIGURE
MOVED: SALES GUIDANCE WAS MAINTAINED, UNCHANGED, AT $43.75–44.25B.** A supplier chain hangs off **what
a prime contractor BUYS**, which tracks **sales and capex** — not off **EPS and segment margin**, which
is what moved. ⚠⚠ **THE ATTEMPTED MECHANISM — *"NOC raised guidance, so its suppliers will see more
orders"* — IS CONTRADICTED BY ITS OWN SOURCE DOCUMENT: the top line NOC guided to is the SAME top line
as before. It needs an *"and also NOC will eventually have to buy more"*, and that "and also" is the
part-1 test failing.**
⚠⚠ **THIS IS `T-2026-10-15-01` (TSMC) REPEATING EXACTLY, ON THE DEFENCE SIDE AND WITH THE SIGNS EVEN
CLEANER.** There, revenue growth was raised while capex — the figure with the supplier chain — was
reaffirmed. **Here, EPS and margin were raised while sales were maintained.** ⚠ **The shape is now
established across two unrelated industries five sessions apart: A MARGIN OR EPS RAISE IS NOT A
SECOND-ORDER CATALYST, BECAUSE NOBODY SUPPLIES MARGIN. Expect it every earnings season.**
⚠ **And the defence-award finding stands behind it independently: fourteen-plus instances say US
defence programme disclosure does not produce a §4 Company B.**

**Outcome:** **REJECTED at part 1.** No `move` call — the kill is upstream of price, so one would have
been the thirteenth decorative refusal.

---

### T-2026-10-20-04 — RTX Corporation (RTX) Q3 2026 — REJECTED (rule (iii) costume #1 — guidance against CONSENSUS, not its own prior figure; rule (iv) SIXTH APPEARANCE; part 1 — own results)

**Company A / the news:** RTX's **2026-10-20** Q3 print: revenue **$24.97B, +11.1% y/y**; FY2026
revenue guidance **midpoint $97.25B**, reported as **"1.1% above analysts' estimates."**
**Company B / the candidate:** **none reached.**

**1. Mechanism:** **cannot be written** — RTX's own quarter, no counterparty, no transaction.
**REJECT at part 1.**

**⚠⚠ RULE (iii), COSTUME #1, IN ITS PUREST FORM — AND THE CONTRAST WITH `-03` ONE ENTRY ABOVE IS THE
POINT OF LOGGING BOTH.** The only benchmark the source supplies for RTX's guidance is **"above
analysts' estimates"** — **consensus**, not **RTX's own prior range**, which appears nowhere in the
available reporting. ⚠ **A figure above consensus establishes nothing about whether RTX's own outlook
MOVED, and the gap between a guide and a consensus BELONGS TO NOBODY** (the standing Cigna
$280.0B-vs-$287.2B instance). ⚠⚠ **NOC AND RTX REPORTED THE SAME MORNING AND SIT ON OPPOSITE SIDES OF
THIS TEST: NOC's raise is against its OWN prior range (a clean pass that still dies on which figure
moved); RTX's is against CONSENSUS (not establishable in either direction). 09-29 produced the same
pass/fail pair one entry apart — IOVA against AAR. The test is cheap, it discriminates, and it
discriminated again today.**

**⚠⚠ RULE (iv) — RTX IS NOW AT SIX APPEARANCES IN NINE SESSIONS ACROSS FIVE DISTINCT DISCLOSURES**
(09-29 AMRAAM $20.7B · 10-02 SM-6 *"up to"* $24.4B · 10-09 SM-3 *"up to"* $6.3B · 10-12 the SM-3 award
re-served twice in one run · 10-14 USAF Nuclear Weapons Center *"up to"* $8B · **10-20 the Q3 print**)
**AND IT HAS DIED AT PART 1 EVERY SINGLE TIME.** ⚠ **Today's arrival is a DIFFERENT KIND of disclosure
— an earnings print rather than a programme award — and it dies at the same rung for the same reason:
a first-order disclosure by a company that names no second party.** ⚠⚠ **THAT IS THE STRONGEST FORM OF
RULE (iv) YET: a new disclosure TYPE on a recurring ticker is still not fresh evidence when the kill is
structural. A ticker that keeps arriving and keeps dying the same death is telling you about its
industry's disclosure practice, not about a candidate maturing. Expect RTX again; the answer is already
written.**

**Outcome:** **REJECTED at part 1,** with rule (iii) failing independently. No `move` call — decorative.

---

### T-2026-10-20-05 — MKS Inc. (MKSI) / TTM Technologies (TTMI) — Ophir Optics $650M — REJECTED (merger arbitrage is not in §4; rule (viii) — consideration paid OUT by one buyable leg and IN to the other; part 1 — both legs are named parties)

**Company A / the news:** **2026-10-19 8-K** — **MKS Inc.** agreed to sell its **Ophir Optics**
business to **TTM Technologies** for **$650M all-cash**, subject to customary closing adjustments.
Both parties **US-listed**.
**Company B / the candidate:** **none exists.** Both legs are named parties to the transaction.

**1. Mechanism:** **cannot be written without an "and also".** ⚠ **MERGER AND DIVESTITURE
ARBITRAGE IS NOT IN §4 — the standing item covers three such deals in two sessions (onsemi/Synaptics,
Schneider/PTC, CHRW/RXO) and the answer needed no query then or now.** §4 asks whose **economics
change** because of an event at **another** company; in an asset sale **both** parties are first-order,
and the asset itself is not listed.
**2. Dollar path:** ⚠ **RULE (viii), BOTH SIGNS IN ONE TRANSACTION, WHICH IS UNUSUAL ENOUGH TO
RECORD:** the **$650M is consideration paid OUT by TTM** (wrong sign at the acquirer — the GEHC/Sofie
and CHRW/RXO shape) **and capital paid IN to MKS** (wrong sign at the seller — the TotalEnergies/GIP
and SOCAR shape). ⚠ **Neither leg has disclosed segment REVENUE attached to it. The same figure fails
rule (viii) twice, in opposite directions, depending on which side you stand on.**
**3 / 4:** not reached.

**Hard filters:** not reached — the kill is at part 1, upstream of price and upstream of §3.
⚠ *Both tickers are plausibly US-listed and TTM is plausibly below the §3 $10B floor; NEITHER WAS
PULLED, because a cap figure on a candidate that does not exist documents nothing.*

**Outcome:** **REJECTED at part 1.** ⚠ **Noted for the pattern, not for the trade: this is the second
optics/photonics transaction in the SAME 24-hour window** (with the 3M/Amazon optical-connectivity
arrangement) **— and a theme appearing twice is a reason for the correlation check to be stricter if
either ever produces a candidate, NOT corroboration that the theme is an opportunity. A shared cause is
not a mechanism, and that holds for a shared THEME across two unrelated transactions too.**

---

### T-2026-10-20-06 — §3 / non-qualifying / disposed-repeat sweep of TWELVE items — REJECTED (disposed as one, ZERO drill queries spent)

Every remaining item the three scans returned, with the rung that kills it. ⚠ **Each of these was
disposed on the face of the scan output, by a rule already on the standing list. No drill query was
spent on any of them, which is the entire point of keeping the list.**

| Item | Figure | Killed at |
|---|---|---|
| **BAE Systems** / US DoW APKWS framework, up to 7 years, capacity to 35,000 kits/yr | **no value disclosed** | **§3 — UK-listed.** Plus **part 2** (capacity in kits, not dollars, not revenue) and the standing defence-award finding. |
| **General Dynamics Mission Systems** / US Navy nuclear cruise-missile fire control | **$194M modification** | **part 2** — $194M against GD revenue ~$50B is **~0.4%**, an order of magnitude under §4's 10% floor. Plus **rule (iii)** (a *modification*, original award date not stated) and the defence-award finding. |
| **GE Vernova** / Côte d'Ivoire Songon 372MW, 9E turbine + generator | **no value disclosed** | **part 2** — no figure at all. **Rule (iv)**: GEV's third appearance in six sessions. |
| **Elbit Systems** / EXTRA-MR + PULS to "a European customer" | **~$235M** | **rule (v)** — counterparty **unnamed**, and the funnel volunteered it is a government-to-government framework. **§3** independently (Israel-domiciled, below-floor ADR shape). |
| **Aquirian** / Western Energetics, Mt Ida extension to 2030 | **~A$21M** | **§3** — Australian microcap. **Rule (iii)** — an *extension*. **Part 3** — a 2030 horizon. |
| **Wärtsilä** / Origem Energia, 7 Brazilian projects, 371MW | **no value disclosed** | **§3** — Finnish-listed. **Rule (iii)** — source says the engine supply was **"previously announced."** |
| **Tower Semiconductor / Semtech** — expanded multiyear dedicated SiGe capacity, US + Israel + Japan | **no value disclosed** | **part 2** — no figure, so no dollar path. **Rule (iii)** — *"expanded"*. **Part 1** — both parties named, so the candidate IS the headline. ⚠ *§3 status of TSEM/SMTC not pulled: three kills upstream.* |
| **Anthropic / Nscale** compute arrangement | **~$45B** | **not an announcement** — reported as **still under discussion, terms not finalised.** Plus the **PRE-IPO CONTRACT BOOK** shape already disposed on Nscale's $103B, and **Anthropic is not listed.** |
| **Samsung Bioepis / Brazilian Ministry of Health** | **none disclosed** | **one party is a GOVERNMENT** (the standing "a government action is not a Company A" object) **+ no figure + §3.** |
| **Broadcom / NTT Docomo** | **terms not disclosed** | **part 2** — no figure. |
| **PT Krakatau Steel** / Australian Steel Traders, HRC/HRS | **up to 30,000 t/yr, NO dollar amount** | **unit is not money** (the 10-12 sovereign-diesel false-positive's companion failure) **+ §3** (Indonesian). |
| **JPMorgan** — $230B financed under a **$1.5T** national-security initiative | **$230B / $1.5T** | **rule (v) + no named recipient** — the source states it does not identify the financed companies or project-level commitments. ⚠ **THE LARGEST NUMBERS IN THE WHOLE RUN AND THE EMPTIEST: a trillion-dollar FINANCING CEILING AVAILABLE TO SOMEBODY ELSE, unnamed. Rule (viii)'s Brookfield/Bloom $25B and Tesla $30B shape, two orders of magnitude up. SCALE MAKES IT MORE CONVINCING, NOT LESS.** |

**⚠ RE-SERVE RATE, SIXTH CONSECUTIVE SESSION: GE Vernova** returns for a **third** time in six sessions
(10-15 Venture Global frame agreements, 10-19 in the sweep, 10-20 Côte d'Ivoire) and **Elbit's unnamed
European customer** is the same rule (v) blank as 10-19's. ⚠ **Reading the log before the tape cost one
`grep` and saved three drills — the sixth session running that it has.**

**Outcome:** **ALL TWELVE REJECTED.** ⚠ **Nine of the twelve carry either no dollar figure at all or a
figure in the wrong unit, at the wrong party, or available to nobody in particular. That ratio is the
funnel's actual inventory and it has not moved in six weeks.**

---

### 2026-10-19 (08:13 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, all exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$99,852.41** at
pre-flight). `clock` at **08:13:13** reads `is_open: false`, `next_open` **2026-10-19T09:30**,
`next_close` **2026-10-19T16:00** — **both carrying TODAY's date: the pre-market full-session
signature, read off the DATES and not the boolean. Not a holiday, not an early close.** Window
screened: **the completed 2026-10-16 session and the weekend into Monday — THREE CALENDAR DAYS,
ONE TRADING DAY.** The Monday shape; expected and noted. **Three broad scans plus two drills, all
exit 0. FIVE theses, ALL FIVE REJECTED.** ⚠ **Written deliberately short against open human item
(9): the corpus grew +38.3% last week and a tighter entry is the only lever this seat holds.**

**⚠⚠ ALL THREE BROAD FRAMINGS VOLUNTEERED THE ABSENCE AGAIN (3 for 3), AND THE
SEGMENT-QUANTIFICATION FRAMING MAKES IT FIFTEEN CONSECUTIVE SESSIONS — 09-29 → 10-19 UNBROKEN.**
Verbatim: framing one, *"only one announcement clearly satisfies all stated conditions"* (and that
one is §3-dead) · framing two, *"No qualifying disclosure can be established from the available
results"* · framing three, *"does not identify any qualifying event."*

**⚠⚠⚠ THE BINDING CONSTRAINT MOVED THIS SESSION, AND IT IS THE FIRST TIME IT HAS: FROM PART 1 TO
§3.** Five sessions running, theses died because **no Company B existed** (10-12 zero eligible
tickers at part 1 · 10-13 one · 10-14 two · 10-15 two · 10-16 three). **Today the funnel delivered
THREE GENUINE TWO-PARTY TRANSACTIONS — the most it has ever produced — and §3 killed all three
before part 1 was reached:** 44.01/Frontier (`-04`), **NOVONIX/PowerCo** and **Orion
Minerals/Glencore** (both in the sweep). ⚠ **Company B now EXISTS and is NOT US-LISTED. That is a
different failure from an absence, and one session is not a finding — recorded for the next three
reviews to test, not acted on.**

**⚠ ZERO `move` CALLS AND ZERO MARKET CAPS SOURCED — THE SIXTH CONSECUTIVE SESSION, AND CORRECT
RATHER THAN OMITTED.** Not one candidate reached the priced-in filter: every kill was §3, part 1,
rule (v) or rule (viii), all upstream of price. The one US-listed name with a real disclosure in the
window (**Cleveland-Cliffs**, Q3 beat) dies at **part 1 — its own results** — which is upstream of
§3 as well, so a `move` would have been the **12th decorative refusal** and a cap figure would have
documented nothing. ⚠ **A §3 figure exists to make an ACCEPTED thesis auditable; there is no
accepted thesis.**

**⚠⚠ THE RE-SERVE RATE IS NOW 5 FOR 5 SESSIONS:** **TSMC Q3** (`T-2026-10-15-01`) and **Schneider
Electric** (10-16 sweep) both came back under a 10-19 dateline, and **LS Electric** arrives for a
**third** time on a genuinely new $125M deal — **rule (iv) exactly: a recurring issuer whose kill is
structural.** ⚠ **Reading the log first cost one `grep` and saved three drills.**

**⚠ THE 10-16 DEFERRAL IS DISCHARGED, NOT DROPPED.** `T-2026-10-16-04` deferred the five pre-open
bank prints because they reported *after* that run. **They have now reported and were screened** —
`T-2026-10-19-02`. A deferred item that is never reached is indistinguishable from one that was
missed; this one was reached and died.

---

### T-2026-10-19-01 — Russia sanctions suspension → US airline / refiner fuel cost lines — REJECTED (part 1 — no Company B; rule (viii); rule (vi) on a 60-day reversible measure)
**Company A / the news:** Trump signed an executive order on **2026-10-16** suspending the sanctions,
restrictions and duties provided for by the **Graham Act**, including proposed duties of up to 100% on
major buyers of Russian oil, two days before they were due to take effect on **10-18**. Brent fell
~1.8% into Monday. Rubio: the President wants **up to 60 days** to assess the economic effect; the
order carries **no fixed end date**.
**Company B / the candidate:** a US airline or refiner whose fuel/feedstock cost line falls.

**1. Mechanism (one sentence):** **FAILS, AND IT FAILS AT THE SUBJECT.**
> *"The sanctions suspension causes [a US airline]'s fuel expense line to fall because more Russian
> barrels reach the market."*

⚠ **There is no Company A in the §4 sense: ONE party (the US government), no transaction, no named
counterparty.** The drill asked explicitly and the source confirms **no individual Russian bank, oil
company or refinery is named as exempted.** ⚠⚠ **And the sentence cannot be completed without
"…*and also* the barrels actually arrive, *and also* crude stays down, *and also* the carrier does not
hedge it away" — three second clauses, which is the mechanism test failing three times over.**
⚠ **This is the root cause the eight standing rules share, in its purest form: I would be supplying
the entire causal chain and then pointing at a Brent print adjacent to it.**

**2. Dollar path:** **FAILS — rule (viii) read broadly.** The only quantified figure in the window is
a **proposed diesel-export arrangement of ~2.3M bbl in October rising to ~7.6M bbl/month** — a
**political announcement's volume, not segment revenue or a disclosed cost at any Company B**, and the
source states it is **not established that these volumes were released by the waiver itself.** ⚠ **The
drill asked directly whether any US airline, chemical company or refiner had disclosed a guidance
change or a quantified fuel figure between 10-16 and 10-19: *"no disclosed guidance change or
quantified fuel/feedstock-cost figure."* No company, no figure.**

**3. Timing window:** **FAILS — rule (vi).** A measure suspended for a **60-day assessment with no
fixed end date** can reverse inside one quarter. ⚠ **A cost tailwind that may be withdrawn before it
is ever reported is not a two-quarter thesis; it is a headline with a timer on it.**

**4. Invalidation:** **not reached** — parts 1–3 all fail.

**Hard filters:** **not reached.** Priced-in, correlation and §3 all sit downstream of a mechanism
that has no subject. ⚠ *(Correlation is trivially clear in any case — zero open satellite positions,
so no driver can collide.)*

**Outcome:** **REJECTED.** The largest genuinely new event of the window and it is structurally dead
at the first test. ⚠ **Worth naming plainly, because it is the version of this error that is hardest
to see: the event is real, dated, market-moving and verifiable, and it still contains no second
company. A big true event is not a thesis.**

---

### T-2026-10-19-02 — the Friday bank cohort (TRV · TFC · MTB · RF · CFG) — REJECTED (part 1 — no cross-company disclosure in any of five releases; the 10-16 deferral discharged)
**Company A / the news:** all five reported **Q3 2026 on 2026-10-16**, after the 10-16 pre-market run.
Travelers: net income **$1.917B**, core income **$1.947B**.
**Company B / the candidate:** none found.

**1. Mechanism (one sentence):** **FAILS — THERE IS NO CANDIDATE TO PUT IN THE SENTENCE.** The drill
asked each of the five for a technology-vendor contract, an outsourcing agreement, a named
acquisition or divestiture counterparty, a disclosed exposure to a named borrower, or a quantified
spend commitment to a named supplier. **Five rows, five blanks.** A bank's quarterly release is a
report on **its own** balance sheet; there is no second party in it by construction.

**2. Dollar path:** **not reached.** The figures that exist (TRV's $1.917B) are **Company A's own
earnings** — rule (viii)'s plainest shape.
**3. Timing window / 4. Invalidation:** **not reached.**

**Hard filters:** **not reached** — part 1 is upstream.

**Outcome:** **REJECTED, and the 10-16 deferral is hereby DISCHARGED.** ⚠⚠ **ONE HONEST QUALIFIER,
RECORDED BECAUSE IT CUTS AGAINST THE CONCLUSION: the source states the primary releases were not in
its result set and that *"no such disclosure reported" should not be treated as proof that the
releases contained none."* ⚠ **So this is a rejection on ABSENCE OF EVIDENCE, not on evidence of
absence, and it is labelled as such.** The decision is unchanged — §4 requires a disclosed mechanism
before a buy, so an unfound disclosure and a nonexistent one produce the same answer today — but
**the two are not the same fact, and a log that blurs them would be overstating what this run
established.**

---

### T-2026-10-19-03 — data-centre project delays / CoreWeave bond distress → equipment-supplier read-through — REJECTED (rule (v) — no named project, no named supplier; rule (viii) — an analyst estimate; and it is the weekly review's own finding being re-served as an opportunity)
**Company A / the news:** CoreWeave's Oct-2031 bonds briefly yielded **above 16%** on 10-16, other
notes at **75–78c** (~16.4–16.5%); bonds financing data-centre construction for **Meta, Nvidia and
Oracle** below face value; press reports of "numerous large data-centre projects delayed or blocked"
on power, water, noise and air-pollution constraints.
**Company B / the candidate:** none establishable.

**1. Mechanism (one sentence):** **FAILS — rule (v), and this is the rule's single cleanest
instance.** The drill asked for the specific projects, operator, location, MW or dollar size, and the
**named suppliers who themselves disclosed an order deferral, backlog cut or guidance cut.** Verbatim:
*"do not identify any specific delayed or cancelled U.S. data-centre project, nor do they name an
equipment supplier or contractor that disclosed a resulting order deferral."* ⚠ **"Numerous projects"
is a market-structure claim about an industry, not a transaction. The source left the blank; filling
it in is not research.**

**2. Dollar path:** **FAILS — rule (viii) read broadly.** The only quantity offered is **Dan Ives'
estimate that 5–10% of planned projects will not be built** — ⚠ **an analyst estimate, which is not a
disclosed figure at any company, and the bond yields are a SECONDARY-MARKET PRICE, not revenue.**

**3. Timing window / 4. Invalidation:** **not reached.**

**Hard filters:** **not reached.** ⚠ *(And §3 would close the obvious door anyway: CoreWeave's
distress is expressed in its BONDS, and a debt instrument is not §3-eligible.)*

**Outcome:** **REJECTED.** ⚠⚠ **AND THE REASON THIS ENTRY MATTERS IS THE DIRECTION IT ARRIVED FROM.**
Friday's weekly review found the **AI / data-centre theme unwound**, taking every headline row of the
reject board with it — and it filed that explicitly as **the three-review promotion rule's result,
NOT as a new finding in the opposite direction.** ⚠ **Today the funnel served the same unwind back as
a buyable idea, and the temptation is to treat last week's work as corroboration for a trade pointing
the other way. It is not: the unwind is a TAPE observation, this is a press narrative with no named
party, and §3 forbids expressing the short side at all. The finding stays a finding; it does not
become a thesis.**

---

### T-2026-10-19-04 — 44.01 / Frontier $11.7M carbon-removal offtake — REJECTED (§3 both legs; part 2 catastrophically; rule (viii) — capital paid OUT by the only buyable leg)
**Company A / the news:** **2026-10-19** — **Frontier** agreed offtake with **44.01** for permanent
removal and storage of **20,932 tonnes of CO₂** between 2028 and 2031, **US$11.7M**. ⚠ **The single
item in the whole window that framing one accepted as satisfying its conditions — both parties named,
a specific transaction, a disclosed figure, and the figure is revenue to the supplier.**
**Company B / the candidate:** 44.01 (the supplier), or a US-listed member of the Frontier buyer group.

**1. Mechanism (one sentence):** writable in one clause for the supplier leg — *"Frontier's purchase
causes 44.01's carbon-removal revenue to rise because Frontier is paying for 20,932 tonnes of
removal."* ⚠ **The sentence is clean. Everything else fails.**

**2. Dollar path:** **FAILS, AND BY THREE ORDERS OF MAGNITUDE ON THE BUYABLE LEG.** 44.01 is
**Omani and privately held — not buyable at all.** Frontier is a **buyer coalition**, so the only legs
with a ticker are its US-listed members, and for them **$11.7M spread across a multi-member coalition
and four years is immaterial against revenue measured in the hundreds of billions** — nowhere near
§4's 10%-of-revenue floor. ⚠ **It is also rule (viii)'s shape exactly: capital paid OUT by the
buyable leg. The money is a COST to every company here that one could actually own.**

**3. Timing window:** **FAILS — rule (vi).** Delivery runs **2028–2031**, ~**8 to 20 quarters** out
against §4's two-quarter ceiling.
**4. Invalidation:** **not reached.**

**Hard filters:** **§3 — FAIL on both legs** (44.01 not US-listed and not public; Frontier not an
issuer). Priced-in and correlation **not reached.**

**Outcome:** **REJECTED.** ⚠ **Logged at full length precisely because it is the window's only
complete two-party transaction with a real figure — and it still fails on size, listing and horizon.
A disclosure that passes the test the last fifteen sessions kept failing is not thereby a trade;
it just fails further down.**

---

### T-2026-10-19-05 — §3 / non-qualifying / disposed-repeat sweep of NINE items — REJECTED (disposed as one, zero drill queries spent)
**The rule:** an item whose §3 or structural kill is visible in the broad-scan text itself gets no ID
and no drill query. Each is named with its reason so the next run can see it was reached.

**§3 — NAMED TWO-PARTY TRANSACTIONS THAT ARE SIMPLY NOT US-LISTED (two — and see the session note,
this is where the constraint moved):** **NOVONIX / PowerCo** — ⚠ **both parties named, and the 10-19
announcement REPLACED a prior BINDING offtake with a framework under which volume and price are
negotiated later, so the disclosure DELETED its own dollar figure. Part 2 fails on a release that
previously would have passed it** (NVX is ASX-primary and far below §3's floor; PowerCo is VW's
German subsidiary) · **Orion Minerals / Glencore** **US$250M offtake, $40M first phase** — a South
African mining transaction, neither leg US-listed.
**RULE (v) — COUNTERPARTY UNNAMED (three):** **Elbit Systems** **$235M** EXTRA-MR rockets and PULS
launchers to *"a European country"* — ⚠ **an unnamed sovereign ministry, and the figure is the
ANNOUNCER's own revenue (rule viii)** · **Samsung Electro-Mechanics**, figure disclosed, customer only
*"a global major company"* · **LS ELECTRIC** **$125M** US data-centre power deal for *"a U.S. big tech
company"* — ⚠ **THIRD APPEARANCE, rule (iv): genuinely new transaction, structurally identical kill
to 10-13 (Bloom Energy $138.5M) and the 10-15 re-serve. Korea-listed on top.**
**PART 1 — OWN RESULTS, NO COMPANY B (two):** **Cleveland-Cliffs** Q3 profit beat (⚠ **the only
US-listed name with a real disclosure in the window; the beat is against ANALYST ESTIMATES, which is
rule (viii)'s consensus shape, and §3's cap floor is not even reached before part 1 kills it**) ·
**Delta's** fuel-cost forecast cut — **dated 10-14, outside the window (rule iii), and it is Company
A's own guidance.**
**NO COMPANY A / MACRO OR GOVERNMENT OBJECT (two):** **September industrial production +0.7%,
manufacturing +0.3%, capacity utilisation 76.9%** · **CPI / PPI / import prices and the Oct 27–28 FOMC
hold expectation** — ⚠ **ONE party, no transaction. Already disposed at `T-2026-10-12-05` and
`T-2026-10-13-08`; NO NEW ID MINTED, following the 10-14/10-15/10-16 precedent exactly. A government
statistical release has one party whether it is scheduled, printing or printed.**
**ALREADY DISPOSED — RE-SERVED, NOT RE-LITIGATED (named as re-serves, not as new disposals):**
**TSMC Q3** (`T-2026-10-15-01`) · **Schneider Electric** (10-16 sweep, §3 French-listed).

**Hard filters:** not reached on any item — every one died at **§3**, **part 1**, **rule (iii)**,
**rule (iv)**, **rule (v)** or **rule (viii)**, all upstream.

**Outcome:** **REJECTED, nine items, one entry, zero drill queries spent.**

---

### 2026-10-16 (08:13 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, all exit 0 (`trading_enabled: true`, LIVE paper, broker equity **$100,397.17** at
pre-flight). `clock` at **08:13:02** reads `is_open: false` with `next_open` **2026-10-16T09:30** and
`next_close` **2026-10-16T16:00** — **both carrying TODAY's date**, the **PRE-MARKET full-session
signature, read off the DATES and not the boolean. Not a holiday, not an early close.**
Window screened: **the completed 2026-10-15 session and overnight into Friday** — a
**ONE-TRADING-DAY, ONE-CALENDAR-DAY** window, the ordinary shape. **Three broad Perplexity scans plus
two drills, all exit 0.** **FIVE theses written, ALL FIVE REJECTED.**

**⚠⚠ ALL THREE BROAD FRAMINGS VOLUNTEERED THE ABSENCE, AND THE SEGMENT-QUANTIFICATION FRAMING MAKES
IT FOURTEEN CONSECUTIVE SESSIONS (09-29 → 10-16 UNBROKEN).** Verbatim, framing one: *"no clearly
documented US corporate announcement in the specified window with a confirmed cross-company
operational effect."* Framing two (the earnings-window drill): *"No company can be confirmed … as
having disclosed all of the requested elements."* Framing three (knock-on): *"No qualifying case can
be identified from the available reports."*

**⚠⚠ THE RE-SERVE RATE IS NOW 4 FOR 4 SESSIONS, AND TODAY'S RE-SERVE IS ONE DAY OLD.** **TSMC's Q3
print** came back under a 10-16 dateline (*"TSMC just posted record profit"*) — **disposed YESTERDAY at
`T-2026-10-15-01`**. **September PPI / retail sales** came back as well, **disposed at
`T-2026-10-12-05` and `T-2026-10-13-08`**. ⚠ **Reading the log first cost one `grep` and saved two
drills.**

**⚠⚠ ZERO `move` CALLS AND ZERO MARKET-CAP FIGURES SOURCED — AND BOTH ARE CORRECT, NOT OMISSIONS.**
The funnel delivered **THREE US-listed names into part 1 this session — `JBHT`, `AA` and `NVDA`
(contextual) — the most it has ever delivered — and all three died AT part 1**, which is upstream of
both the priced-in filter and the §3 universe check. ⚠ **A `move` on any of them would have been
DECORATIVE (the 9th, 10th and 11th such refusals), and so would sourcing a market cap: a §3 figure
exists to make an ACCEPTED thesis auditable, and there is no accepted thesis.** ⚠⚠ **THE PROGRESSION
IS NOW FIVE SESSIONS LONG AND POINTS ONE WAY — 10-12 zero eligible tickers at part 1 · 10-13 one ·
10-14 two · 10-15 two · 10-16 THREE. THE BINDING CONSTRAINT SITS ABOVE THE PRICE CHECK, AND THE FUNNEL
GETTING BETTER AT DELIVERING BIG ELIGIBLE TICKERS HAS BOUGHT NOTHING.**

**⚠ THE FIVE PRE-OPEN BANK PRINTS (TRV, TFC, MTB, RF, CFG) LAND AFTER THIS RUN AND ARE NOT EVENTS
YET** — disposed below at `T-2026-10-16-04`, not carried as a lead.

---

### T-2026-10-16-01 — Taiwan / TEEMA $4B Texas AI industrial park — REJECTED (rule (v) NEW COSTUME — the most fillable blank this funnel has ever produced; part 1; part 3; rule (viii))
**Company A / the news:** Taiwan's Ministry of Economic Affairs, reported **2026-10-16** (Bloomberg,
Focus Taiwan, Reuters/Yahoo), plans US industrial parks to host an AI-hardware supply chain, **starting
with a Texas complex estimated at up to $4 billion**, each park put at **$2–4B**. **Private businesses
provide the funding; the government provides loan guarantees and regulatory coordination. The
fundraising body named is the Taiwan Electrical and Electronic Manufacturers' Association (TEEMA).**
**Company B / the candidate:** **NONE REACHED.** The drill asked for every company that has signed,
committed to, or been contractually named. Source, verbatim: the plan *"does **not** identify any
company as having signed, committed to, or been contractually named as a participant"*, and
*"Nvidia, TSMC, and Foxconn had made no commitment to the parks."*

**1. Mechanism (one sentence):** **NOT WRITTEN.** There is no Company B to put in the sentence.
**2. Dollar path:** **FAILS — rule (viii) read broadly.** The **$4B is a PROJECT-LEVEL COST ESTIMATE**.
It is **not segment revenue at any Company B**; it is not revenue at all; and *"the reported $4 billion
is a project-level estimate, not an announced contribution by Nvidia, TSMC, Foxconn, Wistron, or
another named company."* **No amount is attributable to any named company.**
**3. Timing window:** **FAILS DECISIVELY — rule (vi).** Source: **no city, county, site or address**;
**no construction start date, completion date, operating date, or schedule for subsequent sites.** ⚠ **A
park with no disclosed groundbreaking cannot show in any company's reported results inside §4's
two-quarter ceiling. Part 3 kills it in one step.**
**4. Invalidation:** not reached.

**Hard filters:** **NOT REACHED** — died at part 1, upstream of all three. ⚠ **No `move` call, no
market cap sourced. Both declined deliberately.**

**Outcome:** **REJECTED.**
⚠⚠ **AND IT IS A GENUINELY NEW RULE (v) COSTUME, WORTH THE ENTRY ON THAT GROUND ALONE: AN UNNAMED
PRIVATE CONSORTIUM ORGANISED BY A NAMED TRADE ASSOCIATION — WHICH MEANS THE BLANK COMES WITH A
LOOKUPABLE MEMBERSHIP ROSTER.** ⚠ **Every earlier rule (v) blank was diffuse (an "unnamed supply
base") or singular and redacted ("Party A"). THIS ONE IS NEITHER: TEEMA is a real organisation whose
members are published, many of them listed, so a run can construct a candidate list in one search and
feel it has been *sourced*. ⚠⚠ **A MEMBERSHIP ROSTER IS A LIST OF COMPANIES THAT COULD PARTICIPATE. IT
IS NOT A TRANSACTION, AND THE DISTANCE BETWEEN THE TWO IS THE WHOLE OF §4.** The priors arrive
instantly and unbidden — Texas industrial REITs, electrical equipment (ETN, EMR, PWR, VRT),
engineering and construction — ⚠ **and not one of them is named in the source. THE SOURCE LEFT THE
BLANK; FILLING IT IN IS NOT RESEARCH.**
⚠ **Note also the §3 shape of the named parties: Foxconn and Wistron are TAIWAN-LISTED; the only
US-listed names in the story (NVDA, TSM's ADR) are named as intended *beneficiaries* of a plan they
have not committed to.**

---

### T-2026-10-16-02 — J.B. Hunt (JBHT) Q3 2026 → the rail read-through (UNP / NSC / BRK) — REJECTED (part 1 — no transaction; rule (iii) on the read-through; part 2 on BNSF-inside-BRK)
**Company A / the news:** **J.B. Hunt Transport Services (JBHT)** reported Q3 2026 after the close
**2026-10-15**: total operating revenue **$3.68B, up 20%** from $3.05B; revenue ex-fuel-surcharge
**$3.01B, up 13%**; operating income **$247.1M, up 2%**; GAAP EPS **$1.82**; fuel surcharge revenue
**$670.8M**; and **record intermodal volumes, up 8% year over year**, with higher driver, fuel, claims
and medical costs partly offsetting the revenue growth.
**Company B / the candidate:** **the Class I railroads that haul JBHT's intermodal containers** —
reached as a constructed chain, **not supplied by any source.** Source, verbatim: *"No named external
counterparty company with a specific dollar value appears in the reported Q3 results … J.B. Hunt's
release was solely its own quarterly financial results and operating commentary."*

**1. Mechanism (one sentence):** **NOT WRITTEN HONESTLY.** The best available sentence is *"record
intermodal volumes at JBHT cause its rail haulage partners' intermodal segment revenue to improve
because JBHT pays them per container moved"* — ⚠ **and it describes an ONGOING COMMERCIAL
ARRANGEMENT, NOT AN EVENT. Nothing changed between the railroads and JBHT on 2026-10-15; a quarterly
results release by the customer is not a new transaction with the supplier.**
**2. Dollar path:** **FAILS, AND ON TWO COUNTS.** (a) **No dollar figure is attributable to any
railroad** — JBHT disclosed its own revenue, not its purchased-transportation payments to any named
carrier. (b) ⚠ **JBHT's eastern/western intermodal haulage runs over BNSF, which is NOT SEPARATELY
BUYABLE — it is a wholly owned Berkshire Hathaway subsidiary, and BNSF's revenue is a single-digit
share of BRK's total revenue, well under §4's 10% materiality floor.** ⚠⚠ **THAT SHARE IS MY OWN
ESTIMATE AND WAS **NOT SOURCED THIS RUN** — it is recorded as a corroborating reason, NOT as the kill.
The kill is part 1.**
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:** **NOT REACHED.** ⚠ **No `move` on UNP, NSC, CSX or BRK; no market cap sourced for
any of them.**

**Outcome:** **REJECTED.**
⚠⚠ **THIS IS THE STRONGEST PULL IN TODAY'S WINDOW AND IT IS RECORDED AS SUCH, BECAUSE IT IS EXACTLY
THE HONEST-BROKER FAILURE §4 DESCRIBES.** A **+20% revenue print with record volumes** at a logistics
company reads as a *discovery about the freight cycle*, and the second-order chain assembles itself in
one step without any source being asked. ⚠ **AND IT DIES ON A RULE ALREADY IN THE BOOK: rule (iii) —
RAIL VOLUMES ARE THE RAILROADS' OWN WEEKLY PUBLIC DISCLOSURE (AAR carload and intermodal reports).
There is NOTHING in JBHT's release that is new to a railroad's own disclosure. The read-through is not
early; it is a week late and public.** ⚠ **It is the competitor/customer earnings read-across — the
SHARED-CAUSE object — which §4 kills every time, and the 10-15 carry-forward predicted it would
arrive.**

---

### T-2026-10-16-03 — Alcoa (AA) Q3 2026 + South32 shareholder approval — REJECTED (part 1 — own results; §3 on the one named external party; rule (viii) — GEHC/Sofie costume repeating)
**Company A / the news:** **Alcoa (AA)** reported Q3 2026 on **2026-10-15**: revenue **$3.704B** vs
$2.995B a year earlier; net income **$483M / $1.81 diluted EPS** vs $232M / $0.88; adjusted EPS
**$1.82**; alumina production **2.5M metric tons**, aluminium **649,000 metric tons**; quarterly
dividend **$0.10**, payable Nov 13 to holders of record Oct 27. The release also stated that
**South32 shareholders approved Alcoa's acquisition on 2026-10-15.**
**Company B / the candidate:** **NONE.** The release names **exactly one external company — South32 —
and it is on the wrong side of the transaction in two separate ways.**

**1. Mechanism (one sentence):** **NOT WRITTEN.** No external beneficiary is named. The production and
earnings figures are Alcoa's own.
**2. Dollar path:** **FAILS — rule (viii), AND IT IS THE GEHC/SOFIE COSTUME ARRIVING AGAIN.**
**Acquisition consideration flows OUT of the buyable leg (Alcoa) to the acquired party.** ⚠ **And this
instance is weaker still than GEHC's: the cited report discloses NO DOLLAR VALUE for the transaction at
all, so there is not even a wrong-direction figure to reject — there is no figure.**
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:** **§3 FAILS ON THE ONLY NAMED COUNTERPARTY — South32 is ASX-listed, not US-listed.**
⚠ **Priced-in and correlation NOT REACHED; no `move` call on AA; AA's market cap NOT SOURCED, because
AA is the first-order headline name and §4 does not buy it at any price.**

**Outcome:** **REJECTED.** ⚠ **A strong earnings beat at a US-listed >$10B-plausible industrial is the
most ordinary-looking lead this funnel produces and it is first-order every time. The one external
name in the release is simultaneously (a) not US-listed, (b) being acquired rather than selling
anything, and (c) attached to no disclosed figure. THREE INDEPENDENT DOORS, ALL CLOSED.**

---

### T-2026-10-16-04 — the Friday pre-open bank cohort (TRV · TFC · MTB · RF · CFG) — REJECTED (rule (iii), PUREST FORM — they report AFTER this run)
**Company A / the news:** Nasdaq's pre-market earnings list for **2026-10-16** names **Travelers
(TRV), Truist Financial (TFC), M&T Bank (MTB), Regions Financial (RF) and Citizens Financial (CFG)**
as reporting **before today's open** — i.e. **after this 08:13 run and before the 09:35 run.**
**Company B / the candidate:** **NONE, AND NONE CAN EXIST YET.**

**1. Mechanism (one sentence):** **UNWRITABLE — THE EVENT HAS NOT HAPPENED.** Source on the cohort:
*"No qualifying disclosure established from the available results"* for every one of the five.
**2. Dollar path:** no figures exist to path.
**3. Timing window:** n/a.
**4. Invalidation:** n/a.

**Hard filters:** not reached.

**Outcome:** **REJECTED — `T-2026-10-13-08` precedent applied exactly.** ⚠⚠ **A SCHEDULED RELEASE IS
NOT AN EVENT. This is rule (iii) at its earliest possible failure point: the question "is this new to
the company's own disclosure?" cannot even be asked of a disclosure that does not exist.** ⚠ **The
cohort is NOT carried forward as a lead for the 09:35 seat either: five bank earnings reports are
FIRST-ORDER financial results, and §4 buys Company B, not Company A. If one of them discloses a named
external counterparty with a dollar figure, that is Monday's window, not a reason to pre-authorise
anything today.**

---

### T-2026-10-16-05 — §3 / non-qualifying / disposed-repeat sweep of TEN items — REJECTED (disposed as one, ZERO drill queries spent)
**The rule:** an item whose §3 or structural kill is visible in the broad-scan text itself does not get
its own ID and does not get a drill query. Each is named with its reason so the next run can see it was
reached, not missed.

**§3 — NOT US-LISTED (four):** **Schneider Electric SE** (French-listed; reported its fastest sales
growth in five years and a second 2026 guidance raise on data-centre demand — ⚠ **and the source adds
the part 2 kill for free: *"no revenue figure, guidance range, customer names, or confirmed effect on
US counterparties"*. An industry signal, not a transaction**) · **Telefonaktiebolaget LM Ericsson**
(Swedish-listed, US ADR; its Q3 call discussed **its own** component-cost pressure — part 1, no
Company B, and the cost line is the announcer's) · **Foxconn Technology Group** and **Wistron Corp.**
(both Taiwan-listed; named only contextually in `T-2026-10-16-01`).
**§3 — NON-US REGULATOR / NO COMPANY (one):** **Ofgem** energy-price action (UK).
**RULE (viii) + §3 (one):** **Polibeli Group** — a ~**$130.1M** five-year cloud-computing contract for
its subsidiary with a Japanese client. ⚠ **The figure is the ANNOUNCING company's own revenue, which
is rule (viii) read broadly; and the issuer is nowhere near §3's floor.**
**NO COMPANY A / GOVERNMENT-ACTION OR FORECAST OBJECT (two):** **Fed Chair Kevin Warsh's 2026-10-16
remarks** declining to prejudge the **Oct 27–28 FOMC** — ⚠ **ONE party, no transaction, and the source
states he *"declined to provide specific guidance"*, so the object is the ABSENCE of news** ·
**the National Retail Federation's forecast of +4.2% US holiday spending** — ⚠ **an INDUSTRY
FORECAST, which is rule (v)'s shape in a trade-body costume: it names no company and describes no
transaction, while reading as quantified and actionable.**
**BELOW §3's CAP FLOOR (one):** **Quaker Houghton** Q3 release.
**ALREADY DISPOSED — RE-SERVED, NOT RE-LITIGATED (two, named here as the re-serve and NOT as new
disposals):** **TSMC Q3 2026** (`T-2026-10-15-01`, **ONE DAY OLD**; its $60–64B capex separately at
`T-2026-10-05-05`) · **September PPI (+1.3% m/m vs a 0.5% forecast) and retail sales (+0.8% headline,
+0.1% control group)** (`T-2026-10-12-05`, `T-2026-10-13-08`). ⚠⚠ **NO NEW ID WAS MINTED FOR THE MACRO
PRINTS, FOLLOWING THE 10-14 AND 10-15 PRECEDENT EXACTLY: THE PRINTS HAVE NOW MOVED FROM "SCHEDULED" TO
"PRINTED", AND A CHANGE IN STATUS IS NOT A CHANGE IN ELIGIBILITY. A third and fourth entry for one
rejection would inflate the thesis count rather than record anything.**

**Hard filters:** not reached on any item — every one died at **§3**, **rule (iii)**, **rule (v)**,
**rule (viii)** or **part 1**, all upstream.

**Outcome:** **REJECTED, ten items, one entry, zero drill queries spent.**

---

### 2026-10-15 (08:19 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$99,853.59** at
pre-flight). `clock` at **08:19:46** reads `is_open: false` with `next_open` **2026-10-15T09:30** and
`next_close` **2026-10-15T16:00** — both carrying **TODAY's** date, the **PRE-MARKET full-session
signature**, read off the **DATES** and not the boolean. **Not a holiday, not an early close.**
Window screened: **the completed 2026-10-14 session and overnight into Thursday** — a
**ONE-TRADING-DAY, ONE-CALENDAR-DAY** window, the ordinary shape. **Four Perplexity scans, all exit 0**
(three broad — structural framing first, then the segment-quantification framing, then the knock-on
framing — plus one drill on the single largest disclosure of the window). **FIVE theses written, ALL
FIVE REJECTED.**

**⚠⚠ THE STRUCTURAL FRAMING WAS QUERY ONE AND IT PAID A SEVENTH CONSECUTIVE SESSION — SEVEN ITEMS
RETURNED, SIX SELF-EXCLUDED WITH A NAMED REASON EACH.** Its own conclusion, verbatim: *"no item can be
confirmed as satisfying every stated test."* The exclusions supplied for free — Promino/Social Commerce
Brands (CSE-listed, counterparty's listing unestablished) · Mercuria/Heritage Minerals (neither listing
established; AUD prepayment) · Taihan Cable *"and its US unit"* (⚠ **not two companies — a parent and
its own subsidiary**) · Ocugen/Roots Pharmaceutical (signed **10-13**, outside the window — the source
applying **rule (iii)** before I did). **Four items, four reasons, zero queries spent.**

**⚠⚠ AND THE SECOND FRAMING DELIVERED THE THIRTEENTH CONSECUTIVE SESSION OF VOLUNTEERED ABSENCE
(09-29 → 10-15 UNBROKEN):** *"no company can be confirmed as meeting all of the requested criteria"* …
*"does **not** verify a qualifying company that both quantified the value to its own named reporting
segment and disclosed that segment's share of total revenue."*

**⚠⚠ THE FUNNEL RE-SERVED THIS LOG'S OWN DISPOSED REJECTS FOR A **THIRD** CONSECUTIVE SESSION, AND
BOTH ARE FROM **TWO DAYS AGO**:** **EnergyX/Trafigura ~$2B** (disposed `T-2026-10-13-02`, and this
time the source added the kill itself — *"based on an assumed lithium price of $20,000 per tonne"*,
⚠ an **ESTIMATE, NOT A DISCLOSED FIGURE**) · **LS Electric/Bloom Energy $138.7M** (disposed
`T-2026-10-13-01`, now re-stamped **10-15** over a **10-13** announcement — and the source caught its
own re-stamp: *"LS Electric announced the contract on October 13, not October 15"*). ⚠ **Reading the
log first cost one `grep` and saved two drills. The re-serve rate is now 3 for 3 sessions.**

**⚠⚠ ZERO `move` CALLS, AND THE CAUSE IS THE 10-14 CAUSE REPEATED WITH **BIGGER** TICKERS: TWO
GENUINELY ELIGIBLE US-LISTED NAMES REACHED THE RUN — `GEV` at **~$250.3B** and `BKR` at **~$56.0B**,
both an order of magnitude clear of §3's floor — AND **BOTH DIED AT PART 1**, which is UPSTREAM of the
priced-in filter.** ⚠ **A `move` on either would have been DECORATIVE and was declined for that reason
— the SEVENTH and EIGHTH such refusals** (SYNA 10-05, CEREBRAS 10-06, no-eligible-ticker 10-12, BE
10-13, HRL 10-14, AMD 10-14). ⚠⚠ **THE PROGRESSION IS NOW FOUR SESSIONS LONG AND POINTS ONE WAY:
10-12 no eligible ticker · 10-13 one · 10-14 two · 10-15 two, and the two are the LARGEST market caps
the funnel has ever delivered to part 1. THE BINDING CONSTRAINT SITS ABOVE THE PRICE CHECK, AND
CLEARING §3 BY A FACTOR OF TWENTY-FIVE BUYS NOTHING.**

**⚠ TODAY'S MACRO PRINTS (September PPI and retail sales) LAND INSIDE THIS SESSION. NO ID WAS MINTED
— following the 10-14 precedent exactly.** The object is already disposed at `T-2026-10-12-05` and
`T-2026-10-13-08`; a government statistical release has **ONE party and no transaction** whether it is
scheduled, printing or printed, and a third entry for one rejection would inflate the thesis count
rather than record anything. **Noted the dates, did nothing.**

---

### T-2026-10-15-01 — TSMC (TSM) Q3 2026 print — REJECTED (part 1 — no Company B; rule (iii) SPLIT VERDICT IN ONE RELEASE)
**Company A / the news:** TSMC reported Q3 2026 on **2026-10-15** (record net profit, 2nm share
climbing). **Two guidance figures moved in opposite rule-(iii) directions in the SAME release:** it
**RAISED** its own full-year 2026 USD revenue-growth outlook to **~44% from its own prior ~40%** — a
clean rule (iii) **PASS**, the company's own prior figure present in the source — and it
**REITERATED** full-year 2026 capex at **US$60–64B**, old range and new range **identical**.
**Company B / the candidate:** the semiconductor capital-equipment tier the headline summons on sight
— **AMAT / LRCX / KLA** (ASML is Netherlands-listed, §3).

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.**
> *Attempted:* "TSMC raising its 2026 revenue-growth outlook causes AMAT's Semiconductor Systems
> revenue to improve because TSMC will buy more wafer-fab equipment."
⚠⚠ **THE SAME RELEASE CONTRADICTS THE CAUSAL PATH IN ITS OWN WORDS. The equipment order book responds
to CAPEX, and capex was REITERATED UNCHANGED at $60–64B. The figure that moved (revenue) is not the
figure that buys equipment; the figure that buys equipment did not move.** ⚠ **To make the sentence
work it needs "and also TSMC will eventually have to spend more to serve that revenue" — an *and also*,
which §4 says is the kill.**

**2. Dollar path:** **NOT REACHED** (part 1 failed). ⚠ **And it would have failed here too: TSMC named
NO external equipment supplier** (source, verbatim: *"the cited reports do not identify any specific
external equipment supplier or vendor in that announcement"*) — **rule (v), the unnamed supply base.**
**3. Timing window:** **NOT REACHED.** The capex that did not change spans *"2026–2028"*.
**4. Invalidation:** **NOT REACHED.**

**Hard filters:**
- Priced-in (§4): **NOT CALLED — DECLINED AS DECORATIVE.** No candidate survived part 1, so there was
  nothing to price-check. ⚠ **An absent check, not a passing one.**
- Correlation (§4): no open satellite positions → **no driver to collide with** (vacuously clear).
- Universe (§3): **NOT REACHED on the candidates.** TSM itself is the headline name and not a
  candidate at any cap.

**Outcome:** **REJECTED at part 1.** ⚠⚠ **THIS IS THE MOST INFORMATIVE ENTRY OF THE RUN AND IT ADDS A
NEW RULE-(iii) COSTUME: A SINGLE RELEASE CARRYING A GENUINE PASS AND A GENUINE FAIL ON TWO DIFFERENT
FIGURES — AND THE ONE THAT PASSES IS THE ONE WITH NO SECOND-ORDER MECHANISM ATTACHED TO IT.** A reader
who checks rule (iii) and stops at the first "yes" proceeds on the **revenue** figure and never notices
that the **capex** figure — the only one with a supplier chain hanging off it — was a **reaffirmation**,
which is costume #1 on the rule (iii) list. ⚠ **THE TEST MUST BE APPLIED TO THE FIGURE THE MECHANISM
ACTUALLY RUNS ON, NOT TO THE RELEASE.** ⚠ Companion note: TSMC capex was already disposed at
`T-2026-10-05-05` ($60–64B, no Company B reached) — **the figure has not moved since, which is itself
the rule (iii) answer, and the verdict was RE-DERIVED here from today's source rather than inherited.**

---

### T-2026-10-15-02 — GE Vernova (GEV) · Baker Hughes (BKR) / Venture Global frame agreements — REJECTED (part 1 named parties; part 3 decisively; rule (viii) NEW COSTUME)
**Company A / the news:** **Venture Global (VG) 8-K, announced 2026-10-15:** *"power and grid frame
agreements"* with **GE Vernova** and **Baker Hughes Energy Services** covering **up to 16 new
power-island units, each rated 720 MW**, plus associated transformer equipment, supporting up to
**10 GW** of grid-independent capacity for AI data centres. Separately, an **Initial Unit Manufacturing
Reservation Agreement** with GE Vernova for **eight** of the remaining 15 power islands.
**Company B / the candidate:** **GEV** and **BKR**.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN — §4's PREMISE DOES NOT APPLY.**
⚠⚠ **GEV AND BKR ARE THE NAMED PARTIES. They are not Company B; they ARE the headline.** §4 is
explicit — *"you are not chasing the headline name."* ⚠ **The genuine second-order question — who
supplies GE Vernova's turbine and generator components — returns an UNNAMED SUPPLY BASE: rule (v).**
The only other knock-on available is "more gas-fired generation helps gas producers," which is **a
market, not a transaction** — the shared-cause object.

**2. Dollar path:** **FAILS, AND THE FAILURE CARRIES A NEW COSTUME.** ⚠ **Venture Global's
announcement disclosed NO dollar value for the power-island agreement, and neither GEV nor BKR stated
what it is worth to their own reporting segment** (source, verbatim: *"no available source reported
that GE Vernova or Baker Hughes stated what the agreement was worth to their own reporting segment,
revenue, or backlog"*). ⚠⚠ **THE ~$17.2B FIGURE IN CIRCULATION IS NOT THE ONE §4 ASKS FOR, ON FOUR
COUNTS AT ONCE, AND IT IS THE LARGEST NUMBER THIS FUNNEL HAS EVER PRODUCED:** it is **(a) CONDITIONAL**
— *"if all contemplated purchase orders under both frame agreements are executed, subject to
adjustments"* · **(b) AN AGGREGATE ACROSS TWO SEPARATE FRAME AGREEMENTS PLUS GE Grid equipment**, i.e.
broader than the announced power-island arrangement · **(c) UNALLOCATED between GEV and BKR**, so
neither buyable leg has a figure · and **(d) MONEY PAID OUT BY VENTURE GLOBAL**, the non-candidate leg.
⚠⚠ **NEW RULE-(viii) ENTRY — A CONTINGENT AGGREGATE CEILING SPANNING MULTIPLE AGREEMENTS AND MULTIPLE
RECIPIENTS. It is rule (v)'s CEILING sub-shape crossed with rule (viii)'s WRONG-PARTY shape, and its
SCALE is the whole of its persuasive force.** ⚠ **$17.2B divided between two companies over nine years,
contingent on orders nobody has placed, is not a dollar path — it is a press-release maximum.**
**3. Timing window:** ⚠⚠ **FAILS INDEPENDENTLY AND DECISIVELY, AND THIS KILL NEEDED NO FUNNEL QUERY —
PART 3 WAS AVAILABLE FROM THE FIRST SENTENCE.** First purchase order *"by the end of 2026"* (**a PO is
not revenue**) · POs for the eight reservation units *"beginning in early 2027"* · **power generation
available ~late 2028 / early 2029** · **frame-agreement delivery schedule running through 2034.**
⚠ **That is ~8 to ~32 quarters against §4's ceiling of TWO.**
**4. Invalidation:** **NOT REACHED.**

**Hard filters:**
- Priced-in (§4): **NOT CALLED — DECLINED AS DECORATIVE** (7th and 8th refusals). Both names die at
  part 1, upstream of the filter. ⚠ **An absent check, not a passing one.**
- Correlation (§4): no open satellite positions → no driver to collide with (vacuously clear).
- Universe (§3): **PASSES, AND BY THE WIDEST MARGIN ON RECORD — WHICH IS THE POINT.** `GEV`
  **~$250.31B** (source: Zolmax citing company market data, as-of 2026-10-15; a second source read
  ~$251.4B on the 10-14 price — ⚠ **two sources, two figures, both ~25× the floor, so the
  inconsistency is immaterial to the test and is reported rather than reconciled**). `BKR` **~$56.0B**
  (source: Simply Wall St, as-of 2026-10-14). Both US-listed common stock.

**Outcome:** **REJECTED — part 1, part 2 and part 3, each sufficient alone.** ⚠⚠ **THE LESSON IS THE
ONE GFS TAUGHT FROM THE OTHER DIRECTION: §3 PASSING TELLS YOU NOTHING. Two mega-cap US names, a real
8-K, a real counterparty, a real dated transaction and a $17.2B number — and the strategy kills it
three times over before price is ever consulted.** ⚠ **RULE (iv) FIRES TOO: VENTURE GLOBAL IS NOW AT
ITS THIRD APPEARANCE** (10-02 the ConocoPhillips 20-year SPA with first delivery 2030, logged twice
that session) **AND IT HAS DIED ON PART 3 / RULE (vi) EVERY SINGLE TIME. A ticker that keeps arriving
and keeps dying the same death is telling you about its INDUSTRY'S CONTRACTING HORIZON — LNG and
merchant power are STRUCTURALLY long-dated — not about a candidate maturing.** ⚠ **Expect this issuer
again; the answer is already written.**

---

### T-2026-10-15-03 — Vir Biotechnology (VIR) / Gilead Sciences (GILD) — REJECTED (part 1 — both parties named; rule (viii); part 3)
**Company A / the news:** Announced **2026-10-14** — a multi-programme collaboration and licence
agreement between **Vir Biotechnology** and **Gilead Sciences**: **up to $135M** in upfront and
near-term preclinical milestone payments, comprising **$90M upfront ($65M cash + a $25M equity
investment)** and **up to $45M** in milestones.
**Company B / the candidate:** **none exists.**

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN — BOTH PARTIES ARE NAMED.** ⚠ **Vir is the named
recipient and Gilead the named payer; §4's premise ("news about A, find unnamed B") has no subject
left.** The genuine second-order question — who manufactures the programmes — reaches **preclinical**
assets with **no CDMO named anywhere in the source**: rule (v)/(vii).

**2. Dollar path:** **FAILS ON BOTH LEGS AND IN BOTH DIRECTIONS.** For **GILD** the $90M is capital
paid **OUT** — rule (viii), wrong sign. For **VIR** the $25M equity component **DILUTES rather than
earns** (the AstraZeneca-convertible-preferred precedent), and the **$45M milestone tranche is a
CEILING** (*"up to"*) contingent on **preclinical** success — rule (v). ⚠ **Neither party assigned any
of it to a named reporting segment, and on GILD's ~$100B+ revenue base $90M is immaterial by two
orders of magnitude regardless.**
**3. Timing window:** **FAILS INDEPENDENTLY.** *Preclinical* milestones are **multi-year by
definition** — far beyond §4's two quarters. The regulatory/clinical version of rule (vi).
**4. Invalidation:** **NOT REACHED.**

**Hard filters:**
- Priced-in (§4): **NOT CALLED — no candidate survived part 1.**
- Correlation (§4): no open satellite positions → no driver to collide with.
- Universe (§3): ⚠⚠ **VIR's MARKET CAP IS *UNRESOLVED*, NOT PASSED AND NOT FAILED — the query returned
  no figure and NONE WAS ASSUMED.** It never needed resolving: the entry dies at part 1, upstream.
  ⚠ **Do not inherit a §3 verdict from this entry (the VAL / GFS precedent).** GILD is comfortably
  above the floor but is the first-order payer.

**Outcome:** **REJECTED at part 1.** ⚠ **This was the structural framing's ONLY self-declared
qualifying item of the whole run** — *"the only item that can be reported as meeting the named-company,
disclosed-amount, US-listed-company, and new-announcement criteria."* ⚠⚠ **AND IT IS THE RE-SERVE
WARNING'S SIBLING: THE FUNNEL'S OWN "BEST CANDIDATE OF THE RUN" DIED AT §4's FIRST PART. A source
certifying an item against ITS OWN four tests is not certifying it against §4's.**

---

### T-2026-10-15-04 — Hallador Energy (HNRG) $700M MISO Zone 6 supply agreement — REJECTED (rule (v) — counterparty unnamed; part 1)
**Company A / the news:** Announced **2026-10-14** — Hallador Energy signed a **$700M** total agreement
with *"an unidentified utility operating in MISO Zone 6"*, reported as ~**$271M capacity revenue** and
~**$422M energy revenue** over the term, associated with the **Merom Generating Station**.
**Company B / the candidate:** **none reachable.**

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** ⚠⚠ **HNRG IS THE HEADLINE NAME AND THE WINNER,
AND THE COUNTERPARTY IS NOT A COMPANY — IT IS A BLANK.** *"An unidentified utility operating in MISO
Zone 6"* is **rule (v) in its purest form: a precise figure ($700M, split to the million) attached to
an UNNAMED party made to look nameable by a named geography and a named plant.** ⚠ **The priors arrive
instantly — the MISO Zone 6 utility list is short and public (AEP/Indiana Michigan, Duke Indiana,
CenterPoint/Vectren, Hoosier, IPL/AES Indiana) — AND NAMING ONE WOULD BE ME FILLING THE SOURCE'S BLANK,
NOT RESEARCH. THE PARTY-A PRECEDENT (10-05 Synaptics) IS EXACTLY THIS OBJECT. NOT TAKEN.**

**2. Dollar path:** ⚠ **The figures belong to HNRG — the first-order winner — and the source could not
tie them to a formal reporting segment** (*"refers to the 'segment level' and Merom Generating Station
but does not identify a formal reporting-segment name"*, share of total revenue **not disclosed**).
**3. Timing window:** **NOT REACHED.** ⚠ *"Over the term"* with no term stated is not a timing window;
capacity-plus-energy utility agreements are routinely multi-year, which is the rule (vi) shape.
**4. Invalidation:** **NOT REACHED.**

**Hard filters:**
- Priced-in (§4): **NOT CALLED** — no candidate survived part 1.
- Correlation (§4): no open satellite positions → no driver to collide with.
- Universe (§3): ⚠ **HNRG's MARKET CAP IS *UNRESOLVED*, NOT PASSED AND NOT FAILED** — the query
  returned no figure and none was assumed. It never needed resolving. ⚠ **It is very likely below
  §3's $10B floor, and "very likely" is NOT a §3 finding — do not inherit one from this entry.**

**Outcome:** **REJECTED — rule (v) and part 1.** ⚠ **The 15th instance of "a disclosed figure with no
nameable counterparty," and it was disposed without a drill query because the shape was recognised on
sight. That recognition is what the standing-rules list is for.**

---

### T-2026-10-15-05 — §3 / non-qualifying / disposed-repeat sweep of SIXTEEN items — REJECTED (disposed as one, zero drill queries spent)
**Company A / the news:** everything else the four scans returned. **Company B:** none reached on any.
**Disposed as one entry rather than sixteen**, because sixteen near-identical rejections would inflate
the thesis count without recording anything the shape does not already say.

**Already disposed in THIS log — re-served by the funnel (3rd consecutive session of this):**
**EnergyX / Trafigura ~$2B** (`T-2026-10-13-02`; the source added its own kill — the figure is *"based
on an assumed lithium price of $20,000 per tonne"*, **an estimate, not a disclosure**) ·
**LS Electric / Bloom Energy $138.7M** (`T-2026-10-13-01`; **re-stamped 10-15 over a 10-13
announcement**, and the source caught its own re-stamp).

**§3 — NOT US-LISTED or below the floor (eight):** Promino (CSE + OTC) · Social Commerce Brands
(listing unestablished) · Mercuria / Heritage Minerals (AUD$40M gold prepayment, neither listing
established) · Taihan Cable ~$82M (Korea-listed) · Symrise (Frankfurt) · Kuros Biosciences (SIX) ·
Antofagasta (LSE) · Nel ASA (Oslo) · Rajesh Power Services + Nexa Dynamics (India) ·
Persistent Systems (India; and ⚠ **quarterly order BOOKINGS, not a new announced order**) ·
Sphere Corp ~$21.29M (listing unestablished) · Axe Compute (Nasdaq-listed but **no cap established
and no dollar value disclosed** for the Penguin Solutions work).
**RULE (iii) — outside the window / previously announced:** Ocugen / Roots Pharmaceutical (signed
**10-13**; the source applied the rule before I did) · Constellation / Google (a **secondary commentary
piece** on agreements already public, **not in the 24-hour window** — ⚠ **and CEG is the first-order
named party regardless**).
**RULE (vii) — vertical integration / no external beneficiary (three):** **IBA — 12 Cyclone KIUBE 300
cyclotrons for *"a leading radiopharmaceutical producer"*** ⚠⚠ **THE MIRROR IMAGE OF THE 10-06 GEHC
FINDING, AND IT CLOSES THE SAME LOOP FROM THE SUPPLIER SIDE: on 10-06 a named US acquirer had no
nameable equipment beneficiary because it makes its own cyclotrons; today a named cyclotron maker has
no nameable customer — and IBA is BELGIAN-LISTED, so §3 kills the one named leg anyway. BOTH ENDS OF
THE CHAIN, TWO WEEKS APART, AND NEITHER YIELDS A COMPANY B.** · Symrise's own India capacity (no
external party) · Scout Motors **$300M** supplier park, *"~1,000 supplier jobs"* (⚠ **no supplier
company named** — rule (v), and Scout is VW-owned and not separately listed).
**MERGER ARBITRAGE — not in §4 (one):** IonQ acquiring a cybersecurity firm for *"up to $1.3B"*
(⚠ a **ceiling** on top of the merger-arb kill).
**GUIDANCE ISSUANCE WITH NO COMPANY B (two):** Kuros raising 2026 sales growth to 36–40% · Antofagasta
raising 2026 cash-cost guidance to **$2.60–2.70/lb from $2.40–2.60/lb** (⚠ **a genuine rule (iii) PASS
— the company's own prior range is right there — and a §3 kill, LSE-listed. A clean pass on one filter
is not progress toward a trade.**).

**Hard filters:** not reached on any item; every one died at §3, rule (iii), rule (v), rule (vii) or
the §4 premise. **Zero `move` calls, zero drill queries.**

**Outcome:** **REJECTED, all sixteen.** ⚠ **The funnel's self-exclusions did four of these for free
and `grep` on this log did two more. The sweep cost nothing because the shapes were recognised rather
than re-derived.**

---

### 2026-10-14 (08:21 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$101,007.25** at
pre-flight). `clock` at **08:21:37** reads `is_open: false` with `next_open` **2026-10-14T09:30** and
`next_close` **2026-10-14T16:00** — both carrying **TODAY's** date, the **PRE-MARKET full-session
signature**, read off the **DATES** and not the boolean. **Not a holiday, not an early close.**
Window screened: **the completed 2026-10-13 session and overnight into Wednesday** — a
**ONE-TRADING-DAY, ONE-CALENDAR-DAY** window, the ordinary shape, exactly as the 10-13 close seat
predicted. **Four Perplexity scans, all exit 0** (three broad — structural framing first, then the
segment-quantification framing, then the knock-on framing — plus one drill on the single event that
put an eligible US-listed ticker in a dated transaction). **FIVE theses written, ALL FIVE REJECTED.**

**⚠⚠ THE STRUCTURAL FRAMING WAS QUERY ONE AND IT PAID A SIXTH CONSECUTIVE SESSION, BUT TODAY IT PAID
IN A NEW CURRENCY: IT RETURNED SIX ITEMS AND SELF-EXCLUDED ALL SIX IN A TABLE WITH A NAMED FAILURE
AGAINST EACH.** Its own conclusion, verbatim: *"no announcement can be confirmed as meeting all
criteria simultaneously."* The exclusions it supplied for free — Hormel/Brakebush (seller is a family,
not a contracting company) · Galderma/ZO Skin Health (**SIX-listed**, counterparty private) ·
Chemring/Roke (**LSE-listed** *and* *"the counterparty is unnamed"*) · Alpha Compute (counterparty
unnamed **and** *"signed October 9, 2026, rather than announced within the last 24 hours"* — the source
applying **rule (iii)** before I did) · FF EAI/FFAI (signed 10-12) · Aegis Logistics/Tristar (Indian
issuer). **Six items, six reasons, zero queries spent disposing of them.**

**⚠⚠ AND THE SECOND FRAMING DELIVERED THE TWELFTH CONSECUTIVE SESSION OF VOLUNTEERED ABSENCE
(09-29 → 10-14 UNBROKEN), IN THE FLATTEST WORDS IT HAS USED YET:** *"No company can be confirmed to
meet the full screen from the available results"* … *"the evidence provided does not establish any
US-listed company with market capitalization above $10 billion that satisfies **all** requested
criteria."* ⚠ **It then listed the three near-misses with their own kills attached — and the first of
them was RTX again.**

**⚠⚠ THE PRIORS ARRIVED ON SCHEDULE, AGAINST THE FACTS, AND NOT ONE IS WRITTEN DOWN AS A CANDIDATE.**
The Lockheed/Avio item summoned **the solid-rocket-motor tier** — the exact prior this log already
names as reflexive — and the summoning is worse than usual, because **the whole point of Lockheed
buying *merchant* Italian capacity is that NOC's and L3Harris/Aerojet's capacity is constrained.**
⚠ **So the prior points the WRONG WAY: the read-across is negative for the US incumbents, §3 forbids
expressing a negative, and the "competitor loses relative standing" flip is the shared-cause object.
NOT TAKEN.** The Fermi item summoned **the GPU vendor for any AI-compute headline**, and AMD was
*already in the headline*.

**⚠ ZERO `move` CALLS, AND THE CAUSE IS THE 10-13 CAUSE ONE RUNG HIGHER: TWO GENUINELY ELIGIBLE
US-LISTED TICKERS REACHED THE RUN (`HRL`, `AMD`) AND **BOTH DIED AT PART 1**, which is UPSTREAM of the
priced-in filter.** `asset` was pulled on both the structural question and the instrument question
rather than assumed: **HRL** returns `us_equity` / NYSE / tradable, and **AVIO** returns **404 — not in
the US equity universe at all**, so §3's kill on Avio is **established, not inherited** from its 10-07
disposal. ⚠ **A `move` on HRL or AMD would have been DECORATIVE and was declined for that reason —
the fifth and sixth such refusals (SYNA 10-05, CEREBRAS 10-06, no-eligible-ticker 10-12, BE 10-13).
This is the fourth state of the priced-in filter, in its instructive form: tickers existed and the
funnel's own structure killed them before price could matter.**

---

### T-2026-10-14-01 — AVIO (ineligible) / LMT (first-order) — REJECTED (§3 established; part 1; part 2 wrong quantity)
**Company A / the news:** **2026-10-13** — Lockheed Martin and **Avio S.p.A.** announced a strategic
cooperation agreement giving Lockheed access to part of Avio's **merchant solid-rocket-motor** capacity
for the **ER GMLRS** and **PrSM** programs. Avio disclosed **"more than $500 million"** of investment in
new **US** production capacity (Businesswire 2026-10-13; defence-industry.eu).
**Company B / the candidate:** **None survives.** Avio is the party whose economics change; Lockheed is
the headline name and the **buyer** of capacity.

**1. Mechanism (one sentence):** *not written — see Outcome.* The only honest sentence names **Avio** as
Company B, and Avio cannot be bought here at any price.
**2. Dollar path:** **FAILS.** The one disclosed figure, **>$500M, is Avio's own CAPEX** — capital paid
**OUT**, not segment revenue at any eligible Company B (**rule (viii)**). ⚠ **The source states the
other half itself: it *"does not disclose the agreement's financial terms, expected revenue, unit
volumes, or a specific cost impact for Lockheed Martin."***
**3. Timing window:** *not reached.* A greenfield SRM line is a multi-year build; **rule (vi)** would
kill it independently had parts 1 and 2 not.
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **not called — DECORATIVE.** No eligible Company B existed to call it on.
- Correlation (§4): **no operand** — zero open satellite positions, so no `driver` field to collide with.
- Universe (§3): **AVIO → `asset` returns 404, not in the US equity universe.** ⚠ **ESTABLISHED FROM
  SOURCE THIS RUN, NOT INHERITED from the 10-07 disposal** (the GFS/VAL lesson). LMT passes §3 and is
  irrelevant, being first-order.

**Outcome:** **REJECTED three times over.** ⚠⚠ **This is the thirteenth US-defence-award instance and
the FIRST where the mechanism is sound, the beneficiary is named, the figure is real and dated — and
the beneficiary is simply NOT LISTED HERE. A different door on the same corridor: the previous twelve
died because the tier below the prime was confidential; this one dies because the tier below the prime
was named and is ITALIAN.** ⚠ **No re-query was issued on "who supplies Avio's new US plant" — the
catalogue's answer is already written and the standing rule is to spend ONE query and stop. The plant
has a dollar figure, a programme and a country, and **no contractor, engineer or equipment vendor
whatsoever** — rule (v)'s capex-blank costume, the BDX shape.**

---

### T-2026-10-14-02 — AMD — REJECTED (part 1; part 2 no figure; rule (viii) NEW COSTUME)
**Company A / the news:** **2026-10-13** — **Fermi** (FRMI, the Texas data-centre/energy developer)
announced a **credit support agreement with AMD** backstopping a lease for **phase one of Project
Matador**, Carson County, Texas — **222 MW** gross, with a partnership framework for expansion to
**650 MW**. Fermi shares rose double digits on it.
**Company B / the candidate:** **AMD** — US-listed, NASDAQ, far above §3's floor. The only genuinely
eligible second-order-looking name this run produced.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** AMD is a **named party to the announcement**,
so §4's premise — news about Company A, find Company B — does not apply. Any sentence that makes AMD
second-order here needs a second clause ("*and also* AMD will presumably sell the GPUs into it"), which
is the "and also" kill.
**2. Dollar path:** **FAILS, on the source's own words:** *"No source in the available reporting
discloses a dollar amount of revenue, orders, or purchase commitments attributable to AMD"* and *"a
figure for AMD is not disclosed."* **No AMD reporting segment is identified** — the source calls AMD
only *"the high performance and adaptive computing leader."*
**3. Timing window:** **FAILS independently.** The only dollar figure in the story — **~$6.5B** — is
**Fermi's expected revenue over an initial FIFTEEN-YEAR term**, i.e. the wrong company **and** ~60
quarters against §4's two-quarter ceiling.
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **not called — DECORATIVE.** Part 1 kills it upstream; a `move` on AMD would have
  converted an honest absence into a fake exercise.
- Correlation (§4): **no operand** — empty sleeve.
- Universe (§3): AMD passes on instrument and cap. ⚠ **Passing §3 bought it nothing, which is the
  normal case.**

**Outcome:** **REJECTED.** ⚠⚠ **AND IT CARRIES A GENUINELY NEW COSTUME FOR RULE (viii), WORTH THE ENTRY
ON ITS OWN: A CREDIT BACKSTOP IS A CONTINGENT LIABILITY ASSUMED BY THE BUYABLE LEG — THE OPPOSITE SIGN
FROM REVENUE — AND IT READS AS A STRONG COMMERCIAL SIGNAL BECAUSE THE MARKET PRICED FERMI UP ON IT.**
The catalogue already holds capital paid in, capital paid out, financing ceilings available to somebody
else, synergy estimates and misses against consensus. **This is the first *guarantee*: AMD has promised
to stand behind somebody else's rent. The amount is undisclosed, and if it is ever quantified it will
appear as a risk, not a sale.** ⚠ **Do not rehabilitate this if AMD later announces a chip order into
Matador — that would be a NEW event with its own entry, not this one maturing.**

---

### T-2026-10-14-03 — HRL — REJECTED (part 1 — Company A is the payer; no Company B exists)
**Company A / the news:** **2026-10-14** — **Hormel Foods (HRL, NYSE)** announced a definitive agreement
to acquire **Brakebush Brothers**, a chicken company, for **~$1.055 billion**, closing expected Q1
fiscal 2027.
**Company B / the candidate:** **None.** Brakebush is **private** and family-held — unbuyable at any
price; no supplier, contractor or co-packer is named by any source.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** HRL is the **headline name** and the **payer**.
**2. Dollar path:** **FAILS — form five.** $1.055B is **acquisition consideration paid OUT by the only
listed party to a private seller** — the **GEHC/Sofie** shape exactly: the money leaves the buyable leg
and the receiving leg cannot be bought.
**3. Timing window:** Closing **Q1 FY2027** and revenue contribution later — and §4 does not reach it,
because **merger activity is not in §4 at all**: a target whose price is contractually pinned has no
economics left to change, and the acquirer is first-order.
**4. Invalidation:** *not reached.*

**Hard filters:**
- Priced-in (§4): **not called — DECORATIVE.** Part 1 is upstream.
- Correlation (§4): **no operand** — empty sleeve.
- Universe (§3): **HRL `asset` → `us_equity` / NYSE / tradable / fractionable — instrument test PASSES,
  pulled from source this run.** ⚠ **Market cap NOT resolved and deliberately so: the funnel declined
  to attach one and the thesis was already dead at part 1. §3's cap is UNRESOLVED, NOT PASSED — do not
  inherit a §3 verdict from this entry** (the VAL/GFS precedent).

**Outcome:** **REJECTED.** ⚠ **The honest note is how close this came to looking usable: a real
transaction, a precise figure to three decimals, a US-listed party above any plausible floor, and a
dated 8-K-grade release. Everything §4 asks for except a Company B.**

---

### T-2026-10-14-04 — RTX — REJECTED (rule (iv), FIFTH APPEARANCE IN EIGHT SESSIONS; rule (v) ceiling; no Company A)
**Company A / the news:** **2026-10-13** — RTX reportedly received an **"up to $8 billion"** contract
from the **US Air Force Nuclear Weapons Center** for strategic communications modernisation.
**Company B / the candidate:** **None offered, none sought.**

**1.–4.:** *not written.* The answer was already in the catalogue and **zero queries were spent.**

**Hard filters:** not reached.

**Outcome:** **REJECTED on four independent grounds already on file:** RTX is **first-order**; the
counterparty is a **government body**, not a Company A (a government action has **one party** and no
transaction); **"up to $8B" is a CEILING**, not a figure (**rule (v)**); and **no supplier below RTX is
named**, which is this funnel's settled defence-disclosure pattern.
⚠⚠ **THIS IS RTX's FIFTH APPEARANCE IN EIGHT SESSIONS AND ITS FOURTH DISTINCT AWARD** (09-29 AMRAAM
$20.7B · 10-02 SM-6 *"up to"* $24.4B · 10-09 SM-3 *"up to"* $6.3B · 10-12 the SM-3 award **re-served
twice in one run** · 10-14 USAF NWC *"up to"* $8B). ⚠ **It died the same death every time.** ⚠⚠ **AND
THE NEW AWARD IS THE STRONGER FORM OF RULE (iv)'s WARNING, NOT THE WEAKER ONE: 10-12's re-serve could
be dismissed as the funnel repeating itself, but this is a GENUINELY NEW, GENUINELY LARGE, GENUINELY
DATED award — and it is still telling me about the defence sector's DISCLOSURE PRACTICE rather than
about a candidate maturing. A fresh transaction is not fresh evidence when the kill is structural.**
⚠ **Fourteenth US-defence-award instance counted** (thirteenth was T-2026-10-14-01).

---

### T-2026-10-14-05 — §3 / non-qualifying sweep of NINE, disposed as one — REJECTED
Nine items dealt with in a single entry because each dies on one structural reading, with **zero
follow-up queries spent** on any of them:

- **Galderma / ZO Skin Health**, $1.5B enterprise value — **§3: Galderma is SIX-listed (Swiss)**; ZO is
  private. Two kills.
- **Chemring Group / Roke → an unnamed major US defence prime**, *"at least $170M over five years"*,
  $16M initial order — **§3: LSE-listed**, **and rule (v): the counterparty is unnamed.** ⚠ **A fresh
  costume of the unnamed-customer shape that `T-2026-10-13-01` logged: here the blank is a *named
  industry role* ("major U.S. defense contractor") carrying a figure, a term and a product.**
- **Alpha Compute (ALP, NASDAQ)**, **$81,732,160** four-year GPU lease — counterparty unnamed; **signed
  2026-10-09, not announced in window (rule (iii), stated by the source itself)**; and **$81.7M on a
  microcap makes part 2's 10% test and §3's $10B floor JOINTLY UNSATISFIABLE** — the free one-step screen.
- **FF EAI Robotics (FFR) / Faraday Future (FFAI)**, ~$200M and ~$60M business valuations — both
  **far below §3's $10B floor**; agreements signed **10-12**; no contract term.
- **Aegis Logistics / Tristar**, $809M for 90% — **§3: Indian issuer.**
- **Moreld ASA / Norwegian Defence Materiel Agency** — **§3 non-US** *and* a government counterparty.
- **BigBear.ai**, *">$225M"* federal awards (10-13) — below §3's floor, and the source states the figure
  *"includes contract options and ceilings rather than earned revenue"* — **rule (v)'s ceiling sub-shape
  with the source applying it for me.**
- **LS Electric / Bloom Energy, $138,458,284** — ⚠ **an EXACT RE-SERVE of `T-2026-10-13-01`, one session
  old, same parties and same figure to the cent. Disposed on the log, not on the tape: part 1 — the one
  US-listed party (BE) is the PAYER. Reading the log first cost one grep and saved a drill.**
- **THE MACRO COMPLEX, including September CPI printing TODAY at 08:30 ET** (PPI and retail sales 10-15,
  ASML/TSMC later this week) — ⚠⚠ **NO NEW ID MINTED, AND THAT IS DELIBERATE: this is the same disposed
  object as `T-2026-10-12-05` and `T-2026-10-13-08`, and re-litigating it would inflate the thesis count
  with a third entry for one rejection.** ⚠ **It has moved from "the forward calendar — nothing has
  happened yet" to a print that lands inside this session, and that changes its STATUS, not its
  ELIGIBILITY: a macro print has ONE party and no transaction — the government-action object in a
  calendar's clothing.**

---

### 2026-10-13 (08:26 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,820.09** at
pre-flight). `clock` at **08:26:35** reads `is_open: false` with `next_open` **2026-10-13T09:30** and
`next_close` **2026-10-13T16:00** — both carrying **TODAY's** date, the **PRE-MARKET full-session
signature**, read off the **DATE** and not the boolean. **Not a holiday, not an early close.** The data
plane agrees and corroborates the discriminator rather than any bar's completeness: `bars --days 4
--adjustment all` returns **NO bar dated 2026-10-13**.

Window screened: **the completed 2026-10-12 session and overnight into Tuesday 2026-10-13** — a
**ONE-TRADING-DAY, ONE-CALENDAR-DAY** window, the ordinary shape, and the 10-12 close seat predicted it
in those words. **Four Perplexity scans, all exit 0** (three broad/structural, one drill on the single
transaction of the day carrying both a disclosed dollar figure and a US-listed party).
**EIGHT theses written, ALL EIGHT REJECTED.** Zero `move` calls — cause stated at the foot of this block.

**⚠⚠ THE STRUCTURAL FRAMING WAS QUERY ONE AGAIN AND IT PAID A FIFTH CONSECUTIVE SESSION — AND TODAY IT
PAID IN THE FORM THE RULE WAS WRITTEN FOR: it returned exactly ONE qualifying item and SELF-EXCLUDED
FOUR MORE WITH THE REASON ATTACHED.** Asking for **two named parties, both of them companies, a
disclosed dollar amount, and the exact announcement date** returned EnergyX/Trafigura (`-02`) as the
single structural match, and disposed of **LS Electric/Bloom Energy** (*"both are non-US companies"* —
⚠ **the source was WRONG on that point and the drill corrected it; see `-01`**), **Hiteck/Visara**
(*"headline value is an 'up to' ceiling"*), **Bluejay/Toray** (*"disclosed a contractual milestone but
no dollar amount"*) and the Saudi/Gulf items, for **zero follow-up queries**.
⚠⚠ **AND THE 10-12 FALSE-POSITIVE LESSON FIRED CORRECTLY ON ITS SECOND OUTING: the framing's single
"qualifying" return (EnergyX/Trafigura) SATISFIES STRUCTURE AND FAILS PARTY TYPE — both parties are
PRIVATE. Last session the structure arrived with two SOVEREIGN STATES; this session with two PRIVATE
companies. "IT RETURNED THE SHAPE" IS STILL NOT GROUNDS TO PROCEED, and the additive party-type test
written down on 10-12 caught it in one step.**

**⚠⚠ THE SECOND FRAMING (won-a-contract / quantified-to-its-own-segment) RETURNED A VOLUNTEERED ABSENCE
AGAIN — UNBROKEN SINCE 09-29 — IN THE SOURCE'S OWN WORDS:** *"No qualifying company can be
identified from the available results"* … *"the evidence provided supports **zero confirmed matches**,
rather than a constructed list of likely candidates."* ⚠ **The source declined to manufacture
candidates in the same sentence in which §4's honest-broker paragraph warns me not to. FIVE items
self-excluded with reasons** (Technip Energies' €250–500M **band** entering *"backlog, not … a
quantified impact on that segment's revenue"* · LS Electric/Bloom **no segment named** · Aequs/Safran
**no value** · IRCON **governmental counterparty** · BEL **no customer-by-customer breakdown**).

**⚠⚠ AND THE THIRD BROAD SCAN PRODUCED THE STRONGEST FORM OF THE STANDING FINDING THIS LOG HAS ON
RECORD — FOUR QUALIFYING EVENTS, AND THE SOURCE ANSWERED §4's QUESTION IN THE NEGATIVE ON EVERY SINGLE
ONE, IN IDENTICAL WORDS:** *"No second publicly traded US company is named by the source as directly
affected"* — written out four times, once each for **ENVX**, **BP**, **EQX** and **ARREF**.
⚠ **ELEVENTH CONSECUTIVE SESSION of a volunteered absence, 09-29 through 10-13 unbroken (09-29, 09-30,
10-01, 10-02, 10-05, 10-06, 10-07, 10-08, 10-09, 10-12, 10-13 — COUNTED, not inherited: the standing
item read TEN through 10-12), and the FOURTH
in which EVERY broad scan produced one.** ⚠ **A four-for-four denial inside ONE query is the cleanest
instance yet of the mechanism: the tier below a named party is commercially confidential, so the source
volunteers the absence when asked for a second company. A volunteered absence is stronger than a
silence.**

**⚠⚠ THE PRIORS ARRIVED ANYWAY, AGAINST THE DENIALS, AND NOT ONE WAS WRITTEN DOWN AS A CANDIDATE:** the
data-centre electrical tier (ETN/PWR/VRT/HUBB) for the Bloom switchgear order — ⚠ **the most seductive
of the run, because `T-2026-10-13-01` names a REAL 38-kV switchgear order with a REAL dollar figure and
a REAL delivery schedule, and the eligible US-listed names in that tier were instantly ready** — the
lithium/cathode complex (ALB/Livent/Piedmont) for EnergyX/Trafigura, the gold-development contractor
tier for EQX's South Railroad permits, and AMAT/LRCX/KLA once more for the ASML capacity lines.
⚠ **EACH IS A FACT ABOUT AN INDUSTRY, NOT ABOUT A TRANSACTION. Reported with its count and not
promoted.**

**⚠⚠ ZERO `move` CALLS, AND THE CAUSE IS CLEANER THAN ANY PRIOR INSTANCE OF THE FOURTH STATE: the ONE
US-listed party in the ONE transaction of the day is BLOOM ENERGY, AND IT IS THE *PAYER*.** The
candidate died at **part 1, upstream of the priced-in filter**, so there was no eligible ticker to call
`move` on. ⚠⚠ **A `move` CALL ON BE WOULD HAVE BEEN DECORATIVE — a passing or failing number on a name
with no mechanism — AND IT IS DECLINED FOR THE FOURTH TIME ON THAT GROUND** (SYNA 10-05, CEREBRAS
10-06, no-eligible-ticker 10-12, **BE today**). **This is the FOURTH STATE — the filter having nothing
to fire on — NOT a pass.** ⚠ **An absent check and a passing one look identical in a run summary. This
one is ABSENT.**

**Housekeeping, all re-derived at this seat and none inherited:** week anchor **RECOMPUTED** (today is
**Tuesday**, ISO week 42 weekday 2, anchor **2026-10-12**) and found **matching** `week_of`, so
`new_positions_this_week` **DELIBERATELY NOT RE-RESET**, **0 of 3** · breaker **INACTIVE** with
`halt_triggered_at: none`, so **NO `HALT_CLEARED_AT` COMPARISON WAS DUE** · `control.md` notes **EMPTY**
· core **70.2441%** ($70,820.093456 / $100,820.09) **IN BAND** by 5.24 points, **83rd consecutive run**,
`rebalance_delta` **−$246.03**, a **DISTANCE READOUT AND NOT A DIFFERENCE** · satellite **0.0%**, count
**0** · cash **$30,000.00 = 29.76%** · `orders --status all` still **ONE ROW** for the whole account
history (the 09-03 core fill, terminal), so §7's limbo warning has **no operand rather than a clean
bill** · **ledger RECONCILED: `positions.md` holds zero satellite blocks and the broker returns one row,
VOO. No disagreement.**

⚠ **§6 CAP, BASIS NAMED: 5% of the `account` equity $100,813.16 is $5,040.66; 5% of the `sleeves`
equity $100,820.09 is $5,041.00. The two readings are $6.93 apart with no order in the interval — the
moving pre-market mark again, and the reason no cap figure is written without its basis.**

⚠ **ONE OBSERVATION, REPORTED NOT RECONCILED: the complete 2026-10-12 bar reads `n` 1,393 / `v` 32,547
this morning — BYTE-IDENTICAL to the SECOND of the two readings the 10-12 close seat took a minute
apart (1,392/32,544 then 1,393/32,547). The late-print drift SETTLED overnight. `balance_asof` has
advanced to 2026-10-12.**

---

### T-2026-10-13-01 — Bloom Energy (BE) / LS Electric $138.5M switchgear order — REJECTED
**Company A / the news:** **LS Electric** (Korea-listed, 006260.KS) announced on its own site on
**2026-10-13** a contract signed with **Bloom Energy** worth **$138,458,284** — 38-kV-class high-voltage
switchgear and distribution transformers, **deliveries April–July 2027**, for a **fuel-cell-based
on-site power generation project at a data centre under construction in Pennsylvania** owned by an
unnamed *"major U.S. technology company"* (LS Electric release; Yonhap; Korea Herald; transformer-magazine).
**Company B / the candidate:** **NONE REACHED.** Bloom Energy is the only US-listed party and it is the
**PAYER**; the data-centre owner is **UNNAMED**.

**1. Mechanism (one sentence):** **NOT WRITTEN.** ⚠⚠ **THE SENTENCE CANNOT BE WRITTEN IN THE DIRECTION
§3 PERMITS. The disclosed $138.5M is money leaving Bloom, not arriving: it is Bloom's INPUT COST for a
project whose own revenue to Bloom is UNDISCLOSED.** The only version that improves a revenue line
reads *"the switchgear order implies a Pennsylvania fuel-cell deployment **and also** implies Bloom
books product revenue on it of an undisclosed size"* — **a second clause carrying the entire load, which
is the "and also" kill in its textbook form.**
**2. Dollar path:** **FAILS INDEPENDENTLY, AND ON THE *QUANTITY*, NOT THE SIZE.** The one disclosed
figure is attributed by the source **to LS Electric's supply contract, not to revenue or a cost-line
change at a named US-listed company** — the source said so in those words: *"Any conclusion that the
data-center owner's revenue or costs change by a particular amount would be an inference unsupported by
the cited announcement."* **This is form five — the figure is disclosed and is the WRONG QUANTITY — and
specifically the sub-shape where the figure is capital paid OUT by the buyable leg** (the CVX/Hess
Midstream $200M and GEHC/Sofie $945M shape, now its third instance).
**3. Timing window:** Deliveries **April–July 2027** are **two to three quarters out** from Q4 2026 and
revenue recognition is later and undisclosed — ⚠ **borderline-to-failing against §4's two-quarter
ceiling, and NOT the reason this died.** No deadline set; there is no position.
**4. Invalidation:** **NOT WRITTEN** — no thesis to invalidate.

**Hard filters:**
- Priced-in (§4): **NOT RUN — the candidate died at part 1, upstream of the filter.** ⚠ **A `move` call
  on BE would have been DECORATIVE. Declined deliberately; this is the fourth state, not a pass.**
- Correlation (§4): **vacuously clear** — zero open satellite positions, so no `driver` field exists to
  collide with. ⚠ **Recorded as VACUOUS, not as a pass.**
- Universe (§3): **LS Electric FAILS outright — Korea-listed, not US.** **BE's market cap was NOT
  SOURCED this run and is therefore UNRESOLVED, NOT PASSED** — ⚠ **the kill does not rest on it, and
  per the VAL/GFS precedent no §3 verdict may be inherited from this entry.**

**Outcome:** **REJECTED on part 1 (no Company B in a permitted direction) and part 2 (the figure is the
wrong quantity — capital paid OUT by the only US-listed leg), independently, with part 3 also pressing.**
⚠⚠ **THE RUN'S REAL FINDING, AND IT IS A NEW COSTUME OF RULE (v): AN UNNAMED *CUSTOMER* CARRYING A MAP
PIN, A DELIVERY SCHEDULE AND A PRODUCT SPEC.** The data-centre owner is one entity that definitely
exists, definitely contracted on a dated day, and is withheld on purpose — ⚠ **and unlike "Party A" it
is withheld by a THIRD party's release rather than by its own filing, so there is not even a filer
obliged to name it later.** ⚠ **THE PULL WAS REAL AND IS RECORDED: the shortlist of eligible
US-listed "major technology companies" building Pennsylvania data centres is short, and naming one would
have been a GUESS DRESSED AS A DEDUCTION. NO GUESS WAS MADE AND NONE IS RECORDED AS A CANDIDATE.**
⚠ **The electrical-tier prior (ETN/PWR/VRT/HUBB) arrived instantly and was NOT written down — the order
went to LS Electric, which is precisely a fact about who did NOT win it.**

---

### T-2026-10-13-02 — EnergyX / Trafigura $2B lithium offtake — REJECTED
**Company A / the news:** **2026-10-12** — **EnergyX** and **Trafigura Group** signed a **binding
10-year take-or-pay offtake agreement** for **100,000 metric tons** of lithium products, valued at
**"more than $2.0 billion" at current lithium prices** (Reuters via kelo.com; battery-tech.net; TipRanks).
**Company B / the candidate:** **NONE REACHED.**

**1. Mechanism (one sentence):** **NOT WRITTEN** — no eligible party exists on either side.
**2. Dollar path:** **NOT REACHED.** ⚠ **Note the figure's own weakness even so: it is an estimate
"based on current lithium prices" against a fixed TONNAGE — a quantity dressed as a dollar amount, the
same defect as 10-12's four-rung tonnage ladder.**
**3. Timing window:** **NOT REACHED** (a 10-year term is outside the two-quarter ceiling on its face).
**4. Invalidation:** **NOT WRITTEN.**

**Hard filters:**
- Priced-in (§4): **NOT RUN — no ticker exists to run it on.**
- Correlation (§4): **vacuous** — zero open positions.
- Universe (§3): **FAILS OUTRIGHT AND IMMEDIATELY — BOTH PARTIES ARE PRIVATE COMPANIES.** The source
  stated it in the table itself: *"EnergyX: No — private company. Trafigura: No — private company."*

**Outcome:** **REJECTED at §3 in one step.** ⚠⚠ **ITS VALUE IS AS THE STRUCTURAL FRAMING'S SECOND KNOWN
FALSE POSITIVE, AND IT CONFIRMS THE FIX WRITTEN DOWN YESTERDAY WORKS.** It carries **two named parties,
a precise date, a binding contract, a term length and a dollar figure** — the entire shape the framing
exists to find — ⚠ **and it is untradeable because the PARTY TYPE test fails: both parties are private.**
10-12's instance failed the same test with **sovereign states**; this one fails it with **private
companies**. ⚠ **The additive party-type and unit tests are now load-bearing on consecutive sessions.
Keep them in the query itself, where they cost one clause.**

---

### T-2026-10-13-03 — Enovix (ENVX) preliminary Q3 2026 beat + $19M Korea expansion — REJECTED
**Company A / the news:** **2026-10-12 8-K** — Enovix pre-announced Q3 revenue of **~$11M** against
prior guidance and a **$9.5M** consensus, EPS **−$0.14** vs **−$0.16** consensus, plus a **$19M Korea
plant expansion** to add capacity (stocktitan 8-K; ground.news).
**Company B / the candidate:** **NONE — THE SOURCE DENIED IT EXPLICITLY:** *"No second publicly traded
US company is named by the source as directly affected."*

**1. Mechanism (one sentence):** **NOT WRITTEN** — no second company to write it about.
**2. Dollar path:** **JOINTLY UNSATISFIABLE — THE FREE ONE-STEP SCREEN, AND IT IS THE REASON NO SUPPLIER
SEARCH WAS ATTEMPTED.** A **$19M** capex programme cannot be 10% of revenue at any company clearing
§3's **$10B** market-cap floor, so part 2's test and §3's floor cannot both be satisfied by any
Company B. ⚠ **The search was pointless before it started; it was not started.**
**3. Timing window:** **NOT REACHED.**
**4. Invalidation:** **NOT WRITTEN.**

**Hard filters:**
- Priced-in (§4): **NOT RUN.** ⚠ **The source reports shares "jump 13" on the pre-announcement, which
  would very likely FAIL the filter had the candidate reached it (shape two) — but ENVX is the HEADLINE
  NAME, so §4's premise does not apply to it at any price.**
- Correlation (§4): **vacuous** — zero open positions.
- Universe (§3): **ENVX's market cap was NOT SOURCED this run — UNRESOLVED, NOT PASSED, and the kill
  does not rest on it.** ⚠ **Resisting the inherited impression that it sits below the floor: an
  unsourced recollection is not a §3 verdict, and this log's own rule forbids writing one.**

**Outcome:** **REJECTED on part 1 (volunteered absence of any Company B) and part 2 (jointly
unsatisfiable on a $19M programme), independently.** Enovix is first-order and outside §4 at any price.

---

### T-2026-10-13-04 — BP p.l.c. (BP) Q3 impairment $3–4.5B + production guidance — REJECTED
**Company A / the news:** **2026-10-13** — BP guided to Q3 impairments of **$3.0–4.5B** in its gas and
low-carbon-energy segment, with upstream production of **2.190–2.240 mmboe/d** against **2.201** in Q2
and prior guidance of **2.100–2.245** (Reuters; Morningstar/Alliance News).
**Company B / the candidate:** **NONE — DENIED IN THE SOURCE'S OWN WORDS:** *"No second publicly traded
US company is named by the source as directly affected."*

**1. Mechanism (one sentence):** **NOT WRITTEN, AND IT POINTS THE WRONG WAY.** ⚠⚠ **This is the EIGHTH
REJECT FORM in its second recorded instance (SUPN, 10-08, was the first): a multi-billion-dollar
impairment is a sound, large, well-disclosed mechanism that points DOWNWARD, and §3 permits only the
LONG side — no options, no inverse, nothing not bought outright with settled cash.**
⚠⚠ **THE TEMPTING MOVE IS TO FLIP IT INTO A "COMPETITOR BENEFITS" LONG (XOM/CVX/SHEL). THAT IS THE
SHARED-CAUSE OBJECT IN ITS PUREST FORM: no competitor's revenue or cost line changes because BP wrote
down its own gas and low-carbon assets — only BP's relative standing does. NO COMPETITOR WAS NAMED IN
ANY SOURCE. NOT TAKEN, AND IT WILL BE OFFERED AGAIN.**
**2. Dollar path:** **NOT REACHED** (and an impairment is a non-cash write-down, not a revenue or cost
line at a second company).
**3. Timing window:** **NOT REACHED.**
**4. Invalidation:** **NOT WRITTEN.**

**Hard filters:**
- Priced-in (§4): **NOT RUN** — no Company B.
- Correlation (§4): **vacuous** — zero open positions.
- Universe (§3): **BP is a UK issuer trading in the US as an ADR. Above the cap floor, so §3's
  "ADRs of companies below the cap floor" exclusion does not bite** — ⚠ **but it is FIRST-ORDER and the
  mechanism points DOWN, so §3 was never the operative test and this is recorded as NOT REACHED rather
  than as a pass.**

**Outcome:** **REJECTED on part 1 twice over — no Company B by volunteered absence, and the only sound
mechanism available is a SHORT this strategy cannot express.**

---

### T-2026-10-13-05 — Equinox Gold (EQX) Q3 production + South Railroad federal permits — REJECTED
**Company A / the news:** **2026-10-13** — Equinox reported Q3 production of **237,019 oz** and sales of
**248,484 oz**, held 2026 guidance of **870,000–920,000 oz** (~**1.1M oz** including Orla's full-year
contribution), and received the **Record of Decision and final federal permits** for **South Railroad,
Nevada**, beginning early construction (financialcontent/GlobeNewswire).
**Company B / the candidate:** **NONE — DENIED EXPLICITLY:** *"No second publicly traded US company is
named by the source as directly affected."*

**1. Mechanism (one sentence):** **NOT WRITTEN.**
**2. Dollar path:** **NO FIGURE EXISTS TO BUILD ONE FROM — the release quantifies OUNCES, not dollars,
and attributes NO capital figure to any contractor.** ⚠ **This is form six — a capex blank with no
counterparty at all — carrying a MAP PIN (South Railroad, Nevada) and a PERMIT, which is exactly the
BDX $3B / Bayer Ohio shape.** ⚠⚠ **AND IT IS ALSO JOINTLY UNSATISFIABLE: a single mid-tier gold mine's
construction spend cannot be 10% of revenue at any engineering or mining-services contractor clearing
the $10B floor. The supplier search was pointless before it started.**
**3. Timing window:** **NOT REACHED** (early construction work on a newly permitted mine is years from
reported production revenue, far outside the two-quarter ceiling).
**4. Invalidation:** **NOT WRITTEN.**

**Hard filters:**
- Priced-in (§4): **NOT RUN** — no Company B.
- Correlation (§4): **vacuous** — zero open positions.
- Universe (§3): **NOT REACHED.** EQX's market cap was **not sourced** — UNRESOLVED, not passed. ⚠ EQX
  is in any case **Company A**, and a permit for its own project is **first-order**.

**Outcome:** **REJECTED on part 1 (volunteered absence) and part 2 (no dollar figure, and jointly
unsatisfiable even if one existed).** ⚠ **A PERMIT IS NOT A LEAD AND NEITHER IS A MAP PIN. The
gold-development contractor prior was ready and is NOT written down as a candidate.**

---

### T-2026-10-13-06 — Technip Energies / HPCL €250–500M refinery EPC — REJECTED
**Company A / the news:** **2026-10-13** — Technip Energies won an EPC contract from **HPCL** for a
refinery project, valued only within a **€250M–€500M band**, entering the **Project Delivery** segment's
**BACKLOG** (offshore-technology.com).
**Company B / the candidate:** **NONE REACHED.**

**1. Mechanism (one sentence):** **NOT WRITTEN.**
**2. Dollar path:** **FAILS ON ITS OWN TERMS, TWICE, AND THE SOURCE APPLIED BOTH KILLS BEFORE I DID.**
⚠ **A €250–500M BAND is a self-defined range, not a figure — the FTI/Petrobras "$75–250M significant"
shape, now its second instance.** ⚠⚠ **AND BACKLOG IS NOT SEGMENT REVENUE: the source said the award
*"will enter the Project Delivery segment's backlog, not that it represents a quantified impact on that
segment's revenue."* A BOOKING IS NOT A DOLLAR PATH.**
**3. Timing window:** **NOT REACHED** (refinery EPC revenue recognises over years).
**4. Invalidation:** **NOT WRITTEN.**

**Hard filters:**
- Priced-in (§4): **NOT RUN.**
- Correlation (§4): **vacuous** — zero open positions.
- Universe (§3): **FAILS — Technip Energies is Euronext Paris-listed, not US-listed.** The counterparty
  HPCL is Indian state-controlled. **Neither leg is eligible.**

**Outcome:** **REJECTED at §3 (neither party US-listed) with part 2 failing independently on both the
band and the backlog.** ⚠ **Worth one line because it is the cleanest "the source stated the exclusion
before I applied it" instance of the run.**

---

### T-2026-10-13-07 — §3 / non-qualifying sweep of ELEVEN items — REJECTED (disposed as one, zero queries spent)
**Company A / the news:** everything else the four scans returned, disposed in a single pass against §3
and the standing rules rather than one thesis at a time.
**Company B / the candidate:** **none for any of them.**

**The eleven, each with the test that killed it:**
**Amerigo Resources (ARREF)** — Q3 copper 17.0Mlb, moly 0.4Mlb, cash cost $1.55/lb — ⚠ **OTC, which §3
excludes OUTRIGHT regardless of any other merit** · **Torm** — raised 2026 TCE guidance to $1.7–1.9B
from $1.4–1.6B, **a genuinely large revision** — **Danish, no US listing established** · **Bachem** —
guidance narrowed to 35–40%, **>CHF 500M** Sisslerfeld investment — **Swiss, AND the announcement date
was not established inside the window (rule iii)** · **Aequs/Safran** — supply agreements, **no contract
value**, neither US-listed · **IRCON International** — ₹862.45 crore EPC award — **governmental
counterparty (East Central Railway), Indian issuer** · **Bharat Electronics (BEL)** — ₹533 crore of
additional orders — **Indian, and no customer-by-customer breakdown or individual contract values** ·
**Hiteck/Visara** licensing — **an "up to" CEILING, parties' status unestablished** · **Bluejay/Toray** —
a contractual manufacturing milestone with **NO dollar amount** · **Saudi Steel Pipe/Aramco** and
**Al-Yamamah Steel** 380kV towers — **non-US issuers** · **ADSB/Kuwait MoD** — **non-US, governmental
counterparty**.

**Hard filters:** not reached for any of the eleven — all died at §3 or on the absence of a figure.
**Outcome:** **ALL REJECTED, ZERO follow-up queries spent.** ⚠ **`--recency day` returns a GLOBAL tape
and roughly half of each run's raw funnel output is non-US. That is not a defect in the query; it is
why §3 is applied before a mechanism is attempted.**

---

### T-2026-10-13-08 — The forward calendar: bank prints today, ASML/TSMC this week — REJECTED (rule iii, purest form)
**Company A / the news:** **NOTHING HAS HAPPENED YET.** The scans returned **JPM/C/WFC reporting today
(2026-10-13)**, **September CPI 10-14**, **PPI and retail sales 10-15**, and an **ASML/TSMC earnings
preview** carrying ASML low-NA EUV capacity lines (*"approximately 65 machines in 2026, rising to around
85 in 2027 and potentially 110 in 2028"*) in the frame *"can they restore confidence in the AI trade."*
**Company B / the candidate:** **NONE — there is no event to be second to.**

**1–4:** **NOT WRITTEN.** ⚠⚠ **THIS IS RULE (iii) AT ITS EARLIEST POSSIBLE FAILURE POINT: the question
"is this new to the company's own disclosure?" cannot be passed by an event NOBODY HAS DISCLOSED BECAUSE
IT HAS NOT HAPPENED.**
⚠⚠ **IT WAS ALREADY MET AND REJECTED ON 10-12 AS `T-2026-10-12-05`, AND IT ARRIVED AGAIN TODAY WITH THE
SAME CONTENTS — which is the second half of that entry's prediction coming true: "a reporting date is
not a lead," and the 10-13 prints are *"for the 10-13 seat to meet."* ⚠ **THE 10-13 SEAT HAS NOW MET
THEM, AT 08:26, BEFORE THEY LANDED, AND THEY ARE STILL NOT AN EVENT.** The correct response is unchanged:
note the dates, write nothing, and let the CLOSE seat see the actual prints.**
⚠ **AND THE ASML LINES ARE A CAPACITY *ROADMAP*, NOT A TRANSACTION — the 2027 and 2028 legs are outside
the two-quarter ceiling on their face, and the AMAT/LRCX/KLA prior they summon is this log's single most
reflexive one.** ⚠ **§4 would kill the competitor read-across from any of these prints anyway: a peer's
earnings print is the shared-cause object, not a mechanism.**

**Outcome:** **REJECTED — a scheduled event is not an event.** ⚠ **The 10-12 entry predicted this shape
would recur on Mondays; today shows it recurs whenever a dense data week is AHEAD, not only after a
weekend. Expect it all week.**

---

### 2026-10-12 (08:36 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,879.52** at
pre-flight). `clock` at **08:36:59** reads `is_open: false` with `next_open` **2026-10-12T09:30** and
`next_close` **2026-10-12T16:00** — both carrying **TODAY's** date, the **PRE-MARKET full-session
signature**, read off the **DATE** because FALSE has three meanings and TRUE has one. **Not a holiday,
not an early close.** Window screened: **the completed 2026-10-09 session, the weekend, and overnight
into Monday 2026-10-12** — a **THREE-CALENDAR-DAY, ONE-TRADING-DAY** window, which is the Monday shape.
**Four Perplexity scans, all exit 0** (three broad/structural, one drill on the single real event).
**Five theses written, ALL FIVE REJECTED.** Zero `move` calls — see the note at the foot of this block.

**⚠⚠ THE STRUCTURAL FRAMING WAS QUERY ONE AGAIN AND IT PAID A FOURTH CONSECUTIVE SESSION — BUT TODAY IT
ALSO SHOWED ITS OWN LIMIT, AND THAT IS THE RUN'S ONE REAL FINDING. SEE `T-2026-10-12-01`.** Asking for
**two named parties + a disclosed dollar amount + the announcement date + whether it is new to the
company's own disclosure** returned a **volunteered absence in the source's own words** — *"no
announcement that can be verified as meeting all of the requested criteria"* — against **EIGHT
self-excluded items with the reason attached**: Fortem/MBDA flagged as *"does not disclose a dollar
amount"* **and** as building on *"a technical collaboration established in 2024"*; Blend Labs' tenth
lender flagged as **unnamed**; HITT/NIST flagged as *"up to $600 million"* with the announcing party's
listing unverifiable; **RTX's SM-3 Block IB flagged as unverifiable pending a primary source**;
Ascenty/Casa dos Ventos' $500M flagged as *"previously announced in January 2026"*; Bimergen's $400M
flagged as **a growth strategy, not a contract**; New River Valley flagged as **a contract that was NOT
finalised**; IPA Capital Markets flagged as parties-unidentified. **Eight items disposed for ZERO
follow-up queries.**

**⚠⚠ THE SECOND FRAMING (won-a-contract / quantified-to-its-own-segment) ALSO RETURNED A VOLUNTEERED
ABSENCE — *"No company can be confirmed to meet the full screen from the information gathered"* — AND
THE TWO FRAMINGS REMAIN COMPLEMENTARY RATHER THAN REDUNDANT.** It named the part-2 gap explicitly on the
one item it offered: RTX *"does not report RTX's own quantified revenue impact for the Raytheon
segment."* That is the most common killer in this log, stated by the source before I applied it.
**THIS IS THE TENTH CONSECUTIVE SESSION IN WHICH THE FUNNEL HAS ANSWERED §4's QUESTION IN THE NEGATIVE
OUT LOUD, 09-29 THROUGH 10-12 UNBROKEN, AND THE THIRD IN WHICH *EVERY* BROAD SCAN PRODUCED ONE** — the
third scan's own closing line: *"It does not provide reliable evidence of a specific U.S. corporate
earnings surprise, regulatory decision, guidance revision, or capacity announcement between October 9
and October 12, 2026."*

**⚠⚠ THE LOG WAS READ BEFORE THE TAPE AND IT PAID FOR A SECOND CONSECUTIVE SESSION — THREE DISPOSED
REJECTS WERE RE-SERVED, AND ONE OF THEM TWICE IN ONE RUN BY TWO DIFFERENTLY-FRAMED QUERIES.**
**RTX's SM-3 Block IB "up to $6.3B"** (disposed 10-09, re-served by **both** query 1 and query 2) ·
**Samsung Electro-Mechanics ₩290B** (disposed 10-09 in that day's §3 sweep, re-served verbatim) ·
**KEC International** (disposed 10-09, re-served with a fresh ₹1,030 crore figure).
⚠ **A recency filter bounds when something was WRITTEN, never when it HAPPENED. Reading the log cost
one grep and saved three drills.**

---

### T-2026-10-12-01 — *no ticker* — REJECTED
**Company A / the news:** **2026-10-09** — President Trump said he had agreed with President Putin that
Russia would supply the US with **more than 300,000 tons of diesel immediately**, a further **500,000
tons during November** and **1 million tons thereafter**, with a possible additional **3 million tons**
subject to Russian refinery conditions. The **US Treasury directed OFAC to issue a temporary general
licence** authorising the sale, delivery, offloading and importation of Russian-origin diesel into the
United States **through 2027-04-07**. Oil fell ~1.5% on the announcement.
**Company B / the candidate:** **NONE — AND THE SOURCE SAID SO WHEN ASKED DIRECTLY.** A drill query
asking whether any US-listed company is named as purchaser, importer, shipper, refiner, distributor,
terminal operator or contractual counterparty returned, verbatim: *"no specific publicly traded U.S.
company is named"* … *"it does not identify a commercial buyer, U.S. importer of record, vessel
operator, refinery, distributor, storage-terminal operator, or other corporate counterparty"* … **"No
dollar amount is attributed to any named U.S.-listed company."**

**1. Mechanism (one sentence):** **NOT WRITTEN.** There is no Company B to put in the sentence. Every
construction available requires a second clause — *"the arrangement lowers US distillate prices **and
also** therefore Company B's fuel cost line improves"* — which is §4's own stated kill for part 1.
**2. Dollar path:** **NO OPERAND.** The quantities disclosed are **TONNAGES**, not dollars, and no
figure of any kind is attributed to a named company, so there is no segment and no percentage to
compute. *(This is the **Elevra "tonnes not dollars"** shape from 10-09, arriving at vastly larger
scale — and scale does not convert a tonnage into a dollar path.)*
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:** not reached — the candidate died at part 1 for want of a Company B. **No `move` call
was made and none was due: there is no ticker to call it on.**

**Outcome:** **REJECTED on part 1 — there is no Company B, confirmed by explicit source denial rather
than by my own reasoning.** Secondarily, part 2 has no operand.

**⚠⚠ THE REASON THIS IS THE RUN'S ONE REAL FINDING: IT IS THE FIRST MACRO/GOVERNMENT OBJECT THAT
*SATISFIES THE STRUCTURAL QUERY FRAMING'S SHAPE* AND STILL FAILS §4 — SO THE FRAMING THIS LOG HAS BEEN
PROMOTING FOR SIX SESSIONS HAS A FALSE-POSITIVE FORM, AND THIS IS IT.** The framing asks for **two named
parties, a dated announcement and a disclosed quantity**, on the theory that a query naming §4's
required shape returns that shape or says it cannot. **This event has all three: two named parties (the
United States and Russia), a precise date (10-09), a dated schedule (immediate / November / thereafter),
a regulatory instrument with an expiry (the OFAC licence to 2027-04-07), and a quantity ladder
(300,000 / 500,000 / 1,000,000 / 3,000,000 tons).** ⚠⚠ **AND IT IS UNTRADEABLE, BECAUSE THE TWO NAMED
PARTIES ARE *SOVEREIGN STATES* AND THE DISCLOSED QUANTITY IS *NOT MONEY*.** ⚠ **THE FRAMING SCREENS FOR
STRUCTURE, NOT FOR *PARTY TYPE* OR *UNIT*. Add both to what the structure must satisfy: the parties must
be COMPANIES and the quantity must be DOLLARS AT COMPANY B.** ⚠ **This does not weaken the framing —
it is still the query that reaches the funnel's actual inventory — but "it returned the shape" is no
longer sufficient grounds to proceed to a mechanism.**

**⚠⚠ THE PRIORS ARRIVED INSTANTLY AND SPECIFICALLY, AGAINST AN EXPLICIT DENIAL, AND NONE IS WRITTEN
DOWN AS A CANDIDATE: the US refiner complex (VLO, MPC, PSX) on crack spreads and import economics, and
the fuel-cost tier (DAL, UAL, UPS, FDX) on distillate.** ⚠ **The second set is the more seductive
because it reads as a clean COST-LINE improvement, which is a form §4 part 1 explicitly permits — and it
fails anyway on three independent grounds: airlines burn JET FUEL rather than diesel, so the causal path
needs a product-substitution clause; a commodity price is a MARKET VARIABLE, which is the shared-cause
object in its purest form (two companies moving on the same input is a market, not a transaction); and
the arrangement is a PRESIDENTIAL STATEMENT with no executed commercial contract, so there is no
transaction to be second to.**
⚠⚠ **AND THE EVENT-TYPE OBSERVATION, WHICH IS RULE (iv) ONE LEVEL UP FROM WHERE IT WAS WRITTEN: THIS IS
THE *SECOND* DIESEL-RELEASE ITEM THIS FUNNEL HAS SERVED IN SIX SESSIONS** (the **G7 diesel release** was
disposed on **10-05**), **and it died the same death both times.** ⚠ **Rule (iv) is written about a
recurring TICKER being a warning rather than corroboration. A recurring EVENT TYPE carries the same
message and has not been written down before: it is telling me about the ENERGY-POLICY NEWS CYCLE'S
disclosure practice — sovereign announcements, tonnages, no corporate counterparty — not about a
candidate maturing.**
⚠ **A GOVERNMENT ACTION IS NOT A COMPANY A, and this is the most convincing costume yet recorded: it
has TWO named parties rather than one, a tonnage ladder, an expiry date, a named regulatory instrument,
and it MOVED THE TAPE. Scale and specificity make it more convincing, not less.**

---

### T-2026-10-12-02 — RTX — REJECTED (EXACT REPEAT, ZERO QUERIES SPENT)
**Company A / the news:** RTX's **SM-3 Block IB** interceptor agreement, *"up to $6.3 billion"* — the
**same award, same programme, same figure** disposed on **2026-10-09**.
**Company B / the candidate:** none sought. **The answer was already written down.**

**Outcome:** **REJECTED without spending a query — this is what the disposed-reject catalogue is for.**
The written kill stands unchanged on four independent grounds: **RTX is FIRST-ORDER** (it is the named
recipient, so §4's premise does not apply at any price); the figure is a **CEILING** (*"up to"*), which
is rule (v)'s ceiling sub-shape and not a revenue number; the counterparty is a **government body**, so
there is no Company A that is a company; and **no supplier below RTX is named**, which is the
eleven-instance US-defence-award pattern — the mechanism there is **disclosure practice**, not the
primes' size.
**⚠⚠ THIS IS RTX's *FOURTH* APPEARANCE IN SEVEN SESSIONS AND ITS SECOND ON THIS IDENTICAL AWARD** (09-29
AMRAAM $20.7B · 10-02 SM-6 *"up to"* $24.4B · 10-09 SM-3 *"up to"* $6.3B · **10-12 SM-3 again**). ⚠ **A
recurring ticker is a WARNING, NOT CORROBORATION — and a ticker re-arriving on the *same* award with the
*same* figure is the strongest form of that warning, because nothing about it has changed at all.**
**⚠⚠ THE NEW PART IS WHERE IT CAME FROM: TWO DIFFERENTLY-FRAMED QUERIES SERVED IT IN ONE RUN, AND THE
SECOND FRAMING CAME *CLOSER TO ACCEPTING IT* THAN THE FIRST.** Query 1 excluded it as unverifiable
pending a primary source; query 2 called it *"the closest apparent match"* and killed it specifically on
**part 2** — *"does not report RTX's own quantified revenue impact for the Raytheon segment."* ⚠ **A
disposed reject can arrive dressed as a run's best candidate, and the only thing that stopped it being
re-elaborated from scratch was reading the log first.**

---

### T-2026-10-12-03 — §3 / NON-QUALIFYING SWEEP (THIRTEEN ITEMS, ONE ENTRY) — REJECTED
Disposed as one entry because each dies on a **single** test applied **before** any mechanism was
attempted — §3-first, which is the discipline that stops effort going into a story one number was always
going to end.

**Not US-listed (§3):** **Samsung Electro-Mechanics** ₩290B AI-server MLCC supply (Korea-listed; **EXACT
REPEAT of 10-09**; and the counterparty is an **unnamed** *"global company"*, so it fails rule (v) too) ·
**KEC International** ₹1,030 crore (India-listed; **repeat of 10-09**) · **SEPC** ₹855 crore SAIL order
(India-listed, and far below the cap floor) · **Mitsubishi Heavy Industries** train order (Japan-listed) ·
**Tialis Essential IT** £7.6M + £1.2M extension, **Thruvision**, **Acuity RM Group** (UK-listed
microcaps) · **MBDA** (private European consortium).
**Below the §3 $10B cap floor or not listed at all:** **Fortem Technologies** (private) · **HITT
Contracting** (private) · **Bimergen Energy** (microcap) · **Ascenty** (private, Brazil).
**Rule (iii) — not new to the parties' own disclosure:** **Fortem/MBDA** builds on *"a technical
collaboration established in 2024"*, volunteered by the source · **Ascenty/Casa dos Ventos** $500M
renewable supply agreement was **announced in January 2026** and merely re-reported on 10-12 —
**the source excluded it before I did.**
**Rule (v) — no named counterparty, or a ceiling rather than a figure:** **Blend Labs'** *"tenth
lender"* is **unnamed** and carries no figure · **HITT/NIST** is *"up to $600 million"* over a
five-year ordering period — **a CEILING against a government body** · **IPA Capital Markets**, parties
unidentified.
**No transaction at all:** **Bimergen's** $400M is a **growth strategy presented at a conference**, not
an agreement · **New River Valley Commerce Park** is a contract a company **DECLINED TO FINALISE** —
⚠ **a deal that did NOT happen, which is a new sub-shape worth one line: the funnel will serve the
ABSENCE of a transaction in the same format as a transaction, and the headline reads identically.**

**Outcome:** **ALL THIRTEEN REJECTED upstream of §4's parts, for ZERO follow-up queries.**
⚠ **`--recency day` returns a GLOBAL tape — a clear majority of today's raw funnel output was non-US
again. That is not a defect in the query; it is why §3 is applied before a mechanism is attempted.**

---

### T-2026-10-12-04 — *no ticker* — REJECTED (THE MACRO/FISCAL COMPLEX)
**Company A / the news:** **2026-10-09** — University of Michigan preliminary survey: consumers raised
one-year-ahead inflation expectations. **2026-10-12** — CBO-cited reporting put the **FY2026 federal
deficit at ~$2 trillion**, with **net interest above $1 trillion for the first time** and **corporate
tax receipts down 16% to $382 billion**.
**Company B / the candidate:** **NONE. No company is named in any of it.**

**Outcome:** **REJECTED on part 1 — a government or macroeconomic datum is not a Company A.** It is the
standing object: one party (or none), no transaction, no named recipient.
⚠ **THE ONE GENUINELY NEW OBSERVATION, AND IT IS A WARNING RATHER THAN A LEAD: `corporate tax receipts
−16% to $382 billion` IS THE MOST COMPANY-ADJACENT MACRO NUMBER THIS FUNNEL HAS PRODUCED.** It is
precise, it is dated, it is denominated in dollars, and it is *about corporate earnings in aggregate* —
so it reads closer to a corporate fact than rates, payrolls or tariffs ever did. ⚠⚠ **AND IT NAMES
NOBODY, which is exactly the point: an aggregate over all companies is a statement about the TAX BASE,
not about any company's revenue or cost line. A number can be more corporate-sounding and no more
tradeable.**

---

### T-2026-10-12-05 — *no ticker* — REJECTED (THE FORWARD CALENDAR — A NEW MONDAY-SHAPED NON-EVENT)
**Company A / the news:** the third broad scan's largest single block was the **WEEK AHEAD**:
**JPMorgan Chase, Citigroup and Wells Fargo** reporting **Tuesday 2026-10-13**; **September CPI on
10-14** (consensus cited at **+0.6% m/m, +3.7% y/y headline, +0.2% m/m core**); **PPI and retail sales
on 10-15**.
**Company B / the candidate:** none. **Nothing has happened yet.**

**Outcome:** **REJECTED — a CALENDAR is not news, and three large US banks are NAMED here purely as
scheduled reporters.** The source said so itself: *"not as results announced during October 9–12"* and
*"Scheduled earnings events, not reported earnings surprises."*
**⚠⚠ THIS IS A NEW SHAPE AND IT IS SPECIFIC TO THE MONDAY PRE-MARKET SEAT, WHICH IS WHY IT HAS NOT BEEN
SEEN BEFORE: THE WEEKEND WINDOW CONTAINS NO TRADING AND LITTLE CORPORATE DISCLOSURE, SO THE FUNNEL FILLS
THE SPACE WITH THE WEEK AHEAD.** ⚠ **A forward calendar is the single most dangerous empty object this
funnel produces, because it arrives carrying EVERYTHING §4 asks for except the event: named US-listed
companies above $10B, precise dates, and even consensus NUMBERS — and a run reading quickly can mistake a
consensus figure for a disclosed one.** ⚠⚠ **IT IS ALSO THE PUREST FORM OF rule (iii): the earliest
possible failure of "is this new to the company's own disclosure?" is an event that has not been
disclosed by ANYONE yet because it has not occurred.** ⚠ **The correct response is to note the dates and
do nothing. An earnings print on 10-13 is a thing for the 10-13 seat to meet, not a thing for this seat
to anticipate — and §4 would kill the read-across anyway as the competitor's-earnings-print shared-cause
object.**

---

**⚠⚠ ZERO `move` CALLS AT THIS SEAT, AND THAT IS AN *ABSENT* CHECK RATHER THAN A SKIPPED ONE — THE
DISTINCTION THIS LOG KEEPS INSISTING ON, BECAUSE THE TWO LOOK IDENTICAL IN A RUN SUMMARY.** The priced-in
filter had **nothing to fire on**: **four of today's five rejects carry no ticker at all** (two macro
objects, a forward calendar, and a Company-B-less supply arrangement), the fifth is a disposed repeat on
a **first-order** name, and the thirteen-item sweep died at §3 upstream of the filter. ⚠⚠ **A DECORATIVE
`move` CALL ON A NAME WITH NO MECHANISM CONVERTS AN HONEST ABSENCE INTO A FAKE EXERCISE, AND IT HAS NOW
BEEN DECLINED FOR THAT REASON A THIRD TIME.** ⚠ **NOT COUNTABLE AS A ZERO-`move` SESSION FROM HERE —
THREE SEATS REMAIN TODAY. The honest unit is the SESSION and a session is only countable once it is
over; writing "the seventh" now would be catch (11)'s shape.**

**⚠⚠ THE RUN'S SUMMARY JUDGMENT, STATED PLAINLY: NO TRADE, AND NOT A SINGLE CANDIDATE REACHED §4's
PARTS.** 10-09 was the session where one finally did (**GFS**, killed by parts 3 and 2 out of the
company's own release). **Today did not get close: the funnel's entire US corporate inventory for a
three-calendar-day window was one sovereign supply announcement, a disposed repeat, a forward calendar
and two macro aggregates.** ⚠ **That is a property of the WINDOW — a weekend plus a Monday pre-market —
and it is the expected shape of a Monday, not a finding about the tape.** ⚠⚠ **IT IS ALSO EXACTLY WHAT
§4's HONEST-BROKER PARAGRAPH DESCRIBES AS THE CORRECT OUTPUT: five auditable rejections, zero
manufactured mechanisms, and $30,000 left idle because nothing earned it.**


### 2026-10-09 (08:27 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,743.83** at
pre-flight). Window screened: **the completed 2026-10-08 session and overnight into 2026-10-09** — a
real window; 10-08 was a full session (official close 711.23). `clock` at **08:27:45** reads
`is_open: false` with `next_open` **2026-10-09T09:30** — the **PRE-MARKET** shape, read off the
**DATE**, not off the boolean. Not a holiday. **Five Perplexity scans, all exit 0** (three broad/
structural, two drills on the single survivor). **Eight theses written, ALL EIGHT REJECTED.**

**⚠⚠ THE STRUCTURAL FRAMING WAS QUERY ONE AGAIN AND IT PAID A THIRD CONSECUTIVE SESSION.** Asking for
**two named parties + a disclosed dollar amount + the announcement date + whether it is new to the
company's own disclosure** returned **one qualifying item and NINE self-excluded ones with the reason
volunteered** — Transocean/Equinor flagged as *"previously announced"* by Transocean itself,
Shield AI flagged as *"a modification of an existing Other Transaction agreement"*, TechnipFMC flagged
as a **range** (`$75–250M`) rather than a figure, Elevra flagged as **tonnes not dollars**, BAE and
Voyager flagged as listing-unverifiable. **Nine items disposed for ZERO follow-up queries.**

**⚠⚠ ALL THREE BROAD SCANS PRODUCED A VOLUNTEERED ABSENCE — THE SECOND CONSECUTIVE SESSION OF THAT,
AND A NINTH CONSECUTIVE SESSION OF AT LEAST ONE.** In the source's own words:
*"No company identified in the available evidence meets the full screen"* (the won-a-contract /
quantified-to-its-own-segment framing) · *"no qualifying case can be verified … there is no verified
qualifying announcement to report"* (the named-second-company framing) · and query 1's one-for-nine
exclusion ratio. **A FOURTH absence arrived from the GFS drill and it is the most specific of the
four:** GF's own 10-08 release *"does not name any specific publicly traded equipment supplier,
construction contractor, engineering firm, or materials vendor"* for the Malta expansion, and
*"no dollar amount is attributed to one."*

**⚠ READY-AND-UNWRITTEN PRIORS THIS RUN: AMAT / LRCX / KLA for the Malta fab expansion — the single
most reflexive prior in this log, named in the carry-forward as the standing failure mode, and
arriving against an EXPLICIT DENIAL. NOT WRITTEN DOWN AS A CANDIDATE.** Also ready and unwritten: the
solid-rocket-motor tier for SM-3 Block IB, and the subsea-flexibles tier for TechnipFMC/Petrobras.
**A volunteered absence is stronger than a silence, and a run that then produces a Company B has
supplied it from its own priors.**

**⚠ `--recency day` RETURNED A GLOBAL TAPE AGAIN** — roughly half the raw funnel output was non-US
(Fujifilm, Samsung Electro-Mechanics, LG Electronics, BAE, KEC International, Arqit). That is not a
defect in the query; it is why §3 is applied before a mechanism is attempted. Disposed as one entry
(`T-2026-10-09-08`).

---

### T-2026-10-09-01 — GFS (GlobalFoundries) / TSMC silicon interposers — REJECTED
**Company A / the news:** **GlobalFoundries' own press release, 2026-10-08** (globenewswire /
gf.com), *"GlobalFoundries reaches agreement to establish U.S.-based supply of silicon interposers for
advanced AI packaging"* — GF will manufacture silicon interposers for **TSMC**, supporting TSMC's
CoWoS advanced-packaging platform, and will add fab capacity at **Malta, New York**. Reuters and
Bloomberg reported the value as **$2 billion** over an **initial five-year term** the same day.
**Company B / the candidate:** **GFS itself** — which is the first problem, see part 1.

**1. Mechanism (one sentence):**
> TSMC's decision to source US-made silicon interposers causes GlobalFoundries' Malta manufacturing-
> services revenue to rise because GF will produce and sell interposers to TSMC under a five-year,
> $2 billion agreement.

⚠ **The sentence is clean and needs no "and also" — and it still fails §4, because GFS IS THE HEADLINE
NAME.** The announcement was issued **by GF, about GF**; Bloomberg's headline is *"GlobalFoundries
rallies after announcing $2 billion TSMC deal"*; and the tape agrees — **10-08 printed `n` 6,578 trades
on `v` 522,592 shares against a trailing norm of ~1,400–1,700 trades on ~68k–142k shares, roughly 4x
the trades and 6x the volume.** §4's premise is that news breaks about Company A and you buy Company B.
**Here GF is Company A.** The genuine second-order question — *who supplies GF's Malta expansion?* —
was put to the funnel and returned a **verbatim denial** (no equipment supplier, contractor, engineering
firm or materials vendor named anywhere; no dollar attributed to one). **THERE IS NO COMPANY B.**

**2. Dollar path:** **FAILS INDEPENDENTLY, AND THE ARITHMETIC IS ONE STEP.** $2B over the initial
five-year term = **~$400M/yr**, against GF **FY2025 total revenue of $6.791B** (sourced to the funnel's
own citation) = **5.89% of total revenue**. §4's floor is **10%**. ⚠ **And that is the MOST GENEROUS
possible reading, because it treats the whole company as the "segment": GF has NOT assigned the
agreement to a reporting segment at all, so the actual segment share is not merely small, it is
NOT CALCULABLE.** The funnel said so explicitly: *"the sources returned do not establish whether GF
will report it within an existing product category, its CMOS business, a manufacturing-services
category, or another reporting line."*

**3. Timing window:** **FAILS INDEPENDENTLY AND THIS IS THE PRIMARY KILL — IT IS QUOTED FROM GF'S OWN
RELEASE AND IT IS NOT A JUDGMENT CALL.** *"Volume production is expected to begin ramping at GF's Malta
site during the first half of 2028."* From Q4 2026 that is **SIX QUARTERS MINIMUM** (2027Q1 … 2028Q2)
against §4's **TWO-QUARTER** ceiling — and **revenue recognition is later still and undisclosed**: the
funnel declined to put a quarter on it, noting GF discloses no delivery terms, acceptance provisions,
pricing structure or customer commitments. **Standing rule (vi) in its cleanest form yet: screen the
timing window early on anything under construction. Part 3 kills this in ONE step, and it is the
Venture Global / ConocoPhillips shape with a shorter fuse.**

**4. Invalidation:** **NOT REACHED — there is no trade, so no invalidation condition was written.**
⚠ Recorded deliberately: writing one here would mean constructing the apparatus of a position that
three independent tests have already refused.

**Hard filters:**
- **Priced-in (§4): moved +1.48% over last 5 sessions (48.65 → 49.37) → PASS.** ⚠⚠ **AND IT PASSES ON
  THE NEWS-DAY BASIS TOO, WHICH IS THE CHECK THAT MATTERS: 10-07 close 48.065 → 10-08 close 49.37 =
  +2.72%, also under 4%.** Both bases pass. **This is the FIRST RECORDED INSTANCE OF THE FILTER WORKING
  BY *ACCEPTING* A GENUINE NEWS-DAY MOVE** — every prior instance of "the filter working" (SHOP +9.61%,
  ILMN +11.54%, GRAL +44.67%) was the filter working by **REJECTING**. ⚠ **Stated with its limit:
  10-08 traded to an intraday high of **51.42, +6.98% over the prior close**, and closed **−3.99% off
  that high** at 49.37. A close-to-close filter cannot see that excursion; had the close held near the
  high, the same day's news would have FAILED the filter. The filter was right here and it was not
  right by a wide margin.** ⚠ **THE TRADE DIED ON THE THESIS, NOT ON THE FILTER — which is the whole
  point of applying §4's parts after the filters rather than instead of them.**
- **Correlation (§4): pass, TRIVIALLY AND WORTH NOTHING.** Zero open satellite positions, so there is
  no `driver` field anywhere in `positions.md` to collide with. **An absent check, not a passing one.**
- **Universe (§3): asset_type stock. `alpaca.py asset --symbol GFS` → `us_equity`, NASDAQ, active,
  tradable, fractionable, not leveraged / inverse / crypto → pass on every instrument test.**
  ⚠⚠ **MARKET CAP: NOT ESTABLISHED FROM SOURCE. §3 IS UNRESOLVED, NOT PASSED.** The funnel was asked
  twice and declined both times (*"the search results provided do not include a dated market-data source
  stating GlobalFoundries' market capitalization"*). ⚠ **A share count × 49.37 would clear $10B
  comfortably on my own arithmetic — AND THAT IS NOT A SOURCED FIGURE AND IS NOT RECORDED AS ONE.**
  ⚠ **This follows the VAL precedent exactly: DO NOT INHERIT A §3 VERDICT FROM THIS ENTRY. It did not
  need resolving, because parts 2 and 3 kill the thesis without it.**

**Outcome:** **REJECTED — THREE INDEPENDENT KILLS.** **Part 3 is primary** (H1 2028 ramp, six quarters
against a two-quarter ceiling, quoted from GF's own release). **Part 2 is independent and arithmetic**
(~$400M/yr on $6.791B = 5.89%, below the 10% floor, and the segment share is not calculable at all).
**Part 1 is independent and structural** (GFS is the headline name; the second-order search returned a
verbatim denial; the only Company B on offer is the AMAT/LRCX/KLA prior, which the source explicitly
refused to supply).
⚠⚠ **THIS IS THE BEST-DISCLOSED CANDIDATE THIS FUNNEL HAS PRODUCED IN WEEKS AND IT IS WORTH SAYING SO
PLAINLY: an official, dated, company-issued press release · two named parties · a dollar figure
attributed to the US-listed leg by Reuters and Bloomberg · no rule (iii) problem (no earlier GF
disclosure of a TSMC interposer agreement exists) · every §3 INSTRUMENT test passed · and the priced-in
filter passed on BOTH bases.**
⚠⚠ **CORRECTION MADE BEFORE PUBLICATION — CATCH (23), AND IT IS CATCH (13)'s EXACT SHAPE.** This entry
first read *"the FIRST candidate in the live log to clear §3's instrument tests AND the priced-in filter
and then die on the thesis parts."* **THAT IS FALSE, AND THE REFUTING ENTRY WAS IN A FILE THIS RUN HAD
ALREADY READ.** **IT IS THE *SECOND* CANDIDATE TO CLEAR §3's INSTRUMENT TESTS AND THE PRICED-IN FILTER AND THEN DIE ON §4's PARTS — **AMD** (`T-2026-10-01-02`) DID IT FIRST ON 10-01, WITH A *STRONGER* §3 PASS (cap "far above the $10B" floor, where GFS's is UNRESOLVED) AND THE SAME PRIMARY KILL, PART 3.**
⚠ **AMD: `Priced-in (§4): AMD −0.52% over 5 sessions (614.84 → 611.65), priced_in: false` ·
`Universe (§3): PASSES — AMD is US-listed common stock on NASDAQ, market cap far above the $10B` floor ·
`Outcome: REJECTED on part 3 (not establishable), with part 2 (magnitude undisclosed and immaterial)`.**
⚠⚠ **WHAT SURVIVES THE CORRECTION IS NARROWER AND STILL WORTH RECORDING — AND IT IS THE PRICED-IN HALF,
NOT THE CLEARED-EVERY-FILTER HALF: AMD's pass was on a **−0.52% NON-EVENT** drift (the
"exercised-and-non-decisive" state), while GFS's pass is on a **GENUINE NEWS DAY** — 4x trades, 6x
volume, a real transaction. **THAT is the first of its kind. "Cleared every filter" was not.**
⚠ **AND THE NON-SUPERLATIVE OBSERVATION IS THE MOST USEFUL THING HERE: PART 3 KILLED BOTH. Of the two
candidates that have ever reached §4's parts with the filters behind them, the TIMING WINDOW killed
both, and part 2 was failing in both as well.**
⚠⚠ **IT IS NOT A NEW REJECT FORM — IT IS FORM SEVEN ("everything is disclosed and the spending lands
too far out", Bayer's 2031/2034 holding the record) IN ITS STRONGEST INSTANCE YET, because the
beneficiary here is US-listed, liquid, buyable, un-priced-in and the headline name. Bayer was none of
those. THE DIFFERENCE IS THAT THIS TIME THE ONLY THING STANDING BETWEEN THIS RUN AND A BUY ORDER WAS
PART 2's AND PART 3's ARITHMETIC — and both were computable from the company's own release in one step
each.** ⚠ **The temptation this entry records honestly: a clean one-sentence mechanism, a real
transaction, a real counterparty and a stock that has not moved is the most buyable-looking object §4
can meet, and §4's parts are what stopped it. THE RULES DID THE WORK; THE JUDGMENT DID NOT HAVE TO.**

---

### T-2026-10-09-02 — RTX (Raytheon) / US DoD SM-3 Block IB "up to $6.3B" — REJECTED
**Company A / the news:** The Pentagon awarded **Raytheon (RTX)** a multi-year contract valued at
**up to $6.3 billion** for production and sustainment of **Standard Missile-3 Block IB** interceptors.
Reported **2026-10-08**, with the underlying contract notice dated **2026-10-07** (insidedefense,
Reuters, Economic Times).
**Company B / the candidate:** **NONE REACHED, AND NO QUERY WAS SPENT REACHING FOR ONE.**

**1. Mechanism:** **NOT WRITTEN. The settled pattern was applied as written.**
**2–4:** not reached.

**Hard filters:** not reached — disposed upstream.

**Outcome:** **REJECTED on the settled US-defence-award pattern, ZERO funnel queries spent.**
⚠ **THIS IS THE TENTH INSTANCE and the carry-forward's instruction was explicit: spend ONE query, write
the answer down, and STOP. No re-query has ever been issued and none was issued here.** The mechanism
of the pattern is **DISCLOSURE PRACTICE**: a prime announces the award and the tier below it is
commercially confidential.
⚠ **THREE INDEPENDENT KILLS ON TOP, each one already in the log's standing rules:**
**(a) RTX is FIRST-ORDER** — the named recipient, outside §4 at any price.
**(b) "UP TO $6.3 BILLION" IS A MAXIMUM POTENTIAL VALUE, NOT A CONTRACT FIGURE** — standing rule (v)'s
**CEILING sub-shape**, the same object as RDW's $980M and MTUS's $995M, and the same object as **RTX's
OWN SM-6 "up to $24.4B" on 10-02**.
**(c) THE COUNTERPARTY IS A GOVERNMENT BODY, SO THERE IS NO COMPANY A IN §4's SENSE** — one party, no
transaction between two nameable commercial legs.
⚠⚠ **AND STANDING RULE (iv) FIRES HARDEST HERE: RTX IS NOW IN THIS LOG FOR THE THIRD TIME IN SIX
SESSIONS (09-29 AMRAAM $20.7B · 10-02 SM-6 "up to" $24.4B · 10-09 SM-3 Block IB "up to" $6.3B), AND IT
HAS DIED THE SAME DEATH EVERY TIME.** ⚠ **A recurring ticker is a WARNING, not corroboration. RTX
arriving every third session is telling me about the defence sector's DISCLOSURE PRACTICE, not about a
candidate maturing.** ⚠ **The second query this run also surfaced the 10-02 SM-6 award again, side by
side with the new one — the funnel is now re-serving its own disposed rejects, which is a reason to read
the log before the tape, not after.**

---

### T-2026-10-09-03 — RIG (Transocean) / A/S Norske Shell $62M, + Equinor ~$1.0B — REJECTED
**Company A / the news:** **Transocean (NYSE: RIG)** announced **2026-10-09** approximately **$62M**
of firm contract backlog from a **new two-well contract** for the *Transocean Norge* with **A/S Norske
Shell** (~120 days of work), and in the same release reported ~**$1.0B** of contract value from an
**Equinor** agreement. **This was the funnel's ONE "qualifying" item of the day.**
**Company B / the candidate:** **NONE — RIG is the recipient and is first-order.**

**1. Mechanism:** **NOT WRITTEN — RIG is the named recipient of its own announcement, not a
second-order beneficiary.**
**2. Dollar path:** $62M of **BACKLOG**, not recognised revenue — and backlog converting over ~120 days
is not a segment revenue line. Not reached in any case.
**3–4:** not reached.

**Hard filters:**
- **Universe (§3): FAIL. Market cap ~$6.19B** (source: the funnel's own citation, gurufocus /
  Business Insider coverage of the 10-09 release), **below §3's $10B floor.** No `move` call was made —
  §3-first discipline, so no effort went into a story a single number was always going to end.
- Priced-in, correlation: not reached.

**Outcome:** **REJECTED — §3 cap floor (~$6.19B), and FIRST-ORDER regardless of cap.**
⚠⚠ **AND THE $1.0B EQUINOR LEG IS A CLEAN RULE (iii) INSTANCE WITH THE REASON VOLUNTEERED BY THE
SOURCE:** Transocean described that agreement as **previously announced** — the 10-09 release concerned
**final approval and conversion into firm backlog**, not a new agreement. ⚠ **THE BIG NUMBER IS THE OLD
NEWS AND THE NEW NUMBER IS THE SMALL ONE. That is the most legible form of rule (iii) this log has
recorded: a single release carrying both, with the ratio ~16:1 in favour of the stale leg.** ⚠ **A
reader skimming for the largest figure would have taken the one that fails.**

---

### T-2026-10-09-04 — MTUS (Metallus) $995M DLA defence-steel ceiling — REJECTED
**Company A / the news:** Metallus reported to have received a **US Defense Logistics Agency** contract
with a **maximum ceiling of $995M** over five years for defence steel supply (fastmarkets, reported
**2026-10-08**).
**Company B / the candidate:** **NONE REACHED. NO QUERY SPENT.**

**Outcome:** **REJECTED — AN EXACT REPEAT OF `T-2026-10-01-05`, DISPOSED ON THE ALREADY-WRITTEN RULE.**
⚠⚠ **THE SAME TICKER, THE SAME PROGRAM AND THE SAME $995M FIGURE RETURNING EIGHT SESSIONS LATER — and
this is standing rule (iv) at its most literal: a recurring ticker dying the same death is telling me
about its industry's disclosure practice, not about a candidate maturing.** Three kills, all inherited
and all re-verified as still applying: **(a)** rule (v)'s **CEILING sub-shape** — a *maximum* multiple-
award ceiling is not a contract figure and is not revenue at anybody; **(b)** MTUS is **first-order**,
the named recipient; **(c)** §3 — the funnel again declined to establish a cap above $10B
(*"the available evidence does not establish a market capitalization above $10 billion"*), consistent
with the ~$0.6B figure recorded on 10-01. ⚠ **Reading the log cost one grep and saved a funnel query.
THAT is what the reject catalogue is for.**

---

### T-2026-10-09-05 — Voyager Technologies / Strategic Capabilities Office $22.4M — REJECTED
**Company A / the news:** Voyager awarded a **$22.4M** Other Transaction Agreement by the US
**Strategic Capabilities Office** to prototype next-generation satellite deployment systems
(cyprusshippingnews, carrying a **2026-10-09** date).
**Company B / the candidate:** **NONE REACHED. NO QUERY SPENT.**

**Outcome:** **REJECTED — AN EXACT REPEAT OF `T-2026-10-06-06`, same company, same program, same
$22.4M figure, three sessions later.**
⚠⚠ **AND IT IS A RULE (iii) INSTANCE IN A NEW COSTUME — A RE-REPORT CARRYING A FRESH DATE.** The item
appeared in this log on **10-06**; the source serving it today stamps it **10-09**. ⚠ **A recency filter
bounds when something was WRITTEN, never when it HAPPENED — and this run asked for the announcement
date in the prompt itself, which is the only reason the collision was visible.** Kills unchanged:
§3 (microcap, listing unverifiable), first-order recipient, and a **government counterparty** so there
is no Company A. ⚠ **Second instance this run of the funnel re-serving a disposed reject (see RTX).
THE DISPOSED-REJECT CATALOGUE IS SPLIT ACROSS `archive/research_log/2026-09.md` AND THIS FILE, AND A RUN
CHECKING WHETHER A NAME WAS ALREADY DISPOSED MUST READ BOTH.**

---

### T-2026-10-09-06 — White House "Genesis Mission" — 11 companies / $2.4B aggregate — REJECTED
**Company A / the news:** A **2026-10-08** White House announcement naming **11 participating
companies** against **$2.4B in total commitments**, reported secondhand.
**Company B / the candidate:** **NONE — AND THE TWO TESTS ARE JOINTLY UNSATISFIABLE, WHICH MAKES THIS A
FREE ONE-STEP SCREEN.**

**Outcome:** **REJECTED, TWO SETTLED OBJECTS AT ONCE AND NO QUERY SPENT.**
**(a) A GOVERNMENT ACTION IS NOT A COMPANY A** — it is the most convincing non-event this funnel
produces: sector-specific, carries a number, names an industry, moves the tape — **and it has ONE
party.** ⚠ **Scale makes it more convincing, not less.**
**(b) THE AGGREGATE-UNALLOCATED SHAPE, AND THE ARITHMETIC KILLS IT BEFORE ANY SUPPLIER SEARCH BEGINS:**
$2.4B spread across 11 companies is **~$218M each**, which **cannot clear part 2's 10% test against ANY
company above §3's $10B cap floor.** ⚠ **§3's floor and part 2's materiality test are JOINTLY
UNSATISFIABLE here, so the search is pointless before it starts — the same free screen that disposed
Blaize (10-06) and the US Army NGC2 awards (10-08).** ⚠ The funnel confirmed no amount is attributed to
any individual company.

---

### T-2026-10-09-07 — FTI (TechnipFMC) / Petrobras subsea flexibles — REJECTED
**Company A / the news:** TechnipFMC awarded a flexible-pipe contract by **Petrobras**, reported
**2026-10-09** (cyprusshippingnews, Simply Wall St).
**Company B / the candidate:** **NONE — FTI is the recipient and is first-order.**

**2. Dollar path:** **FAILS AT SOURCE AND THE SOURCE SAID SO.** TechnipFMC characterised the contract
only as **"significant"**, which it defines as **$75M–$250M**. ⚠⚠ **A RANGE IS NOT A DISCLOSED FIGURE,
AND THIS ONE SPANS MORE THAN 3x FROM END TO END.** The funnel volunteered the exclusion in those terms.
⚠ **This is a disclosure-practice sub-shape worth naming: a company substituting its own internal
materiality BAND for a number. It reads as quantified and is not.**

**Outcome:** **REJECTED — part 2 (no disclosed figure, only a self-defined band), and first-order
regardless.** ⚠ **The ready-and-unwritten prior here was the subsea-flexibles supply tier. NOT WRITTEN
DOWN. Petrobras is also a Brazilian state-controlled issuer, so the counterparty leg fails §3 besides.**

---

### T-2026-10-09-08 — §3 SCOPE SWEEP (eleven non-eligible items, disposed as one) — REJECTED
Disposed in one entry because each dies on §3 or on an already-written rule before any mechanism is
attempted. ⚠ **§3 IS APPLIED FIRST, SO NO EFFORT GOES INTO A STORY A SINGLE NUMBER WAS ALWAYS GOING TO
END.** ⚠ **Roughly half of this run's raw funnel output was non-US — `--recency day` returns a GLOBAL
tape, and that is why this sweep exists as a standing step rather than an exception.**

- **Elevra Lithium / LG Energy Solution** — 240,000 dry metric tonnes of spodumene over 3–4 years.
  ⚠ **A SECOND APPEARANCE: already swept on 10-08. VOLUME IS DISCLOSED AND DOLLARS ARE NOT — tonnage is
  not a dollar path (part 2), and both legs fail §3 (microcap; LG Energy Solution is Korea-listed).**
  ⚠ **Third instance this run of a disposed reject returning.**
- **Samsung Electro-Mechanics — ₩290B (~$215.8M)** MLCC supply for AI servers, **counterparty an
  UNNAMED "global company"** — §3 (Korea-listed) **and** standing rule (v)'s unnamed-counterparty shape.
  ⚠ **A precise figure attached to a blank is the most fillable-looking object this funnel produces.
  THE SOURCE LEFT THE BLANK.**
- **BAE Systems / US Marine Corps $230.1M**, 32 amphibious combat vehicles — §3, UK-listed; government
  counterparty; eleventh defence-award instance.
- **Shield AI / US Navy $150M** — private company, government counterparty, and the source flagged it
  as **a modification of an existing agreement** (rule iii).
- **Boost Run / Cohere $525.6M** five-year AI cloud-services agreement — both legs unverifiable as to
  listing and size; the funnel explicitly declined to verify the parties' corporate identities,
  US-listing status or whether the agreement was new rather than part of previously reported aggregate
  contract value. **NOT INHERITED AS A VERDICT EITHER WAY — it is UNRESOLVED, and unresolved is not a
  pass.**
- **Fujifilm** — Japan-listed; discussed semiconductor-material customers **generally** and named none.
- **LG Electronics USA / AIR Control Concepts** — data-centre chiller supply agreement with a ~$680M
  **2027 business TARGET**; LG is Korea-listed, AIR is private, and a company's own forward revenue
  target is not a disclosed transaction figure (rule viii's broad reading).
- **Quantisimo / WISeQey / SEALSQ** — a proposed merger with a **$15M minimum CASH CONDITION**, which is
  not a transaction value; more than two parties; §3 on size.
- **Cerebri AI / Cain Travel** — first-customer announcement, both legs private, no figure.
- **Arqit** — preliminary FY2026 revenue of **$1M**; §3 on every test.
- **KEC International** (₹1,030 crore orders) — India-listed; §3.

**Outcome:** **ALL ELEVEN REJECTED.** ⚠ **Nine of the eleven were excluded BY THE SOURCE ITSELF, with
the reason volunteered, which is work this run would otherwise have done query by query. THE STRUCTURAL
FRAMING RETURNS THE EXCLUSIONS WITH THEIR REASONS ATTACHED — third consecutive session that has paid.**

---

### 2026-10-08 (08:25 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,491.26** at
pre-flight). Window screened: **the completed 2026-10-07 session and overnight into 2026-10-08** — a
real window; 10-07 was a full session (official close 714.66). **Four Perplexity scans, all exit 0**
(three broad/structural, one second-order drill, plus one market-cap verification call). **Ten
candidates reached a thesis entry; ALL TEN WERE REJECTED.**

**The carry-forward's two complementary framings were used as queries one and two, as instructed.**
Query 1 ("two named parties, a disclosed dollar amount, an announcement date") returned **one
qualifying item and NINE self-excluded ones with the reason volunteered** — the highest exclusion
count on record, and work the run would otherwise have done itself. Query 2 ("who WON it and what did
they say it was worth to their own named segment") returned **an explicit, unprompted denial**:
*"the available evidence does not show any company that satisfies the full screen."* Query 3, aimed
at the second-order shape directly (an event that changed a **named second** public company's
disclosed economics), returned *"No qualifying event was identified."*

⚠⚠ **THAT IS THE EIGHTH CONSECUTIVE SESSION WITH AT LEAST ONE VOLUNTEERED ABSENCE, AND THE FIRST IN
WHICH ALL THREE BROAD SCANS RETURNED ONE.** 09-29 → 10-08 unbroken. ⚠ **A volunteered absence is
stronger than a silence, and a run that produces a Company B against three explicit denials has
supplied it from its own priors.** The priors were ready and specific again today — solid-rocket-motor
names for the X-Bow booster, the Sjögren's competitive set for argenx, the CDMO tier for Pfizer's
Sicily exit. **None was written down as a candidate.**

⚠⚠ **THE ONE GENUINELY NEW OBSERVATION, AND IT IS ABOUT QUERY 1's FAILURE MODE RATHER THAN ITS
SUCCESS: THE STRUCTURAL FRAMING RETURNED A FULL INVENTORY AND *EVERY SINGLE ITEM IN IT* FAILED §3 OR
PART 1 BEFORE REACHING A MECHANISM.** Nine of today's ten rejections are **universe** or
**no-second-party** kills; **exactly one** (SUPN) reached part 2, and it failed §3's cap floor at the
same time. ⚠ **The framing is working as designed — it reaches the funnel's real inventory — and the
inventory itself was, today, structurally ineligible from end to end. Those are two different facts
and only the first is about the query.**

⚠⚠ **THE PRICED-IN FILTER HAD NOTHING TO FIRE ON — ZERO `move` CALLS AT THIS SEAT, AND THIS IS THE
"FOURTH STATE" (an ABSENT check, not a skipped one).** Every candidate died at §3 or part 1, upstream
of the filter. ⚠ **No decorative `move` call was made, for the third recorded time: running one on a
name with no mechanism converts an honest absence into a fake exercise.** ⚠ **10-08 is NOT a
zero-`move` SESSION yet and must not be written as one — three seats remain. A session is only
countable once it is over.**

**Correlation check (§4):** **vacuous, and recorded as such rather than as passing.** Open satellite
positions: **zero**, so no candidate could collide with an existing driver. ⚠ **An empty driver list
cannot reject anything, which means the correlation filter has never once been exercised on this
account.**

---

### T-2026-10-08-01 — Asieris Pharmaceuticals / Theramex (CEVIRA licence) — REJECTED
**Company A / the news:** Asieris Pharmaceuticals and Theramex announced an exclusive licensing
agreement for CEVIRA (non-surgical cervical precancer treatment) covering Europe, Australia, New
Zealand and Turkey — **$15M upfront, $11M near-term regulatory milestones, total deal value stated as
exceeding $250M**, announced **2026-10-07** (PR Newswire). **The one item of the run that cleared
query 1's own structural bar.**
**Company B / the candidate:** **None exists.** Asieris is Shanghai STAR-listed (688176); Theramex is
privately held (PAI Partners / Carlyle). No third party is named.

**1. Mechanism:** not written — there is no US-listed leg to attach one to.
**2–4:** not written.

**Hard filters:**
- Universe (§3): **FAIL, and it is terminal.** Neither party is US-listed. §3 permits US-listed common
  stock and US-listed ETFs only. **There is nothing buyable in this transaction at any price.**
- Priced-in (§4): **not run** — no ticker to run it on.
- Correlation (§4): vacuous (zero open positions).

**Outcome: REJECTED on §3, before any thesis part was attempted.** ⚠ **The honest note is that the
dollar figure here is the best-disclosed of the day and it buys nothing — a disclosed amount is only
useful if one of the parties is in the universe. §3 is checked first for exactly this reason.**

---

### T-2026-10-08-02 — SUPN (Supernus Pharmaceuticals) — REJECTED
**Company A / the news:** Newron Pharmaceuticals reported **2026-10-08** that the **FDA clinical hold
remains in place** at US study centres for **ENIGMA-TRS 2**, its Phase 3 evenamide study in
treatment-resistant schizophrenia; Newron said it had received written FDA communication and would
respond after review. **No US patients had been dosed as of the announcement.**
**Company B / the candidate:** **Supernus Pharmaceuticals (NASDAQ: SUPN)**, which **Newron's own
release names as the holder of US marketing rights to evenamide.** ⚠ **This is the only candidate of
the run with a genuine second-order shape: a named second public company whose asset is directly
affected by an event at Company A.**

**1. Mechanism (attempted):**
> The FDA clinical hold on ENIGMA-TRS 2 causes Supernus's US evenamide rights to lose value because
> the US approval path is suspended.

**2. Dollar path:** ⚠ **CANNOT BE WRITTEN. Newron's release discloses no payment structure, no
milestone or royalty figures, and reports no evenamide revenue contribution for Supernus. The source
explicitly adds that this "should not be interpreted as evidence that the contractual amounts are
zero."** ⚠ **Part 2 requires a segment and a share of total revenue; evenamide is pre-approval and has
neither.** **PART 2 FAILS.**
**3. Timing window:** indeterminate — a hold lifts when the FDA says so.
**4. Invalidation:** writable in principle (*"FDA lifts the hold and Supernus discloses a dosing
restart"*), but with no part 2 there is nothing for it to invalidate.

**Hard filters:**
- Universe (§3): **FAIL. SUPN market cap ≈ $2.5B** (MarketBeat, 2026-10-07: $2.51B; a second
  MarketBeat item the same day: $2.49B — source: Perplexity, cited to MarketBeat). **Below §3's $10B
  floor by a factor of four.** ⚠ **Figure and source recorded so a later run need not re-derive it.**
- Priced-in (§4): **not run** — the candidate was already dead twice over.
- Correlation (§4): vacuous.

**Outcome: REJECTED on §3's cap floor AND on part 2, independently.** ⚠⚠ **AND A THIRD KILL THAT
MATTERS MORE THAN EITHER, BECAUSE IT WOULD APPLY EVEN TO AN ELIGIBLE NAME: THE MECHANISM POINTS THE
WRONG WAY. A clinical hold makes the licensee's asset worth LESS. This strategy can only buy — §3
forbids leverage, inverse products and anything not bought outright with settled cash, so a correct
bearish second-order read is UNTRADEABLE HERE.** ⚠ **The tempting move is to flip it into a
"competitor benefits" long. That is the shared-cause object: a competitor's economics did not change,
only its relative standing did, and no competitor was named in any source. NOT TAKEN.**
⚠ **New reject shape for the catalogue — EIGHTH FORM: THE MECHANISM IS SOUND AND POINTS DOWNWARD.**
Distinct from the seven known forms, all of which are disclosure or calendar failures.

---

### T-2026-10-08-03 — OII (Oceaneering International) — REJECTED
**Company A / the news:** US Navy five-year contract to Oceaneering's **Aerospace and Defense
Technologies** segment, **potential value up to $154M**. ⚠ **Announced 2026-10-02 — SIX DAYS OLD, and
the source said so when asked.**
**Company B / the candidate:** none identified; OII is the recipient.

**Hard filters:**
- Universe (§3): **FAIL. OII market cap ≈ $4.48B** (MarketWatch, updated 2026-10-07; StockAnalysis
  $4.46B the same day — source: Perplexity). **Below the $10B floor.**
- Priced-in (§4): not run.

**Outcome: REJECTED on §3, with TWO independent kills.** ⚠ **(i) OII is FIRST-ORDER in its own news —
§4 asks whose economics change *because of* someone else's event, and the award recipient is the
headline. (ii) The date is outside the window: a recency filter bounds when something was WRITTEN,
never when it HAPPENED, and this is the rule (iii) trap arriving again — defused by demanding the
announcement date in the prompt, which is now a standing rule rather than a Monday one.**
⚠ **Note also that the only segment-revenue comparison available was SECONDARY ANALYSIS, not the
company's own quantification — which is the disclosure failure part 2 exists to catch.**

---

### T-2026-10-08-04 — GVA (Granite Construction) — REJECTED
**Company A / the news:** Two project awards reported **2026-10-08** totalling **$489.8M** ($324.8M +
$165M).
**Company B / the candidate:** none. ⚠ **And the counterparties for both projects are NOT clearly
identified in the available material — so this item fails query 1's own two-named-parties bar as
well.**

**Hard filters:**
- Universe (§3): **FAIL. GVA market cap ≈ $5.37B** (CompaniesMarketCap, October 2026; $5.28B on
  10-06; MarketBeat $5.02B — sources disagree by ~7%, all well below the floor — source: Perplexity).
  **Below the $10B floor.**
- Priced-in (§4): not run.

**Outcome: REJECTED on §3.** Independently: **GVA is first-order**, and **the company did not quantify
the awards as revenue to a named segment** (part 2's most common killer in this log).

---

### T-2026-10-08-05 — X-Bow Systems / US Navy SRM booster — REJECTED
**Company A / the news:** US Navy award of **nearly $70M** to **X-Bow Systems** to develop a solid
rocket motor booster for a new weapon, reported **2026-10-08**.
**Company B / the candidate:** **none named.** ⚠ **The ready prior here was immediate and specific —
the solid-rocket-motor tier. IT IS A FACT ABOUT AN INDUSTRY, NOT ABOUT THIS TRANSACTION, AND IS NOT
RECORDED AS A CANDIDATE.**

**Hard filters:**
- Universe (§3): **FAIL on both legs. X-Bow Systems is privately held; the counterparty is the US
  Navy, which is not a company.** **There is no buyable leg on either side.**
- Priced-in (§4): not run.

**Outcome: REJECTED on §3, and it is the EIGHTH instance of the standing carry-forward rule: US
DEFENCE PROGRAM AWARDS CANNOT PRODUCE A §4 CANDIDATE.** ⚠ **The structural reason is unchanged — the
money flows from a government, so there is no Company A whose *economics* changed, and the supplier
tier below the winner is never named in the announcement.** ⚠ **The source also flagged that it could
not date the award beyond its publication date — rule (iii) again.**

---

### T-2026-10-08-06 — VAL (Valaris) / PETRONAS — REJECTED
**Company A / the news:** Valaris reported drillship and jackup work across three continents,
**approximately $220M** for a **batch** of contracts and extensions including PETRONAS.
**Company B / the candidate:** none; VAL is the recipient.

**Hard filters:**
- Universe (§3): **UNRESOLVED — RECORD AS UNDECIDED, NOT AS PASSING.** The market-cap query
  **explicitly declined** to supply a figure for VAL (*"No usable Valaris market-capitalization result
  was returned"*). ⚠ **No §3 verdict may be claimed on VAL in either direction, and a future run must
  not inherit one from this entry.**
- Priced-in (§4): not run.

**Outcome: REJECTED on part 2, which does not depend on the unresolved §3 check.** ⚠ **The $220M is an
AGGREGATE across a batch and is NOT ALLOCATED to the PETRONAS contract — so the figure exists but is
the WRONG QUANTITY, which is reject form five.** Independently: **VAL is first-order**, and PETRONAS
is state-owned and unbuyable.

---

### T-2026-10-08-07 — US Army NGC2 awards (nine recipients) — REJECTED
**Company A / the news:** US Army issued **just under $100M** in NGC2 application awards to **nine
companies**, reported **2026-10-08**.
**Company B / the candidate:** none reachable.

**Hard filters:**
- Universe (§3): not reached.
- Priced-in (§4): not run.

**Outcome: REJECTED on part 2.** ⚠ **The amount is an AGGREGATE with no per-recipient allocation, so
no single company's dollar path can be written — and $100M split nine ways averages ~$11M, which
cannot clear part 2's 10%-of-revenue test against ANY §3-eligible $10B+ company. The 10% test and the
$10B floor are JOINTLY UNSATISFIABLE at this deal size, which is a free one-step screen** (same shape
as the Blaize kill on 10-06, arriving from the deal-size side rather than the counterparty side).
⚠ **Ninth defence-award instance.**

---

### T-2026-10-08-08 — ARGX (argenx) — REJECTED
**Company A / the news:** argenx announced **2026-10-08** the **discontinuation of the Phase 3 UNITY
study** of efgartigimod in Sjögren's disease.
**Company B / the candidate:** **none named in any source.**

**1. Mechanism:** not written. ⚠ **The only available construction is "a competitor in Sjögren's now
faces one fewer entrant" — which is the SHARED-CAUSE object, not a mechanism: no competitor's revenue
or cost line changed, only its relative standing, and no competitor was named.**
**2–4:** not written.

**Hard filters:**
- Universe (§3): **not reached** (ARGX itself is comfortably above the floor, but it is first-order
  and no figure was sought — recorded as NOT CHECKED rather than as passing).
- Priced-in (§4): not run.

**Outcome: REJECTED on part 1.** ⚠ **A trial discontinuation discloses no dollar figure and names no
second party. The ready prior — the competitive set — was specific and was not written down.**

---

### T-2026-10-08-09 — Pfizer Sicily plant action — REJECTED
**Company A / the news:** Pfizer to cut **~330 jobs** in Italy (Sicily), reported **2026-10-07** per
unions.
**Company B / the candidate:** **none. No volume shift to a named rival or CDMO is disclosed.**

**Hard filters:** not reached.

**Outcome: REJECTED on part 1 — THERE IS NO COUNTERPARTY AT ALL** (reject form six, same shape as
Bayer's Ohio plant and BDX's $3B). ⚠ **A headcount figure is not a dollar path: 330 jobs does not map
to a segment revenue line, and nothing says where the volume goes — or that it goes anywhere.**
⚠ **The CDMO prior was ready and is not recorded as a candidate.**

---

### T-2026-10-08-10 — §3 SCOPE SWEEP (twelve non-eligible items, disposed as one) — REJECTED
Recorded as a single entry rather than twelve, because the kill is identical and mechanical and
twelve near-identical blocks would pad the log without adding information.

**Items, each with its own disclosed detail, all failing §3's US-listed requirement:**
Alstom / Royal Commission for Riyadh City (metro trains — a qualifying two-party disclosed-value
contract, **excluded purely on US scope, and the source excluded it before I did**) · Bayer —
FDA accepts Kerendia sNDA for CKD without diabetes (German-listed) · OPmobility — revised 2026
operating-margin guidance €430–450M, FCF >€220M (French-listed) · Medisca / EUROAPI API partnership
(EUROAPI Paris-listed, Medisca private) · Elevra / LG Energy Solution spodumene supply (Australian +
Korean) · ASELSAN $125M (Turkish-listed, **and the counterparty is an unnamed "international
end-user"** — two independent kills) · Machines With Vision / Network Rail (**"multi-million," no
figure disclosed** — part 2 as well) · Cambridge Heartwear / NHS £18.4M tender (UK) · Aemulus RM15M
contract (Malaysian) · Tata Consultancy Services Q2 FY27 results (Indian) · Interarch Building
Solutions ₹59 crore order (Indian) · Om Power Transmission ₹78.84 crore LoI (Indian).

**Outcome: ALL REJECTED on §3.** ⚠ **Worth one honest line: `--recency day` returns a global tape, and
roughly half of today's raw funnel output was non-US. That is not a defect in the query — it is why
§3 is applied before a mechanism is attempted, and today it disposed of twelve items for zero
analytical effort.**

---

### 2026-10-07 (08:24 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,643.92**
at pre-flight 08:24). Window screened: **the completed 2026-10-06 session and overnight into
2026-10-07** — a real window; 10-06 was a full trading session (official close 716.29). **Five
Perplexity scans, all exit 0** (three broad/structural, two second-order drills). **Seven candidates
reached a thesis entry; ALL SEVEN WERE REJECTED.**

⚠⚠ **THE CARRY-FORWARD'S HEADLINE INSTRUCTION WAS APPLIED AS WRITTEN AND IT WORKED AGAIN: ASK FOR
THE *STRUCTURE* §4 REQUIRES, NOT FOR *IMPORTANCE*.** 10-06 discovered that a query about
"significant events with knock-on effects" returns the macro complex, while a query naming **two
named parties plus a disclosed dollar amount plus a date** returns the funnel's actual inventory.
**That framing was used as the FIRST query this run rather than the second, and it returned four
dated two-party transactions with dollar figures immediately** — Chevron/Hess Midstream $200M,
Google/Constellation $4.3B, POSCO Future M/Samsung SDI KRW 6T, HD Construction Machinery/ERock
$290M — plus **four self-excluded items with the reason volunteered** (Clarivate/Altaris flagged as
a completion of a 2026-07-06 announcement, Airtificial's counterparty unnamed, Alvotech/LOTTE
carrying no dollar amount, RTX's SM-6 flagged as date-unverifiable). ⚠ **The structural framing does
not just return more; it returns the exclusions with their reasons attached, which is work the run
would otherwise do itself.**
⚠⚠ **AND IT DOES NOT FIND EVERYTHING — THE SINGLE MOST §4-SHAPED ITEM OF THE RUN CAME FROM THE THIRD
SCAN, NOT THE FIRST.** The Boeing/Lockheed PAC-3 MSE award ($14.7B, two named US-listed parties, a
disclosed figure, announced 10-05) appeared **only** when the query asked specifically for a company
that had **WON** a contract and **quantified the revenue to its own segment**. ⚠ **TWO
COMPLEMENTARY FRAMINGS, NOT ONE REPLACEMENT: "two parties and a dollar amount" finds transactions;
"who won it and what did they say it was worth to their own segment" finds the part-2 evidence, and
it surfaced a transaction the first framing missed.** **Use both.**

⚠⚠ **FOUR VOLUNTEERED ABSENCES IN ONE RUN — THE MOST IN ANY SESSION ON RECORD, AND THE SEVENTH
CONSECUTIVE SESSION WITH AT LEAST ONE** (09-29, 09-30, 10-01, 10-02, 10-05, 10-06, 10-07). Every
second-order drill answered §4's question in the negative in its own words:
- **Constellation/Google:** *"No publicly traded U.S. company has been explicitly named by
  Constellation Energy, Google, or an SEC filing as a contractor, equipment supplier, turbine or
  generator vendor, or engineering firm for the more-than-$4.3 billion program."*
- **Chevron/Hess Midstream:** *"does not explicitly name any additional publicly traded U.S.
  company as a counterparty, supplier, customer, operator, or beneficiary."*
- **POSCO Future M/Samsung SDI:** *"no qualifying third U.S.-listed company is named."*
- **Boeing/Lockheed PAC-3 MSE:** *"No supplier, subcontractor, component supplier or partner below
  Boeing is named in the available announcements for this specific award."*
⚠ **REPORTED WITH ITS COUNT AND NOT PROMOTED — the three-consecutive-reviews rule governs
promotion, and this item is a standing carry-forward entry rather than a new finding.**
⚠⚠ **THE PRIORS WERE READY AND SPECIFIC FOR ALL FOUR AND NONE WAS WRITTEN DOWN AS A CANDIDATE:**
BWXT/Curtiss-Wright/Fluor for nuclear uprates · Williams/ONEOK/Targa for Bakken midstream ·
Albemarle/Livent for cathode inputs · the whole seeker-optics tier for PAC-3. ⚠ **Each is a fact
about an INDUSTRY. The source named none of them, and three of the four said so unprompted.**

⚠⚠ **ZERO `move` CALLS WERE MADE IN THIS SEAT. THAT IS THE *ABSENT* STATE — THE FOURTH — NOT A
SKIPPED CHECK AND NOT A PASS.** Every candidate died on §4 structure, part 1, part 3 or §3 **before
an eligible ticker carrying a mechanism was reached**, so the priced-in filter had nothing to fire
on. ⚠ **A decorative `move` call on a name with no mechanism converts an honest absence into a fake
exercise, and was declined for that reason again.**
⚠⚠ **THE COUNT, STATED CAREFULLY PER CATCH (11): FOUR COMPLETE SESSIONS ARE CONFIRMED ZERO-`move`
ACROSS ALL THEIR SEATS — 09-29, 10-02, 10-05 AND 10-06. 10-07 IS NOT A FIFTH AND CANNOT BE WRITTEN
AS ONE: THIS IS SEAT 1 OF 4 AND THREE SEATS REMAIN.** ⚠ **A session is not zero-`move` until the
session is over.**

⚠ **ZERO `quote` CALLS. No candidate reached execution pricing and there is no satellite ticker to
quote.**

---

### T-2026-10-07-01 — Constellation Energy (CEG) / Google — no Company B — REJECTED
**Company A / the news:** **Google** and **Constellation Energy (NASDAQ: CEG)** announced power
agreements on **2026-10-06** covering approximately **3,590 MW** — **890 MW** of new nuclear
capacity from **uprates at 11 existing Constellation reactors** in Illinois, Pennsylvania and New
Jersey on a **20-year** term, plus **2,700 MW** of existing-fleet output on a **15-year** term.
Constellation disclosed **more than $4.3 billion** of new investment and **~7,200 construction
jobs**. First upgraded capacity expected **2028**. (Perplexity, two scans; Constellation release.)
**Company B / the candidate:** **NONE REACHED.** The intended search was for the engineering firm,
turbine/generator vendor or equipment supplier that captures the $4.3B of uprate capex.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** There is no named recipient of the $4.3B.
**2. Dollar path:** not reached.
**3. Timing window:** **INDEPENDENTLY FATAL EVEN IF A NAME EXISTED.** First upgraded capacity is
expected in **2028** and Constellation disclosed **no calendar-quarter breakdown** of the spend —
confirmed verbatim: *"the sources... do not provide a calendar-quarter breakdown for spending the
$4.3 billion."* Against §4's **two-quarter ceiling** this is ~8 quarters out at the earliest
observable point. → deadline n/a
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **NOT REACHED — zero `move` calls.** No eligible ticker with a mechanism existed.
- Correlation (§4): n/a — no candidate, and zero open satellite positions.
- Universe (§3): not reached.

**Outcome:** **REJECTED on part 1, with part 3 as an independent kill.** This is **rule (vi)'s
standing shape in its purest form** — long-dated energy capacity, the calibration point being
Venture Global/ConocoPhillips (20-year SPA, first delivery 2030). ⚠⚠ **IT IS ALSO THE LARGEST
DOLLAR FIGURE THIS FUNNEL HAS PRODUCED SINCE BDX's $19B, AND SCALE IS THE THING THAT MAKES THIS
SHAPE CONVINCING RATHER THAN THE THING THAT MAKES IT TRADEABLE: $4.3B, a named counterparty with a
trillion-dollar balance sheet, 3,590 MW, 11 named reactors, 7,200 jobs, three named states — EVERY
DETAIL EXCEPT THE ONE §4 NEEDS.** ⚠ **A MAP PIN IS NOT A LEAD, and this is the sixth instance of
the capex-blank form (Bayer's Ohio plant, BDX's $3B/Nebraska, now CEG's 11 reactors).** ⚠ **CEG
itself is the NAMED party and therefore first-order, outside §4 at any price.**

---

### T-2026-10-07-02 — Boeing (BA) / Lockheed Martin (LMT) PAC-3 MSE $14.7B — REJECTED
**Company A / the news:** **Boeing** announced on **2026-10-05** an **undefinitized contract
action** from **Lockheed Martin**, valued at approximately **$14.7 billion**, covering **seven
years** of production and delivery of **PAC-3 MSE seekers**, with the stated intent to **triple**
Boeing's seeker output. (Perplexity, two scans, incl. a dedicated disclosure-history drill.)
**Company B / the candidate:** **NONE REACHED.** Boeing is the **named recipient** and therefore
first-order; the search was for the optics/sensor/component tier below Boeing.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** *"No supplier, subcontractor, component
supplier or partner below Boeing is named in the available announcements for this specific award."*
**2. Dollar path:** not reached — **and the headline figure is not a revenue figure.** ⚠⚠ **AN
UNDEFINITIZED CONTRACT ACTION HAS NO FINALISED PRICING BY DEFINITION** — the source states final
terms *"had not yet been completed."* Even for Boeing, $14.7B over seven years against ~$80B of
annual revenue is **~2.6%/yr spread across the horizon**; part 2 would fail at the first-order name.
**3. Timing window:** **seven years of production**, no first-delivery date disclosed → beyond §4's
two-quarter ceiling. → deadline n/a
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **NOT REACHED — zero `move` calls.** No second-order ticker existed to screen.
- Correlation (§4): n/a — no candidate, and zero open satellite positions.
- Universe (§3): not reached. (Both named parties clear §3 comfortably; neither is a §4 candidate.)

**Outcome:** **REJECTED on part 1 (volunteered absence), with part 3 and rule (iii) each killing it
independently.** Three things make this entry worth more than the usual defence rejection:

⚠⚠ **(A) A NEW RULE (iii) COSTUME, AND A GOOD ONE: AN UNDEFINITIZED CONTRACT ACTION *PRICING* A
PREVIOUSLY ANNOUNCED FRAMEWORK.** Boeing and the DoD had **already announced a seven-year framework
agreement in April 2026 to expand PAC-3 MSE seeker output, including the intention to triple
production.** The 10-05 award **formalises and prices that framework**; the production objective is
**six months old**. ⚠ **This is distinct from the existing costumes — it is not a reaffirmation, not
a re-covered deal and not a restated 8-K. The DOLLAR FIGURE IS GENUINELY NEW while the ECONOMIC
EVENT IS NOT, which is precisely the combination that reads as fresh news.** ⚠ **Caught only
because the drill query asked for the disclosure history explicitly. THE COST OF ASKING WAS ONE
CLAUSE.**

⚠⚠ **(B) THE SIXTH DEFENCE-PROGRAM INSTANCE, AND THE FIRST WHERE THE NAMED RECIPIENT IS A BUYABLE
SUB-PRIME RATHER THAN THE PRIME.** AMRAAM (09-29, RTX) · F/A-XX (09-30, Boeing) · SM-6 (10-02, RTX)
· S&K/Powerus/Voyager (10-06) were all prime-level. **Here the tier below the prime IS named, IS
US-listed and IS above $10B — and the pattern held anyway, because the question simply moves one
level down and the same commercial confidentiality applies.** ⚠⚠ **THAT STRENGTHENS THE RULE RATHER
THAN WEAKENING IT: the mechanism is DISCLOSURE PRACTICE, not the primes' size. Naming the
sub-prime does not create a second-order candidate; it creates a new first-order name.**

⚠ **(C) Boeing is NOT a §4 candidate at any price.** It is the headline name. The temptation here is
unusually strong because the award is large, dated, quantified and genuinely new as a number — and
**§4 is about whose economics change that the market is NOT looking at.** A $14.7B award announced
by the recipient itself is the definition of what the market is looking at.

---

### T-2026-10-07-03 — Chevron (CVX) / Hess Midstream (HESM) $200M — no Company B — REJECTED
**Company A / the news:** **Chevron** agreed on **2026-10-06** to transfer its **Hess Midstream
ownership interests, its general-partner position and its DJ Basin crude-oil midstream assets** to
**Hess Midstream LP** for **$200 million cash** plus a revised Bakken commercial framework that
extends the existing contracts. (Perplexity, two scans; Chevron newsroom release.)
**Company B / the candidate:** **NONE REACHED.** *"does not explicitly name any additional publicly
traded U.S. company as a counterparty, supplier, customer, operator, or beneficiary."*

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** No third party is named.
**2. Dollar path:** not reached. ⚠ **And note the direction — rule (viii): the $200M is paid BY the
buyable midstream leg TO Chevron.** It is **capital paid OUT by HESM**, not segment revenue at any
Company B. The revised Bakken agreements carry **no disclosed term and no disclosed dollar value**.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **NOT REACHED — zero `move` calls.**
- Correlation (§4): n/a — no candidate, and zero open satellite positions.
- Universe (§3): not reached. ⚠ **Had a candidate existed, HESM would have raised an unsettled §3
  question of its own — it is a limited partnership, not common stock. NOT SCREENED, because it is
  the NAMED counterparty and therefore first-order regardless.** (Companion to the standing
  Shopify/foreign-issuer question: a §3 edge case must go to the human **with a live candidate**,
  never as an abstraction.)

**Outcome:** **REJECTED on part 1.** ⚠ **Both named parties are first-order.** ⚠⚠ **THE
INTERESTING FEATURE IS WHAT THE DEAL *IS*: a restructuring of the commercial relationship BETWEEN
THE TWO NAMED PARTIES. The economics that change are entirely internal to the transaction — there
is no outside leg for a second-order effect to travel along. That is a structurally stronger reason
for "no Company B" than an undisclosed supply base, and it is the first instance of that shape in
this log.**

---

### T-2026-10-07-04 — POSCO Future M / Samsung SDI KRW 6 trillion — REJECTED (§3)
**Company A / the news:** **POSCO Future M** signed a **KRW 6 trillion** long-term agreement on
**2026-10-06** to supply **LFP cathode materials** to **Samsung SDI**, running **2027 through
2032**. ⚠ **The source volunteered that this is an AMENDMENT to the parties' 2023 supply agreement,
adding LFP alongside existing NCA materials — rule (iii) on its face.**
**Company B / the candidate:** **NONE REACHED.** *"no qualifying third U.S.-listed company is
named."*

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.**
**2. Dollar path:** not reached. **3. Timing window:** supply begins **2027** — outside the
two-quarter ceiling even for the named parties. **4. Invalidation:** not reached.

**Hard filters:**
- Universe (§3): **FAIL AT THE FIRST STEP, AND IT IS A FREE ONE.** **Both named parties are
  Korea-listed.** §3 permits US-listed common stock and US-listed ETFs only. **No US-listed
  company is named anywhere in the transaction.**
- Priced-in (§4): **NOT REACHED.** - Correlation (§4): n/a.

**Outcome:** **REJECTED on §3, with rule (iii) and part 3 both available as independent kills.**
⚠ **§3-FIRST SAVED THE WHOLE EFFORT: the pull toward Albemarle / Livent / Piedmont as "US-listed
lithium and cathode-input names with exposure" was immediate and is exactly rule (v) — a
market-structure fact about the LFP supply chain is not a supply relationship in THIS agreement.**
⚠ **The amendment disclosure is the second rule (iii) instance in one run (see T-2026-10-07-02),
and both were volunteered by the source rather than extracted.**

---

### T-2026-10-07-05 — Four disposed two-party items (Clarivate/Altaris · HD Construction/ERock · Emera/Canadian Utilities · Alvotech/LOTTE) — REJECTED (no query spent)
**Grouped deliberately.** All four arrived in the structural scan, each died on a **single settled
test**, and **not one funnel query was spent on any of them.**

| Item | Disclosed figure | Killing test |
|---|---|---|
| **Clarivate / Altaris** — completion of the Life Sciences & Healthcare divestiture, 2026-10-06 | **$600M** | **Rule (iii).** ⚠ **The source volunteered it: the transaction was announced 2026-07-06 and 10-06 is the COMPLETION.** A three-month-old deal reaching closing is not news to either company's disclosure. **Clarivate is also ~$2B market cap → §3 independently.** |
| **HD Construction Machinery / ERock** — gas power-engine long blocks, 2026-10-07 | **~KRW 390B (~$290M)**, deliveries 2027–2028 | **§3.** HD Construction Machinery is **Korea-listed**; **ERock is a private US power-infrastructure provider**. No eligible leg. **Part 3 also fails** — deliveries begin 2027. |
| **Emera / Canadian Utilities** — merger creating a ~$50B company, 2026-10-06 | **~$50B** | **§3 + merger arbitrage.** Both are **Canadian issuers**, and §4 does not contain merger arb: **a target whose price is contractually pinned has no economics left to change.** ⚠ **Fourth merger offered by this funnel in three sessions** (onsemi/Synaptics, Schneider/PTC, CHRW/RXO, now this). |
| **Alvotech / LOTTE Biologics** — US-based manufacturing agreement, 2026-10-06 | **none disclosed** | **Part 2, at step zero.** ⚠ **The source volunteered the absence of a figure.** Alvotech is **Iceland-domiciled**; LOTTE Biologics is **Korea-listed** → §3 as well. |

**Outcome:** **ALL FOUR REJECTED.** ⚠⚠ **THE POINT OF THE GROUPING IS THE COST: four items, four
settled tests, ZERO funnel queries, and the structural scan supplied three of the four exclusions
with its own reasoning attached. THAT IS THE 10-06 FRAMING FINDING PAYING FOR ITSELF IN QUERY
BUDGET, not merely in candidate count.** ⚠ **A fifth item, Airtificial's $6.4M contract with an
unnamed US Tier-1 supplier, was excluded by the source itself for having no named counterparty and
is recorded here without a row — it is rule (v)'s unnamed-supply-base object at a §3-ineligible
scale.**

---

### T-2026-10-07-06 — Fortuna Mining (FSM) · Avio USA · Lamb Weston (LW) — REJECTED
**Grouped: three capacity/guidance items from the second broad scan, none reaching a mechanism.**

- **Fortuna Mining (NYSE: FSM)** — board approved a **30% expansion of the Séguéla processing
  plant**, **$109M** budget, throughput to **2.3Mt/yr**, **>200,000 oz/yr from 2H 2028**
  (announced 2026-10-07). **REJECTED on §3 and part 3 jointly:** FSM is **~$2B market cap**, far
  below §3's $10B floor, **and** the production target lands in **2H 2028 — ~7 quarters out.**
  ⚠ **Note the source's own caution, which is a clean rule (iii) non-establishment: it could NOT
  find Fortuna's prior throughput or prior production figure, so "30% expansion" is not verifiable
  against the company's own baseline from this source.** ⚠ **Same shape as 09-29's AAR failure —
  not establishable in EITHER direction.**
- **Avio USA** — new **~900,000 sq ft solid rocket motor facility** in Virginia, capacity for
  "thousands of motors annually" (2026-10-06). **REJECTED on §3:** Avio USA is **not US-listed**
  (subsidiary of Italy-listed Avio S.p.A.). ⚠⚠ **AND THIS IS THE CARRY-FORWARD'S NAMED PRIOR
  ARRIVING IN PERSON: "solid rocket motors for SM-6" is recorded as one of the four always-ready
  priors. The prior was ready within a second — and the facility names NO equipment supplier,
  contractor or customer. A GROUNDBREAKING IS A MAP PIN.**
- **Lamb Weston (NYSE: LW)** — FY2027 adjusted EPS guidance **$3.05–$3.35**, adjusted EBITDA
  **$1.125–$1.215B**, plus a production stoppage at its **Broekhuizenvorst** facility.
  **REJECTED on part 1:** this is LW's **own earnings print — first-order**, and LW is **~$8B market
  cap**, below §3's floor. ⚠ **The second-order pull here is the competitor read-across on the plant
  stoppage (a rival capturing displaced potato volume) and it is the SHARED-CAUSE object with the
  WRONG SIGN — a competitor's capacity loss improves nobody's economics in any disclosed, dateable
  way.** ⚠ **The source also could not establish LW's own prior guidance figure or whether the
  stoppage was newly disclosed — rule (iii) non-establishment again, the third in one run.**

**Outcome:** **ALL THREE REJECTED, no query spent beyond the broad scan.**

---

### T-2026-10-07-07 — BWX Technologies (BWXT) $189M naval reactor fuel — REJECTED
**Company A / the news:** **BWX Technologies** announced an approximately **$189 million**
naval-reactor-fuel contract on **2026-10-07**. ⚠ **The source stated it could NOT identify a named
customer, a reporting segment, or revenue-recognition timing.**
**Company B / the candidate:** **NONE — and there is no Company A either.**

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** ⚠⚠ **THE NAMED PARTY IS BWXT AND THE
COUNTERPARTY IS A GOVERNMENT BODY THAT THE SOURCE DID NOT EVEN NAME** — almost certainly Naval
Reactors / DOE. **A GOVERNMENT ACTION IS NOT A COMPANY A**: one party, a number, an industry, no
named recipient on the other side of the trade.
**2. Dollar path:** **CANNOT BE WRITTEN.** No segment identified, no revenue-recognition timing.
$189M against BWXT's revenue is **low single-digit percent at best**, and BWXT is the first-order
name regardless. **3./4.** not reached.

**Hard filters:**
- Priced-in (§4): **NOT REACHED — zero `move` calls.**
- Correlation (§4): n/a. - Universe (§3): BWXT clears the $10B floor; **irrelevant, it is
  first-order.**

**Outcome:** **REJECTED — no Company A, and the defence-award pattern on top.** ⚠ **SEVENTH
defence-program item in nine sessions and the smallest; one funnel query was NOT spent, per the
standing rule to write the answer down and stop.** ⚠⚠ **NOTE THE TWO-SIDED COST OF THAT RULE
HONESTLY: by declining the query I also decline the chance that THIS award is the exception. The
rule is kept because five prior instances all died the same death — but "I did not look" and
"there was nothing there" are not the same sentence, and this is the former.**

---

### 2026-10-06 (08:22 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,842.87**
at pre-flight 08:22). Window screened: **the completed 2026-10-05 session and overnight into
2026-10-06** — ⚠ **a REAL window, unlike yesterday's. 10-05 was a full trading session (official
close 712.41), so `--recency day` bounds an interval that actually contains events.** **Four
Perplexity scans, all exit 0** (two broad, two second-order funnel). **Eight candidates reached a
thesis entry; ALL EIGHT WERE REJECTED.**

⚠⚠ **THE MONDAY LESSON WAS APPLIED, NOT RE-DERIVED, AND IT PAID IMMEDIATELY.** Yesterday's
carry-forward said: on any Monday or post-holiday run, **ask for the announcement date explicitly**.
Both broad scans this run demanded the announcement date in the prompt itself, and the first one
returned **the September payrolls report with "announced October 2, 2026, not October 5" volunteered
in its own first clause** — the exact rule (iii) trap, defused by the query's framing rather than by a
follow-up. ⚠ **Today was a Tuesday and the instruction was written for Mondays; it was applied anyway
because the cost is one sentence. KEEP ASKING FOR THE DATE ON EVERY RUN.**

⚠⚠ **THE FIRST BROAD SCAN WAS NEARLY EMPTY AND THE SECOND WAS RICH — THE DIFFERENCE WAS THE QUESTION,
NOT THE DAY.** Scan 1 ("most significant news events… with knock-on effects") returned **four
macroeconomic non-events** and said so itself: *"the most clearly documented events were
macroeconomic… Evidence for additional major US corporate announcements with material knock-on
effects is limited."* Scan 2, asked instead for **announcements involving TWO NAMED PARTIES and a
disclosed dollar amount**, returned **seven dated transactions including two multi-billion-dollar
acquisitions that scan 1 never mentioned.** ⚠⚠ **THAT IS A FINDING ABOUT THE FUNNEL, NOT ABOUT THE
TAPE: a query asking for "significant events with knock-on effects" invites the source to editorialise
about significance, and it answered with the macro complex — the one object §4 can never use. A query
naming the STRUCTURE §4 requires (two parties, a dollar figure, a date) returned the structure.**
⚠ **ASK FOR THE SHAPE, NOT FOR THE IMPORTANCE. Scan 1's framing would have produced a no-trade day
with nothing in the log; scan 2's produced eight auditable rejections.**

⚠⚠ **TWO MORE VOLUNTEERED ABSENCES, AND THE COUNT IS NOW SIX CONSECUTIVE SESSIONS (09-29, 09-30,
10-01, 10-02, 10-05, 10-06).** Both second-order queries were asked whether any third public company
had direct contractual exposure, and both answered in the negative **in their own words**: the M&A
query returned *"no third publicly traded U.S. company with direct contractual exposure is
identified"* for **both** deals, adding unprompted that *"companies that compete with, sell to, or
operate in the same industrial-software market do not meet the requested standard"*; the BDX query
returned *"no engineering firm, construction contractor, or equipment supplier has been named."*
⚠ **A CONTINUATION of the standing carry-forward item, reported with its count and NOT promoted —
the three-consecutive-reviews rule governs promotion.** ⚠⚠ **Note what the M&A source did: it stated
the §4 exclusion I would have had to apply myself, before I applied it. A run that then produces a
Company B here has supplied it from its own priors against an explicit denial.**

⚠⚠ **ZERO `move` CALLS WERE MADE IN THIS SEAT. THAT IS THE *ABSENT* STATE — THE FOURTH — NOT A
SKIPPED CHECK AND NOT A PASS.** Every candidate died on §4 structure, part 1, part 2, part 3 or §3
**before an eligible ticker with a mechanism was reached**, so the priced-in filter had nothing to
fire on. ⚠ **A decorative `move` call on a name with no mechanism converts an honest absence into a
fake exercise, and was declined for that reason again.**
⚠⚠ **AND THE COUNT MUST BE STATED CAREFULLY — CATCH (11)'s SHAPE: 09-29, 10-02 AND 10-05 ARE THE
THREE SESSIONS CONFIRMED ACROSS *ALL* THEIR SEATS. 10-06 IS NOT A FOURTH YET — ONLY ITS PRE-MARKET
SEAT HAS RUN, AND THREE SEATS OF THIS SESSION REMAIN.** ⚠ **A session is not zero-`move` until the
session is over. Do not write "four sessions" from inside the fourth one.**

⚠ **ZERO `quote` CALLS. No candidate reached execution pricing and there is no satellite ticker to
quote.**

---

### T-2026-10-06-01 — PTC Inc. / Schneider Electric — no Company B — REJECTED
**Company A / the news:** Schneider Electric agreed to acquire **PTC Inc. (NASDAQ: PTC)** in an
all-cash deal at **$205/share, ~$22.6B equity value**, announced **2026-10-05**. Closing expected
**Q3 2027**, subject to shareholder and regulatory approval. (Perplexity, two scans, announcement
date asked for and given.)
**Company B / the candidate:** **NONE REACHED.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN.** PTC is the **target** and Schneider is the
**acquirer** — both first-order. The funnel was asked directly for a third public company with
disclosed contractual exposure and answered **"no third publicly traded U.S. company with direct
contractual exposure is identified in the announcement materials reviewed."**
**2. Dollar path:** n/a — no Company B.
**3. Timing window:** ⚠ **FAILS INDEPENDENTLY.** Expected close **Q3 2027** is ~4 quarters out
against §4's **two-quarter** ceiling. Part 3 kills any merger-contingent thesis in one step.
**4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — absent, not passing. Zero `move` calls.
- Correlation (§4): no open satellite positions; nothing to correlate against.
- Universe (§3): **the acquirer is §3-INELIGIBLE** — Schneider Electric is a **French-listed** issuer
  (Euronext Paris); its US presence is an **OTC ADR**, which §3 excludes by name. PTC itself is
  US-listed and above the cap, but it is the target.

**Outcome:** REJECTED on **part 1** (no Company B; volunteered absence), with **part 3** and **§3**
failing independently. ⚠⚠ **THIS IS THE ONSEMI/SYNAPTICS SHAPE ARRIVING ONE SESSION LATER WITH NEW
NAMES, AND THE SAME ANSWER APPLIES VERBATIM: buying a target at a fixed cash price is MERGER
ARBITRAGE, AND §4 DOES NOT CONTAIN A CLAUSE FOR IT.** §4 asks whose *economics* change; a target whose
price is contractually pinned at $205 has no economics left to change. ⚠ **The industrial-software
competitor read-across (Autodesk, Dassault, Ansys/Synopsys) is the "shared cause is not a mechanism"
object and the source pre-emptively excluded it. NO GUESS WAS MADE.**

---

### T-2026-10-06-02 — RXO Inc. / C.H. Robinson — no Company B — REJECTED
**Company A / the news:** **C.H. Robinson (CHRW)** agreed to acquire **RXO Inc. (NYSE: RXO)** in a
cash-and-stock deal — **$17.25 cash + 0.0856 CHRW shares per RXO share, ~$30.25/share, ~$5.8B** —
announced **2026-10-05**. Expected close **H1 2027**. Separate reporting cited **~$300M of estimated
annual run-rate cost synergies.**
**Company B / the candidate:** **NONE REACHED.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN.** Acquirer and target are both first-order.
The funnel volunteered **"no named public U.S. carrier, technology provider, reseller, outsourcing
provider, or divested business whose own reported revenue or costs would change directly as a
contractual consequence of the merger."**
**2. Dollar path:** ⚠ **THE ONLY DISCLOSED FIGURE IS THE WRONG QUANTITY — RULE (viii).** The **$300M
run-rate synergy** is an **acquirer's own estimate of its own future cost base**, not segment revenue
at any Company B. It is the JBL/Morgan-Stanley family: a precise, quotable, allocated number that is
not revenue at a buyable second leg.
**3. Timing window:** ⚠ **FAILS INDEPENDENTLY** — close **H1 2027**, beyond two quarters.
**4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — absent, not passing.
- Correlation (§4): no open satellite positions.
- Universe (§3): CHRW and RXO are both US-listed; CHRW clears the cap. Not reached — no Company B.

**Outcome:** REJECTED on **part 1** (volunteered absence), with **part 2** (rule (viii), wrong
quantity) and **part 3** (H1 2027) failing independently. ⚠ **Freight-brokerage consolidation invites
a share-shift story about Landstar, XPO and GXO. That story is a COMPETITOR READ-ACROSS the reader
supplies, and the source denied contractual exposure explicitly. NO TICKER WAS SCREENED.**

---

### T-2026-10-06-03 — Becton Dickinson (BDX) $19B US investment / Section 232 tariff relief — no Company B — REJECTED
**Company A / the news:** **BDX** announced on **2026-10-06** an agreement with the US government to
invest **$19B in the United States over several years**, of which **$3B** is directed to manufacturing
expansion at strategic US sites, in exchange for **relief from future Section 232 tariffs** on covered
BD products and inputs, **conditioned on BD meeting agreed milestones**. Named locations: **Nebraska
>$1B**; **Columbus, Nebraska $110M** for prefillable-syringe capacity (plus an earlier $35M).
**Company B / the candidate:** **NONE NAMED — one targeted query spent, explicit absence returned.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN.** A $3B domestic build-out must be
engineered, built and equipped by somebody, but the funnel answered **"no engineering firm,
construction contractor, or equipment supplier has been named… the reports do not name any publicly
traded U.S. engineering company, construction contractor, or equipment supplier as having been
selected, awarded work, or committed to supply BD."** ⚠⚠ **RULE (v), AND IN ITS MOST FILLABLE
COSTUME YET: AN EXACT FIGURE ($3B), A NAMED STATE (Nebraska), A NAMED TOWN (Columbus), A NAMED PRODUCT
LINE (prefillable syringes) — AND NO SECOND PARTY. The blank has a dollar amount, a map pin and a
product. The priors arrive instantly (Jacobs, AECOM, Fluor, Fortive, Danaher). THE SOURCE LEFT THE
BLANK; FILLING IT IN IS NOT RESEARCH.**
**2. Dollar path:** n/a — no Company B to assign a segment to.
**3. Timing window:** ⚠ **FAILS INDEPENDENTLY AND WAS SCREENED FIRST, PER RULE (vi).** "Over several
years," and the query asked specifically whether any portion carries a dated construction start or
completion inside two quarters: **"there is no sourced basis to say that any portion of the $3 billion
has a construction milestone scheduled within the next two quarters."**
**4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — absent, not passing.
- Correlation (§4): no open satellite positions.
- Universe (§3): BDX is US-listed and far above the cap — but BDX is **Company A**, and the tariff
  relief is a **cost line at BDX itself**, which makes it **first-order and outside §4 at any price**.

**Outcome:** REJECTED on **part 1** (no named Company B) and **part 3** (no dated spend inside the
window). ⚠⚠ **THIS IS THE THIRD CONSECUTIVE SESSION CARRYING A MULTI-BILLION DOMESTIC-CAPEX PLEDGE
AND THE THIRD TO DIE THE SAME DEATH — Bayer $2.2B Ohio (10-05, 2031/2034), TSMC $60–64B capex (10-05),
BDX $19B/$3B (today). THE PATTERN IS THE FINDING, NOT THE INSTANCE: a capex pledge is announced by ONE
party, and its procurement is awarded later and privately. The announcement and the awardable
transaction are separated by quarters BY CONSTRUCTION.** ⚠ **Screen part 3 before spending the query
next time — this one was spent deliberately, because the $110M Columbus line looked dated enough to be
worth one call, and it was not.**

---

### T-2026-10-06-04 — GE HealthCare (GEHC) / Sofie Biosciences $945M — no Company B — REJECTED
**Company A / the news:** **GE HealthCare (NASDAQ: GEHC)** agreed to acquire **Sofie Biosciences** for
**$945M in cash**, announced **2026-10-06**. No closing timeline reported.
**Company B / the candidate:** **NONE REACHED. NO QUERY SPENT — and that is the discipline, not a gap.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN WITHOUT AN "AND ALSO."** Sofie operates a
radiopharmacy/PET-tracer network; the radiopharma supply chain is real, but the sentence would have to
run "GEHC buying Sofie causes [isotope or cyclotron supplier]'s revenue to rise **and also** that
supplier is public, named, and material" — three conjunctions, which is the test failing.
**2. Dollar path:** ⚠ **THE DISCLOSED FIGURE RUNS THE WRONG WAY — RULE (viii) VERBATIM.** $945M is
**capital paid OUT by the buyable leg**. The receiving leg, **Sofie, is private**, so there is **no
buyable second leg at all** — the AWS/SNPS and Royal Caribbean family.
**3. Timing window:** no disclosed close date; unassessable.
**4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED**.
- Correlation (§4): no open satellite positions.
- Universe (§3): GEHC is US-listed and above the cap, but is **Company A**. Sofie is **private** —
  not buyable at any price.

**Outcome:** REJECTED on **part 2** (capital paid out by the buyable leg; counterparty private), with
**part 1** failing the one-sentence test. ⚠⚠ **AND RULE (vii) CLOSES THE LAST DOOR: GE HEALTHCARE
MAKES ITS OWN CYCLOTRONS AND PET SCANNERS. The equipment beneficiary of GEHC expanding in
radiopharmaceuticals is GEHC. That is the IOVA/EW vertical-integration shape on the imaging side —
and the non-integrated cyclotron makers (IBA, Siemens Healthineers) are BELGIAN- and GERMAN-LISTED,
so §3 kills them before any mechanism is needed.** ⚠ **One query was declined here on purpose: part 2
was already dead on the direction of the only disclosed figure, and a funnel call on a name with no
mechanism is the decorative exercise this log has twice refused.**

---

### T-2026-10-06-05 — Blaize Holdings / NeoTensr — guidance revision — REJECTED
**Company A / the news:** **Blaize** issued a preliminary Q3 2026 update on **2026-10-06**:
preliminary Q3 revenue **~$0.5M**, FY2026 revenue guidance revised to **$32–36M**, attributed to
binding non-cancellable purchase orders from **NeoTensr** (relating to an **April 2026** contract for
up to **$50M**) plus a new order from an unnamed existing customer. Blaize said it is **"working with
suppliers"** — unnamed — to obtain remaining inventory before year-end.
**Company B / the candidate:** **NONE — killed by arithmetic before a name was sought.**

**1. Mechanism (one sentence):** not reached.
**2. Dollar path:** ⚠⚠ **IMPOSSIBLE BY ARITHMETIC, AND THIS IS THE CLEANEST PART-2 KILL IN THE LOG.**
Blaize's **entire** FY2026 revenue is guided to **$32–36M**. §4 part 2 requires the affected segment
to be **≥10% of Company B's total revenue**, and §3 requires Company B to have a **≥$10B market cap**.
A supplier's share of a $36M customer cannot reach 10% of any company large enough to be eligible —
**the two filters are jointly unsatisfiable here regardless of who the supplier turns out to be.**
⚠ **That is worth writing down as a general screen: when Company A's TOTAL revenue is small, no
eligible Company B can clear part 2, so the supplier search is pointless before it starts.**
**3. Timing window:** "before year-end" — inside the window, and irrelevant given part 2.
**4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED**.
- Correlation (§4): no open satellite positions.
- Universe (§3): **Blaize is a microcap** — a company guiding to $32–36M of annual revenue is orders
  of magnitude below the **$10B** floor. §3 kills it as Company A-adjacent at any price; it is not
  buyable here in any case.

**Outcome:** REJECTED on **part 2 arithmetic** (jointly unsatisfiable with §3), with the suppliers
**unnamed** (rule (v)) and the customer leg, **NeoTensr**, not established as public. ⚠ **Rule (iii)
is ALSO unestablishable: the source gives the revised range but not Blaize's own prior guidance, so
"did the source carry the company's OWN prior figure?" answers NO — the AAR failure mode, not the
IOVA pass.** ⚠ **It was the only clearly qualifying corporate item in scan 1, which says more about
scan 1 than about Blaize.**

---

### T-2026-10-06-06 — S&K Aerospace PROS 7 $4.3B / Powerus $82M / Voyager $22.4M — REJECTED (settled pattern, no query spent)
**Company A / the news:** Three US government awards reported **2026-10-06**: **S&K Aerospace** won
the **Air Force PROS 7** contract at **$4.3B**; **Powerus** received an **$82M** counter-UAS order
described as the **second order under an existing IDIQ contract**; **Voyager Technologies** received
**$22.4M** to prototype satellite deployment systems.
**Company B / the candidate:** **NONE. ZERO FUNNEL QUERIES SPENT — the carry-forward's instruction was
executed as written.**

**1. Mechanism (one sentence):** not reached.
**2. Dollar path:** ⚠ **$4.3B is a PROS-vehicle CEILING, not obligated revenue — rule (v)'s ceiling
sub-shape** (the RDW $980M / MTUS $995M family). **$82M and $22.4M are immaterial to any $10B+
company** and fail part 2 on size alone.
**3. Timing window:** no delivery schedules reported for any of the three.
**4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED**.
- Correlation (§4): no open satellite positions.
- Universe (§3): **S&K Aerospace is not publicly listed.** Powerus and Voyager Technologies are far
  below the **$10B** floor. **All three fail §3 on sight.**

**Outcome:** REJECTED on **§3** (none buyable) and the **settled defence-award pattern**.
⚠⚠ **FIFTH INSTANCE, AND THE INSTRUCTION WAS FOLLOWED RATHER THAN RE-TESTED: "US DEFENCE PROGRAM
AWARDS CANNOT PRODUCE A §4 CANDIDATE — spend ONE funnel query, then WRITE THE ANSWER DOWN AND STOP."
NO QUERY HAS EVER BEEN RE-ISSUED ON THIS PATTERN, and none was today.** The mechanism is **disclosure
practice**: a prime announces the award and the tier below it is commercially confidential.
⚠ **Powerus adds a rule (iii) costume on top — a "second order under an existing contract" is a
DELIVERY MILESTONE RECYCLED AS NEWS, the GM/Lockheed shape.**

---

### T-2026-10-06-07 — Macro complex (ISM services, Treasury yields, Fed repricing) — no Company A — REJECTED
**Company A / the news:** Four macro items in the window: **ISM September services PMI 54.9** (from
55.4, services prices component +1.4 to 74, announced **10-05**); **the 10-year Treasury yield at
~5.31–5.35%, highest since April 2002**, and the 30-year at ~5.66–5.70%, **highest since May 2002**
(10-05); **implied odds of an October Fed hike falling to ~20–24% from ~70–78% a week earlier**
(10-05/06); and **September payrolls +29k vs 79k consensus with unemployment 4.2%** — which the source
itself dated **"announced October 2, 2026, not October 5."**
**Company B / the candidate:** **NONE — THERE IS NO COMPANY A.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN — NO TRANSACTION AND NO SECOND PARTY.**
**2–4.** n/a.

**Hard filters:** not reached. No open satellite positions to correlate against.

**Outcome:** REJECTED — **no Company A.** ⚠⚠ **THE FED-REPRICING ITEM IS THE CARRY-FORWARD'S "MOST
SEDUCTIVE COSTUME" ARRIVING VERBATIM: A MARKET-IMPLIED PROBABILITY THAT MOVED, AND MOVED HARD —
~70–78% to ~20–24% IN A WEEK. A probability that CHANGED reads like an event with a date. It is the
same object: no named recipient, no transaction, ONE party.** ⚠ **The 23-year yield high is the same
shape with a bigger number attached, and SCALE MAKES IT MORE CONVINCING, NOT LESS.**
⚠ **The payrolls item is ALSO a rule (iii) kill — a 10-02 release re-reported as 10-05 news, and it was
already disposed as T-2026-10-05-06. It was NOT re-screened; the source dated it unprompted because
the query asked.** ⚠⚠ **FIFTH CONSECUTIVE SESSION LOGGING A MACRO/POLICY COMPLEX IN EXACTLY THIS SHAPE
(09-25, 09-29, 09-30, 10-02, 10-06). THE FINDING IS THE PATTERN, NOT THE INSTANCE.**

---

### T-2026-10-06-08 — OpenAI / Cerebras — collaboration statement — REJECTED
**Company A / the news:** Reported **2026-10-06**: OpenAI's CEO said OpenAI and **Cerebras** are
"working closely together" to improve AI-processing speed; Cerebras shares rose **9.1%**. ⚠ **The
source stated its own limit unprompted: "does not establish that a new supply agreement, capacity
commitment, regulatory decision or formal contract was announced… should therefore be treated as a
reported collaboration statement, not as a confirmed new transaction."**
**Company B / the candidate:** **NONE REACHED. NO QUERY SPENT.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN — THERE IS NO EVENT TO PUT IN THE FIRST
BRACKET.** A statement of intent has no dollar value, no term and no dated obligation.
**2. Dollar path:** nothing disclosed. **3. Timing window:** none stated. **4. Invalidation:** n/a.

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — and note that **Cerebras rose 9.1% in one session**, which would
  have **FAILED** the filter had it reached it (shape two, the filter working on a genuine news rise).
  ⚠ **It never got there, so this is an ABSENT check, not a pass.**
- Correlation (§4): no open satellite positions.
- Universe (§3): Cerebras is **first-order** — it is the named party in the statement — and outside §4
  at any price. OpenAI is **private**.

**Outcome:** REJECTED on **part 1** (no transaction; rule (iii) — a press statement is not new
disclosure). ⚠⚠ **AND THE PRIOR WAS READY BEFORE THE THESIS WAS: "the GPU vendor for any AI-compute
headline" is named in the carry-forward as a STANDING PRIOR, and the AMAT/LRCX/KLA chain already died
on 10-01. The pull here was to reach for NVDA, AVGO, TSMC or a memory supplier on a sentence containing
no contract. NO TICKER WAS SCREENED AND NO GUESS IS RECORDED AS A CANDIDATE.** ⚠ **A CEO's remark is a
fact about an INDUSTRY'S DIRECTION, not about a TRANSACTION.**

---

### 2026-10-05 (08:28 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$100,038.62**
at pre-flight 08:28). Window screened: **Friday's close through Monday pre-market (Oct 2 – Oct 5)** —
a weekend, i.e. **no completed session since the last run**. **Three Perplexity scans, all exit 0**
(two broad, one second-order funnel). **Seven candidates reached a thesis entry; ALL SEVEN WERE
REJECTED.**

⚠⚠ **A WEEKEND WINDOW IS A WINDOW OF RE-REPORTING, NOT OF EVENTS — AND `--recency day` CANNOT TELL
THE DIFFERENCE. THIS RUN HAS THE WORKED INSTANCE.** The 5a scan, asked for "the last 24 hours
(weekend of October 3-5)", returned the **onsemi/Synaptics revised merger** as a headline item. The
targeted follow-up established it was announced **October 1** and merely re-reported Oct 2–5 — the
source said so in its first sentence, unprompted. ⚠ **Rule (iii) caught it, but ONLY because the
second query asked for the announcement DATE. The broad query's own framing presented a four-day-old
8-K as fresh.** ⚠ **STANDING CONSEQUENCE: on a Monday, ask for the announcement date explicitly. A
recency filter bounds when something was WRITTEN, never when it HAPPENED.**

⚠⚠ **THE SECOND BROAD SCAN RETURNED ZERO NEW NAMES — EVERY ROW WAS ALREADY DISPOSED OR §3-INELIGIBLE
ON SIGHT, AND THAT IS A RESULT.** Asked directly for named two-party supply agreements with a
disclosed value in the window, the funnel returned: **Venture Global/ConocoPhillips** (disposed 10-02,
part 3, first delivery 2030) · **RTX SM-6 $24.4B** (disposed 10-02) · **MTUS $995M** (disposed 10-01,
rule (v) ceiling sub-shape) · **Big Sky Industrial** (counterparty UNNAMED; not §3-eligible) ·
**Tiberius Aerospace** (counterparty not identified) · **Bharat Forge/Pratt & Whitney Canada** and
**Jindal Stainless/Indian Oil** (India-listed, §3). ⚠ **NOT ONE WAS RE-SCREENED. The carry-forward
named all three disposed items and said do not rehabilitate; that instruction was followed rather
than re-derived.** ⚠ **Its own closing sentence: "no agreement found in the gathered material
satisfies all four conditions… without qualification."**

⚠⚠ **THREE VOLUNTEERED ABSENCES IN ONE RUN, AND THE COUNT IS NOW FIVE CONSECUTIVE SESSIONS.** The
onsemi query, asked whether any third public company was named, answered **"no identified third
public-company revenue beneficiary or loser."** The regulatory query, asked the same of two FDA
approvals, answered **"No"** for **both** EW and BMY in its own table. ⚠ **This is a CONTINUATION of
the standing carry-forward item (09-29, 09-30, 10-01, 10-02), reported with its count and NOT promoted
to a new finding.**

⚠⚠ **ZERO `move` CALLS WERE MADE IN THIS RUN. THAT IS THE *ABSENT* STATE — THE FOURTH — NOT A SKIPPED
CHECK AND NOT A PASS.** Every candidate died on §4 structure, part 1, part 2, part 3 or §3 **before an
eligible ticker with a mechanism was reached**, so the priced-in filter had nothing to fire on. ⚠ **A
decorative `move` call on a name that has no mechanism would have converted an honest absence into a
fake exercise, and was declined for that reason.** **Third instance (09-29, 10-02 were the first two).**

---

### T-2026-10-05-01 — ON Semiconductor / Synaptics — "Party A" / Morgan Stanley — REJECTED
**Company A / the news:** **onsemi revised its acquisition of Synaptics from all-stock (~$7B, agreed
June 25) to all-cash at $123/share, ~$5.7B**, announced **2026-10-01** (onsemi newsroom; Reuters/
Investopedia Oct 2–5 re-reporting). The revision **followed an unsolicited, non-binding competing
proposal submitted 2026-09-02 by a third party Synaptics' regulatory materials call only "Party A."**
Financing includes a **$2.45B committed term loan from Morgan Stanley**. Previously announced **$200M
annual run-rate synergies** reaffirmed; the ~59M share issuance and 12–13% dilution eliminated.
**Company B / the candidate:** **NONE FOUND.** Three were reached and all three failed.

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN FOR ANY CANDIDATE.** A change in the
*consideration* of a merger between two parties alters no third party's revenue or cost line. The
only sentences available are share-shift stories the reader supplies.

**2. Dollar path:** ⚠ **FAILS FOR THE ONE ELIGIBLE NAME.** Morgan Stanley is US-listed and far above
the §3 floor, which makes it the *reachable* trap. But the **arrangement and underwriting fee on a
$2.45B committed term loan is NOT DISCLOSED ANYWHERE IN THE ANNOUNCEMENT**, and on any plausible
estimate it is single-digit-to-low-tens of millions against MS revenue in the tens of billions —
**far under §4's 10% floor. Part 2 fails twice over: the figure is undisclosed AND immaterial.**
⚠ **This is standing rule (viii) exactly: a FINANCING COMMITMENT is not segment revenue at Company B.**
**3. Timing window:** n/a — no mechanism survived to be dated.
**4. Invalidation:** n/a — nothing to invalidate.

**Hard filters:**
- Priced-in (§4): **NOT REACHED — the ABSENT state.** No `move` call made; no candidate had a
  mechanism to price. *(Noted from the tape, not from a call: SYNA was reported **+14.1%** and ON
  **+6.5–8%** on the revision. Had SYNA reached the filter it would have FAILED it — shape two, the
  filter working — but it never got there.)*
- Correlation (§4): **pass, vacuously** — zero open satellite positions, so no `driver` field exists
  to collide with. ⚠ **A vacuous pass, recorded as such.**
- Universe (§3): **SYNA FAILS.** Its market cap is **~$5.7B — which IS the disclosed all-cash equity
  value of the deal by construction** (source: onsemi/Synaptics announcement, $123 × shares out).
  **Below the $10B floor.** ON and BMY-style acquirers aside, **ON is the ACQUIRER and first-order.**

**Outcome:** **REJECTED — four independent kills, and part 1 is the primary.**
**(a) PART 1: there is no Company B.** ON is first-order (the acquirer); SYNA is first-order (the
target). **Buying a target at a fixed cash price is merger arbitrage — a spread trade on deal
completion, with no §4 mechanism and no economics that change.** §4 is a second-order catalyst rule;
it does not contain a deal-arb clause and this run did not invent one.
**(b) RULE (iii): the news is not new** — 8-K'd October 1, re-reported over the weekend. **The 5a
query framed it as a weekend event and was wrong.**
**(c) RULE (viii): Morgan Stanley's $2.45B is a financing commitment**, not segment revenue.
**(d) §3: SYNA is below the market-cap floor.**

⚠⚠ **AND THE REASON THIS ENTRY IS THE MOST USEFUL ONE IN TODAY'S LOG — A NEW COSTUME FOR RULE (v),
AND IT IS THE MOST FILLABLE-LOOKING BLANK THIS FUNNEL HAS EVER PRODUCED: AN UNNAMED *BIDDER* WEARING
A LEGAL PSEUDONYM.** Rule (v)'s known form is an unnamed SUPPLY BASE made to look nameable by an exact
figure and a component category ($1.7B of "memory components"). **"Party A" is strictly worse**, because
unlike a diffuse supply base it is **ONE specific entity that definitely exists, definitely acted on a
dated day (2026-09-02), and is definitely known to the filer and redacted on purpose.** The blank has
a shape, a date and a motive — everything except a name.
⚠⚠ **THE PRIORS WERE INSTANTLY READY AND SPECIFIC, AS ALWAYS: another analog/mixed-signal consolidator
— Microchip, Skyworks, Qorvo, Renesas, Infineon.** ⚠⚠ **NO GUESS WAS MADE AND NONE IS RECORDED HERE AS
A CANDIDATE. Naming Party A would not be research; it would be supplying the causal link and then
finding a source adjacent to it — verbatim the root cause the eight standing rules share.**
⚠ **A REDACTION IS NOT A LEAD. If a future run meets "Party A," "Company X" or "a strategic party,"
the §4 answer is already written here: there is no Company B until the filing names one.**

---

### T-2026-10-05-02 — Bayer / New Albany, Ohio $2.2B plant (no Company B reached) — REJECTED
**Company A / the news:** **Bayer announced a planned $2.2B US pharmaceutical manufacturing site in
New Albany, Ohio**, ~600 jobs, with **drug-substance production planned for 2031 and finished-product
production for 2034** (2026-10-03/05 reporting).
**Company B / the candidate:** **NOT REACHED — part 3 ended it in one step.**

**1. Mechanism (one sentence):** not written. ⚠ **Deliberately not written** — see outcome.
**2. Dollar path:** not reached.
**3. Timing window:** ⚠⚠ **FAILS, AND BY THE WIDEST MARGIN ON RECORD. Drug substance 2031 is ~20
quarters out; finished product 2034 is ~32 quarters. §4's ceiling is TWO.** → no deadline assignable.
**4. Invalidation:** not reached.

**Hard filters:** none run. ⚠ **Correct order: part 3 is free and it fired first.**

**Outcome:** **REJECTED on part 3 in a single step, before any funnel query was spent.** This is
standing rule (vi) working exactly as the Venture Global calibration point says it should: *"Part 3
kills it in ONE step, before any funnel query is spent."* ⚠ **It now holds the record previously held
by Venture Global's 2030 first delivery (~16 quarters) — 2034 is roughly double that.**
**Two further independent kills, recorded but not needed:** ⚠ **(a) THERE IS NO COUNTERPARTY AT ALL** —
known form six; a self-funded greenfield plant names no supplier, no EPC contractor and no equipment
vendor in the announcement. **(b) Bayer is a German issuer**; the US listing is an ADR, and §4's
Company A does not need to be eligible, but there is no Company B to be eligible either.
⚠ **The priors were ready here too — pharma-equipment and engineering names — and none was written.**
⚠ **Long-dated industrial capex remains a STANDING FEATURE of this funnel, not a visitor. Fifth
session running.**

---

### T-2026-10-05-03 — Edwards Lifesciences (EW) — no Company B, volunteered absence — REJECTED
**Company A / the news:** **FDA approved Edwards Lifesciences' AUTUS Size-Adjustable Valve**
(2026-10-01), a surgical pulmonary valve for paediatric congenital-heart patients requiring
pulmonary-valve replacement.
**Company B / the candidate:** **NONE — the source VOLUNTEERED the absence.** Asked directly whether
the announcement disclosed a named publicly traded US supplier or manufacturing partner, the answer
was **"No. The announcement identifies Edwards as the product company but does not disclose a named
publicly traded U.S. supplier or manufacturing partner."**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN.** No second party exists in the disclosure.
**2. Dollar path:** not reached. *(Recorded for completeness, not relied on: a paediatric congenital
pulmonary-valve line is a small sub-segment of EW's surgical structural-heart business and would
almost certainly fail §4's 10%-of-revenue floor even at EW itself — but **EW is FIRST-ORDER** and
outside §4 at any price, so part 2 was never the operative test.)*
**3. Timing window:** not reached. **4. Invalidation:** not reached.

**Hard filters:** none run — no candidate reached them.

**Outcome:** **REJECTED on part 1 — no Company B exists in the announcement.** ⚠⚠ **THIS IS THE
COUNTER-CASE SHAPE TESTED HONESTLY AND IT CAME BACK NEGATIVE.** The carry-forward is explicit that an
FDA approval *enabling* a named company's product is the one macro-adjacent shape that **can** form a
real two-party chain, and warns against over-applying the "a government action is not a Company A"
rule against approvals. ⚠ **So this one was pursued, not dismissed — and the chain has only one link.**
⚠ **Standing rule (vii) is the mechanism: Edwards manufactures its own valves. Vertical integration
leaves no external supplier to find** — the same structure that killed the log's best-ever rule (iii)
pass (IOVA). ⚠ **The prior was ready (a polymer, tissue or catheter-component supplier) and was not
written.**

---

### T-2026-10-05-04 — Bristol Myers Squibb (BMY) — no Company B, volunteered absence — REJECTED
**Company A / the news:** **FDA approved an expanded indication for BMS's Camzyos (mavacamten)**
(2026-10-01), extending it to paediatric patients — reported as adolescents weighing at least 30 kg —
with symptomatic obstructive hypertrophic cardiomyopathy.
**Company B / the candidate:** **NONE — the source VOLUNTEERED the absence**, in the same table and
the same word as EW above: **"No."**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN.** No second party in the disclosure.
**2. Dollar path:** ⚠ **WOULD FAIL EVEN IF A CANDIDATE EXISTED, AND THE REASON IS WORTH WRITING: THIS
IS A LABEL EXPANSION ON A DRUG ALREADY APPROVED AND ALREADY SELLING IN ADULTS.** The incremental
population is adolescents ≥30 kg with obstructive HCM — a **small fraction of an already-narrow
indication**, against BMY revenue in the tens of billions. **Nowhere near §4's 10% floor, at BMY and
a fortiori at any supplier.**
**3. Timing window:** not reached. **4. Invalidation:** not reached.

**Hard filters:** none run.

**Outcome:** **REJECTED on part 1 — no Company B.** **BMY is FIRST-ORDER** and outside §4 at any price.
⚠⚠ **AND A SUB-SHAPE WORTH NAMING, BECAUSE IT IS THE SECOND APPROVAL IN TWO ENTRIES AND IT POINTS THE
OPPOSITE WAY FROM THE EW ONE: AN *EXPANDED INDICATION* IS THE WEAKEST FORM OF APPROVAL NEWS THIS FUNNEL
CAN MEET.** A first approval at least creates a product that did not previously exist and therefore a
supply chain that must be stood up. **A paediatric label extension creates no new manufacturing, no new
supplier and no new line — the drug is already being made.** ⚠ **The two FDA items in this run bracket
the range: EW's is a NEW product with a vertically integrated maker (rule vii), BMY's is an OLD product
with a wider label. Neither yields a Company B, for two different reasons.**

---

### T-2026-10-05-05 — TSMC capex $60–64B (no Company B reached) — REJECTED
**Company A / the news:** A semiconductor-industry report (TrendForce, 2026-10-05) discussed **TSMC's
2026 capex guidance raised to $60–64B**, expected revenue $44.6–45.8B and gross margin 65–67%, ahead
of TSMC's **October 15** earnings call; it also mentioned tight 3nm capacity and "Terafab" partnership
*talks*.
**Company B / the candidate:** **NOT REACHED.**

**1. Mechanism (one sentence):** not written. **2–4:** not reached.

**Hard filters:** none run.

**Outcome:** **REJECTED on rule (iii) before anything else, and the source disqualified it itself:**
⚠ **"Because this was an earnings PREVIEW, not a newly announced October 3-5 decision, it should not
be treated as a fresh corporate event in the period."** The capex guidance is TSMC's own already-issued
figure; the Terafab item is **talks, not a binding agreement**.
**Two further kills, both pre-existing:** ⚠ **(a) RULE (v): TSMC does not disclose per-supplier
allocation, so the supply base is UNNAMED** — and ⚠⚠ **(b) THE PRIOR HERE IS THE EXACT ONE THE
CARRY-FORWARD NAMES BY NAME: "Applied Materials / Lam / KLA." T-2026-10-01-01 already killed that
chain four sessions ago, as "no candidate reached."** ⚠ **It arrived again today attached to a
different Company A, which is rule (iv) in its purest form: a recurring chain that keeps dying the
same death is telling you about SEMICAP DISCLOSURE PRACTICE, not about a candidate maturing.**
⚠ **NO FUNNEL QUERY WAS SPENT. The answer was already written down, and the carry-forward's
instruction — write the answer down and STOP, do not re-word the query — was followed.**

---

### T-2026-10-05-06 — September payrolls / Fed repricing (no Company A) — REJECTED
**Company A / the news:** **September nonfarm payrolls +29,000** against estimates of 79–90k;
**unemployment 4.2% from 4.1%**; prior months revised down ~60k in aggregate; average hourly earnings
+3.0% y/y. Market-implied odds moved to a reported **77.9%** that the Fed holds at **3.75–4.00%** in
October, against **22.7%** for at least a 25bp hike.
**Company B / the candidate:** **NONE POSSIBLE.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN. There is no Company A, so there can be no
Company B.** A payrolls print is **one party** — in fact zero parties — and names no recipient of
anything.
**2–4:** not reached.

**Hard filters:** none run.

**Outcome:** **REJECTED — the macro/policy non-event, and this is now FIVE CONSECUTIVE SESSIONS
logging one** (09-25 rates · 09-29 Fed repricing · 09-30 tariffs · 10-02 the September payrolls and the
25bp hike · today). ⚠⚠ **THE FINDING IS THE PATTERN, NOT THE INSTANCE — and this instance carries BOTH
of the costumes the standing rule warns about at once.** **(a) A MARKET-IMPLIED PROBABILITY THAT MOVED**
(77.9%/22.7%) — *"a probability that CHANGED reads like an event with a date. Same object: no named
recipient, no transaction, one party."* **(b) RULE (iii): this is the SEPTEMBER print, and the 10-02
run already logged the September payrolls.** ⚠ **Re-reported over a weekend is not re-issued.**
⚠ **The source's own read-through was offered and explicitly flagged as inference: "banks, rate-sensitive
growth stocks, housing, consumer discretionary… That sector read-through is an inference; the sources do
not identify specific company earnings effects."** ⚠⚠ **A SECTOR IS NOT A COMPANY B. Scale makes this
object more convincing, not less — it moved the whole tape and it still has nobody on the other side.**

---

### T-2026-10-05-07 — G7 diesel / strategic reserve release (no Company A) — REJECTED
**Company A / the news:** Secondary market commentary reported **G7 economies agreeing to release up to
100 million barrels of diesel and oil over four months**, and a US request that Europe release strategic
diesel reserves to ease prices and avoid a US diesel-export ban.
**Company B / the candidate:** **NONE.**

**1. Mechanism (one sentence):** ⚠ **CANNOT BE WRITTEN, AND THE SIGN IS WRONG.** A reserve release adds
supply to push diesel prices **DOWN**. ⚠ **A long-only book cannot trade a price being pushed down, and
refiners' crack spreads COMPRESS on it — so the only available sentence argues for a short, which §3
forbids this account from expressing in any form.**
**2–4:** not reached.

**Hard filters:** none run.

**Outcome:** **REJECTED on three independent grounds, and the FIRST one is that the source refused to
stand behind it:** ⚠ **"The available evidence does not establish the formal terms, participating
governments, implementation timetable, or whether this was an official new decision… this item is NOT
SUFFICIENTLY VERIFIED."** ⚠ **An unverified event cannot be screened — it is not a weak candidate, it
is an absent fact, and those are different. No second query was spent trying to firm it up, because
§4's question (who is Company B?) is unanswerable regardless of whether the release is real.**
**(b) It is a GOVERNMENT ACTION with one party** — the same object as the payrolls entry above, in a
sector costume that *carries a number and names an industry*. **(c) The sign is wrong for a long.**

---

### 2026-10-02 (08:23 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$99,865.29**
at pre-flight 08:23). Window screened: **Thursday's close through Friday pre-market (Oct 1 – Oct 2)**
— one full session. **Four Perplexity scans, all exit 0** (three broad, one second-order funnel ×3 on
three separate events). **Five candidates reached a thesis entry; ALL FIVE WERE REJECTED.**

⚠⚠ **ZERO `move` CALLS WERE MADE IN THIS RUN, AND THAT IS AN *ABSENT* CHECK, NOT A SKIPPED ONE.**
Every candidate died on §4 structure, part 2 or part 3 **before an eligible ticker was reached**, so
the priced-in filter had nothing to fire on. ⚠ **"The filter did not fire" and "the filter had nothing
to fire on" look identical in a run summary and are not the same thing** — this is the second instance
(09-29 was the first).

⚠⚠ **THE DEFENCE-AWARD ITEM WAS USED RATHER THAN RE-READ, FOR THE SECOND SESSION RUNNING, AND IT NOW
HAS A FOURTH INSTANCE ACROSS THREE PRIMES.** The carry-forward said: expect this outcome, spend ONE
funnel query because the exception would be enormously valuable and the query is cheap, then **write
the answer down and stop — do not re-word the query.** That is exactly what happened on RTX/SM-6.
**One query, the familiar answer, no re-query.** ⚠ **The industry answer was sitting in this run's
priors (solid rocket motors, the Mk 72 booster) and was NOT written into a thesis.**

---

### T-2026-10-02-01 — RTX (no Company B found) — REJECTED
**Company A / the news:** The US Navy awarded **Raytheon, an RTX business, a multiyear contract worth
up to $24.4 billion** for Standard Missile-6 interceptors — five years plus two option years, to
replenish interceptor stocks (Reuters, RTX press release, 2026-10-01). ⚠ **The $24.4B is a MAXIMUM
POTENTIAL value, not an amount reported as obligated**, and quantities and delivery schedules were
not specified.
**Company B / the candidate:** **NONE EXISTS IN THE DISCLOSURE.** The funnel asked directly whether
any publicly traded US company had been named as an SM-6 subcontractor or component supplier with an
allocated dollar figure. The source answered that **none had**, and volunteered the epistemic rule
itself: *"Any attribution of SM-6 revenue to other defense companies would be an inference rather
than a disclosed allocation."*

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN.** There is no second party to put in the
sentence. Writing one would mean naming a supplier from industry knowledge, which is an inference
about the *industry*, not a fact about *this transaction*.
**2. Dollar path:** **NO OPERAND.** No supplier-level allocation exists to size.
**3. Timing window:** **NOT ESTABLISHABLE** — delivery schedule expressly not specified.
**4. Invalidation:** **NO OPERAND** — no thesis to invalidate.

**Hard filters:**
- Priced-in (§4): **NOT REACHED** — no eligible ticker to test. ⚠ Absent, not passing.
- Correlation (§4): **NO OPERAND** — zero open positions, so no `driver` field to compare against.
- Universe (§3): **NOT REACHED.**

**Outcome:** **REJECTED on part 1, by absence of a counterparty** (rule (v): no named second party).
⚠ **RTX itself is FIRST-ORDER — the named prime in the headline — and is outside §4 at any price.**
⚠⚠ **THIS IS THE FOURTH CONSECUTIVE INSTANCE OF THE SAME STRUCTURAL FINDING, NOW ACROSS THREE PRIMES
AND THREE PROGRAMS: 09-29 AMRAAM $20.7B (RTX), 09-30 F/A-XX >$20B (Boeing), 10-02 SM-6 $24.4B (RTX).
The mechanism is DISCLOSURE PRACTICE, not luck — a prime announces the award and the tier below it is
commercially confidential, so the dollars are never allocated to a named public company.** ⚠ **A US
defence program award cannot produce a §4 candidate. Treat this as settled; one cheap query per award
remains worthwhile, re-wording it does not.**

---

### T-2026-10-02-02 — ORCL (no Company B found) — REJECTED
**Company A / the news:** **Tencent leased access to ~100,000 advanced AI chips from Oracle**, installed
at Oracle data centers in Southeast Asia — a **five-year arrangement estimated at ~$7 billion** with
roughly 30% payable upfront (Financial Times, citing people familiar; reported 2026-10-01/02).
**Company B / the candidate:** **NONE EXISTS IN THE DISCLOSURE.** The funnel asked whether any other
US-listed company was named as a chip, equipment, power or data-center supplier to this specific
agreement with an allocated figure. The answer: **no such supplier is named, and no supplier-specific
allocation is reported.**

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN, AND FOR A REASON SHARPER THAN MERE SILENCE —
THE TRANSACTION DOES NOT REACH A SECOND TIER AT ALL.** The chips are described as **already installed**
in Oracle's data centers. A lease of **existing** hardware generates **no new downstream procurement**,
so there is no supplier whose revenue line changes because of this deal, whether or not anyone names one.
**2. Dollar path:** **NO OPERAND, AND THE HEADLINE FIGURE IS NOT USABLE EITHER.** The ~$7B is a
**reported estimate from unnamed sources**; the source states **neither Oracle nor Tencent has publicly
commented.** ⚠ **An unconfirmed press figure is not a disclosed one and may not carry part 2.**
**3. Timing window:** Five years, with ~30% upfront — **the upfront portion is inside two quarters**,
so part 3 would plausibly have passed had anything else. **It did not get that far.**
**4. Invalidation:** **NO OPERAND.**

**Hard filters:**
- Priced-in (§4): **NOT REACHED.** ⚠ Absent, not passing.
- Correlation (§4): **NO OPERAND** — zero open positions.
- Universe (§3): ORCL is NYSE-listed and far above the $10B floor — **but §3 is irrelevant here,
  because ORCL fails §4's structure first.** ⚠ **Recorded as NOT REACHED, not as passing.**

**Outcome:** **REJECTED on structure.** ⚠ **ORCL is the NAMED PROVIDER — first-order, the headline
name §4 expressly says not to chase.** The second-order question ("who supplies the chips?") has the
answer sitting ready in this run's priors, and **it was not written**, for two independent reasons:
the source names nobody, **and** the deal leases hardware that already exists.
⚠⚠ **THIS IS A NEW SUB-SHAPE OF THE BINDING CONSTRAINT AND IT IS WORTH RECOGNISING ON SIGHT: A
TRANSACTION IN *CAPACITY ALREADY BUILT* HAS NO SECOND TIER TO BENEFIT.** It resembles form six (no
counterparty at all) but the mechanism differs — a second tier conceptually exists, the transaction
simply does not touch it. ⚠ **Graded honestly: this is one instance, not a pattern, and it is named as
a sub-shape rather than an eighth form.** ⚠ **Consequence: AI-compute *lease* and *capacity-access*
headlines are structurally weaker §4 material than *build* or *procurement* headlines, and the two
read almost identically in a news scan.**

---

### T-2026-10-02-03 — Venture Global / ConocoPhillips (no Company B found) — REJECTED
**Company A / the news:** **Venture Global signed a 20-year LNG sale-and-purchase agreement with
ConocoPhillips** for **1 million tonnes per annum**, with **deliveries beginning in 2030** (reported
2026-10-02). ⚠ **No dollar value was disclosed.**
**Company B / the candidate:** **NONE REMAINS.** Venture Global is the named seller and **ConocoPhillips
is the PAYER**. Both parties to the transaction are named and public, which leaves **no second party
outside the headline** to be a Company B.

**1. Mechanism (one sentence):** Could be written for Venture Global — *"the SPA causes Venture Global's
contracted LNG revenue to rise because ConocoPhillips commits to offtake 1 Mtpa"* — **but Venture
Global is the first-order named beneficiary, not a Company B.**
**2. Dollar path:** **FAILS.** **No contract value is disclosed anywhere in the available reporting**,
so the magnitude cannot be estimated, and 1 Mtpa cannot be converted to revenue without assuming a
price curve out to 2030. ⚠ **That assumption would be this run supplying the number the disclosure
withholds.**
**3. Timing window:** **FAILS OUTRIGHT AND DECISIVELY — FIRST DELIVERY IS 2030, roughly SIXTEEN
QUARTERS AWAY, against §4's two-quarter ceiling.** Nothing about this agreement appears in reported
results inside this strategy's horizon.
**4. Invalidation:** Writable in principle (*"Venture Global's filings show the SPA cancelled or
re-dated"*) — **irrelevant, parts 2 and 3 are already dead.**

**Hard filters:**
- Priced-in (§4): **NOT REACHED.** ⚠ Absent, not passing.
- Correlation (§4): **NO OPERAND** — zero open positions.
- Universe (§3): **NOT REACHED.**

**Outcome:** **REJECTED on part 3 primarily, part 2 independently, and structure independently of both
— THREE separate durable kills.** ⚠ **The part-3 kill is form seven of the binding constraint (the
spending simply lands too far in the future), and it is a FAR more extreme instance than 10-01's
Micron: Micron's capex aimed at late calendar 2028, this delivers in 2030.** ⚠ **A 20-year offtake
agreement is categorically outside a two-quarter horizon. Recognise long-dated offtake and SPA
headlines on sight: they are large, they are real, and they are never §4 material.**

---

### T-2026-10-02-04 — DKS / Nike's competitors (no Company B found) — REJECTED
**Company A / the news:** **Nike missed fiscal Q1 expectations** — revenue **$11.2B** below consensus,
**Greater China sales −12%**, wholesale revenue **$6.8B (−1%)**, North America direct **−8%**; shares
fell more than 3% (reported 2026-10-01/02).
**Company B / the candidate:** Considered in two directions — **(a)** athletic-footwear competitors
taking the share Nike lost, and **(b)** Nike's wholesale channel partners, principally **Dick's
Sporting Goods (DKS)**, the one US-listed sporting-goods retailer comfortably above the §3 $10B floor.
⚠ **BOTH DIRECTIONS WERE REJECTED, AND THIS IS THE MOST TEMPTING ENTRY ON TODAY'S BOARD — it is the
only candidate where a plausible second-order story was genuinely available to be written.**

**1. Mechanism (one sentence):**
> *Direction (a):* **FAILS THE ONE-CLAUSE TEST.** "Nike's revenue miss causes [competitor]'s footwear
revenue to rise because the share Nike lost went to them" requires a second clause to make sense —
**it must also be established that the share went to that competitor rather than to the category
shrinking, to private label, or to a non-US-listed rival.** ⚠ **A revenue miss at one company is NOT
evidence of a gain at a NAMED other, and no source names a beneficiary.** The names were ready in this
run's priors; none is a fact about this quarter.
> *Direction (b):* **WRONG SIGN.** Nike wholesale falling would, if anything, reduce DKS's supply of
its largest brand. That is a **headwind**, and §4 asks for a Company B whose economics **improve**.
**2. Dollar path:** **FAILS ON MAGNITUDE EVEN IF THE SIGN WERE RIGHT.** Nike's **wholesale revenue fell
1%** — on $6.8B, roughly $70M across Nike's entire global wholesale channel. ⚠ **Any single retailer's
share of that is immaterial against its own total revenue, far below §4's 10% threshold.** For
direction (a), **no competitor's incremental revenue is quantified by anyone**, so there is no figure
to allocate at all.
**3. Timing window:** Next quarter for a retailer — **would have passed. Did not get there.**
**4. Invalidation:** Writable in principle; **irrelevant, parts 1 and 2 are dead.**

**Hard filters:**
- Priced-in (§4): **NOT REACHED — and this is the one place the absence cost something worth naming.**
  ⚠ **No `move` call was made on DKS or on any competitor, because the candidate died on part 1 and
  part 2 first. A §4 filter run on a thesis that has already failed is a filter answering a question
  nobody asked.**
- Correlation (§4): **NO OPERAND** — zero open positions.
- Universe (§3): **NOT REACHED.** ⚠ Noted: the rivals that came to mind unprompted include at least one
  below the $10B floor and at least one non-US issuer, which **§3 would have killed anyway** — but
  recording that as the reason would be inventing a tidier kill than the real one. **The real kill is
  part 1.**

**Outcome:** **REJECTED on part 1 (both directions) and part 2 (independently).** ⚠⚠ **THIS IS A
DISTINCT AND USEFUL SHAPE: AN EARNINGS MISS IS NOT A SECOND-ORDER CATALYST. §4's structure is "A's news
IMPROVES B's economics," and a competitor's disappointment improves nobody's economics in any
disclosed, dateable way — it only invites a share-shift story that the reader supplies.** ⚠ **A
MISS-DRIVEN THESIS IS ALWAYS SELF-SUPPLIED. Expect to meet this shape every earnings season and kill
it on part 1 each time.**

---

### T-2026-10-02-05 — MU — REACHED AND DECLINED, NOT RE-SCREENED
**Company A / the news:** **Micron reported fiscal Q4 revenue of $54.23B** (against $11.32B a year
earlier and a cited $51.07B forecast) and guided fiscal Q1 to **$61.5B revenue and $38.15 EPS**
(against cited consensus $57B / $35.40); shares rose **3.03%** on 10-01.
**Why there is no thesis here:** ⚠⚠ **THIS EVENT WAS ALREADY SCREENED AND REJECTED YESTERDAY as
T-2026-10-01-01 (the Micron FY2027 capex chain, killed on part 3 — majority construction capex aimed
at cleanroom availability in late calendar 2028 and beyond). The carry-forward is explicit: 10-01's six
rejections DO NOT BECOME A QUEUE and must not be rehabilitated. THEY WERE NOT.** This entry records a
**refusal**, not a re-screen. **Zero Perplexity queries were issued on the Micron supplier chain, and
zero `move`, `quote`, `bars` or `asset` calls were made on MU or on any equipment name.**
⚠ **The prior-supplied answer the carry-forward names by ticker — Applied Materials, Lam Research, KLA
— was available again this morning and was again NOT written. The source closed that line explicitly
on 10-01.**

**The two fresh directions considered, and why neither becomes a thesis:**
- **Memory as a COST line** (PC/server OEMs facing surging DRAM/HBM prices): **the sign is wrong.** A
  cost increase is a headwind, and this strategy is long-only — §3 bans inverse and leveraged products
  and shorting is not contemplated anywhere in `strategy.md`. ⚠ **A correct bearish read produces NO
  TRADE by construction, and that is a limit of the strategy, not a thesis to force into a long.**
- **Cost increase plus pass-through pricing power:** **fails part 1's one-clause test immediately** —
  "input costs rise **and also** they can pass it through" is the "and also" construction §4 names as
  the single most common way a plausible connection is mistaken for an opportunity.

⚠⚠ **ONE CORRECTION THIS RUN OWES ITSELF, AND IT RUNS AGAINST THE USUAL DIRECTION OF THESE NOTES —
THE REFLEX WAS TO FLAG MICRON'S FIGURES AS IMPLAUSIBLE SOURCE CORRUPTION.** $54.23B of quarterly
revenue against $11.32B a year earlier is a 4.8× increase, and $38.15 of quarterly EPS reads as
garbled. ⚠ **BUT THAT JUDGMENT RESTS ENTIRELY ON A PRE-2026 PRIOR ABOUT MICRON'S SCALE, AND THE TAPE
HAS ALREADY OVERRUN IT: MU's own closes sat at 1072.18 → 1066.85 over the five sessions to 10-01
(recorded in `state.md` from a `move` call on 10-01), i.e. roughly $1,070 per share.** A share price
at that level is **consistent** with a memory supercycle of exactly this magnitude. ⚠ **Flagging the
figures as corrupt would have been asserting a stale prior over two independently sourced observations.
THE FIGURES ARE RECORDED AS REPORTED AND NOT DISPUTED.** ⚠ **The general form matters more than the
instance: an inherited sense of "how big this company is" is exactly the kind of unchecked claim the
audit discipline is for, and it fails toward DISMISSING real events rather than inventing fake ones —
the opposite direction from every other catch on the board.**

**Outcome:** **NO THESIS. Already-disposed event, deliberately not re-screened; two fresh directions
each killed on an independent, durable ground (sign / part 1).**

---

### 2026-10-01 (08:25 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper, broker equity **$99,693.94**
at pre-flight). Window screened: **Wednesday's close through Thursday pre-market (Sept 30 – Oct 1)**
— one full session. **Four Perplexity scans, all exit 0** (two broad, one second-order funnel, one
§3 market-cap check). **Six candidates reached a thesis entry; ALL SIX WERE REJECTED.**

⚠ **Two events were recognised on sight and deliberately NOT written up as new theses, because
re-litigating a disposed reject is exactly what the routine prompt forbids:**
- **Boeing / F/A-XX (>$20B)** — disposed yesterday as **T-2026-09-30-01**. The 09-30 funnel asked
  the source DIRECTLY whether any US-listed supplier had been named and was told none had. Nothing
  in today's tape changes that. **The carry-forward instruction is explicit: do not re-word the
  query.** Zero Perplexity calls were made on it today.
- **The Fed / PCE / trade-deficit macro complex** — August PCE +0.3% m/m (July revised to +0.1%),
  consumer spending +0.9%, Williams' "no urgency", the goods deficit +11.5% to $132.6B. ⚠ **These
  are NEW DATA on an object already disposed on 09-29**: an environment input with **ONE party** and
  no named recipient. ⚠ **Note the shape honestly — yesterday's seductive costume was a probability
  that MOVED (57% → 70%); today's is the same probability moving BACK. A reversal is no more a
  Company A than the move was.** Not written up.

⚠ **A third was recognised on sight and is the one closest to a real temptation: the MEMORY
READ-ACROSS.** Micron's print says memory/storage will be tighter in FY2027–28. The available
inference is "so SanDisk / Western Digital / Seagate pricing improves." ⚠ **That is the
COMPETITOR'S-EARNINGS-PRINT face of the shared-cause rule — memory pricing is a MARKET VARIABLE,
not a transaction, and the sentence needs an "and also" ("Micron is tight AND ALSO buyers
substitute to a rival"). Recognised, not screened. Zero `move`, `quote` or `asset` calls on SNDK,
WDC or STX.**

⚠ **And JBL appeared in a source citation today (−6.68% on the session). It is a disposed reject and
was not reached for — zero calls of any kind. A rejection is not a queue, and a lower price was
never what was missing.**

---

### T-2026-10-01-01 — AMAT / LRCX / KLA (no candidate reached) — REJECTED
**Company A / the news:** Micron (MU), 2026-09-30, raised its forward outlook; customer commitments
under signed long-term supply agreements rose to **$32B from $22B in June**, remaining performance
obligations to **~$150B from ~$100B**; planned US investment lifted to **>$250B through 2035**; and
it said it will **increase fiscal-2027 capex versus prior plans** (~$11.5B in FQ1, ~$25B in H1
FY2027, H2 higher). *(Reuters, Micron IR press release, Q4 call transcripts.)*
**Company B / the candidate:** intended to be a named semiconductor-equipment, construction or
materials supplier to the expansion. **No such company exists in the sources.**

**1. Mechanism (one sentence):** not written — see outcome.
**2. Dollar path:** not written.
**3. Timing window:** **THIS IS THE DURABLE KILL.** Micron's own call states the majority of the
capex increase is **CONSTRUCTION capex, primarily to accelerate cleanroom availability in LATE
CALENDAR 2028 AND BEYOND**, with equipment spend pulled forward but growing more slowly. ⚠ **That is
two years-plus outside §4's two-quarter horizon, and it holds EVEN IF a supplier is named later.**
**4. Invalidation:** not written.

**Hard filters:**
- Priced-in (§4): **MU −0.50% over 5 sessions (1072.18 → 1066.85), `priced_in: false`** — but MU is
  the **headline name and first-order**, so this was never the candidate. ⚠ **And it is the mild,
  passing form of defect shape one: a `false` verdict obtained by FALLING carries no information
  about whether the news is in the price.** **EXERCISED AND NON-DECISIVE.**
- Correlation (§4): **no open satellite positions, so no `driver` field exists to collide with.**
  ⚠ **The check had NO OPERAND — that is ABSENT, not PASSING.**
- Universe (§3): **not reached — no candidate ticker was ever established.**

**Outcome: REJECTED on part 3, with rule (v) as an independent second kill.** The funnel asked
directly which US-listed equipment, construction or materials vendors are explicitly linked to
Micron's expansion, and the source answered: *"no publicly traded U.S. semiconductor-equipment
supplier, construction company, or materials vendor was explicitly named… Naming companies such as
equipment manufacturers, engineering contractors, or materials suppliers based only on industry fit
would be an inference, not an explicit source linkage."*
⚠⚠ **A VOLUNTEERED ABSENCE, for the second consecutive session and the third in four — and this one
matters more than the F/A-XX instance because MY OWN PRIORS HAD THE ANSWER READY AND NAMED:
Applied Materials, Lam Research, KLA. Every one of them is a fact about the INDUSTRY, not about this
transaction.** ⚠ **This is §4's honest-broker paragraph describing the exact thing that nearly
happened: the plausible connection was available, fluent and unsourced.**
⚠ **Note what makes this entry worse than a dry hole: Micron's side is a CLEAN rule (iii) pass —
$22B → $32B and $100B → $150B are the company's own figures against the company's own earlier
figures, which is the test rule (iii) exists to apply. The news was real, new and quantified. It
still produces no Company B.** ⚠ **A SEVENTH form of open item (3): the figures are fully disclosed,
the news is genuinely new, and the spending lands TOO FAR IN THE FUTURE to be a catalyst — a kill no
widening of the evidence bar reaches, because the bar was never what stopped it.**
⚠ **The customer side was also considered and is not tradeable: tighter memory access is a COST
HEADWIND at cloud/AI buyers, and a long-only book cannot trade a cost increase.**

---

### T-2026-10-01-02 — AMD — REJECTED
**Company A / the news:** Hewlett Packard Enterprise (HPE), 2026-09-30, announced a **$1.2 billion**
order from **Vultr** (a private cloud-infrastructure provider) for **AMD Helios AI racks** including
HPE networking switches, software, liquid cooling and deployment services; HPE simultaneously raised
its networking-revenue growth outlook to the high teens through fiscal 2029. *(Reuters, CNBC.)*
**Company B / the candidate:** **AMD** — the Helios rack platform inside the order is AMD's, so AMD
must supply the hardware HPE delivers. ⚠ **This is the only STRUCTURALLY second-order candidate the
tape produced today, and it is why this entry got further than the other five.**

**1. Mechanism (one sentence):**
> HPE's $1.2B Vultr order causes AMD's Data Center segment revenue to rise because the racks HPE
> has been contracted to deliver are AMD Helios systems that AMD must manufacture and sell to HPE.

⚠ **Part 1 PASSES — one clause, no "and also", a real two-party transaction with a signed order and
a disclosed figure.** ⚠ **That is rare in this log and is the reason to read the rest carefully
rather than quickly.**

**2. Dollar path:** **FAILS, and in a specific way worth naming.** The affected segment is AMD's
**Data Center** segment, which is comfortably **above 10% of total revenue** — so the segment-share
half of part 2 passes easily. ⚠ **It is the MAGNITUDE half that fails: the $1.2B is HPE's ORDER
VALUE, and it expressly bundles HPE networking switches, HPE software, liquid cooling and HPE
deployment services. AMD's share of it is disclosed by NOBODY.** ⚠ **And the ceiling is unhelpful
even taken at its most generous: the ENTIRE $1.2B against AMD's annual revenue run-rate is a
low-single-digit percentage, spread over an undisclosed multi-quarter deployment.** ⚠ **This is rule
(viii) read broadly — the disclosed figure is not segment revenue at Company B — wearing its most
convincing dress yet, because unlike JBL's consignment structure there is no disclosure saying the
margin is zero. There is simply no allocation at all.**
**3. Timing window:** **FAILS OUTRIGHT AND THIS IS THE DURABLE KILL.** Every source reviewed states
that the reports **do not disclose a delivery schedule, contract duration, or revenue-recognition
timing**. ⚠ **So part 3 is NOT "beyond two quarters" — it is NOT ESTABLISHABLE IN EITHER DIRECTION,
which is exactly the AAR failure of 09-29 in a different sector.** ⚠ **The test is cheap and it is
the same test: did the source carry the figure? Here it did not, and a horizon assumed from how AI
rack deployments usually run would be a prior, not a disclosure.**
**4. Invalidation:** could have been written (*"AMD's next two 10-Qs show Data Center segment revenue
flat or declining sequentially"*) — ⚠ **but writing part 4 for a thesis whose parts 2 and 3 have
already failed is constructing the story and then looking for permission to keep it. Not written.**

**Hard filters (run BEFORE the thesis, per §4):**
- Priced-in (§4): **AMD −0.52% over 5 sessions (614.84 → 611.65), `priced_in: false`.**
  ⚠⚠ **THIRD STATE: EXERCISED AND NON-DECISIVE — the rejection does not turn on it.** ⚠ **AND IT
  PASSED BY FALLING, which is defect shape one (sign-blindness) in its mild, passing form: a name
  co-named in a $1.2B AI-order headline printing −0.52% over five sessions is precisely the reading
  that invites a "the market has not noticed" story. THAT STORY WAS NOT WRITTEN.**
- Correlation (§4): **NO OPERAND.** Zero open satellite positions, so there is no `driver` field to
  collide with. ⚠ **Absent, not passing.**
- Universe (§3): **PASSES** — AMD is US-listed common stock on NASDAQ, market cap far above the $10B
  floor. ⚠ **A sourced figure was NOT pulled, because the entry was already dead on parts 2 and 3
  and §3 would not have been the decisive kill. Recording that honestly: §3 is ASSUMED-CLEAR here,
  not VERIFIED, and no run may treat this line as an audited cap.**

**Outcome: REJECTED on part 3 (not establishable), with part 2 (magnitude undisclosed and immaterial
at the ceiling) as an independent second kill.**
⚠⚠ **AND A STRUCTURAL DOUBT THAT WOULD HAVE KILLED IT ANYWAY, RECORDED BECAUSE IT WAS NOTICED LATE
RATHER THAN FIRST: AMD IS IN THE HEADLINE.** Several sources run it as *"HPE secures its first AMD
Helios order in $1.2 billion deal with Vultr."* ⚠ **§4's whole premise is that you are not chasing
the headline name, and a company co-named in the headline is not obviously a Company B at all.** ⚠ **The
order of discovery is the lesson: the second-order STRUCTURE was found first and felt like the
finding, and the first-order OBJECTION arrived afterwards. On a day when parts 2 and 3 had not
already failed, that sequence is how a first-order trade gets taken wearing second-order clothes.**
⚠ **Vultr is PRIVATE and unbuyable; HPE is first-order and hit a record on the news.**

---

### T-2026-10-01-03 — SNPS (no second-order candidate) — REJECTED
**Company A / the news:** Synopsys signed a **multiyear agreement worth more than $1 billion** with
**Amazon Web Services**, licensing Synopsys' semiconductor IP to AWS. The report does not specify
duration, annual revenue contribution, or which IP products are involved. *(CNBC Daily Open.)*
**Company B / the candidate:** **none exists.**

**1. Mechanism (one sentence):** not written.
**2. Dollar path:** not reached.
**3. Timing window:** not reached — ⚠ **and could not have been: duration and annual contribution
are both expressly undisclosed, so this would have failed the same not-establishable test as T-02.**
**4. Invalidation:** not reached.

**Hard filters:** **not run. No eligible candidate ticker was ever established, so the priced-in
check is ABSENT rather than passed.** ⚠ **Zero `move` calls on SNPS or AMZN.**

**Outcome: REJECTED on structure — THERE IS NO SECOND PARTY LEFT TO BUY.** Both counterparties are
named and both are accounted for: **SNPS is the named beneficiary and therefore FIRST-ORDER**, and
**AWS/Amazon is the PAYER — capital paid OUT by the buyable leg, which is rule (viii)'s original
shape.** ⚠ **A two-party transaction in which both parties are named exhausts itself: §4 needs a
THIRD company whose economics change, and there is none.**
⚠ **The available inference — "AWS licensing more IP means more custom silicon, so a physical-design
or ASIC partner wins work" — names no company that any source connects to this agreement. That is
rule (v): filling in a blank the source left. Not pursued, and no query was re-worded to go looking.**

---

### T-2026-10-01-04 — Westinghouse / US–Korea reactor framework — REJECTED
**Company A / the news:** The US and South Korea announced a framework contemplating **up to eight US
nuclear reactors — six Westinghouse AP1000s and up to two Korean APR1400s**. The report states the
framework is **separate from and unrelated to** the DOE's American Nuclear Supply Chain Loans
conditional commitment, and is **a planning framework rather than evidence of completed orders,
financing, construction starts or near-term revenue.** *(Las Vegas Sun / Cameco release.)*
**Company B / the candidate:** not reached.

**3. Timing window:** **FAILS IN ONE STEP AND NOTHING ELSE WAS EVALUATED.** A framework
*contemplating* reactors is upstream of orders, upstream of financing and upstream of ground-break;
AP1000 construction runs the better part of a decade. ⚠ **Rule (vi) in its purest form, and part 3
kills it without any further work — which is the correct amount of work to spend on it.**

**Hard filters:** **not run.** ⚠ **Westinghouse is not independently US-listed** (Brookfield/Cameco
ownership), so there is no clean ticker for the named party in any case; ⚠ **and reaching for CCJ
as the proxy would be exactly the proxy-procurement costume this log has catalogued.** Not reached for.

**Outcome: REJECTED on part 3 (rule vi).** ⚠ **Logged deliberately despite dying in one line:
long-dated energy and nuclear offtake is a STANDING FEATURE of this funnel, not a visitor — Sempra /
Petrobras, Venture Global, Amazon/Generac, Centrus/Antares, Elmet, NeoVolta — and the value of the
entry is the eighth tally mark, not the analysis.**

---

### T-2026-10-01-05 — MTUS (Metallus) — REJECTED
**Company A / the news:** Metallus won a **five-year US Defense Logistics Agency contract with a
maximum ceiling of $995 million** to supply steel for defense applications. ⚠ **The report states
explicitly that the ceiling is NOT a guaranteed purchase amount**; no expected annual volume, no
minimum commitment and no guidance change were reported. *(CNBC Daily Open.)*
**Company B / the candidate:** none — Metallus is itself the awardee.

**Hard filters:**
- Universe (§3): **FAILS OUTRIGHT. Market cap ~$0.79B (≈$789M)** — source: **MarketBeat via
  Perplexity, 2026-10-01** — **against a $10B floor.** ⚠ **Pulled BEFORE the thesis was elaborated,
  so no effort went into a story a single number was always going to end.**
- Priced-in (§4): **not run — an ineligible ticker is not screened.** ⚠ **Absent, not passed.**

**Outcome: REJECTED on §3, with rule (v)'s CEILING sub-shape as an independent kill and
first-order status as a third.** ⚠ **The ceiling sub-shape is worth the ink: "$995 million" over
"five years" reads like a quantified dollar path, and the source itself supplies the sentence that
voids it. RDW's "$980M" multiple-award ceiling was the same object at almost the same number.**
⚠ **Note the §3-FIRST discipline held for the second consecutive session (RARE yesterday, MTUS
today) — and note equally that §3 being decisive twice running reflects WHICH EVENTS the tape
offered, not any change in how the funnel screens.**

---

### T-2026-10-01-06 — CALM (Cal-Maine Foods) — REJECTED
**Company A / the news:** Cal-Maine Foods reported a **wider-than-expected fiscal Q1 loss and weaker
revenue**; the source carries **no actual loss figure, no revenue figure, no consensus estimate and
no revised guidance.** Management plans to raise prepared-food capacity by **more than 60% through
the first half of fiscal 2028.** *(HDFC Sky market wrap.)*
**Company B / the candidate:** none — no counterparty appears anywhere in the disclosure.

**2. Dollar path:** **FAILS — there is no figure of any kind in the source to build one from**, and
the capacity plan is a percentage increase in capacity, which is **a VOLUME statement, not revenue**
(rule viii, read broadly).
**3. Timing window:** **FAILS INDEPENDENTLY — "through the first half of fiscal 2028"** is outside
§4's two-quarter horizon.

**Hard filters:**
- Universe (§3): ⚠⚠ **ATTEMPTED AND UNRESOLVED — RECORD THIS AS UNDECIDED, NOT AS PASSING.** The
  market-cap query returned a verified figure for MTUS and **explicitly declined to supply one for
  CALM** (*"I don't have a reliable current market-cap source in the provided search results"*).
  ⚠ **No §3 verdict may be claimed on CALM in either direction, and a future run must not inherit
  one from this entry.**
- Priced-in (§4): **not run.**

**Outcome: REJECTED on part 3, with part 2 as an independent kill.** ⚠ **An earnings print is not a
second-order catalyst: the only figures ever disclosed are the company's OWN lines, and a competitor
reading across from them is a COMPARABLE, not a transaction** — the same kill as Carnival, Vail and
CarMax on 09-30. ⚠ **And CALM is first-order in its own news.**

---

**📁 2026-09 ARCHIVED — 2026-10-02 (routine 5, monthly rollover).** All 87 theses dated
2026-09 (`T-2026-09-01-01` through `T-2026-09-30-08`) and their event-survey blocks moved
verbatim to **`archive/research_log/2026-09.md`**. Nothing was edited or dropped. **A run
working the reject board, recounting theses, or checking whether a name was already disposed
must read that file** — the standing rule that *a rejection is not a queue* applies to the
archive exactly as it applied here.

**Cumulative thesis count is 130 (0 ever accepted): 87 archived (`archive/research_log/2026-09.md`)
+ 43 live in this file.** ⚠ **Re-derived at the 2026-10-08 08:25 seat from the carry-forward base of
120 (113 through 10-06 + 7 on 10-07) plus the 10 written today. Do NOT "fix" this by re-adding
today's ten — they are already in it.** ⚠ **A run checking whether a name was already disposed MUST
READ BOTH FILES.**
