from django.db import models
from django.conf import settings


class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(required=True)
    last_name = models.CharField(required=True)
    date_of_birth = models.DateField(required=True)
    radius = models.IntegerField(default=None)
    post_code = models.CharField(required=True)
    subscribed_to_newsletter = models.BooleanField(default=True)
    phone_number = models.CharField(default=None)
