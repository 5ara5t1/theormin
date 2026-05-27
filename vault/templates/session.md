<%*
const hours = await tp.system.prompt("Hours");
const subject = await tp.system.prompt("Subject");
const activity = await tp.system.prompt("Activity (one line)");
-%>
---
type: session
date: <% tp.date.now("YYYY-MM-DD") %>
hours: <% hours %>
subject: <% subject %>
activity: "<% activity %>"
---

# Session — <% tp.date.now("YYYY-MM-DD") %>

**<% hours %>h — <% subject %>**

## What I did

<% activity %>

## What I worked through

## What I'm leaving open
