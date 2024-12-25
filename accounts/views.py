from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm  # Import both forms

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'account_dashboard')  # Default to 'home' if no 'next' is provided
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect(next_url)
            else:
                form.add_error(None, 'Invalid login credentials')
                messages.error(request, 'Invalid login credentials. Please try again.')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user after validation
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def account_dashboard(request):
    # You can add logic here to get user-specific data
    return render(request, 'accounts/dashboard.html')