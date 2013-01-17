DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

# Django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}