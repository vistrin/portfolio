"""Regenerate the shared and data-driven parts of every page, in place.

Pages stay complete static HTML; this script rewrites only the regions between markers:

    <!-- partial:nav --> ... <!-- /partial:nav -->      copied from _partials/nav.html
    <!-- partial:footer --> ... <!-- /partial:footer -->
    <!-- career:start --> ... <!-- career:end -->       Experience page, rendered from data/

Data:
- data/site.json              exported from the private career-db repo; don't edit by hand:
                              python ../career-db/tools/career_db.py export-public ../portfolio/data/site.json
- data/experience_layout.json which approved entries appear on the Experience page, in which groups

Run after editing a partial, the layout, or re-exporting site.json:

    python build.py           # rewrite pages
    python build.py --check   # exit 1 if any page is out of date (used by the pre-commit hook)

Per-page adjustments made while copying partials:
- {{name}}, {{email}}, {{linkedin}} are filled from site.json's profile.
- Links to the current page get aria-current="page".
- A dropdown button is marked .is-current when the current page is in its menu.
- On index.html, links like "index.html#process" become "#process".
"""
import json
import re
import sys
from html import escape as _escape
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS = ROOT / "_partials"
DATA = ROOT / "data"
PARTIAL = re.compile(r"(<!-- partial:(\w+) -->\n).*?(\n *<!-- /partial:\2 -->)", re.S)
def escape(text):
    """Escape for element text and double-quoted attributes; leaves apostrophes readable."""
    return _escape(text, quote=False).replace('"', "&quot;")


CAREER = re.compile(r"(<!-- career:start -->\n)(?:.*?\n)?( *<!-- career:end -->)", re.S)


def fail(msg):
    sys.exit(f"build.py: {msg}")


def load_json(name):
    path = DATA / name
    if not path.exists():
        fail(f"missing data/{name}")
    return json.loads(path.read_text(encoding="utf-8"))


def fill_tokens(html, profile):
    tokens = {"name": profile["name"], "email": profile["email"], "linkedin": profile["linkedin"]}
    html = re.sub(r"\{\{(\w+)\}\}", lambda m: escape(tokens[m.group(1)]) if m.group(1) in tokens else fail(f"unknown token {m.group(0)}"), html)
    return html


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


def linkedin_link(profile):
    handle = profile["linkedin"]
    return f'<a href="https://www.{escape(handle)}" target="_blank" rel="noopener">{escape(handle)}</a>'


def render_experience(site, layout):
    """The Experience page body: header, summary, skills, jobs, education, publications."""
    p = site["profile"]
    employers = {e["id"]: e for e in site["employers"]}
    entries = {e["id"]: e for e in site["entries"]}
    summary = site.get("summary") or fail("site.json has no summary; set site_export.summary in career-db")
    out = []
    w = out.append

    w('      <div class="cs-header">')
    w('        <div class="cs-num">Experience</div>')
    w(f'        <h1 class="cs-title" id="resume-title">{escape(summary["headline"])}</h1>')
    w(f'        <div class="cs-sub"><a href="mailto:{escape(p["email"])}">{escape(p["email"])}</a> · {linkedin_link(p)}</div>')
    w('      </div>')
    w('')
    w(f'      <p class="resume-summary">{escape(summary["text"])}</p>')

    blocks = site.get("skill_blocks", [])
    if blocks:
        w('')
        w('      <div class="resume-block">')
        w('        <h2 class="section-label">Skills</h2>')
        if len(blocks) > 1:
            w('        <div class="skills-cols">')
        for b in blocks:
            label = escape(b["category"])
            if len(blocks) > 1:
                w(f'          <div>\n            <h3 class="cs-col-label">{label}</h3>')
            w(f'        <ul class="card-tags" aria-label="{label}">')
            for item in b["items"]:
                w(f'          <li class="tag">{escape(item)}</li>')
            w('        </ul>')
            if len(blocks) > 1:
                w('          </div>')
        if len(blocks) > 1:
            w('        </div>')
        w('      </div>')

    w('')
    w('      <div class="resume-block">')
    w('        <h2 class="section-label">Professional experience</h2>')
    for job in layout["jobs"]:
        emp = employers.get(job["employer"]) or fail(f"layout employer {job['employer']} has no approved entries in site.json")
        org = job.get("org", emp["name"])
        meta = " · ".join(x for x in (emp.get("location"), emp["dates"]) if x)
        w('')
        w('        <article class="job">')
        w('          <header class="job-head">')
        if org:
            w('            <div>')
            w(f'              <h3 class="job-title">{escape(emp["title"])}</h3>')
            w(f'              <p class="job-org">{escape(org)}</p>')
            w('            </div>')
        else:
            w(f'            <h3 class="job-title">{escape(emp["title"])}</h3>')
        w(f'            <p class="job-meta">{escape(meta)}</p>')
        w('          </header>')
        for group in job["groups"]:
            heading = group.get("heading")
            if heading:
                text = escape(heading)
                if group.get("link"):
                    text = f'<a href="{escape(group["link"])}">{text}</a>'
                w('')
                w(f'          <h4 class="job-group">{text}</h4>')
            w('          <ul class="resume-list">')
            for i in group["entries"]:
                e = entries.get(i) or fail(f"layout entry {i} is not an approved resume entry in site.json")
                if e["employer_id"] != job["employer"]:
                    fail(f"layout entry {i} belongs to {e['employer_id']}, not {job['employer']}")
                w(f'            <li data-entry="{escape(i)}">{escape(e["text"])}</li>')
            w('          </ul>')
        w('        </article>')
    w('      </div>')

    w('')
    w('      <div class="resume-block">')
    w('        <h2 class="section-label">Education</h2>')
    w('        <ul class="edu-list">')
    for ed in site["education"]:
        w(f'          <li><strong>{escape(ed["degree"])}</strong><span>{escape(ed["school"])}</span></li>')
    w('        </ul>')
    w('      </div>')

    if site.get("publications"):
        w('')
        w('      <div class="resume-block">')
        w('        <h2 class="section-label">Publications</h2>')
        for pub in site["publications"]:
            w(f'        <p class="pub">{escape(pub["citation"])}</p>')
        w('      </div>')
    return "\n".join(out)


def main():
    check = "--check" in sys.argv[1:]
    site = load_json("site.json")
    layout = load_json("experience_layout.json")
    partials = {p.stem: fill_tokens(p.read_text(encoding="utf-8").replace("\r\n", "\n").strip("\n"), site["profile"])
                for p in PARTIALS.glob("*.html")}
    experience = render_experience(site, layout)

    changed, missing = [], []
    for page in sorted(ROOT.glob("*.html")):
        raw = page.read_bytes().decode("utf-8")
        crlf = "\r\n" in raw
        text = raw.replace("\r\n", "\n")
        found = set()

        def fill_partial(m):
            name = m.group(2)
            if name not in partials:
                fail(f"{page.name}: no _partials/{name}.html")
            found.add(name)
            return m.group(1) + localize(partials[name], page.name) + m.group(3)

        new = PARTIAL.sub(fill_partial, text)
        new = CAREER.sub(lambda m: m.group(1) + experience + "\n" + m.group(2), new)
        missing += [f"{page.name}: missing <!-- partial:{n} --> markers" for n in partials if n not in found]
        if new != text:
            changed.append(page.name)
            if not check:
                page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))

    if missing:
        fail("\n".join(missing))
    if check:
        if changed:
            fail("out of date, run `python build.py`: " + ", ".join(changed))
        print("build.py: all pages up to date")
    else:
        print("Updated: " + (", ".join(changed) if changed else "nothing (already up to date)"))


if __name__ == "__main__":
    main()
