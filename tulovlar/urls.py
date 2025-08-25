from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TulovlarViewSet

router = DefaultRouter()
router.register(r'tulovlar', TulovlarViewSet, basename='tulovlar')

urlpatterns = [
    path('', include(router.urls))
]