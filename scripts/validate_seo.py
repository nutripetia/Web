#!/usr/bin/env python3
"""SEO acceptance checks on built Jekyll output. Read-only; no deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys
import xml.etree.ElementTree as ET

ROOT = Path("_site")
DOMAIN = "https://nutripetia.es"
ROUTES = {
    "/": ("index.html", "es"),
    "/metodologia/": ("metodologia/index.html", "es"),
    "/investigaciones/": ("investigaciones/index.html", "es"),
    "/nosotros/": ("nosotros/index.html", "es"),
    "/en/": ("en/index.html", "en"),
    "/en/about/": ("en/about/index.html", "en"),
    "/en/methodology/": ("en/methodology/index.html", "en"),
}
# The EN equivalents must be reviewed by Editorial before requiring hreflang.
PAIRS_PENDING_EDITORIAL = (
    ("/", "/en/"),
    ("/nosotros/", "/en/about/"),
    ("/metodologia/", "/en/methodology/"),
)


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.titles = []
        self.descriptions = []
        self.canonicals = []
        self.h1_count = 0
        self._title = False
        self._title_text = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang", "")
        elif tag == "title":
            self._title = True
            self._title_text = ""
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta" and attrs.get("name", "").lower() == "description":
            self.descriptions.append(attrs.get("content", "").strip())
        elif tag == "link" and "canonical" in attrs.get("rel", "").lower().split():
            self.canonicals.append(attrs.get("href", "").strip())

    def handle_data(self, data):
        if self._title:
            self._title_text += data

    def handle_endtag(self, tag):
        if tag == "title" and self._title:
            self.titles.append(self._title_text.strip())
            self._title = False


def main():
    errors = []
    if not ROOT.is_dir():
        sys.exit("SEO validation FAILED: _site missing; run Jekyll build first")
    titles, descriptions = {}, {}
    for route, (relative, expected_lang) in ROUTES.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"{route}: missing HTML {relative}")
            continue
        parser = Metadata()
        parser.feed(path.read_text(encoding="utf-8"))
        if parser.lang.lower() != expected_lang:
            errors.append(f"{route}: html lang={parser.lang!r}, expected {expected_lang!r}")
        if len(parser.titles) != 1 or not parser.titles[0]:
            errors.append(f"{route}: expected exactly one nonempty title")
        else:
            titles.setdefault(parser.titles[0].casefold(), []).append(route)
        if len(parser.descriptions) != 1 or not parser.descriptions[0]:
            errors.append(f"{route}: expected exactly one nonempty meta description")
        else:
            descriptions.setdefault(parser.descriptions[0].casefold(), []).append(route)
        expected = DOMAIN + route
        if parser.canonicals != [expected]:
            errors.append(f"{route}: canonical {parser.canonicals!r}, expected {[expected]!r}")
        if parser.h1_count != 1:
            errors.append(f"{route}: expected one H1, found {parser.h1_count}")

    for label, groups in (("title", titles), ("description", descriptions)):
        for routes in groups.values():
            if len(routes) > 1:
                errors.append(f"Duplicate {label}: {', '.join(routes)}")

    sitemap = ROOT / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("sitemap.xml missing")
    else:
        try:
            tree = ET.parse(sitemap)
            urls = {node.text.strip() for node in tree.iter()
                    if node.tag.endswith("loc") and node.text}
            for route in ROUTES:
                expected = DOMAIN + route
                if expected not in urls:
                    errors.append(f"{route}: missing from sitemap ({expected})")
            for url in urls:
                parsed = urlparse(url)
                if parsed.scheme != "https" or parsed.netloc != "nutripetia.es":
                    errors.append(f"Unexpected sitemap host/scheme: {url}")
        except ET.ParseError as exc:
            errors.append(f"Invalid sitemap XML: {exc}")

    if errors:
        print("SEO validation FAILED:")
        for err in errors:
            print(" -", err)
        return 1
    print(f"SEO validation OK: {len(ROUTES)} routes; titles, descriptions, lang, canonical, H1, sitemap")
    print("NOTE: hreflang equivalence and deployed HTTP responses are not tested")
    return 0


if __name__ == "__main__":
    sys.exit(main())
