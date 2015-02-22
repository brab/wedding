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
