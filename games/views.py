from django.shortcuts import render, redirect
from .models import Game, Comment, Genre, LBHistory
from .form import CommentForm, UpGameForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import LBHSerializer
import os, zipfile, shutil
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

@method_decorator(csrf_exempt, name='dispatch')
class LBHistoryViewset(viewsets.ModelViewSet):
    queryset = LBHistory.objects.all().order_by('-score')
    serializer_class = LBHSerializer


def game_detail(request, id):
    game = Game.objects.get(id=id)
    csrf_token = get_token(request)  # Lấy CSRF token từ Django

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
    
    return render(request,"game_detail.html", {'game':game, 'form':form, 'user':request.user,  "csrf_token": csrf_token})


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
        if game.file:
            file_path = game.file.path
            parent_path = os.path.dirname(file_path)
            if os.path.exists(parent_path):
                shutil.rmtree(parent_path)
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
            form.save_m2m()    # Lưu mối quan hệ ManyToMany
            if game.file:
                if zipfile.is_zipfile(game.file.path): #Check file zip
                    game.extract()
            return redirect('home')
    else:
        form = UpGameForm()
    return render(request,'Uploadgame.html', {'form': form, 'games': user_games})

@login_required
def Edit_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == "POST":
        form = UpGameForm(request.POST,  request.FILES, instance=game)
        if form.is_valid():
            if 'image' in request.FILES and game.image:
                game.delete()
                
            if 'file' in request.FILES:
                print("file")
                if game.file:
                    old_file = game.file.path
                    if os.path.exists(old_file):
                        os.remove(old_file)
            form.save()
            return redirect('up_game')
    else:
        form = UpGameForm(instance=game)
    return render(request, 'Edit_game.html',{'game': Game, 'form': form})   


