#!/usr/bin/env python3
"""Audit all published Markdown for empty content, malformed fences and local 404s.

Zero dependencies. Run: python3 scripts/audit_published_docs.py

This confirms structural integrity only, not tool/command correctness
or whether external websites are still reachable.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
CONTENTS = ("collector", "examiner", "docs", "osint", "playbooks", "snippets")
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
HTML_LINK = re.compile(r'''(?:href|src)\s*=\s*["']([^"']+)["']''', re.I)
FENCE = re.compile(r'^\s*([\x60]{3,}|~{3,})([^\r\n]*)$')


def published_files() -> list[Path]:
    docs = [ROOT / "README.md", ROOT / "home.md", ROOT / "_sidebar.md"]
    for folder in CONTENTS:
        docs.extend(sorted((ROOT / folder).rglob("*.md")))
    return [p for p in docs if p.is_file()]


def dest_for(page: Path, raw: str) -> Path | None:
    raw = raw.strip().strip("<>")
    if not raw or raw in {"/", "#", "#/"} or re.match(r"^(https?:|mailto:|tel:|data:|javascript:)", raw, re.I):
        return None
    is_router = raw.startswith("#/")
    if raw.startswith("#") and not is_router:
        return None
    raw = raw[2:] if is_router else raw
    raw = unquote(raw.split("#", 1)[0].split("?", 1)[0])
    if not raw:
        return None
    base = ROOT if is_router or raw.startswith("/") else page.parent
    target = (base / raw.lstrip("/")).resolve()
    if target != ROOT and ROOT not in target.parents:
        raise ValueError(f"link escapes the repo: {raw}")
    return target


def check_page(path: Path) -> tuple[list[str], list[str]]:
    issues, warnings = [], []
    rel = path.relative_to(ROOT).as_posix()
    body = path.read_text(encoding="utf-8-sig")
    visible = body.strip()

    if not visible:
        return [f"{rel}: EMPTY published page"], warnings
    if len(visible) < 400:
        issues.append(f"{rel}: less than 400 characters; not a usable published page")
    elif len(visible) < 900:
        warnings.append(f"{rel}: short ({len(visible)} characters); review content depth")

    has_markdown_h1 = bool(re.search(r"^#\s+\S+", body, re.M))
    has_html_h1 = path.name == "home.md" and bool(re.search(r"<h1[ >]", body, re.I))
    if path.name != "_sidebar.md" and not (has_markdown_h1 or has_html_h1):
        issues.append(f"{rel}: missing H1 title")

    fence = None
    for num, line in enumerate(body.splitlines(), 1):
        fm = FENCE.match(line)
        if fm:
            seq, lang = fm.groups()
            if fence is None:
                fence = (seq[0], len(seq), num)
            elif seq[0] == fence[0] and len(seq) >= fence[1] and not lang.strip():
                fence = None
            continue
        if fence is not None:
            continue

        for raw in LINK.findall(line) + HTML_LINK.findall(line):
            try:
                target = dest_for(path, raw)
                if target is not None and not target.is_file():
                    issues.append(f"{rel}:{num}: missing local target {raw!r} ({target.relative_to(ROOT)})")
            except ValueError as exc:
                issues.append(f"{rel}:{num}: {exc}")

    if fence is not None:
        issues.append(f"{rel}: unclosed code fence opened at line {fence[2]}")
    return issues, warnings


def main() -> int:
    files = published_files()
    problems, warnings = [], []
    for page in files:
        a, b = check_page(page)
        problems.extend(a)
        warnings.extend(b)
    print(f"Audited {len(files)} Markdown pages in published content directories.")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in problems:
        print(f"ERROR: {item}")
    print(f"Result: {len(problems)} errors, {len(warnings)} content-depth warnings.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
