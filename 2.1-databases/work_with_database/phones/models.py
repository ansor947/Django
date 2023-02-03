
from django.db import models

 


class Phone(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    
