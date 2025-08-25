from django.db import models

# Create your models here.
class Guruhlar(models.Model):
    nomi = models.CharField(max_length=255)
    kurs = models.TextField()
    uqituvchi = models.TextField()
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.nomi()