import json

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.models import CustomUser
from .models import CustomLoginForm



# Create your views here.
#from pip._vendor.requests.cookies import MockResponse

class simulateLDAP:
    def __init__(self, status_code):
        self.userdata = None
        self.status_code = status_code


def validate(username, password):
    print(f"todo validate: {username} / {password}")
    return simulateLDAP(200)  # Simulate blocked account


class Logout(LogoutView):
    next_page = reverse_lazy('login')


class CustomLogin(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True  ## if logged user goes to login
    ## overrider success redirect
    def get_success_url(self):
        return reverse_lazy('asset_manager')
    ## overrider the login logic
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(f" form validation?")
        ### bypass
        user = CustomUser.objects.get(name=username)
        print(f"login attemp: {user}")
        if user is not None:
            login(self.request, user)
            print(f"found user: {user}")
            login(self.request, user)
            print(f"logged user: {self.request.user}")
           # print(f"Session data: {self.request.session.items()}")
            return redirect(self.get_success_url())
        form.add_error(None, "non valid case?")
        messages.error(self.request, "non valid case?")
        return self.form_invalid(form)

        customAuthenticatorResponse = validate(username=username, password=password);
        print(f"customAuthResponse: {customAuthenticatorResponse}")
        print(customAuthenticatorResponse)

        if customAuthenticatorResponse is None:
          #  messages.error(self.request, "There was an error connecting to the authentication service.")
            form.add_error(None, "There was an error connecting to the authentication service.")
            return self.form_invalid(form)
        if customAuthenticatorResponse.status_code == 403:
            messages.error(self.request, "Wrong username / password")
            form.add_error(None, "Wrong username / password")
            return self.form_invalid(form)
        if customAuthenticatorResponse.status_code == 409:
            form.add_error(None, "Too many wrong attepts - account is blocked for 5mins")
            messages.error(self.request, "Too many wrong attepts - account is blocked for 5mins")
            return self.form_invalid(form)
        if customAuthenticatorResponse.status_code == 200:
            # todo implement method to return user object, if no existing user -create
            user = self.get_or_create_user(customAuthenticatorResponse.userdata)
            login(self.request, user)
            return redirect(self.get_success_url())
        form.add_error(None, "non valid case?")
        messages.error(self.request, "non valid case?")
        return self.form_invalid(form)

    def get_or_create_user(self, username):
        #todo pass userdata json
        #ldap_userdata = json.loads(userdata)
        ## userdata is json with key-values, name='Name', pin=123, email=user@email.com'
        try:
           # user = Users.objects.get(pin=ldap_userdata['pin'])
            user = Users.objects.get(name=username)
            return user
        except:
            ## create new user
            user = Users.objects.create(
                name=username,
                email='default@mail.com',
                pin=123,
            )
            return user

from django.shortcuts import render

# Create your views here.
