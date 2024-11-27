#!/bin/bash
PY_FILES=$(find . -type d \( -name ".venv" -o -name "features" \) -prune -o -name "*.py" -print)
PYLINT_ARGS="--output-format=colorized --disable=E0401"
source /app/.venv/bin/activate
pylint $PY_FILES $PYLINT_ARGS