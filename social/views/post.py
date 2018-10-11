# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from social.models import Post
from social.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
