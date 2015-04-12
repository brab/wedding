# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0004_auto_20150301_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='attending',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
