from .common import *

# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'comeo_one',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'comeo_one_user',
        'PASSWORD': 'secretpass',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
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