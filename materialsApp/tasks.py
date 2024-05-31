from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from materialsApp.models import Course
from materialsApp.services import all_send_mail
from usersApp.models import User


@shared_task()
def send_update(course_id, update_files):
    email_list = []
    course = Course.objects.get(id=course_id)
    print(course.sub_course.all())
    for sub in course.sub_course.all():
        email_list.append(sub.user.email)
    subject = 'Онлайн школа'
    massage = f'Обновленно: {update_files}, {email_list}'
    email = ['denis_belenko@mail.ru']
    all_send_mail(subject, massage, email,)


@shared_task()
def check_user():
    date_today = timezone.now().today().date()
    days = relativedelta(months=1)
    max_last_date = date_today - days
    users = User.objects.all()
    for user in users:
        print(user.email)
        print(user.last_login)
        print(max_last_date)
        if user.is_active is True and user.last_login < max_last_date:
            user.is_active = False
            user.save()
    print("Проверка завершена!")



