from rest_framework.serializers import ModelSerializer
from .models import asset
class   AssetSerializer(ModelSerializer):
    class Meta:
        model = asset
        fields = ["id","price","type", "description","quantifier","title","create_date","thumnail","User"]
