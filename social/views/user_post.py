# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from social.models import Post
from social.serializers import PostSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing posts of given user."""

    def get_queryset(self):
        return Post.objects.filter(owner=self.kwargs['user_pk'])

    serializer_class = PostSerializer
