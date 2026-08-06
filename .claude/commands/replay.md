---
description: Dry-run a routine locally — full logic, no orders, no commit. Usage: /replay 1
---

Replay a routine without touching the account or the repo history.

The argument is which routine to run: `1`–`5`, or a name fragment like `premarket`,
`open`, `midday`, `close`, `weekly`. If no argument was given, list the five and ask which.

**Before running anything**, check `TRADING_ENABLED` in `control.md`:

- If it is `false`, the scripts already refuse to submit orders. Safe to proceed.
- If it is `true`, **stop and tell the user**. A replay of the market-open routine with
  trading enabled will place real paper orders — real in the sense that they hit the
  account, fill, and land in the ledger, which is exactly what a replay is meant to avoid.
  Offer to set it to `false` first, and wait for an answer.

Then:

1. Read `routines/<n>-*.md` in full.

2. Follow it exactly as a scheduled run would — including reading every memory file it
   names. The point is to exercise the real path, not a summary of it.

3. **Two deviations, and only these two:**
   - Do not run `scripts/commit.py`. Nothing gets committed or pushed.
   - Do not post anything to ClickUp. Show the summary it *would* have posted.

4. Write file changes normally, so the user can inspect the diff. Report `git status` and
   `git diff --stat` at the end so it is obvious what the run touched.

5. Report what happened, and separately, **what would have been different in a real run** —
   orders that would have been submitted, the ClickUp task that would have been created,
   the commit message.

6. Remind the user that the working tree now has uncommitted changes from the replay, and
   that `git checkout -- .` discards them. A replay left in the tree will otherwise be
   picked up and committed by the next real run as though it had happened today.
