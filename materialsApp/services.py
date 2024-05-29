from django.core.mail import send_mail

from app import settings


def all_send_mail(subject, massage, email):
    try:
        send_mail(
            subject=subject,
            message=massage,
            recipient_list=email,
            from_email=settings.ADDRESS_MAIL_RU,
        )
        return True
    except Exception:
        return False
