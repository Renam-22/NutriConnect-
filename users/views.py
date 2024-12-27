from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from django.contrib.auth.decorators import login_required
from dietary_preferences.views import dietary_preferences_view
from .forms import CustomUserCreationForm,CustomUserProfileForm


@guest
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            bmi = calculate_bmi(form.cleaned_data['weight'], form.cleaned_data['height'])
            request.user.bmi = bmi
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def detail(request):
    return render(request,'auth/user_details.html')

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = CustomUserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            bmi = calculate_bmi(form.cleaned_data['weight'], form.cleaned_data['height'])
            request.user.bmi = bmi
            user = form.save()
            return redirect('dashboard')
    else:
        form = CustomUserProfileForm(instance=request.user)
    return render(request, 'auth/update_profile.html', {'form': form})


def calculate_bmi(weight, height):
        return weight / ((height / 100) ** 2)