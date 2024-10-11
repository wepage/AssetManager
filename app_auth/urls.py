from django.urls import path

from app_auth.views.activate_account import ActivateAccountView
from app_auth.views.login import AppUserLogin
from app_auth.views.logout import AppUserLogout

urlpatterns = [
    path('login', AppUserLogin.as_view(), name='login'),
    path('logout', AppUserLogout.as_view(), name='logout'),
    path('activate-account', ActivateAccountView.as_view(), name='activate-account'),
]