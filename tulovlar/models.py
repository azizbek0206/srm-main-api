from django.db import models

class Tulovlar(models.Model):
    uquvchi = models.CharField(max_length=255)
    miqdor = models.IntegerField()  # tulangan o‘rniga miqdor
    sana = models.DateField()  # auto_now=True olib tashlandi
    holat = models.CharField(max_length=20, choices=[('To‘langan', 'To‘langan'), ('Kutilmoqda', 'Kutilmoqda')], default='To‘langan')

    def __str__(self):
        return self.uquvchi