from .common import *

# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

STATIC_URL = '/home/comeo_env/comeo_project/comeo_app/static/comeo_app/'
MEDIA_ROOT = '/Users/ipostolaki/envs/comeo_sync/comeo_project/media'

# LOCALE_PATHS = ('/Users/ipostolaki/envs/comeo_sync/comeo_project/comeo_app/locale/',)

# Custom email backend which support ssl connection supported by zoho
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'contact@comeo.org.md'
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD