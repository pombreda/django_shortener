# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.util import ErrorList

from django_shortener.models import Shrt

import hashlib

class ShrtForm(ModelForm):
    
    class Meta:
        model = Shrt
        fields = ('urlfull',)
        
    def clean_urlfull(self):
        urlfull = self.cleaned_data['urlfull']
        urlmd5 = hashlib.md5(urlfull)       
        #check the uniqueness  of the url by its md5
        if Shrt.objects.filter(urlmd5__iexact=urlmd5.hexdigest()).count() > 0:
           raise forms.ValidationError("This URL already exists, please change it.")
        
        return urlfull
