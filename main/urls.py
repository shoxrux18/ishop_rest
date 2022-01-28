from xml.etree.ElementInclude import include
from django.urls import path
from .views import CategoryView,CategoryEditView,ProductsView,ProductCreateView,ProductEditView

app_name = 'main'

urlpatterns = [
    path("category/",CategoryView.as_view(),name='category'),
    path("category/<int:pk>/",CategoryEditView.as_view(),name='category-edit'),
    path("products/",ProductsView.as_view(),name='products'),
    path("product/",ProductCreateView.as_view(),name='product'),
    path("product/<int:pk>/",ProductEditView.as_view(),name='product'),

    
]