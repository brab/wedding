# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 17, 52, 33, 376384)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 3, 17, 52, 39, 281084)),
            preserve_default=False,
        ),
    ]
