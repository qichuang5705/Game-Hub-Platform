from rest_framework.serializers import ModelSerializer
from .models import LBHistory, Game


class LBHSerializer(ModelSerializer): #Bảng API leader board history
    class Meta:
        model = LBHistory
        fields = ['games','score']


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"