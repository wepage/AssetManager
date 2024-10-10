from django.urls import path

from users.views.create_users import CreateUser
from users.views.list_users import ListUsers
from users.views.view_user import ViewUserProfile

urlpatterns = [
    path('profile', ViewUserProfile.as_view(), name='profile-user'),
    path('users/', ListUsers.as_view(), name='list-users'),
    path('users/create', CreateUser.as_view(), name='create-user'),
    path('users/view/<int:pk>', ViewUserProfile.as_view(), name='view-user')

]