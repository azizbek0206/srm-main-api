# views.py
from rest_framework import viewsets
from .models import Tulovlar
from .serializers import TulovlarSerializer

class TulovlarViewSet(viewsets.ModelViewSet):
    queryset = Tulovlar.objects.all()
    serializer_class = TulovlarSerializer