# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.context_processors import csrf
from django.shortcuts import render_to_response,redirect
from django.http import Http404
from django_shortener.models import Shrt
from django.contrib.auth.models import User
from django.conf import settings
from django_shortener.urlshortener import urlshortener

import hashlib

import logging

logger = logging.getLogger(__name__)

from django.forms import ModelForm

class ShrtForm(ModelForm):
    class Meta:
        model = Shrt
        fields = ('urlfull',)
"""
    home page
"""
def home(request):
    shortener = Shrt.objects.all()
    form = ShrtForm()
    context = {'form':form, 'shrt': shortener}
    context.update(csrf(request))
    return render_to_response('django_shortener/home.html', context)
"""
    save a new full url in a short way
    1) we check the POST request
    2) we validate the form
    3) we calculate the MD5 of the urlfull field
    4) we check if that md5 is already in the database
    5) if yes ; we stop
    6) if no ; we store the datas
"""
def new_shrt(request):
    if request.method == 'POST':
        form = ShrtForm(request.POST)
        if form.is_valid():
            #get the Model object
            shrt_url = Shrt()
            #create a md5sum on the urlfull
            urlmd5 = hashlib.md5(form.cleaned_data['urlfull'])
            shrt_url.urlmd5 = urlmd5.hexdigest()

            #get the size of the random shortener string
            length = settings.SHRT
            #let's generate the shortener string
            shrt = urlshortener()
            shortener = shrt.run(length["url_size"])

            from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
            try:
                #check if the urlfull is unique by verifying its md5
                shrt_url.validate_unique()
                
                #start an instance of the form
                new_shortener = form.save(commit=False)                
                
                #1) urlshortener
                #assign the shortener                 
                new_shortener.urlshort = shortener
                
                #2) md5 of the urlfull
                #assign the urlmd5 calculated "before" the "try/except"
                new_shortener.urlmd5 = urlmd5.hexdigest()
                
                #3) 
                #user ?
                if request.user.is_authenticated():
                    user = request.user
                else:
                    user = User()
                    user.id = 0
                #assign the user object
                new_shortener.user = user
                #finally : SAVE !
                new_shortener.save()
                
            #validation error
            except ValidationError as e:
                non_field_errors = e.message_dict['urlmd5']
        
        #create a new instance for the new form :)
        form = ShrtForm()        
        context = {'form':form, 'shrt': shortener}
        context.update(csrf(request))
        
    return redirect(home)
"""
    show the full url from a short one
"""
def show_shrt(request,shrt):       
    try:
        #then let's search the url from its "MD5 sum"
        urlfull = Shrt.objects.filter(urlshort__exact=shrt)
        context = {'shrt': urlfull, 'action':'show_shrt'}
        return render_to_response('django_shortener/home.html', context)
                
    except Shrt.DoesNotExist:
        raise Http404
