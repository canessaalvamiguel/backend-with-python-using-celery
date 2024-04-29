from django.shortcuts import render
from app1.tasks import async_send_email


def index(request):
    mail_sent = False
    if request.method == 'POST':
        email = request.POST.get('email')
        async_send_email(email)
        mail_sent = True

    return render(request, 'index.html', {
        'mail_sent': mail_sent
    })
