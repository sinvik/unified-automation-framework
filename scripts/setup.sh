#!/bin/bash
# Setup environment
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt
