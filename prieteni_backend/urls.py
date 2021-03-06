"""prieteni_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, static
from django.contrib import admin

from social.urls import router as social_router, \
    user_router as social_user_router, \
    post_router as social_post_router

from social.views import ObtainJWTView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include(social_router.urls)),
    url(r'^', include(social_user_router.urls)),
    url(r'^', include(social_post_router.urls)),

    url(r'^api-token-auth', ObtainJWTView.as_view()),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
