# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, TableRewards
from .forms import TableChat
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
def chat_view(request):
    user = request.user
    table = TableRewards.objects.get(userid=user)

    form = TableChat(instance=table)  

    if request.method == "POST":
        form = TableChat(request.POST, instance=table)  # Cập nhật dữ liệu
        if form.is_valid():
            form.save()

    return render(request, "comment.html", {'form': form,'table': table})