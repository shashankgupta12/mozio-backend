# /service_area_api/views.py

from django.shortcuts import render
from rest_framework import generics
from .serializers import ServiceAreaSerializer
from .models import ServiceArea


class CreateView(generics.ListCreateAPIView):

    """This class handles the http POST request of our REST API."""

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new service area."""

        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    """This class handles the http GET (one), PUT, and DELETE requests of our REST API."""

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
