from setuptools import setup, find_packages
from django_shortener import __version__ as version

setup(
    name='django_shortener',
    version=version,
    description='URL Shortener System',
    author='Olivier Demah',
    author_email='olivier@foxmask.info',
    url='https://github.com/foxmask/django_shortener',
    download_url='https://github.com/foxmask/django_shortener/archive/django-shortener-'+version+'.tar.gz',  
    packages=find_packages(),
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
    ],
    include_package_data=True,
)
