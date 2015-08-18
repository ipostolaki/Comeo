from .common import *
from .secret import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'comeo_one',
        'USER': 'comeo_one_user',
        'PASSWORD': secret_psql_pass,
        'HOST': 'localhost',
        'PORT': '', # Set to empty string for default.
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

STATIC_URL = '/home/comeo_lab_env/comeo_project/comeo_app/static/comeo_app/'
MEDIA_ROOT = '/Users/ipostolaki/envs/comeo_sync/comeo_project/media'

#LOCALE_PATHS = ('/Users/ipostolaki/envs/comeo_sync/comeo_project/comeo_app/locale/',)

# custom email backend which support ssl connection supported by zoho
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'contact@comeo.org.md'
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD