from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #home page
    url(r'^$', 'django_shortener.views.home', name='home'),    
    #add an url
    url(r'^new_shrt$', 'django_shortener.views.new_shrt', name='new_shrt'),
    #go to the url
    url(r'^(?P<shrt>[a-zA-Z0-9]+)$', 'django_shortener.views.shrt_go', name='shrt_go'),    
)
