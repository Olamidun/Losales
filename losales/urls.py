"""losales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount.providers.github.views import oauth2_login
from .views import GoogleLogin, GithubLogin, github_callback, empty_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('password-reset/<uidb64>/<token>', empty_view, name='password_reset_confirm'),
    path('dj-rest-auth/github/', GithubLogin.as_view(), name="gh_login"),
    path('dj-rest-auth/github/callback', github_callback, name='github_callback'),
    path('dj-rest-auth/github/url', oauth2_login ),
    path('store/', include('stores.urls')),
    path('items/', include('items.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
