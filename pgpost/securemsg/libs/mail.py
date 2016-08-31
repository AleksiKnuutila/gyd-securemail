from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_login_mail(email, token):

    context = {'token': token}
    msg_plain = render_to_string('../templates/email/login.txt', context)
    msg_html = render_to_string('../templates/email/login.html', context)

    mail = EmailMultiAlternatives(
      subject="GetYourData.org Secure Mail confirmation token",
      body=msg_plain,
      from_email="GetYourData.org <robot@getyourdata.org>",
      to=[email],
      headers={"Reply-To": "noreply@datam.me"}
    )
    mail.attach_alternative(msg_html, "text/html")

    mail.send()
