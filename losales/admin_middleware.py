from inspect import getmodule
import django
from django.contrib import admin
from django.http import Http404, response

class RestrictStaffToAdminMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        module = getmodule(view_func)
        if module is django.contrib.admin.sites and not request.user.is_staff:
            ip = request.META.get('HTTP_X_REAL_IP', request.META.get('REMOTE_ADDR'))
            ua = request.META.get('HTTP_USER_AGENT')
            raise Http404
