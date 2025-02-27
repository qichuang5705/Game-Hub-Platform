from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('games/', include('games.urls')),
    path('payments/',include('payments.urls')),
    path('security/', include('security.urls')),
    path('store/', include('assets.urls')),
    path('rewards/', include('rewards.urls')),
    path('accounts/', include('allauth.urls')),  # URL của allauth
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)