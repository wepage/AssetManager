from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from custom_auth.permissions import PermissionChecker
from .forms import AssetForm
from .models import Asset


# Create your views here.
class create(PermissionChecker, CreateView):
    permission_role = 'admin'  # Define required permission role
    model = Asset
    form_class = AssetForm
    template_name = 'form_asset.html'
    success_url = reverse_lazy('asset_manager')
    def get_context_data(self, **kwargs):
        ## return custom variables to template
        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'Create new asset'
        context['view_description'] = 'create new asset to assign to users'
        return context

class edit(UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = 'form_asset.html'
    success_url = reverse_lazy('asset_manager')
    def get_context_data(self, **kwargs):
        ## return custom variables to template
        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'Edit existing asset'
        context['view_description'] = 'edit existing asset'
        return context


class view(DetailView):
    model = Asset
    template_name = 'asset_detail_view.html'
    context_object_name = 'asset'  # Optional, to specify the context name for the object
    def get_context_data(self, **kwargs):
        ## return custom variables to template
        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'Details of asset'
        context['view_description'] = 'Details of asset'
        return context


class AssetManager(ListView):
    model = Asset
    template_name = 'manager_assets.html'
    paginate_by = 5
    ordering = ['-id']
    context_object_name = 'assets'

    #override for the search
    def get_queryset(self):
        name = self.request.GET.get('name', None)  # string ?
        if name is not None:
            ##select where name like %name ?
            return Asset.objects.filter(name__icontains=name)
        return Asset.objects.all()  # return all

    ## return custom variables to template
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        ## kato na symfony
        context['view_name'] = 'Asset manager'
        context['view_description'] = 'Manage existing assets - search by name or create new one'
        return context

class UserAssetManager(AssetManager):
    pass;
    # ## override tova koeto e razli4no
    # # Get base queryset from parent class (SearchAssetView)
    # queryset = super().get_queryset()
    #
    # # search by user logged in
    # user = self.request.user
    # user_assets = UserAsset.objects.filter(user=user).values_list('asset_id', flat=True)
    # return queryset.filter(id__in=user_assets)

### old function based view
# def list(request):
#     # list all assets
#     assets = Asset.objects.all()
#     print(assets)
#     return render(request, 'list_assets.html', {'data': assets})
#
#
# def create(request):
#     if request.method == 'POST':
#         form = AssetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('assets_list')
#         ##todo handle error ?
#     # get request return template ?
#     form = AssetForm
#     return render(request, 'form_asset.html', {'form': form})
#
#
# def manage(request, asset_id=None):
#     if asset_id:  ## poppylva formata
#         #asset = Asset.objects.filter(id=asset_id)
#         asset = get_object_or_404(Asset, id=asset_id)
#         view_name = "Manage asset"
#         #form = AssetForm(instance=asset)
#     else:
#         asset = None
#         view_name = "Create asset"
#        # form = AssetForm()  ## prazna forma
#     form = AssetForm(instance=asset)
#     ## handle form submit
#     if request.method == 'POST':
#         form = AssetForm(request.POST, instance=asset)
#         if form.is_valid():
#             form.save()
#             return redirect('assets_list')
#         ##todo nevalidna forma ?
#     return render(request, 'form_asset.html', {'view_name': view_name,'form': form})