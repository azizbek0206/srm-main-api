from rest_framework import viewsets
from .models import Tulovlar
from .serializers import tulovlarSerializer

class TulovlarViewSet(viewsets.ModelViewSet):
    queryset = Tulovlar.objects.all()
    serializer_class = tulovlarSerializer