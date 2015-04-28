# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0011_guestgroup_responded'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='diet',
            field=models.CharField(default=b'normal', max_length=64, choices=[(b'normal', b'None'), (b'vegetarian', b'Vegetarian'), (b'vegan', b'Vegan')]),
            preserve_default=True,
        ),
    ]
