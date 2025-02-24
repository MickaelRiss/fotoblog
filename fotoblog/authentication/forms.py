from django import forms

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