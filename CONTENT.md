# Editing the site

The site is built by [Eleventy](https://www.11ty.dev/) from the files in `src/`. You edit text in content files. The build turns them into the HTML pages. You don't edit HTML to change text.

## Preview and publish

```sh
npm install      # once, after cloning
npm start        # builds, serves at http://localhost:8080, and reloads as you save
npm run build    # one-off build into _site/
```

Pushing to `main` publishes the site. GitHub Actions runs the build and deploys `_site/`. The "Last updated" line in every footer is the month of that build. `_site/` is generated, so don't edit or commit it.

## Where things live

| To change… | Edit |
| --- | --- |
| A case study's text, card, tags, or facts | `src/case-studies/<name>.md` |
| Home page hero, Approach, skills list, page description | `src/index.md` |
| Experience page wording, titles, dates | career-db, then re-export `data/site.json` (see below) |
| Which entries show on the Experience page, and their groups | `data/experience_layout.json` |
| A diagram | `src/_includes/diagrams/<name>.svg` |
| Nav bar | `src/_includes/partials/nav.liquid` (case study links are automatic) |
| Footer | `src/_includes/partials/footer.liquid` (name, email, and LinkedIn come from `data/site.json`) |
| Confidentiality notice | `src/_includes/partials/confidentiality.liquid` |
| How a case study page is laid out | `src/_includes/layouts/case-study.liquid` |
| Styles / scripts | `src/style.css`, `src/site.js` |

## Writing text

Content files are YAML between the `---` lines. A few rules cover almost everything:

- **Short text** goes on one line: `title: DevSecOps Compliance Platform`.
- **Long text** uses `>-` and is indented on the following lines. Line breaks inside it are ignored, so wrap lines wherever is comfortable:
  ```yaml
  summary: >-
    Support teams kept being asked to migrate untested code. The checks lived
    in an inch-thick folder of forms, not in a system.
  ```
- **A one-line value containing `: `** (colon then space) must be quoted: `heading: "Design decision: discoverable, but protected"`. Or use `>-`, which never needs quotes.
- **Indentation matters.** Use spaces, not tabs, and keep items in a list lined up.
- **Formatting:** `*italic*`, `**bold**`, `[link text](page.html)`. Type `&`, curly quotes, and dashes directly; the build escapes them.
- Lines starting with `#` are comments and don't appear on the site.

## Case study fields

Each file in `src/case-studies/` is one case study. Its file name becomes the URL (`devsecops.md` → `devsecops.html`). The `num` field sets the order everywhere: home page cards, the Work menu, and each page's "Next" link. The last case study has no Next link, only "All case studies".

```yaml
num: "02"                     # quoted, so it stays "02" and not 2
title: DevSecOps Compliance Platform
subtitle: General Motors IT · Information architecture & UX
anchor: devsecops             # id of the page section; heading id defaults to <anchor>-title
title_id: dso-title           # optional: override that heading id
career_ids: P-DSO GM-DSO-01   # optional: career-db sources, written into an HTML comment

summary: >-                   # home page card text, and the page's search/social description
  ...
tags: [IA & workflow, Gate design, Compliance UX]

facts:                        # the label/value list under the title
  Timeline: ...
  My role: ...

story:                        # the four story blocks; each label holds a list of paragraphs
  The ask:
    - First paragraph.
    - Second paragraph.
  What the problem actually was: [...]
  What I did: [...]
  What happened: [...]

sections: [...]               # optional extra sections between the story and the diagram (below)

diagram:                      # optional
  file: dso.svg               # in src/_includes/diagrams/
  label: Information architecture — staged deployment pipeline
  insight_label: Key design problem
  insight: >-
    ...

depth:                        # optional expandable "more detail" block at the end
  summary: How far the design went, and what got cut
  parts:
    Scope growth:
      - Paragraph.
    Context:
      - Paragraph.
```

The labels under `facts`, `story`, and `depth.parts` are displayed as written. Their order in the file is the order on the page. Leave out `sections`, `diagram`, or `depth` and that part of the page is skipped.

## Add a section to an existing case study

Add an entry under `sections:` (create the key if the file doesn't have one). Every part of a section is optional, and the parts render in this order:

```yaml
sections:
  - heading: How the rescue shaped forecasting   # h2 subhead
    paragraphs:
      - >-
        The rescue paragraph…
      - >-
        The forecasting paragraph…
    steps_label: Access states for a protected dataset   # numbered steps; label is for screen readers
    steps:
      Search finds the asset: Tables and datasets appear in results even if you can't open them.
      Request access: Once access is granted, the values appear.
    table:
      caption: "The vocabulary: one word, three meanings"
      columns: [What people said, What it referred to, What we called it]
      rows:
        - [Running a scenario, The values entered before a run, Parameters]
    note: A small-print note under the section.
```

For several sections, add more `- heading: …` entries. They appear in the order listed.

## Add a case study

1. Copy an existing file in `src/case-studies/` to a new name, e.g. `new-project.md`. That name becomes `new-project.html`.
2. Set `num` to the next number, and pick a new `anchor`. Remove `title_id` unless you need it.
3. Replace the text. Delete `sections`, `diagram`, or `depth` if you don't need them.
4. For a diagram, add an SVG to `src/_includes/diagrams/` and set `diagram.file`. Give it `role="img"`, a `<title>`, and a `<desc>` (see the existing ones). Use IDs that are unique on the page, including the arrowhead `marker` id.

The card, Work menu entry, and Next links appear automatically. Two things don't update on their own: the home page grid (`.cards-grid` in `src/style.css`) is sized for the current number of cards, and `src/index.md` describes the case studies in its `description` and hero text.

## Experience page

The wording comes from the private career-db repo, never from this one:

```sh
python ../career-db/tools/career_db.py export-public ../portfolio/data/site.json   # from career-db
```

Then rebuild. `data/experience_layout.json` decides which approved entries appear and how they're grouped. The build stops with an error if the layout names an entry that isn't in `site.json`.

## Checks before committing

The pre-commit hook (enable once with `git config core.hooksPath .githooks`) builds the site and runs career-db's `lint-site` over the sources and the built pages. It blocks the commit if the build fails or banned content appears.
