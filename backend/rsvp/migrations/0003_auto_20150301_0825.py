# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20150301_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invite',
            name='num_guests',
        ),
        migrations.AddField(
            model_name='invite',
            name='description',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
