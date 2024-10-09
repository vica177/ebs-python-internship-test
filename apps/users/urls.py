from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import ListUsersView, RegisterUserView

urlpatterns = [
    path("register", RegisterUserView.as_view(), name="token_register"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("list", ListUsersView.as_view(), name="listUsers"),
]
