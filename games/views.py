from django.shortcuts import render, redirect
from .models import Game, Comment, Genre, LBHistory
from .form import CommentForm, UpGameForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from .serializers import LBHSerializer, GameSerializer
import os, zipfile, shutil





class LBHistoryViewset(viewsets.ModelViewSet):
    queryset = LBHistory.objects.all().order_by('-score')
    serializer_class = LBHSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user  # Lấy user từ request
        print("User submitting score:", user)  # Debug xem user có đúng không
        serializer.save(users=user)  # Lưu user vào model
    
        

class GameViewset(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    
    @action(detail=True, methods=['post'], url_path='post_score')
    def post_score(self, request, pk=None):
        """
        API POST điểm số cho một game cụ thể
        URL: /API/gameapi/{game_id}/post_score/
        """
        game = Game.objects.get(pk=pk)
        user = request.user  # Lấy user từ request (giả định authentication đã bật)
        score = request.data.get('score')  # Lấy score từ request body

        if score is None:
            return Response({"error": "Score is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Tạo lịch sử điểm mới
        lb_entry = LBHistory.objects.create(games=game, users=user, score=score)
        serializer = LBHSerializer(lb_entry)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def game_detail(request, id):
    game = Game.objects.get(id=id)
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
    
    return render(request,"game_detail.html", {'game':game, 'form':form, 'user':request.user})


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


