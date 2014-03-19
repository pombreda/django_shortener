================
Django Shortener
================

Description :
=============

Django Shortener provides an URL shortener service


Requirements :
==============
* Python = 3.4.0
* Django >= 1.5
* django-simple-captcha = 0.4.2


Installation :
=============

settings : 
---------

.. code:: python

    INSTALLED_APPS = (
            'django_th',
    )


you can set the size of the URL and also the domain that will host the service:

.. code:: python
	
	SHRT = {
    	'url_size':20, 					#set the size of the length of the short url to be build
    	'url_domain':'http://foo.bar/' 	#set the domain that will provide the URL shortener
    } 
    
in TEMPLATE_CONTEXT_PROCESSORS add 

.. code:: python

    'django_shortener.context_processors.short_domain',

thus you could use the foo.bar domain as the short domain that will handle the short url 


To set a simple captcha, add the following to ask math question and "drop"
noises

.. code:: python

    CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
    CAPTCHA_NOISE_FUNCTIONS = ()


in the templates : 
------------------
in your templates to create a link : 

.. code:: python

    <a href="{{ short_domain.url_domain }}{{ shrt.urlshort }}">{{ shrt.urlfull }}</a>  

you can have a look at the home.html template for a closer look at how it works

if you need a template tag that parses a text and retreive links with short url use 
   
.. code:: python

    {{ text|shrt }}
   
or even 

.. code:: python

    {{ text|shrt|escape|safe }}
    
How it's working :
=================

The full URL are stored "as is" with an associated short URL automatically generated and a MD5 is done on this one and stored too

When a short url is displayed, to get the full 'version', we do a MD5 of this one and retreive the full one.    
