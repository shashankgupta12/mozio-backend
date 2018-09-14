# /provider_api/models.py

from django.db import models


class Provider(models.Model):

    """This class represents the provider model."""

    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    phone_number = models.BigIntegerField(blank=False)
    language = models.CharField(max_length=255, blank=False)
    currency = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""

        return 'Name: {}, Email: {}, Phone Number: {}, Language: {}, Currency: {}'.format(self.name,
                self.email, self.phone_number, self.language,
                self.currency)
