# serializers.py
from rest_framework import serializers
from .models import Davomat, Oquvchilar

class OquvchilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquvchilar
        fields = ['id', 'ism', 'familiya', 'telefon', 'kurs']


class DavomatSerializer(serializers.ModelSerializer):
    Davomat.objects.select_related("oquvchi").all()
    oquvchi_id = serializers.PrimaryKeyRelatedField(
        queryset=Oquvchilar.objects.all(), 
        source='oquvchi', 
        write_only=True,
        required=False  # majburiy emas, null bo‘lsa ham bo‘ladi
    )

    class Meta:
        model = Davomat
        fields = ['id', 'oquvchi', 'oquvchi_id', 'sana', 'attended', 'guruh', 'uqituvchi']
