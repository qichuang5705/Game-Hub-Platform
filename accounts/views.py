from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponseForbidden, HttpResponse 

#Chuyển trang theo vai trò
def redirect_base_on_role(user):
    if user.is_superuser:
        user.role = 'admin'
        return redirect('/admin/')
    elif user.role == 'player':
        return redirect('#')
    elif user.role == 'developer':
        return redirect('#')
    elif user.role == 'designer':
        return redirect('#')

def login_view(request): # đổi tên hàm thành login_view tránh xung đột hàm login có sẵn của django
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}")
                return redirect_base_on_role(user)
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def huy(request):
    return HttpResponse("Hello HUy")

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')
 