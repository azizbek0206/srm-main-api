from rest_framework import serializers
from .models import  Guruhlar

class GuruhlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruhlar
        fields = '__all__'