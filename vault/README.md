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
| `00-meta/` | Curriculum, dashboard, reading list, problem log |
| `01-weeks/` | Week plans, daily session logs, weekly reflections |
| `02-summaries/` | Chapter summaries |
| `03-theorems/` | Reproved-from-memory log |
| `04-problems/` | One note per worked problem |
| `05-derivations/` | Scanned handwriting + transcriptions |
| `06-checkpoints/` | The nine self-assessment exams |
| `07-references/` | Lecture notes, papers, video courses |
| `templates/` | Templater templates |

## Frontmatter

YAML frontmatter is what `scripts/extract_from_vault.py` reads to compile `data/*.csv`, which feeds the README dashboard.

- Use the templates so frontmatter doesn't get missed.
- `type:` values: `problem`, `theorem`, `session`, `summary`, `derivation`, `reference`, `checkpoint`, `reflection`.
- `book:` IDs match `data/books.yaml`.

Pushes to GitHub trigger the CI workflow that regenerates the public dashboard.
