# State

**AGENT-OWNED. Rewritten by every run. This is the run-to-run state machine.**

Each routine starts blind — a fresh clone, no conversation history, nothing but these
files. This file is what the previous run left behind. Read it before you do anything.

The block below is parsed by `scripts/common.py` and gates real behavior
(`alpaca.py buy` refuses to submit while the circuit breaker is active). Keep the
`key: value` format exactly. Prose goes underneath.

⚠ **KEEP `last_run` TO ONE LINE.** This file was 324KB / 2,988 lines on 2026-11-13, almost all
of it a `last_run:` *value* that had grown into a multi-thousand-byte paragraph. A value that
needs a paragraph belongs in `journal.md`. The compaction has now held across eight runs.

```
last_run: 2026-11-18 07:03 ET 1-premarket-research — selftest 5/5 exit 0. Pre-market full session, not a holiday. Ledger reconciled on three sides and AGREES (satellite empty, 91st absent seat). 5 theses written, 0 accepted, 5 rejected. Plan dated 2026-11-18 carries ZERO intents. Core 69.03% in band, no rebalance. Breaker INACTIVE 0/3, cap 0/3, no week reset due. MAIN FINDING: the §4 priced-in window is structurally blind to a post-close catalyst — 9 of 13 names "passed" a test that could not fail.
prior_run: 2026-11-17 16:06 ET 4-market-close-journal — hold for the bell succeeded, official close VOO 672.80, equity 96,638.36 close-basis, day -0.7689%, no backfill owed.
week_of: 2026-11-16
new_positions_this_week: 0
consecutive_closed_losses: 0
circuit_breaker: INACTIVE
halt_triggered_at: none
core_established: true
core_ticker: VOO
core_pct: 69.03
satellite_pct: 0.0
cash_pct: 30.97
open_thesis_ids: none
```

---

## Where things stand (2026-11-18 07:03 ET, **PRE-MARKET BASIS — marks are indications, not closes**)

`clock` **07:03:10** — `is_open: false` with **both** `next_open` and `next_close` carrying
**2026-11-18**: the pre-market full-session signature, **not a holiday**. Wednesday, ordinary
session, opens **09:30 ET**.

- **Equity $96,856.26 (PRE-MARKET)** · core VOO 99.046311231 sh @ 706.74, mark **675.00**,
  unrealised **−$3,143.73 / −4.491%** · cash exactly **$30,000.00**.
  ⚠⚠ **675.00 IS A PRE-MARKET INDICATION, NOT A TRADED CLOSE.** It is why equity sits
  **$217.90 above** 11-17's close-basis **$96,638.36**. **Do not record it as a close or build a
  day-change off it.** `bars` returned **no 2026-11-18 row** — the correct pre-market shape.
- **Sleeves: core 69.03% / satellite 0.00% / cash 30.97%.** `core_in_band: true`,
  `rebalance_needed: false`. **4.03pp of room to the §2 65% floor — NO REBALANCE DUE.**
  ⚠ `rebalance_delta: 943.12` (against `core_target_value: 67,799.38`) is **a distance readout,
  not an order.** The share count has not changed since the 2026-09-03 fill.
- **OFFICIAL CLOSES: 11-11 698.25 · 11-12 696.04 · 11-13 693.05 · 11-16 680.36 · 11-17 672.80.**
- **Satellite sleeve is empty and always has been.** Live Alpaca and `positions.md` AGREE —
  reconciled at this seat on three sides (`positions` one row; `sleeves` satellite `count: 0`;
  zero satellite blocks in the ledger). **§7 overnight exposure is structurally zero.**
- **§5.1–§5.4 are ABSENT, NOT PASSING** — no entry price, no high-water mark, no deadline, no
  invalidation string exists. **91st absent seat, 80th absent date.** No §5.1 news query was run
  or owed: there is no company to check. ⚠ **Core VOO is EXEMPT from §5.**
- **282 thesis IDs written, 0 ever accepted — RE-DERIVED AT THIS SEAT, NOT CARRIED.**
  `grep -c '^### T-2026'`: **66** live + **87** + **129** = **282** (was 277 on 11-17; this seat
  added 5). ⚠ **Re-derive each time; do not carry this number forward.** ⚠ **This counts thesis
  IDs, not items considered** — sweep entries hold many items each. Paths that resolve:
  **`archive/research_log/2026-09.md`**, **`archive/research_log/2026-10.md`**.
- Breaker **INACTIVE 0/3** · weekly cap **0/3 used** · `TRADING_ENABLED: true` ·
  `HALT_CLEARED_AT: none` · `alerts.md` has **no open and no systemic incidents**.

## Week rollover — re-derived at this seat, no reset due

`isocalendar` on 2026-11-18 → ISO **2026-W47 wd 3**, Monday anchor **2026-11-16** = inherited
`week_of` **2026-11-16**. They match. `new_positions_this_week` is 0 under any anchor.

## ⚠⚠⚠ THE FINDING OF THIS RUN — THE §4 PRICED-IN WINDOW IS BLIND TO A POST-CLOSE CATALYST

**Mechanically verified, not argued, and it is the first time this corpus has spent the
priced-in check at scale (thirteen `move` calls).**

Nvidia reported **after the 2026-11-17 close** (FQ4 guided ~**$130B ±3%** vs ~$124.89B
consensus; next-FY growth raised to **~75% from ~70%**; +4% extended, NDX futures +1.3%).
`move --sessions 5` returned `to_close` **155.49 (NVDA)** and **712.975 (MU)** — both confirmed
by `bars` to be the **11-17** closes, and `bars` has **no 11-18 row**.

⚠ **So every `priced_in` verdict this morning was computed on a window containing ZERO
post-catalyst sessions.** A `false` does not mean "the market has not repriced this news"; it
means **"no session has traded since this news."** Those are different statements and only the
first is a clearance. **Nine of thirteen names "passed" a test that could not have failed**,
because the complex **sold off into the print** — NVDA itself **−7.88%** over the window.

⚠⚠ **SECOND, SEPARATE DEFECT — DO NOT CONFLATE: the filter is magnitude-based and
direction-blind.** §4's text is *"moved more than 4%... you are late"*; the script implements
`abs(move) > 4`. **SMCI read `priced_in: true` after FALLING 13.10%**; APH −4.50% and ETN −4.86%
likewise. ⚠⚠ **THIS SEAT HONORED ALL FOUR `true` VERDICTS AS SKIPS AND ATTEMPTED NO OVERRIDE,
WHICH IS THE WHOLE REASON THE DEFECT IS SAFE TO WRITE DOWN.** The argument "the filter is
direction-blind, therefore buy the one that fell 13%" is **averaging into weakness wearing a
filter-critique costume**, and §7 forbids averaging down. **It is reported for the human to fix
in code if they choose. It is not a permission a run may grant itself.**
⚠ **Note the asymmetry: defect (a) makes the filter TOO PERMISSIVE and is the dangerous one.
This seat's answer to it was to reject the whole family anyway** — the only move that does not
lean on a broken filter in either direction.

**RULE FOR THE OPEN SEAT, THE DAY THIS MATTERS:** when the plan's catalyst broke after the prior
close, **you are the first seat that can actually perform the priced-in test.** Re-run
`move --sessions 5` after the open and treat the pre-market reading as **unperformed**, not
passed. **Today it is moot — zero BUY intents, nothing to revalidate.**

## Research — 5 theses, 0 accepted, 5 rejected

The overnight window was **dominated by one event** and it produced no trade. The two that cost
a drill query each:

- **`T-2026-11-18-01` (MU)** — part 1 **PASSED cleanly**; killed on **part 4**. Micron's
  calendar-2026 HBM book is **sold out on price and volume** (management, 2025-12-17), so no
  observable in the next two quarters distinguishes "Nvidia's raise flowed through" from "the
  memory cycle did what it was already doing." **An invalidation condition that cannot fail is
  not an invalidation condition.** Part 2 also failed: the drill returned **$41.5B and $54.2B for
  the same quarter** — a 30% disagreement on the denominator, neither figure from a filing.
  ⚠ **The sold-out fact read as the thesis's STRONGEST link on first draft and is what severs
  it** — capacity-bound suppliers do not re-rate their next two quarters on a customer's demand
  guidance; their next two quarters were sold last year. ⚠ **Caveat on the caveat, reported at
  real strength: that statement covers a period now ENDING.**
- **`T-2026-11-18-02` (VRT/ANET/AVGO/MRVL/COHR/GEV/PWR)** — killed on **part 3**: an **FY28**
  demand revision reaches infrastructure **revenue** through orders → backlog → recognition,
  two-to-four quarters out. Only the narrative lands inside the window, and **backlog is not a
  reported result.** APH, ETN, CLS and SMCI were removed **by the priced-in filter before a
  thesis was written**, which is the order §4 requires.

The other three: **`-03`** GSK/Nuvalent's neladalkib FDA approval → the only US-listed
read-across is **Pfizer's Lorbrena at ~0.6–2.5% of revenue** (ALK+ is ~3–5% of NSCLC), an order
of magnitude under §4's 10% floor, **and the direction is negative in a long-only strategy**.
**`-04`** the retail-sales / December-hike complex → **not a second-order catalyst at all: no
Company A, no segment, no dollar path**; a macro print reprices within minutes and the print has
already happened. **`-05`** a six-item sweep (Viatris/Pacira completion, Shionogi/IntraBio,
Medline secondary, Everforth DARPA task order, Red Cat guidance withdrawal, Pfizer/Seagen FTC),
**zero drill queries spent**.

⚠ **Pattern across the sweep worth keeping: three of six failed because a DATE does not land in
the window (two completions of previously-announced deals, one mis-dated procedural step) and
two because the sourcing NAMES NO COUNTERPARTY.** The second is the instructive one: **an event
can be real, dated, large and correctly reported and still yield no trade, because "who is on
the other side of this" is a fact press coverage routinely omits and an agent must never supply
from its own knowledge.**

## Carry forward

1. ⚠ **ROUTINE 2's SCHEDULE: THE ASK IS WITH THE HUMAN. DO NOT RE-SEND.** 11-02 → 11-12 fired
   08:35–08:47 (`is_open: false`); 11-13 fired 10:43 mid-session; **11-16 did not fire at all**;
   **11-17 fired 08:36, the ordinary pre-bell shape.** Sent out of band 11-12, re-sent 11-16.
   Re-send **only** if routine 2 begins firing consistently *after* the bell in a way that changes
   what the human must fix. **A repeat pre-bell firing is not new information.** ⚠ Per `control.md`
   this is **recorded, not diagnosed** — a firing time is not a schedule fault, and manual "Run
   now" invocations are indistinguishable from scheduled ones. This seat fired **07:03 vs nominal
   08:00, the fifteenth consecutive EST session in the −1h shape.**
2. ⚠⚠ **THE INSURANCE COMMIT MUST INCLUDE `journal.md` AND THE CLICKUP SUMMARY — that scoping
   error is what cost 2026-11-13.** That seat's insurance commit carried `positions.md` and
   `state.md` only; when its second commit never landed, the two artifacts lost were **exactly the
   two it omitted**, and they are the two with no other source. **11-16 and 11-17 did it correctly.**
3. ⚠ **DO NOT WRITE A SUPERLATIVE ABOUT THIS ACCOUNT'S HISTORY WITHOUT RANKING IT FIRST.** The
   11-16 close seat published "the worst session in this account's history" and it was false by a
   factor of two; 11-17 ranked before publishing and got it right. **Rank off a CLOSE, not a
   partial bar** — 11-17's 15:15 summary ranked off a partial and published "4th-worst of 53"
   when the official close made it 5th (corrected by comment on ClickUp task `86bd4hbb1`). The
   ranking table is in `journal.md` 2026-11-17 and is cheap to re-derive.
4. **THE TWO ENDPOINTS DISAGREE ON A SESSION CLOSE AND §5.4 READS FROM ONE OF THEM — EIGHTH
   distinct instance.** Today: `lastday_price` **673.19** vs the official `bars` close **672.80**
   for 11-17 = **0.39 / 0.0580%**. Prior: 11-17 post-bell **0.42 / 0.0624%** (the widest), 11-17
   intraday 0.10, 11-16 post-bell 0.27, 11-13 +0.33. **Not a dividend-basis artifact** — adjusted
   and unadjusted agree to the cent. **Build P&L and stamp `highest_close` from official `bars`
   closes only, on one adjustment basis, one call.**
5. ⚠ **THE IN-PROGRESS-BAR DEFECT: gate every `highest_close` write on `clock`, never on the
   shape, presence or apparent stability of the bar.** 11-17 pulled the same dated bar twice two
   minutes apart with the market open and got **669.96 then 670.45** — a finished close does not
   change between pulls. The bar carries **no flag**. ⚠⚠ **It is not merely theoretical: that same
   run published a corrupted ordinal off a partial bar forty minutes after writing the warning.
   Documenting the hazard is not the same as being protected from it.** ⚠ All of 11-17's partial
   prints read LOW against the official close, and so did 11-16's — **TWO SESSIONS IS NOT A RULE.
   Do not treat "partials read low" as a correction factor.**
6. **The §5.4 staleness detector and the `highest_close` backfill branch are UNPROVEN CODE** at
   the **91st** absent-seat ordinal. The first satellite position will be their first live test.
7. **`--adjustment all` IS NOT A TOTAL-RETURN SERIES ON THIS FEED** (verified 2026-11-13: adjusted
   and unadjusted closes identical to the cent on 259 of 260 sessions, across all four VOO
   ex-dividend dates). **Any review using the flag's output understates the benchmark and flatters
   the agent.** True 12-month VOO total return is **+14.615%**.
8. **The paper broker does not pay dividends.** Cash is exactly $30,000.00, not $30,180.52 — the
   2026-09-28 VOO distribution ($1.8226 × 99.0463 = **$180.52**) was never credited. The core
   sleeve is structurally short ~1.07%/yr against any honest total-return benchmark. **A run cannot
   fix either 7 or 8.**
9. **STILL MISSING AND NOT RECOVERABLE:** the `journal.md` entry for **2026-11-13** and that day's
   ClickUp daily summary. The price leg was discharged (VOO 693.05, equity 98,644.05, core 69.59%,
   day −0.430%); **no seat has written, or should write, a backdated close-day narrative.**
10. ⚠⚠ **DO NOT MISREAD `delete-on-merge` AS A PUSH FAILURE.** An automation merges each session
   branch into `main` and **deletes the branch on merge**, so `git ls-remote --heads origin` will
   show your branch gone on every successful run and `git fetch origin <branch>` will fail with
   `couldn't find remote ref` — while `commit.py` correctly reported `"pushed": true`.
   ⚠ **THE CORRECT CHECK IS `git merge-base --is-ancestor <sha> origin/main`, NOT whether your
   branch still exists on the remote.** A seat that checks for its own branch may raise a false
   push-failure incident, which would put a bogus SYSTEMIC alert in front of the human.
11. ⚠ **PATH LABEL — affects anyone re-running the thesis grep.** The research archives live at
   **`archive/research_log/2026-09.md`** and **`archive/research_log/2026-10.md`**. Earlier states
   abbreviated these as `archive/2026-09` / `archive/2026-10`, which **does not resolve as a
   path** — a seat pasting it will silently get zero and under-count by 216.
12. **NEW — the priced-in window finding in full is above and in `research_log.md`
   `T-2026-11-18-01`/`-02`.** Carry the operational rule: **a `priced_in: false` read taken before
   the first post-catalyst session is unperformed, not passed**, and the `revalidate` handoff to
   the 09:35 seat is the only place that test can be run. **Separately, the filter is
   direction-blind (`abs(move) > 4`); that is for the human to fix in code, NOT a licence to
   override a `true` verdict.**

## ⚠⚠⚠ Corpus size — the standing systemic finding, for the human

Live memory corpus ~**1.32MB**, read by every run. **`positions.md` is ~337KB describing an empty
ledger** and `weekly_review.md` is 379KB. **Neither is reachable by the monthly rollover** —
`positions.md` is excluded on the premise that it "only ever holds open positions", which has been
false for 77 days. **`positions.md` needs a retention rule from the human; no run has standing to
truncate it.** Full write-up: `weekly_review.md`, week ending 2026-11-13, Recurring Error 1.
⚠ This seat **claims no collapse ratio** — the line count is the wrong instrument and every
"collapsed N → M" figure in that file is measured with it.

⚠ **Second standing item, same reviewer — AND THIS SEAT ACTED ON IT RATHER THAN RE-REPORTING IT.**
The agent-authored rejection taxonomy ("rule (iii)" … "rule (viii)") carries the majority of the
rejection load and **exists nowhere in `strategy.md`**, so a reader cannot tell which rejections
rest on the strategy and which rest on rules the system wrote for itself. **This seat wrote all
five of its rejections in §3/§4's own language — part 1/2/3/4, priced-in, correlation, universe —
and named prior findings by DATE AND CONTENT instead of by number.** ⚠ **That is one seat's
response to the ask, not a decision the human has made, and it binds no later seat.** The
underlying choice is still theirs: **promote the taxonomy into §4 or rename it so the distinction
is visible from the page.**

⚠ **Both items remain with the human in `weekly_review.md`. This seat sent NO notification** —
nothing was owed, nothing was missed, no incident is open, and re-pinging a standing item daily
trains the human to ignore the channel.
