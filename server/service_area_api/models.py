# /service_area_api/models.py

from django.db import models


class ServiceArea(models.Model):

    """This class represents the service area model."""

    pid = models.PositiveSmallIntegerField(blank=False)
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=19, decimal_places=2, blank=False)
    polygon = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """Returns a human readable representation of the model instance."""

        return 'Pid: {}, Name: {}, Price: {}, Polygon: {}'.format(self.pid,
                self.name, self.price, self.polygon)
