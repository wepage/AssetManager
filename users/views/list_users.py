from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from users.models import User


class ListUsers(ListView):
    model = User
    template_name = 'list-users.html'
    context_object_name = 'users'

    def get_queryset(self):
        # Debugging messages
        print(f"[debug] In ListUsers view - Current user: {self.request.user} / {type(self.request.user)}")
        print(f"[debug] User is authenticated: {self.request.user.is_authenticated}")
        print(f"[debug] Incoming request user: {self.request.user} / Authenticated: {self.request.user.is_authenticated}")
        print(f"[debug] Session data: {self.request.session.items()}")

        # Return the queryset for users
        return super().get_queryset()
