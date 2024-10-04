from django.shortcuts import render, redirect
from .forms import AssetForm


# Create your views here.

def list(request):
    # list all assets
    return render(request, template_name='list_assets.html')


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
