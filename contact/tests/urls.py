from django.conf.urls.defaults import patterns, include


urlpatterns = patterns(
    '',
    (r'^jmbo/', include('jmbo.urls')),
    (r'^contact/', include('contact.urls')),
)
