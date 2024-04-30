import time
from datetime import datetime
from celery import shared_task


@shared_task
def send_mail(to):
    time.sleep(2)
    print(f">>> Email sent to {to} at {datetime.now()}")
    return True


@shared_task
def send_welcome_email(to):
    print(f">>> Welcome email sent to {to} at {datetime.now()}")
    return True


@shared_task
def send_subscription_email(to):
    print(f">>> Subscription email sent to {to} at {datetime.now()}")
    return True

@shared_task
def update_mails_sent(*args):
    print(f">>> All emails were sent")
