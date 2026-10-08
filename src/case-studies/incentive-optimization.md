---
# Case study 03. Field guide: CONTENT.md. The page URL is this file's name: incentive-optimization.html.
num: "03"
title: Incentive Optimization Tool
subtitle: General Motors IT · Information architecture & UX · Rescue project
anchor: inc
career_ids: P-RESCUE GM-RESCUE-01

# Card on the home page (also the page's search/social description)
summary: >-
  A vehicle-sales project had been stuck for six months. People used one word, “scenario,” for
  different things, and nobody could trace where a result came from.
tags:
  - Object modeling
  - Process mapping
  - Provenance

facts:
  Timeline: Five business days from stalled to an implementable design.
  My role: Defined the objects and the tracking structure, and did the interface design.
  Worked with: >-
    The lead data scientist and the primary business user (met in person), the data warehouse
    sales team that asked for help, and the development team that built the tool.
  Measure: >-
    Stalled for about six months before I was brought in; an implementable design five business
    days later; the tool was built.

story:
  The ask:
    - >-
      A vehicle-sales project team on the data warehouse asked for help with an analysis project
      that had been stuck for about six months. The business wanted to compare incentive programs
      (cash back, discount, loyalty reward) and use each month’s results to decide what to offer next.
  What the problem actually was:
    - >-
      The people on the project used one word, “scenario,” for different things. When they said they
      wanted to run a scenario and analyze a scenario, they meant two different things. The data
      scientist’s hand-off to the business owner depended on a previous scenario’s data, and what
      looked like one document was really many, each with its own lineage.
  What I did:
    - >-
      I met the lead data scientist and the primary business user in person. I had the business
      user walk me through their process step by step, then described it back, asking what happens
      when they take each step or change each input, until we agreed on what each thing was and
      which things deserved to be tracked as their own record.
    - >-
      From that I designed the structure. Each month’s run generates around a hundred scenarios. The
      analyst selects and recommends one, which a person can adjust by hand. The recommended scenario
      plus the month’s actual results feed the next month’s run. Every scenario keeps track of where
      it came from, and human-adjusted scenarios are tracked separately from model-generated ones. I
      also did the UI design, which simplified their process.
  What happened:
    - >-
      The project went from stalled to an implementable design in five business days, and the tool
      was built by the development team that later built DREAMS. I kept the scenario list and bubble
      chart the team already liked. The value was not in changing the model’s output but in giving
      the process recognizable, trackable steps.

diagram:
  file: inc.svg
  label: Monthly scenario loop with lineage
  insight_label: Key IA decision
  insight: >-
    What looked like one document was many. Separating the objects, and recording where each one
    came from, let the interface follow the actual process.

depth:
  summary: What I don’t know, and how this connects
  parts:
    What I don’t know:
      - >-
        I don’t remember exactly why the project had stalled. What I can speak to is what I found
        once I was in the room: a vocabulary and a process that nobody had pinned down.
    Connection:
      - >-
        This is where I learned how loosely people use the word “scenario,” and I brought that
        method into the forecasting work. I believe it is one reason I moved onto DREAMS; that is my
        reading, not something I was told.
---
