from .common import *
from .secret import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'comeo_one',
        'USER': 'comeo_one_user',
        'PASSWORD': secret_psql_pass,
        'HOST': 'localhost',
        'PORT': '',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['.comeo.org.md']

STATIC_URL = '/static/'
MEDIA_ROOT = '/home/comeo_lab_env/comeo_project/media'

LOCALE_PATHS = ('/home/comeo_lab_env/comeo_project/comeo_app/locale/',)

# Custom email backend which support ssl connection supported by zoho
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'contact@comeo.org.md'
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"