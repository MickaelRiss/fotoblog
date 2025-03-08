from django import forms
from blog.models import Photo, Blog

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']

    image = forms.ImageField(
        widget=forms.FileInput(attrs={
        "class": "w-full text-sm text-gray-700 file:border-0 file:bg-blue-500 file:text-white file:px-6 file:py-2 file:rounded-lg file:hover:bg-blue-600 file:focus:outline-none file:transition-all file:duration-300"
    }))
    caption = forms.CharField(
        widget=forms.TextInput(attrs={
        "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs"
        }),    
        label='Description'
    )

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
        "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs"
        }),
        label='Titre'
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
        "class": "w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-xs"
        }),
        label='Contenu' 
    )