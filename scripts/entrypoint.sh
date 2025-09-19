#!/usr/bin/env bash
set -e

# Run migrations, collectstatic, seed and start ASGI server (uvicorn)
python config/manage.py migrate --noinput || true
python config/manage.py collectstatic --noinput || true

# Seed data
python config/manage.py seed_data || true

# Start uvicorn for ASGI (Channels)
uvicorn config.config.asgi:application --host 0.0.0.0 --port 8000
