# /service_area_api/models.py

from django.db import models


class ServiceArea(models.Model):

    """This class represents the service area model."""

    pid = models.PositiveSmallIntegerField(blank=False)
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    geometry = models.CharField(max_length=255, blank=False)

    latitude_1 = models.IntegerField(blank=False)
    longitude_1 = models.IntegerField(blank=False)

    latitude_2 = models.IntegerField(blank=False)
    longitude_2 = models.IntegerField(blank=False)

    latitude_3 = models.IntegerField(blank=False)
    longitude_3 = models.IntegerField(blank=False)

    latitude_4 = models.IntegerField(blank=False)
    longitude_4 = models.IntegerField(blank=False)

    def __str__(self):
        """Returns a human readable representation of the model instance."""

        return 'Pid: {}, Name: {}, Price: {}, Geometry: {}, Latitudes: {}, {}, {}, {}, Longitudes: {}, {}, {}, {}'.format(
            self.pid,
            self.name,
            self.price,
            self.geometry,
            self.latitude_1,
            self.latitude_2,
            self.latitude_3,
            self.latitude_4,
            self.longitude_1,
            self.longitude_2,
            self.longitude_3,
            self.longitude_4,
            )
