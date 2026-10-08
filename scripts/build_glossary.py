"""Add Terminology callouts to the lesson pages and build the Glossary page.

The terms live in scripts/terms.json: one list of [term, definition] pairs
for each page, keyed by the page's path inside docs/. Each term belongs to
the first page (in nav order) that explains it.

This script:
1. puts a `!!! terms "Terminology"` callout straight after each page's
   learning intentions (replacing any Terminology callout already there)
2. writes docs/reference/glossary.md, an A-Z list of every term linking to
   the page that explains it

Run it from the repo root whenever terms.json changes:
    python scripts/build_glossary.py
"""

import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TERMS = ROOT / "scripts" / "terms.json"
GLOSSARY = DOCS / "reference" / "glossary.md"

LEARN = re.compile(r'^!!! learn ".*"\n(?:    .*\n|\n(?=    ))*', re.MULTILINE)
OLD_TERMS = re.compile(r'\n!!! terms "Terminology"\n(?:    .*\n)+')


def nav_titles():
    """Return {page path: nav title} from zensical.toml."""
    config = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    titles = {}

    def walk(items):
        for item in items:
            for title, value in item.items():
                if isinstance(value, list):
                    walk(value)
                else:
                    titles[value] = title

    walk(config["project"]["nav"])
    return titles


def callout(terms):
    lines = ['!!! terms "Terminology"']
    lines += [f"    - **{term}** – {definition}" for term, definition in terms]
    return "\n".join(lines) + "\n"


def add_callouts(pages):
    for path, terms in pages.items():
        page = DOCS / path
        text = page.read_text(encoding="utf-8")
        text = OLD_TERMS.sub("\n", text, count=1)
        match = LEARN.search(text)
        if not match:
            sys.exit(f"{path}: no learning intentions callout to put the terms after")
        end = match.end()
        text = text[:end] + "\n" + callout(terms) + "\n" + text[end:].lstrip("\n")
        page.write_text(text, encoding="utf-8")
        print(f"{path}: {len(terms)} terms")


def write_glossary(pages, titles):
    entries = []
    seen = {}
    for path, terms in pages.items():
        for term, definition in terms:
            key = term.lower()
            if key in seen:
                sys.exit(f"'{term}' is on both {seen[key]} and {path}")
            seen[key] = path
            entries.append((term, definition, path))
    entries.sort(key=lambda entry: entry[0].lower())

    groups = {}
    for term, definition, path in entries:
        first = term[0].upper()
        letter = "0–9" if first.isdigit() else first
        groups.setdefault(letter, []).append((term, definition, path))

    def anchor(letter):
        return "0-9" if letter == "0–9" else letter.lower()

    lines = [
        "# Glossary",
        "",
        "This glossary lists every technical term introduced on this site, in alphabetical order. "
        "Each term links to the page where it is first explained, and each page lists its new terms "
        "in a Terminology callout at the top.",
        "",
        " · ".join(f"[{letter}](#{anchor(letter)})" for letter in groups),
    ]
    for letter, items in groups.items():
        heading = f"## {letter}" + (" { #0-9 }" if letter == "0–9" else "")
        lines += ["", heading, ""]
        for term, definition, path in items:
            link = Path("..") / path
            lines.append(f"- **{term}** – {definition} ([{titles.get(path, path)}]({link.as_posix()}))")
    GLOSSARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {GLOSSARY.relative_to(ROOT)} ({len(entries)} terms)")


def main():
    pages = json.loads(TERMS.read_text(encoding="utf-8"))
    add_callouts(pages)
    write_glossary(pages, nav_titles())


if __name__ == "__main__":
    main()
