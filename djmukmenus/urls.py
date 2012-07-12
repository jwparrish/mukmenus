from django.conf.urls.defaults import patterns, include, url
from menus.views import *
from django.conf import settings
import os.path

static = os.path.join(os.path.dirname(__file__), 'static')
media = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'PDF'))


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'menus.views.home', name='home'),
    # url(r'^djmukmenus/', include('djmukmenus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		#(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': static }),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': media }),
	)