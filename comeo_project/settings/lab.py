from .common import *

print("Lab settings loaded")

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['.comeo.org.md']

STATIC_URL = '/static/'
MEDIA_ROOT = '/home/comeo_lab_env/comeo_project/media'

# Custom email backend which support ssl connection supported by zoho
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'contact@comeo.org.md'
EMAIL_HOST_PASSWORD = ENV_EMAIL_HOST_PASSWORD

CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"