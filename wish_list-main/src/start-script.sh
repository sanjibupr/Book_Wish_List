#!/usr/bin/env bash
gunicorn --workers=4 --bind=0.0.0.0:5000 --log-level=info --timeout 50 autoapp:app
