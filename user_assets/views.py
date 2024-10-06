from django.db import connection
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages  # Import the messages framework
from django.views.generic import CreateView

from .models import UserAsset
from assets.models import Asset
from users.models import CustomUser
from .forms import UserAssetForm




class AssignAssetsView(CreateView):
    model = UserAsset
    form_class = UserAssetForm
    template_name = 'assign_asset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['user_id']
        context['user'] = get_object_or_404(CustomUser, id=user_id)
        context['assets'] = Asset.objects.all()
        return context

    def form_valid(self, form):
        ##
        user_id = self.kwargs['user_id']
        user = get_object_or_404(CustomUser, id=user_id)
        asset = form.cleaned_data['asset']
        assigned_date = form.cleaned_data['assigned_date']
        print(f"debug assign asset to user {user}")
        print(f"debug assign asset  {asset}")
        # Create the UserAsset entry
        print(f"Debug: Assigning asset '{asset}' to user '{user}' on '{assigned_date}'")
        print(f"Debug: Assigning asset_id '{asset.id}' to user_id '{user.id}' on '{assigned_date}'")
        user_asset = UserAsset(
            user=user,
            asset=asset,
            assigned_date=assigned_date,
            )

        print(user.id)
        print(f"debug: {user_asset.user} // {user_asset.asset} // {user_asset.assigned_date}")
        # user_asset = UserAsset(
        #     user=user,
        #     asset=asset,
        #     assigned_date=assigned_date,
        #     )
        user_asset = UserAsset.objects.create(
            user=user,
            asset=asset,
            assigned_date=assigned_date
        )
        print(connection.queries[-1])  # Print the last query executed
        print(f'debug new relation: {user_asset}')
        try:
            user_asset.save()
        except:
            print(f'failed?')
            return
        #UserAsset.objects.create(user=user, asset=asset, assigned_date=assigned_date)

        # Add a success message
        messages.success(self.request, 'Success! Asset has been added.')

        return super().form_valid(form)

    def get_success_url(self):
        user_id = self.kwargs['user_id']
        return reverse_lazy('assign_assets', kwargs={'user_id': user_id})