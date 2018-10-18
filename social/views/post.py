# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status, viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.decorators import action
from rest_framework.response import Response

from social.models import Post, Like
from social.serializers import PostSerializer, LikeSerializer
from social.auth import assert_user_model, is_user_model

from django.db.utils import IntegrityError


class PostPermission(BasePermission):
    def _can_create(self, request, view):
        return True

    def _can_change(self, request, view):
        return request.user.pk == view.get_object().owner.pk

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            is_user_model(request.user) and
            (self._can_create(request, view) if request.method == 'POST' else
                self._can_change(request, view))
        )


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)

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
