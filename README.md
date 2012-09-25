django-shortener
================

Create short URL from a long one

The model is this one :


    from django.db import models

    from django.contrib.auth.models import User
 
    class Shrt(models.Model):
	    urlfull = models.URLField(unique=True)
	    urlmd5 = models.CharField(max_length=40,unique=True)
	    urlshort = models.CharField(max_length=80)
	    user = models.ForeignKey(User)



How it's working :
=================

The full URL are stored "as is" with an associated short URL automatically generated and a MD5 is done on this one and stored too

When a short url is displayed, to get the full 'version', we do a MD5 of this one and retreive the full one.    

to set the size, add this to your settings.py

	
	SHRT = {
    	'url_size':20, 					#set the size of the length of the short url to be build
    	'url_domain':'http://foo.bar/ 	#set the domain that will provide the URL shortener
    } 
    
in TEMPLATE_CONTEXT_PROCESSORS add 

    'django_shortener.context_processors.short_domain',
        
thus you could use the foo.bar domain as the short domain that will handle the short url 
and so in your template use : 

    <a href="{{ short_domain.url_domain }}{{ shrt.urlshrt }}">{{ shrt.urlfull }}</a>  

you can have a look at the home.html template for a closer look at how it works