from rest_framework import serializers

from main.models import Category,Product

class CategoryListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only = True)
    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only = True)
    category = CategoryListSerializer(read_only = True)
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only = True)
    class Meta:
        model = Product
        exclude = ("added_at","updated_at")
