from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path('ws/markup/tasks/', consumers.TasksConsumer.as_asgi()),
    re_path(r'ws/markup/(?P<article_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
