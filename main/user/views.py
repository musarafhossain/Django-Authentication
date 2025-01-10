from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        fm = AuthenticationForm(request, request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully !!')
                return redirect('home')
            else:
                print("Login failed...")
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {
        'form': fm
    })

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
    else:
        fm = RegistrationForm()
    return render(request, 'register.html', {
        'form' : fm,
    })

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'profile.html')