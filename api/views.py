from django.shortcuts import render
from .models import Product, Sliders, Configs
from .serializers import ProductSerializer, SlidersSerializer, ConfigsSerializer
from rest_framework import viewsets

# class based view
# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    



class SlidersView(viewsets.ModelViewSet):
    queryset = Sliders.objects.all()
    serializer_class = SlidersSerializer



class ConfigsView(viewsets.ModelViewSet):
    queryset = Configs.objects.all()
    serializer_class = ConfigsSerializer