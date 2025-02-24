from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=60,
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Entrer votre nom d'utilisateur",
        })
    )

    password = forms.CharField(label='', max_length=60,
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Entrer votre mot de passe",
        })
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
        }),
        label="Ancien mot de passe"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
        }),
        label="Nouveau mot de passe"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
        }),
        label="Confirmer le nouveau mot de passe"
    )