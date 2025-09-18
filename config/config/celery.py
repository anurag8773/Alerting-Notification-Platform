import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Example schedule
app.conf.beat_schedule = {
    'run-reminder-engine-every-minute': {
        'task': 'alerts.tasks.run_reminder_engine',
        'schedule': 60.0,
    }
}
