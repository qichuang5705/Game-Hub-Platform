from django.shortcuts import render
from . import views

def base(request):
    return render(request, 'api/player/base.html')

def login_page(request):
    years = range(1900, 2026)
    return render(request, 'api/account/login_page.html', {'years': years})

