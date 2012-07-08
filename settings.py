import os
import sys
from os.path import join


# This directory.
PROJECT_DIR = os.path.dirname(__file__)

# Paths to add on os.path
PATHS = (
    os.path.abspath(join(PROJECT_DIR, 'apps')),
    os.path.abspath(join(PROJECT_DIR, '../_APPS'))
)
[sys.path.insert(0, i) if i not in sys.path else None for i in PATHS]




DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "%s/wknd.sqlite" % PROJECT_DIR,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Australia/Adelaide'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = '%s/media/' % PROJECT_DIR
MEDIA_URL = '/media/'
STATIC_ROOT = '%s/static/' % PROJECT_DIR
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
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
    'userena.middleware.UserenaLocaleMiddleware',
)

ROOT_URLCONF = 'wknd_crew.urls'

TEMPLATE_DIRS = (
    '%s/templates' % PROJECT_DIR,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.admindocs',

    'south',
    #'social_auth',
    #'registration',
    #'profiles',
    'userena',
    'guardian',
    'easy_thumbnails',
    'debug_toolbar',

    'wknd',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
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
APPLICATION_PER_DAY_LIMIT = 2



"""
Third party apps settings go after that line

"""

# Django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

"""
# Django social auth
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID = '331958003555865'
FACEBOOK_API_SECRET = '5a1d9a765db277a6d65457de4cf3e786'

#LOGIN_URL = '/login/'
#LOGIN_REDIRECT_URL = '/logging-in/'
#LOGIN_ERROR_URL = '/login-error/'
#LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/'
"""

# Django userena
AUTH_PROFILE_MODULE = 'wknd.Profile'
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
USERENA_SIGNIN_REDIRECT_URL = '/id/%(username)s/'
LOGIN_URL = '/id/sign-in/'
LOGOUT_URL = '/id/sign-out/'

# Django gueardian
ANONYMOUS_USER_ID = -1
