from .models import User
from .serializers import UserSerializer

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions import PermissionDenied


class SocialUserBackend:
    def get_user(user_id):
        try:
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user)
            return serializer.data
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        # dirty hack to allow admin page access via usual credentials
        if (request.path.startswith('/admin')):
            return None

        if username and password:
            # should throw DoesNotExist itself, no need to check
            user = User.objects.get(email=username)
            if check_password(password, user.password):
                serializer = UserSerializer(user)
                django_user = DjangoUser(
                    username=serializer.data['name'],
                    email=serializer.data['email'],
                    pk=serializer.data['id'],
                )
                return django_user
            else:
                return PermissionDenied('Wrong password')
        return None
