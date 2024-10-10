from django.contrib.auth.views import LogoutView


class AppUserLogout(LogoutView):
    next_page = 'login'
