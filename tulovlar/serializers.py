# serializers.py
from rest_framework import serializers
from .models import Tulovlar

class TulovlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tulovlar
        fields = '__all__'