from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_shortener.views.home', name='home'),
    url(r'^(?P<shrt>[a-zA-Z0-9]+)$', 'django_shortener.views.show_shrt', name='show_shrt'),
    url(r'^new_shrt$', 'django_shortener.views.new_shrt', name='new_shrt'),
    # url(r'^django_shortener/', include('django_shortener.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   # url(r'^admin/', include(admin.site.urls)),

)
