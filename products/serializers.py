from rest_framework import serializers
from .models import Product
from categories.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Використовуємо лише ID категорії

    class Meta:
        model = Product
        fields = '__all__'  # Включаємо всі поля продукту, зокрема поле категорії (ID категорії)
