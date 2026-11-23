#!/usr/bin/env python3
"""WT-036: read-only pre-build checks for public Jekyll source pages.

Run from repository root: python3 scripts/check_source_contract.py
No dependencies, writes, network calls or publication.
"""
from pathlib import Path
import re
import sys

PUBLIC = (
    "index.md", "nosotros.md", "metodologia.md",
    "investigaciones/index.md", "en/index.md",
    "en/about.md", "en/methodology.md",
)
ROOT = Path(__file__).resolve().parent.parent
errors = []
routes = {}
titles = {}
for name in PUBLIC:
    path = ROOT / name
    if not path.is_file():
        errors.append(f"Missing public source: {name}")
        continue
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        errors.append(f"Missing YAML front matter: {name}")
        continue
    fm = match.group(1)
    def field(key):
        found = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", fm, re.M)
        return found.group(1).strip('"\'') if found else ""
    route = field("permalink") or ("/" if name == "index.md" else "")
    if not route or not route.startswith("/") or not route.endswith("/"):
        errors.append(f"Invalid permalink: {name}: {route!r}")
    if route in routes:
        errors.append(f"Duplicate permalink: {route} in {routes[route]} and {name}")
    routes[route] = name
    title = field("title")
    if not title:
        errors.append(f"Missing title: {name}")
    elif title in titles:
        errors.append(f"Duplicate page title: {title!r} in {titles[title]} and {name}")
    titles[title] = name
    if not field("description"):
        errors.append(f"Missing description: {name}")
    expected_lang = "en" if name.startswith("en/") else "es"
    if field("lang") not in ("", expected_lang):
        errors.append(f"Unexpected language: {name}")
    if field("published").lower() == "false":
        errors.append(f"Public page marked unpublished: {name}")

# Detect broken internal links expressed with Jekyll's relative_url filter.
for name in PUBLIC:
    path = ROOT / name
    if not path.is_file():
        continue
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\{\{\s*['\"](/[^'\"]+)['\"]\s*\|\s*relative_url\s*\}\}", text):
        if target.split("#", 1)[0].split("?", 1)[0] not in routes:
            errors.append(f"Unresolved internal route {target} referenced by {name}")

# Reservations must remain excluded from generated output.
for directory in ("guia", "articulos", "auditorias"):
    base = ROOT / directory
    if not base.exists():
        continue
    for path in base.rglob("index.md"):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
        fm = match.group(1) if match else ""
        if not re.search(r"^published:\s*false\s*$", fm, re.M) or not re.search(r"^sitemap:\s*false\s*$", fm, re.M):
            errors.append(f"Reservation not excluded: {path.relative_to(ROOT)}")

if errors:
    print("Source contract FAILED:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"Source contract OK: {len(PUBLIC)} public pages, {len(routes)} unique routes; reservations checked")
