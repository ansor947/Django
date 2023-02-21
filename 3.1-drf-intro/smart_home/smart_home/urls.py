"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from measurement.models import Sensor
from measurement.serializers import SensorSerializer
from measurement.views import SensorSpecific, SensorChange, SensorList, SensorSpecific

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  

    path('sensors/', SensorSpecific.as_view(), name='create_sensor'),
    path('sensors/<pk>/', SensorChange.as_view(), name='change_sensor'),
    path('sensors/', SensorList.as_view(), name='list_sensors'),
    path('sensors/<pk>/', SensorSpecific.as_view(), name='specific_sensors'),
    path('sensors/', SensorSpecific.as_view(), name='add_measurement')
]
