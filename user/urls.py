from django.urls import path
from .views import register_user, user_login, user_logout, home

urlpatterns = [
    path('', home, name='Home'),                                    # Home Page
    path('register/', register_user, name='register-user'),         # Register Page
    path('login/', user_login, name='login-user'),                  # Login Page
    path('logout/', user_logout, name='user-logout')                # Logout Page
]