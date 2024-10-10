from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
from users.models import User

"""
View to show specific user profile or to view the logged in user profile as my-profile
reuse same view, same template but on different ednpoint
in the template there is a check to hide a button if its view for my profile or specific user profile

"""
class ViewUserProfile(DetailView):
    model = User
    template_name = 'profile-user.html'
    context_object_name = 'user'

    # Check if 'pk' is in the URL, if not return the logged-in user
    def get_object(self):
        if 'pk' in self.kwargs:
            return get_object_or_404(User, pk=self.kwargs['pk'])
        return self.request.user

    def get_context_data(self, **kwargs):
        ## return custom variables to template
        context = super().get_context_data(**kwargs)

        ## kato na symfony
        context['user_assets'] = []
        context['view_name'] = 'Profile'
        context['view_description'] = 'Detailed view of user profile'
        return context

