from django.urls import path
from calculator.views import counter

urlpatterns = [
    
    path('counter/<str:dishs>/<int:quantitys>/', counter, name = 'counter'),
    
]
