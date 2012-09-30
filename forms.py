# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput
from django.forms.util import ErrorList
from django.utils.translation import ugettext as _

from django_shortener.models import Shrt

import hashlib

class ShrtForm(ModelForm):
    
    class Meta:
        model = Shrt
        fields = ('urlfull',)
        widgets = {               
                   'urlfull': TextInput(attrs={'placeholder':_('add a shorten url'),'size':80})
        }
        
    """         
        1) we calculate the MD5 of the urlfull field
        2) we check if that md5 is already in the database
        3) if yes ; we stop
        4) if no ; return the value 
    """
    def clean_urlfull(self):
        urlfull = self.cleaned_data['urlfull']
        #1) 
        urlmd5 = hashlib.md5(urlfull)       
        #2) check the uniqueness  of the url by its md5
        if Shrt.objects.filter(urlmd5__iexact=urlmd5.hexdigest()).count() > 0:
            #3) stop
           raise forms.ValidationError(_("This URL already exists, please change it."))
        #4) continue ; return the value
        return urlfull
