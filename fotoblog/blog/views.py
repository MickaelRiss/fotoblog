from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Photo, Blog
from blog.forms import PhotoForm
@login_required
def home(request):
    photos = Photo.objects.all()
    return render(request, 'blog/home.html', context={'photos': photos})

@login_required
def photo_upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        photo = form.save(commit=False)
        photo.uploader = request.user
        photo.save()
        return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})