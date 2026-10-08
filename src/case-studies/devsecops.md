---
# Case study 02. Field guide: CONTENT.md. The page URL is this file's name: devsecops.html.
num: "02"
title: DevSecOps Compliance Platform
subtitle: General Motors IT · Information architecture & UX
anchor: devsecops
title_id: dso-title
career_ids: P-DSO GM-DSO-01

# Card on the home page (also the page's search/social description)
summary: >-
  Support teams kept being asked to migrate untested code. The checks lived in an inch-thick
  folder of forms, not in a system.
tags:
  - IA & workflow
  - Gate design
  - Compliance UX

facts:
  Timeline: About three years of intermittent design input, alongside the portal work in case study 01.
  My role: >-
    UX and information architecture for the initial platform: the project record, gate structure,
    and document flow. Another owner took it over full-time as it changed direction.
  Worked with: The support team that fielded migration requests, project managers, and development teams.
  Measure: No outcome figures. The project-management workflow was superseded by a purchased platform.

story:
  The ask:
    - >-
      The support team was tired of being asked to migrate code between environments (dev to test,
      test to prod) that hadn’t been properly tested or had no backout plan. They wanted a platform
      to stop it.
  What the problem actually was:
    - >-
      Nobody could see readiness. I had an inch-thick folder of forms on my desk, and nearly every
      page asked for the same project name. The gate checks existed as paperwork, not as a system,
      so there was no single place to see what a project had or lacked.
  What I did:
    - >-
      Made the gate the structure. A team creates a project once and its details carry through.
      Documents attach to the gate that needs them, and approval at a gate unlocks the next
      environment, which the platform could build, so support stopped creating environments nobody used.
  What happened:
    - >-
      GM bought a commercial code management platform and the project-management side was dropped.
      The tool was repurposed as a workbench for data scientists, connected to the portal, so they
      could pull data from source systems into their notebooks.
    - By then I had moved to other projects, so I shaped only the initial design.

diagram:
  file: dso.svg
  label: Information architecture — staged deployment pipeline
  insight_label: Key design problem
  insight: >-
    Readiness was invisible because every check lived on a separate form. Capturing the project
    once and attaching evidence to gates was designed to make the state of any project readable in
    one place.

depth:
  summary: How far the design went, and what got cut
  parts:
    Scope growth:
      - >-
        The design became detailed. Teams could run automated and specialized tests from the
        interface, upload documents, and build backout plans in the tool itself. I don’t remember
        the specifics of the backout-plan builder, only that it was elaborate.
    Context:
      - >-
        This was before Microsoft Teams and Azure were in use at GM. When the company chose a
        commercial code management platform, the project-management scope went away, and the tool
        took on its data scientist role under a different owner.
---
