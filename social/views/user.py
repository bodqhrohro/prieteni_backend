# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import BasePermission

from social.models import User
from social.serializers import UserSerializer
from social.auth import is_user_model


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('HEAD', 'OPTIONS', 'POST'):
            return True
        elif request.method == 'GET':
            return request.user and request.user.is_authenticated
        elif request.method in ('PUT', 'DELETE'):
            return is_user_model(request.user) and \
                request.user.pk == view.get_object().pk
        else:
            return False


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for accessing users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(UserViewSet, self).get_serializer(*args, **kwargs)
