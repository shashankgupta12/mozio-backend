# /service_area_api/tests.py

from django.test import TestCase
from .models import ServiceArea
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):

    """This class defines the test suite for the service area model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.service_area_provider_id = 1
        self.service_area_name = 'name'
        self.service_area_price = 500.00
        self.service_area_polygon = 'geojson'
        self.service_area = \
            ServiceArea(pid=self.service_area_provider_id,
                        name=self.service_area_name,
                        price=self.service_area_price,
                        polygon=self.service_area_polygon)

    def test_model_can_create_a_service_area(self):
        """Test the ServiceArea model can create a service area."""

        old_count = ServiceArea.objects.count()
        self.service_area.save()
        new_count = ServiceArea.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    """This class defines the test suite for the service area API views."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.client = APIClient()
        self.service_area_data = {
            'pid': 1,
            'name': 'name',
            'price': 500.00,
            'polygon': 'geojson',
            }
        self.response = self.client.post(reverse('create'),
                self.service_area_data, format='json')

    def test_api_can_post_a_service_area(self):
        """Test the API can create/POST a service area."""

        self.assertEqual(self.response.status_code,
                         status.HTTP_201_CREATED)

    def test_api_can_get_a_service_area(self):
        """Test the API can GET a service area"""

        service_area = ServiceArea.objects.get()
        response = self.client.get(reverse('details',
                                   kwargs={'pk': service_area.id}),
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, service_area)

    def test_api_can_upadate_a_service_area(self):
        """Test the API can update/PUT a given service_area."""

        service_area = ServiceArea.objects.get()
        change_service_area = {
            'pid': 1,
            'name': 'new name',
            'price': 1000.00,
            'polygon': 'new geojson',
            }
        response = self.client.put(reverse('details',
                                   kwargs={'pk': service_area.id}),
                                   change_service_area, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_service_area(self):
        """Test the API can DELETE a given service area."""

        service_area = ServiceArea.objects.get()
        response = self.client.delete(reverse('details',
                kwargs={'pk': service_area.id}), format='json',
                follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
