from django import forms
from .models import Asset


class createAsset(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name']
