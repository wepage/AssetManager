from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from app_auth.forms import LoginForm

"""
#login view supports different custom auth methods
login with person number


"""


class AppUserLogin(LoginView):
    authentication_form = LoginForm  # Custom form if needed
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirect logged-in users away from login page

    ## overrider success redirect
    def get_success_url(self):
        return reverse_lazy('list-users')

    # Override the form_valid method to bypass authentication and manually log in the user
    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        ##
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            print(f"[debug] login failed for {username} / {password} / {user}")
            return self.form_invalid(form)
        if user.name is None or user.email is None:
            print("acount is not complete ?")
            return HttpResponseRedirect(reverse_lazy('complete_account'))
        if user.is_active is False:
            print("account is not active ?")
            return HttpResponseRedirect(reverse_lazy('activate-account'))

        ## everything is ok with user account - login and redirect
        print(f"[debug] loggin user found- {user} / {type(user)}")
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


