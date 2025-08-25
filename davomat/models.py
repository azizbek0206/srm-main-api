from django.db import models

# Create your models here.

class Davomat(models.Model):
    guruh = models.TextField()
    sana = models.DateField(auto_now=True)
    uqituvchi = models.TextField()
    kelganlar = models.TextField()

    def __str__(self):
        return self.guruh