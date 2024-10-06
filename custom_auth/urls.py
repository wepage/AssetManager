from django.urls import path

from .views import CustomLogin, Logout

urlpatterns = [
    path('login', CustomLogin.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout')
]