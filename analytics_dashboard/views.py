from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'home.html', {})


def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                error_message = "Oops, something went wrong..."
    
    context = {
        'error_message': error_message,
        'form': form
    }
    return render(request,'login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')