import time
from datetime import datetime
from threading import Thread


def async_send_email(to):
    task = Thread(target=send_mail, args=(to,))
    task.start()


def send_mail(to):
    time.sleep(2)
    print(">>> Email sent to", to, "at", datetime.now())
