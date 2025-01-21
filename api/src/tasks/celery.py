from celery import Celery

from api.src.settings import settings

celery = Celery("tasks", broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", include=["api.src.tasks.tasks"])
