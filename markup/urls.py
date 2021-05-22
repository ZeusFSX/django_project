from . import views
from django.urls import path

from .views import send_email_task, run_long_task

urlpatterns = [
    path('run_task/send_email/', send_email_task),
    path('run_task/long_work/', run_long_task),
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:article_id>/', views.room, name='article_id'),
]

from markup.models import ConnectedUsers
ConnectedUsers.objects.all().delete()
