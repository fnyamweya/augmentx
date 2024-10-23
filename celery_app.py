from celery import Celery
import os

# Celery configuration
redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
celery_app = Celery(
    "augmentx",
    broker=redis_url,
    backend=redis_url
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],  
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
