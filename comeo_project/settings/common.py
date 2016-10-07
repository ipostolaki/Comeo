import os

from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _


PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))  # comeo_project folder

# TODO: Raise warning / exception in case if critical env vars were not retrieved
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ENV_RABBIT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
ENV_RABBIT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')
ENV_EMAIL_HOST_PASSWORD = os.environ.get('SECRET_EMAIL_HOST_PASSWORD')
OUTSIDE = os.environ.get('OUTSIDE')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'pg_database',
        'PORT': '5432',
    }
}

# Media files are served by Nginx, Docker has a mapped media volume, thus uploaded files are persisted
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/uploaded/'

PROJECT_APPS = (
    'apps.base',
    'apps.profiles',
    'apps.crowdfunding',
    'apps.registry',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'django.contrib.humanize',
    'ckeditor',
) + PROJECT_APPS


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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('ru', _('Russian')),
    ('ro', _('Romanian')),
    ('en', _('English')),
)

LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'comeo_project/locale'),)


LOGIN_URL = 'profiles:login'
LOGIN_REDIRECT_URL = 'profiles:profile'


TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + [
    'django.core.context_processors.request',
    'shared.context_processors.environment_processor']


AUTH_USER_MODEL = 'profiles.ComeoUser'


# Email
DEFAULT_FROM_EMAIL = 'contact@comeo.org.md'
SERVER_EMAIL = 'contact@comeo.org.md'

# Celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
BROKER_URL = 'amqp://{}:{}@rabbit:5672//'.format(ENV_RABBIT_USER, ENV_RABBIT_PASS)
CELERY_RESULT_BACKEND = BROKER_URL

# Misc
ADMINS = (('Ilia', 'ilia.ravemd@gmail.com'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s:%(lineno)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(module)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'INFO',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.join(PROJECT_ROOT, 'logs'), "django.log"),
            'maxBytes': 1024 * 1024 * 1,
            'backupCount': 100,
            'level': 'INFO',  # log file will not store debug level records
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'apps': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'py.warnings': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'mail.intended': {
            'handlers': ['mail_admins', 'file'],
            'level': 'INFO',
        },
    }
}
