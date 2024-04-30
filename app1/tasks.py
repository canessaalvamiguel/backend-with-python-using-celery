import time
from datetime import datetime
from celery import shared_task


@shared_task
def send_mail(to):
    time.sleep(2)
    print(f">>> Email sent to {to} at {datetime.now()}")
