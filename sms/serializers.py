from rest_framework import serializers
from .models import SMSShablon, Qarzdor
class SMSShablonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSShablon
        fields = '__all__'

class QarzdorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qarzdor
        fields = '__all__'



