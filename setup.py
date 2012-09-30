from setuptools import setup
 
setup(
    name='django_shortener',
    version='0.1',
    description='URL Shortener System',
    author='Olivier Demah',
    author_email='olivier@foxmask.info',
    url='https://github.com/foxmask/django_shortener',
    download_url='https://github.com/downloads/foxmask/django_shortener/django-shortener-0.1.tar.gz',  
    packages=['django_shortener'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'        
    ]
)