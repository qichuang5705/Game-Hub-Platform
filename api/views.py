from django.shortcuts import render
from . import views

def base(request):
    years = range(1900, 2026)
    return render(request, 'api/base.html', {'years': years})

def game(request):
     return render(request, 'api/page_game.html')

def donate(request):
     return render(request, 'api/donate.html')
