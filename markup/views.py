from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer

from .models import Article, Entity
from .serializers import ArticleSerializer, EntitySerializers

from django.http import HttpResponse
from django.shortcuts import render

from markup.models import ConnectedUsers

from django.http import HttpResponse
from markup.tasks import send_email, long_work


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ArticleSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EntitySerializers


def index(request):
    return render(request, 'index.html')


def list_finished_tasks(request):
    return render(request, 'list.html')


def room(request, article_id):
    # Send article by id to user
    news = Article.objects.get(id=article_id)
    if news:
        return render(request, 'room.html', {
            'article_id': article_id,
            'title': news.title,
            'text': news.text
        })
    else:
        return HttpResponse('Wrong article id')


def users_online(request):

    if request.user.is_authenticated:
        connected_users = [user for user in ConnectedUsers.objects.all()]
        return render(request, 'online.html', {
            'connected_users': connected_users
        })


def send_email_task(request):
    email_task_id = send_email.apply_async(queue='email', args=(['some_email@gmail.com'],))
    return HttpResponse(f'The jobs for sending email in progress. Wait for finish. Task id {email_task_id}')


def run_long_task(request):
    ml_task_id = long_work.apply_async(queue='long_task', args=(5,))
    return HttpResponse(f'The jobs are %s and  {ml_task_id}')

