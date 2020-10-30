from django.urls import path, include
from favourite.api.views import FavouriteListApiView, FavouriteCreateApiView, FavouriteDeleteApiView

app_name = "favourite"

urlpatterns = [
    path('list/', FavouriteListApiView.as_view(), name='list'),
    path('create/', FavouriteCreateApiView.as_view(), name='create'),
    path('delete/<pk>', FavouriteDeleteApiView.as_view(), name='delete'),

]