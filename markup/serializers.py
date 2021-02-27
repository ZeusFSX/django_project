from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article, Entity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class EntitySerializers(serializers.ModelSerializer):
    article = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Entity
        fields = "__all__"
