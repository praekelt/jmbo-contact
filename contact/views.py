from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView
from django.contrib import messages

try:
    from foundry.decorators import layered
    HAS_FOUNDRY = True
except ImportError:
    HAS_FOUNDRY = False
from contact.forms import SiteContactFormBasic, SiteContactFormWeb


class BaseSiteContact(FormView):
    form_class = NotImplemented
    template_name = "contact/site_contact.html"
    success_url = "/"

    def form_valid(self, form):
        message.success(
            self.request, 
            _("Thanks for getting in touch. We'll get back to you as \
soon as possible.")
        )
        return super(BaseSiteContact, self).form_valid(form)


class SiteContactBasic(BaseSiteContact):
    form_class = SiteContactFormBasic


class SiteContactWeb(BaseSiteContact):
    form_class = SiteContactFormWeb


if HAS_FOUNDRY:
    @layered(default='web')
    def site_contact(request):
        return

    site_contact_basic = SiteContactBasic.as_view()
    site_contact_web = SiteContactWeb.as_view()

else:
    site_contact = SiteContactWeb.as_view()
