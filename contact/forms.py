from django import forms
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage, mail_managers
from django.utils.translation import ugettext as _

from captcha.fields import ReCaptchaField
from preferences import preferences
from jmbo.forms import as_div


class BaseSiteContactForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        max_length=150,
    )
    email_address = forms.EmailField(
        label=_('Email address'),
        max_length=150,
    )
    message = forms.CharField(
        label=_('Message'),
        max_length=10000,
        widget=forms.widgets.Textarea
    )

    def handle_valid(self, *args, **kwargs):
        """
        Send the email.
        """
        recipients = [recipient.email for recipient in \
                preferences.ContactPreferences.email_recipients.all()]
        if not recipients:
            mail_managers(
                'Error: No email address specified',
                'Users are trying to contact the site for which no \
email address could be found.',
                fail_silently=False
            )
            return None

        else:
            name = self.cleaned_data['name']
            email = self.cleaned_data['email_address']
            current_site = Site.objects.get_current()
            message = self.cleaned_data['message']
            subject = "Contact Message from %s" % current_site.name
            from_address = "%s <%s>" % (name, email)
            mail = EmailMessage(
                subject,
                message,
                from_address,
                recipients,
                headers={'From': from_address, 'Reply-To': from_address}
            )
            mail.send(fail_silently=False)

    as_div = as_div


class SiteContactFormBasic(BaseSiteContactForm):
    pass


class SiteContactFormWeb(BaseSiteContactForm):
    captcha = ReCaptchaField(
        label=_('Captcha'),
        error_messages={'required': _('Please enter the text.')}
    )
