"""assetManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetManager.as_view(), name='asset_manager'),
    path('create', views.create.as_view(), name='asset_create'),
    path('edit/<int:pk>', views.edit.as_view(), name='asset_edit'),
    # path('', views.list, name="assets_list"),
    # path('create', views.create, name='create_asset'),
    # path('manage', views.manage, name='manage_asset'),
    # path('manage/<int:asset_id>', views.manage, name='manage_asset')
]
