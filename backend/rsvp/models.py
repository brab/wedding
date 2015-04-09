"""
RSVP Models
"""
from django.db import models


class Event(models.Model):
    """
    An Event object
    """
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    description = models.CharField(max_length=256)
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class GuestGroup(models.Model):
    """
    An guest group object
    """
    code = models.CharField(max_length=16, unique=True, )
    updated = models.DateTimeField(auto_now=True)
    responded = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{0}'.format(self.code)


class Guest(models.Model):
    """
    A Guest object
    """
    name = models.CharField(max_length=128)
    group = models.ForeignKey(GuestGroup, blank=True, null=True, )
    events = models.ManyToManyField(Event, through='Attendance', )

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Attendance(models.Model):
    """
    An attendance object
    """
    event = models.ForeignKey(Event)
    guest = models.ForeignKey(Guest)
    attending = models.BooleanField(default=True)
