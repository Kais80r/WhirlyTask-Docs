"""Check local Markdown destinations, heading anchors and SVG assets.

Run from any directory: python tools/check_docs.py
No packages or network access are required.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def visible_markdown(text: str) -> str:
    return re.sub(r"^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", text, flags=re.M | re.S)


def heading_ids(text: str) -> set[str]:
    ids: set[str] = set()
    counts: dict[str, int] = {}
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", visible_markdown(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        ids.add(f"{slug}-{count}" if count else slug)
    ids.update(re.findall(r'\bid=["\x27]([^"\x27]+)["\x27]', text))
    return ids


def main() -> int:
    pages = sorted([ROOT / 'README.md', *(ROOT / 'docs').rglob('*.md')])
    cache = {page.resolve(): page.read_text(encoding='utf-8-sig') for page in pages}
    errors: list[str] = []
    links = 0
    for page, text in cache.items():
        relative = page.relative_to(ROOT)
        if len(re.findall(r'^# ', text, re.M)) != 1:
            errors.append(f'{relative}: expected one page title')
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', visible_markdown(text)):
            destination = match[1].strip().split(' "', 1)[0].strip('<>')
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'{relative}: missing or out-of-repository target {destination}')
                continue
            # GitHub paths are case sensitive even when this checker runs on Windows.
            cursor = ROOT
            for part in target.relative_to(ROOT).parts:
                if part not in {entry.name for entry in cursor.iterdir()}:
                    errors.append(f'{relative}: incorrect path case {destination}')
                    break
                cursor /= part
            if parsed.fragment and target.suffix.lower() == '.md':
                content = cache.get(target) or target.read_text(encoding='utf-8-sig')
                if unquote(parsed.fragment) not in heading_ids(content):
                    errors.append(f'{relative}: missing heading {destination}')
    diagrams = list((ROOT / 'docs/assets').rglob('*.svg'))
    for diagram in diagrams:
        try:
            ElementTree.parse(diagram)
        except ElementTree.ParseError as error:
            errors.append(f'{diagram.relative_to(ROOT)}: invalid SVG: {error}')
    if errors:
        print('\n'.join(errors))
        print(f'FAIL: {len(errors)} documentation errors')
        return 1
    print(f'PASS: {len(pages)} Markdown pages, {links} local links, {len(diagrams)} SVG assets')
    return 0


if __name__ == '__main__':
    sys.exit(main())
