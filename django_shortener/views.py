# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.conf import settings
from django import forms
from django.template import RequestContext

from django_shortener.urlshortener import urlshortener
from django_shortener.forms import ShrtForm
from django_shortener.models import Shrt

import hashlib

import logging

logger = logging.getLogger(__name__)


def home(request):
    """
        home page
    """

    shortener = Shrt.objects.all().order_by('-id')[:5]
    form = ShrtForm()
    context = {'form': form, 'shrt': shortener}
    context.update(csrf(request))
    return render_to_response('django_shortener/home.html', context, context_instance=RequestContext(request))


def new_shrt(request):
    """
        save a new full url in a short way
        1) we check the POST request
        2) we validate the form
        3) if validated: we store the datas
    """

    # 1)
    if request.method == 'POST':
        form = ShrtForm(request.POST)
        # 2)
        if form.is_valid():
            # user ?
            if request.user.is_authenticated():
                user = request.user
            else:
                user = User()
                user.id = 0

            # create a md5sum on the urlfull
            urlmd5 = hashlib.md5(form.cleaned_data['urlfull'])

            # get the size of the random shortener string
            length = settings.SHRT

            # let's generate the shortener string
            shrt = urlshortener()
            urlshort = shrt.run(length["url_size"])

            # start an instance of the form
            new_shortener = form.save(commit=False)
            # assign the shortener
            new_shortener.urlshort = urlshort
            # assign the urlmd5 calculated "before" the "try/except"
            new_shortener.urlmd5 = urlmd5.hexdigest()
            # assign the user object
            new_shortener.user = user
            # finally : SAVE !
            new_shortener.save()

            return redirect(home)

    # part done while the request.methode != POST or form is not valid
    context = {'form': form, 'shrt': Shrt.objects.all()}
    context.update(csrf(request))
    return render_to_response('django_shortener/home.html', context, context_instance=RequestContext(request))


def show_shrt(request, shrt):
    """
        go to the full url from a short one
    """

    try:
        # then let's search the url from its "MD5 sum"
        #shrt is uniq
        urlfull = Shrt.objects.filter(urlshort__exact=shrt)
        for s in urlfull:
            return redirect(s.urlfull)

    except Shrt.DoesNotExist:
        raise Http404
