import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_file_celery.settings')

app = Celery('test_file_celery', broker_url='redis://redis:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
