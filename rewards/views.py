# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Chat, Avatar, FrameAvatar, FrameChat, Inventory
from .forms import InventForm
from django.conf import settings
from django.contrib import messages


@login_required
def change_chat_frame(request):
    if request.method == "POST":
        new_frame = request.POST.get("frame")
        profile, created = CustomUser.objects.get_or_create(user=request.user)
        profile.chat_frame = new_frame
        profile.save()
        return JsonResponse({"status": "success", "new_frame": new_frame})
    return JsonResponse({"status": "error"}, status=400)


@login_required
def Bag(request):
    user = request.user
    invent = Inventory.objects.get(user=user)  # Lấy Inventory của use
    if request.method == "POST":
        form_chat = InventForm(request.POST, user=request.user, instance=invent)
        if form_chat.is_valid():
            form_chat.save()
            return redirect('bag')  # Điều hướng sau khi lưu thành công
        else:
            print(form_chat.errors)
    else:
        form_chat = InventForm( user=request.user, instance=invent)
    return render(request, "bag.html", {'form': form_chat, 'MEDIA_URL': settings.MEDIA_URL})


@login_required
def ShopReward(request):
    chat = FrameChat.objects.all()
    avatar = FrameAvatar.objects.all()
    return render(request, "shop.html", {'MEDIA_URL': settings.MEDIA_URL,'chat': chat, 'avatar':avatar})


@login_required
def buy_frame(request):
    if request.method == "POST":
        frame_id = request.POST.get("frame_id")
        frame_type = request.POST.get("frame_type")
        user = request.user

        if frame_type == "chat":
            frame = get_object_or_404(FrameChat, id=frame_id)
        elif frame_type == "ava":
            frame = get_object_or_404(FrameAvatar, id=frame_id)
        else:
            messages.error(request, "Loại khung không hợp lệ!")
            return redirect("shop")  
        

        if user.points < frame.price:
            messages.error(request, "Bạn không đủ điểm để mua khung này!")
            return redirect("shop") 
        user.points -= frame.price
        user.save()
        if frame_type == "chat":
            Chat.objects.create(user=user, frame_chat=frame)
        elif frame_type == "ava":
            Avatar.objects.create(user=user, frame_avatar=frame)
     
        messages.success(request, "Mua thành công!")
        return redirect("shop")
    else:
        messages.error(request, "Yêu cầu không hợp lệ.")
        return redirect("shop")