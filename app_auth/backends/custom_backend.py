from django.contrib import messages
from django.contrib.auth.backends import BaseBackend

from users.models import User

"""
depend on provided username deside which type of auth to use
- numeric username - pin auth
- standard - ldap auth

"""


def auth_with_pin(request, pin, password):
    # todo password validation
    user = User.objects.filter(pin=pin).first()
    if user is None:
        messages.error(request, "user not exists?")
        return None
    return user


def auth_with_ldap(request, username, password):
    # todo integrate with ldap
    user = User.objects.filter(name=username).first()
    if user is None:
        messages.error(request, "user not exists?")
        return None
    return user


class CustomBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        username = (kwargs.get('username'));
        password = kwargs.get('password')

        # check type of auth
        if username.isnumeric():
            pin = int(username)
            return auth_with_pin(request, pin=pin, password=password)
        # ldap based auth
        return auth_with_ldap(request, username=username, password=password)

    ## get user from session
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
