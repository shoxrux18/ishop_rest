from django.urls import path
from .views import DeliveryAddressListView,DeliveryAddressCreateView,DeliveryAddressEditView
from .views import OrderCreateView,OrderListView,OrderStatusView

app_name = 'cart'

urlpatterns = [
    path('delivery-addresses/',DeliveryAddressListView.as_view(),name = 'delivery-address-list'),
    path('delivery-address/',DeliveryAddressCreateView.as_view(),name='delivery-address-create'),
    path('delivery-address/<int:pk>/',DeliveryAddressEditView.as_view(),name='delivery-address-edit'),
    path('order/',OrderCreateView.as_view(),name='order'),
    path('orders/',OrderListView.as_view(),name='orders'),
    path('order/status/<int:pk>/<int:status>/',OrderStatusView.as_view(),name='order-status')
]

