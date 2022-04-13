from django.urls import path
from .views import RegionListView,DistrictListView,CountryListView
app_name = 'common'

urlpatterns = [
    path('regionlist/<int:pk>/',RegionListView.as_view(),name='regionlist'),
    path('countrylist/',CountryListView.as_view(),name='countrylist'),
    path('districtlist/<int:pk>/',DistrictListView.as_view(),name='districtlist'),
    
]


