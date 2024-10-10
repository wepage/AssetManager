from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from functools import wraps

"""
decorators to manage views based on user
user required - active user
staff required - can access crud views
admin required - staff + crud for users

"""


def user_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_active:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Your account is not active.")

    return _wrapped_view


def staff_required(view_func):
    @user_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_straff or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have access.")

    return _wrapped_view


def superuser_required(view_func):
    @user_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have access.")

    return _wrapped_view
