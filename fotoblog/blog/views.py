from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Photo, Blog
from blog.forms import PhotoForm, BlogForm, DeleteBlogForm

@login_required
def home(request):
    photos = Photo.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', context={'photos': photos, 'blogs': blogs})

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

@login_required
def blog_and_photo_upload(request):
    photo_form = PhotoForm()
    blog_form = BlogForm()
    if request.method == 'POST':
        photo_form = PhotoForm(request.POST, request.FILES)
        blog_form = BlogForm(request.POST)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('home')
    return render(request, 'blog/create_blog_post.html', context={'blog_form': blog_form, 'photo_form': photo_form})


@login_required
def blog_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/view_blog.html', context={'blog': blog})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    edit_blog = BlogForm(instance=blog)
    delete_blog = DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_blog = BlogForm(request.POST, instance=blog)
            if edit_blog.is_valid():
                edit_blog.save()
                return redirect('home')
        elif 'delete_blog' in request.POST:
            delete_blog = DeleteBlogForm(request.POST)
            if delete_blog.is_valid():
                blog.delete()
                return redirect('home')
        
    return render(request, 'blog/edit_blog.html', context={'edit_blog': edit_blog, 'delete_blog': delete_blog})