<%*
const name = await tp.system.prompt("Theorem name");
const book = await tp.system.prompt("Source book id");
const minutes = await tp.system.prompt("Time to reprove (minutes)");
const result = await tp.system.suggester(
  ["passed", "partial", "failed"],
  ["passed", "partial", "failed"]
);
-%>
---
type: theorem
theorem: "<% name %>"
book: <% book %>
date: <% tp.date.now("YYYY-MM-DD") %>
result: <% result %>
time_minutes: <% minutes %>
tags: [reprove]
---

# <% name %>

## Statement

## Proof (reproduced from memory)

## Attempts

| Date | Result | Time | Notes |
|------|--------|------|-------|
| <% tp.date.now("YYYY-MM-DD") %> | <% result %> | <% minutes %>m | |

## Connections
