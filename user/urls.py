from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user, user_login, user_logout, home

urlpatterns = [
    path('', home, name='Home'),                                    # Home Page
    path('register/', register_user, name='register-user'),         # Register Page
    path('login/', user_login, name='login-user'),                  # Login Page
    path('logout/', user_logout, name='user-logout'),               # Logout Page

    # Password reset url
    path('password-reset/',                                                                             # password-reset
     auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),
     name="reset_password"),

    path('password-reset-done/',                                                                        # password-reset-done
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),          # password-reset-confirm
     name="password_reset_confirm"),

    path('password-reset-complete/',                                                                    # password-reset-complete
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),
]