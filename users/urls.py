from django.urls import path

from users.views.create_users import CreateUser
from users.views.list_users import ListUsers
from users.views.view_user import ViewUser

urlpatterns = [
    path('', ListUsers.as_view(), name='list-users'),
    path('create', CreateUser.as_view(), name='create-user'),
    path('view/<int:user_id', ViewUser.as_view(), name='view-user')
]