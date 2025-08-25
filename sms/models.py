from django.db import models

class SMSShablon(models.Model):
    kod = models.CharField(max_length=50, unique=True)
    matn = models.TextField()

    def __str__(self):
        return self.kod

class Qarzdor(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    qarz_miqdori = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ism



    
