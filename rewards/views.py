# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Chat, Avatar, FrameAvatar, FrameChat, Inventory
from .forms import ChatForm, AvatarForm
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
        print(request)
        form_type = request.POST.get('form_type')
        print(form_type)
        if form_type == 'avatar_form':
            form_avatar = AvatarForm(request.POST, user=request.user, instance=invent)
            if form_avatar.is_valid():
                form_avatar.save()
                return redirect('bag') 
            else:
                print(form_avatar.errors)
        elif form_type == 'chat_form':
            form_chat = ChatForm(request.POST, user=request.user, instance=invent)
            if form_chat.is_valid():
                form_chat.save()
                return redirect('bag')
            else:
                print(form_chat.errors)
    else:
        form_avatar = AvatarForm(user=request.user, instance=invent)
        form_chat = ChatForm(user=request.user, instance=invent)
    return render(request, "bag.html", {'form_chat': form_chat, 'form_avatar': form_avatar})


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
    