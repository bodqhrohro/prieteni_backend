# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer


class ObtainJWTView(JSONWebTokenAPIView):
    """API endpoint getting a JWT by login/password."""

    serializer_class = JSONWebTokenSerializer
