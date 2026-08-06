#!/usr/bin/env python3
"""ClickUp client: daily summaries and deduplicated operational alerts.

Usage:
  python scripts/clickup.py ping
  python scripts/clickup.py create-task --name "2026-08-05 - Daily Trading Summary" \
      --file summary.md
  python scripts/clickup.py comment --task-id abc123 --file note.md
  python scripts/clickup.py find-open --contains "Circuit breaker active"
  python scripts/clickup.py alert --key circuit-breaker \
      --title "Circuit breaker active" --file detail.md [--routine 4-market-close]

Alert policy, implemented once here so no routine reimplements it:

  * One ClickUp task per incident, never one per run. A condition that persists
    across runs gets a comment on the existing task.
  * Titles are "[ALERT] YYYY-MM-DD - <title>", visually distinct from the daily
    summaries while still sorting alongside them by date.
  * --title must be STABLE across runs, with no dates or counts inside it. It is
    the dedupe key on the ClickUp side, and a title that changes each run would
    create a new task every run, which is the exact behaviour this prevents.

Dedupe is resolved by querying ClickUp rather than by reading a local file. That
is forced by the push-failure case: an alert about a failed push cannot look up
its own history in a repo whose push just failed. Since that path needs a remote
lookup anyway, all incidents use it rather than maintaining two mechanisms that
would drift apart.
"""

import argparse
import re

import common as c

ALERT_PREFIX = "[ALERT]"


def _headers():
    env = c.require("CLICKUP_API_TOKEN")
    return {"Authorization": env["CLICKUP_API_TOKEN"]}


def _list_id():
    return c.require("CLICKUP_LIST_ID")["CLICKUP_LIST_ID"]


def ping():
    status, payload = c.http("GET", f"{c.CLICKUP_API}/list/{_list_id()}", headers=_headers())
    if not c.ok(status):
        c.fail("could not read the ClickUp list", status=status, response=payload)
    return {"ok": True, "list_id": payload.get("id"), "list_name": payload.get("name")}


def create_task(name, markdown, tags=None):
    body = {"name": name, "markdown_description": markdown}
    if tags:
        body["tags"] = tags
    status, payload = c.http("POST", f"{c.CLICKUP_API}/list/{_list_id()}/task",
                             headers=_headers(), body=body)
    if not c.ok(status):
        # Older ClickUp lists reject markdown_description; plain text still gets
        # the summary in front of the human, which matters more than formatting.
        body.pop("markdown_description", None)
        body["description"] = markdown
        status, payload = c.http("POST", f"{c.CLICKUP_API}/list/{_list_id()}/task",
                                 headers=_headers(), body=body)
    if not c.ok(status):
        c.fail("could not create ClickUp task", status=status, response=payload, name=name)
    return {"ok": True, "task_id": payload.get("id"), "url": payload.get("url"), "name": name}


def comment(task_id, text):
    status, payload = c.http("POST", f"{c.CLICKUP_API}/task/{task_id}/comment",
                             headers=_headers(), body={"comment_text": text})
    if not c.ok(status):
        c.fail("could not comment on ClickUp task", status=status, response=payload,
               task_id=task_id)
    return {"ok": True, "task_id": task_id, "comment_id": payload.get("id")}


def find_open(contains):
    """First non-closed task whose name contains `contains`. None if there is none."""
    status, payload = c.http("GET", f"{c.CLICKUP_API}/list/{_list_id()}/task",
                             headers=_headers(),
                             params={"archived": "false", "include_closed": "false",
                                     "subtasks": "true", "order_by": "created",
                                     "reverse": "true"})
    if not c.ok(status):
        c.fail("could not search the ClickUp list", status=status, response=payload)
    needle = contains.strip().lower()
    for task in (payload or {}).get("tasks", []):
        if needle in str(task.get("name", "")).lower():
            return task
    return None


# --------------------------------------------------------------------------
# alerts.md -- the local mirror and the escalation counter
# --------------------------------------------------------------------------

def read_ledger(key):
    """(occurrences, task_id) for an incident key already in alerts.md."""
    text = c.read_text("alerts.md")
    block = re.search(
        r"^###\s+" + re.escape(key) + r"\s*$(.*?)(?=^###\s|\Z)",
        text, re.S | re.M,
    )
    if not block:
        return 0, None
    body = block.group(1)
    occ = re.search(r"^-\s*occurrences:\s*(\d+)", body, re.M)
    tid = re.search(r"^-\s*clickup_task_id:\s*(\S+)", body, re.M)
    return (int(occ.group(1)) if occ else 0,
            tid.group(1) if tid and tid.group(1) not in ("-", "none") else None)


def write_ledger(key, task_id, occurrences, routine, detail, systemic):
    """Upsert the incident block under 'Open incidents' in alerts.md."""
    text = c.read_text("alerts.md")
    today = c.et_today().isoformat()
    existing = re.search(r"^###\s+" + re.escape(key) + r"\s*$(.*?)(?=^###\s|\Z)",
                         text, re.S | re.M)
    first_seen = today
    routines = routine or "unknown"
    if existing:
        prior = re.search(r"^-\s*first_seen:\s*(\S+)", existing.group(1), re.M)
        if prior:
            first_seen = prior.group(1)
        prior_routines = re.search(r"^-\s*routines:\s*(.*)$", existing.group(1), re.M)
        if prior_routines and routine and routine not in prior_routines.group(1):
            routines = f"{prior_routines.group(1).strip()}, {routine}"
        elif prior_routines:
            routines = prior_routines.group(1).strip()

    flat_detail = " ".join(str(detail or "").split())[:600]
    block = (
        f"### {key}\n"
        f"- first_seen:      {first_seen}\n"
        f"- last_seen:       {today}\n"
        f"- occurrences:     {occurrences}\n"
        f"- clickup_task_id: {task_id or '-'}\n"
        f"- routines:        {routines}\n"
        f"- status:          {'SYSTEMIC' if systemic else 'OPEN'}\n"
        f"- detail:          {flat_detail}\n\n"
    )

    if existing:
        text = text[:existing.start()] + block + text[existing.end():]
    else:
        text = text.replace("## Open incidents\n\n*(none)*",
                            "## Open incidents\n\n" + block.rstrip())
        if block not in text:   # placeholder already consumed by an earlier incident
            text = re.sub(r"(^## Open incidents\s*$)", r"\1\n\n" + block.rstrip(),
                          text, count=1, flags=re.M)
    c.write_text(text, "alerts.md")


def alert(key, title, detail, routine=None):
    """Create or update the single ClickUp task for this incident.

    Escalation: a guard violation seen more than once for the same file stops
    being an incident and is reported as SYSTEMIC. One accidental write to a
    protected file is a slip; the same routine reaching for the same file across
    runs means a prompt is steering it wrong, which is a bug to fix rather than
    an event to keep logging.
    """
    occurrences, known_task = read_ledger(key)
    occurrences += 1
    systemic = key.startswith("guard-violation") and occurrences > 1

    task_name = f"{ALERT_PREFIX} {c.et_today().isoformat()} - {title}"
    if systemic:
        task_name = f"{ALERT_PREFIX} SYSTEMIC {c.et_today().isoformat()} - {title}"

    body = (
        f"**Incident:** `{key}`\n\n"
        f"**Routine:** {routine or 'unknown'}\n\n"
        f"**Time:** {c.et_stamp()}\n\n"
        f"**Occurrence:** {occurrences}\n\n"
    )
    if systemic:
        body += (
            "> **SYSTEMIC — this is the "
            f"{occurrences}{'nd' if occurrences == 2 else 'th'} occurrence.**\n"
            "> A single accidental write to a protected file is a slip. Repeated attempts\n"
            f"> by `{routine or 'a routine'}` mean its prompt is steering it toward a file\n"
            "> it must never touch. Fix the prompt rather than clearing this alert.\n\n"
        )
    body += f"---\n\n{detail}\n"

    existing = find_open(title)
    if existing:
        comment(existing["id"], body)
        task_id, action = existing["id"], "commented"
    else:
        created = create_task(task_name, body)
        task_id, action = created["task_id"], "created"

    write_ledger(key, task_id, occurrences, routine, detail, systemic)
    return {"ok": True, "action": action, "task_id": task_id, "key": key,
            "occurrences": occurrences, "systemic": systemic}


def _read_file_arg(path, inline):
    if inline:
        return inline
    if not path:
        c.fail("provide --file or --text")
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError as exc:
        c.fail(f"could not read {path}: {exc}")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("ping")

    p = sub.add_parser("create-task")
    p.add_argument("--name", required=True)
    p.add_argument("--file")
    p.add_argument("--text")

    p = sub.add_parser("comment")
    p.add_argument("--task-id", required=True)
    p.add_argument("--file")
    p.add_argument("--text")

    p = sub.add_parser("find-open")
    p.add_argument("--contains", required=True)

    p = sub.add_parser("alert")
    p.add_argument("--key", required=True,
                   help="stable incident key, e.g. push-failure or guard-violation:control.md")
    p.add_argument("--title", required=True,
                   help="stable title with NO dates or counts inside -- this is the dedupe key")
    p.add_argument("--file")
    p.add_argument("--text")
    p.add_argument("--routine")

    args = parser.parse_args()
    try:
        if args.cmd == "ping":
            c.emit(ping())
        elif args.cmd == "create-task":
            c.emit(create_task(args.name, _read_file_arg(args.file, args.text)))
        elif args.cmd == "comment":
            c.emit(comment(args.task_id, _read_file_arg(args.file, args.text)))
        elif args.cmd == "find-open":
            found = find_open(args.contains)
            c.emit({"ok": True, "found": bool(found),
                    "task_id": found.get("id") if found else None,
                    "name": found.get("name") if found else None})
        elif args.cmd == "alert":
            c.emit(alert(args.key, args.title, _read_file_arg(args.file, args.text),
                         args.routine))
    except c.ApiError as exc:
        c.fail(str(exc))


if __name__ == "__main__":
    main()
