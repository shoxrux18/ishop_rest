from rest_framework.authtoken import views
from django.urls import path

from account.views import ChangePasswordView,UpdateProfileView
from .views import MeView
app_name = 'account'

urlpatterns = [
    path('auth/', views.obtain_auth_token,name='auth'),
    path('me/',MeView.as_view(),name='me'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
]

