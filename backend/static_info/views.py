"""
Static Info Views
"""
from django.shortcuts import render


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
