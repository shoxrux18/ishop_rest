
from rest_framework.serializers import ValidationError
from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from django.db import transaction
from cart.models import DeliveryAddress,Order
from cart.serializers import DeliveryAddressListSerializer,DeliveryAddressSerializer
from cart.serializers import OrderSerializer,OrderProductSerializer,OrderListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DeliveryAddressListView(ListAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressListSerializer


    def filter_queryset(self,queryset):
        return queryset.filter(user = self.request.user)


class DeliveryAddressCreateView(CreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer


    def perform_create(self,serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.save()

class DeliveryAddressEditView(RetrieveUpdateDestroyAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer

    def filter_queryset(self,queryset):
        return queryset.filter(user = self.request.user)

class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class =  OrderSerializer

    def perform_create(self,serializer):
        with transaction.atomic():
            serializer.validated_data['user'] = self.request.user
            serializer.save()


class OrderListView(ListAPIView):
    queryset = Order.objects.all().prefetch_related('delivery_address',
    'delivery_address__country','delivery_address__region','delivery_address__district',
    'orderproduct_set','orderproduct_set__product')
    serializer_class = OrderListSerializer


    def filter_queryset(self,queryset):
        return queryset.filter(user = self.request.user)
        

class OrderStatusView(APIView):
    def post(self,request,pk,status):
        order = Order.objects.get(id=pk)

        if status not in Order.STATUS_CHECK or status not in Order.STATUS_CHECK[order.status]:
            raise Response({
                "status":"fail",
                "data":"Status qiymati no'to'gri"
            })

        Order.objects.filter(id=pk).update(status=status)

        return Response({
            "status":"success",
            "data":{
                "status":status
            }
        })