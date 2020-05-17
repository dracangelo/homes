from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=50)
    # location
    description = models.CharField(max_length=1000)
    
    icon = models.ImageField(upload_to='property/', null=True)