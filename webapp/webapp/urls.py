from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^favicon.ico', redirect_to, {'url': settings.STATIC_URL + 'favicon.ico'}),

    url(r'^$', 'blog.views.index', name='home'),
    url(r'^b/', include('blog.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
