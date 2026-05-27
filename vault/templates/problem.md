<%*
const book = await tp.system.prompt("Book id (e.g. tao-analysis-1)");
const chapter = await tp.system.prompt("Chapter (e.g. 2)");
const ref = await tp.system.prompt("Problem ref (e.g. 2.2.3)");
const subject = await tp.system.prompt("Subject");
const phase = await tp.system.prompt("Phase (1-6)");
const minutes = await tp.system.prompt("Minutes spent");
const status = await tp.system.suggester(
  ["solved", "partial", "stuck", "revisit"],
  ["solved", "partial", "stuck", "revisit"]
);
const id = `${book}-${ref.replace(/\./g, "-")}`;
-%>
---
type: problem
id: <% id %>
book: <% book %>
chapter: <% chapter %>
problem_ref: "<% ref %>"
subject: <% subject %>
phase: <% phase %>
date: <% tp.date.now("YYYY-MM-DD") %>
minutes: <% minutes %>
status: <% status %>
tags: [phase-<% phase %>, <% subject %>]
---

# <% book %> <% ref %>

## Statement

## Approach

## Solution

## What was hard

## Connections
