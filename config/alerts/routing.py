from django.urls import re_path
from . import consumers

# Define WebSocket URL patterns
websocket_urlpatterns = [
    re_path(r"ws/notifications/$", consumers.NotificationConsumer.as_asgi()),
]