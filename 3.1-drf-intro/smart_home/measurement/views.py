from requests import Response

from .models import Sensor

from .serializers import SensorSerializer

from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend



class SensorSpecific(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']

    def post_create_sensor(self, request):
        return Response(self.filterset_fields)
    
    

class SensorChange(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']

    def patch_change_sensor(self, request):
        if (self.filterset_fields == ['name'] or self.filterset_fields == ['description']) or self.filterset_fields == ['name', 'description']:
            return Response(self.filterset_fields)
        
    
    
    
class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer( many=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']

    def get_list_sensors(self, request):
        return Response(self.filterset_fields)
    


class SensorSpecific(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    
    def get_specific_sensors(self, request):
        id = self.id
        name = self.name
        description = self.description
        measurements =  self.measurements
        return Response({'id': id}, {'name': name}, {'description': description}, {'measurements': measurements})
    
    def post_add_measurement(self, request):
        id = self.id
        temperature = self.temperature
        return Response({'id': id}, {'temperature': temperature})

