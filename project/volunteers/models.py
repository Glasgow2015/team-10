from django.db import models
from django.conf import settings


class Volunteer(models.Model):
    email = models.EmailField(null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50)
    subscribed_to_newsletter = models.BooleanField(default=True)
    phone_number = models.CharField(default=None, max_length=50)