#!/usr/bin/env bash
# Convenience: extract vault → regenerate charts → regenerate README.
# Run from repo root: ./scripts/refresh.sh
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/extract_from_vault.py
python3 scripts/gen_charts.py
python3 scripts/gen_readme.py
echo "✓ refresh complete"
