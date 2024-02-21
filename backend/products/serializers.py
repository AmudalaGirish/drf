from rest_framework import serializers
from .models import Product

class ProductSerailizer(serializers.Serializer):
    model = Product
    fields = [
        'title',
        'content',
        'price',
        'sale_price',
        'get_discount'
    ]