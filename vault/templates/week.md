<%*
const weekNum = await tp.system.prompt("Week number (e.g. 2)");
const startDate = await tp.system.prompt("Start date (YYYY-MM-DD)");
const endDate = await tp.system.prompt("End date (YYYY-MM-DD)");
const phase = await tp.system.prompt("Phase (1-6)");
const weekStr = String(weekNum).padStart(2, "0");
-%>
---
type: week
week: <% weekNum %>
start_date: <% startDate %>
end_date: <% endDate %>
phase: <% phase %>
---

# Week <% weekNum %> (<% startDate %> → <% endDate %>)

Budget: 30 hours.

## Plan

| Stream | Hours | Notes |
|--------|-------|-------|
|        |       |       |

### Daily targets

- Mon:
- Tue:
- Wed:
- Thu:
- Fri:
- Sat:
- Sun:

### Out of scope this week

- 

## Sessions

| Date | Hours | Subject | Activity |
|------|-------|---------|----------|

## Problems worked

| Date | Book | Ref | Subject | Min | Status | Note |
|------|------|-----|---------|-----|--------|------|

## Reading completed

- [ ] 

## Chapter summaries written

- [ ] 

## Theorems reproved

- 

## Scans

End-of-week PDF in `vault/05-derivations/week-<% weekStr %>/`. Add the file path here when uploaded.

## Reflection

_(Fill in at end of week.)_

### Looking ahead

- 
