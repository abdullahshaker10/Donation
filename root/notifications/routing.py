from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Make the pattern match from the start and be more specific
    re_path(r'^notifications/ws$', consumers.NotificationConsumer.as_asgi()),
]