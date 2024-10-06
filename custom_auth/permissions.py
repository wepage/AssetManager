from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


class PermissionChecker:
    login_url = 'login'  # URL name for the login page

    def dispatch(self, request, *args, **kwargs):
        # Call the original dispatch method to ensure the standard behavior
        result = super().dispatch(request, *args, **kwargs)

        # Check permissions based on the role defined in the view
        role = getattr(self, 'permission_role', None)
        if role and not self.check_permissions(request, role):
            return self._redirect_to_login(request)

        return result

    def check_permissions(self, request, role):
        print("check for permisions")
        print(role)
        print(request.user)
        if not request.user.is_authenticated:
            return False  # Not logged in

        if role == 'user' and not request.user.is_authenticated:
            return False  # User needs to be logged in

        if role == 'staff' and not request.user.is_staff:
            return False  # Requires staff access

        if role == 'admin' and not request.user.is_superuser:
            return False  # Requires superuser access

        return True  # Permission granted

    def _redirect_to_login(self, request):
        print(f'PERMISSIONS: no permissions for this page? / user: {request.user}')
        messages.error(request, "You do not have rights for this action.")
        return redirect(reverse(self.login_url))
