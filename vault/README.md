# theormin vault

Obsidian vault for the [theormin](../README.md) project.

## Setup

1. Install [Obsidian](https://obsidian.md).
2. Open this `vault/` folder as a vault (not the repo root).
3. Settings → Community plugins → install Dataview and Templater.
4. Templater → Template folder location → `templates`.

## Folders

| Folder | Contents |
|--------|----------|
| `00-meta/` | Curriculum, dashboard, reading list |
| `01-weeks/` | One file per week — plan, sessions table, problems table, reflection |
| `02-summaries/` | Chapter summaries (when a chapter warrants one) |
| `03-theorems/` | Reproved-from-memory log |
| `04-problems/` | Optional write-ups for notable problems only |
| `05-derivations/` | End-of-week PDF scans + indices |
| `06-checkpoints/` | The nine self-assessment exams |
| `07-references/` | Lecture notes, papers, video courses |
| `templates/` | Templater templates |

## Workflow

Day-to-day:

1. Read book → take notes / work problems on paper.
2. End of session, open this week's `01-weeks/week-XX.md`.
3. Add a row to `## Sessions` table for the study block.
4. Add rows to `## Problems worked` for problems solved.

When a chapter is done: write a summary in `02-summaries/<book>/`.

End of week:

1. Reprove a theorem from memory → write up in `03-theorems/`.
2. Scan paper to PDF → drop in `05-derivations/week-XX/` with an index.
3. Fill in the `## Reflection` section at the bottom of the week file.
4. `git push`. CI regenerates the public dashboard.

## What the dashboard reads

- `## Sessions` and `## Problems worked` tables in each week file → hours and problem counts.
- Frontmatter on `02-summaries/` notes → chapter progress.
- Files in `03-theorems/` with `type: theorem` → reproved theorems.
- `data/books.yaml` → reading shelf.

The Python in `scripts/` does the extraction. `## type:` values in frontmatter: `week`, `summary`, `theorem`, `derivation_index`, `reference`, `checkpoint`. `problem` and `session` frontmatter is optional (for the rare standalone note); the canonical record is the weekly table.
