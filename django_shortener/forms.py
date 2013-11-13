# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput
from django.forms.util import ErrorList
from django.utils.translation import ugettext as _
from django.conf import settings
from django_shortener.models import Shrt
from django.utils.html import mark_safe
import hashlib


class ShrtForm(ModelForm):

    class Meta:
        model = Shrt
        fields = ('urlfull',)
        widgets = {
            'urlfull': TextInput(attrs={'placeholder': _('enter an url'), 'size': 80})
        }

    """
        1) we calculate the MD5 of the urlfull field
        2) we check if that md5 is already in the database
        3) if yes ; we stop
        4) if no ; return the value 
    """

    def clean_urlfull(self):
        urlfull = self.cleaned_data['urlfull']
        # 1)
        urlmd5 = hashlib.md5(urlfull)
        # 2) check the uniqueness  of the url by its md5
        url_data = Shrt.objects.filter(urlmd5__iexact=urlmd5.hexdigest())
        if url_data.count() > 0:
            msg = _("This URL already exists. Here is its short form <a href='{short_domain}/{urlshrt}'>{urlshrt}</a>").format(
                urlshrt=url_data[0].urlshort, short_domain=settings.SHRT['short_domain'])
            # 3) stop
            raise forms.ValidationError(mark_safe(msg))
        # 4) continue ; return the value
        return urlfull
