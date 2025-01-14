from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('game.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Thêm đường dẫn này
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
