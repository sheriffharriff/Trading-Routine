---
description: Stop the agent from trading — sets TRADING_ENABLED to false in control.md.
---

Halt trading.

`control.md` is human-owned and the routines are forbidden from writing it, but this command
runs on the human's behalf, so editing it here is correct.

1. Read `control.md`.

2. Set `TRADING_ENABLED: false` in the settings block. Change nothing else — leave
   `HALT_CLEARED_AT` and the notes exactly as they are.

3. If the user gave a reason with the command (`/halt earnings week, sitting this one out`),
   add it as a dated bullet under `## Notes` so the next run knows why it is halted. A halt
   with no recorded reason is one you will be puzzled by in three weeks.

4. Confirm what changed, and state clearly what this does and does not do:

   - **Does:** stop all new orders. `buy` and `sell` will print intended orders and submit
     nothing. Every routine still runs, researches, journals, and commits.
   - **Does not:** close existing positions. They stay open and unmanaged in the sense that
     no exit can execute — including stop-losses. §5.3 and §5.4 will be evaluated and
     reported but cannot act.

   That second point is the one that matters. Say it explicitly. A halted system holding
   losing positions still holds them.

5. Do not commit unless the user asks. If they do, use
   `git add control.md && git commit -m "control: halt trading" && git push origin main`
   directly — **not** `scripts/commit.py`, which is built to revert exactly this change.
