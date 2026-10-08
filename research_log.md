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
