from django.db import models

class Kurslar(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=[('Aktiv', 'Aktiv'), ('Passiv', 'Passiv')], default='Aktiv')

    def __str__(self):
        return self.name