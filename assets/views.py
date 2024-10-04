from django.shortcuts import render


# Create your views here.

def list(request):
    # list all assets
    return render(request, template_name='list_assets.html')


def create(request):
    pass


def manage(request):
    pass
