from django.urls import path
from .views import coding

urlpatterns = [
    path('coding/', coding, name='coding'),    
]