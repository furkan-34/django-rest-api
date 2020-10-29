from django.urls import path, include
from book.api.views import BookListApiView, BookDetailApiView, BookCreateApiView, BookUpdateDeleteApiView

app_name = "book"

urlpatterns = [
    path('list/', BookListApiView.as_view(), name='list'),
    path('detail/<slug>', BookDetailApiView.as_view(), name='detail'),
    path('create/', BookCreateApiView.as_view(), name='create'),
    path('validate/<pk>', BookUpdateDeleteApiView.as_view(), name='validate')
]