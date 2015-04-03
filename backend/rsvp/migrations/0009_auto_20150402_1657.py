# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0008_auto_20150303_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attending', models.BooleanField(default=True)),
                ('event', models.ForeignKey(to='rsvp.Event')),
                ('guest', models.ForeignKey(to='rsvp.Guest')),
                ('invite', models.ForeignKey(to='rsvp.Invite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='guest',
            name='attending',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='invite',
        ),
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(to='rsvp.Guest', through='rsvp.Attendance'),
            preserve_default=True,
        ),
    ]
