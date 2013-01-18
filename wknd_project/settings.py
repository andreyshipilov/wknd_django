# -*- coding: utf-8 -*-
import re, sys
from os.path import join, abspath, dirname



# This directory.
PROJECT_DIR = dirname(__file__)

# Paths to add on os.path
PATHS = (
    abspath(join(PROJECT_DIR, 'apps')),
)
[sys.path.insert(0, i) if i not in sys.path else None for i in PATHS]


# Settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    #('Andrey', 'yeah@right.com'),
)
MANAGERS = ADMINS

TIME_ZONE = 'Australia/Adelaide'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False
MEDIA_ROOT = join(PROJECT_DIR, "media")
MEDIA_URL = '/media/'
STATIC_ROOT = join(PROJECT_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)
SECRET_KEY = '_c#^&2xzwd@xt@i2b5kftn+*-9$t&l+bg9&zb3@^jq)&^s38*d'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
ROOT_URLCONF = 'wknd_project.urls'
WSGI_APPLICATION = 'wknd_project.wsgi.application'
TEMPLATE_DIRS = (
    join(PROJECT_DIR, "templates"),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
) + TEMPLATE_CONTEXT_PROCESSORS

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',
    #'social_auth',
    'sorl.thumbnail',
    'debug_toolbar',
    'google_analytics',
    'compressor',

    'wknd',
    'usrs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# WKND defaults
AUTH_PROFILE_MODULE = 'usrs.Profile'
APPLICATION_PER_DAY_LIMIT = 2
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


"""
Third party apps settings go after that line.

"""



"""
# Django social auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
"""

# Compressor
COMPRESS_OUTPUT_DIR = 'min'
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter',]



# Local settings
try:
    from local_settings import *
except ImportError:
    pass

# Live settings
try:
    from live_settings import *
except ImportError:
    pass
