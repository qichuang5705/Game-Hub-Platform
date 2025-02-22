from django.urls import path
from .views import chinhsach, data_deletion

urlpatterns = [
    path('privacy-policy/', chinhsach, name="chinhsach"),
    path('data-deletion/', data_deletion, name="data_deletion"),
]
