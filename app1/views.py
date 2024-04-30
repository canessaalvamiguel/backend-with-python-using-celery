from datetime import timedelta, datetime

from django.shortcuts import render
from app1.tasks import send_mail, send_welcome_email, send_subscription_email, update_mails_sent
from celery import group, chain, chord


def index(request):
    mail_sent = False
    if request.method == 'POST':
        email = request.POST.get('email')
        # send_mail.apply_async(
        #     args=[email],
        #     #countdown=10
        #     eta=datetime.now() + timedelta(seconds=10)
        # )

        # tasks = group(
        #     send_mail.s(email),
        #     send_welcome_email.s(email),
        #     send_subscription_email.s(email)
        # )
        # tasks.apply_async(
        #     countdown=10
        # )

        # tasks = chain(
        #     send_mail.s(email),
        #     send_welcome_email.s(),
        #     send_subscription_email.s()
        # )
        # tasks.apply_async(
        #          countdown=10
        # )

        # Callback runs only if all task are executed successfully
        chord(
            [
                send_mail.s(email),
                send_welcome_email.s(email),
                send_subscription_email.s(email)
            ]
        )(
            update_mails_sent.s()
        )
        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
