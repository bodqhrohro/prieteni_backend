from .models import User, Post, Like

from rest_framework import serializers, exceptions


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
    owner = UserSerializerMini(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner')

    def save(self, **kwargs):
        if not self.context['request'].user \
                or not isinstance(self.context['request'].user, User):
            raise exceptions.NotAcceptable(
                'You\'re trying to post as wrong user. Don\'t do that')

        self.validated_data['owner'] = self.context['request'].user

        return super(PostSerializer, self).save(**kwargs)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializerMini(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user')
