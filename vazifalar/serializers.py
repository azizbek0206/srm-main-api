from rest_framework import serializers
from .models import Vazifalar


class VazifalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vazifalar
        fields = '__all__'
