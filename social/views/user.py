# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from social.models import User
from social.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(UserViewSet, self).get_serializer(*args, **kwargs)
