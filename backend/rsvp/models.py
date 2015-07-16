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
    uri = models.CharField(max_length=128, null=True, blank=True, )

    class Meta(type):
        """
        Meta info
        """
        ordering = ['datetime_start', ]

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
    diet = models.CharField(
        max_length=64,
        choices=(
            ('normal', '--', ),
            ('vegetarian', 'Vegetarian', ),
            ('vegan', 'Vegan', ),
        ),
        default='normal',
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    @property
    def responded(self):
        """
        Return whether this guest has responded
        """
        try:
            return self.group.responded or False
        except AttributeError:
            return False

    @property
    def attendance_list(self):
        """
        Return a pretty string representation of the attendances
        """
        if self.responded:
            return str(self.attendance_set.all())
        else:
            return 'Not yet responded'



class Attendance(models.Model):
    """
    An attendance object
    """
    event = models.ForeignKey(Event)
    guest = models.ForeignKey(Guest)
    attending = models.BooleanField(default=True)

    class Meta(type):
        """
        Meta info
        """
        ordering = ['event', ]

    def __unicode__(self):
        return '{0} {1} attending {2}'.format(
            self.guest,
            'is' if self.attending else 'WILL NOT BE',
            self.event,
        )
