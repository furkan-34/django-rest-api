from django.urls import path, include

from comment.api.views import CommentCreateApiView, CommentListApiView, CommentValidateApiView

app_name = "comment"

urlpatterns = [
    path('create/', CommentCreateApiView.as_view(), name='create'),
    path('list/', CommentListApiView.as_view(), name='list'),
    path('validate/<pk>', CommentValidateApiView.as_view(), name='validate'),

    


]
