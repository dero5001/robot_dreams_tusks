from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot.settings')

app = Celery('robot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'my_schedule': {
        'task': 'user.tasks.users_count',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    }
}
