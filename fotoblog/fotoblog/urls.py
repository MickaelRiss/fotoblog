"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import authentication.views
import blog.views
from django.contrib.auth.views import LogoutView, PasswordChangeView
from authentication.forms import CustomPasswordChangeForm
## UNIQUEMENT DANS UN ENV DE DEV PAS PROD
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__', include('django_browser_reload.urls')),
    path('login/', authentication.views.LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/password_change/', PasswordChangeView.as_view(template_name='authentication/password_change.html', form_class=CustomPasswordChangeForm), name='password_change'),
    path('user/profile/', authentication.views.profile, name='profile'),
    path('user/upload_profile_photo/', authentication.views.upload_profile_photo, name='upload_profile_photo'),
    path('signup/', authentication.views.signup, name='signup'),
    path('blog/home/', blog.views.home, name='home'),
    path('blog/photo_upload/', blog.views.photo_upload, name='photo_upload'),
    path('blog/create/', blog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>/', blog.views.blog_view, name='blog_view'),
    path('blog/<int:blog_id>/edit/', blog.views.edit_blog, name='edit_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
