from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SMSShablonViewSet, QarzdorViewSet, send_sms

router = DefaultRouter()
router.register(r'uquvchilar', SMSShablonViewSet, basename='shablon')
router.register(r'qarzdorlar', QarzdorViewSet, basename='qarzdorlar')

urlpatterns = [
    path('', include(router.urls)),
    path('send-sms/', send_sms),
]
