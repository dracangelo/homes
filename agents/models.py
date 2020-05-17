from django.db import models

# Create your models here.

class Agents(models.Model):
    name = models.CharField(max_length= 70)
    title = models.CharField(max_length= 70)
    image = models.ImageField(upload_to='agents/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Agents'
        verbose_name_plural = 'Agents'