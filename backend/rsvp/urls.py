"""
RSVP URLs
"""
from django.conf.urls import patterns, url

from rsvp import views


urlpatterns = patterns( #pylint: disable=invalid-name
    '',
    url(r'^$', views.index, name='rsvp', ),
    url(r'^detail$', views.index, name='rsvp_detail', ),
)
