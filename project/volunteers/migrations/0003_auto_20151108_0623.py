# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_remove_volunteer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='post_code',
            new_name='city',
        ),
    ]
