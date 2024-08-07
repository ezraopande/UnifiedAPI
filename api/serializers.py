from rest_framework import serializers
from .models import Product, Sliders, Configs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class SlidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = '__all__'
        
        
        
class ConfigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configs
        fields = '__all__'