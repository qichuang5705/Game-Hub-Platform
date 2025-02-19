from django.urls import path, include
from .views import Bag, ShopReward, buy_frame
urlpatterns = [
    path('', Bag, name="bag"),
    path('shop/', ShopReward, name="shop"),
     path('buy/', buy_frame, name="buy"),
] 