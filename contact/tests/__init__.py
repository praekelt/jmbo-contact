from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse


class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

    def test_form_render(self):
        response = self.client.get(reverse("site_contact"))
        self.assertEqual(response.status_code, 200)
        self.failUnless(
            """<iframe \
src="http://www.google.com/recaptcha/api/noscript?k=xxx&hl=en" \
height="300" width="500" frameborder="0"></iframe>""" in response.content
        )
