import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from materialsApp.models import Course, Lesson
from usersApp.models import Payments, User

load_dotenv()
PASS_SUPERUSER = os.environ.get('PASS_SUPERUSER')


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Course.objects.all().delete()
        Payments.objects.all().delete()
        Lesson.objects.all().delete()

        user_add = [
            {'first_name': 'Vadim', 'last_name': 'Valov', 'email': 'vadim@mail.ru', 'is_active': True, },
            {'first_name': 'Valera', 'last_name': 'Pupkin', 'email': 'valera@mail.ru', 'is_active': True, },
            {'first_name': 'Milana', 'last_name': 'Gudcova', 'email': 'milana@mail.ru', 'is_active': True, },
        ]
        superuser = User.objects.create(
            first_name='Admin',
            email='admin@mail.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        superuser.set_password(PASS_SUPERUSER)
        superuser.save()

        for person in user_add:
            users = User.objects.create(**person)
            users.set_password('44444')
            users.save()

        add_course = [
            {'name': 'English', 'description': 'Курс по английскому языку'},
            {'name': 'Python', 'description': 'Курс по Python языку'},
            {'name': 'Kotlin', 'description': 'Курс по Kotlin языку'},
        ]
        course_list = [Course(**course_item) for course_item in add_course]
        Course.objects.bulk_create(course_list)

        vadim = User.objects.get(first_name='Vadim')
        valera = User.objects.get(first_name='Valera')
        milana = User.objects.get(first_name='Milana')

        english = Course.objects.get(name='English')
        python = Course.objects.get(name='Python')
        kotlin = Course.objects.get(name='Kotlin')

        add_lesson = [
            {'name': 'lesson 1', 'description': 'Первый урок', 'course': english},
            {'name': 'lesson 2', 'description': 'Первый урок', 'course': python},
            {'name': 'lesson 3', 'description': 'Первый урок', 'course': kotlin}
        ]

        lesson_list = [Lesson(**item_lesson) for item_lesson in add_lesson]
        Lesson.objects.bulk_create(lesson_list)
        lesson_1 = Lesson.objects.get(name='lesson 1')

        add_payment = [
            {'user': vadim, 'paid_course': english, 'sum_paid': 10000.32, 'method_paid': 'cash'},
            {'user': valera, 'paid_lesson': lesson_1, 'sum_paid': 30000, 'method_paid': 'transfer'},
            {'user': milana, 'paid_course': kotlin, 'sum_paid': 25750, 'method_paid': 'cash'}
        ]

        payment_list = [Payments(**payment) for payment in add_payment]
        Payments.objects.bulk_create(payment_list)
