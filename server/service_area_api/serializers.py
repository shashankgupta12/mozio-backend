# /service_area_api/serializers.py

from rest_framework import serializers
from .models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:

        """Meta class to map serializer's fields with the model fields."""

        model = ServiceArea
        fields = ('id', 'pid', 'name', 'price', 'polygon')
