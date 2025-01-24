from django.shortcuts import render, redirect,get_object_or_404
from .forms import AssetForm
from .models import asset
from django.http import HttpResponse
def assetview(request):
    if request.method == 'POST':
        form = AssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('asset_list')  
        else:
            print(form.errors) 
    else:
        form = AssetForm()
    return render(request, 'asset_form.html', {'form': form})
def asset_list_view(request):
    assets = asset.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})
def asset_detail(request, asset_id):
    selected_asset = get_object_or_404(asset, id=asset_id)
    return render(request, 'asset_detail.html', {'asset': selected_asset})

def buy_asset(request, asset_id):
    return HttpResponse(f"You have bought asset with ID {asset_id}")

