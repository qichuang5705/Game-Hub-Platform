from django.shortcuts import render, redirect,get_object_or_404
from .forms import AssetForm
from .models import * 
from django.http import HttpResponse,HttpResponseForbidden,FileResponse
<<<<<<< HEAD
from django.core.files.storage import default_storage
=======

>>>>>>> 31e47d73b7f2b19a82600966750bb9fc2e592487
def assetview(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('asset_upload')  
        else:
            print(form.errors) 
    else:
        form = AssetForm()
    return render(request, 'asset_form.html', {'form': form})

def asset_list_view(request):
    if not request.user.is_authenticated:
        # Nếu người dùng chưa đăng nhập
        return render(request, 'ErrorLogin.html')
    
    user = request.user  # Lấy người dùng đã đăng nhập
    if user.role == 'player':
        # Nếu người dùng  là player, không thể truy cap
        return render(request, 'ErrorTruyCap.html')
    assets = asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets,'MEDIA_URL': settings.MEDIA_URL})
def asset_detail(request, asset_id):
    selected_asset = get_object_or_404(asset, id=asset_id)
    return render(request, 'asset_detail.html', {'asset': selected_asset,'MEDIA_URL': settings.MEDIA_URL})

def asset_edit_view(request, asset_id):
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

def asset_buy_view(request, asset_id):
    asset1 = get_object_or_404(asset, id=asset_id)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        Purchase.objects.create(user=None, asset=asset1, payment_method=payment_method)
        return redirect('purchase_success')

    return render(request, 'buy_asset.html', {'asset': asset1,'MEDIA_URL': settings.MEDIA_URL})


def purchase_success_view(request):
    user = request.user if request.user.is_authenticated else None 
    
    #purchases = Purchase.objects.filter(user=user) if user else []  
    purchases = Purchase.objects.all()
    return render(request, 'purchase_success.html', {'purchases': purchases})

def download_asset_view(request, asset_id):
    asset1 = get_object_or_404(asset, id=asset_id) 

    if asset.file:  
        response = FileResponse(asset1.file.open('rb'), as_attachment=True)
        return response

    return HttpResponse("File không tồn tại", status=404)