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
plan_date: 2026-10-02
generated_by: 1-premarket-research
market_open_today: yes
```

Market opens today **2026-10-02 at 09:30 ET** (`alpaca.py clock` at 08:23:38 ET: `is_open:
false`, `next_open: 2026-10-02T09:30:00-04:00`, `next_close: 2026-10-02T16:00:00-04:00`).
**Not a holiday** — the market is closed because it is pre-market and `next_open` points at
**today**. ⚠ **Read the date, not the boolean. FALSE has three meanings — pre-market,
post-bell, holiday — and TRUE has one.** ⚠ **Corroborated independently from the data plane:
`bars` returns a complete 2026-10-01 bar and NO bar dated 2026-10-02 — the pre-market shape,
confirmed rather than assumed.**

**One pre-market run today, at 08:23–08:26 ET.** Selftest passed all five checks
(`trading_enabled: true`, LIVE paper account, broker equity **$99,865.29** at pre-flight).

⚠ **This file arrived carrying `plan_date: 2026-10-01` — ONE CALENDAR DAY OLD AND CORRECTLY
SO**, because yesterday's pre-market run wrote it and all four of yesterday's routines
committed (`git log`: the 10-01 close is `ffacda0`, merged as `2b98666`). ⚠ **The 09-28 gap
therefore remains a ONE-DAY, THREE-ROUTINE event and is still NOT reported as ongoing.**
⚠ **THE STALENESS GATE STILL HAS NOT BEEN TESTED. The count will be 32 after today's open** —
it is exercised once per market-open run and has never fired, because it has never met a plan
whose date was not today. **Its alert path remains untested code.** ⚠ **AND THE REASON IT
MATTERS, RESTATED BECAUSE TODAY'S PLAN IS AGAIN EMPTY: A FRESH EMPTY PLAN AND A STALE PLAN
PRODUCE A BYTE-FOR-BYTE IDENTICAL ZERO-ORDER RUN. Freshness must be read OFF `plan_date` and
NEVER inferred from the outcome.** This plan is **fresh and deliberately empty**.

---

## Tape context

Yesterday's **official** VOO close, from `bars --adjustment all` on a **completed** session
and **pulled fresh by this run rather than inherited**, is **702.255** (o 702.95, h 703.43,
l 697.50). The two prior sessions on the same basis: **09-30 700.605**, **09-29 702.27**.

⚠ **THE "A COMPLETED BAR IS NOT IMMUTABLE IN `n`/`v`" ITEM GETS A SECOND INSTANCE, AND IT IS
A CLEAN REPLICATION OF 10-01's.** The 2026-10-01 bar read **n 1633 / v 51892** to yesterday's
close run and reads **n 1634 / v 51893** on this run's fresh pull — **while its close held at
702.255 to the cent.** ⚠ **Late-reported prints keep arriving after the bell, so `n` and `v`
drift on a bar that is genuinely complete. They are not merely a weak completeness signal —
they are not STABLE, so no run may use "v is low" or "v changed" as evidence in either
direction. The CLOSE is the stable field; the CLOCK is the reliable discriminator.**
⚠ **Noted: this also means the n/v FLOOR test's own inputs drift. Today's bar clears the
previously recorded floors (1,450 / 43,730) either way, and no mark is due, so nothing turns
on it — but the floor test is a corroborant built on a moving ruler, which weakens it further.**

⚠⚠ **EVERY VOO CLOSE OLDER THAN 2026-09-28 EXISTS ON TWO BASES AND THEY ARE NOT
INTERCHANGEABLE.** VOO went ex-dividend 09-28; `--adjustment all` rescaled every prior close
by **0.997432**, while `--adjustment raw` and `--adjustment split` return the original prints.
⚠ **09-28 onward agree to the cent on both bases, because the ex-date lies at or before them —
the divergence is entirely in the sessions BEFORE it.** ⚠ **The 09-03 core fill at 706.74 is a
RAW print. NAME THE BASIS IN THE SENTENCE OR DO NOT WRITE THE SENTENCE.**

**On the 10-01 official close:** equity **$99,555.77**, core **$69,555.77 = 69.8661%**, cash
**30.1339%**. ⚠ **RE-DERIVED FROM A FRESH `positions` PULL THIS RUN, NOT CARRIED: qty
99.046311231 × 702.255 + $30,000 reproduces yesterday's close figure to the cent, so it is a
CHECKED fact rather than an inherited one.**
**On the 08:23 broker mark:** equity **$99,856.37**, core **$69,856.37 = 69.96%**, cash
**30.04%**, `rebalance_delta` **+$43.09**. ⚠ **These two figures must never be differenced —
the 09-30 close run supplied the worked instance, where differencing a broker mark against an
official close understated a real −$164.91 day as −$51.50, a threefold error.**

⚠⚠ **THE PRE-MARKET BASIS TRAP WAS WALKED UP TO AND DECLINED FOR A SECOND CONSECUTIVE
MORNING, WHICH MAKES IT A REPLICATION RATHER THAN A ONE-OFF:** core `current_price` reads
**705.29**, i.e. **+$3.035 above the 702.255 official close** — larger than 10-01's +$2.915 and
roughly TRIPLE the largest of the ten catalogued post-bell gaps (range −$0.97 to +$1.145).
⚠ **IT MUST NOT BE ADDED TO THAT SERIES.** Those ten are all **POST-BELL** observations; this
is a **PRE-MARKET** indication. Appending it would manufacture a spurious "largest gap on
record" that is an artifact of **mixing two different times of day**, not of any widening.
⚠ **DIFFERENT HOUR, DIFFERENT SERIES. The post-bell series still has ten members and its
largest is still +$1.145.** ⚠ **And note what is NOT claimed: two consecutive large pre-market
gaps are not a "pre-market series" either — there are two observations and no basis for a range.**

⚠ **`lastday_price` reads 702.35 against the official 702.255 close — a +$0.095 gap. That is
the SETTLED finding, not a new one:** `last_equity`-style artifacts are `lastday_price` not
being the official close, propagated through one multiplication. ⚠ **STOP PREDICTING WHY IT
DIFFERS; DO NOT RE-OPEN IT.** The field stays unusable as a day's P&L for a now-NAMED reason.

⚠ **THE INTRADAY-DRIFT ITEM GETS A TENTH INSTANCE:** `selftest` reported **$99,865.29** at
08:23 and `sleeves` returned **$99,856.37** seconds later — an **$8.92** spread. ⚠ **Well
inside the established $1.97–$216.91 range and therefore NOT evidence of anything narrowing.**
⚠ **An equity figure is only meaningful with its CALL and its TIMESTAMP attached.**
⚠ **This bites §6's 5% sizing cap, which is computed against live equity — 5% of the 08:23
mark is $4,992.82 (against $4,977.79 on the official close). IT HAS NO OPERAND TODAY, because
this plan carries no BUY intent — and it has never had one in this account's history.**

---

## Sleeves and the rebalance question

| Sleeve | Value (08:23 broker) | % | Target | In band? |
|---|---:|---:|---:|---|
| Core (VOO) | $69,856.37 | **69.96%** | 70% | **yes** (65–75) |
| Satellite | $0.00 | **0.00%** | 30% | n/a — empty |
| Cash | $30,000.00 | **30.04%** | — | §2 permits idle satellite cash |

**NO REBALANCE IS DUE, ON EITHER BASIS.** Core sits **4.96 points** inside the 65% edge on
the broker mark (**4.87** on the official close). ⚠ **Do NOT act on `rebalance_delta: +$43.09`:
§2 rebalances at the BAND EDGE, not toward the 70% target. It is a DISTANCE READOUT, NOT AN
INSTRUCTION.** ⚠ **`rebalance_delta` is now POSITIVE for an ELEVENTH consecutive run. That is
NOT the sign-instability defect resolving — the same quantity disagreed in sign on 09-24.**
**Fifty-seventh consecutive run inside 69.59–70.22%.**

**⚠⚠ CHECK `cash`. IT READ EXACTLY $30,000.00 AGAIN AT 08:23 — A FOURTEENTH READING, NOW ON
THE FIFTH CALENDAR DAY SINCE VOO's 09-28 EX-DATE. DAY 5 OF 8.** ⚠ **Fourteen readings across
five days are ONE unresolved observation of an unpaid dividend, not fourteen data points.**
⚠ **NON-ARRIVAL THIS EARLY IS STILL EXPECTED, NOT EVIDENCE — settlement runs on the PAY date,
not the ex-date, and no reading's HOUR makes it stronger, because settlement does not run on
the bell.** **The falsifiable test, written in advance and still running: `cash` should rise to
~$30,180.45. IF IT HAS NOT BY 2026-10-07, the paper account does not model dividends at all —
in which case the book structurally under-earns its own benchmark by VOO's entire ~1.0% annual
yield and §1's "beat the S&P TOTAL RETURN" is unwinnable BY CONSTRUCTION rather than by
strategy.** ⚠ **That is a finding for the human, not something any run may fix.** The implied
~$180.45 credit is an **INFERENCE** — Alpaca does not publish the figure — and must stay
labelled as one.

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

⚠⚠ **ABSENT IS NOT PASSING, AND §5 HAS NEVER HAD AN OPERAND IN THIS ACCOUNT'S HISTORY** — 22
completed sessions since 2026-09-01, 19 after the 09-03 core fill, zero satellite positions
ever. ⚠ **The counter is NOT advanced by this run: at 08:23 the market has not opened, so
today is not a completed session and a pre-market seat has none of today's to add (catch 11).**
⚠ **The refusal was AVAILABLE and TAKEN here, which is the strong form — a pre-market seat is
one of the two the catch names as exposed.**

---

## Intents

### BUY — none

**NOTHING IS TO BE BOUGHT TODAY.** ⚠ **THIS IS A RESULT, NOT AN EMPTY SEARCH, AND THE
DISTINCTION IS LOAD-BEARING: every gate was OPEN.** Breaker **INACTIVE**; week **0 of 3**
under §6's cap; satellite sleeve **entirely empty** with **30.04% idle cash**; **$4,992.82** of
headroom under the 5% cap; `control.md` notes **(none)**; `TRADING_ENABLED: true`.
**Nothing blocked a purchase. The research produced nothing that satisfied §4.**

**Five candidates were screened and all five were rejected** — see `research_log.md`
T-2026-10-02-01 through -05. **Where they died:**

| ID | Candidate | Durable kill |
|---|---|---|
| T-2026-10-02-01 | RTX / SM-6 $24.4B Navy award | **Part 1 — no counterparty named anywhere** (rule (v)); RTX itself first-order |
| T-2026-10-02-02 | ORCL / Tencent ~$7B AI-chip lease | **Structure** — ORCL is first-order; **and the deal leases ALREADY-INSTALLED hardware, so no second tier is touched**; figure unconfirmed |
| T-2026-10-02-03 | Venture Global / ConocoPhillips LNG SPA | **Part 3 — first delivery 2030**, ~16 quarters out; part 2 (no value disclosed) and structure kill it independently |
| T-2026-10-02-04 | DKS / Nike's competitors | **Part 1 — "and also" construction**, no named beneficiary; part 2 immaterial; **sign wrong for a long** |
| T-2026-10-02-05 | MU fiscal Q4 / Q1 guide | **Already disposed 10-01; deliberately NOT re-screened.** Two fresh directions killed on sign and on part 1 |

⚠⚠ **ZERO `move` CALLS WERE MADE THIS RUN. THAT IS AN *ABSENT* CHECK, NOT A SKIPPED ONE** —
every candidate died on structure, part 1, part 2 or part 3 **before an eligible ticker was
reached.** ⚠ **"The filter did not fire" and "the filter had nothing to fire on" look identical
in a run summary and are not the same thing.** **Second instance; 09-29 was the first.**

⚠⚠ **THE DEFENCE-AWARD FINDING NOW HAS FOUR INSTANCES ACROSS THREE PRIMES AND THREE PROGRAMS**
(09-29 AMRAAM $20.7B RTX · 09-30 F/A-XX >$20B Boeing · 10-02 SM-6 $24.4B RTX). **ONE funnel
query was spent and NO re-query was issued**, per the standing instruction. The source
volunteered the epistemic rule itself: *"Any attribution of SM-6 revenue to other defense
companies would be an inference rather than a disclosed allocation."* ⚠ **A US defence program
award cannot produce a §4 candidate. The cause is disclosure practice, not an under-searched
funnel.**

### SELL — none

**No satellite positions exist.** §5.1 and §5.2 were evaluated and have **NO OPERAND**; §5.3's
distance is **UNDEFINED** and §5.4 is **NOT ARMED**. ⚠ **Core VOO is exempt from all four (§5)
and is never a SELL candidate — §7 forbids selling core to fund satellite trades, and a
`highest_close` on core would fabricate a §5.4 trailing stop on the one position the strategy
exempts.** **Sixty-fifth consecutive refusal to stamp a mark on core.**

### REBALANCE — none

Core **69.96%** on the 08:23 broker mark, **69.8661%** on the 10-01 official close. **Both are
inside §2's 65–75% band**, with 4.96 points of room to the lower edge. **No REBALANCE intent.**

---

## For the market-open run

1. **Re-read `plan_date` above and confirm it is 2026-10-02 before acting on anything.** This
   plan is fresh and **deliberately empty of BUY intents**. ⚠ **A fresh empty plan and a stale
   plan produce an identical zero-order run — read freshness OFF the field, never off the
   outcome.** If the gate fires, that is new information and its alert path has never run.
2. **There is nothing to execute.** No BUY, no SELL, no REBALANCE. The correct outcome at 09:35
   is **zero orders**, and it follows from the PLAN, not from a guardrail. ⚠ **DO NOT GENERATE
   AN INTENT AT THE OPEN. That seat has no funnel and may only execute what was written before
   the bell; a position opened at 09:35 without a plan entry routes AROUND the discipline
   rather than satisfying it.**
3. **`revalidate` lines: NONE, because there is no BUY intent to revalidate.** ⚠ **Recorded
   explicitly so the absence is not mistaken for an omission.**
4. **Check `cash` and report it.** Expect **exactly $30,000.00** — **day 5 of 8** on the
   dividend test. ⚠ **A reading of $30,000.00 resolves nothing in either direction; only the
   2026-10-07 deadline does.** If it reads ~$30,180, **say so loudly** — the test has resolved
   in the account's favour and §1 is winnable after all.
5. **Confirm the sleeve band before touching anything.** Core should still be ~69.8–70.0%. ⚠ **If
   it has moved outside 65–75% on the open, §2 acts at the BAND EDGE — and `rebalance_delta` is
   a distance readout, not an instruction.**
6. ⚠ **A BAR DATED TODAY IS PARTIAL WHILE THE MARKET IS OPEN AND ITS `c` FIELD IS THE LAST
   TRADE WEARING A CLOSE'S CLOTHES.** 10-01's midday run proved the mechanism: `c` 700.35 equalled
   `latestTrade.p` 700.35 to the cent. **No `bars` close may be stamped as a mark before the
   bell on any basis**, and `n`/`v` cannot tell you otherwise — they are not even stable on a
   bar that is genuinely complete (see Tape context, second instance today).
7. ⚠ **GNRC IS NOT YOURS TO LOOK AT.** It is the **named counterparty** in the Amazon
   announcement — **first-order, outside §4 at any price.** ⚠ **And note the honest grading: in
   the 09:35 seat this refusal is STRUCTURALLY UNAVAILABLE to violate, because that seat has no
   funnel at all. A refusal that could not have been violated is not evidence of restraint.**
8. **Today's scheduled macro is the September payrolls release** (consensus ~85–94k vs 162k in
   August, unemployment ~4.1%), landing around the open. ⚠ **NO INTENT DEPENDS ON IT, and it is
   NOT a reason to trade.** It is noted only so the open run is not surprised by an unusually
   wide spread or a gappy first print. ⚠ **A macro release is not a §4 catalyst — there is no
   Company A and no segment revenue line to size.**
