from django.shortcuts import render
from games.models import Game
# Create your views here.
def TestKhungChat(request):
    return render(request, 'comment.html')
