
from unicodedata import category
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, response
from main.models import Category,Product
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from main.serializers import CategoryListSerializer,CategorySerializer, ProductListSerializer, ProductSerializer,CategoryListFilterSerializer,ProductListFilterSerializer
from rest_framework.views import APIView,View
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from account.models import User
from django.db import transaction
from rest_framework.permissions import AllowAny
from django.shortcuts import render


class MainIndex(View):
    def get(self,request):
        return render(request,'main/index.html')



class CategoryView(APIView):
    permisson_classes = []
    def get(self, request):
        return Response({
            "categories": CategoryListSerializer(Category.objects.all(),many=True).data
    })
    def post(self, request):
        data = CategorySerializer(data = request.data)
        if not data.is_valid():
            return Response({
                "status":"fail",
                "data":data.errors
            })
        data.save()
        return Response({
            "status":"success",
            "data":CategoryListSerializer(data.instance).data
        })
class CategoryEditView(APIView):
    def get(self,request,pk):
        return Response({
            'category': CategoryListSerializer(Category.objects.get(id=pk)).data
        })   
    def put(self, request,pk):
        data = CategorySerializer(data = request.data)
        if not data.is_valid():
            return Response({
                "status":"fail",
                "data":data.errors
            })
        data.save()
        return Response({
            "status":"success",
            "data":CategoryListSerializer(data.instance).data
        })


    def delete(self, request):
        pass


    def patch(self, request):
        pass

class ProductsView(ListAPIView):
    permisson_classes = []
    pagination_class = LimitOffsetPagination
    queryset = Product.objects.order_by("-updated_at").all().prefetch_related('category')
    serializer_class = ProductListSerializer


class CategoryFilterView(ListAPIView):
    def get(self, request, pk):
        return Response({
            'category': CategoryListFilterSerializer(Product.objects.filter(category_id=pk),many=True).data
        })

class ProductFilterView(ListAPIView):
    search_fields = [ 'name_uz', 'name_en', 'id']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFilterIdView(ListAPIView):
    def get(self,request,pk):
        return Response({
            "product":ProductListFilterSerializer(Product.objects.filter(id=pk),many=True).data
        })
   


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductEditView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductLikeView(APIView):
    
    def get(self,request,pid):
        with transaction.atomic():
            product = Product.objects.select_for_update().get(id=pid)
            if Product.objects.filter(id=product.id,like_users__id = request.user.id).exists():
                product.like -= 1
                product.like_users.remove(request.user)
                product.save()
                return Response({
                    "data":"Siz like ni qaytarib oldingiz"
                })

            product.like += 1
            product.like_users.add(request.user)
            product.save()

            return Response({
                "data":"Siz like bosdingiz"
            })