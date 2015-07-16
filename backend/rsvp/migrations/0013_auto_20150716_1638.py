# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0012_guest_diet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['event']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['datetime_start']},
        ),
        migrations.AddField(
            model_name='event',
            name='uri',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='diet',
            field=models.CharField(default=b'normal', max_length=64, choices=[(b'normal', b'--'), (b'vegetarian', b'Vegetarian'), (b'vegan', b'Vegan')]),
        ),
    ]
