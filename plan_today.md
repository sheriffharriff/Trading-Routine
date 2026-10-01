# Today's Plan

**AGENT-OWNED. Written by the pre-market routine, consumed by the market-open routine,
overwritten daily.**

This file is the handoff between the two runs. The pre-market run does the thinking and
writes intents here; the market-open run executes them. Nothing gets bought that was not
written here first, which is what forces every buy to sleep on a written thesis instead of
being reasoned into existence at the moment of execution.

The market-open run **re-validates every intent against fresh quotes before acting**. An
intent written at 08:00 can be dead by 09:35 — an overnight gap can push a candidate past
the §4 4%-in-five-sessions priced-in threshold, in which case the trade is skipped and the
skip is logged. A stale intent is a proposal, not an instruction.

---

## Status

`plan_date` is load-bearing, not a comment. The market-open routine compares it to today's
ET date and **refuses to execute any intent from a plan not dated today** — it logs the
stale plan, posts an alert, and proceeds to the core/rebalance section only.

If the pre-market run failed, was skipped, or crashed before writing, this file still holds
yesterday's intents. Executing them would be running stale research as though it were
fresh — the candidate has had another full session to move, and the §4 priced-in check that
cleared it was performed against prices that no longer exist. Doing nothing is strictly
better. Core and rebalance actions are exempt from the gate because neither depends on the
day's research.

```
plan_date: 2026-10-01
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-01 at 09:30 ET** (`alpaca.py clock` at 08:24:57 ET: `is_open:
false`, `next_open: 2026-10-01T09:30:00-04:00`, `next_close: 2026-10-01T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** ⚠ **Corroborated independently: `bars` returns a
complete 2026-09-30 bar and NO bar dated 2026-10-01 — the pre-market shape, confirmed not
assumed.**

**One pre-market run today, at 08:21–08:25 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$99,693.94** at pre-flight).

⚠ **This file arrived carrying `plan_date: 2026-09-30` — ONE CALENDAR DAY OLD AND CORRECTLY
SO**, because yesterday's pre-market run wrote it and all four of yesterday's routines
committed (`git log`: pre-market, open, midday `8dc0340`, close `78b7594`). ⚠ **The 09-28 gap
therefore remains a ONE-DAY, THREE-ROUTINE event and is still NOT reported as ongoing.**
⚠ **THE STALENESS GATE STILL HAS NOT BEEN TESTED. The count is 30, not 31** — it is exercised
once per market-open run and has never fired, because it has never met a plan whose date was
not today. **Its alert path remains untested code.**

---

## Tape context

Yesterday's **official** VOO close, from `bars --adjustment all` on a **completed** session
and **pulled fresh by this run rather than inherited**, is **700.605** (o 704.52, h 707.20,
l 700.605, n 2053, v 61032). The two prior sessions on the same basis: **09-29 702.27**,
**09-28 703.60**.

⚠ **ONE SMALL NEW FACT WORTH A LINE: the 09-30 bar's `n`/`v` have MOVED since the close run
read them** — 2050/61014 then, **2053/61032** now — **while the close held at 700.605 to the
cent.** ⚠ **A completed daily bar is not immutable in its trade counts (late-reported
prints), so `n` and `v` are even weaker completeness evidence than the standing warning says.
The CLOSE is the stable field; the clock is still the reliable discriminator.**

⚠⚠ **EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT
INTERCHANGEABLE.** VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close
by **0.997432**, while `--adjustment raw` and `--adjustment split` return the original prints.
⚠ **09-28, 09-29 and 09-30 agree to the cent on both bases, because the ex-date lies at or
before all three — the divergence is entirely in the sessions BEFORE it.** ⚠ **The 09-03 core
fill at 706.74 is a RAW print. NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**

**On the 09-30 official close:** equity **$99,392.34**, core **$69,392.34 = 69.8166%**, cash
**30.1834%**.
**On the 08:24 broker mark:** equity **$99,681.06**, core **$69,681.06 = 69.9040%**, cash
**30.0960%**, `rebalance_delta` **+$95.68**. ⚠ **These two figures must never be differenced
— the 09-30 close run supplied the worked instance, where differencing a broker mark against
an official close understated a real −$164.91 day as −$51.50, a threefold error.**

⚠⚠ **A BASIS TRAP THIS RUN WALKED UP TO AND DECLINED, WHICH IS NEW IN SHAPE:** core
`current_price` reads **703.52**, i.e. **+$2.915 above the 700.605 official close** — far
larger than any of the nine catalogued post-bell gaps (range −$0.97 to +$1.145). ⚠ **IT MUST
NOT BE ADDED TO THAT SERIES. Those nine are all POST-BELL observations; this is a PRE-MARKET
indication on a morning when softer PCE moved futures. Appending it would have produced a
spurious new "largest gap on record" by nearly triple — a superlative that is an artifact of
mixing two different times of day, not of any widening.** ⚠ **Different hour, different
series. The post-bell series still has nine members and its largest is still +$1.145.**

⚠ **THE INTRADAY-DRIFT ITEM GOT ITS SEVENTH INSTANCE:** `selftest` reported **$99,693.94** at
08:21 and `sleeves` returned **$99,681.06** at 08:24 — a **$12.88** spread. ⚠ **Well inside
the established $1.97–$216.91 range and therefore NOT evidence of anything narrowing.** ⚠ **An
intraday equity figure is only meaningful with its CALL and its TIMESTAMP attached.**
⚠ **This bites §6's 5% sizing cap, which is computed against live equity — 5% of the 08:24
mark is $4,984.05. It has no operand today only because there is no BUY intent.**

---

## Sleeves and the rebalance question

| Sleeve | Value (08:24 broker) | % | Target | In band? |
|---|---:|---:|---:|---|
| Core (VOO) | $69,681.06 | **69.90%** | 70% | **yes** (65–75) |
| Satellite | $0.00 | **0.00%** | 30% | n/a — empty |
| Cash | $30,000.00 | **30.10%** | — | §2 permits idle satellite cash |

**NO REBALANCE IS DUE, ON EITHER BASIS.** Core sits **4.90 points** inside the 65% edge on
the broker mark (4.82 on the official close). ⚠ **Do NOT act on `rebalance_delta: +$95.68`:
§2 rebalances at the BAND EDGE, not toward the 70% target.** ⚠ **`rebalance_delta` is now
POSITIVE for an EIGHTH consecutive run. That is NOT the sign-instability defect resolving —
the same quantity disagreed in sign on 09-24.** **Fifty-fourth consecutive run inside
69.59–70.22%.**

**⚠ CHECK `cash`.** It read **exactly $30,000.00** at 08:24 — a **tenth** reading, now on the
**fourth calendar day** since VOO's 09-28 ex-date. **Day 4 of 8.** ⚠ **NON-ARRIVAL THIS EARLY
IS EXPECTED, NOT EVIDENCE — settlement runs on the PAY date, not the ex-date. Do not read
$30,000.00 as the test resolving in either direction.** **The falsifiable test, written in
advance: `cash` should rise to ~$30,180.45. If it has NOT by 2026-10-07, the paper account
does not model dividends at all — in which case §1's "beat the S&P TOTAL RETURN" is
unwinnable BY CONSTRUCTION, by VOO's entire ~1.0% annual yield.** ⚠ **That is a finding for
the human, not something any run may fix.** The ~$180.45 credit is an **INFERENCE** — Alpaca
does not publish the figure — and must stay labelled as one.

---

## Position review — §5

**Zero satellite positions. Reconciliation is CLEAN.** `alpaca.py positions` returns **one
row, core VOO**, 99.046311231 shares at avg_entry **706.74** (a **RAW** print), cost_basis
$69,999.99 — unchanged since the 09-03 fill — against **zero satellite blocks in
`positions.md`. THEY AGREE.** ⚠ **Compared satellite-to-satellite, never raw ledger against
raw broker. Core VOO was removed from the working list BEFORE any §5 rule was read**, per §5's
core exemption.

| Rule | Status | Why it is not "passing" |
|---|---|---|
| **§5.1** thesis invalidation | **NO OPERAND** | No thesis is held, so there is no invalidation condition to read verbatim. **Zero news-on-holdings Perplexity queries were due; zero were run.** |
| **§5.2** time stop | **NO OPERAND** | No `timing_window` and no deadline field exists anywhere in `positions.md`. |
| **§5.3** hard stop −7% | **DISTANCE UNDEFINED** | There is no `entry_price` to measure a drawdown from. ⚠ **Not "comfortably far" — undefined.** |
| **§5.4** trailing stop −10% | **NOT ARMED** | There is no `highest_close` field — the **third state**, carrying **no `(as of …)` date at all.** It arms on the first **satellite** fill; the 09-03 core fill was not one. |

⚠⚠ **ABSENT IS NOT PASSING, AND §5 HAS NEVER HAD AN OPERAND IN THIS ACCOUNT'S HISTORY** — 21
completed sessions since 2026-09-01, 18 after the 09-03 core fill, zero satellite positions
ever. ⚠ **The counter is NOT advanced by this run: at 08:24 the market has not opened, so
today is not a completed session and a pre-market seat has none of today's to add (catch 11).**

---

## Intents

### BUY

**NONE.**

⚠ **Every gate that could have blocked a buy was OPEN, and nothing was blocked.** Circuit
breaker **INACTIVE** (`halt_triggered_at: none`); `new_positions_this_week` **0 of 3**;
satellite sleeve **empty** with **~30% idle cash**; `control.md` notes **(none)**;
`TRADING_ENABLED: true`. **Research ran in full and produced no eligible candidate.** Per §4,
that is a successful run, not a failed one.

**Six candidates reached a `research_log.md` entry and all six were rejected:**

| ID | Candidate | Killed by |
|---|---|---|
| T-2026-10-01-01 | **Micron FY2027 capex chain** (no ticker) | **Part 3** — the capex rise is majority **CONSTRUCTION** capex to accelerate **cleanroom availability in late calendar 2028 and beyond**. Durable even if a supplier is named later. **Rule (v)** second: the source volunteered that **no US-listed equipment, construction or materials vendor is explicitly named.** |
| T-2026-10-01-02 | **AMD** (via HPE/Vultr $1.2B) | **Part 3 — NOT ESTABLISHABLE**: no delivery schedule, contract duration or revenue-recognition timing disclosed anywhere. **Part 2** second: AMD's share of the $1.2B is disclosed by nobody, and the full $1.2B is low-single-digit % of AMD's revenue. ⚠ **Part 1 PASSED cleanly.** |
| T-2026-10-01-03 | **SNPS / AWS $1B+** (no candidate) | **Structure — there is no second party left to buy.** SNPS is the named beneficiary (first-order); **Amazon is the PAYER** (capital paid out, rule viii). No third company is named. |
| T-2026-10-01-04 | **US–Korea 8-reactor framework** | **Part 3 (rule vi)** — a framework *contemplating* reactors, expressly **not** orders, financing or construction starts. Westinghouse is not independently US-listed. |
| T-2026-10-01-05 | **MTUS** (Metallus) | **§3 OUTRIGHT — market cap ~$0.79B against a $10B floor** (MarketBeat via Perplexity). Plus **rule (v)'s CEILING sub-shape** — the source says the $995M "is not a guaranteed purchase amount" — and first-order status. |
| T-2026-10-01-06 | **CALM** (Cal-Maine) | **Part 3** — prepared-food capacity plan runs **through H1 fiscal 2028**. **Part 2** second: no figure of any kind in the source, and a capacity percentage is a VOLUME statement. ⚠ **§3 ATTEMPTED AND UNRESOLVED — no verified cap was available. UNDECIDED, not passing.** |

⚠⚠ **THE FINDING OF THIS RUN, AND IT IS THE SECOND CONSECUTIVE SESSION TO PRODUCE IT: THE
SOURCE VOLUNTEERED THE ABSENCE OF A COMPANY B, UNPROMPTED, IN ITS OWN WORDS** — *"no publicly
traded U.S. semiconductor-equipment supplier, construction company, or materials vendor was
explicitly named as a direct beneficiary… Naming companies such as equipment manufacturers,
engineering contractors, or materials suppliers based only on industry fit would be an
inference, not an explicit source linkage."* ⚠ **The carry-forward instruction was to WRITE
THAT DOWN and stop rather than re-word the query. NO RE-QUERY WAS ISSUED.**

⚠⚠ **AND THE PULL IS NAMED, BECAUSE NAMING IT IS THE ONLY DEFENCE. TODAY'S INSTANCE IS THE
SHARPEST YET, BECAUSE MY OWN PRIORS HAD THE ANSWER READY AND SPECIFIC: Applied Materials, Lam
Research, KLA.** Every one is a fact about the **industry**, not about this transaction.
⚠ **Micron's side is a CLEAN rule (iii) pass — $22B → $32B and ~$100B → ~$150B are the
company's own figures against its own earlier figures. The news was real, new and quantified,
and it STILL produces no Company B.** ⚠⚠ **That is a SEVENTH form of the binding constraint
in open item (3), and the one no widening of the evidence bar reaches: everything is
disclosed and the spending simply lands too far in the future.**

⚠⚠ **THE MOST DECISION-RELEVANT ENTRY TODAY IS T-02 (AMD), AND IT IS NOT THE REJECTION THAT
MATTERS BUT THE ORDER OF DISCOVERY.** Part 1 passed cleanly — one clause, no "and also", a
signed order, a disclosed figure, a named platform. ⚠ **The second-order STRUCTURE was found
first and felt like the finding; the first-order OBJECTION (AMD is co-named in the headline:
"HPE secures its first AMD Helios order in $1.2 billion deal with Vultr") arrived
AFTERWARDS.** ⚠ **On a day when parts 2 and 3 had not already failed, that sequence is exactly
how a first-order trade gets taken wearing second-order clothes. Record the sequence, not just
the verdict.**

⚠ **THE PRICED-IN FILTER HAD THREE OPERANDS AND DECIDED NOTHING — the third state again
(EXERCISED AND NON-DECISIVE), for the second consecutive session.** `move` calls:
**AMD −0.52%** (614.84 → 611.65), **HPE +2.50%** (62.34 → 63.90), **MU −0.50%** (1072.18 →
1066.85) — all three `priced_in: false`, and **not one rejection turned on any of them.**
⚠⚠ **AMD AND MU BOTH PASSED BY FALLING, which is sign-blindness in its mild form: a name
co-named in a $1.2B AI-order headline printing −0.52% over five sessions is precisely the
reading that invites a "the market has not noticed" story. THAT STORY WAS NOT WRITTEN.**
⚠⚠ **AND HPE SUPPLIES A FRESH, MILD INSTANCE OF OPEN ITEM (2) — THE WINDOW MASKING AN EVENT
MOVE.** HPE's five-session reading is **+2.50%**, but the **news day alone ran 61.51 → 63.90 =
+3.886%**, and the window swept up a prior **−3.187%** slide (09-24 63.535 → 09-29 61.51).
⚠ **Graded honestly: this is WEAKER than the AKAM instance, because even the uncancelled event
move (+3.886%) was still BELOW the 4% threshold — so the filter would have passed HPE on the
news day too. The window hid ~1.4pp and changed no verdict.** ⚠ **A mild instance recorded as
mild. HPE was first-order regardless.**

⚠ **THE CORRELATION CHECK HAD NO OPERAND — ABSENT, NOT PASSING.** Zero satellite blocks means
there is no `driver` field anywhere to collide with. **A candidate cannot fail §4's
correlation test in this account today.**

⚠ **TWO EVENTS WERE RECOGNISED ON SIGHT AND NOT RE-LITIGATED, AND THAT IS THE CORRECT
OUTPUT:** **Boeing / F/A-XX** (disposed 09-30; the source was asked directly and stated no
US-listed supplier is named — **zero queries issued today**) and **the Fed / PCE /
trade-deficit complex** (environment input, ONE party; disposed 09-29). ⚠ **Note the new
costume on the macro item: yesterday's was a probability that MOVED 57% → 70%; today's is the
same probability moving BACK on a softer August PCE. A reversal is no more a Company A than
the move was.** ⚠ **A third was recognised and declined: the MEMORY READ-ACROSS from Micron's
tightness to SanDisk / Western Digital / Seagate — the competitor's-earnings-print face of the
shared-cause rule, needing an "and also". Zero calls on any of the three.** ⚠ **JBL appeared
in a citation at −6.68% and was NOT reached for: a rejection is not a queue, and the price was
never what was missing.**

### SELL

**NONE.** No satellite positions exist. §5 has no operand — see the table above, where each
rule's status is recorded as **ABSENT rather than as passing**.

### REBALANCE

**NONE.** Core is **69.90%** on the 08:24 broker mark, inside the 65–75% band by **4.90
points**. ⚠ **Do not act on `rebalance_delta: +$95.68` — §2 rebalances at the band edge, not
toward the 70% target.**

---

## For the market-open run

**Zero BUY intents, so ZERO `move` re-validation calls are due. That is an ABSENT check, not a
skipped one** — record it that way. ⚠ **There is no `revalidate` line below because there is
no intent to revalidate; the absence is deliberate, not an omission.**

⚠ **The staleness gate: this plan is dated 2026-10-01 and today's ET date is 2026-10-01
(computed, not assumed), so it is FRESH.** ⚠ **But note what that does and does not tell you:
a FRESH EMPTY plan and a STALE plan produce a byte-for-byte identical zero-order run. Read
`plan_date`, never the outcome.** The gate will have been exercised **thirty-one times without
ever firing** after today's open; its alert path **remains untested code**. The first morning
it does fire will by construction be a morning when the pre-market run failed — i.e. the
morning with no fresh notes to lean on. **Read routine 2's Step 2 then; do not recall it.**

**⚠ CHECK `cash`.** It read **exactly $30,000.00** at 08:24 today — **day 4 of 8**. It should
read **$30,000.00** if the VOO dividend still has not been paid, or **~$30,180.45** if it has.
**Either reading is informative; record which one you got, and do not treat $30,000.00 as the
test resolving.**

**⚠ A BAR DATED TODAY IS PARTIAL ONCE THE MARKET IS OPEN**, and at 09:35 it will not look like
a stub. ⚠ **Do not use it as a close. `n` and `v` cannot tell you otherwise — and this run
found they are not even stable on a COMPLETED bar (the 09-30 bar's n/v moved from 2050/61014
to 2053/61032 overnight while its close held at 700.605).** Use a fresh `quote` for execution
reference and `bars` only on completed sessions.

**⚠ YOU MAY NOT OPEN A POSITION THAT IS NOT WRITTEN ABOVE.** Today nothing is. ⚠ **Idle cash,
an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an opportunity routine 2 may act
on** — a position opened at 09:35 without a plan entry routes **around** the discipline rather
than satisfying it. **Core and rebalance are the only non-research actions available, and
neither is due.**
