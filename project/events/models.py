from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(default=None, max_length=500)
    date = models.DateField()
    post_code = models.CharField(max_length=20)
    contact_number = models.CharField(default=None, max_length=20)
