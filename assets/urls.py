from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('list/',asset_list_view, name='asset_list'),
    path('', assetview, name='asset_upload'),
    path('asset/<int:asset_id>/',asset_detail, name='asset_detail'),
    path('buy/<int:asset_id>/',asset_buy_view, name='asset_buy_view'),
    path('edit/<int:asset_id>/', asset_edit_view, name='edit_asset'),
    path('success/', purchase_success_view, name='purchase_success'),
    path('download/<int:asset_id>/', download_asset_view, name='download_asset'),
]
