from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class ActivateAccountView(TemplateView):
    def get(self, request, *args, **kwargs):
        request_for_activate = self.request
        print(request_for_activate)
        if request_for_activate:
            print(f"[activate account rq] {self.request.user}  requested account activation" )
        return render(request, 'activate-account.html', context= {
            'view_name': 'Account need activation',
            'view_description': 'Your account is still not activated'
        })