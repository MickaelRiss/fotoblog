from django.shortcuts import render, redirect
from authentication.forms import LoginForm, SignUpForm, UploadProfilePhotoForm
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.conf import settings

#### EXEMPLE DU CODE EXECUTE POUR LoginView
class LoginPage(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            message = 'Nom d\'utilisateur ou mot de passe incorrect'

        return render(request, self.template_name, {'form': form, 'message': message})
    
@login_required
def profile(request):
    user = request.user
    return render(request, 'authentication/profile.html', {'user': user})

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    
    return render(request, 'authentication/signup.html', {'form': form})

@login_required
def upload_profile_photo(request):
    form = UploadProfilePhotoForm(instance=request.user)
    actual_photo = request.user.profile_photo.url
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        photo = form.save(commit=False)
        photo.uploader = request.user
        form.save()
        return redirect('profile')

    return render(request, 'authentication/upload_profile_photo.html', {'form': form, 'actual_photo': actual_photo})
