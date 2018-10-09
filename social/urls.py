from rest_framework_nested import routers

from .views import PostViewSet, UserViewSet, UserPostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'posts', UserPostViewSet, base_name='user-post')
