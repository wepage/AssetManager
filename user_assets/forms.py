from django import forms
from .models import UserAsset


class UserAssetForm(forms.ModelForm):
    class Meta:
        model = UserAsset
        fields = ['asset', 'assigned_date']
        widgets = {
            'assigned_date': forms.DateInput(attrs={'type': 'date'}),
        }