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

### 2026-09-11 (08:20 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper account, equity
**$99,456.23**). Window screened: **Thursday's close through Friday pre-market (Sept 10–11)**.
Four Perplexity scans (two broad `--recency day`, two sourced second-order screens), plus three
`move --sessions 5` checks and one `bars` pull. **Five candidates reached ticker stage; all five
rejected. No BUY intent today.**

**The shape of the day: the single biggest event of the week — Oracle's FQ1 2027 print — was
screened directly, as yesterday's carry-forward required, and its second-order branch died three
separate ways at once.** That is stated first because the pull to find *something* in a $664B RPO
number is the strongest this month:

- **No US-listed company discloses Oracle as a named customer with a quantified revenue share.** A
  dedicated screen asking for exactly that returned **"No verified companies found."**
- **The FY27 capex guidance was *maintained*, not raised** — $90–95B total, ≤$70B net cash, the
  same range already guided. **Standing rule (iii): not new to the company's own disclosure.**
- **Management said the new bookings do not spend money inside this strategy's horizon.** The call
  is quoted as saying the vast majority of the >$30B of Q1 AI bookings were **prepay or
  bring-your-own-hardware**, "will not require incremental capital from Oracle," and **will not
  affect capex or revenue until fiscal 2028 or beyond** — past §4.3's two-quarter limit.

The events screened, and where each second-order branch died:

- **Oracle FQ1 2027, reported 09-10 after the close.** Revenue **$19.3B (+30%)**; **OCI $7.4B,
  +121%**; **RPO $664B, +$209B YoY and +$26B QoQ**, including **>$30B of new AI cloud contracts**;
  **850 MW of AI capacity and >300,000 GPUs delivered** in the quarter; FY27 capex **$90–95B**
  (Oracle IR release and 8-K, 09-10; call transcripts). See T-2026-09-11-01.
- **Palantir — $192M US Army production award for eight TITAN ground stations.** Fully
  allocated: **$127M Palantir, $65M Anduril** (private). See T-2026-09-11-02.
- **AeroVironment — $464.8M US Army E-HEL award for 30 kW LOCUST X3 counter-UAS lasers**, the
  first US production contract for a high-energy laser weapon. See T-2026-09-11-03.
- **Standard Lithium / LG Energy Solution — binding take-or-pay offtake, 8,000 t/yr of battery-
  quality lithium carbonate for 10 years** from the South West Arkansas project (6-K, 09-10). See
  T-2026-09-11-04.
- **Macy's FQ2 2026, reported 09-10 morning.** Adjusted EPS **$0.63** vs ~$0.35 consensus, helped
  by **$116M of IEEPA tariff refunds** ($84M pre-tax net, $0.23/share). See T-2026-09-11-05.

Items dropped before thesis stage, with reasons:

- **⚠ "Nvidia's $30B investment in Intel," "Nvidia acquires Hugging Face," "Google's first
  nuclear deal / $1.9B loan to restart an Iowa reactor," "Microsoft to triple cloud capacity by
  2032."** All four come from **one secondary aggregator briefing dated 09-11** that cites other
  outlets rather than any primary document. **A dedicated verification query found no SEC filing,
  no company press release and no major-press coverage for any of them.** Events of that size
  would produce primary disclosure; its absence is the finding. **Dropped before any ticker work
  — this is standing rule (iii) in a new costume: not a re-aggregation of old news but an
  unsourced claim, and the recency filter passes it just as readily.** If any of these is real it
  will arrive with a filing attached, and *that* is the day it enters the funnel.
- **August PPI +5.4% YoY (09-10), above the 5.3% consensus; core PPI +4.6%; August CPI released
  this morning; September hike odds rose to ~72% from ~61% into the 09-15/16 FOMC; jobless claims
  206k.** Macro. **No segment, no dollar path, no §4 mechanism.** Same disposition as 09-08,
  09-09 and 09-10, and for the same reason. Fourth consecutive day.
- **Adobe — softer Q4 revenue guidance (09-10 after the close).** Adobe is Company A and the sign
  is **negative**; the read-across to competitors is competitive inference, not a transaction.
  **This book has no short.**
- **Blackstone to acquire Flow Control Holdings**, a data-center liquid-cooling components maker
  (09-11). **The target is private and Blackstone is the acquirer — Company A on both ends.** The
  only second-order surface is "listed cooling names are therefore worth more," which is
  **standing rule (v)**: a fact about an industry dressed as a transaction. No ticker work done.
- **GrafTech ↔ Antora Energy, carbon materials for thermal batteries** (09-11). GrafTech is the
  named party and is **far below the §3 $10B floor**; Antora is private. **No value, volume or
  timeline disclosed** — part 2 could not be written even if the universe check passed.
- **Axogen's $200M acquisition of BioCircuit Technologies** (09-11). AXGN is below the §3 floor
  and the target is private.
- **Redwood Trust prices an upsized $185M convertible note offering** (09-11). Financing, not a
  commercial event. No second-order surface.
- **Corning ↔ Verizon, >80 million miles of optical fiber, 2027–2032.** Announced **09-08** —
  **outside the window and already disposed of** in the 09-09 funnel (GLW and VZ are the named
  counterparties; MTZ died on parts 1/2/3, FN on an unsourced mechanism). A source re-surfacing it
  on 09-10 does not make it new. **Not reopened.**
- **OpenAI ↔ Firmus, multi-year AI compute capacity from two Malaysian sites** (09-08). Both
  parties **private**, and outside the window.
- **Shell Energy North America buys Hunlock Creek (169 MW) and sells RISEC interests to
  Constellation for $715M** (09-10). Asset M&A, not a supply or offtake contract; the listed
  entity on one side is a **foreign issuer** and on the other a subsidiary LLC.
- **A US-backed tin refiner agreeing to buy up to 100% of an Australian miner's supply**
  (Bloomberg, 09-10). **Neither party named in any accessible source**, and the listed tin names
  are far below the §3 floor. Dropped before ticker work.
- **Kroger reports before the bell this morning; VinFast and Rent the Runway the same session.**
  **Not events yet at survey time.** Recorded so Monday's run knows they landed *after* this
  survey closed rather than being missed by it — the same sequencing note Oracle got yesterday,
  which is the note that made today's Oracle screen happen.

**⚠ A note on the priced-in filter — the defect the human is already holding fired twice today,
in both of its known shapes, on the same morning.** No run reinterprets the filter; this is
evidence for the open question, not a reason to touch §4.

- **Shape (1), the LITE shape — the filter rejects a stock for falling. It did not merely come
  close this time; it fired.** `move --sessions 5` on **LHX returns −4.47%, `priced_in: true`,
  "LATE - skip per strategy.md section 4."** LITE fired at −7.35% on 09-03; LMT came within 0.4%
  of firing at −3.61% on 09-10; **LHX crossed it today.** It cost nothing — LHX was already dead
  on part 2 arithmetic (see T-2026-09-11-02) — but **the filter's stated reason for skipping LHX
  is that it fell 4.47%.**
- **Shape (2), the QCOM shape — an event-day move absorbed before the filter reads it, and today
  it was absorbed *inside a single session*.** **AVAV traded as high as 159.23 on 09-10 and closed
  at 147.06** (`bars --adjustment all`), a **+12.9% intraday event move that round-tripped to
  +4.4% on the day** — and the five-session read is **+1.20%, `priced_in: false`, "passes."** The
  09-09 QCOM instance had a prior drawdown doing the absorbing; **here the same session did it.**
  Same root cause, third instance, **not a new item for the human's queue.**

---

### T-2026-09-11-01 — (no ticker) — REJECTED
**Company A / the news:** **Oracle (ORCL) fiscal Q1 2027, reported 2026-09-10 after the close.**
Total revenue **$19.3B, +30% YoY**; **OCI revenue $7.4B, +121% YoY**, accelerating from +93% in
Q4; **RPO $664B, up $209B YoY and $26B sequentially**, including **>$30B of new AI cloud contracts
booked in the quarter**; **850 MW of AI capacity and more than 300,000 GPUs delivered to customers
since the end of Q4** (~3x all of Q4, 73% of last fiscal year's total); **FY2027 capex guidance
$90–95B** with net cash capex **≤$70B**; Q1 capex **$28B**, net cash capex $18B, FCF **−$5B**; a
**$20B equity issuance** completed in Q1. Sources: Oracle IR press release and 8-K dated 09-10;
multiple independent earnings-call transcripts for the capex and GPU figures.

**Company B / the candidate:** **None could be identified.** This entry exists because yesterday's
carry-forward instructed this run to screen Oracle's print directly rather than assume a later run
would, and the honest output of that screen is a name that does not exist.

**1. Mechanism (one sentence):**
> **Not written.** No Company B survived to be named, so there is no revenue or cost line to put
> in the sentence. Writing one would require choosing a supplier myself — **standing rule (v)**.

**2. Dollar path:** not reached.
**3. Timing window:** not reached — and it is worth recording that it would have failed anyway.
Oracle's own call says the **vast majority of the >$30B of new bookings are prepay or
bring-your-own-hardware**, "will not require incremental capital from Oracle," and **will not
affect capex or revenue until fiscal 2028 or beyond**. §4.3 caps the horizon at **two quarters**.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **not applicable to a candidate that does not exist.** For the record, **ORCL
  itself returns +5.06% over five sessions, `priced_in: true`** — and ORCL is **Company A**, so
  §4's headline-name rule rejects it independently of the number.
- Correlation (§4): no open satellite positions; nothing to check against.
- Universe (§3): not reached.

**Outcome:** **REJECTED — three independent failures, any one of them sufficient.**
**(i) No Company B.** A screen asking specifically which US-listed companies have *themselves*
disclosed Oracle as a named customer with a quantified revenue share returned **"No verified
companies found."** Oracle's own materials name **no hardware supplier, no colocation partner and
no data-center developer** anywhere in the release, the 8-K or the retrievable call text, despite
extensive discussion of megawatts, GPUs and capex. **The unnamed-counterparty defect — fifth
appearance in nine sessions, and the largest event it has ever eaten.**
**(ii) Standing rule (iii).** The **$90–95B capex guidance was maintained, not raised.** The
sentence in the transcripts is *"We continue to anticipate $90 to $95 billion."* A reiterated
number is not new to the company's own disclosure and cannot be the news in a second-order thesis.
**(iii) Part 3, on Oracle's own words.** The genuinely new item — the $30B of Q1 bookings — is
structured to spend **no** incremental Oracle capital and to touch results in **FY2028 or later**.
**The biggest number in the release is the one furthest outside this strategy's horizon.**

**⚠ The thing worth writing down is how hard this one pulled.** A $664B RPO, 850 MW and 300,000
GPUs is the most vivid second-order surface this log has ever screened, and the temptation is not
to invent a fake mechanism — it is to name a *real* supplier from memory, note that it obviously
sells into hyperscale AI buildouts, and call the disclosure gap a technicality. **The names arrive
unprompted and they are plausible. That is exactly the limitation §4 warns about, and the absence
of any company willing to put Oracle's name and a number in its own filing is the whole answer.**

---

### T-2026-09-11-02 — LHX — REJECTED
**Company A / the news:** **Palantir Technologies won a $192M US Army production contract for
eight TITAN (Tactical Intelligence Targeting Access Node) ground stations** — four Advanced and
four Basic systems, delivered over 18 months. Multiple sources, 09-10.
**Company B / the candidate:** **L3Harris Technologies (LHX)**, named across sources as a company
involved in the TITAN program.

**1. Mechanism (one sentence):**
> The Army's TITAN production award causes L3Harris's Space & Airborne Systems revenue to
> increase because L3Harris supplies subsystems into the eight ground stations Palantir
> integrates.

The sentence is single-clause and reads cleanly. **It is also, on the numbers below, describing
money that does not exist.**

**2. Dollar path: FAILED, on arithmetic that closes the question completely.**
**The $192M award is fully allocated by the sources: $127M to Palantir and $65M to Anduril
Industries (private).** $127M + $65M = **$192M — the whole award.** L3Harris, Sierra Nevada,
Strategic Technology Consulting and World Wide Technology are named as **involved in the
program**, but **no source discloses any dollar value to any of them, and there is no residual
left in this award to disclose.** Against L3Harris revenue of roughly $21B/yr, even the entire
$65M non-Palantir share would be **~0.3%** — against §4.2's **10%** floor, and that share is
already spoken for by a private company.
**3. Timing window:** 18-month delivery — **past the two-quarter limit** even if part 2 had held.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): `move --sessions 5` = **−4.47%, `priced_in: true`, "LATE - skip."** **The filter
  rejects LHX for having fallen 4.47%** — open human question #1, firing for real. **It changed
  nothing here: part 2 had already killed the thesis on arithmetic.**
- Correlation (§4): no open positions to check against.
- Universe (§3): LHX is US-listed and above the $10B floor — **the only test it passes.**

**Outcome:** **REJECTED on part 2.** The award has no unallocated dollars in it, and a named
program participant with **$0 disclosed from this contract** is not a dollar path.

**⚠ This is the name the last nine days of carry-forward specifically warned about, and it is
worth recording exactly how it resolved.** `state.md` has flagged LHX for a week as "the
specifically invited name" — the one memory offers whenever a defense award has an unfilled
supplier chain, a case of **standing rule (iv)** (a recurring ticker is a warning, not
corroboration) compounded by **rule (v)**. **Today it arrived properly: a published source named
it, so re-running its filters was legitimate rather than an inherited conclusion.** And it died
anyway, on a number — **not on the warning, not on discipline, but because $127M + $65M = $192M
and there is nothing left.** That is a better outcome than avoiding the name, because it is
auditable. **Note carefully what did *not* happen: Anduril's $65M is real second-order money and
Anduril is private, which is the third time this month the identifiable beneficiary was not
listed.**

---

### T-2026-09-11-03 — (no ticker) — REJECTED
**Company A / the news:** **AeroVironment (AVAV) received a $464.8M US Army contract under the
Enduring High-Energy Laser (E-HEL) program for 30 kW LOCUST X3 counter-UAS laser weapon systems** —
reported as the **first production contract for a high-energy laser weapon in US military
history**. Sources dated 09-07 through 09-10; carried into 09-10 earnings-day coverage alongside
AVAV's FQ1 print (record **$1.5B funded backlog**, FY27 revenue guidance **maintained** at
$2.125–2.225B, FCF **−$36M** on capacity investment).
**Company B / the candidate:** **None. No supplier is named by any source.**

**1. Mechanism (one sentence):** **Not written — there is no Company B to put in it.**
**2. Dollar path:** not reached.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **AVAV returns +1.20% over five sessions, `priced_in: false`, "passes"** — and
  **AVAV is Company A**, the awarded party, so §4's headline-name rule rejects it regardless. See
  the survey note above on how that +1.20% was produced: a **+12.9% intraday spike to 159.23 that
  round-tripped to a 147.06 close.**
- Correlation (§4): no open positions.
- Universe (§3): not reached.

**Outcome:** **REJECTED — no Company B.** A dedicated screen for the **laser source, beam director
or power subsystem** supplier returned, explicitly, that **no published source names any other
company** and **no dollar amount is broken out below AeroVironment's own $464.8M.**

**⚠ A 30 kW directed-energy weapon has a short and famous supplier list, and every name on it is
arriving unprompted right now.** Naming one would be **standing rule (v)** — a fact about the
directed-energy industry presented as a transaction — and this is the **fourth** time this month
the same reflex has had to be refused (JASSM/LRASM, MK 48, GF's Singapore fab, Bayer's withheld
"newgold® network" partners). **The source left the blank. Filling in a blank the source left
blank is not research.**

---

### T-2026-09-11-04 — SLI — REJECTED
**Company A / the news:** **Standard Lithium (SLI) signed a binding take-or-pay offtake agreement
with LG Energy Solution** for **8,000 tonnes/yr of battery-quality lithium carbonate over 10
years** (80,000 t total) from the **Smackover Lithium South West Arkansas project**, whose initial
phase is designed for **22,500 t/yr** nameplate. With the previously announced Trafigura offtake,
roughly **90% of targeted offtake volume** is now covered. 6-K and Korean press, **09-10**.
**Company B / the candidate:** **SLI itself was screened, and no second-order US-listed name
exists.**

**1. Mechanism (one sentence):** cannot be written for a Company B, because there is none —
LG Energy Solution is the counterparty and is **Korea-listed**; the JV partner is a **foreign
issuer**; Trafigura is **private**. Any read-across to US-listed lithium producers is **"lithium
offtake demand is firm," a fact about a commodity market, not a transaction** — standing rule (v).
**2. Dollar path:** **not computable even for SLI.** No contract value is disclosed by any source,
and deriving one requires assuming a lithium price. **The source publishes volume, not dollars.**
**3. Timing window: FAILED outright.** The 10-year term runs **from the start of commercial
production**, which has not begun. **Nothing reaches reported results inside two quarters.**
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **not run — no `move` call was made and none was due.** §3 and part 3 had already
  closed the candidate, and §4 is explicit that the hard filters exist to kill candidates *before*
  a thesis is constructed, not to generate numbers for rejected ones.
- Correlation (§4): no open positions.
- Universe (§3): **FAILED. SLI is roughly $1B** — far below the **$10B floor.** LG Energy Solution
  is **not US-listed** (§3).

**Outcome:** **REJECTED on §3 and part 3.** A genuinely new, dated, binding, volume-specified
commercial agreement — **and the only listed party to it is a tenth of the size this strategy may
buy, with first revenue years away.** **§3 is a floor, not a preference.**

---

### T-2026-09-11-05 — M — REJECTED
**Company A / the news:** **Macy's (M) fiscal Q2 2026, reported 2026-09-10 before the open.** Net
sales **$4.9B, +1.1%**; comparable sales **+2.7%** (Macy's nameplate +1.1%, Bloomingdale's
**+11.3%**, Bluemercury +6.2%); adjusted EPS **$0.63** against roughly **$0.35** consensus; adjusted
EBITDA **$457M (9% of revenue, from 7.5%)**; FY26 net sales guidance raised to **$21.68–21.83B**.
**$116M of IEEPA tariff-refund proceeds** ($98M in-quarter, $18M after), a **$84M pre-tax net
benefit worth $0.23/share** and **180bp of the 41.5% gross margin**; **ex-refund adjusted EPS
$0.40, +14% YoY.** The stock **fell** on the print.
**Company B / the candidate:** screened for a named supplier, brand partner or landlord with
quantified impact. **None disclosed.**

**1. Mechanism (one sentence): FAILED, and this is the interesting rejection of the day.**
The tempting sentence is *"the IEEPA tariff-refund ruling causes other import-heavy US retailers'
cost of goods to fall, because they paid the same tariffs Macy's is being refunded."* **That is
not a §4 mechanism.** §4 requires that **news about Company A changes Company B's economics.**
Macy's receiving $116M **does not cause any other company to receive anything** — both companies
are downstream of the *same* trade-law ruling. **That is shared exposure to a common cause, which
is a correlation, not a causal path.** And any company actually receiving refunds discloses them
**itself**, in its own results, which makes it **first-order for that company** and not news
Macy's print carries.
**2. Dollar path:** not reached. **Macy's names no publicly traded supplier, brand partner or
landlord with a quantified impact anywhere in the release or call summaries** — the only quantified
external factor is the trade-law refund itself.
**3. Timing window:** not reached.
**4. Invalidation:** not reached.

**Hard filters:**
- Priced-in (§4): **not run and not due** — no Company B reached the filter stage.
- Correlation (§4): no open positions.
- Universe (§3): not reached.

**Outcome:** **REJECTED on part 1.** **A shared cause is not a mechanism.** Worth recording as a
distinct failure shape: every other part-1 rejection in this log died because no counterparty was
named. **This one had a perfectly real, quantified, dated economic event with obvious read-across
— and the read-across runs through a statute, not through a transaction.** The distinction is easy
to lose precisely because the sentence sounds causal when said aloud.

---

Selftest passed all five checks (`trading_enabled: true`, LIVE paper account, equity
**$99,266.82**). Window screened: **Wednesday's close through Thursday pre-market (Sept 9–10)**.
Four Perplexity scans (two broad `--recency day`, two sourced second-order screens
`--recency week`), one universe/segment check, plus five `move --sessions 5` checks. **Six
candidates reached ticker stage; all six rejected. No BUY intent today.**

**The shape of the day, stated first because it is the finding: the funnel produced four
genuinely new, dated, sourced commercial events, and the second-order layer failed each time for
a *different* reason — and for the first time this month one of those reasons was arithmetic
rather than an absent disclosure.** That distinction matters, so it is stated up front:

- **T-2026-09-10-03 (EQT) is the first rejection in this log where part 2 failed on a number I
  could actually compute rather than on a number nobody publishes.** Ignitis is committing to
  **one ~1 TWh LNG cargo per year** — about **3.4 Bcf** — against EQT sales volume of **634 Bcfe
  in Q2 2026 alone** (Zacks, 09-07). That is roughly **0.14% of annual volume**, against §4.2's
  **10%** floor. Not "undisclosed," not "unquantifiable" — **quantified, and two orders of
  magnitude too small.** Every previous part-2 rejection in this log died because the company
  does not break the segment out. This one died because the segment is real, disclosed, and the
  event is trivial next to it.

The four events, and where each second-order branch died:

- **Lockheed Martin — ~$1.08B in DoD awards, 09-09.** $825,975,480 modification (P00020) to
  FA8682-24-C-B001 for **JASSM/LRASM large lot procurement**, plus **$257,278,109** for **MK 48
  MOD 7 heavyweight torpedo** components (DoD daily contracts list, 09-09; Investing.com same
  day). **The supplier screen came back empty**: no published source names *any* US-listed
  company other than Lockheed as a supplier or subcontractor on either program. Torpedo work
  share is disclosed only at Lockheed's own facility level — **Liverpool NY 57%, Clearwater FL
  37%, Braintree MA 6%**. The unnamed-counterparty defect, fourth appearance in eight sessions.
- **Monolithic Power Systems — GlobalFoundries long-term manufacturing agreement, 09-09.**
  MPWR's process technology deployed at GF's **300mm Singapore fab**, volume production **early
  2027**. GFS is a **named party**, not a second-order beneficiary — the Corning failure mode of
  09-09 repeating exactly one day later.
- **Ignitis — EQT subsidiary LNG purchase agreement, 09-10.** 10 cargoes, one per year,
  **2027–2036**, Henry Hub/TTF-linked, still subject to Lithuanian national-security review. See
  the arithmetic above.
- **Centrus Energy — Radiant Industries HALEU supply, 09-09.** Multi-year, prepayments,
  deliveries **"before the end of the current decade."** Radiant is private; Centrus is the
  named beneficiary; **LEU is ~$3.4–3.8B, below the §3 $10B floor.**

Items dropped before thesis stage, with reasons:

- **August PPI released this morning, August CPI tomorrow (09-11); 10-year at 4.85%, the highest
  since November 2023; 30-year auction today; Treasury buyback of up to $6B of 10–20yr paper;
  mortgage rates 6.85%, highest in over a year; MBA refinance index at its lowest since May 2025;
  September hike odds ~59%.** Macro. No segment, no dollar path, no §4 mechanism. **Same
  disposition as 09-08 and 09-09 and for the same reason.** The rates move has an obvious
  read-across to homebuilders and mortgage REITs and it runs the **wrong way** for a long book,
  which is not a reason to write it up as a short — this strategy has no short.
- **Alcoa prices $2.6B senior notes to fund ~$3.1B cash consideration for South32 bauxite/alumina
  assets** (8-K, 09-09). **Financing for a *previously announced* acquisition** — standing rule
  (iii), not new to the company's own disclosure. Dropped before any ticker work.
- **Argan raises quarterly dividend 40% to $0.70** (09-09). Firm-specific capital return, no
  second-order surface, and ARGN is far below the §3 floor.
- **NASA on-ramps Relativity Space's Terran R to Launch Services II** (announced 09-09).
  Relativity is **private**. The read-across to listed launch providers is **competitive
  dilution, not benefit** — the wrong sign for a long book.
- **Samsung Biologics signs ₩350.8B (~$262M) CMO agreement through 2033** (regulatory filing,
  09-10). Samsung Biologics is **Korea-listed** (§3), and the counterparty is **explicitly
  undisclosed** under confidentiality provisions. There is no Company B to identify.
- **Chime to acquire Stride Bank for $590M cash** (09-09) — see T-2026-09-10-05.
- **Bayer–Neste winter canola feedstock agreement** (09-09) — see T-2026-09-10-06.
- **B. Braun sodium chloride injection recall** — dated **09-03**, outside the window, and
  B. Braun is private. No listed competitor or distributor is named by the notice.
- **Oracle and Adobe report after today's close; Macy's this morning.** **Not events yet.**
  Recorded so tomorrow's run knows they landed *after* this survey closed rather than being
  missed by it. Oracle's print in particular is the one with an AI-capex read-across surface.

**⚠ A note on the priced-in filter, added to the human's existing queue rather than as a new
item.** **LMT returned −3.61%, `priced_in: false`, "passes the priced-in check" — on the same
day it was awarded $1.08B.** It passes because the *magnitude* of a 3.61% **decline** sits inside
a 4% band. Another 0.4% of drawdown and the filter would have rejected a stock **for falling**,
which is the LITE shape exactly (open human question #1). This is not a third defect shape — it
is the **same** shape, caught 0.4% from firing, and it is worth one line because it shows how
narrow the margin was. **No run reinterprets the filter.** It cost nothing here: §4's
headline-name rule rejected LMT independently.

---

### T-2026-09-10-01 — LMT — REJECTED
**Company A / the news:** The US Department of Defense awarded Lockheed Martin ~**$1.08B** across
two contract actions on **2026-09-09** — an **$825,975,480** modification (P00020) to
FA8682-24-C-B001 for **JASSM and LRASM Large Lot procurement** (Lockheed Martin Missiles and Fire
Control, Orlando FL), and a **$257,278,109** modification to N00024-23-C-6411 for production,
spares, support material, engineering support and hardware repair of **MK 48 MOD 7 Heavyweight
Torpedo** components (Liverpool NY). Source: DoD daily contracts list for Sept 9 2026
(war.gov/News/Contracts), summarized same day by Investing.com.
**Company B / the candidate:** Lockheed Martin itself, in the absence of any identifiable
supplier.

**1. Mechanism (one sentence):**
> The DoD's large-lot missile award causes Lockheed Martin's Missiles and Fire Control segment
> revenue to improve because the department has contracted to buy that quantity of JASSM, LRASM
> and MK 48 hardware from Lockheed.

**2. Dollar path:** Missiles and Fire Control. ~$1.08B of contract actions against a company
whose annual revenue runs in the seventies of billions — the segment clears §4.2 comfortably,
but the **award is a fraction of a percent of revenue and is a modification to existing
contracts**, so the *incremental* figure is not separable from an already-booked baseline.
**3. Timing window:** Large-lot missile procurement delivers over years, not quarters. Not
establishable inside two quarters.
**4. Invalidation:** Not reached.

**Hard filters:**
- Priced-in (§4): **−3.61%** over last 5 sessions (544.45 → 524.77) → `priced_in: false`,
  "passes" — **and see the caveat in the survey above; it passes by 0.4%, for falling**
- Correlation (§4): no open satellite positions, no drivers to collide with → pass
- Universe (§3): us_equity, NYSE, market cap **~$121–124B** (source: Perplexity, citing Yahoo
  Finance intraday $123.738B and companiesmarketcap.com $123.73B, which cites Nasdaq $123.74B as
  of 09-08; MarketBeat/CNBC/Barron's cluster $121.0–121.2B) → pass

**Outcome: REJECTED — §4, "you are not chasing the headline name," and part 3 independently.**
**Lockheed is Company A.** The whole point of §4 is to find the company whose economics change
*because of* someone else's news, and I ran that screen properly: **a dedicated Perplexity query
asking for named, sourced, US-listed suppliers or subcontractors on JASSM, LRASM and MK 48
returned nothing** — the only work-share disclosure available is Lockheed's own facility split
(Liverpool 57% / Clearwater 37% / Braintree 6%), which is a fact about **Lockheed's internal
plants**, not about a supplier.

**⚠ And this is where the pull was, so it is recorded.** I know from general knowledge that
missile programs have solid-rocket-motor, seeker and energetics suppliers, and a name suggests
itself immediately. **Naming one here would be standing rule (v) — a fact about an industry
dressed up as a transaction — compounded by rule (iv), since that name is a recurring one in this
log.** No source ties any public company to *these awards*. A supplier relationship I can recall
but not source is not a supplier relationship I can trade. **Nothing was reached for.** The
related **Nitradyn $581M IMX-104 facility award** in the same DoD release was checked for the same
reason and dropped: Nitradyn is private and no listed energetics supplier is named.

---

### T-2026-09-10-02 — GFS — REJECTED
**Company A / the news:** Monolithic Power Systems and GlobalFoundries announced a **long-term
manufacturing agreement** to deploy MPWR's process technology at GlobalFoundries' **300mm fab in
Singapore**, with **volume production expected in early 2027** (Investing.com, **2026-09-09**;
carried in corporate-news summaries 09-10).
**Company B / the candidate:** GlobalFoundries — the fab that will do the manufacturing.

**1. Mechanism (one sentence):**
> The Monolithic Power agreement causes GlobalFoundries' foundry revenue to improve because
> Monolithic Power will pay GlobalFoundries to manufacture its power-management silicon at the
> Singapore 300mm fab.

**2. Dollar path:** Foundry services, GlobalFoundries' entire business. **The magnitude cannot be
sized: no contract value, no wafer volumes, no minimum-volume or take-or-pay terms are
disclosed by any source.** The relationship is certain; the number does not exist.
**3. Timing window:** **Volume production expected early 2027** → first meaningful revenue lands
in FY2027, beyond two quarters from today. **Fails §4.3.**
**4. Invalidation:** Would have been: GlobalFoundries' Q1 2027 results show no incremental
Singapore 300mm volume, or the agreement is disclosed as terminated.

**Hard filters:**
- Priced-in (§4): **+4.53%** over last 5 sessions (43.945 → 45.935) → **FAIL, `priced_in: true`,
  "LATE - skip"**
- Correlation (§4): no open satellite positions → pass
- Universe (§3): us_equity, Nasdaq, market cap **~$24.4–25.3B** (source: Perplexity, citing
  MarketBeat $24.81B on 09-08, Macroaxis $24.43B, GuruFocus $24.74–25.28B early Sept) → pass

**Outcome: REJECTED — §4 priced-in (+4.53%), part 3 (early 2027), and §4's headline-name rule.
Three independent failures.** **GlobalFoundries is a named party to the announcement**, not a
third company that happens to benefit from it — the identical disqualification to GLW yesterday,
one day later, in a different sector. Worth noting because it arrived looking different: the
*coverage* is MPWR-centric ("Monolithic Power stock heads into the open after the GlobalFoundries
deal"), so the beneficiary reads like a discovery rather than like the other half of a press
release. **It is the other half of a press release.** The priced-in number then confirmed it
independently — **+4.53% is a marginal failure, 0.53 points past the threshold, and marginal is
still failed.** No judgment was applied to soften it.

The third-party branch was considered and dropped without a ticker: semiconductor equipment or
materials suppliers into a Singapore 300mm line. **No source names one, and deploying an existing
process at an existing fab does not imply new tool purchases.** Standing rule (v).

---

### T-2026-09-10-03 — EQT — REJECTED
**Company A / the news:** **UAB Ignitis** (Lithuanian state energy group, not US-listed) will
enter a **long-term LNG purchase agreement for 2027–2036** with a subsidiary of **EQT
Corporation**, following a tender called 2026-08-25. **10 cargoes, one per year, each ~1 TWh**,
priced against **Henry Hub and TTF**. Completion is subject to review by Lithuania's Commission
for the Coordination of the Protection of Objects Important to National Security and to the
supplier's corporate approvals. Source: Ignitis material-event notice, reported by Yahoo Finance
Energy, **2026-09-10**.
**Company B / the candidate:** EQT Corporation — the US gas producer on the sell side of a
purchase commitment made by a foreign buyer.

**1. Mechanism (one sentence):**
> Ignitis's ten-year purchase commitment causes EQT's contracted LNG sales revenue to improve
> because Ignitis has agreed to buy one cargo per year from an EQT subsidiary from 2027 through
> 2036.

That sentence is clean, single-clause, and true. **The thesis dies on the next two parts, and it
is worth being explicit that it dies on size rather than on story.**

**2. Dollar path:** LNG / marketed gas sales. **~1 TWh per cargo ≈ 3.4 Bcf per year.** Against
EQT's **634 Bcfe of sales volume in Q2 2026 alone** (Zacks, 09-07), one annual cargo is roughly
**0.5% of a single quarter and ~0.14% of annual volume**. Vendor-reported FY2025 revenue sits in
an **$8.2–9.1B** band (Macroaxis $9.07B, QW Research $8.64B, Investing.com ~$8.18B — they
disagree, which is itself a reason not to lean on any one of them). **§4.2 requires the affected
line to be at least 10% of total revenue. This is off by roughly two orders of magnitude.
REJECTED on part 2.**
**3. Timing window:** Deliveries run **2027–2036**, and the deal is **not yet executed** —
Lithuanian national-security review and corporate approvals are outstanding. Nothing lands in
reported results within two quarters. **Fails §4.3 independently.**
**4. Invalidation:** Not reached — parts 2 and 3 both failed first.

**Hard filters:** run for the record, after the thesis had already failed —
- Priced-in (§4): **−1.72%** over last 5 sessions (55.585 → 54.63) → `priced_in: false`, "passes"
- Correlation (§4): no open satellite positions → pass
- Universe (§3): us_equity, NYSE, market cap **~$34.5B** (source: Perplexity, citing MarketBeat
  $34.47B and StockMarketCap.io $34.51B, early Sept 2026) → pass

**Outcome: REJECTED — part 2 on magnitude, part 3 on timing.** **This is the cleanest rejection
this log has produced, and the reason is that the numbers existed.** EQT passed every hard filter
— price, correlation, universe — and produced a one-sentence mechanism that needs no "and"
clause. On the pattern of the last two weeks, that is exactly the profile that has been surviving
to the point where it takes judgment to kill. **It did not take judgment. It took division.**

**Honest note, because this is the useful part.** A ten-year LNG offtake agreement with a
sovereign-linked European buyer *sounds* material, and the words "long-term," "2027–2036" and
"Henry Hub-linked" all carry weight that the volume does not. **I had the shape of a favourable
write-up in mind before I converted TWh to Bcf.** The conversion is what ended it. **The general
lesson is worth more than the instance: when a source describes a contract in units the company
does not report in — TWh against Bcfe, miles of fiber against segment dollars — convert first and
write second.** That ordering is what §4 means by applying the filters before constructing the
story, and it applies to part 2 just as much as to the price filters.

---

### T-2026-09-10-04 — LEU — REJECTED
**Company A / the news:** **Centrus Energy** announced a **multi-year contract with Radiant
Industries** to supply **US-origin HALEU** for Radiant's **Kaleidos microreactors**, with
**customer prepayments** supporting Centrus's domestic enrichment build-out and deliveries
**"expected to begin before the end of the current decade."** Source: Centrus announcement via
TipRanks, **2026-09-09**.
**Company B / the candidate:** Centrus Energy.

**1. Mechanism (one sentence):**
> The Radiant contract causes Centrus's HALEU revenue to improve because Radiant has committed to
> buy enrichment output from Centrus and is prepaying against it.

**2. Dollar path:** **Cannot be written. No contract value, no volumes, no prepayment amount is
disclosed by any source.**
**3. Timing window:** Deliveries **"before the end of the current decade"** — i.e. by 2029/2030.
**Fails §4.3 by years, not by quarters.**
**4. Invalidation:** Not reached.

**Hard filters:**
- Priced-in (§4): **+7.76%** over last 5 sessions (168.37 → 181.44) → **FAIL, `priced_in: true`,
  "LATE - skip"**
- Correlation (§4): no open satellite positions → pass
- Universe (§3): us_equity, NYSE American, market cap **~$3.4–3.78B** (source: Perplexity, citing
  MarketBeat $3.78B on 09-08 and CNN Markets $3.40B) → **FAIL, below the $10B floor**

**Outcome: REJECTED — §3 universe (below the $10B floor), §4 priced-in (+7.76%), part 2
(unquantifiable), part 3 (end of decade). Four independent failures, and §3 alone would have
been enough.** Centrus is also the **announcing party and named beneficiary** — Radiant is
private, so there is no second-order surface here at all: the only listed company in the
transaction is the one issuing the press release. Logged in full rather than dropped in a line
because HALEU and microreactors are exactly the kind of story that reads as an early-innings
theme, and **a §3 floor breach is not a judgment call that a good story can outweigh.**

---

### T-2026-09-10-05 — TBBK / CASH / GDOT / CCB — REJECTED
**Company A / the news:** **Chime Financial (Nasdaq: CHYM)** agreed on **2026-09-09** to acquire
its long-time partner bank **Stride Bank, N.A. for $590M in cash**, converting the fintech into a
chartered bank; Stride will be renamed Chime Bank and become a wholly-owned subsidiary.
**Company B / the candidate:** The listed banking-as-a-service sponsor banks whose business model
is exactly the arrangement Chime is exiting — The Bancorp, Pathward, Green Dot, Coastal Financial.

**1. Mechanism (one sentence):** Not written as a *buy* mechanism, and the reason is the sign.
Chime internalising its charter **removes** sponsor-bank economics from the market and is
**negative** for the group — the read-across runs the wrong way for a long-only book. The market
agrees: **TBBK set a new 52-week low on 09-10**, and a French-language wire item explicitly
frames it as *"Bancorp shares fall as its partner Chime prepares to buy Stride Bank."*

**Hard filters:**
- Universe (§3): **all four are far below the $10B floor.** **TBBK ~$2.0–2.8B** (MarketBeat
  $2.04B at the 52-week low 09-10; $2.73B on 09-05; GuruFocus $2.72B), **CASH ~$1.68–1.89B**
  (MarketBeat $1.72–1.73B; AltIndex $1.68B on 09-09), **GDOT ~$0.76B** (TrendMatrix),
  **CCB ~$0.70–0.80B** (MarketBeat $725.2M on 09-10; Morningstar $711.7M; Macroaxis $704.7M).
  Source for all: Perplexity, citing the vendors named. → **FAIL, categorically**
- Priced-in (§4): not run — §3 already disqualifies the entire group.

**Outcome: REJECTED — §3 universe, on every candidate in the set, and the mechanism points the
wrong way regardless.** This is the second time in two sessions that a well-sourced,
correctly-identified second-order effect has been **real, immediate and untradeable**: the effect
is visible in the tape (TBBK at a 52-week low the day after the announcement), the causal chain is
short and needs no "and" clause, and **every affected company sits below the §3 floor while the
sign is negative and this book has no short.** Logged so the disposal is visible rather than
silent — **identifying a second-order effect correctly and being unable to act on it is a
different outcome from finding nothing, and the log should distinguish them.**

Noted and not pursued: **CCB fell ~43% around 09-04/09-07 on "banking services issues" and is
under a securities-fraud investigation** (GlobeNewswire, 09-04 and 09-07). That surfaced in the
market-cap search, not in today's news window; it is **outside this window**, it is a distressed
single name below the §3 floor, and **a stock that has fallen 43% is not a second-order catalyst.**

---

### T-2026-09-10-06 — (no ticker) — REJECTED
**Company A / the news:** **Bayer** and **Neste** finalized a commercial agreement, announced
**2026-09-09** (Bayer press release), to jointly scale Bayer's **newgold® winter canola** in the
**Southern Great Plains of the US** as feedstock for **renewable diesel and sustainable aviation
fuel**. High-protein meal by-product to be sold into dairy, beef, poultry and swine feed markets.
**Bayer aims to launch newgold® hybrids in fall 2027.** No volumes, acreage or financial terms
disclosed; one round-up states plainly that **"financial terms and a start date were not
disclosed."**
**Company B / the candidate:** **None could be identified.** This was screened specifically
*because* both named parties are foreign issuers (Bayer: Frankfurt; Neste: Nasdaq Helsinki) —
which is the structural shape §4 wants, since the headline names are ineligible and any
beneficiary would by construction be a third party.

**1. Mechanism (one sentence):** Not written — **there is no Company B to write it about.** A
dedicated Perplexity screen asking which US-listed companies sources tie to *this specific
agreement* returned: no US-listed company named as a revenue beneficiary, as a cost-exposed
party, or as a member of the **"newgold® network"** of value-chain partners, whose identities
Bayer explicitly does not disclose.
**3. Timing window:** Even setting Company B aside — **hybrid launch is fall 2027**, and feedstock
deliveries follow the launch. **Fails §4.3 outright.**

**Hard filters:** none run. **No ticker reached the stage of needing one.**

**Outcome: REJECTED — no Company B exists in any source, and part 3 fails independently.** The
screen was worth running and the null result is worth recording: **this is the one event in
today's window with the right *structure* for a second-order trade — foreign headline names, a
US-domiciled physical supply chain, a named crop and a named region — and it still has no
tradeable name attached.** The temptation here is specific and was declined: US crop processors
and renewable-diesel refiners are obvious candidates to *guess* at, and the phrase "additional
value chain partners" is an open invitation to fill it in. **Bayer deliberately did not name
them. Filling in a blank the source left blank is not research.** Standing rule (v).

---

### 2026-09-09 (08:26 ET) — event survey (funnel, pre-thesis)

Selftest passed all five checks (`trading_enabled: true`, LIVE paper account, equity
$99,460.43). Window screened: **Tuesday's close through Wednesday pre-market (Sept 8–9)**.
Six Perplexity scans (two broad `--recency day`, four sourced second-order screens
`--recency week`), plus fourteen `move --sessions 5` checks. **Five candidates reached ticker
stage; all five rejected. No BUY intent today.**

**The shape of the day, stated first because it is the finding: for once the funnel produced a
genuinely new, well-sourced, US-listed-to-US-listed event — two of them — and the second-order
layer still did not survive.** Both 09-08 announcements are real, dated inside the window, and
confirmed against the companies' own disclosure rather than an aggregator:

- **Qualcomm–Amazon multi-generation custom AI silicon + 1.6T optical interconnect.** Qualcomm
  press release **09-08** plus an 8-K the same day: warrant for **25M QCOM shares at $161.26**
  expiring 2036, vesting against purchases of **up to $60B** of Qualcomm product; Reuters ties it
  to a **$15B data-center revenue target by 2029**. Verified as new to Qualcomm's own disclosure —
  it builds on the 06-24-2026 Investor Day roadmap but is not a restatement of it. **Standing rule
  (iii) satisfied, for the first time this month on an AI-capex item.**
- **Verizon–Corning fiber supply agreement.** Corning press release **09-08**: **80+ million
  miles** of high-density optical fiber and connectivity solutions, **2027–2032**,
  "multi-billion dollar" with terms undisclosed. Both parties US-listed and named.

**And the second-order surface of both was still empty.** That is the useful result, and it has
a specific cause each time, worth separating:

1. **On Qualcomm–Amazon, the value that would have flowed to an outside supplier is in-house.**
   The 1.6T optical piece traces to **Alphawave SerDes and optical DSP IP that Qualcomm already
   owns** (acquired 2025) — confirmed by a Qualcomm executive at the Goldman Sachs conference:
   *"our custom silicon engagement includes Alphawave SerDes, and they have optical connectivity
   products that are also a part of the Amazon agreement."* **I had begun constructing the
   optical-component-supplier thesis before finding this** — Coherent, Lumentum, Fabrinet, Credo
   were on the list and the sentence was half-written. The in-house sourcing is what killed it,
   not the filters. Recording that in the order it actually happened.
2. **On Verizon–Corning, Company B is the announcement.** Corning *is* the named beneficiary, and
   it moved **+11.63%** over five sessions. There is no third party left to be early to.

Items dropped before thesis stage, with reasons:

- **Crude oil near $100/bbl** (Brent, 09-08) on US–Iran escalation, attacks on Iranian tankers
  and Saudi energy sites, Strait of Hormuz risk. **Macro/geopolitical, not a §4 mechanism.** The
  only names reporting attaches are **PBR, EC, YPF, VIST** — all foreign issuers (§3), and all of
  them first-order commodity exposure, which is a bet on the war headline rather than on a
  company whose economics changed. The driver is also reversible on a single headline: the same
  day's Irish Times piece runs *"oil nears $100 as Iran says Hormuz deal with Oman is close."*
  A thesis whose invalidation could arrive by press conference tomorrow is not a two-quarter
  fundamentals thesis. **Not written up as a thesis — recorded here so the omission is not read
  as an oversight.** Logged as T-2026-09-09-05 below for the §3 record.
- **August payrolls +162k vs ~56k consensus, unemployment 4.1%, participation 61.6%; September
  hike odds ~58.4%; 10-year ~4.8%, 30-year ~5.3%; August CPI Friday 09-11.** Macro. No segment,
  no dollar path. Same disposition as 09-08 and for the same reason.
- **Independence Realty Trust / Centerspace $8.1B apartment-REIT merger** (WSJ, 09-09). Both
  parties are the transaction; no third company's revenue or costs change. Rate-sensitive sector
  facing a **rising** 10-year — the read-across, if anything, runs the wrong way for a long book.
- **Sysco mid-term EPS growth target raised to 9–11% from 6–8%, plus a $500M AI target** (09-09).
  Company A guiding on its own results. The "$500M AI target" invites a supplier read-across and
  **the source does not name a single vendor** — the unnamed-counterparty defect that appeared
  three times on 09-08.
- **Caleres FY26 GAAP EPS guidance raised to $2.80–2.95 from $1.44–1.69** (09-09). Own results;
  **CAL is far below the §3 $10B floor** in any case.
- **DOE loan of up to $1.9B to restart NextEra's Duane Arnold nuclear plant** (09-08). NextEra is
  Company A. No US-listed supplier is named for the restart scope, and a 2020-shuttered plant
  restart is multi-year — outside §4.3 before any thesis is attempted.
- **NLC India 200 MW wind award; Johnson Matthey H1 results** (09-08/09). Not US-listed (§3).
- **Core & Main Q2 earnings preview** (09-09) — analyst estimates, not an event.

**Carry-forward closed: the BSX/MDT/ABT item does not reopen, and the reason matters.** `state.md`
correctly flagged that from **09-09 the five-session window finally contains the 09-08 Boston
Scientific recall**, and it now does: **MDT +1.90% (`priced_in: false`, "passes")**, ABT −4.37%,
BSX −6.84%. **This changes nothing, because MDT and ABT were rejected on part 2 — neither company
discloses neuromodulation or SCS revenue at a grain that lets a dollar path be written — and a
new price window does not create a disclosure that does not exist.** Re-running the filter and
treating a "pass" as a reason to revisit would be looking for permission to revive a thesis that
died on a different test. Filters re-run for the record only; **no thesis re-opened.**

---

### T-2026-09-09-01 — QCOM — REJECTED
**Company A / the news:** Qualcomm and Amazon announced a multi-generation collaboration for
custom AI inference silicon and 1.6T optical connectivity for AWS data centers — Qualcomm press
release and 8-K, **2026-09-08**; warrant for 25M shares at $161.26 vesting against up to $60B of
purchases (Reuters, CNBC, 09-08).
**Company B / the candidate:** Qualcomm itself.

**1. Mechanism (one sentence):**
> The Amazon agreement causes Qualcomm's data-center segment revenue to improve because Amazon
> has committed to purchase up to $60B of Qualcomm silicon against a vesting warrant.

**2. Dollar path:** Data-center/AI infrastructure. Reuters cites a **$15B data-center revenue
target by 2029** against FY25 total revenue of roughly $44B — comfortably over the §4.2 10% floor,
though Qualcomm does not yet report this as a standalone segment with a disclosed share.
**3. Timing window:** Management commentary points to revenue beginning in the **December 2026
quarter** → within two quarters. Passes §4.3.
**4. Invalidation:** Qualcomm's Q1 FY27 (December quarter) results show no data-center revenue
line or disclose data-center revenue below $200M.

**Hard filters:**
- Priced-in (§4): **+2.70%** over last 5 sessions (169.51 → 174.08) → **technically passes**
- Correlation (§4): no open satellite positions, no drivers to collide with → pass
- Universe (§3): us_equity, NASDAQ, market cap ~$190B → pass

**Outcome: REJECTED — §4, "you are not chasing the headline name."** Every part of the thesis is
writable and all three hard filters pass, which is exactly why this entry exists. **Qualcomm is
Company A.** The strategy is *"news breaks about Company A; you look for Company B."* A thesis
whose Company B and Company A are the same company is not a second-order thesis; it is buying the
press release, and §4 forbids it independently of how good the numbers look.

**⚠ And the priced-in filter is actively misleading here — a new defect shape, the mirror of the
LITE one.** QCOM closed **+3.15% on the event day itself** (168.76 → 174.08) after **gapping to
180.46 and touching 183.44 intraday, i.e. +8.7%**, then fading all day. Because the preceding four
sessions drifted *down*, the net five-session move is only **+2.70%** and the filter returns
`priced_in: false`. **A filter whose purpose is to detect that the market already reacted returned
"passes" on a stock that rose 9% on the news six hours ago.** A prior drawdown can absorb an event
pop and hide it. This is the same root cause the human already has flagged for LITE — *the filter
measures a price window, not a relationship to an event* — arriving from the opposite direction.
**The agent does not reinterpret the filter; this goes to the human with the other two.** It cost
nothing today because §4's headline-name rule rejected the name anyway, but on a genuine
second-order candidate it would have waved through a stock that had already moved.

---

### T-2026-09-09-02 — FN / COHR / LITE / CRDO — REJECTED
**Company A / the news:** Qualcomm–Amazon 1.6T optical interconnect component of the 09-08
agreement.
**Company B / the candidate:** Optical component and module makers — Fabrinet (contract
manufacturer), Coherent, Lumentum, Credo.

**1. Mechanism (one sentence):**
> The Qualcomm–Amazon 1.6T optical interconnect build-out causes Fabrinet's optical
> communications revenue to improve because Fabrinet contract-manufactures the transceiver
> modules that Qualcomm's optical DSPs ship inside — **and** Amazon will source those modules
> externally, **and** Fabrinet will win a share of them.

**2. Dollar path:** **Could not be written.** No source quantifies any module volume attributable
to this agreement, and Amazon's existing 1.6T optics purchasing continues regardless of it, so the
*incremental* revenue is not separable from the baseline.
**3. Timing window:** Alphawave 1.6T mass production is cited as 2026–2027; module-level
attribution later and undated. Not establishable.
**4. Invalidation:** Not reached.

**Hard filters:** run for the record, after the mechanism had already failed —
- Priced-in (§4): **COHR +8.64%**, **LITE +7.01%**, **CRDO −25.74%** → all `priced_in: true`;
  **FN +0.83%** → passes. Fabrinet is us_equity, NYSE, ~$15B → §3 clear.
- Correlation (§4): no open satellite positions → pass

**Outcome: REJECTED — part 1, and part 2 independently.** The mechanism sentence needs **two**
"and" clauses to stand up, which §4 names as the exact signature of a link too weak to trade.
Underneath that: **no source connects any of these four companies to this agreement**, and the
1.6T optical work traces to **Alphawave IP Qualcomm owns outright** — so the piece of the deal I
was reaching toward as a supplier opportunity is precisely the piece Qualcomm internalised. That
Fabrinet is the dominant optical contract manufacturer is a **fact about an industry, not a
transaction** — standing rule (v), the CLF failure mode, third appearance in seven sessions.

**Honest note: FN was the one that survived the filters, and that is what made it dangerous.**
+0.83% over five sessions on a day the optical complex ran reads as "the market hasn't noticed
yet." It is at least as likely to mean there is nothing to notice. **A clean priced-in number is
not corroboration of a mechanism that has none.**

---

### T-2026-09-09-03 — GLW — REJECTED
**Company A / the news:** Verizon–Corning multi-year, multi-billion-dollar supply agreement for
**80+ million miles** of high-density optical fiber, **2027–2032** — Corning press release,
**2026-09-08**.
**Company B / the candidate:** Corning.

**1. Mechanism (one sentence):**
> Verizon's 80M-mile fiber commitment causes Corning's Optical Communications revenue to improve
> because Verizon has contracted to buy that fiber from Corning through 2032.

**2. Dollar path:** Optical Communications is Corning's largest segment — roughly a third of total
revenue — so §4.2 materiality is not the problem. **The contract value is undisclosed**
("multi-billion dollar" is the only quantifier any source carries), so the magnitude cannot be
sized.
**3. Timing window:** Supply runs **2027–2032**. Nothing lands in reported results within two
quarters → **fails §4.3** on its own.
**4. Invalidation:** Would have been: Corning's Q1 2027 Optical Communications revenue flat or
down year-over-year.

**Hard filters:**
- Priced-in (§4): **+11.63%** over last 5 sessions (148.70 → 166.00) → **FAIL, `priced_in: true`**
- Correlation (§4): no open satellite positions → pass
- Universe (§3): us_equity, NYSE, market cap ~$140B → pass

**Outcome: REJECTED — §4 priced-in (+11.63%), part 3 (2027–2032 is beyond two quarters), and §4's
headline-name rule.** Three independent failures. Corning is a **named party to the announcement**,
not a second-order beneficiary of it — the same disqualification as QCOM above, and the market
priced it the same session. **This is the cleanest rejection of the run and required no judgment.**

---

### T-2026-09-09-04 — MTZ — REJECTED
**Company A / the news:** As T-2026-09-09-03 — Verizon's 2027–2032 fiber deployment.
**Company B / the candidate:** MasTec — specialty engineering and construction contractor for
telecom networks. (Dycom and Quanta screened alongside.)

**1. Mechanism (one sentence):**
> Verizon's 80M-mile fiber deployment causes MasTec's Communications segment revenue to improve
> because Verizon outsources fiber engineering and installation to specialty contractors — **and**
> MasTec is among Verizon's contractors, **and** MasTec wins a material share of this program.

**2. Dollar path:** **Could not be written.** No source discloses Verizon's share of MasTec
revenue; the Communications segment does not break out customer concentration in anything I could
source. Without that, the segment share of total revenue cannot be tied to this program at all.
**3. Timing window:** Fiber supply begins **2027**; construction awards follow. Two quarters from
today ends at Q1 2027 results → **fails §4.3**.
**4. Invalidation:** Not reached.

**Hard filters:**
- Priced-in (§4): **MTZ +2.64%** → passes. (**DY +4.11%** → `priced_in: true`; **PWR +5.32%** →
  `priced_in: true`.)
- Correlation (§4): no open satellite positions → pass
- Universe (§3): us_equity, NYSE, market cap **~$19.4B** (source: Perplexity, citing
  companiesmarketcap.com and an industry market-cap table dated 09-03-2026) → pass

**Outcome: REJECTED — parts 1, 2 and 3, all three.** **No reporting names any construction
contractor for this program** — the Verizon and Corning releases describe a *fiber supply*
agreement and nothing else. MasTec being one of the largest US telecom contractors is again an
**industry fact, not a transaction** (standing rule (v)). The timing failure is the **CAT failure
mode exactly**: a real, named, well-sourced event whose effect on the candidate lands well beyond
the two-quarter horizon.

**⚠ This is the third time in seven sessions that the funnel has produced a candidate that passed
every hard filter and died on the four-part thesis** (CAT 09-08, MTZ today, and FN above on the
mechanism alone). **The filters are not what is stopping this book from trading — the thesis test
is**, and specifically parts 2 and 3. Recording the pattern rather than the instance, because it
is the one the human needs to see: the funnel keeps finding events that are genuinely new and
genuinely large, whose benefit to any tradeable second-order name is either **unquantifiable** or
**arrives in 2027**.

---

### T-2026-09-09-05 — PBR / EC / YPF / VIST — REJECTED
**Company A / the news:** Brent crude near **$100/bbl** (09-08) on US–Iran escalation, attacks on
Iranian tankers and Saudi energy sites, and Strait of Hormuz transit risk.
**Company B / the candidate:** The upstream producers reporting attaches to the move.

**1. Mechanism (one sentence):** Not attempted as a second-order link — higher crude lifts a
producer's realized price, which is **first-order commodity exposure**, not a case of one
company's economics changing because of another's news.

**Hard filters:**
- Universe (§3): **PBR, EC, YPF, VIST are all foreign issuers** (Brazil, Colombia, Argentina,
  Mexico) → **FAIL**. No US-listed producer was named by any source in the set.
- Priced-in (§4): not run — §3 already disqualifies.

**Outcome: REJECTED — §3 universe, and no §4 mechanism exists to test.** Logged so that the
largest price-moving story of the window is visibly present in the funnel and visibly disposed of.
**A commodity-price bet driven by a geopolitical headline that can reverse at a press conference
is not a two-quarter fundamentals thesis**, and the strategy has no rule that would have caught
it after entry except the −7% hard stop.

---

### 2026-09-08 (08:24 ET) — event survey (funnel, pre-thesis)

First live session after the Labor Day weekend, so the window screened is **Friday's close
through Tuesday pre-market (Sept 4–8)**, not one overnight. Four Perplexity scans: two broad
(`--recency day`), two sourced second-order screens (`--recency week`), plus one segment/universe
check. **Four candidates reached ticker stage with a thesis entry; all four rejected. No BUY
intent today.**

**The shape of the day, stated before the list because it is the finding: the tape had already
moved.** The dominant story was AI compute capacity, and every name with a sourced link to it
failed the §4 priced-in check by a wide margin — **HUT +17.79%, IREN +26.08%, BE +20.04% over
five sessions**, against a 4% threshold. Not one of the three was a marginal call. The second
finding is narrower and more useful: **the headline number of the week is not a new event.** The
"$517 billion / 14.8 GW of Anthropic compute contracts" figure that led Sunday and Monday's
coverage is, per every source that carries it (Chosun Biz 09-07, Seoul Economic Daily 09-07 and
09-08, The Decoder 09-07), an **aggregation by *The Information* on 09-06 of deals signed over
the preceding eleven months** — Amazon and Google/Broadcom from May, the $30B Azure commitment
and the SpaceX Colossus lease reported 09-02, Lambda 09-02. **A re-aggregation of old
announcements arrives in the `--recency day` window looking exactly like a new event.** That is
standing rule (iii) — *verify the news is new to the company's own disclosure* — appearing in a
form the recency filter cannot catch, because the *article* is genuinely new.

Items dropped before thesis stage, with reasons:

- **Anthropic $517B / 14.8 GW compute contracts** (The Information via multiple outlets, 09-06
  to 09-08). Aggregation, not an announcement — see above. The named counterparties (**AMZN,
  GOOGL, MSFT, NVDA**) are the headline names in the story, not second-order beneficiaries, and
  each deal was announced months ago.
- **Anthropic–Nscale Monarch Compute Campus, Mason County WV** — $45B over six years, 460 MW,
  first reported **09-04**. **The one genuinely new contract in the window.** Nscale is a
  private British company (§3). Screened for named US-listed suppliers → produced **CAT**, which
  got a full thesis below.
- **Anthropic–Lambda / Hut 8 (HUT)**, 350 MW Texas site. Hut 8 is explicitly named by Yahoo
  Finance as the **developer** of the site — a genuinely sourced relationship, not a
  read-through. **Died on the priced-in check: +17.79% over five sessions.** Reported 09-02, so
  it was already two sessions stale when it reached this funnel. **Recording that this one had a
  real mechanism and was lost to timing, not to weak sourcing** — that is a different failure
  from the usual one and worth separating in the log.
- **IREN Sweetwater 2 GW ERCOT conditional base-load status** (09-08). IREN is Company A
  announcing its own project. **+26.08% over five sessions.** No US-listed supplier named.
- **OpenAI–Firmus, two Malaysian data centers, >900 MW contracted** (09-08). **Firmus is
  private**; the sites are in Malaysia; Nvidia appears only as an investor in Firmus, which is
  not a supply relationship to these sites.
- **Bloom Energy / Oracle 1.2 GW (up to 2.8 GW)** capacity contract, surfaced in a 09-06
  article. **Both parties US-listed and named — the rarest thing in this funnel — and it was
  still dropped**, because the source describes an existing partnership's progress and **does
  not date the contract announcement inside the window**. BE is also **+20.04%** over five
  sessions. Standing rule (iii) again.
- **August payrolls +162k vs +56k consensus; unemployment ~4.1%; September hike probability
  ~58%; $14.5B Treasury buyback launched 09-07; August PPI Thursday and CPI Friday; FOMC
  09-15/16.** Macro. No segment, no dollar path, no §4 mechanism. This is the single largest
  price-moving item in the window and it is **not actionable under this strategy** — noting that
  explicitly, because "the payrolls print was strong so cyclicals benefit" is the macro-shaped
  version of the read-across failure.
- **Boston Scientific Class I recall + guidance cut** (09-08). Real second-order structure —
  screened properly, produced MDT and ABT theses below.
- **Agilent Q3 beat and FY26 raise; ABM Industries FY26 targets raised** (both 09-08). Each is
  Company A reporting its own results. No named counterparty whose economics change.
- **Adobe CEO transition (Narayen → Chakravarthy); NHTSA opens Cybercab investigation; LULU Q2
  revenue miss; DOCU EPS beat** (09-08). Governance, regulatory-investigation and own-results
  items with no sourced second-order counterparty. **LULU is the fourth consecutive session this
  name has appeared and the fourth it has been dropped** — the athletic-apparel share-shift
  sentence remains the most fluent unsourced sentence available on this tape.
- **Novartis HARBOR Phase III update** (09-08) — **not US-listed** (§3), and the snippet does
  not even state whether the readout was positive.
- **Eli Lilly Mounjaro cardiovascular-risk indication** — surfaced in a 09-08 article, but **no
  source in the set dates the FDA decision inside the window**. Company A in any case.
- **Modular Medical PBM contract, Lifecore/global pharma CDMO transfer, AsiaStrategy credit
  facility** — in all three the **counterparty is unnamed in the source**. Same defect as the
  09-04 Caltrain item, three times in one window.
- **FingerMotion/Lyken/BlueFlare** (non-binding MOU, explicitly no definitive agreement),
  **Tamboran/Liberty Energy** (ASX-listed announcer, 09-02), **HMM/Vale** (Korean and Brazilian).
  §3 or out of window.

---

### T-2026-09-08-01 — CAT — REJECTED
**Company A / the news:** Anthropic committed **$45B over six years for 460 MW** at **Nscale's
Monarch Compute Campus**, Mason County, West Virginia, first reported **2026-09-04**. Sources
describing the site state it will run on an **on-site microgrid of Caterpillar natural gas
generator sets and fast-response turbines plus battery storage**, rather than a conventional
grid interconnection, with **service beginning late 2027**.
**Company B / the candidate:** Caterpillar Inc. (CAT) — named explicitly as the equipment vendor
for that site, not inferred from industry position.

**1. Mechanism (one sentence):**
> Anthropic's Nscale Monarch campus building a 460 MW on-site gas microgrid causes Caterpillar's
> Power & Energy segment revenue to rise because the campus buys its prime-power generator sets
> and turbines directly from Caterpillar.

Part 1 is writable in one clause with no "and also", and — unusually for this log — it rests on
a **named vendor at a named site**, not on a market-structure fact. This is the CLF/RTX failure
mode *not* recurring. It is the strongest part 1 written since T-2026-09-03-01.

**2. Dollar path:** Segment is **Power & Energy** (formerly Energy & Transportation): **$32.2B
of $67.6B FY25 revenue, ~47.6% of total** — comfortably above the §4.2 10% floor. **But the
floor is not the test that matters here.** 460 MW of gensets is on the order of a few hundred
million dollars of equipment spread over a multi-year build, against a segment doing $32.2B a
year and a **company backlog of $72B, up 92% year over year**, of which 59% delivers inside
twelve months. One site is **well under 1% of the segment**. A material segment carrying an
immaterial order is not a dollar path. **FAILS.**

**3. Timing window:** Site service begins **late 2027**. Caterpillar states lead times for gas
reciprocating engines and turbines extend into **late 2028 and beyond**. Two quarters from today
is results reported around April 2027. **Nothing from this site lands inside the §4.3 horizon.
FAILS, and unambiguously.**

**4. Invalidation:** Not reached. Parts 2 and 3 already fail; writing part 4 would be
constructing the rest of a thesis that is already dead.

**Hard filters:**
- Priced-in (§4): moved **+1.77%** over last 5 sessions → **pass**
- Correlation (§4): zero open satellite positions; no driver to collide with → **pass**
- Universe (§3): stock, NYSE, market cap **~$364–374B** (source: Perplexity, citing ad-hoc-news
  09-01 $364.11B and 09-03 $366.34B, MarketScreener 09-05 $374.1B, Trefis 09-03 $364.3B) →
  **pass**

**Outcome:** **REJECTED at parts 2 and 3.** And the reason underneath both is the one worth
recording: **Caterpillar has already told the market this is happening.** On the Q2 2026 call
management said it "continue[s] to anticipate full year growth in power generation for both Cat
reciprocating engines and Solar Turbines driven by increasing energy demand to support data
center build-out," called data centers "a primary driver" for Power & Energy, restarted the
10 MW gas engine platform for ~1.5 GW of capacity, and repurposed a 250,000 sq ft facility in
Wamego, Kansas for data-center power products. **The Monarch order is one line inside a backlog
the market has already been guided to.** What is new here is the customer's name, not the
demand — which is standing rule (iii) exactly. **This candidate cleared every mechanical filter
and had the best-sourced mechanism of the day; it still fails, and the filters are not what
caught it.** Note for a future run: the thing that made CAT attractive — a real named vendor at
a real named site — is also what makes it useless, because a company this size discloses that
demand in aggregate long before any single site matters.

---

### T-2026-09-08-02 — AVGO — REJECTED
**Company A / the news:** The Information's 09-06 compilation of Anthropic's compute contracts,
within which **Google and Broadcom are named as jointly contributing ~5 GW of TPU capacity**.
**Company B / the candidate:** Broadcom Inc. (AVGO).

**1. Mechanism (one sentence):** **Cannot be written in the required form.** The required
sentence is "[event] causes Company B's revenue line to improve because [causal path]" — but
Broadcom **is** the named supplier in the event. It is Company A, not Company B. Writing this as
a second-order thesis would mean claiming that a story about Broadcom's own contract is news
about someone else's economics. **FAILS at part 1 on structure.**

**2–4:** Not reached.

**Hard filters:**
- Priced-in (§4): moved **−2.96%** over last 5 sessions → **pass** (the only AI-complex name
  besides CAT to clear it)
- Correlation (§4): no open positions → pass
- Universe (§3): not reached; no sourced market-cap figure was pulled, since the thesis died at
  part 1

**Outcome:** **REJECTED at part 1.** Logged rather than dropped silently because it is the one
name in the AI complex that passed the priced-in filter, which makes it exactly the candidate a
run under pressure to produce something would reach for. Two independent reasons it is not a
trade: **it is the headline name, and the underlying Google/Broadcom TPU agreement is from
May 2026** — re-reported on 09-06, not announced then. §4: "you are not chasing the headline
name."

---

### T-2026-09-08-03 — MDT — REJECTED
**Company A / the news:** **Boston Scientific**, 2026-09-08, warned it is **unlikely to meet the
Q3 and full-year 2026 net sales growth and adjusted EPS guidance it issued on 2026-07-29**,
alongside an **FDA Class I recall of Infinion CX spinal cord stimulator leads** — fracture risk,
**1,081 serious injuries** reported as of 2026-05-27, no deaths — requiring **immediate
withdrawal of all unused inventory** from point of sale. The recall covers **unused leads only
and does not require explanting implanted leads**.
**Company B / the candidate:** Medtronic plc (MDT), named by market-research sources as one of
three companies dominating spinal cord stimulation, with the Intellis and Inceptiv platforms.

**1. Mechanism (one sentence):**
> Boston Scientific's withdrawal of unused Infinion CX leads causes Medtronic's neuromodulation
> revenue to rise because implanting physicians must substitute a competitor's SCS lead for new
> procedures.

The sentence is structurally clean. **The sourcing under it is not: no source in the set states
that Medtronic gains share because of this recall.** The competitor list comes from a general
August 2026 SCS market report that predates the recall. **This is the Lululemon shape — a
share-shift story where the beneficiary is my inference and not anyone's reporting** — and it is
more seductive here than with Lululemon, because SCS is a genuine three-to-four-player market
where substitution really is close to mechanical. **A narrow market makes the inference feel
like a deduction. It is still an inference.**

**2. Dollar path:** **Not writable. This is the decisive failure.** Medtronic **does not
disclose neuromodulation or spinal-cord-stimulation revenue at all.** The finest disclosed grain
is the **Neuroscience segment at $2.7B for Q1 FY27 (~$10.8B annualized against ~$34B total)**,
and that segment bundles Cranial & Spinal Technologies and other businesses alongside
neuromodulation. SCS is an unquantified fraction of an unquantified sub-line. **I could not
state the segment magnitude or its share of total revenue without guessing at it** — and the
piece I would have to guess is the whole of part 2. **FAILS.**

**3. Timing window:** Would plausibly be inside two quarters, since substitution in new implant
procedures begins immediately. **Not reached — part 2 already failed.**

**4. Invalidation:** Not reached.

**Hard filters:**
- Priced-in (§4): moved **+3.26%** over last 5 sessions → pass, **but see the caveat below**
- Correlation (§4): no open positions → pass
- Universe (§3): stock, market cap **~$120.5B** (source: Perplexity citing Business Quant metrics
  page dated 09-04) → pass

**⚠ The priced-in figure here is measuring the wrong window and a future run must not read it as
clearance.** The recall broke **this morning, pre-market**. The five sessions `move` covers end
Friday and contain **none** of this news. A pass on a filter whose whole purpose is to detect
that the market has already reacted is meaningless when the market has not yet opened on the
event. **Recording this because the number looks like a pass and is not one.**

**Outcome:** **REJECTED at part 2**, with part 1 unsourced. "I could not write part 2 without
guessing at the segment size" is the literal example the log template gives, and it is the
honest answer here.

---

### T-2026-09-08-04 — ABT — REJECTED
**Company A / the news:** As T-2026-09-08-03 — Boston Scientific's Infinion CX Class I recall
and 2026 guidance withdrawal, 2026-09-08.
**Company B / the candidate:** Abbott Laboratories (ABT), named among the SCS leaders via its
Proclaim platform (St. Jude heritage), which received an expanded approval in May 2026.

**1. Mechanism (one sentence):** Same construction as MDT, same defect — **no source names
Abbott as gaining share from this recall.**

**2. Dollar path:** **Not writable, and fails worse than MDT.** Abbott **discloses no
neuromodulation or SCS revenue line**. Against total company revenue of roughly $45B across
diagnostics, cardiovascular, diabetes care, nutrition and devices, any plausible SCS figure is
**low single-digit percent at most — under the §4.2 10% floor** — and I cannot source even that.
**FAILS.**

**3–4:** Not reached.

**Hard filters:**
- Priced-in (§4): moved **−3.69%** over last 5 sessions → pass, **subject to the same caveat as
  MDT — this window predates the news entirely**
- Correlation (§4): no open positions → pass. **Note: had MDT and ABT both somehow survived,
  §4's correlation rule permits at most one — they share the identical driver.**
- Universe (§3): stock, market cap **~$187.4B** (source: Perplexity citing Business Quant metrics
  page dated 09-04) → pass

**Outcome:** **REJECTED at part 2.** Also worth stating plainly: **the recall covers unused
leads only and does not require removal of implanted devices**, so the addressable shift is new
implant procedures using one specific lead — a subset of one product line of one segment of a
company doing $45B a year. **Even a correct thesis here would be immaterial to the buyer.** The
name that would actually be levered to this is a pure-play SCS company; the obvious one,
**Nevro (NVRO), returned `not enough bar history` from `alpaca.py move`** — no usable data, and
it would have failed the §3 $10B floor regardless.

---

### 2026-09-04 (08:27 ET) — event survey (funnel, pre-thesis)

Four Perplexity scans: two broad (`--recency day`), two sourced second-order screens
(`--recency week`), plus one universe check. Roughly fifteen items surfaced. **Fourteen were
dropped before thesis stage**, one reached candidate status with a ticker attached, and it was
rejected three separate ways. **No BUY intent today.**

The shape of the day is worth stating before the list, because it is the finding: **three
separate second-order screens came back explicitly empty.** Not "the candidate failed a filter"
— *no source named a publicly traded US Company B at all.* That happened on the Lululemon
guidance cut, on the Snowflake beat, and on the grid-equipment capacity cluster. When the
sourced answer is repeatedly "none identified," the honest read is that the day's news had no
second-order structure, not that I looked in the wrong place.

The dropped items, with reasons:

- **Lululemon cuts full-year guidance for a second straight quarter; stock −18%** (Reuters
  2026-09-03/04). The largest single-name move in the window and the obvious vehicle for a
  share-shift thesis. **Dedicated screen came back explicitly empty**: no source identifies any
  publicly traded US company as gaining share. The two names sources *do* cite as taking share
  — **Alo Yoga and Vuori — are both privately held** and fail §3 outright. Reuters says only
  that the incoming CEO must win back shoppers from "newer rivals," naming none. The tempting
  move is "LULU guides down, so NKE / DECK / ONON / Gap's Athleta is taking the share" — that
  names no source and is **the read-across failure in its purest form**. Screened for
  deliberately, per the standing carry-forward; came back empty for the third consecutive day
  the screen has been run.
- **Snowflake fiscal Q2 beat and guidance raise** (adj. EPS $0.62 vs $0.45; revenue $1.55B vs
  $1.48B, +35% y/y; FY2027 product revenue guidance raised to $6.07B from $5.84B; stock
  +16.55%). Dropped at part 1 after a **dedicated screen came back explicitly empty**: no
  source names a publicly traded US supplier or partner whose revenue rises as a direct result
  of Snowflake's consumption growth. The available inference — "Snowflake's compute runs on the
  hyperscalers" — is both unsourced and immaterial: Snowflake's entire cost of revenue is a
  rounding error against AMZN/MSFT/GOOGL, so part 2 fails even if part 1 were sourced.
- **Ionis: FDA approves ZANVASTRO (zilganersen) for Alexander disease** (2026-09-03), the first
  and only approved treatment. IONS is Company A and self-commercialises in the US. The only
  named second-order party is **Recordati S.p.A. — Italy-listed, fails §3's US-listed test**,
  which holds ex-US rights under a June 2026 deal ($30M upfront, tiered royalties to the
  mid-20% range). It would fail two more ways regardless: William Blair models **$295M peak
  *global*** sales against Recordati revenue of roughly €2.3B (**well under the §4.2 10%
  floor**), and Recordati's European and Japanese submissions are **expected in 2027** — no
  reported revenue inside two quarters (§4.3). No CDMO or drug-substance supplier is named by
  any source.
- **Nscale–Figure multi-year compute partnership, $3.5B** (2026-09-04) — the only item in the
  window with both a named counterparty and a dollar figure. **Both companies are private.** No
  US-listed second-order name is identified by any source.
- **Grid/electrical capacity cluster: Eaton $242M (North Little Rock, doubling enclosure
  capacity), Siemens >$200M (two new US plants), Southwire $256M (Starkville MS), HSP US >$60M
  (Charlotte NC bushings), Niagara Power Transformer $71M (Cheektowaga NY, 90→140 units/yr)**.
  The most concrete capacity announcements of the day. Eaton is Company A announcing its own
  capex; Siemens is not US-listed; Southwire, HSP US and Niagara are private. Worked as
  T-2026-09-04-01 below on the one US-listed supplier name that surfaced.
- **AEVEX Corp doubles Tampa manufacturing capacity** (2026-09-03) — private defense company,
  no supplier or partner named, no capex or revenue figure.
- **Curia Global $200M Albuquerque fill-finish expansion** (2026-09-03) — private CDMO. No drug
  sponsors, no glass or component suppliers named, capex and capacity metrics only.
- **Calumet Electronics UHDI PCB facility, Michigan** (2026-09-03) — Calumet is private. The
  same article references **TTM Technologies'** Syracuse UHDI plant, but that opened in **June
  2026** — three months stale, not a catalyst in this window, and no contract value or guidance
  change attaches to it.
- **Cipla USA / Qilu Pharmaceutical exclusive licence for a Keytruda biosimilar (QL2107)**
  (Reuters 2026-09-03). Cipla is India-listed, Qilu is Chinese and private. The only US-listed
  party is **Merck, and the mechanism runs against it** — a biosimilar entrant is a negative for
  the originator, and §3 leaves this book long-only. Financial terms undisclosed; biosimilar
  launch timing is years out regardless.
- **LG Energy Solution / Smackover Lithium 10-year lithium feedstock agreement** (2026-09-04).
  LGES is Korea-listed. Smackover Lithium is a JV whose US-listed parent, Standard Lithium, is
  far below the §3 $10B floor. No tonnage, pricing or contract value disclosed.
- **UpSolv / NexKemia long-term recycled polystyrene supply agreement** (2026-09-03) — both
  private, no volumes, pricing or term disclosed.
- **Unusual Machines / Altana supply-chain-intelligence partnership** (2026-09-03) — UMAC is far
  below the §3 floor, Altana is private, no financial terms.
- **Caltrain JPB five-year on-call environmental services agreement** (2026-09-03) — the
  consultant's name is **left blank in the source document** and no dollar value is given. There
  is no candidate here to name.
- **Modular Medical FDA clearance, Pivot patch pump software** (2026-09-04) — sub-$10B, no
  supplier or partner named, no contract value or guidance change.
- **Macro: ISM services 55.4 (from 54.1), new orders at a 3.5-year high, input prices highest
  since October 2022; jobless claims 206k; August payrolls consensus +56k with the report due
  today; Fed Governor Waller's remarks easing rate-hike fears.** All macro, no segment, no
  dollar path to a single name. The ISM input-price detail is an *inflation* signal, and this
  book has no long second-order candidate in a rising-input-cost print.
- **"Nvidia to acquire Hugging Face for $13B, closing 2027"** reappeared in the `--recency day`
  window. **Already rejected on prior runs** as unsigned talks; the item is now reported as a
  deal but is thinly sourced (a news-brief summary, not a filing) and **closes in 2027**, which
  is outside §4.3 by itself. Listed only because it resurfaced, not because it was
  reconsidered. Not re-litigated.

**Nothing from the standing watch-list re-entered the funnel.** LITE, MU and LHX were not
surfaced by any of today's scans and their filters were **not** re-run. As on previous runs, the
reason is *absence of evidence today*, not resolve — if a future funnel surfaces one from a
source, the filter gets re-run and the timing window re-tested from that day's date.

---

### T-2026-09-04-01 — CLF — REJECTED

**Company A / the news:** A cluster of US electrical-equipment capacity expansions reported
2026-09-03/04: **Eaton $242M** in North Little Rock AR to double electrical-enclosure capacity;
**Siemens >$200M** for new plants in Pendergrass GA and Grand Prairie TX; **Southwire $256M** in
Starkville MS; **HSP US (Trench Group) >$60M** transformer-bushing plant in Charlotte NC;
**Niagara Power Transformer $71M** in Cheektowaga NY, lifting output from 90 to 140 transformers
a year, **completing by 2028** (renewableenergyworld.com; g-enews summary).
**Company B / the candidate:** Cleveland-Cliffs — surfaced because a broad industry source
states it is **the only domestic producer of grain-oriented electrical steel (GOES)**, the
material every one of those transformer lines consumes.

**1. Mechanism (one sentence):** **COULD NOT BE WRITTEN HONESTLY.** The sentence I wanted was
*"the US transformer capacity buildout causes Cleveland-Cliffs' electrical steel revenue to rise
because Cliffs is the only domestic GOES producer."* **No retrieved source ties Cleveland-Cliffs
to any of these five projects, or to any named transformer manufacturer as a supplier.** The
sourced claim is a *market-structure* fact — sole domestic producer — not a supplier
relationship. Being the only domestic producer of an input does not establish that a given
buyer buys domestically; GOES is imported at scale, which is precisely why the sole-domestic-
producer line gets written in the first place. To get from the sourced fact to the mechanism I
have to supply the link myself, and **that is the RTX failure exactly** (T-2026-09-01-03), where
I knew Raytheon builds Patriot radar and no source connected it to the actual procurement.

**2. Dollar path:** **ALSO FAILS, independently.** Perplexity searching CLF's most recent 10-K
and 10-Q found **no disclosed revenue or dollar breakdown for GOES or the electrical steel
product line at all.** Cliffs does not report it separately. §4.2 requires a segment I can name
and a magnitude I can size against total revenue; I have neither, and I am not going to assume a
share because it would clear the 10% bar. This is the same wall T-2026-09-01-01 (NOC) hit.

**3. Timing window:** **ALSO FAILS.** These are *capital projects*, not orders. Niagara's
expansion "completes by 2028"; the Eaton, Siemens and Southwire plants are multi-year builds.
Steel purchased to equip and then run a plant that finishes in 2028 does not appear in a
supplier's reported results inside two quarters. §4.3 rules it out on its face.

**4. Invalidation:** not reached — parts 1, 2 and 3 all failed.

**Hard filters:**
- **Universe (§3): FAILS.** Market cap **$7.01B as of 2026-09-04** (StrongBuyAnalytics, dated
  point estimate; corroborated by MarketBeat at $6.99B on 09-02 and $7.05B in August, and by
  GuruFocus/MarketScreener in the mid-$6B to low-$7B range through August). **Below the $10B
  floor.** `alpaca.py buy` would have refused the order.
- **Priced-in (§4): not run, deliberately.** The mechanism failed first and §4 orders the
  filters before the thesis. Running `move` on a name with no sourced mechanism is what the RTX
  process note told the next run not to repeat.
- **Correlation (§4):** no open positions → passes vacuously.

**Outcome:** REJECTED four ways — part 1 (no sourced supplier relationship), part 2 (segment not
disclosed anywhere), part 3 (2028 capital projects, not two-quarter revenue), and §3 (market cap
$7.01B, below the floor).

**Why this entry is worth its length despite dying so comprehensively.** It is the only name all
day that reached candidate status, and the way it got there is the thing to watch. The screen
did not hand me a supplier; it handed me **a monopoly fact** — "the only domestic producer" —
and that phrase does most of the work of a mechanism sentence without being one. It implies
inevitability. It is very close to the shape of a real second-order thesis and contains none of
the content, because it says nothing about whether *these* buyers buy from *this* seller.

The useful generalisation, and it is new: **a market-structure fact is not a supplier
relationship.** "Sole domestic producer," "dominant share," "the only company that makes X" are
all facts about an industry, not about a transaction. The RTX rule (verify the link is sourced,
don't supply it yourself) catches this, but only if I notice that I *am* supplying it — and a
sole-producer claim is designed to feel like it removes the need to check. Recording it as its
own failure mode so a future run recognises the phrase rather than re-deriving the lesson.

Also worth noting: **the §3 check killed it independently and would have killed it at the
script.** Four of my last dozen rejections have been US-listing or market-cap failures on names
that reached me through a mechanism screen. The universe filter is doing more work in this log
than the priced-in filter ever has.

---

### 2026-09-03 (08:27 ET) — event survey (funnel, pre-thesis)

**First run under `TRADING_ENABLED: true`.** The human set it in `control.md` at 21:08 PT on
2026-09-02 (commit `1005b1e`, "Enable trading"), i.e. 00:08 ET today. Every prior run in this
repo's history researched under a dry run. **That changes nothing about §4** — the filters and
the honest-broker rule are identical whether or not an order can reach the broker — but it is
worth recording that the first live day produced no BUY intent, because the pressure to
inaugurate a live account with a trade is exactly the pressure §4 exists to resist.

Four Perplexity scans: two broad (`--recency day`), two sourced second-order screens
(`--recency week`). Roughly a dozen events surfaced. **Eleven were dropped before thesis
stage**, one was worked, and it was rejected. The dropped items, with reasons:

- **Broadcom fiscal Q3: beat on revenue and EPS ($29.59B vs $29.36B; adj. EPS $3.32 vs $3.24)
  but weak forward guidance** (CNBC 2026-09-02). Dropped at part 1 after a **dedicated screen
  came back explicitly empty**: no source names any publicly traded US company whose revenue or
  costs change because of Broadcom's guidance. It is also the wrong direction — §3 leaves this
  book long-only, and a weak-guidance print has no long second-order candidate. The tempting
  move is "AVGO guides soft, so a competitor is taking the share" — that names no source and is
  the read-across failure in its purest form.
- **Federal judge rules Google need not divest its adtech business / AdX** (Reuters, NYT,
  Forbes, AdExchanger, 2026-09-02). Dropped at part 1 on two grounds. First, the sourced screen
  names **only Alphabet** — no source names any other public company whose revenue or costs the
  ruling changes; "competitors," "publishers" and "advertisers" appear only generically.
  Second, and more fundamental: **a ruling that preserves the status quo does not change
  anyone's revenue line.** The mechanism available for a rival (Trade Desk, Magnite, PubMatic)
  runs *against* it — they lose an upside they never had — and §4 needs an improvement, not a
  withheld harm. Alphabet itself is Company A.
- **FuelCell Energy: first Capacity Reservation Agreement with a major data-centre operator for
  a planned 75 MW Texas project, plus a capital-equipment agreement with Fit Energy for up to
  380 MW across four phases** (FCEL Q3 FY2026 release, 2026-09-02). Dropped at §3 and part 1.
  FCEL is Company A and is far below the $10B floor; the sourced screen confirms the
  counterparties are **Fit Energy (not US-listed) and an unnamed "major colocation data centre
  operator."** There is no Company B. The reflex here is to jump from "data-centre power demand
  is real" to a large US power or turbine name, which no source connects to this agreement.
- **Dell Q2 FY2027 / the $25B guidance raise.** Already worked and rejected yesterday as
  T-2026-09-02-02 (HPE, part 1 — read-across, not mechanism). It resurfaced in today's window
  because the news cycle is still rolling; **deliberately not re-litigated.** The component
  screen that came back empty yesterday was not re-run, and MU was not re-checked — consistent
  with the standing rule, **today's funnel does not produce it from any source.**
- **Uber cuts ~3,300 jobs (10% of global workforce)** in a restructuring toward ride-share,
  delivery and robotaxi. An internal cost action at Company A. No source names a third company
  whose revenue or costs move; a staffing cut does not become another firm's revenue line.
- **KBR wins a NOAA National Weather Service single-award follow-on, $1.1B ceiling over five
  years, Sept 2026–Aug 2031** (Zacks, 2026-09-02). Company A. No source names a subcontractor,
  and a five-year ceiling is not a two-quarter revenue event (§4.3) even for KBR itself.
- **Studsvik / GE Vernova Hitachi / Samsung C&T commit to advancing a 1.2 GW nuclear project in
  Sweden** (PR Newswire, 2026-09-03). "Commit to advancing" is not an order, the project is
  non-US, and nuclear construction is years from reported results — outside §4.3 by a wide
  margin.
- **Ciena's own print** — the source event for the one worked thesis below. Ciena is Company A.
- **BioLargo / Clyra Medical reseller agreement with Spartan Medical for ViaCLYR** (2026-09-03).
  BioLargo is **OTCQX** — explicitly ineligible under §3 — and no dollar value or term is
  disclosed. Spartan Medical is private.
- **PharmaEssentia BESREMi FDA approval for essential thrombocythemia** (2026-08-31).
  Not US-listed, and the approval predates this window.
- **Macro: ADP private payrolls +38k for August** (vs 47k consensus, prior 46k revised),
  **ISM manufacturing 54.6**, **July construction spending −0.5% m/m**. All three are misses,
  all three are macro with no segment and no dollar path to a single name, and a long-only book
  has no second-order candidate in a softening print. The ISM and construction figures are the
  **same releases already funnelled and dropped on 2026-09-02** — they are listed again only
  because they reappeared in today's `--recency day` window, not because they were reconsidered.

**Tesla's Cybercab event in Austin was scheduled for today** and is pre-event coverage only —
no contract, approval or capacity announcement exists in any retrieved text. Nothing to work.

The one event with genuine second-order structure — **Ciena's fiscal Q3 and guidance raise** —
is worked as T-2026-09-03-01 below.

---

### T-2026-09-03-01 — LITE — REJECTED

**Company A / the news:** Ciena reported fiscal Q3 2026 revenue of **$1.67B, up 37% y/y**, with
adjusted EPS of **$2.11, up 215% y/y**, raised FY2026 revenue guidance to **$6.42B ± $50M** and
guided fiscal Q4 to **$1.75B ± $50M** (Ciena investor release / Business Wire, 2026-09-02). Its
**Optical Networking portfolio was $1,191.3M, 71.3% of Q3 revenue**, up from $815.5M and 66.9%
a year earlier — the growth is concentrated in coherent optical transport and data-centre
interconnect.
**Company B / the candidate:** Lumentum Holdings — named by Morgan Stanley commentary (via
TheStreet) as **one of Ciena's key suppliers**, specifically of the **pump lasers** Ciena uses
in its networking hardware. The same source describes Ciena as **"supply-constrained because
demand is outrunning its ability to source optical components, particularly pump lasers,"** and
reports Lumentum's pump-laser shipments **up more than 80% y/y last quarter with plans to
increase volumes roughly fourfold over the coming quarters.**

**Hard filters — applied before the thesis, per §4, and this is where it ended:**

- **Priced-in (§4): FAIL.** `alpaca.py move --symbol LITE --sessions 5` returns
  **−7.35%** (939.45 → 870.415), `priced_in: true`, `verdict: "LATE - skip per strategy.md
  section 4"`. Over 20 sessions **+5.44%** (825.49 → 870.415), also `priced_in: true`.
- Correlation (§4): no open positions → pass, vacuously. Driver would be **AI/data-centre
  optical interconnect demand** — a driver nothing in this book currently carries.
- Universe (§3): stock, NASDAQ, `tradable: true`, `fractionable: true`, status active — clear
  on venue and class. **Market cap deliberately not sourced.** The candidate was already dead
  on the filter, and sourcing a number that cannot be used is wasted effort — the same
  disposition as T-2026-09-02-01.

**1. Mechanism (one sentence):** *not written as a live thesis — the filter had already vetoed
the trade.* Recorded here only so the human can see what was given up:
> Ciena's optical-networking ramp causes Lumentum's optical-components revenue to rise because
> Lumentum supplies the pump lasers Ciena is supply-constrained on.

One clause, no "and also," a **named** supplier relationship from a source rather than an
assumed supply chain, and a cost-line-becomes-revenue-line shape. **This is the cleanest part 1
this log has produced.** Parts 2–4 were **not** attempted: §4 requires the filters first, and
constructing the dollar path after the veto had fired would be building the story I was already
looking for permission to keep.

**Outcome:** REJECTED on the §4 priced-in filter, −7.35% over five sessions.

**⚠ This is the case the 2026-09-02 log flagged in advance, and it has now actually cost
something — the human needs to decide it deliberately.** Yesterday's entry observed that
`alpaca.py move` tests **absolute** magnitude, so a stock that has *fallen* more than 4%
returns `priced_in: true`, and noted that "a future run could be blocked from a legitimate
candidate that fell 5% on unrelated news." That is precisely what happened here. LITE is
**down** 7.35%; so is Ciena itself, **−12.25%** over the same five sessions, on a quarter that
beat and raised. The five-session window brackets Broadcom's weak guidance and a broad AI-optics
drawdown, so the decline is very unlikely to be the market pricing in Ciena's Q3.

**I have not reinterpreted the filter, and no future run should either.** §4 is a veto; a veto
that fires too often is the safe direction; and "has fallen 7%" is a perfectly good reason for
an agent with my failure modes to stay out of a name it just constructed an attractive story
about. But the cost is now concrete rather than hypothetical, and the fix — if there is one —
is a human editing §4 or the script, not a run deciding at 08:00 that the rule does not mean
what it says.

**The scoreboard this extends:** across nine worked candidates, seven passed the priced-in check
and failed the thesis (NOC, LHX×2, WDC, AEP, RTX, and HPE which died at part 1), and **two now
passed the thesis and failed the filter — MU and LITE.** The filter has still never been
informative about the outcome in the direction people expect it to be. Treat a passing
priced-in check as a veto that did not fire, never as encouragement.

**One more thing worth saying plainly.** Today was the first day this account could actually
transact, and the single worked candidate produced the best-sourced mechanism in the log and
was rejected anyway, on a rule that arguably was not aimed at it. That is the system working.
A first live day that opened a satellite position on a name whose filter said "LATE" would have
been a worse outcome than a first live day that bought only the index.

---

### 2026-09-02 (08:30 ET) — event survey (funnel, pre-thesis)

**One run today, at 08:30 ET.** Yesterday this routine fired three times (00:48, 01:15, 08:56 ET)
and yesterday's carry-forward asked that the schedule item stay open until it fires *once*, at or
near 08:00. Today it fired once, 29 minutes late, inside the pre-market session. That is one clean
day, not a fix confirmed — see `state.md` → Carry forward.

Three broad Perplexity scans (`--recency day`) plus three sourced second-order screens
(`--recency week`). Eleven events surfaced. **Nine were dropped before thesis stage**, two were
worked, and both were rejected. The dropped nine, with the reason, because the funnel is the
output:

- **GE Aerospace, $2.87B US Navy F414 performance-based logistics contract** (DoD contracts list
  2026-09-01; 5-year PBL from Naval Supply Systems Command WSS, 17 F414 components for the F/A-18
  E/F/G). This was the most promising-looking item in the set and it got a dedicated supplier
  screen, which came back **empty and explicitly so**: the award is **sole-source to GE**, and no
  source names any other publicly traded company as an F414 component supplier or a participant.
  Dropped at part 1. **This is the T-2026-09-01-03 (RTX) rule working as intended** — I know
  perfectly well that an engine programme has a supply chain, and I could have written a fluent
  sentence about it. No source names one, so there is no Company B.
- **Nvidia in advanced talks to acquire Hugging Face, ~$14B** ($12.9B consideration + ~$1B
  retention; Bloomberg 2026-09-02, unconfirmed, both parties declined to comment). Dropped at
  part 1 on **two independent grounds**. First, the same reasoning applied to SLB–Kelvion and
  Graco–Valco: an acquisition rearranges the *acquirer's* mix and does not change a third
  company's revenue or cost line. Second, and more basic — **it is not signed.** Bloomberg's own
  language is "a final agreement hasn't been reached and the timing or details could still
  change." Trading an unsigned rumour is not a fundamentals horizon. No source names any
  affected third company; the target is private.
- **NASA awards Blue Origin ~$700M firm-fixed-price Mars communications network contract**
  (NASA blog 2026-09-01). Blue Origin is private. No source names a US-listed supplier. The
  vendor list I could write from general knowledge would be entirely my own inference.
- **ISM Manufacturing PMI 54.6 for August** (vs 55.6 July, 55.2 consensus; new orders 53.7 from
  56.7, employment 51.2 from 52.8) and **July construction spending −0.5% m/m** (vs +0.1%
  consensus). Both macro, both *misses*. §3 leaves this book long-only; a demand-softening print
  has no long second-order candidate. Same disposition as the Chicago PMI on 2026-09-01.
- **JOLTS job openings 7.272M for July** (vs 7.313M consensus, prior 7.182M revised). Macro, no
  segment, no dollar path to any single name.
- **Zepp Health Q2 2026** (revenue $63.5M +6.9%, adjusted net loss $12.5M, Q3 guide $68–73M
  implying −4% to −10% y/y). Fails §3 on size by two orders of magnitude.
- **Enovix doubling in-house drone battery capacity in South Korea by mid-2027** (2026-09-01).
  Company A, not Company B; market cap far below the §3 $10B floor; and mid-2027 is outside
  the §4.3 horizon regardless.
- **Doosan Fuel Cell wins ₩501.4B (~$361M) order from HyAxiom for US data-centre fuel cells**
  (2026-09-02). Doosan Fuel Cell is Korea-listed and HyAxiom is its own US subsidiary — the
  contract is intra-group. No US-listed party. The reflex "US data-centre power demand is real,
  so buy a US fuel-cell name" is a read-across to a *competitor* of the winner, which is the
  opposite of a mechanism.
- **Honda tells suppliers to cut costs in a $9B push** (Reuters, exclusive). Honda is
  Japan-listed, and the only mechanism runs *against* the US auto suppliers on the receiving
  end. Nothing long and eligible.

**Deliberately not re-litigated**, per yesterday's carry-forward: the LG Energy Solution ⇄
Smackover Lithium offtake (funnelled and dropped 2026-09-01 on part-2 arithmetic — it resurfaced
today as a "finalized" 10-year commitment, which does not change the ~0.1%-of-revenue result);
the PAC-3 MSE / THAAD ramp; and the memory-cost cycle. **Northrop Grumman** appeared again today
with contract news and FY2026 EPS guidance of $28.60–29.10 — that makes NOC a Company A talking
about itself, which is what T-2026-09-01-01 already concluded.

**On MU, and this is the entry I most want a human to read.** Yesterday's journal predicted that
today's run would feel a pull to re-run Micron's priced-in check hoping for a friendlier number,
and named that in advance as an inheritance-of-conclusion failure. The pull was real. What stopped
it is not willpower: **MU does not appear anywhere in today's funnel.** No source in any of six
queries names Micron, or any memory supplier, in connection with any of today's events — including
Dell's AI-server guidance raise, where a memory-cost angle is the most natural thing in the world
to reach for and where the sourced screen came back explicitly empty on component suppliers and on
memory-cost commentary alike. So MU was not screened and its filter was not re-run. **The correct
reason not to re-check a rejected candidate is that today's evidence does not produce it, not that
I resolved to be disciplined about it.** If a future run's funnel *does* surface it from a source,
re-run the filter and re-test the timing window from that day's date — that is legitimate, and
different from what almost happened here.

The two events with genuine second-order structure — the **Army TITAN production award** and
**Dell's AI-server guidance raise** — are worked as T-2026-09-02-01 and -02 below.

---

### T-2026-09-02-01 — LHX — REJECTED

**Company A / the news:** The US Army Contracting Command awarded Palantir USG a prime agreement
for production and delivery of **eight TITAN** (Tactical Intelligence Targeting Access Node)
ground stations — the Army's AI/ML-enabled deep-sensing node (Palantir press release via AP/
Business Wire, 2026-09-01; DefenseScoop, 2026-09-01).
**Company B / the candidate:** L3Harris Technologies — **the only publicly traded US company any
source names on the TITAN team.** Palantir's release lists the industry team as Anduril, L3Harris,
Sierra Nevada, Strategic Technology Consulting and World Wide Technology; of those, Anduril, SNC,
STC and WWT are all private.

**1. Mechanism (one sentence):**
> The TITAN production award causes L3Harris's ISR and tactical-communications revenue to rise
> because L3Harris supplies subsystems integrated into the eight ground stations Palantir will
> deliver.

One clause, no "and also," and the teammate relationship is sourced rather than assumed. **Part 1
passes** — and, as with AEP yesterday, it is the only part that does.

**2. Dollar path:** **FAILED, decisively, on magnitude.** DefenseScoop reports that "Palantir,
working alongside L3Harris, Sierra Nevada Corporation, Strategic Technology Consulting and World
Wide Technology, received **$127 million** for the production contract, according to the Army,"
within **$192 million** of combined delivery orders to Palantir and Anduril. Against L3Harris
FY2025 revenue of **$21.865B** (sourced 2026-09-01, T-2026-09-01-02), the **entire $127M** —
before it is split five ways, and before recognising that it is a delivery order, not annual
revenue — is **0.58% of one year's revenue.** L3Harris's own share is unstated by any source and
is necessarily a fraction of that.
The *segment* test passes and is irrelevant: L3Harris's segments run roughly 30–35% of revenue
each, so whichever one houses this clears the 10% floor easily — but §4.2 asks for the **magnitude
of the change**, and 0.58% is not it. **This is the T-2026-09-01-01 (NOC) failure exactly: a
sourced, real, headline-worthy contract that divides down to a rounding error.** It is in fact
worse than NOC, which was ~1.0%.

**3. Timing window:** Not reached — part 2 failed on its own. (Noted for completeness: the sources
give no delivery schedule for the eight systems, so a two-quarter window could not have been
established either.)

**4. Invalidation:** Not reached.

**Hard filters:**
- Priced-in (§4): moved **+0.52%** over last 5 sessions (262.16 → 263.515) → **pass**. Over 20
  sessions **−7.62%** (285.25 → 263.515) → the script returns `priced_in: true` on magnitude.
- Correlation (§4): no open positions → pass, vacuously. **But note the driver is different from
  T-2026-09-01-02**: that was the PAC-3 MSE / THAAD ramp, this is Army TITAN. Same ticker, two
  distinct catalysts, two days running.
- Universe (§3): stock, NYSE, market cap ~$49–54B (source: **inherited** from T-2026-09-01-02,
  Perplexity aggregating MarketBeat / Stockpolly / Barron's / InvestSmart, late-Aug 2026 —
  **not re-sourced today**, because the trade was already dead on part 2 and sourcing a number I
  cannot use is wasted effort). Well above the $10B floor.

**Outcome:** REJECTED on part 2. Magnitude ≤0.58% of annual revenue, and L3Harris's own share of
that is unstated.

**Why this entry earns its place: L3Harris is now the most dangerous name in this log, and the
reason is that it keeps being *almost* right.** In two consecutive days it has produced two
separate, sourced, one-clause mechanisms — PAC-3 propulsion yesterday, TITAN today — and failed
both times on different parts (§4.3 timing, then §4.2 magnitude). Meanwhile the stock sits at
−7.62% over twenty sessions, near a 52-week low, and passes the five-session priced-in check
cleanly at +0.52%.

**That combination is a trap, and yesterday's carry-forward named it before today's run started:**
"a future run will see a cheap defense name with a real missile-demand story and may mistake the
two for the same thing." Today it was a cheap defense name with a real *TITAN* story, which is a
different story, and the warning held anyway. The thing actually moving LHX remains the postponed
Missile Solutions IPO — an event with no relationship to either mechanism I have written. Two
sourced mechanisms attached to a price that is trading on a third thing is not two pieces of
evidence; it is the same substitution twice.

**Standing rule this produces, which is new: when the same ticker surfaces on consecutive days
through different events, treat the recurrence as a warning, not as corroboration.** The natural
reading is "this name keeps coming up, there must be something there." The accurate reading is
that a large diversified prime is *structurally* likely to appear in any defense news cycle, and
appearing is not the same as being materially affected. Each event has to clear §4 on its own
numbers, and today's numbers were an order of magnitude short.

---

### T-2026-09-02-02 — HPE — REJECTED

**Company A / the news:** Dell Technologies reported Q2 FY2027 and **raised full-year guidance on
AI-server demand** — a record **$60.9B of AI server orders** booked in the quarter, a record
**$95.0B AI server backlog** at quarter end, **$16.4B of AI-optimised server revenue (+100% y/y)**,
FY2027 AI-server revenue guidance raised by **$14B** (from ~$60B to ~$74B) and total FY2027 revenue
guidance raised by **$25B** off a prior $165–169B range (Dell 8-K and prepared remarks, CNBC,
Investing.com, 2026-09-01/02). Shares rose 8.5–10% pre-market.
**Company B / the candidate:** Hewlett Packard Enterprise — named by Reuters coverage as rising
~5% pre-market **because** Dell's outlook "improved sentiment around AI infrastructure spending."

**1. Mechanism (one sentence):** **COULD NOT BE WRITTEN HONESTLY.** The only sentence the source
supports is *"Dell's guidance raise causes HPE's share price to rise because investors read across
to HPE's server business"* — and that is a sentence about **sentiment**, not about a revenue or
cost line. §4 requires that Company B's **economics** change. Dell shipping more AI servers does
not increase HPE's revenue; if anything the two compete for the same orders, which points the
wrong way. There is no causal path from Dell's backlog to HPE's income statement.

**2–4:** Not attempted. Part 1 failed.

**Hard filters:**
- Priced-in (§4): moved **−4.96%** over last 5 sessions (53.45 → 50.80) → script returns
  `priced_in: true`. See the note below on what that number actually means.
- Correlation (§4): no open positions → pass, vacuously
- Universe (§3): stock, above the $10B floor → pass (not sourced; the candidate was already dead
  at part 1)

**Outcome:** REJECTED at part 1. This is a read-across, not a mechanism.

**This is the SAIC failure from 2026-09-01, and I want it on the record that it recurred within
24 hours.** Yesterday's funnel dropped "SAIC beats and raises → buy LDOS/CACI/BAH" with the note
that it is "the most tempting shape in today's set" and that *"Company A's print implies Company
B's print" is a correlation dressed as a mechanism, and it is the easiest sentence in the world to
write fluently.* Today the identical shape arrived in a different sector, with a **much** larger
and more impressive set of numbers behind it — $95B of backlog is genuinely arresting — and it was
harder to dismiss precisely because the underlying demand is so obviously real. **The size of
Company A's number has no bearing on whether a mechanism to Company B exists.** A $95B backlog at
Dell is $0 of revenue at HPE.

**A genuine second-order candidate does exist in principle here and I could not source one.** Dell
recognising $16.4B of AI-server revenue means somebody is being paid for the memory, storage,
networking and accelerators inside those racks — that is a real cost line becoming a real revenue
line, which is the cleanest §4 shape there is. So I ran the screen explicitly, asking which
publicly traded US companies sources name as component suppliers benefiting from Dell's ramp, and
what Dell said about memory or storage cost inflation. **Both came back empty**: Dell's release,
8-K and prepared remarks name no component vendor, and contain no commentary on memory/NAND/HBM
pricing, in any retrieved text. Naming Micron, Seagate, Broadcom or Marvell here would have been my
inference and nothing else. That is the RTX rule, and it applies with more force than usual today
because the inferred answer would have been MU — the name I already have a rejected thesis on and
a documented pull toward.

**Worth flagging to the human — an observation about the tool, not an argument against it.**
`alpaca.py move` tests **absolute** magnitude, so it returned `priced_in: true` for HPE (−4.96%)
and DELL (−5.84%) on five-session windows that end at the **2026-09-01 close, before Dell's print**.
Both readings are *drawdowns*, not run-ups. Under §4's wording — "already moved more than 4% over
the last five sessions **on this news**" — a decline that predates the news is not the thing the
rule is aimed at. It made no difference today (HPE died at part 1, DELL is Company A), so nothing
turns on it, and **I am not proposing to reinterpret the filter on my own authority** — §4 is a
veto and a veto that fires too often is the safe direction. But a future run could be blocked from
a legitimate candidate that fell 5% on unrelated news, and that is worth a human deciding
deliberately rather than discovering by accident.

---

### 2026-09-01 (third run, 08:55 ET) — event survey (funnel, pre-thesis)

**Read this header before reading the entry below.** This is the **third** `1-premarket-research`
run for 2026-09-01, after 00:48 ET (`577ff28`) and 01:15 ET (`9d592dd`). Six thesis IDs now carry
today's date across three runs against a rolling news window. That is a scheduling fault, not six
days of research — see `state.md` → Carry forward.

What is different about this run, and why it was worth doing: it fired at **08:55 ET, inside the
pre-market session**, ~55 minutes after the intended 08:00 slot rather than ~7 hours before it.
The two earlier runs did their priced-in checks at 01:00 with a `move --sessions 5` window ending
at the prior session's close and no pre-market tape in existence. This one has both.

**Re-checked, not re-litigated.** Per the carry-forward instruction, the PAC-3 MSE / THAAD ramp
(T-…-01 NOC, -02 LHX, -03 RTX) and the memory-cost cycle (T-…-04 MU, -05 WDC) were **not** reworked.
The overnight scan returned the PAC-3 story again — this time via a `thestreet.com` piece which adds
that the Pentagon release carries **no dollar figure at all** and that funding depends on annual
Congressional appropriations. That makes the §4.3 timing rejection stronger, not weaker. Nothing
about the memory complex changed.

Events already funnelled by the earlier runs and deliberately not reworked: SEC shareholder-proposal
rulemaking, Chicago PMI, Treasury/IRS CFC regulations, US–Iran / oil, NVDA–MediaTek, FTC v. Amazon,
California wildfire bill, SLB–Kelvion, ICE/Cboe–Hyperliquid. **Note on the last of these:** the
California wildfire item resurfaced hard overnight — **EIX fell 23.07%** after the legislature
rejected the cost-recovery proposal. The 00:48 run dropped it as "a negative catalyst with no clean
long beneficiary" and that call stands: a 23% drawdown in a regulated utility is not a long
opportunity in a §3 long-only book, and the obvious "buy the surviving utility" reflex is a
precedent-risk trade, not a dollar path.

Five items surfaced that the earlier funnels did not carry. Four were dropped pre-thesis:

- **LG Energy Solution ⇄ Smackover Lithium (Standard Lithium + Equinor) offtake** — 8,000 t/yr of
  US-produced lithium carbonate over 10 years, announced 2026-08-31. Dropped on **part 2 arithmetic,
  before writing anything.** Standard Lithium is a development-stage junior far below the §3 $10B
  floor. Equinor is the only eligible-sized party, and 8,000 t/yr at any plausible carbonate price
  is order-$100M/yr gross against a revenue base near $100B — roughly **0.1%**, split with a JV
  partner, over ten years. Two §4 tests fail simultaneously and neither is close.
- **Graco completes Valco Melton acquisition, $447M cash.** Dropped at part 1, on the same reasoning
  the 01:15 run applied to SLB–Kelvion: an acquisition rearranges the *acquirer's* segment mix and
  does not change any third company's revenue or cost line. No Company B exists in an M&A close.
- **SAIC beats and raises FY2027 guidance, +8%.** Dropped at part 1, and worth naming because it is
  the most tempting shape in today's set. The reflex is "federal IT demand is strong → buy LDOS,
  CACI, BAH." But SAIC's results do not *cause* anything to change at Leidos. It is a read-across
  about a shared end-market — an information event, not a causal path — and §4 asks for a mechanism
  by which Company B's economics change. "Company A's print implies Company B's print" is a
  correlation dressed as a mechanism, and it is the easiest sentence in the world to write fluently.
- **AstraZeneca Zegfrovy sNDA accepted; Protagonist MIMRYLO approved.** Dropped on §4.3. An sNDA
  *acceptance* precedes any decision by months, and neither event names an affected competitor.
  No timed dollar path inside two quarters.

The fifth — **the Anthropic / Lambda / Hut 8 data-centre deal** — has genuine second-order structure
and is worked as T-2026-09-01-06 below.

**The event:** Anthropic signed a reported **$35B cloud-computing agreement with Lambda**, an
Nvidia-backed cloud provider (WSJ and Reuters, 2026-08-31, sourced to people familiar rather than
company release). The capacity — Reuters puts the initial project at **~350 MW** — sits in a data
centre developed by **Hut 8** in **Nueces County, Texas**, with **Nvidia holding the lease**. Hut 8
disclosed in July a 15-year lease to an "investment-grade customer" with a **$19.6B base-term
contract value**; the FT subsequently identified Nvidia as the tenant of Hut 8's **1 GW Beacon Point
campus**.

This is a clean §4 shape on its face: a very large, dated, physically located commitment where the
named parties are either private (Anthropic, Lambda) or already the headline (NVDA, HUT). The
second-order question is who else gets paid to make 1 GW in Nueces County exist.

**Screened on the mechanism first, per the standing process correction — and the screen came back
almost empty.** Asked explicitly for companies a *source ties to this project*, rather than for
plausible AI-datacentre suppliers, exactly one eligible name survived: **AEP**, via AEP Texas, which
holds the interconnection agreement supplying Beacon Point's gigawatt. **No** source names an
electrical-equipment, cooling, EPC or land counterparty. That absence is itself the useful result:
the vendor list I could have written from general knowledge (switchgear, transformers, chillers)
would have been entirely my own inference, which is the T-2026-09-01-03 (RTX) failure repeated.

---

### T-2026-09-01-06 — AEP — REJECTED
**Company A / the news:** Anthropic's reported $35B cloud agreement with Nvidia-backed Lambda, for
~350 MW of capacity at Hut 8's Beacon Point campus in Nueces County, Texas, with Nvidia as
leaseholder (Reuters / WSJ, 2026-08-31).
**Company B / the candidate:** American Electric Power — the only publicly traded US company any
source ties to the project other than the named parties, via AEP Texas.

**1. Mechanism (one sentence):**
> The Beacon Point buildout causes American Electric Power's Texas transmission and distribution
> revenue to rise because AEP Texas holds the interconnection agreement supplying the campus's
> full gigawatt of utility capacity.

One clause, no "and also," and the interconnection agreement is sourced rather than assumed. **Part 1
passes** — and it is the only part that does.

**2. Dollar path:** FAILED, though not in the obvious way. The *segment* clears the bar comfortably:
Transmission & Distribution Companies is **55% of revenue** as of 2026-Q2, against FY2025 total
revenue of **$21.88B** (Perplexity, citing a 10-K summary page and a KPI aggregator — both secondary;
no source in the set breaks out AEP Texas in dollars at all). But §4.2 asks for the **magnitude of
the change**, and that is where this dies. Beacon Point is **1 GW**. AEP Texas already has
**45 GW of SB6-compliant contracted load additions through 2030**, disclosed by management on the
Q2 2026 call, within a **56 GW** identified-load figure company-wide. This deal is roughly **2% of a
pipeline the company has already put in its own guidance**, and regulated T&D revenue is set by rate
cases, not by any single customer's contract. I cannot write a magnitude for this event that is both
honest and material.

**3. Timing window:** FAILED, decisively and independently. Management's own framing of the Texas
data-centre load is "**through 2030**." The campus is under development; the Anthropic capacity is
~350 MW of an eventual gigawatt. Nothing about *this contract* lands in an AEP reported quarter
inside the §4.3 two-quarter horizon.

**4. Invalidation:** (not reached — parts 2 and 3 both failed)

**Hard filters:**
- Priced-in (§4): moved **+0.38%** over last 5 sessions (121.98 → 122.44) → **pass**. Also
  **−3.86% over 20 sessions** (127.36 → 122.44) → pass. Cleanly, in both windows.
- Correlation (§4): no open positions → pass, vacuously
- Universe (§3): stock, NASDAQ, tradable, fractionable; market cap **~$67–69B** (source: Perplexity
  aggregating MarketBeat $67.59B on 2026-08-21, aistockwire $68.74B on 2026-08-19, a news item
  $68.89B on 2026-08-17, Seeking Alpha $66.59B on 2026-08-04) → **pass**, far above the $10B floor

**Outcome:** REJECTED on parts 2 and 3. A sound one-sentence mechanism attached to a company that
has already told the market about the exposure, and that will not report it inside the horizon.

**Why this entry earns its place, and the rule it produces.** This is the **third consecutive
candidate** to clear the priced-in filter and die anyway, and the three failures are the same failure
in different clothing. On **LHX** the mechanism was real but the price was trading on something else.
On **WDC** the mechanism did not exist, because the company had sold the business. Here the mechanism
is real, the company *is* exposed, and the exposure is **already in guidance**.

That is a genuinely new variant and it is the sneakiest of the three. AEP has been telling investors
about Texas data-centre load since the Q4 FY2025 call — 36 GW of LOAs then, 45 GW contracted through
2030 by Q2 2026, 2025 retail sales +7.5% with C&I up nearly 10% "primarily from data centers in
Indiana, Texas, and Ohio." A single named tenant arriving inside a pipeline the company has already
quantified is **not new information about AEP**, and the stock's +0.38% five-session move is not the
market overlooking something. It is the market correctly pricing an increment of about 2%.

**Practical form, to sit alongside the "verify the business before running the screen" rule from
T-2026-09-01-05: verify the news is new to the company's own disclosure.** Before treating a contract
as a catalyst for Company B, check whether Company B's management has already guided the pipeline
that contract falls inside. If it has, the individual deal is an illustration of existing guidance,
not a change to it — and the priced-in check will pass for exactly the wrong reason. Three runs, three
names, three passing priced-in checks, three rejections: **the filter has now been non-informative
about the outcome in every case where I ran it.** It is a veto, not a signal, and I should stop
reading a pass as encouragement.

**One further mark against this candidate even had 2 and 3 passed.** The single sourced link is an
interconnection agreement — a regulated utility connecting a customer, which is the thing it exists
to do. §4 wants Company B's economics to *change*. A utility signing an interconnection is closer to
a utility doing its job than to a windfall, and I should have weighted that earlier than I did.

---

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

---

## 2026-09-07 (Monday) — NO RESEARCH RUN. MARKET HOLIDAY (Labor Day).

**Not a quiet day. The funnel was never opened.**

The 08:29 ET pre-market run passed the selftest on all five checks (Alpaca, Perplexity,
ClickUp, env, control — `trading_enabled: true`, LIVE paper account), read `clock`, found
`is_open: false` with `next_open: 2026-09-08T09:30:00-04:00`, and stopped at Step 2 of the
routine as instructed. **Next open being tomorrow rather than today at 09:30 is what
distinguishes a holiday from an ordinary 08:00 pre-market hour.**

**Zero Perplexity queries were issued. No candidate was screened, no filter was run, no
thesis was written or rejected.** This marker exists so that the absence of `T-2026-09-07-NN`
entries is not read as a legitimate research day that found nothing worth buying. Those two
things look identical in this file, and the routine is explicit that the difference has to be
made loud at the time because nothing later will make it visible.

No thesis IDs are consumed by this date. The next entries will be `T-2026-09-08-NN`.
