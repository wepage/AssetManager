from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import User
from app_auth.permission_decorator import staff_required


class CreateUser(CreateView):
    model = User
    template_name = 'create-user.html'
    form_class = UserForm
    success_url = reverse_lazy('list-users')
