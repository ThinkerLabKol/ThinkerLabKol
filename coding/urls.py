from django.urls import path
from .views import coding, coding_registration, success

urlpatterns = [
    path('coding/', coding, name='coding'),
    path('coding-registration/', coding_registration, name='coding-registration'),
    path('coding-registration-success/', success, name='coding-success')
]
