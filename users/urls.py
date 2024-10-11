from django.urls import path

from users.views.create_users import CreateUser
from users.views.list_users import ListUsers
from users.views.view_user import ViewUserProfile

urlpatterns = [

    path('/', ListUsers.as_view(), name='list-users'),
    path('profile', ViewUserProfile.as_view(), name='profile-user'),
    path('create', CreateUser.as_view(), name='create-user'),
    path('view/<int:pk>', ViewUserProfile.as_view(), name='view-user'),
    #path('edit/<int:pk>', UpdateUserProfile.as_view(), name='update-user'),
   # path('completeProfile', CompleteUserProfile.as_view(), name='complete-profile-user'),




]