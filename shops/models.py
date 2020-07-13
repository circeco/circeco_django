from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(null=True)
    webURL = models.CharField(max_length=50, null=True)
    serviceType = models.CharField(max_length=25, null=True) 

    def __str__(self): 
        return self.name


