from rest_framework import serializers
from .models import Truck, Driver


class TruckSerializer(serializers.ModelSerializer):
    """
    Serializer for Truck model.
    
    Serializes all fields of the Truck model.
    """
    class Meta:
        model = Truck
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    """
    Serializer for Driver model.
    
    Serializes all fields of the Driver model.
    """
    class Meta:
        model = Driver
        fields = "__all__"
