from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import CustomUser
from .forms import UserForm


class manage_users(ListView):
    model = CustomUser
    template_name = 'manager_users.html'
    paginate_by = 10
    ordering = ['-id']
    context_object_name = 'users'

    # override for the search
    def get_queryset(self):
        name = self.request.GET.get('name', None)  # string ?
        if name is not None:
            ##select where name like %name ?
            return CustomUser.objects.filter(name__icontains=name)
        return CustomUser.objects.all()  # return all

    ## return custom variables to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'User manager'
        context['view_description'] = 'Manage existing users - search by name or create new one'
        return context


class create(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'form_asset.html'
    success_url = reverse_lazy('users_manager')

    def get_context_data(self, **kwargs):
        ## return custom variables to template
        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'Create new asset'
        context['view_description'] = 'create new asset to assign to users'
        return context


class edit(UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'form_asset.html'
    success_url = reverse_lazy('users_manage')

    def get_context_data(self, **kwargs):
        ## return custom variables to template
        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'Edit existing user'
        context['view_description'] = 'edit existing user'
        return context