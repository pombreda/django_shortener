from django.conf import settings

def short_domain(request):
    '''
    A context processor to add the "short domain" from the settings, to the current Context
    '''
    return {'short_domain': settings.SHRT }
