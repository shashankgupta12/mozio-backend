# /provider_api/test.py

from django.test import TestCase
from .models import Provider
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):

    """This class defines the test suite for the provider model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.provider_name = 'name'
        self.provider_email = 'email@email.com'
        self.provider_phone_number = 88888888
        self.provider_language = 'language'
        self.provider_currency = 'currency'
        self.provider = Provider(name=self.provider_name,
                                 email=self.provider_email,
                                 phone_number=self.provider_phone_number,
                                 language=self.provider_language,
                                 currency=self.provider_currency)

    def test_model_can_create_a_provider(self):
        """Test the Provider model can create a provider."""

        old_count = Provider.objects.count()
        self.provider.save()
        new_count = Provider.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    """This class defines the test suite for the provider API views."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.client = APIClient()
        self.provider_data = {
            'name': 'name',
            'email': 'email@email.com',
            'phone_number': 88888888,
            'language': 'language',
            'currency': 'currency',
            }
        self.response = self.client.post(reverse('create'),
                self.provider_data, format='json')

    def test_api_can_post_a_provider(self):
        """Test the API can create/POST a provider."""

        self.assertEqual(self.response.status_code,
                         status.HTTP_201_CREATED)

    def test_api_can_get_a_provider(self):
        """Test the API can GET a provider"""

        provider = Provider.objects.get()
        response = self.client.get(reverse('details',
                                   kwargs={'pk': provider.id}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, provider)

    def test_api_can_upadate_a_provider(self):
        """Test the API can update/PUT a given provider."""

        provider = Provider.objects.get()
        change_provider = {
            'name': 'new name',
            'email': 'new_email@email.com',
            'phone_number': 99999999,
            'language': 'new language',
            'currency': 'new currency',
            }
        response = self.client.put(reverse('details',
                                   kwargs={'pk': provider.id}),
                                   change_provider, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_provider(self):
        """Test the API can DELETE a given provider."""

        provider = Provider.objects.get()
        response = self.client.delete(reverse('details',
                kwargs={'pk': provider.id}), format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
