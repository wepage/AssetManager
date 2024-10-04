from django.shortcuts import render, redirect, get_object_or_404
from .forms import AssetForm
from .models import Asset


# Create your views here.

def list(request):
    # list all assets
    assets = Asset.objects.all()
    print(assets)
    return render(request, 'list_assets.html', {'data': assets})


def create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assets_list')
        ##todo handle error ?
    # get request return template ?
    form = AssetForm
    return render(request, 'form_asset.html', {'form': form})


def manage(request, asset_id=None):
    if asset_id:  ## poppylva formata
        #asset = Asset.objects.filter(id=asset_id)
        asset = get_object_or_404(Asset, id=asset_id)
        #form = AssetForm(instance=asset)
    else:
        asset = None;
       # form = AssetForm()  ## prazna forma
    form = AssetForm(instance=asset)
    ## handle form submit
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('assets_list')
        ##todo nevalidna forma ?
    return render(request, 'form_asset.html', {'form': form})
