from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from .models import Game, Comment, Genre, LBHistory, CustomUser
from .form import CommentForm, UpGameForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    
def game_detail(request, gameId):
    game = get_object_or_404(Game,id=gameId)
    history = (
        LBHistory.objects.filter(games=game)  # Lọc lịch sử theo game
        .values('users')  # Chỉ nhóm theo user ID
        .annotate(max_score=Max('score'))  # Lấy điểm cao nhất của từng user
        .order_by('-max_score')  # Sắp xếp theo điểm giảm dần
    )

    # Tạo một dictionary chứa toàn bộ user, với key là user.id
    user_dict = {user.id: user for user in CustomUser.objects.all()}

    # Duyệt qua danh sách history và gán đối tượng user tương ứng
    for entry in history:
        entry['user'] = user_dict[entry['users']]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.games = game
            comment.users = request.user
            comment.save()
            return redirect('game_detail', gameId=game.id)
    else:
        form = CommentForm()
    
    return render(request,"game_detail.html", {'game':game, 'leader':history, 'form':form, 'user':request.user})

@login_required
def DeleteComment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user == comment.users or request.user.is_superuser:
        comment.delete()
    return redirect ('game_detail', comment.games.id)

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
    idgame = Game.objects.order_by('-id').first()
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
    return render(request,'Uploadgame.html', {'form': form, 'games': user_games, 'gameid': idgame})

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