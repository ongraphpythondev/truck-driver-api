from rest_framework.viewsets import ModelViewSet
from .models import Truck, Driver
from .serializers import TruckSerializer, DriverSerializer


class TruckAPIView(ModelViewSet):
    """
    API viewset for Truck model.

    Provides CRUD operations for Truck instances.
    Filters out deleted trucks and orders by creation date.
    """
    queryset = Truck.objects.filter(is_deleted=False).order_by("-created_at")
    serializer_class = TruckSerializer


class DriverAPIView(ModelViewSet):
    """
    API viewset for Driver model.

    Provides CRUD operations for Driver instances.
    Filters out deleted drivers and orders by creation date.
    """
    queryset = Driver.objects.filter(is_deleted=False).order_by("-created_at")
    serializer_class = DriverSerializer
