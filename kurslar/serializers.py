from rest_framework import serializers
from .models import Kurslar

class KurslarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurslar
        fields = '__all__'