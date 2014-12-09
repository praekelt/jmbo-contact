from django.conf.urls.defaults import patterns, url

from contact import views


urlpatterns = patterns(
    '',
    url(r'^$', 'contact.views.site_contact', name='site_contact'),
)
