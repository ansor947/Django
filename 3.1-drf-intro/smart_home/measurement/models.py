from django.db import models

 

class Sensor:

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.headline

    


class Measurement:

    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline

 
