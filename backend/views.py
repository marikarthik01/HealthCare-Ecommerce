from django.shortcuts import render
from .models import Products  
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class Productsview(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer