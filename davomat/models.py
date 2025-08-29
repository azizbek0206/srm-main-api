# davomat/models.py
from django.db import models

class Oquvchilar(models.Model):
    ism = models.TextField()
    familiya = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20, blank=True)
    kurs = models.ForeignKey('kurslar.Kurslar', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.ism} {self.familiya}"


class Davomat(models.Model):
    oquvchi = models.CharField(max_length=255)
    # oquvchi = models.ForeignKey('Oquvchilar', on_delete=models.SET_NULL, null=True, blank=True)  # blank=True qo‘shdim
    sana = models.DateField()
    attended = models.BooleanField(default=False)
    guruh = models.CharField(max_length=255, blank=True)
    uqituvchi = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.oquvchi} - {self.sana}" if self.oquvchi else f"O‘quvchi yo‘q - {self.sana}"
