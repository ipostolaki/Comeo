import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comeo_project.settings')

rabbit_address = 'amqp://guest:guest@localhost:5672//'
app = Celery('comeo_app', backend=rabbit_address, broker=rabbit_address)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
