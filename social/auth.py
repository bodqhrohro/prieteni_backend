from .models import User
from .serializers import UserSerializer

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions import PermissionDenied
from django.test import override_settings

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

AUTH_USER_MODEL = 'social.User'


class SocialUserJSONWebTokenAuthentication(JSONWebTokenAuthentication):
    @override_settings(AUTH_USER_MODEL=AUTH_USER_MODEL)
    def authenticate_credentials(self, payload):
        return super(SocialUserJSONWebTokenAuthentication, self)\
            .authenticate_credentials(payload)


class DummyDjangoUser(DjangoUser):
    def __init__(self, **kwargs):
        super(DummyDjangoUser, self).__init__(**kwargs)


class SocialUserBackend:
    def get_user(user_id):
        try:
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user)
            return serializer.data
        except User.DoesNotExist:
            return None

    @override_settings(AUTH_USER_MODEL=AUTH_USER_MODEL)
    def authenticate(self, request, username=None, password=None):
        # dirty hack to allow admin page access via usual credentials
        if (request and request.path.startswith('/admin')):
            return None

        if username and password:
            # should throw DoesNotExist itself, no need to check
            user = User.objects.get(email=username)
            if check_password(password, user.password):
                serializer = UserSerializer(user)
                django_user = DummyDjangoUser(
                    username=serializer.data['name'],
                    email=serializer.data['email'],
                    pk=serializer.data['id'],
                )
                return django_user
            else:
                return PermissionDenied('Wrong password')
        return None
