from django.shortcuts import render, redirect
from .models import Game, Comment
from .form import CommentForm, UpGameForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
import os

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
            return redirect('game_detail', id=game.id)
    else:
        form = CommentForm()
    return render(request,"game_detail.html", {'game':game, 'form':form, 'user':request.user, 'MEDIA_URL': settings.MEDIA_URL})


def DeleteComment(request, comment_id):
    com = Comment.objects.get(id=comment_id)
    if com.users == request.user:
        com.delete()
        return redirect('game_detail',id=com.games.id)
    # else:
    #     return render(request, 'error.html', {'message': 'Bạn không có quyền xóa bình luận này.'})

def Delete_Game(request, game_id):
    game = Game.objects.get(id=game_id)
    if game.user == request.user:
        if game.image:
            image_path = game.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        game.delete()
        return redirect('up_game')

@login_required
def UpGame(request):
    user_games = Game.objects.filter(user=request.user)
    if request.method == "POST":
        form = UpGameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect('home')
    else:
        form = UpGameForm()
    return render(request,'Uploadgame.html', {'form': form, 'games': user_games})