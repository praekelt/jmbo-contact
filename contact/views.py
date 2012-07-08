from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

from jmbo.generic.views import GenericForm
from foundry.decorators import layered

from contact.forms import SiteContactFormBasic, SiteContactFormWeb


class BaseSiteContact(GenericForm):

    def get_form_class(self, *args, **kwargs):
        return NotImplemented

    def get_template_name(self, *args, **kwargs):
        return 'contact/site_contact.html'

    def get_success_message(self, *args, **kwargs):
        """
        Returns user message to display after successful submission.
        """
        return _("Thanks for getting in touch. We'll get back to you as \
soon as possible.")

    def redirect(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')


class SiteContactBasic(BaseSiteContact):

    def get_form_class(self, *args, **kwargs):
        return SiteContactFormBasic


class SiteContactWeb(BaseSiteContact):

    def get_form_class(self, *args, **kwargs):
        return SiteContactFormWeb


@layered(default='web')
def site_contact(request):
    return

site_contact_basic = SiteContactBasic()
site_contact_web = SiteContactWeb()
