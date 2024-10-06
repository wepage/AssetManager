from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_users.as_view(), name='users_manager'),
    path('create', views.create.as_view(), name='users_create'),
    path('edit/<int:pk>', views.edit.as_view(), name='users_edit'),
]