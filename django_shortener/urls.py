from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #home page
    url(r'^$', 'django_shortener.views.home', name='home'),
    url(r'^(?P<shrt>[a-zA-Z0-9]+)$', 'django_shortener.views.show_shrt', name='show_shrt'),
    url(r'^new_shrt$', 'django_shortener.views.new_shrt', name='new_shrt'),
    #go to the url
)
