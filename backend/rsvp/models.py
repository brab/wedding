"""
RSVP Models
"""
from django.db import models


class Invite(models.Model):
    """
    An invitation object
    """
    _names = models.CharField()
    code = models.CharField()
    #events_attending = models.
    notes = models.TextField()
    num_guests = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)


    @property
    def names(self):
        """
        Names property
        """
        return self._names.split(',')

    @names.setter
    def names(self, names_list, ):
        """
        Names property setter
        """
        self._names = ','.join(names_list)
