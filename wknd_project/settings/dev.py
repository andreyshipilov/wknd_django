"""
Development settings.
"""
from os.path import join
from common import *


DEBUG = True

COMPRESS_ENABLED = True

TEMPLATE_DEBUG = DEBUG

WSGI_APPLICATION = "wknd_project.wsgi.dev.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        #"NAME": join(BASE_DIR, "../default.db"),
        "NAME": "wknd",
        "USER": "dev",
        "PASSWORD": "dev"
    }
}

INSTALLED_APPS += (
    "django.contrib.webdesign",
    "debug_toolbar",
    "django_extensions",
    "django_reset",
)

MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)
