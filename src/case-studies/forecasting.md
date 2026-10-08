---
# Case study 03. Field guide: CONTENT.md. The page URL is this file's name: forecasting.html.
num: "03"
title: Product Resource Forecasting
subtitle: General Motors IT · Information architecture & UX · includes the rescue project that shaped it
anchor: prf
career_ids: P-FC P-RESCUE P-DREAMS GM-FC-01 GM-RESCUE-01 GM-DREAMS-01

# Card on the home page (also the page's search/social description)
summary: >-
  “Scenario” meant three different things, and a project had stalled six months over it.
  Defining the objects got it to an implementable design in five days.
tags:
  - Object modeling
  - Vocabulary
  - Decision support

facts:
  Timeline: >-
    Rescue: five business days from stalled to an implementable design. Forecasting: the pilot for
    DREAMS, the data science model management tool I went on to design.
  My role: >-
    Defined the vocabulary and object model, and designed the interfaces for scenario setup,
    filtering, and comparison.
  Worked with: >-
    The lead data scientist and business owner on the rescue; the data scientist who built the
    forecasting model and its business users; the development team that later built DREAMS.
  Measure: >-
    The stalled project reached an implementable design in five business days and was built. For
    forecasting there is no time-saved figure: the gain was a capability that hadn’t existed.

story:
  The ask:
    - "Rescue: help a vehicle-sales incentive project that had been stuck for six months."
    - >-
      Forecasting: “just a report” where business users enter parameters and a machine-learning
      model returns scenarios.
  What the problem actually was:
    - >-
      People said “scenario” and meant three different things. What looked like one document was
      many objects, and changing any input (data, parameters, or model) changes the result. Nobody
      could reliably say how they had arrived at a given scenario.
  What I did:
    - >-
      Rescue: met the lead data scientist and business owner in person, had them walk me through
      their process step by step, and played it back until we agreed what each thing was. I wrote a
      shared vocabulary and designed a structure that tracked provenance, including how one
      period’s recommendation plus actuals feeds the next run.
    - >-
      Forecasting: reused the method. I went through the data scientist’s prototype word by word to
      pin down inputs, ranges, and meanings, then designed scenario setup, filtering, and
      side-by-side comparison.
  What happened:
    - >-
      The incentive tool was built by the development team that later built DREAMS. Forecasting
      users had wanted out of spreadsheets; comparing generated scenarios, each spanning 90+ product
      lines over up to ten years, had meant comparing spreadsheets by hand. One user said it did
      what they had been doing, only better and faster.

sections:
  - table:
      caption: "The vocabulary: one word, three meanings"
      columns: [What people said, What it referred to, What we called it]
      rows:
        - [Running a scenario, The values entered before a run, Parameters]
        - [Getting the scenarios, What the model generates, Output]
        - [Updating a scenario, A generated result edited by a person, Adjusted scenario]

diagram:
  file: prf.svg
  label: Object model — what a scenario is made of, and how it carries forward
  insight_label: Key IA decision
  insight: >-
    A scenario is not one document. Separating the objects (data, parameters, model, output), and
    recording each scenario’s lineage, let the interface follow the actual process instead of a
    single imagined report.

depth:
  summary: What I deliberately left alone, and how this connects to DREAMS
  parts:
    What I left alone:
      - >-
        Users were already happy with how scenarios were output, a ranked list plus a bubble chart
        for analysis, so I kept it. The leverage was upstream: giving the process recognizable,
        trackable steps and building the interface to match.
    The through-line:
      - >-
        The rescue project taught me to pull apart the objects hiding inside “one report,” and I
        applied that directly to forecasting. Forecasting then piloted DREAMS, which let a data
        scientist upload data and a model, schedule runs with chosen compute resources, chain models
        together, and track which model and data produced each result. I believe the rescue is one
        reason I moved onto DREAMS; that is my reading, not something I was told.
---
