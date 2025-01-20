from django.shortcuts import render, redirect
from .models import Game, Comment
from .form import CommentForm, UpGameForm
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings


def game_detail(request, id):
    game = Game.objects.get(id=id)
    # com = game.comment_set.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.games = game
            comment.users = request.user
            comment.save()
            return redirect('game', id=game.id)
    else:
        form = CommentForm()
    return render(request,"game_detail.html", {'game':game, 'form':form, 'user':request.user, 'MEDIA_URL': settings.MEDIA_URL})


def DeleteComment(request, comment_id):
    com = Comment.objects.get(id=comment_id)
    if com.users == request.user:
        com.delete()
        return redirect('game',id=com.games.id)
    # else:
    #     return render(request, 'error.html', {'message': 'Bạn không có quyền xóa bình luận này.'})

@login_required
def UpGame(request):
    if request.method == "POST":
        form = UpGameForm(request.POST, request.FILES)
        if form.is_valid():
            Game = form.save()
            return redirect('home')
    else:
        form = UpGameForm()
    return render(request,'Uploadgame.html', {'form': form})