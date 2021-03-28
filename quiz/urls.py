from django.urls import path
from .views import test, test_list

urlpatterns = [
    path('all-test/', test_list, name='test-list'),
    path('test/<int:id>/', test, name='test'),
]    
