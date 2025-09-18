from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Note: Ensure that the WebSocket consumer is set up to handle "notify" type messages.
def push_notification(user_id, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {"type": "notify", "message": message}
    )
    