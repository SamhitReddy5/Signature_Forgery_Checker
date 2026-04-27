#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

source .venv/bin/activate

nohup python mac_app.py >/dev/null 2>&1 &

sleep 3

open http://127.0.0.1:5000