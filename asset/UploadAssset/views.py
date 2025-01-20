from django.shortcuts import render,render
from django.http import HttpResponse
from rest_framework import viewsets,permissions
from .models import asset
from .serializers import AssetSerializer
from django.shortcuts import render

class AssetViewSet(viewsets.ModelViewSet):
    queryset = asset.objects.filter()
    serializer_class = AssetSerializer
#   permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
