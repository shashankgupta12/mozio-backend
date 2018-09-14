# /provider_api/views.py

from django.shortcuts import render
from rest_framework import generics
from .serializers import ProviderSerializer
from .models import Provider


class CreateView(generics.ListCreateAPIView):

    """This class handles the http POST request of our REST API."""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new provider."""

        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    """This class handles the http GET (one), PUT, and DELETE requests of our REST API."""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
