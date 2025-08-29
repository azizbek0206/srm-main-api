# davomat/views.py
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Davomat, Oquvchilar
from .serializers import DavomatSerializer, OquvchilarSerializer



class OquvchilarViewSet(viewsets.ModelViewSet):
    queryset = Oquvchilar.objects.all()
    serializer_class = OquvchilarSerializer


class DavomatViewSet(viewsets.ModelViewSet):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sana']