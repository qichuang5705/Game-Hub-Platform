from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from .models import Game, Comment, LBHistory, CustomUser, Ratting
from assets.models import asset
from .form import CommentForm, UpGameForm, RattingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from .serializers import LBHSerializer
import os, zipfile, shutil
from django.db.models import Q
from django.core.paginator import Paginator


# class IsDeveloper(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'developer'

class LBHistoryViewset(viewsets.ModelViewSet):
    serializer_class = LBHSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user  # Lấy user hiện tại
        return LBHistory.objects.filter(games__user=user).order_by('-score')
    
    def perform_create(self, serializer):
        print(self.request)
        user = self.request.user  
        game_id = self.request.session.get("current_game_id")  

        if not game_id:
            return Response({"error": "No game in session"}, status=400)

        game = get_object_or_404(Game, id=game_id)  

        print("User submitting score:", user)  
        print("Game ID:", game.id)  

        serializer.save(users=user, games=game)  
    


def game_detail(request, gameId):
    game = get_object_or_404(Game,id=gameId)
    rating_user = Ratting.objects.get(game=game,user=request.user)
    request.session["current_game_id"] = gameId  # Lưu gameId vào session thực hiện cho API
    comments = game.comment_set.all().order_by('-datecreate')
    paginator = Paginator(comments, 5)  # Hiển thị 5 bình luận mỗi trang
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    game.views+=1
    game.save()
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
        form_type = request.POST.get('form_type')
        print(form_type)
        if form_type == 'form_rating':
            print('form_ratting')
            form_ratting = RattingForm(request.POST)
            if form_ratting.is_valid():
                rating_value = form_ratting.cleaned_data['ratting']
                print(rating_value)
                rating, _ = Ratting.objects.get_or_create(user=request.user, game=game)
                rating.ratting = rating_value
                rating.save()
                TrungBinhRating(game)
                return redirect('game_detail', gameId=game.id)
            else:
                print(form_ratting.errors)
        elif form_type == 'form_comment':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.games = game
                comment.users = request.user
                comment.save()
                return redirect('game_detail', gameId=game.id)
            else:
                print(form.errors)
    else:
        form = CommentForm()
        form_ratting = RattingForm()
    return render(request,"game_detail.html", {'game':game, 'leader':history, 'form':form, 'user':request.user, 'form_ratting': form_ratting, 'phantrang': page_obj, 
                                               'rating_user': rating_user})

def TrungBinhRating(game):
    rating = Ratting.objects.filter(game=game)
    number = rating.count()
    if number > 0:
        tb = 0
        for rate in rating:
            print(rate.ratting)
            tb+= rate.ratting
        tb/=number
        game.ratting = tb
        game.save()

@login_required
def DeleteComment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user == comment.users or request.user.is_superuser:
        comment.delete()
    return redirect ('game_detail', comment.games.id)

@login_required
def Delete_Game(request, game_id):
    if request.user.role != 'developer':
        return redirect('errortruycap')
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
    if request.user.role != 'developer':
        return redirect('errortruycap')
    
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
            messages.success(request, "Game đã được tải lên thành công!")
            return redirect('home')
        else:
            messages.error(request, "Có lỗi xảy ra. Vui lòng kiểm tra lại.")
    else:
        form = UpGameForm()
    return render(request,'Uploadgame.html', {'form': form, 'games': user_games})

@login_required
def Edit_game(request, game_id):
    if request.user.role != 'developer':
        return redirect('errortruycap')
    game = Game.objects.get(id=game_id)
    name_image = os.path.basename(game.image.name)
    parent_image = os.path.dirname(game.image.path)
    if request.method == "POST":
        form = UpGameForm(request.POST,  request.FILES, instance=game)
        if form.is_valid():
            if 'image' in request.FILES:
                path = os.path.join(parent_image, name_image)
                if os.path.exists(path):
                    os.remove(path)
                    
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
    return render(request, 'Edit_game.html',{'game': game, 'form': form})   



def search(request):
    query = request.GET.get('words')  # Lấy từ khóa tìm kiếm 
    view_name = request.GET.get('view')  # Lấy tên view hiện tại game hay shop asset
    print(view_name)
    if not query:
        print("K có words")
        return redirect('home')  # Nếu không có từ khóa, chuyển hướng về view home

    if view_name == 'home':
        print("home")
        # Tìm kiếm trên model Game
        results = Game.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        template_name = 'home.html'  
        variable = 'games'
    elif view_name == 'asset_list':
        print("shop")
        # Tìm kiếm trên model Asset
        results = asset.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        template_name = 'asset_list.html'  
        variable = 'assets'
    else:
        results = []
        variable = 'none'
        template_name = 'home.html' 
    print(template_name)
    print(variable)
    return render(request, template_name, {variable: results, 'query': query})

