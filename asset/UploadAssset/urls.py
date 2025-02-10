from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('list/',asset_list_view, name='asset_create'),
    path('', assetview, name='asset_list'),
    path('asset/<int:asset_id>/',asset_detail, name='asset_detail'),
    path('buy/<int:asset_id>/',buy_asset, name='buy_asset'),
    path('edit/<int:asset_id>/', asset_edit_view, name='edit_asset'),
    path('success/', purchase_success_view, name='purchase_success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)