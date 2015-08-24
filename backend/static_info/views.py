"""
Static Info Views
"""
from django.shortcuts import render

from rsvp.models import Event

def fri_dinner(request):
    """
    Friday Dinner details
    """
    try:
        event = Event.objects.filter(uri__icontains='friday-dinner')[0]
    except (Event.DoesNotExist, Event.MultipleObjectsReturned):
        event = None
    return render(
        request,
        'static_info/fri_dinner.html',
        {
            'event': event,
        },
    )

def sun_lunch(request):
    """
    Sunday Lunch details
    """
    try:
        event = Event.objects.filter(uri__icontains='sunday-lunch')[0]
    except (Event.DoesNotExist, Event.MultipleObjectsReturned):
        event = None
    return render(
        request,
        'static_info/sun_lunch.html',
        {
            'event': event,
        },
    )

def index(request):
    """
    Static Info index view
    """
    return render(
        request,
        'static_info/index.html',
        {},
    )

def itinerary(request):
    """
    The schedule of the wedding day
    """
    return render(
        request,
        'static_info/itinerary.html',
        {},
    )

def people(request):
    """
    Our wedding party
    """
    return render(
        request,
        'static_info/people.html',
        {},
    )

def rsvp(request):
    """
    RSVP
    """
    return render(
        request,
        'static_info/rsvp.html',
        {},
    )

def travel(request):
    """
    Travelling to Vancouver
    """
    return render(
        request,
        'static_info/travel.html',
        {},
    )
