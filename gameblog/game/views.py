from django.shortcuts import render, redirect
from .models import Game, Comment
from .form import *

# Create your views here.
def game(request, id):
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
    return render(request,"game.html", {'game':game, 'form':form, 'user':request.user})

def DeleteComment(request, comment_id):
    com = Comment.objects.get(id=comment_id)
    if com.users == request.user:
        com.delete()
        return redirect('game',id=com.games.id)
    # else:
    #     return render(request, 'error.html', {'message': 'Bạn không có quyền xóa bình luận này.'})