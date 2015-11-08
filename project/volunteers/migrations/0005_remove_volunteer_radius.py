# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0004_volunteer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='radius',
        ),
    ]
