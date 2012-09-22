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
"""
def new_shrt(request):
    if request.method == 'POST':
        form = ShrtForm(request.POST)
        if form.is_valid():
            #get the size of the random shortener string
            length = settings.SHRT
            #let's generate the shortener string
            shrt = urlshortener()
            shortener = shrt.run(length["url_size"])
            #create the "md5sum" of the shortener
            urlmd5 = hashlib.md5(shortener)

            if request.user.is_authenticated():
                user = request.user
            else:
                user = User()
                user.id = 0
            new_shortener = form.save(commit=False)
            new_shortener.urlshort = shortener
            new_shortener.urlmd5 = urlmd5.hexdigest()
            new_shortener.user = user
            new_shortener.save()
        
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
        #do a md5 on a shortener
        urlmd5 = hashlib.md5(shrt)            
        #then let's search the url from its "MD5 sum"
        urlfull = Shrt.objects.filter(urlmd5__exact=urlmd5.hexdigest())
        context = {'shrt': urlfull, 'action':'show_shrt'}
        return render_to_response('django_shortener/home.html', context)
                
    except Shrt.DoesNotExist:
        raise Http404
    
