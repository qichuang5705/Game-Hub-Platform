from django.shortcuts import render
from .models import Game, Comment
# Create your views here.
def game(request, id):
    game = Game.objects.get(id=id)
    com = game.comment_set.all()
    return render(request,"game.html", {'game':game,'comment':com})