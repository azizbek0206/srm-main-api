from django.shortcuts import render
from .models import Davomat
from .serializers import DavomatSerializer
from rest_framework import viewsets

class DavomatViewSet(viewsets.ModelViewSet):  # <-- ReadOnlyModelViewSet emas!
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializer
