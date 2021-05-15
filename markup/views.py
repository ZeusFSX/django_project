from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer

from .models import Article, Entity
from .serializers import ArticleSerializer, EntitySerializers


import datetime

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render

from markup.models import ConnectedUsers


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


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


def webhook(request):
    channel_layer = get_channel_layer()
    if not channel_layer.groups:
        return HttpResponse('No any groups available')
    async_to_sync(channel_layer.group_send)(
        list(channel_layer.groups.keys())[0],
        {
            'type': 'chat_message',
            'message': 'Hello from the Web. Current time is %s' % datetime.datetime.now()
        }
    )
    return HttpResponse("Result is OK. Check windows of the firstly created chat for a new message")


def users_online(request):
    connected_users = [str(user) for user in ConnectedUsers.objects.all()]
    return HttpResponse("Currently connected: %s" % connected_users)
