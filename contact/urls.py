from django.conf.urls.defaults import patterns, url

from contact import views


urlpatterns = patterns(
    '',
    url(r'^$', views.site_contact, name='site_contact'),
)
