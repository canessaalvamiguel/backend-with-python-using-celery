from datetime import timedelta, datetime

from django.shortcuts import render
from app1.tasks import send_mail


def index(request):
    mail_sent = False
    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail.apply_async(
            args=[email],
            #countdown=10
            eta=datetime.now() + timedelta(seconds=10)
        )
        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
