from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {"form": form})


def login_view(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return redirect('site:index')

    return render(request, 'account/login.html', {})


@login_required()
def profile_view(request):
    return render(request, 'account/profile.html')


def logout_view(request):
    logout(request)

    return redirect('site:index')

