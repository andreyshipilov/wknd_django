"""
Production settings

"""
from common import *


WSGI_APPLICATION = 'wsgi.prod.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': ,
    }
}

ALLOWED_HOSTS = []

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': ,
    }
}

COMPRESS_CSS_FILTERS += [
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS += [
    'compressor.filters.jsmin.JSMinFilter',
]
