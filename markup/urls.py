from . import views
from django.urls import path

urlpatterns = [
    path('webhook/', views.webhook),
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:article_id>/', views.room, name='article_id'),
]

from markup.models import ConnectedUsers
ConnectedUsers.objects.all().delete()
