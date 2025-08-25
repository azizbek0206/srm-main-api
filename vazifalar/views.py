from rest_framework import viewsets
from .models import Vazifalar
from .serializers import VazifalarSerializer

class VazifaViewSet(viewsets.ModelViewSet):
    queryset = Vazifalar.objects.all()
    serializer_class = VazifalarSerializer