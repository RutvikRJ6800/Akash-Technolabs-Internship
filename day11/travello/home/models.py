from django.db import models
from django.db.models.base import Model
from django.db import models
# Create your models here.
class Destination(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='None/', height_field=None, width_field=None, max_length=None)
    offer = models.BooleanField()
