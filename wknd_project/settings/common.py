# -*- coding: utf-8 -*-
import os
from sys import path

from django.conf.global_settings import (TEMPLATE_CONTEXT_PROCESSORS,
                                         STATICFILES_FINDERS)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '_c#^&2xzwd@xt@i2b5kftn+*-9$t&l+bg9&zb3@^jq)&^s38*d'

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

THIRD_PARTY_APPS = (
    'compressor',
    'south',
    'typogrify',
)

LOCAL_APPS = (
    'usrs',
    'wknd',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'wknd_project.urls'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Australia/Adelaide'
USE_I18N = False
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Django compressor
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
    'compressor.filters.css_default.CssAbsoluteFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

# Django extensions.
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
