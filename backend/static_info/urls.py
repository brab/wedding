"""
Static Info URLs
"""
from django.conf.urls import patterns, url

from static_info import views


urlpatterns = patterns( #pylint: disable=invalid-name
    '',
    url(r'^$', views.index, name='index', ),
    url(r'^the-day$', views.itinerary, name='itinerary', ),
    url(r'^travel$', views.travel, name='travel', ),
)
