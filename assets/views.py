from django.shortcuts import render, redirect
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


def manage(request):
    pass
