<%*
const topic = await tp.system.prompt("Topic");
const book = await tp.system.prompt("Source book id");
const chapter = await tp.system.prompt("Chapter");
const scan = await tp.system.prompt("Scan filename (e.g. 2026-05-30-foo.pdf), or leave blank");
-%>
---
type: derivation
date: <% tp.date.now("YYYY-MM-DD") %>
topic: "<% topic %>"
book: <% book %>
chapter: <% chapter %>
related_problems: []
scan: <% scan %>
tags: []
---

# <% topic %>

**Source:** <% book %> ch. <% chapter %>

## Setup

## Key steps

## Result

## Scan

![[<% scan %>]]

## Notes for future-me
