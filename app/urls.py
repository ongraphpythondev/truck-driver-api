from rest_framework import routers
from django.urls import path, include
from .views import TruckAPIView, DriverAPIView

# Initialize the default router
router = routers.DefaultRouter()
router.register(r'trucks', TruckAPIView)
router.register(r'drivers', DriverAPIView)

# URL patterns for the API endpoints
urlpatterns = [
    path('', include(router.urls)),
]
