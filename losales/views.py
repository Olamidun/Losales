
import urllib.parse
from django.shortcuts import redirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter 
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.urls import reverse

from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = ""


def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'https://localhost:800/store/drinks-and-liquor?{params}')

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://localhost:8000/dj-rest-auth/github/callback'
    client_class = OAuth2Client


    # @property
    # def callback_url(self):
    #     return self.request.build_absolute_uri(reverse('github_callback'))
    # 0e8095933d35171bbc4d4a6b085c3c8341723923
