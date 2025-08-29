from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DavomatViewSet, OquvchilarViewSet

router = DefaultRouter()
router.register(r'davomat', DavomatViewSet, basename='davomat')
router.register(r'oquvchilar', OquvchilarViewSet, basename='oquvchilar')

urlpatterns = [
    path('', include(router.urls))
]