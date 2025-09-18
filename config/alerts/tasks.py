from celery import shared_task
from django.contrib.auth.models import User
from .models import Alert, Notification
from .services import push_notification

@shared_task
def run_reminder_engine():
    alerts = Alert.objects.all().order_by('-created_at')[:5]  # demo: pick last 5
    for alert in alerts:
        users = User.objects.filter(profile__team=alert.team)
        for user in users:
            notif, created = Notification.objects.get_or_create(user=user, alert=alert)
            if created:
                push_notification(user.id, f"New alert: {alert.title}")
