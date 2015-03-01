"""
RSVP app views
"""
from django.shortcuts import render

def index(request):
    """
    RSVP index view
    """
    return render(
        request,
        'rsvp/index.html',
        {},
    )
