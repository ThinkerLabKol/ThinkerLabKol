from django.urls import path
from .views import register_user, user_login, home

urlpatterns = [
    path('', home, name='Home'),
    path('register/', register_user, name='register-user'),         # Register Page
    path('login/', user_login, name='login-user'),                  # Login Page
]