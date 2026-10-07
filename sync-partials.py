"""Copy the shared nav and footer from _partials/ into every page.

Each page marks where a partial goes:

    <!-- partial:nav -->
    ...replaced on every run...
    <!-- /partial:nav -->

Edit _partials/nav.html or _partials/footer.html, then run:

    python sync-partials.py

Per-page adjustments made while copying:
- Links to the current page get aria-current="page".
- A dropdown button is marked .is-current when the current page is in its menu.
- On index.html, links like "index.html#process" become "#process".
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS = ROOT / "_partials"
MARKER = re.compile(r"(<!-- partial:(\w+) -->\n).*?(\n *<!-- /partial:\2 -->)", re.S)


def localize(html, page):
    html = html.replace(' aria-current="page"', "")
    html = re.sub(rf'(<a href="{re.escape(page)}")', r'\1 aria-current="page"', html)

    def mark_menu(m):
        menu = m.group(0)
        if 'aria-current="page"' in menu:
            menu = menu.replace('class="nav-menu-btn"', 'class="nav-menu-btn is-current"', 1)
        return menu

    html = re.sub(r'<li class="nav-menu">.*?</ul>\s*</li>', mark_menu, html, flags=re.S)
    if page == "index.html":
        html = html.replace('href="index.html#', 'href="#')
    return html


def main():
    partials = {p.stem: p.read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n") for p in PARTIALS.glob("*.html")}
    changed, missing = [], []
    for page in sorted(ROOT.glob("*.html")):
        raw = page.read_bytes().decode("utf-8")
        crlf = "\r\n" in raw
        text = raw.replace("\r\n", "\n")
        found = set()

        def fill(m):
            name = m.group(2)
            if name not in partials:
                sys.exit(f"{page.name}: no _partials/{name}.html")
            found.add(name)
            return m.group(1) + localize(partials[name], page.name) + m.group(3)

        new = MARKER.sub(fill, text)
        missing += [f"{page.name}: missing <!-- partial:{n} --> markers" for n in partials if n not in found]
        if new != text:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
            changed.append(page.name)
    print("Updated: " + (", ".join(changed) if changed else "nothing (already in sync)"))
    if missing:
        sys.exit("\n".join(missing))


if __name__ == "__main__":
    main()
