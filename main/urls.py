from django.urls import path
from .views import CategoryView,CategoryEditView,ProductsView,ProductCreateView,ProductEditView
from .views import CategoryFilterView,ProductFilterView,ProductFilterIdView,ProductLikeView
app_name = 'main'

urlpatterns = [
    path("category/",CategoryView.as_view(),name='category'),
    path("category/<int:pk>/",CategoryEditView.as_view(),name='category-edit'),
    path("products/",ProductsView.as_view(),name='products'),
    path("product/",ProductCreateView.as_view(),name='product'),
    path("product/<int:pk>/",ProductEditView.as_view(),name='product'),
    path("category_id/<int:pk>/",CategoryFilterView.as_view(),name="category_id"),
    path('productss/',ProductFilterView.as_view(),name='productss'),
    path('product_id/<int:pk>/',ProductFilterIdView.as_view(),name="product_id"),
    path('product_like/<int:pid>/',ProductLikeView.as_view(),name="product_like")

    
]