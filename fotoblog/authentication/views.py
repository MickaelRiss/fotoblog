from django.shortcuts import render, redirect
from authentication.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.contrib.auth.decorators import login_required


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