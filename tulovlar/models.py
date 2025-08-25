from django.db import models

# Create your models here.
class Tulovlar(models.Model):
    uquvchi = models.CharField(max_length=255)
    guruh = models.TextField()
    tulangan = models.TextField()
    sana  = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.uquvchi