# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Shop, Inventory
from .forms import InventForm, ShopForm
from django.conf import settings
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
    if request.method == "POST":
        form = InventForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu dữ liệu vào database
            return redirect('bag')  # Điều hướng sau khi lưu thành công
    else:
        form = InventForm()
    return render(request, "bag.html", {'form': form, 'MEDIA_URL': settings.MEDIA_URL})


@login_required
def ShopReward(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu dữ liệu vào database
            return redirect('shop')  # Điều hướng sau khi lưu thành công
    else:
        form = ShopForm()
    return render(request, "shop.html", {'form': form, 'MEDIA_URL': settings.MEDIA_URL})
