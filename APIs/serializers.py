from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ModelSerializer

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_size']
        depth = 1