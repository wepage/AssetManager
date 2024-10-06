from django.urls import path
from .views import AssignAssetsView

urlpatterns = [
    path('assets/assign/<int:user_id>/', AssignAssetsView.as_view(), name='assign_assets'),
]