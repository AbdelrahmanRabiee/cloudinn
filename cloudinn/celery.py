# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloudinn.settings')

app = Celery('cloudinn')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()