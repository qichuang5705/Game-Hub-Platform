from django.shortcuts import render, redirect,get_object_or_404
from .forms import AssetForm
from .models import * 
from django.http import HttpResponse,HttpResponseForbidden,FileResponse
from django.core.files.storage import default_storage
from payments.models import Wallet
from django.contrib import messages
from django.db import transaction
from payments.models import *
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def assetview(request):
    if request.user.role != 'designer':
        return redirect('errortruycap')
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            asset = form.save(commit=False) 
            asset.owner = request.user  
            form.save()  
            return redirect('asset_upload')  
        else:
            print(form.errors) 
    else:
        form = AssetForm()
    return render(request, 'asset_form.html', {'form': form})


@login_required
def asset_list_view(request):
    if request.user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    user = request.user  # Lấy người dùng đã đăng nhập
    assets = asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets,'MEDIA_URL': settings.MEDIA_URL})

@login_required
def asset_detail(request, asset_id):
    if request.user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    selected_asset = get_object_or_404(asset, id=asset_id)
    return render(request, 'asset_detail.html', {'asset': selected_asset,'MEDIA_URL': settings.MEDIA_URL})


@login_required
def asset_edit_view(request, asset_id):
    if request.user.role != 'designer':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    asset_obj = get_object_or_404(asset, id=asset_id)  

    if request.method == 'POST':
        asset_obj.title = request.POST.get('title', asset_obj.title)
        asset_obj.price = request.POST.get('price', asset_obj.price)
        asset_obj.type = request.POST.get('type', asset_obj.type)
        asset_obj.description = request.POST.get('description', asset_obj.description)

      
        if 'thumnail' in request.FILES:
            if asset_obj.thumnail:
                default_storage.delete(asset_obj.thumnail.path)  
            asset_obj.thumnail = request.FILES['thumnail']

      
        if 'file' in request.FILES:
            if asset_obj.file:
                default_storage.delete(asset_obj.file.path)  
            asset_obj.file = request.FILES['file']

        asset_obj.save()
        return redirect('asset_list')  

    return render(request, 'edit_asset.html', {'asset': asset_obj})

@login_required
def asset_buy_view(request, asset_id):
    if request.user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')


    asset1 = get_object_or_404(asset, id=asset_id)
    wallet, _ = Wallet.objects.get_or_create(user=request.user)

    if Purchase.objects.filter(user=request.user, asset=asset1).exists():
        messages.warning(request, "Bạn đã mua asset này trước đó!")
        return redirect("purchase_success")

    if wallet.balance < asset1.price:
        messages.error(request, "Số dư không đủ để mua sản phẩm này!")
        return redirect("asset_list")

    try:
        with transaction.atomic():
            # Trừ tiền từ ví
            wallet.balance -= asset1.price
            wallet.save()

            # Ghi lại lịch sử giao dịch
            TransactionHistory.objects.create(
                user=request.user,
                transaction_type="purchase",
                amount=asset1.price,
                status="success",
                balance_after_transaction=wallet.balance
            )

            # Tạo giao dịch mua hàng
            Purchase.objects.create(user=request.user, asset=asset1, payment_method="wallet")

        messages.success(request, f"Mua {asset1.title} thành công! Số dư còn lại: {wallet.balance} USD")
    except Exception as e:
        messages.error(request, f"Có lỗi xảy ra: {str(e)}")

    return redirect("purchase_success")

@login_required
def purchase_success_view(request):
    if request.user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')


    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'purchase_success.html', {'purchases': purchases})

@login_required
def download_asset_view(request, asset_id):
    if request.user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    asset1 = get_object_or_404(asset, id=asset_id) 

    if asset.file:  
        response = FileResponse(asset1.file.open('rb'), as_attachment=True)
        return response

    return HttpResponse("File không tồn tại", status=404)

@login_required
def purchase_asset(request, asset_id):
    if request.user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    asset = get_object_or_404(asset, id=asset_id)
    
    wallet, _ = Wallet.objects.get_or_create(user=request.user)


    if Purchase.objects.filter(user=request.user, asset=asset).exists():
        messages.warning(request, "Bạn đã mua asset này trước đó!")
        return redirect("store")


    if wallet.balance < asset.price:
        messages.error(request, "Số dư không đủ để mua sản phẩm này!")
        return redirect("store")

    try:
        with transaction.atomic():

            wallet.balance -= asset.price
            wallet.save()


            TransactionHistory.objects.create(
                user=request.user,
                transaction_type="purchase",
                amount=asset.price,
                status="success",
                balance_after_transaction=wallet.balance
            )

            # Lưu giao dịch mua asset
            Purchase.objects.create(user=request.user, asset=asset, payment_method="wallet")

        messages.success(request, f"Mua {asset.title} thành công! Số dư còn lại: {wallet.balance} USD")
    except Exception as e:
        messages.error(request, f"Có lỗi xảy ra: {str(e)}")

    return redirect("store")

@login_required
def delete_asset(request, asset_id):
    if request.user.role != 'designer' :
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    asset_obj = get_object_or_404(asset, id=asset_id)

    # Debug xem user hiện tại và owner của asset
    print(f"Current User: {request.user.id}, Asset Owner: {asset_obj.owner.id if asset_obj.owner else None}")
    print(request.user)
    # Kiểm tra quyền sở hữu
    if asset_obj.owner != request.user:
        messages.error(request, "Bạn không có quyền xóa asset này!")
        return redirect("asset_detail", asset_id=asset_obj.id)

    asset_obj.delete()
    messages.success(request, "Asset đã được xóa thành công!")
    return redirect("asset_list")