"""
RSVP app views
"""
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rsvp.models import GuestGroup

def detail(request, code):
    """
    RSVP detail view
    """
    guest_group = None
    try:
        guest_group = GuestGroup.objects.get(code__iexact=code)
    except GuestGroup.DoesNotExist:
        render(
            request,
            'rsvp/index.html',
            {'error': 'Please re-enter your Invite Word', },
        )
    if request.method == 'POST':
        print request.POST
        for ind, guest in enumerate(guest_group.guest_set.all()):
            guest.name = request.POST.get('guest_{0}_name'.format(ind))
            guest.save()
        guest_group.notes = request.POST.get('notes', '', ).strip()
        guest_group.save()
    return render(
        request,
        'rsvp/detail.html',
        {'guest_group': guest_group, },
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
                guest_group = GuestGroup.objects.get(code__iexact=invite_word)
            except GuestGroup.DoesNotExist:
                error = "Your Invite Word doesn't look quite right. " \
                    "Please try again"
            else:
                return HttpResponseRedirect(reverse(
                    'rsvp_detail',
                    args=(guest_group.code.lower(), )
                ))
        else:
            error = 'Please enter the Invite Word from your invitation'
    return render(
        request,
        'rsvp/index.html',
        {'error': error, },
    )
