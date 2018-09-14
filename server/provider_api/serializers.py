# /provider_api/serializers.py

from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):

    """Serializer to map the Model instance into JSON format."""

    class Meta:

        """Meta class to map serializer's fields with the model fields."""

        model = Provider
        fields = (
            'id',
            'name',
            'email',
            'phone_number',
            'language',
            'currency',
            )
