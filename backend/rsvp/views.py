"""
RSVP app views
"""
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rsvp.models import Invite

def detail(request, code):
    """
    RSVP detail view
    """
    invite = None
    try:
        invite = Invite.objects.get(code=code)
    except Invite.DoesNotExist:
        render(
            request,
            'rsvp/index.html',
            {'error': 'Please re-enter your Invite Word', },
        )
    return render(
        request,
        'rsvp/detail.html',
        {'invite': invite, },
    )

def index(request):
    """
    RSVP index view
    """
    error = None
    if request.method == 'POST':
        invite_word = request.POST.get('invite_word')
        if invite_word:
            try:
                invite = Invite.objects.get(code__iexact=invite_word)
            except Invite.DoesNotExist:
                error = "Your Invite Word doesn't look quite right. " \
                    "Please try again"
            else:
                return HttpResponseRedirect(reverse(
                    'rsvp_detail',
                    args=(invite.code.lower(), )
                ))
        else:
            error = 'Please enter the Invite Word from your invitation'
    return render(
        request,
        'rsvp/index.html',
        {'error': error, },
    )
