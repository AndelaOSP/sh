"""
Production specific settings.
"""

from core.settings.base import *
import dj_database_url
import os

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
