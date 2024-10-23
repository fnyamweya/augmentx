# app.py

from fastapi import FastAPI
from celery.result import AsyncResult
from api.endpoints import router
from celery import Celery
from celery_app import celery_app  # Import Celery app

app = FastAPI(
    title="AugmentX API",
    description="API for AugmentX: Data Augmentation Tool",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc" 
)

# Register API router
app.include_router(router)

# Background task route (example of using Celery)
@app.post("/augment_async/")
async def run_augmentation_task(data: dict):
    task = celery_app.send_task('tasks.long_running_augmentation', args=[data])
    return {"task_id": task.id, "status": "Task started"}


@app.get("/augment_async/status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    return {"task_id": task_id, "status": task_result.status, "result": str(task_result.result)}
