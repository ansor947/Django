from django.urls import path
from calculator.views import counter

urlpatterns = [
    
    path('counter/', counter, name = 'counter'),
    
]
