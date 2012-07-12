import os.path

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from djmukmenus.menus.views import frontpage

static = os.path.join(os.path.dirname(__file__), 'static')
media = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'PDF'))


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'menus.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/', 'show_indexes': True }),
    )