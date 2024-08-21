#!/bin/bash
PROJECT_DIR="/bot/french-news"
source "$PROJECT_DIR/.venv/bin/activate"
python "$PROJECT_DIR/src/main.py"
deactivate
