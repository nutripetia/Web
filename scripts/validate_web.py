#!/usr/bin/env python3
"""Read-only structural checks against Jekyll output; no deploy or publishing."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

root = Path('_site')
errors = []
if not root.is_dir():
    sys.exit('ERROR: _site not found; run Jekyll build first')

# Contract of existing public routes, independent of baseurl / domain.
public = [
    'index.html', 'nosotros/index.html', 'metodologia/index.html',
    'investigaciones/index.html', 'en/index.html',
    'en/about/index.html', 'en/methodology/index.html',
]
for relative in public:
    if not (root / relative).is_file():
        errors.append(f'Missing required route: {relative}')

reserved_sources = sorted([*Path('guia').rglob('index.md'), Path('articulos/index.md'), Path('auditorias/index.md')])
for source in reserved_sources:
    text = source.read_text(encoding='utf-8')
    if 'published: false' not in text or 'sitemap: false' not in text:
        errors.append(f'Reservation flags missing: {source}')
    relative = source.with_suffix('.html')
    if (root / relative).exists():
        errors.append(f'Unapproved placeholder published: {relative}')

# Jekyll sitemap must not expose unpublished reservations.
sitemap = root / 'sitemap.xml'
if not sitemap.is_file():
    errors.append('Missing sitemap.xml')
else:
    try:
        tree = ET.parse(sitemap)
        urls = [node.text or '' for node in tree.iter() if node.tag.endswith('loc')]
        for source in reserved_sources:
            marker = '/' + source.parent.as_posix().strip('/') + '/'
            if any(url.rstrip('/').endswith(marker.rstrip('/')) for url in urls):
                errors.append(f'Unapproved URL in sitemap: {marker}')
        for path in ['/investigaciones/', '/en/', '/nosotros/']:
            if not any(url.rstrip('/').endswith(path.rstrip('/')) for url in urls):
                errors.append(f'Missing URL in sitemap: {path}')
    except ET.ParseError as exc:
        errors.append(f'Invalid sitemap XML: {exc}')

if errors:
    print('Web validation FAILED:')
    for err in errors:
        print(' -', err)
    sys.exit(1)
print(f'Web validation OK: {len(public)} public routes, {len(reserved_sources)} reserved indexes, sitemap checked')
