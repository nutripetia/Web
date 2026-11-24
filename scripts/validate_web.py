#!/usr/bin/env python3
"""Validate built public routes and explicit unpublished reservations."""
from pathlib import Path
from urllib.parse import urlsplit
import sys
import xml.etree.ElementTree as ET
import yaml

def frontmatter(source):
    lines = source.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"Missing front matter: {source}")
    end = lines.index("---", 1)
    data = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(data, dict):
        raise ValueError(f"Invalid front matter: {source}")
    return data

def route(source, data):
    path = data.get("permalink")
    if not isinstance(path, str) or not path.startswith("/") or ":" in path or ".." in path.split("/"):
        raise ValueError(f"Explicit static permalink required: {source}")
    return path

def output(root, path):
    return root / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))

def validate(root, sources, urls):
    errors = []
    seen = set()
    for source in sources:
        try:
            data = frontmatter(source)
            path = route(source, data)
            if path in seen:
                errors.append(f"Duplicate permalink: {path}")
            seen.add(path)
            if data.get("published") is False:
                if data.get("sitemap") is not False:
                    errors.append(f"Reservation missing sitemap:false: {source}")
                if output(root, path).exists() or path.rstrip("/") in urls:
                    errors.append(f"Reserved route exposed: {path}")
            else:
                if not output(root, path).is_file():
                    errors.append(f"Missing public route: {path}")
                if data.get("sitemap") is not False and path.rstrip("/") not in urls:
                    errors.append(f"Missing sitemap route: {path}")
        except (ValueError, OSError, yaml.YAMLError) as exc:
            errors.append(str(exc))
    return errors

def main():
    root = Path("_site")
    if not root.is_dir():
        sys.exit("ERROR: build Jekyll first")
    tree = ET.parse(root / "sitemap.xml")
    urls = {urlsplit(n.text or "").path.rstrip("/") for n in tree.iter() if n.tag.split("}")[-1] == "loc"}
    sources = sorted(p for section in ("guia", "perros", "gatos", "articulos", "auditorias") for p in Path(section).rglob("index.md"))
    errors = validate(root, sources, urls)
    for path in ("/", "/nosotros/", "/metodologia/", "/investigaciones/", "/en/", "/en/about/", "/en/methodology/", "/guia/", "/perros/", "/gatos/"):
        if not output(root, path).is_file():
            errors.append(f"Missing required route: {path}")
        if path.rstrip("/") not in urls:
            errors.append(f"Missing required sitemap route: {path}")
    if errors:
        sys.exit("Web validation FAILED:\n" + "\n".join(errors))
    print(f"Web validation OK: {len(sources)} thematic indexes")

if __name__ == "__main__":
    main()
