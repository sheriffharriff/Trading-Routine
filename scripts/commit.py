#!/usr/bin/env python3
"""Commit and push the run's work, protecting the human-owned files.

  python scripts/commit.py --routine 1-premarket-research \
      --message "premarket: 3 theses, 1 accepted, plan written" \
      [--summary-file /tmp/run-summary.md]

Two invariants have to hold at the same time, and naively they conflict:

  1. strategy.md and control.md are human-owned. The agent never writes them.
  2. Every run must push, or the next run starts blind and the work is gone.

So a violation does not abort the commit. The protected paths are reverted
surgically -- `git checkout HEAD -- <path>`, those paths only, never a broad
reset that would discard legitimate work on agent-owned files alongside them --
and everything else is committed and pushed normally. The violation is reported
loudly rather than being paid for with the run's output.

Adding a protected file that does not yet exist in HEAD is allowed: that is the
initial commit of the file, not an edit to it.
"""

import argparse

import common as c

GIT_IDENTITY = ("-c", "user.name=trading-agent", "-c", "user.email=agent@local")
DIFF_LIMIT = 4000


def has_head():
    return c.git("rev-parse", "--verify", "HEAD")[0] == 0


def tracked_in_head(path):
    return c.git("cat-file", "-e", f"HEAD:{path}")[0] == 0


def current_branch():
    """The branch this run is on. Empty string if HEAD is detached."""
    code, out, _ = c.git("rev-parse", "--abbrev-ref", "HEAD")
    if code != 0 or out in ("", "HEAD"):
        return ""
    return out


def staged_files():
    return [line.strip() for line in c.git("diff", "--cached", "--name-only")[1].splitlines()
            if line.strip()]


def enforce_protected(routine):
    """Revert any staged change to a human-owned file. Returns the violations."""
    violations = []
    if not has_head():
        return violations

    staged = staged_files()
    for path in c.PROTECTED_FILES:
        if path not in staged:
            continue
        if not tracked_in_head(path):
            continue          # first-time add of the file itself, not an edit
        diff = c.git("diff", "--cached", "--", path)[1]
        if not diff.strip():
            continue
        c.git("checkout", "HEAD", "--", path)
        violations.append({"file": path, "diff": diff[:DIFF_LIMIT],
                           "truncated": len(diff) > DIFF_LIMIT})
    return violations


def report_violations(violations, routine):
    for violation in violations:
        path = violation["file"]
        detail = (
            f"`{path}` was modified during this run and has been reverted from HEAD "
            f"before committing. The rest of the run's work was committed and pushed "
            f"normally.\n\n"
            f"**Reverted diff:**\n\n```diff\n{violation['diff']}\n```"
            + ("\n\n_(diff truncated)_" if violation["truncated"] else "")
        )
        try:
            import clickup
            clickup.alert(
                key=f"guard-violation:{path}",
                title=f"Guard violation - {path} was modified by a routine",
                detail=detail,
                routine=routine,
            )
        except BaseException:
            # The alert helper exits non-zero on its own failures, so the exception
            # itself carries no detail worth printing. Say what was lost instead.
            print(f"WARNING: guard-violation alert for {path} could not be posted to "
                  f"ClickUp; the revert still happened and is recorded in this run's "
                  f"output and commit message", flush=True)


def do_commit(message):
    c.git("add", "-A")
    if not staged_files():
        return False, "nothing to commit"
    code, out, err = c.git(*GIT_IDENTITY, "commit", "-m", message)
    if code != 0:
        return False, err or out
    return True, out


def do_push(routine, message, summary):
    """Rebase onto the run's own branch then push. One retry, then alert.

    The branch is whatever the run was started on -- routine sessions get a
    per-session branch, not main -- so it is read from HEAD rather than named
    here. A branch that does not exist on the remote yet is created by the push;
    the pull before it simply finds nothing to rebase onto.

    Concurrency is not really expected -- the five routines never overlap -- but
    a rebase costs nothing and turns a rejected push into a resolved one.
    """
    branch = current_branch()
    if not branch:
        last_error = "HEAD is detached; there is no branch to push to"
    else:
        for attempt in (1, 2):
            c.git("pull", "--rebase", "origin", branch)
            code, out, err = c.git("push", "origin", branch)
            if code == 0:
                return True, out
            last_error = err or out
            if attempt == 1:
                print(f"push failed, retrying once: {last_error}", flush=True)

    target = f"`{branch}`" if branch else "its branch"
    detail = (
        f"Routine `{routine}` could not push to {target}. Everything it "
        f"learned this run is committed locally in a container that is about to be "
        f"destroyed, so treat the content below as the only surviving copy.\n\n"
        f"**Commit message:** {message}\n\n"
        f"**Git error:**\n\n```\n{last_error}\n```\n\n"
    )
    if summary:
        detail += f"---\n\n**Run summary:**\n\n{summary}\n"

    try:
        import clickup
        clickup.alert(key="push-failure",
                      title=f"Push to {branch or 'branch'} failed - run output at risk",
                      detail=detail, routine=routine)
    except BaseException:
        print("WARNING: the push-failure alert could not be posted to ClickUp either. "
              "This run's output exists only in this container and will be lost when it "
              "is destroyed. The summary follows:\n\n" + (summary or "(no summary provided)"),
              flush=True)

    return False, last_error


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--routine", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--summary-file")
    args = parser.parse_args()

    summary = ""
    if args.summary_file:
        try:
            with open(args.summary_file, encoding="utf-8") as handle:
                summary = handle.read()
        except OSError:
            summary = ""

    c.git("add", "-A")
    violations = enforce_protected(args.routine)
    if violations:
        report_violations(violations, args.routine)
        c.git("add", "-A")          # pick up the alerts.md the report just wrote

    message = args.message
    if violations:
        files = ", ".join(v["file"] for v in violations)
        message += f"\n\nGUARD: reverted unauthorised changes to {files}"

    committed, commit_detail = do_commit(message)
    pushed, push_detail = do_push(args.routine, message, summary)

    result = {
        "ok": pushed,
        "routine": args.routine,
        "et": c.et_stamp(),
        "committed": committed,
        "commit_detail": commit_detail,
        "pushed": pushed,
        "push_detail": push_detail,
        "guard_violations": [v["file"] for v in violations],
    }
    if violations:
        result["guard_note"] = ("human-owned files were reverted before committing; "
                                "the rest of the run's work was preserved")
    if not pushed:
        result["warning"] = ("PUSH FAILED - the next run will start without this run's "
                             "work. A ClickUp alert carries the summary.")
    c.emit(result, 0 if pushed else 1)


if __name__ == "__main__":
    main()
