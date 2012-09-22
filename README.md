django-shortener
================

Create short URL from a long one

The model is this one :


    from django.db import models

    from django.contrib.auth.models import User
 
    class Shrt(models.Model):
        urlfull = models.TextField()
        urlmd5 = models.CharField(max_length=40,unique=True)
        urlshort = models.CharField(max_length=80)
        user = models.ForeignKey(User)



How it's working :
=================

The full URL are stored "as is" with an associated short URL automatically generated and a MD5 is done on this one and stored too

When a short url is displayed, to get the full 'version', we do a MD5 of this one and retreive the full one.    