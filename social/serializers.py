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
    liked_by_me = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'likes_count', 'liked_by_me')

    def save(self, **kwargs):
        user = self.context['request'].user

        from social.auth import assert_user_model
        assert_user_model(user)

        self.validated_data['owner'] = user

        return super(PostSerializer, self).save(**kwargs)

    def get_liked_by_me(self, obj):
        user = self.context['request'].user

        from social.auth import assert_user_model
        try:
            assert_user_model(user)
        except exceptions.NotAcceptable:
            return None

        return obj.liked_by(user)


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializerMini(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user')
