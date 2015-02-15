"""
Wedding Site URLs
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns( #pylint: disable=invalid-name
    '',
    url(r'', include('static_info.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
