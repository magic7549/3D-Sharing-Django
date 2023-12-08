from django.apps import AppConfig
from django.conf import settings


class ContestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contest'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import tasks
            tasks.start_scheduler()
