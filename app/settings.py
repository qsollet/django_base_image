import os
import random
import string
import importlib
import glob

# Find the application settings and import it
webapp = glob.glob('*/settings.py')
webapp.remove('app/settings.py')
webapp = os.path.dirname(webapp[0])
globals().update(importlib.import_module('{}.settings'.format(webapp)).__dict__)

# Then override some of the settings

# For some reason if we generate the key randomly at this point the session ends up corrupted often
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    ''.join([random.SystemRandom().choice(string.digits + string.ascii_letters) for _ in range(50)]),
)

STATIC_ROOT = os.environ.get(
    'DJANGO_STATIC_ROOT',
    '/static/',
)

MEDIA_ROOT = os.environ.get(
    'DJANGO_MEDIA_ROOT',
    '/media/',
)

DEBUG = 'True' == os.environ.get(
    'DJANGO_DEBUG',
    'False',
)

APP_NAME = os.environ.get(
    'DJANGO_APP_NAME',
    'app',
)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DJANGO_DB_ENGINE',
            'django.db.backends.postgresql',
        ),
        'NAME': os.environ.get(
            'DJANGO_DB_NAME',
            APP_NAME,
        ),
        'USER': os.environ.get(
            'DJANGO_DB_USER',
            APP_NAME,
        ),
        'PASSWORD': os.environ.get(
            'DJANGO_DB_PASSWORD',
            'password',
        ),
        'HOST': os.environ.get(
            'DJANGO_DB_HOST',
            'database',
        ),
        'PORT': os.environ.get(
            'DJANGO_DB_PORT',
            '5432',
        ),
    }
}

# TODO add ALLOWED_HOSTS ?
# ALLOWED_HOSTS = ['*']
