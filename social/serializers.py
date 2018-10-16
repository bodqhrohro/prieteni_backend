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
    owner = UserSerializerMini(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner')

    def save(self, **kwargs):
        user = self.context['request'].user

        from social.auth import assert_user_model
        assert_user_model(user)

        self.validated_data['owner'] = user

        return super(PostSerializer, self).save(**kwargs)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializerMini(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user')
