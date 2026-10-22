#!/usr/bin/env python3
"""Render the Docsify _sidebar.md from site/navigation.json (stdlib only).

Usage:
  python scripts/generate_sidebar.py          # update the published menu
  python scripts/generate_sidebar.py --check  # verify generated menu is current

Planned/drafting entries remain in the registry but are not emitted. This is
navigation hiding, NOT access control: everything committed to a public
repository can still be opened directly by URL.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "site" / "navigation.json"
SIDEBAR = ROOT / "_sidebar.md"
STATUSES = {"planned", "drafting", "ready", "published"}
HEADER_PATTERN = re.compile(r"^[A-Z0-9 &/\-]+$")
NO_MARKDOWN = re.compile(r"[\[\]\r\n]")


def fail(message: str) -> None:
    raise ValueError(message)


def assert_link(path: str, label: str, *, published: bool) -> None:
    if not isinstance(path, str) or not path.startswith("/"):
        fail(f"{label}: path must begin with '/'")
    if path == "/":
        return
    if ".." in Path(path).parts or "\\" in path or not path.endswith(".md"):
        fail(f"{label}: expected an internal .md route without traversal: {path!r}")
    if published:
        target = ROOT / path.lstrip("/")
        if not target.is_file():
            fail(f"{label}: published target missing: {path}")


def render(catalog: dict) -> str:
    if catalog.get("schema_version") != 1:
        fail("site/navigation.json: unsupported schema_version")
    sections = catalog.get("sections")
    if not isinstance(sections, list):
        fail("site/navigation.json: sections must be a list")

    output = []
    ids = set()
    for section in sections:
        if not isinstance(section, dict):
            fail("Every section must be an object")
        title = section.get("title")
        sid = section.get("id")
        status = section.get("status")
        if not isinstance(sid, str) or not re.fullmatch(r"[a-z0-9-]+", sid):
            fail(f"Invalid section id: {sid!r}")
        if sid in ids:
            fail(f"Duplicate section id: {sid}")
        ids.add(sid)
        if not isinstance(title, str) or not HEADER_PATTERN.fullmatch(title):
            fail(f"{sid}: header must be uppercase plain text: {title!r}")
        if status not in STATUSES:
            fail(f"{sid}: invalid status: {status!r}")
        items = section.get("items")
        if not isinstance(items, list):
            fail(f"{sid}: items must be a list")
        published_items = []
        for item in items:
            if not isinstance(item, dict):
                fail(f"{sid}: item must be an object")
            label, path, item_status = item.get("label"), item.get("path"), item.get("status")
            if not isinstance(label, str) or not label or NO_MARKDOWN.search(label):
                fail(f"{sid}: invalid item label: {label!r}")
            if item_status not in STATUSES:
                fail(f"{sid}/{label}: invalid status {item_status!r}")
            if status != "published" and item_status == "published":
                fail(f"{sid}/{label}: item cannot be published inside an unpublished section")
            visible = status == "published" and item_status == "published"
            assert_link(path, f"{sid}/{label}", published=visible)
            if visible:
                published_items.append(f"  - [{label}]({path})")

        if status == "published":
            if not published_items:
                fail(f"{sid}: a published section must contain published links")
            output.append(f"- **{title}**\n" + "\n".join(published_items))
    return "\n".join(output) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if sidebar is not up to date")
    args = parser.parse_args()

    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        expected = render(catalog)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Navigation validation failed: {exc}", file=sys.stderr)
        return 1

    previous = SIDEBAR.read_text(encoding="utf-8") if SIDEBAR.exists() else ""
    if args.check:
        if previous != expected:
            diff = difflib.unified_diff(
                previous.splitlines(keepends=True),
                expected.splitlines(keepends=True),
                fromfile="_sidebar.md (committed)",
                tofile="_sidebar.md (generated)",
            )
            print("".join(diff), file=sys.stderr)
            print("Run: python scripts/generate_sidebar.py", file=sys.stderr)
            return 1
        print("Navigation OK: published pages exist; planned entries remain hidden.")
        return 0

    if previous == expected:
        print("Sidebar unchanged; generated navigation is current.")
    else:
        SIDEBAR.write_text(expected, encoding="utf-8")
        print("Updated _sidebar.md from site/navigation.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
