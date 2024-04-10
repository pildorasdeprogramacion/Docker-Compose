from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update({
    'broker_url': 'amqp://guest:guest@localhost:5672//',
    'result_backend': 'rpc://',
    'broker_connection_retry_on_startup': True,

})

app.autodiscover_tasks()
