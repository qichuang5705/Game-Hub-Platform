from django.shortcuts import render, redirect
from .models import Game, Comment, Genre, LBHistory
from .form import CommentForm, UpGameForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import LBHSerializer
import os, zipfile


class LBHistoryViewset(viewsets.ModelViewSet):
    queryset = LBHistory.objects.all()
    serializer_class = LBHSerializer

# class LeaderBoardAPIView(viewsets.view):
#     def post(self, request, *args, **kwargs):
#         # Lấy dữ liệu từ request
#         game_id = request.data.get('game_id')
#         user_id = request.data.get('user_id')
#         score = request.data.get('score')

#         if not game_id or not user_id or not score:
#             return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

#         # Kiểm tra xem người chơi đã có điểm trong game này chưa
#         leader_board_game, created = Leader_board_game.objects.update_or_create(
#             games_id=game_id, users_id=user_id, defaults={'score': score}
#         )

#         # Nếu tạo mới, trả về 201 Created. Nếu cập nhật, trả về 200 OK
#         status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK

#         return Response({"message": "Score updated successfully"}, status=status_code)

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
                print("C")
                game.delete()
                
                # name = os.path.basename(game.image.path)
                # old_image = f"{os.path.dirname(game.image.path)}\\games\\image\\{name}"
                # print(old_image)
                # if os.path.exists(old_image):
                #     print("CÓ")
                #     os.remove(old_image)
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


