# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0010_auto_20150403_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestgroup',
            name='responded',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
