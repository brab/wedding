# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_guest_attending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=64)),
                ('guests', models.ManyToManyField(to='rsvp.Guest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
