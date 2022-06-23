from asyncore import write
from dataclasses import field
from rest_framework.serializers import ValidationError
from rest_framework import serializers
from common.serializer import CountrySerializer,RegionSerializer,DistrictSerializer
from .models import DeliveryAddress,Order,OrderProduct
from main.models import Product


class DeliveryAddressListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    region = RegionSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)
    class Meta:
        model = DeliveryAddress
        exclude = ['user']


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        exclude = ['user']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OrderProduct
        fields = ('product','quantity')

    def validate(self, attrs):
       data = super().validate(attrs)
       if attrs['product'].available < attrs['quantity']:
        raise ValidationError({"quantity":f"Iltimos,{attrs['product'].available} ta kiriting"})
       return data
        

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many = True, write_only=True)

    class Meta:
        model = Order
        fields = ('delivery_address', 'products')

    def create(self, validated_data):
        products = validated_data.pop('products')
        total_price = 0
        for row in products:
            total_price += row['product'].price * row['quantity']

        validated_data['total_price'] = total_price

        order = super().create(validated_data=validated_data)

        for row in products:

            product = Product.objects.select_for_update().get(id=row['product'].id)
            if product.available < row['quantity']:
                raise Exception("NOT FOUND")

            product.available -= row['quantity']
            product.save()

            OrderProduct.objects.create(order=order,price=row['product'].price,**row)

        return order


class ProductForOrderListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only = True)
    class Meta:
        model = Product
        fields = ('id','name')



class OrderProductListSerializer(serializers.ModelSerializer):
    product = ProductForOrderListSerializer(read_only=True)
    class Meta: 
        model = OrderProduct
        fields = ('product','quantity','price')




class OrderListSerializer(serializers.ModelSerializer):
    delivery_address = DeliveryAddressListSerializer(read_only=True)
    orderproduct_set = OrderProductListSerializer(many = True,read_only=True)
    class Meta:
        model=Order
        exclude = ['user']


