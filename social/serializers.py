from .models import User, Post, Like

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'location', 'bio',
                  'avatar')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserSerializerMini(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'avatar')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner')


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializerMini(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user')
