from django.shortcuts import render, redirect
from authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                message = f'Bonjour {user.username}, vous avez bien ete connecte'
                return redirect('home')
            else:
                message = 'Nom d\'utilisateur ou mot de passe incorrect'
            
    return render(request, 'authentication/login.html', {'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')