from django.db import models

class Kurslar(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    text = models.TextField()
    text2 = models.TextField()
    text1 = models.TextField()

    def __str__(self):
        return self.name()
