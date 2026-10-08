---
# Case study 01. Field guide: CONTENT.md. The page URL is this file's name: data-discovery.html.
num: "01"
title: Enterprise Data Discovery Platform
subtitle: General Motors IT · Enterprise data warehouse portal · Information architecture & UX
anchor: edr
career_ids: P-EDW GM-EDW-01 GM-EDW-02 GM-EDW-03 GM-EDW-05 GM-EDW-07 GM-EDW-08

# Card on the home page (also the page's search/social description)
summary: >-
  The ask was a place to find reports. The problem was a library with no books:
  assets were published with vague names and no useful metadata.
tags:
  - Information architecture
  - Metadata
  - Access-aware search

facts:
  Timeline: About six years, from the start of my GM tenure, overlapping with case study 02.
  My role: >-
    Information architect and UX designer for the portal: metadata standards, vocabulary,
    classification, and discovery and access design.
  Worked with: >-
    ETL, BI, data governance, and cloud storage teams; the InfoSphere administrator; report authors.
  Measure: >-
    I don’t have usage or search-time figures for the portal itself. Baseline: before the data
    warehouse, a cross-system question such as, “What does this vehicle cost us?” took weeks to answer.

story:
  The ask:
    - Build a website where people can find their reports.
  What the problem actually was:
    - >-
      A library with no books in it. Report authors could publish whenever they liked, often
      with vague names and descriptions, so an asset was findable only if you already knew it existed.
    - >-
      Early interviews showed people knew their task but not source systems or project names.
      Discovery depended on describing each asset by what it does and what questions it can
      answer. I raised this early: the metadata had to come before the interface.
  What I did:
    - >-
      Put most of my effort into getting useful metadata from source systems all the way to the
      portal: data dictionaries, classification, and a shared vocabulary built with the ETL, BI,
      governance, and storage teams. I defined what a catalog entry carried for every asset and
      worked to get assets tagged, labeled, and classified in terms the business actually used.
  What happened:
    - >-
      The warehouse’s standardized pipelines and its 360 datasets streamlined weeks-long analysis
      work considerably, and the portal made those assets visible to anyone in the company. The
      product went through three names: Business Intelligence Gateway, EDW portal, and later Maxis.
    - >-
      Adoption is the open question. I can’t say how many people knew it existed, or knew enough
      about data analysis to use it.

sections:
  - heading: "Design decision: discoverable, but protected"
    paragraphs:
      - >-
        Search had to respect security tiers (Sarbanes-Oxley, PII, HR, R&D). Hiding everything a
        user couldn’t open would also have hidden useful data from people who could request it, so
        I designed for discovery without exposure:
    steps_label: Access states for a protected dataset
    steps:
      Search finds the asset: Tables and datasets appear in results even if you can’t open them.
      Structure visible, values masked: You can see that a column such as a card number exists. The values are blanked.
      Request access: Once access is granted, the values appear.
    note: A few tables were hidden entirely until the user already had access.

diagram:
  file: edw.svg
  label: Data model and metadata — 360 segments and the catalog entry
  insight_label: Key IA decision
  insight: >-
    Metadata before interface. Findability was a supply problem, not a navigation problem, so the
    effort went into what every asset said about itself.

depth:
  summary: What I tried that didn’t work, and what changed along the way
  parts:
    Visual navigation:
      - >-
        Stakeholders kept asking for relationship graphs, navigation graphs, and clickable
        business-term explainers. Some were fully built; others failed in testing and prototyping.
        All were fun and not very useful for finding things. I concluded the leverage was in metadata.
    Classification tooling:
      - >-
        The team repeatedly tried to use IBM InfoSphere to classify and organize assets. Setup and
        agreement on approach kept stalling, and I spent a lot of time with its administrator trying
        to get data classified.
    Naming:
      - >-
        The team wanted to call the business projects that produced reports “applications.” It
        confused people. After several years of filling a whiteboard with synonyms, “collections” won out.
    Platform churn:
      - >-
        The first design assumed SharePoint. Direction then changed to a custom-built system, and
        scope and priorities shifted again with new directors.
---
