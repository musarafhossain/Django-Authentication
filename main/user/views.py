from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
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
    return render(request, 'profile.html')