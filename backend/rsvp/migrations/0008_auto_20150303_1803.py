# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_auto_20150303_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='guests',
        ),
        migrations.AddField(
            model_name='event',
            name='invites',
            field=models.ManyToManyField(to='rsvp.Invite'),
            preserve_default=True,
        ),
    ]
