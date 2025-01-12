from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html', {'user': request.user})


def login(request):
    return render(request, 'login.html')

def changepass(request):
    return render(request, 'password_change_for.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def in4(request):
    return render(request, "in4user.html")

