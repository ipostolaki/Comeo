import os

from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _

from .secret import *
import comeo_app


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # comeo_project folder
COMEO_APP_DIR_PATH = os.path.dirname(os.path.realpath(comeo_app.__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

SECRET_KEY = key

MEDIA_URL = '/uploaded/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comeo_app',
    'crispy_forms',
    'bootstrapform',
    'django_extensions',
    'django.contrib.humanize',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'comeo_project.urls'

WSGI_APPLICATION = 'comeo_project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'Europe/Kiev'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_URL = '/login/'

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + [
    'django.core.context_processors.request',
    'comeo_app.context_processors.environment_processor']


LOGIN_REDIRECT_URL = '/profile/'

AUTH_USER_MODEL = 'comeo_app.ComeoUser'


LANGUAGES = (
    ('ru', _('Russian')),
    ('ro', _('Romanian')),
    ('en', _('English')),
)

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (os.path.join(COMEO_APP_DIR_PATH, 'locale'),)

# Email
DEFAULT_FROM_EMAIL = 'contact@comeo.org.md'
SERVER_EMAIL = 'contact@comeo.org.md'

# Custom non django
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

ADMINS = (('Ilia', 'ilia.ravemd@gmail.com'),)