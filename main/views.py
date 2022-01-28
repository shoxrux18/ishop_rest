
from rest_framework.response import Response
from django.http import JsonResponse, response
from main.models import Category,Product
from django.views.decorators.csrf import csrf_exempt

from main.serializers import CategoryListSerializer,CategorySerializer, ProductListSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
class CategoryView(APIView):
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
    pagination_class = LimitOffsetPagination
    queryset = Product.objects.order_by("-updated_at").all().prefetch_related('category')
    serializer_class = ProductListSerializer

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductEditView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

