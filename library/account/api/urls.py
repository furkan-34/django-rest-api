from django.urls import path, include
from account.api.views import ProfileView, ChangePasswordView, CreateUserView

app_name = "account"

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('register/', CreateUserView.as_view(), name='user_create'),

]