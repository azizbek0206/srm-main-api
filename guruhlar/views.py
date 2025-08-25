from django.shortcuts import render
from .models import Guruhlar
from .serializers import GuruhlarSerializer
from rest_framework import viewsets

class GuruhlarViewSet(viewsets.ModelViewSet):  # <-- ReadOnlyModelViewSet emas!
    queryset = Guruhlar.objects.all()
    serializer_class = GuruhlarSerializer
