from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def send_login_mail(email, token):
    login_link = "http://localhost:8000/securemsg/login/%s" % token
    html_body = """
        <a href="%s">%s</a>
    """ % (login_link, login_link)

    mail = EmailMultiAlternatives(
      subject="Your one-off login link to pgpost",
      body=login_link,
      from_email="PGPost <aleksi.knuutila@iki.fi>",
      to=[email],
      headers={"Reply-To": "noreply@datam.me"}
    )
    mail.attach_alternative(html_body, "text/html")

    mail.send()
