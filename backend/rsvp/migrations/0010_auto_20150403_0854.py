# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0009_auto_20150402_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=16)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='invite',
        ),
        migrations.RemoveField(
            model_name='event',
            name='guests',
        ),
        migrations.RemoveField(
            model_name='event',
            name='invites',
        ),
        migrations.DeleteModel(
            name='Invite',
        ),
        migrations.AddField(
            model_name='guest',
            name='events',
            field=models.ManyToManyField(to='rsvp.Event', through='rsvp.Attendance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='group',
            field=models.ForeignKey(blank=True, to='rsvp.GuestGroup', null=True),
            preserve_default=True,
        ),
    ]
