from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.api.models import Comment

from library.permissions import  IsOwnerOrAdmin
from comment.api.pagination import CommentPagination

class CommentCreateApiView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CommentListApiView(ListAPIView):
    
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    
    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        query = self.request.GET.get('q')
        if query:
            queryset =queryset.filter(post = query)
        return queryset
        
    
class CommentValidateApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    
    permission_classes = [IsOwnerOrAdmin]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
