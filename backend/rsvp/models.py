"""
RSVP Models
"""
from django.db import models


class Guest(models.Model):
    """
    A Guest object
    """
    attending = models.BooleanField(default=True)
    invite = models.ForeignKey('Invite')
    name = models.CharField(max_length=128)


class Invite(models.Model):
    """
    An invitation object
    """
    code = models.CharField(max_length=16, unique=True, )
    #events_attending = models.
    description = models.CharField(max_length=64)
    notes = models.TextField()
    updated = models.DateTimeField(auto_now=True)
