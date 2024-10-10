from django.views import View
from django.views.generic import DetailView
from users.models import User

class ViewUser(DetailView):
    model = User

