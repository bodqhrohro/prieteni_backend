# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

from social.models import Post, Like
from social.serializers import PostSerializer, LikeSerializer
from social.auth import assert_user_model

from django.db.utils import IntegrityError


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(PostViewSet, self).get_serializer(*args, **kwargs)

    @action(methods=['post', 'delete'], detail=True)
    def like(self, request, pk=None):
        assert_user_model(request.user)

        if request.method == 'POST':
            try:
                like = Like.set_like(post=self.get_object(), user=request.user)
                serializer = LikeSerializer(like)
                return Response(serializer.data)
            except IntegrityError:
                return Response({'status': 'Already liked.'},
                                status=status.HTTP_409_CONFLICT)
        elif request.method == 'DELETE':
            Like.unlike(post=self.get_object(), user=request.user)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
