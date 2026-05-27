<%*
const book = await tp.system.prompt("Book id (e.g. tao-analysis-1)");
const chapter = await tp.system.prompt("Chapter (e.g. 2)");
const sections = await tp.system.prompt("Sections (comma-separated, e.g. 2.1, 2.2)");
const subject = await tp.system.prompt("Subject (real_analysis | linear_algebra | etc.)");
const phase = await tp.system.prompt("Phase (1-6)");
-%>
---
type: summary
book: <% book %>
chapter: <% chapter %>
sections: [<% sections %>]
status: in_progress
date_started: <% tp.date.now("YYYY-MM-DD") %>
date_completed:
hours: 0
problems_worked: 0
tags: [phase-<% phase %>, <% subject %>]
---

# <% book %> — Ch. <% chapter %>

## What this chapter establishes

## Key definitions

## Major theorems (proof sketches)

## Where this connects

## What felt important

## Open questions
