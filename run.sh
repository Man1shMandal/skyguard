#!/usr/bin/env bash
set -e

# Activate venv if present
if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

python3 app.py