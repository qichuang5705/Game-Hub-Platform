from django.shortcuts import render, redirect
from .models import Game, Comment
from .form import *
# Create your views here.
def game(request, id):
    game = Game.objects.get(id=id)
    com = game.comment_set.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.games = game
            comment.users = request.user
            comment.save()
    else:
        form = CommentForm()
    return render(request,"game.html", {'game':game,'comment':com, 'form':form})