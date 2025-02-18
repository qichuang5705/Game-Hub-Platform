from django.urls import path, include
from .views import Bag, ShopReward
urlpatterns = [
    path('', Bag, name="test"),
    path('shop/', ShopReward, name="shop"),
] 