from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from book.api.pagination import BookPagination

from book.api.serializers import BookSerializer, BookCreateSerializer, BookUpdateDeleteSerializer
from book.api.models import Book
from library.permissions import IsAdmin


class BookListApiView(ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_filters = ['title', 'content']
    pagination_class = BookPagination
    
    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

class BookDetailApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

class BookCreateApiView(ListCreateAPIView):
    permission_classes = [IsAdmin]

    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class BookUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]

    queryset = Book.objects.all()
    serializer_class = BookUpdateDeleteSerializer
    lookup_field = 'pk'


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

