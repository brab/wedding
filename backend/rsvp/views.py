"""
RSVP app views
"""
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from rsvp.models import Attendance, Guest, GuestGroup

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
            {'error': 'Please re-enter your R.S.V.P. Word', },
        )
    if request.method == 'POST':
        guests = guest_group.guest_set.all()
        attendances = Attendance.objects.filter(
            guest__in=guests
        )
        for attendance in attendances:
            attendance.attending = True \
                if 'attendance_{0}'.format(attendance.id) in request.POST \
                else False
            attendance.save()
        for guest in guests:
            guest.diet = request.POST.get(
                'guest_{0}_diet'.format(guest.id),
                'normal',
            )
            print guest.diet
            guest.save()
        guest_group.responded = True
        guest_group.save()
        messages.success(
            request,
            "Thanks for responding! We're looking forward to seeing you soon!",
        )
        return redirect('index')
    diet_choices = Guest._meta.get_field_by_name('diet')[0].choices
    events = guest_group.guest_set.first().events.all()
    return render(
        request,
        'rsvp/detail.html',
        {
            'diet_choices': diet_choices,
            'events': events,
            'guest_group': guest_group,
        },
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
