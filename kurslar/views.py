from django.shortcuts import render
from .models import Kurslar
from .serializers import KurslarSerializer
from rest_framework import viewsets

class KurslarViewSet(viewsets.ModelViewSet):  # <-- ReadOnlyModelViewSet emas!
    queryset = Kurslar.objects.all()
    serializer_class = KurslarSerializer
