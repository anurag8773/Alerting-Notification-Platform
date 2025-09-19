# Alerting & Notification Platform (Django + Channels + Celery)

This project implements the PRD using:
- Django + DRF
- Django Channels for WebSocket in-app notifications
- Celery + Redis for background scheduler
- Postgres for DB

## Quick start (Docker)
1. Copy `.env.sample` to `.env` and edit if needed.
2. Run:
   docker-compose up --build

3. App at http://localhost:8000
4. WebSocket endpoint: ws://localhost:8000/ws/notifications/

Seeded users are created by `seed_data` (see management command). Default passwords are in the seed script.

Notes:
- WebSocket connections use Django session auth (log in via admin or endpoints).
- To test reminders, use the admin to create alerts and trigger the `trigger_reminders` admin action or let Celery Beat run every minute.
- This file also include Postman Collection(AlertingPlatform.postman_collection) import it in Postman and test the entry points.
 