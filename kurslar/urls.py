from rest_framework.routers import DefaultRouter
from .views import KurslarViewSet
from django.urls import path, include



router = DefaultRouter()
router.register(r'kurslar', KurslarViewSet, basename='kurslar')

urlpatterns = [
    path('', include(router.urls))
]