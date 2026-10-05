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

**Cumulative thesis count is 98 (0 ever accepted): 87 archived + 11 live in this file.**
