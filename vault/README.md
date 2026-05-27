# theormin vault

Obsidian vault for the [theormin](../README.md) project.

## How to use

1. Install [Obsidian](https://obsidian.md).
2. Open this `vault/` folder as a vault (not the repo root — `vault/` specifically).
3. Settings → Community plugins → turn on Community plugins → install **Dataview** and **Templater**.
4. Templater → Template folder location → set to `templates`.

## What's here

| Folder | What it holds |
|--------|---------------|
| `00-meta/` | Curriculum, dashboard, reading list, problem log |
| `01-weeks/` | Week plans + reflections |
| `02-summaries/` | Chapter summaries — your personal compressed Landau-Lifshitz |
| `03-theorems/` | Reproved-from-memory log |
| `04-problems/` | One note per worked problem |
| `05-derivations/` | Scanned handwriting + transcriptions |
| `06-checkpoints/` | The nine self-assessment exams |
| `07-references/` | External lecture notes, papers, video courses |
| `templates/` | Templater templates for new notes |

## Frontmatter is load-bearing

Every note's YAML frontmatter is read by `scripts/extract_from_vault.py`, which compiles it into `data/*.csv`, which feeds the public README dashboard. So:

- Use templates (Templater plugin) to never miss frontmatter.
- Use the right `type:` value (`problem`, `theorem`, `session`, `summary`, `derivation`, `reference`, `checkpoint`, `reflection`).
- Use IDs that match `data/books.yaml`.

When you push to GitHub, the CI workflow regenerates the public dashboard.
