from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VazifaViewSet

router = DefaultRouter()
router.register(r'vazifa', VazifaViewSet, basename='vazifa')

urlpatterns = [
    path('', include(router.urls))
]