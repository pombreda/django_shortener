from django import template
from django.conf import settings
from django_shortener.models import Shrt
import re, hashlib

register = template.Library()

def shrt(input):       
    # urls = re.findall('https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return re.sub('https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', shrt_replace,input)

"""
    for each url found we :
    1) get the md5 of this url in the database
    2) return the corresponding urlshort 
"""
def shrt_replace(matchobj):
    links = ''
    urlmd5 = hashlib.md5(matchobj.group(0))
    print urlmd5.hexdigest()
    shrt_url = Shrt.objects.filter(urlmd5__exact=urlmd5.hexdigest())
    for url in shrt_url:
        links += '<a href="'+settings.SHRT['url_domain']+url.urlshort+'">'+url.urlfull+'</a>'
    return links
    
register.filter(shrt)