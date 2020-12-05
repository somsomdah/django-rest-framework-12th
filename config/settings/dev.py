import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "myDB",
        "USER": "root",
        "PASSWORD": "7436",
        "HOST": "localhost",
        "PORT": "3306"
    }
}