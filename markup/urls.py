from . import views
from django.urls import path

urlpatterns = [
    path('webhook/', views.webhook),
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

from markup.models import ConnectedUsers
ConnectedUsers.objects.all().delete()
