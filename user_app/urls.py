from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, LogoutView, DeleteUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),  # Token login
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("<int:pk>/", DeleteUserView.as_view(), name='delete'),
]
