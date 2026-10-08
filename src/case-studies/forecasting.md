---
# Case study 04. Field guide: CONTENT.md. The page URL is this file's name: forecasting.html.
num: "04"
title: Product Resource Forecasting
subtitle: General Motors IT · Information architecture & UX · Pilot for DREAMS
anchor: prf
career_ids: P-FC P-DREAMS GM-FC-01 GM-DREAMS-01

# Card on the home page (also the page's search/social description)
summary: >-
  Planners wanted out of spreadsheets. A business user could enter parameters and get about a
  hundred scenarios back, but comparing them, or tracing how a result was produced, was hard.
tags:
  - Object modeling
  - Decision support
  - Interface design

facts:
  Timeline: Pilot project within the larger DREAMS effort.
  My role: >-
    Defined the vocabulary and object model; designed scenario setup, filtering, and side-by-side
    comparison.
  Worked with: >-
    The data scientist who helped build the machine-learning model, the business users who ran it,
    and the data science group.
  Measure: >-
    No time-saved figure; the gain was a capability that hadn’t existed. Each run returns around a
    hundred scenarios, each covering 90+ product lines over up to ten years.

story:
  The ask:
    - >-
      “Just a report”: a business user enters parameters, clicks a button, and a machine-learning
      model works through the possible scenarios and returns reports. The criteria could be
      elaborate, such as a headcount cost ceiling for the first years of a program and a different
      capital ceiling later.
  What the problem actually was:
    - >-
      Planners had been doing this analysis in spreadsheets and wanted out of them: even basic
      filtering and sorting got messy when the data didn’t line up. What they lacked was an easy way
      to generate scenarios, and a way to make sense of them once generated.
    - >-
      The terminology made it worse. The same word covered what you ran and what you got back, and
      the inputs used to run the model were easily confused with the data that goes into it. A
      result depends on at least four things (input data, input parameters, the model, and the
      outputs), and changing any one gives a different result. Users needed to answer: how did I get
      this result, and which parameters and data did I start with?
  What I did:
    - >-
      I spent most of my time with the data scientist who helped create the model. Working from his
      prototype, we went word by word through every prompt and input: what each meant and what its
      minimum and maximum could be. I reframed input parameters as boundaries, so users could see up
      front what to expect in the results.
    - >-
      Then I designed scenario setup, and a main interface for sifting through around a hundred
      scenario reports: sort and filter by criteria, open one scenario, and compare it against
      another side by side. Result review stayed familiar, with numbers and line graphs, because
      planners were already comfortable reading results that way.
  What happened:
    - >-
      Comparing scenarios had meant checking one spreadsheet against another by hand; the new
      interface made it possible in one place. One user said it did what they had been doing, only
      better and faster. I was also asked to produce a promotional presentation for the project. It
      was the pilot for DREAMS and shaped how I designed that platform.

diagram:
  file: prf.svg
  label: What a scenario is made of
  insight_label: Key IA decision
  insight: >-
    A result is not one document: it is the product of data, parameters, a model, and outputs.
    Making those separate objects, and keeping their lineage, let the interface answer “how did I
    get this?”

depth:
  summary: What I left alone, and how this connects
  parts:
    What I left alone:
      - >-
        The way results are reviewed. Planners already read numbers and line graphs, and the output
        format didn’t need to change; the leverage was upstream, in making the inputs and their
        meanings clear.
    Where the method came from:
      - >-
        The approach of pulling apart the objects hiding inside “one report” came from the incentive
        project.
    DREAMS:
      - >-
        Forecasting was the pilot for DREAMS, the platform where data scientists upload data and
        models, schedule runs on chosen compute resources, chain models together, and track which
        model and data produced each result.
---
