from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import os


def send_login_mail(email, token):
    context = {'token': token}
    msg_plain = render_to_string('../templates/email/login.txt', context)
    msg_html = render_to_string('../templates/email/login.html', context)

    mail = EmailMultiAlternatives(
      subject="GetYourData.org Secure Mail confirmation token",
      body=msg_plain,
      from_email="GetYourData.org <%s>" % os.environ['FROM_EMAIL'],
      to=[email],
      headers={"Reply-To": "noreply@datam.me"}
    )
    mail.attach_alternative(msg_html, "text/html")

    mail.send()

def send_data_received_mail(email, slug):
    link = '%s/securemsg/decrypt_index?slug=%s' % (settings.APP_BASE_URL, slug)
    context = {'link': link}
    msg_plain = render_to_string('../templates/email/data_received.txt', context)
    msg_html = render_to_string('../templates/email/data_received.html', context)

    mail = EmailMultiAlternatives(
      subject="GetYourData.org Secure Mail response",
      body=msg_plain,
      from_email="GetYourData.org <%s>" % os.environ['FROM_EMAIL'],
      to=[email],
      headers={"Reply-To": "noreply@datam.me"}
    )
    mail.attach_alternative(msg_html, "text/html")

    mail.send()
