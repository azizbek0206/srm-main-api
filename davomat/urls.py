from rest_framework.routers import DefaultRouter
from .views import DavomatViewSet
from django.urls import path, include



router = DefaultRouter()
router.register(r'davomat', DavomatViewSet, basename='davomat')

urlpatterns = [
    path('', include(router.urls))
]