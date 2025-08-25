from rest_framework import serializers
from .models import Davomat

class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'