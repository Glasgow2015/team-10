# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_auto_20151108_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 11, 8, 6, 30, 1, 245321, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]
