from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.basesdjango.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prodDjango',
        'USER': 'demo_us',
        'PASSWORD': '{r{)br>AB%8*#gUg',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}