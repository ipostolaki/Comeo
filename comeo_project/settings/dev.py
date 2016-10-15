from .common import *


DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ["localhost"]

STATIC_URL = '/static/'

INSTALLED_APPS += ('debug_toolbar', 'django_extensions', 'apps.comeo_debug')

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'email-dummy/'

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"


# django debug toolbar configuration
def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    # needed to skip INTERNAL_IPS check, which depends on Docker machine ip
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

# ipython
# SHELL_PLUS_PRE_IMPORTS = (
#     ('module.submodule1', ('class1', 'function2')),
#     ('module.submodule2', 'function3'),
#     ('module.submodule3', '*'),
#     'module.submodule4'
# )
