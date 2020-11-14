from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from library.permissions import IsAdmin
from account.api.serializers import UserSerializer, UpdatePasswordSerializer, RegisterSerializer


class ProfileView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj
        
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)
        
        
class ChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdatePasswordSerializer
    model = User
    
    def get_object(self, queryset=None):
        return self.request.user
        
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                
                return Response({"status": False, "error_code": 403,
                                 "message": "Wrong Password"},
                                status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({"status": True, "code": 200}, status=status.HTTP_200_OK)
        else:
            return Response({"status": False, "error_code": "PARAMETERS_REQUIRED", "message": "Validation Error"},
                            status=status.HTTP_400_BAD_REQUEST)
            
            
class CreateUserView(CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer

    

