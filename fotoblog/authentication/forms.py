from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()

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

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'role']
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Nom d'utilisateur"
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Email"
        }),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Prénom"
        }),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Nom de famille"
        }),
    )
    role = forms.ChoiceField(
        choices= User._meta.get_field('role').choices,
        widget=forms.Select(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 text-sm shadow-xs bg-white",
        })
    )
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Mot de passe"
        }),
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs",
            "placeholder": "Confirmez le mot de passe"
        }),
    )

class UploadProfilePhotoForm(ModelForm):
    class Meta:
        model = User
        fields = ['profile_photo']
    
    profile_photo = forms.ImageField(
        widget=forms.FileInput(attrs={
        "class": "w-full text-sm text-gray-700 file:border-0 file:bg-blue-500 file:text-white file:px-6 file:py-2 file:rounded-lg file:hover:bg-blue-600 file:focus:outline-none file:transition-all file:duration-300"
        })
    )