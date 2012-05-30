from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views', 
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive', name='blog.archive.day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive', name='blog.archive.month'),
    url(r'^(?P<year>\d{4})/$', 'archive', name='blog.archive.year'),

    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)$', 'view', name='blog.post'),

    url(r'^$', 'index', name='blog.index'), 
)
