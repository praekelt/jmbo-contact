from django.conf.urls import patterns, include


urlpatterns = patterns(
    '',
    (r'^jmbo/', include('jmbo.urls')),
    (r'^contact/', include('contact.urls')),
)
