from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from game.models import Game
def home(request):
    game = Game.objects.all().values()
    return render(request, 'home.html', {'user': request.user, 'game': game})


def login(request):
    return render(request, 'login.html')

def changepass(request):
    return render(request, 'password_change_for.html')

def signup(request):
    if request.method == "POST":
        form = FormUser(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = FormUser()
    return render(request, "signup.html", {"form": form})

def in4(request):
    user = request.user
    if request.method == "POST":
        form = APIin4(request.POST,  instance=user)
        if form.is_valid():
            form.save()
    else:
        form = APIin4( instance=user)
    return render(request, "in4user.html", {'form': form})

