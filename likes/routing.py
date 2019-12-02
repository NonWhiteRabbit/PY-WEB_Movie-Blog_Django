from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('likes/', consumers.LikeConsumer)
]
