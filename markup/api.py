from rest_framework import viewsets, permissions

from .models import Article, Entity
from .serializers import ArticleSerializer, EntitySerializers


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ArticleSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntitySerializers
