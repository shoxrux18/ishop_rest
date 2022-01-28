from rest_framework.generics import RetrieveAPIView,UpdateAPIView
from .serializers import ProfileEditSerializer, ProfileSerializer,UpdateUserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
# Create your views here.

class MeView(RetrieveAPIView):
    serializer_class = ProfileSerializer


    def get_object(self):
        return self.request.user



class ChangePasswordView(UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileEditSerializer

class UpdateProfileView(UpdateAPIView):
    
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer