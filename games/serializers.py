from rest_framework.serializers import ModelSerializer
from .models import LBHistory


class LBHSerializer(ModelSerializer): #Bảng API leader board history
    class Meta:
        model = LBHistory
        fields = ['games', 'users','score']


