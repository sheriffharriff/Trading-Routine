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

### 2026-11-13 (07:01 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$99,141.26**).
`clock` 07:01:40 — `is_open: false`, `next_open` **2026-11-13T09:30:00-05:00**, `next_close`
**2026-11-13T16:00:00-05:00**. **Both fields carry today's date: the pre-market full-session
signature, NOT a holiday.** Friday, ordinary session.

**WEEK ROLLOVER — NO ACTION, RE-DERIVED WITH `isocalendar`, NOT INHERITED.** ISO **2026-W46
weekday 5**, Monday anchor **2026-11-09** = inherited `week_of`. `new_positions_this_week`
stays **0 of 3**.

**NEW POSITIONS PERMITTED THROUGHOUT.** Breaker **INACTIVE 0/3** · cap **0 of 3** · satellite
**0.0% deployed, $30,000 cash** · `control.md` Notes **(none)**. Nothing blocked a buy except
the candidates.

**FUNNEL SPEND: three broad sweeps, ZERO drill queries, three `move` calls, one `asset` call.**
Sweep 1 asked for disclosure dates and named counterparties up front (the retained 11-11
clause). Sweep 2 **excluded AI/data-centre/semis/macro by construction** — built from the
11-12 standing finding that the AI-datacentre supply tier is structurally unactionable, so the
sweep should stop paying to re-discover that. It returned **three items, all failing on their
face**. Sweep 3 inverted the leg again and demanded a **named US-listed RECIPIENT above $10B
with a quantified transaction** — it produced the day's only well-formed candidate.

⚠⚠ **THE DAY'S FINDING, AND IT IS MECHANICAL RATHER THAN A JUDGEMENT CALL: BOTH OF THE ONLY TWO
CANDIDATES THAT WERE FRESH, NAMED AND QUANTIFIED ENOUGH TO REACH THE HARD FILTERS WERE KILLED BY
THE PRICED-IN CHECK, BY ENORMOUS MARGINS — LEU +17.11% AND AMAT +19.34% OVER FIVE SESSIONS
AGAINST A 4% THRESHOLD.** That is 4× and 5× the limit, not a near miss.
⚠ **This is the first session on record where the §4 hard filter, not parts 1–3, did the killing
on every candidate that got that far.** The usual shape is a thesis dying at part 2 or 3 on
judgement. Today the arithmetic closed both doors before judgement was needed — which is
exactly the order §4 prescribes ("apply these before writing the thesis, not after"), and the
cheapest possible run: **zero drill queries spent.**
⚠⚠⚠ **THE HYPOTHESIS THIS RAISES, OFFERED AS A HYPOTHESIS AND NOT PROMOTED TO A RULE — a seat
may not invent a standing rule mid-run:** the properties that let a candidate survive parts 1–4
(fresh disclosure, named counterparty, quantified value, clear causal path) may be **the same
properties that cause the market to price it within hours**. If that holds, the sweep is not
merely unlucky — it is **structurally late on precisely the events that are well-formed enough
to be actionable**, and the well-formed/already-moved correlation is causal rather than
coincidental. **Two instances is not evidence.** What would test it: record `move_pct` for
every candidate reaching the hard filters and see whether well-formed candidates carry
systematically higher five-session moves than the malformed ones. **Only the human may turn
that into a prompt or `strategy.md` change.**

---

### T-2026-11-13-01 — LEU (Centrus Energy) ← Oklo's multi-year HALEU fuel contracts — REJECTED (priced-in +17.11%, FOUR TIMES the threshold; part 3 at ~12 quarters; part 2 unquantifiable; and it is the FIRST-ORDER leg)

**Company A / the news:** Oklo Inc. (NYSE: OKLO) announced multi-year HALEU fuel contracts with
Centrus Energy (NYSE: LEU), first disclosed **2026-11-12**. Oklo prepays for future deliveries;
contracted fuel supports **up to five Aurora powerhouses for multiple years**; **deliveries
begin in 2029**. **No dollar value disclosed.** (Perplexity, sweep 3, citing businesswire
2026-11-12.)
**Company B / the candidate:** Centrus Energy (LEU) — the named supplier and the recipient of
the prepayments.

**1. Mechanism (one sentence):**
> Oklo's prepaid multi-year HALEU purchase causes Centrus Energy's enrichment-segment contracted
> backlog to rise because Oklo is paying cash in advance of 2029 deliveries.

**2. Dollar path:** **CANNOT BE WRITTEN.** The announcement discloses **no dollar value** — only
"fuel for up to five Aurora powerhouses." Without a value there is no magnitude and therefore no
segment share, so the §4 10%-of-revenue materiality test **cannot be evaluated at all**, let
alone passed. ⚠ **Recorded as unquantifiable rather than small: those are different results and
collapsing them would overstate what this run established.**
**3. Timing window:** **FAILS.** Deliveries **begin 2029** — roughly **twelve quarters** out
against §4's two-quarter ceiling. Revenue recognition cannot precede delivery; only the
prepayment lands sooner, and a prepayment is a balance-sheet item, not a reported-results event.
**4. Invalidation:** not written — the thesis was already dead three ways.

**Hard filters:**
- Priced-in (§4): **+17.11%** over 5 sessions (88.90 → 104.115), `priced_in: true`,
  verdict *"LATE - skip"* → **FAIL**. ⚠ **This alone ends it, and it was run before the thesis
  was written.**
- Correlation (§4): **vacuously passes** — zero open satellite positions, so no shared driver
  exists to collide with. ⚠ **Recorded as vacuous, not as a pass: with an empty book this test
  has no discriminating power and must not be cited as though it confirmed anything.**
- Universe (§3): `asset` returns **us_equity / NYSE / active / tradable**. Market cap **NOT
  ESTABLISHED** — no drill query was spent, because the priced-in filter and part 3 had already
  closed the trade and §4 orders the cheap mechanical checks first. ⚠ **Not claimed as a pass.**

**Outcome:** **REJECTED, four independent ways.** (i) Priced-in by 4× the threshold. (ii) Part 3
fails by ~12 quarters. (iii) Part 2 is unquantifiable on the disclosed facts. (iv) ⚠ **AND THE
STRUCTURAL OBJECTION THAT WOULD HAVE KILLED IT EVEN AT AN UNCHANGED PRICE: LEU IS THE FIRST-ORDER
LEG.** The strategy is "news breaks about Company A; find Company B whose economics improve
because of it." Centrus is the company **named in the release as receiving the money** — buying
it is buying the headline, which §4 opens by forbidding. ⚠ **Also rule (iv): this is the SECOND
appearance of the HALEU fuel complex in TWO sessions** (`T-2026-11-12-03`, Standard Nuclear /
Antares TRISO, killed on rule (iii) + §3). The complex keeps resurfacing and keeps dying.

---

### T-2026-11-13-02 — AMAT (Applied Materials) ← Q4 results and ">30% WFE growth in 2027" commentary — REJECTED (priced-in +19.34%; part 1 — a CONDITION is not an event; part 3 outside the horizon)

**Company A / the news:** Applied Materials reported quarterly results described as better than
expected, first disclosed **2026-11-12**. CEO Gary Dickerson said advanced-semiconductor demand
**remains above supply** and that multiyear investment in new fab capacity is needed;
wafer-fab-equipment demand is projected to rise **more than 30% year over year in 2027**.
⚠ **The source explicitly frames the 30% figure as company commentary, NOT a committed capacity
announcement, and discloses no revenue, EPS surprise or capex dollar figure.**
**Company B / the candidate:** none reached — AMAT itself was screened as the only quantified leg.

**1. Mechanism (one sentence):** **CANNOT BE WRITTEN AS AN EVENT.** ⚠⚠ **"Demand remains above
supply" and "WFE will grow 30% in 2027" are descriptions of a STANDING CONDITION, not something
that happened in the last 24 hours.** This is the 11-10 AAON shape exactly — *a company's own
order book is a CONDITION, not an event* — arriving in a new sector. Part 1 requires "[Event]
causes [Company B]'s [line] to [improve]", and there is no event in the first slot: nothing
changed on 11-12 except that a company described a market it was already in.
**2. Dollar path:** no dollar figure disclosed for the capacity investment; the 30% is an
industry-wide WFE projection, not a Company-B revenue line.
**3. Timing window:** **FAILS.** A **full-year 2027** industry projection spans roughly quarters
two through five from here, and its early reported effect is a forecast rather than a result.
**4. Invalidation:** not written — dead at part 1.

**Hard filters:**
- Priced-in (§4): **+19.34%** over 5 sessions (319.335 → 381.095), `priced_in: true`,
  verdict *"LATE - skip"* → **FAIL**. ⚠ **Nearly 5× the threshold — the market absorbed this
  print immediately.**
- Correlation (§4): vacuously passes (empty book) — again, no discriminating power.
- Universe (§3): not evaluated; the trade was closed before it was worth a query.

**Outcome:** **REJECTED.** Priced-in by ~5×; part 1 fails because the "news" is a condition, not
an event; part 3 is outside the two-quarter horizon; and AMAT is the **first-order leg** of its
own earnings print. ⚠ **The second-order door was also already shut: `T-2026-10-01-01`
(AMAT/LRCX/KLA) reached no candidate, and the semicap tier has produced no Company B in six
weeks of trying.** No drill query was spent re-testing that.

---

### T-2026-11-13-03 — the data-centre onsite-power tier ← NTT DATA / Bloom Energy 900 MW deployment — REJECTED (rule (iii): disclosed 2026-11-05, EIGHT DAYS old; no value; and the standing structurally-unactionable tier)

**Company A / the news:** NTT DATA agreed with **Bloom Energy** to deploy **900 MW** of onsite
power across multiple global data-centre projects. ⚠ **First disclosed 2026-11-05** — surfaced by
a `--recency day` sweep run on 11-13. **No dollar value; no additional counterparties.**
**Company B / the candidate:** none reached.

**Hard filters / disposal:** **rule (iii) — the news is eight days old**, so whatever repricing
it justified happened last week. ⚠⚠ **THE SWEEP-WINDOW / DISCLOSURE-DATE GAP, FIFTH INSTANCE IN
THREE SESSIONS.** The 11-11 and 11-12 seats both recorded it; demanding the disclosure date
*inside the query* is again the only reason it was caught, and it caught this one immediately.
**Keep the clause.** Independently: **no dollar value** (part 2 unquantifiable), and both named
legs are the **spenders/first-order parties**. ⚠ **AND IT IS THE AI-DATACENTRE POWER TIER — the
object the 11-12 seat established as STRUCTURALLY UNACTIONABLE under §4 after the funnel returned
the exact missing figure a prior seat had named and the thesis died anyway.** Sweep 2 was
deliberately built to exclude this tier; it arrived through sweep 1 regardless.
**Outcome:** **REJECTED. Zero drill queries spent** — correctly, since no new evidence could move
a verdict that is structural rather than evidentiary.

---

### T-2026-11-13-04 — FRMI (Fermi) ← a reported 600 MW power-supply contract with an unnamed data-centre operator — REJECTED (rule (v): counterparty unnamed; no value; first-disclosure date not established)

**Company A / the news:** Fermi reportedly signed a **600 MW** power-supply contract with "a
large-scale data-centre operator," timing reported **2026-11-13**. ⚠ **The source itself flags
this as incompletely verified: the operator is NOT named, no dollar value is reported, and the
original disclosure date is unclear.**
**Company B / the candidate:** none reachable.

**Hard filters / disposal:** **rule (v) — the counterparty is an unnamed blank**, so there is no
second leg to screen and no way to identify whose economics change. **No dollar value** → part 2
unquantifiable. **No established first-disclosure date** → rule (iii) cannot even be tested.
⚠ **Three unknowns is not a thin thesis, it is an absent one.** Same structurally-unactionable
tier as `-03`.
**Outcome:** **REJECTED. Zero drill queries spent.** ⚠ **Explicitly NOT sent to a drill query to
name the operator:** the 11-12 rule (iv) finding is that supplying the exact missing figure in
this tier did not move the verdict, so paying to fill this blank is buying a kill already owned.

---

### T-2026-11-13-05 — the macro / policy complex (October core CPI +0.3% m/m, a third consecutive upside print · Williams "inflation far too high" · Daly tightening bias · December hike repricing · PPI pending) — REJECTED (no Company A — the standing object, unchanged)

**The news:** October core CPI **+0.3% m/m**, reportedly above expectations for a third
consecutive month (first disclosed **2026-11-10**). NY Fed's Williams said inflation was "far too
high" and the Fed "still has work to do"; Daly reportedly expressed a bias toward further
tightening (**11-12/11-13**). Dow futures lower on December-hike fears; PPI awaited.
**Disposal:** **no Company A.** §4 requires news *about a company* whose knock-on effect reaches a
different company; an index-level rate path has no issuer and reaches every holding at once, which
is the definition of an undiversifiable factor rather than a second-order catalyst. ⚠ **This is
the standing macro object — rejected at essentially every seat since early October
(`-11-11-04`, `-11-10-05`, `-11-09-04`, `-10-06-07`, `-10-05-06`).** Recorded for completeness
and for the §5 read-across; **zero drill queries spent.** ⚠ **Also rule (iii) on the CPI leg: the
print is three days old.**
⚠ **ONE THING WORTH CARRYING, AND IT IS A CORE-SLEEVE OBSERVATION, NOT A TRADE:** a hawkish
repricing is the macro state most likely to move the §2 core sleeve out of its 65–75% band. Core
sits at **69.74%** with **4.74pp** of room to the floor, so there is nothing to act on; the
midday and close seats should keep reading `rebalance_delta` rather than the narrative.
**Outcome:** **REJECTED.** No Company A, no second-order leg, no trade.

---

### T-2026-11-13-06 — sweep: twelve items disposed as one — REJECTED (ZERO drill queries spent)

Every item returned by the three sweeps that failed on its face. Named here so a later seat can
see what was looked at and not re-litigate it.

| Item | Kill |
|---|---|
| Global Ordnance Holdings / ARQUIMEA USA teaming agreement (11-12, US DoW prime, +129,000 sq ft) | **§3 both legs private**; no contract value, no unit volume |
| Safeway Richmond CA bakery closure (WARN filed **10-20**, effective 12-20, 92 workers) | **rule (iii), 24 days old**; **no replacement supplier named**, so no Company B; 92 workers is immaterial to any $10B+ issuer |
| Capricor Therapeutics ~10% workforce cut (11-10, FDA decision due 11-22) | own workforce only, **no external party**; §3 market cap; rule (iii) |
| Aurobindo / Aurolife FDA inspection closed "Voluntary Action Indicated" | **no first-disclosure date, no value, no named affected party**; foreign-listed |
| York Space Systems / Tomorrow.io — customer named behind a **$187M** contract (11-12) | **both legs private** (§3) |
| Star Equity / KBS Builders **$2M**, 12 modules (11-12) | **customer unnamed** (rule (v)); §3 micro-cap; $2M immaterial |
| Stellantis global supplier conference, 61 suppliers honoured (11-12) | **no value, no volume, no percentage** attached to any named supplier; foreign-listed |
| Net Power — up to **~$180M** contingent reimbursement (11-12) | **customer unnamed**; **contingent on no ESA being executed** — a conditional non-event |
| SBC Medical / NeuroBrain Dynamics (11-13) | counterparty **Taipei-based** (§3); no transaction value |
| Syncron / TEMOT International service-provider agreement (11-12) | §3 both legs; no value |
| Intermountain Electronics selects ISNetworld (11-12) | §3 both legs; no value |
| Liberty Defense — investor-relations engagement (11-13) | **not an operating event at all**; §3 |

⚠ **The distribution is the point and it is unchanged from 11-12: of twelve items, FIVE die on §3
alone (private or foreign counterparties), THREE on an unnamed counterparty, TWO on a stale
disclosure date, and ONE is not an operating event.** Nothing here reached a mechanism sentence.
**Outcome:** **ALL REJECTED, disposed as one entry, zero queries spent.**

---

### 2026-11-12 (07:01 ET) — event survey (funnel, pre-thesis)

Selftest **5/5**, exit 0 (`trading_enabled: true`, LIVE paper, equity **$98,849.07** at pre-flight).
`clock` 07:01:49 — `is_open: false`, `next_open` **2026-11-12T09:30:00-05:00**, `next_close`
**2026-11-12T16:00:00-05:00**: **both fields carry today's date — the pre-market full-session
signature. NOT a holiday.** Thursday, ordinary session. ⚠ **Read off the DATES, not the boolean.**

**WEEK ROLLOVER — NO ACTION DUE, RE-DERIVED AT THIS SEAT WITH `isocalendar`, NOT INHERITED.**
ISO **2026-W46, weekday 4**; Monday anchor **2026-11-09** = inherited `week_of` **2026-11-09**.
`new_positions_this_week` stays **0 of 3**.

**NEW POSITIONS PERMITTED THROUGHOUT.** Breaker **INACTIVE 0/3** · cap **0 of 3** · satellite
**0.0% deployed, $30,000 cash** · `control.md` **Notes: (none)**. ⚠ **Nothing blocked a buy except
the candidates, and that is the whole of today's result.**

**FUNNEL SPEND: four broad sweeps + two drill queries = six Perplexity calls; one `move` call.**
**Sweeps:** (1) corporate disclosures with the **disclosure date** and the **named-counterparty**
clause both demanded up front — the 11-11 one-clause change, retained because it paid for itself
twice; (2) regulatory / FDA / tariff / procurement decisions; (3) ⚠⚠ **A NEW SWEEP ANGLE, BUILT
DIRECTLY FROM THE 11-11 FINDING THAT THE TRANSACTION SWEEP IS STRUCTURALLY BIASED TOWARD COMPANY A:
it asked only for disclosures where the ISSUER IS THE BUYER AND THE NAMED COUNTERPARTY IS THE
SELLER** — i.e. it inverted the leg the press release comes from. **It returned ZERO US-listed
buyers, which is a clean and informative null rather than a failed query: the bias is not that the
sweep is worded badly, it is that BUYERS DO NOT ISSUE THE RELEASE.** ⚠ **Keep the angle; expect
thin returns from it and do not read thinness as a reason to go back to Company-A-shaped sweeps.**
(4) companies raising their **OWN PRIOR CAPEX** figure, excluding revenue raises and
reaffirmations by construction — **the sweep that produced the day's one real piece of work.**

⚠ **THE SWEEP-WINDOW / DISCLOSURE-DATE GAP APPEARED TWICE MORE TODAY, FOR THE THIRD AND FOURTH
TIME IN TWO SESSIONS:** a `--recency day` sweep run on **11-12** surfaced CoreWeave's **11-10**
release and Anthropic's **late-September** generator purchase as though both were fresh. **A SWEEP
WINDOW IS NOT A DISCLOSURE DATE**, and the only defence that has ever worked is demanding the
disclosure date **inside the query**.

---

### T-2026-11-12-02 — the AI-datacenter supply tier ← CoreWeave's raise of its OWN FY2026 CAPEX guidance — REJECTED (part 1 / rule (v); part 2; and a NEW rule (iii) costume) — ⚠⚠ **AND IT CORRECTS A FACTUAL CLAIM IN `T-2026-11-11-02`**
**Company A / the news:** **CoreWeave (CRWV)**, Q3 2026 release dated **2026-11-10**, stated
verbatim: *"We now expect full year 2026 capital expenditures of **$37 billion to $39 billion**,
raising the low end of our prior guidance range of **$35 billion to $39 billion**."* Prior range
issued with **Q2 2026 results, August 2026.** Stated reason: expectation to *"deploy infrastructure
and deliver it to customers sooner than planned."*
**Company B / the candidate:** **none reached** — the GPU, power, cooling, networking and EPC tier.
⚠ **The source states plainly that NO sentence anywhere in the release or the call names a supplier,
vendor, OEM or contractor with a dollar amount attached.**

⚠⚠⚠ **FIRST, THE CORRECTION, BECAUSE IT CHANGES WHAT THE PRIOR ENTRY ASSERTED AND IS NOT LEFT
BESIDE IT.** `T-2026-11-11-02` reads: *"The figure a supplier thesis would run on is CAPEX, and the
source discloses no change to it."* **THAT IS WRONG. THE CAPEX FIGURE DID MOVE, AND IT MOVED IN THE
SAME 11-10 RELEASE THE 11-11 SEAT WAS ALREADY READING.** That seat applied the right rule — *apply
rule (iii) to the figure the mechanism runs on* — to a **mis-stated fact**, and reached the right
verdict for a reason that was not true. ⚠ **A right answer from a false premise is the most
expensive kind of correct, because nothing downstream flags it.** The entry is amended in place.

**1. Mechanism: STILL NOT WRITABLE WITHOUT AN "AND ALSO", AND THE REASON IS NOW RULE (v), NOT THE
WRONG-FIGURE DEFECT.** With the capex correction applied, the 10-15 TSMC shape **no longer
describes this entry** — the figure with a supplier chain hanging off it is precisely the figure
that moved. ⚠⚠ **AND THE THESIS DIES ANYWAY, ONE RUNG LOWER AND HARDER: THERE IS NO NAMED
RECIPIENT. $37–39B of capex with no vendor named anywhere is the "unnamed supply base" costume at
the largest scale this funnel has ever met — and the obvious fill-ins (NVDA, VRT, DELL, SMCI, AAON)
arrive instantly and are entirely the reader's. THE SOURCE LEFT THE BLANK; FILLING IT IS NOT
RESEARCH.**
**2. Dollar path: FAILS TWICE, AND BOTH FAILURES ARE NEW SHAPES WORTH THE SPACE.**
  ⚠⚠⚠ **(a) ONLY THE LOW END MOVED. THE CEILING IS UNCHANGED AT $39B — NOT ONE DOLLAR WAS ADDED TO
  THE MAXIMUM CoreWeave HAS EVER TOLD ANYONE IT MIGHT SPEND IN 2026.** A supplier thesis needs
  **incremental** dollars; what was removed was the possibility of CoreWeave spending **less**.
  ⚠ **"RAISED CAPEX GUIDANCE" IS TRUE OF THE RANGE AND FALSE OF THE CEILING, and the headline
  phrasing carries the first meaning while a supplier thesis runs on the second.**
  ⚠⚠ **(b) THE STATED REASON IS TIMING, NOT VOLUME:** *"deliver it to customers sooner than
  planned."* **A PULL-FORWARD INSIDE AN UNCHANGED CEILING MOVES WHEN SUPPLIERS ARE PAID, NOT HOW
  MUCH.** A schedule change is not a dollar path.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **not reached — no candidate to measure.** CRWV is Company A and unbuyable under §4.
- Correlation (§4): not reached — zero open positions, no `driver` fields to collide with.
- Universe (§3): not reached; the thesis dies at part 1.

**Outcome:** **REJECTED** at **part 1 (rule (v), no named recipient)** and at **part 2 (ceiling
unchanged; timing not volume)**, independently.
⚠⚠ **AND THE GENERALISABLE FINDING, WHICH IS A NEW COSTUME FOR RULE (iii)'s LIST — A ONE-SIDED
RANGE NARROWING WEARING A GUIDANCE RAISE'S CLOTHES.** It passes the rule (iii) test as written
(the company's own prior figure is present in the source, and the new range differs), so a reader
who tests the release and stops at the first "yes" proceeds on a number that **did not increase the
total available to anybody.** ⚠ **It is the MIRROR IMAGE of costume #1 (reaffirmation): there, old
range and new range are identical; here, the FLOOR rose and the CEILING was reaffirmed in the same
breath — and only the floor gets quoted.** ⚠⚠ **THE TEST, AND IT IS ONE CLAUSE: ASK WHICH END OF
THE RANGE MOVED. For a supplier thesis, only the top end is a dollar path.**
⚠ **Rule (iv): this complex is now in its SIXTH consecutive session** (11-05 valuation unwind ·
11-06 IREN/QCOM · 11-09 sovereign-AI tier · 11-10 AAON/AAOI · 11-11 CRWV revenue · **11-12 CRWV
capex**) **and CRWV itself is at a THIRD appearance** (10-19 bond distress, 11-11, 11-12). **Every
one died at part 1 or part 2.** ⚠⚠ **AND TODAY IS THE STRONGEST FORM OF THAT WARNING YET, STRONGER
THAN THE 10-20 RTX INSTANCE: the 11-11 seat named the exact figure whose absence killed its thesis,
that figure turned out to have moved, THE FUNNEL CAME BACK WITH IT — AND THE THESIS STILL DIED, one
rung lower. THE FUNNEL DELIVERED THE MISSING EVIDENCE AND THE KILL DID NOT MOVE. That is the
clearest statement this log has produced that the AI-infrastructure complex is structurally
unactionable under §4, not merely under-documented.**

---

### T-2026-11-12-01 — Caterpillar (CAT) ← Anthropic's ~$3.4B / 1.7 GW generator commitment taken over from OnePWR Solutions — REJECTED (rule (iii), the news is six weeks old; THE JOIN, the candidate is named only in secondary reporting; and a NEW rule (viii) shape)
**Company A / the news:** **Anthropic** (private, pre-IPO) bought commitments for **1.7 GW of
heavy-duty gas-fired generators** for **~$3.4B**. ⚠⚠ **THE TRANSACTION WAS STRUCK IN LATE SEPTEMBER
2026**; it was first **reported by the Financial Times on 2026-11-08** and republished by Reuters the
same day. **There is no Anthropic disclosure dated 11-11 or 11-12 at all** — the item reached this
seat only because a `--recency day` sweep re-served two-to-six-week-old reporting as fresh.
**Company B / the candidate:** **Caterpillar (CAT)** — named as the generator manufacturer **only in
secondary reporting** (Yahoo Finance 11-12, citing CNBC), on the basis that OnePWR had previously
ordered the units from CAT and Anthropic assumed the order book.

⚠ **DISCLOSED CONFLICT, STATED RATHER THAN LEFT IMPLICIT: Company A here is the company that makes
the model running this routine.** It changes nothing — Anthropic is private and unbuyable under §3,
the candidate leg is CAT, and all three kills below are structural — **but a seat researching its
own maker's news should say so on the record rather than let a later reader discover it.**

**1. Mechanism: NOT WRITABLE, AND IT IS THE JOIN IN ITS PUREST FORM YET.** The **primary** source
(Reuters/FT) names **OnePWR Solutions**, a private San Antonio equipment supplier — **and the source
volunteered that the $3.4B figure and the OnePWR name are NOT IN THE SAME SENTENCE.** The **CAT**
name appears nowhere in the primary report; it arrives one layer further out, in an aggregator
citing a broadcaster. ⚠⚠ **SO THE CHAIN IS: a figure in one sentence → a private counterparty in
another → a US-listed name supplied by a third party reporting on the first two. ASK WHICH SENTENCE
CONTAINS BOTH THE FIGURE AND THE RECIPIENT — here no sentence contains either pairing.**
**2. Dollar path: FAILS, AND THIS IS A SHAPE RULE (viii) HAS NOT MET — A SECONDARY-MARKET TRANSFER
OF AN EXISTING ORDER BOOK.** ⚠⚠⚠ **The $3.4B did not buy new generators from Caterpillar. It bought
OnePWR's ALREADY-PLACED ORDERS. Those units were ordered BEFORE this transaction; CAT's backlog
already contains them; what changed is WHOSE NAME IS ON THEM.** A change of counterparty on an
existing order is **not incremental segment revenue at Company B** — and if it shows up at CAT at
all it shows up as a novation, not a sale. ⚠ **The nearest prior entry is FMC/Tessenderlo's
secondary-market SHARE purchase; this is worse-shaped, because there the money at least bought an
asset at a disclosed price from a party you could identify — here the money bought a QUEUE POSITION
and the manufacturer is a bystander to its own backlog.**
  ⚠ **And no segment figure exists even if the novation were granted: no source attributes any
  portion of $3.4B to CAT, the spend is spread across an undisclosed multi-year install, and CAT's
  Energy & Transportation segment turns over multiples of it per quarter. §4's 10%-of-revenue floor
  cannot even be tested.**
**3. Timing window:** not reached. *(Directionally hostile anyway: a 1.7 GW generator installation
programme is multi-year, and the package reportedly included the engineering and construction work.)*
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **CAT +1.77%** over 5 sessions (591.16 → 601.63) → `priced_in: false`,
  *"passes the priced-in check"*. ⚠ **PULLED AND RECORDED DELIBERATELY EVEN THOUGH THE THESIS WAS
  ALREADY DEAD, because it is the auditable number and because this is the FIRST reading in the
  direction-blind series that is a genuine, modest RISE — instance 17, and the only one of the last
  four where "passes" and "has not already moved" actually agree.** ⚠⚠ **IT IS ALSO EXACTLY WHY THE
  FILTER IS NOT A SUBSTITUTE FOR PART 1: the filter said "go" on a thesis with no named recipient,
  no primary-source candidate and no incremental dollar. A hard filter passing is not progress.**
- Correlation (§4): pass by construction — zero open positions.
- Universe (§3): **CAT passes trivially** (US-listed common stock, Dow component, market cap far
  above the $10B floor). ⚠ **Recorded as a pass that bought nothing, per the standing note that a
  clean pass on one filter is not progress toward a trade. OnePWR Solutions is PRIVATE and §3-dead;
  Anthropic is PRIVATE and §3-dead.**

**Outcome:** **REJECTED** on **three independent grounds**: **rule (iii)** — the economic event is
six weeks old and the reporting four days old, in a sweep that presented it as 24-hour news;
**the JOIN / rule (v)** — the only §3-eligible name in the story is supplied by secondary reporting,
not by the disclosure; and **part 2** — the money bought an existing order book, which is the
wrong-direction, wrong-party shape in a costume rule (viii) had not yet seen.

---

### T-2026-11-12-03 — Standard Nuclear ← HALEU TRISO fuel supply agreement with Antares; backlog $241.5M → $577.2M — REJECTED (rule (iii): the agreement was EXECUTED IN AUGUST; §3 kills both named legs)
**Company A / the news:** Standard Nuclear's **2026-11-12** results release disclosed an executed
fuel-supply agreement for **one metric ton of HALEU TRISO fuel** with options for up to **seven
more**, converting a previously nonbinding arrangement into a contract, and **total backlog rising
from its OWN prior $241.5M at 2026-06-30 to $577.2M at 2026-09-30.** Named counterparties:
**Antares** (the supply agreement) and **Radiant** (a completed full core load for its Kaleidos
microreactor).
**Company B / the candidate:** **none reachable.**

**1. Mechanism:** not reached. **2. Dollar path:** not reached. **3./4.:** not reached.

**Hard filters:**
- Universe (§3): **BOTH NAMED LEGS ARE PRIVATE.** Antares and Radiant are advanced-reactor
  developers; the source does not state that either is publicly traded, and neither is US-listed.
  **The door is closed before a mechanism is needed** — §3-first discipline, pull the eligibility
  before elaborating the story.
- Priced-in / correlation: not reached.

**Outcome:** **REJECTED.** ⚠⚠ **AND IT IS WORTH THE SPACE FOR TWO REASONS, NEITHER OF WHICH IS THE
VERDICT.** ⚠ **ONE — IT IS A CLEAN RULE (iii) PASS ON THE BACKLOG AND A CLEAN RULE (iii) FAIL ON THE
AGREEMENT, FROM THE SAME RELEASE.** The backlog move is the company's **own** prior figure, dated,
quoted, and more than doubled — the single best-formed rule (iii) pass in this run. **The supply
agreement it is attributed to was EXECUTED IN AUGUST 2026 and merely aggregated into a November
backlog number.** ⚠ **That is the 10-15 "one release, one genuine pass and one genuine fail on two
different figures" defect in a new sector — and here the PASS and the FAIL point at the same
economic event, which is new. A BACKLOG FIGURE IS A RESTATEMENT OF CONTRACTS ALREADY SIGNED; its
freshness is a property of the ACCOUNTING DATE, not of the deal.** ⚠ **TWO — it is the fourth clean
rule (iii) pass in two sessions to yield no Company B.**

---

### T-2026-11-12-04 — National Vision Holdings (EYE) ← FY2026 guidance CUT — REJECTED (rule (viii) wrong direction; rule (v) no named recipient)
**Company A / the news:** **2026-11-12** Q3 release cut FY2026 comp-sales growth from its **own**
**3.0–5.0% → 2.0–3.0%**, revenue **$2.037–2.076B → $2.019–2.038B**, adjusted operating income
**$119–139M → $119–131M**, and planned new stores **30–35 → ~30**.
**Company B / the candidate:** **none named.** The source states explicitly that no affected
public-company counterparty is identified, and that any supplier, landlord or competitor linkage
*"would be an inference, not a reported fact."*

**1. Mechanism:** not writable. ⚠ **The disclosed figures all move DOWN at Company A, so the only
available long story is a competitor share-shift read-across — the standing shared-cause object,
and the 10-02 sub-shape specifically: an earnings MISS IS NOT A SECOND-ORDER CATALYST, because a
competitor's disappointment improves nobody's economics in any disclosed, dateable way.**
⚠⚠ **AND THE STORE-COUNT CUT IS THE SAME TRAP WITH A HARDER EDGE: ~5 fewer stores means somebody
builds, fits out and supplies five fewer stores — ARITHMETICALLY CERTAIN, NEGATIVE IN SIGN, AND
NAMING NOBODY. It is the 11-04 onsemi DIVERSION shape with the sign reversed, which makes it
unusable for a long-only book twice over.**
**2.–4.:** not reached. **Hard filters:** not reached; §3 not tested on any leg.
**Outcome:** **REJECTED** at **part 1.**

---

### T-2026-11-12-05 — FDA Commissioner's National Priority Voucher programme shelved — REJECTED (government action, no named recipient — the standing object, unchanged)
**Company A / the news:** Reuters, **2026-11-12**: the FDA stopped advancing new applications to the
National Priority Voucher programme, applications still open; HHS said the pilot remained under
review. Names **Merck KGaA** (a prior voucher, Pergoveris) and **Revolution Medicines** (a pending
application, Rasonque) — ⚠ **but the report does not state that a decision issued on 11-12 changed
anything for either.**
**Company B / the candidate:** **none.**
**1.–4.:** not reached. **Hard filters:** not reached.
**Outcome:** **REJECTED.** ⚠ **The standing government-action object, and it needed no query beyond
the sweep that surfaced it: ONE PARTY, NO TRANSACTION, NO NAMED RECIPIENT OF ANYTHING.** ⚠ **The
counter-case is explicitly not over-applied against: an FDA *approval* enabling a named product
with a named supplier is a real two-party chain. THIS IS A PROGRAMME BEING PAUSED — the opposite
shape, and it removes an option rather than conferring one. §4 asks whose economics CHANGE, and a
withdrawn accelerator names no beneficiary.**

---

### T-2026-11-12-06 — FreeCast / Kind Wireless — REJECTED (§3 on both legs; no value, no commitment, no timing)
**Company A / the news:** **2026-11-12** — FreeCast agreed to supply Kind Wireless, a newly launched
MVNO, with a branded media/streaming platform on FreeCast's PaaS technology.
**Company B / the candidate:** **none §3-eligible.**
**Hard filters:** Universe (§3): **FreeCast is a microcap far below the $10B floor and Kind Wireless
is not identified as publicly traded.** The source discloses **no contract value, no minimum
commitment and no timing** beyond an expected rollout. **Door closed before a mechanism is needed.**
**Outcome:** **REJECTED** at **§3**, logged rather than dropped so the funnel's full output is
visible. ⚠ **This is the ELMT discipline applied cheaply: pull eligibility first, so no effort goes
into a story a single number was always going to end.**

---

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

### T-2026-11-11-02 — the AI-datacenter supply tier ← CoreWeave's raise of its OWN FY2026 revenue guidance — REJECTED (no counterparty named; rule (iv), fifth appearance of this complex in five sessions) — ⚠⚠⚠ **AMENDED 2026-11-12: THE "CAPEX UNCHANGED" PREMISE BELOW WAS FALSE. The verdict stands; the stated reason does not. See `T-2026-11-12-02`.**
**Company A / the news:** **CoreWeave (CRWV)** reported **2026-11-10** and **raised its own
FY2026 guidance**: revenue **$12.4–13.2B → $13.0–13.3B**, adjusted operating income
**$960M–1.15B → $1.275–1.375B**, citing continued AI-infrastructure demand (CNBC, 2026-11-10).
**Company B / the candidate:** none reached — the GPU, power, cooling and networking tier. ⚠ **The
source states plainly that NO specific customer, supplier or counterparty is named.**

**1. Mechanism:** not written without an "and also". ⚠⚠ **THIS IS THE 10-15 TSMC DEFECT ARRIVING
IN A NEW SECTOR, AND IT IS WHY RULE (iii) PASSING IS NOT PROGRESS: the figure that MOVED is
REVENUE, and revenue has no supplier chain hanging off it. The figure a supplier thesis would run
on is CAPEX. ⚠⚠⚠ **CORRECTION, 2026-11-12 — THIS CLAUSE ORIGINALLY READ "and the source
discloses no change to it [capex]", AND THAT WAS FALSE. THE SAME 2026-11-10 RELEASE THIS SEAT WAS
READING RAISED FY2026 CAPEX GUIDANCE TO $37–39B FROM ITS OWN PRIOR $35–39B, QUOTED VERBATIM.**
⚠ **So the right rule — *apply rule (iii) to the figure the mechanism runs on* — was applied here to a
MIS-STATED FACT, and this entry reached the right verdict for a reason that was not true.**
✅ **THE REJECTION STANDS AND IS STRENGTHENED, ONE RUNG LOWER: the capex move was a LOW-END-ONLY
NARROWING with the $39B CEILING UNCHANGED, attributed to pulling deployment FORWARD rather than to
spending MORE — and NO SUPPLIER IS NAMED ANYWHERE IN THE RELEASE OR THE CALL.** See
`T-2026-11-12-02` for the full working and for the new rule (iii) costume it mints.
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

**📁 2026-10 ARCHIVED — 2026-11-13 (routine 5, monthly rollover).** All 129 thesis entries
dated 2026-10 (`T-2026-10-01-01` through `T-2026-10-30-06`) and their event-survey blocks
moved verbatim to **`archive/research_log/2026-10.md`**. Nothing was edited or dropped.
⚠ **This rollover was due 2026-11-06 and is one week late; the 2026-11-06 review never ran.**

**📁 2026-09 ARCHIVED — 2026-10-02 (routine 5, monthly rollover).** All 87 theses dated
2026-09 (`T-2026-09-01-01` through `T-2026-09-30-08`) and their event-survey blocks moved
verbatim to **`archive/research_log/2026-09.md`**. Nothing was edited or dropped.

**A run working the reject board, recounting theses, or checking whether a name was already
disposed MUST READ BOTH ARCHIVE FILES** — the standing rule that *a rejection is not a queue*
applies to the archives exactly as it applied in the live file.

**Cumulative thesis count is 269 (0 ever accepted): 87 archived in `2026-09.md` + 129
archived in `2026-10.md` + 53 live in this file.** ⚠ **Re-derived at the 2026-11-13 review
seat by counting `^### T-` header lines in all three files and taking the FIRST thesis ID on
each line as that entry's own ID: 87 + 129 + 53 = 269, and all 269 are distinct — there are
no duplicate thesis IDs anywhere in the corpus.**

⚠⚠ **A CORRECTION MADE INSIDE THIS RUN, RECORDED BECAUSE IT IS THE EXACT SHAPE OF RECURRING
ERROR 4/5.** An earlier step of this same review reported "3 duplicate thesis IDs
(`T-2026-10-15-02`, `T-2026-11-11-02`, `T-2026-11-12-02`)" and month counts of 130/55. Both
were wrong, and wrong the same way: `grep -oE` counted *every* thesis ID appearing on a header
line, and several headers cite OTHER theses in their own title text (e.g. the `T-2026-11-11-02`
header carries an amendment pointer to `T-2026-11-12-02`). The cross-reference was counted as a
second entry. **The corpus has 269 theses and zero ID collisions.** The lesson is the standing
one: the least reliable number in this corpus is the one describing the run's own work, and the
fix was to count header LINES and extract one ID per line rather than count ID MATCHES.

⚠ **The previously carried figure of "130 cumulative" was the 2026-10-08 reading and had not
been updated in five weeks.**
