from django.urls import path
from .views import *

urlpatterns = [
    path('list/',asset_list_view, name='asset_create'),
    path('', assetview, name='asset_list'),
    path('asset/<int:asset_id>/',asset_detail, name='asset_detail'),
    path('buy/<int:asset_id>/',buy_asset, name='buy_asset'),
]
