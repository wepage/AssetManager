# forms.py

from django import forms


class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'ldapUser', 'class': 'form-control'}),
        label='Username'
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        label='Password'
    )

    def __init__(self, *args, **kwargs):
        # You can accept a request parameter if needed
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)  # Call the parent constructor
