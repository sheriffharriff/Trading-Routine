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
plan_date: 2026-10-05
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-05 at 09:30 ET** (`alpaca.py clock` at 08:28:54 ET: `is_open:
false`, `next_open: 2026-10-05T09:30:00-04:00`, `next_close: 2026-10-05T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** ⚠ **Corroborated independently from the data plane:
`bars --adjustment all` returns a complete **2026-10-02** bar and **NO bar dated 2026-10-05**
— the pre-market shape, confirmed rather than assumed.**

**One pre-market run today, at 08:28–08:31 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$100,038.62** at pre-flight).

⚠ **This file arrived carrying `plan_date: 2026-10-02` — THREE CALENDAR DAYS OLD AND CORRECTLY
SO, BECAUSE THE INTERVENING DAYS WERE A WEEKEND.** Friday's pre-market run wrote it and all
four of Friday's routines committed. ⚠⚠ **NOTE THE SHAPE CAREFULLY: a Monday is the one morning
when a correct plan is three days old, so "the date is not yesterday" is NOT evidence of a
missed run. Compare `plan_date` to the last TRADING day, not to the calendar.**
⚠ **THE STALENESS GATE STILL HAS NOT BEEN TESTED. The count will be 33 after today's open** —
exercised once per market-open run, never fired, because it has never met a plan whose date was
not today. **Its alert path remains untested code.** ⚠⚠ **AND THE REASON IT MATTERS, RESTATED
BECAUSE TODAY'S PLAN IS AGAIN EMPTY: A FRESH EMPTY PLAN AND A STALE PLAN PRODUCE A BYTE-FOR-BYTE
IDENTICAL ZERO-ORDER RUN. Freshness must be read OFF `plan_date` and NEVER inferred from the
outcome.** This plan is **fresh and deliberately empty**.

---

## Tape context

⚠⚠ **THERE IS NO NEW SESSION TO REPORT. THE LAST COMPLETED SESSION IS STILL 2026-10-02, THE SAME
ONE FRIDAY'S RUNS MEASURED.** A Monday pre-market run is the only seat that reads the same closing
tape its predecessor read. **Nothing below is a new observation of the market; it is the same
observation, re-pulled from source rather than inherited.**

The **official** VOO close, from `bars --adjustment all` on a **completed** session and **pulled
fresh by this run**, is **707.35** (o 708.30, h 710.09, l 705.545). The two prior sessions on the
same basis: **10-01 702.255**, **09-30 700.605**.

⚠ **A COUNTER-INSTANCE TO THE "A COMPLETED BAR'S `n`/`v` DRIFT" ITEM, AND IT CUTS THE RIGHT WAY.**
The 2026-10-02 bar read **n 2,524 / v 134,995** to Friday's close run and reads **n 2,524 /
v 134,995** on this run's fresh pull — **identical, over a full weekend.** ⚠ **So `n`/`v` drift
SOMETIMES and not ALWAYS. That does not weaken the standing rule, it completes it: a field that
sometimes moves on a complete bar is unusable as evidence in EITHER direction, and "it did not
move this time" is not a validation any more than "it moved" was a refutation.** ⚠ **The CLOSE is
the stable field; the CLOCK is the reliable discriminator.**

⚠⚠ **EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT INTERCHANGEABLE.**
VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close by **0.997432**, while
`raw` and `split` return the original prints. ⚠ **09-28 onward agree on both bases; the divergence
is entirely in the sessions BEFORE it.** ⚠ **The 09-03 core fill at 706.74 is a RAW print. NAME THE
BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**

**On the 10-02 official close:** equity **$100,060.4082**, core **$70,060.4082 = 70.0181%**, cash
**29.9819%**. ⚠ **RE-DERIVED FROM A FRESH `positions` PULL THIS RUN, NOT CARRIED: qty 99.046311231
× 707.35 + $30,000.00 reproduces it to the cent, so it is a CHECKED fact rather than an inherited
one.**
**On the 08:28 broker mark:** equity **$100,038.62**, core **$70,038.618061 = 70.01%**, cash
**29.99%**, `rebalance_delta` **−$11.58**.
⚠⚠ **THESE TWO FIGURES MUST NEVER BE DIFFERENCED.** The 08:28 `current_price` of **707.13** sits
**−$0.22** against the official 707.35 — this is a **PRE-MARKET** reading and belongs to a
**DIFFERENT SERIES** from the post-bell broker/official gaps. ⚠ **The gap is a moving live midpoint,
not an offset — settled 10-02 by a same-day pair that swung $0.4954/share and changed sign in thirty
minutes. Do not append this number to that series.**
⚠ **NEVER `equity − last_equity` as a day's P&L. NEVER `unrealized_intraday_pl` or `change_today`**
— the 08:28 pull reports `unrealized_intraday_pl: −40.61` and `change_today: −0.00058`, which are
pre-market noise against a `lastday_price` of 707.54 that is itself not the official close.
⚠ **An equity figure is meaningless without its CALL and its TIMESTAMP.**

**§6's 5% cap against the 08:28 live equity is $5,001.93.** ⚠ **It has no operand today — this plan
carries no BUY intent, as no plan ever has.** The open run must recompute it against equity at 09:35,
not against this figure.

---

## Reconciliation

**THE LEDGER AGREES WITH THE BROKER. ZERO SATELLITE POSITIONS ON BOTH SIDES.**

`alpaca.py positions` returns **one row, core VOO** — 99.046311231 shares, avg_entry **706.74** (a
**RAW** print), cost_basis **$69,999.99**, unchanged since the 09-03 fill — against **zero satellite
blocks in `positions.md`. THEY AGREE.** ⚠ **Core VOO was removed from the working list BEFORE any §5
rule was read**, per §5's core exemption. ⚠ **Every reconciliation here is satellite-to-satellite; a
run that compares the raw ledger to the raw broker will read a correct ledger as broken.**

**No discrepancy was found, so no discrepancy is flagged.** ⚠ **Twenty-fourth session with nothing
to reconcile — and an agreeing ledger and an empty ledger are the same artifact here. That is not a
clean bill of health on the reconciliation logic; it is the absence of a test.**

---

## ⚠⚠ THE DIVIDEND TEST — DAY 6 OF 8, TWO SESSIONS LEFT, AND THE READING IS UNCHANGED

**`cash` reads exactly $30,000.00 at 08:28 — a NINETEENTH consecutive reading.** ⚠ **Nineteen
readings are ONE unresolved observation, not nineteen pieces of evidence**, and non-arrival remains
**EXPECTED** rather than informative — settlement runs on the PAY date.

⚠⚠ **THE FALSIFIABLE TEST, WRITTEN IN ADVANCE AND REPEATED VERBATIM: `cash` should rise to about
$30,180.76. IF IT HAS NOT BY 2026-10-07, THE PAPER ACCOUNT DOES NOT MODEL DIVIDENDS AT ALL.** The
implied credit (**$1.825/share × 99.046311231**) is an **INFERENCE** — Alpaca does not publish it.
**Two sessions remain: today and 10-06, with 10-07 the deadline. The close run and tomorrow's
pre-market run are the two seats that will read `cash` before it expires.**

⚠ **The price of the answer, already established and not re-derived: VOO's trailing 12 months is
+16.3118% on `--adjustment all` against +14.9863% on `raw`, so dividends are 1.3254pp/yr. If the
account never collects them, the 70% core structurally under-earns by ~0.93pp/yr, which on top of
the 4.89pp cash drag is a ~5.82pp ANNUAL HANDICAP BEFORE ANY DECISION.** ⚠ **That is a finding for
the human, not something any seat can fix.**

---

## Intents

### BUY

**NONE.** ⚠ **Seven theses were written this run and all seven were rejected. There is no BUY intent
because no candidate survived §4, not because the run was blocked from making one.**

⚠⚠ **EVERY GATE WAS OPEN AND THAT IS THE POINT.** Circuit breaker **INACTIVE** · weekly cap **0 of
3** · satellite sleeve **0.0%, entirely undeployed** · ~**30% idle cash** · `control.md` notes
**(none)** · `TRADING_ENABLED: true`. **Nothing stopped a buy today except the evidence.**

**What the funnel actually returned, so the human can see the shape rather than the count:**

| Thesis | Company A | Why it died | Test that fired FIRST |
|---|---|---|---|
| T-2026-10-05-01 | onsemi/Synaptics revised $5.7B all-cash | No Company B; "Party A" is a redaction; MS's $2.45B is financing; SYNA ~$5.7B < $10B | **part 1** |
| T-2026-10-05-02 | Bayer $2.2B Ohio plant | Drug substance **2031**, finished product **2034** — ~20 to ~32 quarters vs a ceiling of 2 | **part 3** |
| T-2026-10-05-03 | FDA / Edwards AUTUS valve | No named supplier — **volunteered absence**; EW vertically integrated (rule vii) | **part 1** |
| T-2026-10-05-04 | FDA / BMS Camzyos paediatric | No named supplier — **volunteered absence**; label expansion creates no new line | **part 1** |
| T-2026-10-05-05 | TSMC capex $60–64B | **Earnings PREVIEW, not an event** (rule iii); unnamed supply base; AMAT/LRCX/KLA already killed 10-01 | **rule (iii)** |
| T-2026-10-05-06 | September payrolls +29k | **No Company A** — one party, no recipient; and it is September's print, already logged 10-02 | **part 1 / macro** |
| T-2026-10-05-07 | G7 diesel reserve release | Source says **"not sufficiently verified"**; one party; **sign wrong for a long** | **premise** |

⚠⚠ **THE SECOND BROAD SCAN RETURNED ZERO NEW NAMES. Every row it produced was already disposed
(Venture Global/ConocoPhillips 10-02, RTX SM-6 10-02, MTUS 10-01) or §3-ineligible on sight (Big Sky
Industrial and Tiberius Aerospace — counterparty UNNAMED; Bharat Forge and Jindal Stainless —
India-listed). NOT ONE WAS RE-SCREENED.** ⚠ **The carry-forward named all three disposed items and
said do not rehabilitate at a different price. That instruction was followed, not re-derived.**

⚠⚠ **THE ONE ENTRY THE HUMAN SHOULD READ IS T-2026-10-05-01, FOR A NEW COSTUME OF RULE (v): AN
UNNAMED *BIDDER* WEARING A LEGAL PSEUDONYM.** Synaptics' filings call the competing bidder only
**"Party A"** — one specific entity that definitely exists, acted on a dated day (2026-09-02), and is
known to the filer and redacted on purpose. **It is a more fillable-looking blank than rule (v)'s
unnamed supply base, because the blank has a shape, a date and a motive — everything except a name.**
⚠ **The priors were instantly ready (Microchip, Skyworks, Qorvo, Renesas, Infineon) and NO GUESS WAS
MADE.** ⚠ **A REDACTION IS NOT A LEAD.**

⚠ **NO `move` CALLS WERE MADE. That is the ABSENT state — the fourth — not a skipped check and not a
pass**, because every candidate died before an eligible ticker with a mechanism was reached. ⚠ **A
decorative `move` call would have converted an honest absence into a fake exercise and was declined
for that reason.** **Third instance after 09-29 and 10-02.**

### SELL

**NONE — AND THE DISTINCTION MATTERS: §5 HAD NO OPERAND, IT DID NOT PASS.**

**Zero open satellite positions**, so §5.1 (thesis invalidation), §5.2 (time stop), §5.3 (hard stop
−7%) and §5.4 (trailing stop −10%) **each had nothing to evaluate.** ⚠ **No Perplexity news check was
run on any holding, because there is no holding to check — that is an absent step, not a completed
one.** ⚠ **"Nothing close to triggering" would be FALSE. The distance to each rule is not large; it is
UNDEFINED, and those are different facts.** **§5.1–§5.4 have never had an operand: 24 sessions since
2026-09-01, 21 of them post-fill, zero satellite positions ever.**

### REBALANCE

**NONE — core is inside the §2 band and not near an edge.**

Core **70.01%** against a 65–75% band: **5.01 points inside the 65 edge and 4.99 inside the 75 edge.**
`core_in_band: true`, `rebalance_needed: false`. ⚠ **`rebalance_delta: −$11.58` IS A DISTANCE READOUT,
NOT AN INSTRUCTION** — negative only because core sits fractionally above the 70% target. **§2 acts at
the band edge, not at the target.** **Sixtieth consecutive run inside 69.59–70.22%.**

---

## Revalidation instructions for the 09:35 run

**There is nothing to revalidate.** ⚠ **This section normally names the specific number the open run
must re-check for each BUY intent; with no BUY intent, there is no number.** ⚠ **Do not read its
emptiness as "all checks passed" — there were no checks to carry forward.**

**What the open run should still do, none of which depends on this plan:**
1. **Read `plan_date` above and confirm it is 2026-10-05** before anything else. ⚠ **If it is not,
   the gate fires for the first time in 33 exercises — read routine 2's Step 2 then, do not recall it.**
2. **Re-read `cash` from a fresh `account` or `sleeves` call.** ⚠ **It should read $30,000.00 for a
   twentieth time. If it reads ~$30,180.76, THE DIVIDEND HAS ARRIVED and that resolves an eight-day
   open question — record it loudly and name the exact figure.**
3. **Confirm core is still in band** against live 09:35 equity. **No rebalance is due on this morning's
   reading and none should be manufactured from a moving mark.**
4. ⚠ **Open nothing.** **Routine 2 executes only what this file already contains.** ⚠⚠ **Opening at
   09:35 without a plan entry routes AROUND the discipline that is the whole point of this handoff.
   Idle cash, an INACTIVE breaker and an unused 0-of-3 weekly cap are NOT an opportunity routine 2 may
   act on.**
