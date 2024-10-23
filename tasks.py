from celery_app import celery_app

@celery_app.task
def long_running_augmentation(data):
    # Long-running augmentation logic here (e.g., image processing, text augmentation, etc.)
    # This is just an example. Replace it with real logic.
    augmented_data = f"Augmented data from {data}"
    return augmented_data
