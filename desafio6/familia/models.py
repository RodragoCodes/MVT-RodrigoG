from django.db import models
from datetime import datetime, date
# Create your models here.

class familiares(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    nacimiento= models.DateField()
    DNI= models.CharField(max_length=14)
