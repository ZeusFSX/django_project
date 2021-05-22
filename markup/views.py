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
from markup.tasks import add, mul


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


def run_task(request):
    sum_task_id = add.apply_async(queue='low_priority', args=(5, 5))
    ml_task_id = mul.apply_async(queue='low_priority', args=(5, 5))
    return HttpResponse('The jobs are %s and %s' % (sum_task_id, ml_task_id))
