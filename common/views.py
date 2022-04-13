from .models import Region,Country,District
from rest_framework.generics import ListAPIView
from common.serializer import CountrySerializer,DistrictSerializer,RegionSerializer 
# Create your views here.
from rest_framework.response import Response
class CountryListView(ListAPIView):
  
       
       
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class RegionListView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get(self, request,pk):
            return Response({
            'category': RegionSerializer(Region.objects.filter(country=pk),many=True).data
        })
   
    

class DistrictListView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def get(self, request,pk):
            return Response({
            'category': DistrictSerializer(District.objects.filter(region=pk),many=True).data
        })