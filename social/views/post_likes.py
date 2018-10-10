# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from social.models import Post
from social.serializers import LikeSerializer


class PostLikeViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing posts."""

    def get_queryset(self):
        Post.objects.get(pk=self.kwargs['post_pk'])

    serializer_class = LikeSerializer
