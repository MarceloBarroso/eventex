from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings
#!/usr/local/bin/python
# coding: utf-8


# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', homepage),
)


if settings.DEBUG:
    urlpatterns += patterns('',
	(r'^media/(?P<path>.*)$',
	'django.views.static.serve',
	{ 'document_root': settings.MEDIA_ROOT })
    )
