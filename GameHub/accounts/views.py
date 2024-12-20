from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'login.html')

def huy(request):
    return HttpResponse("Hello HUy")

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')
 