from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView

from favourite.api.pagination import FavouritePagination
from library.permissions import IsAdmin, IsOwnerOrAdmin
from favourite.api.models import Favourite

from favourite.api.serializers import FavouriteListSerializer, FavouriteCreateSerializer

class FavouriteListApiView(ListAPIView):
    pagination_class = FavouritePagination
    serializer_class = FavouriteListSerializer
    
    permission_classes = [IsOwnerOrAdmin]
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Favourite.objects.all()
        else:
            return Favourite.objects.filter(user = self.request.user)
    
    
class FavouriteCreateApiView(CreateAPIView):
    serializer_class = FavouriteCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = serializer.validated_data.get('user'))

class FavouriteDeleteApiView(RetrieveDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListSerializer
    lookup_field = 'pk'
    
    permission_classes = [IsOwnerOrAdmin]
